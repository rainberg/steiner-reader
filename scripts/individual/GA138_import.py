#!/usr/bin/env python3
"""Standalone import script for GA138 — GA138 - Von der Initiation. Von Ewigkeit und Augenblick. Von Geisteslicht und Lebensdunkel"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA138 - Von der Initiation. Von Ewigkeit und Augenblick. Von Geisteslicht und Lebensdunkel"""
GA_NUMBER = "GA138"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "ERSTER VORTRAG München, 25. August 1912",
    "paragraphs": [
      "Von der Initiation",
      "Von Ewigkeit und Augenblick",
      "Von Geisteslicht und",
      "Lebensdunkel",
      "Ein Zyklus von sieben Vorträgen",
      "und ein Sondervortrag",
      "gehalten in München",
      "vom 25. bis 31. August 1912",
      "RUDOLF STEINER VERLAG",
      "DORNACH/SCHWEIZ",
      "Nach einer vom Vortragenden nicht durchgesehenen Nachschrift",
      "herausgegeben von der Rudolf Steiner-Nachlaßverwaltung",
      "Die Herausgabe besorgte Edwin Froböse",
      "vom 30. August 1912",
      "Gesamtausgabe Dornach 1959",
      "Bibliographie-Nr. 138",
      "Das Siegel auf dem Einband",
      "hat Rudolf Steiner 1912 für die Buchausgabe des dritten Mysteriendramas",
      "«Der Hüter der Schwelle» entworfen",
      "#c 1959 by Rudolf Steiner-Nachlaßverwaltung, Dornach/Schweiz",
      "Satz: Kooperative Dürnau, Dürnau",
      "Printed in Germany by Greiserdruck, Rastatt",
      "Am Beginne unseres Münchner Vortragszyklus sei es mir auch dies­mal wie in den letzten Jahren gestattet, die erste Vortragsstunde zu einer Art von Einleitung zu benutzen für dasjenige, was an den fol­genden Tagen vorzubringen sein wird.",
      "Der erste Gedanke, der sich Ihnen am Beginne unseres Zyklus aufdrängen mag, wird vielleicht doch mit demjenigen zusammen­hängen, womit wir gerade diesen Münchner Zyklus nun schon seit einigen Jahren einleiten durften: mit unseren theosophisch-künstlerischen Aufführungen. Und wenn ich selbst den Gedanken hier äußern darf, der mir bei dieser Gelegenheit vor die Seele tritt, so ist es der, daß es mich selbst mit der allertiefsten Befriedigung erfüllt, daß wir - sowohl das vorige Jahr wie auch dieses Mal - diese Auffüh­rungen eröffnen durften mit der Rekonstruktion des Mysteriums von Eleusis. Und ich sage es und möchte es ganz besonders deutlich gesagt haben, daß dies mir gelegentlich dieses Münchner Vortrags­zyklus die allergrößte Befriedigung gewährt. Vielleicht, da wir uns in diesem Jahre wieder eines stärkeren Besuches erfreuen dürfen, als das in den verflossenen Jahren der Fall war, wird es auch nicht unnötig sein, einige Worte bei dieser Gelegenheit zu wiederholen, die ich mir schon öfter gerade hier in München auszusprechen gestattete.",
      "Was mit diesem Mysterium von Eleusis verbunden ist, das hängt ja recht innig mit dem Streben zusammen, das wir hier in den mitteleuropäischen Gegenden seit Jahren als theosophisches Streben das unsrige nennen. Wir begannen - vor einem recht kleinen Kreis, von dem jetzt eigentlich nur noch wenige, recht wenige der theosophischen Bewegung treu geblieben sind - in Berlin vor Jahren, gera­de anknüpfend an alles, was für die theosophische Bewegung von unserem hochverehrten Edouard Schuré geleistet worden ist durch die Rekonstruktion des Mysteriums von Eleusis und die Darstellung der Einweihung, der Initiationsprinzipien der verschiedensten Zeiten",
      "und Völker, mit diesem sozusagen eine Art von Introduktion dieser unserer theosophischen Bewegung. Und jetzt, da wir seit Jah­ren hier in München so manches an Szenischem vorführen durften von dem, was aus Edouard Schurés Seele hervorgegangen ist, dürfen wir das, was wir zu tun vermocht haben, wie eine Art Besiegelung desjenigen auffassen, was für einen kleineren Kreis von uns sich an Gefühlen, an Empfindungen und Gedanken gerade an diesen Aus­gangspunkt unseres Strebens gebunden hat. Und soll ich charakteri­sieren, was sich daran gebunden hat, so möchte ich sagen: Es floß aus der rein spirituellen Art, aus der keusch-spirituellen Art, in wel­cher diese Dinge vor unsere Seele hintraten, eine innere Zuversicht, ein inneres Vertrauen, das dahin ging, daß wir uns sagen konnten: wenn wir diese Empfindungen, diese Gefühle mit dem, was sonst in unserer Seele lebt für das theosophische Streben, in uns einfließen lassen, so dürfen wir hoffen, daß uns einiges wenigstens gelingen wird. Das sagten uns damals, als wir begannen, die Dinge selbst; das sagte uns ihre ernste, ihre tief in das spirituelle Wesen eindringende Art, und das sagten uns die Jahre, die seit jener Zeit verflossen sind.",
      "Welchen Glauben konnten wir damals im Beginne und dann im Verlaufe der letzten Jahre haben?",
      "Die Wichtigkeit des Augenblickes - ich meine des Augenblickes in welthistorischer Beziehung - in der Entwickelung der Mensch­heit konnte einem vor die Seele treten; und vor die Seele treten konnte einem der Gedanke, daß es ganz gesetzmäßig ist in der Evo­lution der Menschheit, daß in unserer Gegenwart neue Kräfte und gerade Kräfte des spirituellen Lebens in die Menschenseelen herein­wollen, wenn diese sich aufrechterhalten wollen gegenüber dem, was die Gegenwart und die allernächste Zukunft von dem Innern dieser Menschenseelen verlangen werden. Ich darf an etwas Persön­liches - das mir aber nichts Persönliches ist - anknüpfen, indem ich diese Gedanken ausspreche. Jahre vorher, bevor wir mit unserer gei­steswissenschaftlichen Bewegung begannen, hatte ich öfter Gelegen­heit, über mancherlei geistige Angelegenheiten mit dem ja inzwi­schen in die höheren Welten eingegangenen deutschen Kunsthistori­ker Herman Grimm zu sprechen. Auf Spaziergängen von Weimar",
      "nach Tiefurt oder auch in Berlin wurde mancher Gedanke aus­gesprochen über die Anforderungen des Geisteslebens unserer Zeit und über die Anforderungen dessen, was notwendig ist für unsere Zeit gemäß der Natur, wie sich die Menschheit im Laufe der euro­päischen Entwickelung ihre Ziele gesucht hat und sich in ihrem Seelenleben hat zurechtfinden wollen. Ein Gedanke kam immer wieder zum Vorschein, wenn man mit diesem an allem Geistesleben des Abendlandes so interessierten Herman Grimm sprach: wie im Grunde genommen die europäische Menschheit zurückblicken kann auf eine Anzahl von Jahrhunderten oder auch auf die letzten zwei Jahrtausende so, daß der europäische Mensch, wenn er in seine Seele schaut, wenn er die Bedürfnisse seiner Seele prüft und sich fragt: Was kann ich verstehen, was ist mir begreiflich von dem Menschlichen, das da vorgeht und das ich brauche für das eigene Seelenleben? - sich sagen kann: Wie unverständlich auch manches sein mag in bezug auf Einzelheiten des Lebens, irgendwo kann ich anknüpfen an das, was ich selber erlebe, wenn ich die neuen Zeiten mir geschichtlich vor die Seele treten lasse.",
      "Ja, auch jene Verwick­lungen, die bestanden haben im römischen Kaiserreich, die zur Zeit Cäsars oder auch noch während der republikanischen römischen Zeit vorhanden waren, erscheinen, möchte man sagen, verständlich dem europäischen Bewußtsein der neueren Zeit. Man findet sich zu­recht, wenn man diese Seelen verstehen will, wenn auch das, was sie fühlen und denken, oftmals weit abliegt von dem, was der gegenwär­tige Mensch fühlen und denken kann.",
      "Ganz anders aber werden die Dinge, wenn die Seele zurückblickt ins alte Griechenland. Und nur wenn man nicht tief genug geht, wenn man es nicht tief genug nimmt mit dem, was man menschliches Verständnis nennen will, kann man sagen, daß einem als moderner Mensch das Griechentum ebenso verständlich sein kann wie etwa das Römertum und die fol­genden Zeiten.",
      "Es beginnt, wenn man rückschreitend ins Griechen­tum hineinkommt und auf seine Seele wirken läßt, was aus den ge­schichtlichen Urkunden überliefen ist, etwas Unverständliches. Und ich möchte das Wort wiederholen als ein durchaus klares und verständliches, das Herman Grimm öfter gebraucht hat: Ein solcher",
      "Mensch wie Alkibiades ist der reine Märchenfürst, verglichen mit Cäsar oder mit denen, die zur Zeit Cäsars gelebt haben. Ganz anders erscheint da griechisches Leben, erscheint Menschliches und Göttliches miteinander verbunden, ganz anders erscheint das Leben des Alltags und das, was man das Hereinleuchten von Göttlichem in das Leben des Alltages nennen kann; ganz anders erscheint das ganze Seelenleben, das auf dem Boden des alten Griechenlandes lebte. Auffällig werden die Dinge insbesondere, wenn man jene Gestalten auf die Seele wirken läßt, welche im Grunde genom­men viel lebendiger in der modernen Seele als die Gestalten, von denen die Geschichte erzählt, werden können, wenn man die Gestalten eines Homer, eines Äschylos oder eines Sophokles auf sich wirken läßt.",
      "Wenn man von einem solchen Gedanken ausgeht, kann man schon aus alledem, was die gegenwärtige Bildung ergibt, sich sagen:",
      "Je weiter man in der Menschheitsentwickelung zurückgeht, desto mehr erscheint der Mensch unmittelbar angeknüpft an ein Über­sinnliches, das hereinleuchtet in seine Seele, das da wirkt in seiner Seele, denn der Anfang eines ganz neuen Menschentumes offenbart sich schon, wenn man sich nicht oberflächlich, sondern gründlich der griechischen Seele naht. Daher erscheint auch etwas ganz Beson­deres, wenn man die Literaturwerke geschichtlicher Art, die im Lau­fe der europäischen Bildung entstanden sind, auf sich wirken läßt. Wie über etwas, was sie bewältigt haben, schreiben die Geschichts­schreiber über die verschiedenen Zeiten bis zurück in die römische Zeit. Wo Sie einen Geschichtsschreiber aufschlagen, werden Sie fin­den, daß er imstande sein wird, Gefühle und Empfindungen seiner Gegenwart bis ins alte Römertum hinein zu benutzen, um lebendig, gerundet die Gestalten zu machen, die er darstellt. Der bloßen Ge­schichtsschreibung - versuchen Sie einmal von diesem Gedanken ausgehend die Sache wirklich durchzugehen -, auch wo die besten Geschichtsschreiber wirken, werden die griechischen Gestalten, selbst noch der späteren griechischen Zeit, wie Silhouetten, wie Schattenbilder. Sie können nicht lebendig werden. Oder wer, der ein echtes Gefühl hat für einen Menschen, der mit seinen Füßen auf",
      "dem Boden steht, könnte behaupten, daß es je in Wahrheit einem Geschichtsschreiber gelungen ist, einen Lykurg oder einen Alkibia­des so auf die Beine zu stellen, wie dies zum Beispiel gegenüber dem Cäsar der Fall sein kann? Geheimnisvoll erscheint die griechische Seele, wenn man zurückblickt in die Zeiten des Griechentums. Ge­heimnisvoll erscheint sie dem Blick, der sie nur mit dem gewöhnli­chen Bewußtsein erfassen will. Und nur der empfindet richtig, der dieses Geheimnisvolle empfindet. Da kann man wohl die Frage auf­werfen: Wie würde eine griechische Seele gegenüber so manchem gefühlt haben, was der modernen Seele voll empfindlich, voll ver­ständlich ist?",
      "Nehmen wir eine frühe griechische Seele. Versuchen wir mit mancherlei von dem, was doch jetzt schon die Geisteswissenschaft an die Hand gibt, uns in diese griechische Seele hineinzufühlen. Da fragt man sich dann: Was würde die griechische Seele zu der Gestalt, der Darstellung des Sündenfalles, des Verlaufes und der Darstellung der alten Geschichte gesagt haben, die der späteren europäischen Seele so begreiflich sind? Die Paradiesesgeschichte, alles, was die spä­teren Zeiten als das Alte Testament in sich aufnahmen, es wäre der griechischen Seele recht fremd gewesen, so fremd, wie den bloß mo­dernen Menschen die griechische Seele selber bleibt. Die Versu­chung im Paradies, die Adam- und Eva-Geschichte, wie sie zum Bei­spiel im Mittelalter oder noch in der neuen Zeit lebten, man kann sie sich nicht in die griechische Seele so hineindenken, daß diese grie­chische Seele die Sache voll verstände, so verstände, daß man es, wenn man tiefer in die Sache geht, etwa Verständnis nennen kann. Daher ist es aber auch für uns notwendig, daß wir sozusagen unsere Seele erst zubereiten, um diese ganz andersartige Zeit wieder für uns verständlich zu machen. Wenn man solche Gedanken hegt, dann empfindet man so recht, was im Grunde genommen unsere allerneueste Zeit uns gebracht hat.",
      "Als am letzten Sonntag nach der letzten Szene des «Mysteriums von Eleusis» der Vorhang niederging, mußte ich denken, wie dank­bar wir sein dürfen, daß wir in unserer Gegenwart in der Lage sind, das Auge und die Seele hinrichten zu können auf den Verlauf von",
      "Vorgängen, welche uns diese griechische Seele in ihrem Fühlen und Erleben zeigen, und außerdem für das Anschauen dieser Vorgänge Seelen im Zuschauerraume zu haben, die sich denken können, daß in der Evolution der Menschheit über die Erde hin die menschliche Seele von Epoche zu Epoche andere Formen angenommen hat, ganz anders die Umgebung und das eigene Leben empfinden gelernt hat. Wir haben uns die Jahre hindurch bemüht, verstehen zu lernen, wie die menschlichen Seelen im Anbeginn der Erdenentwickelung leben mußten, als die äußere Leiblichkeit und damit das innere Seelenle­ben ein ganz anderes waren als später.",
      "Wir haben uns bemüht verste­hen zu lernen, wie die Menschenseelen lebten in der atlantischen Zeit und in der nachatlantischen Zeit, und haben dadurch die Mög­lichkeit gewonnen zu sagen: Oh, die Menschenseele, wie mannigfal­tig hat sie sich in uns ausgelebt! Die Seele, die in jedem von uns ist und immer wieder durch Inkarnationen und Inkarnationen hin­durchgegangen ist, nicht um dasselbe zu erleben, sondern um immer wieder und wieder anderes zu erleben - wie mannigfaltig hat sie sich ausgelebt!",
      "Und so mag es uns denn gelingen, da unten zu sitzen im Zuschauerraum und einmal zu vergessen, was uns in unserer Zeit unmittelbar bewegen muß, und unbefangen und objektiv aufzuneh­men, was die Seelen eben seelisch in ganz anderen Zeiten ihr eigen nannten. Wir brauchen nicht unseren Verstand in Bewegung zu set­zen, wir brauchen uns nur unserem unmittelbaren Empfinden hin­zugeben, dann zeigt sich uns schon, daß die Vorgänge, die sich da ab­spielen in dem rekonstruierten Mysterium von Eleusis, alles das zwar in sich haben, was die Seelen von den dunkelsten Lebensunter­gründen bis hinauf zu den Geisteslichtern, von den Schmerzen bis zu den Seligkeiten durchlebten, aber dies auf mannigfaltige Art im Laufe der Zeit erlebten.",
      "Und dann erhält man vielleicht ganz naiv und unbefangen - aber dafür vielleicht um so sicherer - ein Gefühl davon, was der Grieche empfand, wenn Namen ausgesprochen wur­den, Vorstellungen angeregt wurden wie Demeter, Persephone, Dionysos. Man erhält vielleicht die Möglichkeit, daß ganze Welten aus dem Innern der Seele vor uns hintreten, wenn diese Vorstellun­gen in uns angeregt werden.",
      "Als Menschen finden wir uns innerhalb der äußeren physischen Welt. Wir lernen sie kennen durch unsere Sinne, durch die Erlebnis­se unserer Seele und durch das, was wir mit unserem Verstande und unserer Vernunft erleben können. In einer ganz bestimmten Weise fühlen wir heute gewissermaßen unabhängig unsere Seele von dem äußeren Leben der uns umgebenden Natur und alles dessen, was sich in der Natur verbirgt. Wie der Mensch demgegenüber heute empfindet, das drückt sich wieder aus in einer Art, wie die griechi­sche Seele nicht hätte empfinden können. Das Entfremdetwerden gegenüber der Natur, das Betonen, daß man die Sinneswelt verlassen müsse, um in die spirituellen Welten hinaufzudringen, wäre dem Griechen noch nicht verständlich gewesen. Aber in seiner Art fühlte er, wie es einen bedeutsamen Unterschied, eine bedeutsame Tren­nung gibt zwischen dem, was man in dem menschlichen Innern nen­nen kann den Geist, und was man nennen kann die Seele. Das sind ja Worte für das menschliche Erleben, zwei verschiedene Gebiete zunächst und hart aneinanderstoßend: Seelisches und Geistiges.",
      "Richten wir den Blick hin auf die Szene gleich im Beginn der Auf­führung: Demeter, in stolzer geistiger Keuschheit vor Persephone stehend, sie mahnend, nicht zu genießen von den Früchten, die Eros geben kann. Wir richten das Auge hin auf diese Demeter. Alles, was der Mensch geistig nennt, wovon er sich sagt, er ist seiner teilhaftig als Geist, das erblickt er in der Demeter. Aber er erblickt auch, wie innerhalb der Erdenwelt dieses Geistige verbunden ist mit dem Sinn­lichsten, mit dem Materiellsten. Demeter, die Göttin, die Hervor-bringerin der Feldfrüchte und Vorsteherin der äußeren Einrichtun­gen und sittlichen Ordnungen der Menschheit - als Menschengeist, keusch und stolz gegenüber vielem, was sonst auch im Menschen lebt, aber innig verbunden mit der äußeren Sinneswelt, diese durch­dringend, so steht Demeter vor uns. Persephone tritt sogleich vor das innere Auge hin als etwas, das uns in unserer Seele wachruft die Vorstellung des menschlich Seelischen, verbunden mit alledem, wo­mit der Mensch in seinem individuellen Dasein dadurch verbunden ist, daß er mit seiner Seele eben in den Erdenleiden und Erdenfreu­den drinnensteht. Verbunden mit all dem, was die Erdenleiden und",
      "Erdenfreuden durchzuckt, muß sich die Seele fühlen, wenn sie sich vorstellen will, was in Persephone lebt. Ganz Seele - Persephone, ganz Menschengeist - Demeter. Und wenn wir dann den Verlauf des Mysteriums von Eleusis auf uns wirken lassen, wenn die Grund­töne, die gleich beim allerersten Gespräch zwischen Demeter und Persephone angeschlagen werden, weiter in uns klingen und sich verschlingen und sich finden und dann endlich zu der Gestalt des Dionysos herankommen - wie findet sich da der ganze Mensch sel­ber in Dionysos, wie findet sich dasjenige, was in uns lebendig wird gegenüber der Demeter und Persephone, zugleich in Dionysos! Und wir sehen in der letzten Szene ein Streben der Seele der Menschheit nach Harmonisierung ihres Seelischen mit dem Geistigen: das ganze dionysische Spiel - aus dem Lebensdunkel zum Geisteslicht hinauf!",
      "Ich kommentiere nicht und möchte nicht ein künstlerisches Werk zerpflücken, ich möchte nur die Empfindungen, die über intime Seelengeheimnisse im Menschen aufgehen können, in Worte brin­gen, wenn sich der Mensch dem Mysterium von Eleusis gegenüber­gestellt sieht. Niemals wird es mir einfallen zu sagen, in Demeter sei personifiziert oder symbolisiert eine ursprüngliche Form des Men­schengeistes und in Persephone die menschliche Seele. Das hieße dem Plastischen des Kunstwerkes Gewalt antun, steife Verstandes­begriffe anwenden gegenüber dem, was im Kunstwerke lebt, wie Menschen oder sonstige Wesen selber lebendig leben. Aber was man empfinden darf, was man empfinden kann über Seelengeheimnisse, das darf man sagen.",
      "Und jetzt stellen wir einmal vor uns hin zwei Bilder. Stellen wir das spätere europäische Bewußtsein vor unsere Seele hin, das erst jetzt in unserer Gegenwart beginnt sich aufzulösen und lechzen wird nach denjenigen Formen, die ihm in Wahrheit die Theosophie weist, wie es durch die Jahrhunderte gewirkt hat: diese europäische Seele, die Lebensrätsel empfand, wenn ihr vorgestellt wurde, wie der Mensch, der erste Mensch da stand - Mann, Weib - in unendlichem Abstand von seinem Gotte, den er fürchten mußte, hörend die ver­lockende Stimme einer Wesenheit, fremd der eigenen Menschensee­le. Woher kommt diese Wesenheit? Was ist sie? Wie ist sie verwandt",
      "mit dem eigenen Seelischen? Kaum denkt die europäische Seele, das europäische Bewußtsein daran, sich darüber aufzuklären. Sie nimmt hin die Fremdheit des Luzifer, sie begnügt sich damit zu wissen, daß von ihm die Erkenntnis, aber auch die Verführungsstimme ausge­gangen ist. Und wie tönen dann wie aus Weltenfernen heraus die Worte, die das göttliche Strafgericht verhängt nach der Verführung! Wie sind sie schon durch ihre Fassung geeignet, die Seele gar nicht dazu aufzurufen, sich zu fragen: Wo lebt das, was da draußen im Makrokosmos durch die Räume klingt, in dem eigensten intimsten Seelenleben? Man versuche empfindend das, was als der Paradieses­vorgang vorgestellt werden kann, bildlich darzustellen; man versu­che zu empfinden, wie unnatürlich es wäre, die entsprechenden Ge­stalten, mit denen man es dabei zu tun hat, in rein menschlichen Formen darzustellen. Und jetzt versuche man sich vorzustellen, wie selbstverständlich es ist, daß da, wo von intimsten, tiefsten Seelen­angelegenheiten der Griechen gesprochen wird, die menschliche Ge­stalt der Demeter, die menschliche Gestalt der Persephone, selbst die menschliche Gestalt des Dionysos oder des Zeus vor unseren Augen steht! Man versuche daraus zu empfinden, wie unendlich nahe der griechischen Seele dasjenige lag, was zugleich durch den Makrokosmos geht!",
      "Es braucht nur ein Wort ausgesprochen zu werden, um das zu charakterisieren, worum es sich dabei handelt. Einfach, ganz einfach kann dieses Wort ausgesprochen sein. Man braucht nur zu sagen: Bevor durch unseren hochverehrten Edouard Schuré das Mysterium von Eleusis nicht rekonstruiert war, so wie wir es jetzt sehen kön­nen, war es eben nicht da. Und jetzt haben wir es! Man braucht nur zu empfinden, was in diesen beiden Sätzen liegt, dann ist alles gesagt. Es handelt sich gegenüber dieser Sache um etwas, was meiner Emp­findung nach alles triviale Aussprechen eines Dankgefühles über­ragt. Damit ist aber hingewiesen auf die ganze Bedeutung, welche diese Rekonstruktion des Mysteriums von Eleusis für das moderne spirituelle Leben hat. Dann aber mag sich auch manche Seele geste­hen, daß alles, was mit diesem Mysterium von Eleusis zusammen­hängt und was in bezug auf die historische Wiedererweckung der",
      "Initiationsprinzipien der verschiedenen Epochen durch denselben Autor geschehen ist, etwas ist, woraufhin bestimmt ist das Tiefste, das Intimste der europäischen Seelennatur. Und eine Verpflichtung liegt vor, eine Verpflichtung heilig ernster Art für jeden, der es auf­richtig und ernst mit dem spirituellen Leben meint, gerade diese Art hineinzutragen in das moderne Seelenleben.",
      "Meine lieben Freunde! Sie können viel den Leuten draußen in der Welt sprechen von allerlei theosophischen Dingen; es kann auch sein, daß die Leute von einem solchen Sprechen befriedigt erschei­nen können.",
      "Wenn man aber in die Tiefen der Seelen hineinzublicken vermag, dann weiß man, wessen die Seelen bedürftig sind, wie notwendig es ist, ihnen das zu geben, dessen sie sich vielleicht nicht bewußt sind, was sie aber in ihren tiefsten Herzensgründen wahr­haftig verlangen! Solche Gefühle waren es, die meine Seele durch­drangen, als wir am letzten Sonntag den Vorhang heruntergehen sahen nach der letzten Szene des «Mysteriums von Eleusis».",
      "Und wenn man so empfinden möchte dasjenige, was sich abgespielt hat, dann lebt in diesem Empfinden selber so viel, daß man ihm Frucht­barkeit und Wirkenskraft für das Leben zugesteht. Und wenn wir diese Fruchtbarkeit, diese Wirksamkeit in den letzten Jahren an so manchem sahen, dann dürfen wir auch leicht hinwegkommen über manches andere, was heute nicht hierhergehört, was sich aber hem­mend dieser Fruchtbarkeit, dieser Wirksamkeit entgegenstellt und vielleicht noch mehr entgegenstellen wird, als dies in den verflosse­nen Jahren der Fall war.",
      "Und daß ich selber etwa nicht allein dastehe mit diesem Empfinden, das konnten mich die Wochen lehren, wel­che unseren Münchner Aufführungen vorangingen. Sie sehen ja in den ersten Tagen, in denen Sie im Beginne unserer Münchner Zeit diesen Mysterienaufführungen gegenüberstehen, eine Anzahl der Freunde von der Bühne herab, und da Sie ja alle wohl diejenigen kennen, die Sie da sehen, so brauche ich, was ich ja wahrhaftig tun würde, hier nicht die Namen aller einzelnen Ihnen anzuführen.",
      "Aber das wohl darf ich sagen: daß wir alle, die wir hier sitzen, war­mes Dankgefühl gegenüber denjenigen empfinden dürfen, die sich wochenlang mit Hingebung - denn das ist notwendig, wenn es auch",
      "oftmals nicht so aussieht -, mit Hingebung aller ihrer Kräfte wid­men dem Studium und dem Durchdringen der Gestalten, die sie dar­zustellen haben. Und in allen denen, die Sie selber auf der Bühne sehen, lebt das Bewußtsein, daß sie Diener sind der spirituellen Welt, daß in unserer Zeit die Notwendigkeit besteht, der allgemei­nen Menschenkultur spirituelle Werte zuzuführen, und daß alles versucht werden muß, um diese spirituellen Werte der allgemeinen Menschenkultur zuzuführen.",
      "Verehrung gegenüber den spirituellen Angelegenheiten läßt die Mitspielenden so manches, was die Vorbe­reitungen für die Aufführungen erfordern, gern ertragen. Das darf einmal gesagt werden aus dem Grunde, weil es ja mit unserer ganzen Sache zusammenhängt und weil wahrhaftig die Anstrengungen zu große sind, als daß gerade nur etwa Ehrgeiz oder Eitelkeit, sich von der Bühne herab betrachten zu lassen, die einzelnen dahin führen würde, sich zu Darstellern der betreffenden Gestalten zu machen.",
      "Mit besonderem Danke müssen wir aber derer gedenken, die sozusa­gen hinter den Kulissen, aber vielleicht viel sichtbarer noch als die einzelnen Darsteller, in opferwilliger, hingebungsvoller Art nun schon seit Jahren ihr Können und ihr Streben - besonders ihr Kön­nen, was noch mehr ist als ihr Streben - in den Dienst gerade dieser Sache stellen. Wir dürfen es wie eine An inneres Karma gerade unse­rer Bewegung ansehen, daß wir in der Lage sind, eine Persönlichkeit zu haben, welche alles, was das Bühnenbild erfordert in bezug auf -sagen wir Umhüllungen und Kleidungen, in bezug auf die Kostüme der Darsteller, wenn ich dieses triviale, mir abscheulich klingende Wort aus der allgemeinen Bühnensprache gebrauchen will, in einer solchen Weise besorgt, daß es nicht nur den Intentionen, die mir sel­ber am Herzen liegen, entspricht, sondern auch getragen ist von wahrer Spiritualität.",
      "Wir dürfen es als ein günstiges Karma unserer Bewegung innerhalb Mitteleuropas betrachten, eine solche Persön­lichkeit unter uns zu haben. Und daß dieses Karma tiefer begründet ist, das zeigt sich auch darin, daß dieselbe Persönlichkeit in so ausge­zeichneter Art mitwirken konnte bei allem, was zum Beispiel für unsern «Kalender» in den letzten Monaten hat geschehen können, der ja wie alle unsere Unternehmungen dem großen Ziele dienen",
      "soll; so daß gewiß in erster Linie bei denjenigen, die nicht nur als Darsteller, sondern auch in dem Ganzen in hervorragender Weise mitwirken, der Name des Fräulein von Eckardtstein genannt werden darf. Dann darf ich mit innigstem Dankgefühl gedenken und möch­te dieses Dankgefühl in Ihren Herzen mit anregen auch für unsere hingebungsvollen Maler Volckert, Linde, Haß und in diesem Jahre auch Steglich aus Kopenhagen. Ich möchte es anregen in Ihren Her­zen, weil wahrhaftig etwas dazu gehört, aus den spirituellen Tiefen heraus etwas anzustreben, daß für das Auge äußerlich da ist, was uns vor der Seele steht. Und viele müssen, weil es zu viele sind, unge­nannt bleiben. Ja, wenn so ein Bühnenbild dasteht, dann merkt man nicht, daß dafür - vielleicht nur für die letzte Zurichtung außerdem -dasjenige, was der Maler zugerichtet hat in einem Raume, der viel größer ist als dieser Saal hier, ausgespannt sein muß und daß vierzig bis fünfzig Personen auf dem Boden herumkriechen müssen, um überhaupt das alles an Ort und Stelle zu bringen, wohin es gehört. Eine solche Verpflichtung übernehmen gern unsere Freunde; sie kriechen gern auf dem Boden herum, um alles anzunähen, was ange­näht werden muß, und was dann vielleicht nur für wenige Minuten von der Bühne herab sichtbar erscheint. Warum sage ich das alles?",
      "Vielleicht erscheint es manchem höchst unnötig, dies zu sagen. Theosophie aber besteht nicht bloß in Theorien und Prophetien. Theosophie besteht in der hingebungsvollen Opferwilligkeit für das, was unsere Zeit von uns fordert, auch dann, wenn wir unmittel­bar selbst diese Forderungen nur dann erfüllen, wenn wir einmal viele Tage lang auf dem Boden herumrutschen müssen, um das in Ordnung zu bringen, was dann in uns sich beleben kann im An­blick, was lebendig sein soll in unserer Seele, damit diese Seele mit den Anforderungen der modernen Zeit fertig werden kann. Ein Ge­fühl dafür soll erregt werden, daß von wirklicher menschlicher Ar­beit der Kern ausgeht für jenes spirituelle Leben, das der Zukunft der Menschen auch notwendig ist. Dann, wenn man solches fühlt, wird man auch immer mehr und mehr verstehen, wie zusammen­wachsen müssen die Seelen derer, die sich Theosophen nennen wol­len, in gemeinsamen, ernsten und würdigen Zielen im konkreten",
      "unmittelbaren Arbeiten. Denn wert ist vor allen Dingen das, was der einzelne tut, was der einzelne schafft, was der einzelne bereit ist, an Opfern zu bringen! Und wen ist das, was der einzelne sich er­wirbt an Ertragsamkeit für Enttäuschungen.",
      "Hier an diesem Orte und in unserer mitteleuropäischen geisteswissenschaftlichen Bewe­gung darf es gesagt werden: Es haben diejenigen, deren Karma es ist, ein wenig sozusagen zusammenzuhalten die Fäden, die wir brau­chen für die Bildung des spirituellen Kernes, wahrhaftig in den letz­ten Zeiten nicht wenige Enttäuschungen erlebt. Aber mag manches Wort über solche Enttäuschungen gefallen sein, eines ist noch nicht gefallen, und wir möchten es erbitten von den spirituellen Mächten, die hinter unserer Bewegung stehen und sie anfeuern, daß dieses Wort nicht zu fallen braucht, ein Wort: daß unsere lieben Mitarbei­ter erlahmen möchten.",
      "Solange sie ihre Hände regen, solange sie ihre Gedanken regen, können wir uns für unsere geistige Bewegung sa­gen: Sie wollen! Und solange sie wollen werden, gleichgültig, ob sich das Gedeihen auf den ersten Tag zeigt oder erst nach Jahrhun­derten, solange sie wollen werden, solange werden sie im rechten Sinne des Wortes Theosophen sein!",
      "Fühlen wir uns in diesem Wol­len, das auch Enttäuschungen ertragen kann, in wahrer, arbeitsamer Liebe zusammen, dann werden wir arbeiten können. Dann wird daraus entspringen dasjenige, was der Menschheit in ihrer gegen­wärtigen Entwickelungsstufe notwendig ist.",
      "Mögen unsere Kräfte schwach sein, wir können keine stärkeren bringen als wir haben. Eines können wir aber; seit Monaten betonen wir dieses eine, und ich mußte in diesen Tagen dieses einen gedenken. Es gab Zwischen­tage zwischen unseren Aufführungen; viele unserer Freunde waren vom Morgen bis zum Abend bei den Generalproben beschäftigt.",
      "Unser lieber Dr. Unger hatte Ihnen in diesen Tagen hier in Mün­chen Vorträge gehalten. Es war für mich etwas tief Erfreuliches, Beseligendes, als unser lieber Freund, der Direktor Sellin, gestern morgen zu mir kam, voller Begeisterung über diese beiden Vorträge des Dr.",
      "Unger, und mir hinter den Kulissen das Wort sagte: «Eine Bewegung, die solche begeisterte Vertreter vor der Öffentlichkeit hat, geht nicht zugrunde!» Denn worüber darf ich mich selbergestatten",
      "Sie mir dieses aufrichtige, ehrliche Wort - am allermeisten freuen, wenn gerade so etwas vorkommen kann? Ich kann mich am meisten freuen über die selbständige Kraft, über die durchaus selb­ständige Art, wie hier eine Menschenpersönlichkeit aus sich heraus, frei, ohne sich unmittelbar nur an dasjenige zu halten, was ich selber aussprechen kann, die Sache aus sich heraus nach ihren eigenen Fä­higkeiten begründet!",
      "Wer selbst selbständig wirken will, wird nichts freudiger, aufrichtiger begrüßen, als wenn eine selbständige Persön­lichkeit neben ihm Schulter an Schulter steht und dasjenige gibt, was sie zu geben in der Lage ist, nachdem sie erkannt hat, daß es sich zum Ganzen fügen kann. Eine Festesfreude war es mir, als Direktor Sellin kam und - ich möchte sagen wie aus kindlichem Herzen her­aus, denn es stellte sich so dar - seine volle Begeisterung aussprach über das, was er gehört hatte.",
      "Ich darf es Ihnen sagen und weiß, daß es mir doch eine große Anzahl glauben werden, daß ich die innigste Freude habe über solche Selbständigkeit, über ein solches individuel­les Wirken, und daß dies die Wahrheit ist. Wenige Zeiten vorher be­kam ich einen Brief, der ungefähr sagte, daß es notwendig wäre, mancherlei zu tun innerhalb der deutschen theosophischen Bewe­gung, weil ja doch sonst niemand zu Worte komme als der, welcher wortgetreu das nachsprechen mag, was ich selbst sage.",
      "So ist oftmals die Darstellung draußen in der Welt von dem, was die Wahrheit ist! Nicht Kritik soll geübt werden an einem solchen Wort, das objektiv eine Unrichtigkeit im straffsten Sinne des Wortes enthält, auch nicht ein Tadel oder eine Strafe soll darin liegen.",
      "Man kann nur Mit­leid haben mit einem solchen Wort. Aber das andere, was für uns positiv sein kann, muß immer wieder und wieder betont werden: Fühlen wir uns verpflichtet zur Wahrhaftigkeit, zur Prüfung dessen, was ist!",
      "Und fühlen wir es uns verboten, über irgend etwas zu spre­chen, bevor wir es kennengelernt haben, bevor wir auf dasselbe ein­gegangen sind! Sonst gibt es keinen Segen in einer okkulten Ent­wickelung, in einer okkulten Bestrebung.",
      "Wahrheit und Wahrhaf­tigkeit - das ist oberstes Gesetz. Was nützen alle Prophetien, was nützen alle Charakteristiken übersinnlicher Tatsachen, wenn sie nicht getaucht sind in das Bad ehrlichster, aufrichtigster Wahrhaftigkeit!",
      "Sie mögen manches von dem Orte, von dem ich zu Ihnen spre­chen darf, an diesen oder jenen geisteswissenschaftlichen Wahrhei­ten entgegennehmen; am allerliebsten ist es mir aber, wenn Sie hier dieses Wort entgegennehmen, daß es mein eigenstes, innerstes Be­streben Ihnen gegenüber immer sein wird, über nichts zu sprechen, als worüber ich sprechen darf im Sinne ehrlichster Wahrhaftigkeit, und daß ich den Segen einer okkulten Bewegung in nichts anderem sehen kann als in dem Sich-Verpflichtetfühlen zur Wahrhaftigkeit! Mag es unseren Wünschen zuwider sein, mag es entgegen sein dem, was unser Ehrgeiz, unsere Eitelkeit verlangen, mag es manchem in unserer Seele zuwider sein, mag es uns zuwider sein, irgendeiner Autorität uns zu unterwerfen - das kann richtig sein.",
      "Einer Autori­tät sollen wir uns freiwillig und willig unterwerfen: der Autorität der Wahrhaftigkeit, so daß alles, was wir leisten können - nicht nur in dem, was wir sagen, sondern auch in dem, was wir tun, was wir im einzelnen tun - durchdrungen sei von Wahrhaftigkeit. Das suchen Sie auch in dem, was wir in unseren theosophisch-künstleri-schen Bestrebungen vor Ihre Augen stellten.",
      "Versuchen Sie es zu fin­den, und vielleicht werden Sie sehen, daß wir auch manches nicht er­reichten, aber eines werden Sie sehen: daß es unser Bestreben ist, das, was wir tun, zu tauchen in die Sphäre und in die Atmosphäre der Wahrhaftigkeit, daß wir es uns verbieten, von Toleranz zu spre­chen, wenn diese Toleranz nicht auch wahrhaftig da ist, wenn wir sie nicht auch wahrhaftig üben. Denn das, daß man den andern into­lerant nennt, macht die Toleranz nicht aus; daß man etwas anderes von jemandem erzählt, als er vertritt, das macht die Toleranz nicht aus; daß man immer betont, man sei tolerant, das macht die Tole­ranz nicht aus.",
      "Wenn man aber wahrhaftig ist, dann kennt man sei­nen Wert, dann weiß man auch, wie weit man gehen darf. Und ist man ein Diener der Wahrhaftigkeit, dann ist man selbstverständlich tolerant.",
      "In einleitender Weise durften wohl auch solche Worte gespro­chen werden, obwohl es sonst nicht meine Art ist, auf allerlei Mah­nungen und Ermahnungen einzugehen. Aber wie sollten denn nicht gerade bei einer solchen Gelegenheit diese Worte sich dem Herzen",
      "loslösen, die aufmerksam machen möchten, wie wir aus innig ver­wandtem Impuls heraus in der Lage waren, diese Rekonstruktion des Mysteriums von Eleusis in gewisser Beziehung immer wieder und wieder zu etwas zu machen, woran wir anknüpfen. Wir wollten zu den europäischen Seelen ehrlich und aufrichtig, wahrhaftig sein und wollten im Sinne der Wahrhaftigkeit suchen, wonach die euro­päische Seele lechzt.",
      "Was oftmals das Tiefste ist, erkundet sich zu­letzt in den einfachsten Worten, formuliert sich zuletzt in den ein­fachsten Worten. Lernen wir aus ehrlicher, aufrichtiger Überzeu­gung von dem, was der Zeit not tut, erkennen, was es für eine Tat war, aus den dunklen Geistestiefen heraus, die gerade dann begin­nen, wenn wir vom Römertum ins Griechentum kommen, dieses Mysterium von Eleusis wiederzuerschaffen.",
      "Fühlen wir, was es heißt: Bevor das Mysterium von Eleusis durch unsern hochverehr­ten Edouard Schuré nicht geschaffen war, war es nicht da, und jetzt ist es da! Wir haben es und dürfen auf es bauen, und damit auf die alleinige Art, wie wahrhaftiges Griechentum vor unsere Seele hin­treten kann, daß sie darauf hinschauen kann.",
      "Wenn wir das empfin­den, fühlen wir die Bedeutung dessen - womit wir diese unsere Münchner Unternehmungen eröffnen dürfen - in diesem Jahre wie im vorigen. Dann dürfen wir es jeder einzelnen hier befindlichen Seele überlassen, mit welcher Herzlichkeit - von der ich sicher bin, daß sie bei vielen eine innige sein wird - sie der Gedanke erfüllt, daß der Schöpfer dieser Rekonstruktion des Mysteriums von Eleusis unter uns gerade während dieser Münchner Zeit weilt."
    ],
    "sentences": [
      [
        "Von der Initiation"
      ],
      [
        "Von Ewigkeit und Augenblick"
      ],
      [
        "Von Geisteslicht und"
      ],
      [
        "Lebensdunkel"
      ],
      [
        "Ein Zyklus von sieben Vorträgen"
      ],
      [
        "und ein Sondervortrag"
      ],
      [
        "gehalten in München"
      ],
      [
        "vom 25. bis 31.",
        "August 1912"
      ],
      [
        "RUDOLF STEINER VERLAG"
      ],
      [
        "DORNACH/SCHWEIZ"
      ],
      [
        "Nach einer vom Vortragenden nicht durchgesehenen Nachschrift"
      ],
      [
        "herausgegeben von der Rudolf Steiner-Nachlaßverwaltung"
      ],
      [
        "Die Herausgabe besorgte Edwin Froböse"
      ],
      [
        "vom 30.",
        "August 1912"
      ],
      [
        "Gesamtausgabe Dornach 1959"
      ],
      [
        "Bibliographie-Nr. 138"
      ],
      [
        "Das Siegel auf dem Einband"
      ],
      [
        "hat Rudolf Steiner 1912 für die Buchausgabe des dritten Mysteriendramas"
      ],
      [
        "«Der Hüter der Schwelle» entworfen"
      ],
      [
        "#c 1959 by Rudolf Steiner-Nachlaßverwaltung, Dornach/Schweiz"
      ],
      [
        "Satz: Kooperative Dürnau, Dürnau"
      ],
      [
        "Printed in Germany by Greiserdruck, Rastatt"
      ],
      [
        "Am Beginne unseres Münchner Vortragszyklus sei es mir auch dies­mal wie in den letzten Jahren gestattet, die erste Vortragsstunde zu einer Art von Einleitung zu benutzen für dasjenige, was an den fol­genden Tagen vorzubringen sein wird."
      ],
      [
        "Der erste Gedanke, der sich Ihnen am Beginne unseres Zyklus aufdrängen mag, wird vielleicht doch mit demjenigen zusammen­hängen, womit wir gerade diesen Münchner Zyklus nun schon seit einigen Jahren einleiten durften: mit unseren theosophisch-künstlerischen Aufführungen.",
        "Und wenn ich selbst den Gedanken hier äußern darf, der mir bei dieser Gelegenheit vor die Seele tritt, so ist es der, daß es mich selbst mit der allertiefsten Befriedigung erfüllt, daß wir - sowohl das vorige Jahr wie auch dieses Mal - diese Auffüh­rungen eröffnen durften mit der Rekonstruktion des Mysteriums von Eleusis.",
        "Und ich sage es und möchte es ganz besonders deutlich gesagt haben, daß dies mir gelegentlich dieses Münchner Vortrags­zyklus die allergrößte Befriedigung gewährt.",
        "Vielleicht, da wir uns in diesem Jahre wieder eines stärkeren Besuches erfreuen dürfen, als das in den verflossenen Jahren der Fall war, wird es auch nicht unnötig sein, einige Worte bei dieser Gelegenheit zu wiederholen, die ich mir schon öfter gerade hier in München auszusprechen gestattete."
      ],
      [
        "Was mit diesem Mysterium von Eleusis verbunden ist, das hängt ja recht innig mit dem Streben zusammen, das wir hier in den mitteleuropäischen Gegenden seit Jahren als theosophisches Streben das unsrige nennen.",
        "Wir begannen - vor einem recht kleinen Kreis, von dem jetzt eigentlich nur noch wenige, recht wenige der theosophischen Bewegung treu geblieben sind - in Berlin vor Jahren, gera­de anknüpfend an alles, was für die theosophische Bewegung von unserem hochverehrten Edouard Schuré geleistet worden ist durch die Rekonstruktion des Mysteriums von Eleusis und die Darstellung der Einweihung, der Initiationsprinzipien der verschiedensten Zeiten"
      ],
      [
        "und Völker, mit diesem sozusagen eine Art von Introduktion dieser unserer theosophischen Bewegung.",
        "Und jetzt, da wir seit Jah­ren hier in München so manches an Szenischem vorführen durften von dem, was aus Edouard Schurés Seele hervorgegangen ist, dürfen wir das, was wir zu tun vermocht haben, wie eine Art Besiegelung desjenigen auffassen, was für einen kleineren Kreis von uns sich an Gefühlen, an Empfindungen und Gedanken gerade an diesen Aus­gangspunkt unseres Strebens gebunden hat.",
        "Und soll ich charakteri­sieren, was sich daran gebunden hat, so möchte ich sagen: Es floß aus der rein spirituellen Art, aus der keusch-spirituellen Art, in wel­cher diese Dinge vor unsere Seele hintraten, eine innere Zuversicht, ein inneres Vertrauen, das dahin ging, daß wir uns sagen konnten: wenn wir diese Empfindungen, diese Gefühle mit dem, was sonst in unserer Seele lebt für das theosophische Streben, in uns einfließen lassen, so dürfen wir hoffen, daß uns einiges wenigstens gelingen wird.",
        "Das sagten uns damals, als wir begannen, die Dinge selbst; das sagte uns ihre ernste, ihre tief in das spirituelle Wesen eindringende Art, und das sagten uns die Jahre, die seit jener Zeit verflossen sind."
      ],
      [
        "Welchen Glauben konnten wir damals im Beginne und dann im Verlaufe der letzten Jahre haben?"
      ],
      [
        "Die Wichtigkeit des Augenblickes - ich meine des Augenblickes in welthistorischer Beziehung - in der Entwickelung der Mensch­heit konnte einem vor die Seele treten; und vor die Seele treten konnte einem der Gedanke, daß es ganz gesetzmäßig ist in der Evo­lution der Menschheit, daß in unserer Gegenwart neue Kräfte und gerade Kräfte des spirituellen Lebens in die Menschenseelen herein­wollen, wenn diese sich aufrechterhalten wollen gegenüber dem, was die Gegenwart und die allernächste Zukunft von dem Innern dieser Menschenseelen verlangen werden.",
        "Ich darf an etwas Persön­liches - das mir aber nichts Persönliches ist - anknüpfen, indem ich diese Gedanken ausspreche.",
        "Jahre vorher, bevor wir mit unserer gei­steswissenschaftlichen Bewegung begannen, hatte ich öfter Gelegen­heit, über mancherlei geistige Angelegenheiten mit dem ja inzwi­schen in die höheren Welten eingegangenen deutschen Kunsthistori­ker Herman Grimm zu sprechen.",
        "Auf Spaziergängen von Weimar"
      ],
      [
        "nach Tiefurt oder auch in Berlin wurde mancher Gedanke aus­gesprochen über die Anforderungen des Geisteslebens unserer Zeit und über die Anforderungen dessen, was notwendig ist für unsere Zeit gemäß der Natur, wie sich die Menschheit im Laufe der euro­päischen Entwickelung ihre Ziele gesucht hat und sich in ihrem Seelenleben hat zurechtfinden wollen.",
        "Ein Gedanke kam immer wieder zum Vorschein, wenn man mit diesem an allem Geistesleben des Abendlandes so interessierten Herman Grimm sprach: wie im Grunde genommen die europäische Menschheit zurückblicken kann auf eine Anzahl von Jahrhunderten oder auch auf die letzten zwei Jahrtausende so, daß der europäische Mensch, wenn er in seine Seele schaut, wenn er die Bedürfnisse seiner Seele prüft und sich fragt: Was kann ich verstehen, was ist mir begreiflich von dem Menschlichen, das da vorgeht und das ich brauche für das eigene Seelenleben? - sich sagen kann: Wie unverständlich auch manches sein mag in bezug auf Einzelheiten des Lebens, irgendwo kann ich anknüpfen an das, was ich selber erlebe, wenn ich die neuen Zeiten mir geschichtlich vor die Seele treten lasse."
      ],
      [
        "Ja, auch jene Verwick­lungen, die bestanden haben im römischen Kaiserreich, die zur Zeit Cäsars oder auch noch während der republikanischen römischen Zeit vorhanden waren, erscheinen, möchte man sagen, verständlich dem europäischen Bewußtsein der neueren Zeit.",
        "Man findet sich zu­recht, wenn man diese Seelen verstehen will, wenn auch das, was sie fühlen und denken, oftmals weit abliegt von dem, was der gegenwär­tige Mensch fühlen und denken kann."
      ],
      [
        "Ganz anders aber werden die Dinge, wenn die Seele zurückblickt ins alte Griechenland.",
        "Und nur wenn man nicht tief genug geht, wenn man es nicht tief genug nimmt mit dem, was man menschliches Verständnis nennen will, kann man sagen, daß einem als moderner Mensch das Griechentum ebenso verständlich sein kann wie etwa das Römertum und die fol­genden Zeiten."
      ],
      [
        "Es beginnt, wenn man rückschreitend ins Griechen­tum hineinkommt und auf seine Seele wirken läßt, was aus den ge­schichtlichen Urkunden überliefen ist, etwas Unverständliches.",
        "Und ich möchte das Wort wiederholen als ein durchaus klares und verständliches, das Herman Grimm öfter gebraucht hat: Ein solcher"
      ],
      [
        "Mensch wie Alkibiades ist der reine Märchenfürst, verglichen mit Cäsar oder mit denen, die zur Zeit Cäsars gelebt haben.",
        "Ganz anders erscheint da griechisches Leben, erscheint Menschliches und Göttliches miteinander verbunden, ganz anders erscheint das Leben des Alltags und das, was man das Hereinleuchten von Göttlichem in das Leben des Alltages nennen kann; ganz anders erscheint das ganze Seelenleben, das auf dem Boden des alten Griechenlandes lebte.",
        "Auffällig werden die Dinge insbesondere, wenn man jene Gestalten auf die Seele wirken läßt, welche im Grunde genom­men viel lebendiger in der modernen Seele als die Gestalten, von denen die Geschichte erzählt, werden können, wenn man die Gestalten eines Homer, eines Äschylos oder eines Sophokles auf sich wirken läßt."
      ],
      [
        "Wenn man von einem solchen Gedanken ausgeht, kann man schon aus alledem, was die gegenwärtige Bildung ergibt, sich sagen:"
      ],
      [
        "Je weiter man in der Menschheitsentwickelung zurückgeht, desto mehr erscheint der Mensch unmittelbar angeknüpft an ein Über­sinnliches, das hereinleuchtet in seine Seele, das da wirkt in seiner Seele, denn der Anfang eines ganz neuen Menschentumes offenbart sich schon, wenn man sich nicht oberflächlich, sondern gründlich der griechischen Seele naht.",
        "Daher erscheint auch etwas ganz Beson­deres, wenn man die Literaturwerke geschichtlicher Art, die im Lau­fe der europäischen Bildung entstanden sind, auf sich wirken läßt.",
        "Wie über etwas, was sie bewältigt haben, schreiben die Geschichts­schreiber über die verschiedenen Zeiten bis zurück in die römische Zeit.",
        "Wo Sie einen Geschichtsschreiber aufschlagen, werden Sie fin­den, daß er imstande sein wird, Gefühle und Empfindungen seiner Gegenwart bis ins alte Römertum hinein zu benutzen, um lebendig, gerundet die Gestalten zu machen, die er darstellt.",
        "Der bloßen Ge­schichtsschreibung - versuchen Sie einmal von diesem Gedanken ausgehend die Sache wirklich durchzugehen -, auch wo die besten Geschichtsschreiber wirken, werden die griechischen Gestalten, selbst noch der späteren griechischen Zeit, wie Silhouetten, wie Schattenbilder.",
        "Sie können nicht lebendig werden.",
        "Oder wer, der ein echtes Gefühl hat für einen Menschen, der mit seinen Füßen auf"
      ],
      [
        "dem Boden steht, könnte behaupten, daß es je in Wahrheit einem Geschichtsschreiber gelungen ist, einen Lykurg oder einen Alkibia­des so auf die Beine zu stellen, wie dies zum Beispiel gegenüber dem Cäsar der Fall sein kann?",
        "Geheimnisvoll erscheint die griechische Seele, wenn man zurückblickt in die Zeiten des Griechentums.",
        "Ge­heimnisvoll erscheint sie dem Blick, der sie nur mit dem gewöhnli­chen Bewußtsein erfassen will.",
        "Und nur der empfindet richtig, der dieses Geheimnisvolle empfindet.",
        "Da kann man wohl die Frage auf­werfen: Wie würde eine griechische Seele gegenüber so manchem gefühlt haben, was der modernen Seele voll empfindlich, voll ver­ständlich ist?"
      ],
      [
        "Nehmen wir eine frühe griechische Seele.",
        "Versuchen wir mit mancherlei von dem, was doch jetzt schon die Geisteswissenschaft an die Hand gibt, uns in diese griechische Seele hineinzufühlen.",
        "Da fragt man sich dann: Was würde die griechische Seele zu der Gestalt, der Darstellung des Sündenfalles, des Verlaufes und der Darstellung der alten Geschichte gesagt haben, die der späteren europäischen Seele so begreiflich sind?",
        "Die Paradiesesgeschichte, alles, was die spä­teren Zeiten als das Alte Testament in sich aufnahmen, es wäre der griechischen Seele recht fremd gewesen, so fremd, wie den bloß mo­dernen Menschen die griechische Seele selber bleibt.",
        "Die Versu­chung im Paradies, die Adam- und Eva-Geschichte, wie sie zum Bei­spiel im Mittelalter oder noch in der neuen Zeit lebten, man kann sie sich nicht in die griechische Seele so hineindenken, daß diese grie­chische Seele die Sache voll verstände, so verstände, daß man es, wenn man tiefer in die Sache geht, etwa Verständnis nennen kann.",
        "Daher ist es aber auch für uns notwendig, daß wir sozusagen unsere Seele erst zubereiten, um diese ganz andersartige Zeit wieder für uns verständlich zu machen.",
        "Wenn man solche Gedanken hegt, dann empfindet man so recht, was im Grunde genommen unsere allerneueste Zeit uns gebracht hat."
      ],
      [
        "Als am letzten Sonntag nach der letzten Szene des «Mysteriums von Eleusis» der Vorhang niederging, mußte ich denken, wie dank­bar wir sein dürfen, daß wir in unserer Gegenwart in der Lage sind, das Auge und die Seele hinrichten zu können auf den Verlauf von"
      ],
      [
        "Vorgängen, welche uns diese griechische Seele in ihrem Fühlen und Erleben zeigen, und außerdem für das Anschauen dieser Vorgänge Seelen im Zuschauerraume zu haben, die sich denken können, daß in der Evolution der Menschheit über die Erde hin die menschliche Seele von Epoche zu Epoche andere Formen angenommen hat, ganz anders die Umgebung und das eigene Leben empfinden gelernt hat.",
        "Wir haben uns die Jahre hindurch bemüht, verstehen zu lernen, wie die menschlichen Seelen im Anbeginn der Erdenentwickelung leben mußten, als die äußere Leiblichkeit und damit das innere Seelenle­ben ein ganz anderes waren als später."
      ],
      [
        "Wir haben uns bemüht verste­hen zu lernen, wie die Menschenseelen lebten in der atlantischen Zeit und in der nachatlantischen Zeit, und haben dadurch die Mög­lichkeit gewonnen zu sagen: Oh, die Menschenseele, wie mannigfal­tig hat sie sich in uns ausgelebt!",
        "Die Seele, die in jedem von uns ist und immer wieder durch Inkarnationen und Inkarnationen hin­durchgegangen ist, nicht um dasselbe zu erleben, sondern um immer wieder und wieder anderes zu erleben - wie mannigfaltig hat sie sich ausgelebt!"
      ],
      [
        "Und so mag es uns denn gelingen, da unten zu sitzen im Zuschauerraum und einmal zu vergessen, was uns in unserer Zeit unmittelbar bewegen muß, und unbefangen und objektiv aufzuneh­men, was die Seelen eben seelisch in ganz anderen Zeiten ihr eigen nannten.",
        "Wir brauchen nicht unseren Verstand in Bewegung zu set­zen, wir brauchen uns nur unserem unmittelbaren Empfinden hin­zugeben, dann zeigt sich uns schon, daß die Vorgänge, die sich da ab­spielen in dem rekonstruierten Mysterium von Eleusis, alles das zwar in sich haben, was die Seelen von den dunkelsten Lebensunter­gründen bis hinauf zu den Geisteslichtern, von den Schmerzen bis zu den Seligkeiten durchlebten, aber dies auf mannigfaltige Art im Laufe der Zeit erlebten."
      ],
      [
        "Und dann erhält man vielleicht ganz naiv und unbefangen - aber dafür vielleicht um so sicherer - ein Gefühl davon, was der Grieche empfand, wenn Namen ausgesprochen wur­den, Vorstellungen angeregt wurden wie Demeter, Persephone, Dionysos.",
        "Man erhält vielleicht die Möglichkeit, daß ganze Welten aus dem Innern der Seele vor uns hintreten, wenn diese Vorstellun­gen in uns angeregt werden."
      ],
      [
        "Als Menschen finden wir uns innerhalb der äußeren physischen Welt.",
        "Wir lernen sie kennen durch unsere Sinne, durch die Erlebnis­se unserer Seele und durch das, was wir mit unserem Verstande und unserer Vernunft erleben können.",
        "In einer ganz bestimmten Weise fühlen wir heute gewissermaßen unabhängig unsere Seele von dem äußeren Leben der uns umgebenden Natur und alles dessen, was sich in der Natur verbirgt.",
        "Wie der Mensch demgegenüber heute empfindet, das drückt sich wieder aus in einer Art, wie die griechi­sche Seele nicht hätte empfinden können.",
        "Das Entfremdetwerden gegenüber der Natur, das Betonen, daß man die Sinneswelt verlassen müsse, um in die spirituellen Welten hinaufzudringen, wäre dem Griechen noch nicht verständlich gewesen.",
        "Aber in seiner Art fühlte er, wie es einen bedeutsamen Unterschied, eine bedeutsame Tren­nung gibt zwischen dem, was man in dem menschlichen Innern nen­nen kann den Geist, und was man nennen kann die Seele.",
        "Das sind ja Worte für das menschliche Erleben, zwei verschiedene Gebiete zunächst und hart aneinanderstoßend: Seelisches und Geistiges."
      ],
      [
        "Richten wir den Blick hin auf die Szene gleich im Beginn der Auf­führung: Demeter, in stolzer geistiger Keuschheit vor Persephone stehend, sie mahnend, nicht zu genießen von den Früchten, die Eros geben kann.",
        "Wir richten das Auge hin auf diese Demeter.",
        "Alles, was der Mensch geistig nennt, wovon er sich sagt, er ist seiner teilhaftig als Geist, das erblickt er in der Demeter.",
        "Aber er erblickt auch, wie innerhalb der Erdenwelt dieses Geistige verbunden ist mit dem Sinn­lichsten, mit dem Materiellsten.",
        "Demeter, die Göttin, die Hervor-bringerin der Feldfrüchte und Vorsteherin der äußeren Einrichtun­gen und sittlichen Ordnungen der Menschheit - als Menschengeist, keusch und stolz gegenüber vielem, was sonst auch im Menschen lebt, aber innig verbunden mit der äußeren Sinneswelt, diese durch­dringend, so steht Demeter vor uns.",
        "Persephone tritt sogleich vor das innere Auge hin als etwas, das uns in unserer Seele wachruft die Vorstellung des menschlich Seelischen, verbunden mit alledem, wo­mit der Mensch in seinem individuellen Dasein dadurch verbunden ist, daß er mit seiner Seele eben in den Erdenleiden und Erdenfreu­den drinnensteht.",
        "Verbunden mit all dem, was die Erdenleiden und"
      ],
      [
        "Erdenfreuden durchzuckt, muß sich die Seele fühlen, wenn sie sich vorstellen will, was in Persephone lebt.",
        "Ganz Seele - Persephone, ganz Menschengeist - Demeter.",
        "Und wenn wir dann den Verlauf des Mysteriums von Eleusis auf uns wirken lassen, wenn die Grund­töne, die gleich beim allerersten Gespräch zwischen Demeter und Persephone angeschlagen werden, weiter in uns klingen und sich verschlingen und sich finden und dann endlich zu der Gestalt des Dionysos herankommen - wie findet sich da der ganze Mensch sel­ber in Dionysos, wie findet sich dasjenige, was in uns lebendig wird gegenüber der Demeter und Persephone, zugleich in Dionysos!",
        "Und wir sehen in der letzten Szene ein Streben der Seele der Menschheit nach Harmonisierung ihres Seelischen mit dem Geistigen: das ganze dionysische Spiel - aus dem Lebensdunkel zum Geisteslicht hinauf!"
      ],
      [
        "Ich kommentiere nicht und möchte nicht ein künstlerisches Werk zerpflücken, ich möchte nur die Empfindungen, die über intime Seelengeheimnisse im Menschen aufgehen können, in Worte brin­gen, wenn sich der Mensch dem Mysterium von Eleusis gegenüber­gestellt sieht.",
        "Niemals wird es mir einfallen zu sagen, in Demeter sei personifiziert oder symbolisiert eine ursprüngliche Form des Men­schengeistes und in Persephone die menschliche Seele.",
        "Das hieße dem Plastischen des Kunstwerkes Gewalt antun, steife Verstandes­begriffe anwenden gegenüber dem, was im Kunstwerke lebt, wie Menschen oder sonstige Wesen selber lebendig leben.",
        "Aber was man empfinden darf, was man empfinden kann über Seelengeheimnisse, das darf man sagen."
      ],
      [
        "Und jetzt stellen wir einmal vor uns hin zwei Bilder.",
        "Stellen wir das spätere europäische Bewußtsein vor unsere Seele hin, das erst jetzt in unserer Gegenwart beginnt sich aufzulösen und lechzen wird nach denjenigen Formen, die ihm in Wahrheit die Theosophie weist, wie es durch die Jahrhunderte gewirkt hat: diese europäische Seele, die Lebensrätsel empfand, wenn ihr vorgestellt wurde, wie der Mensch, der erste Mensch da stand - Mann, Weib - in unendlichem Abstand von seinem Gotte, den er fürchten mußte, hörend die ver­lockende Stimme einer Wesenheit, fremd der eigenen Menschensee­le.",
        "Woher kommt diese Wesenheit?",
        "Was ist sie?",
        "Wie ist sie verwandt"
      ],
      [
        "mit dem eigenen Seelischen?",
        "Kaum denkt die europäische Seele, das europäische Bewußtsein daran, sich darüber aufzuklären.",
        "Sie nimmt hin die Fremdheit des Luzifer, sie begnügt sich damit zu wissen, daß von ihm die Erkenntnis, aber auch die Verführungsstimme ausge­gangen ist.",
        "Und wie tönen dann wie aus Weltenfernen heraus die Worte, die das göttliche Strafgericht verhängt nach der Verführung!",
        "Wie sind sie schon durch ihre Fassung geeignet, die Seele gar nicht dazu aufzurufen, sich zu fragen: Wo lebt das, was da draußen im Makrokosmos durch die Räume klingt, in dem eigensten intimsten Seelenleben?",
        "Man versuche empfindend das, was als der Paradieses­vorgang vorgestellt werden kann, bildlich darzustellen; man versu­che zu empfinden, wie unnatürlich es wäre, die entsprechenden Ge­stalten, mit denen man es dabei zu tun hat, in rein menschlichen Formen darzustellen.",
        "Und jetzt versuche man sich vorzustellen, wie selbstverständlich es ist, daß da, wo von intimsten, tiefsten Seelen­angelegenheiten der Griechen gesprochen wird, die menschliche Ge­stalt der Demeter, die menschliche Gestalt der Persephone, selbst die menschliche Gestalt des Dionysos oder des Zeus vor unseren Augen steht!",
        "Man versuche daraus zu empfinden, wie unendlich nahe der griechischen Seele dasjenige lag, was zugleich durch den Makrokosmos geht!"
      ],
      [
        "Es braucht nur ein Wort ausgesprochen zu werden, um das zu charakterisieren, worum es sich dabei handelt.",
        "Einfach, ganz einfach kann dieses Wort ausgesprochen sein.",
        "Man braucht nur zu sagen: Bevor durch unseren hochverehrten Edouard Schuré das Mysterium von Eleusis nicht rekonstruiert war, so wie wir es jetzt sehen kön­nen, war es eben nicht da.",
        "Und jetzt haben wir es!",
        "Man braucht nur zu empfinden, was in diesen beiden Sätzen liegt, dann ist alles gesagt.",
        "Es handelt sich gegenüber dieser Sache um etwas, was meiner Emp­findung nach alles triviale Aussprechen eines Dankgefühles über­ragt.",
        "Damit ist aber hingewiesen auf die ganze Bedeutung, welche diese Rekonstruktion des Mysteriums von Eleusis für das moderne spirituelle Leben hat.",
        "Dann aber mag sich auch manche Seele geste­hen, daß alles, was mit diesem Mysterium von Eleusis zusammen­hängt und was in bezug auf die historische Wiedererweckung der"
      ],
      [
        "Initiationsprinzipien der verschiedenen Epochen durch denselben Autor geschehen ist, etwas ist, woraufhin bestimmt ist das Tiefste, das Intimste der europäischen Seelennatur.",
        "Und eine Verpflichtung liegt vor, eine Verpflichtung heilig ernster Art für jeden, der es auf­richtig und ernst mit dem spirituellen Leben meint, gerade diese Art hineinzutragen in das moderne Seelenleben."
      ],
      [
        "Meine lieben Freunde!",
        "Sie können viel den Leuten draußen in der Welt sprechen von allerlei theosophischen Dingen; es kann auch sein, daß die Leute von einem solchen Sprechen befriedigt erschei­nen können."
      ],
      [
        "Wenn man aber in die Tiefen der Seelen hineinzublicken vermag, dann weiß man, wessen die Seelen bedürftig sind, wie notwendig es ist, ihnen das zu geben, dessen sie sich vielleicht nicht bewußt sind, was sie aber in ihren tiefsten Herzensgründen wahr­haftig verlangen!",
        "Solche Gefühle waren es, die meine Seele durch­drangen, als wir am letzten Sonntag den Vorhang heruntergehen sahen nach der letzten Szene des «Mysteriums von Eleusis»."
      ],
      [
        "Und wenn man so empfinden möchte dasjenige, was sich abgespielt hat, dann lebt in diesem Empfinden selber so viel, daß man ihm Frucht­barkeit und Wirkenskraft für das Leben zugesteht.",
        "Und wenn wir diese Fruchtbarkeit, diese Wirksamkeit in den letzten Jahren an so manchem sahen, dann dürfen wir auch leicht hinwegkommen über manches andere, was heute nicht hierhergehört, was sich aber hem­mend dieser Fruchtbarkeit, dieser Wirksamkeit entgegenstellt und vielleicht noch mehr entgegenstellen wird, als dies in den verflosse­nen Jahren der Fall war."
      ],
      [
        "Und daß ich selber etwa nicht allein dastehe mit diesem Empfinden, das konnten mich die Wochen lehren, wel­che unseren Münchner Aufführungen vorangingen.",
        "Sie sehen ja in den ersten Tagen, in denen Sie im Beginne unserer Münchner Zeit diesen Mysterienaufführungen gegenüberstehen, eine Anzahl der Freunde von der Bühne herab, und da Sie ja alle wohl diejenigen kennen, die Sie da sehen, so brauche ich, was ich ja wahrhaftig tun würde, hier nicht die Namen aller einzelnen Ihnen anzuführen."
      ],
      [
        "Aber das wohl darf ich sagen: daß wir alle, die wir hier sitzen, war­mes Dankgefühl gegenüber denjenigen empfinden dürfen, die sich wochenlang mit Hingebung - denn das ist notwendig, wenn es auch"
      ],
      [
        "oftmals nicht so aussieht -, mit Hingebung aller ihrer Kräfte wid­men dem Studium und dem Durchdringen der Gestalten, die sie dar­zustellen haben.",
        "Und in allen denen, die Sie selber auf der Bühne sehen, lebt das Bewußtsein, daß sie Diener sind der spirituellen Welt, daß in unserer Zeit die Notwendigkeit besteht, der allgemei­nen Menschenkultur spirituelle Werte zuzuführen, und daß alles versucht werden muß, um diese spirituellen Werte der allgemeinen Menschenkultur zuzuführen."
      ],
      [
        "Verehrung gegenüber den spirituellen Angelegenheiten läßt die Mitspielenden so manches, was die Vorbe­reitungen für die Aufführungen erfordern, gern ertragen.",
        "Das darf einmal gesagt werden aus dem Grunde, weil es ja mit unserer ganzen Sache zusammenhängt und weil wahrhaftig die Anstrengungen zu große sind, als daß gerade nur etwa Ehrgeiz oder Eitelkeit, sich von der Bühne herab betrachten zu lassen, die einzelnen dahin führen würde, sich zu Darstellern der betreffenden Gestalten zu machen."
      ],
      [
        "Mit besonderem Danke müssen wir aber derer gedenken, die sozusa­gen hinter den Kulissen, aber vielleicht viel sichtbarer noch als die einzelnen Darsteller, in opferwilliger, hingebungsvoller Art nun schon seit Jahren ihr Können und ihr Streben - besonders ihr Kön­nen, was noch mehr ist als ihr Streben - in den Dienst gerade dieser Sache stellen.",
        "Wir dürfen es wie eine An inneres Karma gerade unse­rer Bewegung ansehen, daß wir in der Lage sind, eine Persönlichkeit zu haben, welche alles, was das Bühnenbild erfordert in bezug auf -sagen wir Umhüllungen und Kleidungen, in bezug auf die Kostüme der Darsteller, wenn ich dieses triviale, mir abscheulich klingende Wort aus der allgemeinen Bühnensprache gebrauchen will, in einer solchen Weise besorgt, daß es nicht nur den Intentionen, die mir sel­ber am Herzen liegen, entspricht, sondern auch getragen ist von wahrer Spiritualität."
      ],
      [
        "Wir dürfen es als ein günstiges Karma unserer Bewegung innerhalb Mitteleuropas betrachten, eine solche Persön­lichkeit unter uns zu haben.",
        "Und daß dieses Karma tiefer begründet ist, das zeigt sich auch darin, daß dieselbe Persönlichkeit in so ausge­zeichneter Art mitwirken konnte bei allem, was zum Beispiel für unsern «Kalender» in den letzten Monaten hat geschehen können, der ja wie alle unsere Unternehmungen dem großen Ziele dienen"
      ],
      [
        "soll; so daß gewiß in erster Linie bei denjenigen, die nicht nur als Darsteller, sondern auch in dem Ganzen in hervorragender Weise mitwirken, der Name des Fräulein von Eckardtstein genannt werden darf.",
        "Dann darf ich mit innigstem Dankgefühl gedenken und möch­te dieses Dankgefühl in Ihren Herzen mit anregen auch für unsere hingebungsvollen Maler Volckert, Linde, Haß und in diesem Jahre auch Steglich aus Kopenhagen.",
        "Ich möchte es anregen in Ihren Her­zen, weil wahrhaftig etwas dazu gehört, aus den spirituellen Tiefen heraus etwas anzustreben, daß für das Auge äußerlich da ist, was uns vor der Seele steht.",
        "Und viele müssen, weil es zu viele sind, unge­nannt bleiben.",
        "Ja, wenn so ein Bühnenbild dasteht, dann merkt man nicht, daß dafür - vielleicht nur für die letzte Zurichtung außerdem -dasjenige, was der Maler zugerichtet hat in einem Raume, der viel größer ist als dieser Saal hier, ausgespannt sein muß und daß vierzig bis fünfzig Personen auf dem Boden herumkriechen müssen, um überhaupt das alles an Ort und Stelle zu bringen, wohin es gehört.",
        "Eine solche Verpflichtung übernehmen gern unsere Freunde; sie kriechen gern auf dem Boden herum, um alles anzunähen, was ange­näht werden muß, und was dann vielleicht nur für wenige Minuten von der Bühne herab sichtbar erscheint.",
        "Warum sage ich das alles?"
      ],
      [
        "Vielleicht erscheint es manchem höchst unnötig, dies zu sagen.",
        "Theosophie aber besteht nicht bloß in Theorien und Prophetien.",
        "Theosophie besteht in der hingebungsvollen Opferwilligkeit für das, was unsere Zeit von uns fordert, auch dann, wenn wir unmittel­bar selbst diese Forderungen nur dann erfüllen, wenn wir einmal viele Tage lang auf dem Boden herumrutschen müssen, um das in Ordnung zu bringen, was dann in uns sich beleben kann im An­blick, was lebendig sein soll in unserer Seele, damit diese Seele mit den Anforderungen der modernen Zeit fertig werden kann.",
        "Ein Ge­fühl dafür soll erregt werden, daß von wirklicher menschlicher Ar­beit der Kern ausgeht für jenes spirituelle Leben, das der Zukunft der Menschen auch notwendig ist.",
        "Dann, wenn man solches fühlt, wird man auch immer mehr und mehr verstehen, wie zusammen­wachsen müssen die Seelen derer, die sich Theosophen nennen wol­len, in gemeinsamen, ernsten und würdigen Zielen im konkreten"
      ],
      [
        "unmittelbaren Arbeiten.",
        "Denn wert ist vor allen Dingen das, was der einzelne tut, was der einzelne schafft, was der einzelne bereit ist, an Opfern zu bringen!",
        "Und wen ist das, was der einzelne sich er­wirbt an Ertragsamkeit für Enttäuschungen."
      ],
      [
        "Hier an diesem Orte und in unserer mitteleuropäischen geisteswissenschaftlichen Bewe­gung darf es gesagt werden: Es haben diejenigen, deren Karma es ist, ein wenig sozusagen zusammenzuhalten die Fäden, die wir brau­chen für die Bildung des spirituellen Kernes, wahrhaftig in den letz­ten Zeiten nicht wenige Enttäuschungen erlebt.",
        "Aber mag manches Wort über solche Enttäuschungen gefallen sein, eines ist noch nicht gefallen, und wir möchten es erbitten von den spirituellen Mächten, die hinter unserer Bewegung stehen und sie anfeuern, daß dieses Wort nicht zu fallen braucht, ein Wort: daß unsere lieben Mitarbei­ter erlahmen möchten."
      ],
      [
        "Solange sie ihre Hände regen, solange sie ihre Gedanken regen, können wir uns für unsere geistige Bewegung sa­gen: Sie wollen!",
        "Und solange sie wollen werden, gleichgültig, ob sich das Gedeihen auf den ersten Tag zeigt oder erst nach Jahrhun­derten, solange sie wollen werden, solange werden sie im rechten Sinne des Wortes Theosophen sein!"
      ],
      [
        "Fühlen wir uns in diesem Wol­len, das auch Enttäuschungen ertragen kann, in wahrer, arbeitsamer Liebe zusammen, dann werden wir arbeiten können.",
        "Dann wird daraus entspringen dasjenige, was der Menschheit in ihrer gegen­wärtigen Entwickelungsstufe notwendig ist."
      ],
      [
        "Mögen unsere Kräfte schwach sein, wir können keine stärkeren bringen als wir haben.",
        "Eines können wir aber; seit Monaten betonen wir dieses eine, und ich mußte in diesen Tagen dieses einen gedenken.",
        "Es gab Zwischen­tage zwischen unseren Aufführungen; viele unserer Freunde waren vom Morgen bis zum Abend bei den Generalproben beschäftigt."
      ],
      [
        "Unser lieber Dr.",
        "Unger hatte Ihnen in diesen Tagen hier in Mün­chen Vorträge gehalten.",
        "Es war für mich etwas tief Erfreuliches, Beseligendes, als unser lieber Freund, der Direktor Sellin, gestern morgen zu mir kam, voller Begeisterung über diese beiden Vorträge des Dr."
      ],
      [
        "Unger, und mir hinter den Kulissen das Wort sagte: «Eine Bewegung, die solche begeisterte Vertreter vor der Öffentlichkeit hat, geht nicht zugrunde!» Denn worüber darf ich mich selbergestatten"
      ],
      [
        "Sie mir dieses aufrichtige, ehrliche Wort - am allermeisten freuen, wenn gerade so etwas vorkommen kann?",
        "Ich kann mich am meisten freuen über die selbständige Kraft, über die durchaus selb­ständige Art, wie hier eine Menschenpersönlichkeit aus sich heraus, frei, ohne sich unmittelbar nur an dasjenige zu halten, was ich selber aussprechen kann, die Sache aus sich heraus nach ihren eigenen Fä­higkeiten begründet!"
      ],
      [
        "Wer selbst selbständig wirken will, wird nichts freudiger, aufrichtiger begrüßen, als wenn eine selbständige Persön­lichkeit neben ihm Schulter an Schulter steht und dasjenige gibt, was sie zu geben in der Lage ist, nachdem sie erkannt hat, daß es sich zum Ganzen fügen kann.",
        "Eine Festesfreude war es mir, als Direktor Sellin kam und - ich möchte sagen wie aus kindlichem Herzen her­aus, denn es stellte sich so dar - seine volle Begeisterung aussprach über das, was er gehört hatte."
      ],
      [
        "Ich darf es Ihnen sagen und weiß, daß es mir doch eine große Anzahl glauben werden, daß ich die innigste Freude habe über solche Selbständigkeit, über ein solches individuel­les Wirken, und daß dies die Wahrheit ist.",
        "Wenige Zeiten vorher be­kam ich einen Brief, der ungefähr sagte, daß es notwendig wäre, mancherlei zu tun innerhalb der deutschen theosophischen Bewe­gung, weil ja doch sonst niemand zu Worte komme als der, welcher wortgetreu das nachsprechen mag, was ich selbst sage."
      ],
      [
        "So ist oftmals die Darstellung draußen in der Welt von dem, was die Wahrheit ist!",
        "Nicht Kritik soll geübt werden an einem solchen Wort, das objektiv eine Unrichtigkeit im straffsten Sinne des Wortes enthält, auch nicht ein Tadel oder eine Strafe soll darin liegen."
      ],
      [
        "Man kann nur Mit­leid haben mit einem solchen Wort.",
        "Aber das andere, was für uns positiv sein kann, muß immer wieder und wieder betont werden: Fühlen wir uns verpflichtet zur Wahrhaftigkeit, zur Prüfung dessen, was ist!"
      ],
      [
        "Und fühlen wir es uns verboten, über irgend etwas zu spre­chen, bevor wir es kennengelernt haben, bevor wir auf dasselbe ein­gegangen sind!",
        "Sonst gibt es keinen Segen in einer okkulten Ent­wickelung, in einer okkulten Bestrebung."
      ],
      [
        "Wahrheit und Wahrhaf­tigkeit - das ist oberstes Gesetz.",
        "Was nützen alle Prophetien, was nützen alle Charakteristiken übersinnlicher Tatsachen, wenn sie nicht getaucht sind in das Bad ehrlichster, aufrichtigster Wahrhaftigkeit!"
      ],
      [
        "Sie mögen manches von dem Orte, von dem ich zu Ihnen spre­chen darf, an diesen oder jenen geisteswissenschaftlichen Wahrhei­ten entgegennehmen; am allerliebsten ist es mir aber, wenn Sie hier dieses Wort entgegennehmen, daß es mein eigenstes, innerstes Be­streben Ihnen gegenüber immer sein wird, über nichts zu sprechen, als worüber ich sprechen darf im Sinne ehrlichster Wahrhaftigkeit, und daß ich den Segen einer okkulten Bewegung in nichts anderem sehen kann als in dem Sich-Verpflichtetfühlen zur Wahrhaftigkeit!",
        "Mag es unseren Wünschen zuwider sein, mag es entgegen sein dem, was unser Ehrgeiz, unsere Eitelkeit verlangen, mag es manchem in unserer Seele zuwider sein, mag es uns zuwider sein, irgendeiner Autorität uns zu unterwerfen - das kann richtig sein."
      ],
      [
        "Einer Autori­tät sollen wir uns freiwillig und willig unterwerfen: der Autorität der Wahrhaftigkeit, so daß alles, was wir leisten können - nicht nur in dem, was wir sagen, sondern auch in dem, was wir tun, was wir im einzelnen tun - durchdrungen sei von Wahrhaftigkeit.",
        "Das suchen Sie auch in dem, was wir in unseren theosophisch-künstleri-schen Bestrebungen vor Ihre Augen stellten."
      ],
      [
        "Versuchen Sie es zu fin­den, und vielleicht werden Sie sehen, daß wir auch manches nicht er­reichten, aber eines werden Sie sehen: daß es unser Bestreben ist, das, was wir tun, zu tauchen in die Sphäre und in die Atmosphäre der Wahrhaftigkeit, daß wir es uns verbieten, von Toleranz zu spre­chen, wenn diese Toleranz nicht auch wahrhaftig da ist, wenn wir sie nicht auch wahrhaftig üben.",
        "Denn das, daß man den andern into­lerant nennt, macht die Toleranz nicht aus; daß man etwas anderes von jemandem erzählt, als er vertritt, das macht die Toleranz nicht aus; daß man immer betont, man sei tolerant, das macht die Tole­ranz nicht aus."
      ],
      [
        "Wenn man aber wahrhaftig ist, dann kennt man sei­nen Wert, dann weiß man auch, wie weit man gehen darf.",
        "Und ist man ein Diener der Wahrhaftigkeit, dann ist man selbstverständlich tolerant."
      ],
      [
        "In einleitender Weise durften wohl auch solche Worte gespro­chen werden, obwohl es sonst nicht meine Art ist, auf allerlei Mah­nungen und Ermahnungen einzugehen.",
        "Aber wie sollten denn nicht gerade bei einer solchen Gelegenheit diese Worte sich dem Herzen"
      ],
      [
        "loslösen, die aufmerksam machen möchten, wie wir aus innig ver­wandtem Impuls heraus in der Lage waren, diese Rekonstruktion des Mysteriums von Eleusis in gewisser Beziehung immer wieder und wieder zu etwas zu machen, woran wir anknüpfen.",
        "Wir wollten zu den europäischen Seelen ehrlich und aufrichtig, wahrhaftig sein und wollten im Sinne der Wahrhaftigkeit suchen, wonach die euro­päische Seele lechzt."
      ],
      [
        "Was oftmals das Tiefste ist, erkundet sich zu­letzt in den einfachsten Worten, formuliert sich zuletzt in den ein­fachsten Worten.",
        "Lernen wir aus ehrlicher, aufrichtiger Überzeu­gung von dem, was der Zeit not tut, erkennen, was es für eine Tat war, aus den dunklen Geistestiefen heraus, die gerade dann begin­nen, wenn wir vom Römertum ins Griechentum kommen, dieses Mysterium von Eleusis wiederzuerschaffen."
      ],
      [
        "Fühlen wir, was es heißt: Bevor das Mysterium von Eleusis durch unsern hochverehr­ten Edouard Schuré nicht geschaffen war, war es nicht da, und jetzt ist es da!",
        "Wir haben es und dürfen auf es bauen, und damit auf die alleinige Art, wie wahrhaftiges Griechentum vor unsere Seele hin­treten kann, daß sie darauf hinschauen kann."
      ],
      [
        "Wenn wir das empfin­den, fühlen wir die Bedeutung dessen - womit wir diese unsere Münchner Unternehmungen eröffnen dürfen - in diesem Jahre wie im vorigen.",
        "Dann dürfen wir es jeder einzelnen hier befindlichen Seele überlassen, mit welcher Herzlichkeit - von der ich sicher bin, daß sie bei vielen eine innige sein wird - sie der Gedanke erfüllt, daß der Schöpfer dieser Rekonstruktion des Mysteriums von Eleusis unter uns gerade während dieser Münchner Zeit weilt."
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ZWEITER VORTRAG München, 26. August 1912",
    "paragraphs": [
      "Wir werden in diesem kurzen Vortragszyklus wichtige Angelegenheiten des geistigen Lebens zu besprechen haben, Angelegenheiten, die dieses geistige Leben im umfassendsten Sinne berühren. Wir werden zu sprechen haben über dasjenige, was zugrunde liegt der sogenannten Initiation oder Einweihung, und - nachdem wir auf einige Geheimnisse und Gesetze dieser Initiation werden hingedeutet haben - von der Bedeutung dessen, was ausstrahlt im Laufe der Menschheitsentwickelung für das Leben von der Initiation und von den Initiierten. Wir werden von allem, was da ausstrahlt, zu sprechen haben mit Bezug auf dasjenige, was man in die einander so entgegengesetzten Vorstellungen zusammenfassen kann: Ewigkeit und Augenblick, Geisteslicht und Lebensdunkel. Nachdem wir unter dem Gesichtspunkt, den uns diese Vorstellungen liefern werden, gewissermaßen das` Leben des Menschen werden betrachtet haben, soll dann wieder zurückgekommen werden auf die Kraft der Initiation und auf die Kraft der Initiierten. Begrenzen also soll diesmal diese Betrachtungen das Prinzip der Initiation.",
      "Ewigkeit - wir brauchen die Vorstellung nur anzuschlagen, und wir fühlen es, es klingt etwas in uns, was zusammenhängt mit den tiefsten Sehnsuchten der menschlichen Seele, mit dem Höchsten, das unter seinen Strebenszielen der Mensch benennen kann. Augenblick - ein Wort, das uns immer wieder hindeutet auf dasjenige, in dem wir eigentlich leben, und auf die Notwendigkeit, in diesem Augenblick, in dem wir leben, dasjenige aufzusuchen, was uns den Ausblick geben kann in das Land der Sehnsucht, in die Ewigkeit.",
      "Man braucht sich nur zu erinnern, daß das tiefste Geheimnis seiner größten Dichtung Goethe in seinen «Faust» so hineingelegt hat, daß er den Faust gegenüber dem Augenblicke aussprechen läßt: «Verweile doch! du bist so schön!» und sich dann gestehen läßt: Wenn das Gesinnung der Seele werden kann, wenn es möglich ist, daß sich die Seele identifizieren könnte mit einem Geständnis, zum Augenblicke",
      "zu sagen: «Verweile doch! du bist so schön!», dann müßte sogleich das Geständnis für Faust folgen, daß er würdig wäre, dem Gegner des Erdenmenschentums, dem Mephistopheles, zu verfallen. Was mit der Empfindung, die aus dem Augenblicke quillt, zusammenhängt, hat ja Goethe zum eigentlichen Grundgeheimnis seiner größten Dichtung gemacht. So scheint es, als ob dasjenige, in dem wir leben, der Augenblick, ganz entgegengesetzt wäre dem, was wir als Ewigkeit bezeichnen und wonach die Menschenseele immer wieder und wieder lechzen muß, sich sehnen muß.",
      "Geisteslicht - soviel wir theosophische Betrachtungen angestellt haben im Laufe der Jahre, wir haben erkannt, daß das Bestreben nach dem Geisteslicht überall das zugrunde liegend hat: den Menschen hinauszuführen aus dem Lebensdunkel. Und wieder können wir etwas aus einer der größten Dichtungen der Menschheitsentwickelung, aus dem «Faust» heraus fühlen: wie ein Dichter, wenn er eine große, in sich umfassende Seele schildern will, nicht umhin kann, sie auch herauskommen zu lassen aus dem Lebensdunkel. - Denn, was umwebt Faust im Beginne der Dichtung? Worin ist er ganz verstrickt? Im Lebensdunkel! Und wie oft mußten wir es betonen, daß dieses Lebensdunkel für den Menschen eine so große Kraft und Gewalt hat, daß das Geisteslicht, wenn es ihn in unreifem Zustande trifft, auf ihn so wirken kann, daß es ihn nicht erhellt, daß es ihn blendet, daß es ihn betäubt. So kann es sich nicht nur darum handeln: Wie geht der Weg zum Geisteslicht, wo ist er zu finden? - sondern vor allem muß es sich darum handeln: Wie muß der Mensch den Weg der Seele wandeln, der ihn in richtiger Weise zum Geisteslicht führen kann? - Damit sind nur die Linien gezeichnet, die uns in diesen Vorträgen beschäftigen sollen, und wir stehen ja in einer solchen Phase unserer theosophischen Arbeit, daß wir nicht vom Anbeginn an die Dinge zu entwickeln brauchen, sondern vielfach an Bekanntes anknüpfen können.",
      "Wenn das Wort Initiation, das sich uns so innig verbündet hat mit den Worten Ewigkeit und Geisteslicht, an uns herandringt, dann werden in der Seele lebendig alle die großen Menschen, welche wir im Laufe der Menschheitsepochen als die Initiierten kennen.",
      "Und mit ihnen werden auch diese Menschheitsepochen selber in unserer Seele erweckt, wie sie abgelaufen sind, wie die Menschen in ihnen lebten und wie das Licht aus den Initiationsstätten und von den Initiierten zu den Menschen strömte, um eigentlich das erst möglich zu machen, was die Impulse, die eigentlich treibenden Kräfte der Menschheitsentwickelung zu allen Zeiten gewesen sind. Es würde viel zu weit führen, bei Gelegenheit einer solchen Besprechung immer zurückzuweisen in ausführlicher Weise auf das, was innerhalb der Erdenentwickelung geschehen ist, bevor jene so oft besprochene atlantische Katastrophe über die Erde hereingebrochen ist, welche das Antlitz unserer Erde vollständig verändert hat. Wir bekommen schon eine hinlängliche und ausreichende Vorstellung von dem, was da in Betracht kommt, wenn wir die nachatlantischen Zeiten ins Auge fassen und uns an die eigentümliche Konfiguration des Menschen erinnern, wie sie so verschiedenartig sich ausgeprägt hat im Folgelauf der Zeit.",
      "Wir lassen unsern Blick zurückschweifen auf die tonangebende Kultur, wie sie sich angeschlossen hat, unmittelbar nachdem das Antlitz der Erde neugestaltet war durch die atlantische Katastrophe, und wir haben so oft mit Ehrfurcht zurückgewiesen auf dasjenige, was damals in der ersten Epoche der nachatlantischen Zeit die großen heiligen Lehrer der Menschheit gebracht haben an derjenigen Erdenstätte, an der später die indische Kultur sich entwickelt hat. Wir haben darauf aufmerksam gemacht, wie nur von unten nach oben aufschauen kann die Seele zu den hehren spirituellen Lehren, die damals durch Menschen-Individualitäten in die Welt gekommen sind, welche noch alle innere Größe in sich trugen derjenigen Menschen, die in der atlantischen Zeit den unmittelbaren Zusammenhang mit den göttlichen, mit den spirituellen Welten gehabt haben, wie das in den späteren Epochen der Menschheit nicht mehr möglich gewesen ist. Wir haben darauf hingewiesen, wie das Erbe der heute nur noch für den Okkultisten zu erreichenden atlantischen Weisheit in der nachatlantischen Form in den uralt heiligen Lehrern der ersten nachatlantischen Kulturperiode gelebt hat, und wir haben darauf hingewiesen, wie das, was damals gelebt hat, wovon es keine",
      "Aufzeichnungen gibt außer in dem, was wir die Akasha-Chronik nennen, für den Menschen hinlänglich groß und bedeutend erscheint, wenn ihm die Nachklänge davon entgegenleuchten in der indischen oder überhaupt in der orientalischen Literatur. Die Höhe der Moralität, die Höhe der Spiritualität, die in diesen Schriften als der Nachklang uralter geistiger Lehren enthalten ist, können der gegenwärtigen Menschheit gar nicht einmal - insofern von äußerer Bildung gesprochen wird - voll zum Bewußtsein kommen.",
      "Am wenigsten kann das in denjenigen Ländern sein, welche vorbereitet worden sind zu ihrer gegenwärtigen äußeren Kultur durch das, was das Christentum in seinen verschiedenen Formen im Laufe der letzten Jahrhunderte hat leisten können. So fühlte sich die Seele von unten nach oben gerichtet, wenn sie zu all dem Großen, heute nur zu Erahnenden hinaufblickte, das selbst nur noch als ein Nachklang dieser uralten Spiritualität zu uns gekommen ist.",
      "Wenn man die Sache so ansieht und sich vor allem dessen bewußt ist, was hier oft erwähnt worden ist, daß die Menschheit erst wieder in der siebenten, in der letzten Epoche der nachatlantischen Zeit - wir stehen jetzt in der fünften - dazu gelangen wird, aus dem Lebensdunkel heraufzuholen das Verständnis für das, was einmal am Ausgangspunkte der nachatlantischen Zeit gelebt hat und die Impulse gegeben hat für die menschheitliche Entwickelung, und wenn man bedenkt, daß die Menschheit wird heranreifen müssen bis zur letzten Epoche, um das in sich wieder zu fühlen und zu erleben, was damals erlebt und gefühlt worden ist, dann bekommt man aber auch ein Gefühl und eine Empfindung dafür, wie hoch das Prinzip der Initiation gewesen sein muß, welche die Impulse gegeben hat zu dieser uralt heiligen spirituellen Kultur der Menschheit. Und dann sehen wir, wie Im Laufe der folgenden Epochen die Menschheit - ringend nach anderen geistigen Schätzen, nach anderen Schätzen des Erdendaseins - gleichsam immer weiter und weiter heruntersteigt, wie sie andere Formen annimmt, wie aber je nachdem, was die Zeiten fordern, die großen Initiierten aus der geistigen Welt heraus der Menschheit geben, was sie für ihre Kultur als Impulse für eine bestimmte Epoche nötig hat.",
      "Wir sehen dann vor unserem Blick auftauchen die Zarathustra",
      "Kultur, die ganz andersartig ist, wenn wir sie in ihrem wahren Lichte betrachten, als die Kultur der heiligen Rishis; dann die ägyptischchaldäische Kultur; dann das, was in Griechenland die uralt heiligen Mysterien waren, wovon wir gestern in einem ganz anderen Sinne noch gesprochen haben, sehen überall hereinleuchten das Geisteslicht in das Lebensdunkel, wie es für die verschiedenen Zeiten notwendig ist.",
      "Wenn wir uns jetzt einmal am Ausgange unserer Betrachtungen fragen: Welche Vorstellungen können wir uns von einem Initiierten bilden - es ist ja selbstverständlich, daß von einem so umfassenden Begriff namentlich im Beginne des Vortragszyklus zunächst nur Annäherungsbegriffe gegeben werden können, wir werden dann immer tiefer und tiefer in das Wesen der Initiation eindringen können -, so wird es zunächst notwendig sein, daß wir mancherlei von dem zusammennehmen, was wir bereits auf theosophischem Felde gehört haben. Machen wir uns klar, daß zur völligen Initiation notwendig ist, daß der Mensch innerhalb seines physischen Leibes die Welt nicht so betrachtet, daß er durch seine Augen und die anderen Sinnesorgane die Welt um sich herum wahrnimmt oder durch seinen an das Gehirn gebundenen Verstand und durch das, was er seinen Orientierungssinn nennen kann, diese Welt oder irgendeine Welt, die ihn umgibt, sieht.",
      "Daß der Mensch sich auch nicht über diese Welten, wie es gewöhnlich der Fall ist, seine Begriffe bildet, sondern daß er in die Lage gekommen ist, durch das, was man nennen kann «außerhalb seines physischen Leibes Welten wahrzunehmen», in seinem Seelensein etwas zu haben, was ein übersinnlicher, ein geistiger Leib genannt werden mag, der in sich solche Wahrnehmungsorgane - aber höherer Art - hat, wie der physische Leib die Augen, die Ohren und die übrigen Wahrnehmungs- und Verstandesorgane hat. Welten sehen, ohne sich der Organe des physischen Leibes zu bedienen, das ist das, was man als eine zunächst nicht vielsagende, aber in ihrer Trockenheit zutreffende Definition des Initiierten geben kann.",
      "Und die großen Initiierten, welche die bedeutsamen Kulturimpulse im Folgelauf der Zeiten den Menschen gegeben haben, sie haben diese Unabhängigkeit vom Sinnenleibe und dieses Gebrauchen eines ganz",
      "anderen Leibes eben in einem höchsten Maße erreicht. Ich möchte nicht in Abstraktionen viel sprechen, ich möchte möglichst auch zur Exemplifizierung Konkretes anführen, möchte also heute als ein Beispiel für ein solches Leben außerhalb des Sinnenleibes in einer höheren, der Seele zugehörigen Organisation das Folgende anführen.",
      "Wenn derjenige, der auch nur einige Schritte auf dem Wege zur Initiation gemacht hat, sich durch Selbstbesinnung klarmacht, was er eigentlich in sich und an sich erlebt, so kann er sich etwa das Folgende sagen: Zu dem ersten, was ich an mir erfahre, gehört, daß ich außer meinem sinnlichen, fleischlichen Leibe in mir habe einen feineren, nennen wir ihn ätherischen Leib, den wir so mit uns herum- tragen, wie wir den physischen Leib im Erdensein herumtragen. Wer die ersten Schritte zur Initiation hinauf macht, erlebt das zunächst so, daß er sich darin erfühlt, daß er dieses Erfühlen wahrnimmt, wie er auf anderer Stufe fühlt, was in seinem Blutsystem, in seinem Nervensystem lebt, oder was ersteht auf dem Boden seines Muskelsystems.",
      "Dieses innere Fühlen und Erleben ist ja da und das kann auch für den ätherischen Leib da sein. Insbesondere ist es dann nützlich für den Menschen, der auf den ersten Schritten zur Initiation ist, den besonderen Unterschied oder, man könnte auch sagen, die Beziehung zwischen dem Sich-Erfühlen, dem Sich-Erleben in dem elementarischen oder ätherischen Leibe und in dem physischen Leibe kennenzulernen.",
      "Man erlebt sich also in dem elementarischen Leibe, wie man weiß, daß man sein Blut, seinen Herzschlag oder seinen Pulsschlag in sich hat. Um sich das klarzumachen, kann man diesen elementarischen Leib in Zusammenhang betrachten mit dem physischen Leibe, in den man ja mehr hineingewöhnt ist als in das, was man sich erst erringt auf dieser geistigen Wanderschaft.",
      "Man kann sich sagen: In dem elementarischen Leibe hast du einen Teil, der entspricht dem physischen Gehirn, alledem, was deinen Kopf ausmacht. Der Kopf, das Gehirn ist gleichsam herauskristallisiert aus dem ätherischen Leibe und in demselben so darin, daß man es vergleichen könnte mit einer Wassermenge und einem Stück Eis, das darin schwimmt, wenn man das Wasser mit dem ätherischen Leibe vergleichen wollte und das Eis mit dem aus dem ätherischen",
      "Leibe herauskristallisierten physischen Leibe. Aber man fühlt, man erlebt, daß ein inniger Zusammenhang ist zwischen dem, was man den Ätherteil des Kopfes oder des Gehirns nennen kann, und dem physischen Kopfe selber. Man weiß dann, wie man seine Gedanken schafft, wie man seine Erinnerungsbilder bildet innerhalb des ätherischen Leibes und wie das physische Gehirn nur gleichsam ein Spiegelungsapparat ist, weiß aber auch, wie das Gehirn eng zusammenhängend ist mit dem ätherischen Leibe. Insbesondere kann man das",
      "dann erleben, wenn man sich recht stark beschäftigen muß mit Anstrengungen, die zusammenhängen mit dem physischen Plan, mit dem physischen Sein, wenn man viel nachdenken muß über die Dinge> wenn man also seinen physischen Leib anstrengen muß, daß er heraufholt aus den Tiefen des Lebens die Erinnerungsvorstellungen, um sie zusammenzuhalten. An einem solchen Vorgange ist im- mer zunächst, gleichgültig, ob man es weiß oder nicht, der ätherische Leib beteiligt.",
      "Aber es ist das physische Gehirn innig damit verbunden, und wenn man das physische Gehirn ermüdet, merkt man sehr, sehr die Ermüdung des Gehirns in dem betreffenden Ätherteile. Man merkt dann, daß man in dem, was man als elementarischen Gehirnteil erlebt, etwas wie einen Klotz, wie einen Fremdkörper hat, daß man nicht mehr herankann an das, woran man herankommen muß, denn die Beweglichkeit im physischen Gehirn ist etwas, was parallel gehen muß der Beweglichkeit im ätherischen Leibe.",
      "Man kann dann das deutliche Gefühl haben: Dein Ätherleib ermüdet auch nicht, er könnte bis in alle Ewigkeit fort die Gedankenbilder zusammenschließen und heraufholen dasjenige, was du weißt; aber um es in der physischen Welt zum Ausdruck zu bringen, muß es sich spiegeln, und da versagt das Gehirn. - Der elementarische Leib ermüdet nicht. Gerade weil er immerfort tätig sein kann, verspürt er die Ermüdung des Gehirns um so mehr.",
      "Man merkt gleichsam, was da das Gehirn an versagenden Kräften produziert. Und wenn es einschläft und in die Dumpfheit der Ermüdung verfällt,",
      "kann man sich sagen: Jetzt mußt du aufhören, sonst würdest du dich krank machen. - Man kann nicht den Ätherleib abnutzen. Aber auf dem Umwege, daß man dem Gehirn übermäßige Dinge zumutet,",
      "kann man fortfahren, es noch weiter zu ermüden und es so in einen lebenversagenden, toten Zustand bringen. Und das verträgt ein lebendiger Organismus nicht, daß etwas, was mit ihm in einem normalen Zusammenhange sein soll, partiell tot ist, daß es in einen abnormen Zustand kommt. Also man muß sich aus einem freien Entschluß sagen: Damit du nicht etwa abtötest einen Teil deines Gehirns, der dann von sich aus weiterfrißt, mußt du aufhören, wenn du dein Gehirn als ein Stück Fremdkörper in dir selbst empfindest.",
      "So ist das Erleben, wenn man das Verhältnis aufsucht zwischen demjenigen, was im menschlichen elementarischen oder ätherischen Leibe entspricht dem Gehirn oder dem Kopfe, und dem physischen Gehirn oder physischen Kopfe selber. Da ist ein inniger Zusammenhang. Es verläuft das äußere Sinnensein in der Tat so, daß es unmöglich ist, den Parallelismus zwischen beiden in übergroßem Maße zu durchbrechen. Man möchte sagen, wenn man dieses Verhältnis ausdrücken will: In unserm Kopfe, namentlich in unserm Gehirn haben wir einen recht treuen Ausdruck der Ätherkräfte, haben wir etwas, was in seiner äußeren Erscheinung und in seinen äußeren Funktionen wirklich ein treues Abbild ist der Funktionen und der Vorgänge in dem entsprechenden Ätherteil.",
      "Anders ist das für andere Organe des menschlichen elementarischen oder ätherischen Leibes und die entsprechenden physisch- sinnlichen Organe. Da sind die Dinge ganz anders. Ich will ein Beispiel anführen. Nehmen wir einmal die Hände. Geradeso wie dem Kopf oder dem Gehirn ein Ätherteil, ein elementarischer Teil in dem elementarischen Leibe entspricht, so entsprechen auch den Händen elementarische, ätherische Vorgänge des menschlichen Ätherleibes. Aber zwischen den äußeren physischen Händen und ihren Aufgaben und dem, was eigentlich dem zugrunde liegt in dem entsprechenden elementarischen oder ätherischen Teil, ist ein viel größerer Unterschied als zwischen dem physischen Kopfe und dem entsprechenden Teile in dem menschlichen elementarischen Leibe. Was die Hände tun, ist viel mehr bloß in der Sinneswelt verlaufend, ist viel mehr bloß eine sinnliche Verrichtung, und was die dazugehörigen elementarischen oder ätherischen Organe tun, findet nur zum",
      "allergeringsten Teile in dem, was physisch in den Händen zum Ausdruck kommt, seine Offenbarung. Ich muß, wie man das oftmals muß, um die entsprechenden Tatsachen zu charakterisieren, allerdings Dinge sagen, die für ein physisches Empfinden und für ein In- Worte-Fassen von physischen Beobachtungen grotesk und paradox erscheinen, die aber doch dem Tatbestand, der hier zugrunde liegt, völlig entsprechen und die jeder, der etwas über die Dinge weiß, unmittelbar so empfinden wird, wie ich es auszusprechen habe.",
      "Den physischen Händen entsprechen elementarische Teile. Aber abgesehen davon, daß in den Händen, in den Bewegungen das zum Ausdruck kommt, was dem elementarischen Teile entspricht, sind diese ätherischen Organe innerhalb des Ätherleibes wahrhaftige Geistorgane.",
      "Ein höheres, viel intuitiveres, geistigeres Tun wird verrichtet in den Organen, die in den Händen und ihren Funktionen zum Ausdruck kommen, als durch das Äthergehirn. Wer auf diesem Gebiete Fortschritte gemacht hat, wird sagen: Ja, das Gehirn, auch das ätherisch zugrunde liegende, ist eigentlich das ungeschickteste geistige Organ, das der Mensch an sich trägt.",
      "Denn sobald man sich betätigt in dem elementarischen Teile des Gehirns, hat man verhältnismäßig sehr bald diesen Fremdkörper des Gehirns zu spüren. Diejenigen geistigen Verrichtungen aber, die gebunden sind an die Organe, die den Händen zugrunde liegen und einen unvollkommenen Ausdruck in den Händen und ihren Funktionen gewinnen, dienen zu weit höherem, geistigerem Erkennen und Beobachten; diese Organe führen schon in übersinnliche Welten und können sich beschäftigen mit der Wahrnehmung und mit der Orientierung in den übersinnlichen Welten.",
      "Drückt man als geistiger Schauer einen solchen Tatbestand aus, so muß man - etwas paradox, aber eben zutreffend - sagen: Das menschliche Gehirn ist das ungeschickteste Organ als Forschungsorgan für die geistige Welt, und die Hände - was ihnen geistig zugrunde liegt - sind viel interessantere, viel bedeutungsvollere Organe für die Erkenntnis dieser Welt, vor allen Dingen viel geschicktere Organe als das Gehirn. Auf dem Wege zur Initiation lernt man gar nicht sonderlich viel, wenn man von dem Gebrauch des Gehirnes zum freien Gebrauch des elementarischen Gehirnes",
      "vordringt. Der Unterschied ist nicht besonders groß zwischen dem, was man erreicht durch ein geläutertes intuitives Gehirndenken und durch ein reguläres geistiges Erarbeiten in dem elementarischen geistigen Ebenbild des Gehirns.",
      "Aber ins Große wächst der Unterschied zwischen dem, was in der Welt die Hände verrichten, und dem, was mit demjenigen elementarischen Teile zu verrichten ist, der ebenso geistig zugrunde liegt den Händen wie das ätherische Gehirn dem physischen. Und nicht viel braucht man auszubilden auf dem Wege zur Initiation in bezug auf das, was dem Gehirn entspricht, denn das ist kein besonders wichtiges Organ.",
      "Aber was den Händen zugrunde liegt, das hängt zusammen - wie Sie es beschrieben finden in «Wie erlangt man Erkenntnisse der höheren Welten?» - mit der Tätigkeit der Lotosblume in der Herzgegend, die aber dann ihre Kraftstrahlen so ausstrahlt, daß sie die Organisation bilden, welche in unvollkommener Weise auf der Stufe, auf welcher der Mensch als physischer Mensch steht, in den Händen und ihren Funktionen dasteht. Wenn man zu einer solchen Sache aufrückt und sich eine Vorstellung machen kann von dem großen Unterschied, der besteht zwischen dem bloßen Gebrauch der physischen Hände und demjenigen, was man sich erarbeitet in bezug auf eine Übersinnliche Welt durch die viel geschickteren elementarischen Organe, welche den Händen zugrunde liegen, als es die elementarischen Organe des Gehirnes sind, dann bekommt man einen lebendigen Begriff von dem Sich-Hineinleben in die Initiation, von dem Reicherwerden des Menschen.",
      "Man wird nicht dadurch erheblich reicher, daß man fühlt: Dein Hirn will ausstrahlen und fühlen den Ätherteil des Gehirns. Das ist der Fall, aber es ist nicht das eigentlich tonangebende, bedeutsame Erleben.",
      "Das bedeutsame Erleben beginnt damit, daß man auch andere Partien sich ausdehnen und einen Zusammenhang mit der Welt sich erschaffen fühlt. Und wenn das auch paradox ist, so ist es doch so, daß man sagen kann: Das ungeschickteste Organ zum geistigen Forschen ist das Gehirn, denn es ist das am wenigsten ausbildungsfähige.",
      "Dagegen eröffnen sich ganz andere Perspektiven, wenn man die anderen scheinbar untergeordneten Organe berücksichtigt.",
      "So findet eine völlige Umwandlung mit dem statt, was der Mensch in sich erlebt, wenn er aufsteigt die ersten Schritte hinauf zu den Höhen der Initiation, und notwendig ist es, daß man sich zum Bewußtsein bringt, daß man dieses als innere Umwandlung der menschlichen Persönlichkeit so erfaßt, wie sonst auch das Prinzip der Entwickelung in der Welt ist, so daß das eine in das andere übergeht und man - wenn es vielleicht auch nicht ganz sachgemäß ist - das Spätere das Vollkommenere gegenüber dem Früheren nennt. Wenn man an dem Gang der Entwickelung sich klarmacht, wie das eine ins andere sich verwandelt, wie der Keim der Pflanze sich umwandelt und zu Blättern, Blüte und Frucht wird, dann kann man sich sagen: Die menschliche Persönlichkeit findet auch so etwas, was sie ist und was sie werden kann, durch die Mittel, die angegeben sind in «Wie erlangt man Erkenntnisse der höheren Welten?» und die die ersten Anfänge zu dem sind, was dann auch in die höchsten Regionen der Initiation hinaufführt.",
      "Es ist gut - und Sie werden sehen, daß es gut ist -, sich so eine lebendige Vorstellung davon hervorzurufen, wie die Menschen, die im Spirituellen Führer sein sollen im Folgelauf der Zeiten, sich innerlich umwandeln, wie das, was erst veranlagt ist im Menschen und sich so unvollkommen zeigt wie die Hände gegenüber den anderen Organen, sich verwandelt, was der Mensch äußerlich nicht bemerkt; dafür wird er aber innerlich um so bedeutungsvoller ein anderer. Daß so in der Welt etwas enthalten ist, wie es vorhanden ist für den, der etwa blind ist und nicht sehen kann, was man sonst mit den Augen sieht, was erst in Erscheinung tritt, wenn das Auge da ist, so ist die Welt des Spirituellen um uns herum vorhanden.",
      "Aber wir müssen ihr entgegenbringen, was wir selbst ihr entgegenbringen können, damit uns das entgegenkommt, was spirituell in der Welt enthalten ist.",
      "Innerhalb der verschiedenen Menschheitsepochen muß nun ein- strömen in den Gang der Entwickelung als Impulse das, was so gegeben werden kann durch ein Sich-Hineinleben in die geistigen Welten. Das lag immer dem zugrunde, was von den Mysterien, von den Initiationsstätten ausgegangen ist. Man stellt sich richtig den Gang der Menschheitsentwickelung vor, wenn man sich hinter dem, was",
      "äußerlich wahrnehmbar ist, als die eigentlich treibenden Kräfte und Individualitäten die großen Initiierten vorstellt. Wie der Zusammenhang ist zwischen dem, was diese großen Initiierten zu tun haben, und dem, was dann äußerlich in der Welt geschieht, das ist vielfach erst durch Theosophie oder Okkultismus überhaupt durchschaubar. Für das äußere, rein geschichtliche, rein gelehrte Erkennen ist es so, daß man eigentlich nur sieht: Da verläuft die Menschheitsgeschichte, da verläuft die Menschheitsentwickelung. Aber man sieht nicht die treibenden Kräfte, die dahinter sind. So verfolgt man in der äußeren Geschichte wie eine Kette von Erscheinungen, bei der sich Glied an Glied anreiht, was äußerlich aufeinander folgt. Daß aber an einer gewissen Stelle der Kette Einschläge aus einer ganz anderen Welt kommen, auf dem Umwege der Initiation kommen, das ist das, was wir - aus Gründen, die auch schon erörtert worden sind - durch die theosophische Erkenntnis in uns aufnehmen können. So erblicken wir theosophisch gerade das Innerlichste in dem Folgelauf der Zeiten, dasjenige, was dann doch auch für die ganze Signatur, für den ganzen Charakter der Entwickelung am meisten zugrunde liegt. So empfinden wir die Religionen, die Vielgestaltigkeit der religiösen Entwickelung als einen Ausfluß der Initiierten, empfinden, wie die Impulse aus den Initiations- und Mysterienstätten herausfließend in das allgemeine Leben der Menschheit übergehen.",
      "Wer die Entwickelung der Menschheit so betrachtet, der kommt ganz selbstverständlich - und beim wahren Okkultismus war das immer der Fall - nicht zu einer irgendwie gearteten, von vornherein angenommenen Bevorzugung der einen Religion vor der anderen. Es gehört zu den allerersten Erfordernissen der Initiation, alle jene Vorurteile, alle jene Vorempfindungen und Vorgefühle abzustreifen, welche in der Menschenseele dadurch erwachsen, daß sie in irgendein Religionssystem, in irgendeine Religionsgemeinschaft hineininkarniert ist. Sorgfältig muß die Selbsterziehung darüber wachen, daß nichts mehr in der Seele sitzt, was der einen Religion den Vorzug geben könnte vor der anderen. Mit völliger Unbefangenheit muß gegenübergestanden werden dem, was Inhalt der verschiedenen Religionen ist, die im Laufe der Menschheitsentwickelung durch die",
      "Initiation als Impulse in die Entwickelung hineingestellt worden sind. Sobald man eine Vorliebe hat für die eine oder andere Form, bildet sich sogleich etwas wie ein astralischer Nebel, durch den man keinen freien Ausblick haben kann. Wer noch aus der ja für das gewöhnliche Leben selbstverständlichen Zuneigung eine vorurteilsvolle Bevorzugung der einen Religion in der Seele hat, der wird ganz gewiß nicht die anderen Religionen verstehen können, denn er wird in sich fühlen, wenn er auch nichts davon weiß, das Vorherrschen des einen Teiles der Initiationsinhalte und wird nicht zu einer vorurteilsfreien Erkenntnis des anderen Teiles kommen. So ist es für eine okkulte Betrachtung ganz selbstverständlich, in unbefangener Weise allen verschiedenen Ausflüssen und Impulsen aus den Initiationen gegenüberzustehen. So wenig wie jemand, der eine Pflanze betrachtet und der Blüte den Vorzug vor der Wurzel gibt, sich ein objektives Urteil über den ganzen Bau der Pflanze schaffen kann, so wenig kann derjenige ein richtiges Urteil gewinnen, der die Religionen nicht in völlig gleicher Unbefangenheit betrachten kann.",
      "Wir werden über die Anforderungen, welche die menschliche Seele an sich stellen muß, wenn sie die ersten Schritte zur Initiation macht, gerade in diesen Vorträgen sprechen. Zunächst wollte ich ein Gefühl dafür hervorrufen, wie die Initiation zum Leben steht und namentlich wie die verschiedenen Initiationsstätten und Initiationsimpulse zu der fortlaufenden Menschheitsentwickelung besonders in der nachatlantischen Zeit stehen.",
      "Nun aber erlebt eine okkulte Forschung, wenn sie diesen Gang der Menschheitsentwickelung dUrchmacht, etwas höchst Eigentümliches, was man nur im richtigen Maße verstehen, einschätzen wird, wenn solche Worte ehrlich und aufrichtig verstanden werden, wie sie eben ausgesprochen worden sind von der Gleichbedeutung der Religionen. Wenn solche Worte zur Selbstverständlichkeit geworden sind, dann erlebt man etwas ganz Eigentümliches, was uns gerade in diesen Vorträgen immer klarer und klarer werden soll.",
      "Man richte den Blick auf die die Menschheit im Laufe der Zeiten erleuchtenden Initiierten hin. Der Mensch, der zunächst in der Sinneswelt steht, kann, hinblickend auf die Initiierten, wenn sie als",
      "historische Gestalten überliefert sind, sich sagen: Das sind die großen Gestalten der Weltgeschichte. Wo es wichtig war, hat die Historie dafür gesorgt, daß man möglichst wenig von diesen Gestalten weiß.",
      "Nun mag es wieder paradox erscheinen, wenn gesagt wird: es ist ungeheuer gut, daß die Menschheit so wenig zum Beispiel von Homer weiß, denn dadurch kann die äußere Blüte der Gelehrsamkeit das Bild des Homer doch nicht so entstellen, wie dies bei den anderen Persönlichkeiten der Fall sein kann. Bei Goethe wird das erst einmal der Fall sein, wenn er - was man ja so recht herbeisehnen kann - eine so unbekannte Persönlichkeit sein wird, wie es jetzt Homer ist.",
      "Die Menschenseele kann in der äußeren Welt hinschauen auf diese Gestalten und sieht dann, was diese in der äußeren Welt getan haben. Dann kann der Mensch selber die ersten Schritte zur Initiation machen und so vorgehen, daß er auf die großen Gestalten der Initiation - einen Buddha oder einen Zarathustra - den Blick hinrichtet, sich erinnert, was ihm Buddha oder Zarathustra war in der Sinnes- weIt, was er dort für einen Eindruck von diesen Menschheits-Individualitäten empfangen hat, und kann sich dann fragen, wenn auf dem Wege zur Initiation einiges von dem Geisteslicht in ihn hereingebrochen ist: Wie erscheint mir jetzt Buddha, wie erscheint mir jetzt Zarathustra? - Er wird sich dann sagen: Jetzt erkenne ich mehr von Buddha, von Zarathustra; ich weiß etwas, was ich noch nicht wissen konnte, als ich in der Sinneswelt stand. - Dann kann sich der Mensch noch weiterentwickeln, und es kommt dann die Stufe, auf welcher er noch besser einsehen wird, was diese Erscheinungen als geistige Wesenheiten sind.",
      "Einen Buddha, einen Zarathustra wird man immer mehr und mehr erkennen, je mehr man sich selbst in das Geisteslicht hineinlebt, bis dann eine gewisse Grenze kommt, wo das ab bricht. Es ist das eine geheimnisvolle Erscheinung, auf die aber jetzt nicht eingegangen zu werden braucht.",
      "Es genügt, wenn gesagt wird: wenn es gegen die höheren Welten zu geht, kann das abbrechen. So ist es gegenüber allen Initiierten, die uns in der Weltentwickelung entgegentreten. Es kann leicht der noch nicht sehr weit fortgeschrittene Geist - Erkennen über diese Verhältnisse sich täuschen; das macht nicht viel aus.",
      "Denn es kann vorkommen, daß irgendeine",
      "Menschen-Individualität, die in der Vorzeit als geistiger Schauer sehr hoch gestanden hat, später wieder verkörpert ist und scheinbar heruntergestiegen ist von ihrer früheren geistigen Höhe. Die wahre Tatsache ist nur die, daß innerhalb der Menschheitsentwickelung Dinge zu verrichten sind, wo solche, die schon Initiierte waren, hineinverkörpert sind als Uninitiierte, um Taten zu verrichten, für die sie durch die Zeitverhältnisse nötig sind, so daß die Initiation, die sich für eine oder mehrere Inkarnationen verbirgt, hin- einwirken muß in eine gewisse Arbeitsweise. Da können dann über solche Individualitäten, wie sie uns da oder dort in ihrem äußeren Lebenslauf entgegentreten, um selbst ihren Weg zu machen, sehr leicht Täuschungen entstehen, und man kann sich über sie ganz falsche Vorstellungen machen. Die werden aber nach und nach im Laufe des Fortschreitens korrigiert werden müssen. Deshalb bleibt es doch richtig, daß die Stellung des Menschen zu den Initiierten im allgemeinen eine solche ist, daß er sie immer mehr und mehr kennenlernt, je mehr er selbst die Stufen hinaufschreitet, die ihm das Geisteslicht zugänglich machen. Nur eine merkwürdige Erscheinung finden wir in der Aufeinanderfolge der Menschheitsepochen.",
      "Was ich Ihnen eben gesagt habe von dem manchmal beirrenden Wiedererscheinen der Initiierten, so daß man glauben könnte, sie seien heruntergestiegen von ihrer Höhe, dafür könnte ich Beispiele anführen, und wahrscheinlich würden Sie im höchsten Grade erstaunt sein, wenn ich Ihnen sagte, in welcher Weise zum Beispiel Dante im 19. Jahrhundert wieder inkarniert war. Aber ich habe hier nicht die Aufgabe, das, was für mich selbst ein Forschungsergebnis war und was für mich selber feststeht, jetzt weiter zu besprechen, sondern die Dinge, die alle kennen, welche im Okkultismus bewandert sind, beweiskräftig vorzubringen, alles andere zurücktreten zu lassen und nichts anderes vorzubringen, als was allgemein anerkannt ist da, wo echter Okkultismus vertreten ist. Eine andere merkwürdige Erscheinung zeigt sich uns aber, die man am besten so aussprechen kann: Es tritt uns eine Individualität entgegen, bei der es keinen Sinn hat davon zu sprechen, daß sie so initiiert worden sei wie die anderen Initiierten, daß zwar durch sie das Prinzip der Initiation",
      "objektiv in der Welt vor uns steht, daß es da ist, daß es aber sinnlos wäre, davon zu sprechen, diese Individualität wäre auf der Erde so initiiert worden wie die andern Initiierten im Laufe der Menschheitsentwickelung. Ich habe die Tatsache oftmals berührt.",
      "Es gehört ein gewisser Grad von Mißverständnis dazu, diese Tatsache als aus einem spezifisch christlichen Vorurteil heraus herrührend aufzufassen. Wahrhaftig nicht aus einem irgendwie christlichen Vorurteil heraus, sondern weil sie gesagt werden muß als ein objektives okkultes Forschungsergebnis, soll es gesagt sein.",
      "Diese eine Individualität, die nicht initiiert worden ist wie die anderen Initiierten, sondern bei der es völlig sinnlos wäre, davon zu sprechen, daß sie so durch die Initiation durchgegangen wäre wie die anderen Initiierten, diese Individualität ist eben der Christus Jesus! Und ebensowenig - das sei hier noch einmal wie früher schon betont - wie der eine Waage begreifen kann, der da sagt, daß die Waage an zwei Punkten aufzuhängen wäre anstatt an einem, da es zum Wesen der Waage gehört, daß sich der Waagebalken um einen Punkt dreht, ebensowenig wie der ein Mechaniker ist, der behaupten würde, man solle die Waage an zwei oder mehreren Punkten aufhängen, was kein sachverständig`er Mechaniker sagen könnte, ebensowenig ist der kein sachverständiger Okkultist, der die Ansicht vertreten wollte, daß zu unserer Erdenentwickelung nicht nur ein Unterstützungspunkt, ein Hypomochlion, ein Festes gehöre.",
      "Ich sagte, daß dies ein objektives okkultes Forschungsresultat ist, das jeder anerkennen kann, gleichgültig ob er Buddhist oder Mohammedaner ist.",
      "Wer gewisse Schritte in der okkulten Entwickelung gemacht hat, lernt die Initiierten kennen, insofern sie große Persönlichkeiten sind oder Taten getan haben; er lernt sie kennen in den geistigen Welten, wenn er gewisse Stufen zur Initiation hinaufrückt, und er lernt sie noch mehr kennen, wenn er dann noch weiter aufrückt. Nehmen wir zum Beispiel an, es habe jemand in seinem Erdenleben keine Gelegenheit gehabt, den Buddha kennenzulernen; denken wir uns, er habe sich nicht mit ihm beschäftigt. Ich kenne Leute, die tief eingedrungen waren in das ganze abendländische Leben, die aber keinen blassen Begriff hatten von dem Buddha; von ihnen kann man sagen,",
      "daß sie sich innerhalb der physischen Welt, innerhalb ihres Leibesdaseins nicht beschäftigt haben mit dem Buddha. Oder nehmen wir Menschen, die sich in ihrem Erdendasein nicht beschäftigt haben mit den Größen der chinesischen Religion, und denken wir uns nun, es hätten diese Menschen durch die Initiation die überphysischen Welten betreten, oder - von einigen weiß ich das - daß sie sie betreten haben nach dem physischen Tode: da können sie kennenlernen, weil sie ihnen begegnen, den Buddha, den Moses, den Zarathustra als Geisteswesen und können sich Kenntnis, ein Wissen von ihnen aneignen.",
      "Da ist es ihnen kein Hindernis, wenn sie sich von diesen Persönlichkeiten ein Wissen aneignen wollen, daß sie auf der Erde dazu keine Gelegenheit hatten. Das ist anders bei dem Christus, und ich bitte Sie, dieses als eine rein okkulte Tatsache hinzunehmen.",
      "Man nehme an, daß sich jemand hier auf der Erde keinen Zusammenhang geschaffen habe in irgendeiner Inkarnation, die er schon erlebt hat, mit der Christus-Wesenheit. Dann ist ihm das, wenn er in einer außerphysischen Welt wahrnimmt, ein Hindernis, um in den höheren Welten den Christus zu finden; dann kann sich ihm der Christus nicht in der reinen Gestalt darstellen!",
      "Es gehört zur Erkenntnis, zum Erschauen der Christus-Wesenheit in den höheren Welten, daß man sich auf der Erde dazu vorbereitet hat! Das ist der okkulte Unterschied in dem Verhältnis des Menschen zu dem Christus und zu den anderen Initiierten.",
      "Das Christus-Ereignis ist ein solches, daß ein Spezifisches in seiner wichtigsten Phase eben gerade der physischen Erdentwickelung angehört, daß es hereinstrahlte in die physische Erdentwickelung und für diese den Gleichgewichtspunkt bildet.",
      "Man möchte sagen: Nehmen wir an, die Erde würde von denjenigen Wesen, die sich als Menschenseelen ausleben, zunächst nicht berücksichtigt. Es wäre durch irgend etwas im Weltenverlaufe geschehen, daß die Menschenseelen gesagt hätten: Wir berücksichtigen die Erde nicht; warum sollen wir uns da unten inkarnieren? - Es ist das natürlich eine unmögliche Tatsache, aber nehmen wir an, es wäre so. - Diese Menschenseelen würden dann, insofern das, was zur Erde gehört, geistig ist, es auch erleben können in den geistigen Welten,",
      "und was als hehre, große Prinzipien in den Initiierten wirkte, wäre erschaubar in den höheren Welten. Wollte nun eine solche Seele in den höheren Welten die Frage richten - sagen wir an den Weltenverlauf: Ich will von all den Wesen, die da in den höheren Welten sind, dasjenige genau kennenlernen, seiner eigentlichen Weltmission und seiner eigentlichen Aufgabe nach genau kennenlernen, das der Christus ist -, dann müßte einem solchen Menschenseelenwesen die Antwort werden: Wenn du dieses eine Wesen, das der Christus eben",
      "für uns ist, kennenlernen willst, dann mußt du dich auf der Erde inkarnieren, dann mußt du mitmachen in irgendeiner Weise das Mysterium von Golgatha, um eine Beziehung zu dem Christus-Wesen zu gewinnen! Denn das Christus.Mysterium mußte sich nach den Weltgesetzen auf der Erde abspielen. Die Erde ist der Schauplatz, wo sich nach den Weltgesetzen das Mysterium von Golgatha abspielen mußte und wo man sich für das Verständnis der Christus-Wesenheit die eigentliche Grundlage bilden muß. Und was man sich auf der Erde daher erwirbt für das Christus-Verständnis, das ist die Vorbereitung - und zwar in einem ganz anderen Maße als irgend etwas anderes, wofür die Erde Vorbereitung ist - für alles Erschauen und",
      "Erkennen dieser betreffenden Wesenheit in den höheren Welten. Daher war es so, daß in der Tat die Darlebung des Initiationsprinzipes bei der Christus-Wesenheit sich in einer ganz anderen Weise darstellte als bei den anderen Initiierten. Die letzteren erlebten eine übersinnliche Welt zuweilen in der tiefgehendsten Weise, gaben die Impulse, die daraus kamen, im Folgelauf der Menschheitsentwickelung; aber wenn sie in den höheren Welten erlebten, drinnenstanden, so waren sie aus ihrem physischen Leibe heraus. Wenn es auch bei hohen Initiierten gar nicht vieles bedarf, um aus dem physischen Leibe herauszukommen, wenn auch nur ein kleiner Schritt notwendig war, um aus dem physischen Leibe heraus gleich in eine Fülle von geistigen Tatsachen zu kommen, so bleibt es doch wahr, daß dieses Überspringen von dem physischen Leibe zu den höheren Leibern notwendig ist. Bei dem Christus Jesus haben wir die eigentümliche Erscheinung, daß er nach dem Prinzip der Initiation, nach dem, was man sonst braucht an Darstellung der Initiation, wissentlich",
      "- was wir so wissentlich im Menschensinne nennen - im Grunde genommen in den ganzen drei Jahren, in denen er auf der Erde gelebt hat, sich nicht im Initiationssinne von dem physischen Leibe entfernt hat, sondern immer darinnengeblieben ist. Und was er dar- gelebt hat und der Welt gegeben hat während dieser drei Jahre, das hat er durch den physischen Leib gegeben. Durch die überphysischen Leiber haben die andern Initiierten der Menschheit gegeben, was sie zu geben hatten. In dem Christus haben wir die eine einzige Individualität, die alles, was sie getan hat, was sie gesprochen hat, was von ihr ausgegangen ist in die Menschheitsentwickelung, durch den physischen Leib und nicht auf dem Umwege durch höhere Leiber gegeben hat.",
      "Dem populären Bewußtsein lebt sich das dadurch dar, daß es sich dem Gefühl nach so beurteilt: In dem Christus haben wir etwas vor uns, was das primitivste Bewußtsein verstehen kann, was jemand hat durch einen Leib, durch den wir sprechen, wenn wir im Alltags- leben sind. Dadurch dieses innige Verbundensein, dieses brüderliche Verbundensein mit der Christus-Individualität und dieses Verstehenkönnen der Christus-Individualität ohne Bildung, aus dem primitivsten, ursprünglichsten menschlichen Gemüt heraus!",
      "Daher die Notwendigkeit des Hinaufarbeitens zu einem höheren Verständnis, wenn man die anderen Initiierten verstehen will. Es ist daher wahr, was ich in den letzten zehn Jahren oft betont habe: In dem Christus haben wir einen Initiierten, den das primitivste Gemüt verstehen kann, obwohl ihn jemand, der zu einem höheren Verständnis aufrückt, dann noch besser versteht.",
      "Was mit einem menschlichen Leibe verbunden sein kann, das war am meisten diesen menschlichen Leib vergeistigend in Christus Jesus vorhanden und wirkte in einem menschlichen Leibe durch den Christus Jesus. Dagegen bei den anderen Initiierten war das der Fall, daß sie, während sie ihr Spirituelles zu geben hatten, nicht vollständig im physischen Leib wirken konnten, sondern immer einen Ruck heraus machen mußten und dann wieder verkünden konnten, was ihnen aus der übersinnlichen Welt geblieben ist; während es bei dem Christus immer so war, daß er alles durch den physischen Leib in der physischen Welt darzuleben hatte.",
      "Solche Dinge muß man berücksichtigen, wenn man auf die wahren Verhältnisse eingehen will. Alles andere ist ein Herumreden, so, wenn man etwa davon spricht, der Christus stehe höher oder die andern Initiierten stehen höher. Durch diese Rangordnung, auf die es absolut nicht ankommt, begreift man nichts. Darauf aber kommt es an, daß man in die Verhältnisse der Wesenheiten einen Blick tut. Nach seinem Geschmack mag der eine den einen, der andere den anderen Religionsstifter höher nennen. Das wird nicht viel schaden, denn solchen Schwächen sind die Menschen immer unterworfen. Aber darauf kommt es an, zu wissen, worin der wirkliche, der reale Unterschied besteht zwischen der Art, wie der Christus und wie die anderen Initiierten in der Welt dastehen. Dann kann man die Menschen ruhig sagen lassen: Ich halte die eine Individualität für höher als die andere, nach dem, wie sie gewirkt haben.",
      "Begreift man aber den charakterisierten Unterschied, dann begreift man auch den Unterschied in den Impulsen, die durch die Initiierten in die Welt gekommen sind."
    ],
    "sentences": [
      [
        "Wir werden in diesem kurzen Vortragszyklus wichtige Angelegenheiten des geistigen Lebens zu besprechen haben, Angelegenheiten, die dieses geistige Leben im umfassendsten Sinne berühren.",
        "Wir werden zu sprechen haben über dasjenige, was zugrunde liegt der sogenannten Initiation oder Einweihung, und - nachdem wir auf einige Geheimnisse und Gesetze dieser Initiation werden hingedeutet haben - von der Bedeutung dessen, was ausstrahlt im Laufe der Menschheitsentwickelung für das Leben von der Initiation und von den Initiierten.",
        "Wir werden von allem, was da ausstrahlt, zu sprechen haben mit Bezug auf dasjenige, was man in die einander so entgegengesetzten Vorstellungen zusammenfassen kann: Ewigkeit und Augenblick, Geisteslicht und Lebensdunkel.",
        "Nachdem wir unter dem Gesichtspunkt, den uns diese Vorstellungen liefern werden, gewissermaßen das` Leben des Menschen werden betrachtet haben, soll dann wieder zurückgekommen werden auf die Kraft der Initiation und auf die Kraft der Initiierten.",
        "Begrenzen also soll diesmal diese Betrachtungen das Prinzip der Initiation."
      ],
      [
        "Ewigkeit - wir brauchen die Vorstellung nur anzuschlagen, und wir fühlen es, es klingt etwas in uns, was zusammenhängt mit den tiefsten Sehnsuchten der menschlichen Seele, mit dem Höchsten, das unter seinen Strebenszielen der Mensch benennen kann.",
        "Augenblick - ein Wort, das uns immer wieder hindeutet auf dasjenige, in dem wir eigentlich leben, und auf die Notwendigkeit, in diesem Augenblick, in dem wir leben, dasjenige aufzusuchen, was uns den Ausblick geben kann in das Land der Sehnsucht, in die Ewigkeit."
      ],
      [
        "Man braucht sich nur zu erinnern, daß das tiefste Geheimnis seiner größten Dichtung Goethe in seinen «Faust» so hineingelegt hat, daß er den Faust gegenüber dem Augenblicke aussprechen läßt: «Verweile doch! du bist so schön!» und sich dann gestehen läßt: Wenn das Gesinnung der Seele werden kann, wenn es möglich ist, daß sich die Seele identifizieren könnte mit einem Geständnis, zum Augenblicke"
      ],
      [
        "zu sagen: «Verweile doch! du bist so schön!», dann müßte sogleich das Geständnis für Faust folgen, daß er würdig wäre, dem Gegner des Erdenmenschentums, dem Mephistopheles, zu verfallen.",
        "Was mit der Empfindung, die aus dem Augenblicke quillt, zusammenhängt, hat ja Goethe zum eigentlichen Grundgeheimnis seiner größten Dichtung gemacht.",
        "So scheint es, als ob dasjenige, in dem wir leben, der Augenblick, ganz entgegengesetzt wäre dem, was wir als Ewigkeit bezeichnen und wonach die Menschenseele immer wieder und wieder lechzen muß, sich sehnen muß."
      ],
      [
        "Geisteslicht - soviel wir theosophische Betrachtungen angestellt haben im Laufe der Jahre, wir haben erkannt, daß das Bestreben nach dem Geisteslicht überall das zugrunde liegend hat: den Menschen hinauszuführen aus dem Lebensdunkel.",
        "Und wieder können wir etwas aus einer der größten Dichtungen der Menschheitsentwickelung, aus dem «Faust» heraus fühlen: wie ein Dichter, wenn er eine große, in sich umfassende Seele schildern will, nicht umhin kann, sie auch herauskommen zu lassen aus dem Lebensdunkel. - Denn, was umwebt Faust im Beginne der Dichtung?",
        "Worin ist er ganz verstrickt?",
        "Im Lebensdunkel!",
        "Und wie oft mußten wir es betonen, daß dieses Lebensdunkel für den Menschen eine so große Kraft und Gewalt hat, daß das Geisteslicht, wenn es ihn in unreifem Zustande trifft, auf ihn so wirken kann, daß es ihn nicht erhellt, daß es ihn blendet, daß es ihn betäubt.",
        "So kann es sich nicht nur darum handeln: Wie geht der Weg zum Geisteslicht, wo ist er zu finden? - sondern vor allem muß es sich darum handeln: Wie muß der Mensch den Weg der Seele wandeln, der ihn in richtiger Weise zum Geisteslicht führen kann? - Damit sind nur die Linien gezeichnet, die uns in diesen Vorträgen beschäftigen sollen, und wir stehen ja in einer solchen Phase unserer theosophischen Arbeit, daß wir nicht vom Anbeginn an die Dinge zu entwickeln brauchen, sondern vielfach an Bekanntes anknüpfen können."
      ],
      [
        "Wenn das Wort Initiation, das sich uns so innig verbündet hat mit den Worten Ewigkeit und Geisteslicht, an uns herandringt, dann werden in der Seele lebendig alle die großen Menschen, welche wir im Laufe der Menschheitsepochen als die Initiierten kennen."
      ],
      [
        "Und mit ihnen werden auch diese Menschheitsepochen selber in unserer Seele erweckt, wie sie abgelaufen sind, wie die Menschen in ihnen lebten und wie das Licht aus den Initiationsstätten und von den Initiierten zu den Menschen strömte, um eigentlich das erst möglich zu machen, was die Impulse, die eigentlich treibenden Kräfte der Menschheitsentwickelung zu allen Zeiten gewesen sind.",
        "Es würde viel zu weit führen, bei Gelegenheit einer solchen Besprechung immer zurückzuweisen in ausführlicher Weise auf das, was innerhalb der Erdenentwickelung geschehen ist, bevor jene so oft besprochene atlantische Katastrophe über die Erde hereingebrochen ist, welche das Antlitz unserer Erde vollständig verändert hat.",
        "Wir bekommen schon eine hinlängliche und ausreichende Vorstellung von dem, was da in Betracht kommt, wenn wir die nachatlantischen Zeiten ins Auge fassen und uns an die eigentümliche Konfiguration des Menschen erinnern, wie sie so verschiedenartig sich ausgeprägt hat im Folgelauf der Zeit."
      ],
      [
        "Wir lassen unsern Blick zurückschweifen auf die tonangebende Kultur, wie sie sich angeschlossen hat, unmittelbar nachdem das Antlitz der Erde neugestaltet war durch die atlantische Katastrophe, und wir haben so oft mit Ehrfurcht zurückgewiesen auf dasjenige, was damals in der ersten Epoche der nachatlantischen Zeit die großen heiligen Lehrer der Menschheit gebracht haben an derjenigen Erdenstätte, an der später die indische Kultur sich entwickelt hat.",
        "Wir haben darauf aufmerksam gemacht, wie nur von unten nach oben aufschauen kann die Seele zu den hehren spirituellen Lehren, die damals durch Menschen-Individualitäten in die Welt gekommen sind, welche noch alle innere Größe in sich trugen derjenigen Menschen, die in der atlantischen Zeit den unmittelbaren Zusammenhang mit den göttlichen, mit den spirituellen Welten gehabt haben, wie das in den späteren Epochen der Menschheit nicht mehr möglich gewesen ist.",
        "Wir haben darauf hingewiesen, wie das Erbe der heute nur noch für den Okkultisten zu erreichenden atlantischen Weisheit in der nachatlantischen Form in den uralt heiligen Lehrern der ersten nachatlantischen Kulturperiode gelebt hat, und wir haben darauf hingewiesen, wie das, was damals gelebt hat, wovon es keine"
      ],
      [
        "Aufzeichnungen gibt außer in dem, was wir die Akasha-Chronik nennen, für den Menschen hinlänglich groß und bedeutend erscheint, wenn ihm die Nachklänge davon entgegenleuchten in der indischen oder überhaupt in der orientalischen Literatur.",
        "Die Höhe der Moralität, die Höhe der Spiritualität, die in diesen Schriften als der Nachklang uralter geistiger Lehren enthalten ist, können der gegenwärtigen Menschheit gar nicht einmal - insofern von äußerer Bildung gesprochen wird - voll zum Bewußtsein kommen."
      ],
      [
        "Am wenigsten kann das in denjenigen Ländern sein, welche vorbereitet worden sind zu ihrer gegenwärtigen äußeren Kultur durch das, was das Christentum in seinen verschiedenen Formen im Laufe der letzten Jahrhunderte hat leisten können.",
        "So fühlte sich die Seele von unten nach oben gerichtet, wenn sie zu all dem Großen, heute nur zu Erahnenden hinaufblickte, das selbst nur noch als ein Nachklang dieser uralten Spiritualität zu uns gekommen ist."
      ],
      [
        "Wenn man die Sache so ansieht und sich vor allem dessen bewußt ist, was hier oft erwähnt worden ist, daß die Menschheit erst wieder in der siebenten, in der letzten Epoche der nachatlantischen Zeit - wir stehen jetzt in der fünften - dazu gelangen wird, aus dem Lebensdunkel heraufzuholen das Verständnis für das, was einmal am Ausgangspunkte der nachatlantischen Zeit gelebt hat und die Impulse gegeben hat für die menschheitliche Entwickelung, und wenn man bedenkt, daß die Menschheit wird heranreifen müssen bis zur letzten Epoche, um das in sich wieder zu fühlen und zu erleben, was damals erlebt und gefühlt worden ist, dann bekommt man aber auch ein Gefühl und eine Empfindung dafür, wie hoch das Prinzip der Initiation gewesen sein muß, welche die Impulse gegeben hat zu dieser uralt heiligen spirituellen Kultur der Menschheit.",
        "Und dann sehen wir, wie Im Laufe der folgenden Epochen die Menschheit - ringend nach anderen geistigen Schätzen, nach anderen Schätzen des Erdendaseins - gleichsam immer weiter und weiter heruntersteigt, wie sie andere Formen annimmt, wie aber je nachdem, was die Zeiten fordern, die großen Initiierten aus der geistigen Welt heraus der Menschheit geben, was sie für ihre Kultur als Impulse für eine bestimmte Epoche nötig hat."
      ],
      [
        "Wir sehen dann vor unserem Blick auftauchen die Zarathustra"
      ],
      [
        "Kultur, die ganz andersartig ist, wenn wir sie in ihrem wahren Lichte betrachten, als die Kultur der heiligen Rishis; dann die ägyptischchaldäische Kultur; dann das, was in Griechenland die uralt heiligen Mysterien waren, wovon wir gestern in einem ganz anderen Sinne noch gesprochen haben, sehen überall hereinleuchten das Geisteslicht in das Lebensdunkel, wie es für die verschiedenen Zeiten notwendig ist."
      ],
      [
        "Wenn wir uns jetzt einmal am Ausgange unserer Betrachtungen fragen: Welche Vorstellungen können wir uns von einem Initiierten bilden - es ist ja selbstverständlich, daß von einem so umfassenden Begriff namentlich im Beginne des Vortragszyklus zunächst nur Annäherungsbegriffe gegeben werden können, wir werden dann immer tiefer und tiefer in das Wesen der Initiation eindringen können -, so wird es zunächst notwendig sein, daß wir mancherlei von dem zusammennehmen, was wir bereits auf theosophischem Felde gehört haben.",
        "Machen wir uns klar, daß zur völligen Initiation notwendig ist, daß der Mensch innerhalb seines physischen Leibes die Welt nicht so betrachtet, daß er durch seine Augen und die anderen Sinnesorgane die Welt um sich herum wahrnimmt oder durch seinen an das Gehirn gebundenen Verstand und durch das, was er seinen Orientierungssinn nennen kann, diese Welt oder irgendeine Welt, die ihn umgibt, sieht."
      ],
      [
        "Daß der Mensch sich auch nicht über diese Welten, wie es gewöhnlich der Fall ist, seine Begriffe bildet, sondern daß er in die Lage gekommen ist, durch das, was man nennen kann «außerhalb seines physischen Leibes Welten wahrzunehmen», in seinem Seelensein etwas zu haben, was ein übersinnlicher, ein geistiger Leib genannt werden mag, der in sich solche Wahrnehmungsorgane - aber höherer Art - hat, wie der physische Leib die Augen, die Ohren und die übrigen Wahrnehmungs- und Verstandesorgane hat.",
        "Welten sehen, ohne sich der Organe des physischen Leibes zu bedienen, das ist das, was man als eine zunächst nicht vielsagende, aber in ihrer Trockenheit zutreffende Definition des Initiierten geben kann."
      ],
      [
        "Und die großen Initiierten, welche die bedeutsamen Kulturimpulse im Folgelauf der Zeiten den Menschen gegeben haben, sie haben diese Unabhängigkeit vom Sinnenleibe und dieses Gebrauchen eines ganz"
      ],
      [
        "anderen Leibes eben in einem höchsten Maße erreicht.",
        "Ich möchte nicht in Abstraktionen viel sprechen, ich möchte möglichst auch zur Exemplifizierung Konkretes anführen, möchte also heute als ein Beispiel für ein solches Leben außerhalb des Sinnenleibes in einer höheren, der Seele zugehörigen Organisation das Folgende anführen."
      ],
      [
        "Wenn derjenige, der auch nur einige Schritte auf dem Wege zur Initiation gemacht hat, sich durch Selbstbesinnung klarmacht, was er eigentlich in sich und an sich erlebt, so kann er sich etwa das Folgende sagen: Zu dem ersten, was ich an mir erfahre, gehört, daß ich außer meinem sinnlichen, fleischlichen Leibe in mir habe einen feineren, nennen wir ihn ätherischen Leib, den wir so mit uns herum- tragen, wie wir den physischen Leib im Erdensein herumtragen.",
        "Wer die ersten Schritte zur Initiation hinauf macht, erlebt das zunächst so, daß er sich darin erfühlt, daß er dieses Erfühlen wahrnimmt, wie er auf anderer Stufe fühlt, was in seinem Blutsystem, in seinem Nervensystem lebt, oder was ersteht auf dem Boden seines Muskelsystems."
      ],
      [
        "Dieses innere Fühlen und Erleben ist ja da und das kann auch für den ätherischen Leib da sein.",
        "Insbesondere ist es dann nützlich für den Menschen, der auf den ersten Schritten zur Initiation ist, den besonderen Unterschied oder, man könnte auch sagen, die Beziehung zwischen dem Sich-Erfühlen, dem Sich-Erleben in dem elementarischen oder ätherischen Leibe und in dem physischen Leibe kennenzulernen."
      ],
      [
        "Man erlebt sich also in dem elementarischen Leibe, wie man weiß, daß man sein Blut, seinen Herzschlag oder seinen Pulsschlag in sich hat.",
        "Um sich das klarzumachen, kann man diesen elementarischen Leib in Zusammenhang betrachten mit dem physischen Leibe, in den man ja mehr hineingewöhnt ist als in das, was man sich erst erringt auf dieser geistigen Wanderschaft."
      ],
      [
        "Man kann sich sagen: In dem elementarischen Leibe hast du einen Teil, der entspricht dem physischen Gehirn, alledem, was deinen Kopf ausmacht.",
        "Der Kopf, das Gehirn ist gleichsam herauskristallisiert aus dem ätherischen Leibe und in demselben so darin, daß man es vergleichen könnte mit einer Wassermenge und einem Stück Eis, das darin schwimmt, wenn man das Wasser mit dem ätherischen Leibe vergleichen wollte und das Eis mit dem aus dem ätherischen"
      ],
      [
        "Leibe herauskristallisierten physischen Leibe.",
        "Aber man fühlt, man erlebt, daß ein inniger Zusammenhang ist zwischen dem, was man den Ätherteil des Kopfes oder des Gehirns nennen kann, und dem physischen Kopfe selber.",
        "Man weiß dann, wie man seine Gedanken schafft, wie man seine Erinnerungsbilder bildet innerhalb des ätherischen Leibes und wie das physische Gehirn nur gleichsam ein Spiegelungsapparat ist, weiß aber auch, wie das Gehirn eng zusammenhängend ist mit dem ätherischen Leibe.",
        "Insbesondere kann man das"
      ],
      [
        "dann erleben, wenn man sich recht stark beschäftigen muß mit Anstrengungen, die zusammenhängen mit dem physischen Plan, mit dem physischen Sein, wenn man viel nachdenken muß über die Dinge> wenn man also seinen physischen Leib anstrengen muß, daß er heraufholt aus den Tiefen des Lebens die Erinnerungsvorstellungen, um sie zusammenzuhalten.",
        "An einem solchen Vorgange ist im- mer zunächst, gleichgültig, ob man es weiß oder nicht, der ätherische Leib beteiligt."
      ],
      [
        "Aber es ist das physische Gehirn innig damit verbunden, und wenn man das physische Gehirn ermüdet, merkt man sehr, sehr die Ermüdung des Gehirns in dem betreffenden Ätherteile.",
        "Man merkt dann, daß man in dem, was man als elementarischen Gehirnteil erlebt, etwas wie einen Klotz, wie einen Fremdkörper hat, daß man nicht mehr herankann an das, woran man herankommen muß, denn die Beweglichkeit im physischen Gehirn ist etwas, was parallel gehen muß der Beweglichkeit im ätherischen Leibe."
      ],
      [
        "Man kann dann das deutliche Gefühl haben: Dein Ätherleib ermüdet auch nicht, er könnte bis in alle Ewigkeit fort die Gedankenbilder zusammenschließen und heraufholen dasjenige, was du weißt; aber um es in der physischen Welt zum Ausdruck zu bringen, muß es sich spiegeln, und da versagt das Gehirn. - Der elementarische Leib ermüdet nicht.",
        "Gerade weil er immerfort tätig sein kann, verspürt er die Ermüdung des Gehirns um so mehr."
      ],
      [
        "Man merkt gleichsam, was da das Gehirn an versagenden Kräften produziert.",
        "Und wenn es einschläft und in die Dumpfheit der Ermüdung verfällt,"
      ],
      [
        "kann man sich sagen: Jetzt mußt du aufhören, sonst würdest du dich krank machen. - Man kann nicht den Ätherleib abnutzen.",
        "Aber auf dem Umwege, daß man dem Gehirn übermäßige Dinge zumutet,"
      ],
      [
        "kann man fortfahren, es noch weiter zu ermüden und es so in einen lebenversagenden, toten Zustand bringen.",
        "Und das verträgt ein lebendiger Organismus nicht, daß etwas, was mit ihm in einem normalen Zusammenhange sein soll, partiell tot ist, daß es in einen abnormen Zustand kommt.",
        "Also man muß sich aus einem freien Entschluß sagen: Damit du nicht etwa abtötest einen Teil deines Gehirns, der dann von sich aus weiterfrißt, mußt du aufhören, wenn du dein Gehirn als ein Stück Fremdkörper in dir selbst empfindest."
      ],
      [
        "So ist das Erleben, wenn man das Verhältnis aufsucht zwischen demjenigen, was im menschlichen elementarischen oder ätherischen Leibe entspricht dem Gehirn oder dem Kopfe, und dem physischen Gehirn oder physischen Kopfe selber.",
        "Da ist ein inniger Zusammenhang.",
        "Es verläuft das äußere Sinnensein in der Tat so, daß es unmöglich ist, den Parallelismus zwischen beiden in übergroßem Maße zu durchbrechen.",
        "Man möchte sagen, wenn man dieses Verhältnis ausdrücken will: In unserm Kopfe, namentlich in unserm Gehirn haben wir einen recht treuen Ausdruck der Ätherkräfte, haben wir etwas, was in seiner äußeren Erscheinung und in seinen äußeren Funktionen wirklich ein treues Abbild ist der Funktionen und der Vorgänge in dem entsprechenden Ätherteil."
      ],
      [
        "Anders ist das für andere Organe des menschlichen elementarischen oder ätherischen Leibes und die entsprechenden physisch- sinnlichen Organe.",
        "Da sind die Dinge ganz anders.",
        "Ich will ein Beispiel anführen.",
        "Nehmen wir einmal die Hände.",
        "Geradeso wie dem Kopf oder dem Gehirn ein Ätherteil, ein elementarischer Teil in dem elementarischen Leibe entspricht, so entsprechen auch den Händen elementarische, ätherische Vorgänge des menschlichen Ätherleibes.",
        "Aber zwischen den äußeren physischen Händen und ihren Aufgaben und dem, was eigentlich dem zugrunde liegt in dem entsprechenden elementarischen oder ätherischen Teil, ist ein viel größerer Unterschied als zwischen dem physischen Kopfe und dem entsprechenden Teile in dem menschlichen elementarischen Leibe.",
        "Was die Hände tun, ist viel mehr bloß in der Sinneswelt verlaufend, ist viel mehr bloß eine sinnliche Verrichtung, und was die dazugehörigen elementarischen oder ätherischen Organe tun, findet nur zum"
      ],
      [
        "allergeringsten Teile in dem, was physisch in den Händen zum Ausdruck kommt, seine Offenbarung.",
        "Ich muß, wie man das oftmals muß, um die entsprechenden Tatsachen zu charakterisieren, allerdings Dinge sagen, die für ein physisches Empfinden und für ein In- Worte-Fassen von physischen Beobachtungen grotesk und paradox erscheinen, die aber doch dem Tatbestand, der hier zugrunde liegt, völlig entsprechen und die jeder, der etwas über die Dinge weiß, unmittelbar so empfinden wird, wie ich es auszusprechen habe."
      ],
      [
        "Den physischen Händen entsprechen elementarische Teile.",
        "Aber abgesehen davon, daß in den Händen, in den Bewegungen das zum Ausdruck kommt, was dem elementarischen Teile entspricht, sind diese ätherischen Organe innerhalb des Ätherleibes wahrhaftige Geistorgane."
      ],
      [
        "Ein höheres, viel intuitiveres, geistigeres Tun wird verrichtet in den Organen, die in den Händen und ihren Funktionen zum Ausdruck kommen, als durch das Äthergehirn.",
        "Wer auf diesem Gebiete Fortschritte gemacht hat, wird sagen: Ja, das Gehirn, auch das ätherisch zugrunde liegende, ist eigentlich das ungeschickteste geistige Organ, das der Mensch an sich trägt."
      ],
      [
        "Denn sobald man sich betätigt in dem elementarischen Teile des Gehirns, hat man verhältnismäßig sehr bald diesen Fremdkörper des Gehirns zu spüren.",
        "Diejenigen geistigen Verrichtungen aber, die gebunden sind an die Organe, die den Händen zugrunde liegen und einen unvollkommenen Ausdruck in den Händen und ihren Funktionen gewinnen, dienen zu weit höherem, geistigerem Erkennen und Beobachten; diese Organe führen schon in übersinnliche Welten und können sich beschäftigen mit der Wahrnehmung und mit der Orientierung in den übersinnlichen Welten."
      ],
      [
        "Drückt man als geistiger Schauer einen solchen Tatbestand aus, so muß man - etwas paradox, aber eben zutreffend - sagen: Das menschliche Gehirn ist das ungeschickteste Organ als Forschungsorgan für die geistige Welt, und die Hände - was ihnen geistig zugrunde liegt - sind viel interessantere, viel bedeutungsvollere Organe für die Erkenntnis dieser Welt, vor allen Dingen viel geschicktere Organe als das Gehirn.",
        "Auf dem Wege zur Initiation lernt man gar nicht sonderlich viel, wenn man von dem Gebrauch des Gehirnes zum freien Gebrauch des elementarischen Gehirnes"
      ],
      [
        "vordringt.",
        "Der Unterschied ist nicht besonders groß zwischen dem, was man erreicht durch ein geläutertes intuitives Gehirndenken und durch ein reguläres geistiges Erarbeiten in dem elementarischen geistigen Ebenbild des Gehirns."
      ],
      [
        "Aber ins Große wächst der Unterschied zwischen dem, was in der Welt die Hände verrichten, und dem, was mit demjenigen elementarischen Teile zu verrichten ist, der ebenso geistig zugrunde liegt den Händen wie das ätherische Gehirn dem physischen.",
        "Und nicht viel braucht man auszubilden auf dem Wege zur Initiation in bezug auf das, was dem Gehirn entspricht, denn das ist kein besonders wichtiges Organ."
      ],
      [
        "Aber was den Händen zugrunde liegt, das hängt zusammen - wie Sie es beschrieben finden in «Wie erlangt man Erkenntnisse der höheren Welten?» - mit der Tätigkeit der Lotosblume in der Herzgegend, die aber dann ihre Kraftstrahlen so ausstrahlt, daß sie die Organisation bilden, welche in unvollkommener Weise auf der Stufe, auf welcher der Mensch als physischer Mensch steht, in den Händen und ihren Funktionen dasteht.",
        "Wenn man zu einer solchen Sache aufrückt und sich eine Vorstellung machen kann von dem großen Unterschied, der besteht zwischen dem bloßen Gebrauch der physischen Hände und demjenigen, was man sich erarbeitet in bezug auf eine Übersinnliche Welt durch die viel geschickteren elementarischen Organe, welche den Händen zugrunde liegen, als es die elementarischen Organe des Gehirnes sind, dann bekommt man einen lebendigen Begriff von dem Sich-Hineinleben in die Initiation, von dem Reicherwerden des Menschen."
      ],
      [
        "Man wird nicht dadurch erheblich reicher, daß man fühlt: Dein Hirn will ausstrahlen und fühlen den Ätherteil des Gehirns.",
        "Das ist der Fall, aber es ist nicht das eigentlich tonangebende, bedeutsame Erleben."
      ],
      [
        "Das bedeutsame Erleben beginnt damit, daß man auch andere Partien sich ausdehnen und einen Zusammenhang mit der Welt sich erschaffen fühlt.",
        "Und wenn das auch paradox ist, so ist es doch so, daß man sagen kann: Das ungeschickteste Organ zum geistigen Forschen ist das Gehirn, denn es ist das am wenigsten ausbildungsfähige."
      ],
      [
        "Dagegen eröffnen sich ganz andere Perspektiven, wenn man die anderen scheinbar untergeordneten Organe berücksichtigt."
      ],
      [
        "So findet eine völlige Umwandlung mit dem statt, was der Mensch in sich erlebt, wenn er aufsteigt die ersten Schritte hinauf zu den Höhen der Initiation, und notwendig ist es, daß man sich zum Bewußtsein bringt, daß man dieses als innere Umwandlung der menschlichen Persönlichkeit so erfaßt, wie sonst auch das Prinzip der Entwickelung in der Welt ist, so daß das eine in das andere übergeht und man - wenn es vielleicht auch nicht ganz sachgemäß ist - das Spätere das Vollkommenere gegenüber dem Früheren nennt.",
        "Wenn man an dem Gang der Entwickelung sich klarmacht, wie das eine ins andere sich verwandelt, wie der Keim der Pflanze sich umwandelt und zu Blättern, Blüte und Frucht wird, dann kann man sich sagen: Die menschliche Persönlichkeit findet auch so etwas, was sie ist und was sie werden kann, durch die Mittel, die angegeben sind in «Wie erlangt man Erkenntnisse der höheren Welten?» und die die ersten Anfänge zu dem sind, was dann auch in die höchsten Regionen der Initiation hinaufführt."
      ],
      [
        "Es ist gut - und Sie werden sehen, daß es gut ist -, sich so eine lebendige Vorstellung davon hervorzurufen, wie die Menschen, die im Spirituellen Führer sein sollen im Folgelauf der Zeiten, sich innerlich umwandeln, wie das, was erst veranlagt ist im Menschen und sich so unvollkommen zeigt wie die Hände gegenüber den anderen Organen, sich verwandelt, was der Mensch äußerlich nicht bemerkt; dafür wird er aber innerlich um so bedeutungsvoller ein anderer.",
        "Daß so in der Welt etwas enthalten ist, wie es vorhanden ist für den, der etwa blind ist und nicht sehen kann, was man sonst mit den Augen sieht, was erst in Erscheinung tritt, wenn das Auge da ist, so ist die Welt des Spirituellen um uns herum vorhanden."
      ],
      [
        "Aber wir müssen ihr entgegenbringen, was wir selbst ihr entgegenbringen können, damit uns das entgegenkommt, was spirituell in der Welt enthalten ist."
      ],
      [
        "Innerhalb der verschiedenen Menschheitsepochen muß nun ein- strömen in den Gang der Entwickelung als Impulse das, was so gegeben werden kann durch ein Sich-Hineinleben in die geistigen Welten.",
        "Das lag immer dem zugrunde, was von den Mysterien, von den Initiationsstätten ausgegangen ist.",
        "Man stellt sich richtig den Gang der Menschheitsentwickelung vor, wenn man sich hinter dem, was"
      ],
      [
        "äußerlich wahrnehmbar ist, als die eigentlich treibenden Kräfte und Individualitäten die großen Initiierten vorstellt.",
        "Wie der Zusammenhang ist zwischen dem, was diese großen Initiierten zu tun haben, und dem, was dann äußerlich in der Welt geschieht, das ist vielfach erst durch Theosophie oder Okkultismus überhaupt durchschaubar.",
        "Für das äußere, rein geschichtliche, rein gelehrte Erkennen ist es so, daß man eigentlich nur sieht: Da verläuft die Menschheitsgeschichte, da verläuft die Menschheitsentwickelung.",
        "Aber man sieht nicht die treibenden Kräfte, die dahinter sind.",
        "So verfolgt man in der äußeren Geschichte wie eine Kette von Erscheinungen, bei der sich Glied an Glied anreiht, was äußerlich aufeinander folgt.",
        "Daß aber an einer gewissen Stelle der Kette Einschläge aus einer ganz anderen Welt kommen, auf dem Umwege der Initiation kommen, das ist das, was wir - aus Gründen, die auch schon erörtert worden sind - durch die theosophische Erkenntnis in uns aufnehmen können.",
        "So erblicken wir theosophisch gerade das Innerlichste in dem Folgelauf der Zeiten, dasjenige, was dann doch auch für die ganze Signatur, für den ganzen Charakter der Entwickelung am meisten zugrunde liegt.",
        "So empfinden wir die Religionen, die Vielgestaltigkeit der religiösen Entwickelung als einen Ausfluß der Initiierten, empfinden, wie die Impulse aus den Initiations- und Mysterienstätten herausfließend in das allgemeine Leben der Menschheit übergehen."
      ],
      [
        "Wer die Entwickelung der Menschheit so betrachtet, der kommt ganz selbstverständlich - und beim wahren Okkultismus war das immer der Fall - nicht zu einer irgendwie gearteten, von vornherein angenommenen Bevorzugung der einen Religion vor der anderen.",
        "Es gehört zu den allerersten Erfordernissen der Initiation, alle jene Vorurteile, alle jene Vorempfindungen und Vorgefühle abzustreifen, welche in der Menschenseele dadurch erwachsen, daß sie in irgendein Religionssystem, in irgendeine Religionsgemeinschaft hineininkarniert ist.",
        "Sorgfältig muß die Selbsterziehung darüber wachen, daß nichts mehr in der Seele sitzt, was der einen Religion den Vorzug geben könnte vor der anderen.",
        "Mit völliger Unbefangenheit muß gegenübergestanden werden dem, was Inhalt der verschiedenen Religionen ist, die im Laufe der Menschheitsentwickelung durch die"
      ],
      [
        "Initiation als Impulse in die Entwickelung hineingestellt worden sind.",
        "Sobald man eine Vorliebe hat für die eine oder andere Form, bildet sich sogleich etwas wie ein astralischer Nebel, durch den man keinen freien Ausblick haben kann.",
        "Wer noch aus der ja für das gewöhnliche Leben selbstverständlichen Zuneigung eine vorurteilsvolle Bevorzugung der einen Religion in der Seele hat, der wird ganz gewiß nicht die anderen Religionen verstehen können, denn er wird in sich fühlen, wenn er auch nichts davon weiß, das Vorherrschen des einen Teiles der Initiationsinhalte und wird nicht zu einer vorurteilsfreien Erkenntnis des anderen Teiles kommen.",
        "So ist es für eine okkulte Betrachtung ganz selbstverständlich, in unbefangener Weise allen verschiedenen Ausflüssen und Impulsen aus den Initiationen gegenüberzustehen.",
        "So wenig wie jemand, der eine Pflanze betrachtet und der Blüte den Vorzug vor der Wurzel gibt, sich ein objektives Urteil über den ganzen Bau der Pflanze schaffen kann, so wenig kann derjenige ein richtiges Urteil gewinnen, der die Religionen nicht in völlig gleicher Unbefangenheit betrachten kann."
      ],
      [
        "Wir werden über die Anforderungen, welche die menschliche Seele an sich stellen muß, wenn sie die ersten Schritte zur Initiation macht, gerade in diesen Vorträgen sprechen.",
        "Zunächst wollte ich ein Gefühl dafür hervorrufen, wie die Initiation zum Leben steht und namentlich wie die verschiedenen Initiationsstätten und Initiationsimpulse zu der fortlaufenden Menschheitsentwickelung besonders in der nachatlantischen Zeit stehen."
      ],
      [
        "Nun aber erlebt eine okkulte Forschung, wenn sie diesen Gang der Menschheitsentwickelung dUrchmacht, etwas höchst Eigentümliches, was man nur im richtigen Maße verstehen, einschätzen wird, wenn solche Worte ehrlich und aufrichtig verstanden werden, wie sie eben ausgesprochen worden sind von der Gleichbedeutung der Religionen.",
        "Wenn solche Worte zur Selbstverständlichkeit geworden sind, dann erlebt man etwas ganz Eigentümliches, was uns gerade in diesen Vorträgen immer klarer und klarer werden soll."
      ],
      [
        "Man richte den Blick auf die die Menschheit im Laufe der Zeiten erleuchtenden Initiierten hin.",
        "Der Mensch, der zunächst in der Sinneswelt steht, kann, hinblickend auf die Initiierten, wenn sie als"
      ],
      [
        "historische Gestalten überliefert sind, sich sagen: Das sind die großen Gestalten der Weltgeschichte.",
        "Wo es wichtig war, hat die Historie dafür gesorgt, daß man möglichst wenig von diesen Gestalten weiß."
      ],
      [
        "Nun mag es wieder paradox erscheinen, wenn gesagt wird: es ist ungeheuer gut, daß die Menschheit so wenig zum Beispiel von Homer weiß, denn dadurch kann die äußere Blüte der Gelehrsamkeit das Bild des Homer doch nicht so entstellen, wie dies bei den anderen Persönlichkeiten der Fall sein kann.",
        "Bei Goethe wird das erst einmal der Fall sein, wenn er - was man ja so recht herbeisehnen kann - eine so unbekannte Persönlichkeit sein wird, wie es jetzt Homer ist."
      ],
      [
        "Die Menschenseele kann in der äußeren Welt hinschauen auf diese Gestalten und sieht dann, was diese in der äußeren Welt getan haben.",
        "Dann kann der Mensch selber die ersten Schritte zur Initiation machen und so vorgehen, daß er auf die großen Gestalten der Initiation - einen Buddha oder einen Zarathustra - den Blick hinrichtet, sich erinnert, was ihm Buddha oder Zarathustra war in der Sinnes- weIt, was er dort für einen Eindruck von diesen Menschheits-Individualitäten empfangen hat, und kann sich dann fragen, wenn auf dem Wege zur Initiation einiges von dem Geisteslicht in ihn hereingebrochen ist: Wie erscheint mir jetzt Buddha, wie erscheint mir jetzt Zarathustra? - Er wird sich dann sagen: Jetzt erkenne ich mehr von Buddha, von Zarathustra; ich weiß etwas, was ich noch nicht wissen konnte, als ich in der Sinneswelt stand. - Dann kann sich der Mensch noch weiterentwickeln, und es kommt dann die Stufe, auf welcher er noch besser einsehen wird, was diese Erscheinungen als geistige Wesenheiten sind."
      ],
      [
        "Einen Buddha, einen Zarathustra wird man immer mehr und mehr erkennen, je mehr man sich selbst in das Geisteslicht hineinlebt, bis dann eine gewisse Grenze kommt, wo das ab bricht.",
        "Es ist das eine geheimnisvolle Erscheinung, auf die aber jetzt nicht eingegangen zu werden braucht."
      ],
      [
        "Es genügt, wenn gesagt wird: wenn es gegen die höheren Welten zu geht, kann das abbrechen.",
        "So ist es gegenüber allen Initiierten, die uns in der Weltentwickelung entgegentreten.",
        "Es kann leicht der noch nicht sehr weit fortgeschrittene Geist - Erkennen über diese Verhältnisse sich täuschen; das macht nicht viel aus."
      ],
      [
        "Denn es kann vorkommen, daß irgendeine"
      ],
      [
        "Menschen-Individualität, die in der Vorzeit als geistiger Schauer sehr hoch gestanden hat, später wieder verkörpert ist und scheinbar heruntergestiegen ist von ihrer früheren geistigen Höhe.",
        "Die wahre Tatsache ist nur die, daß innerhalb der Menschheitsentwickelung Dinge zu verrichten sind, wo solche, die schon Initiierte waren, hineinverkörpert sind als Uninitiierte, um Taten zu verrichten, für die sie durch die Zeitverhältnisse nötig sind, so daß die Initiation, die sich für eine oder mehrere Inkarnationen verbirgt, hin- einwirken muß in eine gewisse Arbeitsweise.",
        "Da können dann über solche Individualitäten, wie sie uns da oder dort in ihrem äußeren Lebenslauf entgegentreten, um selbst ihren Weg zu machen, sehr leicht Täuschungen entstehen, und man kann sich über sie ganz falsche Vorstellungen machen.",
        "Die werden aber nach und nach im Laufe des Fortschreitens korrigiert werden müssen.",
        "Deshalb bleibt es doch richtig, daß die Stellung des Menschen zu den Initiierten im allgemeinen eine solche ist, daß er sie immer mehr und mehr kennenlernt, je mehr er selbst die Stufen hinaufschreitet, die ihm das Geisteslicht zugänglich machen.",
        "Nur eine merkwürdige Erscheinung finden wir in der Aufeinanderfolge der Menschheitsepochen."
      ],
      [
        "Was ich Ihnen eben gesagt habe von dem manchmal beirrenden Wiedererscheinen der Initiierten, so daß man glauben könnte, sie seien heruntergestiegen von ihrer Höhe, dafür könnte ich Beispiele anführen, und wahrscheinlich würden Sie im höchsten Grade erstaunt sein, wenn ich Ihnen sagte, in welcher Weise zum Beispiel Dante im 19.",
        "Jahrhundert wieder inkarniert war.",
        "Aber ich habe hier nicht die Aufgabe, das, was für mich selbst ein Forschungsergebnis war und was für mich selber feststeht, jetzt weiter zu besprechen, sondern die Dinge, die alle kennen, welche im Okkultismus bewandert sind, beweiskräftig vorzubringen, alles andere zurücktreten zu lassen und nichts anderes vorzubringen, als was allgemein anerkannt ist da, wo echter Okkultismus vertreten ist.",
        "Eine andere merkwürdige Erscheinung zeigt sich uns aber, die man am besten so aussprechen kann: Es tritt uns eine Individualität entgegen, bei der es keinen Sinn hat davon zu sprechen, daß sie so initiiert worden sei wie die anderen Initiierten, daß zwar durch sie das Prinzip der Initiation"
      ],
      [
        "objektiv in der Welt vor uns steht, daß es da ist, daß es aber sinnlos wäre, davon zu sprechen, diese Individualität wäre auf der Erde so initiiert worden wie die andern Initiierten im Laufe der Menschheitsentwickelung.",
        "Ich habe die Tatsache oftmals berührt."
      ],
      [
        "Es gehört ein gewisser Grad von Mißverständnis dazu, diese Tatsache als aus einem spezifisch christlichen Vorurteil heraus herrührend aufzufassen.",
        "Wahrhaftig nicht aus einem irgendwie christlichen Vorurteil heraus, sondern weil sie gesagt werden muß als ein objektives okkultes Forschungsergebnis, soll es gesagt sein."
      ],
      [
        "Diese eine Individualität, die nicht initiiert worden ist wie die anderen Initiierten, sondern bei der es völlig sinnlos wäre, davon zu sprechen, daß sie so durch die Initiation durchgegangen wäre wie die anderen Initiierten, diese Individualität ist eben der Christus Jesus!",
        "Und ebensowenig - das sei hier noch einmal wie früher schon betont - wie der eine Waage begreifen kann, der da sagt, daß die Waage an zwei Punkten aufzuhängen wäre anstatt an einem, da es zum Wesen der Waage gehört, daß sich der Waagebalken um einen Punkt dreht, ebensowenig wie der ein Mechaniker ist, der behaupten würde, man solle die Waage an zwei oder mehreren Punkten aufhängen, was kein sachverständig`er Mechaniker sagen könnte, ebensowenig ist der kein sachverständiger Okkultist, der die Ansicht vertreten wollte, daß zu unserer Erdenentwickelung nicht nur ein Unterstützungspunkt, ein Hypomochlion, ein Festes gehöre."
      ],
      [
        "Ich sagte, daß dies ein objektives okkultes Forschungsresultat ist, das jeder anerkennen kann, gleichgültig ob er Buddhist oder Mohammedaner ist."
      ],
      [
        "Wer gewisse Schritte in der okkulten Entwickelung gemacht hat, lernt die Initiierten kennen, insofern sie große Persönlichkeiten sind oder Taten getan haben; er lernt sie kennen in den geistigen Welten, wenn er gewisse Stufen zur Initiation hinaufrückt, und er lernt sie noch mehr kennen, wenn er dann noch weiter aufrückt.",
        "Nehmen wir zum Beispiel an, es habe jemand in seinem Erdenleben keine Gelegenheit gehabt, den Buddha kennenzulernen; denken wir uns, er habe sich nicht mit ihm beschäftigt.",
        "Ich kenne Leute, die tief eingedrungen waren in das ganze abendländische Leben, die aber keinen blassen Begriff hatten von dem Buddha; von ihnen kann man sagen,"
      ],
      [
        "daß sie sich innerhalb der physischen Welt, innerhalb ihres Leibesdaseins nicht beschäftigt haben mit dem Buddha.",
        "Oder nehmen wir Menschen, die sich in ihrem Erdendasein nicht beschäftigt haben mit den Größen der chinesischen Religion, und denken wir uns nun, es hätten diese Menschen durch die Initiation die überphysischen Welten betreten, oder - von einigen weiß ich das - daß sie sie betreten haben nach dem physischen Tode: da können sie kennenlernen, weil sie ihnen begegnen, den Buddha, den Moses, den Zarathustra als Geisteswesen und können sich Kenntnis, ein Wissen von ihnen aneignen."
      ],
      [
        "Da ist es ihnen kein Hindernis, wenn sie sich von diesen Persönlichkeiten ein Wissen aneignen wollen, daß sie auf der Erde dazu keine Gelegenheit hatten.",
        "Das ist anders bei dem Christus, und ich bitte Sie, dieses als eine rein okkulte Tatsache hinzunehmen."
      ],
      [
        "Man nehme an, daß sich jemand hier auf der Erde keinen Zusammenhang geschaffen habe in irgendeiner Inkarnation, die er schon erlebt hat, mit der Christus-Wesenheit.",
        "Dann ist ihm das, wenn er in einer außerphysischen Welt wahrnimmt, ein Hindernis, um in den höheren Welten den Christus zu finden; dann kann sich ihm der Christus nicht in der reinen Gestalt darstellen!"
      ],
      [
        "Es gehört zur Erkenntnis, zum Erschauen der Christus-Wesenheit in den höheren Welten, daß man sich auf der Erde dazu vorbereitet hat!",
        "Das ist der okkulte Unterschied in dem Verhältnis des Menschen zu dem Christus und zu den anderen Initiierten."
      ],
      [
        "Das Christus-Ereignis ist ein solches, daß ein Spezifisches in seiner wichtigsten Phase eben gerade der physischen Erdentwickelung angehört, daß es hereinstrahlte in die physische Erdentwickelung und für diese den Gleichgewichtspunkt bildet."
      ],
      [
        "Man möchte sagen: Nehmen wir an, die Erde würde von denjenigen Wesen, die sich als Menschenseelen ausleben, zunächst nicht berücksichtigt.",
        "Es wäre durch irgend etwas im Weltenverlaufe geschehen, daß die Menschenseelen gesagt hätten: Wir berücksichtigen die Erde nicht; warum sollen wir uns da unten inkarnieren? - Es ist das natürlich eine unmögliche Tatsache, aber nehmen wir an, es wäre so. - Diese Menschenseelen würden dann, insofern das, was zur Erde gehört, geistig ist, es auch erleben können in den geistigen Welten,"
      ],
      [
        "und was als hehre, große Prinzipien in den Initiierten wirkte, wäre erschaubar in den höheren Welten.",
        "Wollte nun eine solche Seele in den höheren Welten die Frage richten - sagen wir an den Weltenverlauf: Ich will von all den Wesen, die da in den höheren Welten sind, dasjenige genau kennenlernen, seiner eigentlichen Weltmission und seiner eigentlichen Aufgabe nach genau kennenlernen, das der Christus ist -, dann müßte einem solchen Menschenseelenwesen die Antwort werden: Wenn du dieses eine Wesen, das der Christus eben"
      ],
      [
        "für uns ist, kennenlernen willst, dann mußt du dich auf der Erde inkarnieren, dann mußt du mitmachen in irgendeiner Weise das Mysterium von Golgatha, um eine Beziehung zu dem Christus-Wesen zu gewinnen!",
        "Denn das Christus.Mysterium mußte sich nach den Weltgesetzen auf der Erde abspielen.",
        "Die Erde ist der Schauplatz, wo sich nach den Weltgesetzen das Mysterium von Golgatha abspielen mußte und wo man sich für das Verständnis der Christus-Wesenheit die eigentliche Grundlage bilden muß.",
        "Und was man sich auf der Erde daher erwirbt für das Christus-Verständnis, das ist die Vorbereitung - und zwar in einem ganz anderen Maße als irgend etwas anderes, wofür die Erde Vorbereitung ist - für alles Erschauen und"
      ],
      [
        "Erkennen dieser betreffenden Wesenheit in den höheren Welten.",
        "Daher war es so, daß in der Tat die Darlebung des Initiationsprinzipes bei der Christus-Wesenheit sich in einer ganz anderen Weise darstellte als bei den anderen Initiierten.",
        "Die letzteren erlebten eine übersinnliche Welt zuweilen in der tiefgehendsten Weise, gaben die Impulse, die daraus kamen, im Folgelauf der Menschheitsentwickelung; aber wenn sie in den höheren Welten erlebten, drinnenstanden, so waren sie aus ihrem physischen Leibe heraus.",
        "Wenn es auch bei hohen Initiierten gar nicht vieles bedarf, um aus dem physischen Leibe herauszukommen, wenn auch nur ein kleiner Schritt notwendig war, um aus dem physischen Leibe heraus gleich in eine Fülle von geistigen Tatsachen zu kommen, so bleibt es doch wahr, daß dieses Überspringen von dem physischen Leibe zu den höheren Leibern notwendig ist.",
        "Bei dem Christus Jesus haben wir die eigentümliche Erscheinung, daß er nach dem Prinzip der Initiation, nach dem, was man sonst braucht an Darstellung der Initiation, wissentlich"
      ],
      [
        "- was wir so wissentlich im Menschensinne nennen - im Grunde genommen in den ganzen drei Jahren, in denen er auf der Erde gelebt hat, sich nicht im Initiationssinne von dem physischen Leibe entfernt hat, sondern immer darinnengeblieben ist.",
        "Und was er dar- gelebt hat und der Welt gegeben hat während dieser drei Jahre, das hat er durch den physischen Leib gegeben.",
        "Durch die überphysischen Leiber haben die andern Initiierten der Menschheit gegeben, was sie zu geben hatten.",
        "In dem Christus haben wir die eine einzige Individualität, die alles, was sie getan hat, was sie gesprochen hat, was von ihr ausgegangen ist in die Menschheitsentwickelung, durch den physischen Leib und nicht auf dem Umwege durch höhere Leiber gegeben hat."
      ],
      [
        "Dem populären Bewußtsein lebt sich das dadurch dar, daß es sich dem Gefühl nach so beurteilt: In dem Christus haben wir etwas vor uns, was das primitivste Bewußtsein verstehen kann, was jemand hat durch einen Leib, durch den wir sprechen, wenn wir im Alltags- leben sind.",
        "Dadurch dieses innige Verbundensein, dieses brüderliche Verbundensein mit der Christus-Individualität und dieses Verstehenkönnen der Christus-Individualität ohne Bildung, aus dem primitivsten, ursprünglichsten menschlichen Gemüt heraus!"
      ],
      [
        "Daher die Notwendigkeit des Hinaufarbeitens zu einem höheren Verständnis, wenn man die anderen Initiierten verstehen will.",
        "Es ist daher wahr, was ich in den letzten zehn Jahren oft betont habe: In dem Christus haben wir einen Initiierten, den das primitivste Gemüt verstehen kann, obwohl ihn jemand, der zu einem höheren Verständnis aufrückt, dann noch besser versteht."
      ],
      [
        "Was mit einem menschlichen Leibe verbunden sein kann, das war am meisten diesen menschlichen Leib vergeistigend in Christus Jesus vorhanden und wirkte in einem menschlichen Leibe durch den Christus Jesus.",
        "Dagegen bei den anderen Initiierten war das der Fall, daß sie, während sie ihr Spirituelles zu geben hatten, nicht vollständig im physischen Leib wirken konnten, sondern immer einen Ruck heraus machen mußten und dann wieder verkünden konnten, was ihnen aus der übersinnlichen Welt geblieben ist; während es bei dem Christus immer so war, daß er alles durch den physischen Leib in der physischen Welt darzuleben hatte."
      ],
      [
        "Solche Dinge muß man berücksichtigen, wenn man auf die wahren Verhältnisse eingehen will.",
        "Alles andere ist ein Herumreden, so, wenn man etwa davon spricht, der Christus stehe höher oder die andern Initiierten stehen höher.",
        "Durch diese Rangordnung, auf die es absolut nicht ankommt, begreift man nichts.",
        "Darauf aber kommt es an, daß man in die Verhältnisse der Wesenheiten einen Blick tut.",
        "Nach seinem Geschmack mag der eine den einen, der andere den anderen Religionsstifter höher nennen.",
        "Das wird nicht viel schaden, denn solchen Schwächen sind die Menschen immer unterworfen.",
        "Aber darauf kommt es an, zu wissen, worin der wirkliche, der reale Unterschied besteht zwischen der Art, wie der Christus und wie die anderen Initiierten in der Welt dastehen.",
        "Dann kann man die Menschen ruhig sagen lassen: Ich halte die eine Individualität für höher als die andere, nach dem, wie sie gewirkt haben."
      ],
      [
        "Begreift man aber den charakterisierten Unterschied, dann begreift man auch den Unterschied in den Impulsen, die durch die Initiierten in die Welt gekommen sind."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "DRITTER VORTRAG München, 27. August 1912",
    "paragraphs": [
      "Wenn wir von der Initiation und ihrer Bedeutung für das ganze menschliche Leben und für die menschliche Entwickelung sprechen wollen, müssen wir in das Wesen dessen, um was es sich eigentlich handelt, aus denjenigen Begriffen und Vorstellungen heraus einzudringen versuchen, welche nun einmal notwendig sind, um die über- sinnlichen Welten überhaupt in richtiger Art zu charakterisieren. Es ist ja begreiflich, daß die menschliche Seele auf jeder Stufe ihrer Entwickelung die allertiefste Sehnsucht danach hat, etwas darüber zu erfahren, wie es in jenen Welten aussieht, denen man in mehr oder weniger berechtigter Weise das Prädikat der Ewigkeit beilegen kann.",
      "Daher muß es auch begreiflich erscheinen, daß die menschlichen Seelen danach trachten, ohne viel Vorbereitung erst mit den Vorstellungen, mit den Begriffen, die man im Sinnensein hat, in diese höheren Welten hineinzudringen. Ich sage ausdrücklich: das ist begreiflich.",
      "Und dem kann auch in einer gewissen Weise entsprochen werden da, wo es sich um Befriedigung der Ewigkeitssehnsucht in diesen oder jenen Religionsbekenntnissen handelt. Wenn es sich aber in wahrhaft theosophischem Sinne darum handelt, tiefer in den Urquell alles Geistigen und damit namentlich in den Urquell alles seelischen Lebens einzudringen, dann muß man - nach und nach wenigstens - sich befreunden mit der Notwendigkeit, seine Vorstellungen, seine Begriffe in einer gewissen Weise umzuwandeln, bevor man sich richtige Ideen von den höheren, den übersinnlichen Welten machen will.",
      "Weil dies - wie wir in den nächsten Vorträgen sehen werden - insbesondere zur Charakteristik der eigentlichen ChristusErscheinung notwendig ist, sei es mir heute gestattet, einiges über die notwendige Umwandlung und Umformung des menschlichen Vorstellungslebens zu sprechen, wenn der Mensch hinaufdringen will zu Ideen über die übersinnlichen Welten.",
      "Damit muß man sich schon einmal bekanntmachen, daß in den übersinnlichen Welten alles anders ist als in dem Sinnensein, denn",
      "eine genaue Wiederholung eines Weltendaseins findet sich eigentlich nirgends im Universum. Wenn nun alles anders ist, warum sollte dann durchaus angenommen werden, daß die menschlichen Vorstellungen und Begriffe für die höheren Welten in gleichem Maße gültig seien, wie sie gültig sind für das Sinnensein? Das sind sie eben nicht. Wer den praktischen Aufstieg in diejenigen Welten, welche die Initiation eröffnet, wirklich vollführt, das heißt wer Erfahrungen hat im übersinnlichen Erleben, der weiß, wie wir gleich hören werden, daß er nicht nur vieles sonstiges an sich wandeln muß, ich könnte hier gleich sprechen: zurücklassen muß beim Hüter der Schwelle, sondern auch viele von seinen Gewohnheiten, Vorstellungen, Begriffen und Ideen dort ablegen muß, bevor er in die übersinnlichen, höheren Welten eindringen kann.",
      "Vor allen Dingen wollen wir ausgehen von gewissen Vorstellungen, die uns ja alle im Sinnensein beherrschen müssen. Ein Begriffspaar, möchte ich sagen, zwei Begriffssysteme sind da besonders ausschlaggebend. Sie stehen für unser Sinnensein nebeneinander, laufen nebeneinander her. Das eine ist alles, was wir uns an Vorstellungen machen über die natürliche Welt, über die Naturgesetze, Naturkräfte. Neben alledem, was wir uns darüber an Vorstellungen bilden, steht für unser gewöhnliches Leben im Sinnensein das, was wir nennen die moralische Weltordnung, die Summe unserer moralischen Vorstellungen, Begriffe und Ideen. Bei einer richtigen Selbstbesinnung wird der Mensch sehr bald darauf verfallen, daß er für das Sinnensein diese beiden Begriffssysteme - Naturordnung und moralische Weltordnung - auseinanderhalten müsse. Wenn wir eine Pflanze erklären - nehmen wir an, wir haben eine Giftpflanze vor uns -, so erklären wir sie aus den Naturkräften, aus den Naturgesetzen heraus. Und ich möchte sagen, wir verderben uns die Erklärung der Pflanze nicht dadurch, daß wir die Pflanze dafür moralisch verantwortlich machen, daß sie eine Giftpflanze ist. Wir halten dafür, daß es zum gesunden Denken innerhalb des Sinnenseins bei den Erklärungen des natürlichen Daseins gehört, uns zunächst von dem zu emanzipieren, was wir die moralischen Begriffe und Ideen nennen. Wir wissen ja, daß wir diese Art von Emanzipation selbst noch üben",
      "müssen, wenn wir zu unbefangenen, objektiven Vorstellungen im Tierreiche kommen wollen. Es hätte keinen Sinn, so fühlen und empfinden wir, den Löwen für seine Grausamkeit ebenso verantwortlich zu machen, wie wir einen Menschen für seine Grausamkeit verantwortlich machen.",
      "Und wenn viele heutige Naturerklärer schon im Tierreiche so etwas wie moralische Begriffe finden, ich möchte sagen, mehr nach dem Geschmack als nach einer wahrhaftigen Notwendigkeit, so mag das schon in einem gewissen Sinne berechtigt sein. Aber man kann doch nur sprechen von einem Anklang an moralische Vorstellungen bei dem, was die Tiere tun, was im Tierreiche geschieht.",
      "Naturerklärung erfordert, wenn wir sie rein entwickeln sollen, ein Emanzipieren von moralischen Vorstellungen und Begriffen, wenn wir mit unseren Erklärungen unmittelbar im Sinnensein verbleiben wollen. Dann aber tritt in unser Leben herein majestätisch, möchte man sagen, mit unbedingten, absoluten Forderungen - so wird eine unbefangene Selbstbeobachtung und Selbstbesinnung sagen - die moralische Weltordnung.",
      "Und man weiß, daß die moralischen Vorstellungen dasjenige sind, was über den Wert des Menschen entscheidet; ja, nicht nur über den Wert des Menschen innerhalb des menschlichen Zusammenlebens, sondern so entscheidet, daß man selbst sagen kann: Auch der, welcher sich der Unmoralität bezichtigen muß, wird, wenn er damit begnadet sein kann oder könnte, in einem besonderen Momente ruhig über sich nachzudenken, seinen eigenen Wert als Menschenwesen danach bestimmen, wie die in sein Bewußtsein hereinleuchtenden moralischen Vorstellungen sind. Das muß immer wieder betont werden, daß man diese zwei Vorstellungssysteme gehörig voneinander unterscheidet.",
      "Dies wird völlig anders in dem Augenblicke, wo man die höheren Welten betritt, wo man dazu gelangt, außerhalb seines physischen Leibes wahrzunehmen, zu beobachten, zu erleben, zu erfahren, und dadurch in höhere übersinnliche Welten eintritt. Zuerst beobachtet man ja, wenn man wirklich zu einem Beobachten gelangt, mit jenem Leibe, von dem ich gestern einiges angedeutet habe: mit dem elementarischen oder ätherischen Leibe. Dann betrachtet man die",
      "Welt - oder vielmehr eine zweite übersinnliche Welt - mit seinem astralischen Leibe. Und je weiter man hinaufsteigt in die höheren Welten, desto mehr verlieren die Vorstellungen, die Begriffe, die man sich erarbeitet, die man gewonnen hat in der gewöhnlichen physischen Welt, ihre Bedeutung.",
      "Sie müssen sich wandeln, damit wir in richtiger Weise das bezeichnen und verstehen können, was uns in den übersinnlichen höheren Welten entgegentritt. In der gewöhnlichen Welt des Sinnenseins haben wir nur eines, was uns an eine fundamentale Tatsache erinnern kann, die jeder hellsichtige Mensch kennt: man spricht in Sinnbildern, in Symbolen, so daß die Worte wiederum anklingen an das, was wieder erst in seiner Realität, in seiner Wirklichkeit in den höheren Welten erfahren wird.",
      "Wenn jemand das Wort gebraucht: Geiz oder Neid oder Haß «brenne», so ist in einem solchen Wort eigentlich etwas enthalten, was man zu jenen vielen wunderbaren Geheimnissen der sprachschöpferischen Tätigkeit rechnet, wo hereinleuchtet in das primitive, elementarische menschliche Bewußtsein dasjenige, was in seiner Wirklichkeit erst in den höheren Welten vorhanden ist. Denn jeder weiß, daß er, wenn er von brennendem Haß spricht, nicht ein Brennen meint, wie es das natürliche Brennen eines Feuers draußen in der natürlichen Welt ist; er weiß, daß er sozusagen im übertragenen Sinne spricht, und daß es ihm nichts helfen würde, wenn er Dinge und Vorgänge der Natur dadurch erklären wollte, daß er moralische Vorstellungen zu Hilfe rufen wollte.",
      "Sobald man von Vorgängen der höheren Welten spricht, spricht man nicht in demselben Sinne sinnbildlich oder in einem Anklange, wenn man solche Ausdrücke gebraucht. - Ich darf wohl daran erinnern, daß zweimal in dem Drama «Der Hüter der Schwelle» der Ausdruck gebraucht ist, daß gewisse seelische Vorgänge, Empfindungen, Wünsche «brennen» in den höheren Welten. Damit ist nicht etwas wie ein Sinnbild, sondern etwas ganz Reales, Wirkliches, real Spirituelles gemeint.",
      "Luzifer zum Beispiel würde niemals in demselben Sinne sagen: dieses oder jenes brenne ihn, wie ein Mensch im Sinnensein vom Haß sagen könnte, er brenne ihn; sondern Luzifer würde es sagen in wahrhaftem, ganz wirklichem Sinne. Was man nämlich in den übersinnlichen",
      "Welten vergleichen könnte mit der Naturordnung, mit den Naturvorgängen der sinnlichen Welt, steht in diesen übersinnlichen Welten in einem viel innigeren Zusammenhange mit dem, was man für diese Welten wiederum moralische Welten nennen kann, als diese beiden Vorstellungsreihen hier in der Sinneswelt zueinander stehen.",
      "Wir können uns sogleich einen Begriff von diesen beiden Vorstellungen bilden, wenn wir zu des Menschen elementarischem Leibe gehen. Solange wir beim physischen Leibe bleiben, können wir sagen, eine Hand könne sich erheben, um eine moralische Tat zu begehen.",
      "Wir sehen sie mit unseren sinnlichen Augen, untersuchen sie mit der zu der sinnlichen Welt gehörigen Wissenschaft, um ihre Funktionen zu erklären. Diese Erklärung der Hand innerhalb des Sinnenseins wird sich nicht wesentlich unterscheiden, ob wir es zu tun haben mit einer Hand, die ausholt zu einer moralischen oder zu einer unmoralischen Tat.",
      "Wie auch die Hand geformt ist, soweit sie überhaupt im Sinnensein erklärt werden kann: in das, was wir her- beitragen zur Erklärung der Hand, dürfen wir nicht hineinmischen, ob diese Hand gewöhnlich zu moralischen oder unmoralischen Taten ausholt. Anders liegt die Sache mit dem elementarischen Leibe des Menschen.",
      "Dieser elementarische Leib, zum Beispiel irgendein Glied desselben, erscheint für das hellseherische Bewußtsein unvollkommen ausgebildet. Und wenn wir uns fragen, warum in einem entsprechenden Fall dies bei einem Organ des elementarischen Leibes ist, wenn wir nach den wahren Ursachen fragen, so erscheint uns als der Grund einer solchen unvollkommenen Ausbildung zum Beispiel irgendein moralischer Fehler, irgendein moralischer Mangel, eine moralische Unvollkommenheit des Menschen.",
      "Im elementarischen Leibe drückt sich tatsächlich die moralische Qualität des Menschen schon in einer gewissen Weise aus. Noch deutlicher, noch intensiver aber drückt sie sich aus in dem astralischen Leibe.",
      "Während man also einem Menschen durchaus Unrecht täte, bei dem man annehmen wollte, daß irgendeine Verstümmelung der Ausdruck wäre von etwas Moralischem in ihm, ist es bei dem, was der moralischen Welt angehört, durchaus so, wenn wir die Worte Naturordnung,",
      "Naturvorgänge und moralische Ursachen ineinander- laufend denken, daß dort in den höheren Welten moralische Qualitäten wirkliche Naturursachen auch sind und sich ausdrücken in den Formen, in den Vorgängen dieser übersinnlichen Welten. Damit kein Mißverständnis entsteht, möchte ich noch ausdrücklich bemerken, daß die Ausbildung der höheren Organismen des Menschen, der höheren Leiber, wenn wir so sagen dürfen, des elementarischen, des astralischen Leibes, in ihrer Vollkommenheit oder Unvollkommenheit nichts zu tun haben braucht mit der vollkommenen oder unvollkommenen Ausbildung des physischen Leibes. Der Mensch kann, selbst von Geburt an, irgendein physisches Organ verkrüppelt ausgebildet haben, und das entsprechende ätherische Organ kann nicht nur dann ganz normal ausgebildet sein, sondern sogar unter Umständen vollkommener, in sich vollendeter ausgebildet sein, wenn das entsprechende physische Organ verkümmert oder verkrüppelt ist. Was also ganz und gar nicht anwendbar wäre für das Sinnensein, daß die moralischen Qualitäten ihren getreuen Ausdruck finden in den Formen des physischen Leibes, das ist ganz und gar der Fall für das, was auch schon vom Menschen den über- sinnlichen Welten angehört.",
      "So sehen wir, daß das, was für das Sinnensein gleichsain nebeneinander hergeht - Naturordnung und moralische Ordnung -, verwoben ist für die übersinnlichen Welten, so daß wir, wenn wir von einem elementarischen Leibesglied sprechen, gar wohl sagen können: diese oder jene Form ist bewirkt durch Haß. Der Haß drückt sich anders aus in dem betreffenden elementarischen Leibesglied als die Liebe. Das hat durchaus Sinn, ein solches Wort für die übersinnlichen Welten zu gebrauchen; das hat keinen Sinn, wenn man bei einer bloßen Naturerklärung in dem Sinnensein verbleiben will. Charakteristisch tritt uns diese Notwendigkeit der Begriffswandlung für die höheren Welten besonders zum Beispiel für das entgegen, was man im gewöhnlichen Sinnensein, im gewöhnlichen Leben zu den Begierden, zu den Wünschen rechnet. Wie treten im Sinnensein die Begierden, die Wünsche, die Emotionen auf? Sie treten so auf, daß wir sie gleichsam aus dem Innern des menschlichen Seelenwesens",
      "hervorgehen sehen. Wenn wir in einem Menschen eine besondere Begierde erregt finden, so erkennen wir daraus, wie sein Inneres gestimmt ist, wie dieses Innere aus sich diese Begierde heraustreibt, und daß vor allem das Seeleninnere maßgebend ist für die Artung von Begierden, die dieser Mensch hat. Denn wir wissen sehr wohl, daß zum Beispiel gegenüber einem Stück Kalbfleisch der eine Mensch ganz andere Begierden entwickelt als der andere; das hängt nicht von dem Kalbfleisch ab, sondern von dem, was der Mensch im Sinnensein in seinem Innern hat. Gegenüber einer Raffaelischen Madonna kann der eine Mensch vollständig kalt bleiben, während der andere eine ganze Welt von Gefühlen erlebt. Wir können daher sagen: im Innern des Menschen entzündet sich seine Begierdenwelt.",
      "Das wird anders, wenn wir die übersinnlichen Welten betreten. Was man für diese Welten Wünsche, Begierden, Emotionen nennen kann - es wäre nur ein leeres Geschwätz, zu sagen, daß man davon in diesen Welten nicht reden könne, denn Wünsche, Begierden und so weiter sind dort vorhanden -, das wird in der überwiegendsten Mehrzahl der Fälle immer durch Äußeres bewirkt, durch das, was das Wesen wirklich sieht, was es schaut. Daher liegt dem Hellseher in den übersinnlichen Welten viel weniger nahe dieses Hinblicken auf das Innere des Wesens, das er vor sich hat, um dessen Wünsche, Begierden und so weiter anzuschauen, sondern er wird die Umgebung dieses Wesens in der übersinnlichen Welt betrachten. Wenn er also sieht: da ist ein Wesen in der übersinnlichen Welt, und das hat Wünsche, Begierden, Emotionen - dann sieht er nicht so wie hier in der physischen Welt auf das Wesen selbst hin, sondern er sieht sich die Umgebung an; er untersucht: welche anderen Wesen halten sich dort in der Umgebung dieses Wesens auf? Und er wird immer sehen, daß je nachdem, was dort für Wesen in der Umgebung sind, auch die Begehrungen, die Wünsche, die Emotionen des Wesens sein werden, das da ist. Immer werden durch Äußeres ausgelöst die Wünsche, Begierden, Emotionen. Wie sich das macht, das kann Ihnen an einem Falle ganz besonders einleuchtend sein.",
      "Nehmen wir an, ein Mensch komme in die übersinnlichen Welten hinein, entweder indem er die ersten Stufen der Initiation durchmacht",
      "und dadurch in die höheren Welten eindringt, oder indem er durch die Pforte des Todes geht und auf diese Weise in die höheren Welten hineinkommt. Der Hellseher beobachtet ihn nun in den übersinnlichen Welten.",
      "Nehmen wir an, dieser Mensch hätte aus der Sinneswelt, weil das zu seinen Eigenschaften gehört, irgendeine Unvollkommenheit mitgenommen, irgend etwas, was er nicht kann, oder eine moralische Unvollkommenheit oder irgend etwas, was er verbrochen hat in der physischen Welt und was nun eine zehrende Erinnerung ist in den übersinnlichen Welten. Um dies zu suchen, kommt es für den Hellseher nicht so sehr darauf an, in das Seelen- innere dieses Menschen jetzt hineinzublicken, sondern die Umgebung anzuschauen.",
      "Warum? Weil ein solcher Seeleninhalt, ein solches Eigenschaftliches in der Seele, das man als eine Unvollkommenheit, als einen moralischen Defekt mitgenommen hat, etwas Reales, etwas Wirkliches bewirkt.",
      "Das leitet den Menschen, führt ihn, bringt ihn hin an einen gewissen Ort der übersinnlichen Welt. An welchen Ort? An den Ort, wo ein Wesen ist, welches in vollkommenem Zustande das hat, was man, wenn man dort ankommt, in unvollkommenem Zustande hat.",
      "Dieser moralische Defekt, dieses Bewußtsein von einer mangelnden Fähigkeit bewirkt also etwas Wirkliches, geleitet einen auf einen Weg, stellt einen zu einem Wesen, welches das in vollkommener Weise hat, was man selbst unvollkommen hat, worauf es gerade ankommt. Und nun ist man verurteilt, indem dieses Wesen einem gegenübergestellt ist, es fortwährend anzuschauen.",
      "Man kommt in den übersinnlichen Welten durch reale Vorgänge - nicht durch das, was man im Sinnensein Begierden nennt - in die Nähe von Wesenheiten, die alles das haben, was man nicht hat, die einem fortwährend zeigen, was einem fehlt. Schaut also der Hellseher dorthin, was da für Wesen sind in der Umgebung eines Menschen, so weiß er aus der objektiven Beobachtung, was dem Menschen fehlt, was ihm mangelt.",
      "Was man verurteilt ist fortwährend anzuschauen, in wessen Nähe man kommt, das steht, kann man sagen, als ein fortwährender Vorwurf da. Und dieser Vorwurf, der also draußen steht, bewirkt, daß in dem Wesen das entsteht, was man in den übersinnlichen Welten als eine Begierde bezeichnen",
      "könnte, als der Wunsch, anders zu werden, und was die Tätigkeit, die Kraft erzeugt, sich wirklich so durchzuarbeiten, daß man die Unvollkommenheit, den Fehler ablegt. Sagen Sie nicht, dann müßten ja die übersinnlichen Welten für alles, was wir fehlerhaft haben, das vollkommene Wesen zeigen. Diese Übersinnliche Welt ist wirklich so reich, daß sie uns für alle unsere Fehler die vollkommenen Wesen gegenüberstellen kann, ist viel reicher, als man es sich nach dem Sinnensein denkt. Oh, diese Welt ist schon so, daß sie den Menschen hinstellen kann vor irgendein Wesen, welches das in Vollkommenheit hat, was er selber in Unvollkommenheit hat. Das gibt einen Begriff, wie Wünsche, Begierden reale Kräfte sind, die unsere Wege bewirken in den übersinnlichen Welten, nicht als ob wir wie mit etwas Objektivem in unseren Wünschen dastehen und stehenbleiben können, sondern je nachdem wie wir sind, werden wir unseren Weg geführt und dort hingestellt, wo das, was wir nicht haben, uns als ein Reales oder als ein wirklicher Vorwurf entgegenscheint.",
      "Man könnte sehr leicht sagen: wenn das so ist, so wäre der Mensch in den übersinnlichen Welten völlig unfrei, denn dann stände er der Außenwelt gegenüber und müßte an sich so arbeiten, wie es die Außenwelt bewirkt. Wenn man aber in den übersinnlichen Welten beobachtet, dann stellt sich heraus: das eine Wesen empfindet den Vorwurf und beginnt zu arbeiten, so daß es sich der Vollkommenheit entgegenarbeitet; das andere Wesen aber läßt das bleiben, wehrt sich, etwas nachzuahmen, was ihm als Vorwurf vorgestellt ist. Dieses Wehren aber bewirkt in den übersinnlichen Welten etwas ganz anderes als im Sinnensein. Wenn sich ein Wesen wehrt, diese Nachfolge wirklich zu leisten, so wird es wieder hinweggedrängt und hingedrängt in ganz andere Welten, die ihm ungewohnt sind, in denen es sich nicht auskennt, wofür ihm die Lebensbedingungen fehlen; das heißt, es verurteilt sich ein solches Wesen zu einer Art Zerstörungsprozeß in sich selber. Man kann durchaus wählen zwischen dem Fruchtbaren, Fördernden, das einem gezeigt wird, und sich selber ihm entsprechend verhalten, oder man kann sich durchimpfen mit zerstörenden Kräften, wenn man sich ihm widersetzt. Freiheit hat man. Aber die Durcheinanderwirkung des",
      "Moralischen und dessen, was im übersinnlichen Raume vorgeht, findet durchaus statt.",
      "Ein weiteres Beispiel für so etwas ist, daß unsere Begriffe von schön und häßlich, wie wir sie mit vollem Rechte für die Sinneswelt haben, eigentlich nicht mehr angewendet werden können, sobald wir in die übersinnlichen Welten hinaufkommen, und zwar aus mehrfachen Gründen. Wenn wir in den übersinnlichen Welten wahrnehmen, so erblicken wir zunächst einen bedeutsamen Unterschied in bezug auf die Wesen, die uns dort entgegentreten.",
      "Von dem einen wird man - vermöge der intuitiven Erkenntnis> die man da haben kann - sagen können: Dieses Wesen, das du da anschaust, ist imstande, hat den Willen, alles, was es in sich hat, wirklich auch äußerlich in seiner äußeren Erscheinung darzuleben. Nehmen wir an, ein solches Wesen habe einen elementarischen Lichtleib, es gehöre zu den Wesen, die sich nicht in der Sinneswelt verkörpern, sondern nur in den höheren Welten einen Lichtleib annehmen oder dergleichen.",
      "Dieser Lichtleib kann der Ausdruck dessen sein, was es in seinem Innern ist. Es ist nicht wie ein Mensch im Sinnensein, der uns entgegentritt in einer bestimmten Form und der die mannigfaltigsten Gefühle, Empfindungen und so weiter in sich verbergen kann, so daß er sagen kann: Meine Gefühle sind für mich; was sich im Äußeren zeigt, das ist meine Naturgestalt; ich kann wohl das, was sich in meiner Seele zeigt, verbergen.",
      "So ist es für gewisse Wesen der übersinnlichen Welt nicht, sie zeigen in ihrer Gestalt den Unmittelbarsten Ausdruck dessen, was sie in sich tragen. In den Ingredienzien liegt offen zutage, was sie im Innern sind.",
      "Andere Wesen gibt es, welche das nicht können, ihr eigentliches Innere unmittelbar in ihrer äußeren übersinnlichen Erscheinung zur Darstellung, zur Offenbarung zu bringen. Diesen Wesen gegenüber hat das hellseherische Bewußtsein das Gefühl von etwas Abstoßendem, von etwas, wovon es weg möchte, von etwas, was preßt, was sogar recht widerwärtig sein kann.",
      "So kann man zweierlei Wesenheiten unterscheiden: solche, die voll Willens sind, ihr Inneres - wenn ich den Ausdruck gebrauchen darf - zur Schau zu tragen, das Innere darzuleben, und solche Wesen, denen gegenüber man das Gefühl hat: was sie zur",
      "Schau tragen, das ist recht verkrüppelt, denn was in ihnen sitzt, ist verborgen, das tritt nicht heraus. Beim Sinnensein des Menschen kann man nicht in demselben Grade sagen, wenn einer etwas verbergen kann und wenn sich dem anderen gleich alles auf die Lippen drängt: sie unterscheiden sich naturgemäß. Sie unterscheiden sich in ihrem Antlitz, aber nicht naturgemäß. Für die übersinnlichen Welten sind das zwei radikal andere Klassen von Wesenheiten: die einen, welche alles offenbaren, was sie in ihrem Innern haben, und ihnen gegenüber diejenigen, welche dies nicht offenbaren können. Wenn wir die Bezeichnung schön und häßlich gebrauchen wollen ungefähr mit dem Ausdruck, den wir in der Sinneswelt haben, so müssen wir sie für diese zwei Klassen von Wesenheiten gebrauchen. Man kommt in den übersinnlichen Welten nur dadurch zu Rande, daß man die Wesenheiten, welche alles offenbaren, schön nennen kann, denn man empfindet ihnen gegenüber ebenso wie einem schönen Bilde gegenüber. Und wie etwas Häßliches empfindet man die Wesen, welche das Innere nicht in dem Äußeren offenbaren. Schön und häßlich hängt, wenn man den Ausdruck gebrauchen darf, mit der Naturgrundlage dieser Wesenheiten zusammen. Was hat das zur Folge?",
      "Wenn das hellseherische Bewußtsein in eine Welt eintritt, wo es so gegenüber Schön und Häßlich empfinden muß, so muß es überhaupt vieles in seiner ganzen Empfindungsart ändern. Es ist dem Hellseher ganz natürlich, zu sagen, ein Wesen, welches alles, was es innen hat, offenbart, sei schön. Aber unmittelbar drängt sich dazu die andere Vorstellung: damit es schön sein kann, muß es aufrichtig, ehrlich sein! Es ist schön, weil es nichts verbirgt, weil es auf dem Antlitz trägt, was es in sich hat. Wahr und schön ist dasselbe, wenn man in die übersinnlichen Welten kommt. Und ein Wesen, das nicht sein Inneres offenbart, ist häßlich; das empfindet man unmittelbar im hellseherischen Bewußtsein. Aber man empfindet noch etwas anderes: es lügt einen an, es zeigt nicht, was es zeigen sollte! Das Häßliche ist zugleich das Lügnerische! Das Wahre, Aufrichtige und Ehrliche ist zugleich das Schöne, und das Häßliche das Lügnerische. Und man kommt in den übersinnlichen Welten dazu, daß die Trennung",
      "der Begriffe wahr und schön auf der einen Seite und häßlich und lügnerisch auf der anderen Seite jeden Sinn verliert. So muß man einem Wesen gegenüber den Ausdruck schön gebrauchen, wenn man die Empfindung hat: da ist etwas aufrichtig zu einem; und hat man die gegenteilige Empfindung, so muß man es häßlich nennen.",
      "Daraus sieht man, wie die moralischen und die ästhetischen Begriffe eine Verbindung eingehen, wenn man in die höheren Welten hinaufgelangt. Das ist überhaupt das Eigentümliche des Hinaufrükkens in die übersinnlichen Welten, daß die Begriffe zusammengehen, daß in bezug auf das, was in der physisch-sinnlichen Welt getrennt bezeichnet werden muß, Verschmelzungen, Zusammenfügungen entstehen. Daher muß man sich andere Empfindungsweisen aneignen, wenn man Bezeichnungen der Sinneswelt für Übersinnliche Wesenheiten gebraucht. Man ist fast immer genötigt, diese Dinge noch einfacher und noch mehr dem sinnlichen Bewußtsein genähert darzustellen, als es eigentlich einer vollständig richtigen Darstellung entsprechen kann, denn die Dinge komplizieren sich sehr. Wenn ich eben ausgeführt habe, wie sich die Begriffe von wahr, aufrichtig und schön auf der einen Seite und von häßlich und lügnerisch auf der anderen Seite verknüpfen, so müssen wir noch etwas anderes hinzufügen.",
      "Wenn man in die übersinnlichen Welten eindringt, kann man ein Wesen finden, welches man nach allen Begriffen, die man sich im Sinnensein angeeignet hat, als ein schönes Wesen bezeichnen muß, als ein herrliches Wesen vielleicht: schön, strahlend, herrlich. Nun hat man es vor sich. Es ist aber kein Beweis, daß es auch ein gutes Wesen ist, wenn es einem so entgegentritt, es kann ein ganz böses sein und einem in der hehrsten Engelsgestalt entgegentreten. Denn nach dem Begriffe von schön, den man sich in der Sinneswelt gebildet hat, nennt man ein solches Wesen in der übersinnlichen An- schauung schön. Wie sollte man es auch nicht! Wenn man es abgebildet finden würde in der Sinneswelt, würde man es mit vollem Rechte schön nennen. Ein solches Wesen kann das häßlichste sein, das es nur gibt; trotzdem kann es als ein schönes bezeichnet werden,",
      "wenn man bei den Bezeichnungen der Sinneswelt bleibt. Es kann ein ganz böses Wesen sein, kann die Bosheit und die Schlechtigkeit und die Unwahrheit, die einen anlügt, behalten, kann ein Teufel in Engelsgestalt sein. Das ist durchaus möglich in den übersinnlichen Welten. Nun kann sich durch mancherlei Weise, wovon wir noch sprechen werden, herausstellen, daß man nach und nach hinter die Sache kommt, wenn man sich mit dem hellseherischen Bewußtsein der Sache gegenüberstellt. Man hat also vor sich eine Engelsgestalt und kann sich jetzt sagen, wenn man es so weit gebracht hat, denkend bleiben zu können beim übersinnlichen Anschauen: Daß du jetzt einen Engel siehst oder irgendeine herrliche Gestalt, dadurch mußt du dich nicht täuschen lassen; das kann alles möglich sein, es kann ein Engel sein, kann aber auch ein Teufel sein. Nun kann man anfangen mit dem, was man so oft tun muß, wenn man hinaufrückt in die höheren Welten: mit einer gehörigen Selbstprüfung. Man kann mit sich zu Rate gehen und untersuchen, wieviel Eigenschaften von Selbstsinn, von Egoismus man in sich hat. Dann durchdringt sich die Seele mit mancherlei Bitternissen, dann kommt mancherlei Wermut in die Seele hinein. Aber dieses Bittere, Peinigende",
      "kann gerade dazu führen, daß man sich wieder eine kurze Zeit reinigt, daß man sich läutert in seinem Selbstsinn, in seinem Egoismus. Und wenn man dadurch zu dem Urteil kommt, wie wenig man eigentlich frei ist von dem Selbstsinn und daß man danach streben muß, frei zu werden, dann erleuchtet sich einem der ganze Prozeß, der sich abspielt im Seeleninnern. Wenn man es nun so weit gebracht hat, daß einem, wenn man solche Selbstbetrachtung anstellt, das nicht entfällt, was man anschaut - denn das wird in der Regel bei den ersten Schritten geschehen , so fängt unter Umständen der Engel an, gar kein Engel zu sein, sondern recht häßliche Formen anzunehmen, und man kann nach und nach dahinterkommen, daß man sich sagt: Dem Wesen, dem du da als einem bösen entgegengetreten bist, hast du die Möglichkeit gegeben, seine Bösartigkeit zum Ausdruck zu bringen, indem es dir erst eine ganz andere Gestalt vorgaukelte; aber du hast es gezwungen, dir seine wahre Gestalt zu zeigen, indem du dich mit reineren Gefühlen durchdrungen hast.",
      "So hat ein seelischer Vorgang in der übersinnlichen Welt ein Zwingendes, ein Kraftendes; so macht man es selber den Wesen möglich, einen anzulügen, oder man zwingt sie, einem ihre wahre Gestalt darzustellen. Wie man hineintritt in die übersinnliche Welt, mit welchen Qualitäten, danach stellt sie sich einem dar. Was man die Quelle der Täuschungen nennt, damit muß man noch ganz anders vorgehen, als es gewöhnlich geschieht. Es kann jemand in die übersinnlichen Welten hineintreten und allerlei Herrliches beschreiben. Wenn Sie ihm sagen, er hätte sich getäuscht, so wäre das nicht",
      "wahr; denn er hat es gesehen. Aber er hat nicht das gesehen, was er gesehen haben würde, wenn er das getan hätte, was ich eben beschrieben habe. Hätte er es so gemacht, so hätte er zugleich die Wahrheit gesehen.",
      "Denn von einem Teufel ist es schön, wenn er sich als Teufel darstellt, während es häßlich ist, wenn er eine Engelsgestalt darstellt. Man kann gar nicht anders als solche Begriffe sich anzueignen. So muß man sich vor allen Dingen abgewöhnen, wenn man in die übersinnlichen Welten hineintritt, die Dinge mit den Vorstellungen zu bezeichnen, die man gewonnen hat in der sinnlichen Welt.",
      "Wenn man dies, was man im Sinnensein gewonnen hat, beibehielte, so würde man erst zu der Gestalt, die einem so entgegentritt, sagen: Es ist ein schöner Engel -, und nachher: Es ist ein häßlicher Teufel! - So kann es aber das hellseherische Bewußtsein nicht ausdrücken, wenn man richtig charakterisieren will, sondern zu dem häßlichen Teufel muß man sagen: Es ist ein schöner Teufel -, trotzdem er nach sinnlichen Begriffen grundhäßlich ist. Dazu kommt man aber nicht dadurch, daß man einfach alle Begriffe auf den Kopf stellt, die man aus dem Sinnensein hat.",
      "Das wäre ein bequemer Weg. Dann könnte jemand zum Beispiel den Devachanplan dadurch beschreiben, daß er für alles, was in der Sinneswelt häßlich ist, schön setzt, für schön häßlich, für grün rot, für schwarz weiß und so weiter.",
      "So kann man es aber nicht machen, sondern die Begriffe müssen angeeignet sein im Erleben der übersinnlichen Welten. Man eignet sie sich so an wie die Anschauungen, die das heranreifende Kind von der Sinneswelt sich aneignet, nicht durch Theorien, sondern durch Erleben, und findet es dann völlig unnatürlich, einen",
      "Teufel häßlich zu nennen, der sich als Teufel darstellt, wenn man sich bewußt ist, daß man die Sprache der übersinnlichen Welten redet. Aber man muß sich eine solche Empfindungsweis`e aneignen, wenn man sich wirklich in den übersinnlichen Welten orientieren will, wenn man in ihnen sich auskennen und herumgehen will. Daher können Sie sich nun leicht eine Vorstellung machen, was gemeint ist, wenn man der Einfachheit halber sagt: Auf der einen Seite steht die Sinneswelt, auf der anderen Seite sind die übersinnlichen Welten; da kommt man aus dem Sinnensein uber die entsprechende Grenze in das übersinnliche Sein hinein. Geht man mit alledem, was man im Sinnensein gewonnen hat, da hinein, wendet man das an, was man gewonnen hat an Vorstellungen, Begriffen, Ideen aus der Sinneswelt, so ist alles unzutreffend; dann redet man lauter Verkehrtheiten. Man muß gründlich an der Grenze umlernen und zwar nicht theoretisch, sondern lebendig. Man kann das überhaupt nicht brauchen, was man sich in der Sinneswelt an Vorstellungen angeeignet hat, man muß es zurücklassen. Sie sehen, daß man vieles zurück- lassen muß, womit man recht innig verbunden ist in der Welt des Sinnenseins, und ich möchte Ihnen jetzt die Sache konkret-anschaulich, nicht aus Theorien heraus beschreiben.",
      "Nehmen wir an, jemand gelangt, nachdem er sich die Fähigkeit angeeignet hat, die gekennzeichnete Grenze zu überschreiten, von der Sinneswelt in die Übersinnliche Welt hinein. An der Grenze früge er sich: Was muß ich jetzt zurücklassen, wenn ich mich auskennen will in der übersinnlichen Welt? Ich muß zurücklassen - so kann er sich bei guter Selbstbesinnung sagen - eigentlich alles, was ich in den verschiedenen Inkarnationen vom Erdenurbeginn an bis in die Jetztzeit auf der Erde erlebt, gelernt, mir angeeignet habe. Das muß ich hier ablegen, denn ich betrete eine Welt, in welcher das, was man innerhalb der Inkarnationen lernen kann, keinen Sinn mehr hat. Es ist leicht, möchte ich sagen, so etwas auszusprechen; es ist leicht, so etwas anzuhören; es ist leicht, das in Begriffsabstraktionen zu fassen. Aber es ist eine ganze innere Welt, so etwas zu empfinden, zu fühlen, zu erleben: alles dort abzulegen wie die Kleider, was man in all den Inkarnationen in dem Sinnensein sich angeeignet hat, um",
      "in eine Welt hineinzugehen, innerhalb welcher das alles keinen Sinn mehr hat. Hat man diese Empfindung lebendig, dann hat man auch eine lebendige Erfahrung - wirklich nichts, was mit irgendeiner Theorie zusammenhängt -, wie man sie hat, wenn man in der wirklichen Welt eben einem wirklichen Menschen gegenübertritt, den man kennenlernt, indem er zu einem spricht, sich zu einem verhält, den man nicht kennenlernt, indem man sich von ihm Begriffe konstruiert, sondern indem er mit einem lebt. So steht man an der Grenze zwischen Sinnensein und Geistessein nicht einem Begriffssystem, sondern einer Realität gegenüber, die nur als eine übersinnliche Realität wirkt, aber so konkret, so lebendig wie ein Mensch: das ist der Hüter der Schwelle. Er ist da als ein konkretes, reales Wesen. Und lernt man ihn kennen, so lernt man ihn auch kennen als ein Wesen, das in die Kategorie von Wesen gehört, die in einer gewissen Weise mitgemacht haben das Leben vom Erdenurbeginn, dann aber nicht dasjenige mitgemacht haben, was man als Seelenwesen erlebt. Das ist das Wesen, das in dem Mysteriendrama «Der Hüter der Schwelle» dramatisiert werden sollte mit den Worten:",
      "Bekannt ist dir, der dieses Reiches Schwelle",
      "Behüten muß seit Erdenurbeginn,",
      "Was, um es zu betreten, Wesen brauchen,",
      "Die deiner Zeit und deiner Art gehören.",
      "Dieses «deiner Zeit und deiner Art» ist etwas, was aus dem Wesen der Sache heraus folgt. Andere Zeiten und andere Art haben die Menschen - andere Art und andere Zeiten haben die Wesen, die in einer gewissen Weise getrennt gegangen sind von den Wegen der Menschheit seit dem Erdenurbeginn. Da kommen wir mit einem Wesen zusammen, demgegenüber man sich sagt: Ich habe ein Wesen vor mir, das erfährt und erlebt vieles in der Welt; aber es beschäftigt sich nicht mit dem, was man an Liebe, an Schmerzen und Pein, aber auch an Fehlern und Unmoralischem auf der Erde erleben kann; es weiß nichts und will nichts wissen von dem, was sich abgespielt hat in der menschlichen Grundwesenheit bis jetzt. Die christliche Überlieferung",
      "drückt diesen Tatbestand dadurch aus, daß sie sagt: Vor dem Geheimnis der Menschwerdung verhüllten diese Wesenheiten ihr Antlitz. Eine ganze Welt ist in dem Unterschiede zwischen diesen Wesenheiten und den menschlichen Wesenheiten ausgedrückt.",
      "Und nun kommt eine Empfindung, die man unmittelbar hat, die sich so einstellt, wie wenn man einem Menschen gegenüber, der blonde Haare hat, die unmittelbare Empfindung hat: der hat blonde Haare. So tritt die Empfindung auf: Dadurch, daß du durch die Erdenkulturen durchgegangen bist, hast du dir notwendigerweise Unvollkommenheiten angeeignet, aber du mußt wieder zurückkommen zu dem ursprünglichen Zustand, mußt auf der Erde den Weg wieder zurückfinden, und dieses Wesen kann dir das zeigen, weil es deine Fehler nicht angenommen hat. Jetzt steht man einem Wesen gegenüber wie einem wirklichen Vorwurf, groß und grandios, wie ein Ansporn zu dem, was man nicht ist. Das zeigt einem dieses Wesen in lebendigster Weise, und da kann man sich ganz ausgefüllt fühlen vor dem Wesen von dem Wissen dessen, was man ist oder nicht ist. Da steht man dem lebendigen Vorwurf gegenüber. In die Klasse der Erzengel, der Archangeloi, wie wir sagen, gehört dieses Wesen. Es ist eine ganz reale Begegnung, und sie veranlaßt, daß einem plötzlich vor Augen tritt, was man als Erdenmensch im Sinnensein geworden ist. Selbsterkenntnis ist es zugleich im wahrhaftigen, umfassendsten Sinne. Sich selbst schaut man, wie man ist, und sich selbst schaut man, wie man nun werden soll!",
      "Zu diesem Schauen ist der Mensch nicht immer geeignet. Ich habe heute nur von der Begriffs- und Vorstellungswelt gesprochen, die abgelegt werden muß. Vieles andere muß ebenso abgelegt werden.",
      "Man muß, wenn man bis zum Hüter der Schwelle hinkommt, ei- gentlich alles ablegen, was man von sich weiß. Man muß nur dann noch etwas haben, um es durchzubringen. Darauf kommt es an! Daß man an der Grenze alles zurücklassen muß, das bewirkt ein inneres Erlebnis, dem man eben gewachsen sein muß, und die Vorbereitung bis zu dieser Stufe der Hellsichtigkeit muß darin bestehen und besteht bei einer richtigen Schulung darin - bei einer richtigen Schulung darf man nicht von Gefahren sprechen, denn gerade eine",
      "richtige Schulung beseitigt die Gefahren -, daß man ertragen lernt, was sonst schauervoll, schreckensvoll wäre. Zum Ertragen muß man kommen durch die Vorbereitung, denn das` ist die Grundkraft zu allem weiteren Erleben.",
      "Im gewöhnlichen Leben ist der Mensch nicht fähig, alles das zu ertragen, was man ertragen muß, wenn man vor dem Hüter der Schwelle steht. Denn der Hüter der Schwelle ist zu etwas höchst Sonderbarem genötigt, das beurteilt werden muß von dem Gesichtspunkt der übersinnlichen Welt, wenn es nicht mißverstanden werden soll.",
      "Der Mensch ist immer so, daß sich die Tätigkeiten der übersinnlichen Welt in ihm abspielen; er weiß nur nichts davon. Während wir denken, empfinden, wollen, läuft immer eine Tätigkeit des astralischen Leibes und ein Zusammenhang mit der astralen Welt nebenher.",
      "Aber der Mensch weiß nichts davon, weil er, wenn er das wissen würde, was seine eigenen Leiber sind, es nicht ertragen könnte und davon betäubt würde. Daher muß diese Wesenheit, wenn ihr der Mensch ohne genügende Vorbereitung gegenübertritt, ihm das alles verhüllen und sich selber verhüllen; sie muß einen Schleier ziehen vor die Übersinnliche Welt.",
      "Sie muß es tun zum Schutze des Menschen, der, im Sinnensein stehend, den Anblick nicht ertragen könnte. Da sehen wir so recht einen Begriff, den wir im Sinnensein nur moralisch beurteilen können, als Unmittelbarste Naturordnung.",
      "Der Schutz des Menschen vor dem Sehen der übersinnlichen Welt ist die Funktion des Hüters der Schwelle, die Erhaltung des Menschen in dem Zustande, in dem er ist, bevor er sich in genügender Weise auf die übersinnlichen Welten vorbereitet hat.",
      "So haben wir versucht, einige Vorstellungen zusammenzufügen, die uns hinführen können zu einem Begriff von dem Hüter der Schwelle. Solche Vorstellungen, solche Begriffe und Ideen, Erfahrungen und Erlebnisse versuchte ich in einem kleinen Buche zusammenzustellen, das in den nächsten Tagen Ihnen hier noch dargeboten werden soll und das Ihnen neben den Vorträgen selbst eine wichtige Hilfe sein kann. Es wird in eine Reihe von acht Meditationen zerfallen und wird sich so darstellen, daß der Leser, wenn er diese Meditationen durchmacht, dadurch für sein Seelenleben etwas",
      "haben wird. Einige von den Vorstellungen, die uns zum Hüter der Schwelle hinführen können, versuchte ich heute zu charakterisieren. Von diesem ausgehend werden wir versuchen, an dem Hüter der Schwelle vorbeigehend, einige Einblicke und Ausblicke zu charakterisieren, um dann noch tiefer die Christus-Wesenheit und die Christus-Initiation verstehen zu können."
    ],
    "sentences": [
      [
        "Wenn wir von der Initiation und ihrer Bedeutung für das ganze menschliche Leben und für die menschliche Entwickelung sprechen wollen, müssen wir in das Wesen dessen, um was es sich eigentlich handelt, aus denjenigen Begriffen und Vorstellungen heraus einzudringen versuchen, welche nun einmal notwendig sind, um die über- sinnlichen Welten überhaupt in richtiger Art zu charakterisieren.",
        "Es ist ja begreiflich, daß die menschliche Seele auf jeder Stufe ihrer Entwickelung die allertiefste Sehnsucht danach hat, etwas darüber zu erfahren, wie es in jenen Welten aussieht, denen man in mehr oder weniger berechtigter Weise das Prädikat der Ewigkeit beilegen kann."
      ],
      [
        "Daher muß es auch begreiflich erscheinen, daß die menschlichen Seelen danach trachten, ohne viel Vorbereitung erst mit den Vorstellungen, mit den Begriffen, die man im Sinnensein hat, in diese höheren Welten hineinzudringen.",
        "Ich sage ausdrücklich: das ist begreiflich."
      ],
      [
        "Und dem kann auch in einer gewissen Weise entsprochen werden da, wo es sich um Befriedigung der Ewigkeitssehnsucht in diesen oder jenen Religionsbekenntnissen handelt.",
        "Wenn es sich aber in wahrhaft theosophischem Sinne darum handelt, tiefer in den Urquell alles Geistigen und damit namentlich in den Urquell alles seelischen Lebens einzudringen, dann muß man - nach und nach wenigstens - sich befreunden mit der Notwendigkeit, seine Vorstellungen, seine Begriffe in einer gewissen Weise umzuwandeln, bevor man sich richtige Ideen von den höheren, den übersinnlichen Welten machen will."
      ],
      [
        "Weil dies - wie wir in den nächsten Vorträgen sehen werden - insbesondere zur Charakteristik der eigentlichen ChristusErscheinung notwendig ist, sei es mir heute gestattet, einiges über die notwendige Umwandlung und Umformung des menschlichen Vorstellungslebens zu sprechen, wenn der Mensch hinaufdringen will zu Ideen über die übersinnlichen Welten."
      ],
      [
        "Damit muß man sich schon einmal bekanntmachen, daß in den übersinnlichen Welten alles anders ist als in dem Sinnensein, denn"
      ],
      [
        "eine genaue Wiederholung eines Weltendaseins findet sich eigentlich nirgends im Universum.",
        "Wenn nun alles anders ist, warum sollte dann durchaus angenommen werden, daß die menschlichen Vorstellungen und Begriffe für die höheren Welten in gleichem Maße gültig seien, wie sie gültig sind für das Sinnensein?",
        "Das sind sie eben nicht.",
        "Wer den praktischen Aufstieg in diejenigen Welten, welche die Initiation eröffnet, wirklich vollführt, das heißt wer Erfahrungen hat im übersinnlichen Erleben, der weiß, wie wir gleich hören werden, daß er nicht nur vieles sonstiges an sich wandeln muß, ich könnte hier gleich sprechen: zurücklassen muß beim Hüter der Schwelle, sondern auch viele von seinen Gewohnheiten, Vorstellungen, Begriffen und Ideen dort ablegen muß, bevor er in die übersinnlichen, höheren Welten eindringen kann."
      ],
      [
        "Vor allen Dingen wollen wir ausgehen von gewissen Vorstellungen, die uns ja alle im Sinnensein beherrschen müssen.",
        "Ein Begriffspaar, möchte ich sagen, zwei Begriffssysteme sind da besonders ausschlaggebend.",
        "Sie stehen für unser Sinnensein nebeneinander, laufen nebeneinander her.",
        "Das eine ist alles, was wir uns an Vorstellungen machen über die natürliche Welt, über die Naturgesetze, Naturkräfte.",
        "Neben alledem, was wir uns darüber an Vorstellungen bilden, steht für unser gewöhnliches Leben im Sinnensein das, was wir nennen die moralische Weltordnung, die Summe unserer moralischen Vorstellungen, Begriffe und Ideen.",
        "Bei einer richtigen Selbstbesinnung wird der Mensch sehr bald darauf verfallen, daß er für das Sinnensein diese beiden Begriffssysteme - Naturordnung und moralische Weltordnung - auseinanderhalten müsse.",
        "Wenn wir eine Pflanze erklären - nehmen wir an, wir haben eine Giftpflanze vor uns -, so erklären wir sie aus den Naturkräften, aus den Naturgesetzen heraus.",
        "Und ich möchte sagen, wir verderben uns die Erklärung der Pflanze nicht dadurch, daß wir die Pflanze dafür moralisch verantwortlich machen, daß sie eine Giftpflanze ist.",
        "Wir halten dafür, daß es zum gesunden Denken innerhalb des Sinnenseins bei den Erklärungen des natürlichen Daseins gehört, uns zunächst von dem zu emanzipieren, was wir die moralischen Begriffe und Ideen nennen.",
        "Wir wissen ja, daß wir diese Art von Emanzipation selbst noch üben"
      ],
      [
        "müssen, wenn wir zu unbefangenen, objektiven Vorstellungen im Tierreiche kommen wollen.",
        "Es hätte keinen Sinn, so fühlen und empfinden wir, den Löwen für seine Grausamkeit ebenso verantwortlich zu machen, wie wir einen Menschen für seine Grausamkeit verantwortlich machen."
      ],
      [
        "Und wenn viele heutige Naturerklärer schon im Tierreiche so etwas wie moralische Begriffe finden, ich möchte sagen, mehr nach dem Geschmack als nach einer wahrhaftigen Notwendigkeit, so mag das schon in einem gewissen Sinne berechtigt sein.",
        "Aber man kann doch nur sprechen von einem Anklang an moralische Vorstellungen bei dem, was die Tiere tun, was im Tierreiche geschieht."
      ],
      [
        "Naturerklärung erfordert, wenn wir sie rein entwickeln sollen, ein Emanzipieren von moralischen Vorstellungen und Begriffen, wenn wir mit unseren Erklärungen unmittelbar im Sinnensein verbleiben wollen.",
        "Dann aber tritt in unser Leben herein majestätisch, möchte man sagen, mit unbedingten, absoluten Forderungen - so wird eine unbefangene Selbstbeobachtung und Selbstbesinnung sagen - die moralische Weltordnung."
      ],
      [
        "Und man weiß, daß die moralischen Vorstellungen dasjenige sind, was über den Wert des Menschen entscheidet; ja, nicht nur über den Wert des Menschen innerhalb des menschlichen Zusammenlebens, sondern so entscheidet, daß man selbst sagen kann: Auch der, welcher sich der Unmoralität bezichtigen muß, wird, wenn er damit begnadet sein kann oder könnte, in einem besonderen Momente ruhig über sich nachzudenken, seinen eigenen Wert als Menschenwesen danach bestimmen, wie die in sein Bewußtsein hereinleuchtenden moralischen Vorstellungen sind.",
        "Das muß immer wieder betont werden, daß man diese zwei Vorstellungssysteme gehörig voneinander unterscheidet."
      ],
      [
        "Dies wird völlig anders in dem Augenblicke, wo man die höheren Welten betritt, wo man dazu gelangt, außerhalb seines physischen Leibes wahrzunehmen, zu beobachten, zu erleben, zu erfahren, und dadurch in höhere übersinnliche Welten eintritt.",
        "Zuerst beobachtet man ja, wenn man wirklich zu einem Beobachten gelangt, mit jenem Leibe, von dem ich gestern einiges angedeutet habe: mit dem elementarischen oder ätherischen Leibe.",
        "Dann betrachtet man die"
      ],
      [
        "Welt - oder vielmehr eine zweite übersinnliche Welt - mit seinem astralischen Leibe.",
        "Und je weiter man hinaufsteigt in die höheren Welten, desto mehr verlieren die Vorstellungen, die Begriffe, die man sich erarbeitet, die man gewonnen hat in der gewöhnlichen physischen Welt, ihre Bedeutung."
      ],
      [
        "Sie müssen sich wandeln, damit wir in richtiger Weise das bezeichnen und verstehen können, was uns in den übersinnlichen höheren Welten entgegentritt.",
        "In der gewöhnlichen Welt des Sinnenseins haben wir nur eines, was uns an eine fundamentale Tatsache erinnern kann, die jeder hellsichtige Mensch kennt: man spricht in Sinnbildern, in Symbolen, so daß die Worte wiederum anklingen an das, was wieder erst in seiner Realität, in seiner Wirklichkeit in den höheren Welten erfahren wird."
      ],
      [
        "Wenn jemand das Wort gebraucht: Geiz oder Neid oder Haß «brenne», so ist in einem solchen Wort eigentlich etwas enthalten, was man zu jenen vielen wunderbaren Geheimnissen der sprachschöpferischen Tätigkeit rechnet, wo hereinleuchtet in das primitive, elementarische menschliche Bewußtsein dasjenige, was in seiner Wirklichkeit erst in den höheren Welten vorhanden ist.",
        "Denn jeder weiß, daß er, wenn er von brennendem Haß spricht, nicht ein Brennen meint, wie es das natürliche Brennen eines Feuers draußen in der natürlichen Welt ist; er weiß, daß er sozusagen im übertragenen Sinne spricht, und daß es ihm nichts helfen würde, wenn er Dinge und Vorgänge der Natur dadurch erklären wollte, daß er moralische Vorstellungen zu Hilfe rufen wollte."
      ],
      [
        "Sobald man von Vorgängen der höheren Welten spricht, spricht man nicht in demselben Sinne sinnbildlich oder in einem Anklange, wenn man solche Ausdrücke gebraucht. - Ich darf wohl daran erinnern, daß zweimal in dem Drama «Der Hüter der Schwelle» der Ausdruck gebraucht ist, daß gewisse seelische Vorgänge, Empfindungen, Wünsche «brennen» in den höheren Welten.",
        "Damit ist nicht etwas wie ein Sinnbild, sondern etwas ganz Reales, Wirkliches, real Spirituelles gemeint."
      ],
      [
        "Luzifer zum Beispiel würde niemals in demselben Sinne sagen: dieses oder jenes brenne ihn, wie ein Mensch im Sinnensein vom Haß sagen könnte, er brenne ihn; sondern Luzifer würde es sagen in wahrhaftem, ganz wirklichem Sinne.",
        "Was man nämlich in den übersinnlichen"
      ],
      [
        "Welten vergleichen könnte mit der Naturordnung, mit den Naturvorgängen der sinnlichen Welt, steht in diesen übersinnlichen Welten in einem viel innigeren Zusammenhange mit dem, was man für diese Welten wiederum moralische Welten nennen kann, als diese beiden Vorstellungsreihen hier in der Sinneswelt zueinander stehen."
      ],
      [
        "Wir können uns sogleich einen Begriff von diesen beiden Vorstellungen bilden, wenn wir zu des Menschen elementarischem Leibe gehen.",
        "Solange wir beim physischen Leibe bleiben, können wir sagen, eine Hand könne sich erheben, um eine moralische Tat zu begehen."
      ],
      [
        "Wir sehen sie mit unseren sinnlichen Augen, untersuchen sie mit der zu der sinnlichen Welt gehörigen Wissenschaft, um ihre Funktionen zu erklären.",
        "Diese Erklärung der Hand innerhalb des Sinnenseins wird sich nicht wesentlich unterscheiden, ob wir es zu tun haben mit einer Hand, die ausholt zu einer moralischen oder zu einer unmoralischen Tat."
      ],
      [
        "Wie auch die Hand geformt ist, soweit sie überhaupt im Sinnensein erklärt werden kann: in das, was wir her- beitragen zur Erklärung der Hand, dürfen wir nicht hineinmischen, ob diese Hand gewöhnlich zu moralischen oder unmoralischen Taten ausholt.",
        "Anders liegt die Sache mit dem elementarischen Leibe des Menschen."
      ],
      [
        "Dieser elementarische Leib, zum Beispiel irgendein Glied desselben, erscheint für das hellseherische Bewußtsein unvollkommen ausgebildet.",
        "Und wenn wir uns fragen, warum in einem entsprechenden Fall dies bei einem Organ des elementarischen Leibes ist, wenn wir nach den wahren Ursachen fragen, so erscheint uns als der Grund einer solchen unvollkommenen Ausbildung zum Beispiel irgendein moralischer Fehler, irgendein moralischer Mangel, eine moralische Unvollkommenheit des Menschen."
      ],
      [
        "Im elementarischen Leibe drückt sich tatsächlich die moralische Qualität des Menschen schon in einer gewissen Weise aus.",
        "Noch deutlicher, noch intensiver aber drückt sie sich aus in dem astralischen Leibe."
      ],
      [
        "Während man also einem Menschen durchaus Unrecht täte, bei dem man annehmen wollte, daß irgendeine Verstümmelung der Ausdruck wäre von etwas Moralischem in ihm, ist es bei dem, was der moralischen Welt angehört, durchaus so, wenn wir die Worte Naturordnung,"
      ],
      [
        "Naturvorgänge und moralische Ursachen ineinander- laufend denken, daß dort in den höheren Welten moralische Qualitäten wirkliche Naturursachen auch sind und sich ausdrücken in den Formen, in den Vorgängen dieser übersinnlichen Welten.",
        "Damit kein Mißverständnis entsteht, möchte ich noch ausdrücklich bemerken, daß die Ausbildung der höheren Organismen des Menschen, der höheren Leiber, wenn wir so sagen dürfen, des elementarischen, des astralischen Leibes, in ihrer Vollkommenheit oder Unvollkommenheit nichts zu tun haben braucht mit der vollkommenen oder unvollkommenen Ausbildung des physischen Leibes.",
        "Der Mensch kann, selbst von Geburt an, irgendein physisches Organ verkrüppelt ausgebildet haben, und das entsprechende ätherische Organ kann nicht nur dann ganz normal ausgebildet sein, sondern sogar unter Umständen vollkommener, in sich vollendeter ausgebildet sein, wenn das entsprechende physische Organ verkümmert oder verkrüppelt ist.",
        "Was also ganz und gar nicht anwendbar wäre für das Sinnensein, daß die moralischen Qualitäten ihren getreuen Ausdruck finden in den Formen des physischen Leibes, das ist ganz und gar der Fall für das, was auch schon vom Menschen den über- sinnlichen Welten angehört."
      ],
      [
        "So sehen wir, daß das, was für das Sinnensein gleichsain nebeneinander hergeht - Naturordnung und moralische Ordnung -, verwoben ist für die übersinnlichen Welten, so daß wir, wenn wir von einem elementarischen Leibesglied sprechen, gar wohl sagen können: diese oder jene Form ist bewirkt durch Haß.",
        "Der Haß drückt sich anders aus in dem betreffenden elementarischen Leibesglied als die Liebe.",
        "Das hat durchaus Sinn, ein solches Wort für die übersinnlichen Welten zu gebrauchen; das hat keinen Sinn, wenn man bei einer bloßen Naturerklärung in dem Sinnensein verbleiben will.",
        "Charakteristisch tritt uns diese Notwendigkeit der Begriffswandlung für die höheren Welten besonders zum Beispiel für das entgegen, was man im gewöhnlichen Sinnensein, im gewöhnlichen Leben zu den Begierden, zu den Wünschen rechnet.",
        "Wie treten im Sinnensein die Begierden, die Wünsche, die Emotionen auf?",
        "Sie treten so auf, daß wir sie gleichsam aus dem Innern des menschlichen Seelenwesens"
      ],
      [
        "hervorgehen sehen.",
        "Wenn wir in einem Menschen eine besondere Begierde erregt finden, so erkennen wir daraus, wie sein Inneres gestimmt ist, wie dieses Innere aus sich diese Begierde heraustreibt, und daß vor allem das Seeleninnere maßgebend ist für die Artung von Begierden, die dieser Mensch hat.",
        "Denn wir wissen sehr wohl, daß zum Beispiel gegenüber einem Stück Kalbfleisch der eine Mensch ganz andere Begierden entwickelt als der andere; das hängt nicht von dem Kalbfleisch ab, sondern von dem, was der Mensch im Sinnensein in seinem Innern hat.",
        "Gegenüber einer Raffaelischen Madonna kann der eine Mensch vollständig kalt bleiben, während der andere eine ganze Welt von Gefühlen erlebt.",
        "Wir können daher sagen: im Innern des Menschen entzündet sich seine Begierdenwelt."
      ],
      [
        "Das wird anders, wenn wir die übersinnlichen Welten betreten.",
        "Was man für diese Welten Wünsche, Begierden, Emotionen nennen kann - es wäre nur ein leeres Geschwätz, zu sagen, daß man davon in diesen Welten nicht reden könne, denn Wünsche, Begierden und so weiter sind dort vorhanden -, das wird in der überwiegendsten Mehrzahl der Fälle immer durch Äußeres bewirkt, durch das, was das Wesen wirklich sieht, was es schaut.",
        "Daher liegt dem Hellseher in den übersinnlichen Welten viel weniger nahe dieses Hinblicken auf das Innere des Wesens, das er vor sich hat, um dessen Wünsche, Begierden und so weiter anzuschauen, sondern er wird die Umgebung dieses Wesens in der übersinnlichen Welt betrachten.",
        "Wenn er also sieht: da ist ein Wesen in der übersinnlichen Welt, und das hat Wünsche, Begierden, Emotionen - dann sieht er nicht so wie hier in der physischen Welt auf das Wesen selbst hin, sondern er sieht sich die Umgebung an; er untersucht: welche anderen Wesen halten sich dort in der Umgebung dieses Wesens auf?",
        "Und er wird immer sehen, daß je nachdem, was dort für Wesen in der Umgebung sind, auch die Begehrungen, die Wünsche, die Emotionen des Wesens sein werden, das da ist.",
        "Immer werden durch Äußeres ausgelöst die Wünsche, Begierden, Emotionen.",
        "Wie sich das macht, das kann Ihnen an einem Falle ganz besonders einleuchtend sein."
      ],
      [
        "Nehmen wir an, ein Mensch komme in die übersinnlichen Welten hinein, entweder indem er die ersten Stufen der Initiation durchmacht"
      ],
      [
        "und dadurch in die höheren Welten eindringt, oder indem er durch die Pforte des Todes geht und auf diese Weise in die höheren Welten hineinkommt.",
        "Der Hellseher beobachtet ihn nun in den übersinnlichen Welten."
      ],
      [
        "Nehmen wir an, dieser Mensch hätte aus der Sinneswelt, weil das zu seinen Eigenschaften gehört, irgendeine Unvollkommenheit mitgenommen, irgend etwas, was er nicht kann, oder eine moralische Unvollkommenheit oder irgend etwas, was er verbrochen hat in der physischen Welt und was nun eine zehrende Erinnerung ist in den übersinnlichen Welten.",
        "Um dies zu suchen, kommt es für den Hellseher nicht so sehr darauf an, in das Seelen- innere dieses Menschen jetzt hineinzublicken, sondern die Umgebung anzuschauen."
      ],
      [
        "Warum?",
        "Weil ein solcher Seeleninhalt, ein solches Eigenschaftliches in der Seele, das man als eine Unvollkommenheit, als einen moralischen Defekt mitgenommen hat, etwas Reales, etwas Wirkliches bewirkt."
      ],
      [
        "Das leitet den Menschen, führt ihn, bringt ihn hin an einen gewissen Ort der übersinnlichen Welt.",
        "An welchen Ort?",
        "An den Ort, wo ein Wesen ist, welches in vollkommenem Zustande das hat, was man, wenn man dort ankommt, in unvollkommenem Zustande hat."
      ],
      [
        "Dieser moralische Defekt, dieses Bewußtsein von einer mangelnden Fähigkeit bewirkt also etwas Wirkliches, geleitet einen auf einen Weg, stellt einen zu einem Wesen, welches das in vollkommener Weise hat, was man selbst unvollkommen hat, worauf es gerade ankommt.",
        "Und nun ist man verurteilt, indem dieses Wesen einem gegenübergestellt ist, es fortwährend anzuschauen."
      ],
      [
        "Man kommt in den übersinnlichen Welten durch reale Vorgänge - nicht durch das, was man im Sinnensein Begierden nennt - in die Nähe von Wesenheiten, die alles das haben, was man nicht hat, die einem fortwährend zeigen, was einem fehlt.",
        "Schaut also der Hellseher dorthin, was da für Wesen sind in der Umgebung eines Menschen, so weiß er aus der objektiven Beobachtung, was dem Menschen fehlt, was ihm mangelt."
      ],
      [
        "Was man verurteilt ist fortwährend anzuschauen, in wessen Nähe man kommt, das steht, kann man sagen, als ein fortwährender Vorwurf da.",
        "Und dieser Vorwurf, der also draußen steht, bewirkt, daß in dem Wesen das entsteht, was man in den übersinnlichen Welten als eine Begierde bezeichnen"
      ],
      [
        "könnte, als der Wunsch, anders zu werden, und was die Tätigkeit, die Kraft erzeugt, sich wirklich so durchzuarbeiten, daß man die Unvollkommenheit, den Fehler ablegt.",
        "Sagen Sie nicht, dann müßten ja die übersinnlichen Welten für alles, was wir fehlerhaft haben, das vollkommene Wesen zeigen.",
        "Diese Übersinnliche Welt ist wirklich so reich, daß sie uns für alle unsere Fehler die vollkommenen Wesen gegenüberstellen kann, ist viel reicher, als man es sich nach dem Sinnensein denkt.",
        "Oh, diese Welt ist schon so, daß sie den Menschen hinstellen kann vor irgendein Wesen, welches das in Vollkommenheit hat, was er selber in Unvollkommenheit hat.",
        "Das gibt einen Begriff, wie Wünsche, Begierden reale Kräfte sind, die unsere Wege bewirken in den übersinnlichen Welten, nicht als ob wir wie mit etwas Objektivem in unseren Wünschen dastehen und stehenbleiben können, sondern je nachdem wie wir sind, werden wir unseren Weg geführt und dort hingestellt, wo das, was wir nicht haben, uns als ein Reales oder als ein wirklicher Vorwurf entgegenscheint."
      ],
      [
        "Man könnte sehr leicht sagen: wenn das so ist, so wäre der Mensch in den übersinnlichen Welten völlig unfrei, denn dann stände er der Außenwelt gegenüber und müßte an sich so arbeiten, wie es die Außenwelt bewirkt.",
        "Wenn man aber in den übersinnlichen Welten beobachtet, dann stellt sich heraus: das eine Wesen empfindet den Vorwurf und beginnt zu arbeiten, so daß es sich der Vollkommenheit entgegenarbeitet; das andere Wesen aber läßt das bleiben, wehrt sich, etwas nachzuahmen, was ihm als Vorwurf vorgestellt ist.",
        "Dieses Wehren aber bewirkt in den übersinnlichen Welten etwas ganz anderes als im Sinnensein.",
        "Wenn sich ein Wesen wehrt, diese Nachfolge wirklich zu leisten, so wird es wieder hinweggedrängt und hingedrängt in ganz andere Welten, die ihm ungewohnt sind, in denen es sich nicht auskennt, wofür ihm die Lebensbedingungen fehlen; das heißt, es verurteilt sich ein solches Wesen zu einer Art Zerstörungsprozeß in sich selber.",
        "Man kann durchaus wählen zwischen dem Fruchtbaren, Fördernden, das einem gezeigt wird, und sich selber ihm entsprechend verhalten, oder man kann sich durchimpfen mit zerstörenden Kräften, wenn man sich ihm widersetzt.",
        "Freiheit hat man.",
        "Aber die Durcheinanderwirkung des"
      ],
      [
        "Moralischen und dessen, was im übersinnlichen Raume vorgeht, findet durchaus statt."
      ],
      [
        "Ein weiteres Beispiel für so etwas ist, daß unsere Begriffe von schön und häßlich, wie wir sie mit vollem Rechte für die Sinneswelt haben, eigentlich nicht mehr angewendet werden können, sobald wir in die übersinnlichen Welten hinaufkommen, und zwar aus mehrfachen Gründen.",
        "Wenn wir in den übersinnlichen Welten wahrnehmen, so erblicken wir zunächst einen bedeutsamen Unterschied in bezug auf die Wesen, die uns dort entgegentreten."
      ],
      [
        "Von dem einen wird man - vermöge der intuitiven Erkenntnis> die man da haben kann - sagen können: Dieses Wesen, das du da anschaust, ist imstande, hat den Willen, alles, was es in sich hat, wirklich auch äußerlich in seiner äußeren Erscheinung darzuleben.",
        "Nehmen wir an, ein solches Wesen habe einen elementarischen Lichtleib, es gehöre zu den Wesen, die sich nicht in der Sinneswelt verkörpern, sondern nur in den höheren Welten einen Lichtleib annehmen oder dergleichen."
      ],
      [
        "Dieser Lichtleib kann der Ausdruck dessen sein, was es in seinem Innern ist.",
        "Es ist nicht wie ein Mensch im Sinnensein, der uns entgegentritt in einer bestimmten Form und der die mannigfaltigsten Gefühle, Empfindungen und so weiter in sich verbergen kann, so daß er sagen kann: Meine Gefühle sind für mich; was sich im Äußeren zeigt, das ist meine Naturgestalt; ich kann wohl das, was sich in meiner Seele zeigt, verbergen."
      ],
      [
        "So ist es für gewisse Wesen der übersinnlichen Welt nicht, sie zeigen in ihrer Gestalt den Unmittelbarsten Ausdruck dessen, was sie in sich tragen.",
        "In den Ingredienzien liegt offen zutage, was sie im Innern sind."
      ],
      [
        "Andere Wesen gibt es, welche das nicht können, ihr eigentliches Innere unmittelbar in ihrer äußeren übersinnlichen Erscheinung zur Darstellung, zur Offenbarung zu bringen.",
        "Diesen Wesen gegenüber hat das hellseherische Bewußtsein das Gefühl von etwas Abstoßendem, von etwas, wovon es weg möchte, von etwas, was preßt, was sogar recht widerwärtig sein kann."
      ],
      [
        "So kann man zweierlei Wesenheiten unterscheiden: solche, die voll Willens sind, ihr Inneres - wenn ich den Ausdruck gebrauchen darf - zur Schau zu tragen, das Innere darzuleben, und solche Wesen, denen gegenüber man das Gefühl hat: was sie zur"
      ],
      [
        "Schau tragen, das ist recht verkrüppelt, denn was in ihnen sitzt, ist verborgen, das tritt nicht heraus.",
        "Beim Sinnensein des Menschen kann man nicht in demselben Grade sagen, wenn einer etwas verbergen kann und wenn sich dem anderen gleich alles auf die Lippen drängt: sie unterscheiden sich naturgemäß.",
        "Sie unterscheiden sich in ihrem Antlitz, aber nicht naturgemäß.",
        "Für die übersinnlichen Welten sind das zwei radikal andere Klassen von Wesenheiten: die einen, welche alles offenbaren, was sie in ihrem Innern haben, und ihnen gegenüber diejenigen, welche dies nicht offenbaren können.",
        "Wenn wir die Bezeichnung schön und häßlich gebrauchen wollen ungefähr mit dem Ausdruck, den wir in der Sinneswelt haben, so müssen wir sie für diese zwei Klassen von Wesenheiten gebrauchen.",
        "Man kommt in den übersinnlichen Welten nur dadurch zu Rande, daß man die Wesenheiten, welche alles offenbaren, schön nennen kann, denn man empfindet ihnen gegenüber ebenso wie einem schönen Bilde gegenüber.",
        "Und wie etwas Häßliches empfindet man die Wesen, welche das Innere nicht in dem Äußeren offenbaren.",
        "Schön und häßlich hängt, wenn man den Ausdruck gebrauchen darf, mit der Naturgrundlage dieser Wesenheiten zusammen.",
        "Was hat das zur Folge?"
      ],
      [
        "Wenn das hellseherische Bewußtsein in eine Welt eintritt, wo es so gegenüber Schön und Häßlich empfinden muß, so muß es überhaupt vieles in seiner ganzen Empfindungsart ändern.",
        "Es ist dem Hellseher ganz natürlich, zu sagen, ein Wesen, welches alles, was es innen hat, offenbart, sei schön.",
        "Aber unmittelbar drängt sich dazu die andere Vorstellung: damit es schön sein kann, muß es aufrichtig, ehrlich sein!",
        "Es ist schön, weil es nichts verbirgt, weil es auf dem Antlitz trägt, was es in sich hat.",
        "Wahr und schön ist dasselbe, wenn man in die übersinnlichen Welten kommt.",
        "Und ein Wesen, das nicht sein Inneres offenbart, ist häßlich; das empfindet man unmittelbar im hellseherischen Bewußtsein.",
        "Aber man empfindet noch etwas anderes: es lügt einen an, es zeigt nicht, was es zeigen sollte!",
        "Das Häßliche ist zugleich das Lügnerische!",
        "Das Wahre, Aufrichtige und Ehrliche ist zugleich das Schöne, und das Häßliche das Lügnerische.",
        "Und man kommt in den übersinnlichen Welten dazu, daß die Trennung"
      ],
      [
        "der Begriffe wahr und schön auf der einen Seite und häßlich und lügnerisch auf der anderen Seite jeden Sinn verliert.",
        "So muß man einem Wesen gegenüber den Ausdruck schön gebrauchen, wenn man die Empfindung hat: da ist etwas aufrichtig zu einem; und hat man die gegenteilige Empfindung, so muß man es häßlich nennen."
      ],
      [
        "Daraus sieht man, wie die moralischen und die ästhetischen Begriffe eine Verbindung eingehen, wenn man in die höheren Welten hinaufgelangt.",
        "Das ist überhaupt das Eigentümliche des Hinaufrükkens in die übersinnlichen Welten, daß die Begriffe zusammengehen, daß in bezug auf das, was in der physisch-sinnlichen Welt getrennt bezeichnet werden muß, Verschmelzungen, Zusammenfügungen entstehen.",
        "Daher muß man sich andere Empfindungsweisen aneignen, wenn man Bezeichnungen der Sinneswelt für Übersinnliche Wesenheiten gebraucht.",
        "Man ist fast immer genötigt, diese Dinge noch einfacher und noch mehr dem sinnlichen Bewußtsein genähert darzustellen, als es eigentlich einer vollständig richtigen Darstellung entsprechen kann, denn die Dinge komplizieren sich sehr.",
        "Wenn ich eben ausgeführt habe, wie sich die Begriffe von wahr, aufrichtig und schön auf der einen Seite und von häßlich und lügnerisch auf der anderen Seite verknüpfen, so müssen wir noch etwas anderes hinzufügen."
      ],
      [
        "Wenn man in die übersinnlichen Welten eindringt, kann man ein Wesen finden, welches man nach allen Begriffen, die man sich im Sinnensein angeeignet hat, als ein schönes Wesen bezeichnen muß, als ein herrliches Wesen vielleicht: schön, strahlend, herrlich.",
        "Nun hat man es vor sich.",
        "Es ist aber kein Beweis, daß es auch ein gutes Wesen ist, wenn es einem so entgegentritt, es kann ein ganz böses sein und einem in der hehrsten Engelsgestalt entgegentreten.",
        "Denn nach dem Begriffe von schön, den man sich in der Sinneswelt gebildet hat, nennt man ein solches Wesen in der übersinnlichen An- schauung schön.",
        "Wie sollte man es auch nicht!",
        "Wenn man es abgebildet finden würde in der Sinneswelt, würde man es mit vollem Rechte schön nennen.",
        "Ein solches Wesen kann das häßlichste sein, das es nur gibt; trotzdem kann es als ein schönes bezeichnet werden,"
      ],
      [
        "wenn man bei den Bezeichnungen der Sinneswelt bleibt.",
        "Es kann ein ganz böses Wesen sein, kann die Bosheit und die Schlechtigkeit und die Unwahrheit, die einen anlügt, behalten, kann ein Teufel in Engelsgestalt sein.",
        "Das ist durchaus möglich in den übersinnlichen Welten.",
        "Nun kann sich durch mancherlei Weise, wovon wir noch sprechen werden, herausstellen, daß man nach und nach hinter die Sache kommt, wenn man sich mit dem hellseherischen Bewußtsein der Sache gegenüberstellt.",
        "Man hat also vor sich eine Engelsgestalt und kann sich jetzt sagen, wenn man es so weit gebracht hat, denkend bleiben zu können beim übersinnlichen Anschauen: Daß du jetzt einen Engel siehst oder irgendeine herrliche Gestalt, dadurch mußt du dich nicht täuschen lassen; das kann alles möglich sein, es kann ein Engel sein, kann aber auch ein Teufel sein.",
        "Nun kann man anfangen mit dem, was man so oft tun muß, wenn man hinaufrückt in die höheren Welten: mit einer gehörigen Selbstprüfung.",
        "Man kann mit sich zu Rate gehen und untersuchen, wieviel Eigenschaften von Selbstsinn, von Egoismus man in sich hat.",
        "Dann durchdringt sich die Seele mit mancherlei Bitternissen, dann kommt mancherlei Wermut in die Seele hinein.",
        "Aber dieses Bittere, Peinigende"
      ],
      [
        "kann gerade dazu führen, daß man sich wieder eine kurze Zeit reinigt, daß man sich läutert in seinem Selbstsinn, in seinem Egoismus.",
        "Und wenn man dadurch zu dem Urteil kommt, wie wenig man eigentlich frei ist von dem Selbstsinn und daß man danach streben muß, frei zu werden, dann erleuchtet sich einem der ganze Prozeß, der sich abspielt im Seeleninnern.",
        "Wenn man es nun so weit gebracht hat, daß einem, wenn man solche Selbstbetrachtung anstellt, das nicht entfällt, was man anschaut - denn das wird in der Regel bei den ersten Schritten geschehen , so fängt unter Umständen der Engel an, gar kein Engel zu sein, sondern recht häßliche Formen anzunehmen, und man kann nach und nach dahinterkommen, daß man sich sagt: Dem Wesen, dem du da als einem bösen entgegengetreten bist, hast du die Möglichkeit gegeben, seine Bösartigkeit zum Ausdruck zu bringen, indem es dir erst eine ganz andere Gestalt vorgaukelte; aber du hast es gezwungen, dir seine wahre Gestalt zu zeigen, indem du dich mit reineren Gefühlen durchdrungen hast."
      ],
      [
        "So hat ein seelischer Vorgang in der übersinnlichen Welt ein Zwingendes, ein Kraftendes; so macht man es selber den Wesen möglich, einen anzulügen, oder man zwingt sie, einem ihre wahre Gestalt darzustellen.",
        "Wie man hineintritt in die übersinnliche Welt, mit welchen Qualitäten, danach stellt sie sich einem dar.",
        "Was man die Quelle der Täuschungen nennt, damit muß man noch ganz anders vorgehen, als es gewöhnlich geschieht.",
        "Es kann jemand in die übersinnlichen Welten hineintreten und allerlei Herrliches beschreiben.",
        "Wenn Sie ihm sagen, er hätte sich getäuscht, so wäre das nicht"
      ],
      [
        "wahr; denn er hat es gesehen.",
        "Aber er hat nicht das gesehen, was er gesehen haben würde, wenn er das getan hätte, was ich eben beschrieben habe.",
        "Hätte er es so gemacht, so hätte er zugleich die Wahrheit gesehen."
      ],
      [
        "Denn von einem Teufel ist es schön, wenn er sich als Teufel darstellt, während es häßlich ist, wenn er eine Engelsgestalt darstellt.",
        "Man kann gar nicht anders als solche Begriffe sich anzueignen.",
        "So muß man sich vor allen Dingen abgewöhnen, wenn man in die übersinnlichen Welten hineintritt, die Dinge mit den Vorstellungen zu bezeichnen, die man gewonnen hat in der sinnlichen Welt."
      ],
      [
        "Wenn man dies, was man im Sinnensein gewonnen hat, beibehielte, so würde man erst zu der Gestalt, die einem so entgegentritt, sagen: Es ist ein schöner Engel -, und nachher: Es ist ein häßlicher Teufel! - So kann es aber das hellseherische Bewußtsein nicht ausdrücken, wenn man richtig charakterisieren will, sondern zu dem häßlichen Teufel muß man sagen: Es ist ein schöner Teufel -, trotzdem er nach sinnlichen Begriffen grundhäßlich ist.",
        "Dazu kommt man aber nicht dadurch, daß man einfach alle Begriffe auf den Kopf stellt, die man aus dem Sinnensein hat."
      ],
      [
        "Das wäre ein bequemer Weg.",
        "Dann könnte jemand zum Beispiel den Devachanplan dadurch beschreiben, daß er für alles, was in der Sinneswelt häßlich ist, schön setzt, für schön häßlich, für grün rot, für schwarz weiß und so weiter."
      ],
      [
        "So kann man es aber nicht machen, sondern die Begriffe müssen angeeignet sein im Erleben der übersinnlichen Welten.",
        "Man eignet sie sich so an wie die Anschauungen, die das heranreifende Kind von der Sinneswelt sich aneignet, nicht durch Theorien, sondern durch Erleben, und findet es dann völlig unnatürlich, einen"
      ],
      [
        "Teufel häßlich zu nennen, der sich als Teufel darstellt, wenn man sich bewußt ist, daß man die Sprache der übersinnlichen Welten redet.",
        "Aber man muß sich eine solche Empfindungsweis`e aneignen, wenn man sich wirklich in den übersinnlichen Welten orientieren will, wenn man in ihnen sich auskennen und herumgehen will.",
        "Daher können Sie sich nun leicht eine Vorstellung machen, was gemeint ist, wenn man der Einfachheit halber sagt: Auf der einen Seite steht die Sinneswelt, auf der anderen Seite sind die übersinnlichen Welten; da kommt man aus dem Sinnensein uber die entsprechende Grenze in das übersinnliche Sein hinein.",
        "Geht man mit alledem, was man im Sinnensein gewonnen hat, da hinein, wendet man das an, was man gewonnen hat an Vorstellungen, Begriffen, Ideen aus der Sinneswelt, so ist alles unzutreffend; dann redet man lauter Verkehrtheiten.",
        "Man muß gründlich an der Grenze umlernen und zwar nicht theoretisch, sondern lebendig.",
        "Man kann das überhaupt nicht brauchen, was man sich in der Sinneswelt an Vorstellungen angeeignet hat, man muß es zurücklassen.",
        "Sie sehen, daß man vieles zurück- lassen muß, womit man recht innig verbunden ist in der Welt des Sinnenseins, und ich möchte Ihnen jetzt die Sache konkret-anschaulich, nicht aus Theorien heraus beschreiben."
      ],
      [
        "Nehmen wir an, jemand gelangt, nachdem er sich die Fähigkeit angeeignet hat, die gekennzeichnete Grenze zu überschreiten, von der Sinneswelt in die Übersinnliche Welt hinein.",
        "An der Grenze früge er sich: Was muß ich jetzt zurücklassen, wenn ich mich auskennen will in der übersinnlichen Welt?",
        "Ich muß zurücklassen - so kann er sich bei guter Selbstbesinnung sagen - eigentlich alles, was ich in den verschiedenen Inkarnationen vom Erdenurbeginn an bis in die Jetztzeit auf der Erde erlebt, gelernt, mir angeeignet habe.",
        "Das muß ich hier ablegen, denn ich betrete eine Welt, in welcher das, was man innerhalb der Inkarnationen lernen kann, keinen Sinn mehr hat.",
        "Es ist leicht, möchte ich sagen, so etwas auszusprechen; es ist leicht, so etwas anzuhören; es ist leicht, das in Begriffsabstraktionen zu fassen.",
        "Aber es ist eine ganze innere Welt, so etwas zu empfinden, zu fühlen, zu erleben: alles dort abzulegen wie die Kleider, was man in all den Inkarnationen in dem Sinnensein sich angeeignet hat, um"
      ],
      [
        "in eine Welt hineinzugehen, innerhalb welcher das alles keinen Sinn mehr hat.",
        "Hat man diese Empfindung lebendig, dann hat man auch eine lebendige Erfahrung - wirklich nichts, was mit irgendeiner Theorie zusammenhängt -, wie man sie hat, wenn man in der wirklichen Welt eben einem wirklichen Menschen gegenübertritt, den man kennenlernt, indem er zu einem spricht, sich zu einem verhält, den man nicht kennenlernt, indem man sich von ihm Begriffe konstruiert, sondern indem er mit einem lebt.",
        "So steht man an der Grenze zwischen Sinnensein und Geistessein nicht einem Begriffssystem, sondern einer Realität gegenüber, die nur als eine übersinnliche Realität wirkt, aber so konkret, so lebendig wie ein Mensch: das ist der Hüter der Schwelle.",
        "Er ist da als ein konkretes, reales Wesen.",
        "Und lernt man ihn kennen, so lernt man ihn auch kennen als ein Wesen, das in die Kategorie von Wesen gehört, die in einer gewissen Weise mitgemacht haben das Leben vom Erdenurbeginn, dann aber nicht dasjenige mitgemacht haben, was man als Seelenwesen erlebt.",
        "Das ist das Wesen, das in dem Mysteriendrama «Der Hüter der Schwelle» dramatisiert werden sollte mit den Worten:"
      ],
      [
        "Bekannt ist dir, der dieses Reiches Schwelle"
      ],
      [
        "Behüten muß seit Erdenurbeginn,"
      ],
      [
        "Was, um es zu betreten, Wesen brauchen,"
      ],
      [
        "Die deiner Zeit und deiner Art gehören."
      ],
      [
        "Dieses «deiner Zeit und deiner Art» ist etwas, was aus dem Wesen der Sache heraus folgt.",
        "Andere Zeiten und andere Art haben die Menschen - andere Art und andere Zeiten haben die Wesen, die in einer gewissen Weise getrennt gegangen sind von den Wegen der Menschheit seit dem Erdenurbeginn.",
        "Da kommen wir mit einem Wesen zusammen, demgegenüber man sich sagt: Ich habe ein Wesen vor mir, das erfährt und erlebt vieles in der Welt; aber es beschäftigt sich nicht mit dem, was man an Liebe, an Schmerzen und Pein, aber auch an Fehlern und Unmoralischem auf der Erde erleben kann; es weiß nichts und will nichts wissen von dem, was sich abgespielt hat in der menschlichen Grundwesenheit bis jetzt.",
        "Die christliche Überlieferung"
      ],
      [
        "drückt diesen Tatbestand dadurch aus, daß sie sagt: Vor dem Geheimnis der Menschwerdung verhüllten diese Wesenheiten ihr Antlitz.",
        "Eine ganze Welt ist in dem Unterschiede zwischen diesen Wesenheiten und den menschlichen Wesenheiten ausgedrückt."
      ],
      [
        "Und nun kommt eine Empfindung, die man unmittelbar hat, die sich so einstellt, wie wenn man einem Menschen gegenüber, der blonde Haare hat, die unmittelbare Empfindung hat: der hat blonde Haare.",
        "So tritt die Empfindung auf: Dadurch, daß du durch die Erdenkulturen durchgegangen bist, hast du dir notwendigerweise Unvollkommenheiten angeeignet, aber du mußt wieder zurückkommen zu dem ursprünglichen Zustand, mußt auf der Erde den Weg wieder zurückfinden, und dieses Wesen kann dir das zeigen, weil es deine Fehler nicht angenommen hat.",
        "Jetzt steht man einem Wesen gegenüber wie einem wirklichen Vorwurf, groß und grandios, wie ein Ansporn zu dem, was man nicht ist.",
        "Das zeigt einem dieses Wesen in lebendigster Weise, und da kann man sich ganz ausgefüllt fühlen vor dem Wesen von dem Wissen dessen, was man ist oder nicht ist.",
        "Da steht man dem lebendigen Vorwurf gegenüber.",
        "In die Klasse der Erzengel, der Archangeloi, wie wir sagen, gehört dieses Wesen.",
        "Es ist eine ganz reale Begegnung, und sie veranlaßt, daß einem plötzlich vor Augen tritt, was man als Erdenmensch im Sinnensein geworden ist.",
        "Selbsterkenntnis ist es zugleich im wahrhaftigen, umfassendsten Sinne.",
        "Sich selbst schaut man, wie man ist, und sich selbst schaut man, wie man nun werden soll!"
      ],
      [
        "Zu diesem Schauen ist der Mensch nicht immer geeignet.",
        "Ich habe heute nur von der Begriffs- und Vorstellungswelt gesprochen, die abgelegt werden muß.",
        "Vieles andere muß ebenso abgelegt werden."
      ],
      [
        "Man muß, wenn man bis zum Hüter der Schwelle hinkommt, ei- gentlich alles ablegen, was man von sich weiß.",
        "Man muß nur dann noch etwas haben, um es durchzubringen.",
        "Darauf kommt es an!",
        "Daß man an der Grenze alles zurücklassen muß, das bewirkt ein inneres Erlebnis, dem man eben gewachsen sein muß, und die Vorbereitung bis zu dieser Stufe der Hellsichtigkeit muß darin bestehen und besteht bei einer richtigen Schulung darin - bei einer richtigen Schulung darf man nicht von Gefahren sprechen, denn gerade eine"
      ],
      [
        "richtige Schulung beseitigt die Gefahren -, daß man ertragen lernt, was sonst schauervoll, schreckensvoll wäre.",
        "Zum Ertragen muß man kommen durch die Vorbereitung, denn das` ist die Grundkraft zu allem weiteren Erleben."
      ],
      [
        "Im gewöhnlichen Leben ist der Mensch nicht fähig, alles das zu ertragen, was man ertragen muß, wenn man vor dem Hüter der Schwelle steht.",
        "Denn der Hüter der Schwelle ist zu etwas höchst Sonderbarem genötigt, das beurteilt werden muß von dem Gesichtspunkt der übersinnlichen Welt, wenn es nicht mißverstanden werden soll."
      ],
      [
        "Der Mensch ist immer so, daß sich die Tätigkeiten der übersinnlichen Welt in ihm abspielen; er weiß nur nichts davon.",
        "Während wir denken, empfinden, wollen, läuft immer eine Tätigkeit des astralischen Leibes und ein Zusammenhang mit der astralen Welt nebenher."
      ],
      [
        "Aber der Mensch weiß nichts davon, weil er, wenn er das wissen würde, was seine eigenen Leiber sind, es nicht ertragen könnte und davon betäubt würde.",
        "Daher muß diese Wesenheit, wenn ihr der Mensch ohne genügende Vorbereitung gegenübertritt, ihm das alles verhüllen und sich selber verhüllen; sie muß einen Schleier ziehen vor die Übersinnliche Welt."
      ],
      [
        "Sie muß es tun zum Schutze des Menschen, der, im Sinnensein stehend, den Anblick nicht ertragen könnte.",
        "Da sehen wir so recht einen Begriff, den wir im Sinnensein nur moralisch beurteilen können, als Unmittelbarste Naturordnung."
      ],
      [
        "Der Schutz des Menschen vor dem Sehen der übersinnlichen Welt ist die Funktion des Hüters der Schwelle, die Erhaltung des Menschen in dem Zustande, in dem er ist, bevor er sich in genügender Weise auf die übersinnlichen Welten vorbereitet hat."
      ],
      [
        "So haben wir versucht, einige Vorstellungen zusammenzufügen, die uns hinführen können zu einem Begriff von dem Hüter der Schwelle.",
        "Solche Vorstellungen, solche Begriffe und Ideen, Erfahrungen und Erlebnisse versuchte ich in einem kleinen Buche zusammenzustellen, das in den nächsten Tagen Ihnen hier noch dargeboten werden soll und das Ihnen neben den Vorträgen selbst eine wichtige Hilfe sein kann.",
        "Es wird in eine Reihe von acht Meditationen zerfallen und wird sich so darstellen, daß der Leser, wenn er diese Meditationen durchmacht, dadurch für sein Seelenleben etwas"
      ],
      [
        "haben wird.",
        "Einige von den Vorstellungen, die uns zum Hüter der Schwelle hinführen können, versuchte ich heute zu charakterisieren.",
        "Von diesem ausgehend werden wir versuchen, an dem Hüter der Schwelle vorbeigehend, einige Einblicke und Ausblicke zu charakterisieren, um dann noch tiefer die Christus-Wesenheit und die Christus-Initiation verstehen zu können."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "VIERTER VORTRAG München, 28. August 1912",
    "paragraphs": [
      "Wir brauchen, um zu den Aufgaben dieses kurzen Vortragszyklus zu kommen, solche Vorstellungen, wie wir sie gestern gewonnen haben, und noch einige, die wir eben haben müssen, wenn wir charakterisieren wollen, was vorgestern in dem programmatischen Vortrage angedeutet worden ist.",
      "Sie werden finden, daß überall, wo in der Literatur oder sonstwo von der Initiation gesprochen wird, irgendwie jenes Rätsel berührt wird, das allem Menschlichen so naheliegt: das Rätsel vom Tode. Und Sie werden finden, daß in alledem, was man Berichte nennen könnte, darauf hingewiesen wird, daß der zu Initiierende auf einer gewissen Stufe so etwas in einer etwas anderen Form durchzumachen hat, wie der Durchgang durch die Pforte des Todes es eben ist. Diese Berichte beruhen für den Okkultisten tatsächlich auf Wahrheit. Denn die Erfahrungen, die beim Aufstieg in die geistigen Welten durchzumachen sind, berühren sich mit denselben Erfahrungen, die der Mensch durchzumachen hat beim naturgemäßen Übergange vom Leben im Sinnenleibe zu jenem andersartigen Leben, das in einer ganz anderen Umhüllung stattfindet zwischen dem Tode und einer neuen Geburt. Wenn man so recht herankommen will an dasjenige, um was es sich dabei handelt, muß man zuerst fragen: Als was weiß sich denn eigentlich der Mensch im gewöhnlichen Leben? - Es ist vielleicht nicht gerade interessant, eine so abstrakte Frage aufzuwerfen, aber zum Verständnis des Initiationsvorganges ist es schon notwendig, diese Frage ins Auge zu fassen: Als was weiß sich denn die Seele?",
      "Was sie während des Schlafes ist, das weiß ja die Seele nicht, denn entweder verläuft der Schlaf in Bewußtlosigkeit, oder aber es spielen in den Schlaf herein Träume, die ja erst durch den Okkultismus gedeutet werden müssen, wenn man sie in der richtigen Weise verstehen will. Bei der Frage: Was ist sich der Mensch, was ist seine Seele im gewöhnlichen Sinnensein? - kann also doch nur die Frage des",
      "Tageslebens in Betracht kommen. Nun wissen wir, daß zunächst jene Tore da sind, welche wir unsere Sinnesorgane nennen, durch welche die Farben- und Lichtwelt, die Tonwelt, die Geruchwelt, Wärme und Kälte und so weiter in unsere Seele hereinströmen, und was wir im Sinnensein unsere Welt nennen, ist ja im Grunde genommen nur eine Zusammenfassung alles dessen, was eben durch die Tore unserer Sinne einströmt.",
      "Dann haben wir das Instrument unseres Verstandes, unserer Empfindungen, unseres Wollens; mit dem verarbeiten wir, was in der äußeren Welt uns entgegentritt. Es treten in unserer Seele auf Begierden, Wünsche, Strebungen, Befriedigungen, Unbefriedigungen, Beseligungen, Enttäuschungen und so weiter, und wenn wir den ganzen Umfang dessen, als was sich der Mensch weiß, eigentlich ins Auge fassen, so ist es alles dieses.",
      "Wenn man für das gewöhnliche Leben erkennen will, was Innenwelt ist, so kann man eigentlich nichts anderes anführen als die Summe dessen, was jetzt charakterisiert worden ist. Dabei kann sich der Mensch auch von außen betrachten.",
      "Er kann seinen Leib betrachten. Er wird sich durch die mannigfaltigsten Tatsachen, die jetzt nicht im einzelnen ausgeführt zu werden brauchen, bewußt, daß er seinen Leib als sein Werkzeug für das wache Tagesleben während des Lebens zwischen Geburt und Tod anzusehen hat.",
      "Es spielen in dieses Leben Sehnsüchte herein, die wir schon berührt haben; es spielt herein die Sehnsucht zu wissen, was der Mensch eigentlich innerhalb der Grenzen von Geburt und Tod ist, die Sehnsucht herauszukommen aus dem, was man das Lebensdunkel nennen könnte. Aber darüber hinaus hat eben der Mensch zunächst nichts, hat zunächst nicht im gewöhnlichen Sinnensein Erlebnisse.",
      "Seine Erlebnisse sind eben so, daß die auf- und ablaufenden Triebe, Begierden, Sinnesempfindungen, Vorstellungen, Verstandeskombinationen und so weiter das wache Tagesleben erfüllen. Knüpfen wir nun daran dasjenige an, was uns am Schlusse unseres gestrigen Vortrages entgegengetreten ist.",
      "Wir haben darauf aufmerksam gemacht, wie der Mensch, wenn er an die Grenze zwischen Sinnensein und Geistessein kommt, seine Vorstellungen ändern muß, wie er zurücklassen muß, was er gedacht",
      "hat über häßlich und schön, über wahr und falsch, über gut und böse, weil diese Begriffe eine ganz andere Bedeutung und einen nach ganz anderen Richtungen hin gehenden Wert erhalten, wenn man die geistigen Welten betritt. Daraus schon können wir eine Idee bekommen, wie wir uns wandeln müssen, wenn wir in die geistigen Welten eintreten wollen. Nun, nachdem wir beobachtet haben, als was sich der Mensch weiß im wachen Tagesleben zwischen Geburt und Tod, können wir uns mit Beziehung auf das gestern Gesagte einmal fragen: Was kann der Mensch von alledem, als was er sich so weiß, mitnehmen über die Grenze, wo der Hüter der Schwelle steht? Was kann er von allem, was er an Trieben, Begierden und Leidenschaften im Sinnensein erlebt und erfährt, von seinen Empfindungen und Vorstellungen, von Verstandesbegriffen und Urteilen, die er durchmacht, mit hinübernehmen über die Grenze, wo der Hüter der Schwelle steht? - Ja, es gehört zu den ersten Schritten der Initiation, daß der Mensch erfährt: von alledem, was man so anführen kann, was man selber ist, kann man gar nichts mitnehmen! Und es ist nicht etwa übertrieben oder paradox gesprochen, sondern wörtlich wahr gesprochen, wenn man sagt: Von allem, worüber man eigentlich im Sinnensein reden kann, kann man gar nichts in die geistige Welt mit hinübernehmen, sondern man muß alles zurücklassen an der Grenze, an welcher der Hüter der Schwelle steht.",
      "Aber machen Sie sich nunmehr eines klar: An alledem, was man da als sich weiß im Sinnensein, haftet doch eines, ein höchst Erhebliches daran, und zwar wirklich das, worauf es ankommt bei den Schritten der Initiation. Es haftet daran, daß man das liebt und gern hat und daß man gar nicht einmal auskommt, wenn man den gewöhnlichen, etwas unsympathischen Begriff des Egoismus darauf anwendet. Dadurch ist man nicht fertig, daß man sagt Der Mensch soll seinen Egoismus ablegen, dann wird er selbstlos hinüberkommen in die Region der geistigen Welt. Das ist, wenn man trivial sprechen darf, leicht gesagt. Aber dieser Egoismus ist in den geheimeren, feineren Gliederungen seines Wesens innig zusammenhängend mit dem, was wir nicht nur egoistisch für wertvoll halten im Leben, sondern für wertvoll halten müssen, weil wir dadurch Mensch sind in",
      "der Welt, in der wir uns aufzuhalten haben. Wir sind Menschen dadurch, daß wir zusammenhalten können, was wir erfahren, und daß wir in einer gewissen Weise darüber denken können, daß wir erleben können.",
      "Durch das alles sind wir die Menschen, die wir sind. Und was wir Tüchtiges leisten können im gewöhnlichen Sinnen- sein, leisten wir dadurch, daß wir wertschätzen unsere Fähigkeit, zusammenzuhalten in unserer Persönlichkeit, in unserer Individualität, was wir erleben.",
      "Und würden wir das nicht wertschätzen, was wir erleben, so würden wir Faulenzer oder träge Menschen im Leben werden und nichts für die gewöhnliche Welt erreichen. Es wäre daher oberflächlich> zu sagen: Der Egoismus ist unter allen Umständen als etwas Schädliches anzusehen.",
      "Denn in seiner feineren Gliederung bedeutet er die Kraft, welche den Menschen vorwärtstreibt in der Welt, in der er nun einmal inkarniert ist. Und dennoch: es muß das alles abgelegt werden, es muß zurückbleiben, muß aus dem einfachen Grunde zurückbleiben, weil es ungeeignet ist für die Welt, die wir betreten müssen.",
      "Wie unser Sinnenleib ungeeignet ist für ein Eisenbad von 9000C, so ist das, was wir unser Selbst nennen, mit dem, was wir lieben in der gewöhnlichen Welt, ungeeignet in der geistigen Welt. Und man muß es aus dem Grunde zurücklassen, weil einem etwas Ähnliches passieren würde, wie unserm sinnlichen Leib passieren würde, wenn wir uns in ein Eisenbad von 900CC hineinstürzen würden: wir würden keinen Aufenthalt darin haben können, würden darin zugrunde gehen.",
      "Nun wird Ihnen ein Gedanke auftauchen, der ganz selbstverständlich ist, der nur in seiner Tiefe erfaßt und erfühlt werden muß, der Gedanke: Wenn ich nun alles ablege> was ich bin, wovon man überhaupt reden kann im Sinnensein, was bleibt mir denn dann eigentlich? Kann ich denn dann noch selber hineingehen in die geistige Welt, wenn ich mich zuerst ablegen muß? - Das ist es, daß der Mensch nichts von dem, wovon er weiß, daß er es ist, in die über- sinnlichen Welten hinein mitnehmen kann, und daß alles, was er in diese Welten hinein mitnehmen kann, etwas ist, wovon er nichts weiß in der gewöhnlichen Welt. Das sind die verborgenen, in den Untergründen der Seele liegenden Daseinselemente, die in dem",
      "Menschen drinnenstecken, von denen er nichts weiß. Und die mussen so stark sein, daß der Mensch aus dem, wovon er nichts weiß, in die geistigen Welten das Nötige hineinbringt, wenn er alles das, wovon er weiß, draußen ablegen muß. Um den Gedanken, oder besser gesagt, die Empfindung recht gründlich zu erfassen, verbinden Sie das, was eben gesagt worden ist, mit dem gewöhnlichen Todesgedanken. Es ist nur selbstverständlich für das gewöhnliche Sinnesleben, daß der Mensch alles das, als was er sich bezeichnen kann, liebt. Und weil er nichts weiter von sich weiß, so hat er bei der Unsterblichkeitssehnsucht die Sehnsucht, das zu behalten, was er im Sinnen- sein liebt. Deshalb kann der Schauer so groß werden und es kann eine Furchterfülltheit eintreten vor der geistigen Welt, weil der Gedanke auftauchen muß: Du gehst in ein wesenloses Unbestimmtes hinein, du weißt nicht, ob du dich darinnen bewahren kannst, denn das, wovon du weißt, geht dir verloren!",
      "Nun gehört es zur Initiation, daß das, was in den verborgenen Untergründen der Seele liegt an Daseinselementen, schon während des Sinneslebens heraufgeholt und zum Bewußtsein gebracht wird. Das geschieht zum Teil durch die Mittel, welche geschildert sind in «Wie erlangt man Erkenntnisse der höheren Welten?», indem aus den Untergründen der Seele Erlebnisse ins Bewußtsein heraufgehoben werden, die gleichsam als ein verdichtetes, verstärktes Seelenleben herauskommen. Und dieses verdichtete, verstärkte Seelenleben, wovon man sonst nichts weiß, kann hinübergehen in die geistige Welt. Daher bereitet man sich durch Meditationen, Konzentrationen, durch das, was im «Hüter der Schwelle» genannt ist das «gedankenkräftige Verhalten der Seele», darauf vor, etwas mit hinüberzunehmen in die geistige Welt, etwas dort drüben sein zu können. Was geschieht denn aber mit dem, was man abgelegt hat?",
      "Das ist nun etwas außerordentlich Wichtiges. Zunächst könnte man, wenn man bildhaft, anschaulich schildert, wirklich sagen: Das, wovon man reden kann im Sinnensein, wovon man weiß, das legt man an der Grenze beim Hüter der Schwelle ab, wie wenn man seine Kleider ausziehen und ohne Kleider hinübergehen würde in bezug auf alles Seelische in die geistige Welt. Bildhaft ist das ganz richtig",
      "gesprochen. Aber die Initiation macht es notwendig, daß nicht bloß dies geschieht, sondern daß noch etwas anderes geschieht: daß man zwar sein Selbst und alles, was an einem ist, ablegt, aber doch etwas davon mitnimmt, sonst verliert man nämlich allen Zus ammenhang mit dem Sein, von dem man einzig und allein früher gewußt hat.",
      "Also man muß doch etwas mitnehmen! Wir stehen hier vor einem Widerspruch, der allerdings ein sehr leicht lösbarer ist: daß wir alles zurücklassen sollen und doch von dem Zurückgelassenen etwas mitnehmen sollen.",
      "Sie werden es leicht verstehen, wenn ich es vergleiche mit einer Erscheinung des gewöhnlichen Lebens, was es der Seele ist, wenn sie diesen Vorgang durch macht. Es gibt im Leben auch einen ähnlichen Vorgang, den wir mit diesem anderen, obwohl er viel empfindungskräftiger> viel vehementer ist, vergleichen können.",
      "Das ist der Vorgang, wenn wir uns an etwas erinnern, was wir im Leben erlebt haben. Was Sie gestern erlebt haben, das haben Sie zurückgelassen, aber Sie haben es in der Erinnerung mit sich genommen. Darauf kommt es an, daß man sich durch die vorhergehenden Meditationen, Konzentrationen und so weiter bereitgemacht hat, daß man, wenn man über die Schwelle in die geistigen Welten hinüberkommt, die Kraft hat, in einer übersinnlichen Erinnerung festzuhalten, was man zurückgelassen hat.",
      "Ist man nicht in der entsprechenden Weise vorbereitet, so hat man diese Kraft nicht, um sich daran zu erinnern. Dann ist man aber für sein Bewußtsein ein Nichts, weil man nichts weiß von sich. Das ist es, daß man sich durch übersinnliche Erinnerung, wenn man in der geistigen Welt drinnensteht, an das erinnert, was man zurückgelassen hat.",
      "Sonst kann man nichts mitnehmen als diese Erinnerungen, und daß man sie mitnimmt, das bewahrt einem das, was man nennen könnte die Kontinuität, die Erhaltung des Selbstes. Auch im gewöhnlichen Leben geht einem der Zusammenhang des Bewußtseins und damit das eigentliche Selbst verloren, wenn man Dinge, an die man sich erinnern sollte - sagen wir vieles in unserem Leben -, einfach auslöschen muß aus seinem Bewußtsein und krankhaft vergessen hat.",
      "An der fortlaufenden Erinnerung hängt vieles im gewöhnlichen Leben. An der Erinnerung im übersinnlichen Leben - die Erinnerung an das gewöhnliche",
      "Leben zu bewahren - hängt alles, was die ersten Schritte der Initiation möglich macht. Diese Erinnerung ist eben möglich, und sie tritt durch die Initiation ein, und von ihr aus können Sie wieder den Faden hinüberziehen nach dem Rätsel des Todes.",
      "Wenn der Mensch durch den Tod hindurchgeht, so hat er zwar nicht dieselben Kräfte, die er durch die Initiation erwirbt, aber in gewisser Weise bekommt er Kräfte, wenn er seinen Leib ablegt, indem ihm andere Wesen der übersinnlichen Welt helfen. Er bekommt die Möglichkeit, die Erinnerung für das zu bewahren, was er vergessen hat, indem er seinen Leib abgelegt hat.",
      "Und jetzt haben Sie im Realen die Möglichkeit, sich auf die Frage zu antworten: Was bleibt von meinen Seelenerlebnissen, wenn ich durch die Pforte des Todes durchgegangen bin, wie lebt die Seele weiter? Das ist die allerwichtigste Frage.",
      "Und Sie haben durch die Erfahrung der Initiierten die Antwort: Die Seele lebt weiter, weil in den tiefen, verborgenen Untergründen der Seele Kräfte sind, die in der Erinnerung festhalten können, was erlebt ist. Unsterblich sein heißt, die Kraft haben, in der Erinnerung das abgelebte, das vergangene Dasein bewahren zu können.",
      "Das ist die eigentliche Definition der menschlichen Unsterblichkeit. Durch die Initiation wird der Beweis erbracht, der Erfahrungsbeweis, daß im Menschen Kräfte leben, die [ermöglichen, sich] nach Ablegung des sinnlichen Leibes erinnern [zu] können an alles, was der Mensch im Sinnensein und überhaupt erlebt hat.",
      "So bewahrt sich der Mensch selbst durch die Zukunft hindurch, so erlebt er sein früheres Sein als Erinnerungen im zukünftigen Sein. Fühlen Sie die ganze Gewalt des Gedankens, der sich durch die Initiation ergibt und der ausgesprochen werden konnte in den Worten: Das Menschenwesen ist von solcher Art, daß es durch die Kräfte der übersinnlichen Erinnerung sein eigenes Wesen durch zukünftige Zeiten trägt.",
      "Wenn Sie diesen Gedanken fühlen, in die Leerheit des Weltenalls hinein ihn fühlen so, daß Sie sich vorstellen die sich selbst durch die Ewigkeiten tragende Seele, dann haben Sie eine viel bessere Definition dessen, was man eine Monade nennt, als sie durch irgendwelche philosophische Begriffe gegeben werden könnte. Denn dann fühlen Sie, was eine Monade, ein in sich geschlossenes, sich",
      "selber tragendes Wesen ist. Über diese Dinge sind denn doch nur Vorstellungen zu gewinnen durch die Erfahrungen der Initiation.",
      "Das ist erst die eine Seite dessen, was ich Ihnen zu schildern habe. Wir müssen die ersten Schritte der Initiation noch genauer betrachten, wenn wir erfühlend zu dem kommen wollen, was uns Vorstellungen über die Initiation geben kann.",
      "Nehmen wir an, ein Mensch habe durch gedankenkräftiges Verhalten seiner Seele, oder mit einem Fremdwort: durch Meditation es dahin gebracht, daß er außerhalb seines physischen Leibes wahrnehmen kann, daß er zunächst wahrnehmen kann in seinem elementarischen oder ätherischen Leibe. Erlebt wird dieses Wahrnehmen in jenem Leibe, der enger gebunden ist in seinen einzelnen Teilen an das Gehirn, weniger eng zum Beispiel an die Hände, erlebt wird das Sich-Einfühlen in den ~elementarischen Leib dadurch, daß man das Gefühl hat: Du weitest dich aus, du wirst breiter, fließest hinaus in die unbestimmten Weltenweiten. - So ist das subjektive Gefühl.",
      "Aber es ist nicht so, daß man ins Wesenlose und Unbestimmte hinausrinnt, sondern da ist alles konkretes Leben. Man lebt sich in lauter Konkretheiten hinein, und man gewinnt zugleich ganz bestimmte Erlebnisse in diesem SichAusweiten.",
      "Besonders ein Gefühl kann man leicht erhalten, und es wird kaum - wenn nicht ganz besondere Umstände vorliegen - jemandem, der die ersten Schritte der Initiation durchmacht, erspart bleiben, diese Erfahrung zu machen. Es ist die Erfahrung der Bangigkeit, der Ängstlichkeit, die Erfahrung, als ob man im Weltenall wäre und keinen Boden unter den Füßen hätte, ein Bedrückendes in der Seele.",
      "Das sind so die inneren Erlebnisse, die man dabei durchmacht. Dann aber das noch Wichtigere.",
      "Wenn man im gewöhnlichen Leben denkt, eine Vorstellung hat, wenn ein Gedanke den anderen kommen läßt, da fügt man den einen Gedanken zum anderen hinzu, man gliedert dann vielleicht Empfindungen hinzu, Wünsche, Wollen und so weiter, und beim gesunden Seelenleben wird man immer die Möglichkeit haben, zu sagen: Ich denke dies, ich fühle das. - Denn es wäre schon eine Unterbrechung, eine Störung des gesunden Seelenlebens, wenn man nicht die Möglichkeit hätte, in dieser Weise zu sprechen. Beim HineInwachsen",
      "in den elementarischen oder ätherischen Leib weitet man sich aus, aber zugleich weiten sich die Gedanken aus. Man verliert das Gefühl, als ob man in sich wäre, wenn man denkt, und man bekommt das Gefühl: man wächst in die elementarische Welt hinein, und die ist durchzogen von Gedanken, und diese Gedanken denken sich. Das tritt als ein Erlebnis auf. Es ist so, wie wenn man ausgelöscht wäre und wie wenn sich die Gedanken denken würden, wie wenn die Gefühle, die man selbst hat oder die die Dinge haben, sich erfühlen, als ob man nicht selber wollen könnte, sondern als ob das alles in einem zum Wollen erwachte. Hingegeben sein an die Objektivität, an die Welt, das ist ein Gefühl, das man hat. Aber es ist in der Regel so - und das ist wieder eine Erfahrung bei den ersten Schritten der Initiation -, daß sich hinzugesellt ein anderes Gefühl. In demselben Maße, in dem man sich ausweitet, in dem sich die Gedanken selber denken, die Empfindungen sich erfühlen, wird das Bewußtsein immer schwächer und schwächer, immer mehr und mehr herabgestimmt; das Wissen betäubt sich.",
      "Nun ist die Notwendigkeit vorhanden, etwas ganz Bestimmtes in der Seele eintreten zu lassen, wenn solche Erfahrungen in der Seele gemacht werden. Es ist eine Notwendigkeit vorhanden, daß diese Dinge möglichst genau von den Seelen erfaßt werden. Deshalb habe ich, wenn auch nicht dieselben, so doch ähnliche Dinge, die in dieselbe Richtung gehen, in dem Buche «Ein Weg zur Selbsterkenntnis des Menschen» zusammengestellt, und Sie werden, wenn Sie die Vorträge in Verbindung bringen mit diesem Buche, davon mancherlei haben können. Ein ganz bestimmtes Seelisches, das man selber herbeiführt, muß dann eintreten, ähnlich wie ich es gestern geschildert habe. Man muß nämlich Selbstbesinnung üben, muß versuchen schonungslos, rücksichtslos recht grobe Fehler, von denen man weiß, daß man sie hat, sich vorzuhalten, so daß einem vor die Seele kommt, wie wenig man eigentlich dem großen Menschheits-Ideale entspricht. Man muß sich hineinfühlen in dieses Wenig-Entsprechen dem großen Menschheits-Ideale: recht meditativ, recht gedankenkräftig gerade seine moralische oder sonstige Schwachheit sich vor die Seele rufen. Wenn man das tut, wird man nämlich dadurch stärker.",
      "Und das, was schon angefangen hat sich abzudämpfen, was sich schon so dargestellt hat, als ob es wie in einer seelischen Ohnmacht verschwinden wollte, wird wieder heller. Man fängt wieder an, das zu sehen. Aber man erfährt wieder etwas anderes bei dieser Gelegenheit, was in einfache Worte gebracht werden kann, was aber bei den ersten Schritten auf dem Wege zur Initiation bedrückend und sogar bestürzend ist. Das alles sind Worte, die für das Seelenleben gemeint sind, nicht für das Leibesleben, denn dem, der in richtiger Weise hineingeführt wird in die geistige Welt, ist auch solche Anweisung zugeflossen, daß man von äußeren körperlichen Gefahren nicht",
      "sprechen kann. Es kann ein solcher Mensch, wenn er wirklich treulich die guten Ratschläge einhält, äußerlich im Leben ein gleicher Mensch bleiben, trotzdem es innen auf- und abwogt von allerlei Peinigendem, Schmerzlichem, von Enttäuschungen und vielleicht auch erahnten Seligkeiten.",
      "Aber solche Dinge muß man durchmachen, denn in ihnen liegen die Kei`me des höheren Schauens, der höheren Einsicht. Etwas lernt man erkennen: man lernt, indem man außerhalb des physischen Leibes beobachten, wahrnehmen, erleben lernt, indem man also dazu kommt, in dem elementarischen Leibe zu leben, daß man in die elementarische Welt auf die geschilderte Art hineinwächst.",
      "Dann aber, wenn man das macht, was eben geschildert worden ist, lernt man den Grund kennen, warum diese elementarische Welt wie in einer Art Ohnmacht verschwindet, was man mit trockenem Wort so aussprechen dürfte, daß man sagt: Diese Welt mag einen nicht, sie findet, daß man nicht hineinpaßt. Und dieses Abdämpfen, dieses Verschwinden ist einfach der Ausdruck dafür: sie läßt einen nicht hinein.",
      "Aber indem man sich dann seine Fehler vorwirft, wird man stärker, und so hellt sich das wieder auf, was erst verschwunden war. Man bekommt aber dadurch das deutliche Gefühl: Eine übersinnliche Welt elementarischer Art ist um dich herum, aber du darfst nur bis zu einem gewissen Maße hinein.",
      "In dem Maße, wie du dich selbst moralisch, intellektuell immer stärker und stärker machst, läßt sie dich herein, sonst nicht; und sie zeigt dies dadurch, daß sie vor dir verschwindet.",
      "Das ist das Spannende, das Bedrückende oder manchmal auch das Zehrende oder Verzehrende, das - gewissermaßen - Kämpfen um die geistige Welt, und das Bewußtsein, wie unwürdig man ihrer ist. Und indem man Selbstbesinnung und das gedankenkräftige Verhalten der Seele, also Meditieren, Konzentrieren und das Sich-Durchdringen mit moralischen Impulsen kräftig fortsetzt, kann man eben immer mehr und mehr hineinkommen auf solche Art in die elementarische Welt. Aber dieses Hineinkommen in die elementarische Welt ist doch eigentlich nur die erste Stufe der Initiation. Wenn man die nächste Stufe besprechen will, muß man auf eine höchst eigentümliche Erscheinung aufmerksam machen, für die es eigentlich nichts recht Entsprechendes im gewöhnlichen Sinnensein gibt.",
      "Dasjenige, in dem der Mensch lebt, nachdem er elementarisch wahrnehmen kann, ist sein elementarischer Leib. Aber den hat er früher auch schon gehabt. Der Unterschied des elementarischen Leibes vor und nach dem übersinnlichen Beobachten ist nur der, daß der elementarische Leib durch die Initiation gleichsam auferweckt wird.",
      "Während er früher gleichsam geschlafen hat, ist er nachher auferweckt. Das ist eigentlich der treffendste Ausdruck, den man für die Sache gebrauchen kann. Aber eines wird man bemerken. Wenn man sich die Fähigkeit erworben hat, durch diese oder jene Maßnahmen, die man im Seelenleben getroffen hat, die eine oder die andere Tatsache oder das eine oder das andere Wesen der elementarischen Welt zu sehen - nun, so sieht man eben dieses eine Wesen.",
      "Nehmen Sie nun an, Sie haben Ihre Vorbereitungen so weit getrieben, daß Sie das eine Wesen oder ein zweites Wesen sehen. Dieses eine oder das zweite Wesen werden Sie dann wahrscheinlich, wenn Sie sich bei derselben Kraft erhalten, immer wieder sehen.",
      "Das ist keine Schwierigkeit. Aber Sie sehen nicht leicht etwas anderes. Wenn Sie eine Zeit aussetzen und nachher wieder zurückkommen, so sehen Sie doch wieder dasselbe. Kurz, es ist nicht in der elementarischen Welt so, wie es in der Sinneswelt ist.",
      "Sind für die letztere die Augen einmal präpariert, so sehen sie alles mögliche; sind die Ohren einmal präpariert, so hören sie alles gleich. So ist es nicht in der elementarischen Welt. Da müssen Sie von Stück zu Stück, von Wesensart zu",
      "Wesensart immer neu die Teile Ihres elementarischen Leibes präparieren. Da müssen Sie die ganze Welt absuchen, da muß man für jedes einzelne Wesen den Ätherleib immer wieder und wieder` erwecken. Denn man stellt nur eine Beziehung, eine Verwandtschaft her zu dem, was man einmal gesehen hat, wofür man einmal den Ätherleib erweckt hat, und muß immer neue Beziehungen erwecken.",
      "Das kann der Ätherleib allein nicht. Er kann sich nicht beherrschen, er kann nur immer zu demselben Wesen zurückkehren, oder er kann warten, bis er präpariert ist, um andere Wesen zu sehen. Ein Mensch, der die ersten Schritte auf dem Wege zur Initiation durchgemacht hat und dazu gelangt ist, dieses oder jenes Wesen, diesen oder jenen Vorgang zu sehen, kann sich noch nicht orientieren in der geistigen übersinnlichen Welt, er kann nicht, weil er nicht zu den Wesen beliebig den Zugang hat, frei vergleichen ein Wesen mit dem anderen.",
      "Soll man sich orientieren, soll man nicht bloß anschauen, sondern mit Bestimmtheit sagen: dieses oder jenes ist ein Wesen, dieses oder jenes ist ein Vorgang -, so muß man es vergleichen können mit anderen Wesen und Vorgängen in der übersinnlichen Welt. Man muß den Weg vom einen zum anderen machen können, man muß sich orientieren können.",
      "Dieses Orientieren muß man auch erst lernen. Man lernt es dadurch, daß man durch fortgesetztes Meditieren, Sich-Durchmoralisieren Kräfte zuwachsen fühlt, die man in ihrer Tätigkeit als etwas ganz Merkwürdiges empfindet.",
      "Und da muß man darauf zurückkommen, wenn man es beschreiben will, daß zwar der elementarische Leib für das gewöhnliche Leben da ist, aber immerfort schlafend ist, und daß man ihn für das über- sinnliche Wahrnehmen erst erwecken muß. Aber man muß in der Seele die Kräfte haben, um ihn zu erwecken.",
      "Was man da tut, erlebt man in einer ganz besonderen Weise. Ich kann es nur durch einen Vergleich klarmachen.",
      "Denken Sie sich, Sie schlafen ein und würden wissen: Im Bette liegt dein Leib, du kannst ihn nicht rühren, aber du bist dir bewußt, er ist da! Du aber gehst in eine geistige Welt hinein und kommst nach einiger Zeit wieder zurück, um diesen Leib wieder aufzuwekken. - Das kann bewußt geschehen. Aber wie es beim Menschen im",
      "gewöhnlichen Leben geschieht, so geschieht es unbewußt. Was ich Ihnen eben geschildert habe, das macht der Mensch durch; er wird in bezug auf seine Leiblichkeit wachend und schlafend, und er ist es selber, der sich aufweckt; nur hat er kein Bewußtsein, daß er es ist, der seinen physischen Leib erweckt.",
      "Wenn man die ersten Schritte zur Initiation durchgemacht hat, dann hat man dieses Bewußtsein. Daher ist es tatsächlich so, daß man weiß: Da hast du deinen elementarischen Leib. - Dem steht man so gegenüber, daß man fühlt: das ist der enger gebundene Teil, der dem Gehirn entspricht, dies der weiter bewegliche Teil, der den Händen entspricht, dies - das mag jetzt paradox erscheinen - der ganz bewegliche Teil, der den Füßen entspricht.",
      "Von alledem weiß man, aber das schläft an einem. Und indem man sich weiterentwickelt und die nötigen inneren seelischen Anstalten macht und hinkommt zur geistigen Welt, ist das ein fortwährendes Aufwecken.",
      "Einmal weckt man dieses Stüc\"k, ein andermal ein anderes Stück auf, einmal entzündet man diese Bewegung, einmal eine andere. Kurz, es ist ein bewußtes Auferwecken des elementarischen Leibes, so daß man sprechen könnte von einem Schlafzustand des elementarischen Leibes, in dem dieser gewöhnlich ist, und von einem Wachzustande, in welchen man ihn durch die Initiation bringt.",
      "Das ist der Unterschied in bezug auf Schlafen und Wachen beim physischen Leibe und beim elementarischen Leibe: beim physischen Leibe sind Schlafen und Wachen Wechselzustände, sie geschehen nacheinander; beim elementarischen Leibe geschieht nicht ein solches Nacheinander, da ist es ein Gleichzeitiges. So kann jemand dazu kommen, auf dem Wege zur Initiation durch die ersten Maßnahmen viel aufzuwecken in bezug auf die elementarischen Teile des Kopfes, während noch alles im tiefen Schlafe ist, was den Händen oder den Füßen entspricht.",
      "Während es beim physischen Leibe so ist, daß er einmal schläft und einmal wacht, ist es beim elementarischen Leibe so, daß nebeneinander sind die wachenden und die schlafenden Teile. Und darin besteht der Fortschritt, daß die schlafenden Teile immer mehr und mehr zu wachenden gemacht werden.",
      "Das ist es, was man eigentlich tut.",
      "Wenn der Mensch nicht eine geistige Wesenheit wäre, so könnte es nicht geschehen, was ich zum Vergleich herangezogen habe, dann könnte er nicht seinen physischen Leib im Bette liegend haben und wahrnehmen, wie er ihn auferweckt. So ist aber das Seelische noch etwas Selbständiges gegenüber dem allen, was da erweckt wird. Was Stück für Stück dieses aufweckt, das ist nicht der elementarische Leib. Das ist etwas anderes. Und wenn Sie den Begriff fassen: in deiner Seele ist etwas, was eine tätige Herrschaft ausübt über den elementarischen Leib, so daß es ihn Stück für Stück auferweckt, dann haben Sie eine konkrete richtige Vorstellung dessen, was man astralischen Leib nennt. Und leben im astralischen Leibe, sich erleben im astralischen Leibe, heißt zunächst: sich erfühlen in einer Art innerer Kraftwesenheit, welche imstande ist, nach und nach, Stück für Stück, den schlafenden elementarischen Leib zum bewußten Leben zu erwecken. Es gibt also einen Zustand, den man so bezeichnen kann: man erlebt sich jetzt außerhalb des physischen Leibes, man erlebt sich aber nicht nur in dem elementarischen Leibe, sondern in dem astralischen Leibe.",
      "Um sich klar zu werden über diesen Schritt der Initiation, ist es notwendig, daß man sich Unterscheidungsvermögen aneignet für das, was man bloß innerlich erleben kann, wenn man in seinen elementarischen Leib hineinkommt. Ich habe Ihnen geschildert, was man erlebt, wenn man in den elementarischen oder ätherischen Leib hineinkommt: man erweitert sich, man fließt aus. Das ist das konkrete Gefühl. Aber das ist auch das hauptsächlichste allgemeine Gefühl, das man hat: daß man aus dem physischen Leib herausdringt, immer weiter und weiter wird und sich hinausergießt in die Weiten der Welt. Das Sich-Hineinleben in den astralischen Leib und bewußt in dem leben, was Stück für Stück den elementarischen Leib erweckt, das ist noch mit etwas anderem verknüpft: mit einem Springen aus sich heraus, und etwas Ergreifen, was schon draußen war; nicht ein Erweitern dessen, was schon ist. Wenn man im elementarischen Leibe ist, weiß man: Der physische Leib gehört noch dazu. Wenn man sich aber in den astralischen Leib hineinlebt, so weiß man: Du bist, wie wenn du erst in dir gelebt hättest, aus dir heraus",
      "und in etwas anderes hineingedrungen, und jetzt ist dein physischer Leib - und vielleicht auch der elementarische - etwas außer dir; du bist etwas, worin du früher nicht gesteckt hast, und jetzt ist dein physischer Leib etwas, was dein Objekt geworden ist, was nicht mehr dein Subjekt ist; du schaust ihn von außen an.",
      "Dieses sich Überspringen, sein eigener Anschauer sein und sich Erfassen, ist der Übergang zu dem Sein im astralischen Leibe. Wenn man da hinüberkommt, wenn man diesen Sprung getan hat und weiß: dies bist du nun, das schaust du an wie früher eine Pflanze oder einen Stein -, dann hat man zunächst ein Gefühl, von dem man sagen kann, es wird wohl keinem zu Initiierenden auf den ersten Stufen erspart bleiben; es ist die Empfindung: Nun bist du in der übersinnlichen Welt, da breitet sie sich aus, ins Unendliche hin. Man kann nicht einmal sagen «nach allen Seiten», denn sie hat viel mehr Seiten und auch ganz andere Dimensionen als die gewöhnliche Welt. Aber man ist allein drinnen. Man ist mit seinem Leben im astralischen Leibe drinnen - und überall die Welt, unendliche Ausbreitung, nirgends ein Wesen, man selbst allein! Und es überkommt einen, was man nennen kann: das seelisch höchst gesteigerte Einsamkeitsgefühl.",
      "Es kommt darauf an, daß man solche Gefühle erträgt, daß man sie durchmachen kann, denn in dem Überwinden dieser Gefühle ergeben sich die Kräfte, die einen weiterführen, die zu Seherkräften werden. Und höchst real wird das, was ich in dem Drama «Der Hüter der Schwelle» in wenige Zeilen hineinzubringen versuchte, wo Maria den Johannes in die unendlichen Eisgefilde führt, wo die Menschenseele einsam, ganz einsam ist. Und ist man in dieser Einsamkeit drinnen, dann muß man warten, geduldig warten. Daß man warten kann, daß man sich soviel moralische Kraft angeeignet hat, um zu warten, davon hängt viel ab. Denn dann kommt etwas, was man sich so sagen kann: Ja, jetzt bist du innerhalb von Unendlichkeiten ganz allein, aber in dir steigt etwas auf wie lauter Erinnerungen, die doch wieder keine Erinnerungen sind. Ich sage, «wie lauter Erinnerungen, die doch wieder keine Erinnerungen sind», weil alle Erinnerungen des gewöhnlichen Lebens so sind, daß man sich erinnert",
      "an das, dem man einmal gegenübergestanden hat, was man einmal erlebt hat. Aber denken Sie sich, Sie ständen da mit dem Innern Ihrer Seele, und es tauchten Vorstellungen auf, die verlangen, daß Sie sie auf etwas beziehen. Aber Sie haben sie nie erlebt. Sie wissen, diese Vorstellungen beziehen sich auf Wesenheiten, aber Sie standen den Wesenheiten nie gegenüber. Dieses innere Heraufsteigen einer Welt, die einem unbekannt ist, von der man aber weiß: du trägst sie in dir, es sind lauter Abbildungen, das ist das nächste, was zu den Erlebnissen auf dem Wege zur Initiation gehört.",
      "Und dann macht man eine sonderbare Erfahrung, die Erfahrung, daß man ein Verhältnis gewinnen kann zu dem, was da an Vorstellungen auftaucht, daß man lieben und hassen kann, was da auf- taucht, daß man Ehrfurcht hegen kann gegenüber dem einen, Hochmut gegenüber dem anderen. Es erwacht nicht nur eine Summe von inneren Vorstellungen, sondern es erwacht etwas wie auf- und abwogende übersinnliche Gefühle und Empfindungen. Man ist ganz mit sich allein, allein mit seiner inneren Welt, welche da auftaucht.",
      "Man weiß zunächst selber nichts außer irgendeinem unbestimmten Dunkel, aber man ist voller Beziehung zu diesen Dingen. Nehmen wir ein charakteristisches Beispiel. Etwas, das da als Bild auftaucht, flößt einem Liebe ein. Jetzt ist man in einer starken Versuchung. Eine furchtbare Versuchung tritt auf, denn man liebt jetzt etwas, was in einem selber drinnen ist. Man ist der Versuchung ausgesetzt, die Sache deshalb zu lieben, weil sie einem selbst angehört, und man muß jetzt mit aller Kraft dahin wirken, daß man dieses Wesen nicht liebt, weil man es hat, sondern deshalb, weil es dieses oder jenes ist - trotzdem es in einem ist. Selbstlos machen das, was in dem Selbst drinnen ist, das wird Aufgabe. Und das ist eine schwere Aufgabe, eine Aufgabe, mit der sich nichts Seelisches in der gewöhnlichen Sinneswelt vergleichen läßt. Im gewöhnlichen Sinnensein ist es gar nicht möglich, daß ein Mensch ganz selbstlos liebt, was in ihm drinnen ist. Das muß er aber, wenn er dort hinaufkommt. Dadurch, daß man das Wesen überstrahlt mit der Kraft der Liebe, strahlt es selber Kraft aus, und man merkt jetzt dadurch: das will aus einem heraus. Und man merkt weiter: Je mehr man selber Liebe anwenden kann,",
      "desto mehr bekommt es selber die Kraft, etwas, was wie eine Hülle in einem ist, zu durchbrechen und hinauszudringen in die Welt. Wenn man es haßt, bekommt es ebenso Kraft; e& spannt einen dann, preßt einen und drängt sich durch, wie wenn sich die Lungen oder das Herz durch die Haut des Leibes durchdrängen wollten. Das geht durch alles, womit man sich durch Liebe und Haß in ein Verhältnis bringt. Aber der Unterschied zwischen beiden Erlebnissen ist der: Was man selbstlos liebt, das geht fort, aber man fühlt, es nimmt einen mit, man macht den Weg durch, den es selber durchmacht. Was man haßt oder dem gegenüber man hochmütig ist, das durchreißt die Hülle und geht fort und läßt einen allein, und man bleibt in der Einsamkeit. Diesen Unterschied merkt man auf einer bestimmten Stufe sehr stark: man wird mitgenommen oder zurückgelassen. Und wenn man mitgenommen wird, so hat man die Möglichkeit, hinzukommen zu dem Wesen> das man in seinem Abbild erlebt hat.",
      "Man lernt es kennen. Und dadurch, daß in einem auftauchen die Abbilder von Wesen, die man noch nicht kennt, und man zu ihnen Beziehungen erhält, kommt man aus sich heraus und kommt zu der ganzen Bevölkerung, die man in einer zweiten geistigen Welt kennenlernt. Man lebt sich ein in eine Welt, welche gewöhnlich die devachanische Welt genannt wird, die eigentliche geistige Welt, nicht etwa in die astralische Welt. Denn das ist ein vollständiges Unding, daß der Mensch durch seinen astralischen Leib, den ich beschrieben habe als den Erwecker des elementarischen Leibes, in die astralische Welt käme, sondern man kom,mt in die eigentliche geistige Welt, in das, was in meiner «Theosophie» das Geisterland genannt wird, und steht lauter geistigen Wesenheiten gegenüber.",
      "Wie man diese weiter kennenlernt, wie sie sich abstufen, wie sie zu dem werden, was beschrieben ist als die Welt der höheren Hierarchien, die wir kennengelernt haben von den Angeloi hinauf bis zu den Seraphim, davon morgen weiter."
    ],
    "sentences": [
      [
        "Wir brauchen, um zu den Aufgaben dieses kurzen Vortragszyklus zu kommen, solche Vorstellungen, wie wir sie gestern gewonnen haben, und noch einige, die wir eben haben müssen, wenn wir charakterisieren wollen, was vorgestern in dem programmatischen Vortrage angedeutet worden ist."
      ],
      [
        "Sie werden finden, daß überall, wo in der Literatur oder sonstwo von der Initiation gesprochen wird, irgendwie jenes Rätsel berührt wird, das allem Menschlichen so naheliegt: das Rätsel vom Tode.",
        "Und Sie werden finden, daß in alledem, was man Berichte nennen könnte, darauf hingewiesen wird, daß der zu Initiierende auf einer gewissen Stufe so etwas in einer etwas anderen Form durchzumachen hat, wie der Durchgang durch die Pforte des Todes es eben ist.",
        "Diese Berichte beruhen für den Okkultisten tatsächlich auf Wahrheit.",
        "Denn die Erfahrungen, die beim Aufstieg in die geistigen Welten durchzumachen sind, berühren sich mit denselben Erfahrungen, die der Mensch durchzumachen hat beim naturgemäßen Übergange vom Leben im Sinnenleibe zu jenem andersartigen Leben, das in einer ganz anderen Umhüllung stattfindet zwischen dem Tode und einer neuen Geburt.",
        "Wenn man so recht herankommen will an dasjenige, um was es sich dabei handelt, muß man zuerst fragen: Als was weiß sich denn eigentlich der Mensch im gewöhnlichen Leben? - Es ist vielleicht nicht gerade interessant, eine so abstrakte Frage aufzuwerfen, aber zum Verständnis des Initiationsvorganges ist es schon notwendig, diese Frage ins Auge zu fassen: Als was weiß sich denn die Seele?"
      ],
      [
        "Was sie während des Schlafes ist, das weiß ja die Seele nicht, denn entweder verläuft der Schlaf in Bewußtlosigkeit, oder aber es spielen in den Schlaf herein Träume, die ja erst durch den Okkultismus gedeutet werden müssen, wenn man sie in der richtigen Weise verstehen will.",
        "Bei der Frage: Was ist sich der Mensch, was ist seine Seele im gewöhnlichen Sinnensein? - kann also doch nur die Frage des"
      ],
      [
        "Tageslebens in Betracht kommen.",
        "Nun wissen wir, daß zunächst jene Tore da sind, welche wir unsere Sinnesorgane nennen, durch welche die Farben- und Lichtwelt, die Tonwelt, die Geruchwelt, Wärme und Kälte und so weiter in unsere Seele hereinströmen, und was wir im Sinnensein unsere Welt nennen, ist ja im Grunde genommen nur eine Zusammenfassung alles dessen, was eben durch die Tore unserer Sinne einströmt."
      ],
      [
        "Dann haben wir das Instrument unseres Verstandes, unserer Empfindungen, unseres Wollens; mit dem verarbeiten wir, was in der äußeren Welt uns entgegentritt.",
        "Es treten in unserer Seele auf Begierden, Wünsche, Strebungen, Befriedigungen, Unbefriedigungen, Beseligungen, Enttäuschungen und so weiter, und wenn wir den ganzen Umfang dessen, als was sich der Mensch weiß, eigentlich ins Auge fassen, so ist es alles dieses."
      ],
      [
        "Wenn man für das gewöhnliche Leben erkennen will, was Innenwelt ist, so kann man eigentlich nichts anderes anführen als die Summe dessen, was jetzt charakterisiert worden ist.",
        "Dabei kann sich der Mensch auch von außen betrachten."
      ],
      [
        "Er kann seinen Leib betrachten.",
        "Er wird sich durch die mannigfaltigsten Tatsachen, die jetzt nicht im einzelnen ausgeführt zu werden brauchen, bewußt, daß er seinen Leib als sein Werkzeug für das wache Tagesleben während des Lebens zwischen Geburt und Tod anzusehen hat."
      ],
      [
        "Es spielen in dieses Leben Sehnsüchte herein, die wir schon berührt haben; es spielt herein die Sehnsucht zu wissen, was der Mensch eigentlich innerhalb der Grenzen von Geburt und Tod ist, die Sehnsucht herauszukommen aus dem, was man das Lebensdunkel nennen könnte.",
        "Aber darüber hinaus hat eben der Mensch zunächst nichts, hat zunächst nicht im gewöhnlichen Sinnensein Erlebnisse."
      ],
      [
        "Seine Erlebnisse sind eben so, daß die auf- und ablaufenden Triebe, Begierden, Sinnesempfindungen, Vorstellungen, Verstandeskombinationen und so weiter das wache Tagesleben erfüllen.",
        "Knüpfen wir nun daran dasjenige an, was uns am Schlusse unseres gestrigen Vortrages entgegengetreten ist."
      ],
      [
        "Wir haben darauf aufmerksam gemacht, wie der Mensch, wenn er an die Grenze zwischen Sinnensein und Geistessein kommt, seine Vorstellungen ändern muß, wie er zurücklassen muß, was er gedacht"
      ],
      [
        "hat über häßlich und schön, über wahr und falsch, über gut und böse, weil diese Begriffe eine ganz andere Bedeutung und einen nach ganz anderen Richtungen hin gehenden Wert erhalten, wenn man die geistigen Welten betritt.",
        "Daraus schon können wir eine Idee bekommen, wie wir uns wandeln müssen, wenn wir in die geistigen Welten eintreten wollen.",
        "Nun, nachdem wir beobachtet haben, als was sich der Mensch weiß im wachen Tagesleben zwischen Geburt und Tod, können wir uns mit Beziehung auf das gestern Gesagte einmal fragen: Was kann der Mensch von alledem, als was er sich so weiß, mitnehmen über die Grenze, wo der Hüter der Schwelle steht?",
        "Was kann er von allem, was er an Trieben, Begierden und Leidenschaften im Sinnensein erlebt und erfährt, von seinen Empfindungen und Vorstellungen, von Verstandesbegriffen und Urteilen, die er durchmacht, mit hinübernehmen über die Grenze, wo der Hüter der Schwelle steht? - Ja, es gehört zu den ersten Schritten der Initiation, daß der Mensch erfährt: von alledem, was man so anführen kann, was man selber ist, kann man gar nichts mitnehmen!",
        "Und es ist nicht etwa übertrieben oder paradox gesprochen, sondern wörtlich wahr gesprochen, wenn man sagt: Von allem, worüber man eigentlich im Sinnensein reden kann, kann man gar nichts in die geistige Welt mit hinübernehmen, sondern man muß alles zurücklassen an der Grenze, an welcher der Hüter der Schwelle steht."
      ],
      [
        "Aber machen Sie sich nunmehr eines klar: An alledem, was man da als sich weiß im Sinnensein, haftet doch eines, ein höchst Erhebliches daran, und zwar wirklich das, worauf es ankommt bei den Schritten der Initiation.",
        "Es haftet daran, daß man das liebt und gern hat und daß man gar nicht einmal auskommt, wenn man den gewöhnlichen, etwas unsympathischen Begriff des Egoismus darauf anwendet.",
        "Dadurch ist man nicht fertig, daß man sagt Der Mensch soll seinen Egoismus ablegen, dann wird er selbstlos hinüberkommen in die Region der geistigen Welt.",
        "Das ist, wenn man trivial sprechen darf, leicht gesagt.",
        "Aber dieser Egoismus ist in den geheimeren, feineren Gliederungen seines Wesens innig zusammenhängend mit dem, was wir nicht nur egoistisch für wertvoll halten im Leben, sondern für wertvoll halten müssen, weil wir dadurch Mensch sind in"
      ],
      [
        "der Welt, in der wir uns aufzuhalten haben.",
        "Wir sind Menschen dadurch, daß wir zusammenhalten können, was wir erfahren, und daß wir in einer gewissen Weise darüber denken können, daß wir erleben können."
      ],
      [
        "Durch das alles sind wir die Menschen, die wir sind.",
        "Und was wir Tüchtiges leisten können im gewöhnlichen Sinnen- sein, leisten wir dadurch, daß wir wertschätzen unsere Fähigkeit, zusammenzuhalten in unserer Persönlichkeit, in unserer Individualität, was wir erleben."
      ],
      [
        "Und würden wir das nicht wertschätzen, was wir erleben, so würden wir Faulenzer oder träge Menschen im Leben werden und nichts für die gewöhnliche Welt erreichen.",
        "Es wäre daher oberflächlich> zu sagen: Der Egoismus ist unter allen Umständen als etwas Schädliches anzusehen."
      ],
      [
        "Denn in seiner feineren Gliederung bedeutet er die Kraft, welche den Menschen vorwärtstreibt in der Welt, in der er nun einmal inkarniert ist.",
        "Und dennoch: es muß das alles abgelegt werden, es muß zurückbleiben, muß aus dem einfachen Grunde zurückbleiben, weil es ungeeignet ist für die Welt, die wir betreten müssen."
      ],
      [
        "Wie unser Sinnenleib ungeeignet ist für ein Eisenbad von 9000C, so ist das, was wir unser Selbst nennen, mit dem, was wir lieben in der gewöhnlichen Welt, ungeeignet in der geistigen Welt.",
        "Und man muß es aus dem Grunde zurücklassen, weil einem etwas Ähnliches passieren würde, wie unserm sinnlichen Leib passieren würde, wenn wir uns in ein Eisenbad von 900CC hineinstürzen würden: wir würden keinen Aufenthalt darin haben können, würden darin zugrunde gehen."
      ],
      [
        "Nun wird Ihnen ein Gedanke auftauchen, der ganz selbstverständlich ist, der nur in seiner Tiefe erfaßt und erfühlt werden muß, der Gedanke: Wenn ich nun alles ablege> was ich bin, wovon man überhaupt reden kann im Sinnensein, was bleibt mir denn dann eigentlich?",
        "Kann ich denn dann noch selber hineingehen in die geistige Welt, wenn ich mich zuerst ablegen muß? - Das ist es, daß der Mensch nichts von dem, wovon er weiß, daß er es ist, in die über- sinnlichen Welten hinein mitnehmen kann, und daß alles, was er in diese Welten hinein mitnehmen kann, etwas ist, wovon er nichts weiß in der gewöhnlichen Welt.",
        "Das sind die verborgenen, in den Untergründen der Seele liegenden Daseinselemente, die in dem"
      ],
      [
        "Menschen drinnenstecken, von denen er nichts weiß.",
        "Und die mussen so stark sein, daß der Mensch aus dem, wovon er nichts weiß, in die geistigen Welten das Nötige hineinbringt, wenn er alles das, wovon er weiß, draußen ablegen muß.",
        "Um den Gedanken, oder besser gesagt, die Empfindung recht gründlich zu erfassen, verbinden Sie das, was eben gesagt worden ist, mit dem gewöhnlichen Todesgedanken.",
        "Es ist nur selbstverständlich für das gewöhnliche Sinnesleben, daß der Mensch alles das, als was er sich bezeichnen kann, liebt.",
        "Und weil er nichts weiter von sich weiß, so hat er bei der Unsterblichkeitssehnsucht die Sehnsucht, das zu behalten, was er im Sinnen- sein liebt.",
        "Deshalb kann der Schauer so groß werden und es kann eine Furchterfülltheit eintreten vor der geistigen Welt, weil der Gedanke auftauchen muß: Du gehst in ein wesenloses Unbestimmtes hinein, du weißt nicht, ob du dich darinnen bewahren kannst, denn das, wovon du weißt, geht dir verloren!"
      ],
      [
        "Nun gehört es zur Initiation, daß das, was in den verborgenen Untergründen der Seele liegt an Daseinselementen, schon während des Sinneslebens heraufgeholt und zum Bewußtsein gebracht wird.",
        "Das geschieht zum Teil durch die Mittel, welche geschildert sind in «Wie erlangt man Erkenntnisse der höheren Welten?», indem aus den Untergründen der Seele Erlebnisse ins Bewußtsein heraufgehoben werden, die gleichsam als ein verdichtetes, verstärktes Seelenleben herauskommen.",
        "Und dieses verdichtete, verstärkte Seelenleben, wovon man sonst nichts weiß, kann hinübergehen in die geistige Welt.",
        "Daher bereitet man sich durch Meditationen, Konzentrationen, durch das, was im «Hüter der Schwelle» genannt ist das «gedankenkräftige Verhalten der Seele», darauf vor, etwas mit hinüberzunehmen in die geistige Welt, etwas dort drüben sein zu können.",
        "Was geschieht denn aber mit dem, was man abgelegt hat?"
      ],
      [
        "Das ist nun etwas außerordentlich Wichtiges.",
        "Zunächst könnte man, wenn man bildhaft, anschaulich schildert, wirklich sagen: Das, wovon man reden kann im Sinnensein, wovon man weiß, das legt man an der Grenze beim Hüter der Schwelle ab, wie wenn man seine Kleider ausziehen und ohne Kleider hinübergehen würde in bezug auf alles Seelische in die geistige Welt.",
        "Bildhaft ist das ganz richtig"
      ],
      [
        "gesprochen.",
        "Aber die Initiation macht es notwendig, daß nicht bloß dies geschieht, sondern daß noch etwas anderes geschieht: daß man zwar sein Selbst und alles, was an einem ist, ablegt, aber doch etwas davon mitnimmt, sonst verliert man nämlich allen Zus ammenhang mit dem Sein, von dem man einzig und allein früher gewußt hat."
      ],
      [
        "Also man muß doch etwas mitnehmen!",
        "Wir stehen hier vor einem Widerspruch, der allerdings ein sehr leicht lösbarer ist: daß wir alles zurücklassen sollen und doch von dem Zurückgelassenen etwas mitnehmen sollen."
      ],
      [
        "Sie werden es leicht verstehen, wenn ich es vergleiche mit einer Erscheinung des gewöhnlichen Lebens, was es der Seele ist, wenn sie diesen Vorgang durch macht.",
        "Es gibt im Leben auch einen ähnlichen Vorgang, den wir mit diesem anderen, obwohl er viel empfindungskräftiger> viel vehementer ist, vergleichen können."
      ],
      [
        "Das ist der Vorgang, wenn wir uns an etwas erinnern, was wir im Leben erlebt haben.",
        "Was Sie gestern erlebt haben, das haben Sie zurückgelassen, aber Sie haben es in der Erinnerung mit sich genommen.",
        "Darauf kommt es an, daß man sich durch die vorhergehenden Meditationen, Konzentrationen und so weiter bereitgemacht hat, daß man, wenn man über die Schwelle in die geistigen Welten hinüberkommt, die Kraft hat, in einer übersinnlichen Erinnerung festzuhalten, was man zurückgelassen hat."
      ],
      [
        "Ist man nicht in der entsprechenden Weise vorbereitet, so hat man diese Kraft nicht, um sich daran zu erinnern.",
        "Dann ist man aber für sein Bewußtsein ein Nichts, weil man nichts weiß von sich.",
        "Das ist es, daß man sich durch übersinnliche Erinnerung, wenn man in der geistigen Welt drinnensteht, an das erinnert, was man zurückgelassen hat."
      ],
      [
        "Sonst kann man nichts mitnehmen als diese Erinnerungen, und daß man sie mitnimmt, das bewahrt einem das, was man nennen könnte die Kontinuität, die Erhaltung des Selbstes.",
        "Auch im gewöhnlichen Leben geht einem der Zusammenhang des Bewußtseins und damit das eigentliche Selbst verloren, wenn man Dinge, an die man sich erinnern sollte - sagen wir vieles in unserem Leben -, einfach auslöschen muß aus seinem Bewußtsein und krankhaft vergessen hat."
      ],
      [
        "An der fortlaufenden Erinnerung hängt vieles im gewöhnlichen Leben.",
        "An der Erinnerung im übersinnlichen Leben - die Erinnerung an das gewöhnliche"
      ],
      [
        "Leben zu bewahren - hängt alles, was die ersten Schritte der Initiation möglich macht.",
        "Diese Erinnerung ist eben möglich, und sie tritt durch die Initiation ein, und von ihr aus können Sie wieder den Faden hinüberziehen nach dem Rätsel des Todes."
      ],
      [
        "Wenn der Mensch durch den Tod hindurchgeht, so hat er zwar nicht dieselben Kräfte, die er durch die Initiation erwirbt, aber in gewisser Weise bekommt er Kräfte, wenn er seinen Leib ablegt, indem ihm andere Wesen der übersinnlichen Welt helfen.",
        "Er bekommt die Möglichkeit, die Erinnerung für das zu bewahren, was er vergessen hat, indem er seinen Leib abgelegt hat."
      ],
      [
        "Und jetzt haben Sie im Realen die Möglichkeit, sich auf die Frage zu antworten: Was bleibt von meinen Seelenerlebnissen, wenn ich durch die Pforte des Todes durchgegangen bin, wie lebt die Seele weiter?",
        "Das ist die allerwichtigste Frage."
      ],
      [
        "Und Sie haben durch die Erfahrung der Initiierten die Antwort: Die Seele lebt weiter, weil in den tiefen, verborgenen Untergründen der Seele Kräfte sind, die in der Erinnerung festhalten können, was erlebt ist.",
        "Unsterblich sein heißt, die Kraft haben, in der Erinnerung das abgelebte, das vergangene Dasein bewahren zu können."
      ],
      [
        "Das ist die eigentliche Definition der menschlichen Unsterblichkeit.",
        "Durch die Initiation wird der Beweis erbracht, der Erfahrungsbeweis, daß im Menschen Kräfte leben, die [ermöglichen, sich] nach Ablegung des sinnlichen Leibes erinnern [zu] können an alles, was der Mensch im Sinnensein und überhaupt erlebt hat."
      ],
      [
        "So bewahrt sich der Mensch selbst durch die Zukunft hindurch, so erlebt er sein früheres Sein als Erinnerungen im zukünftigen Sein.",
        "Fühlen Sie die ganze Gewalt des Gedankens, der sich durch die Initiation ergibt und der ausgesprochen werden konnte in den Worten: Das Menschenwesen ist von solcher Art, daß es durch die Kräfte der übersinnlichen Erinnerung sein eigenes Wesen durch zukünftige Zeiten trägt."
      ],
      [
        "Wenn Sie diesen Gedanken fühlen, in die Leerheit des Weltenalls hinein ihn fühlen so, daß Sie sich vorstellen die sich selbst durch die Ewigkeiten tragende Seele, dann haben Sie eine viel bessere Definition dessen, was man eine Monade nennt, als sie durch irgendwelche philosophische Begriffe gegeben werden könnte.",
        "Denn dann fühlen Sie, was eine Monade, ein in sich geschlossenes, sich"
      ],
      [
        "selber tragendes Wesen ist.",
        "Über diese Dinge sind denn doch nur Vorstellungen zu gewinnen durch die Erfahrungen der Initiation."
      ],
      [
        "Das ist erst die eine Seite dessen, was ich Ihnen zu schildern habe.",
        "Wir müssen die ersten Schritte der Initiation noch genauer betrachten, wenn wir erfühlend zu dem kommen wollen, was uns Vorstellungen über die Initiation geben kann."
      ],
      [
        "Nehmen wir an, ein Mensch habe durch gedankenkräftiges Verhalten seiner Seele, oder mit einem Fremdwort: durch Meditation es dahin gebracht, daß er außerhalb seines physischen Leibes wahrnehmen kann, daß er zunächst wahrnehmen kann in seinem elementarischen oder ätherischen Leibe.",
        "Erlebt wird dieses Wahrnehmen in jenem Leibe, der enger gebunden ist in seinen einzelnen Teilen an das Gehirn, weniger eng zum Beispiel an die Hände, erlebt wird das Sich-Einfühlen in den ~elementarischen Leib dadurch, daß man das Gefühl hat: Du weitest dich aus, du wirst breiter, fließest hinaus in die unbestimmten Weltenweiten. - So ist das subjektive Gefühl."
      ],
      [
        "Aber es ist nicht so, daß man ins Wesenlose und Unbestimmte hinausrinnt, sondern da ist alles konkretes Leben.",
        "Man lebt sich in lauter Konkretheiten hinein, und man gewinnt zugleich ganz bestimmte Erlebnisse in diesem SichAusweiten."
      ],
      [
        "Besonders ein Gefühl kann man leicht erhalten, und es wird kaum - wenn nicht ganz besondere Umstände vorliegen - jemandem, der die ersten Schritte der Initiation durchmacht, erspart bleiben, diese Erfahrung zu machen.",
        "Es ist die Erfahrung der Bangigkeit, der Ängstlichkeit, die Erfahrung, als ob man im Weltenall wäre und keinen Boden unter den Füßen hätte, ein Bedrückendes in der Seele."
      ],
      [
        "Das sind so die inneren Erlebnisse, die man dabei durchmacht.",
        "Dann aber das noch Wichtigere."
      ],
      [
        "Wenn man im gewöhnlichen Leben denkt, eine Vorstellung hat, wenn ein Gedanke den anderen kommen läßt, da fügt man den einen Gedanken zum anderen hinzu, man gliedert dann vielleicht Empfindungen hinzu, Wünsche, Wollen und so weiter, und beim gesunden Seelenleben wird man immer die Möglichkeit haben, zu sagen: Ich denke dies, ich fühle das. - Denn es wäre schon eine Unterbrechung, eine Störung des gesunden Seelenlebens, wenn man nicht die Möglichkeit hätte, in dieser Weise zu sprechen.",
        "Beim HineInwachsen"
      ],
      [
        "in den elementarischen oder ätherischen Leib weitet man sich aus, aber zugleich weiten sich die Gedanken aus.",
        "Man verliert das Gefühl, als ob man in sich wäre, wenn man denkt, und man bekommt das Gefühl: man wächst in die elementarische Welt hinein, und die ist durchzogen von Gedanken, und diese Gedanken denken sich.",
        "Das tritt als ein Erlebnis auf.",
        "Es ist so, wie wenn man ausgelöscht wäre und wie wenn sich die Gedanken denken würden, wie wenn die Gefühle, die man selbst hat oder die die Dinge haben, sich erfühlen, als ob man nicht selber wollen könnte, sondern als ob das alles in einem zum Wollen erwachte.",
        "Hingegeben sein an die Objektivität, an die Welt, das ist ein Gefühl, das man hat.",
        "Aber es ist in der Regel so - und das ist wieder eine Erfahrung bei den ersten Schritten der Initiation -, daß sich hinzugesellt ein anderes Gefühl.",
        "In demselben Maße, in dem man sich ausweitet, in dem sich die Gedanken selber denken, die Empfindungen sich erfühlen, wird das Bewußtsein immer schwächer und schwächer, immer mehr und mehr herabgestimmt; das Wissen betäubt sich."
      ],
      [
        "Nun ist die Notwendigkeit vorhanden, etwas ganz Bestimmtes in der Seele eintreten zu lassen, wenn solche Erfahrungen in der Seele gemacht werden.",
        "Es ist eine Notwendigkeit vorhanden, daß diese Dinge möglichst genau von den Seelen erfaßt werden.",
        "Deshalb habe ich, wenn auch nicht dieselben, so doch ähnliche Dinge, die in dieselbe Richtung gehen, in dem Buche «Ein Weg zur Selbsterkenntnis des Menschen» zusammengestellt, und Sie werden, wenn Sie die Vorträge in Verbindung bringen mit diesem Buche, davon mancherlei haben können.",
        "Ein ganz bestimmtes Seelisches, das man selber herbeiführt, muß dann eintreten, ähnlich wie ich es gestern geschildert habe.",
        "Man muß nämlich Selbstbesinnung üben, muß versuchen schonungslos, rücksichtslos recht grobe Fehler, von denen man weiß, daß man sie hat, sich vorzuhalten, so daß einem vor die Seele kommt, wie wenig man eigentlich dem großen Menschheits-Ideale entspricht.",
        "Man muß sich hineinfühlen in dieses Wenig-Entsprechen dem großen Menschheits-Ideale: recht meditativ, recht gedankenkräftig gerade seine moralische oder sonstige Schwachheit sich vor die Seele rufen.",
        "Wenn man das tut, wird man nämlich dadurch stärker."
      ],
      [
        "Und das, was schon angefangen hat sich abzudämpfen, was sich schon so dargestellt hat, als ob es wie in einer seelischen Ohnmacht verschwinden wollte, wird wieder heller.",
        "Man fängt wieder an, das zu sehen.",
        "Aber man erfährt wieder etwas anderes bei dieser Gelegenheit, was in einfache Worte gebracht werden kann, was aber bei den ersten Schritten auf dem Wege zur Initiation bedrückend und sogar bestürzend ist.",
        "Das alles sind Worte, die für das Seelenleben gemeint sind, nicht für das Leibesleben, denn dem, der in richtiger Weise hineingeführt wird in die geistige Welt, ist auch solche Anweisung zugeflossen, daß man von äußeren körperlichen Gefahren nicht"
      ],
      [
        "sprechen kann.",
        "Es kann ein solcher Mensch, wenn er wirklich treulich die guten Ratschläge einhält, äußerlich im Leben ein gleicher Mensch bleiben, trotzdem es innen auf- und abwogt von allerlei Peinigendem, Schmerzlichem, von Enttäuschungen und vielleicht auch erahnten Seligkeiten."
      ],
      [
        "Aber solche Dinge muß man durchmachen, denn in ihnen liegen die Kei`me des höheren Schauens, der höheren Einsicht.",
        "Etwas lernt man erkennen: man lernt, indem man außerhalb des physischen Leibes beobachten, wahrnehmen, erleben lernt, indem man also dazu kommt, in dem elementarischen Leibe zu leben, daß man in die elementarische Welt auf die geschilderte Art hineinwächst."
      ],
      [
        "Dann aber, wenn man das macht, was eben geschildert worden ist, lernt man den Grund kennen, warum diese elementarische Welt wie in einer Art Ohnmacht verschwindet, was man mit trockenem Wort so aussprechen dürfte, daß man sagt: Diese Welt mag einen nicht, sie findet, daß man nicht hineinpaßt.",
        "Und dieses Abdämpfen, dieses Verschwinden ist einfach der Ausdruck dafür: sie läßt einen nicht hinein."
      ],
      [
        "Aber indem man sich dann seine Fehler vorwirft, wird man stärker, und so hellt sich das wieder auf, was erst verschwunden war.",
        "Man bekommt aber dadurch das deutliche Gefühl: Eine übersinnliche Welt elementarischer Art ist um dich herum, aber du darfst nur bis zu einem gewissen Maße hinein."
      ],
      [
        "In dem Maße, wie du dich selbst moralisch, intellektuell immer stärker und stärker machst, läßt sie dich herein, sonst nicht; und sie zeigt dies dadurch, daß sie vor dir verschwindet."
      ],
      [
        "Das ist das Spannende, das Bedrückende oder manchmal auch das Zehrende oder Verzehrende, das - gewissermaßen - Kämpfen um die geistige Welt, und das Bewußtsein, wie unwürdig man ihrer ist.",
        "Und indem man Selbstbesinnung und das gedankenkräftige Verhalten der Seele, also Meditieren, Konzentrieren und das Sich-Durchdringen mit moralischen Impulsen kräftig fortsetzt, kann man eben immer mehr und mehr hineinkommen auf solche Art in die elementarische Welt.",
        "Aber dieses Hineinkommen in die elementarische Welt ist doch eigentlich nur die erste Stufe der Initiation.",
        "Wenn man die nächste Stufe besprechen will, muß man auf eine höchst eigentümliche Erscheinung aufmerksam machen, für die es eigentlich nichts recht Entsprechendes im gewöhnlichen Sinnensein gibt."
      ],
      [
        "Dasjenige, in dem der Mensch lebt, nachdem er elementarisch wahrnehmen kann, ist sein elementarischer Leib.",
        "Aber den hat er früher auch schon gehabt.",
        "Der Unterschied des elementarischen Leibes vor und nach dem übersinnlichen Beobachten ist nur der, daß der elementarische Leib durch die Initiation gleichsam auferweckt wird."
      ],
      [
        "Während er früher gleichsam geschlafen hat, ist er nachher auferweckt.",
        "Das ist eigentlich der treffendste Ausdruck, den man für die Sache gebrauchen kann.",
        "Aber eines wird man bemerken.",
        "Wenn man sich die Fähigkeit erworben hat, durch diese oder jene Maßnahmen, die man im Seelenleben getroffen hat, die eine oder die andere Tatsache oder das eine oder das andere Wesen der elementarischen Welt zu sehen - nun, so sieht man eben dieses eine Wesen."
      ],
      [
        "Nehmen Sie nun an, Sie haben Ihre Vorbereitungen so weit getrieben, daß Sie das eine Wesen oder ein zweites Wesen sehen.",
        "Dieses eine oder das zweite Wesen werden Sie dann wahrscheinlich, wenn Sie sich bei derselben Kraft erhalten, immer wieder sehen."
      ],
      [
        "Das ist keine Schwierigkeit.",
        "Aber Sie sehen nicht leicht etwas anderes.",
        "Wenn Sie eine Zeit aussetzen und nachher wieder zurückkommen, so sehen Sie doch wieder dasselbe.",
        "Kurz, es ist nicht in der elementarischen Welt so, wie es in der Sinneswelt ist."
      ],
      [
        "Sind für die letztere die Augen einmal präpariert, so sehen sie alles mögliche; sind die Ohren einmal präpariert, so hören sie alles gleich.",
        "So ist es nicht in der elementarischen Welt.",
        "Da müssen Sie von Stück zu Stück, von Wesensart zu"
      ],
      [
        "Wesensart immer neu die Teile Ihres elementarischen Leibes präparieren.",
        "Da müssen Sie die ganze Welt absuchen, da muß man für jedes einzelne Wesen den Ätherleib immer wieder und wieder` erwecken.",
        "Denn man stellt nur eine Beziehung, eine Verwandtschaft her zu dem, was man einmal gesehen hat, wofür man einmal den Ätherleib erweckt hat, und muß immer neue Beziehungen erwecken."
      ],
      [
        "Das kann der Ätherleib allein nicht.",
        "Er kann sich nicht beherrschen, er kann nur immer zu demselben Wesen zurückkehren, oder er kann warten, bis er präpariert ist, um andere Wesen zu sehen.",
        "Ein Mensch, der die ersten Schritte auf dem Wege zur Initiation durchgemacht hat und dazu gelangt ist, dieses oder jenes Wesen, diesen oder jenen Vorgang zu sehen, kann sich noch nicht orientieren in der geistigen übersinnlichen Welt, er kann nicht, weil er nicht zu den Wesen beliebig den Zugang hat, frei vergleichen ein Wesen mit dem anderen."
      ],
      [
        "Soll man sich orientieren, soll man nicht bloß anschauen, sondern mit Bestimmtheit sagen: dieses oder jenes ist ein Wesen, dieses oder jenes ist ein Vorgang -, so muß man es vergleichen können mit anderen Wesen und Vorgängen in der übersinnlichen Welt.",
        "Man muß den Weg vom einen zum anderen machen können, man muß sich orientieren können."
      ],
      [
        "Dieses Orientieren muß man auch erst lernen.",
        "Man lernt es dadurch, daß man durch fortgesetztes Meditieren, Sich-Durchmoralisieren Kräfte zuwachsen fühlt, die man in ihrer Tätigkeit als etwas ganz Merkwürdiges empfindet."
      ],
      [
        "Und da muß man darauf zurückkommen, wenn man es beschreiben will, daß zwar der elementarische Leib für das gewöhnliche Leben da ist, aber immerfort schlafend ist, und daß man ihn für das über- sinnliche Wahrnehmen erst erwecken muß.",
        "Aber man muß in der Seele die Kräfte haben, um ihn zu erwecken."
      ],
      [
        "Was man da tut, erlebt man in einer ganz besonderen Weise.",
        "Ich kann es nur durch einen Vergleich klarmachen."
      ],
      [
        "Denken Sie sich, Sie schlafen ein und würden wissen: Im Bette liegt dein Leib, du kannst ihn nicht rühren, aber du bist dir bewußt, er ist da!",
        "Du aber gehst in eine geistige Welt hinein und kommst nach einiger Zeit wieder zurück, um diesen Leib wieder aufzuwekken. - Das kann bewußt geschehen.",
        "Aber wie es beim Menschen im"
      ],
      [
        "gewöhnlichen Leben geschieht, so geschieht es unbewußt.",
        "Was ich Ihnen eben geschildert habe, das macht der Mensch durch; er wird in bezug auf seine Leiblichkeit wachend und schlafend, und er ist es selber, der sich aufweckt; nur hat er kein Bewußtsein, daß er es ist, der seinen physischen Leib erweckt."
      ],
      [
        "Wenn man die ersten Schritte zur Initiation durchgemacht hat, dann hat man dieses Bewußtsein.",
        "Daher ist es tatsächlich so, daß man weiß: Da hast du deinen elementarischen Leib. - Dem steht man so gegenüber, daß man fühlt: das ist der enger gebundene Teil, der dem Gehirn entspricht, dies der weiter bewegliche Teil, der den Händen entspricht, dies - das mag jetzt paradox erscheinen - der ganz bewegliche Teil, der den Füßen entspricht."
      ],
      [
        "Von alledem weiß man, aber das schläft an einem.",
        "Und indem man sich weiterentwickelt und die nötigen inneren seelischen Anstalten macht und hinkommt zur geistigen Welt, ist das ein fortwährendes Aufwecken."
      ],
      [
        "Einmal weckt man dieses Stüc\"k, ein andermal ein anderes Stück auf, einmal entzündet man diese Bewegung, einmal eine andere.",
        "Kurz, es ist ein bewußtes Auferwecken des elementarischen Leibes, so daß man sprechen könnte von einem Schlafzustand des elementarischen Leibes, in dem dieser gewöhnlich ist, und von einem Wachzustande, in welchen man ihn durch die Initiation bringt."
      ],
      [
        "Das ist der Unterschied in bezug auf Schlafen und Wachen beim physischen Leibe und beim elementarischen Leibe: beim physischen Leibe sind Schlafen und Wachen Wechselzustände, sie geschehen nacheinander; beim elementarischen Leibe geschieht nicht ein solches Nacheinander, da ist es ein Gleichzeitiges.",
        "So kann jemand dazu kommen, auf dem Wege zur Initiation durch die ersten Maßnahmen viel aufzuwecken in bezug auf die elementarischen Teile des Kopfes, während noch alles im tiefen Schlafe ist, was den Händen oder den Füßen entspricht."
      ],
      [
        "Während es beim physischen Leibe so ist, daß er einmal schläft und einmal wacht, ist es beim elementarischen Leibe so, daß nebeneinander sind die wachenden und die schlafenden Teile.",
        "Und darin besteht der Fortschritt, daß die schlafenden Teile immer mehr und mehr zu wachenden gemacht werden."
      ],
      [
        "Das ist es, was man eigentlich tut."
      ],
      [
        "Wenn der Mensch nicht eine geistige Wesenheit wäre, so könnte es nicht geschehen, was ich zum Vergleich herangezogen habe, dann könnte er nicht seinen physischen Leib im Bette liegend haben und wahrnehmen, wie er ihn auferweckt.",
        "So ist aber das Seelische noch etwas Selbständiges gegenüber dem allen, was da erweckt wird.",
        "Was Stück für Stück dieses aufweckt, das ist nicht der elementarische Leib.",
        "Das ist etwas anderes.",
        "Und wenn Sie den Begriff fassen: in deiner Seele ist etwas, was eine tätige Herrschaft ausübt über den elementarischen Leib, so daß es ihn Stück für Stück auferweckt, dann haben Sie eine konkrete richtige Vorstellung dessen, was man astralischen Leib nennt.",
        "Und leben im astralischen Leibe, sich erleben im astralischen Leibe, heißt zunächst: sich erfühlen in einer Art innerer Kraftwesenheit, welche imstande ist, nach und nach, Stück für Stück, den schlafenden elementarischen Leib zum bewußten Leben zu erwecken.",
        "Es gibt also einen Zustand, den man so bezeichnen kann: man erlebt sich jetzt außerhalb des physischen Leibes, man erlebt sich aber nicht nur in dem elementarischen Leibe, sondern in dem astralischen Leibe."
      ],
      [
        "Um sich klar zu werden über diesen Schritt der Initiation, ist es notwendig, daß man sich Unterscheidungsvermögen aneignet für das, was man bloß innerlich erleben kann, wenn man in seinen elementarischen Leib hineinkommt.",
        "Ich habe Ihnen geschildert, was man erlebt, wenn man in den elementarischen oder ätherischen Leib hineinkommt: man erweitert sich, man fließt aus.",
        "Das ist das konkrete Gefühl.",
        "Aber das ist auch das hauptsächlichste allgemeine Gefühl, das man hat: daß man aus dem physischen Leib herausdringt, immer weiter und weiter wird und sich hinausergießt in die Weiten der Welt.",
        "Das Sich-Hineinleben in den astralischen Leib und bewußt in dem leben, was Stück für Stück den elementarischen Leib erweckt, das ist noch mit etwas anderem verknüpft: mit einem Springen aus sich heraus, und etwas Ergreifen, was schon draußen war; nicht ein Erweitern dessen, was schon ist.",
        "Wenn man im elementarischen Leibe ist, weiß man: Der physische Leib gehört noch dazu.",
        "Wenn man sich aber in den astralischen Leib hineinlebt, so weiß man: Du bist, wie wenn du erst in dir gelebt hättest, aus dir heraus"
      ],
      [
        "und in etwas anderes hineingedrungen, und jetzt ist dein physischer Leib - und vielleicht auch der elementarische - etwas außer dir; du bist etwas, worin du früher nicht gesteckt hast, und jetzt ist dein physischer Leib etwas, was dein Objekt geworden ist, was nicht mehr dein Subjekt ist; du schaust ihn von außen an."
      ],
      [
        "Dieses sich Überspringen, sein eigener Anschauer sein und sich Erfassen, ist der Übergang zu dem Sein im astralischen Leibe.",
        "Wenn man da hinüberkommt, wenn man diesen Sprung getan hat und weiß: dies bist du nun, das schaust du an wie früher eine Pflanze oder einen Stein -, dann hat man zunächst ein Gefühl, von dem man sagen kann, es wird wohl keinem zu Initiierenden auf den ersten Stufen erspart bleiben; es ist die Empfindung: Nun bist du in der übersinnlichen Welt, da breitet sie sich aus, ins Unendliche hin.",
        "Man kann nicht einmal sagen «nach allen Seiten», denn sie hat viel mehr Seiten und auch ganz andere Dimensionen als die gewöhnliche Welt.",
        "Aber man ist allein drinnen.",
        "Man ist mit seinem Leben im astralischen Leibe drinnen - und überall die Welt, unendliche Ausbreitung, nirgends ein Wesen, man selbst allein!",
        "Und es überkommt einen, was man nennen kann: das seelisch höchst gesteigerte Einsamkeitsgefühl."
      ],
      [
        "Es kommt darauf an, daß man solche Gefühle erträgt, daß man sie durchmachen kann, denn in dem Überwinden dieser Gefühle ergeben sich die Kräfte, die einen weiterführen, die zu Seherkräften werden.",
        "Und höchst real wird das, was ich in dem Drama «Der Hüter der Schwelle» in wenige Zeilen hineinzubringen versuchte, wo Maria den Johannes in die unendlichen Eisgefilde führt, wo die Menschenseele einsam, ganz einsam ist.",
        "Und ist man in dieser Einsamkeit drinnen, dann muß man warten, geduldig warten.",
        "Daß man warten kann, daß man sich soviel moralische Kraft angeeignet hat, um zu warten, davon hängt viel ab.",
        "Denn dann kommt etwas, was man sich so sagen kann: Ja, jetzt bist du innerhalb von Unendlichkeiten ganz allein, aber in dir steigt etwas auf wie lauter Erinnerungen, die doch wieder keine Erinnerungen sind.",
        "Ich sage, «wie lauter Erinnerungen, die doch wieder keine Erinnerungen sind», weil alle Erinnerungen des gewöhnlichen Lebens so sind, daß man sich erinnert"
      ],
      [
        "an das, dem man einmal gegenübergestanden hat, was man einmal erlebt hat.",
        "Aber denken Sie sich, Sie ständen da mit dem Innern Ihrer Seele, und es tauchten Vorstellungen auf, die verlangen, daß Sie sie auf etwas beziehen.",
        "Aber Sie haben sie nie erlebt.",
        "Sie wissen, diese Vorstellungen beziehen sich auf Wesenheiten, aber Sie standen den Wesenheiten nie gegenüber.",
        "Dieses innere Heraufsteigen einer Welt, die einem unbekannt ist, von der man aber weiß: du trägst sie in dir, es sind lauter Abbildungen, das ist das nächste, was zu den Erlebnissen auf dem Wege zur Initiation gehört."
      ],
      [
        "Und dann macht man eine sonderbare Erfahrung, die Erfahrung, daß man ein Verhältnis gewinnen kann zu dem, was da an Vorstellungen auftaucht, daß man lieben und hassen kann, was da auf- taucht, daß man Ehrfurcht hegen kann gegenüber dem einen, Hochmut gegenüber dem anderen.",
        "Es erwacht nicht nur eine Summe von inneren Vorstellungen, sondern es erwacht etwas wie auf- und abwogende übersinnliche Gefühle und Empfindungen.",
        "Man ist ganz mit sich allein, allein mit seiner inneren Welt, welche da auftaucht."
      ],
      [
        "Man weiß zunächst selber nichts außer irgendeinem unbestimmten Dunkel, aber man ist voller Beziehung zu diesen Dingen.",
        "Nehmen wir ein charakteristisches Beispiel.",
        "Etwas, das da als Bild auftaucht, flößt einem Liebe ein.",
        "Jetzt ist man in einer starken Versuchung.",
        "Eine furchtbare Versuchung tritt auf, denn man liebt jetzt etwas, was in einem selber drinnen ist.",
        "Man ist der Versuchung ausgesetzt, die Sache deshalb zu lieben, weil sie einem selbst angehört, und man muß jetzt mit aller Kraft dahin wirken, daß man dieses Wesen nicht liebt, weil man es hat, sondern deshalb, weil es dieses oder jenes ist - trotzdem es in einem ist.",
        "Selbstlos machen das, was in dem Selbst drinnen ist, das wird Aufgabe.",
        "Und das ist eine schwere Aufgabe, eine Aufgabe, mit der sich nichts Seelisches in der gewöhnlichen Sinneswelt vergleichen läßt.",
        "Im gewöhnlichen Sinnensein ist es gar nicht möglich, daß ein Mensch ganz selbstlos liebt, was in ihm drinnen ist.",
        "Das muß er aber, wenn er dort hinaufkommt.",
        "Dadurch, daß man das Wesen überstrahlt mit der Kraft der Liebe, strahlt es selber Kraft aus, und man merkt jetzt dadurch: das will aus einem heraus.",
        "Und man merkt weiter: Je mehr man selber Liebe anwenden kann,"
      ],
      [
        "desto mehr bekommt es selber die Kraft, etwas, was wie eine Hülle in einem ist, zu durchbrechen und hinauszudringen in die Welt.",
        "Wenn man es haßt, bekommt es ebenso Kraft; e& spannt einen dann, preßt einen und drängt sich durch, wie wenn sich die Lungen oder das Herz durch die Haut des Leibes durchdrängen wollten.",
        "Das geht durch alles, womit man sich durch Liebe und Haß in ein Verhältnis bringt.",
        "Aber der Unterschied zwischen beiden Erlebnissen ist der: Was man selbstlos liebt, das geht fort, aber man fühlt, es nimmt einen mit, man macht den Weg durch, den es selber durchmacht.",
        "Was man haßt oder dem gegenüber man hochmütig ist, das durchreißt die Hülle und geht fort und läßt einen allein, und man bleibt in der Einsamkeit.",
        "Diesen Unterschied merkt man auf einer bestimmten Stufe sehr stark: man wird mitgenommen oder zurückgelassen.",
        "Und wenn man mitgenommen wird, so hat man die Möglichkeit, hinzukommen zu dem Wesen> das man in seinem Abbild erlebt hat."
      ],
      [
        "Man lernt es kennen.",
        "Und dadurch, daß in einem auftauchen die Abbilder von Wesen, die man noch nicht kennt, und man zu ihnen Beziehungen erhält, kommt man aus sich heraus und kommt zu der ganzen Bevölkerung, die man in einer zweiten geistigen Welt kennenlernt.",
        "Man lebt sich ein in eine Welt, welche gewöhnlich die devachanische Welt genannt wird, die eigentliche geistige Welt, nicht etwa in die astralische Welt.",
        "Denn das ist ein vollständiges Unding, daß der Mensch durch seinen astralischen Leib, den ich beschrieben habe als den Erwecker des elementarischen Leibes, in die astralische Welt käme, sondern man kom,mt in die eigentliche geistige Welt, in das, was in meiner «Theosophie» das Geisterland genannt wird, und steht lauter geistigen Wesenheiten gegenüber."
      ],
      [
        "Wie man diese weiter kennenlernt, wie sie sich abstufen, wie sie zu dem werden, was beschrieben ist als die Welt der höheren Hierarchien, die wir kennengelernt haben von den Angeloi hinauf bis zu den Seraphim, davon morgen weiter."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "FÜNFTER VORTRAG München, 29. August 1912",
    "paragraphs": [
      "Gestern versuchte ich mit Worten, die nun einmal für solche Dinge möglich sind, zu charakterisieren den Unterschied des Herausrükkens aus dem physischen Leibe zu dem Erleben, dem Erfühlen im ätherischen oder elementarischen Leibe und im astralischen Leibe. Und ich bemerkte, daß das Erleben so verläuft, daß das Sich-Hineinleben in den elementarischen oder ätherischen Leib sich ausnimmt wie eine Art Hinausfließen in die Weiten der Welt, wobei man das Bewußtsein durchaus behält, daß man von einem Mittelpunkte, nämlich von seiner eigenen Leiblichkeit, nach allen Seiten ins Unbegrenzte ausströmt.",
      "Das Erleben aber im astralischen Leibe stellt sich so dar, daß es sich wie ein Aus.sich.Herausspringen und Hinein- springen in den astralischen Leib ausnimmt, so daß man sich wirklich jetzt erst erlebend fÜhlt so außerhalb seines physischen Leibes, daß man alles, was man war im physischen Leibe, was man «sich selbst» nennt im physischen Leibe, wie etwas empfindet, was man außer sich hat, wie ein Außer-sich-Seiendes. In einem anderen ist man drinnen.",
      "Ich habe schon gestern darauf hingedeutet, daß die Welt, der man sich dann gegenüber befindet, die Bezeichnung des Geisterlandes tragen muß in Gemäßheit zum Beispiel meiner «Theosophie». Man könnte auch sagen, es sei der niedere Mentalplan, denn es wäre unrichtig zu glauben, daß, wenn man in richtiger, selbstloser Weise dazu gelangt, im astralischen Leibe zu leben, man dann in dem wäre, was man gewöhnlich die astralische Welt nennt, indem man mit diesem Worte etwas Niedriges verbindet.",
      "Nun ist der Unterschied gegenüber dem Leben, Beobachten und Erfahren im Sinnensein und dem Erfahren in dem astralischen Leibe gegenüber dem Geisterlande durchaus verschieden, ganz gewaltig verschieden. Denn im Sinnensein stehen wir gegenüber Stoffen, Kräften, Dingen, Vorgängen und so weiter. Wir stehen auch Wesen gegenüber im Sinnensein, stehen ja vor allen Dingen außer den Wesen der anderen Naturreiche - sofern wir berechtigt sind, sie so zu",
      "nennen - unseren eigenen Mitmenschen gegenüber. Wir stehen im Sinnensein diesen anderen Wesenheiten so gegenüber, daß wir wissen, diese Wesenheiten nehmen in sich auf die Stoffe und Kräfte der Welt eben des Sinnenseins, durchdringen sich damit und leben dadurch mit dem Leben, welches verläuft in den Naturgesetzen und durch die Naturkräfte der äußeren Welt. Kurz, wir müssen unter",
      "scheiden im Sinnensein zwischen dem Naturverlauf und den Wesenheiten, die sich innerhalb dieses Naturverlaufes ausleben und sich mit den Stoffen und Kräften desselben durchdringen. Wir haben den Naturverlauf und die Wesenheiten.",
      "Nehmen wir im astralischen Leibe in der geistigen Welt wahr, so können wir diesen Unterschied auch nicht mehr so machen. Wir stehen eigentlich in dieser geistigen Welt nur Wesenheiten gegenüber, und diesen Wesenheiten steht nicht das entgegen, was man Naturverlauf nennen könnte.",
      "Alles ist Wesen, was einem begegnet, wozu man auf die Weise, wie es gestern angedeutet worden ist, geführt wird. Überall wo etwas ist, ist Wesen> und man kann nicht sagen wie im Sinnensein: Dort ist ein Tier und dort sind äußere Stoffe, die von ihm gegessen werden. - Diese Zweiheit gibt es dort nicht, sondern was ist, ist Wesen.",
      "Und wie man sich zu diesen Wesen zu stellen hat, habe ich auch schon gesagt: daß es hauptsächlich die Welt der Hierarchien ist, die wir von anderen Gesichtspunkten aus öfter charakterisiert haben. In ihrer Stufenfolge lernt man die Welt der Hierarchien kennen, von denjenigen Wesenheiten an, die man zunächst kennenlernt als die Angeloi und Archangeloi, Engel und Erzengel, wie sie in unserer Terminologie genannt werden, bis zu den Wesenheiten, die einem fast zu entschwinden scheinen, so undeutlich werden sie, den Cherubim und Seraphim.",
      "Aber es ist eines möglich, wenn man sich in diesen Welten befindet: eine Beziehung zu diesen Wesenheiten zu gewinnen. Was man im Sinnensein ist, das muß man vorher zurücklassen im Sinne der gestrigen Auseinandersetzungen; aber wie ich Ihnen gesagt habe, man behält es doch zurück in der Erinnerung.",
      "Man trägt die Erinnerung an das Abgelebte in diese Welten hinein, und wie man im Sinnensein auf die Erinnerungen zurücksieht, so blickt man auf das, was man im Sinnensein",
      "ist, von der höheren Welt aus zurück, man hat es in der Erinnerungsvorstellung.",
      "Nun ist gut, wenn man die ersten Schritte der Initiation in die höheren Welten hinaufrückt, daß man unterscheiden lernt zwischen einem ersten Schritt und einem folgenden Schritt. Es ist nicht gut, wenn man diese Unterscheidung nicht machen lernt.",
      "Sie besteht im wesentlichen darin, daß man sich am besten orientieren lernt in den höheren Welten, wenn man zu den ersten Erinnerungsvorstellungen, die man da hinüberträgt und die einen an das Sinnensein erinnern, nicht die Vorstellung des eigenen physischen Leibes und seiner Gestalt hat. Es ist eben eine Erfahrung, daß es besser ist.",
      "Und jeder, der Rat geben soll für diejenigen Übungen, die gemacht werden sollen, um die ersten Schritte der Initiation herbeizuführen, sieht darauf, daß zu den ersten Erinnerungsvorstellungen nach Überschreiten der Grenze, nach dem Vorbeigelangen an dem Hüter der Schwelle nicht eine Anschauung der physischen Leibesform gehört, sondern daß die ersten Erinnerungsvorstellungen im wesentlichen solche sind, die man zusammenfassen könnte mit der Bezeichnung: moralisch-intellektuelle Empfindung seiner selbst. Das sollte man zuerst empfinden, wie man sich moralisch zu taxieren hat, sollte empfinden, welche moralischen oder unmoralischen Neigungen man hat, welches Wahrheitsgefühl oder Oberflächlichkeitsgefühl man hat, empfinden also, wie man sich zu bewerten hat als Seelenmensch.",
      "Das ist es, was als erste Empfindung auftritt. Es tritt nicht so auf> daß man den Ausdruck dafür am besten wählt mit Worten, die dem Sinnensein entnommen sind, denn es ist das Erleben viel intensiver mit uns verbunden, als im Sinnensein etwas Ähnliches ist, wenn man eben hineintritt in die geistige Welt.",
      "Nachdem man etwas getan hat, womit man moralisch nicht einverstanden sein kann, erfüllt sich das ganze Innensein, das man da hat, wie mit einer Bitternis, wie mit etwas, was sich in die Welt, in welche man sich da hineingelebt hat, ausbreitet, was diese Welt erfüllt mit einem Aroma von Bitternis, wobei ich nicht zu denken bitte an ein sinnliches Aroma, aber man fühlt herankommen ein Durchdrungensein mit einem Aroma von Bitternis. Was man moralisch rechtfertigen kann, ist mit",
      "einem sympathischen Aroma erfüllt. Man könnte auch sagen: dunkel, finster ist die Sphäre, in die man hineinkommt, wenn man mit etwas nicht einverstanden war, licht und hell ist die Sphäre der Welt, in die man hineinkommt, wenn man mit sich zufrieden sein kann. So also sollen sein, damit man sich gut orientieren kann, die Bewertungen moralischer oder intellektueller Art, die man sich angedeihen lassen kann und die einem wie der Luftkreis die Welt erfüllen, in die man eintritt. So ist es am besten, wenn man eben seelisch diese Welt empfindet, und wenn erst, nachdem man sich vertraut und bekannt gemacht hat mit diesem seelischen Erfühlen - sagen wir des geistigen Raumes -, die Erinnerung auftritt, die ganz die Form und Gestalt haben kann auch dessen, was physische Leibesform im Sinnensein ist, so daß sich einem diese gleichsam hineinstellt in die neu gewonnene moralische Atmosphäre.",
      "Was ich Ihnen hier beschrieben habe, kann aber auch nicht nur zum Beispiel mitten aus dem Tagesleben heraus auftreten, daß es so kommt wie ein Eintreten in die geistige Welt, wenn man die entsprechenden Schritte zur Initiation gemacht hat, sondern es kann auch noch anders auftreten. Ob es in der einen oder anderen Weise auftritt, das hängt im Grunde genommen von dem Karma des einzelnen Menschen ab, hängt von der ganzen Art seiner Veranlagung ab. Man kann nicht sagen, daß die eine Art des Auftretens besser oder weniger gut wäre als die andere; es kann das eine und das andere vorkommen. Es kann mitten aus dem Tagesleben heraus der Mensch sich wie hineingezogen fühlen in die geistige Welt, aber es kann auch so auftreten, daß er eine andere Art des Erlebens gegenüber dem Schlafe bekommt. Das gewöhnliche Erleben gegenüber dem Schlafe ist ja so, daß der Mensch mit dem Eintreten in den Schlaf bewußtlos wird> daß er mit dem Aufwachen sein Bewußtsein wiedergewinnt, und daß er dann im Tagesleben - mit Ausnahme der Erinnerung an die Träume - nicht eine Erinnerung an das Schlaf- leben hat; er erlebt es bewußtlos. Es kann nun auch das für die ersten Schritte der Initiation auftreten> daß sich etwas anderes in dem Schlaileben ausbreitet, so daß zunächst eine andere Art des Einschlafens eintritt. Man erlebt eine andere Art des Bewußtseins mit dem",
      "Eintritt in das Schlafleben. Die dauert, mehr oder weniger von bewußtlosen Zeiten unterbrochen, verschieden lange, je nachdem der Mensch weiter fortgeschritten ist, aber dann, wenn es gegen den Morgen zugeht, erlischt sie wieder. Und in der ersten Zeit nach dem Einschlafen tritt das ein, was man nennen kann eine Erinnerung an sein moralisches Verhalten, an seine Seelenqualitäten. Diese Erinnerung ist besonders stark nach dem Einschlafen und nimmt immer mehr und mehr ab, je weiter es dem Aufwachen zugeht.",
      "Es ist also> was da als Folge der Übungen zu den ersten Schritten der Initiation eintreten kann, ein Aufhellen, ein Durchhellen des Schlafbewußtseins, das sonst bewußtlos ist, mit Bewußtheit. Da gelangt man dann auch in die Welten der höheren Hierarchien hinein, fühlt sich ihnen angehörend. Aber es muß jetzt dieses Drinnenleben in der Welt, wo alles Wesenheit ist, gegenüber der gewöhnlichen Welt des Sinnenseins etwa in folgender Weise charakterisiert werden. In der Sinneswelt steht zum Beispiel ein Blumentopf vor dem Beobachter, der Beobachter steht davor, der Blumentopf ist draußen, außer ihm, er beobachtet ihn, indem er sich hinstellt und ihn ansieht. Mit einer solchen Beobachtung können wir das Erleben in der eben gemeinten höheren Welt gar nicht vergleichen. Sie würden sich eine ganz falsche Vorstellung machen, wenn Sie glaubten, daß man da drinnen herumgeht und die Wesenheiten auch so von außen ansieht, indem man sich vor sie hinstellt und sie beobachtet, wie man in der Sinneswelt etwa einen Blumenstrauß beobachtet. So ist es nicht. Sondern wenn man etwas vergleichen will im Sinnensein mit der Art> wie man zu der Welt der Hierarchien steht, so könnte es nur das Folgende sein. Es ist ja ein Vergleich, den ich brauche, aber man kann es sich dadurch klarmachen.",
      "Nehmen Sie an, Sie setzen sich irgendwo nieder und nehmen sich vor, nicht über dieses oder jenes mühevoll nachzudenken, sondern Sie wollen zunächst eigentlich über gar nichts Besonderes denken. Wie unhervorgerufen erhebe sich in Ihnen irgendein Gedanke, an den Sie zunächst nicht gedacht haben. Er nimmt Ihre Seele so in Anspruch, daß er sie erfüllt, so daß Sie zu dem Gefühl kommen können: Sie können diesen Gedanken gar nicht mehr unterscheiden von",
      "sich selbst, Sie seien ganz eins mit dem Gedanken, der da aufgetaucht ist. Wenn Sie das Gefühl haben, der Gedanke lebt und zieht Ihre Seele mit sich, die ist mit ihm verbunderi~; und man könnte ebensogut sagen, der Gedanke ist in der Seele wie die Seele im Gedanken -, so ist das etwas Ähnliches im Sinnensein, wie man sich bekannt macht und benimmt mit den Wesenheiten der höheren Hierarchien. Die Worte «man ist neben ihnen, man ist außer ihnen» verlieren allen Sinn. Man ist mit ihnen, wie die Gedanken mit einem leben, aber nicht so, daß man sagen kann: die Gedanken leben in einem -, sondern, daß man sagen muß: der Gedanke denkt sich in einem. - Sie erleben sich, und man erlebt das Erleben derWesenheiten mit. Man ist drinnen in den Wesenheiten, man ist eins mit ihnen, so daß man sein ganzes Wesen in der Sphäre, in der die Wesenheiten leben, ausgegossen hat und man ihr Sein miterlebt, indem man ganz genau weiß, sie erleben sich darinnen.",
      "Es darf niemand glauben, daß er gleich nach den ersten Schritten auf dem Wege zur Initiation das Gefühl habe, er erlebe alles, was diese Wesenheiten erleben. Er braucht durchaus nicht mehr zu wissen als, er ist diesen Wesenheiten gegenüber, wie er im Sinnensein einem Menschen gegenüber ist, den er zum ersten Male sieht. Die Berechtigung des Ausdruckes «die Wesenheiten erleben sich in einem», bleibt bestehen, und doch braucht man auf die erste Bekanntschaft hin nicht mehr zu wissen, als man bei einem Menschen weiß, dem man zum ersten Male begegnet. In dieser Art also ist es ein Miterleben. Das wird immer intensiver und intensiver, und dadurch dringt man auch immer mehr und mehr in das Wesen dieser Wesenheiten ein.",
      "Nun aber verbindet sich mit dem, was so als ein geistiges Erleben geschildert worden ist, etwas anderes. Es verbindet sich damit ein gewisses Grundgefühl, das eigentlich wie eine Art realen Ergebnisses aller einzelnen Erlebnisse in der Seele sitzt. Es ist ein Grundgefühl, das ich Ihnen vielleicht an seinem Gegensatz darstellen kann. Genau entgegengesetzt diesem Grundgefühl, das man da erlebt, ist in der Sinneswelt das, was man erlebt, wenn man an irgendeinem Orte steht und sich ansieht, was ringsherum ist. Denken Sie sich, es stände",
      "jemand in der Mitte des Saales und sähe alles, was hier ist. Da würde er sagen: hier ist der Mensch, dort jener Mensch und so weiter. Das wäre sein Verhältnis zur Umwelt. Das ist aber das Gegenteil der Grundstimmung, die man in der eben charakterisierten Welt hat. Da kann man nicht sagen: ich bin hier, dort ist dieses Wesen, dort jenes -, sondern da muß man sagen: ich bin dieses Wesen. -",
      "Denn tatsächlich ist das eine wahre Empfindung. Was ich eben für alle einzelnen Wesenheiten gesagt habe, das empfindet man auch der Gesamtheit der Welt gegenüber. Man ist eigentlich alles selber. Dieses In-dem-Wesen-Sein breitet sich aus über die ganze Seelenstimmung. Diese Seelenstimmung ist in der Tat da, wenn bewußt die Zeit vom Einschlafen bis zum Aufwachen erlebt wird. Da kann man gar nicht beim bewußten Erleben sich anders fühlen als sich ausgegossen über alles, was man erlebt, sich in allem drinnen, bis ans Ende der Welt, die man überhaupt noch wahrnehmen kann.",
      "Ich habe einmal folgendes versucht, und ich möchte das als eine Episode hier einschalten, nicht um Ihnen etwas Besonderes zu sagen, sondern nur, um mich erklärlich zu machen. Es ist mir nämlich vor Jahren schon aufgefallen, daß gewisse mehr oder weniger über- sinnliche Zustände in den großen Weltdichtungen wie in einem Abglanz einem entgegentreten. Ich meine nämlich, wenn der Hellseher sich klarmacht, was er in gewissen übersinnlichen Erlebnissen als Grundstimmung der Seele hat, und dann die Weltliteratur durchgeht, so findet er bei den wirklich großen Dichtungen da oder dort solche Stimmungen, die gewisse Kapitel oder Abschnitte von diesen Dichtungen durchziehen. Das brauchen nicht etwa okkulte Erlebnisse der Dichter zu sein. Aber der Hellseher kann sich sagen, wenn er das, was er als Seelenstimmung erlebt hat, wie in einem Nachklange in der Sinneswelt wiedererleben will, so kann er zu diesen oder jenen großen Dichtungen gehen und findet dort etwas wie ein Schattenbild in der betreffenden Dichtung. Wenn der Hellseher mit seiner Erfahrung zum Beispiel Dante liest, so hat er zuweilen dieses Gefühl, daß ein solcher Abglanz, Schatten, die man eigentlich richtig in ihrem ursprünglichen Zustande nur hellseherisch erleben kann, in der Dichtung sind. Nun versuchte ich also einmal, gewisse",
      "Zustände, die geschildert werden können, in den Dichtungen aufzusuchen, um eine Art Konkordanz zu bekommen zwischen Erlebnissen in den höheren Welten und dem, was wie im Abglanz in der physischen Welt vorhanden ist. Und zwar fragte ich mich: Könnte es nicht etwa sein, daß jene eigentümliche Seelenstimmung, welche über die Seele ausgegossen ist, wenn ein vollbewußtes Schlafen stattfindet - also ein Sein in den höheren Welten, wie ich es jetzt beschrieben habe, aber in der Stimmung erfaßt -, sich in der Weltliteratur auch im Nachklange in der Stimmung findet? - So direkt hat sich allerdings nichts ergeben.",
      "Aber bei einer anderen Stellung der Frage ergab sich etwas. Man kann sich nämlich auch fragen, weil die Erlebnisse es gestatten: Wie würde ein anderes Wesen, das nicht Mensch ist, also zum Beispiel irgendein anderes Wesen der höheren Hierarchien, diese Seelenstimmung empfinden, das Drinnensein in den höheren Welten?",
      "Oder genauer gesprochen: Der Mensch fühlt sich in dieser Welt drinnen und schaut Wesen der anderen Hierarchien. Wie man nun in der Sinneswelt fragen kann: Was empfindet ein anderer Mensch gegenüber einer Sache, die man selbst empfindet? - so kann man auch gegenüber einem Wesen der höheren Hierarchien diese Frage aufwerfen und hat die Möglichkeit, sich eine Vorstellung zu bilden, was ein anderes Wesen erlebt.",
      "Da kann man sich dann gegenüber dem Leben in den höheren Welten, wie es beim wirklich bewußten Schlafe möglich sein würde, eine bestimmte Art von höherem Erleben vorstellen, als es beim Menschen selber der Fall ist, aber von solchem Erleben, das doch allen möglichen Anteil hat an der Menschenseele. Man kann also an ein Wesen denken, das in eine höhere Hierarchienreihe hineingehört, als es der Mensch auf der Erde ist, das aber doch auf höhere Art alles Menschliche noch empfinden kann.",
      "Wenn man die Frage so stellt, wenn man also nicht auf den gewöhnlichen Menschen reflektiert, sondern auf einen typischen Menschen, und sich die Stimmung vorstellt, so bekommt man die Möglichkeit, etwas in der Weltliteratur zu finden, von dem man sich immerhin den Begriff bilden kann: es ist ausgegossen eine solche Stimmung im Nachklange, von der man eigentlich nur eine richtige Vorstellung bekommt im ursprünglichen Zustande, wenn",
      "man sich in die jetzt geschilderte, charakterisierte Welt hineinversetzt. Nun findet sich allerdings nichts innerhalb der europäischen Literatur, von dem man sagen könnte: Es ist die Seelenstimmung darin fühlbar von dem, was ausgegossen ist über eine Seele, die sich in allem fühlt in der charakterisierten Welt. Aber es ist wunderbar, wie man anfängt in einer neuen Weise zu begreifen und sich aufs neue bewundernd entzückt zu fühlen, wenn man diese Stimmung auf sich wirken läßt im Nachklange, ausgehend von den Reden des Krishna in der «Bhagavad Gita». Ein ganz neues Licht gießt sich aus über diese Zeilen der Bhagavad Gita, wenn man sich vergegenwärtigt, es wäre das nicht in den Worten, sondern in der ausgegossenen Stimmung im Nachklange enthalten, was ich eben jetzt geschildert habe. Ich wollte das nur wie eine Illustration des Hellsehens schildern und es so schildern, daß Sie nun diese Dichtung in die Hand nehmen können und versuchen können die Stimmung aufzufinden, die darin ausgegossen ist, und von da ausgehend ein Gefühl sich er- werben, was das entsprechende Erlebnis des Hellsehers ist, wenn er aus dem Tagesleben bewußt hinüberversetzt ist in die entsprechenden Welten, oder wenn Bewußtheit über den Schlaf sich ausdehnt.",
      "Diese Stimmung, dieses Grundgefühl hat noch etwas anderes beigemischt, es gesellt sich noch etwas anderes hinzu. Und da kann ich allerdings nicht anders, als dadurch einen Begriff davon hervorzurufen, daß ich versuche, in Worten - Worte müssen ja immer aus dem Sinnensein entlehnt werden - so gut es geht das zu schildern, was da erlebt wird. Was erlebt wird, ist etwa folgendes:",
      "Man fühlt sich, soweit man überhaupt von einer Welt etwas fühlt, in diese Welt ergossen. Man fühlt eigentlich nirgends etwas Äußerliches zunächst als nur an dem einen Punkt der Welt, wo man vorher drinnen war. Das fühlt man als das einzige Äußerliche. Was man verbrochen hat, was man Gutes getan hat, das findet man in den einen Punkt der Welt zusammengedrängt. Das ist äußerlich. Im übrigen fühlt man sich mit Qem, was man selbst angerichtet hat in der Welt, über die ganze Welt ausgegossen. Namentlich hat man das Gefühl, daß es ein Unding ist, dieses Verhältnis zur Welt so zu erleben, daß man gewisse Worte darauf anwendet, die natürlich sind im",
      "Sinnensein. So hören zum Beispiel die Worte «vorher» und «nachher» auf, einen Sinn zu haben. Denn mit dem Einschlafen ist es ja so, daß man nicht empfindet: jetzt ist das vorher, und das Aufwachen wird nachher sein, sondern man empfindet gewisse Erlebnisse, die mit dem Einschlafen eintreten, die dann weiter geschehen. Wenn man aber eine gewisse Summe von Erlebnissen durchlebt hat, steht man in einer gewissen Beziehung wieder an demselben Punkt, aber man steht nicht so an demselben Punkt, wie man beim Einschlafen gestanden hat. Wenn man von vorher und nachher spricht, so ist",
      "das Vorher, wenn man es graphisch bezeichnet, in A und das Nachher in B. Man hat vielmehr das Gefühl: eingeschlafen bin ich. Dann wäre schon nicht richtig gebraucht. Es haben sich eben Erlebnisse abgespielt. Vorher und nachher verliert den Sinn dabei. Und wenn ich jetzt das Wort anwende - aber es ist nicht richtig! -, nach einer gewissen Zeit steht man da, wo man`vorher gestanden hat, so muß man sich denken, man steht sich gleichsam gegenüber, wie wenn man aus seinem Leibe hinausgegangen, herumgegangen wäre und hinschauen würde auf sich selber. Man steht also ungefähr an demselben Punkt, wo man gestanden hat beim Herausgehen, aber man steht sich gegenüber. Man hat die Richtung geändert. Dann - wieder nur vergleichsweise gebraucht - gehen die Ereignisse weiter, und es geht so weiter, wie wenn man wieder zum Leibe zurückgeht und wieder dann drinnen ist. Man erlebt nicht ein Vorher und Nachher, sondern man kann es nicht anders bezeichnen als eine Kreislaufbewegung, bei welcher Anfang, Mitte und Ende eigentlich nicht anders gebraucht werden können, als wenn man sie zusammen gebraucht. Wie beim Kreise, wenn er fertig gezogen ist, von jedem Punkte gesagt werden muß, da fängt er an, und - wenn man herum- gegangen ist - da hört er wieder auf - aber von jedem Punkte kann man das sagen -, so ist es bei diesem Erleben. Man hat nicht das Gefühl, daß man eine Zeit durchlebt, sondern eine Kreislaufbewegung",
      "durchmacht, einen Zyklus beschreibt - und verliert bei diesem Erleben vollständig das Gefühl für die Zeit, die man gewöhnlich im Sinnensein hat. Man hat nur das Gefühl: Du bist in der Welt, und die Welt hat zu ihrem Grundcharakter das Zyklische, das Kreishafte. Und ein Wesen, welches nie die Erde betreten haben würde, welches",
      "nie im Sinnensein gewesen wäre, sondern nur in dieser Welt immer gelebt hätte, würde nie auf den Gedanken kommen, die Welt habe einmal einen Anfang genommen und könne gegen ein Ende zulaufen, sondern es würde sich ihm immer nur eine in sich geschlossene Kreiswelt darstellen. Ein solches Wesen hätte gar keine Veranlassung zu sagen, es erstrebe die Ewigkeit, aus dem einfachen Grunde, weil überall alles ewig ist, weil nirgends etwas ist, über das man hin- aussehen könnte als über etwas Zeitliches in etwas Ewiges hinein.",
      "Dieses Gefühl der Zeitlosigkeit, des Zyklischen tritt also auf der entsprechenden Stufe des Hellsehens oder beim bewußten Durchleben des Schlaflebens auf. Aber dies vermischt sich mit einer gewissen Sehnsucht. Die Sehnsucht tritt dadurch hervor, daß man nie bei diesem Erleben in der höheren Welt eigentlich in Ruhe ist, man fühlt sich überall in der Kreisbewegung drinnen, fühlt sich immer bewegt, macht nie irgendwo halt. Und die Sehnsucht, die man hat, ist, irgendwo haltmachen zu können, irgendwo in die Zeit hinein- treten zu können! Genau, möchte ich sagen, das Umgekehrte von dem, was man im Sinnensein erlebt. In diesem fühlt man sich immer in der Zeit und hat die Sehnsucht nach der Ewigkeit. In der Welt, von der ich gesprochen habe, fühlt man in der Ewigkeit und hat die einzige Sehnsucht: Wenn doch irgendwo die Welt stille stände und irgendwo in das Zeitensein einrückte! Das ist das, was man als ein Grundgefühl kennenlernt: die immerwährende Beweglichkeit im All und die Sehnsucht nach der Zeit, das Erleben in dem immerwährenden, sich selber für immer garantierenden Werden - und die Sehnsucht: Ach, könnte man doch irgendwo auch einmal irgendwie vergehen!",
      "Ja, man hat volle Berechtigung, wenn man die Begriffe des Sinnenseins anwendet, solche Dinge paradox zu finden. Aber man darf sich an diesen Paradoxien nicht stoßen, denn das würde bedeuten,",
      "daß man sich nicht einlassen will auf die reale Beschreibung der höheren Welten, bei deren Betreten man nicht nur alles übrige, sondern auch die gewöhnlichen Beschreibungen der Sinneswelt aufgeben muß, wenn man diese höheren Welten in ihrer Wirklichkeit beschreiben will.",
      "Dieses Gefühl, das ich Ihnen geschildert habe, das Sie bitte betrachten wollen als ein Erlebnis, das man in sich selber und an sich selber hat - und es ist wichtig, daß man dieses Erleben in sich selber und an sich selber hat, denn das gehört zu den ersten Schritten auf dem Wege der Initiation -, kann in zweifacher Weise auftreten. Einmal kann dieses Gefühl so auftreten, daß man das, was man erlebt, so ausdrücken müßte: Ich habe eine Sehnsucht nach der Vergänglichkeit, nach dem Sein, zusammengedrängt in der Zeit, ich möchte nicht ausgegossen sein in die Ewigkeit. Dieses Gefühl, bitte das wohl zu beachten, hat man in der geistigen Welt, also nicht etwa im Sinnensein, sondern es braucht, wenn man wieder zurückkommt in die Sinneswelt, gar nicht dazusein, es ist nur da in der geistigen Welt. So kann man sagen, man habe in der geistigen Welt das Gefühl: du möchtest so recht hinein dich erleben in die Zeitlichkeit, möchtest so recht konzentriert sein in Selbständigkeit an einem Punkt des Weltenseins, und möchtest das so vollenden, daß du sagen kannst: Ach, was ist an aller Ewigkeit gelegen, die sich sonst im Universum ausdehnt, ich will mir dieses eine Selbständige sichern, da drinnen will ich sein!",
      "Denken Sie sich diesen Wunsch, dieses Gefühl in der Welt erlebt. Es ist nur noch nicht so genau ausgedrückt, sondern wir müssen zu einer anderen Charakteristik noch kommen, müssen es noch mit etwas anderem verbinden, wenn der Ausdruck genau sein soll. Wenn man dieses Gefühl an das menschliche Sinnensein heranbringen will, so charakterisiert man mit Anklängen an die Sinneswelt. Aber ich habe ja gesagt, dort oben ist alles Wesenheit, und man kann gar nicht anders davon sprechen. Man hat aber noch nicht ganz recht, wenn man sagt, daß alles Wesenheit wäre. Wenn man in der SinnesweIt von einem Wunsche ergriffen ist, so kann man sich sagen: Ach, könntest du dir doch diesen einen Punkt sichern. Wenn man von",
      "den höheren Welten in Wirklichkeit spricht, muß man sagen, man fühlt sich von einem Wesen hingedrängt, und das wirkt in einem und bewirkt in einem, daß man sich so ausdrückt, daß man hinein will in diesen Punkt. Wenn man einen solchen Wunsch verstanden hat - sich diesen Punkt zu sichern, konzentriert zu sein in der Zeitlichkeit - als einen Impuls, der von einem Wesen gegeben wird in der Welt - nur so kann es sein -, so hat man den Einfluß des luziferischen Wesens in der Welt erfaßt.",
      "Jetzt sind wir bei dem Begriff, wo man sagen kann: Wie kann man davon sprechen, man stünde einem luziferischen Wesen gegenüber? Wenn ein solcher Einfluß in den Welten der höheren Hierarchien auftritt: Hingezogensein von der Ewigkeit zu einem selbständigen Konzentriertsein in der Welt, so erlebt man das luziferische Wirken.",
      "Und wenn man es erlebt hat, dann weiß man, wie die Kräfte, die luziferisch sind, beschrieben werden können. Dann werden sie so beschrieben, wie ich es charakterisiert habe, und dann erhält man erst die Möglichkeit, real zu sprechen über einen Gegensatz, der seinen Nachklang auch hineinschickt in unsere Sinneswelt.",
      "Es ist der Gegensatz, der sich einfach dadurch ergibt, daß man jetzt weiß, im Si`nnensein ist es ganz natürlich, daß man in die Zeitlichkeit hineinversetzt ist. Für die geistige Welt, die, bildlich gesprochen, oberhalb der astralen Welt liegt, ist es ganz natürlich, daß man dort nichts mehr von Zeitlichkeit, sondern nur noch Ewigkeit verspürt.",
      "Und der Nachklang der devachanischen Erfahrung, der als Sehnsucht im Zeitlichen auftritt, ist die Sehnsucht nach der Ewigkeit. Das Zusammenspielen der wirklich erlebten Zeit - der wirklich erlebten Zeit im Augenblick - mit der Sehnsucht nach der Ewigkeit kommt davon her, weil unsere Sinneswelt die devachanische Welt durchdringt, die Welt des Geisterlandes.",
      "Und wie hinter unserer Sinneswelt das Geisterland selber für das gewöhnliche sinnliche Wahrnehmen verborgen ist, so ist hinter dem Augenblicke das Ewige verborgen. Und wie man nirgends sagen kann, da hört die Sinneswelt auf, und da beginnt die geistige Welt, sondern wie überall die geistige Welt das Sinnensein durchdringt, so durchdringt jeden Augenblick ihrer Qualität nach die Ewigkeit.",
      "Man erlebt nicht die",
      "Ewigkeit, wenn man hinauskommt aus der Zeit, sondern wenn man im Augenblick selber die Ewigkeit hellseherisch erleben kann. Sie ist im Augenblick selber garantiert, denn sie steckt in jedem Augenblick drinnen.",
      "Wenn Sie irgendwo die Welt nehmen, so können Sie nicht sagen, wenn Sie vom Standpunkt des hellseherischen Bewußtseins aus sprechen, insofern irgendwo in der Welt ein Wesen ist, dieses Wesen sei ein zeitliches, oder dieses Wesen sei ein ewiges. Für das geistige Bewußtsein hat der Ausdruck keinen Sinn: Hier ist ein Wesen, das zeitlich ist -, oder: Hier ist ein Wesen, das ewig ist - sondern etwas ganz anderes hat einen Sinn.",
      "Was dem Dasein zugrunde liegt - Augenblick und Ewigkeit -, ist immer und überall. Die Frage kann nicht anders gestellt sein als: Wie kommt es, daß die Ewigkeit einmal als Augenblick erscheint, daß das Ewige einmal zeitlich erscheint, und daß ein Wesen in der Welt die Gestalt des Zeitlichen annimmt?",
      "Das kommt von nichts anderem als davon her, daß unser Sinnensein überall, wo es auftritt, von luziferischen Wesenheiten zugleich durchsetzt ist. Und soweit das luziferische Wesen hereinspielt, soweit wird die Ewigkeit zur Zeitlichkeit gemacht.",
      "Sie müssen also sagen: Ein Wesen, das irgendwo in der Zeit auftritt, ist soviel ein ewiges Wesen, als es sich zu befreien vermag von dem luziferischen Dasein, und es ist ebensoviel ein zeitliches Wesen, als es unterliegt dem luziferis`chen Dasein. Man hört auf, wenn man geistig zu charakterisieren beginnt, die Ausdrücke des gewöhnlichen Lebens zu gebrauchen.",
      "Wenn man im gewöhnlichen Leben anwendet, was die Religionen lehren und was die Theosophie lehrt, so würde man sagen: Der Mensch hat seinen Leib als äußere Hülle, und er hat in sich sein Seelen- und Geistessein; der Leib ist vergänglich, das Seelen- und Geistessein ist ewig und unsterblich. So ist es richtig gesprochen, insofern man in der Sinnenwelt drinnen ist und dort die Dinge charakterisieren will.",
      "Es ist nicht mehr richtig gesprochen, wenn man den Gesichtspunkt der geistigen Welt anwenden will, sondern da muß man sagen: Der Mensch ist ein Wesen, zu dessen ganzer Natur fortschreitende göttliche Wesen und luziferische Wesen mitwirken müssen. Und insofern fortschreitende göttliche Wesen in ihm sind, ringt sich ein Teil",
      "seines Wesens so los von allem, was daran luziferisch ist, daß es der Ewigkeit teilhaftig ist. Insofern die göttlichen Wesen wirken, hat der Mensch Anteil an dem Ewigen; insofern die luziferische Welt in ihm wirkt, gliedert sich an die Menschenwesenheit alles an, was mit Vergänglichkeit und Zeitlichkeit verbunden ist.",
      "Also als ein Zusammenwirken verschiedenartiger Wesenheiten erscheinen Ewigkeit und Zeitlichkeit. In den höheren Welten hat es auch keinen Sinn mehr, von solchen abstrakten Gegensätzen zu sprechen wie Ewigkeit und Zeitlichkeit; die hören auf, in den höheren Welten einen Sinn zu haben. Da muß man von Wesenheiten sprechen. Deshalb spricht man von fortschreitenden göttlichen Wesenheiten und von luziferischen Wesenheiten. Weil die in den höheren Welten da sind, spiegelt sich ihr Verhältnis zueinander als der Gegensatz von Ewigkeit und Zeitlichkeit.",
      "Ich habe gesagt, es ist gut, wenn der Mensch bei seinem Auf- rücken in die Welt, die hier gemeint ist, zunächst mehr moralische Erinnerungen fühlt und nicht so sehr seine äußere physische Gestalt. Der Mensch soll nach und nach erst - mit den fortgesetzten Übungen für die ersten Schritte der Initiation - auch so hellseherisch werden, daß das Erinnerungsbild an die äußere physische Gestalt auftritt. Mit diesem Auftreten des Erinnerungsbildes der eigenen physischen Gestalt ist aber noch etwas anderes verbunden: daß eigentlich erst von da ab der Mensch - und so ist es gut - nicht nur im allgemeinen sein Seelenleben als Erinnerung fühlt, nicht nur im allgemeinen seine guten und schlechten Taten, seine moralischen und dummen Taten, sondern sein ganzes Ich fühlt. Sein ganzes Selbst fühlt er in dem Moment als Erinnerung, wo er auf seinen Leib als Form zurückschauen kann. Da fühlt er dann sein Wesen wie gespalten. Er schaut auf einen Teil, den er beim Hüter der Schwelle abgelegt hat, und schaut auf das, was er sein Ich nennt in der Sinnes- weIt. Jetzt ist man, wenn man auf sein Ich zurückblickt, auch in bezug auf sein Ich gespalten und sagt sich mit aller Ruhe: Was du dein Ich früher genannt hast, daran erinnerst du dich jetzt nur; jetzt lebst du in einem übergeordneten Ich, und das verhält sich so zu dem früheren Ich, wie du dich als Denker verhältst in bezug auf die Erinnerungen",
      "zum Leben im Sinnensein. Auf das also, was der Mensch eigentlich ist als Erdenmensch, auf seinen Ich-Menschen sieht man erst auf dieser Stufe herunter. Man ist aber da zugleich entrückt in eine noch höhere Welt, die man das höhere Geisterland oder - wenn man will - die höhere Mentalwelt nennen kann, eine etwas von den anderen verschiedene. Da ist man darinnen, wenn man das Ich zwiegespalten fühlt und das gewöhnliche Ich nur noch als Erinnerung fühlt. Da hat man erst die Möglichkeit, in richtiger Weise den Menschen auf der Erde zu beurteilen. Wenn man von dort zurückschaut, fängt man an zu wissen, was der Mensch seiner tiefsten Wesenheit nach ist. Da bekommt man auch die Möglichkeit, ein erlebtes Urteil zu gewinnen über den Verlauf der Geschichte. Da gliedert sich einem die erlebte Menschheitsentwickelung in den Fortgang der Seelen als Ich-Wesen, da ragen heraus aus dem gewöhnlichen Fortgange die Wesen, welche die führenden im Fortgang der Menschheit sind. Da ist es so, wie ich es im zweiten Vortrage charakterisiert habe, daß man wirklich die Impulse erlebt, die fortwährend in die Evolution der Menschheit hineinfließen durch die Initiierten, die überall aus dem Sinnensein in das Geistessein zu gehen haben, damit sie ihre Impulse geben können. Mit dem Punkt, wo man den Menschen als Ich-Wesen erlebt, erlebt man auch erst die wahre Einsicht in das Mensch`enwesen als solches. Nur eine Ausnahme gibt es dabei.",
      "Fassen wir das schon Gesagte zusammen. Wenn der Mensch die ersten Schritte zur Initiation durchmacht, kann er sich hellseherisch zur Welt des nie`deren Geisterlandes erheben; er erlebt die Vorstellungen des Seelischen, des Moralischen, des Intellektuellen, sieht hinunter auf das, was in den Seelen vorgeht, auch wenn sie sich nicht zusammenfassen würden als Ich-Wesen. Das Zusammenfassen der Wesen als Ich-Wesen erlebt man im höheren Geisterlande und damit auch alle Blüten des Geisteslebens in den Initiierten - mit einer einzigen Ausnahme, die richtig und gut ist, wenn sie als Ausnahme eintreten kann und dadurch die allgemeine Regel durchbrochen wird: Vom niederen Geisterlande aus sieht man die ganze Wesenheit des Christus Jesus! So daß man zurückblickend, rein menschlich sehend",
      "und die Erinnerungsvorstellungen festhaltend, die Erinnerung hat an den Christus Jesus, an alle Ereignisse, die mit ihm vorgegangen sind, wenn die andere Bedingung erfüllt ist, von der ich im zweiten Vortrage gesprochen habe. Die Wahrheit über alle anderen Initiierten erlebt man erst in dem höheren Geisterlande.",
      "Da haben wir einen Unterschied von einer ungeheuren Tragweite. Wenn der Mensch hinaufkommt in die geistige Welt, dann sieht er - zurückblickend - auf das Irdische, das er zunächst seelisch sieht, wenn er nicht so die Erinnerung hat, daß er zurückblickend auf das Erdensein sich erinnert an die physisch herumgehenden Menschen in Gestalt und Form. Das soll er erst erleben, wenn er den charakterisierten höheren Punkt erlebt. Nur den Christus Jesus darf und soll er bei den ersten charakterisierten Schritten auf dem Wege zur Initiation sehen! Und er kann ihn sehen, wenn er hinaufrückt und sich überall umgeben sieht von nur Seelischem, das zunächst nicht durchtränkt ist von Ich-Wesenheit, da drinnen aber wie eine Art von Mittelpunkt die Christus-Wesenheit, vollbringend das Mysterium von Golgatha, mit dem Ich durchdrungen.",
      "Was ich Ihnen jetzt gesagt habe, kann natürlich nicht irgendwie aufgefaßt werden als ein Ausfluß einer der bestehenden christlich konfessionellen Weltanschauungen, denn ich glaube nicht, daß es sich irgendwo charakterisiert fände. Aber wohl findet sich in einer gewissen Weise, weil das Christentum eben durchaus nicht in seinem bisherigen Verlauf das erreicht hat, was es erreichen muß, man möchte sagen, das Gegenteil von dem Charakterisierten, aber auf eine sehr eigentümliche Weise, auf die man erst kommt, wenn man die Dinge okkult genau einsieht. Vielleicht werden doch einige von Ihnen wissen, daß es unter den offiziellen Vertretern des Christentums viele gibt, die eine heillose Angst vor allem haben, was man Okkultismus nennt, und alles dieses als ein reines Teufelszeug betrachten, das dem Menschen nur Verderben bringen kann. Warum ist das so? Warum erlebt man es immer wieder und wieder, wenn man mit den Vertretern irgendwelcher Priesterschaft spricht und auf Okkultismus oder Theosophie die Rede kommt, daß sie das abweisen? Und wenn man einem solchen Herrn sagt: Sehen Sie doch",
      "einmal ein, daß die christlichen Heiligen immer die höheren Welten erlebt haben und daß dies in den betreffenden Biographien dargestellt ist -, dann bekommt man zur Antwort: Ja, das ist zwar so, aber das darf nicht angestrebt werden. Man darf zwar das Leben der Heiligen lesen, aber wenn man sich nicht der Gefahr der Teufelei aussetzen will, darf man es nicht nachleben. - Woher kommt das?",
      "Wenn Sie das zusammennehmen, was ich gesagt habe, werden Sie es begreifen: Es ist eine Art Angstgefühl, das sich darin ausdrückt, ein recht starkes Angstgefühl. Die Leute wissen nicht, woher es kommt, aber der Okkultist kann es wissen.",
      "Der Mensch kann - wie ich Ihnen im zweiten Vortrag gesagt habe - in den höheren Welten diese Erinnerung an den Christus nur haben, wenn er ihn richtig hier in der physisch.sinnlichen Welt auf der Erde erfaßt hat. Und richtig ist es, schon in der allernächsten Welt ihn zu haben, in die man eintritt, wo man noch das übrige Menschliche als Erinnerungsvorstellung hat.",
      "Es ist auf der einen Seite nötig, daß man die Erinnerungsvorstellung hat, auf der anderen Seite kann man sie nur haben, wenn man sich hier schon damit durchdrungen hat. Deshalb kommt es vor, daß die, welche etwas mit dem Okkultismus bekannt geworden sind, aber gewisse wichtige und eklatante Tatsachen nicht durchdrungen haben, es für einerlei halten, ob der Mensch in unseren jetzigen Zeiten, wenn er in die höheren Welten hinaufdringt, mit der Christus-Vorstellung bekannt geworden ist oder nicht.",
      "Denn sie glauben, was dort oben ist, hinge doch nicht so stark von dem ab, was man unten erlebt hat, obwohl sie es sonst immer betonen. Es hängt aber gerade die Art, zu dem Christus sich in den höheren Welten zu stellen, davon ab, wie man sich zu ihm verhalten hat in der physischen Welt.",
      "Wenn man es nicht versucht, die richtige Vorstellung von ihm in der physischen Welt hervorzurufen, so kommt man in einer gewissen Weise unreif hinauf und kann ihn dort nicht finden, trotzdem man ihn finden sollte; so daß einem, wenn man nicht auf diese ganz bedeutsame, eklatante Sache bedacht ist, in der Tat durch das Hinaufrücken in die höheren Welten die Christus-Vorstellung vollständig verlorengehen kann. Wenn es also jemand verschmähen würde, schon innerhalb des Sinnenseins ein",
      "Verhältnis zu dem Christus zu gewinnen, so könnte er ein großer Okkultist werden und nichts von dem Christus durch seine Wahrnehmungen in den höheren Welten wissen, denn er würde ihn dort nicht finden und würde nichts lernen können von ihm. Seine Vorstellungen über ihn würden immer mangelhaft sein.",
      "Das ist das Bedeutsame. Ich sage Ihnen damit nicht irgend etwas, was ich Ihnen aus einer subjektiven Meinung heraus sage, sondern was ein gemeinsames objektives Resultat derer ist, die darüber Forschungen angestellt haben.",
      "Bei den Okkultisten kann es objektiv beschrieben werden, daß es so ist; bei dem, der keine Nötigung dazu empfindet, Okkultist zu werden, sondern der nur ein braver Vertreter seines Religionsbekenntnisses ist, äußert es sich mit all jener Unbewußtheit, die ich jetzt als Angstzustand geschildert habe. Und wenn jemand dann den Weg in die höheren Welten unternehmen will, ist das ein großes Teufelszeug, und solche Menschen meinen, der könnte doch vielleicht nicht das richtige Verhältnis zum Christus gewonnen ha- ben, also soll er nur ja nicht aus der gewöhnlichen Welt hinausgeführt werden.",
      "Es ist also diese Angst in einer gewissen Weise eine begründete. Diese Menschen wissen nicht, wie es zum Christus hin- geht> und wenn sie dann in die höheren Welten hineinkommen, geht ihnen der Christus verloren.",
      "Es ist das etwas, was man als eine Art Angst bei einer gewissen Priesterschaft verstehen kann, dem man aber in keiner Weise entgegenkommen kann. Ich bitte diesen kleinen Exkurs, der kulturhistorisch interessant ist, weil man dadurch vieles versteht von dem, was sich im Leben abspielt, als bedeutend zu betrachten und sich nachdenkend im Leben damit zu beschäftigen.",
      "Von zwei verschiedenen Gesichtspunkten aus habe ich Ihnen sozusagen Ausläufer zu dem Christus gezeigt und habe versucht, ein paar Lichter auf die Christus-Wesenheit zu werfen. Alles, was ich gesagt habe, kann auch ohne diese zwei Ausläufer gesagt werden und ist dann auch gültig und verständlich. Aber es ist notwendig, sich objektiv den Tatsachen entgegenzustellen und sie ganz unbeeinflußt von den konfessionellen Richtungen als kosmische Tatsachen ins Auge zu fassen.",
      "Damit haben wir versucht, ein gewisses Licht zu werfen auf die Begriffe Zeitlichkeit, Vergänglichkeit, Augenblick und Ewigkeit auf der einen Seite, Sterblichkeit und Unsterblichkeit auf der andern Seite. Und es haben sich zusammengebunden die Begriffe Vergänglichkeit und Zeitlichkeit mit dem luziferischen Prinzip.",
      "Mit dem Christus - Prinzip werden sich uns Begriffe wie Ewigkeit, Unsterblichkeit zusammenfügen. Es könnte jemand glauben, daß dies im allermindesten wenigstens irgendeine Geringwertung des luziferischen Prinzips sein könnte, eine Abweisung unter allen Umständen, indem bei dem Luziferischen auf das Zeitliche, Vergänglichere, auf das Konzentriertsein auf einen Punkt hingewiesen wird.",
      "Für heute möchte ich das eine nur sagen, daß man nicht unter allen Umständen recht hat> den Lichtträger als etwas zu betrachten, vor dem man sich zu fürchten hätte, daß man Luzifer abzuweisen hat als etwas, von dem man unter allen Umständen loskommen soll. Wenn man das tut, bedenkt man nicht, daß der wahre Okkultismus lehrt, daß es ein ähnliches Gefühl gibt hier in der Sinneswelt wie in der über- sinnlichen Welt.",
      "Im Sinnensein fühlt der Mensch: Ich lebe im Zeitlichen und sehne mich nach der Ewigkeit; ich lebe im Augenblick und begehre die Ewigkeit. Im Geistigen gibt es das Gefühl: Ich lebe im Ewigen und sehne mich nach dem Augenblick.",
      "Und verfolgen Sie jetzt die Mitteilungen aus der`Akasha-Chronik. Ist nicht in der alten Zeit, die wir oft als die lemurische bezeichnet haben, das Mensch-Werden eine Art Übergang aus einem solchen Zustande, wie wir ihn im Schlafe haben, in die Zustände des Wachens?",
      "Verfolgen Sie genau, was in der lemurischen Zeit geschehen ist, und Sie können sich sagen: Indem der Mensch einen Übergang durchmachte aus einem geistigen Schlafzustand in die wachen Erdenzustände, ging die ganze Evolution damals vom Geistigen in das Sinnliche über. Da ist ein Übergang, und unser jetziges Sinnensein bekommt erst einen Sinn seit der lemurischen Zeit.",
      "Und überlegen Sie sich, ob es so unnatürlich ist, daß der Mensch, als er aus der höheren Welt herausschlüpfte, um von dem Luziferischen ergriffen zu sein, etwas mitnahm wie eine Sehnsucht nach dem Ewigen! Dann haben Sie in bezug auf das Luziferische eine Art Erinnerung an einen vorirdischen",
      "Zustand, eine Erinnerung an das, was der Mensch gehabt hat, bevor er in das Sinnensein kam, und was sich nicht hätte erhalten sollen: die Sehnsucht nach dem Augenblick, nach dem Zeitlichen. Inwiefern diese an der Gesamtevolution des Menschen beteiligt ist, davon morgen weiter."
    ],
    "sentences": [
      [
        "Gestern versuchte ich mit Worten, die nun einmal für solche Dinge möglich sind, zu charakterisieren den Unterschied des Herausrükkens aus dem physischen Leibe zu dem Erleben, dem Erfühlen im ätherischen oder elementarischen Leibe und im astralischen Leibe.",
        "Und ich bemerkte, daß das Erleben so verläuft, daß das Sich-Hineinleben in den elementarischen oder ätherischen Leib sich ausnimmt wie eine Art Hinausfließen in die Weiten der Welt, wobei man das Bewußtsein durchaus behält, daß man von einem Mittelpunkte, nämlich von seiner eigenen Leiblichkeit, nach allen Seiten ins Unbegrenzte ausströmt."
      ],
      [
        "Das Erleben aber im astralischen Leibe stellt sich so dar, daß es sich wie ein Aus.sich.Herausspringen und Hinein- springen in den astralischen Leib ausnimmt, so daß man sich wirklich jetzt erst erlebend fÜhlt so außerhalb seines physischen Leibes, daß man alles, was man war im physischen Leibe, was man «sich selbst» nennt im physischen Leibe, wie etwas empfindet, was man außer sich hat, wie ein Außer-sich-Seiendes.",
        "In einem anderen ist man drinnen."
      ],
      [
        "Ich habe schon gestern darauf hingedeutet, daß die Welt, der man sich dann gegenüber befindet, die Bezeichnung des Geisterlandes tragen muß in Gemäßheit zum Beispiel meiner «Theosophie».",
        "Man könnte auch sagen, es sei der niedere Mentalplan, denn es wäre unrichtig zu glauben, daß, wenn man in richtiger, selbstloser Weise dazu gelangt, im astralischen Leibe zu leben, man dann in dem wäre, was man gewöhnlich die astralische Welt nennt, indem man mit diesem Worte etwas Niedriges verbindet."
      ],
      [
        "Nun ist der Unterschied gegenüber dem Leben, Beobachten und Erfahren im Sinnensein und dem Erfahren in dem astralischen Leibe gegenüber dem Geisterlande durchaus verschieden, ganz gewaltig verschieden.",
        "Denn im Sinnensein stehen wir gegenüber Stoffen, Kräften, Dingen, Vorgängen und so weiter.",
        "Wir stehen auch Wesen gegenüber im Sinnensein, stehen ja vor allen Dingen außer den Wesen der anderen Naturreiche - sofern wir berechtigt sind, sie so zu"
      ],
      [
        "nennen - unseren eigenen Mitmenschen gegenüber.",
        "Wir stehen im Sinnensein diesen anderen Wesenheiten so gegenüber, daß wir wissen, diese Wesenheiten nehmen in sich auf die Stoffe und Kräfte der Welt eben des Sinnenseins, durchdringen sich damit und leben dadurch mit dem Leben, welches verläuft in den Naturgesetzen und durch die Naturkräfte der äußeren Welt.",
        "Kurz, wir müssen unter"
      ],
      [
        "scheiden im Sinnensein zwischen dem Naturverlauf und den Wesenheiten, die sich innerhalb dieses Naturverlaufes ausleben und sich mit den Stoffen und Kräften desselben durchdringen.",
        "Wir haben den Naturverlauf und die Wesenheiten."
      ],
      [
        "Nehmen wir im astralischen Leibe in der geistigen Welt wahr, so können wir diesen Unterschied auch nicht mehr so machen.",
        "Wir stehen eigentlich in dieser geistigen Welt nur Wesenheiten gegenüber, und diesen Wesenheiten steht nicht das entgegen, was man Naturverlauf nennen könnte."
      ],
      [
        "Alles ist Wesen, was einem begegnet, wozu man auf die Weise, wie es gestern angedeutet worden ist, geführt wird.",
        "Überall wo etwas ist, ist Wesen> und man kann nicht sagen wie im Sinnensein: Dort ist ein Tier und dort sind äußere Stoffe, die von ihm gegessen werden. - Diese Zweiheit gibt es dort nicht, sondern was ist, ist Wesen."
      ],
      [
        "Und wie man sich zu diesen Wesen zu stellen hat, habe ich auch schon gesagt: daß es hauptsächlich die Welt der Hierarchien ist, die wir von anderen Gesichtspunkten aus öfter charakterisiert haben.",
        "In ihrer Stufenfolge lernt man die Welt der Hierarchien kennen, von denjenigen Wesenheiten an, die man zunächst kennenlernt als die Angeloi und Archangeloi, Engel und Erzengel, wie sie in unserer Terminologie genannt werden, bis zu den Wesenheiten, die einem fast zu entschwinden scheinen, so undeutlich werden sie, den Cherubim und Seraphim."
      ],
      [
        "Aber es ist eines möglich, wenn man sich in diesen Welten befindet: eine Beziehung zu diesen Wesenheiten zu gewinnen.",
        "Was man im Sinnensein ist, das muß man vorher zurücklassen im Sinne der gestrigen Auseinandersetzungen; aber wie ich Ihnen gesagt habe, man behält es doch zurück in der Erinnerung."
      ],
      [
        "Man trägt die Erinnerung an das Abgelebte in diese Welten hinein, und wie man im Sinnensein auf die Erinnerungen zurücksieht, so blickt man auf das, was man im Sinnensein"
      ],
      [
        "ist, von der höheren Welt aus zurück, man hat es in der Erinnerungsvorstellung."
      ],
      [
        "Nun ist gut, wenn man die ersten Schritte der Initiation in die höheren Welten hinaufrückt, daß man unterscheiden lernt zwischen einem ersten Schritt und einem folgenden Schritt.",
        "Es ist nicht gut, wenn man diese Unterscheidung nicht machen lernt."
      ],
      [
        "Sie besteht im wesentlichen darin, daß man sich am besten orientieren lernt in den höheren Welten, wenn man zu den ersten Erinnerungsvorstellungen, die man da hinüberträgt und die einen an das Sinnensein erinnern, nicht die Vorstellung des eigenen physischen Leibes und seiner Gestalt hat.",
        "Es ist eben eine Erfahrung, daß es besser ist."
      ],
      [
        "Und jeder, der Rat geben soll für diejenigen Übungen, die gemacht werden sollen, um die ersten Schritte der Initiation herbeizuführen, sieht darauf, daß zu den ersten Erinnerungsvorstellungen nach Überschreiten der Grenze, nach dem Vorbeigelangen an dem Hüter der Schwelle nicht eine Anschauung der physischen Leibesform gehört, sondern daß die ersten Erinnerungsvorstellungen im wesentlichen solche sind, die man zusammenfassen könnte mit der Bezeichnung: moralisch-intellektuelle Empfindung seiner selbst.",
        "Das sollte man zuerst empfinden, wie man sich moralisch zu taxieren hat, sollte empfinden, welche moralischen oder unmoralischen Neigungen man hat, welches Wahrheitsgefühl oder Oberflächlichkeitsgefühl man hat, empfinden also, wie man sich zu bewerten hat als Seelenmensch."
      ],
      [
        "Das ist es, was als erste Empfindung auftritt.",
        "Es tritt nicht so auf> daß man den Ausdruck dafür am besten wählt mit Worten, die dem Sinnensein entnommen sind, denn es ist das Erleben viel intensiver mit uns verbunden, als im Sinnensein etwas Ähnliches ist, wenn man eben hineintritt in die geistige Welt."
      ],
      [
        "Nachdem man etwas getan hat, womit man moralisch nicht einverstanden sein kann, erfüllt sich das ganze Innensein, das man da hat, wie mit einer Bitternis, wie mit etwas, was sich in die Welt, in welche man sich da hineingelebt hat, ausbreitet, was diese Welt erfüllt mit einem Aroma von Bitternis, wobei ich nicht zu denken bitte an ein sinnliches Aroma, aber man fühlt herankommen ein Durchdrungensein mit einem Aroma von Bitternis.",
        "Was man moralisch rechtfertigen kann, ist mit"
      ],
      [
        "einem sympathischen Aroma erfüllt.",
        "Man könnte auch sagen: dunkel, finster ist die Sphäre, in die man hineinkommt, wenn man mit etwas nicht einverstanden war, licht und hell ist die Sphäre der Welt, in die man hineinkommt, wenn man mit sich zufrieden sein kann.",
        "So also sollen sein, damit man sich gut orientieren kann, die Bewertungen moralischer oder intellektueller Art, die man sich angedeihen lassen kann und die einem wie der Luftkreis die Welt erfüllen, in die man eintritt.",
        "So ist es am besten, wenn man eben seelisch diese Welt empfindet, und wenn erst, nachdem man sich vertraut und bekannt gemacht hat mit diesem seelischen Erfühlen - sagen wir des geistigen Raumes -, die Erinnerung auftritt, die ganz die Form und Gestalt haben kann auch dessen, was physische Leibesform im Sinnensein ist, so daß sich einem diese gleichsam hineinstellt in die neu gewonnene moralische Atmosphäre."
      ],
      [
        "Was ich Ihnen hier beschrieben habe, kann aber auch nicht nur zum Beispiel mitten aus dem Tagesleben heraus auftreten, daß es so kommt wie ein Eintreten in die geistige Welt, wenn man die entsprechenden Schritte zur Initiation gemacht hat, sondern es kann auch noch anders auftreten.",
        "Ob es in der einen oder anderen Weise auftritt, das hängt im Grunde genommen von dem Karma des einzelnen Menschen ab, hängt von der ganzen Art seiner Veranlagung ab.",
        "Man kann nicht sagen, daß die eine Art des Auftretens besser oder weniger gut wäre als die andere; es kann das eine und das andere vorkommen.",
        "Es kann mitten aus dem Tagesleben heraus der Mensch sich wie hineingezogen fühlen in die geistige Welt, aber es kann auch so auftreten, daß er eine andere Art des Erlebens gegenüber dem Schlafe bekommt.",
        "Das gewöhnliche Erleben gegenüber dem Schlafe ist ja so, daß der Mensch mit dem Eintreten in den Schlaf bewußtlos wird> daß er mit dem Aufwachen sein Bewußtsein wiedergewinnt, und daß er dann im Tagesleben - mit Ausnahme der Erinnerung an die Träume - nicht eine Erinnerung an das Schlaf- leben hat; er erlebt es bewußtlos.",
        "Es kann nun auch das für die ersten Schritte der Initiation auftreten> daß sich etwas anderes in dem Schlaileben ausbreitet, so daß zunächst eine andere Art des Einschlafens eintritt.",
        "Man erlebt eine andere Art des Bewußtseins mit dem"
      ],
      [
        "Eintritt in das Schlafleben.",
        "Die dauert, mehr oder weniger von bewußtlosen Zeiten unterbrochen, verschieden lange, je nachdem der Mensch weiter fortgeschritten ist, aber dann, wenn es gegen den Morgen zugeht, erlischt sie wieder.",
        "Und in der ersten Zeit nach dem Einschlafen tritt das ein, was man nennen kann eine Erinnerung an sein moralisches Verhalten, an seine Seelenqualitäten.",
        "Diese Erinnerung ist besonders stark nach dem Einschlafen und nimmt immer mehr und mehr ab, je weiter es dem Aufwachen zugeht."
      ],
      [
        "Es ist also> was da als Folge der Übungen zu den ersten Schritten der Initiation eintreten kann, ein Aufhellen, ein Durchhellen des Schlafbewußtseins, das sonst bewußtlos ist, mit Bewußtheit.",
        "Da gelangt man dann auch in die Welten der höheren Hierarchien hinein, fühlt sich ihnen angehörend.",
        "Aber es muß jetzt dieses Drinnenleben in der Welt, wo alles Wesenheit ist, gegenüber der gewöhnlichen Welt des Sinnenseins etwa in folgender Weise charakterisiert werden.",
        "In der Sinneswelt steht zum Beispiel ein Blumentopf vor dem Beobachter, der Beobachter steht davor, der Blumentopf ist draußen, außer ihm, er beobachtet ihn, indem er sich hinstellt und ihn ansieht.",
        "Mit einer solchen Beobachtung können wir das Erleben in der eben gemeinten höheren Welt gar nicht vergleichen.",
        "Sie würden sich eine ganz falsche Vorstellung machen, wenn Sie glaubten, daß man da drinnen herumgeht und die Wesenheiten auch so von außen ansieht, indem man sich vor sie hinstellt und sie beobachtet, wie man in der Sinneswelt etwa einen Blumenstrauß beobachtet.",
        "So ist es nicht.",
        "Sondern wenn man etwas vergleichen will im Sinnensein mit der Art> wie man zu der Welt der Hierarchien steht, so könnte es nur das Folgende sein.",
        "Es ist ja ein Vergleich, den ich brauche, aber man kann es sich dadurch klarmachen."
      ],
      [
        "Nehmen Sie an, Sie setzen sich irgendwo nieder und nehmen sich vor, nicht über dieses oder jenes mühevoll nachzudenken, sondern Sie wollen zunächst eigentlich über gar nichts Besonderes denken.",
        "Wie unhervorgerufen erhebe sich in Ihnen irgendein Gedanke, an den Sie zunächst nicht gedacht haben.",
        "Er nimmt Ihre Seele so in Anspruch, daß er sie erfüllt, so daß Sie zu dem Gefühl kommen können: Sie können diesen Gedanken gar nicht mehr unterscheiden von"
      ],
      [
        "sich selbst, Sie seien ganz eins mit dem Gedanken, der da aufgetaucht ist.",
        "Wenn Sie das Gefühl haben, der Gedanke lebt und zieht Ihre Seele mit sich, die ist mit ihm verbunderi~; und man könnte ebensogut sagen, der Gedanke ist in der Seele wie die Seele im Gedanken -, so ist das etwas Ähnliches im Sinnensein, wie man sich bekannt macht und benimmt mit den Wesenheiten der höheren Hierarchien.",
        "Die Worte «man ist neben ihnen, man ist außer ihnen» verlieren allen Sinn.",
        "Man ist mit ihnen, wie die Gedanken mit einem leben, aber nicht so, daß man sagen kann: die Gedanken leben in einem -, sondern, daß man sagen muß: der Gedanke denkt sich in einem. - Sie erleben sich, und man erlebt das Erleben derWesenheiten mit.",
        "Man ist drinnen in den Wesenheiten, man ist eins mit ihnen, so daß man sein ganzes Wesen in der Sphäre, in der die Wesenheiten leben, ausgegossen hat und man ihr Sein miterlebt, indem man ganz genau weiß, sie erleben sich darinnen."
      ],
      [
        "Es darf niemand glauben, daß er gleich nach den ersten Schritten auf dem Wege zur Initiation das Gefühl habe, er erlebe alles, was diese Wesenheiten erleben.",
        "Er braucht durchaus nicht mehr zu wissen als, er ist diesen Wesenheiten gegenüber, wie er im Sinnensein einem Menschen gegenüber ist, den er zum ersten Male sieht.",
        "Die Berechtigung des Ausdruckes «die Wesenheiten erleben sich in einem», bleibt bestehen, und doch braucht man auf die erste Bekanntschaft hin nicht mehr zu wissen, als man bei einem Menschen weiß, dem man zum ersten Male begegnet.",
        "In dieser Art also ist es ein Miterleben.",
        "Das wird immer intensiver und intensiver, und dadurch dringt man auch immer mehr und mehr in das Wesen dieser Wesenheiten ein."
      ],
      [
        "Nun aber verbindet sich mit dem, was so als ein geistiges Erleben geschildert worden ist, etwas anderes.",
        "Es verbindet sich damit ein gewisses Grundgefühl, das eigentlich wie eine Art realen Ergebnisses aller einzelnen Erlebnisse in der Seele sitzt.",
        "Es ist ein Grundgefühl, das ich Ihnen vielleicht an seinem Gegensatz darstellen kann.",
        "Genau entgegengesetzt diesem Grundgefühl, das man da erlebt, ist in der Sinneswelt das, was man erlebt, wenn man an irgendeinem Orte steht und sich ansieht, was ringsherum ist.",
        "Denken Sie sich, es stände"
      ],
      [
        "jemand in der Mitte des Saales und sähe alles, was hier ist.",
        "Da würde er sagen: hier ist der Mensch, dort jener Mensch und so weiter.",
        "Das wäre sein Verhältnis zur Umwelt.",
        "Das ist aber das Gegenteil der Grundstimmung, die man in der eben charakterisierten Welt hat.",
        "Da kann man nicht sagen: ich bin hier, dort ist dieses Wesen, dort jenes -, sondern da muß man sagen: ich bin dieses Wesen. -"
      ],
      [
        "Denn tatsächlich ist das eine wahre Empfindung.",
        "Was ich eben für alle einzelnen Wesenheiten gesagt habe, das empfindet man auch der Gesamtheit der Welt gegenüber.",
        "Man ist eigentlich alles selber.",
        "Dieses In-dem-Wesen-Sein breitet sich aus über die ganze Seelenstimmung.",
        "Diese Seelenstimmung ist in der Tat da, wenn bewußt die Zeit vom Einschlafen bis zum Aufwachen erlebt wird.",
        "Da kann man gar nicht beim bewußten Erleben sich anders fühlen als sich ausgegossen über alles, was man erlebt, sich in allem drinnen, bis ans Ende der Welt, die man überhaupt noch wahrnehmen kann."
      ],
      [
        "Ich habe einmal folgendes versucht, und ich möchte das als eine Episode hier einschalten, nicht um Ihnen etwas Besonderes zu sagen, sondern nur, um mich erklärlich zu machen.",
        "Es ist mir nämlich vor Jahren schon aufgefallen, daß gewisse mehr oder weniger über- sinnliche Zustände in den großen Weltdichtungen wie in einem Abglanz einem entgegentreten.",
        "Ich meine nämlich, wenn der Hellseher sich klarmacht, was er in gewissen übersinnlichen Erlebnissen als Grundstimmung der Seele hat, und dann die Weltliteratur durchgeht, so findet er bei den wirklich großen Dichtungen da oder dort solche Stimmungen, die gewisse Kapitel oder Abschnitte von diesen Dichtungen durchziehen.",
        "Das brauchen nicht etwa okkulte Erlebnisse der Dichter zu sein.",
        "Aber der Hellseher kann sich sagen, wenn er das, was er als Seelenstimmung erlebt hat, wie in einem Nachklange in der Sinneswelt wiedererleben will, so kann er zu diesen oder jenen großen Dichtungen gehen und findet dort etwas wie ein Schattenbild in der betreffenden Dichtung.",
        "Wenn der Hellseher mit seiner Erfahrung zum Beispiel Dante liest, so hat er zuweilen dieses Gefühl, daß ein solcher Abglanz, Schatten, die man eigentlich richtig in ihrem ursprünglichen Zustande nur hellseherisch erleben kann, in der Dichtung sind.",
        "Nun versuchte ich also einmal, gewisse"
      ],
      [
        "Zustände, die geschildert werden können, in den Dichtungen aufzusuchen, um eine Art Konkordanz zu bekommen zwischen Erlebnissen in den höheren Welten und dem, was wie im Abglanz in der physischen Welt vorhanden ist.",
        "Und zwar fragte ich mich: Könnte es nicht etwa sein, daß jene eigentümliche Seelenstimmung, welche über die Seele ausgegossen ist, wenn ein vollbewußtes Schlafen stattfindet - also ein Sein in den höheren Welten, wie ich es jetzt beschrieben habe, aber in der Stimmung erfaßt -, sich in der Weltliteratur auch im Nachklange in der Stimmung findet? - So direkt hat sich allerdings nichts ergeben."
      ],
      [
        "Aber bei einer anderen Stellung der Frage ergab sich etwas.",
        "Man kann sich nämlich auch fragen, weil die Erlebnisse es gestatten: Wie würde ein anderes Wesen, das nicht Mensch ist, also zum Beispiel irgendein anderes Wesen der höheren Hierarchien, diese Seelenstimmung empfinden, das Drinnensein in den höheren Welten?"
      ],
      [
        "Oder genauer gesprochen: Der Mensch fühlt sich in dieser Welt drinnen und schaut Wesen der anderen Hierarchien.",
        "Wie man nun in der Sinneswelt fragen kann: Was empfindet ein anderer Mensch gegenüber einer Sache, die man selbst empfindet? - so kann man auch gegenüber einem Wesen der höheren Hierarchien diese Frage aufwerfen und hat die Möglichkeit, sich eine Vorstellung zu bilden, was ein anderes Wesen erlebt."
      ],
      [
        "Da kann man sich dann gegenüber dem Leben in den höheren Welten, wie es beim wirklich bewußten Schlafe möglich sein würde, eine bestimmte Art von höherem Erleben vorstellen, als es beim Menschen selber der Fall ist, aber von solchem Erleben, das doch allen möglichen Anteil hat an der Menschenseele.",
        "Man kann also an ein Wesen denken, das in eine höhere Hierarchienreihe hineingehört, als es der Mensch auf der Erde ist, das aber doch auf höhere Art alles Menschliche noch empfinden kann."
      ],
      [
        "Wenn man die Frage so stellt, wenn man also nicht auf den gewöhnlichen Menschen reflektiert, sondern auf einen typischen Menschen, und sich die Stimmung vorstellt, so bekommt man die Möglichkeit, etwas in der Weltliteratur zu finden, von dem man sich immerhin den Begriff bilden kann: es ist ausgegossen eine solche Stimmung im Nachklange, von der man eigentlich nur eine richtige Vorstellung bekommt im ursprünglichen Zustande, wenn"
      ],
      [
        "man sich in die jetzt geschilderte, charakterisierte Welt hineinversetzt.",
        "Nun findet sich allerdings nichts innerhalb der europäischen Literatur, von dem man sagen könnte: Es ist die Seelenstimmung darin fühlbar von dem, was ausgegossen ist über eine Seele, die sich in allem fühlt in der charakterisierten Welt.",
        "Aber es ist wunderbar, wie man anfängt in einer neuen Weise zu begreifen und sich aufs neue bewundernd entzückt zu fühlen, wenn man diese Stimmung auf sich wirken läßt im Nachklange, ausgehend von den Reden des Krishna in der «Bhagavad Gita».",
        "Ein ganz neues Licht gießt sich aus über diese Zeilen der Bhagavad Gita, wenn man sich vergegenwärtigt, es wäre das nicht in den Worten, sondern in der ausgegossenen Stimmung im Nachklange enthalten, was ich eben jetzt geschildert habe.",
        "Ich wollte das nur wie eine Illustration des Hellsehens schildern und es so schildern, daß Sie nun diese Dichtung in die Hand nehmen können und versuchen können die Stimmung aufzufinden, die darin ausgegossen ist, und von da ausgehend ein Gefühl sich er- werben, was das entsprechende Erlebnis des Hellsehers ist, wenn er aus dem Tagesleben bewußt hinüberversetzt ist in die entsprechenden Welten, oder wenn Bewußtheit über den Schlaf sich ausdehnt."
      ],
      [
        "Diese Stimmung, dieses Grundgefühl hat noch etwas anderes beigemischt, es gesellt sich noch etwas anderes hinzu.",
        "Und da kann ich allerdings nicht anders, als dadurch einen Begriff davon hervorzurufen, daß ich versuche, in Worten - Worte müssen ja immer aus dem Sinnensein entlehnt werden - so gut es geht das zu schildern, was da erlebt wird.",
        "Was erlebt wird, ist etwa folgendes:"
      ],
      [
        "Man fühlt sich, soweit man überhaupt von einer Welt etwas fühlt, in diese Welt ergossen.",
        "Man fühlt eigentlich nirgends etwas Äußerliches zunächst als nur an dem einen Punkt der Welt, wo man vorher drinnen war.",
        "Das fühlt man als das einzige Äußerliche.",
        "Was man verbrochen hat, was man Gutes getan hat, das findet man in den einen Punkt der Welt zusammengedrängt.",
        "Das ist äußerlich.",
        "Im übrigen fühlt man sich mit Qem, was man selbst angerichtet hat in der Welt, über die ganze Welt ausgegossen.",
        "Namentlich hat man das Gefühl, daß es ein Unding ist, dieses Verhältnis zur Welt so zu erleben, daß man gewisse Worte darauf anwendet, die natürlich sind im"
      ],
      [
        "Sinnensein.",
        "So hören zum Beispiel die Worte «vorher» und «nachher» auf, einen Sinn zu haben.",
        "Denn mit dem Einschlafen ist es ja so, daß man nicht empfindet: jetzt ist das vorher, und das Aufwachen wird nachher sein, sondern man empfindet gewisse Erlebnisse, die mit dem Einschlafen eintreten, die dann weiter geschehen.",
        "Wenn man aber eine gewisse Summe von Erlebnissen durchlebt hat, steht man in einer gewissen Beziehung wieder an demselben Punkt, aber man steht nicht so an demselben Punkt, wie man beim Einschlafen gestanden hat.",
        "Wenn man von vorher und nachher spricht, so ist"
      ],
      [
        "das Vorher, wenn man es graphisch bezeichnet, in A und das Nachher in B.",
        "Man hat vielmehr das Gefühl: eingeschlafen bin ich.",
        "Dann wäre schon nicht richtig gebraucht.",
        "Es haben sich eben Erlebnisse abgespielt.",
        "Vorher und nachher verliert den Sinn dabei.",
        "Und wenn ich jetzt das Wort anwende - aber es ist nicht richtig! -, nach einer gewissen Zeit steht man da, wo man`vorher gestanden hat, so muß man sich denken, man steht sich gleichsam gegenüber, wie wenn man aus seinem Leibe hinausgegangen, herumgegangen wäre und hinschauen würde auf sich selber.",
        "Man steht also ungefähr an demselben Punkt, wo man gestanden hat beim Herausgehen, aber man steht sich gegenüber.",
        "Man hat die Richtung geändert.",
        "Dann - wieder nur vergleichsweise gebraucht - gehen die Ereignisse weiter, und es geht so weiter, wie wenn man wieder zum Leibe zurückgeht und wieder dann drinnen ist.",
        "Man erlebt nicht ein Vorher und Nachher, sondern man kann es nicht anders bezeichnen als eine Kreislaufbewegung, bei welcher Anfang, Mitte und Ende eigentlich nicht anders gebraucht werden können, als wenn man sie zusammen gebraucht.",
        "Wie beim Kreise, wenn er fertig gezogen ist, von jedem Punkte gesagt werden muß, da fängt er an, und - wenn man herum- gegangen ist - da hört er wieder auf - aber von jedem Punkte kann man das sagen -, so ist es bei diesem Erleben.",
        "Man hat nicht das Gefühl, daß man eine Zeit durchlebt, sondern eine Kreislaufbewegung"
      ],
      [
        "durchmacht, einen Zyklus beschreibt - und verliert bei diesem Erleben vollständig das Gefühl für die Zeit, die man gewöhnlich im Sinnensein hat.",
        "Man hat nur das Gefühl: Du bist in der Welt, und die Welt hat zu ihrem Grundcharakter das Zyklische, das Kreishafte.",
        "Und ein Wesen, welches nie die Erde betreten haben würde, welches"
      ],
      [
        "nie im Sinnensein gewesen wäre, sondern nur in dieser Welt immer gelebt hätte, würde nie auf den Gedanken kommen, die Welt habe einmal einen Anfang genommen und könne gegen ein Ende zulaufen, sondern es würde sich ihm immer nur eine in sich geschlossene Kreiswelt darstellen.",
        "Ein solches Wesen hätte gar keine Veranlassung zu sagen, es erstrebe die Ewigkeit, aus dem einfachen Grunde, weil überall alles ewig ist, weil nirgends etwas ist, über das man hin- aussehen könnte als über etwas Zeitliches in etwas Ewiges hinein."
      ],
      [
        "Dieses Gefühl der Zeitlosigkeit, des Zyklischen tritt also auf der entsprechenden Stufe des Hellsehens oder beim bewußten Durchleben des Schlaflebens auf.",
        "Aber dies vermischt sich mit einer gewissen Sehnsucht.",
        "Die Sehnsucht tritt dadurch hervor, daß man nie bei diesem Erleben in der höheren Welt eigentlich in Ruhe ist, man fühlt sich überall in der Kreisbewegung drinnen, fühlt sich immer bewegt, macht nie irgendwo halt.",
        "Und die Sehnsucht, die man hat, ist, irgendwo haltmachen zu können, irgendwo in die Zeit hinein- treten zu können!",
        "Genau, möchte ich sagen, das Umgekehrte von dem, was man im Sinnensein erlebt.",
        "In diesem fühlt man sich immer in der Zeit und hat die Sehnsucht nach der Ewigkeit.",
        "In der Welt, von der ich gesprochen habe, fühlt man in der Ewigkeit und hat die einzige Sehnsucht: Wenn doch irgendwo die Welt stille stände und irgendwo in das Zeitensein einrückte!",
        "Das ist das, was man als ein Grundgefühl kennenlernt: die immerwährende Beweglichkeit im All und die Sehnsucht nach der Zeit, das Erleben in dem immerwährenden, sich selber für immer garantierenden Werden - und die Sehnsucht: Ach, könnte man doch irgendwo auch einmal irgendwie vergehen!"
      ],
      [
        "Ja, man hat volle Berechtigung, wenn man die Begriffe des Sinnenseins anwendet, solche Dinge paradox zu finden.",
        "Aber man darf sich an diesen Paradoxien nicht stoßen, denn das würde bedeuten,"
      ],
      [
        "daß man sich nicht einlassen will auf die reale Beschreibung der höheren Welten, bei deren Betreten man nicht nur alles übrige, sondern auch die gewöhnlichen Beschreibungen der Sinneswelt aufgeben muß, wenn man diese höheren Welten in ihrer Wirklichkeit beschreiben will."
      ],
      [
        "Dieses Gefühl, das ich Ihnen geschildert habe, das Sie bitte betrachten wollen als ein Erlebnis, das man in sich selber und an sich selber hat - und es ist wichtig, daß man dieses Erleben in sich selber und an sich selber hat, denn das gehört zu den ersten Schritten auf dem Wege der Initiation -, kann in zweifacher Weise auftreten.",
        "Einmal kann dieses Gefühl so auftreten, daß man das, was man erlebt, so ausdrücken müßte: Ich habe eine Sehnsucht nach der Vergänglichkeit, nach dem Sein, zusammengedrängt in der Zeit, ich möchte nicht ausgegossen sein in die Ewigkeit.",
        "Dieses Gefühl, bitte das wohl zu beachten, hat man in der geistigen Welt, also nicht etwa im Sinnensein, sondern es braucht, wenn man wieder zurückkommt in die Sinneswelt, gar nicht dazusein, es ist nur da in der geistigen Welt.",
        "So kann man sagen, man habe in der geistigen Welt das Gefühl: du möchtest so recht hinein dich erleben in die Zeitlichkeit, möchtest so recht konzentriert sein in Selbständigkeit an einem Punkt des Weltenseins, und möchtest das so vollenden, daß du sagen kannst: Ach, was ist an aller Ewigkeit gelegen, die sich sonst im Universum ausdehnt, ich will mir dieses eine Selbständige sichern, da drinnen will ich sein!"
      ],
      [
        "Denken Sie sich diesen Wunsch, dieses Gefühl in der Welt erlebt.",
        "Es ist nur noch nicht so genau ausgedrückt, sondern wir müssen zu einer anderen Charakteristik noch kommen, müssen es noch mit etwas anderem verbinden, wenn der Ausdruck genau sein soll.",
        "Wenn man dieses Gefühl an das menschliche Sinnensein heranbringen will, so charakterisiert man mit Anklängen an die Sinneswelt.",
        "Aber ich habe ja gesagt, dort oben ist alles Wesenheit, und man kann gar nicht anders davon sprechen.",
        "Man hat aber noch nicht ganz recht, wenn man sagt, daß alles Wesenheit wäre.",
        "Wenn man in der SinnesweIt von einem Wunsche ergriffen ist, so kann man sich sagen: Ach, könntest du dir doch diesen einen Punkt sichern.",
        "Wenn man von"
      ],
      [
        "den höheren Welten in Wirklichkeit spricht, muß man sagen, man fühlt sich von einem Wesen hingedrängt, und das wirkt in einem und bewirkt in einem, daß man sich so ausdrückt, daß man hinein will in diesen Punkt.",
        "Wenn man einen solchen Wunsch verstanden hat - sich diesen Punkt zu sichern, konzentriert zu sein in der Zeitlichkeit - als einen Impuls, der von einem Wesen gegeben wird in der Welt - nur so kann es sein -, so hat man den Einfluß des luziferischen Wesens in der Welt erfaßt."
      ],
      [
        "Jetzt sind wir bei dem Begriff, wo man sagen kann: Wie kann man davon sprechen, man stünde einem luziferischen Wesen gegenüber?",
        "Wenn ein solcher Einfluß in den Welten der höheren Hierarchien auftritt: Hingezogensein von der Ewigkeit zu einem selbständigen Konzentriertsein in der Welt, so erlebt man das luziferische Wirken."
      ],
      [
        "Und wenn man es erlebt hat, dann weiß man, wie die Kräfte, die luziferisch sind, beschrieben werden können.",
        "Dann werden sie so beschrieben, wie ich es charakterisiert habe, und dann erhält man erst die Möglichkeit, real zu sprechen über einen Gegensatz, der seinen Nachklang auch hineinschickt in unsere Sinneswelt."
      ],
      [
        "Es ist der Gegensatz, der sich einfach dadurch ergibt, daß man jetzt weiß, im Si`nnensein ist es ganz natürlich, daß man in die Zeitlichkeit hineinversetzt ist.",
        "Für die geistige Welt, die, bildlich gesprochen, oberhalb der astralen Welt liegt, ist es ganz natürlich, daß man dort nichts mehr von Zeitlichkeit, sondern nur noch Ewigkeit verspürt."
      ],
      [
        "Und der Nachklang der devachanischen Erfahrung, der als Sehnsucht im Zeitlichen auftritt, ist die Sehnsucht nach der Ewigkeit.",
        "Das Zusammenspielen der wirklich erlebten Zeit - der wirklich erlebten Zeit im Augenblick - mit der Sehnsucht nach der Ewigkeit kommt davon her, weil unsere Sinneswelt die devachanische Welt durchdringt, die Welt des Geisterlandes."
      ],
      [
        "Und wie hinter unserer Sinneswelt das Geisterland selber für das gewöhnliche sinnliche Wahrnehmen verborgen ist, so ist hinter dem Augenblicke das Ewige verborgen.",
        "Und wie man nirgends sagen kann, da hört die Sinneswelt auf, und da beginnt die geistige Welt, sondern wie überall die geistige Welt das Sinnensein durchdringt, so durchdringt jeden Augenblick ihrer Qualität nach die Ewigkeit."
      ],
      [
        "Man erlebt nicht die"
      ],
      [
        "Ewigkeit, wenn man hinauskommt aus der Zeit, sondern wenn man im Augenblick selber die Ewigkeit hellseherisch erleben kann.",
        "Sie ist im Augenblick selber garantiert, denn sie steckt in jedem Augenblick drinnen."
      ],
      [
        "Wenn Sie irgendwo die Welt nehmen, so können Sie nicht sagen, wenn Sie vom Standpunkt des hellseherischen Bewußtseins aus sprechen, insofern irgendwo in der Welt ein Wesen ist, dieses Wesen sei ein zeitliches, oder dieses Wesen sei ein ewiges.",
        "Für das geistige Bewußtsein hat der Ausdruck keinen Sinn: Hier ist ein Wesen, das zeitlich ist -, oder: Hier ist ein Wesen, das ewig ist - sondern etwas ganz anderes hat einen Sinn."
      ],
      [
        "Was dem Dasein zugrunde liegt - Augenblick und Ewigkeit -, ist immer und überall.",
        "Die Frage kann nicht anders gestellt sein als: Wie kommt es, daß die Ewigkeit einmal als Augenblick erscheint, daß das Ewige einmal zeitlich erscheint, und daß ein Wesen in der Welt die Gestalt des Zeitlichen annimmt?"
      ],
      [
        "Das kommt von nichts anderem als davon her, daß unser Sinnensein überall, wo es auftritt, von luziferischen Wesenheiten zugleich durchsetzt ist.",
        "Und soweit das luziferische Wesen hereinspielt, soweit wird die Ewigkeit zur Zeitlichkeit gemacht."
      ],
      [
        "Sie müssen also sagen: Ein Wesen, das irgendwo in der Zeit auftritt, ist soviel ein ewiges Wesen, als es sich zu befreien vermag von dem luziferischen Dasein, und es ist ebensoviel ein zeitliches Wesen, als es unterliegt dem luziferis`chen Dasein.",
        "Man hört auf, wenn man geistig zu charakterisieren beginnt, die Ausdrücke des gewöhnlichen Lebens zu gebrauchen."
      ],
      [
        "Wenn man im gewöhnlichen Leben anwendet, was die Religionen lehren und was die Theosophie lehrt, so würde man sagen: Der Mensch hat seinen Leib als äußere Hülle, und er hat in sich sein Seelen- und Geistessein; der Leib ist vergänglich, das Seelen- und Geistessein ist ewig und unsterblich.",
        "So ist es richtig gesprochen, insofern man in der Sinnenwelt drinnen ist und dort die Dinge charakterisieren will."
      ],
      [
        "Es ist nicht mehr richtig gesprochen, wenn man den Gesichtspunkt der geistigen Welt anwenden will, sondern da muß man sagen: Der Mensch ist ein Wesen, zu dessen ganzer Natur fortschreitende göttliche Wesen und luziferische Wesen mitwirken müssen.",
        "Und insofern fortschreitende göttliche Wesen in ihm sind, ringt sich ein Teil"
      ],
      [
        "seines Wesens so los von allem, was daran luziferisch ist, daß es der Ewigkeit teilhaftig ist.",
        "Insofern die göttlichen Wesen wirken, hat der Mensch Anteil an dem Ewigen; insofern die luziferische Welt in ihm wirkt, gliedert sich an die Menschenwesenheit alles an, was mit Vergänglichkeit und Zeitlichkeit verbunden ist."
      ],
      [
        "Also als ein Zusammenwirken verschiedenartiger Wesenheiten erscheinen Ewigkeit und Zeitlichkeit.",
        "In den höheren Welten hat es auch keinen Sinn mehr, von solchen abstrakten Gegensätzen zu sprechen wie Ewigkeit und Zeitlichkeit; die hören auf, in den höheren Welten einen Sinn zu haben.",
        "Da muß man von Wesenheiten sprechen.",
        "Deshalb spricht man von fortschreitenden göttlichen Wesenheiten und von luziferischen Wesenheiten.",
        "Weil die in den höheren Welten da sind, spiegelt sich ihr Verhältnis zueinander als der Gegensatz von Ewigkeit und Zeitlichkeit."
      ],
      [
        "Ich habe gesagt, es ist gut, wenn der Mensch bei seinem Auf- rücken in die Welt, die hier gemeint ist, zunächst mehr moralische Erinnerungen fühlt und nicht so sehr seine äußere physische Gestalt.",
        "Der Mensch soll nach und nach erst - mit den fortgesetzten Übungen für die ersten Schritte der Initiation - auch so hellseherisch werden, daß das Erinnerungsbild an die äußere physische Gestalt auftritt.",
        "Mit diesem Auftreten des Erinnerungsbildes der eigenen physischen Gestalt ist aber noch etwas anderes verbunden: daß eigentlich erst von da ab der Mensch - und so ist es gut - nicht nur im allgemeinen sein Seelenleben als Erinnerung fühlt, nicht nur im allgemeinen seine guten und schlechten Taten, seine moralischen und dummen Taten, sondern sein ganzes Ich fühlt.",
        "Sein ganzes Selbst fühlt er in dem Moment als Erinnerung, wo er auf seinen Leib als Form zurückschauen kann.",
        "Da fühlt er dann sein Wesen wie gespalten.",
        "Er schaut auf einen Teil, den er beim Hüter der Schwelle abgelegt hat, und schaut auf das, was er sein Ich nennt in der Sinnes- weIt.",
        "Jetzt ist man, wenn man auf sein Ich zurückblickt, auch in bezug auf sein Ich gespalten und sagt sich mit aller Ruhe: Was du dein Ich früher genannt hast, daran erinnerst du dich jetzt nur; jetzt lebst du in einem übergeordneten Ich, und das verhält sich so zu dem früheren Ich, wie du dich als Denker verhältst in bezug auf die Erinnerungen"
      ],
      [
        "zum Leben im Sinnensein.",
        "Auf das also, was der Mensch eigentlich ist als Erdenmensch, auf seinen Ich-Menschen sieht man erst auf dieser Stufe herunter.",
        "Man ist aber da zugleich entrückt in eine noch höhere Welt, die man das höhere Geisterland oder - wenn man will - die höhere Mentalwelt nennen kann, eine etwas von den anderen verschiedene.",
        "Da ist man darinnen, wenn man das Ich zwiegespalten fühlt und das gewöhnliche Ich nur noch als Erinnerung fühlt.",
        "Da hat man erst die Möglichkeit, in richtiger Weise den Menschen auf der Erde zu beurteilen.",
        "Wenn man von dort zurückschaut, fängt man an zu wissen, was der Mensch seiner tiefsten Wesenheit nach ist.",
        "Da bekommt man auch die Möglichkeit, ein erlebtes Urteil zu gewinnen über den Verlauf der Geschichte.",
        "Da gliedert sich einem die erlebte Menschheitsentwickelung in den Fortgang der Seelen als Ich-Wesen, da ragen heraus aus dem gewöhnlichen Fortgange die Wesen, welche die führenden im Fortgang der Menschheit sind.",
        "Da ist es so, wie ich es im zweiten Vortrage charakterisiert habe, daß man wirklich die Impulse erlebt, die fortwährend in die Evolution der Menschheit hineinfließen durch die Initiierten, die überall aus dem Sinnensein in das Geistessein zu gehen haben, damit sie ihre Impulse geben können.",
        "Mit dem Punkt, wo man den Menschen als Ich-Wesen erlebt, erlebt man auch erst die wahre Einsicht in das Mensch`enwesen als solches.",
        "Nur eine Ausnahme gibt es dabei."
      ],
      [
        "Fassen wir das schon Gesagte zusammen.",
        "Wenn der Mensch die ersten Schritte zur Initiation durchmacht, kann er sich hellseherisch zur Welt des nie`deren Geisterlandes erheben; er erlebt die Vorstellungen des Seelischen, des Moralischen, des Intellektuellen, sieht hinunter auf das, was in den Seelen vorgeht, auch wenn sie sich nicht zusammenfassen würden als Ich-Wesen.",
        "Das Zusammenfassen der Wesen als Ich-Wesen erlebt man im höheren Geisterlande und damit auch alle Blüten des Geisteslebens in den Initiierten - mit einer einzigen Ausnahme, die richtig und gut ist, wenn sie als Ausnahme eintreten kann und dadurch die allgemeine Regel durchbrochen wird: Vom niederen Geisterlande aus sieht man die ganze Wesenheit des Christus Jesus!",
        "So daß man zurückblickend, rein menschlich sehend"
      ],
      [
        "und die Erinnerungsvorstellungen festhaltend, die Erinnerung hat an den Christus Jesus, an alle Ereignisse, die mit ihm vorgegangen sind, wenn die andere Bedingung erfüllt ist, von der ich im zweiten Vortrage gesprochen habe.",
        "Die Wahrheit über alle anderen Initiierten erlebt man erst in dem höheren Geisterlande."
      ],
      [
        "Da haben wir einen Unterschied von einer ungeheuren Tragweite.",
        "Wenn der Mensch hinaufkommt in die geistige Welt, dann sieht er - zurückblickend - auf das Irdische, das er zunächst seelisch sieht, wenn er nicht so die Erinnerung hat, daß er zurückblickend auf das Erdensein sich erinnert an die physisch herumgehenden Menschen in Gestalt und Form.",
        "Das soll er erst erleben, wenn er den charakterisierten höheren Punkt erlebt.",
        "Nur den Christus Jesus darf und soll er bei den ersten charakterisierten Schritten auf dem Wege zur Initiation sehen!",
        "Und er kann ihn sehen, wenn er hinaufrückt und sich überall umgeben sieht von nur Seelischem, das zunächst nicht durchtränkt ist von Ich-Wesenheit, da drinnen aber wie eine Art von Mittelpunkt die Christus-Wesenheit, vollbringend das Mysterium von Golgatha, mit dem Ich durchdrungen."
      ],
      [
        "Was ich Ihnen jetzt gesagt habe, kann natürlich nicht irgendwie aufgefaßt werden als ein Ausfluß einer der bestehenden christlich konfessionellen Weltanschauungen, denn ich glaube nicht, daß es sich irgendwo charakterisiert fände.",
        "Aber wohl findet sich in einer gewissen Weise, weil das Christentum eben durchaus nicht in seinem bisherigen Verlauf das erreicht hat, was es erreichen muß, man möchte sagen, das Gegenteil von dem Charakterisierten, aber auf eine sehr eigentümliche Weise, auf die man erst kommt, wenn man die Dinge okkult genau einsieht.",
        "Vielleicht werden doch einige von Ihnen wissen, daß es unter den offiziellen Vertretern des Christentums viele gibt, die eine heillose Angst vor allem haben, was man Okkultismus nennt, und alles dieses als ein reines Teufelszeug betrachten, das dem Menschen nur Verderben bringen kann.",
        "Warum ist das so?",
        "Warum erlebt man es immer wieder und wieder, wenn man mit den Vertretern irgendwelcher Priesterschaft spricht und auf Okkultismus oder Theosophie die Rede kommt, daß sie das abweisen?",
        "Und wenn man einem solchen Herrn sagt: Sehen Sie doch"
      ],
      [
        "einmal ein, daß die christlichen Heiligen immer die höheren Welten erlebt haben und daß dies in den betreffenden Biographien dargestellt ist -, dann bekommt man zur Antwort: Ja, das ist zwar so, aber das darf nicht angestrebt werden.",
        "Man darf zwar das Leben der Heiligen lesen, aber wenn man sich nicht der Gefahr der Teufelei aussetzen will, darf man es nicht nachleben. - Woher kommt das?"
      ],
      [
        "Wenn Sie das zusammennehmen, was ich gesagt habe, werden Sie es begreifen: Es ist eine Art Angstgefühl, das sich darin ausdrückt, ein recht starkes Angstgefühl.",
        "Die Leute wissen nicht, woher es kommt, aber der Okkultist kann es wissen."
      ],
      [
        "Der Mensch kann - wie ich Ihnen im zweiten Vortrag gesagt habe - in den höheren Welten diese Erinnerung an den Christus nur haben, wenn er ihn richtig hier in der physisch.sinnlichen Welt auf der Erde erfaßt hat.",
        "Und richtig ist es, schon in der allernächsten Welt ihn zu haben, in die man eintritt, wo man noch das übrige Menschliche als Erinnerungsvorstellung hat."
      ],
      [
        "Es ist auf der einen Seite nötig, daß man die Erinnerungsvorstellung hat, auf der anderen Seite kann man sie nur haben, wenn man sich hier schon damit durchdrungen hat.",
        "Deshalb kommt es vor, daß die, welche etwas mit dem Okkultismus bekannt geworden sind, aber gewisse wichtige und eklatante Tatsachen nicht durchdrungen haben, es für einerlei halten, ob der Mensch in unseren jetzigen Zeiten, wenn er in die höheren Welten hinaufdringt, mit der Christus-Vorstellung bekannt geworden ist oder nicht."
      ],
      [
        "Denn sie glauben, was dort oben ist, hinge doch nicht so stark von dem ab, was man unten erlebt hat, obwohl sie es sonst immer betonen.",
        "Es hängt aber gerade die Art, zu dem Christus sich in den höheren Welten zu stellen, davon ab, wie man sich zu ihm verhalten hat in der physischen Welt."
      ],
      [
        "Wenn man es nicht versucht, die richtige Vorstellung von ihm in der physischen Welt hervorzurufen, so kommt man in einer gewissen Weise unreif hinauf und kann ihn dort nicht finden, trotzdem man ihn finden sollte; so daß einem, wenn man nicht auf diese ganz bedeutsame, eklatante Sache bedacht ist, in der Tat durch das Hinaufrücken in die höheren Welten die Christus-Vorstellung vollständig verlorengehen kann.",
        "Wenn es also jemand verschmähen würde, schon innerhalb des Sinnenseins ein"
      ],
      [
        "Verhältnis zu dem Christus zu gewinnen, so könnte er ein großer Okkultist werden und nichts von dem Christus durch seine Wahrnehmungen in den höheren Welten wissen, denn er würde ihn dort nicht finden und würde nichts lernen können von ihm.",
        "Seine Vorstellungen über ihn würden immer mangelhaft sein."
      ],
      [
        "Das ist das Bedeutsame.",
        "Ich sage Ihnen damit nicht irgend etwas, was ich Ihnen aus einer subjektiven Meinung heraus sage, sondern was ein gemeinsames objektives Resultat derer ist, die darüber Forschungen angestellt haben."
      ],
      [
        "Bei den Okkultisten kann es objektiv beschrieben werden, daß es so ist; bei dem, der keine Nötigung dazu empfindet, Okkultist zu werden, sondern der nur ein braver Vertreter seines Religionsbekenntnisses ist, äußert es sich mit all jener Unbewußtheit, die ich jetzt als Angstzustand geschildert habe.",
        "Und wenn jemand dann den Weg in die höheren Welten unternehmen will, ist das ein großes Teufelszeug, und solche Menschen meinen, der könnte doch vielleicht nicht das richtige Verhältnis zum Christus gewonnen ha- ben, also soll er nur ja nicht aus der gewöhnlichen Welt hinausgeführt werden."
      ],
      [
        "Es ist also diese Angst in einer gewissen Weise eine begründete.",
        "Diese Menschen wissen nicht, wie es zum Christus hin- geht> und wenn sie dann in die höheren Welten hineinkommen, geht ihnen der Christus verloren."
      ],
      [
        "Es ist das etwas, was man als eine Art Angst bei einer gewissen Priesterschaft verstehen kann, dem man aber in keiner Weise entgegenkommen kann.",
        "Ich bitte diesen kleinen Exkurs, der kulturhistorisch interessant ist, weil man dadurch vieles versteht von dem, was sich im Leben abspielt, als bedeutend zu betrachten und sich nachdenkend im Leben damit zu beschäftigen."
      ],
      [
        "Von zwei verschiedenen Gesichtspunkten aus habe ich Ihnen sozusagen Ausläufer zu dem Christus gezeigt und habe versucht, ein paar Lichter auf die Christus-Wesenheit zu werfen.",
        "Alles, was ich gesagt habe, kann auch ohne diese zwei Ausläufer gesagt werden und ist dann auch gültig und verständlich.",
        "Aber es ist notwendig, sich objektiv den Tatsachen entgegenzustellen und sie ganz unbeeinflußt von den konfessionellen Richtungen als kosmische Tatsachen ins Auge zu fassen."
      ],
      [
        "Damit haben wir versucht, ein gewisses Licht zu werfen auf die Begriffe Zeitlichkeit, Vergänglichkeit, Augenblick und Ewigkeit auf der einen Seite, Sterblichkeit und Unsterblichkeit auf der andern Seite.",
        "Und es haben sich zusammengebunden die Begriffe Vergänglichkeit und Zeitlichkeit mit dem luziferischen Prinzip."
      ],
      [
        "Mit dem Christus - Prinzip werden sich uns Begriffe wie Ewigkeit, Unsterblichkeit zusammenfügen.",
        "Es könnte jemand glauben, daß dies im allermindesten wenigstens irgendeine Geringwertung des luziferischen Prinzips sein könnte, eine Abweisung unter allen Umständen, indem bei dem Luziferischen auf das Zeitliche, Vergänglichere, auf das Konzentriertsein auf einen Punkt hingewiesen wird."
      ],
      [
        "Für heute möchte ich das eine nur sagen, daß man nicht unter allen Umständen recht hat> den Lichtträger als etwas zu betrachten, vor dem man sich zu fürchten hätte, daß man Luzifer abzuweisen hat als etwas, von dem man unter allen Umständen loskommen soll.",
        "Wenn man das tut, bedenkt man nicht, daß der wahre Okkultismus lehrt, daß es ein ähnliches Gefühl gibt hier in der Sinneswelt wie in der über- sinnlichen Welt."
      ],
      [
        "Im Sinnensein fühlt der Mensch: Ich lebe im Zeitlichen und sehne mich nach der Ewigkeit; ich lebe im Augenblick und begehre die Ewigkeit.",
        "Im Geistigen gibt es das Gefühl: Ich lebe im Ewigen und sehne mich nach dem Augenblick."
      ],
      [
        "Und verfolgen Sie jetzt die Mitteilungen aus der`Akasha-Chronik.",
        "Ist nicht in der alten Zeit, die wir oft als die lemurische bezeichnet haben, das Mensch-Werden eine Art Übergang aus einem solchen Zustande, wie wir ihn im Schlafe haben, in die Zustände des Wachens?"
      ],
      [
        "Verfolgen Sie genau, was in der lemurischen Zeit geschehen ist, und Sie können sich sagen: Indem der Mensch einen Übergang durchmachte aus einem geistigen Schlafzustand in die wachen Erdenzustände, ging die ganze Evolution damals vom Geistigen in das Sinnliche über.",
        "Da ist ein Übergang, und unser jetziges Sinnensein bekommt erst einen Sinn seit der lemurischen Zeit."
      ],
      [
        "Und überlegen Sie sich, ob es so unnatürlich ist, daß der Mensch, als er aus der höheren Welt herausschlüpfte, um von dem Luziferischen ergriffen zu sein, etwas mitnahm wie eine Sehnsucht nach dem Ewigen!",
        "Dann haben Sie in bezug auf das Luziferische eine Art Erinnerung an einen vorirdischen"
      ],
      [
        "Zustand, eine Erinnerung an das, was der Mensch gehabt hat, bevor er in das Sinnensein kam, und was sich nicht hätte erhalten sollen: die Sehnsucht nach dem Augenblick, nach dem Zeitlichen.",
        "Inwiefern diese an der Gesamtevolution des Menschen beteiligt ist, davon morgen weiter."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "SEKSTER VORTRAG München, 30. August 1912",
    "paragraphs": [
      "Aus den bisher gehaltenen Vorträgen wird Ihnen vielleicht ersichtlich geworden sein, wie nötig es ist, seine Vorstellungen beweglich, wandelbar zu machen, wenn eine richtige Charakteristik von den verschiedenen Welten, von denen man sprechen kann und von denen das Sinnensein, unsere gewöhnliche Sinneswelt doch nur die eine ist, entgegengenommen werden soll. Aus vielem Gesagten kann Ihnen hervorgehen, daß man geradezu eine andere Sprache menschlicher Vorstellungen sprechen muß, wenn man von der einen Welt in die andere den Übergang herbeiführen will.",
      "Das ist die eine Seite der Sache. Aber es gibt eine andere Seite der Sache: daß alle diese Welten wieder zusammenwirken und daß in der einen Welt immer gewissermaßen der Abglanz, die Hineinwirkungen der übrigen Welten wahrzunehmen sind.",
      "In jeder Welt hat man es damit zu tun, daß einem die Erscheinungen und Wesenheiten dieser Welt selbst entgegentreten und dann wieder alles dasjenige, was von den anderen Welten in diese besondere Welt hineinwirkt. Dieses alles muß sorgfältig berücksichtigt werden, wenn man verstehen will, was die Geheimnisse der Initiation sind, welches die Beziehungen des Augenblickes zur Ewigkeit, des Lebensdunkels zum Geisteslichte sind.",
      "Es gibt - wie Sie dargestellt finden in «Wie erlangt man Erkenntnisse der höheren Welten?» - gewisse Regeln, gewisse Anweisungen, welchen sich die Seele unterwerfen kann, um den Aufstieg in die über- sinnlichen Welten zu bewirken. Solche Regeln sind selbstverständlich nicht nur nützlich, sondern demjenigen unentbehrlich, der wirklich die ersten oder die weiteren Schritte der Initiation unternehmen will.",
      "Aber insbesondere in unserer Zeit muß auf eines aufmerksam gemacht werden.",
      "Unsere Zeit hat eine gewisse Eigentümlichkeit, die zusammenhängt mit der ganzen Eigenart des Weltenzyklus, in dem wir leben; unsere Zeit hat etwas Lehrhaftes, etwas Theoretisierendes. Und wie sehr man sich auch bemüht, da oder dort den Hang zum Theoretisieren",
      "abzulegen, er sitzt gewissermaßen doch dem Menschen der Gegenwart in den Seelengründen. Das bewirkt, daß diese Menschen der Gegenwart, wenn es sich um den Aufstieg zu den höheren Welten handelt, zunächst vor allen Dingen erwarten, daß ihnen unter allen Umständen gesagt werde, wie sich jeder einzelne verhalten solle, wenn die Seele in die höheren Welten hinaufgelangen will.",
      "GegenÜber dem wirklichen Erleben des Übersinnlichen stellt sich aber doch etwas ein, was man in gewisser Beziehung mißlich nennen möchte in all denjenigen Darstellungen, welche - man möchte sagen - einen normalen Weg, eine normale Marschroute angeben, um in die höheren Welten hinaufzueilen. Denn das Leben ist etwas Kompliziertes.",
      "Und jede Seele in irgendeiner Lebenslage, in der sie sich befindet - und jedesmal muß man von einer bestimmten Lebenslage ausgehen, wenn man den Aufstieg in die höheren Welten unternehmen will -, steht in einem bestimmten Karma drinnen, hat einen bestimmten Ausgangspunkt. Keine Seele ist in derselben Lage wie die andere.",
      "Daher ist im Grunde genommen auch der Weg in die übersinnlichen Welten hinauf für jede Seele ein individueller, ein solcher, welcher sich je nach der betreffenden Seele beim Ausgangspunkt richtet. Man kann nicht sagen, wenn man im richtigen Sinne sprechen will: so muß nach einem normalen Prinzip unmittelbar jede Seele den Aufstieg in die höheren Welten, die Initiation,`durchmachen.",
      "Daher das Bedürfnis, nicht nur in kurzen Broschüren oder dergleichen - was ja leichter wäre - Anweisungen zu geben: so und so soll es die Seele machen, um den Glauben zu erwecken, man könne, wenn man solche Regeln befolgt, unter allen Umständen in der gleichen Art wie jede andere Seele in die höheren Welten hinaufsteigen. Daher das Mißliche solcher Dinge.",
      "Deshalb namentlich habe ich versucht, in dem Büchelchen «Ein Weg zur Selbsterkenntnis des Menschen» etwas zu zeigen, was individuell ist und doch einer jeden Seele nützlich sein kann. Aber deshalb ergab sich auch die Notwendigkeit, die Mannigfaltigkeit und die Variabilität des Initiationsweges zu zeigen.",
      "Und ohne selbst etwa irgendwie Erklärungen liefern zu wollen über das, was getan worden ist, möchte ich Sie nur darauf hinweisen, wie sich die Notwendigkeiten zu den drei Gestalten ergeben,",
      "welche in den drei Mysterienversuchen - «Die Pforte der Einweihung», «Die Prüfung der Seele» und «Der Hüter der Schwelle» - vor Ihre Seele hintreten als Johannes Thomasius, Capesius und Strader. Sie zeigen Ihnen den Weg der ersten Schritte zur Initiation gleichsam in drei verschiedenen Aspekten.",
      "Man kann von keinem dieser Wege sagen, daß er besser oder schlechter sei als der Weg des anderen; sondern man muß von jedem dieser Wege sagen, daß er sich ergeben mußte je nach dem Karma der betreffenden Individualitäten. Man kann nur sagen: eine Seele, welche so ist wie Johannes Thomasius, oder welche so ist wie Capesius, muß eben solche Wege gehen, wie sie versucht worden sind, nicht in Theorien, nicht lehrhaft, sondern in Gestalten zu zeigen.",
      "Daher das Bedürfnis, solche Gestalten zu zeigen. Und immer notwendiger und notwendiger wird es werden, hinwegzuführen von dem Glauben, daß man mit ein paar Regeln in diesen Dingen auskomme, immer notwendiger wird es sein, gerade auf spirituellem Gebiete von dem Lehrhaften auf das Gestaltete hinzuweisen.",
      "Weil die Beziehungen der Welten so mannigfaltige sind, deshalb müssen auch die Wege der einzelnen Individualitäten so mann1gfaltige sein. Wenn man aber erst dazu kommt, gewisse Individualitäten oder Wesenheiten der höheren Welten ernsthaft ins Auge zu fassen und deren Anteil an dem Menschen zu prüfen, dann muß man erst recht die Notwendigkeit fühlen, diese Gestalten lebendig zu zeigen, sie in ihrer Mannigfaltigkeit hinzustellen, nicht bloß Definitionen von ihnen zu geben.",
      "In unserer Zeit ist es insbesondere für diejenigen, die spirituelle Erkenntnis anstreben, wichtig, solche Gestalten wie Luzifer und Ahriman, denen man auf dem Wege zur Initiation ja immer begegnet, einmal gerade in ihrer Vielartigkeit, in ihrer Variabilität ins Auge zu fassen. Dann wird sich zeigen, wie merkwürdig die Beziehungen und Verkettungen der einen Welt mit der anderen sind.",
      "Es zeigt sich an vielen Zeichen unserer Zeit, daß allmählich Verständnis wachgerufen werden kann für das Hereinspielen der einen Welt in die andere. Ich möchte da zunächst von etwas Naheliegendem ausgehen, das nur nicht immer naheliegend genug empfunden wird.",
      "In unserer Zeit besteht in den weitesten Kreisen das lebhafteste Bedürfnis, die Naturordnung, die Naturgesetze kennenzulernen, die durch alles - auch durch alles Wesenhafte - hindurchwirken, das uns im Sinnensein entgegentritt. Und es besteht der Hang, nicht zu achten auf alles, was etwa von anderen Welten her über den Menschen und das Weltendasein gesagt werden kann, sondern nur sozusagen aus der einen Welt heraus eine gesamte Weltanschauung aufzubauen. Das gibt ja die mehr oder weniger monistischen oder auch als materialistisch bezeichneten Weltanschauungen der Gegenwart. Man möchte sagen, gleichsam wie ein wohltätiger Gegenschlag gegen dieses Bestreben haben sich in unserer Zeit andere Bestrebungen geltend gemacht, welche innerhalb der Welt, in der wir leben, solche Erscheinungen aufsuchen, welche von anderen Gesetzen beherrscht sind als die Welt der Naturordnung, diejenigen Erscheinungen in ihrer Mannigfaltigkeit aufsuchen, welche als widersprechend dieser Naturordnung von dem materialistischen Sinn empfunden werden.",
      "Man sollte wohl achten auf alles, was im Sinne ernster Wissenschaftlichkeit auf diesem Gebiete gearbeitet wird. Denn indem in unserer Zeit dem rein materialistischen Forschen - wenn auch wenig beachtet - ein anderes Forschen entgegentritt, welches andere Zusammenhänge in unserem Sinnensein sucht, als das Sinnensein selber darbietet, wird ja nichts Geringeres getan, als das Hereinspielen ganz anderer Welten mit anderen Daseinsgesetzen schon innerhalb der Forschungsmethoden des Sinnenseins selbst zu suchen. In dieser Beziehung ist es außerordentlich wünschenswert, daß namentlich der Theosoph immer darauf achten sollte, was in dieser Richtung geleistet wird - geleistet wird, indem die wissenschaftlichen Methoden ausgedehnt werden auf das Hereinspielen übersinnlicher Welten in unser Sinnensein. Für kleinere Kreise habe ich schon darauf hingewiesen; für diesen größeren Kreis will ich es heute tun.",
      "In seinem Buche «Das Mysterium des Menschen», das ich Ihnen ganz besonders-empfehlen möchte, hat unser lieber Freund Ludwig Deinhard sich der dankenswerten Aufgabe unterzogen, in dem ersten Teil eine sehr übersichtliche Zusammenstellung und Charakterisierung alles dessen zu bringen, was in unserer Zeit mit den wissenschaftlichen",
      "Methoden, die heute anerkannt sind - aber so, wie sie angewendet sind, eben noch mit Vorurteil angewendet werden -, innerhalb der Welt, die jeder betreten kann, untersucht werden kann über das Hereinspielen einer übersinnlichen Welt. Dies einmal übersichtlich vor sich zu haben, ist eine dankenswerte Aufgabe gewesen, und ist etwas, was jeder kennenlernen sollte, der sich gerade von diesem Gesichtspunkt aus dafür interessiert, wie man auf Schritt und Tritt, wenn man nur die Tatsachen nimmt, das Herausspringen des Übersinnlichen aus dem Sinnensein finden kann. So sehen wir also gerade mit einer wichtigen Aufgabe dieses Buch in der letzten Zeit unter uns, und ich darf wohl auch hier an diesem Orte auf dieses Buch «Das Mysterium des Menschen» von Ludwig Deinhard hinweisen.",
      "Dieses Hereinspielen anderer Welten in die Sinneswelt erzeugt innerhalb der letzteren etwas, was sich nun in allen Welten wiederholt, was in allen Welten auftritt, was aber ganz besonders notwendig macht, daß wir uns bekannt machen mit der Notwendigkeit, nicht pedantisch, einseitig, streng geformt uns Dogmen oder Urteile zu bilden dahin lautend: dieses sei so, jenes so, Luzifer so, Ahriman so, Luziferisches müsse man fliehen, Ahrimanisches müsse man fliehen oder dergleichen. Eingelaufen ist unsere gestrige Betrachtung gerade in solche Dinge.",
      "Nehmen wir an, derjenige, der die ersten Schritte auf dem Wege zur Initiation durchgemacht hat, begegnet, weil er in seinem Seelen- leben durch das Sich-Öffnen der Seelenaugen hellseherisch geworden ist, jener Gestalt, die wir als Luzifer in den übersinnlichen Welten bezeichnen. Als was konnten wir gestern diese Gestalt bezeichnen? Sie tritt der Seele als das entgegen, was immerzu bestrebt ist, das Ewige, das sonst in immerwährender Beweglichkeit und Veränderlichkeit ist, zur Beständigkeit, zum Zeitlichen, zum Augenblicklichen zu machen, so daß es als Individuelles sich erfreuen, groß werden könne. Und tritt man als Seele Luzifer in den übersinnlichen Welten entgegen, so erscheint er dort als der große Lichtträger, welcher einen gleichsam dazu führt - ja, wahrhaftig dazu führt, alle die Schätze, all das Wesenhafte, das da in den spirituellen Welten ist,",
      "herunterzutragen in die Sinneswelt und in der Sinneswelt davon Abglanz und Offenbarung zu schaffen. Und folgt man Luzifer in den übersinnlichen Welten in diesem seinem Bestreben, dann wirkt man dazu, daß die urewige Weltaufgabe erfüllt werde, daß alles Unoffenbare offenbar werde, daß alles Ewige dem Augenblicke anvertraut werde, daß alles, was verfließt im unbestimmten Ewigen, in der innerlichen Größe des individuellen Augenblickes festgehalten werden könne.",
      "Nun sitzt es in jeder Menschenseele wie ein Nachklang aus der geistigen Welt, daß dieses Streben, das Unoffenbare offenbar zu machen, das Ewige im Augenblick zu fixieren, auch wirklich geschehe. Daher ist es, wenn der Mensch entweder durch die Initiation oder durch den Tod die übersinnlichen Welten beschreitet, daß in ihm Luzifer als Lichtesträger wirklich wirkt, und die Gefahren, denen der Mensch in den höheren Welten gegenüber Luzifer ausgesetzt ist, sind nur dann eigentlich vorhanden, wenn der Mensch das, was seine Stellung innerhalb des Sinnenseins zu Luzifer ausmachen soll, in einem zu hohen Maße in die höheren Welten hinein mitbringt. Luzifer ist nur gefährlich beim Wandeln in den höheren Welten, wenn man zu sehr die Natur und Wesenhaftigkeit des Sinnesmenschen in diese höheren Welten hinein mitbringt. Aber wie steht es innerhalb des Sinnenseins selbst, da ja die übersinnlichen Welten immer ins Sinnensein hereinspielen, mit Luzifer? Denn zunächst haben wir es im historischen Gange der Menschheit im Sinnensein und seiner Evolution mit dem Hereinspielen der höheren Welten zu tun, die wirksame Impulse abgeben, damit das eine hinter dem andern im Sinnensein geschehe, wie es in der Geschichte der Menschheit durch das Erdensein hindurch sich abspielt.",
      "Ja, in dieses Sinnensein spielen herein diejenigen Bestrebungen, die wir als menschlich egoistische, als selbstsüchtige Bestrebungen jeder Seele betrachten. Wir wissen ja, daß jede Seelenentwickelung vom Egoismus ausgehen muß. Das ist natürlich. Wir wissen aber auch, daß wieder ein Herausarbeiten aus dem Egoismus stattfinden kann. In all das, was jemals Seelen aus dem Egoismus heraus auf der Erde haben tun können, fällt das hinein, was man nennen kann:",
      "Offenbarung des Ewigen in dem Augenblick. In das, was in der individuellen Seele fixiert ist, spielen fortwährend luziferische Kräfte hinein. Aber noch in etwas anderes spielen sie hinein, nämlich in all das, was der einzelne Mensch gerade für die gesamte WeltenordnUng, für das Weltendasein dadurch tun kann, daß er eine Egoität ist und hat, daß er in sich innerliche Größe entwickeln kann, die aus seinem Innern hervorsprudelt. Was ist denn das individuelle Große in der einzelnen Seele anderes als das, was der Keim des Großen in aller Weltenentwickelung der Menschheit ist? Wodurch haben Homer, Shakespeare, Dante, Goethe auf die Menschheit gewirkt? Dadurch, daß sie Egoitäten waren, daß in ihrem Innern ganze Welten waren, Welten, die nur aus ihrem Innern, aus ihrer Egoität herausgekommen sind. Dadurch aber werden - auf dem Umwege durch die Egoitäten - die Impulse des geistigen Lebens hereingetragen, welche von Epoche zu Epoche gerade die größten, nämlich die geistigen Taten der Menschheit vermitteln. Da ist wieder Luzifer drinnen. Da ist er der Lichtträger, der Impuls und die Macht alles Großen, welches aus der großen punktuellen, aus der einzelnen Menschenseele sprudelnden Ewigkeitskraft in die Menschheitsevolution ausstrahlt.",
      "Zwischen zwei Pole ist die Menschenseele hereingestellt, die einfach der Abdruck und der Abglanz all der Welten sind, in denen die Menschenseele wirklich steht: daß sie sich in sich verhärtet, sich in ihrer Egoität völlig einspinnt und nur das will, was ihr selber dient, was sie selber befriedigt; und daß die Menschenseele aus ihren Tiefen heraus die Kräfte holt, die einstrahlen können in das ganze Leben der Menschheit? Wann tritt nun diese Egoität des Menschen zutage? - Gerade dann, wenn man denkt, wie notwendig es ist, daß ein jeder Mensch das Seinige, was sein Individuellstes ist, was das tiefste Eigentum seiner Egoität ist, den anderen Menschen darbringt. In allem aber, was der Mensch für den Menschen aus seiner Egoität heraus tun kann, lebt wieder Luzifer, der andere Pol des Luzifer. Und in dem, was der Mensch so unter dem Einiluß des Lichtträgers für die Menschheit leisten kann, liegt ein Abglanz dessen, was Luzifer in den höheren Welten wirklich ist, liegt ein Abglanz der schöpferischen Tätigkeit des Luzifer: das Unoffenbare zu dem Offenbaren zu",
      "machen. Kann man also sagen, Luzifer sei böse, oder kann man etwa sagen, Luzifer sei gut? - Man kann nur sagen: Wer behaupten will, Luzifer sei böse und müsse geflohen werden, der müßte 'auch sagen, das Feuer müsse geflohen werden, weil das Leben unter Umständen im Feuer ersterben muß. Man findet auf dem Wege zur Initiation, daß die Ausdrücke gut und böse gar nicht in dieser Art anwendbar sind, sobald man das Wesen der übersinnlichen Weltenordnung charakterisieren will. Das Feuer ist gut, wenn es unter guten Umständen wirkt; es ist schlecht, wenn es unter schlechten Umständen wirkt; an sich ist es nicht gut und nicht schlecht. So ist es mit Luzifer. Er übt einen guten Einfluß auf die Menschenseele aus, wenn er der Anreger wird zum Herausholen alles dessen aus der Menschenseele, was der Mensch als sein Individuelles hinopfern kann am Altare der Menschheitsevolution. Luzifer wird ein böses Wesen, das heißt, was er tut, wird böse, wenn er solche Impulse der Menschenseele gibt, daß diese nur alles zur Selbstbefriedigung in sich hinein-",
      "führen will. Wie die Taten der Wesen wirken in der Welt, das muß man verfolgen, wenn man auf diese Wesenheiten hingewiesen worden ist. Die Wirkungen der übersinnlichen Wesenheiten kann man bezeichnen als gute und böse; die Wesenheiten selber nimmermehr.",
      "Denken Sie einmal, irgendwo - verzeihen Sie das Paradoxon -, ich will nicht sagen, wo es sein könnte, nehmen Sie an, auf irgendeiner Insel sei eine Menschheit, welche die Anschauung hätte, man müsse sich vor Luzifer unter allen Umständen hüten, man müsse ihn so weit weghalten von den Menschen, als es nur irgend möglich ist.",
      "Das würde nicht bezeugen, daß die Menschen dieser Insel die beste Erkenntnis von Luzifer hätten, aber es würde etwas anderes bezeugen, daß nämlich diese Menschen durch ihre eigentümliche Anlage nur in der Lage wären, alles, was Luzifer ihnen geben kann, ins Böse zu verwandeln. Die Anschauungen, die man auf dieser Insel über Luzifer haben würde, wären nur charakteristisch für die Menschen auf dieser Insel, nimmermehr für Luzifer! Ich will nicht sagen, ob es diese Insel gibt. Suchen Sie sie sich selber in der Weltenentwickelung auf.",
      "Was das Luziferische ist, das müssen wir also suchen in dem Wesen, das uns als Luzifer in der übersinnlichen Welt entgegentritt.",
      "Wie Luzifer wirkt, müssen wir in der Modifikation suchen, welche seine Kräfte annehmen, wenn sie zum Beispiel auf eine solche Insel wirken, in einer solchen Insel ihre Wirkungsstrahlen betätigen.",
      "Ahrimanisch - was ist denn das nun? Wenn wir Ahriman gegenübertreten in der übersinnlichen Welt, ist es anders mit seiner Eigenart als mit der Luzifers. Um zu Luzifer in der übersinnlichen Welt in ein Verhältnis zu kommen, braucht man sich im Grunde nur von allen Schlacken unrichtiger Egoität geläutert und gereinigt zu haben, von allen Egoismen im Sinnensein, dann wird einem LUzifer ein sehr guter Führer gerade in den übersinnlichen Welten sein, man wird ihm sozusagen nicht leicht verfallen können.",
      "Mit Ahriman steht die Sache anders. Ahriman hat in der Weltenevolution eine an- dere Aufgabe. Während Luzifer alles Unoffenbare offenbar werden läßt, hat Ahriman die Aufgabe, die sich für unsere Sinneswelt etwa so charakterisieren läßt, daß man sagt: wo unsere Sinneswelt ist, wo sie sichtbar werden kann, da ist auch Ahriman.",
      "Nur ist er die Sinnes- weIt unsichtbar, übersinnlich durchdringend. Wozu hilft Ahriman? Innerhalb der Sinneswelt hilft er gar sehr, er hilft jeder Seele. Er hilft jeder Seele nämlich dazu, daß möglichst viel aus der Sinneswelt, was sich dort abspielt und sich nur innerhalb der Sinneswelt abspielen kann, hinaUfgetragen wird in die höheren Welten.",
      "Die Sinneswelt ist ja zu etwas da, sie ist nicht bloß eine Maja. Sie ist dazu da, daß sich auf ihr Ereignisse abspielen, daß die Wesenheiten Erlebnisse haben. Was sich abspielt, was erlebt wird, das muß hinaufgetragen werden in die übersinnliche Welt.",
      "Und die Kraft, um das Wertvolle aus der Sinneswelt in die Ewigkeiten hinaufzutragen, ist die Kraft Ahrimans. Den Augenblick der Ewigkeit wieder zurückzugeben, das ist die Kraft Ahrimans. Hier aber macht sich dem Ahriman gegenüber etwas ganz anderes geltend für die einzelne Menschenseele.",
      "Was die Menschen zunächst im Sinnensein erleben, ist ihnen unendlich wertvoll, und ich glaube nicht, daß ich auf viel Widerspruch stoße, wenn ich sage: die Leidenschaft, der Hang, dasjenige, was man im Sinnensein erlebt, ja recht gut zu bewahren, womöglich viel davon für die Ewigkeiten aufzusparen, ist im allgemeinen viel größer als der andere Hang, möglichst viel aus den unoffenbarten Welten,",
      "aus den geistigen Welten hinunterzutragen in die Sinneswelt. Der Mensch liebt das Sinnensein auf eine ganz natürliche, begreifliche Weise und möchte möglichst viel daraus in die geistige Welt hinauf- tragen.",
      "Gewisse Konfessionen sagen ihren Leuten, um sie möglichst zu beruhigen, daß man alles, was in der Sinneswelt ist, hübsch mitnehmen kann in das geistige Dasein. Sie sagen es wohl, weil sie unbewußt wissen, wie der Mensch liebt, was er im Sinnensein hat.",
      "Und danach trachtet des Ahriman Kraft, daß alles, was man da hat, auch mit einem hinaufsteige in die übersinnlichen Welten. Dieser Hang, dieser Trieb, das Sinnliche in die Übersinnliche Welt hinaufzutragen, ist stark, ist kraftvoll in der Seele.",
      "Das bekommt man nicht so leicht los, wenn man aus der Sinneswelt durch die Initiation oder durch den Tod hinaufsteigt in die höheren Welten. Daher hat man es in sich, wenn man ein Wesen der höheren Welt geworden ist.",
      "Und begegnet man dort dem Ahriman, so ist er gerade gefährlich in den höheren Welten, weil er einem hilft - was er so gern tut - das, was man im Sinnensein gewonnen und erfahren hat, in die übersinnliche Welt hinaufzutragen. Keinen lieberen Genossen als Ahriman gibt es für die, welche jeden Augenblick bewahren möchten für die Ewigkeit.",
      "Viele Menschen beginnen recht sehr, sobald sie die Pforte zur übersinnlichen Welt überschritten haben, Ahriman als einen sehr bequemen Genossen zu empfinden, denn er ist immer bestrebt, was sich auf der Erde abspielt, zu Anteilen der höheren Welt zu machen und es dort für sich und für seine Wirkungsgenossen in Anspruch zu nehmen. Aber das Schlimmste ist es noch nicht, denn man kommt ja nicht in die übersinnliche Welt hinein, wenn man nicht in einer gewissen Beziehung die Egoität abgestreift hat.",
      "Würde man mit der gewöhnlichen normalen Triebkraft hineingelassen werden in die übersinnlichen Welten, dann würde man sehr bald den Ahriman am Rockzipfel fassen und ihn als einen sehr bequemen Gesellen empfinden. Aber man kann nicht hinein, wenn man so ist.",
      "Indem man hineinkommt, hat man eben schon die Eigenschaft, ihn ein wenig göttlich zu erkennen, indem er - mit einer ungeheuren Tragik - die Erdenevolution gerade im Sinnensein durchdringt und immer bestrebt ist, das Sinnensein so umzugestalten, daß es ein Geistessein",
      "werde. Das ist die tiefe Tragik des Ahriman! Er möchte alles, was irgendwie jemals im Sinnlichen erschienen ist, unmittelbar in ein Geistiges umwandeln, und er kämpft in der Weitenordnung für die Läuterung und Reinigung, für das Durch-das-Feuer-Gehen alles Sinnlichen. Das ist in seinem Sinne gut. Aber es wäre sehr schlimm im Sinne der göttlich-geistigen Wesenheiten, deren Gegner Ahriman in der Weltenordnung ist, wenn er alle seine Absichten ausführen könnte. Da muß vieles anders behandelt werden, als er möchte.",
      "In einem Vergleich möchte ich mich darüber aussprechen. Aber indem Sie den Vergleich anwenden auf die ganze WeltenordnUng, werden Sie empfinden können, wie Ahriman für sich das, was er gut nennen kann, anstrebt, wie es aber unmöglich ist, dieses Gute in sei",
      "ner Gesamtheit der Weltenordnung einzufügen. Nehmen Sie irgendein tierisches Wesen, das zu seiner fortschreitenden Entwickelung im Sinnensein sich häuten muß, das von Zeit zu Zeit die Haut ablegen muß wie ein Abbild seiner selbst und in einer neuen Daseinsform weiter fortschreiten muß. Da muß etwas abgestreift werden zu",
      "einer neuen Daseinsmöglichkeit des betreffenden Wesens. Ahriman möchte alles retten, möchte keine Schlange sich häuten lassen, sondern alles verarbeiten, was da im Sinne der Weltenordnung abgestreift werden muß. Aber der Mensch möchte das auch im Sinnen- sein; er möchte vieles nicht lassen, sondern es mitnehmen, trotzdem es im Sinne einer höheren Weltenordnung für das Zeitliche, für den Augenblick bestimmt ist. Und wenn der Mensch es könnte, so würde er - weil der Hang dazu in ihm so stark ist - im SinnenseIn im- merdar unter all den Fragen, die er nach unbekannten oder sonstigen Wegen stellt, am meisten sich erkundigen: Wo findet man Ahriman, wo kann einem Ahriman wieder helfen, um das, was der Augenblick enthält, in die Ewigkeit hinaufzutragen? Da ist es das eine Gute, daß der Mensch in der Sinneswelt nicht Ahriman finden kann, weil er unsichtbar, übersinnlich in ihr ist. Und dies gehört zu den Obliegenheiten des Hüters der Schwelle, daß Ahriman möglichst stark unsichtbar in der sinnlichen Welt bleibt, so daß der Mensch nur das, was in seinen eigenen Kräften liegt, zur Bewahrung des Augenblickes in der Ewigkeit entfalten kann und sich nicht unbewußterweise",
      "von Ahriman helfen lassen kann. Gutes und Schlimmes spielen da wieder als zwei Pole in das Sinnensein des Menschen herein. Der Mensch schreitet als Seele durch die Menschheitsevolution. Eine Aufgabe innerhalb derselben, die gut und echt und wahr ist, ist diejenige, alles, was Ewigkeitswert hat, hinauszutragen aus der Sinneswelt und einzuverleiben dem Reiche der Ewigkeit. Das ist es ja gerade, was uns obliegt: die wertvollen Schätze der Augenblicke zu nehmen und hinzuopfern am Altare der Ewigkeit. Wenn wir uns für die wertvollen Schätze der Zeitlichkeit von Ahriman helfen lassen, so ist das gut. Wenn wir Ahriman in dem Augenblicke, wo wir die übersinnliche Welt betreten - vorher können wir ihn ja nicht sehen -, kennenlernen und ihm den Hang zeigen, der uns noch verblieben sein kann, auch Wertloses aus der Sinnes- weIt hinaufzutragen in die übersinnliche Welt, dann ist das ja für ihn ein Wertvolles - für seine Gegner ist es ein Wertloses. Da sind wir gute Werkzeuge für ihn, um aus der Sinneswelt in die Ewigkeit überzuleiten, was hier geliebt wird, und was dadurch, daß es von uns geliebt wird, auch seinerseits in diese Ewigkeit hineingestellt wird.",
      "So sehen wir wieder, wie das, was von Ahriman ausgeht, absolut - an sich - nicht gut und nicht böse genannt werden darf, sondern wie es gut oder böse wird je nachdem, wie sich der Mensch ihm unterstellt, je nachdem, wie der Mensch mit ihm in ein Verhältnis tritt. Daraus sehen wir aber überhaupt, wie oberflächlich leicht Beschreibungen werden können, welche den bequemen Fragen dienen möchten: wie ist Ahriman, wie ist Luzifer? Sprache, Antworten auf solche Fragen gibt es im Grunde genommen nicht in denjenigen Welten, wo solche Wesenheiten allein charakterisiert werden sollen: in den höheren Welten. So ist der Mensch eingesponnen in das Lebenslabyrinth. Sowohl Ahriman wie Luzifer wirken in das Lebenslabyrinth herein, und der Mensch hat den Weg zu suchen, um sich in der richtigen Weise zu solchen Mächten zu stellen. Das macht es gerade, daß wir uns entwickeln können, weil wir dadurch zu den Wesen der übersinnlichen Welten Verhältnisse suchen müssen. Und die Beziehungen zu der übersinnlichen Welt werden weniger durch",
      "eine nach dem Muster der Sinneserkenntnis angestrebte Erkenntnis erhalten, als dadurch, daß man sich im Sinne des Charakterisierten Beziehungen verschafft zu diesen übersinnlichen` Wesenheiten. Deshalb muß der Mensch im Lebensdunkel sein, denn in dasselbe spielen die Wesenheiten herein, welche sowohl gut wie böse sein können, und gut oder böse in ihren Wirkungen werden können, je nachdem wir uns zu ihnen stellen. Das macht das Lebensdunkel aus. Das bewirkt es, daß Lebenslicht, Geisteslicht in dieses Lebensdunkel nur dadurch hereinleuchtet, daß wir zu den einzelnen Mächten der übersinnlichen Welt, die in unsere physische Welt hereinspielen, die richtigen Verhältnisse gewinnen, daß wir uns damit bekannt machen, daß sich unsere Vorstellungen und Begriffe wandeln müssen, wenn wir von den übersinnlichen Welten sprechen wollen. An einem anderen Beispiele möchte ich Ihnen noch vor die Seele führen, wie wir anders denken müssen, wenn wir die Beziehungen der Sinneswelt zu dem Übersinnlichen richtig finden wollen.",
      "Da leben wir im Sinnensein, leben so, daß wir um uns und mit uns spielen fühlen das, was wir unser Lebensschicksal nennen. Da ist uns manches sympathisch, manches antipathisch an diesem Leben& schicksal. Und wer eine richtige Selbstbesinnung sich verschaffen kann, der weiß, daß Mitfühlen und Mitempfinden, Sympathie und Anüpathie haben mit den Geschicken des Lebens zu den stärksten Empfindungen gehört, die wir überhaupt haben können, die sich am tiefsten in die Seele eingraben. Nun geht es aber so - warum, brauche ich hier nicht zu wiederholen, weil es in den anfänglichen Vorträgen so oft gesagt wird -, daß wir es in unserem übergeordneten Ich, das sich im Sinne des gestrigen und vorgestrigen Vortrages an das gewöhnliche Ich nur erinnert, es nur wie eine Erinnerung in sich hat, selber sind, die sich zum Beispiel auch dasjenige Schicksal, das uns dann vielleicht ein ganzes Leben hindurch martert und peinigt, zubereiten. Gibt es nicht Menschen, welche die Reinkarnationsidee gerade deshalb ableugnen, weil sie kein Begehren haben, ein neues Dasein sich zurechtzuzimmern, nachdem sie dieses eine durchlebt haben? Warum denken solche Menschen so? Weil sie in dem Glauben befangen sind, daß es in den Welten, in denen der",
      "Mensch nach dem Tode ist, ebenso zugehe wie in der Sinneswelt. Hier kann uns manches gefallen, manches mißfallen. Aber so zu empfinden wie hier, fällt uns gar nicht ein, wenn wir in dem Leben zwischen Tod und neuer Geburt sind.",
      "Dort empfinden wir ganz anders, wenn wir auch hier nichts davon wissen. Wenn wir nach dem Tode in die geistige Welt kommen, dann sehen wir zum Beispiel: Du hast gelebt auf der Erde in einem Sinnensein, du hast eine bestimmte Fähigkeit gehabt, aber diese Fähigkeit kam sehr einseitig bei dir heraus, du hast sie vielleicht auch mißbraucht.",
      "Du mußt jetzt in einem neuen Erdensein in einer anderen Körperlichkeit dich so ausgestalten, daß das Einseitige ausgeglichen wird und daß eine Unvollkommenheit vollkommener werde. Du mußt - mit anderen Worten - das, was du in unvollkommener Gestalt an dir gehabt hast, in einer anderen Unvollkommenheit dir aneignen, damit durch das gegenseitige Wirken die Sache ausgeglichen und harmonisiert werde.",
      "Da beginnt dann eine Zeit beim Durchgang zwischen Tod und neuer Geburt bis zur neuen Geburt hin, wo sich der Mensch sagt: Ich will so geboren werden, daß ich in einem neuen Leben ganz unfähig bin - beispielsweise -, mich in der Malerei zu betätigen, weil ich mich vorher darin betätigt habe und großes Geschick dabei gehabt habe. Denn dadurch, daß ich nun in der Malerei ungeschickt sein werde, werde ich in die Lage kommen, nie ein Urteil in meine Seele einfließen zu lassen, wie wenn ich selber male, sondern nur so, wie es sein muß, wenn ich mich selber vor die Sache stellen muß.",
      "Da werde ich mir andere Kräfte aneignen müssen, weil das heilsam sein kann, um das, was ich früher gehabt habe, zu harmonisieren, auszugleichen. So kann man zurückschauen auf ein Leben zwischen Geburt und Tod, auf etwas, was man glücklich durchlaufen hat, sagt sich aber, wenn man seine gesamte Evolution nur so einrichten würde, daß man sein Leben so erlebt, so hätte man es nicht ausgekostet.",
      "Was erfolgen muß aus Kräften, die gerade in dieser Weise sich ergeben, ist daher die Begierde: was du vorher im Glück erlebt hast, das mußt du jetzt im Leid erleben. Und man richtet nun alles so ein, daß man aus einer Sehnsucht heraus auf einem bestimmten Gebiete Leiden erleben muß, deren Durchmachen einen",
      "wieder weiterbringt im Dasein. Dann liegt die Tatsache vor, daß man im Übersinnlichen verlangt hat nach Leiden und Schmerzen und sie im Sinnensein als etwas empfindet, was inan wegtun möchte. Da wird wahrhaftig der Unterschied zwischen dem Leben im Sinnensein und dem Leben in den übersinnlichen Welten zwischen Tod und neuer Geburt praktisch bedeutsam.",
      "Ganz andere Kräfte wirken in unserem Leben zwischen Tod und neuer Geburt, als uns dann sympathisch oder unsympathisch sind im Leben zwischen Geburt und Tod. Was tut nun der, welcher etwa das Leben in den über- sinnlichen Welten beurteilen würde nach seinen Sympathien und Antipathien im Sinnensein?",
      "Er verpflanzt das, was er im Sinnensein hat, perspektivisch hinein in die übersinnliche Welt. Es ist richtig so, wie wenn Sie auf irgendeine Glastafel aufzeichnen oder aufmalen zum Beispiel eine Rose; dann schauen Sie die Glastafel an, das Glas sehen Sie nicht - Sie schauen durch das Glas durch, aber die Malerei projiziert sich hinten auf eine Riesenwand, und Sie glauben, das ist wirklich.",
      "Es ist aber gar nicht wirklich, sondern Sie haben es nur dort hinausversetzt. In dieser Weise kann der Mensch, wenn er die übersinnliche Welt beurteilen will nach Sympathien und Antipathien im Sinnensein, in die übersinnliche Welt etwas hineinprojizieren wie Schatten, was dann im Übersinnlichen auch eine Gültigkeit haben kann.",
      "Es hat schon eine Wirkung, eine Gültigkeit. Wenn man es nicht sieht, projiziert sich etwas wie ein Nebel auf das, was da drinnen vor dem Betrachter steht.",
      "Das kann uns - wieder von einer anderen Seite her - empfindungsgemäß hinweisen auf das, was wir das Lebensdunkel nennen können. Warum leben wir im Lebensdunkel zwischen Geburt und Tod? Weil berechtigt und selbstverständlich für das Leben zwischen Geburt und Tod Urteile, Wertungen des Lebens sind, die ungültig sein müssen für dasjenige Dasein, das wir selbst verbringen zwischen dem Tode und einer neuen Geburt. Wir brauchen für das Sinnen- sein ein Seelenleben, das keine Gültigkeit für die übersinnliche Welt hat. Wir müssen daher durch die Erkenntnisse, durch dasjenige, was erforscht werden kann in den übersinnlichen Welten, hereinleuchten lassen das Geisteslicht aus den übersinnlichen Welten, damit wir",
      "zu einer Gesamterfassung der Welt kommen. Der größte Fehler, den die Menschen in bezug auf Weltanschauungen machen können, ist der, wenn sie glauben, das, was sie gewonnen haben an Begriffen und Ideen in der Sinneswelt, ausdehnen zu können auf die übersinnliche Welt, wenn sie nicht die Geduld und Ausdauer haben, aus der wirklichen Erforschung des Übersinnlichen heraus sich die Beschreibungen geben zu lassen von demjenigen, was als Geisteslicht aus den übersinnlichen Welten hereinleuchtet in das Lebensdunkel des Sinnenseins. Hier stehen wir allerdings vor der Frage: Ist dann",
      "nur derjenige imstande, dieses Geisteslicht der übersinnlichen Welten auf sich wirken zu lassen, der selber schauen kann in den über- sinnlichen Welten, der also die Initiation genossen hat? - Dieser Glaube ist vielfach in der Welt verbreitet. Vielfach hört man sagen: Wie kann man etwas von den übersinnlichen Welten begreifen, wenn man nicht selber die Initiation durchgemacht hat? Und man hört dann darauf hinweisen, wie das einzig Wahre nur das Durchmachen der Schritte zur Initiation sein kann, das eigentliche Hinauf- steigen in die übersinnliche Welt.",
      "Wie es sich auf diesem Gebiete verhält, wie Begreifen zum Schauen steht in den übersinnlichen Welten, wieviel man von Lebenstrost und Lebenskraft durch das Begreifen des Geisteslichtes im Lebens- dunkel haben kann, das soll der Ausgangspunkt sein für die morgige Betrachtung, die uns noch einige Schritte weiter in die Probleme, die wir in diesem Zyklus betrachten wollen, hineinführen soll."
    ],
    "sentences": [
      [
        "Aus den bisher gehaltenen Vorträgen wird Ihnen vielleicht ersichtlich geworden sein, wie nötig es ist, seine Vorstellungen beweglich, wandelbar zu machen, wenn eine richtige Charakteristik von den verschiedenen Welten, von denen man sprechen kann und von denen das Sinnensein, unsere gewöhnliche Sinneswelt doch nur die eine ist, entgegengenommen werden soll.",
        "Aus vielem Gesagten kann Ihnen hervorgehen, daß man geradezu eine andere Sprache menschlicher Vorstellungen sprechen muß, wenn man von der einen Welt in die andere den Übergang herbeiführen will."
      ],
      [
        "Das ist die eine Seite der Sache.",
        "Aber es gibt eine andere Seite der Sache: daß alle diese Welten wieder zusammenwirken und daß in der einen Welt immer gewissermaßen der Abglanz, die Hineinwirkungen der übrigen Welten wahrzunehmen sind."
      ],
      [
        "In jeder Welt hat man es damit zu tun, daß einem die Erscheinungen und Wesenheiten dieser Welt selbst entgegentreten und dann wieder alles dasjenige, was von den anderen Welten in diese besondere Welt hineinwirkt.",
        "Dieses alles muß sorgfältig berücksichtigt werden, wenn man verstehen will, was die Geheimnisse der Initiation sind, welches die Beziehungen des Augenblickes zur Ewigkeit, des Lebensdunkels zum Geisteslichte sind."
      ],
      [
        "Es gibt - wie Sie dargestellt finden in «Wie erlangt man Erkenntnisse der höheren Welten?» - gewisse Regeln, gewisse Anweisungen, welchen sich die Seele unterwerfen kann, um den Aufstieg in die über- sinnlichen Welten zu bewirken.",
        "Solche Regeln sind selbstverständlich nicht nur nützlich, sondern demjenigen unentbehrlich, der wirklich die ersten oder die weiteren Schritte der Initiation unternehmen will."
      ],
      [
        "Aber insbesondere in unserer Zeit muß auf eines aufmerksam gemacht werden."
      ],
      [
        "Unsere Zeit hat eine gewisse Eigentümlichkeit, die zusammenhängt mit der ganzen Eigenart des Weltenzyklus, in dem wir leben; unsere Zeit hat etwas Lehrhaftes, etwas Theoretisierendes.",
        "Und wie sehr man sich auch bemüht, da oder dort den Hang zum Theoretisieren"
      ],
      [
        "abzulegen, er sitzt gewissermaßen doch dem Menschen der Gegenwart in den Seelengründen.",
        "Das bewirkt, daß diese Menschen der Gegenwart, wenn es sich um den Aufstieg zu den höheren Welten handelt, zunächst vor allen Dingen erwarten, daß ihnen unter allen Umständen gesagt werde, wie sich jeder einzelne verhalten solle, wenn die Seele in die höheren Welten hinaufgelangen will."
      ],
      [
        "GegenÜber dem wirklichen Erleben des Übersinnlichen stellt sich aber doch etwas ein, was man in gewisser Beziehung mißlich nennen möchte in all denjenigen Darstellungen, welche - man möchte sagen - einen normalen Weg, eine normale Marschroute angeben, um in die höheren Welten hinaufzueilen.",
        "Denn das Leben ist etwas Kompliziertes."
      ],
      [
        "Und jede Seele in irgendeiner Lebenslage, in der sie sich befindet - und jedesmal muß man von einer bestimmten Lebenslage ausgehen, wenn man den Aufstieg in die höheren Welten unternehmen will -, steht in einem bestimmten Karma drinnen, hat einen bestimmten Ausgangspunkt.",
        "Keine Seele ist in derselben Lage wie die andere."
      ],
      [
        "Daher ist im Grunde genommen auch der Weg in die übersinnlichen Welten hinauf für jede Seele ein individueller, ein solcher, welcher sich je nach der betreffenden Seele beim Ausgangspunkt richtet.",
        "Man kann nicht sagen, wenn man im richtigen Sinne sprechen will: so muß nach einem normalen Prinzip unmittelbar jede Seele den Aufstieg in die höheren Welten, die Initiation,`durchmachen."
      ],
      [
        "Daher das Bedürfnis, nicht nur in kurzen Broschüren oder dergleichen - was ja leichter wäre - Anweisungen zu geben: so und so soll es die Seele machen, um den Glauben zu erwecken, man könne, wenn man solche Regeln befolgt, unter allen Umständen in der gleichen Art wie jede andere Seele in die höheren Welten hinaufsteigen.",
        "Daher das Mißliche solcher Dinge."
      ],
      [
        "Deshalb namentlich habe ich versucht, in dem Büchelchen «Ein Weg zur Selbsterkenntnis des Menschen» etwas zu zeigen, was individuell ist und doch einer jeden Seele nützlich sein kann.",
        "Aber deshalb ergab sich auch die Notwendigkeit, die Mannigfaltigkeit und die Variabilität des Initiationsweges zu zeigen."
      ],
      [
        "Und ohne selbst etwa irgendwie Erklärungen liefern zu wollen über das, was getan worden ist, möchte ich Sie nur darauf hinweisen, wie sich die Notwendigkeiten zu den drei Gestalten ergeben,"
      ],
      [
        "welche in den drei Mysterienversuchen - «Die Pforte der Einweihung», «Die Prüfung der Seele» und «Der Hüter der Schwelle» - vor Ihre Seele hintreten als Johannes Thomasius, Capesius und Strader.",
        "Sie zeigen Ihnen den Weg der ersten Schritte zur Initiation gleichsam in drei verschiedenen Aspekten."
      ],
      [
        "Man kann von keinem dieser Wege sagen, daß er besser oder schlechter sei als der Weg des anderen; sondern man muß von jedem dieser Wege sagen, daß er sich ergeben mußte je nach dem Karma der betreffenden Individualitäten.",
        "Man kann nur sagen: eine Seele, welche so ist wie Johannes Thomasius, oder welche so ist wie Capesius, muß eben solche Wege gehen, wie sie versucht worden sind, nicht in Theorien, nicht lehrhaft, sondern in Gestalten zu zeigen."
      ],
      [
        "Daher das Bedürfnis, solche Gestalten zu zeigen.",
        "Und immer notwendiger und notwendiger wird es werden, hinwegzuführen von dem Glauben, daß man mit ein paar Regeln in diesen Dingen auskomme, immer notwendiger wird es sein, gerade auf spirituellem Gebiete von dem Lehrhaften auf das Gestaltete hinzuweisen."
      ],
      [
        "Weil die Beziehungen der Welten so mannigfaltige sind, deshalb müssen auch die Wege der einzelnen Individualitäten so mann1gfaltige sein.",
        "Wenn man aber erst dazu kommt, gewisse Individualitäten oder Wesenheiten der höheren Welten ernsthaft ins Auge zu fassen und deren Anteil an dem Menschen zu prüfen, dann muß man erst recht die Notwendigkeit fühlen, diese Gestalten lebendig zu zeigen, sie in ihrer Mannigfaltigkeit hinzustellen, nicht bloß Definitionen von ihnen zu geben."
      ],
      [
        "In unserer Zeit ist es insbesondere für diejenigen, die spirituelle Erkenntnis anstreben, wichtig, solche Gestalten wie Luzifer und Ahriman, denen man auf dem Wege zur Initiation ja immer begegnet, einmal gerade in ihrer Vielartigkeit, in ihrer Variabilität ins Auge zu fassen.",
        "Dann wird sich zeigen, wie merkwürdig die Beziehungen und Verkettungen der einen Welt mit der anderen sind."
      ],
      [
        "Es zeigt sich an vielen Zeichen unserer Zeit, daß allmählich Verständnis wachgerufen werden kann für das Hereinspielen der einen Welt in die andere.",
        "Ich möchte da zunächst von etwas Naheliegendem ausgehen, das nur nicht immer naheliegend genug empfunden wird."
      ],
      [
        "In unserer Zeit besteht in den weitesten Kreisen das lebhafteste Bedürfnis, die Naturordnung, die Naturgesetze kennenzulernen, die durch alles - auch durch alles Wesenhafte - hindurchwirken, das uns im Sinnensein entgegentritt.",
        "Und es besteht der Hang, nicht zu achten auf alles, was etwa von anderen Welten her über den Menschen und das Weltendasein gesagt werden kann, sondern nur sozusagen aus der einen Welt heraus eine gesamte Weltanschauung aufzubauen.",
        "Das gibt ja die mehr oder weniger monistischen oder auch als materialistisch bezeichneten Weltanschauungen der Gegenwart.",
        "Man möchte sagen, gleichsam wie ein wohltätiger Gegenschlag gegen dieses Bestreben haben sich in unserer Zeit andere Bestrebungen geltend gemacht, welche innerhalb der Welt, in der wir leben, solche Erscheinungen aufsuchen, welche von anderen Gesetzen beherrscht sind als die Welt der Naturordnung, diejenigen Erscheinungen in ihrer Mannigfaltigkeit aufsuchen, welche als widersprechend dieser Naturordnung von dem materialistischen Sinn empfunden werden."
      ],
      [
        "Man sollte wohl achten auf alles, was im Sinne ernster Wissenschaftlichkeit auf diesem Gebiete gearbeitet wird.",
        "Denn indem in unserer Zeit dem rein materialistischen Forschen - wenn auch wenig beachtet - ein anderes Forschen entgegentritt, welches andere Zusammenhänge in unserem Sinnensein sucht, als das Sinnensein selber darbietet, wird ja nichts Geringeres getan, als das Hereinspielen ganz anderer Welten mit anderen Daseinsgesetzen schon innerhalb der Forschungsmethoden des Sinnenseins selbst zu suchen.",
        "In dieser Beziehung ist es außerordentlich wünschenswert, daß namentlich der Theosoph immer darauf achten sollte, was in dieser Richtung geleistet wird - geleistet wird, indem die wissenschaftlichen Methoden ausgedehnt werden auf das Hereinspielen übersinnlicher Welten in unser Sinnensein.",
        "Für kleinere Kreise habe ich schon darauf hingewiesen; für diesen größeren Kreis will ich es heute tun."
      ],
      [
        "In seinem Buche «Das Mysterium des Menschen», das ich Ihnen ganz besonders-empfehlen möchte, hat unser lieber Freund Ludwig Deinhard sich der dankenswerten Aufgabe unterzogen, in dem ersten Teil eine sehr übersichtliche Zusammenstellung und Charakterisierung alles dessen zu bringen, was in unserer Zeit mit den wissenschaftlichen"
      ],
      [
        "Methoden, die heute anerkannt sind - aber so, wie sie angewendet sind, eben noch mit Vorurteil angewendet werden -, innerhalb der Welt, die jeder betreten kann, untersucht werden kann über das Hereinspielen einer übersinnlichen Welt.",
        "Dies einmal übersichtlich vor sich zu haben, ist eine dankenswerte Aufgabe gewesen, und ist etwas, was jeder kennenlernen sollte, der sich gerade von diesem Gesichtspunkt aus dafür interessiert, wie man auf Schritt und Tritt, wenn man nur die Tatsachen nimmt, das Herausspringen des Übersinnlichen aus dem Sinnensein finden kann.",
        "So sehen wir also gerade mit einer wichtigen Aufgabe dieses Buch in der letzten Zeit unter uns, und ich darf wohl auch hier an diesem Orte auf dieses Buch «Das Mysterium des Menschen» von Ludwig Deinhard hinweisen."
      ],
      [
        "Dieses Hereinspielen anderer Welten in die Sinneswelt erzeugt innerhalb der letzteren etwas, was sich nun in allen Welten wiederholt, was in allen Welten auftritt, was aber ganz besonders notwendig macht, daß wir uns bekannt machen mit der Notwendigkeit, nicht pedantisch, einseitig, streng geformt uns Dogmen oder Urteile zu bilden dahin lautend: dieses sei so, jenes so, Luzifer so, Ahriman so, Luziferisches müsse man fliehen, Ahrimanisches müsse man fliehen oder dergleichen.",
        "Eingelaufen ist unsere gestrige Betrachtung gerade in solche Dinge."
      ],
      [
        "Nehmen wir an, derjenige, der die ersten Schritte auf dem Wege zur Initiation durchgemacht hat, begegnet, weil er in seinem Seelen- leben durch das Sich-Öffnen der Seelenaugen hellseherisch geworden ist, jener Gestalt, die wir als Luzifer in den übersinnlichen Welten bezeichnen.",
        "Als was konnten wir gestern diese Gestalt bezeichnen?",
        "Sie tritt der Seele als das entgegen, was immerzu bestrebt ist, das Ewige, das sonst in immerwährender Beweglichkeit und Veränderlichkeit ist, zur Beständigkeit, zum Zeitlichen, zum Augenblicklichen zu machen, so daß es als Individuelles sich erfreuen, groß werden könne.",
        "Und tritt man als Seele Luzifer in den übersinnlichen Welten entgegen, so erscheint er dort als der große Lichtträger, welcher einen gleichsam dazu führt - ja, wahrhaftig dazu führt, alle die Schätze, all das Wesenhafte, das da in den spirituellen Welten ist,"
      ],
      [
        "herunterzutragen in die Sinneswelt und in der Sinneswelt davon Abglanz und Offenbarung zu schaffen.",
        "Und folgt man Luzifer in den übersinnlichen Welten in diesem seinem Bestreben, dann wirkt man dazu, daß die urewige Weltaufgabe erfüllt werde, daß alles Unoffenbare offenbar werde, daß alles Ewige dem Augenblicke anvertraut werde, daß alles, was verfließt im unbestimmten Ewigen, in der innerlichen Größe des individuellen Augenblickes festgehalten werden könne."
      ],
      [
        "Nun sitzt es in jeder Menschenseele wie ein Nachklang aus der geistigen Welt, daß dieses Streben, das Unoffenbare offenbar zu machen, das Ewige im Augenblick zu fixieren, auch wirklich geschehe.",
        "Daher ist es, wenn der Mensch entweder durch die Initiation oder durch den Tod die übersinnlichen Welten beschreitet, daß in ihm Luzifer als Lichtesträger wirklich wirkt, und die Gefahren, denen der Mensch in den höheren Welten gegenüber Luzifer ausgesetzt ist, sind nur dann eigentlich vorhanden, wenn der Mensch das, was seine Stellung innerhalb des Sinnenseins zu Luzifer ausmachen soll, in einem zu hohen Maße in die höheren Welten hinein mitbringt.",
        "Luzifer ist nur gefährlich beim Wandeln in den höheren Welten, wenn man zu sehr die Natur und Wesenhaftigkeit des Sinnesmenschen in diese höheren Welten hinein mitbringt.",
        "Aber wie steht es innerhalb des Sinnenseins selbst, da ja die übersinnlichen Welten immer ins Sinnensein hereinspielen, mit Luzifer?",
        "Denn zunächst haben wir es im historischen Gange der Menschheit im Sinnensein und seiner Evolution mit dem Hereinspielen der höheren Welten zu tun, die wirksame Impulse abgeben, damit das eine hinter dem andern im Sinnensein geschehe, wie es in der Geschichte der Menschheit durch das Erdensein hindurch sich abspielt."
      ],
      [
        "Ja, in dieses Sinnensein spielen herein diejenigen Bestrebungen, die wir als menschlich egoistische, als selbstsüchtige Bestrebungen jeder Seele betrachten.",
        "Wir wissen ja, daß jede Seelenentwickelung vom Egoismus ausgehen muß.",
        "Das ist natürlich.",
        "Wir wissen aber auch, daß wieder ein Herausarbeiten aus dem Egoismus stattfinden kann.",
        "In all das, was jemals Seelen aus dem Egoismus heraus auf der Erde haben tun können, fällt das hinein, was man nennen kann:"
      ],
      [
        "Offenbarung des Ewigen in dem Augenblick.",
        "In das, was in der individuellen Seele fixiert ist, spielen fortwährend luziferische Kräfte hinein.",
        "Aber noch in etwas anderes spielen sie hinein, nämlich in all das, was der einzelne Mensch gerade für die gesamte WeltenordnUng, für das Weltendasein dadurch tun kann, daß er eine Egoität ist und hat, daß er in sich innerliche Größe entwickeln kann, die aus seinem Innern hervorsprudelt.",
        "Was ist denn das individuelle Große in der einzelnen Seele anderes als das, was der Keim des Großen in aller Weltenentwickelung der Menschheit ist?",
        "Wodurch haben Homer, Shakespeare, Dante, Goethe auf die Menschheit gewirkt?",
        "Dadurch, daß sie Egoitäten waren, daß in ihrem Innern ganze Welten waren, Welten, die nur aus ihrem Innern, aus ihrer Egoität herausgekommen sind.",
        "Dadurch aber werden - auf dem Umwege durch die Egoitäten - die Impulse des geistigen Lebens hereingetragen, welche von Epoche zu Epoche gerade die größten, nämlich die geistigen Taten der Menschheit vermitteln.",
        "Da ist wieder Luzifer drinnen.",
        "Da ist er der Lichtträger, der Impuls und die Macht alles Großen, welches aus der großen punktuellen, aus der einzelnen Menschenseele sprudelnden Ewigkeitskraft in die Menschheitsevolution ausstrahlt."
      ],
      [
        "Zwischen zwei Pole ist die Menschenseele hereingestellt, die einfach der Abdruck und der Abglanz all der Welten sind, in denen die Menschenseele wirklich steht: daß sie sich in sich verhärtet, sich in ihrer Egoität völlig einspinnt und nur das will, was ihr selber dient, was sie selber befriedigt; und daß die Menschenseele aus ihren Tiefen heraus die Kräfte holt, die einstrahlen können in das ganze Leben der Menschheit?",
        "Wann tritt nun diese Egoität des Menschen zutage? - Gerade dann, wenn man denkt, wie notwendig es ist, daß ein jeder Mensch das Seinige, was sein Individuellstes ist, was das tiefste Eigentum seiner Egoität ist, den anderen Menschen darbringt.",
        "In allem aber, was der Mensch für den Menschen aus seiner Egoität heraus tun kann, lebt wieder Luzifer, der andere Pol des Luzifer.",
        "Und in dem, was der Mensch so unter dem Einiluß des Lichtträgers für die Menschheit leisten kann, liegt ein Abglanz dessen, was Luzifer in den höheren Welten wirklich ist, liegt ein Abglanz der schöpferischen Tätigkeit des Luzifer: das Unoffenbare zu dem Offenbaren zu"
      ],
      [
        "machen.",
        "Kann man also sagen, Luzifer sei böse, oder kann man etwa sagen, Luzifer sei gut? - Man kann nur sagen: Wer behaupten will, Luzifer sei böse und müsse geflohen werden, der müßte 'auch sagen, das Feuer müsse geflohen werden, weil das Leben unter Umständen im Feuer ersterben muß.",
        "Man findet auf dem Wege zur Initiation, daß die Ausdrücke gut und böse gar nicht in dieser Art anwendbar sind, sobald man das Wesen der übersinnlichen Weltenordnung charakterisieren will.",
        "Das Feuer ist gut, wenn es unter guten Umständen wirkt; es ist schlecht, wenn es unter schlechten Umständen wirkt; an sich ist es nicht gut und nicht schlecht.",
        "So ist es mit Luzifer.",
        "Er übt einen guten Einfluß auf die Menschenseele aus, wenn er der Anreger wird zum Herausholen alles dessen aus der Menschenseele, was der Mensch als sein Individuelles hinopfern kann am Altare der Menschheitsevolution.",
        "Luzifer wird ein böses Wesen, das heißt, was er tut, wird böse, wenn er solche Impulse der Menschenseele gibt, daß diese nur alles zur Selbstbefriedigung in sich hinein-"
      ],
      [
        "führen will.",
        "Wie die Taten der Wesen wirken in der Welt, das muß man verfolgen, wenn man auf diese Wesenheiten hingewiesen worden ist.",
        "Die Wirkungen der übersinnlichen Wesenheiten kann man bezeichnen als gute und böse; die Wesenheiten selber nimmermehr."
      ],
      [
        "Denken Sie einmal, irgendwo - verzeihen Sie das Paradoxon -, ich will nicht sagen, wo es sein könnte, nehmen Sie an, auf irgendeiner Insel sei eine Menschheit, welche die Anschauung hätte, man müsse sich vor Luzifer unter allen Umständen hüten, man müsse ihn so weit weghalten von den Menschen, als es nur irgend möglich ist."
      ],
      [
        "Das würde nicht bezeugen, daß die Menschen dieser Insel die beste Erkenntnis von Luzifer hätten, aber es würde etwas anderes bezeugen, daß nämlich diese Menschen durch ihre eigentümliche Anlage nur in der Lage wären, alles, was Luzifer ihnen geben kann, ins Böse zu verwandeln.",
        "Die Anschauungen, die man auf dieser Insel über Luzifer haben würde, wären nur charakteristisch für die Menschen auf dieser Insel, nimmermehr für Luzifer!",
        "Ich will nicht sagen, ob es diese Insel gibt.",
        "Suchen Sie sie sich selber in der Weltenentwickelung auf."
      ],
      [
        "Was das Luziferische ist, das müssen wir also suchen in dem Wesen, das uns als Luzifer in der übersinnlichen Welt entgegentritt."
      ],
      [
        "Wie Luzifer wirkt, müssen wir in der Modifikation suchen, welche seine Kräfte annehmen, wenn sie zum Beispiel auf eine solche Insel wirken, in einer solchen Insel ihre Wirkungsstrahlen betätigen."
      ],
      [
        "Ahrimanisch - was ist denn das nun?",
        "Wenn wir Ahriman gegenübertreten in der übersinnlichen Welt, ist es anders mit seiner Eigenart als mit der Luzifers.",
        "Um zu Luzifer in der übersinnlichen Welt in ein Verhältnis zu kommen, braucht man sich im Grunde nur von allen Schlacken unrichtiger Egoität geläutert und gereinigt zu haben, von allen Egoismen im Sinnensein, dann wird einem LUzifer ein sehr guter Führer gerade in den übersinnlichen Welten sein, man wird ihm sozusagen nicht leicht verfallen können."
      ],
      [
        "Mit Ahriman steht die Sache anders.",
        "Ahriman hat in der Weltenevolution eine an- dere Aufgabe.",
        "Während Luzifer alles Unoffenbare offenbar werden läßt, hat Ahriman die Aufgabe, die sich für unsere Sinneswelt etwa so charakterisieren läßt, daß man sagt: wo unsere Sinneswelt ist, wo sie sichtbar werden kann, da ist auch Ahriman."
      ],
      [
        "Nur ist er die Sinnes- weIt unsichtbar, übersinnlich durchdringend.",
        "Wozu hilft Ahriman?",
        "Innerhalb der Sinneswelt hilft er gar sehr, er hilft jeder Seele.",
        "Er hilft jeder Seele nämlich dazu, daß möglichst viel aus der Sinneswelt, was sich dort abspielt und sich nur innerhalb der Sinneswelt abspielen kann, hinaUfgetragen wird in die höheren Welten."
      ],
      [
        "Die Sinneswelt ist ja zu etwas da, sie ist nicht bloß eine Maja.",
        "Sie ist dazu da, daß sich auf ihr Ereignisse abspielen, daß die Wesenheiten Erlebnisse haben.",
        "Was sich abspielt, was erlebt wird, das muß hinaufgetragen werden in die übersinnliche Welt."
      ],
      [
        "Und die Kraft, um das Wertvolle aus der Sinneswelt in die Ewigkeiten hinaufzutragen, ist die Kraft Ahrimans.",
        "Den Augenblick der Ewigkeit wieder zurückzugeben, das ist die Kraft Ahrimans.",
        "Hier aber macht sich dem Ahriman gegenüber etwas ganz anderes geltend für die einzelne Menschenseele."
      ],
      [
        "Was die Menschen zunächst im Sinnensein erleben, ist ihnen unendlich wertvoll, und ich glaube nicht, daß ich auf viel Widerspruch stoße, wenn ich sage: die Leidenschaft, der Hang, dasjenige, was man im Sinnensein erlebt, ja recht gut zu bewahren, womöglich viel davon für die Ewigkeiten aufzusparen, ist im allgemeinen viel größer als der andere Hang, möglichst viel aus den unoffenbarten Welten,"
      ],
      [
        "aus den geistigen Welten hinunterzutragen in die Sinneswelt.",
        "Der Mensch liebt das Sinnensein auf eine ganz natürliche, begreifliche Weise und möchte möglichst viel daraus in die geistige Welt hinauf- tragen."
      ],
      [
        "Gewisse Konfessionen sagen ihren Leuten, um sie möglichst zu beruhigen, daß man alles, was in der Sinneswelt ist, hübsch mitnehmen kann in das geistige Dasein.",
        "Sie sagen es wohl, weil sie unbewußt wissen, wie der Mensch liebt, was er im Sinnensein hat."
      ],
      [
        "Und danach trachtet des Ahriman Kraft, daß alles, was man da hat, auch mit einem hinaufsteige in die übersinnlichen Welten.",
        "Dieser Hang, dieser Trieb, das Sinnliche in die Übersinnliche Welt hinaufzutragen, ist stark, ist kraftvoll in der Seele."
      ],
      [
        "Das bekommt man nicht so leicht los, wenn man aus der Sinneswelt durch die Initiation oder durch den Tod hinaufsteigt in die höheren Welten.",
        "Daher hat man es in sich, wenn man ein Wesen der höheren Welt geworden ist."
      ],
      [
        "Und begegnet man dort dem Ahriman, so ist er gerade gefährlich in den höheren Welten, weil er einem hilft - was er so gern tut - das, was man im Sinnensein gewonnen und erfahren hat, in die übersinnliche Welt hinaufzutragen.",
        "Keinen lieberen Genossen als Ahriman gibt es für die, welche jeden Augenblick bewahren möchten für die Ewigkeit."
      ],
      [
        "Viele Menschen beginnen recht sehr, sobald sie die Pforte zur übersinnlichen Welt überschritten haben, Ahriman als einen sehr bequemen Genossen zu empfinden, denn er ist immer bestrebt, was sich auf der Erde abspielt, zu Anteilen der höheren Welt zu machen und es dort für sich und für seine Wirkungsgenossen in Anspruch zu nehmen.",
        "Aber das Schlimmste ist es noch nicht, denn man kommt ja nicht in die übersinnliche Welt hinein, wenn man nicht in einer gewissen Beziehung die Egoität abgestreift hat."
      ],
      [
        "Würde man mit der gewöhnlichen normalen Triebkraft hineingelassen werden in die übersinnlichen Welten, dann würde man sehr bald den Ahriman am Rockzipfel fassen und ihn als einen sehr bequemen Gesellen empfinden.",
        "Aber man kann nicht hinein, wenn man so ist."
      ],
      [
        "Indem man hineinkommt, hat man eben schon die Eigenschaft, ihn ein wenig göttlich zu erkennen, indem er - mit einer ungeheuren Tragik - die Erdenevolution gerade im Sinnensein durchdringt und immer bestrebt ist, das Sinnensein so umzugestalten, daß es ein Geistessein"
      ],
      [
        "werde.",
        "Das ist die tiefe Tragik des Ahriman!",
        "Er möchte alles, was irgendwie jemals im Sinnlichen erschienen ist, unmittelbar in ein Geistiges umwandeln, und er kämpft in der Weitenordnung für die Läuterung und Reinigung, für das Durch-das-Feuer-Gehen alles Sinnlichen.",
        "Das ist in seinem Sinne gut.",
        "Aber es wäre sehr schlimm im Sinne der göttlich-geistigen Wesenheiten, deren Gegner Ahriman in der Weltenordnung ist, wenn er alle seine Absichten ausführen könnte.",
        "Da muß vieles anders behandelt werden, als er möchte."
      ],
      [
        "In einem Vergleich möchte ich mich darüber aussprechen.",
        "Aber indem Sie den Vergleich anwenden auf die ganze WeltenordnUng, werden Sie empfinden können, wie Ahriman für sich das, was er gut nennen kann, anstrebt, wie es aber unmöglich ist, dieses Gute in sei"
      ],
      [
        "ner Gesamtheit der Weltenordnung einzufügen.",
        "Nehmen Sie irgendein tierisches Wesen, das zu seiner fortschreitenden Entwickelung im Sinnensein sich häuten muß, das von Zeit zu Zeit die Haut ablegen muß wie ein Abbild seiner selbst und in einer neuen Daseinsform weiter fortschreiten muß.",
        "Da muß etwas abgestreift werden zu"
      ],
      [
        "einer neuen Daseinsmöglichkeit des betreffenden Wesens.",
        "Ahriman möchte alles retten, möchte keine Schlange sich häuten lassen, sondern alles verarbeiten, was da im Sinne der Weltenordnung abgestreift werden muß.",
        "Aber der Mensch möchte das auch im Sinnen- sein; er möchte vieles nicht lassen, sondern es mitnehmen, trotzdem es im Sinne einer höheren Weltenordnung für das Zeitliche, für den Augenblick bestimmt ist.",
        "Und wenn der Mensch es könnte, so würde er - weil der Hang dazu in ihm so stark ist - im SinnenseIn im- merdar unter all den Fragen, die er nach unbekannten oder sonstigen Wegen stellt, am meisten sich erkundigen: Wo findet man Ahriman, wo kann einem Ahriman wieder helfen, um das, was der Augenblick enthält, in die Ewigkeit hinaufzutragen?",
        "Da ist es das eine Gute, daß der Mensch in der Sinneswelt nicht Ahriman finden kann, weil er unsichtbar, übersinnlich in ihr ist.",
        "Und dies gehört zu den Obliegenheiten des Hüters der Schwelle, daß Ahriman möglichst stark unsichtbar in der sinnlichen Welt bleibt, so daß der Mensch nur das, was in seinen eigenen Kräften liegt, zur Bewahrung des Augenblickes in der Ewigkeit entfalten kann und sich nicht unbewußterweise"
      ],
      [
        "von Ahriman helfen lassen kann.",
        "Gutes und Schlimmes spielen da wieder als zwei Pole in das Sinnensein des Menschen herein.",
        "Der Mensch schreitet als Seele durch die Menschheitsevolution.",
        "Eine Aufgabe innerhalb derselben, die gut und echt und wahr ist, ist diejenige, alles, was Ewigkeitswert hat, hinauszutragen aus der Sinneswelt und einzuverleiben dem Reiche der Ewigkeit.",
        "Das ist es ja gerade, was uns obliegt: die wertvollen Schätze der Augenblicke zu nehmen und hinzuopfern am Altare der Ewigkeit.",
        "Wenn wir uns für die wertvollen Schätze der Zeitlichkeit von Ahriman helfen lassen, so ist das gut.",
        "Wenn wir Ahriman in dem Augenblicke, wo wir die übersinnliche Welt betreten - vorher können wir ihn ja nicht sehen -, kennenlernen und ihm den Hang zeigen, der uns noch verblieben sein kann, auch Wertloses aus der Sinnes- weIt hinaufzutragen in die übersinnliche Welt, dann ist das ja für ihn ein Wertvolles - für seine Gegner ist es ein Wertloses.",
        "Da sind wir gute Werkzeuge für ihn, um aus der Sinneswelt in die Ewigkeit überzuleiten, was hier geliebt wird, und was dadurch, daß es von uns geliebt wird, auch seinerseits in diese Ewigkeit hineingestellt wird."
      ],
      [
        "So sehen wir wieder, wie das, was von Ahriman ausgeht, absolut - an sich - nicht gut und nicht böse genannt werden darf, sondern wie es gut oder böse wird je nachdem, wie sich der Mensch ihm unterstellt, je nachdem, wie der Mensch mit ihm in ein Verhältnis tritt.",
        "Daraus sehen wir aber überhaupt, wie oberflächlich leicht Beschreibungen werden können, welche den bequemen Fragen dienen möchten: wie ist Ahriman, wie ist Luzifer?",
        "Sprache, Antworten auf solche Fragen gibt es im Grunde genommen nicht in denjenigen Welten, wo solche Wesenheiten allein charakterisiert werden sollen: in den höheren Welten.",
        "So ist der Mensch eingesponnen in das Lebenslabyrinth.",
        "Sowohl Ahriman wie Luzifer wirken in das Lebenslabyrinth herein, und der Mensch hat den Weg zu suchen, um sich in der richtigen Weise zu solchen Mächten zu stellen.",
        "Das macht es gerade, daß wir uns entwickeln können, weil wir dadurch zu den Wesen der übersinnlichen Welten Verhältnisse suchen müssen.",
        "Und die Beziehungen zu der übersinnlichen Welt werden weniger durch"
      ],
      [
        "eine nach dem Muster der Sinneserkenntnis angestrebte Erkenntnis erhalten, als dadurch, daß man sich im Sinne des Charakterisierten Beziehungen verschafft zu diesen übersinnlichen` Wesenheiten.",
        "Deshalb muß der Mensch im Lebensdunkel sein, denn in dasselbe spielen die Wesenheiten herein, welche sowohl gut wie böse sein können, und gut oder böse in ihren Wirkungen werden können, je nachdem wir uns zu ihnen stellen.",
        "Das macht das Lebensdunkel aus.",
        "Das bewirkt es, daß Lebenslicht, Geisteslicht in dieses Lebensdunkel nur dadurch hereinleuchtet, daß wir zu den einzelnen Mächten der übersinnlichen Welt, die in unsere physische Welt hereinspielen, die richtigen Verhältnisse gewinnen, daß wir uns damit bekannt machen, daß sich unsere Vorstellungen und Begriffe wandeln müssen, wenn wir von den übersinnlichen Welten sprechen wollen.",
        "An einem anderen Beispiele möchte ich Ihnen noch vor die Seele führen, wie wir anders denken müssen, wenn wir die Beziehungen der Sinneswelt zu dem Übersinnlichen richtig finden wollen."
      ],
      [
        "Da leben wir im Sinnensein, leben so, daß wir um uns und mit uns spielen fühlen das, was wir unser Lebensschicksal nennen.",
        "Da ist uns manches sympathisch, manches antipathisch an diesem Leben& schicksal.",
        "Und wer eine richtige Selbstbesinnung sich verschaffen kann, der weiß, daß Mitfühlen und Mitempfinden, Sympathie und Anüpathie haben mit den Geschicken des Lebens zu den stärksten Empfindungen gehört, die wir überhaupt haben können, die sich am tiefsten in die Seele eingraben.",
        "Nun geht es aber so - warum, brauche ich hier nicht zu wiederholen, weil es in den anfänglichen Vorträgen so oft gesagt wird -, daß wir es in unserem übergeordneten Ich, das sich im Sinne des gestrigen und vorgestrigen Vortrages an das gewöhnliche Ich nur erinnert, es nur wie eine Erinnerung in sich hat, selber sind, die sich zum Beispiel auch dasjenige Schicksal, das uns dann vielleicht ein ganzes Leben hindurch martert und peinigt, zubereiten.",
        "Gibt es nicht Menschen, welche die Reinkarnationsidee gerade deshalb ableugnen, weil sie kein Begehren haben, ein neues Dasein sich zurechtzuzimmern, nachdem sie dieses eine durchlebt haben?",
        "Warum denken solche Menschen so?",
        "Weil sie in dem Glauben befangen sind, daß es in den Welten, in denen der"
      ],
      [
        "Mensch nach dem Tode ist, ebenso zugehe wie in der Sinneswelt.",
        "Hier kann uns manches gefallen, manches mißfallen.",
        "Aber so zu empfinden wie hier, fällt uns gar nicht ein, wenn wir in dem Leben zwischen Tod und neuer Geburt sind."
      ],
      [
        "Dort empfinden wir ganz anders, wenn wir auch hier nichts davon wissen.",
        "Wenn wir nach dem Tode in die geistige Welt kommen, dann sehen wir zum Beispiel: Du hast gelebt auf der Erde in einem Sinnensein, du hast eine bestimmte Fähigkeit gehabt, aber diese Fähigkeit kam sehr einseitig bei dir heraus, du hast sie vielleicht auch mißbraucht."
      ],
      [
        "Du mußt jetzt in einem neuen Erdensein in einer anderen Körperlichkeit dich so ausgestalten, daß das Einseitige ausgeglichen wird und daß eine Unvollkommenheit vollkommener werde.",
        "Du mußt - mit anderen Worten - das, was du in unvollkommener Gestalt an dir gehabt hast, in einer anderen Unvollkommenheit dir aneignen, damit durch das gegenseitige Wirken die Sache ausgeglichen und harmonisiert werde."
      ],
      [
        "Da beginnt dann eine Zeit beim Durchgang zwischen Tod und neuer Geburt bis zur neuen Geburt hin, wo sich der Mensch sagt: Ich will so geboren werden, daß ich in einem neuen Leben ganz unfähig bin - beispielsweise -, mich in der Malerei zu betätigen, weil ich mich vorher darin betätigt habe und großes Geschick dabei gehabt habe.",
        "Denn dadurch, daß ich nun in der Malerei ungeschickt sein werde, werde ich in die Lage kommen, nie ein Urteil in meine Seele einfließen zu lassen, wie wenn ich selber male, sondern nur so, wie es sein muß, wenn ich mich selber vor die Sache stellen muß."
      ],
      [
        "Da werde ich mir andere Kräfte aneignen müssen, weil das heilsam sein kann, um das, was ich früher gehabt habe, zu harmonisieren, auszugleichen.",
        "So kann man zurückschauen auf ein Leben zwischen Geburt und Tod, auf etwas, was man glücklich durchlaufen hat, sagt sich aber, wenn man seine gesamte Evolution nur so einrichten würde, daß man sein Leben so erlebt, so hätte man es nicht ausgekostet."
      ],
      [
        "Was erfolgen muß aus Kräften, die gerade in dieser Weise sich ergeben, ist daher die Begierde: was du vorher im Glück erlebt hast, das mußt du jetzt im Leid erleben.",
        "Und man richtet nun alles so ein, daß man aus einer Sehnsucht heraus auf einem bestimmten Gebiete Leiden erleben muß, deren Durchmachen einen"
      ],
      [
        "wieder weiterbringt im Dasein.",
        "Dann liegt die Tatsache vor, daß man im Übersinnlichen verlangt hat nach Leiden und Schmerzen und sie im Sinnensein als etwas empfindet, was inan wegtun möchte.",
        "Da wird wahrhaftig der Unterschied zwischen dem Leben im Sinnensein und dem Leben in den übersinnlichen Welten zwischen Tod und neuer Geburt praktisch bedeutsam."
      ],
      [
        "Ganz andere Kräfte wirken in unserem Leben zwischen Tod und neuer Geburt, als uns dann sympathisch oder unsympathisch sind im Leben zwischen Geburt und Tod.",
        "Was tut nun der, welcher etwa das Leben in den über- sinnlichen Welten beurteilen würde nach seinen Sympathien und Antipathien im Sinnensein?"
      ],
      [
        "Er verpflanzt das, was er im Sinnensein hat, perspektivisch hinein in die übersinnliche Welt.",
        "Es ist richtig so, wie wenn Sie auf irgendeine Glastafel aufzeichnen oder aufmalen zum Beispiel eine Rose; dann schauen Sie die Glastafel an, das Glas sehen Sie nicht - Sie schauen durch das Glas durch, aber die Malerei projiziert sich hinten auf eine Riesenwand, und Sie glauben, das ist wirklich."
      ],
      [
        "Es ist aber gar nicht wirklich, sondern Sie haben es nur dort hinausversetzt.",
        "In dieser Weise kann der Mensch, wenn er die übersinnliche Welt beurteilen will nach Sympathien und Antipathien im Sinnensein, in die übersinnliche Welt etwas hineinprojizieren wie Schatten, was dann im Übersinnlichen auch eine Gültigkeit haben kann."
      ],
      [
        "Es hat schon eine Wirkung, eine Gültigkeit.",
        "Wenn man es nicht sieht, projiziert sich etwas wie ein Nebel auf das, was da drinnen vor dem Betrachter steht."
      ],
      [
        "Das kann uns - wieder von einer anderen Seite her - empfindungsgemäß hinweisen auf das, was wir das Lebensdunkel nennen können.",
        "Warum leben wir im Lebensdunkel zwischen Geburt und Tod?",
        "Weil berechtigt und selbstverständlich für das Leben zwischen Geburt und Tod Urteile, Wertungen des Lebens sind, die ungültig sein müssen für dasjenige Dasein, das wir selbst verbringen zwischen dem Tode und einer neuen Geburt.",
        "Wir brauchen für das Sinnen- sein ein Seelenleben, das keine Gültigkeit für die übersinnliche Welt hat.",
        "Wir müssen daher durch die Erkenntnisse, durch dasjenige, was erforscht werden kann in den übersinnlichen Welten, hereinleuchten lassen das Geisteslicht aus den übersinnlichen Welten, damit wir"
      ],
      [
        "zu einer Gesamterfassung der Welt kommen.",
        "Der größte Fehler, den die Menschen in bezug auf Weltanschauungen machen können, ist der, wenn sie glauben, das, was sie gewonnen haben an Begriffen und Ideen in der Sinneswelt, ausdehnen zu können auf die übersinnliche Welt, wenn sie nicht die Geduld und Ausdauer haben, aus der wirklichen Erforschung des Übersinnlichen heraus sich die Beschreibungen geben zu lassen von demjenigen, was als Geisteslicht aus den übersinnlichen Welten hereinleuchtet in das Lebensdunkel des Sinnenseins.",
        "Hier stehen wir allerdings vor der Frage: Ist dann"
      ],
      [
        "nur derjenige imstande, dieses Geisteslicht der übersinnlichen Welten auf sich wirken zu lassen, der selber schauen kann in den über- sinnlichen Welten, der also die Initiation genossen hat? - Dieser Glaube ist vielfach in der Welt verbreitet.",
        "Vielfach hört man sagen: Wie kann man etwas von den übersinnlichen Welten begreifen, wenn man nicht selber die Initiation durchgemacht hat?",
        "Und man hört dann darauf hinweisen, wie das einzig Wahre nur das Durchmachen der Schritte zur Initiation sein kann, das eigentliche Hinauf- steigen in die übersinnliche Welt."
      ],
      [
        "Wie es sich auf diesem Gebiete verhält, wie Begreifen zum Schauen steht in den übersinnlichen Welten, wieviel man von Lebenstrost und Lebenskraft durch das Begreifen des Geisteslichtes im Lebens- dunkel haben kann, das soll der Ausgangspunkt sein für die morgige Betrachtung, die uns noch einige Schritte weiter in die Probleme, die wir in diesem Zyklus betrachten wollen, hineinführen soll."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "SIEBENTER VORTRAG München, 31. August 1912",
    "paragraphs": [
      "Die gestrige Betrachtung konnten wir damit schließen, daß ein Hinweis gegeben wurde auf die Stellung des einzelnen Menschen zu dem, was Beschreibung der übersinnlichen Welt genannt werden kann, was aus den Forschungen, aus den Beobachtungen, aus den Erlebnissen der Initiation kommt. Und es ist darauf aufmerksam gemacht worden, daß sehr leicht das Urteil zustande kommen könnte, ein Wert und eine Bedeutung für das Seelenleben mit den Ergebnissen der Initiation könnte doch eigentlich nur für denjenigen verbunden sein, der selber die ersten Schritte zur Initiation gemacht hat und imstande ist, durch eigenes Schauen in das Erleben, in die Beobachtung der höheren Welten hineinzudringen.",
      "Es ist schon öfter betont worden, daß dies nicht so ist, daß man allerdings nur dann anschauen, beobachten, erkunden und erforschen kann, was in den höheren Welten vorgeht, wenn man das eigene Selbst, die eigene Seele so umgestaltet hat, daß man in jene anderen Welten hinein- blicken kann, die zwar ganz anders sind als unser Sinnensein, die aber mit unserem Sinnensein - wie gestern erwähnt worden ist - doch in dieser oder jener Beziehung zusammenhängen, vor allem aber als seine Grundlage anzusehen sind. Was dagegen das Begreifen, das Verstehen dieser anderen Welten betrifft, so wäre es ein falsches Urteil, wenn man behaupten wollte, zu dem Verstehen, zu dem Begreifen, zu dem Entgegennehmen dessen, was derjenige geben kann, der die ersten oder die weiteren Schritte zur Initiation gemacht hat, gehöre selber Erleben.",
      "Vielmehr muß immer wieder und wieder betont werden, daß jeder Mensch, der nur unbefangen sich dem hingibt, was von den eigentlichen Geistesforschern in den übersinnlichen Welten erkundet wird, der unbefangen ihre Beschreibungen, Erfahrungen und Mitteilungen aufnimmt und wirklich unbefangenes Urteil, unbefangene Verstandestätigkeit walten läßt, alles, was ihm gegeben werden kann, auch begreifen kann. Für das Sinnensein sind wir in einem ganz anderen Fall.",
      "Es ist durchaus berechtigt zu",
      "sagen, daß kaum ein Mensch aus einer Beschreibung heraus begreifen wird, was die Sixtinische Madonna ist oder was eine ferne, fremde Landschaft ist. Man wird sich, wenn man eine lebendige Phantasie hat, aus einer solchen Beschreibung eine Vorstellung bilden können, aber berechtigt bleibt doch der Ausspruch, daß der erst das, was im Sinnensein ist, begreift, der selbst zum Anschauen kommen kann, so daß für das Sinnensein das Begreifen dem Anschauen nachfolgen muß. Das ist für die höheren Welten durchaus nicht so. Da kann durch die Forscher, was sie erkunden, aus den höheren Welten herausgeholt werden, kann in die Formen und Begriffe menschlicher",
      "Ideen gebracht werden und so der Welt gegeben werden. Da kann man dann selbstverständlich in materialistischen oder sonstigen Dogmen befangen sein, oder man kann überhaupt keinen Willen haben zur Unbefangenen Hingabe an das, was da mitgeteilt wird; dann wird man es nicht begreifen. Es kann durchaus sein, daß man gar keine Schuld daran hat, daß man es nicht begreifen kann, weil ei- nem das bisherige Leben und die bisherige Erziehung nicht die Möglichkeit gegeben haben, sich unbefangen diesen Dingen hinzugeben. Aber jeder, der in der Lage ist, sich diesen Dingen unbefangen hin- zugeben, unbefangen alles zusammenzuhalten, was gesunde Vernunft",
      "und gesundes Urteil gibt, wird sich zuletzt sagen: wenn auch die Dinge zuerst noch so unglaublich scheinen, gerade gesundes, umfassendes und allseitiges Denken fÜhrt zum Begreifen derselben, wenn man auch noch nicht das Allergeringste aus den höheren Welten zu schauen vermag.",
      "Wie ich Ihnen in diesen Tagen mitteilen konnte, daß der, welcher zu einem Schauen der geistigen Welt kommt, in seinem Innensein die Abbilder dessen trägt, was er selbst in seinem Innern hat, ja, zuerst geführt wird durch das, was er in sich zuerst als Bilder hat, so ist es mit dem Begreifen der Dinge der übersinnlichen Welten: das Begreifen geht dem Schauen voran und ist in keiner Weise beeinflußt vom Schauen, noch beeinflußt es selbst das Schauen. Das vorherige Begreifen braucht nicht im geringsten Maße zu beeinflussen, was den Menschen dann zum völlig unbefangenen, wahrheitsgetreuen Schauen bringt. Ein vorheriges Begreifen, ein Erfassen mit allseitiger",
      "Urteilskraft - zu dem allerdings unsere Zeit in den weitesten Kreisen durchaus keine Neigung hat - wird dagegen die Seele, das Gemüt vorbereiten, um auch in der entsprechenden Art in das Schauen eintreten zu können. Daher muß immer wieder und wieder gesagt werden: Wahrer Okkultismus, wahre Geisteswissenschaft, die es ernst und ehrlich meint, wird sich niemals zurückziehen vor der Aufforderung, man begreife, man verstehe unbefangen das, was gesagt ist. Man suche darin einzudringen mit dem gesunden Menschenverstand, mit der sich in alle Gebiete frei ergießenden Urteilskraft, und man wird es können. Mancherlei über diese Sachen finden Sie in der Schrift «Ein Weg zur Selbsterkenntnis des Menschen», in der manches zur Ergänzung dieser Vorträge enthalten sein wird. Aber insbesondere soll es erwähnt werden, daß ein Bedeutendes beigetragen werden kann zur Läuterung, zur Reinigung der Seele, wenn vor allen Dingen diejenigen, welche den Weg zur Geisteswissenschaft aus dem Lebensdunkel heraus suchen, objektiv zu verstehen, objektiv zu begreifen versuchen mit dem, was jedem Menschen, wenn er nur will, als eine gesunde Urteilskraft zur Verfügung stehen kann. Dieser Weg des gesunden Begreifens, des Ablehnens einer jeglichen Autorität und eines jeglichen Autoritätenglaubens gewinnt noch dazu ein besonderes Licht, wenn man eingeht auf gewisse Feinheiten der okkulten Beobachtung.",
      "Aus dem ganzen Sinn und Geist dieser Vorträge ist ja hervorgegangen, daß es sich bei den Schritten, die zur Initiation gemacht werden, immer mehr und mehr für jeden Menschen darum handelt, daß er unabhängig wird in seinem Erleben von dem, wozu ihm sein physischer Leib als Werkzeug dienen kann, daß er zu erleben lernt in seinen höheren Leibern, in seinem elementarischen oder ätherischen Leibe, in seinem astralischen Leibe, auch in dem, was man seinen Ich- oder Gedankenleib nennen kann. Auf dieses Sich.Fähigmachen, um in seinen höheren Leibern wahrzunehmen, kommt es insbesondere bei allen Schritten der Initiation an. Dabei ist es aber notwendig, daß der Mensch etwas dazu tut, um sich freizumachen vom sinnlich-physischen Leibe, daß er bewußt alles dasjenige von sich abstreift, von sich abzieht, was ihn so mit der Welt in Zusammenhang",
      "hält, wie dieser Zusammenhang sich nur durch das Werkzeug des physischen Leibes ergibt. Das ist natürlich namentlich in einem Zeitalter, das so materialistisch ist wie das heutige, nicht für alle Menschen möglich, besonders für die, welche sich heute auch ein Urteil über die Weltenrätsel, über die Weltenerscheinungen zuschreiben, und die durch die sonderbare heutige Erziehungsweise zu dem Glauben verzogen werden, daß man in frühester Jugend schon ein umfassendes Urteil - nicht bloß ein Streben - über die Welterscheinungen gewinnen könne.",
      "Warum wird heute durch unreife, durch rein aus der Leidenschaft und Emotion herausgeborene Urteile in der Welt soviel Unheil angerichtet? Wenn man die Welterscheinungen über- schaut, dann sieht man, daß der Druckmarkt mit den unreifsten Dingen überschwemmt wird, die aus nichts anderem herausgeboren sind als aus Sympathien und Antipathien.",
      "Warum das? Man kann die Frage aufwerfen: Hat es nicht früher auch Menschen gegeben, die den reinen Errungenschaften übersinnlicher Forschung mit Haß und Abscheu aus ihrem Lebensdunkel heraus gegenüberstanden wie in unserer Zeit?",
      "Hat es nicht Dunkelmänner gegeben, wie es die heutigen Materialisten sind, die alle möglichen Mittel, welche Haß, Unwissenheit und Finsternis eingeben, anwandten? Ja, die hat es immer gegeben. Aber in der Weise, wie sie heute wirken, haben sie nicht gewirkt.",
      "Warum nicht? Solche Dinge muß man sich auch manchmal ins Gewissen schreiben. Die Menschen waren da, die die höheren Welten und unbefangenes Eindringen in diese Welten gehaßt haben, weil eben das unbefangene Eindringen in die höheren Welten zuweilen für die Menschen recht unangenehme Tatsachen zutage bringt.",
      "Aber diese Menschen haben oftmals nicht schreiben und lesen gekonnt. Ihr Bildungsniveau entsprach dem Nichtschreiben- und Nichtlesenkönnen. Heute müssen die> welche so denken, vermöge ihrer Bildung schreiben und lesen können, und das große Publikum hat kein Unterscheidungsvermögen, um das, was auf dem Büchermarkt erscheint, wirklich richtig auffassen zu können, und es ist auch nicht viel Wille vorhanden zu einem solchen Unterscheidungsvermögen, um erkennen zu können, daß hier sichtend und klärend das Urteil einer okkultistisch - geisteswissenschaftlichen",
      "Bewegung in unserer Zeit eingreifen muß. Man wird da manches lernen müssen, was den Menschen hart ist zu lernen. Einfach aus den Tatsachen, die sich aus der übersinnlichen Welt heraus ergeben, wird man manches lernen müssen.",
      "So wird man zum Beispiel lernen müssen, daß - auch dann, wenn man in die höheren Welten eindringt durch gewisse partielle Schulung oder Zubereitung seines seelischen und sonstigen Organismus - noch mancherlei zurückbleiben kann in bezug auf jenen Zusammenhang mit der Außenwelt, der nur auf dem Umwege durch den physisch-sinnlichen Leib zustande kommt. Alles, was so in einem geistigen Schauer, wenn man die Grenze überschritten hat, die zwischen dem Sinnensein und dem Geistessein so fest gezogen ist, von gewissen berechtigten Schwächen des Sinnenseins zurückbleibt, hüllt uns in Finsternis und Maja, wenn wir es erleben beim höheren geistigen Schauen. Nur wer unablässig mit sich zu Rate geht, wie er das, was er im Sinnensein haben muß, weil er ein Wesen der Sinneswelt ist, für 'jene Zeiten, da er geistig schauen muß, völlig ausschalten kann, und wie er es dazu bringen kann, daß beim geistigen Schauen nichts von dem hereinspielt, was ihn in der Sinneswelt umgibt, nur der kann wirklich rein und majalos die geistige über- sinnliche Welt schauen.",
      "Nehmen wir einen bestimmten Fall, ohne daß dabei auf irgend etwas angespielt werden soll. Irgend jemand, der die Schritte zur Initiation durchmachen will oder schon durchgemacht hat, habe ein persönliches, auf unmittelbare persönliche Gefühle, persönliche Emotionen beruhendes Verhältnis zu einem anderen Menschen. Nehmen wir an, in einem solchen Verhältnis eines geistigen Erschauers, eines erst zu Initiierenden oder schon mit gewissen Schritten der Initiation Ausgestatteten wäre es so, daß er von Mensch zu",
      "Mensch ein bestimmtes persönliches Verhältnis hätte, ein Verhältnis, das auf Zuneigung beruht, auf solcher Zuneigung, welche im Sinnensein geschlossen wird, sagen wir auf einer zutraulichen Liebe, die im Sinnensein erwacht, die von Leib zu Leib spielt - im höheren Sinne, nicht nur im niederen Sinne, denke ich dabei. Nehmen wir an, so etwas wäre vorhanden und ein solcher geistiger Schauer würde",
      "nun etwas erforschen wollen von der Persönlichkeit, zu der er eine persönliche Zuneigung hat, die sich im Sinnensein gebildet hat, und nehmen wir an, er wäre nicht in der Lage, alles vdn sich abzustreifen, was von im Sinnensein erschaffener Liebe zu der betreffenden Persönlichkeit da ist, dann ist es fast ganz unmöglich, die Wahrheit in bezug auf das übersinnliche Sein einer solchen Persönlichkeit zu erfahren. Oh, es ist notwendig, auf Schritt und Tritt zu versuchen - und wenn man noch so sehr liebt und noch so sehr persönliche Zuneigung hat im Sinnensein -, alles abzustreifen für die Zeiten, wo man das Übersinnliche Dasein betrachten will.",
      "Es ist möglich, daß man eine solche persönliche Zuneigung hat und nicht abstreift, daß man in der Weise, wie es im Sinnensein ist, die betreffende Persönlichkeit gern hat. Dann stellen sich einem solchen geistigen Schauer zum Beispiel über Vergangenheit und Zukunft dieser Persönlichkeit Bilder vor Augen, die unter allen Umständen falsch sein müssen, dann kann eine ganze Fülle von Maja auftauchen.",
      "Darum kann der, welcher es ernst und verantwortungsvoll mit dem nimmt, was der Welt auf dem Felde geistiger Weisheit gegeben werden soll, nicht vorsichtig genug sein, vor allen Dingen etwas der Welt zu verkünden, was im Umkreise des Familiären, des unmittelbar Bekannten stattfindet. Man kann sich überall sichern in der Weise, daß, wenn auf okkulte Ergebnisse hingewiesen wird, die sich auf etwas beziehen, das den unmittelbar persönlichen Umkreis des Untersuchers betrifft, diese im höchsten Maße demjenigen zweifelhaft erscheinen sollten, der sie entgegennehmen soll.",
      "Das ist nicht etwas, was mit Anspielung auf diese oder jene Tatsache gesagt werden soll, sondern was gesagt werden soll, weil es eine objektive Tatsache für jeden Okkultisten ist. Damit hängen aber Dinge zusammen, welche durchaus, man möchte sagen, in höhere Gebiete hinaufspielen. Damit hängt zusammen, daß der, welcher in den übersinnlichen Welten forschen will, wenig geeignet ist, eine gewisse Grundvorstellung richtiger Art in bezug auf religiöse Fragen zu erhalten, wenn er mit seinen Vorurteilen, mit seinen persönlichen Gefühlen irgendeiner besonderen Religionsgemeinschaft zugetan ist, wenn er eine Religionsgemeinschaft mehr liebt als die andere",
      "oder sich gar zum propagandistischen Träger einer Religionsgemeinschaft macht. Wer zur persönlichen Propaganda neigt, kann nicht zugleich objektiver Okkultist sein! Das ist ein Satz, der auch einmal in aller Schärfe ausgesprochen werden muß. Es sind Bedingungen da, die wir mit unserem Karma der abendländischen Kultur in Zusammenhang bringen dürfen, Bedingungen, welche es in einer gewissen Weise dem Abendländer, wenn er sich ein wenig bekannt macht mit den Grundanforderungen des übersinnlichen Lebens, doch nicht gar zu schwer machen, ein objektives Urteil zu gewinnen gerade über die Hineinstellung des größten Ereignisses in die Menschheitsevolution, das wir das Mysterium von Golgatha nennen. Wodurch kommt denn in das religiöse Leben und in seine Auffassung so manches Lebensdunkel hinein? Wodurch kommt das hinein, was nur mit dem Augenblick zu tun haben will und sich nicht zu Geisteslicht und Ewigkeit gerade im religiösen Leben erheben will? Das kommt davon her, weil mit alledem, was menschliche Egoismen sind - und nun nicht bloß Egoismen der einzelnen, sondern auch Egoismen der Stämme, der Rassen, der Völker -, dasjenige innig zusammenhängt, was sich auf das religiöse Leben bezieht. Von diesem Gesichtspunkte aus möchte ich Sie auf eine Erscheinung aufmerksam machen, denn notwendig ist es, daß man diese Dinge völlig unbefangen betrachtet.",
      "Welche Rolle spielt das religiöse Leben bei einem Orientalen in bezug auf seinen Religionsstifter, wenn er den Zusammenhang seiner Rassen- oder nationalen Evolution in Betracht zieht? Untersuchen Sie einmal, ob ein Orientale oder irgendein Nichtabendländer so leicht geschichtlich denken kann über den geschichtlichen Verlauf, in den er hineingestellt ist, ohne dieses geschichtliche Leben an- zuknüpfen an Krishna, Buddha, Mahomet, Konfuzius oder dergleichen? Überall sehen wir ganz selbstverständlich das, was im religiösen Leben sich abspielt, mit dem verbunden, was im profanen äußeren Leben geschieht und in den Gemütern der Leute fließt. Man kann sich eine Geschichtsschreibung eines Buddhisten zum Beispiel nicht denken, ohne daß er in den Mittelpunkt derselben den Buddha stellt. Das sei nicht als eine Kritik gesagt, sondern weil es für diese",
      "Menschen richtig ist, die solchen Kulturentwickelungen angehören. Jetzt gehen wir ins Abendland und sehen nicht auf Dogmen, sondern auf Tatsachen. Ich greife heraus einen anerkannten`Geschichtsschreiber des Abendlandes: Leopold von Ranke, der in aller Welt bekannt ist durch seine Objektivität, seine ruhige Würdigung, seine ganz besondere Art, sich objektiv zu den Dingen zu stellen.",
      "Ranke hat manches Kapitel der geschichtlichen Entwickelung geschrieben. Doch von Ranke ist etwas sehr Merkwürdiges bekannt geworden. Einem Freunde gegenüber hat er sich darüber geäußert, daß er doch den geschichtlichen Verlauf so dargestellt hat, daß er nirgends in Betracht zieht den Christus und die Tatsachen, die sich unmittelbar an den Christus anschließen!",
      "Ranke hat sich bemüht, durch seine Objektivität eine Geschichte des Abendlandes zu schreiben, ohne daß er den Christus hat hineinspielen lassen. Und es hat ihm manche schwere Gewissenspein im Alter gemacht, daß er sich sagen mußte: Ja, wenn nun doch in das Geschehen jene Taten hineinfließen würden, über die keine Dokumente und Urkunden vorhanden sind, ist dann diese Geschichte wahr? - Nicht darum soll das hier angeführt werden, um auseinanderzusetzen, ob sie wahr oder falsch ist - denn ich halte sie in hohem Maße für berechtigt -, sondern weil es eine der besten Geschichten eines der anerkannten Geschichtsschreiber im Abendlande gibt, die Geschichte 5Q geschrieben haben, daß man den Christus herausgelassen hat, daß man den Christus nicht in die Historie mit hineingenommen hat.",
      "Das ist eine fundamental wichtige, eine bedeutsame Tatsache! Wohin hat die abendländische Kultur geführt? Die abendländische Entwickelung hat dazu geführt, daß hier nicht immer zu einem Wesen aufgeschaut wird, das wie eine Mittelpunktfigur der ganzen Geschichte dastehen würde, wenn man daran anknüpfen würde.",
      "Wissenschaft hat nicht dazu geführt! Warum kam das? Beleuchten wir diese Tatsache von einem anderen Gesichtspunkt aus.",
      "Wo haben die großen Religionsstifter gelebt, welche die großen Initiierten waren, die ihren Völkern aus ihren Völkersubstanzen heraus das gaben, was sie brauchten? Ist es denkbar, daß zum Beispiel Hermes aus einer anderen Volkssubstanz heraus auf seine Epoche",
      "gewirkt hätte, oder ist es denkbar, daß Buddha in einer anderen Weise gewirkt hätte als aus der Rasseneigentümlichkeit heraus, in die er hineingestellt war und in diese Rasseneigentümlichkeit hinein seine Kräfte gesendet hat? Und jetzt wenden wir den Blick zu dem, den wir keinen Initiierten nennen, sondern den wir kennen als die Persönlichkeit, auf welche die Welten-Initiation, die kosmische Initiation gewirkt hat.",
      "Gehört er irgendeinem Volke an? - In einem unbekannten Winkel der Welt, fern der großen Reiche, ist er geboren. Da spielten sich die Ereignisse ab. Und da man die Evangelien wie die anderen Urkunden des Neuen Testamentes als historische Urkunden bezweifeln kann, so kann man sagen: Von allen diesen Ereignissen wird nichts bezeugt durch irgendein historisches Dokument.",
      "Und die, welche sich zu ihm als seine Jünger und Schüler gefunden haben, haben sich zu ihm gewendet ohne Unterschied von Stamm, Rasse, Geschlecht und so weiter. So ist der Unterschied! Während sich vorher die Völker zu ihren Rassen-Initiierten gewendet haben, haben sie sich hier zu einem gewendet, der keinem Volke angehört - ja, der sogar gerade seine größten Kulturtaten bei einem Volke verrichtet hat, bei dem er nicht gelebt hat.",
      "Das ist der große Fortschritt aus dem Lebensdunkel zum Geisteslicht, den man nicht verkennen sollte, wenn man es ehrlich meint mit der Evolution der Menschheit. Das sind Dinge, die durchaus in Betracht kommen, Dinge, auf welche diejenige Wissenschaft kräftig hinzuweisen hat, die aus der wirklichen Betrachtung der übersinnlichen Welten entnommen werden kann.",
      "Aus mancherlei von dem, was ich Ihnen sagen durfte, sehen Sie, daß es darauf ankommt, etwas von jenem Urteil zu verstehen, das des Johannes Thomasius Doppelgänger sagt - im «Hüter der Schwelle» -: Das Denken hat eine läuternde Kraft. Diese läuternde Kraft des Denkens wirkt aber auch so, daß sie wirklich aus dem Lebensdunkel in das Geisteslicht herausführt, daß sie wirklich von dem Augenblick zur Ewigkeit hinwegführt. Man will nur nicht gern dem Denken seine läuternde Kraft zugestehen. Denn es ist etwas Eigentümliches um die okkulte Natur dieses Denkens. Eine materialistische Wissenschaft glaubt, daß der Mensch etwa mit seinem Gehirn",
      "denke. Er denkt nicht mit seinem Gehirn; das ist einfach ein Irrtum. Und wenn Sie den ganzen Sinn dessen kennenlernen, was in der Schrift «Ein Weg zur Selbsterkenntnis des Menschen» gesagt ist, so werden Sie auch begreifen, daß der Vorgang des Denkens, die Tätigkeit des Denkens, die Verbindung und Lösung von Ideen nicht im physischen Leibe abläuft, sondern im ätherischen oder elementarischen Leibe. In Wahrheit denkt auch der Mensch, der im gewöhnlichen Leben steht, mit seinem elementarischen oder ätherischen Leibe, nur bewirkt das Stehen im gewöhnlichen Leben, daß der Mensch kein Wissen haben kann von jener Tätigkeit, die in ihm vorgeht, wenn er denkt, aber nur im ätherischen Leibe vorgeht. Im Grunde genommen denkt der Mensch fortwährend, und fortwährend ist der ätherische Leib in Bewegung, und diese Bewegung bedeutet denken. Aber was kommt von alledem zum Bewußtsein, was so im ätherischen Leibe vorgeht? Es kommt nur das zum Bewußtsein, was davon gespiegelt wird. Sie müssen sich ein gewisses Verhältnis des elementarischen Leibes zum physischen Leibe in folgender Art vorstellen.",
      "Nehmen Sie an, Sie gingen in diesem Saale längs dieser Fensterreihe entlang. Nun denken Sie sich, überall an den Wänden zwischen den Fenstern hingen Spiegel. Indem Sie an jedem Spiegel vorbeigehen, zum Beispiel dreimal, sehen Sie Ihr Antlitz; wo kein Spiegel ist, sehen Sie von Ihrem Antlitz nichts. Wenn Sie wieder weitergehen zum nächsten Spiegel, sehen Sie es wieder. Da ist wieder ein Spiegel, der wirft Ihnen das Bild Ihres Antlitzes zurück. Ihr Antlitz ist immer vorhanden auf dem ganzen Wege, aber Sie sehen es nur, wenn es sich spiegelt. Der Ätherleib ist in fortwährendem Gedankenfluß. Aber wann nur wird dieser Gedankenfluß Wahrnehmung? Wenn das, was im physischen Leibe ist, das Gehirn, dasjenige spiegelt, was im ätherischen Leibe vorgeht. Was sonst immer da ist und wovon der Mensch gewöhnlich nichts weiß, das wird gespiegelt vom Gehirn, das wie ein Spiegelungsapparat aufzufassen ist. Und in all den Fällen, wo das Leben gespiegelt wird, wird es bewußt. Daher muß der physische Leib da sein, damit der ätherische Leib, der eigentlich denkt, von seinem Denken etwas wissen kann. Aber es denkt nicht",
      "das Gehirn, und es denkt nicht der physische Leib. Sowenig als das, was im Spiegel erscheint, Sie sind, so wenig ist das, was der Mensch wahrnimmt im Gehirn, sein Denken, denn dieses Denken sitzt im elementarischen oder ätherischen Leibe. Und wenn der Mensch die ersten Schritte zur Initiation machen will, ist es im Grunde genommen so, wie wenn Sie vor der Spiegelung überall vorbeigingen und versuchten in sich selbst zu sein - und dann fähig würden zu empfinden, wie Ihre Form ist, so daß Sie sich dann von innen heraus wahrnehmen würden.",
      "So ist das Hinaufrücken vom Sinnensein zum Geistessein. Während der Mensch sonst nur das wahrnehmen kann, was in seinem Spiegelungsapparat vorgeht, was er als die Spiegelung in seinem Gehirn sieht, kommt er durch die Initiation zum direkten Erleben und Erfühlen im elementarischen Leibe.",
      "Wenn er aber zu diesem inneren Erleben und Erfühlen kommt, dann kommt er zum Beispiel mit einer ganz anderen Welt in Berührung: mit der Welt des Wesenhaften. Dann erweitert sich sein Sein, sein Erleben, sein Erfühlen über die objektive Welt hinüber.",
      "Aber was er dann erlebt, ist eine Welt geistigen Seins, das ist eine Welt, die er in bezug auf den Umfang des Erlebten auch im Sinnensein erleben kann. Aber da erst kann er dann hinaufsteigen, um im geistigen Sein etwas zu erfassen von dem, dessen Abbild nur im Sinnenbilde vorhanden ist.",
      "Und dann kann er begreifen, daß die Impulse der Initiierten nicht bloß aus dem Erden- wissen geflossen sind, sondern daß den großen Initiierten die größten Impulse, die moralischen Impulse und so weiter deshalb zukommen und mit so gewaltiger Kraft wirken, weil sie das, was sie haben, nicht bloß von der Erde nehmen, sondern von dem mitnehmen, was über die Erde hinausgeht. Denn sobald man über die Erde hinaus- kommt, kommt man auch zu dem, was mit dem Erdensein über die Erde hinaus verbunden ist.",
      "Und kommt man durch die Initiation vom Erdensein zum kosmischen Sein, dann kommt man dazu, daß, wenn man einen Initiierten wie zum Beispiel Buddha von diesem Gesichtspunkte aus studiert, man sagt: Er hat in vielen Inkarnationen als Bodhisattva auf der Erde gelebt. Und wer in dieser Beziehung den Buddhismus verstehen gelernt hat, der ist notwendigerweise",
      "ebenso gläubig wie ein Buddhist und weiß, daß in der Persönlichkeit des Gotama Buddha diese Individualität zum letzten Male in einem physischen Leibe lebte, in dieser Inkarnatio`n aber der «Buddha» wurde und dann hinaufgestiegen ist in die geistigen Welten zum geistigen Wirken, so daß der geistige Blick hingelenkt werden kann auf den Übergang der Buddha-Individualität vom Erden- sein zum Geistessein, zu Zusammenhängen mit dem Geistessein. Und wenn man nun diese Individualität zurückverfolgt, so sieht man zwar, wie der Bodhisattva durch viele Inkarnationen geht, aber man kommt dann in eine frühere Zeit zurück, für welche man nicht mehr sagen kann: Wir haben es mit einer Individualität zu tun, die auf der Erde lebt.",
      "Denn da muß man sie auf einem früheren Wohnplatz verfolgen, und es stellt sich die Wandlung dieser eigenartigen Individualität so dar, daß sie hinauswächst über das Erdendasein. Wir sehen den Buddha zu einer bestimmten Zeit herabkommen von einem anderen Planeten unseres Sonnensystems, wo er vorher gewirkt hat, sehen ihn dort wirken und sich für seine Erdenlaufbahn vorbereiten.",
      "Wir verfolgen ihn dann als Bodhisattva und zuletzt als Buddha während seiner irdischen Laufbahn weiter bis zu dem Punkt, da er aus dem Bodhisattva ein Buddha geworden ist, und finden, daß sein Wirken während der Erdeninkarnationen allerdings mit der Erde zusammengewachsen war, daß er aber in ein großes kosmisches Ganzes hineinwächst. Wir sehen ihn hinaufsteigen zu einem anderen Planeten unseres Planetensystems, zum Mars, und dort eine neue Mission unternehmen, die sich anschließt an das, was seine Erdenmission war.",
      "Und wunderbar ist es zu verfolgen, wie sich auf diese Weise ein Ganzes herausstellt. Zuerst sehen wir den Buddha wirksam auf einem anderen Planeten, dann kommt er auf die Erde, und man muß sagen: Diese Individualität des Initiierten Gotama Buddha wirkte eine Weile auf der Erde, dann aber, wenn man sie weiter verfolgen will, muß man zu einem anderen Planeten hinaufsteigen.",
      "So bekommt man eine geschlossene Linie. Für Buddha ist es möglich zu sagen, daß er von einem anderen Planeten heruntergestiegen ist, und daß er nach seinem Wirken auf der Erde wieder hinaufgestiegen ist zu einem anderen Planeten, dessen Bevölkerung",
      "für die Erdenmenschheit wenig Sinn hat, um dort weiterzuwirken, weil dieses Weiterwirken gerade einen Sinn ergibt.",
      "So würde man bei vielen Initiierten finden, wie sie aus dem Kosmos das hereintragen, was bei der Erde selbst mit dem Kosmischen in Zusammenhang steht, und man würde dadurch die kosmische Wandlung der Initiierten ins Auge fassen. Wenn man überall den Dingen auf den Grund zu kommen versucht, dann sieht man zum Beispiel auch etwas, was uns das Lebensdunkel aus einer wirklichen okkulten Betrachtung heraus aufhellt.",
      "Es ist sonderbar, wenn manchmal die Frage aufgeworfen wird: Ist es nicht ungerecht, daß eine solche Individualität wie der Christus etwas Besonderes in die Welt gebracht hat? Und wenn das der Fall ist - so möchten manche sagen -, dann würden ja die, welche nach dem Christus gelebt haben, etwas ganz Besonderes vor der Welt voraus haben!",
      "Sogar Theosophen haben diese Frage aufgeworfen! Aber es sind ja dieselben Seelen, welche in der Zeit nach der Erscheinung des Christus leben, wie die, welche vorher da waren, so daß von Ungerechtigkeit dabei nicht die Rede sein kann.",
      "Nur eine Ausnahme ist in dieser Beziehung zu verzeichnen, und eine solche scheint der Buddha zu sein. Er hat eine Inkarnation durchgemacht, die in der vorchristlichen Zeit verlaufen war, hat also nicht auf irgendeine Art mitgemacht, was durch das Ereignis von Golgatha auf die Erde gekommen ist.",
      "Wenn wir nun dem dort nachgehen, wo sich uns ein Dunkel ergibt, wo wir nicht verstehen können, wie doch eine Seele in einem bestimmten Zeitpunkt Abschied nimmt von der Erde, auf der Erde nicht miterlebt das Mysterium von Golgatha - wer meine früheren Vorträge gehört hat, wird wissen, daß der Buddha es in anderen Welten miterlebte, aber es handelt sich hier um das irdische Miterleben -, wenn wir uns das alles vor die Seelenaugen halten und dem nachgehen, dann stellt sich heraus, daß der Buddha auf den Planeten, wo er in seiner vorirdischen planetarischen Tätigkeit gewirkt hat, von der Zentralindividualität des ganzen Planetensystems geschickt war, von dem Mittelpunktsgeist, von dem, was wir den kosmischen Christus nennen. In uralten Zeiten war der Buddha aus- gesendet worden, um auf einem anderen Planeten zu wirken, um",
      "dann - infolge dieses Wirkens - auf der Erde zu wirken. Und während die Erde der Planet ist, der zum Schauplatz des Mysteriums von Golgatha geworden ist, ist Mars der Planet, auf dem` der Buddha ein ähnliches Ereignis zu vollbringen hatte nach dem, was er auf der Erde zu wirken hatte.",
      "Diese Dinge liegen scheinbar weitab und scheinen dem zu widersprechen, wenn gesagt wird, man könne mit dem gesunden Menschenverstand das begreifen, was aus der Initiation herausgeholt wird. Man soll aber nur einmal alles zusammennehmen, was die Geschichte bietet, und alle Zusammenhänge auffassen, dann wird man sehen, daß der äußere Verlauf der Geschichte eine Bestätigung alles dessen bietet. Und wenn jemand sagt, daß darin keine Bestätigung dieser Dinge liegt, so wendet er nur die gesunde Urteilskraft nicht genügend an. Das tun ja allerdings viele Menschen in unserer Zeit.",
      "Ich wollte mit alledem, was gerade in diesem Vortragszyklus gesagt worden ist, auch davon eine Vorstellung hervorrufen und wollte schon durch die Dramen zeigen, wie in der Tat ganz anders, gewaltig und groß die Welten sind, in die wir eintreten, wenn wir die Pforte zu den übersinnlichen Welten durchschreiten, und ich wollte eine umfassendere Vorstellung davon hervorrufen, als es durch bloße Theorien und Dogmen geschehen kann. Ich wollte manches nicht bloß durch Wortcharakteristiken darstellen und beschreiben, sondern ich wollte eine Empfindung von dem hervorrufen, was hinter der Schwelle ist, wo der Hüter der Schwelle steht. Wenn jemand in unserer heutigen Zeit das Geistesleben überblickt, so geht ihm vielleicht besonders in die Seele herein, was über den Hüter der Schwelle zu sagen ist. Der Hüter steht an der Schwelle, weil die im gewöhnlichen Sinnensein drinnenstehende Menschenseele nicht reif ist zu erleben und zu erfahren, was in den übersinnlichen Welten vorgeht. Er steht zum Schutze da. Das ist ebenso wahr, wie es wahr ist, daß die in die Zukunft hinein lebende Menschenseele mehr und mehr wird erfahren müssen von den übersinnlichen Welten. Warum steht der Hüter da? Weil die Menschenseele, wenn sie unreif den Schritt in die übersinnlichen Welten hinein machen würde - was niemals auf einem gerechten okkultistischen Wege geschehen",
      "kann -, sich unendlicher Furchtsamkeit, unendlichem Schrecken verfallen glauben würde, weil die Menschen aus ihrer Kleinheit, aus ihrer Unreife, aus ihrer Liebe und ihrem Hang zur Sinneswelt nicht ertragen würden, was alles mit dem Eintritt in die übersinnlichen Welten zusammenhängt. Kann man doch nicht einmal denen gegenüber, die fortgeschritten sein wollen, mit dem kommen, was Anspruch erhebt an unsere Zeit!",
      "Von der Stätte aus, von der wir bis jetzt noch die übersinnlichen Wahrheiten verkünden dürfen, mußten wir darauf hinweisen, wie ein übersinnliches Ereignis mit dem übersinnlichen Leib des Menschen im Laufe des zwanzigsten Jahrhunderts eintreten wird, indem die Menschen - wie durch ein Naturereignis - den wiedererscheinenden Christus finden werden. Darauf konnten wir hinweisen.",
      "Aber dieser wiedererscheinende Christus wird nicht auf Schiffen über Meere oder in Eisenbahnen fahren, wird auch nicht im Luftballon fahren, sondern er wird im Individuellen des Menschen - in dem, was von Menschenseele zu Menschenseele geht, und je nachdem, wie die Menschenseelen selbst beschaffen sind - mit den Mitteln erkannt werden, die im Ätherischen gegeben sind. Was wir so sagen dürfen, wie die Erscheinung des wiedererscheinenden Christus sein werde, erweist es sich schwach gegenüber dem, was rein aus der übersinnlichen Welt heraus an die Menschenseele herankommen wird.",
      "Denn die Menschen lieben es, mit sinnlichen Augen zu sehen den Großen, der da kommen soll; sie lieben es, sich vorzustellen, daß er im Aeroplan fährt, daß er über die Meere fährt, lieben es, sinnlich greifen und fassen zu können den, der da kommen soll. Warum ist das?",
      "Weil es sie in Angst versetzt, wirklich mit den übersinnlichen Welten in Berührung zu kommen. Dem Okkultisten stellen sich auch solche Dinge, wie sie geschehen, als maskierte Furcht und Angst vor dem Wahren dar.",
      "Das sei ohne Emotion gesagt, nur als eine Hinstellung des Objektiven. Da wird dann der Okkultist, der den Hüter an der Grenze zwischen Sinnensein und Geistessein erkennt, merken, daß die, welche draußen im gewöhnlichen Leben stehen, es nicht fassen können, daß überhaupt ein Anfang gemacht werden soll mit dem Schreiten in die übersinnliche Welt.",
      "Denn furchtsame Persönlichkeiten sind",
      "sie im Grunde genommen alle. Ihre Furchtsamkeit ist ihnen unbekannt, aber sie maskiert sich ihnen als die besondere Art von Wahrheitssinn, als ein materialistischer Wahrheitssinn. Als ein gewisser Haß, eine Wut, ein Entbranntsein der Kleinheit gegen die andern, die übersinnlichen Welten, erscheint sie bei denen> die sich entgegenstellen der Erkenntnis der übersinnlichen Welt und der über- sinnlichen Wesenheiten.",
      "So mag es kommen, daß auf der einen Seite die stehen, welche die übersinnlichen Welten erkennen wollen, und auf der anderen Seite die, welche nichts davon wissen wollen, oder die sagen werden: die objektive Wissenschaft sagt nichts von den übersinnlichen Welten, denn man kann sie nicht beweisen. Und dasselbe ist es, was auch andere Menschen abhalten wird, hinzugehen zu dem Hüter der Schwelle, nämlich die populären Nachtreter der Wissenschaft, welche da sagen, daß sie die übersinnlichen Welten ablehnen, weil es bei ihnen Wahrheitssinn, persönliche wissenschaftliche Überzeugung sei.",
      "Es ist aber die Furcht, die sie nicht an den Hüter der Schwelle herankommen läßt, und es ist die ganze Kraft dieser Furcht dahinein maskiert, was sich heute als ein Kampf auftun möchte gegen das Herankommen dessen, was aus den übersinnlichen Welten als das Geisteslicht gegenüber dem Lebensdunkel kommen soll. Das ist eine Vorstellung, welche der empfindet, der den Hüter an der Schwelle des Geistesseins kennt und der da weiß, welche Bedeutung die übersinnlichen Erkenntnisse für das ganze Geistesleben der Gegenwart haben.",
      "Warum sitzen Sie hier? Weil ein Strahl des Geisteslichtes in Ihre Seele gezogen ist, der Ihnen sagt, daß übersinnliches Wissen die Menschenseele ergreifen muß. Und weil immer lebendiger und lebendiger geworden ist, was dieser Strahl des Geisteslichtes sagt, deshalb vermehrt sich die Zuschauerschaft und Zuhörerschaft bei unseren Veranstaltungen. Wird man dem natürlichen Sprechen des Geisteslichtes zu den Seelen freien Lauf lassen, so wird es einstrahlen können in die Seelen. Wird man bei den Gegnern der übersinnlichen Erkenntnis draußen siegen, dann wird sich vielleicht das Geisteslicht für eine Weile verdunkeln müssen, wird sich zurückziehen müssen, gezwungenerweise, das heißt es müßte zurückgezogen werden,",
      "um diesen törichten Ausdruck zu gebrauchen. Dann wird die Welt eine Weile den Zusammenhang zwischen dem Lebensdunkel und dem Geisteslicht entbehren müssen. Allerdings ist es auch wieder notwendig, daß die, welche etwas von dem Geisteslichte wissen sollen> noch etwas lernen: daß sie lernen, mit Wahrhaftigkeit auf dasjenige zu schauen, was schon hier in der äußeren Welt aus der geistigen Welt geboten wird. Wer sich heute noch blenden läßt von dem, was pro und contra in bezug auf übersinnliche Erkenntnis gesagt wird, wer nicht in der Seele den festen Impuls aus der übersinnlichen Welt sucht, der nur aus der übersinnlichen Welt selber kommen kann, der wird nicht diesen Impuls finden können.",
      "Ich habe es öfter gesagt, was an Literatur nunmehr vorhanden ist, was durch die Gnade der Meister der Weisheit und des Zusammenklanges der Empfindungen in manchem Literaturwerke gegeben werden durfte, das enthält im Grunde genommen das, wovon man sagen darf, daß es in Gnade den Menschen mitgeteilt werden durfte. Und wenn ich von diesem Augenblicke an nichts weiter schreiben und sprechen könnte: wenn man nur das Vorhandene ausbaut - wenn ich auch selber nicht dabei sein könnte -, wenn man sucht, was mit allem gemeint ist, so wird man finden> was man braucht.",
      "Und damit ist - wenn ich jetzt am Schlusse dieser Vorträge von dem Zusammenhange des persönlichen Karma mit dem Karma dieser Geistesbewegung sprechen darf - auch die Möglichkeit gegeben> daß in einer gewissen Beziehung das nicht mehr ausgelöscht werden kann, was - nicht als «Steinerische Richtung», denn die gibt es nicht, sondern als objektiver Okkultismus in die Welt gekommen ist. Mag noch soviel von Gegnerschaft herankommen, das kann sich nicht beziehen auf das Auslöschen des Okkultismus für die Zukunft, denn es wird doch bleiben, was da ist.",
      "Dafür sehe ich denn doch einen Beweis darin, daß unsere Zeit eine spirituelle Bewegung braucht und daß doch eine Spanne Zeit gegeben ist, wo durch die Gnade unserer spirituellen Hüter dieses Geistesgut in die Sinneswelt hat herabgebracht werden können. Mögen sich Gegner ergeben!",
      "Vielleicht wird gerade durch diese Gegnerschaft das Nötige getan! Und verzeihen Sie den Ausdruck: Gar mancher, der heute willig das theosophische",
      "Geistesgut hinnimmt, der davon beglückt ist: gegenüber dem, was er in der Gegenwart sehen sollte, ist er doch unaufmerksam, da hat",
      "er doch die Schlafmütze auf! Da verpflichtet sich manclier nicht gegenüber der Wahrheit zu der Unterscheidung, was die alleinige Wahrheit sein soll. Vielleicht wird gerade ein klein wenig Verfolgung, die auch nicht schaden kann, dazu beitragen, daß mancher, der die Schlafmütze nicht nur über den Kopf, sondern auch über Augen und Ohren gezogen hat, sie sich dann vom Kopfe herunterziehen wird. Vielleicht wird auch das notwendig sein.",
      "Wie aber die Dinge gehen mögen: jetzt, wo wir am Ende dieses Zyklus stehen - wo so manches an uns herangetreten ist, notwendigerweise, zwangsweise herangetreten ist, was im Grunde genommen widerwärtig ist -, jetzt wollen wir, wie wir es sonst immer tun, daran denken, daß wir wieder einiges von dem spirituellen Leben aufgenommen haben. Jetzt gehen wir wieder auseinander, einer dahin, der andere dorthin, aber das Geisteslicht, nach dem wir alle streben und suchen innerhalb des Lebensdunkels, das läßt uns zusammensein überall, wo wir auch örtlich getrennt sein mögen.",
      "Die Seelen, die hier sitzen, mögen sie ihre Zusammengehörigkeit fühlen im Nacherleben, im Nachmeditieren des Gehörten oder in bezug auf das, was sich an gegenseitiger Liebe gezeigt hat, im Nachleben. Physisch waren wir zusammen, physisch werden wir nicht immer so zusammensein können.",
      "Übersinnlich sind wir zusammen. Lernen wir übersinnlich zusammensein, damit wir das Dasein der übersinnlichen, der überphysischen Welt beweiskräftig machen können! Wenn wir solche Gefühle mitnehmen, nachdem wir solange zusammen waren, dann werden die Seelen das mitnehmen, was Theosophie als das Beste den Menschen mitgeben kann: die Liebe, die aus der spirituellen Wahrheit selber herauskommt.",
      "Und wenn auch zwischen jetzt und derjenigen Gelegenheit, bei der wir wieder so zusammensein möchten, das eine oder andere geschehen mag: das kann doch geschehen unter allen Umständen, daß sich unser physisches Zusammensein in das rechte spirituelle Zusammensein bei örtlichem Auseinander verwandeln werde, damit wirke, lebe und gedeihe in uns das spirituelle Geistesgut. Wir haben doch auch Menschen",
      "der allverschiedensten Denkweisen in unserer Mitte gehabt, aber auch solche Menschen, über deren Erscheinen wir uns immer auch dann freuen, wenn sie etwa gegensätzliche Meinungen in unsere Mitte hineinbringen. Doch nicht um Meinungen und um Gegensätze der Meinungen handelt es sich, sondern um ehrliches, aufrichtiges Wahrheitsgefühl, um, man möchte sagen, ein Verschworensein zur Wahrhaftigkeit und Ehrlichkeit, zur Wahrhaftigkeit und Ehrlichkeit schon im Sinnensein. Daß ich dieses sage, betrachten Sie nicht als etwas, was notwendig erfolgen muß aus dem Thema unseres Vortragszyklus. Was aber notwendig ist, das ist, daß wir auf mancherlei Gebieten das Wahrheitssuchen in unserer Zeit, überhaupt in unserer Gegenwart, haben erleben können.",
      "Und wozu sich im Anfange des Vortragszyklus für mich selbst weniger Gelegenheit gefunden hat, das sei hier am Ende berührt: der",
      "Dank gegenüber denjenigen Persönlichkeiten, die vor allen Dingen auch als offizielle Persönlichkeiten innerhalb unserer unoffiziellen Veranstaltungen erschienen sind. Ich kann nicht alle im einzelnen nennen. Sie haben gestern selber gehört die freundliche Einladung",
      "für den nächsten Kongreß der europäischen Sektionen der Theosophischen Gesellschaft unseres lieben Generalsekretärs der Skandinavischen Sektion, und es haben einige von Ihnen vielleicht auch die Worte des Generalsekretärs der Ungarischen Sektion vernommen. Diesen Persönlichkeiten, worauf wir besonders hinzuweisen haben, ist der Gruß schon an dem ersten Vortrage dargebracht worden, und die, welche ungenannt bleiben mußten, sollen wissen, daß sie in unseren Herzen das aufrichtigste Willkommen gefunden haben, und daß wir ihr Hiersein als eine Bekräftigung dessen auffassen, daß sie doch noch nicht der Anschauung sind, daß wir so schlimme Menschen sind, wie es jetzt beginnt in der Welt dargestellt zu werden. Wie wir also auch im nächsten Jahre beisammen sein mögen, wie sich die Dinge auch gestalten mögen, fassen wir das diesjährige Zusammensein als den Keim zu etwas auf, was uns vielleicht durch alles, was da kommen mag, doch nicht genommen werden kann. Was Ihre Seelen selber aus freiem inneren Erleben als Nachklang empfinden können, womit Sie zurückblicken auf diese Tage von",
      "München, das ist es, woran ich in diesem Augenblicke appellieren möchte, eines jeden Freundes einzelne Seele herzlich begrüßend zum Abschied und zum Wiedertreffen in dem Sinne, wie sich Leute, die sich durch Erkenntnis lieben gelernt haben, immer zusammenfinden und zur rechten Zeit immer wieder treffen müssen."
    ],
    "sentences": [
      [
        "Die gestrige Betrachtung konnten wir damit schließen, daß ein Hinweis gegeben wurde auf die Stellung des einzelnen Menschen zu dem, was Beschreibung der übersinnlichen Welt genannt werden kann, was aus den Forschungen, aus den Beobachtungen, aus den Erlebnissen der Initiation kommt.",
        "Und es ist darauf aufmerksam gemacht worden, daß sehr leicht das Urteil zustande kommen könnte, ein Wert und eine Bedeutung für das Seelenleben mit den Ergebnissen der Initiation könnte doch eigentlich nur für denjenigen verbunden sein, der selber die ersten Schritte zur Initiation gemacht hat und imstande ist, durch eigenes Schauen in das Erleben, in die Beobachtung der höheren Welten hineinzudringen."
      ],
      [
        "Es ist schon öfter betont worden, daß dies nicht so ist, daß man allerdings nur dann anschauen, beobachten, erkunden und erforschen kann, was in den höheren Welten vorgeht, wenn man das eigene Selbst, die eigene Seele so umgestaltet hat, daß man in jene anderen Welten hinein- blicken kann, die zwar ganz anders sind als unser Sinnensein, die aber mit unserem Sinnensein - wie gestern erwähnt worden ist - doch in dieser oder jener Beziehung zusammenhängen, vor allem aber als seine Grundlage anzusehen sind.",
        "Was dagegen das Begreifen, das Verstehen dieser anderen Welten betrifft, so wäre es ein falsches Urteil, wenn man behaupten wollte, zu dem Verstehen, zu dem Begreifen, zu dem Entgegennehmen dessen, was derjenige geben kann, der die ersten oder die weiteren Schritte zur Initiation gemacht hat, gehöre selber Erleben."
      ],
      [
        "Vielmehr muß immer wieder und wieder betont werden, daß jeder Mensch, der nur unbefangen sich dem hingibt, was von den eigentlichen Geistesforschern in den übersinnlichen Welten erkundet wird, der unbefangen ihre Beschreibungen, Erfahrungen und Mitteilungen aufnimmt und wirklich unbefangenes Urteil, unbefangene Verstandestätigkeit walten läßt, alles, was ihm gegeben werden kann, auch begreifen kann.",
        "Für das Sinnensein sind wir in einem ganz anderen Fall."
      ],
      [
        "Es ist durchaus berechtigt zu"
      ],
      [
        "sagen, daß kaum ein Mensch aus einer Beschreibung heraus begreifen wird, was die Sixtinische Madonna ist oder was eine ferne, fremde Landschaft ist.",
        "Man wird sich, wenn man eine lebendige Phantasie hat, aus einer solchen Beschreibung eine Vorstellung bilden können, aber berechtigt bleibt doch der Ausspruch, daß der erst das, was im Sinnensein ist, begreift, der selbst zum Anschauen kommen kann, so daß für das Sinnensein das Begreifen dem Anschauen nachfolgen muß.",
        "Das ist für die höheren Welten durchaus nicht so.",
        "Da kann durch die Forscher, was sie erkunden, aus den höheren Welten herausgeholt werden, kann in die Formen und Begriffe menschlicher"
      ],
      [
        "Ideen gebracht werden und so der Welt gegeben werden.",
        "Da kann man dann selbstverständlich in materialistischen oder sonstigen Dogmen befangen sein, oder man kann überhaupt keinen Willen haben zur Unbefangenen Hingabe an das, was da mitgeteilt wird; dann wird man es nicht begreifen.",
        "Es kann durchaus sein, daß man gar keine Schuld daran hat, daß man es nicht begreifen kann, weil ei- nem das bisherige Leben und die bisherige Erziehung nicht die Möglichkeit gegeben haben, sich unbefangen diesen Dingen hinzugeben.",
        "Aber jeder, der in der Lage ist, sich diesen Dingen unbefangen hin- zugeben, unbefangen alles zusammenzuhalten, was gesunde Vernunft"
      ],
      [
        "und gesundes Urteil gibt, wird sich zuletzt sagen: wenn auch die Dinge zuerst noch so unglaublich scheinen, gerade gesundes, umfassendes und allseitiges Denken fÜhrt zum Begreifen derselben, wenn man auch noch nicht das Allergeringste aus den höheren Welten zu schauen vermag."
      ],
      [
        "Wie ich Ihnen in diesen Tagen mitteilen konnte, daß der, welcher zu einem Schauen der geistigen Welt kommt, in seinem Innensein die Abbilder dessen trägt, was er selbst in seinem Innern hat, ja, zuerst geführt wird durch das, was er in sich zuerst als Bilder hat, so ist es mit dem Begreifen der Dinge der übersinnlichen Welten: das Begreifen geht dem Schauen voran und ist in keiner Weise beeinflußt vom Schauen, noch beeinflußt es selbst das Schauen.",
        "Das vorherige Begreifen braucht nicht im geringsten Maße zu beeinflussen, was den Menschen dann zum völlig unbefangenen, wahrheitsgetreuen Schauen bringt.",
        "Ein vorheriges Begreifen, ein Erfassen mit allseitiger"
      ],
      [
        "Urteilskraft - zu dem allerdings unsere Zeit in den weitesten Kreisen durchaus keine Neigung hat - wird dagegen die Seele, das Gemüt vorbereiten, um auch in der entsprechenden Art in das Schauen eintreten zu können.",
        "Daher muß immer wieder und wieder gesagt werden: Wahrer Okkultismus, wahre Geisteswissenschaft, die es ernst und ehrlich meint, wird sich niemals zurückziehen vor der Aufforderung, man begreife, man verstehe unbefangen das, was gesagt ist.",
        "Man suche darin einzudringen mit dem gesunden Menschenverstand, mit der sich in alle Gebiete frei ergießenden Urteilskraft, und man wird es können.",
        "Mancherlei über diese Sachen finden Sie in der Schrift «Ein Weg zur Selbsterkenntnis des Menschen», in der manches zur Ergänzung dieser Vorträge enthalten sein wird.",
        "Aber insbesondere soll es erwähnt werden, daß ein Bedeutendes beigetragen werden kann zur Läuterung, zur Reinigung der Seele, wenn vor allen Dingen diejenigen, welche den Weg zur Geisteswissenschaft aus dem Lebensdunkel heraus suchen, objektiv zu verstehen, objektiv zu begreifen versuchen mit dem, was jedem Menschen, wenn er nur will, als eine gesunde Urteilskraft zur Verfügung stehen kann.",
        "Dieser Weg des gesunden Begreifens, des Ablehnens einer jeglichen Autorität und eines jeglichen Autoritätenglaubens gewinnt noch dazu ein besonderes Licht, wenn man eingeht auf gewisse Feinheiten der okkulten Beobachtung."
      ],
      [
        "Aus dem ganzen Sinn und Geist dieser Vorträge ist ja hervorgegangen, daß es sich bei den Schritten, die zur Initiation gemacht werden, immer mehr und mehr für jeden Menschen darum handelt, daß er unabhängig wird in seinem Erleben von dem, wozu ihm sein physischer Leib als Werkzeug dienen kann, daß er zu erleben lernt in seinen höheren Leibern, in seinem elementarischen oder ätherischen Leibe, in seinem astralischen Leibe, auch in dem, was man seinen Ich- oder Gedankenleib nennen kann.",
        "Auf dieses Sich.Fähigmachen, um in seinen höheren Leibern wahrzunehmen, kommt es insbesondere bei allen Schritten der Initiation an.",
        "Dabei ist es aber notwendig, daß der Mensch etwas dazu tut, um sich freizumachen vom sinnlich-physischen Leibe, daß er bewußt alles dasjenige von sich abstreift, von sich abzieht, was ihn so mit der Welt in Zusammenhang"
      ],
      [
        "hält, wie dieser Zusammenhang sich nur durch das Werkzeug des physischen Leibes ergibt.",
        "Das ist natürlich namentlich in einem Zeitalter, das so materialistisch ist wie das heutige, nicht für alle Menschen möglich, besonders für die, welche sich heute auch ein Urteil über die Weltenrätsel, über die Weltenerscheinungen zuschreiben, und die durch die sonderbare heutige Erziehungsweise zu dem Glauben verzogen werden, daß man in frühester Jugend schon ein umfassendes Urteil - nicht bloß ein Streben - über die Welterscheinungen gewinnen könne."
      ],
      [
        "Warum wird heute durch unreife, durch rein aus der Leidenschaft und Emotion herausgeborene Urteile in der Welt soviel Unheil angerichtet?",
        "Wenn man die Welterscheinungen über- schaut, dann sieht man, daß der Druckmarkt mit den unreifsten Dingen überschwemmt wird, die aus nichts anderem herausgeboren sind als aus Sympathien und Antipathien."
      ],
      [
        "Warum das?",
        "Man kann die Frage aufwerfen: Hat es nicht früher auch Menschen gegeben, die den reinen Errungenschaften übersinnlicher Forschung mit Haß und Abscheu aus ihrem Lebensdunkel heraus gegenüberstanden wie in unserer Zeit?"
      ],
      [
        "Hat es nicht Dunkelmänner gegeben, wie es die heutigen Materialisten sind, die alle möglichen Mittel, welche Haß, Unwissenheit und Finsternis eingeben, anwandten?",
        "Ja, die hat es immer gegeben.",
        "Aber in der Weise, wie sie heute wirken, haben sie nicht gewirkt."
      ],
      [
        "Warum nicht?",
        "Solche Dinge muß man sich auch manchmal ins Gewissen schreiben.",
        "Die Menschen waren da, die die höheren Welten und unbefangenes Eindringen in diese Welten gehaßt haben, weil eben das unbefangene Eindringen in die höheren Welten zuweilen für die Menschen recht unangenehme Tatsachen zutage bringt."
      ],
      [
        "Aber diese Menschen haben oftmals nicht schreiben und lesen gekonnt.",
        "Ihr Bildungsniveau entsprach dem Nichtschreiben- und Nichtlesenkönnen.",
        "Heute müssen die> welche so denken, vermöge ihrer Bildung schreiben und lesen können, und das große Publikum hat kein Unterscheidungsvermögen, um das, was auf dem Büchermarkt erscheint, wirklich richtig auffassen zu können, und es ist auch nicht viel Wille vorhanden zu einem solchen Unterscheidungsvermögen, um erkennen zu können, daß hier sichtend und klärend das Urteil einer okkultistisch - geisteswissenschaftlichen"
      ],
      [
        "Bewegung in unserer Zeit eingreifen muß.",
        "Man wird da manches lernen müssen, was den Menschen hart ist zu lernen.",
        "Einfach aus den Tatsachen, die sich aus der übersinnlichen Welt heraus ergeben, wird man manches lernen müssen."
      ],
      [
        "So wird man zum Beispiel lernen müssen, daß - auch dann, wenn man in die höheren Welten eindringt durch gewisse partielle Schulung oder Zubereitung seines seelischen und sonstigen Organismus - noch mancherlei zurückbleiben kann in bezug auf jenen Zusammenhang mit der Außenwelt, der nur auf dem Umwege durch den physisch-sinnlichen Leib zustande kommt.",
        "Alles, was so in einem geistigen Schauer, wenn man die Grenze überschritten hat, die zwischen dem Sinnensein und dem Geistessein so fest gezogen ist, von gewissen berechtigten Schwächen des Sinnenseins zurückbleibt, hüllt uns in Finsternis und Maja, wenn wir es erleben beim höheren geistigen Schauen.",
        "Nur wer unablässig mit sich zu Rate geht, wie er das, was er im Sinnensein haben muß, weil er ein Wesen der Sinneswelt ist, für 'jene Zeiten, da er geistig schauen muß, völlig ausschalten kann, und wie er es dazu bringen kann, daß beim geistigen Schauen nichts von dem hereinspielt, was ihn in der Sinneswelt umgibt, nur der kann wirklich rein und majalos die geistige über- sinnliche Welt schauen."
      ],
      [
        "Nehmen wir einen bestimmten Fall, ohne daß dabei auf irgend etwas angespielt werden soll.",
        "Irgend jemand, der die Schritte zur Initiation durchmachen will oder schon durchgemacht hat, habe ein persönliches, auf unmittelbare persönliche Gefühle, persönliche Emotionen beruhendes Verhältnis zu einem anderen Menschen.",
        "Nehmen wir an, in einem solchen Verhältnis eines geistigen Erschauers, eines erst zu Initiierenden oder schon mit gewissen Schritten der Initiation Ausgestatteten wäre es so, daß er von Mensch zu"
      ],
      [
        "Mensch ein bestimmtes persönliches Verhältnis hätte, ein Verhältnis, das auf Zuneigung beruht, auf solcher Zuneigung, welche im Sinnensein geschlossen wird, sagen wir auf einer zutraulichen Liebe, die im Sinnensein erwacht, die von Leib zu Leib spielt - im höheren Sinne, nicht nur im niederen Sinne, denke ich dabei.",
        "Nehmen wir an, so etwas wäre vorhanden und ein solcher geistiger Schauer würde"
      ],
      [
        "nun etwas erforschen wollen von der Persönlichkeit, zu der er eine persönliche Zuneigung hat, die sich im Sinnensein gebildet hat, und nehmen wir an, er wäre nicht in der Lage, alles vdn sich abzustreifen, was von im Sinnensein erschaffener Liebe zu der betreffenden Persönlichkeit da ist, dann ist es fast ganz unmöglich, die Wahrheit in bezug auf das übersinnliche Sein einer solchen Persönlichkeit zu erfahren.",
        "Oh, es ist notwendig, auf Schritt und Tritt zu versuchen - und wenn man noch so sehr liebt und noch so sehr persönliche Zuneigung hat im Sinnensein -, alles abzustreifen für die Zeiten, wo man das Übersinnliche Dasein betrachten will."
      ],
      [
        "Es ist möglich, daß man eine solche persönliche Zuneigung hat und nicht abstreift, daß man in der Weise, wie es im Sinnensein ist, die betreffende Persönlichkeit gern hat.",
        "Dann stellen sich einem solchen geistigen Schauer zum Beispiel über Vergangenheit und Zukunft dieser Persönlichkeit Bilder vor Augen, die unter allen Umständen falsch sein müssen, dann kann eine ganze Fülle von Maja auftauchen."
      ],
      [
        "Darum kann der, welcher es ernst und verantwortungsvoll mit dem nimmt, was der Welt auf dem Felde geistiger Weisheit gegeben werden soll, nicht vorsichtig genug sein, vor allen Dingen etwas der Welt zu verkünden, was im Umkreise des Familiären, des unmittelbar Bekannten stattfindet.",
        "Man kann sich überall sichern in der Weise, daß, wenn auf okkulte Ergebnisse hingewiesen wird, die sich auf etwas beziehen, das den unmittelbar persönlichen Umkreis des Untersuchers betrifft, diese im höchsten Maße demjenigen zweifelhaft erscheinen sollten, der sie entgegennehmen soll."
      ],
      [
        "Das ist nicht etwas, was mit Anspielung auf diese oder jene Tatsache gesagt werden soll, sondern was gesagt werden soll, weil es eine objektive Tatsache für jeden Okkultisten ist.",
        "Damit hängen aber Dinge zusammen, welche durchaus, man möchte sagen, in höhere Gebiete hinaufspielen.",
        "Damit hängt zusammen, daß der, welcher in den übersinnlichen Welten forschen will, wenig geeignet ist, eine gewisse Grundvorstellung richtiger Art in bezug auf religiöse Fragen zu erhalten, wenn er mit seinen Vorurteilen, mit seinen persönlichen Gefühlen irgendeiner besonderen Religionsgemeinschaft zugetan ist, wenn er eine Religionsgemeinschaft mehr liebt als die andere"
      ],
      [
        "oder sich gar zum propagandistischen Träger einer Religionsgemeinschaft macht.",
        "Wer zur persönlichen Propaganda neigt, kann nicht zugleich objektiver Okkultist sein!",
        "Das ist ein Satz, der auch einmal in aller Schärfe ausgesprochen werden muß.",
        "Es sind Bedingungen da, die wir mit unserem Karma der abendländischen Kultur in Zusammenhang bringen dürfen, Bedingungen, welche es in einer gewissen Weise dem Abendländer, wenn er sich ein wenig bekannt macht mit den Grundanforderungen des übersinnlichen Lebens, doch nicht gar zu schwer machen, ein objektives Urteil zu gewinnen gerade über die Hineinstellung des größten Ereignisses in die Menschheitsevolution, das wir das Mysterium von Golgatha nennen.",
        "Wodurch kommt denn in das religiöse Leben und in seine Auffassung so manches Lebensdunkel hinein?",
        "Wodurch kommt das hinein, was nur mit dem Augenblick zu tun haben will und sich nicht zu Geisteslicht und Ewigkeit gerade im religiösen Leben erheben will?",
        "Das kommt davon her, weil mit alledem, was menschliche Egoismen sind - und nun nicht bloß Egoismen der einzelnen, sondern auch Egoismen der Stämme, der Rassen, der Völker -, dasjenige innig zusammenhängt, was sich auf das religiöse Leben bezieht.",
        "Von diesem Gesichtspunkte aus möchte ich Sie auf eine Erscheinung aufmerksam machen, denn notwendig ist es, daß man diese Dinge völlig unbefangen betrachtet."
      ],
      [
        "Welche Rolle spielt das religiöse Leben bei einem Orientalen in bezug auf seinen Religionsstifter, wenn er den Zusammenhang seiner Rassen- oder nationalen Evolution in Betracht zieht?",
        "Untersuchen Sie einmal, ob ein Orientale oder irgendein Nichtabendländer so leicht geschichtlich denken kann über den geschichtlichen Verlauf, in den er hineingestellt ist, ohne dieses geschichtliche Leben an- zuknüpfen an Krishna, Buddha, Mahomet, Konfuzius oder dergleichen?",
        "Überall sehen wir ganz selbstverständlich das, was im religiösen Leben sich abspielt, mit dem verbunden, was im profanen äußeren Leben geschieht und in den Gemütern der Leute fließt.",
        "Man kann sich eine Geschichtsschreibung eines Buddhisten zum Beispiel nicht denken, ohne daß er in den Mittelpunkt derselben den Buddha stellt.",
        "Das sei nicht als eine Kritik gesagt, sondern weil es für diese"
      ],
      [
        "Menschen richtig ist, die solchen Kulturentwickelungen angehören.",
        "Jetzt gehen wir ins Abendland und sehen nicht auf Dogmen, sondern auf Tatsachen.",
        "Ich greife heraus einen anerkannten`Geschichtsschreiber des Abendlandes: Leopold von Ranke, der in aller Welt bekannt ist durch seine Objektivität, seine ruhige Würdigung, seine ganz besondere Art, sich objektiv zu den Dingen zu stellen."
      ],
      [
        "Ranke hat manches Kapitel der geschichtlichen Entwickelung geschrieben.",
        "Doch von Ranke ist etwas sehr Merkwürdiges bekannt geworden.",
        "Einem Freunde gegenüber hat er sich darüber geäußert, daß er doch den geschichtlichen Verlauf so dargestellt hat, daß er nirgends in Betracht zieht den Christus und die Tatsachen, die sich unmittelbar an den Christus anschließen!"
      ],
      [
        "Ranke hat sich bemüht, durch seine Objektivität eine Geschichte des Abendlandes zu schreiben, ohne daß er den Christus hat hineinspielen lassen.",
        "Und es hat ihm manche schwere Gewissenspein im Alter gemacht, daß er sich sagen mußte: Ja, wenn nun doch in das Geschehen jene Taten hineinfließen würden, über die keine Dokumente und Urkunden vorhanden sind, ist dann diese Geschichte wahr? - Nicht darum soll das hier angeführt werden, um auseinanderzusetzen, ob sie wahr oder falsch ist - denn ich halte sie in hohem Maße für berechtigt -, sondern weil es eine der besten Geschichten eines der anerkannten Geschichtsschreiber im Abendlande gibt, die Geschichte 5Q geschrieben haben, daß man den Christus herausgelassen hat, daß man den Christus nicht in die Historie mit hineingenommen hat."
      ],
      [
        "Das ist eine fundamental wichtige, eine bedeutsame Tatsache!",
        "Wohin hat die abendländische Kultur geführt?",
        "Die abendländische Entwickelung hat dazu geführt, daß hier nicht immer zu einem Wesen aufgeschaut wird, das wie eine Mittelpunktfigur der ganzen Geschichte dastehen würde, wenn man daran anknüpfen würde."
      ],
      [
        "Wissenschaft hat nicht dazu geführt!",
        "Warum kam das?",
        "Beleuchten wir diese Tatsache von einem anderen Gesichtspunkt aus."
      ],
      [
        "Wo haben die großen Religionsstifter gelebt, welche die großen Initiierten waren, die ihren Völkern aus ihren Völkersubstanzen heraus das gaben, was sie brauchten?",
        "Ist es denkbar, daß zum Beispiel Hermes aus einer anderen Volkssubstanz heraus auf seine Epoche"
      ],
      [
        "gewirkt hätte, oder ist es denkbar, daß Buddha in einer anderen Weise gewirkt hätte als aus der Rasseneigentümlichkeit heraus, in die er hineingestellt war und in diese Rasseneigentümlichkeit hinein seine Kräfte gesendet hat?",
        "Und jetzt wenden wir den Blick zu dem, den wir keinen Initiierten nennen, sondern den wir kennen als die Persönlichkeit, auf welche die Welten-Initiation, die kosmische Initiation gewirkt hat."
      ],
      [
        "Gehört er irgendeinem Volke an? - In einem unbekannten Winkel der Welt, fern der großen Reiche, ist er geboren.",
        "Da spielten sich die Ereignisse ab.",
        "Und da man die Evangelien wie die anderen Urkunden des Neuen Testamentes als historische Urkunden bezweifeln kann, so kann man sagen: Von allen diesen Ereignissen wird nichts bezeugt durch irgendein historisches Dokument."
      ],
      [
        "Und die, welche sich zu ihm als seine Jünger und Schüler gefunden haben, haben sich zu ihm gewendet ohne Unterschied von Stamm, Rasse, Geschlecht und so weiter.",
        "So ist der Unterschied!",
        "Während sich vorher die Völker zu ihren Rassen-Initiierten gewendet haben, haben sie sich hier zu einem gewendet, der keinem Volke angehört - ja, der sogar gerade seine größten Kulturtaten bei einem Volke verrichtet hat, bei dem er nicht gelebt hat."
      ],
      [
        "Das ist der große Fortschritt aus dem Lebensdunkel zum Geisteslicht, den man nicht verkennen sollte, wenn man es ehrlich meint mit der Evolution der Menschheit.",
        "Das sind Dinge, die durchaus in Betracht kommen, Dinge, auf welche diejenige Wissenschaft kräftig hinzuweisen hat, die aus der wirklichen Betrachtung der übersinnlichen Welten entnommen werden kann."
      ],
      [
        "Aus mancherlei von dem, was ich Ihnen sagen durfte, sehen Sie, daß es darauf ankommt, etwas von jenem Urteil zu verstehen, das des Johannes Thomasius Doppelgänger sagt - im «Hüter der Schwelle» -: Das Denken hat eine läuternde Kraft.",
        "Diese läuternde Kraft des Denkens wirkt aber auch so, daß sie wirklich aus dem Lebensdunkel in das Geisteslicht herausführt, daß sie wirklich von dem Augenblick zur Ewigkeit hinwegführt.",
        "Man will nur nicht gern dem Denken seine läuternde Kraft zugestehen.",
        "Denn es ist etwas Eigentümliches um die okkulte Natur dieses Denkens.",
        "Eine materialistische Wissenschaft glaubt, daß der Mensch etwa mit seinem Gehirn"
      ],
      [
        "denke.",
        "Er denkt nicht mit seinem Gehirn; das ist einfach ein Irrtum.",
        "Und wenn Sie den ganzen Sinn dessen kennenlernen, was in der Schrift «Ein Weg zur Selbsterkenntnis des Menschen» gesagt ist, so werden Sie auch begreifen, daß der Vorgang des Denkens, die Tätigkeit des Denkens, die Verbindung und Lösung von Ideen nicht im physischen Leibe abläuft, sondern im ätherischen oder elementarischen Leibe.",
        "In Wahrheit denkt auch der Mensch, der im gewöhnlichen Leben steht, mit seinem elementarischen oder ätherischen Leibe, nur bewirkt das Stehen im gewöhnlichen Leben, daß der Mensch kein Wissen haben kann von jener Tätigkeit, die in ihm vorgeht, wenn er denkt, aber nur im ätherischen Leibe vorgeht.",
        "Im Grunde genommen denkt der Mensch fortwährend, und fortwährend ist der ätherische Leib in Bewegung, und diese Bewegung bedeutet denken.",
        "Aber was kommt von alledem zum Bewußtsein, was so im ätherischen Leibe vorgeht?",
        "Es kommt nur das zum Bewußtsein, was davon gespiegelt wird.",
        "Sie müssen sich ein gewisses Verhältnis des elementarischen Leibes zum physischen Leibe in folgender Art vorstellen."
      ],
      [
        "Nehmen Sie an, Sie gingen in diesem Saale längs dieser Fensterreihe entlang.",
        "Nun denken Sie sich, überall an den Wänden zwischen den Fenstern hingen Spiegel.",
        "Indem Sie an jedem Spiegel vorbeigehen, zum Beispiel dreimal, sehen Sie Ihr Antlitz; wo kein Spiegel ist, sehen Sie von Ihrem Antlitz nichts.",
        "Wenn Sie wieder weitergehen zum nächsten Spiegel, sehen Sie es wieder.",
        "Da ist wieder ein Spiegel, der wirft Ihnen das Bild Ihres Antlitzes zurück.",
        "Ihr Antlitz ist immer vorhanden auf dem ganzen Wege, aber Sie sehen es nur, wenn es sich spiegelt.",
        "Der Ätherleib ist in fortwährendem Gedankenfluß.",
        "Aber wann nur wird dieser Gedankenfluß Wahrnehmung?",
        "Wenn das, was im physischen Leibe ist, das Gehirn, dasjenige spiegelt, was im ätherischen Leibe vorgeht.",
        "Was sonst immer da ist und wovon der Mensch gewöhnlich nichts weiß, das wird gespiegelt vom Gehirn, das wie ein Spiegelungsapparat aufzufassen ist.",
        "Und in all den Fällen, wo das Leben gespiegelt wird, wird es bewußt.",
        "Daher muß der physische Leib da sein, damit der ätherische Leib, der eigentlich denkt, von seinem Denken etwas wissen kann.",
        "Aber es denkt nicht"
      ],
      [
        "das Gehirn, und es denkt nicht der physische Leib.",
        "Sowenig als das, was im Spiegel erscheint, Sie sind, so wenig ist das, was der Mensch wahrnimmt im Gehirn, sein Denken, denn dieses Denken sitzt im elementarischen oder ätherischen Leibe.",
        "Und wenn der Mensch die ersten Schritte zur Initiation machen will, ist es im Grunde genommen so, wie wenn Sie vor der Spiegelung überall vorbeigingen und versuchten in sich selbst zu sein - und dann fähig würden zu empfinden, wie Ihre Form ist, so daß Sie sich dann von innen heraus wahrnehmen würden."
      ],
      [
        "So ist das Hinaufrücken vom Sinnensein zum Geistessein.",
        "Während der Mensch sonst nur das wahrnehmen kann, was in seinem Spiegelungsapparat vorgeht, was er als die Spiegelung in seinem Gehirn sieht, kommt er durch die Initiation zum direkten Erleben und Erfühlen im elementarischen Leibe."
      ],
      [
        "Wenn er aber zu diesem inneren Erleben und Erfühlen kommt, dann kommt er zum Beispiel mit einer ganz anderen Welt in Berührung: mit der Welt des Wesenhaften.",
        "Dann erweitert sich sein Sein, sein Erleben, sein Erfühlen über die objektive Welt hinüber."
      ],
      [
        "Aber was er dann erlebt, ist eine Welt geistigen Seins, das ist eine Welt, die er in bezug auf den Umfang des Erlebten auch im Sinnensein erleben kann.",
        "Aber da erst kann er dann hinaufsteigen, um im geistigen Sein etwas zu erfassen von dem, dessen Abbild nur im Sinnenbilde vorhanden ist."
      ],
      [
        "Und dann kann er begreifen, daß die Impulse der Initiierten nicht bloß aus dem Erden- wissen geflossen sind, sondern daß den großen Initiierten die größten Impulse, die moralischen Impulse und so weiter deshalb zukommen und mit so gewaltiger Kraft wirken, weil sie das, was sie haben, nicht bloß von der Erde nehmen, sondern von dem mitnehmen, was über die Erde hinausgeht.",
        "Denn sobald man über die Erde hinaus- kommt, kommt man auch zu dem, was mit dem Erdensein über die Erde hinaus verbunden ist."
      ],
      [
        "Und kommt man durch die Initiation vom Erdensein zum kosmischen Sein, dann kommt man dazu, daß, wenn man einen Initiierten wie zum Beispiel Buddha von diesem Gesichtspunkte aus studiert, man sagt: Er hat in vielen Inkarnationen als Bodhisattva auf der Erde gelebt.",
        "Und wer in dieser Beziehung den Buddhismus verstehen gelernt hat, der ist notwendigerweise"
      ],
      [
        "ebenso gläubig wie ein Buddhist und weiß, daß in der Persönlichkeit des Gotama Buddha diese Individualität zum letzten Male in einem physischen Leibe lebte, in dieser Inkarnatio`n aber der «Buddha» wurde und dann hinaufgestiegen ist in die geistigen Welten zum geistigen Wirken, so daß der geistige Blick hingelenkt werden kann auf den Übergang der Buddha-Individualität vom Erden- sein zum Geistessein, zu Zusammenhängen mit dem Geistessein.",
        "Und wenn man nun diese Individualität zurückverfolgt, so sieht man zwar, wie der Bodhisattva durch viele Inkarnationen geht, aber man kommt dann in eine frühere Zeit zurück, für welche man nicht mehr sagen kann: Wir haben es mit einer Individualität zu tun, die auf der Erde lebt."
      ],
      [
        "Denn da muß man sie auf einem früheren Wohnplatz verfolgen, und es stellt sich die Wandlung dieser eigenartigen Individualität so dar, daß sie hinauswächst über das Erdendasein.",
        "Wir sehen den Buddha zu einer bestimmten Zeit herabkommen von einem anderen Planeten unseres Sonnensystems, wo er vorher gewirkt hat, sehen ihn dort wirken und sich für seine Erdenlaufbahn vorbereiten."
      ],
      [
        "Wir verfolgen ihn dann als Bodhisattva und zuletzt als Buddha während seiner irdischen Laufbahn weiter bis zu dem Punkt, da er aus dem Bodhisattva ein Buddha geworden ist, und finden, daß sein Wirken während der Erdeninkarnationen allerdings mit der Erde zusammengewachsen war, daß er aber in ein großes kosmisches Ganzes hineinwächst.",
        "Wir sehen ihn hinaufsteigen zu einem anderen Planeten unseres Planetensystems, zum Mars, und dort eine neue Mission unternehmen, die sich anschließt an das, was seine Erdenmission war."
      ],
      [
        "Und wunderbar ist es zu verfolgen, wie sich auf diese Weise ein Ganzes herausstellt.",
        "Zuerst sehen wir den Buddha wirksam auf einem anderen Planeten, dann kommt er auf die Erde, und man muß sagen: Diese Individualität des Initiierten Gotama Buddha wirkte eine Weile auf der Erde, dann aber, wenn man sie weiter verfolgen will, muß man zu einem anderen Planeten hinaufsteigen."
      ],
      [
        "So bekommt man eine geschlossene Linie.",
        "Für Buddha ist es möglich zu sagen, daß er von einem anderen Planeten heruntergestiegen ist, und daß er nach seinem Wirken auf der Erde wieder hinaufgestiegen ist zu einem anderen Planeten, dessen Bevölkerung"
      ],
      [
        "für die Erdenmenschheit wenig Sinn hat, um dort weiterzuwirken, weil dieses Weiterwirken gerade einen Sinn ergibt."
      ],
      [
        "So würde man bei vielen Initiierten finden, wie sie aus dem Kosmos das hereintragen, was bei der Erde selbst mit dem Kosmischen in Zusammenhang steht, und man würde dadurch die kosmische Wandlung der Initiierten ins Auge fassen.",
        "Wenn man überall den Dingen auf den Grund zu kommen versucht, dann sieht man zum Beispiel auch etwas, was uns das Lebensdunkel aus einer wirklichen okkulten Betrachtung heraus aufhellt."
      ],
      [
        "Es ist sonderbar, wenn manchmal die Frage aufgeworfen wird: Ist es nicht ungerecht, daß eine solche Individualität wie der Christus etwas Besonderes in die Welt gebracht hat?",
        "Und wenn das der Fall ist - so möchten manche sagen -, dann würden ja die, welche nach dem Christus gelebt haben, etwas ganz Besonderes vor der Welt voraus haben!"
      ],
      [
        "Sogar Theosophen haben diese Frage aufgeworfen!",
        "Aber es sind ja dieselben Seelen, welche in der Zeit nach der Erscheinung des Christus leben, wie die, welche vorher da waren, so daß von Ungerechtigkeit dabei nicht die Rede sein kann."
      ],
      [
        "Nur eine Ausnahme ist in dieser Beziehung zu verzeichnen, und eine solche scheint der Buddha zu sein.",
        "Er hat eine Inkarnation durchgemacht, die in der vorchristlichen Zeit verlaufen war, hat also nicht auf irgendeine Art mitgemacht, was durch das Ereignis von Golgatha auf die Erde gekommen ist."
      ],
      [
        "Wenn wir nun dem dort nachgehen, wo sich uns ein Dunkel ergibt, wo wir nicht verstehen können, wie doch eine Seele in einem bestimmten Zeitpunkt Abschied nimmt von der Erde, auf der Erde nicht miterlebt das Mysterium von Golgatha - wer meine früheren Vorträge gehört hat, wird wissen, daß der Buddha es in anderen Welten miterlebte, aber es handelt sich hier um das irdische Miterleben -, wenn wir uns das alles vor die Seelenaugen halten und dem nachgehen, dann stellt sich heraus, daß der Buddha auf den Planeten, wo er in seiner vorirdischen planetarischen Tätigkeit gewirkt hat, von der Zentralindividualität des ganzen Planetensystems geschickt war, von dem Mittelpunktsgeist, von dem, was wir den kosmischen Christus nennen.",
        "In uralten Zeiten war der Buddha aus- gesendet worden, um auf einem anderen Planeten zu wirken, um"
      ],
      [
        "dann - infolge dieses Wirkens - auf der Erde zu wirken.",
        "Und während die Erde der Planet ist, der zum Schauplatz des Mysteriums von Golgatha geworden ist, ist Mars der Planet, auf dem` der Buddha ein ähnliches Ereignis zu vollbringen hatte nach dem, was er auf der Erde zu wirken hatte."
      ],
      [
        "Diese Dinge liegen scheinbar weitab und scheinen dem zu widersprechen, wenn gesagt wird, man könne mit dem gesunden Menschenverstand das begreifen, was aus der Initiation herausgeholt wird.",
        "Man soll aber nur einmal alles zusammennehmen, was die Geschichte bietet, und alle Zusammenhänge auffassen, dann wird man sehen, daß der äußere Verlauf der Geschichte eine Bestätigung alles dessen bietet.",
        "Und wenn jemand sagt, daß darin keine Bestätigung dieser Dinge liegt, so wendet er nur die gesunde Urteilskraft nicht genügend an.",
        "Das tun ja allerdings viele Menschen in unserer Zeit."
      ],
      [
        "Ich wollte mit alledem, was gerade in diesem Vortragszyklus gesagt worden ist, auch davon eine Vorstellung hervorrufen und wollte schon durch die Dramen zeigen, wie in der Tat ganz anders, gewaltig und groß die Welten sind, in die wir eintreten, wenn wir die Pforte zu den übersinnlichen Welten durchschreiten, und ich wollte eine umfassendere Vorstellung davon hervorrufen, als es durch bloße Theorien und Dogmen geschehen kann.",
        "Ich wollte manches nicht bloß durch Wortcharakteristiken darstellen und beschreiben, sondern ich wollte eine Empfindung von dem hervorrufen, was hinter der Schwelle ist, wo der Hüter der Schwelle steht.",
        "Wenn jemand in unserer heutigen Zeit das Geistesleben überblickt, so geht ihm vielleicht besonders in die Seele herein, was über den Hüter der Schwelle zu sagen ist.",
        "Der Hüter steht an der Schwelle, weil die im gewöhnlichen Sinnensein drinnenstehende Menschenseele nicht reif ist zu erleben und zu erfahren, was in den übersinnlichen Welten vorgeht.",
        "Er steht zum Schutze da.",
        "Das ist ebenso wahr, wie es wahr ist, daß die in die Zukunft hinein lebende Menschenseele mehr und mehr wird erfahren müssen von den übersinnlichen Welten.",
        "Warum steht der Hüter da?",
        "Weil die Menschenseele, wenn sie unreif den Schritt in die übersinnlichen Welten hinein machen würde - was niemals auf einem gerechten okkultistischen Wege geschehen"
      ],
      [
        "kann -, sich unendlicher Furchtsamkeit, unendlichem Schrecken verfallen glauben würde, weil die Menschen aus ihrer Kleinheit, aus ihrer Unreife, aus ihrer Liebe und ihrem Hang zur Sinneswelt nicht ertragen würden, was alles mit dem Eintritt in die übersinnlichen Welten zusammenhängt.",
        "Kann man doch nicht einmal denen gegenüber, die fortgeschritten sein wollen, mit dem kommen, was Anspruch erhebt an unsere Zeit!"
      ],
      [
        "Von der Stätte aus, von der wir bis jetzt noch die übersinnlichen Wahrheiten verkünden dürfen, mußten wir darauf hinweisen, wie ein übersinnliches Ereignis mit dem übersinnlichen Leib des Menschen im Laufe des zwanzigsten Jahrhunderts eintreten wird, indem die Menschen - wie durch ein Naturereignis - den wiedererscheinenden Christus finden werden.",
        "Darauf konnten wir hinweisen."
      ],
      [
        "Aber dieser wiedererscheinende Christus wird nicht auf Schiffen über Meere oder in Eisenbahnen fahren, wird auch nicht im Luftballon fahren, sondern er wird im Individuellen des Menschen - in dem, was von Menschenseele zu Menschenseele geht, und je nachdem, wie die Menschenseelen selbst beschaffen sind - mit den Mitteln erkannt werden, die im Ätherischen gegeben sind.",
        "Was wir so sagen dürfen, wie die Erscheinung des wiedererscheinenden Christus sein werde, erweist es sich schwach gegenüber dem, was rein aus der übersinnlichen Welt heraus an die Menschenseele herankommen wird."
      ],
      [
        "Denn die Menschen lieben es, mit sinnlichen Augen zu sehen den Großen, der da kommen soll; sie lieben es, sich vorzustellen, daß er im Aeroplan fährt, daß er über die Meere fährt, lieben es, sinnlich greifen und fassen zu können den, der da kommen soll.",
        "Warum ist das?"
      ],
      [
        "Weil es sie in Angst versetzt, wirklich mit den übersinnlichen Welten in Berührung zu kommen.",
        "Dem Okkultisten stellen sich auch solche Dinge, wie sie geschehen, als maskierte Furcht und Angst vor dem Wahren dar."
      ],
      [
        "Das sei ohne Emotion gesagt, nur als eine Hinstellung des Objektiven.",
        "Da wird dann der Okkultist, der den Hüter an der Grenze zwischen Sinnensein und Geistessein erkennt, merken, daß die, welche draußen im gewöhnlichen Leben stehen, es nicht fassen können, daß überhaupt ein Anfang gemacht werden soll mit dem Schreiten in die übersinnliche Welt."
      ],
      [
        "Denn furchtsame Persönlichkeiten sind"
      ],
      [
        "sie im Grunde genommen alle.",
        "Ihre Furchtsamkeit ist ihnen unbekannt, aber sie maskiert sich ihnen als die besondere Art von Wahrheitssinn, als ein materialistischer Wahrheitssinn.",
        "Als ein gewisser Haß, eine Wut, ein Entbranntsein der Kleinheit gegen die andern, die übersinnlichen Welten, erscheint sie bei denen> die sich entgegenstellen der Erkenntnis der übersinnlichen Welt und der über- sinnlichen Wesenheiten."
      ],
      [
        "So mag es kommen, daß auf der einen Seite die stehen, welche die übersinnlichen Welten erkennen wollen, und auf der anderen Seite die, welche nichts davon wissen wollen, oder die sagen werden: die objektive Wissenschaft sagt nichts von den übersinnlichen Welten, denn man kann sie nicht beweisen.",
        "Und dasselbe ist es, was auch andere Menschen abhalten wird, hinzugehen zu dem Hüter der Schwelle, nämlich die populären Nachtreter der Wissenschaft, welche da sagen, daß sie die übersinnlichen Welten ablehnen, weil es bei ihnen Wahrheitssinn, persönliche wissenschaftliche Überzeugung sei."
      ],
      [
        "Es ist aber die Furcht, die sie nicht an den Hüter der Schwelle herankommen läßt, und es ist die ganze Kraft dieser Furcht dahinein maskiert, was sich heute als ein Kampf auftun möchte gegen das Herankommen dessen, was aus den übersinnlichen Welten als das Geisteslicht gegenüber dem Lebensdunkel kommen soll.",
        "Das ist eine Vorstellung, welche der empfindet, der den Hüter an der Schwelle des Geistesseins kennt und der da weiß, welche Bedeutung die übersinnlichen Erkenntnisse für das ganze Geistesleben der Gegenwart haben."
      ],
      [
        "Warum sitzen Sie hier?",
        "Weil ein Strahl des Geisteslichtes in Ihre Seele gezogen ist, der Ihnen sagt, daß übersinnliches Wissen die Menschenseele ergreifen muß.",
        "Und weil immer lebendiger und lebendiger geworden ist, was dieser Strahl des Geisteslichtes sagt, deshalb vermehrt sich die Zuschauerschaft und Zuhörerschaft bei unseren Veranstaltungen.",
        "Wird man dem natürlichen Sprechen des Geisteslichtes zu den Seelen freien Lauf lassen, so wird es einstrahlen können in die Seelen.",
        "Wird man bei den Gegnern der übersinnlichen Erkenntnis draußen siegen, dann wird sich vielleicht das Geisteslicht für eine Weile verdunkeln müssen, wird sich zurückziehen müssen, gezwungenerweise, das heißt es müßte zurückgezogen werden,"
      ],
      [
        "um diesen törichten Ausdruck zu gebrauchen.",
        "Dann wird die Welt eine Weile den Zusammenhang zwischen dem Lebensdunkel und dem Geisteslicht entbehren müssen.",
        "Allerdings ist es auch wieder notwendig, daß die, welche etwas von dem Geisteslichte wissen sollen> noch etwas lernen: daß sie lernen, mit Wahrhaftigkeit auf dasjenige zu schauen, was schon hier in der äußeren Welt aus der geistigen Welt geboten wird.",
        "Wer sich heute noch blenden läßt von dem, was pro und contra in bezug auf übersinnliche Erkenntnis gesagt wird, wer nicht in der Seele den festen Impuls aus der übersinnlichen Welt sucht, der nur aus der übersinnlichen Welt selber kommen kann, der wird nicht diesen Impuls finden können."
      ],
      [
        "Ich habe es öfter gesagt, was an Literatur nunmehr vorhanden ist, was durch die Gnade der Meister der Weisheit und des Zusammenklanges der Empfindungen in manchem Literaturwerke gegeben werden durfte, das enthält im Grunde genommen das, wovon man sagen darf, daß es in Gnade den Menschen mitgeteilt werden durfte.",
        "Und wenn ich von diesem Augenblicke an nichts weiter schreiben und sprechen könnte: wenn man nur das Vorhandene ausbaut - wenn ich auch selber nicht dabei sein könnte -, wenn man sucht, was mit allem gemeint ist, so wird man finden> was man braucht."
      ],
      [
        "Und damit ist - wenn ich jetzt am Schlusse dieser Vorträge von dem Zusammenhange des persönlichen Karma mit dem Karma dieser Geistesbewegung sprechen darf - auch die Möglichkeit gegeben> daß in einer gewissen Beziehung das nicht mehr ausgelöscht werden kann, was - nicht als «Steinerische Richtung», denn die gibt es nicht, sondern als objektiver Okkultismus in die Welt gekommen ist.",
        "Mag noch soviel von Gegnerschaft herankommen, das kann sich nicht beziehen auf das Auslöschen des Okkultismus für die Zukunft, denn es wird doch bleiben, was da ist."
      ],
      [
        "Dafür sehe ich denn doch einen Beweis darin, daß unsere Zeit eine spirituelle Bewegung braucht und daß doch eine Spanne Zeit gegeben ist, wo durch die Gnade unserer spirituellen Hüter dieses Geistesgut in die Sinneswelt hat herabgebracht werden können.",
        "Mögen sich Gegner ergeben!"
      ],
      [
        "Vielleicht wird gerade durch diese Gegnerschaft das Nötige getan!",
        "Und verzeihen Sie den Ausdruck: Gar mancher, der heute willig das theosophische"
      ],
      [
        "Geistesgut hinnimmt, der davon beglückt ist: gegenüber dem, was er in der Gegenwart sehen sollte, ist er doch unaufmerksam, da hat"
      ],
      [
        "er doch die Schlafmütze auf!",
        "Da verpflichtet sich manclier nicht gegenüber der Wahrheit zu der Unterscheidung, was die alleinige Wahrheit sein soll.",
        "Vielleicht wird gerade ein klein wenig Verfolgung, die auch nicht schaden kann, dazu beitragen, daß mancher, der die Schlafmütze nicht nur über den Kopf, sondern auch über Augen und Ohren gezogen hat, sie sich dann vom Kopfe herunterziehen wird.",
        "Vielleicht wird auch das notwendig sein."
      ],
      [
        "Wie aber die Dinge gehen mögen: jetzt, wo wir am Ende dieses Zyklus stehen - wo so manches an uns herangetreten ist, notwendigerweise, zwangsweise herangetreten ist, was im Grunde genommen widerwärtig ist -, jetzt wollen wir, wie wir es sonst immer tun, daran denken, daß wir wieder einiges von dem spirituellen Leben aufgenommen haben.",
        "Jetzt gehen wir wieder auseinander, einer dahin, der andere dorthin, aber das Geisteslicht, nach dem wir alle streben und suchen innerhalb des Lebensdunkels, das läßt uns zusammensein überall, wo wir auch örtlich getrennt sein mögen."
      ],
      [
        "Die Seelen, die hier sitzen, mögen sie ihre Zusammengehörigkeit fühlen im Nacherleben, im Nachmeditieren des Gehörten oder in bezug auf das, was sich an gegenseitiger Liebe gezeigt hat, im Nachleben.",
        "Physisch waren wir zusammen, physisch werden wir nicht immer so zusammensein können."
      ],
      [
        "Übersinnlich sind wir zusammen.",
        "Lernen wir übersinnlich zusammensein, damit wir das Dasein der übersinnlichen, der überphysischen Welt beweiskräftig machen können!",
        "Wenn wir solche Gefühle mitnehmen, nachdem wir solange zusammen waren, dann werden die Seelen das mitnehmen, was Theosophie als das Beste den Menschen mitgeben kann: die Liebe, die aus der spirituellen Wahrheit selber herauskommt."
      ],
      [
        "Und wenn auch zwischen jetzt und derjenigen Gelegenheit, bei der wir wieder so zusammensein möchten, das eine oder andere geschehen mag: das kann doch geschehen unter allen Umständen, daß sich unser physisches Zusammensein in das rechte spirituelle Zusammensein bei örtlichem Auseinander verwandeln werde, damit wirke, lebe und gedeihe in uns das spirituelle Geistesgut.",
        "Wir haben doch auch Menschen"
      ],
      [
        "der allverschiedensten Denkweisen in unserer Mitte gehabt, aber auch solche Menschen, über deren Erscheinen wir uns immer auch dann freuen, wenn sie etwa gegensätzliche Meinungen in unsere Mitte hineinbringen.",
        "Doch nicht um Meinungen und um Gegensätze der Meinungen handelt es sich, sondern um ehrliches, aufrichtiges Wahrheitsgefühl, um, man möchte sagen, ein Verschworensein zur Wahrhaftigkeit und Ehrlichkeit, zur Wahrhaftigkeit und Ehrlichkeit schon im Sinnensein.",
        "Daß ich dieses sage, betrachten Sie nicht als etwas, was notwendig erfolgen muß aus dem Thema unseres Vortragszyklus.",
        "Was aber notwendig ist, das ist, daß wir auf mancherlei Gebieten das Wahrheitssuchen in unserer Zeit, überhaupt in unserer Gegenwart, haben erleben können."
      ],
      [
        "Und wozu sich im Anfange des Vortragszyklus für mich selbst weniger Gelegenheit gefunden hat, das sei hier am Ende berührt: der"
      ],
      [
        "Dank gegenüber denjenigen Persönlichkeiten, die vor allen Dingen auch als offizielle Persönlichkeiten innerhalb unserer unoffiziellen Veranstaltungen erschienen sind.",
        "Ich kann nicht alle im einzelnen nennen.",
        "Sie haben gestern selber gehört die freundliche Einladung"
      ],
      [
        "für den nächsten Kongreß der europäischen Sektionen der Theosophischen Gesellschaft unseres lieben Generalsekretärs der Skandinavischen Sektion, und es haben einige von Ihnen vielleicht auch die Worte des Generalsekretärs der Ungarischen Sektion vernommen.",
        "Diesen Persönlichkeiten, worauf wir besonders hinzuweisen haben, ist der Gruß schon an dem ersten Vortrage dargebracht worden, und die, welche ungenannt bleiben mußten, sollen wissen, daß sie in unseren Herzen das aufrichtigste Willkommen gefunden haben, und daß wir ihr Hiersein als eine Bekräftigung dessen auffassen, daß sie doch noch nicht der Anschauung sind, daß wir so schlimme Menschen sind, wie es jetzt beginnt in der Welt dargestellt zu werden.",
        "Wie wir also auch im nächsten Jahre beisammen sein mögen, wie sich die Dinge auch gestalten mögen, fassen wir das diesjährige Zusammensein als den Keim zu etwas auf, was uns vielleicht durch alles, was da kommen mag, doch nicht genommen werden kann.",
        "Was Ihre Seelen selber aus freiem inneren Erleben als Nachklang empfinden können, womit Sie zurückblicken auf diese Tage von"
      ],
      [
        "München, das ist es, woran ich in diesem Augenblicke appellieren möchte, eines jeden Freundes einzelne Seele herzlich begrüßend zum Abschied und zum Wiedertreffen in dem Sinne, wie sich Leute, die sich durch Erkenntnis lieben gelernt haben, immer zusammenfinden und zur rechten Zeit immer wieder treffen müssen."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "SONDERVORTRAG München, 30. August 1912",
    "paragraphs": [
      "Der einzelne Mensch, welcher durch die Empfindungen und Sehnsuchten seiner Seele den Drang verspürt, an die theosophische Bewegung heranzutreten, wird - vielleicht ohne daß er sich dessen immer im vollen Umfange bewußt ist - die Befriedigung dessen suchen, was persönlich sein Herz begehrt, was ihm persönlich Ruhe über die großen Rätselfragen des Daseins bringen kann, über diejenigen Fragen, von denen er fühlt, daß er ohne ihre Beantwortung nicht mit dem Leben in der Epoche, in die er durch seine gegenwärtige Inkarnation hineingestellt ist, fertig werden kann. Wenn der einzelne dann da oder dort innerhalb des Geisteslebens seiner Epoche dasjenige findet, was er entgegennehmen kann, um zu diesen Befriedigungen seiner bangen und für ihn notwendigen Seelenrätsel zu kommen, dann sollte er sich aber auch bemühen, zu einem Verständnis davon durchzudringen, daß solches Geistesleben, das sich in irgendeine Epoche hereinstellt, auch für die einzelne Seele nur wirklich das bringen kann, was diese einzelne Seele in der richtigen Weise mit dem Geistigen verbindet, ohne daß diese Richtigkeit der einzelnen Seele immer bewußt wird, wenn solches Geistesleben im Einklange steht mit der Gesamtevolution der Menschheit und Rechenschaft abzulegen vermag vor der Gesamtevolution der Menschheit.",
      "Es mag da oder dort eine geistige Bewegung auftreten, einzelne Seelen mögen glauben, für sich dasjenige, was sie brauchen, in solchen Bewegungen finden zu können. Es kann das, was die Seele also bekommt, und wovon sie selbst glaubt damit befriedigt sein zu können, aber wertlos sein für die wirkliche Entwickelung der Seele, für die wirklichen Kräfte, welche die Seele suchen muß, wenn nicht dasjenige, was ihr als geistiges Leben begegnet, die volle Verantwortung übernehmen kann gegenüber der geistigen Führung und geistigen Leitung der Menschheit in irgendeiner Epoche, wenn nicht diese geistige Bewegung vor diejenigen Mächte hintreten kann, welche die Führung des Geisteslebens der Menschheit haben, und sich vor diesen",
      "Mächten verantworten kann, indem sie von diesen Mächten sozusagen ausgesprochen erhält: Ja, es geschieht mit der geistigen Bewegung dasjenige, was die Zeit verlangt, was die geistigen Kräfte verlangen, welche in die Zeit hereinragen. - Der einzelne Theosoph mag wohl ab und zu auch das Bedürfnis haben Ausschau zu halten, wie das, was er entgegennimmt, zu dem gesamten geistigen Leben steht oder sich auf den verschiedensten Gebieten äußert, was aber vielleicht mehr die Sehnsucht ausdrückt als das Bedürfnis, von der Zeit die Lösung der Rätselfragen zu erwarten, die durch die Geisteswissenschaft gewonnen werden soll. Die theosophische Seele mag, wenn sie auf dasjenige blickt, was sie mit einiger Befriedigung aus der Geisteswissenschaft heraus empfängt, gar manchmal unbefriedigt oder vielleicht auch unsympathisch auf das blicken, was uns überall als Geistesleben in unserer Zeit so umgibt, daß dieses Geistesleben vermeint, auch mit den höchsten Daseinsfragen, den höchsten Rätseln des Menschendaseins zu tun zu haben.",
      "Manches, was da draußen auftritt und ringt nach der Lösung der Daseinsrätsel, nach der Beantwortung der Fragen des Daseins, mag als materialistisch, oberflächlich, ungenügend von mancher Seele empfunden werden, welche die Geisteswissenschaft aufnimmt. Unbefangener Beobachter ist in diesem äußeren Leben aber so mancher, der von der Geisteswissenschaft nichts weiß, so mancher, der auch nicht einmal ahnen kann, was in dem, was wir Geisteswissenschaft nennen, lebt, und der aufrichtig und ehrlich nach der Wahrheit in unserer Epoche ringt, dessen Seele eben ehrlich und aufrichtig nach den Daseinsrätseln hin die tiefste Sehnsucht empfindet.",
      "Nicht mit einem oberflächlichen, alles nivellierenden Blick sollen wir unsere Mitwelt, das was außer uns steht, überschauen, sondern mit einem unterscheidenden",
      "Blick, denn nur dadurch können wir die Möglichkeit gewinnen, in der richtigen Weise an das anzuknüpfen, was da ist. Es kann natürlich nicht in einem einstündigen Vortrage vieles von dem erwähnt werden, woran die, welche die spirituellen Leiter unserer Bewegung sind, heute anknüpfen müssen, was sie voll berücksichtigen müssen. Deshalb kann nur einzelnes herausgehoben werden, und an einzelnen Exempeln soll gezeigt werden, worin draußen in der Welt die",
      "Rätselfragen pulsieren, zu deren Beantwortung, zu deren Befriedigung Geisteswissenschaft sich anschicken will.",
      "Wenn Sie die Welt betrachten, so werden Sie insbesondere finden, daß suchende Seelen - Seelen, denen sich die Daseinsrätsel so recht ins Herz hineindrücken - sich sagen: Wessen bedürfen wir heute, was müssen wir fragen, wo können uns Aussichten über die Ziele des Lebens herkommen? - Seelen, so empfindend, finden sich zahlreich namentlich unter denen, die sich aus der praktischen Technik, der Praxis des Lebens, der Praxis der Arbeit herausarbeiten. Nicht einmal unter den der Philosophie Geneigten sind so viele, die in bangster Weise so denken, als unter den Lebenspraktikern, die ihre Hände unter der Mechanisierung des Lebens abmühen, die dafür aber nach dem hinblicken, was oft die Seele erfüllt, wenn sie nach den Rätseln des Lebens fragen muß. Wir müssen wohl hinhorchen auf solche Seelen, denn wir müssen uns vorstellen, daß die Geisteswissenschaft einst zu antworten hat, Rechenschaft abzulegen hat den leitenden Mächten der Welt gegenüber. Solche Seelen aber gehören zu den besten suchenden Seelen der Gegenwart, und es kann eine Epoche kommen, wo sie herantreten an die Führer des geistigen Lebens, und wo diese auf die Lebensrätsel antworten müssen, die sich unter dem Druck der praktischen Interessen des Lebens herausgebildet haben. Wir brauchen uns nur nicht selber zu blenden, müssen nur den Sinn für das haben, was im Leben vorgeht, und es wird uns überall entgegentreten, wo die wahren Stimmen der Seelensucher sind.",
      "Wer in der letzten Zeit entweder an Buchhandlungen vorbeigegangen ist oder sich an den Bahnhofsbuchhandlungen umgesehen hat, was dort ausgelegt war, und nicht nur hingegangen ist mit dem Bestreben, nur das sich auszusuchen, was er sich kaufen will, der wird überall deutlich ausgelegt gefunden haben ein Buch, das er vielleicht, wenn er Theosoph ist, nicht mit viel Interesse lesen kann, wenn er nur daran denkt, die eigenen Seelenbedürfnisse zu befriedigen, das er aber mit Interesse lesen wird, wenn er sich sagt: wie müssen sich die Dinge stellen, wenn wir mit Antworten auf die Fragen nach den Lebensrätseln den suchenden Seelen entgegenkommen",
      "wollen? Da lag ein Buch aus von einem im praktischen Leben ausgezeichneten Mann, und las man die ersten Seiten, so konnte man sich überzeugen, daß er einen guten Überblick Über unser Zeitalter hat, daß unsere Zeit aufrückt zu der Mechanisierung des äußeren Lebens, daß die Kräfte menschlicher Arbeit immer mehr und mehr hineingedrängt werden in die maschinenmäßige Arbeit.",
      "Es ist das Buch «Zur Kritik der Zeit» von Walther Rathenau. Es ist ein Buch eines unsere Zeit kennenden Menschen, den derjenige auch kennenlernen sollte, der in der Geisteswissenschaft mitsprechen will.",
      "Es ist darin dargestellt, wie in unserer Zeit alles mechanisiert wird, und warum das so kommen mußte. Für umfassende Begriffe wird das größtenteils unrichtig dargestellt, ja, man wird vielleicht mit keinem Ausdruck darin übereinstimmen können, aber darum handelt es sich nicht.",
      "Sondern darum handelt es sich, was die suchenden Seelen in unserer Zeit sagen, und welches die Kräfte sind, mit denen sie suchen, besonders wenn es ein Mensch des praktischen Lebens ist, wie es der Verfasser dieses Buches ist. Ich möchte Ihnen zu Beginn unserer Betrachtung etwas aus einer Stelle dieses Buches vorlesen, die mir wie aus dem Zentrum der Seelenstimmung der Seelen Europas und Amerikas gesprochen erscheint.",
      "Man hört darin förmlich, was unzählige Seelen nicht aussprechen können, was in ihnen Fragen anregen kann, wenn man eine solche Persönlichkeit versteht, wo sie aus sich heraus von der Zeit und der Zeitenseele spricht und sagt: «Sie - die Zeit - sucht ihre Seele und wird sie finden» - trotzdem können Sie in dem ganzen Buche nicht einen einzigen Anhaltspunkt finden, wie die Zeit ihre Seele finden mag, nur Sehnsucht, der Trieb nach etwas Unbekanntem - «freilich gegen den Willen der Mechanisierung. Dieser Epoche lag nichts daran, das Seelenhafte im Menschen zu entfalten; sie ging darauf aus, die Welt benutzbar und somit rationell zu machen, die Wundergrenze zu verschieben und das Jenseitige zu verdecken.",
      "Dennoch sind wir wie je zuvor vom Mysterium umgeben; unter jeder glatten Gedankenfläche tritt es zutage, und von jedem alltäglichen Erlebnis bedarf es eines einzigen Schrittes bis zum Mittelpunkt der Welt.» In diesem Buche wird nirgends angedeutet, wie dieser Schritt gemacht werden soll von den uns umgebenden",
      "Mysterien bis zum Mittelpunkt der Welt. «Die drei Emanationen der Seele: die Liebe zur Kreatur, zur Natur und zur Gottheit konnte die Mechanisierung dem Einzelleben nicht rauben; für das Leben der Gesamtheit wurden sie zur Bedeutungslosigkeit verflüchtigt.",
      "Menschenliebe . . .» - das sagt ein Praktiker der Gegenwart, der sich mit nüchternem Blick seiner Zeit so entgegenstellt, wie er sich ihr entgegenstellen kann, der durch Jahrzehnte selbst angegriffen hat, was in Europa und darüber hinaus die Fäden des ökonomischen Lebens sind, und der selber daran mitgearbeitet hat - «Menschenliebe sank zum kalten Erbarmen und zur Fürsorgepflicht herab, und bedeutet dennoch den ethischen Gipfel der Gesamtepoche; Naturliebe wurde zum sentimentalen Sonntagsvergnügen; Gottesliebe, überdeckt vom Regiebetriebe mythologisch-dogmatischer Ritualien, trat in den Dienst diesseitiger und jenseitiger Interessen und wurde so nicht bloß unedlen Naturen verdächtig.» Weiter sagt Rathenau Worte, auf die der, welcher den Geistesbedürfnissen der Zeit entgegenkommen will, mit gutem Willen entgegenkommen will, hinhören muß, wenn sie auch partiell unrichtig sind, denn sie drücken das aus, was berechtigt aus den Seelen herausströmt und in zukünftigen Zeiten immer mehr aus den Seelen herausströmen wird: Empfindungen, gegen die sich keiner, der Geisteswissenschaft treibt, auflehnen darf, ohne daß ihn das Karma der Zeit treffen wird. «Es gibt wohl keinen einzigen Weg, auf dem es dem Menschen nicht möglich wäre, seine Seele zu finden, und wenn es die Freude am Aeroplan wäre.",
      "Aber die Menschheit wird keine Umwege beschreiten.» Das ist Bedürfnis der Zeit. Das können wir hören, wie die Zeit es ablehnen wird etwas entgegenzunehmen, was unmittelbar zu den Tiefen der Seele, was übersinnlich zu den Tiefen der Seele sprechen wird.",
      "Diese Zeit wird sagen: «Es werden keine Propheten kommen und keine Religionsstifter, denn diese übertäubte Zeit läßt keine Einzelstimme mehr vernehmlich werden: sonst könnte sie heute noch auf Christus und Paulus hören. Es werden keine esoterischen Gemeinden die Führung ergreifen, denn eine Geheimlehre wird schon vom ersten Schüler mißverstanden, geschweige vom zweiten.",
      "Es wird keine Einheitskunst der Welt ihre Seele bringen, denn die Kunst ist",
      "ein Spiegel und ein Spiel der Seele, nicht ihre Urheberin.» Man möchte sagen: So hat sich vor einigen Monaten ein Mann vernehmen lassen. Und was haben wir seit zehn Jahren getan? Wir haben uns bemüht, Antwort zu finden auf das, was so aus der Zeit heraus als ihre Kräfte sich spinnt. Und weiter sagt er: «Das Größte und Wunderbarste ist das Einfache. Es wird nichts geschehen, als daß die Menschheit unter dem Druck und Drang der Mechanisierung, der Unfreiheit, des fruchtlosen Kampfes die Hemmnisse zur Seite schleudern wird, die auf dem Wachstum ihrer Seele lasten. Das wird geschehen nicht durch Grübeln und Denken, sondern durch freies Begreifen und Erleben. Was heute viele reden und einzelne begreifen, das werden später viele und zuletzt alle begreifen: daß gegen die Seele keine Macht der Erde standhält.»",
      "Daß gegen die Seele keine Macht der Erde standhält! Das bedingt unser Vertrauen, daß wir in die Zukunft hineinwachsen mit dem, was wir haben, und uns im Einklang wissen mit den Besten der Zeit, die nichts von uns wissen oder gar nichts wissen wollen. Aber wir wollen uns nicht verleiten lassen gegen das, wonach unsere Zeit dürstet, irgend etwas zu unternehmen, denn wir wissen, die Führung der Menschheit ist höheren, spirituellen Mächten überlassen, und das, was sich in der Menschheit äußert, kommt von diesen spirituellen Mächten, auch wenn es selbst anders erscheinen mag als das, was wir selbst wollen, wenn es nicht durch irgendwelche Willkür, sondern so erzeugt erscheint, daß es wie mit elementarer Gewalt aus dem Zentrum der Seelen mit dem Impuls der Zeit hervorkommt. So spricht zu uns unsere Zeit. Wie sprechen diejenigen Erscheinungen, die unsere Zeit herbeigeführt haben?",
      "Ich möchte zunächst von etwas ausgehen, wohin sich meine Gedanken im Verlaufe dieses Vortragzyklus schon einmal lenkten. Unter den mancherlei Persönlichkeiten, die mir in der Zeit entgegengetreten sind, als ich noch nicht innerhalb der Theosophischen Gesellschaft war, war - wie ich vor einigen Tagen erwähnt habe - auch der Kunsthistoriker Herman Grimm, der mit allem, was er im einzelnen leistete, nichts anderes wollte, als sich bewußt in die Bedürfnisse unserer Zeit hineinzustellen. Sehr Merkwürdiges konnte man mit ihm",
      "erleben. Herman Grimm hat sich in den sechziger Jahren des vergangenen Jahrhunderts herangemacht, eine Biographie Michelangelos zu schreiben. Wer sie heute in die Hand nimmt; wird sie, wenn er nicht von Vorurteilen befangen ist, als das Beste finden, was über Michelangelo geleistet worden ist.",
      "Herman Grimm hat in langer Arbeit sich bemüht, ein gerundetes Bild des Wirkens und Schaffens Michelangelos zu vollenden. Es ist ihm auch gelungen, ein Bild dieser Zeit zu schaffen. Er hat dann auch begonnen, ein Leben Raffaels zu schreiben.",
      "Es gehörte zu den beständigen Geständnissen, die man aus Herman Grimm heraushören konnte, daß es ihm gegenüber Raffael ganz anders erging. Michelangelo konnte er so beschreiben, daß er ein fertiges Bild dieser Persönlichkeit hinstellen konnte, Raffael nur so, daß es für ihn selbst nimmermehr genügte.",
      "Warum? Herman Grimm war ein Mensch, der bei allem, was er begreifen wollte, immer die ursprünglichen Ursachen suchte, und bei Raffael konnte er eben die ursprünglichen Ursachen nicht finden. Wenn er irgendwie mit etwas über Raffael fertig war, dann mußte er finden, daß die Sache doch wieder höchst unvollkommen gelöst war.",
      "Dennoch setzte er immer wieder an, auch kurz vor seinem Tode noch einmal, um ein Leben Raffaels zu schreiben, doch es ist nicht fertig geworden. Ein kurzes Fragment darüber ist dann in seinen nachgelassenen Fragmenten erschienen.",
      "Herman Grimm selber sagte sich etwa: «Ob es mir diesmal anders gelingen wird, wenn ich noch so lange leben werde, irgend etwas zustande zu bringen, was für mich sich deckt mit dem, was man über Raffael wissen möchte?» Es war kurz vor seinem Tode, als er wieder damit anfing, denn es war das Fragment, dem gegenüber er die Feder aus der Hand gelegt hat und gestorben ist. Es ist nur ein Fragment, als er selber noch dazu gekommen war, ein «Leben Raphaels» zu schreiben.",
      "Ich selber mußte, als ich diese Worte in seinem Nachlaß las, eines Momentes gedenken, da ich mit ihm in einem kleinen Kreise einmal zusammen war und gesprochen habe, wie ich es wollte, von den geistigen Angelegenheiten der Menschheit. Ich hatte Herman Grimm sehr lieb und werde ihn immer gleich lieb haben.",
      "Er war eine Persönlichkeit, streng eingeschlossen in das Geistesgebiet, das er sich zubereitet",
      "hatte, und er hatte eine Antwort auf das, was ich so gerne hätte ein- fließen lassen. Sie bestand in folgendem: es war eine bloße Handbewegung des Ablehnens gegenüber dem, was sich in die` Insel seines Geisteslebens etwa hätte von außen her hineinbewegen können von dem, was nicht von ihm mit den Kräften, die man in seiner Zeit haben konnte, aufgenommen werden konnte. Wer mit ihm umzugehen wußte, der verstand ihn und seine Hand, wie sie um die Tischecke herum in ablehnender Bewegung sich befand. Für mich war diese Handbewegung die Grenze zwischen dem, bis wohin ein Geist geht, der mit den geistigen Elementen seiner Epoche dieselbe neu beleben will, und dem, was als neue Kräfte in unsere Zeit einfließen muß. Das war im Jahre 1892.",
      "Warum - ich möchte alles andere jetzt nur in Ihren Seelen anregen - konnte Herman Grimm aus den geistigen Elementen, die in seiner Seele lebten, mit dem Leben Raffaels nicht zustande kommen? Geben Sie sich die Antwort mit alle dem, was für das Geistesleben einer Zeit notwendig sein wird, die so etwas wie das Leben Raffaels wird verstehen wollen.",
      "Damit sage ich nicht, daß das Leben Raffaels etwas Höheres sein muß als zum Beispiel das Leben Michelangelos, sondern ich stelle nur ein Faktum für die Menschenseele vor Sie hin. Versuchen Sie sich eine Antwort zu geben.",
      "Man kann sie sich geben, wenn man den Blick schweifen läßt über das erste Bild, das unser drittes Mysteriendrama, «Der Hüter der Schwelle», eröffnet. Da finden Sie vier Bilder: Elias, Johannes der Täufer, Raffael, Novalis.",
      "Mit dem, was im Laufe unserer jahrelangen geisteswissenschaftlichen Arbeit hat zutage treten können, so daß es plausibel, beweiskräftig erscheinen konnte, haben wir uns bemüht zu zeigen, wie eine gleiche Seelen-Individualität - sich wiederinkarnierend - von Elias zu Johannes dem Täufer hinübergeht, in Raffael wiedergeboren wird, dann in Novalis wiedererscheint. So phantastisch das heute erscheinen mag, so wahr wird man es in einer gar nicht so fernen Zukunft finden, daß man mit dem Begreifen der Welt scheitern wird, wenn man nicht zu Hilfe nehmen wird die Idee der Reinkarnation der Menschenseele und das Karma, das durch die verschiedenen Erdenleben hindurchgeht, was man die spirituellen Zusammenhänge",
      "der Welt nennt. Der erst wird Raffaels Leben beschreiben, der von dem Leben ausgeht, das durch die Geisteswissenschaft erkannt wird. Überall tritt drängend und fragend in unserer Zeit an die Menschenseele heran der Zusammenhang des geistigen Lebens in aller Welt, setzt Fragen hin wie die: Wie kommt es, daß plötzlich im menschlichen Leben Gedanken auftreten wie aus eigener Seele entspringend, die in fern davon liegenden Zeiten da waren und nun wieder auftreten? - Man kann in die Art hineinschauen, wie das geistige Leben wirklich wirkt, wie es in den aufeinanderfolgenden Epochen die Gedanken immer wieder erscheinen läßt, wenn man die geistigen Gedankengänge kennt, welche die Geisteswissenschaft zu enthüllen vermag.",
      "Es ist in den letzten Wochen ein höchst Bedeutsames im deutschen Geistesleben erschienen. Es wird Ihnen sonderbar erscheinen, daß ich es für bedeutsam halte. Aber ich muß es für bedeutsam halten, denn es ist symptomatisch bedeutsam. Ich habe, als ich in Weimar mit Goethe beschäftigt war, viele Persönlichkeiten kennengelernt, die mit der deutschen Gelehrsamkeit tonangebend zusammen- stehen. Unter den mancherlei Germanisten trat mir damals einer entgegen, von dem ich mir außerordentlich Bedeutsames auf seinem Felde versprechen konnte. Es ist Konrad Burdach, der damals Professor in Halle war, dann diesen Posten verlassen hat, um als Privatgelehrter weiterzuleben. Nun hat Konrad Burdach in den letzten Wochen in den Versammlungen der Berliner Akademie der Wissenschaften eine höchst interessante Abhandlung vorgelegt. Sie figuriert zwar zunächst nur unter den akademischen Schriften, doch ist darin eine bedeutsame Frage aufgeworfen - aber eine Frage, die man nicht mit den Mitteln Konrad Burdachs lösen kann, sondern die nur mit den Mitteln der Geisteswissenschaft beantwortet werden kann. Sie werden sich überzeugen, daß es einem Bedürfnis der einzelnen Seele sehr naheliegt, wenn sie über die Zusammenhänge des Lebens nachdenkt, sich zu fragen: Wie steht das Faust-Gedicht der modernen Seele gegenüber? - Haben wir nicht in dem Faust den Lebenspraktiker unserer Zeit hingestellt, der - am Schlusse seines langen Lebens angelangt - vor allem ein praktisches Ideal vor sich hat?",
      "Schauen wir uns Goethe an in seinem praktischen Schaffen: wir können es verfolgen, wie er zu Eckermann, seinem getreuen Sekretär, spricht. Goethe ist genötigt, die spirituelle Entwickelu`ng des Faust darzustellen. Ihm kommt der geistige Inhalt von Raffaels Madonna Sixtina in den Sinn; er konnte diesen erst in seiner späteren Lebenszeit erfassen, weil er ihn zum Beispiel beim ersten Besuch in Dresden noch nicht erfaßt hatte. Er wollte darstellen, wie zum Schluß Fausts Unsterbliches in die höheren Welten aufgenommen wird. Wir sehen, er ringt mit seinem Problem so, daß er einst zu Eckermann sagte: Es ist merkwürdig, wie dämonische Gewalten durch die Welt gehen und aus einem unbekannten Übersinnlichen Gestalten wie Raffael heraussprießen lassen, wie man nicht fertig wird mit Gestalten wie Raffael, ohne daß man sie erklären wird aus ihrem Hervorgehen aus dem Ubersinnlichen heraus. - Man kann ein Gefühl davon haben, wie Goethe gerungen hat von dem allmählichen Übergehenlassen der Entelechie, von dem allmählichen Übergehen der Gestalten in die höheren Welten, bis er dann fertig wird mit einem Menschen, den er zugleich als einen Lebenspraktiker für die kommenden Jahrhunderte hingestellt hat.",
      "Konrad Burdach hat für die Philologie ein Merkwürdiges hingestellt. Wer seine Abhandlung liest, hat das Gefühl: es ist doch sonderbar, wie es der reinen Philologie gelungen ist, ein Parallelbild aus den früheren Jahrhunderten dem Faust an die Seite zu stellen. Es werden die alten Gestalten nur in moderner Form, als wenn sie Goethe gestaltet hätte, wieder hingestellt. Die ganze Moses-Geschichte wird in dieser Weise, als wenn es Goethe gedacht hätte, für seine Zeit hingestellt. Konrad Burdach will damit zeigen, wie in Goethes Denkweise alles einfließt, was sich um die Moses - Gestalt herumgegliedert hat.",
      "So steht ein Mann vor der Pforte, hinter welcher die Übersinnliche Welt ist, die Antworten gibt auf die Frage: Inwiefern sind Gedanken, sind spirituelle Mächte reale Kräfte, die durch die Zeit hindurchwirken und in den verschiedensten Zeiten angemessen diesen Epochen wieder hervortreten? Überall wo wir hinblicken, pocht heute die Welt an die Pforte der übersinnlichen Welt. Unsere Pflicht",
      "ist es, zu unserem Verantwortlichkeitsgefühl gehört es, die Welt, wo sie ehrlich und aufrichtig, nicht aus der persönlichen Willkür heraus fragt, so zu hören, wie es den Empfindungen, den Gefühlen der Seelen angemessen ist. Dabei kommt nicht in Betracht, was wir uns selber einbilden, wie die wahre Entwickelung der Menschheit sein soll.",
      "Ablesen sollen wir aber an den wirklich besten und sehnenden Seelen, wie sie selber in die spirituelle Welt hineinkommen wollen, und zurückhalten das, was wir selber für uns als das Wichtige halten, um es denen geben zu können, die da suchen. Gegenüber einer solchen Kultur, wie die ist, aus der wir heraus arbeiten wollen, und in der viele auswärtige Freunde in Europa und Amerika mit uns deshalb zusammenarbeiten, weil sie wissen, daß es nichts mit Nationalität zu tun hat, schickt es sich nicht darüber zu streiten, was orientalisch, was okzidentalisch ist, in der ein tonangebender Geist gesagt hat: «Gottes ist der Orient, Gottes ist der Okzident!» Das sind Worte Goethes, die uns in der Seele leben, und aus denen heraus wir wirken.",
      "Aber in den Seelen - nicht bloß in den unsrigen, sondern auch in denen, auf die wir hören müssen - leben nicht nur unsere willkürlichen Gedanken, die uns vorschreiben, was wir den anderen zu geben haben, sondern in den Seelen leben Empfindungen, welche die Geister der Jahrhunderte geschaffen haben. Suchen wir eine der uns entgegentretenden Gruppen auf.",
      "Gehen Sie mit mir zu einer der Leistungen, die - wie die Goethes sind - ganz außerordentlich bezeichnend sind für das Empfindungsleben gegenüber der spirituellen Welt und gegenüber den Gestalten, die in der spirituellen Evolution der Menschheit wirken. Gehen Sie mit mir zu einem Kapitel des «Wilhelm Meister» von Goethe.",
      "Verfolgen wir es zusammen, wie er den Wilhelm Meister als den Repräsentanten der Menschheit bewußt hinstellen wollte. Da sehen wir, wie Wilhelm Meister an einem Schlosse ankommt, wie er von dem Führer des Schlosses geführt wird und ihm die Schönheiten des Schlosses gezeigt werden, unter anderem auch die Bildergalerie.",
      "In dieser ist auch enthalten, was den Entwickelungsgang der Menschheit durch die verschiedenen Epochen hindurch darstellen kann, und man sieht daran, wie sich die Menschheit aus uralten Zeiten immer weiter und weiter bis zur Zerstörung",
      "Jerusalems entwickelt hat. Man soll durch die aufeinander- folgenden Bilder begreifen, wie es durch die Kräfte, die in der Evolution der Menschheit wirken, bis zur Zerstörung Jerusalems gekommen ist. Der, welcher geführt wird, Wilhelm Meister, dessen Erziehung der Seele uns geschildert werden soll, fragt seinen Führer: Warum ist hier der Gang der Menschheitsentwickelung bis zur Zerstörung Jerusalems dargestellt und gar nicht innerhalb dieses Ganges das, was kurz davor in die Entwickelung hereingefallen ist: das Leben des Christus mit alle dem, was er in Palästina vollbracht hat? - Da sagt der Führer zu Wilhelm Meister: Dieses in gleicher Weise darzustellen wie den übrigen Gang der Menschheitsentwickelung, verbietet uns das, was unser Heiligstes ist.",
      "Was du hier dargestellt siehst, ist dasjenige, was an Kräften in der Weltgeschichte wirkt und so wirkt, daß es in seinem Zusammenwirken die Menschengruppen, die Nationen angeht, nicht aber die Kräfte, welche im einzelnen ein- gegriffen haben in das Leben einzelner Menschen. Es wäre falsch, in diese Bilderreihe den Christus hineinzustellen, denn der Christus wendet sich intim an jede einzelne Seele, und jede einzelne Seele hat mit ihm fertig zu werden.",
      "Dann führt der Führer den Wilhelm Meister in ein zweites, geheimeres Gemach, wo dargestellt ist, was nicht im gewöhnlichen Sinne in den epochalen Gang der Menschheitsentwickelung hineingestellt werden kann. Da sind wieder Bilder: für sich ist dasjenige hingestellt, was anknüpft an das Mysterium von Golgatha.",
      "In Bildern ist dargestellt vor Wilhelm Meister alles, was an den Christus anknüpft, bis - ja, bis zum Abendmahl. Nicht ist dasjenige da, was sich an das Abendmahl nun als das eigentliche Mysterium von Golgatha anschließt.",
      "Warum, fragt wieder Wilhelm Meister seinen Führer, ist hier in diesem geheimeren Kabinett das dargestellt, was bis zum Abendmahl hinführt, und nicht dasjenige, was sich daran anschließt? Er erhält die Auskunft, daß zunächst keine menschliche Seele in der Lage ist> das, was sich daran anschließt, so darzustellen, daß es das menschliche Gemüt nicht verletzen könnte.",
      "Goethe empfand noch in seiner Zeit aus seinem Spirituellen heraus die Ohnmacht, das große Mysterium darzustellen, weil er wußte, man möchte sagen, auch aus noch unbewußtem Wirken, daß",
      "- die tiefsten Gefühle des Seelenlebens herausgeholt werden müssen, wenn man das Heiligste für die Seele erstreben und vor die Seele hin- stellen soll. So zeigt uns sein Wilhelm Meister, wie man eine zweifache Pforte des Esoterischen überschreiten soll, wenn man sich diesem Heiligen in seiner Seele nähern will.",
      "Was ist damals in Goethes Seele zum Ausdruck gekommen? Es ist zum Ausdruck gekommen, daß, wenn in der neueren Kultur sich die Seele innerhalb ihrer selbst richtig erfaßt, diese neuere Kultur in die Seele ein Heiligstes, ein Hehrstes hineinlegt, das Goethe fühlen mußte. Was seiner Zeit noch nicht gegeben war, um dieses Heiligste darzustellen, muß aber kommen. Es muß mit ganz anderen Mitteln in den Seelen wirken. Wer die Verantwortlichkeit gegenüber dem fühlt, was in der Zeit solche Empfindungen gezeitigt hat, der steht nun der spirituellen Welt gegenüber mit vollem Verantwortlichkeitsgefühl und glaubt diesem Verantwortlichkeitsgefühl nur dienen zu können, wenn er nichts anderes tut, als die Seelen darauf hinzuweisen, wie in unserer Zeit die Epoche reif wird, daß die Seelen, wenn sie zum spirituellen Leben heranwachsen, dasjenige erringen werden, was für den Blick des Wilhelm Meister sich erst nach zweifachem Überschreiten der Pforte zu den höheren Geheimnissen erschließen soll. So wäre die Atmosphäre, die aus dem geistigen Leben der Zeit in unsere Seelen strömt, wenn wir von dem Christus-Geheimnis sprechen wollten, das sich uns enthüllen soll, sprechen wollten von der Intimität, die zwischen der Seele und dieser gewaltigen Macht der Weltentwickelung bestehen wird, wenn jede einzelne Seele reif wird, daß der aus der geistigen Welt heraus neu sich offenbarende Christus intim jeder einzelnen Seele sich nähern wird.",
      "Wir wußten, daß wir nicht anders handeln durften, als dem Führer des Wilhelm Meister zu folgen. Der führt zuerst zu dem, was die Epochen charakterisiert, dann zu dem, was in der geheimeren Kammer abgeschlossen ist, um dann zu dem besondere allerheiligste Vorbereitungen zu treffen, was für jede einzelne Seele, wenn wir die zweite Pforte überschritten haben, nicht anders als in freier Entschließung zu den Seelen sprechen darf. Wenn wir absehen von dem, was sonst aus den Zeiten zu den Seelen spricht, so kann man,",
      "wenn nicht ein äußeres Verhängnis oder dergleichen wirkt, eine Menschenseele nicht auf das aufmerksam machen, was sie erleben oder erwarten soll, sondern auf das, was durch die Gnade` der geistigen Führung der Menschheitsentwickelung in die Seelen sich hineinleben wird. Wir fühlen da zusammenwirken das, was das Geistesleben vorbereitet hat und dann zu dem Geistesleben unserer Zeit geworden ist. Da stehen wir und fühlen unsere Verantwortung gegenüber denen, welche die echten suchenden Seelen waren, und fühlen, wie wir das verantworten können, was wir getan haben. Wir lernen aber auch, daß wir nicht aus unserer Willkür heraus sagen: so soll man es, oder so muß man es machen! Denn warum sollte nicht auch dieses oder jenes so oder so begründet werden? Nein, wir fühlen uns verpflichtet das zu tun, was die schöpferischen Kräfte der Zeit von uns verlangen, nicht, was wir selbst verlangen oder verlangen können. Wir fühlen uns verpflichtet weiter zu schaffen im Sinne derer, die vor uns gesprochen haben, und sagen: Wir wollen nichts anderes heilig halten, als was ihr heilig hieltet und herbeisehntet. Aber wir wollen treu sein dem, was für euch durch die spirituellen Mächte geflossen ist. Dann werden Sie dieses verstehen und nicht auf viele Fragen, die sich vielleicht in diesen Tagen die einzelne Seele hat aufwerfen können, sagen, hier sei etwas unharmonisch verflossen, sondern Sie werden sich sagen: diese Menschen konnten nicht anders handeln, aber sie wußten auch, was sie taten.",
      "Alles drängte zu dem umfassendsten Geistesleben hin, das die Geisteswissenschaft der Welt geben wird, wenn wir die vergangenen Zeiten in Betracht ziehen. Schauen Sie nicht auf das, was von irgendwelchen willkürlichen Bestrebungen der Zeit herausfließt, sondern schauen Sie auf das, was die Zeiten selbst als Notwendigkeiten bringen. Fragen Sie nicht, wie der oder jener, der glaubt auf dem festen Boden der Naturwissenschaft zu stehen, über die Rätsel der Zeit und der Menschenseele denken will, weil er nicht übersehen kann, was in Betracht kommt. Fragen Sie die Großen, welche längst hingestorben sind, die mit Objektivität zu unserer Seele sprechen. Fragen Sie einen Menschen, der so unendlich viel für die Naturwissenschaft des 19. Jahrhunderts getan hat wie Alexander von Humboldt, der in seinem",
      "«Kosmos» ein so umfassendes Bild der Naturentwickelung geben wollte, fragen Sie ihn, wo er hinausdenken wollte über das, was den Naturerklärer interessiert, wo für ihn die tiefsten Rätsel aller Naturfragen berührt sind. Und seine Antwort ist: Das ist der hundertvierte Psalm Davids! - Dieser selbe Alexander von Humboldt aber war wieder eine sehnsüchtige Seele, eine Seele, die - ganz im Besitze der naturwissenschaftlichen Kultur ihrer Zeit - aus dem 19. Jahrhundert heraus den Blick auf das richtete, was aus dem inbrünstigen Fühlen der spirituellen Welt herausgeflossen ist, wie es in dem hundertvierten Psalm Davids zutage tritt. Fragen Sie jetzt, wie vieles von dem, was dort in dem hundertvierten Psalm in hymnenartiger Weise zur Menschenseele spricht, in konkreter Ausgestaltung - wie es für unsere Zeit notwendig ist - in der Geisteswissenschaft zu finden ist! Wenn wir das beachten, dürfen wir sagen: Was antwortet uns die Seele Alexander von Humboldts auf das, was wir tun? - Sie würde uns so antworten, daß sie uns sagte: Ersehnt haben wir das, was ihr versucht, und wir ahnten, daß es kommen muß! - Und Wilheim von Humboidt, der Bruder Alexanders, der große Sprachforscher, der letzte derjenigen Zeit, als in Europa die große Dichtung bekannt wurde, von der ich gestern gesprochen habe, die Bhagavad Gita, dieser große Geist, sprach ungefähr so, daß ei` sagte, er habe schon genug gelebt, nachdem in sein Leben hereingefallen ist die Bekanntschaft mit der Bhagavad Gita.",
      "So hat sich das 19. Jahrhundert in denjenigen Seelen, die am meisten suchend waren, vorbereitet, dasjenige objektiv und unbefangen zu empfangen, was über den ganzen Erdkr`eis hin der Menschheit an spirituellen Schätzen gegeben ist. So hat es sich vorbereitet, um nicht in Einseitigkeit zu verfallen.",
      "Ich wollte Ihnen nicht theoretische Auseinandersetzungen geben. Ich halte theoretische Auseinandersetzungen immer für sehr einseitig, selbst wenn sie die allerbesten sind. An Beispielen wollte ich Ihnen zeigen, wie die Tatsachen sind, und wie die Seelen unter der Gewalt realer Tatsachen empfinden. Ich möchte zurückkommen auf etwas, was Herman Grimm vorgeschwebt hat, wovon er mir sprach auf einem Wege von Weimar nach Tiefurt, was in seiner Seele lebte",
      "wie ein Gebäude, das er aufführen wollte, und wovon er selber in den einleitenden Bemerkungen zu seinen nachgelassenen Fragmenten so spricht, daß es ihm immer vor der Seele geschwebt hat, und daß alle seine einzelnen Arbeiten aus dem herausgeströmt sind, was so in seiner Seele lebte. Was war es, das ihm immer vorschwebte?",
      "Es war nichts geringeres als eine Entwickelungsgeschichte der Menschheit, die er darstellen wollte als eine Geschichte der Entwickelung der nationalen Phantasie der Menschheit aller Völker und Zeiten. Das war ihm das zu Schaffende.",
      "Er wollte untersuchen, wie zum Beispiel in Griechenland die schöpferische Macht der Phantasie gewirkt hat, wie sie einen Horn er, einen Ä`schylos, einen Sophokles an seine Stelle hingestellt hat, wie sie durch die Zeiten gegangen ist bis in die neue Zeit herauf und überall hingestellt hat, was dargestellt werden soll. Ein Mann schritt neben mir her, der den Glauben an die Wahrheit der Phantasie, das Schöpferische der Phantasie hatte, aber eine Welt war rings herum, die keine Anlage hatte, an dieses Schöpferische der Phantasie, an die Abstammung der Phantasie von dem Wahrheitvater zu glauben!",
      "Die Empfindung, welche Sie jetzt in dem dritten Mysterienspiel «Der Hüter der Schwelle» wiederfinden, wo Frau Balde wie ein Gespenst in den himmlischen Reichen erscheint - aber wie ein umgekehrtes Gespenst, denn sonst kommen Gespenster aus der übersinnlichen Welt, Frau Balde aber blickt hinauf und erscheint dort ebenso, wie die übersinnlichen Wesen herunterschreiten auf die Erde - diese Empfindung drängte sich damals in meine Seele und gestaltete sich als das Schicksal der Phantasie. An dieses Schicksal der Phantasie wird man denken müssen, wenn man auf das eingehen will, was Herman Grimm vorschwebte, ohne daß man etwas weiß über die Abstammung der Phantasie von dem Wahrheitvater.",
      "Niemals ist das zustande gekommen, was Herman Grimm vorgeschwebt hat. Er fühlte dunkel, daß da etwas zustande kommen würde, wenn es ihm gelänge, was er wollte. Aber - es ging nicht. Warum ging es nicht? Es ging deshalb nicht, weil einem die Phantasie, wenn man sie nur im allgemein-menschlichen Sinne als schöpferische Weltenmacht betrachten will, fortwährend entschlüpft.",
      "Man empfindet immer, wie die Macht, die man Phantasie",
      "nennt, zwar von der Wahrheit abstammt, aber nicht selbst zur Wahrheit, sondern nur zur Maja hinführen kann, und wie hinter allem, wohin die Phantasie führt, die spirituelle Welt steht, der gegenüber Herman Grimm jene abwehrende Handbewegung machte.",
      "In den letzten Tagen trat diese Empfindung mir wieder vor die Seele gegenüber dem Manne, der aus der Phantasie heraus den Gang der Menschheitsentwickelung schildern wollte, daß ich mir sagte: Er hat das Ideal gehabt, aus dem Geistesleben, aus den spirituellen Mitteln, die ihm seine Zeit gab, Befriedigendes über die Weltenrätsel zu finden. Aber was er aus seiner Zeit heraus erlangen, was er in ehrlicher, auf- richtiger Weise in seine Seele aufnehmen konnte, das gab ihm die Lösung nicht.",
      "Und weil er ehrlich war, unterließ er sie! Daraus ersehen wir, wie unsere Zeit nach dem verlangt, was die Weltenrätsel enthüllen kann, was Aufklärung über die schaffenden Kräfte und schaffenden Mächte geben kann, die hinter den sinnlichen Erscheinungen stehen und die Signatur der Sinneserscheinungen bewirken.",
      "Warum trat mir das in der letzten Zeit vor die Seele? Ich habe mich nie gescheut, auch das Persönliche, wenn das Persönliche objektiv ist, zu erwähnen, und jeder mag darüber denken, wie er will. Ich bestrebe mich, das Persönliche ganz objektiv zu betrachten.",
      "Es trat mir vor die Seele, weil es sich mir ganz von selbst verglich, was ein Geist wollte und nicht konnte, und was nun in einer gewiß schönen Weise zustande gekommen ist durch das Buch unseres verehrten Edouard Schur6 «L`Evolution divine». Lesen Sie es und nehmen Sie sich vor, es so zu lesen, daß Sie in die spirituelle Macht eindringen, die hinter allem Sinnenschein steht, die aber auch in dem Gang der Epochen als die schöpferische Phantasie gewirkt hat.",
      "Und Sie werden sehen, wie unsere Zeit auf das zu antworten beginnt, was heiße, sehnsüchtige, manchmal nicht einmal vollbewußte Fragen unseres Geisteslebens waren. Dann werden Sie in Ihrer Seele die Antwort finden, was Geisteswissenschaft sein soll, aber auch die Antwort, wie Geisteswissenschaft sein soll.",
      "Wie wir denken müssen, damit ein harmonisches Zusammenwirken im Geistesleben der Gegenwart sich einstellen könnte, das war mir ein Bedürfnis im Verlaufe des heutigen Vormittages Ihnen zu sagen."
    ],
    "sentences": [
      [
        "Der einzelne Mensch, welcher durch die Empfindungen und Sehnsuchten seiner Seele den Drang verspürt, an die theosophische Bewegung heranzutreten, wird - vielleicht ohne daß er sich dessen immer im vollen Umfange bewußt ist - die Befriedigung dessen suchen, was persönlich sein Herz begehrt, was ihm persönlich Ruhe über die großen Rätselfragen des Daseins bringen kann, über diejenigen Fragen, von denen er fühlt, daß er ohne ihre Beantwortung nicht mit dem Leben in der Epoche, in die er durch seine gegenwärtige Inkarnation hineingestellt ist, fertig werden kann.",
        "Wenn der einzelne dann da oder dort innerhalb des Geisteslebens seiner Epoche dasjenige findet, was er entgegennehmen kann, um zu diesen Befriedigungen seiner bangen und für ihn notwendigen Seelenrätsel zu kommen, dann sollte er sich aber auch bemühen, zu einem Verständnis davon durchzudringen, daß solches Geistesleben, das sich in irgendeine Epoche hereinstellt, auch für die einzelne Seele nur wirklich das bringen kann, was diese einzelne Seele in der richtigen Weise mit dem Geistigen verbindet, ohne daß diese Richtigkeit der einzelnen Seele immer bewußt wird, wenn solches Geistesleben im Einklange steht mit der Gesamtevolution der Menschheit und Rechenschaft abzulegen vermag vor der Gesamtevolution der Menschheit."
      ],
      [
        "Es mag da oder dort eine geistige Bewegung auftreten, einzelne Seelen mögen glauben, für sich dasjenige, was sie brauchen, in solchen Bewegungen finden zu können.",
        "Es kann das, was die Seele also bekommt, und wovon sie selbst glaubt damit befriedigt sein zu können, aber wertlos sein für die wirkliche Entwickelung der Seele, für die wirklichen Kräfte, welche die Seele suchen muß, wenn nicht dasjenige, was ihr als geistiges Leben begegnet, die volle Verantwortung übernehmen kann gegenüber der geistigen Führung und geistigen Leitung der Menschheit in irgendeiner Epoche, wenn nicht diese geistige Bewegung vor diejenigen Mächte hintreten kann, welche die Führung des Geisteslebens der Menschheit haben, und sich vor diesen"
      ],
      [
        "Mächten verantworten kann, indem sie von diesen Mächten sozusagen ausgesprochen erhält: Ja, es geschieht mit der geistigen Bewegung dasjenige, was die Zeit verlangt, was die geistigen Kräfte verlangen, welche in die Zeit hereinragen. - Der einzelne Theosoph mag wohl ab und zu auch das Bedürfnis haben Ausschau zu halten, wie das, was er entgegennimmt, zu dem gesamten geistigen Leben steht oder sich auf den verschiedensten Gebieten äußert, was aber vielleicht mehr die Sehnsucht ausdrückt als das Bedürfnis, von der Zeit die Lösung der Rätselfragen zu erwarten, die durch die Geisteswissenschaft gewonnen werden soll.",
        "Die theosophische Seele mag, wenn sie auf dasjenige blickt, was sie mit einiger Befriedigung aus der Geisteswissenschaft heraus empfängt, gar manchmal unbefriedigt oder vielleicht auch unsympathisch auf das blicken, was uns überall als Geistesleben in unserer Zeit so umgibt, daß dieses Geistesleben vermeint, auch mit den höchsten Daseinsfragen, den höchsten Rätseln des Menschendaseins zu tun zu haben."
      ],
      [
        "Manches, was da draußen auftritt und ringt nach der Lösung der Daseinsrätsel, nach der Beantwortung der Fragen des Daseins, mag als materialistisch, oberflächlich, ungenügend von mancher Seele empfunden werden, welche die Geisteswissenschaft aufnimmt.",
        "Unbefangener Beobachter ist in diesem äußeren Leben aber so mancher, der von der Geisteswissenschaft nichts weiß, so mancher, der auch nicht einmal ahnen kann, was in dem, was wir Geisteswissenschaft nennen, lebt, und der aufrichtig und ehrlich nach der Wahrheit in unserer Epoche ringt, dessen Seele eben ehrlich und aufrichtig nach den Daseinsrätseln hin die tiefste Sehnsucht empfindet."
      ],
      [
        "Nicht mit einem oberflächlichen, alles nivellierenden Blick sollen wir unsere Mitwelt, das was außer uns steht, überschauen, sondern mit einem unterscheidenden"
      ],
      [
        "Blick, denn nur dadurch können wir die Möglichkeit gewinnen, in der richtigen Weise an das anzuknüpfen, was da ist.",
        "Es kann natürlich nicht in einem einstündigen Vortrage vieles von dem erwähnt werden, woran die, welche die spirituellen Leiter unserer Bewegung sind, heute anknüpfen müssen, was sie voll berücksichtigen müssen.",
        "Deshalb kann nur einzelnes herausgehoben werden, und an einzelnen Exempeln soll gezeigt werden, worin draußen in der Welt die"
      ],
      [
        "Rätselfragen pulsieren, zu deren Beantwortung, zu deren Befriedigung Geisteswissenschaft sich anschicken will."
      ],
      [
        "Wenn Sie die Welt betrachten, so werden Sie insbesondere finden, daß suchende Seelen - Seelen, denen sich die Daseinsrätsel so recht ins Herz hineindrücken - sich sagen: Wessen bedürfen wir heute, was müssen wir fragen, wo können uns Aussichten über die Ziele des Lebens herkommen? - Seelen, so empfindend, finden sich zahlreich namentlich unter denen, die sich aus der praktischen Technik, der Praxis des Lebens, der Praxis der Arbeit herausarbeiten.",
        "Nicht einmal unter den der Philosophie Geneigten sind so viele, die in bangster Weise so denken, als unter den Lebenspraktikern, die ihre Hände unter der Mechanisierung des Lebens abmühen, die dafür aber nach dem hinblicken, was oft die Seele erfüllt, wenn sie nach den Rätseln des Lebens fragen muß.",
        "Wir müssen wohl hinhorchen auf solche Seelen, denn wir müssen uns vorstellen, daß die Geisteswissenschaft einst zu antworten hat, Rechenschaft abzulegen hat den leitenden Mächten der Welt gegenüber.",
        "Solche Seelen aber gehören zu den besten suchenden Seelen der Gegenwart, und es kann eine Epoche kommen, wo sie herantreten an die Führer des geistigen Lebens, und wo diese auf die Lebensrätsel antworten müssen, die sich unter dem Druck der praktischen Interessen des Lebens herausgebildet haben.",
        "Wir brauchen uns nur nicht selber zu blenden, müssen nur den Sinn für das haben, was im Leben vorgeht, und es wird uns überall entgegentreten, wo die wahren Stimmen der Seelensucher sind."
      ],
      [
        "Wer in der letzten Zeit entweder an Buchhandlungen vorbeigegangen ist oder sich an den Bahnhofsbuchhandlungen umgesehen hat, was dort ausgelegt war, und nicht nur hingegangen ist mit dem Bestreben, nur das sich auszusuchen, was er sich kaufen will, der wird überall deutlich ausgelegt gefunden haben ein Buch, das er vielleicht, wenn er Theosoph ist, nicht mit viel Interesse lesen kann, wenn er nur daran denkt, die eigenen Seelenbedürfnisse zu befriedigen, das er aber mit Interesse lesen wird, wenn er sich sagt: wie müssen sich die Dinge stellen, wenn wir mit Antworten auf die Fragen nach den Lebensrätseln den suchenden Seelen entgegenkommen"
      ],
      [
        "wollen?",
        "Da lag ein Buch aus von einem im praktischen Leben ausgezeichneten Mann, und las man die ersten Seiten, so konnte man sich überzeugen, daß er einen guten Überblick Über unser Zeitalter hat, daß unsere Zeit aufrückt zu der Mechanisierung des äußeren Lebens, daß die Kräfte menschlicher Arbeit immer mehr und mehr hineingedrängt werden in die maschinenmäßige Arbeit."
      ],
      [
        "Es ist das Buch «Zur Kritik der Zeit» von Walther Rathenau.",
        "Es ist ein Buch eines unsere Zeit kennenden Menschen, den derjenige auch kennenlernen sollte, der in der Geisteswissenschaft mitsprechen will."
      ],
      [
        "Es ist darin dargestellt, wie in unserer Zeit alles mechanisiert wird, und warum das so kommen mußte.",
        "Für umfassende Begriffe wird das größtenteils unrichtig dargestellt, ja, man wird vielleicht mit keinem Ausdruck darin übereinstimmen können, aber darum handelt es sich nicht."
      ],
      [
        "Sondern darum handelt es sich, was die suchenden Seelen in unserer Zeit sagen, und welches die Kräfte sind, mit denen sie suchen, besonders wenn es ein Mensch des praktischen Lebens ist, wie es der Verfasser dieses Buches ist.",
        "Ich möchte Ihnen zu Beginn unserer Betrachtung etwas aus einer Stelle dieses Buches vorlesen, die mir wie aus dem Zentrum der Seelenstimmung der Seelen Europas und Amerikas gesprochen erscheint."
      ],
      [
        "Man hört darin förmlich, was unzählige Seelen nicht aussprechen können, was in ihnen Fragen anregen kann, wenn man eine solche Persönlichkeit versteht, wo sie aus sich heraus von der Zeit und der Zeitenseele spricht und sagt: «Sie - die Zeit - sucht ihre Seele und wird sie finden» - trotzdem können Sie in dem ganzen Buche nicht einen einzigen Anhaltspunkt finden, wie die Zeit ihre Seele finden mag, nur Sehnsucht, der Trieb nach etwas Unbekanntem - «freilich gegen den Willen der Mechanisierung.",
        "Dieser Epoche lag nichts daran, das Seelenhafte im Menschen zu entfalten; sie ging darauf aus, die Welt benutzbar und somit rationell zu machen, die Wundergrenze zu verschieben und das Jenseitige zu verdecken."
      ],
      [
        "Dennoch sind wir wie je zuvor vom Mysterium umgeben; unter jeder glatten Gedankenfläche tritt es zutage, und von jedem alltäglichen Erlebnis bedarf es eines einzigen Schrittes bis zum Mittelpunkt der Welt.» In diesem Buche wird nirgends angedeutet, wie dieser Schritt gemacht werden soll von den uns umgebenden"
      ],
      [
        "Mysterien bis zum Mittelpunkt der Welt.",
        "«Die drei Emanationen der Seele: die Liebe zur Kreatur, zur Natur und zur Gottheit konnte die Mechanisierung dem Einzelleben nicht rauben; für das Leben der Gesamtheit wurden sie zur Bedeutungslosigkeit verflüchtigt."
      ],
      [
        "Menschenliebe . . .» - das sagt ein Praktiker der Gegenwart, der sich mit nüchternem Blick seiner Zeit so entgegenstellt, wie er sich ihr entgegenstellen kann, der durch Jahrzehnte selbst angegriffen hat, was in Europa und darüber hinaus die Fäden des ökonomischen Lebens sind, und der selber daran mitgearbeitet hat - «Menschenliebe sank zum kalten Erbarmen und zur Fürsorgepflicht herab, und bedeutet dennoch den ethischen Gipfel der Gesamtepoche; Naturliebe wurde zum sentimentalen Sonntagsvergnügen; Gottesliebe, überdeckt vom Regiebetriebe mythologisch-dogmatischer Ritualien, trat in den Dienst diesseitiger und jenseitiger Interessen und wurde so nicht bloß unedlen Naturen verdächtig.» Weiter sagt Rathenau Worte, auf die der, welcher den Geistesbedürfnissen der Zeit entgegenkommen will, mit gutem Willen entgegenkommen will, hinhören muß, wenn sie auch partiell unrichtig sind, denn sie drücken das aus, was berechtigt aus den Seelen herausströmt und in zukünftigen Zeiten immer mehr aus den Seelen herausströmen wird: Empfindungen, gegen die sich keiner, der Geisteswissenschaft treibt, auflehnen darf, ohne daß ihn das Karma der Zeit treffen wird.",
        "«Es gibt wohl keinen einzigen Weg, auf dem es dem Menschen nicht möglich wäre, seine Seele zu finden, und wenn es die Freude am Aeroplan wäre."
      ],
      [
        "Aber die Menschheit wird keine Umwege beschreiten.» Das ist Bedürfnis der Zeit.",
        "Das können wir hören, wie die Zeit es ablehnen wird etwas entgegenzunehmen, was unmittelbar zu den Tiefen der Seele, was übersinnlich zu den Tiefen der Seele sprechen wird."
      ],
      [
        "Diese Zeit wird sagen: «Es werden keine Propheten kommen und keine Religionsstifter, denn diese übertäubte Zeit läßt keine Einzelstimme mehr vernehmlich werden: sonst könnte sie heute noch auf Christus und Paulus hören.",
        "Es werden keine esoterischen Gemeinden die Führung ergreifen, denn eine Geheimlehre wird schon vom ersten Schüler mißverstanden, geschweige vom zweiten."
      ],
      [
        "Es wird keine Einheitskunst der Welt ihre Seele bringen, denn die Kunst ist"
      ],
      [
        "ein Spiegel und ein Spiel der Seele, nicht ihre Urheberin.» Man möchte sagen: So hat sich vor einigen Monaten ein Mann vernehmen lassen.",
        "Und was haben wir seit zehn Jahren getan?",
        "Wir haben uns bemüht, Antwort zu finden auf das, was so aus der Zeit heraus als ihre Kräfte sich spinnt.",
        "Und weiter sagt er: «Das Größte und Wunderbarste ist das Einfache.",
        "Es wird nichts geschehen, als daß die Menschheit unter dem Druck und Drang der Mechanisierung, der Unfreiheit, des fruchtlosen Kampfes die Hemmnisse zur Seite schleudern wird, die auf dem Wachstum ihrer Seele lasten.",
        "Das wird geschehen nicht durch Grübeln und Denken, sondern durch freies Begreifen und Erleben.",
        "Was heute viele reden und einzelne begreifen, das werden später viele und zuletzt alle begreifen: daß gegen die Seele keine Macht der Erde standhält.»"
      ],
      [
        "Daß gegen die Seele keine Macht der Erde standhält!",
        "Das bedingt unser Vertrauen, daß wir in die Zukunft hineinwachsen mit dem, was wir haben, und uns im Einklang wissen mit den Besten der Zeit, die nichts von uns wissen oder gar nichts wissen wollen.",
        "Aber wir wollen uns nicht verleiten lassen gegen das, wonach unsere Zeit dürstet, irgend etwas zu unternehmen, denn wir wissen, die Führung der Menschheit ist höheren, spirituellen Mächten überlassen, und das, was sich in der Menschheit äußert, kommt von diesen spirituellen Mächten, auch wenn es selbst anders erscheinen mag als das, was wir selbst wollen, wenn es nicht durch irgendwelche Willkür, sondern so erzeugt erscheint, daß es wie mit elementarer Gewalt aus dem Zentrum der Seelen mit dem Impuls der Zeit hervorkommt.",
        "So spricht zu uns unsere Zeit.",
        "Wie sprechen diejenigen Erscheinungen, die unsere Zeit herbeigeführt haben?"
      ],
      [
        "Ich möchte zunächst von etwas ausgehen, wohin sich meine Gedanken im Verlaufe dieses Vortragzyklus schon einmal lenkten.",
        "Unter den mancherlei Persönlichkeiten, die mir in der Zeit entgegengetreten sind, als ich noch nicht innerhalb der Theosophischen Gesellschaft war, war - wie ich vor einigen Tagen erwähnt habe - auch der Kunsthistoriker Herman Grimm, der mit allem, was er im einzelnen leistete, nichts anderes wollte, als sich bewußt in die Bedürfnisse unserer Zeit hineinzustellen.",
        "Sehr Merkwürdiges konnte man mit ihm"
      ],
      [
        "erleben.",
        "Herman Grimm hat sich in den sechziger Jahren des vergangenen Jahrhunderts herangemacht, eine Biographie Michelangelos zu schreiben.",
        "Wer sie heute in die Hand nimmt; wird sie, wenn er nicht von Vorurteilen befangen ist, als das Beste finden, was über Michelangelo geleistet worden ist."
      ],
      [
        "Herman Grimm hat in langer Arbeit sich bemüht, ein gerundetes Bild des Wirkens und Schaffens Michelangelos zu vollenden.",
        "Es ist ihm auch gelungen, ein Bild dieser Zeit zu schaffen.",
        "Er hat dann auch begonnen, ein Leben Raffaels zu schreiben."
      ],
      [
        "Es gehörte zu den beständigen Geständnissen, die man aus Herman Grimm heraushören konnte, daß es ihm gegenüber Raffael ganz anders erging.",
        "Michelangelo konnte er so beschreiben, daß er ein fertiges Bild dieser Persönlichkeit hinstellen konnte, Raffael nur so, daß es für ihn selbst nimmermehr genügte."
      ],
      [
        "Warum?",
        "Herman Grimm war ein Mensch, der bei allem, was er begreifen wollte, immer die ursprünglichen Ursachen suchte, und bei Raffael konnte er eben die ursprünglichen Ursachen nicht finden.",
        "Wenn er irgendwie mit etwas über Raffael fertig war, dann mußte er finden, daß die Sache doch wieder höchst unvollkommen gelöst war."
      ],
      [
        "Dennoch setzte er immer wieder an, auch kurz vor seinem Tode noch einmal, um ein Leben Raffaels zu schreiben, doch es ist nicht fertig geworden.",
        "Ein kurzes Fragment darüber ist dann in seinen nachgelassenen Fragmenten erschienen."
      ],
      [
        "Herman Grimm selber sagte sich etwa: «Ob es mir diesmal anders gelingen wird, wenn ich noch so lange leben werde, irgend etwas zustande zu bringen, was für mich sich deckt mit dem, was man über Raffael wissen möchte?» Es war kurz vor seinem Tode, als er wieder damit anfing, denn es war das Fragment, dem gegenüber er die Feder aus der Hand gelegt hat und gestorben ist.",
        "Es ist nur ein Fragment, als er selber noch dazu gekommen war, ein «Leben Raphaels» zu schreiben."
      ],
      [
        "Ich selber mußte, als ich diese Worte in seinem Nachlaß las, eines Momentes gedenken, da ich mit ihm in einem kleinen Kreise einmal zusammen war und gesprochen habe, wie ich es wollte, von den geistigen Angelegenheiten der Menschheit.",
        "Ich hatte Herman Grimm sehr lieb und werde ihn immer gleich lieb haben."
      ],
      [
        "Er war eine Persönlichkeit, streng eingeschlossen in das Geistesgebiet, das er sich zubereitet"
      ],
      [
        "hatte, und er hatte eine Antwort auf das, was ich so gerne hätte ein- fließen lassen.",
        "Sie bestand in folgendem: es war eine bloße Handbewegung des Ablehnens gegenüber dem, was sich in die` Insel seines Geisteslebens etwa hätte von außen her hineinbewegen können von dem, was nicht von ihm mit den Kräften, die man in seiner Zeit haben konnte, aufgenommen werden konnte.",
        "Wer mit ihm umzugehen wußte, der verstand ihn und seine Hand, wie sie um die Tischecke herum in ablehnender Bewegung sich befand.",
        "Für mich war diese Handbewegung die Grenze zwischen dem, bis wohin ein Geist geht, der mit den geistigen Elementen seiner Epoche dieselbe neu beleben will, und dem, was als neue Kräfte in unsere Zeit einfließen muß.",
        "Das war im Jahre 1892."
      ],
      [
        "Warum - ich möchte alles andere jetzt nur in Ihren Seelen anregen - konnte Herman Grimm aus den geistigen Elementen, die in seiner Seele lebten, mit dem Leben Raffaels nicht zustande kommen?",
        "Geben Sie sich die Antwort mit alle dem, was für das Geistesleben einer Zeit notwendig sein wird, die so etwas wie das Leben Raffaels wird verstehen wollen."
      ],
      [
        "Damit sage ich nicht, daß das Leben Raffaels etwas Höheres sein muß als zum Beispiel das Leben Michelangelos, sondern ich stelle nur ein Faktum für die Menschenseele vor Sie hin.",
        "Versuchen Sie sich eine Antwort zu geben."
      ],
      [
        "Man kann sie sich geben, wenn man den Blick schweifen läßt über das erste Bild, das unser drittes Mysteriendrama, «Der Hüter der Schwelle», eröffnet.",
        "Da finden Sie vier Bilder: Elias, Johannes der Täufer, Raffael, Novalis."
      ],
      [
        "Mit dem, was im Laufe unserer jahrelangen geisteswissenschaftlichen Arbeit hat zutage treten können, so daß es plausibel, beweiskräftig erscheinen konnte, haben wir uns bemüht zu zeigen, wie eine gleiche Seelen-Individualität - sich wiederinkarnierend - von Elias zu Johannes dem Täufer hinübergeht, in Raffael wiedergeboren wird, dann in Novalis wiedererscheint.",
        "So phantastisch das heute erscheinen mag, so wahr wird man es in einer gar nicht so fernen Zukunft finden, daß man mit dem Begreifen der Welt scheitern wird, wenn man nicht zu Hilfe nehmen wird die Idee der Reinkarnation der Menschenseele und das Karma, das durch die verschiedenen Erdenleben hindurchgeht, was man die spirituellen Zusammenhänge"
      ],
      [
        "der Welt nennt.",
        "Der erst wird Raffaels Leben beschreiben, der von dem Leben ausgeht, das durch die Geisteswissenschaft erkannt wird.",
        "Überall tritt drängend und fragend in unserer Zeit an die Menschenseele heran der Zusammenhang des geistigen Lebens in aller Welt, setzt Fragen hin wie die: Wie kommt es, daß plötzlich im menschlichen Leben Gedanken auftreten wie aus eigener Seele entspringend, die in fern davon liegenden Zeiten da waren und nun wieder auftreten? - Man kann in die Art hineinschauen, wie das geistige Leben wirklich wirkt, wie es in den aufeinanderfolgenden Epochen die Gedanken immer wieder erscheinen läßt, wenn man die geistigen Gedankengänge kennt, welche die Geisteswissenschaft zu enthüllen vermag."
      ],
      [
        "Es ist in den letzten Wochen ein höchst Bedeutsames im deutschen Geistesleben erschienen.",
        "Es wird Ihnen sonderbar erscheinen, daß ich es für bedeutsam halte.",
        "Aber ich muß es für bedeutsam halten, denn es ist symptomatisch bedeutsam.",
        "Ich habe, als ich in Weimar mit Goethe beschäftigt war, viele Persönlichkeiten kennengelernt, die mit der deutschen Gelehrsamkeit tonangebend zusammen- stehen.",
        "Unter den mancherlei Germanisten trat mir damals einer entgegen, von dem ich mir außerordentlich Bedeutsames auf seinem Felde versprechen konnte.",
        "Es ist Konrad Burdach, der damals Professor in Halle war, dann diesen Posten verlassen hat, um als Privatgelehrter weiterzuleben.",
        "Nun hat Konrad Burdach in den letzten Wochen in den Versammlungen der Berliner Akademie der Wissenschaften eine höchst interessante Abhandlung vorgelegt.",
        "Sie figuriert zwar zunächst nur unter den akademischen Schriften, doch ist darin eine bedeutsame Frage aufgeworfen - aber eine Frage, die man nicht mit den Mitteln Konrad Burdachs lösen kann, sondern die nur mit den Mitteln der Geisteswissenschaft beantwortet werden kann.",
        "Sie werden sich überzeugen, daß es einem Bedürfnis der einzelnen Seele sehr naheliegt, wenn sie über die Zusammenhänge des Lebens nachdenkt, sich zu fragen: Wie steht das Faust-Gedicht der modernen Seele gegenüber? - Haben wir nicht in dem Faust den Lebenspraktiker unserer Zeit hingestellt, der - am Schlusse seines langen Lebens angelangt - vor allem ein praktisches Ideal vor sich hat?"
      ],
      [
        "Schauen wir uns Goethe an in seinem praktischen Schaffen: wir können es verfolgen, wie er zu Eckermann, seinem getreuen Sekretär, spricht.",
        "Goethe ist genötigt, die spirituelle Entwickelu`ng des Faust darzustellen.",
        "Ihm kommt der geistige Inhalt von Raffaels Madonna Sixtina in den Sinn; er konnte diesen erst in seiner späteren Lebenszeit erfassen, weil er ihn zum Beispiel beim ersten Besuch in Dresden noch nicht erfaßt hatte.",
        "Er wollte darstellen, wie zum Schluß Fausts Unsterbliches in die höheren Welten aufgenommen wird.",
        "Wir sehen, er ringt mit seinem Problem so, daß er einst zu Eckermann sagte: Es ist merkwürdig, wie dämonische Gewalten durch die Welt gehen und aus einem unbekannten Übersinnlichen Gestalten wie Raffael heraussprießen lassen, wie man nicht fertig wird mit Gestalten wie Raffael, ohne daß man sie erklären wird aus ihrem Hervorgehen aus dem Ubersinnlichen heraus. - Man kann ein Gefühl davon haben, wie Goethe gerungen hat von dem allmählichen Übergehenlassen der Entelechie, von dem allmählichen Übergehen der Gestalten in die höheren Welten, bis er dann fertig wird mit einem Menschen, den er zugleich als einen Lebenspraktiker für die kommenden Jahrhunderte hingestellt hat."
      ],
      [
        "Konrad Burdach hat für die Philologie ein Merkwürdiges hingestellt.",
        "Wer seine Abhandlung liest, hat das Gefühl: es ist doch sonderbar, wie es der reinen Philologie gelungen ist, ein Parallelbild aus den früheren Jahrhunderten dem Faust an die Seite zu stellen.",
        "Es werden die alten Gestalten nur in moderner Form, als wenn sie Goethe gestaltet hätte, wieder hingestellt.",
        "Die ganze Moses-Geschichte wird in dieser Weise, als wenn es Goethe gedacht hätte, für seine Zeit hingestellt.",
        "Konrad Burdach will damit zeigen, wie in Goethes Denkweise alles einfließt, was sich um die Moses - Gestalt herumgegliedert hat."
      ],
      [
        "So steht ein Mann vor der Pforte, hinter welcher die Übersinnliche Welt ist, die Antworten gibt auf die Frage: Inwiefern sind Gedanken, sind spirituelle Mächte reale Kräfte, die durch die Zeit hindurchwirken und in den verschiedensten Zeiten angemessen diesen Epochen wieder hervortreten?",
        "Überall wo wir hinblicken, pocht heute die Welt an die Pforte der übersinnlichen Welt.",
        "Unsere Pflicht"
      ],
      [
        "ist es, zu unserem Verantwortlichkeitsgefühl gehört es, die Welt, wo sie ehrlich und aufrichtig, nicht aus der persönlichen Willkür heraus fragt, so zu hören, wie es den Empfindungen, den Gefühlen der Seelen angemessen ist.",
        "Dabei kommt nicht in Betracht, was wir uns selber einbilden, wie die wahre Entwickelung der Menschheit sein soll."
      ],
      [
        "Ablesen sollen wir aber an den wirklich besten und sehnenden Seelen, wie sie selber in die spirituelle Welt hineinkommen wollen, und zurückhalten das, was wir selber für uns als das Wichtige halten, um es denen geben zu können, die da suchen.",
        "Gegenüber einer solchen Kultur, wie die ist, aus der wir heraus arbeiten wollen, und in der viele auswärtige Freunde in Europa und Amerika mit uns deshalb zusammenarbeiten, weil sie wissen, daß es nichts mit Nationalität zu tun hat, schickt es sich nicht darüber zu streiten, was orientalisch, was okzidentalisch ist, in der ein tonangebender Geist gesagt hat: «Gottes ist der Orient, Gottes ist der Okzident!» Das sind Worte Goethes, die uns in der Seele leben, und aus denen heraus wir wirken."
      ],
      [
        "Aber in den Seelen - nicht bloß in den unsrigen, sondern auch in denen, auf die wir hören müssen - leben nicht nur unsere willkürlichen Gedanken, die uns vorschreiben, was wir den anderen zu geben haben, sondern in den Seelen leben Empfindungen, welche die Geister der Jahrhunderte geschaffen haben.",
        "Suchen wir eine der uns entgegentretenden Gruppen auf."
      ],
      [
        "Gehen Sie mit mir zu einer der Leistungen, die - wie die Goethes sind - ganz außerordentlich bezeichnend sind für das Empfindungsleben gegenüber der spirituellen Welt und gegenüber den Gestalten, die in der spirituellen Evolution der Menschheit wirken.",
        "Gehen Sie mit mir zu einem Kapitel des «Wilhelm Meister» von Goethe."
      ],
      [
        "Verfolgen wir es zusammen, wie er den Wilhelm Meister als den Repräsentanten der Menschheit bewußt hinstellen wollte.",
        "Da sehen wir, wie Wilhelm Meister an einem Schlosse ankommt, wie er von dem Führer des Schlosses geführt wird und ihm die Schönheiten des Schlosses gezeigt werden, unter anderem auch die Bildergalerie."
      ],
      [
        "In dieser ist auch enthalten, was den Entwickelungsgang der Menschheit durch die verschiedenen Epochen hindurch darstellen kann, und man sieht daran, wie sich die Menschheit aus uralten Zeiten immer weiter und weiter bis zur Zerstörung"
      ],
      [
        "Jerusalems entwickelt hat.",
        "Man soll durch die aufeinander- folgenden Bilder begreifen, wie es durch die Kräfte, die in der Evolution der Menschheit wirken, bis zur Zerstörung Jerusalems gekommen ist.",
        "Der, welcher geführt wird, Wilhelm Meister, dessen Erziehung der Seele uns geschildert werden soll, fragt seinen Führer: Warum ist hier der Gang der Menschheitsentwickelung bis zur Zerstörung Jerusalems dargestellt und gar nicht innerhalb dieses Ganges das, was kurz davor in die Entwickelung hereingefallen ist: das Leben des Christus mit alle dem, was er in Palästina vollbracht hat? - Da sagt der Führer zu Wilhelm Meister: Dieses in gleicher Weise darzustellen wie den übrigen Gang der Menschheitsentwickelung, verbietet uns das, was unser Heiligstes ist."
      ],
      [
        "Was du hier dargestellt siehst, ist dasjenige, was an Kräften in der Weltgeschichte wirkt und so wirkt, daß es in seinem Zusammenwirken die Menschengruppen, die Nationen angeht, nicht aber die Kräfte, welche im einzelnen ein- gegriffen haben in das Leben einzelner Menschen.",
        "Es wäre falsch, in diese Bilderreihe den Christus hineinzustellen, denn der Christus wendet sich intim an jede einzelne Seele, und jede einzelne Seele hat mit ihm fertig zu werden."
      ],
      [
        "Dann führt der Führer den Wilhelm Meister in ein zweites, geheimeres Gemach, wo dargestellt ist, was nicht im gewöhnlichen Sinne in den epochalen Gang der Menschheitsentwickelung hineingestellt werden kann.",
        "Da sind wieder Bilder: für sich ist dasjenige hingestellt, was anknüpft an das Mysterium von Golgatha."
      ],
      [
        "In Bildern ist dargestellt vor Wilhelm Meister alles, was an den Christus anknüpft, bis - ja, bis zum Abendmahl.",
        "Nicht ist dasjenige da, was sich an das Abendmahl nun als das eigentliche Mysterium von Golgatha anschließt."
      ],
      [
        "Warum, fragt wieder Wilhelm Meister seinen Führer, ist hier in diesem geheimeren Kabinett das dargestellt, was bis zum Abendmahl hinführt, und nicht dasjenige, was sich daran anschließt?",
        "Er erhält die Auskunft, daß zunächst keine menschliche Seele in der Lage ist> das, was sich daran anschließt, so darzustellen, daß es das menschliche Gemüt nicht verletzen könnte."
      ],
      [
        "Goethe empfand noch in seiner Zeit aus seinem Spirituellen heraus die Ohnmacht, das große Mysterium darzustellen, weil er wußte, man möchte sagen, auch aus noch unbewußtem Wirken, daß"
      ],
      [
        "- die tiefsten Gefühle des Seelenlebens herausgeholt werden müssen, wenn man das Heiligste für die Seele erstreben und vor die Seele hin- stellen soll.",
        "So zeigt uns sein Wilhelm Meister, wie man eine zweifache Pforte des Esoterischen überschreiten soll, wenn man sich diesem Heiligen in seiner Seele nähern will."
      ],
      [
        "Was ist damals in Goethes Seele zum Ausdruck gekommen?",
        "Es ist zum Ausdruck gekommen, daß, wenn in der neueren Kultur sich die Seele innerhalb ihrer selbst richtig erfaßt, diese neuere Kultur in die Seele ein Heiligstes, ein Hehrstes hineinlegt, das Goethe fühlen mußte.",
        "Was seiner Zeit noch nicht gegeben war, um dieses Heiligste darzustellen, muß aber kommen.",
        "Es muß mit ganz anderen Mitteln in den Seelen wirken.",
        "Wer die Verantwortlichkeit gegenüber dem fühlt, was in der Zeit solche Empfindungen gezeitigt hat, der steht nun der spirituellen Welt gegenüber mit vollem Verantwortlichkeitsgefühl und glaubt diesem Verantwortlichkeitsgefühl nur dienen zu können, wenn er nichts anderes tut, als die Seelen darauf hinzuweisen, wie in unserer Zeit die Epoche reif wird, daß die Seelen, wenn sie zum spirituellen Leben heranwachsen, dasjenige erringen werden, was für den Blick des Wilhelm Meister sich erst nach zweifachem Überschreiten der Pforte zu den höheren Geheimnissen erschließen soll.",
        "So wäre die Atmosphäre, die aus dem geistigen Leben der Zeit in unsere Seelen strömt, wenn wir von dem Christus-Geheimnis sprechen wollten, das sich uns enthüllen soll, sprechen wollten von der Intimität, die zwischen der Seele und dieser gewaltigen Macht der Weltentwickelung bestehen wird, wenn jede einzelne Seele reif wird, daß der aus der geistigen Welt heraus neu sich offenbarende Christus intim jeder einzelnen Seele sich nähern wird."
      ],
      [
        "Wir wußten, daß wir nicht anders handeln durften, als dem Führer des Wilhelm Meister zu folgen.",
        "Der führt zuerst zu dem, was die Epochen charakterisiert, dann zu dem, was in der geheimeren Kammer abgeschlossen ist, um dann zu dem besondere allerheiligste Vorbereitungen zu treffen, was für jede einzelne Seele, wenn wir die zweite Pforte überschritten haben, nicht anders als in freier Entschließung zu den Seelen sprechen darf.",
        "Wenn wir absehen von dem, was sonst aus den Zeiten zu den Seelen spricht, so kann man,"
      ],
      [
        "wenn nicht ein äußeres Verhängnis oder dergleichen wirkt, eine Menschenseele nicht auf das aufmerksam machen, was sie erleben oder erwarten soll, sondern auf das, was durch die Gnade` der geistigen Führung der Menschheitsentwickelung in die Seelen sich hineinleben wird.",
        "Wir fühlen da zusammenwirken das, was das Geistesleben vorbereitet hat und dann zu dem Geistesleben unserer Zeit geworden ist.",
        "Da stehen wir und fühlen unsere Verantwortung gegenüber denen, welche die echten suchenden Seelen waren, und fühlen, wie wir das verantworten können, was wir getan haben.",
        "Wir lernen aber auch, daß wir nicht aus unserer Willkür heraus sagen: so soll man es, oder so muß man es machen!",
        "Denn warum sollte nicht auch dieses oder jenes so oder so begründet werden?",
        "Nein, wir fühlen uns verpflichtet das zu tun, was die schöpferischen Kräfte der Zeit von uns verlangen, nicht, was wir selbst verlangen oder verlangen können.",
        "Wir fühlen uns verpflichtet weiter zu schaffen im Sinne derer, die vor uns gesprochen haben, und sagen: Wir wollen nichts anderes heilig halten, als was ihr heilig hieltet und herbeisehntet.",
        "Aber wir wollen treu sein dem, was für euch durch die spirituellen Mächte geflossen ist.",
        "Dann werden Sie dieses verstehen und nicht auf viele Fragen, die sich vielleicht in diesen Tagen die einzelne Seele hat aufwerfen können, sagen, hier sei etwas unharmonisch verflossen, sondern Sie werden sich sagen: diese Menschen konnten nicht anders handeln, aber sie wußten auch, was sie taten."
      ],
      [
        "Alles drängte zu dem umfassendsten Geistesleben hin, das die Geisteswissenschaft der Welt geben wird, wenn wir die vergangenen Zeiten in Betracht ziehen.",
        "Schauen Sie nicht auf das, was von irgendwelchen willkürlichen Bestrebungen der Zeit herausfließt, sondern schauen Sie auf das, was die Zeiten selbst als Notwendigkeiten bringen.",
        "Fragen Sie nicht, wie der oder jener, der glaubt auf dem festen Boden der Naturwissenschaft zu stehen, über die Rätsel der Zeit und der Menschenseele denken will, weil er nicht übersehen kann, was in Betracht kommt.",
        "Fragen Sie die Großen, welche längst hingestorben sind, die mit Objektivität zu unserer Seele sprechen.",
        "Fragen Sie einen Menschen, der so unendlich viel für die Naturwissenschaft des 19.",
        "Jahrhunderts getan hat wie Alexander von Humboldt, der in seinem"
      ],
      [
        "«Kosmos» ein so umfassendes Bild der Naturentwickelung geben wollte, fragen Sie ihn, wo er hinausdenken wollte über das, was den Naturerklärer interessiert, wo für ihn die tiefsten Rätsel aller Naturfragen berührt sind.",
        "Und seine Antwort ist: Das ist der hundertvierte Psalm Davids! - Dieser selbe Alexander von Humboldt aber war wieder eine sehnsüchtige Seele, eine Seele, die - ganz im Besitze der naturwissenschaftlichen Kultur ihrer Zeit - aus dem 19.",
        "Jahrhundert heraus den Blick auf das richtete, was aus dem inbrünstigen Fühlen der spirituellen Welt herausgeflossen ist, wie es in dem hundertvierten Psalm Davids zutage tritt.",
        "Fragen Sie jetzt, wie vieles von dem, was dort in dem hundertvierten Psalm in hymnenartiger Weise zur Menschenseele spricht, in konkreter Ausgestaltung - wie es für unsere Zeit notwendig ist - in der Geisteswissenschaft zu finden ist!",
        "Wenn wir das beachten, dürfen wir sagen: Was antwortet uns die Seele Alexander von Humboldts auf das, was wir tun? - Sie würde uns so antworten, daß sie uns sagte: Ersehnt haben wir das, was ihr versucht, und wir ahnten, daß es kommen muß! - Und Wilheim von Humboidt, der Bruder Alexanders, der große Sprachforscher, der letzte derjenigen Zeit, als in Europa die große Dichtung bekannt wurde, von der ich gestern gesprochen habe, die Bhagavad Gita, dieser große Geist, sprach ungefähr so, daß ei` sagte, er habe schon genug gelebt, nachdem in sein Leben hereingefallen ist die Bekanntschaft mit der Bhagavad Gita."
      ],
      [
        "So hat sich das 19.",
        "Jahrhundert in denjenigen Seelen, die am meisten suchend waren, vorbereitet, dasjenige objektiv und unbefangen zu empfangen, was über den ganzen Erdkr`eis hin der Menschheit an spirituellen Schätzen gegeben ist.",
        "So hat es sich vorbereitet, um nicht in Einseitigkeit zu verfallen."
      ],
      [
        "Ich wollte Ihnen nicht theoretische Auseinandersetzungen geben.",
        "Ich halte theoretische Auseinandersetzungen immer für sehr einseitig, selbst wenn sie die allerbesten sind.",
        "An Beispielen wollte ich Ihnen zeigen, wie die Tatsachen sind, und wie die Seelen unter der Gewalt realer Tatsachen empfinden.",
        "Ich möchte zurückkommen auf etwas, was Herman Grimm vorgeschwebt hat, wovon er mir sprach auf einem Wege von Weimar nach Tiefurt, was in seiner Seele lebte"
      ],
      [
        "wie ein Gebäude, das er aufführen wollte, und wovon er selber in den einleitenden Bemerkungen zu seinen nachgelassenen Fragmenten so spricht, daß es ihm immer vor der Seele geschwebt hat, und daß alle seine einzelnen Arbeiten aus dem herausgeströmt sind, was so in seiner Seele lebte.",
        "Was war es, das ihm immer vorschwebte?"
      ],
      [
        "Es war nichts geringeres als eine Entwickelungsgeschichte der Menschheit, die er darstellen wollte als eine Geschichte der Entwickelung der nationalen Phantasie der Menschheit aller Völker und Zeiten.",
        "Das war ihm das zu Schaffende."
      ],
      [
        "Er wollte untersuchen, wie zum Beispiel in Griechenland die schöpferische Macht der Phantasie gewirkt hat, wie sie einen Horn er, einen Ä`schylos, einen Sophokles an seine Stelle hingestellt hat, wie sie durch die Zeiten gegangen ist bis in die neue Zeit herauf und überall hingestellt hat, was dargestellt werden soll.",
        "Ein Mann schritt neben mir her, der den Glauben an die Wahrheit der Phantasie, das Schöpferische der Phantasie hatte, aber eine Welt war rings herum, die keine Anlage hatte, an dieses Schöpferische der Phantasie, an die Abstammung der Phantasie von dem Wahrheitvater zu glauben!"
      ],
      [
        "Die Empfindung, welche Sie jetzt in dem dritten Mysterienspiel «Der Hüter der Schwelle» wiederfinden, wo Frau Balde wie ein Gespenst in den himmlischen Reichen erscheint - aber wie ein umgekehrtes Gespenst, denn sonst kommen Gespenster aus der übersinnlichen Welt, Frau Balde aber blickt hinauf und erscheint dort ebenso, wie die übersinnlichen Wesen herunterschreiten auf die Erde - diese Empfindung drängte sich damals in meine Seele und gestaltete sich als das Schicksal der Phantasie.",
        "An dieses Schicksal der Phantasie wird man denken müssen, wenn man auf das eingehen will, was Herman Grimm vorschwebte, ohne daß man etwas weiß über die Abstammung der Phantasie von dem Wahrheitvater."
      ],
      [
        "Niemals ist das zustande gekommen, was Herman Grimm vorgeschwebt hat.",
        "Er fühlte dunkel, daß da etwas zustande kommen würde, wenn es ihm gelänge, was er wollte.",
        "Aber - es ging nicht.",
        "Warum ging es nicht?",
        "Es ging deshalb nicht, weil einem die Phantasie, wenn man sie nur im allgemein-menschlichen Sinne als schöpferische Weltenmacht betrachten will, fortwährend entschlüpft."
      ],
      [
        "Man empfindet immer, wie die Macht, die man Phantasie"
      ],
      [
        "nennt, zwar von der Wahrheit abstammt, aber nicht selbst zur Wahrheit, sondern nur zur Maja hinführen kann, und wie hinter allem, wohin die Phantasie führt, die spirituelle Welt steht, der gegenüber Herman Grimm jene abwehrende Handbewegung machte."
      ],
      [
        "In den letzten Tagen trat diese Empfindung mir wieder vor die Seele gegenüber dem Manne, der aus der Phantasie heraus den Gang der Menschheitsentwickelung schildern wollte, daß ich mir sagte: Er hat das Ideal gehabt, aus dem Geistesleben, aus den spirituellen Mitteln, die ihm seine Zeit gab, Befriedigendes über die Weltenrätsel zu finden.",
        "Aber was er aus seiner Zeit heraus erlangen, was er in ehrlicher, auf- richtiger Weise in seine Seele aufnehmen konnte, das gab ihm die Lösung nicht."
      ],
      [
        "Und weil er ehrlich war, unterließ er sie!",
        "Daraus ersehen wir, wie unsere Zeit nach dem verlangt, was die Weltenrätsel enthüllen kann, was Aufklärung über die schaffenden Kräfte und schaffenden Mächte geben kann, die hinter den sinnlichen Erscheinungen stehen und die Signatur der Sinneserscheinungen bewirken."
      ],
      [
        "Warum trat mir das in der letzten Zeit vor die Seele?",
        "Ich habe mich nie gescheut, auch das Persönliche, wenn das Persönliche objektiv ist, zu erwähnen, und jeder mag darüber denken, wie er will.",
        "Ich bestrebe mich, das Persönliche ganz objektiv zu betrachten."
      ],
      [
        "Es trat mir vor die Seele, weil es sich mir ganz von selbst verglich, was ein Geist wollte und nicht konnte, und was nun in einer gewiß schönen Weise zustande gekommen ist durch das Buch unseres verehrten Edouard Schur6 «L`Evolution divine».",
        "Lesen Sie es und nehmen Sie sich vor, es so zu lesen, daß Sie in die spirituelle Macht eindringen, die hinter allem Sinnenschein steht, die aber auch in dem Gang der Epochen als die schöpferische Phantasie gewirkt hat."
      ],
      [
        "Und Sie werden sehen, wie unsere Zeit auf das zu antworten beginnt, was heiße, sehnsüchtige, manchmal nicht einmal vollbewußte Fragen unseres Geisteslebens waren.",
        "Dann werden Sie in Ihrer Seele die Antwort finden, was Geisteswissenschaft sein soll, aber auch die Antwort, wie Geisteswissenschaft sein soll."
      ],
      [
        "Wie wir denken müssen, damit ein harmonisches Zusammenwirken im Geistesleben der Gegenwart sich einstellen könnte, das war mir ein Bedürfnis im Verlaufe des heutigen Vormittages Ihnen zu sagen."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Der Vortragszyklus schloß sich an die Münchner Festaufführungen des Sommers 1912 an. Begonnen hatten diese Festspiele 1907 am 19. Mai mit der Uraufführung des von Edouard Schuré rekonstruierten «Heiligen Drama von Eleusis». 1909 folgte am 22. August die Uraufführung von dessen Drama «Die Kinder des Luzifer», und 1910 wurde am 15. August das erste Mysteriendrama Rudolf Steiners «Die Pforte der Einweihung» uraufgeführt. In den folgenden Jahren schlossen sich die Uraufführungen der drei anderen seiner Mysteriendramen an: 1911, 17. August «Die Prüfung der Seele»; eingeleitet am 13. August mit der Wiederholung des «Heiligen Drama von Eleusis»; 1912, 24. August «Der Hüter der Schwelle»; 1913, 22. August «Der Seelen Erwachen»; siehe «Vier Mysteriendramen», GA Bibl.-Nr. 14.",
      "Anläßlich der Festspiele hielt Rudolf Steiner folgende Vorträge:1907 2 Vorträge, in «Bilder okkulter Siegel und Säulen. Der Münchner Kongreß Pfingsten 1907 und seine Auswirkungen«, GA Bibl.-Nr. 284, sowie den Zyklus «Die Theosophie des Rosenkreuzers», GA Bibl.Nr. 99. 1909: «Der Orient im Lichte des Okzidents. Die Kinder des Luzifer und die Brüder Christi», GA Bibl.-Nr. 113. 1910: «Die Geheimnisse der biblischen Schöpfungsgeschichte», GA Bibl.-Nr. 122. 1912: «Von der 1nitiation. Von Ewigkeit und Augenblick, von Geisteslicht und Lebensdunkel», GA Bibl.-Nr. 138. 1913: «Die Geheimnisse der Schwelle», GA Bibl.-Nr. 147. 1914 kam es durch den Ausbruch des ersten Weltkrieges nicht mehr zu den bereits angekündigten Aufführungen und Vorträgen; auch nicht mehr zur Niederschrift des geplanten fünften Mysteriendramas.",
      "Textunterlagen: Alle Vorträge dieses Bandes wurden von Walter Vegelahn aus Berlin mitstenographiert. Dem Druck liegt die von ihm vorgenommene Übertragung in Klartext zugrunde. Sein Originalstenogramm liegt nicht vor.",
      "Der Titel des Vortragszyklus wurde von Rudolf Steiner gegeben.",
      "Zu den Ausdrücken «T6eosophie» und «theosopbisch»: Da Rudolf Steiner zur Zeit dieser Vor- träge noch innerhalb der Theosophischen Gesellschaft wirkte, bediente er sich der Ausdrücke «Theosophie» und «theosophisch», aber immer schon im Sinne seiner anthroposophisch orientierten Geisteswissenschaft. Aufgrund einer später von ihm gemachten Angabe wurden in den Ausgaben von 1930 und 1959 die Ausdrücke «Theosophie» und «theosophisch» in «Anthroposophie» und «anthroposophisch» geändert. Für die vorliegende Ausgabe wurden aus historischen Gründen wieder die ursprünglich gesprochenen Ausdrücke eingesetzt.",
      "Werke RudolfSteine`s innerhalb der Gesamtausgabe (GA) werden in den Hinweisen mit der Bibliographie-Nummer angegeben. Siehe auch die Übersicht am Schluß des Bandes.",
      "11    Rekonstruktion des Mysteriums von Eö~leusis: Von Edouard Schure` in «Sanctuaire d`Orient», Paris 1898, autorisierte Ubersetzung («Die Heiligtümer des Orients», Leipzig 1911) von Marie von Sivers und in freie Rhythmen gebracht durch Rudolf Steiner. Einzelausgabe «Das Heilige Drama von Eleusis» durch Marie Steiner-von Sivers, Dornach 1939.",
      "11    li>ir begannen - vor einem recht kleinen Kreis: Siehe «Aus dem Leben von Marie Steiner- von Sivers», biographische Beiträge, zusammengestellt von Hella Wiesberger, Dornach 1956.",
      "12    Herman Grimm, Kassel 1828 - 1901 Berlin. Siehe Rudolf Steiner «Mein Lebensgang», GA Bibl.-Nr. 28. Auch im Vortragswerk wird immer wieder auf Grimm hingewiesen.",
      "20    was heute nicht hierhergehört: Bezieht sich auf die Schwierigkeiten, die sich damals zwischen der Zentralleitung der Theosophischen Gesellschaft in Adyar und Rudolf Steiner ergeben hatten und die bald darauf zur Gründung der unabhängigen Anthroposophischen Gesellschaft führten. Diese Gründung wurde in der Versammlung während dieser Festwochen am 26. August 1912 beschlossen.",
      "21    «Kalender»: Siehe «Der anthroposophische Seelenkalender und der Kalender 1912/13», «Beiträge zur Rudolf Steiner Gesamtausgabe», Heft Nr. 37/38, Frühjahr-Sommer 1972.",
      "22    Freiin Imme von Eckardtstein, Lune`ville 1871 - 1930 Dornach. 1. von Eckardtstein schuf auch für die Dornacher Inszenierung unter Leitung von Marie Steiner alle Kostüme für die vier Mysterien&amen Rudolf Steiners.",
      "Maler Vol:kert, Linde, Haßund... Steglich: Von dem Maler Volckert konnten keine näheren Angaben ermittelt werden. Hermann Linde (Lübeck 1863 - 1923 Arlesheim) wurde 1904 Mitglied der Deutschen Sektion der Theosophischen Gesellschaft, kam 1913 zur Grundsteinlegung des ersten Goetheanums nach Dornach und war mit anderen Malern bei der Ausmalung der großen Kuppel tätig. Fritz Haß (geb. 1864) aus München malte ein Porträt von Rudolf Steiner, zu dem er ihm einige Male gesessen hat. Es wurde 1912 in die Ausstellung der Sommer-Sezession in München aufgenommen. Der Maler William Steglich (1866 - 1918) war Däne und übernahm den Vorsitz des im Jahre 1910 begründeten Zweiges in Kopenhagen.",
      "23    Zwischen tage: Die Aufführungen fanden statt: Sonntag, 18., Eleusis; Dienstag, 20., Die Pforte der Einweihung; Donnerstag, 22., Die Prüfung der Seele; Sonnabend, 24., Der Hüter der Schwelle. - Die Vorträge von Carl Unger fanden am 19., 21. und 23. August statt; das Thema war: Auf dem Wege zur Geisteswissenschaft.",
      "Dr. Ing. Carl Unger, Bad Cannstatt bei Stuttgart 1878 - 1929 Nürnberg. In der damaligen Zeit einer der wirksamsten Vertreter der Anthroposophie Rudolf Steiners. Siehe Carl Unger, «Schriften« I und II, Stuttgart.",
      "A.    W Sel/in, Ludwigslust, Mecklenburg-Schwerin 1840 - 1933 München, Direktor der Hanseatischen Kolonisationsgesellschaft, Hamburg. Siehe «Erinnerungen aus dem Berufs- und Seelenleben eines alten Mannes», Konstanz 1920.",
      "27    Goethe... «Verweile doch> du bist so schön!»: Letzte Worte des sterbenden Faust. Siehe Goethes «Faust», 2. Teil.",
      "29    wir haben so oft mit Eh,fur:ht zurückgewiesen: Siehe z. B. «Das Prinzip der spirituellen Ökonomie im Zusammenhang mit Wiederverkörperungsfragen», GA Bibl.-Nr. 109.",
      "32    ätherischer Leib: Siehe z. B. die in der 1912 erschienenen Schrift «Ein Weg zur Selbsterkenntnis des Menschen» in acht Meditationen dargestellten einzelnen geisteswissenschaftlichen Grunderlebnisse (zweite Meditation), GA Bibl.-Nr. 16.",
      "62    Bekannt ist dir: Worte der Maria im 7. Bild von «Der Hüter der Schwelle».",
      "62/63 die christliche Überlieferung drückt diesen Tatbestand dadurch aus, dafl sie sagt: Siehe Jesaja 6, Vers 1-3.",
      "64 in einem kleinen Buche: Vgl. Hinweis zu Seite 32.",
      "70    im «Hüter der Schwelle»: 8. Bild.",
      "80  in dem Drama «Der Hüter der Schwelle»: 2. und 8. Bild.",
      "82    eine Welt, welche gewöhnlich die devachanische Welt genannt wird: In der theosophischen Terminologie verweisen die Bezeichnungen Devachan- oder Mentalwelt auf dasselbe, was Rudolf Steiner mit dem deutschen Ausdruck «Geisterland» bezeichnet, das in eine niedere und eine höhere Region gegliedert wird.",
      "die Welt der höheren Hierarchien, die wir kennengelernt haben: Siehe «Die Geheimwissenschaft im Umriß», CA Bibl.-Nr. 13, und die Vorträge «Geistige Hierarchien und ihre Widerspiegelung in der physischen Welt. Tierkreis, Planeten, Kosmos», GA Bibl.Nr. 110; «Die Evolution vom Gesichtspunkte des Wahrhaftigen», GA Bibl.-Nr. 132; «Die geistigen Wesenheiten in den Himmelskörpern und Naturreichen», GA Bibl.-Nr. 136.",
      "83 Man könnte auch sagen, es sei der niedere Mentalplan: Vgl. Hinweis zu Seite 82.",
      "84    die Welt der Hierarchien, die wir von anderen Gesichtspunkten aus öfters charakterisiert haben: Vgl. 2. Hinweis zu Seite 82.",
      "91    Bhagavad Gita: Siehe die beiden Vortragszyklen «Die Bhagavad Gita und die Paulusbriefe», GA Bibl.-Nr. 142; «Die okkulten Grundlagen der Bhagavad Gita», GA Bibl.Nr. 146.",
      "107    Ludwig Deinhar~ Deidesheim, Rheinpfalz 1847 - 1917 München, Ingenieur und Industrieller. «Das Mysterium des Menschen im Lichte der psychischen Forschung. Eine Einführung in den Okkultismus», Berlin 1910.",
      "111 Kann man also sagen: In «Der Hüter der Schwelle», 10. Bild.",
      "127    Leopold von Ranke, Riehe/Reg.bez. Merseburg 1795 - 1886 Berlin.",
      "128    des Johannes 1homasius Doppelgänger: In «Der Hüter der Schwelle», 3. Bild.",
      "130    Bodhisattva: TheosoPhisch-indische Rangbezeichnung für einen Menschheitslehrer, bevor er die Buddhaschaft erreicht hat.",
      "131    wir sehen den ....... von einem anderen Planeten: Siehe Vortrag Helsingfors 13. April 1912 in «Die geistigen Wesenheiten in den Himmelskörpern und Naturreichen», GA Bibl.-Nr. 136, in dem der Zusammenhang des Buddha mit dem Planeten Merkur dargestellt ist.",
      "Wir sehen ihn (Buddha) hinauftteigen zum Mars: Von Rudolf Steiner öfters dargestellt, z. B. im Vortrag Kristiania 11. Juni 1912 in «Der Mensch im Lichte von Okkultismus, Theosophie und Philosophie», GA Bibl.-Nr. 137; Neucha`tel, 18. Dezember 1912 in «Das esoterische Christentum», GA Bibl.-Nr. 130; Berlin 22. Dezember 1912 in «Das Leben zwischen dem Tode und der neuen Geburt im Verhältnis zu den kosmischen Tatsachen», GA Bibl.-Nr. 141.",
      "132    wer meinefeüheren Vortrfge gehört hat: Siehe z. B. «Das Lukas-Evangelium», GA BibI.Nr. 114.",
      "136    Ich habe es öfter gesagt... Meister der Weisheit und des Zusamrnenklanges der Empfindun. gen: Näheres siehe in «Zur Geschichte und aus den Inhalten der ersten Abteilung der Esoterischen Schule 1904 bis 1914», GA Bibl.-Nr. 264.",
      "137    Wie aber die Dinge gehen mögen: Vgl. Hinweis zu Seite 20. Siehe die Darstellung der Vorgänge in den «Mitteilungen für die Mitglieder der Deutschen Sektion der Theosophischen Gesellschaft», herausgegeben von Mathilde Scholl.",
      "138    Einladung für den nächsten KongreflderEuropäischen Sektionen der 1heoscphischen Gesellschaft: An diesem Kongreß wurde nicht mehr teilgenommen, denn mit Schreiben vom 7. März 1913 aus Adyar schloß Annie Besant als Präsidentin der Theosophischen Gesellschaft die Deutsche Sektion aus der Theosophischen Gesellschaft aus.",
      "ist der Gruflschon an dem ersten Vortrag da,gebraoht worden: Ist in der Nachschrift nicht festgehalten worden.",
      "Zum Sondervortrag",
      "140    Der Vortrag war ursprünglich nicht vorgesehen - vielleicht haben die schon im Hinweis zu Seite 20 angetönten Auseinandersetzungen mit der Zentralleitung der Theosophischen Gesellschaft dazu Veranlassung gegeben - und wurde deshalb nicht chronologisch eingereiht, sondern an den Schluß gesetzt.",
      "141    die spirituellen Leiter unserer Bewegung: Siehe Hinweis zu Seite 136.",
      "143    Walther Rathenau, Berlin 1867 - 1922 Berlin, wurde ermordet, Staatsmann und Wirtschaftspolitiker. «Zur Kritik der Zeit», S. Fischer-Verlag, Berlin.",
      "146    Herman Grimms... Biographie Michelangelos: «Leben Michelangelos», 2 Bände, Hannover 1860-63.",
      "Er hat dann auch begonnen, ein Leben Raffaels zu schreiben: «Das Leben Raphaels von Urbuni, von Vasari. Übersetzt und kommentiert von Herman Grimm», Berlin 1872; 2. Auflage unter dem Titel «Das Leben Raphaels», Berlin 1886. Sein Werk «Raphael als Weltmacht» erschien 1886.",
      "Ein kurzes Fragment: In «Fragmente». Zweiter und letzter Teil, Berlin und Stuttgart 1902.",
      "147    vier Bilder: Die genannten vier Bilder waren im «Hüter der Schwelle» (1. Bild: Vorsaal zu den Räumen des Mystenbundes) angebracht. Für die Inszenierung des Dramas auf der Goetheanum-Bühne in Dornach wurden sie von William Scott-Pyle (1888 - 1938) ausgeführt. Wiedergegeben in der Bildbeilage zu Heft Nr. 43/44 (Weihnachten 1973) der «Beiträge zur Rudolf Steiner Gesamtausgabe». Siehe auch die Vorträge Rudolf Steiners Köln, 8. Mai 1912 und München, 16. Mai 1912 in «Erfahrungen des Übersinnlichen. Die Wege der Seele zu Christus», GA Bibl.-Nr. 143.",
      "148    Konrad Burdacb, Königsberg 1859 - 1936 Berlin, Mitglied der Preußischen Akademie der Wissenschaften in Berlin, Hauptvertreter der geistesgeschichtlichen Methode in Sprach- und Literaturforschung. Von 1887 - 1902 Professor in Halle. Seine Studie «Faust und Moses» erschien in «Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften». Erster Teil: 2. Mai 1912; zweiter Teil: 11. Juli 1912.",
      "149    zu Eckermann: Sonntag, den 6. Dezember 1829. Siehe hierzu Herman Grimm «Raphael als Weltmacht», Hinweis zu S. 146.",
      "150    «Gottes ist der Crient . . .»: Goethe im «West-östlichen Divan» (Buch des Sängers. - Talismane).",
      "zu einem Kapitel des «Wilhelm Meister»: Siehe «Wilhelm Meisters Wanderjahre» (Zweites Buch, zweites Kapitel). Die angeführten Worte sind von Rudolf Steiner frei wiedergegeben.",
      "153    Ale:cander von Humboldt, Berlin 1769 - 1859 Berlin, Naturforscher. Siehe «Kosmos. Entwurf einer physischen Weltbeschreibung», Stuttgart und Tübingen 1847 (2. Band S. 44-49).",
      "154    Wilhelm von Humboldt, Potsdam i767 - 1835 Tegel bei Berlin, Gelehrter und Staatsmann. Siehe hierzu seinen Brief an August Wilhelm Schlegel vom 21. Juni 1823 (wiedergegeben in «Wilhelm von Humboldt im Verkehr mit seinen Freunden», Berlin o.J.).",
      "155    in den einleitenden Bemerkungen: Herman Grimm, Fragmente: Erster Band, Berlin und Stuttgart, Verlag W. Spemann, 1900: «Von den Anfängen eigener schriftstellerischer Betätigung ab ging mein Sinn dahin, meinen Grundgedanken nachgehend die Geschichte der europäischen Volksentwicklung zu schreiben. ... Es war meine Absicht, die in der Berliner Universität im Laufe von fünfzig Semestern gehaltenen Vorlesungen zu- nächst zu einem Buche zu gestalten, das die Geschichte des geistigen Wachstums der Deutschen enthielte, aber es wird mir zweifelhaft, daß ich dazu kommen werde.» Berlin, September 1899.",
      "Frau Balde: Das «Märchen von der Phantasie» erzählt sie im 6. Bild von «Der Hüter der Schwelle».",
      "156    Edouard Schur6 «L>Evolution divine»: «L`Evolution divine du Sphinz au Christ» war im Februar 1912 mit einer Vorrede von Rudolf Steiner erschienen. Die Deutsche Übersetzung «Die göttliche Entwicklung von der Sphinz bis zum Christus» durch J. Hardt erschien Leipzig 1922."
    ],
    "sentences": [
      [
        "Der Vortragszyklus schloß sich an die Münchner Festaufführungen des Sommers 1912 an.",
        "Begonnen hatten diese Festspiele 1907 am 19.",
        "Mai mit der Uraufführung des von Edouard Schuré rekonstruierten «Heiligen Drama von Eleusis». 1909 folgte am 22.",
        "August die Uraufführung von dessen Drama «Die Kinder des Luzifer», und 1910 wurde am 15.",
        "August das erste Mysteriendrama Rudolf Steiners «Die Pforte der Einweihung» uraufgeführt.",
        "In den folgenden Jahren schlossen sich die Uraufführungen der drei anderen seiner Mysteriendramen an: 1911, 17.",
        "August «Die Prüfung der Seele»; eingeleitet am 13.",
        "August mit der Wiederholung des «Heiligen Drama von Eleusis»; 1912, 24.",
        "August «Der Hüter der Schwelle»; 1913, 22.",
        "August «Der Seelen Erwachen»; siehe «Vier Mysteriendramen», GA Bibl.-Nr. 14."
      ],
      [
        "Anläßlich der Festspiele hielt Rudolf Steiner folgende Vorträge:1907 2 Vorträge, in «Bilder okkulter Siegel und Säulen.",
        "Der Münchner Kongreß Pfingsten 1907 und seine Auswirkungen«, GA Bibl.-Nr. 284, sowie den Zyklus «Die Theosophie des Rosenkreuzers», GA Bibl.Nr. 99. 1909: «Der Orient im Lichte des Okzidents.",
        "Die Kinder des Luzifer und die Brüder Christi», GA Bibl.-Nr. 113. 1910: «Die Geheimnisse der biblischen Schöpfungsgeschichte», GA Bibl.-Nr. 122. 1912: «Von der 1nitiation.",
        "Von Ewigkeit und Augenblick, von Geisteslicht und Lebensdunkel», GA Bibl.-Nr. 138. 1913: «Die Geheimnisse der Schwelle», GA Bibl.-Nr. 147. 1914 kam es durch den Ausbruch des ersten Weltkrieges nicht mehr zu den bereits angekündigten Aufführungen und Vorträgen; auch nicht mehr zur Niederschrift des geplanten fünften Mysteriendramas."
      ],
      [
        "Textunterlagen: Alle Vorträge dieses Bandes wurden von Walter Vegelahn aus Berlin mitstenographiert.",
        "Dem Druck liegt die von ihm vorgenommene Übertragung in Klartext zugrunde.",
        "Sein Originalstenogramm liegt nicht vor."
      ],
      [
        "Der Titel des Vortragszyklus wurde von Rudolf Steiner gegeben."
      ],
      [
        "Zu den Ausdrücken «T6eosophie» und «theosopbisch»: Da Rudolf Steiner zur Zeit dieser Vor- träge noch innerhalb der Theosophischen Gesellschaft wirkte, bediente er sich der Ausdrücke «Theosophie» und «theosophisch», aber immer schon im Sinne seiner anthroposophisch orientierten Geisteswissenschaft.",
        "Aufgrund einer später von ihm gemachten Angabe wurden in den Ausgaben von 1930 und 1959 die Ausdrücke «Theosophie» und «theosophisch» in «Anthroposophie» und «anthroposophisch» geändert.",
        "Für die vorliegende Ausgabe wurden aus historischen Gründen wieder die ursprünglich gesprochenen Ausdrücke eingesetzt."
      ],
      [
        "Werke RudolfSteine`s innerhalb der Gesamtausgabe (GA) werden in den Hinweisen mit der Bibliographie-Nummer angegeben.",
        "Siehe auch die Übersicht am Schluß des Bandes."
      ],
      [
        "11 Rekonstruktion des Mysteriums von Eö~leusis: Von Edouard Schure` in «Sanctuaire d`Orient», Paris 1898, autorisierte Ubersetzung («Die Heiligtümer des Orients», Leipzig 1911) von Marie von Sivers und in freie Rhythmen gebracht durch Rudolf Steiner.",
        "Einzelausgabe «Das Heilige Drama von Eleusis» durch Marie Steiner-von Sivers, Dornach 1939."
      ],
      [
        "11 li>ir begannen - vor einem recht kleinen Kreis: Siehe «Aus dem Leben von Marie Steiner- von Sivers», biographische Beiträge, zusammengestellt von Hella Wiesberger, Dornach 1956."
      ],
      [
        "12 Herman Grimm, Kassel 1828 - 1901 Berlin.",
        "Siehe Rudolf Steiner «Mein Lebensgang», GA Bibl.-Nr. 28.",
        "Auch im Vortragswerk wird immer wieder auf Grimm hingewiesen."
      ],
      [
        "20 was heute nicht hierhergehört: Bezieht sich auf die Schwierigkeiten, die sich damals zwischen der Zentralleitung der Theosophischen Gesellschaft in Adyar und Rudolf Steiner ergeben hatten und die bald darauf zur Gründung der unabhängigen Anthroposophischen Gesellschaft führten.",
        "Diese Gründung wurde in der Versammlung während dieser Festwochen am 26.",
        "August 1912 beschlossen."
      ],
      [
        "21 «Kalender»: Siehe «Der anthroposophische Seelenkalender und der Kalender 1912/13», «Beiträge zur Rudolf Steiner Gesamtausgabe», Heft Nr. 37/38, Frühjahr-Sommer 1972."
      ],
      [
        "22 Freiin Imme von Eckardtstein, Lune`ville 1871 - 1930 Dornach. 1. von Eckardtstein schuf auch für die Dornacher Inszenierung unter Leitung von Marie Steiner alle Kostüme für die vier Mysterien&amen Rudolf Steiners."
      ],
      [
        "Maler Vol:kert, Linde, Haßund...",
        "Steglich: Von dem Maler Volckert konnten keine näheren Angaben ermittelt werden.",
        "Hermann Linde (Lübeck 1863 - 1923 Arlesheim) wurde 1904 Mitglied der Deutschen Sektion der Theosophischen Gesellschaft, kam 1913 zur Grundsteinlegung des ersten Goetheanums nach Dornach und war mit anderen Malern bei der Ausmalung der großen Kuppel tätig.",
        "Fritz Haß (geb. 1864) aus München malte ein Porträt von Rudolf Steiner, zu dem er ihm einige Male gesessen hat.",
        "Es wurde 1912 in die Ausstellung der Sommer-Sezession in München aufgenommen.",
        "Der Maler William Steglich (1866 - 1918) war Däne und übernahm den Vorsitz des im Jahre 1910 begründeten Zweiges in Kopenhagen."
      ],
      [
        "23 Zwischen tage: Die Aufführungen fanden statt: Sonntag, 18., Eleusis; Dienstag, 20., Die Pforte der Einweihung; Donnerstag, 22., Die Prüfung der Seele; Sonnabend, 24., Der Hüter der Schwelle. - Die Vorträge von Carl Unger fanden am 19., 21. und 23.",
        "August statt; das Thema war: Auf dem Wege zur Geisteswissenschaft."
      ],
      [
        "Ing.",
        "Carl Unger, Bad Cannstatt bei Stuttgart 1878 - 1929 Nürnberg.",
        "In der damaligen Zeit einer der wirksamsten Vertreter der Anthroposophie Rudolf Steiners.",
        "Siehe Carl Unger, «Schriften« I und II, Stuttgart."
      ],
      [
        "W Sel/in, Ludwigslust, Mecklenburg-Schwerin 1840 - 1933 München, Direktor der Hanseatischen Kolonisationsgesellschaft, Hamburg.",
        "Siehe «Erinnerungen aus dem Berufs- und Seelenleben eines alten Mannes», Konstanz 1920."
      ],
      [
        "27 Goethe...",
        "«Verweile doch> du bist so schön!»: Letzte Worte des sterbenden Faust.",
        "Siehe Goethes «Faust», 2.",
        "Teil."
      ],
      [
        "29 wir haben so oft mit Eh,fur:ht zurückgewiesen: Siehe z.",
        "«Das Prinzip der spirituellen Ökonomie im Zusammenhang mit Wiederverkörperungsfragen», GA Bibl.-Nr. 109."
      ],
      [
        "32 ätherischer Leib: Siehe z.",
        "B. die in der 1912 erschienenen Schrift «Ein Weg zur Selbsterkenntnis des Menschen» in acht Meditationen dargestellten einzelnen geisteswissenschaftlichen Grunderlebnisse (zweite Meditation), GA Bibl.-Nr. 16."
      ],
      [
        "62 Bekannt ist dir: Worte der Maria im 7.",
        "Bild von «Der Hüter der Schwelle»."
      ],
      [
        "62/63 die christliche Überlieferung drückt diesen Tatbestand dadurch aus, dafl sie sagt: Siehe Jesaja 6, Vers 1-3."
      ],
      [
        "64 in einem kleinen Buche: Vgl.",
        "Hinweis zu Seite 32."
      ],
      [
        "70 im «Hüter der Schwelle»: 8.",
        "Bild."
      ],
      [
        "80 in dem Drama «Der Hüter der Schwelle»: 2. und 8.",
        "Bild."
      ],
      [
        "82 eine Welt, welche gewöhnlich die devachanische Welt genannt wird: In der theosophischen Terminologie verweisen die Bezeichnungen Devachan- oder Mentalwelt auf dasselbe, was Rudolf Steiner mit dem deutschen Ausdruck «Geisterland» bezeichnet, das in eine niedere und eine höhere Region gegliedert wird."
      ],
      [
        "die Welt der höheren Hierarchien, die wir kennengelernt haben: Siehe «Die Geheimwissenschaft im Umriß», CA Bibl.-Nr. 13, und die Vorträge «Geistige Hierarchien und ihre Widerspiegelung in der physischen Welt.",
        "Tierkreis, Planeten, Kosmos», GA Bibl.Nr. 110; «Die Evolution vom Gesichtspunkte des Wahrhaftigen», GA Bibl.-Nr. 132; «Die geistigen Wesenheiten in den Himmelskörpern und Naturreichen», GA Bibl.-Nr. 136."
      ],
      [
        "83 Man könnte auch sagen, es sei der niedere Mentalplan: Vgl.",
        "Hinweis zu Seite 82."
      ],
      [
        "84 die Welt der Hierarchien, die wir von anderen Gesichtspunkten aus öfters charakterisiert haben: Vgl. 2.",
        "Hinweis zu Seite 82."
      ],
      [
        "91 Bhagavad Gita: Siehe die beiden Vortragszyklen «Die Bhagavad Gita und die Paulusbriefe», GA Bibl.-Nr. 142; «Die okkulten Grundlagen der Bhagavad Gita», GA Bibl.Nr. 146."
      ],
      [
        "107 Ludwig Deinhar~ Deidesheim, Rheinpfalz 1847 - 1917 München, Ingenieur und Industrieller.",
        "«Das Mysterium des Menschen im Lichte der psychischen Forschung.",
        "Eine Einführung in den Okkultismus», Berlin 1910."
      ],
      [
        "111 Kann man also sagen: In «Der Hüter der Schwelle», 10.",
        "Bild."
      ],
      [
        "127 Leopold von Ranke, Riehe/Reg.bez.",
        "Merseburg 1795 - 1886 Berlin."
      ],
      [
        "128 des Johannes 1homasius Doppelgänger: In «Der Hüter der Schwelle», 3.",
        "Bild."
      ],
      [
        "130 Bodhisattva: TheosoPhisch-indische Rangbezeichnung für einen Menschheitslehrer, bevor er die Buddhaschaft erreicht hat."
      ],
      [
        "131 wir sehen den ....... von einem anderen Planeten: Siehe Vortrag Helsingfors 13.",
        "April 1912 in «Die geistigen Wesenheiten in den Himmelskörpern und Naturreichen», GA Bibl.-Nr. 136, in dem der Zusammenhang des Buddha mit dem Planeten Merkur dargestellt ist."
      ],
      [
        "Wir sehen ihn (Buddha) hinauftteigen zum Mars: Von Rudolf Steiner öfters dargestellt, z.",
        "B. im Vortrag Kristiania 11.",
        "Juni 1912 in «Der Mensch im Lichte von Okkultismus, Theosophie und Philosophie», GA Bibl.-Nr. 137; Neucha`tel, 18.",
        "Dezember 1912 in «Das esoterische Christentum», GA Bibl.-Nr. 130; Berlin 22.",
        "Dezember 1912 in «Das Leben zwischen dem Tode und der neuen Geburt im Verhältnis zu den kosmischen Tatsachen», GA Bibl.-Nr. 141."
      ],
      [
        "132 wer meinefeüheren Vortrfge gehört hat: Siehe z.",
        "«Das Lukas-Evangelium», GA BibI.Nr. 114."
      ],
      [
        "136 Ich habe es öfter gesagt...",
        "Meister der Weisheit und des Zusamrnenklanges der Empfindun. gen: Näheres siehe in «Zur Geschichte und aus den Inhalten der ersten Abteilung der Esoterischen Schule 1904 bis 1914», GA Bibl.-Nr. 264."
      ],
      [
        "137 Wie aber die Dinge gehen mögen: Vgl.",
        "Hinweis zu Seite 20.",
        "Siehe die Darstellung der Vorgänge in den «Mitteilungen für die Mitglieder der Deutschen Sektion der Theosophischen Gesellschaft», herausgegeben von Mathilde Scholl."
      ],
      [
        "138 Einladung für den nächsten KongreflderEuropäischen Sektionen der 1heoscphischen Gesellschaft: An diesem Kongreß wurde nicht mehr teilgenommen, denn mit Schreiben vom 7.",
        "März 1913 aus Adyar schloß Annie Besant als Präsidentin der Theosophischen Gesellschaft die Deutsche Sektion aus der Theosophischen Gesellschaft aus."
      ],
      [
        "ist der Gruflschon an dem ersten Vortrag da,gebraoht worden: Ist in der Nachschrift nicht festgehalten worden."
      ],
      [
        "Zum Sondervortrag"
      ],
      [
        "140 Der Vortrag war ursprünglich nicht vorgesehen - vielleicht haben die schon im Hinweis zu Seite 20 angetönten Auseinandersetzungen mit der Zentralleitung der Theosophischen Gesellschaft dazu Veranlassung gegeben - und wurde deshalb nicht chronologisch eingereiht, sondern an den Schluß gesetzt."
      ],
      [
        "141 die spirituellen Leiter unserer Bewegung: Siehe Hinweis zu Seite 136."
      ],
      [
        "143 Walther Rathenau, Berlin 1867 - 1922 Berlin, wurde ermordet, Staatsmann und Wirtschaftspolitiker.",
        "«Zur Kritik der Zeit», S.",
        "Fischer-Verlag, Berlin."
      ],
      [
        "146 Herman Grimms...",
        "Biographie Michelangelos: «Leben Michelangelos», 2 Bände, Hannover 1860-63."
      ],
      [
        "Er hat dann auch begonnen, ein Leben Raffaels zu schreiben: «Das Leben Raphaels von Urbuni, von Vasari.",
        "Übersetzt und kommentiert von Herman Grimm», Berlin 1872; 2.",
        "Auflage unter dem Titel «Das Leben Raphaels», Berlin 1886.",
        "Sein Werk «Raphael als Weltmacht» erschien 1886."
      ],
      [
        "Ein kurzes Fragment: In «Fragmente».",
        "Zweiter und letzter Teil, Berlin und Stuttgart 1902."
      ],
      [
        "147 vier Bilder: Die genannten vier Bilder waren im «Hüter der Schwelle» (1.",
        "Bild: Vorsaal zu den Räumen des Mystenbundes) angebracht.",
        "Für die Inszenierung des Dramas auf der Goetheanum-Bühne in Dornach wurden sie von William Scott-Pyle (1888 - 1938) ausgeführt.",
        "Wiedergegeben in der Bildbeilage zu Heft Nr. 43/44 (Weihnachten 1973) der «Beiträge zur Rudolf Steiner Gesamtausgabe».",
        "Siehe auch die Vorträge Rudolf Steiners Köln, 8.",
        "Mai 1912 und München, 16.",
        "Mai 1912 in «Erfahrungen des Übersinnlichen.",
        "Die Wege der Seele zu Christus», GA Bibl.-Nr. 143."
      ],
      [
        "148 Konrad Burdacb, Königsberg 1859 - 1936 Berlin, Mitglied der Preußischen Akademie der Wissenschaften in Berlin, Hauptvertreter der geistesgeschichtlichen Methode in Sprach- und Literaturforschung.",
        "Von 1887 - 1902 Professor in Halle.",
        "Seine Studie «Faust und Moses» erschien in «Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften».",
        "Erster Teil: 2.",
        "Mai 1912; zweiter Teil: 11.",
        "Juli 1912."
      ],
      [
        "149 zu Eckermann: Sonntag, den 6.",
        "Dezember 1829.",
        "Siehe hierzu Herman Grimm «Raphael als Weltmacht», Hinweis zu S. 146."
      ],
      [
        "150 «Gottes ist der Crient . . .»: Goethe im «West-östlichen Divan» (Buch des Sängers. - Talismane)."
      ],
      [
        "zu einem Kapitel des «Wilhelm Meister»: Siehe «Wilhelm Meisters Wanderjahre» (Zweites Buch, zweites Kapitel).",
        "Die angeführten Worte sind von Rudolf Steiner frei wiedergegeben."
      ],
      [
        "153 Ale:cander von Humboldt, Berlin 1769 - 1859 Berlin, Naturforscher.",
        "Siehe «Kosmos.",
        "Entwurf einer physischen Weltbeschreibung», Stuttgart und Tübingen 1847 (2.",
        "Band S. 44-49)."
      ],
      [
        "154 Wilhelm von Humboldt, Potsdam i767 - 1835 Tegel bei Berlin, Gelehrter und Staatsmann.",
        "Siehe hierzu seinen Brief an August Wilhelm Schlegel vom 21.",
        "Juni 1823 (wiedergegeben in «Wilhelm von Humboldt im Verkehr mit seinen Freunden», Berlin o.J.)."
      ],
      [
        "155 in den einleitenden Bemerkungen: Herman Grimm, Fragmente: Erster Band, Berlin und Stuttgart, Verlag W.",
        "Spemann, 1900: «Von den Anfängen eigener schriftstellerischer Betätigung ab ging mein Sinn dahin, meinen Grundgedanken nachgehend die Geschichte der europäischen Volksentwicklung zu schreiben. ...",
        "Es war meine Absicht, die in der Berliner Universität im Laufe von fünfzig Semestern gehaltenen Vorlesungen zu- nächst zu einem Buche zu gestalten, das die Geschichte des geistigen Wachstums der Deutschen enthielte, aber es wird mir zweifelhaft, daß ich dazu kommen werde.» Berlin, September 1899."
      ],
      [
        "Frau Balde: Das «Märchen von der Phantasie» erzählt sie im 6.",
        "Bild von «Der Hüter der Schwelle»."
      ],
      [
        "156 Edouard Schur6 «L>Evolution divine»: «L`Evolution divine du Sphinz au Christ» war im Februar 1912 mit einer Vorrede von Rudolf Steiner erschienen.",
        "Die Deutsche Übersetzung «Die göttliche Entwicklung von der Sphinz bis zum Christus» durch J.",
        "Hardt erschien Leipzig 1922."
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "PERSONENREGISTER",
    "paragraphs": [
      "(H = Hinweis)",
      "Alkibiades (um 450 - 404 v. Chr.)    Linde, Hermann (1863-1923)",
      "14     22 H",
      "Äschylos (525 - 456 v. Chr.)    Lykurg (9. Jh. v. Chr.)",
      "14, 155     15",
      "Buddha, Gotama (560 - 480 v. Chr.)    Mahomet (570 - 632)",
      "40 H, 42, 126ff., 131 H, 132f.     126",
      "Burdach, Konrad (1859 - 1936)    Michelangelo Buonarroti (1475 - 1564)",
      "148 H, 149     146, 147",
      "Cäsar, Cajus Julius (100 - 44 v. Chr.)    Novalis (Friedrich von Hardenberg)",
      "13, 14, 15    (1772-1801)147",
      "Dante (1265 - 1321)    Raffael Santi (1483 - 1520)",
      "41, 89, 110     146ff.",
      "Deinhard, Ludwig (1847-1917)    Ranke, Leopold von (1795-1886)",
      "107 H, 108     127",
      "Rathenau, Walther (1867-1922)",
      "Eckardtstein, Freiin Imme von     143 H, 144",
      "(1871-1930)22H",
      "Eckermann, Johann Peter (1792 - 1854)    Schure, Edouard (1841 - 1929)",
      "149 H     11 H, 12, 19, 26, 156 H",
      "Sellin, A. W. (1840-1933)",
      "Goethe, Johann Wolfgang (1749-1832)     23 H, 24",
      "27 H, 40, 110, 149, 150 H, 152    Shakespeare, William (1564-1616)",
      "Grimm, Herman (1828-1901)     110",
      "12 H, 13, 145, 146 H, 154    Sophokles (496 v. Chr.)",
      "Haß, Fritz (geb. 1864)    Steglich, William (1866- 1918)",
      "22 H     22 H",
      "Homer (9. Jh. v. Chr.)",
      "14, 40, 110,155    Unger, Carl (1878-1929)",
      "Humboldt, Alexander von (1769- 1859)     23 H",
      "Humboldt, Wilhelm von (1767- 1835)    Volckert",
      "154 H     22 H",
      "Konfuzius (551 - 478 v. Chr.)    Zarathustra (6. Jh. v. Chr.)"
    ],
    "sentences": [
      [
        "(H = Hinweis)"
      ],
      [
        "Alkibiades (um 450 - 404 v.",
        "Chr.) Linde, Hermann (1863-1923)"
      ],
      [
        "14 22 H"
      ],
      [
        "Äschylos (525 - 456 v.",
        "Chr.) Lykurg (9.",
        "Jh. v.",
        "Chr.)"
      ],
      [
        "14, 155 15"
      ],
      [
        "Buddha, Gotama (560 - 480 v.",
        "Chr.) Mahomet (570 - 632)"
      ],
      [
        "40 H, 42, 126ff., 131 H, 132f. 126"
      ],
      [
        "Burdach, Konrad (1859 - 1936) Michelangelo Buonarroti (1475 - 1564)"
      ],
      [
        "148 H, 149 146, 147"
      ],
      [
        "Cäsar, Cajus Julius (100 - 44 v.",
        "Chr.) Novalis (Friedrich von Hardenberg)"
      ],
      [
        "13, 14, 15 (1772-1801)147"
      ],
      [
        "Dante (1265 - 1321) Raffael Santi (1483 - 1520)"
      ],
      [
        "41, 89, 110 146ff."
      ],
      [
        "Deinhard, Ludwig (1847-1917) Ranke, Leopold von (1795-1886)"
      ],
      [
        "107 H, 108 127"
      ],
      [
        "Rathenau, Walther (1867-1922)"
      ],
      [
        "Eckardtstein, Freiin Imme von 143 H, 144"
      ],
      [
        "(1871-1930)22H"
      ],
      [
        "Eckermann, Johann Peter (1792 - 1854) Schure, Edouard (1841 - 1929)"
      ],
      [
        "149 H 11 H, 12, 19, 26, 156 H"
      ],
      [
        "Sellin, A.",
        "W. (1840-1933)"
      ],
      [
        "Goethe, Johann Wolfgang (1749-1832) 23 H, 24"
      ],
      [
        "27 H, 40, 110, 149, 150 H, 152 Shakespeare, William (1564-1616)"
      ],
      [
        "Grimm, Herman (1828-1901) 110"
      ],
      [
        "12 H, 13, 145, 146 H, 154 Sophokles (496 v.",
        "Chr.)"
      ],
      [
        "Haß, Fritz (geb. 1864) Steglich, William (1866- 1918)"
      ],
      [
        "22 H 22 H"
      ],
      [
        "Homer (9.",
        "Jh. v.",
        "Chr.)"
      ],
      [
        "14, 40, 110,155 Unger, Carl (1878-1929)"
      ],
      [
        "Humboldt, Alexander von (1769- 1859) 23 H"
      ],
      [
        "Humboldt, Wilhelm von (1767- 1835) Volckert"
      ],
      [
        "154 H 22 H"
      ],
      [
        "Konfuzius (551 - 478 v.",
        "Chr.) Zarathustra (6.",
        "Jh. v.",
        "Chr.)"
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
