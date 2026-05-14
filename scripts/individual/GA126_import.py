#!/usr/bin/env python3
"""Standalone import script for GA126 — GA126 - Okkulte Geschichte"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA126 - Okkulte Geschichte"""
GA_NUMBER = "GA126"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "I",
    "paragraphs": [
      "In der Geisteswissenschaft verhält es sich so, dass die Wahrheiten, die Erkenntnisse um so schwieriger werden, je weitet man von all­gemeinen Verhältnissen heruntersteigt zu besonderen konkreten Ein­zelheiten. Es konnte von Ihnen dies schon bemerkt werden, als in verschiedenen Arbeitsgruppen versucht wurde, im einzelnen ge­schichtlich zu sprechen etwa über die Wiederverkörperungen des grossen Führers der Perserreligion, des Zarathustra - als gesprochen wurde über den Zusammenhang des Zarathustra mit Moses, mit Hermes und auch mit dem Jesus von Nazareth. Auch bei anderen Gelegenheiten sind ja konkrete geschichtliche Fragen bereits berührt worden. Man steigt von Dingen, über welche das menschliche Herz noch dies oder jenes Unwahrscheinliche verhältnismässig leicht hin­nimmt, in Gebiete hinab voll von Unwahrscheinlichkeiten, sobald man heruntersteigt von den grossen Wahrheiten über das geistig Durchtränkt- und Durchwobensein der Welt, von den grossen Welt-gesetzen zur geistigen Natur einer einzelnen Individualität, einer einzelnen Persönlichkeit. Und bei noch nicht genügend vorbereiteten Menschen beginnt in der Regel an diesem Abgrund zwischen den allgemeinen und besonderen Wahrheiten die Ungläubigkeit.",
      "Nun werde ich Ihnen in den Vorträgen, zu denen die heutige Be­trachtung eine Art von Einleitung geben soll, die der okkulten Geschichte angehören und von historischen Tatsachen und geschicht­lichen Persönlichkeiten im Lichte der Geisteswissenschaft handeln, manches Sonderbare zu sagen haben. Sie werden manches Sonderbare hören, das auf Ihren guten Willen wird rechnen müssen, auf jenen guten Willen, der herangeschult ist durch alles dasjenige, was im Laufe von Jahren an geisteswissenschaftlichen Erkenntnissen durch",
      "Ihre Seele gezogen ist. Denn das ist ja die schönste, die bedeutsamste Frucht, die wir gewinnen aus der spirituellen Weltanschauung, dass, so kompliziert, so im einzelnen ausgebaut auch die Erkenntnisse sind, die wir gewinnen, wir zuletzt doch nicht vor uns haben bloss eine Summe von Dogmen, sondern dass wir in uns, in unseren Herzen, in unseren Gemütern durch diese geisteswissenschaftliche Betrach­tungsweise etwas besitzen, was uns hinausrückt über den Standpunkt, den wir sonst durch irgendeine andere Weltbetrachtung gewinnen können.",
      "Nicht Dogmen, nicht Lehrsätze, nicht ein blosses Wissen nehmen wir auf, sondern durch unsere Erkenntnisse werden wir andere Menschen. In gewisser Beziehung gehört zu solchen Partien geistiger Wissenschaft wie diejenigen, die wir jetzt betrachten werden, Seelenverständnis, nicht intellektuelles Verständnis - Seelenverständ­nis, das vielleicht an gar manchen Stellen auch geneigt sein muss, Andeutungen anzuhören und hinzunehmen, die grob, die brutal werden würden, wenn man sie in allzu scharfe Konturen hinein­pressen wollte.",
      "Wovon ich Ihnen gerne Vorstellungen hervorrufen möchte, das ist, dass in dem ganzen auch geschichtlichen Werde-prozess der Menschlieit durch die verschiedenen Jahrtausende hin­durch bis in unsere Tage hinein hinter allem Menschenwerden und menschlichen Geschehen geistige Wesenheiten, geistige Individuali-täten als Leiter, als Führer stehen, und dass für die grössten, für die wichtigsten Tatsachen des historischen Verlaufes dieser oder jener Mensch mit seiner ganzen Seele, mit seinem ganzen Wesen wie ein Werkzeug von dahinterstehenden, planvoll wirkenden Individuall­täten erscheint. Aber wir müssen uns mancherlei Begriffe aneignen, die man im gewöhnlichen Leben nicht hat, wenn wir die merkwürdi­gen, geheimnisvollen Zusammenhänge zwischen dem Früheren und Späteren des geschichtlichen Werdens einsehen wollen.",
      "Wenn Sie sich erinnern an manches, was gesagt worden ist im Laufe der Jahre, so kann Ihnen vor die Seele treten, dass in alten Zeiten, in Zeiten auch der nachatlantischen Kulturentwicklung, wenn wir nur einige Jahrtausende vor unsere gewöhnlich historisch ge­nannte Zeit zurückgehen, die Menschen mehr oder weniger abnorme hellseherische Zustände hatten; dass zwischen dem, was wir heute",
      "das nüchterne, nur auf die physische Welt beschränkte Wachen nennen und zwischen dem bewusstlosen Schiafzustand mit seinem zweifel­haften Reich der Träume ein Bewusstselnsreich war, durch welches der Mensch hineintauchte in eine geistige, in eine spirituelle Realität. Und dasjenige, was heute von gelehrten Leuten, die so viele Mythen und Sagen wissenschaftlich erdichten, als dichtende Volksphantasie ausgelegt wird, wir wissen, dass es in Wahrheit zurückführt auf altes Heilsehen, auf hellsichtige Zustände der Menschenseele, die in jenen Zeiten hinter das physische Dasein sah und das also Geschaute in den Bildern der Mythe und auch der Märchen und Legenden zum Ausdruck gebracht hat.",
      "So dass wirklich, wenn wir alte, und zwar richtige alte Mythen, Märchen und Sagen vor uns haben, wir mehr Erkenntnis, mehr Weisheit und Wahrheit in ihnen finden können als in unserer heutigen abstrakten Gelehrsamkeit und Wissenschaft. Also wir blicken sozusagen auf einen hellsichtigen Menschen zurück, wenn wir den Blick in sehr alte Zeiten lenken, und wir wissen, dass diese Hellsichtigkeit immer mehr und mehr abnimmt bei den ver­schiedenen Völkern verschiedener Zeiten.",
      "Heute, bei dem Vortrage in der Weihnachtsfeier, habe ich sogar darauf aufmerksam machen dürfen, wie in Europa verhältnismässig sehr spät noch Reste des alten Helisehens im weitesten Umfange vorhanden waren. Das Erlöschen des Hellsehens und das Auftreten des auf den physischen Plan be­schränkten Bewusstseins vollzieht sich zu verschiedenen Zeiten bei den verschiedenen Völkern.",
      "Sie können sich nun denken, dass durch die Kulturepochen, wie wir sie aufgezählt haben nach der grossen atlantischen Katastrophe, durch die altindische, altpersische, ägyptisch-chaldäische, griechisch­lateinische und durch unsere Kulturepoche hindurch, die Menschen sozusagen in verschiedenster Art wirken mussten auf dem Plan der Weltgeschichte, weil sie in verschiedener Art verbunden waren mit der geistigen Welt. Wenn wir in die persische, auch noch in die ägyptisch-chaldäische Zeit zurückgehen, da ragt sozusagen das, was der Mensch in seiner Seele fühlte, erlebte, hinauf in geistige Welten, und geistige Mächte spielten in seine Seele herein. Was da eine lebendige Verbindung hatte zwischen der menschlichen Seele und",
      "den geistigen Welten, das hört im wesentlichen erst auf im vierten, im griechisch-lateinischen Zeitraum, und ganz und gar verschwunden ist es erst in unserer Zeit. Für die äussere Geschichte ist es in unserer Zeit nur da vorhanden, wo mit den Mitteln, die den Menschen heute zugänglich sind, bewusst die Verbindung wiederum gesucht wird zwischen dem, was in der Menschenseele lebt, und den geistigen und spirituellen Welten. Also in alten Zeiten, wenn der Mensch hinein-schaute in seine Seele, barg diese Seele nicht nur das in sich, was sie von der physischen Welt gelernt hatte, was sie erdacht hatte nach den Dingen der physischen Welt, sondern es lebte unmittelbar in ihr das­jenige, was wir zum Beispiel als geistige Hierarchien über den Men­schen hinauf bis in die geistigen Welten hinein geschildert haben. Das wirkte durch das Instrument der Menschenseele herunter auf den physischen Plan, und die Menschen wussten sich in Verbindung mit diesen Individualitäten der höheren Hierarchien. Wenn wir zurück­schauen meinetwillen noch in die ägyptisch-chaldälsehe Zeit - aller-dings müssen wir da die älteren Perioden nehmen -, so haben wir Menschen, die sozusagen historische Persönlichkeiten sind; aber wir verstehen sie nicht, wenn wir sie in dem Sinn von heute als historische Persönlichkeiten auffassen.",
      "Wenn wir heute von historischen Persönlichkeiten sprechen, sind wir als Menschen des materialistischen Zeitalters davon überzeugt, dass es nur die Impulse, die Intentionen der betreffenden Persönlich­keiten sind, die da wirken im Laufe der Geschichte. So können wir im Grunde genommen nur noch die Menschen von drei Jahrtausenden verstehen, das heisst allenfalls noch annähernd die Menschen des­jenigen Jahrtausends, das mit der Geburt des Christus Jesus abschliesst, und dann die Menschen des ersten und des zweiten christlichen Jahr­tausends, in dem wir ja selber stehen. Plato, Sokrates, vielleicht auch Thales und Perikles, das sind Menschen, die man allenfalls noch als uns ähnlich verstehen kann. Geht man aber weiter zurück, dann hört die Möglichkeit auf, Menschen zu verstehen, wenn man sie nur aus der Analogie mit den Menschen der Gegenwart verstehen will. So lässt sich etwa der ägyptische Hermes, der grosse Lehrer der ägypti­schen Kultur, nicht mehr verstehen, auch nicht Zarathustra, und nicht",
      "einmal Moses. Wenn wir zurückgehen jenseits des Jahrtausends, das der christlichen Zeitrechnung vorangeht, dann müssen wir schon damit rechnen, dass überall, wo wir es mit historischen Persönlich­keiten zu tun haben, höhere Individualltäten, höhere Hierarchien hinter ihnen stehen, diese Persönlichkeiten gleichsam von sich besessen machen, im besten Sinne des Wortes allerdings. Nun zeigt sich eine eigentümliche Erscheinung, ohne deren Kenntnis wir nicht den historischen Werdegang verstehen können.",
      "Wir haben unterschieden bis zu unserer Zeit fünf Zeiträume. Also wir haben den ersten nachatlantischen Kulturzeitraum weit zurück­reichend in den Jahrtausenden, den indischen Zeitraum; wir haben den zweiten, den altpersischen; den dritten, den ägyptisch-chaldä­ischen; den vierten, den griechisch4ateinischen, und den fünften, unseren eigenen Zeitraum. Schon wenn wir von dem griechisch-lateinischen Charakter zurückgehen zu dem ägyptischen, da müssen wir diesen Übergang für die historische Betrachtungsweise machen, dass wir anstatt einer rein menschlichen Betrachtungsweise, wie sie uns allenfalls noch den Gestalten der griechischen Welt gegenüber bis ins Heroenzeitalter zurück dienen kann, einen anderen Maß-stab anlegen; dass wir anfangen, hinter den einzelnen Persönlich­keiten die geistigen Mächte zu suchen, die Überpersönliches darstellen, und die durch die Persönlichkeiten als ihre Instrumente wirken. Diese geistigen Individualitäten müssen wir dabei ins seelische Auge fassen; so dass wir also förmlich sehen könnten einen Menschen, der auf dem physischen Plan steht, und hinter ihm wirksam eine Wesenheit der höheren Hierarchien, die diesen Menschen gleichsam von hinten hält und ihn hinstellt auf den Platz, auf dem er zu stehen hat innerhalb der Menschheitsentwicklung.",
      "Nun ist es gerade schon interessant genug, von diesem Gesichts­punkt aus die Beziehungen anzuschiagen zwischen den eigentlich wichtigen Vorgängen, den historisch bestimmenden Vorgängen der ägyptisch-chaldäischen Epoche und dergnechisch-latelnischen Epoche. Das sind zwei aufeinanderfolgende Kulturepochen, und wir dringen zunächst, sagen wir, bis zum Jahre 2300, 3200 bis 3500 vor unserer Zeitrechnung, also verhältnismässig gar nicht sehr weit. Dennoch",
      "werden wir nicht begreifen, was da geschehen ist, was ja auch heute schon die alte Geschichte etwas blosslegt; wir werden es nur dann begreifen, wenn wir hinter den geschichtlichen Persönlichkeiten die höheren Individualitäten sehen. Dann aber zeigt sich uns weiter, dass wir von all den wichtigen Dingen, die da im dritten Zeitraum ge­schahen, eine Art Wiederholung haben in dem vierten, im griechisch-lateinischen Zeitraum. Es ist fast so, wie wenn sozusagen das, was durch höhere Gesetze für den vorhergehenden Zeitraum erklärlich ist, durch Gesetze der physischen Welt erklärlich wird für den folgen­den; wie wenn es heruntergestiegen wäre, sich um eine Stufe ver­gröbert hätte, physischer geworden wäre: eine Art von Spiegelung in der physischen Welt zeigt sich uns für grosse Ereignisse der vorher­gehenden Zeiträume.",
      "Ich will Ihnen eben heute eine Einleitung geben und möchte Sie deshalb hinweisen darauf, wie uns in einem bedeutsamen Mythos eine der wichtigsten Tatsachen des ägyptisch-chaldäischen Zeitraumes gegeben ist; wie sich dann dieses Ereignis widerspiegelt, aber um eine Stufe herunterversetzt, im griechisch-latelnischen Zeitraum. Also zwei parallele Tatsachen möchte ich hinstellen, die zusammengehören in okkulter Beziehung; die eine dann gleichsam um einen halben Plan höher und die andere ganz auf der physischen Erde stehend, aber wie eine Art physisch gewordenen Schattenbildes eines geistigen Ereignisses der früheren Epoche. Äusserlich hat die Menschheit solche Ereignisse, wo Mächte der höheren Hierarchien dahinterstehen, immer nur durch Mythen erzählen können. Aber wir werden sehen, was gerade hinter dem Mythos liegt, der uns als das bedeutsamste Ereignis schildert, was aus der chaldälsehen Zeit hereinragt. Wir wollen uns nur die Hauptzüge des Mythos vor Augen stellen. Dieser Mythos besagt das folgende:",
      "Da war einmal ein grosser König, namens Gilgamesch. Aber schon aus dem Namen erkennt derjenige, der solche Namen zu beurteilen vermag, dass wir es nicht bloss mit einem physischen König zu tun haben, sondern mit einer dahinterstehenden Gottheit, mit einer dahinterstehenden geistigen Individualität, von der der König von Erek besessen war, die durch ihn wirkte. Also wir haben es zu tun",
      "mit dem, was wir im realen Sinne einen Gottmenschen zu nennen haben. Er bedrückt die Stadt Erek, so wird uns erzählt. Die Stadt Erek wendet sich an ihre Gottheit Aruru, und diese Gottheit lässt einen Helfer erstehen: aus der Erde heraus erwächst dieser Held. Das sind also die Bilder des Mythos; wir werden sehen, welche Tiefen von historischen Ereignissen hinter diesem Mythos liegen. Die Gott­heit lässt erstehen aus der Erde heraus Eabani, eine Art von mensch­licher Wesenheit, welche im Verhältnis zu Gilgamesch ausschaut wie eine niedere Wesenheit, denn es wird erzählt, dass er Tierfelle hatte, dass er mit Haaren bedeckt war, dass er wie ein Wilder war; aber in seiner Wildheit lebte Gottbeseeltheit, altes Heilsehen, Heliwissen, alte Hell-Erkenntnis.",
      "Eabani lernt eine Frau aus Erek kennen, und er wird dadurch in die Stadt gezogen. Er wird der Freund des Gilgamesch und dadurch zieht Friede in die Stadt ein. Nun herrschen sie beide zusammen, Gilgamesch und Eabani.",
      "Da wird durch eine Nachbarstadt die Stadt­göttin Ischtar der Stadt des Eabani und des Gilgamesch geraubt. Sie unternehmen beide einen Kriegszug gegen die räuberische Stadt. Sie überwinden den König und gewinnen die Stadtgöttin zurück.",
      "Nun ist die Stadtgöttin wiederum in Erek eingezogen, Gilgamesch lebt ihr gegenüber, und da tritt uns das Eigentümliche entgegen, dass Gilgamesch kein Verständnis hat für die eigenartige Natur der Stadt-göttin. Eine Szene spielt sich nun ab, die einen unmittelbar erinnert an eine biblische Szene des Johannes-Evangeliums.",
      "Gilgamesch steht Ischtar gegenüber. Er benimmt sich allerdings anders als der Christus Jesus; er wirft der Stadtgöttin vor, dass sie, bevor sie ihm gegenüber-getreten sei, viele andere Männer geliebt habe.",
      "Namentlich die Bekanntschaft mit dem letzten wirft er ihr vor. Darauf geht sie be­schwerdeführend zu derjenigen Gottheit, zu derjenigen Wesenheit der höheren Hierarchien, der gerade sie, die Stadtgöttin, zugeteilt ist.",
      "Sie geht zu Anu. Und nun sendet Anu einen Stier auf die Erde herab; mit diesem Stier muss Gilgamesch kämpfen. Wer sich an den stier­bekämpfenden Mithras erinnert, der findet einen Anklang daran an dieser Stelle, wo der von Anu heruntergesandte Stier bekämpft werden muss von Gilgamesch.",
      "Alle diese Ereignisse haben - und wir",
      "werden sehen, wenn wir den Mythos erklären werden, welche Tiefen darin stecken - nun dahin geführt, dass Eabani miffierweile gestorben ist. Gilgamesch ist jetzt allein. Ihm kommt ein Gedanke, der furchtbar an seiner Seele zehrt. Unter dem Eindruck dessen, was er da erlebt hat, wird ihm der Gedanke erst bewusst, dass der Mensch doch sterb­lich ist. Ein Gedanke, den er früher nicht berücksichtigt hatte, der tritt ihm in seiner ganzen Furchtbarkeit vor die Seele. Und da ver­nimmt er von dem einzigen Erdenmenschen, der unsterblich ge­blieben ist, während alle anderen Menschen in der nachatlantischen Zeit das Bewusstsein der Sterblichkeit erlangt haben: er hört von dem unsterblichen Xisuthros weit im Westen drüben. Nun unternimmt er, weil er erforschen will die Rätsel von Leben und Tod, den schwe­ren Zug nach dem Westen. - Schon heute kann ich sagen: Dieser Zug nach dem Westen ist kein anderer, als der Zug nach den Geheim­nissen der alten Atlantis, nach den Ereignissen, die vor der grossen atlantischen Katastrophe liegen.",
      "Dahin unternimmt Gilgamesch den Wanderzug. Sehr interessant ist es, dass er vorbei muss an einer Pforte, die behütet ist von Skor­pionenriesen; dass ihn der Geist einführt in das Reich des Todes, dass er eintritt in das Reich des Xisuthros und dass er in diesem Reich des Xisuthros erfährt, dass alle Menschen immer mehr von dem Bewusstsein des Todes durchdrungen werden müssen in der nach-atlantischen Zeit. Nun fragt er Xisuthros, woher er denn ein Wissen habe von seinem ewigen Kern, warum er von dem Bewusstsein der Unsterblichkeit durchdrungen sei. Da sagt ihm Xisuthros: Du kannst es auch werden, aber du musst nacherleben, was ich durchleben musste durch all die Überwindungen von Furcht und Angst und Ein­samkeit, die ich durchmachen musste. Als der Gott Ea beschlossen hatte - in dem, was wir die atlantische Katastrophe nennen - unter­gehen zu lassen, was von der Menschheit nicht weiter fortleben sollte, da trug er mir auf, mich zurückzuziehen in eine Art Schiff. Hinein-nehmen sollte ich die Tiere, die übrigbleiben sollten, und diejenigen Individualitäten, die da in Wahrheit genannt werden die Meister. Mit diesem Schiff überdauerte ich die grosse Katastrophe. So erzählte Xisuthros dem Gilgamesch: Was da durchgemacht worden ist, das",
      "kannst du nur im Innern erleben. Dadurch aber kannst du zum Bewusstsein der Unsterblichkeit kommen, wenn du sieben Nächte und sechs Tage nicht schläfst. - Gilgamesch will sich dieser Probe unterziehen, schiäft aber sehr bald ein. Da bäckt die Frau des Xisu­thros sieben mystische Brote, die sollen ersetzen durch ihren Genuss das, was in den sieben Nächten und sechs Tagen hätte errungen werden sollen. Nun zieht Gilgamesch weiter mit dieser Art Lebens-elixier und macht etwas durch wie ein Bad im Jungbrunnen und kommt wieder an die Küste seiner Heimat, die etwa am Euphrat und Tigris liegt. Da wird ihm die Kraft des Lebenselixiers durch eine Schlange. genommen, und er kommt also wieder ohne das Lebens-elixier in seinem Lande an, aber doch mit dem Bewusstsein, dass es eine Unsterblichkeit gibt, und von Sehnsucht erfüllt, wenigstens noch den Geist des Eabani zu sehen. Der erscheint ihm nun wirklich, und aus dem Gespräch, das sich dann abspinnt, erfahren wir die Art, wie sozusagen für die Kultur der ägyptisch-chaldäischen Zeit das Bewusst­sein des Zusammenhanges mit der geistigen Welt aufgehen konnte. Das ist wichtig, dieses Verhältnis von Gilgamesch und Eabani.",
      "Nun habe ich sozusagen Ihnen die Bilder eines Mythos hingestellt, des bedeutenden Gilgamesch-Mythos, des Mythos, von dem wir sehen werden, dass er uns in die spirituellen Tiefen führen wird, die hinter dem chaldäisch-babylonischen Kulturzeitraum liegen. Ich wollte Ihnen diese Bilder vorführen, die Ihnen zeigen werden, dass sozusagen zwei Individualitäten dastehen: die Individualität einer Wesenheit, die in sich hereinragen hat eine göttlich-geistige Wesenheit: Gilgamesch -und eine, die mehr Mensch ist, aber so, dass wir sie nennen möchten eine junge Seele, die noch wenige Inkarnationen durchgemacht hat und daher noch altes Hellsehen in späte Zeiten hereingetragen hat:",
      "Äusserlich ist uns dieser Eabani so dargestellt, dass er in Tierfelle gekleidet ist. Es wird uns damit seine Wildheit angedeutet; aber eben durch diese Wildheit ist er noch mit alter Hellsichtigkeit begabt einerseits, und auf der anderen Seite ist er eine junge Seele, die viel weniger Inkarnationen durchlebt hat als andere auf der Höhe der Entwicklung stehende Seelen. So stellt uns Gilgamesch dar eine",
      "Wesenheit, die zur Initiation reif war, die nur diese Initiation nicht mehr erreichen konnte, denn der Gang nach Westen ist der Gang zu einer Initiation, die nicht zu Ende geführt worden ist. Wir sehen auf der einen Seite den eigentlichen Inaugurator der chaldäisch­babylonischen Kultur in Gilgamesch und hinter ihm wirksam eine göttlich-geistige Wesenheit, eine Art Feuergeist, und dann neben ihm eine andere Individualität, eine junge Seele, den Eabani; eine Indivi­dualität, die spät erst zur Erdeninkarnation heruntergekommen ist. -Wenn Sie die ,,Geheimwissenschaft\" lesen, so werden Sie sehen, dass die Individualitäten erst nach und nach von den Planeten wieder heruntergekommen sind. - Von dem Austausch dessen, was diese beiden wissen, hängt die babylonisch-chaldäische Kultur ab, und wir werden sehen, dass die ganze babylonisch-chaldäische Kultur ein Ergebnis dessen ist, was von Gilgamesch und Eabani herrührt.",
      "Da ragt Hellsichtigkeit von dem Gottmenschen Gilgamesch und Hell­sichtigkeit von der jungen Seele Eabani in die chaldäisch-babylonische Kultur hinein. Dieser Prozess von zweien, die nebeneinander wirken, von denen der eine dem andern notwendig ist, das spiegelt sich nun ab im spätern vierten Kulturzeitraum, im griechisch-lateinischen, und zwar auf dem physischen Plan.",
      "Zum vollen Verständnis einer solchen Abspiegelung werden wir allerdings erst allmählich gelangen. Es spiegelt sich also ein mehr geistiger Vorgang auf dem physischen Plane ab, als die Menschheit sehr weit heruntergestiegen ist, als sie nicht mehr die Zusammengehörigkeit der menschlichen Persönlich­keit mit der geistig-göttlichen Welt fühlt.",
      "Diese Geheimnisse der geistig-göttlichen Welt sind bewahrt worden in den Mysterienstätten. So zum Beispiel war vieles von den alten, heiligen Geheimnissen, die da kündeten den Zusammenhang der menschlichen Seele mit den göttlich-geistigen Welten, aufbewahrt worden in dem Mysterium der Diana von Ephesus und im ephesischen Tempel. Da war vieles darinnen, was einem Zeitalter, das heraus­gegangen war zur menschlichen Persönlichkeit, nicht mehr verständ­lich war. Und wie ein Wahrzeichen des geringen Verständnisses der bloss äussern Persönlichkeit für das, was spirituell geblieben ist, steht uns die halb mythische Figur des Herostrat da, die nur auf das Äusser­lichste",
      "der Persönlichkeit sieht; Herostrat, der die Feuerfackel wirft in den Tempel des Heiligtums von Ephesus. Wie ein Wahrzeichen des Zusammenstosses der Persöniichkeit mit dem, was von alten spirituellen Zeiten geblieben ist, erscheint uns diese Tat. Und an demselben Tage, wo ein Mensch, bloss um seinen Namen auf die Nachwelt zu bringen, die Feuerfackel wirft in den Tempel des Heilig­tums von Ephesus, an dem gleichen Tage wird der Mensch geboren, der zur Persönlichkeitskultur das allermeiste getan hat auf demjenigen Grund und Boden, auf dem die blosse Persönlichkeitskultur über­wunden werden soll: Herostrat wirft die Fackel an dem Tage, da Alexander der Grosse geboren wird, der Mensch, der ganz Persön­lichkeit ist. So steht Alexander der Grosse da als das Schattenbild des Gilgamesch.",
      "Dahinter steckt eine tiefe Wahrheit. Wie das Schattenbild des Gilgamesch steht Alexander der Grosse im vierten, im griechisch-lateinischen Zeitraum, wie die Projektion eines Geistigen auf den physischen Plan. Und der Eabani' der ist, projiziert auf den physischen Plan, Aristoteles, der Lehrer Alexanders des Grossen. So sonderbar das ist: Alexander und Aristoteles stehen nebeneinander wie Gilga­mesch und Eabani. Und wir sehen sozusagen, wie im ersten Drittel des vierten nachatlantischen Zeitraumes von Alexander dem Grossen herübergetragen wird - nur in die Gesetze des physischen Planes übersetzt - das, was von Gilgamesch der chaldäisch-babylonischen Kultur gegeben worden war. Das drückt sich wunderbar aus, indem als eine Nachwirkung der Taten Alexanders des Grossen an der Stätte des ägyptisch-chaldäischen Kulturschauplatzes Alexandria ge­gründet wird, um es, wie in ein Zentrum, gerade dort hinzusetzen, wohin der dritte Zeitraum, der ägyptisch-babylonisch-chaldäische, so mächtig gereicht hatte. Und alles sollte sich zusammenfinden in diesem alexandrinischen Kulturzentrum. Da sind nach und nach wirklich zusammengekommen all die Kulturströmungen, die sich begegnen sollten aus der nachatlantischen Zeit. Wie in einem Zentrum trafen sie sich gerade in Alexandrien, an der Stätte, die hingestellt war auf den Schauplatz des dritten Kulturzeitraums, mit dem Cha­rakter des vierten Zeitraumes. Und Alexandria überdauerte die Entstehung",
      "des Christentums. Ja, in Alexandria entwickelten sich erst die wichtigsten Dinge des vierten Kulturzeitraumes, als das Christen­tum schon da war. Da waten die grossen Gelehrten tätig, da waten insbesondere die drei allerwesentlichsten Kulturströmungen zu­sammengeflos sen: die alte heidnisch-griechische, die christliche und die mosaisch-hebräische. Die waren zusammen in Alexandria, die wirkten da durcheinander. Und es ist undenkbar, dass die Kultur Alexandriens, die ganz auf Persöniichkeit gebaut war, durch irgend etwas anderes hätte inauguriert werden können als durch das mit Persönlichkeit inspirierte Wesen, wie es Alexander der Grosse war. Denn jetzt nahm gerade durch Alexandrien, durch diesen Kultur-mittelpunkt, alles das, was früher überpersönlich war, was früher überall hinaufgeragt hat von der menschlichen Persönlichkeit in die höheren geistigen Welten, einen persönlichen Charakter an. Die Per­sönlichkeiten, die da vor uns stehen, haben sozusagen alles in sich; wir sehen nurmehr ganz wenig die Mächte, die von höheren Hier­archien aus sie lenken und sie an ihren Platz stellen. All die ver­schiedenen Weisen und Philosophen, die in Alexandria gewirkt haben, sind ganz ins Menschlich-Persöniiche umgesetzte alte Weisheit; überall spricht das Persönliche aus ihnen. Das ist das Eigenartige:",
      "Alles, was im alten Heidentum nur dadurch erklärlich war, dass immer darauf hingewiesen wurde, wie Götter heruntergestiegen sind und sich mit Menschentöchtern verbunden haben, um Helden zu erzeugen - all das wird umgesetzt in die persönliche Tatkraft der Menschen in Alexandria. Und was das Judentum, die mosaische Kultur in Alexandria für Formen angenommen hat, das können wir aus dem ersehen, was uns gerade die Zeiten, in denen das Christen­tum schon da war, zeigen. Da ist nichts mehr vorhanden von jenen tiefen Auffassungen eines Zusammenhanges der Menschenwelt mit der geistigen Welt, wie sie in der Prophetenzeit immerhin vorhanden war, wie sie selbst in den letzten zwei Jahrhunderten vor dem Beginne unserer Zeitrechnung noch zu finden ist: da ist auch im Judentum alles Persönlichkeit geworden. Tüchtige Menschen sind da, mit ausser-ordentlicher Vertiefung in die Geheimnisse der alten Geheimlehren... aber persönlich ist alles geworden, Persönlichkeiten wirken in",
      "Alexandria. Und das Christentum tritt zuerst in Alexandria auf, man möchte sagen, wie in seiner entarteten Kindheitsstufe.",
      "Das Christentum, das berufen ist, das Persönliche im Menschen immer weiter hinaufzuführen in das Unpersönliche, es trat gerade in Alexandria besonders stark auf. Namentlich wirkten die christlichen Persönlichkeiten so, dass wir oftmals den Eindruck haben: es sind in ihren Taten schon Vorwegnahmen späterer Handiungen rein per­sönlich wirkender Bischöfe und Erzbischöfe. So wirkte der Erz­bischof Theophilos im vierten Jahrhundert, so wirkte sein Nach­folger und Verwandter, der heilige Kyrillos. Wir können sie sozu­sagen nur beurteilen von ihren menschlichen Schwächen aus. Das Christentum, das das Grösste der Menschheit geben soll, zeigt sich zuerst in seinen allergrössten Schwächen und von seiner persönlichen Seite. Aber es sollte in Alexandria ein Wahrzeichen vor die ganze Entwicklung der Menschheit hingestellt werden.",
      "Da haben wir wiederum eine solche Projektion von früherem Spirituelleren auf den äusseren physischen Plan. Es gab eine wunder­bare Persönlichkeit in den alten orphischen Mysterien; sie machte die Geheimnisse dieser Mysterien durch; sie gehörte zu den aller­sympathischsten, zu den allerinteressantesten Schülern der alten griechischen orphischen Mysterien. Sie war gut vorbereitet, nament­lich durch eine gewisse keltische Geheimschulung, die sie in früheren Inkarnationen durchgemacht hatte. Diese Individualität hat mit einer tiefen Inbrunst die Geheimnisse der otphischen Mysterien gesucht. Das sollte ja an der eigenen Seele durchlebt werden von den Schülern der orphischen Geheimnisse, was in dem Mythos enthalten ist von dem Dionysos Zagreus, der von den Titanen zerstückelt wird, dessen Leib aber Zeus zu einem höheren Leben emporführt. Als ein indivi­duelles menschliches Erlebnis sollte es gerade von den Orphikern nacherlebt werden, wie der Mensch dadurch, dass er einen gewissen Mysterienweg durchmacht, sozusagen sich auslebt in der äusseren Welt, mit seinem ganzen Wesen zerstückelt wird, aufhört, sich in sich selber zu finden.",
      "Während es sonst eine abstrakte Erkenntnis ist, wenn wir auf die gewöhnliche Art und Weise die Tiere, Pflanzen, Mineralien erkennen,",
      "weil wir ausserhalb ihrer bleiben - so muss derjenige, der eine wirk­liche Erkenntnis im okkulten Sinn erlangen will, sich so üben, wie wenn er in den Tieren, Pflanzen, Mineralien, in Luft und Wasser, in Quellen und Bergen, in den Steinen und Sternen, in den anderen Menschen darinnen wäre, wie wenn er eins wäre mit ihnen. Und dennoch muss er die starke innere Seelenkraft entwickeln als Orphiker, um wiederhergestellt als ganz in sich geschlossene Individualität zu triumphieren über die Zerstückelung in der äusseren Welt. Es gehörte in einer gewissen Weise zum Höchsten, was man an Einweihungs-geheimnissen hat erleben können, wenn dasjenige, was ich Ihnen eben angedeutet habe, menschliches Erlebnis geworden war. Und viele Schüler der orphischen Mysterien haben solche Erlebnisse durch­gemacht, haben auf diese Weise ihre Zerstückelung in der Welt erlebt und haben damit das Höchste durchgemacht, was in vorchrist­lichen Zeiten als eine Art Vorbereitung für das Christentum hat erlebt werden können.",
      "Zu den orphischen Mysterienschülern gehört unter anderen auch die sympathische Persönlichkeit, die nicht mit einem äusseren Namen auf die Nachwelt gekommen ist, die sich aber deutlich zeigt als ein Schüler der orphischen Mysterien, und auf die ich jetzt hindeute. Schon als Jüngling und dann viele Jahre hindurch war diese Persön­lichkeit mit all den griechischen Orphien eng verbunden. Sie hat gewirkt in derjenigen Zeit, die der griechischen Philosophie voran­gegangen ist und die nicht mehr in den Geschichtsbüchern der Philosophie aufgezeichnet ist; denn das, was mit Thales und Heraklit aufgezeichnet ist, das ist ein Nachklang von dem, was die Mysterien-schüler früher in ihrer Art gewirkt haben. Und zu diesen Mysterien-schülern gehört derjenige, von dem ich Ihnen jetzt eben spreche als einem Schüler der orphischen Mysterien, der dann wiederum zu seinem Schüler hatte jenen Pherekydes von Syros, der in dem Münch­ner Zyklus ,,Der Orient im Lichte des Okzidents\" vom vorigen Jahre angeführt worden ist.",
      "Sehen Sie, diese Individualität, die in jenem Schüler der orphischen Mysterien war, sie finden wir durch Forschung in der Akasha­Chronik wiederverkörpert im vierten Jahrhundert der nachchristlichen",
      "Zeit. Wir finden sie in ihrer Wiederverkörperung hineingestellt mitten in das Treiben der Kreise von Alexandria, umgesetzt die orphischen Geheimnisse in persönliche Erlebnisse, freilich höchster Art. Es ist merkwürdig, wie das alles bei der Wiederverkörperung in persönliche Erlebnisse umgesetzt war. Am Ende des vierten Jahr­hunderts der nachchristlichen Zeit als die Tochter eines grossen Mathematikers, des Theon' sehen wir diese Individualität wieder­geboren. Wir sehen, wie in ihrer Seele alles das auflebt, was man durchieben konnte von den orphischen Mysterien an der Anschauung der grossen, mathematischen, lichtvollen Zusammenhänge der Welt. Das alle& war jetzt persönliches Talent, persönliche Fähigkeit. Jetzt brauchte selbst diese Individualität einen Mathematiker zum Vater, um etwas vererbt zu erhalten; so persönlich mussten diese Fähig­keiten sein.",
      "So blicken wir zurück auf Zeiten, wo der Mensch noch in Zu­sammenhang war mit den geistigen Welten wie bei jener orphischen Persönlichkeit; so sehen wir ihr Schattenbild unter denjenigen, die da lehrten in Alexandria an der Grenascheide des vierten und fünften Jahrhunderts. Und noch nichts hatte diese Individualität aufgenom­men von dem, was - man könnte sagen - die Menschen damals über die Schattenseiten des christlichen Anfangs hinwegsehen liess; denn zu gross war noch in dieser Seele alles das, was ein Nachklang war aus den orphischen Mysterien, zu gross, als dass es von jenem anderen Licht, dem neuen Christus-Ereignis, hätte erleuchtet werden können. Was als Christentum ringsherum auftrat, etwa in Theophilos und Kyrillos, das war wahrhaftig so, dass jene orphische Individualität' die jetzt einen persönlichen Charakter angenommen hatte, Grösseres und Weisheitsvolleres zu sagen und zu geben hatte als diejenigen, die das Christentum in jener Zeit zu Alexandria vertraten.",
      "Vom tiefsten Hass erfüllt waren Theophilos sowohl als auch Kyrillos gegen alles, was nicht christlich-kirchlich war in dem engen Sinn, wie es gerade diese beiden Erzbischöfe aufgefasst haben. Ganz persönlichen Charakter hatte das Christentum da angenommen, so einen Persönlichkeitscharakter, dass diese beiden Erzbischöfe sich persönliche Söldlinge anwarben. Überall wurden die Menschen zusammengeholt,",
      "die sozusagen Schutztruppen der Erzbischöfe bilden sollten. Auf Macht im persönlichsten Sinn kam es ihnen an. Und was sie ganz beseelte, das war der Hass gegen das, was aus alten Zeiten herrührte und doch so viel grösser war als das in einem Zerrbild erscheinende Neue.",
      "Der tiefste Hass lebte in den christlichen Würden­trägern Alexandriens namentlich gegen die Individualität des wieder­geborenen Orphikers. Und daher brauchen wir uns nicht zu ver­wundern, dass die wiederverkörperte Orphiker4ndividualität an­geschwärzt wurde als schwarze Magierin.",
      "Und das war genügend, um den ganzen Pöbel, der als Söldlinge angeworben war, aufzu-stacheln gegen die hehre, einzigartige Gestalt des wiederverkörperten Orpheus-Schülers. Und diese Gestalt war noch jung, und sie war trotz ihrer Jugend, trotzdem sie manches durchzumachen hatte, was auch in der damaligen Zeit einem Weibe durch lange Studien hindurch grosse Schwierigkeiten machte, sie war hinaufgestiegen zu dem Lichte, das leuchten konnte über alle Weisheit, über alle Erkenntnis der damaligen Zeiten.",
      "Und es war ein Wunderbares, wie in den Lehrsälen der Hypatia - denn so hiess der wiederverkörperte Orphiker -, wie da die reinste, lichtvollste Weisheit in Alexandrien zu den begeister­ten Hörern drang. Sie hat zu ihren Füssen gezwungen nicht etwa nur die alten Heiden, sondern auch solche einsichtsvolle, tiefgehende Christen wie den Synesius.",
      "Sie war von einem bedeutsamen Einfluss und man konnte das in die Persönlichkeit umgesetzte Wiederauf­leben der alten heidnischen Weisheit des Orpheus in Hypatia in Alexandria erleben.",
      "Und wahrhaftig symbolisch wirkte das Weltenkarma. Was das Geheimnis ihrer Einweihung ausmachte, es erschien wirklich hinein-projiziert, abgeschattet, auf den physischen Plan. Und damit berühren wir ein Ereignis, das symbolisch wirksam und bedeutend ist für manches, was sich in historischen Zeiten abspielt. Wir berühren eines jener Ereignisse, das scheinbar nur ein Märtyrertod ist, das aber ein Symbolum ist, in dem sich spirituelle Kräfte und Bedeutungen aus­sprechen.",
      "Der Wut derer, die um den Erzbischof von Alexandrien waren, verfiel an einem Märztage des Jahres 415 Hypatia. Ihrer Macht, ihrer",
      "geistigen Macht wollte man sich entledigen. Die ungebildetsten, wilden Horden waren hereingehetzt auch von der Umgebung Alexandriens, und unter Vorspiegelungen holte man die jungfräuliche Weise ab. Sie bestieg den Wagen und auf ein Zeichen machten sich die aufgehetzten Leute über sie her, rissen ihr die Kleider vom Leibe, schleppten sie in eine Kirche und rissen ihr buchstäblich das Fleisch von den Knochen. Sie zerfleischten und zerstückelten sie, und die Stücke ihres Leibes wurden von den durch ihre gierigen Leiden­schaften völlig entmenschten Massen noch in der Stadt herum-geschleift. Das ist das Schicksal der grossen Philosophin Hypatia.",
      "Symbolisch, möchte ich sagen, ist da etwas angedeutet, das tief zusammenhängt mit der Gründung Alexanders des Grossen, Alexan­driens, wenn es auch spät erst nach der Begründung Alexandriens sich zuträgt. In diesem Ereignis sind abgespiegelt wichtige Geheim­nisse des vierten nachatlantischen Zeitalters, das so Grosses, Bedeu­tendes in sich hatte, und das auch dasjenige, was es zeigen musste als Auflösung des Alten, als Hinwegfegung des Alten, in einer so paradox grossartigen Weise vor die Welt hingestellt hat in einem so bedeut­samen Symbolum, wie es die Hinschlachtung - anders kann man es nicht nennen - der bedeutendsten Frau von der Wende des vierten und fünften Jahrhunderts, der Hypatia, war."
    ],
    "sentences": [
      [
        "In der Geisteswissenschaft verhält es sich so, dass die Wahrheiten, die Erkenntnisse um so schwieriger werden, je weitet man von all­gemeinen Verhältnissen heruntersteigt zu besonderen konkreten Ein­zelheiten.",
        "Es konnte von Ihnen dies schon bemerkt werden, als in verschiedenen Arbeitsgruppen versucht wurde, im einzelnen ge­schichtlich zu sprechen etwa über die Wiederverkörperungen des grossen Führers der Perserreligion, des Zarathustra - als gesprochen wurde über den Zusammenhang des Zarathustra mit Moses, mit Hermes und auch mit dem Jesus von Nazareth.",
        "Auch bei anderen Gelegenheiten sind ja konkrete geschichtliche Fragen bereits berührt worden.",
        "Man steigt von Dingen, über welche das menschliche Herz noch dies oder jenes Unwahrscheinliche verhältnismässig leicht hin­nimmt, in Gebiete hinab voll von Unwahrscheinlichkeiten, sobald man heruntersteigt von den grossen Wahrheiten über das geistig Durchtränkt- und Durchwobensein der Welt, von den grossen Welt-gesetzen zur geistigen Natur einer einzelnen Individualität, einer einzelnen Persönlichkeit.",
        "Und bei noch nicht genügend vorbereiteten Menschen beginnt in der Regel an diesem Abgrund zwischen den allgemeinen und besonderen Wahrheiten die Ungläubigkeit."
      ],
      [
        "Nun werde ich Ihnen in den Vorträgen, zu denen die heutige Be­trachtung eine Art von Einleitung geben soll, die der okkulten Geschichte angehören und von historischen Tatsachen und geschicht­lichen Persönlichkeiten im Lichte der Geisteswissenschaft handeln, manches Sonderbare zu sagen haben.",
        "Sie werden manches Sonderbare hören, das auf Ihren guten Willen wird rechnen müssen, auf jenen guten Willen, der herangeschult ist durch alles dasjenige, was im Laufe von Jahren an geisteswissenschaftlichen Erkenntnissen durch"
      ],
      [
        "Ihre Seele gezogen ist.",
        "Denn das ist ja die schönste, die bedeutsamste Frucht, die wir gewinnen aus der spirituellen Weltanschauung, dass, so kompliziert, so im einzelnen ausgebaut auch die Erkenntnisse sind, die wir gewinnen, wir zuletzt doch nicht vor uns haben bloss eine Summe von Dogmen, sondern dass wir in uns, in unseren Herzen, in unseren Gemütern durch diese geisteswissenschaftliche Betrach­tungsweise etwas besitzen, was uns hinausrückt über den Standpunkt, den wir sonst durch irgendeine andere Weltbetrachtung gewinnen können."
      ],
      [
        "Nicht Dogmen, nicht Lehrsätze, nicht ein blosses Wissen nehmen wir auf, sondern durch unsere Erkenntnisse werden wir andere Menschen.",
        "In gewisser Beziehung gehört zu solchen Partien geistiger Wissenschaft wie diejenigen, die wir jetzt betrachten werden, Seelenverständnis, nicht intellektuelles Verständnis - Seelenverständ­nis, das vielleicht an gar manchen Stellen auch geneigt sein muss, Andeutungen anzuhören und hinzunehmen, die grob, die brutal werden würden, wenn man sie in allzu scharfe Konturen hinein­pressen wollte."
      ],
      [
        "Wovon ich Ihnen gerne Vorstellungen hervorrufen möchte, das ist, dass in dem ganzen auch geschichtlichen Werde-prozess der Menschlieit durch die verschiedenen Jahrtausende hin­durch bis in unsere Tage hinein hinter allem Menschenwerden und menschlichen Geschehen geistige Wesenheiten, geistige Individuali-täten als Leiter, als Führer stehen, und dass für die grössten, für die wichtigsten Tatsachen des historischen Verlaufes dieser oder jener Mensch mit seiner ganzen Seele, mit seinem ganzen Wesen wie ein Werkzeug von dahinterstehenden, planvoll wirkenden Individuall­täten erscheint.",
        "Aber wir müssen uns mancherlei Begriffe aneignen, die man im gewöhnlichen Leben nicht hat, wenn wir die merkwürdi­gen, geheimnisvollen Zusammenhänge zwischen dem Früheren und Späteren des geschichtlichen Werdens einsehen wollen."
      ],
      [
        "Wenn Sie sich erinnern an manches, was gesagt worden ist im Laufe der Jahre, so kann Ihnen vor die Seele treten, dass in alten Zeiten, in Zeiten auch der nachatlantischen Kulturentwicklung, wenn wir nur einige Jahrtausende vor unsere gewöhnlich historisch ge­nannte Zeit zurückgehen, die Menschen mehr oder weniger abnorme hellseherische Zustände hatten; dass zwischen dem, was wir heute"
      ],
      [
        "das nüchterne, nur auf die physische Welt beschränkte Wachen nennen und zwischen dem bewusstlosen Schiafzustand mit seinem zweifel­haften Reich der Träume ein Bewusstselnsreich war, durch welches der Mensch hineintauchte in eine geistige, in eine spirituelle Realität.",
        "Und dasjenige, was heute von gelehrten Leuten, die so viele Mythen und Sagen wissenschaftlich erdichten, als dichtende Volksphantasie ausgelegt wird, wir wissen, dass es in Wahrheit zurückführt auf altes Heilsehen, auf hellsichtige Zustände der Menschenseele, die in jenen Zeiten hinter das physische Dasein sah und das also Geschaute in den Bildern der Mythe und auch der Märchen und Legenden zum Ausdruck gebracht hat."
      ],
      [
        "So dass wirklich, wenn wir alte, und zwar richtige alte Mythen, Märchen und Sagen vor uns haben, wir mehr Erkenntnis, mehr Weisheit und Wahrheit in ihnen finden können als in unserer heutigen abstrakten Gelehrsamkeit und Wissenschaft.",
        "Also wir blicken sozusagen auf einen hellsichtigen Menschen zurück, wenn wir den Blick in sehr alte Zeiten lenken, und wir wissen, dass diese Hellsichtigkeit immer mehr und mehr abnimmt bei den ver­schiedenen Völkern verschiedener Zeiten."
      ],
      [
        "Heute, bei dem Vortrage in der Weihnachtsfeier, habe ich sogar darauf aufmerksam machen dürfen, wie in Europa verhältnismässig sehr spät noch Reste des alten Helisehens im weitesten Umfange vorhanden waren.",
        "Das Erlöschen des Hellsehens und das Auftreten des auf den physischen Plan be­schränkten Bewusstseins vollzieht sich zu verschiedenen Zeiten bei den verschiedenen Völkern."
      ],
      [
        "Sie können sich nun denken, dass durch die Kulturepochen, wie wir sie aufgezählt haben nach der grossen atlantischen Katastrophe, durch die altindische, altpersische, ägyptisch-chaldäische, griechisch­lateinische und durch unsere Kulturepoche hindurch, die Menschen sozusagen in verschiedenster Art wirken mussten auf dem Plan der Weltgeschichte, weil sie in verschiedener Art verbunden waren mit der geistigen Welt.",
        "Wenn wir in die persische, auch noch in die ägyptisch-chaldäische Zeit zurückgehen, da ragt sozusagen das, was der Mensch in seiner Seele fühlte, erlebte, hinauf in geistige Welten, und geistige Mächte spielten in seine Seele herein.",
        "Was da eine lebendige Verbindung hatte zwischen der menschlichen Seele und"
      ],
      [
        "den geistigen Welten, das hört im wesentlichen erst auf im vierten, im griechisch-lateinischen Zeitraum, und ganz und gar verschwunden ist es erst in unserer Zeit.",
        "Für die äussere Geschichte ist es in unserer Zeit nur da vorhanden, wo mit den Mitteln, die den Menschen heute zugänglich sind, bewusst die Verbindung wiederum gesucht wird zwischen dem, was in der Menschenseele lebt, und den geistigen und spirituellen Welten.",
        "Also in alten Zeiten, wenn der Mensch hinein-schaute in seine Seele, barg diese Seele nicht nur das in sich, was sie von der physischen Welt gelernt hatte, was sie erdacht hatte nach den Dingen der physischen Welt, sondern es lebte unmittelbar in ihr das­jenige, was wir zum Beispiel als geistige Hierarchien über den Men­schen hinauf bis in die geistigen Welten hinein geschildert haben.",
        "Das wirkte durch das Instrument der Menschenseele herunter auf den physischen Plan, und die Menschen wussten sich in Verbindung mit diesen Individualitäten der höheren Hierarchien.",
        "Wenn wir zurück­schauen meinetwillen noch in die ägyptisch-chaldälsehe Zeit - aller-dings müssen wir da die älteren Perioden nehmen -, so haben wir Menschen, die sozusagen historische Persönlichkeiten sind; aber wir verstehen sie nicht, wenn wir sie in dem Sinn von heute als historische Persönlichkeiten auffassen."
      ],
      [
        "Wenn wir heute von historischen Persönlichkeiten sprechen, sind wir als Menschen des materialistischen Zeitalters davon überzeugt, dass es nur die Impulse, die Intentionen der betreffenden Persönlich­keiten sind, die da wirken im Laufe der Geschichte.",
        "So können wir im Grunde genommen nur noch die Menschen von drei Jahrtausenden verstehen, das heisst allenfalls noch annähernd die Menschen des­jenigen Jahrtausends, das mit der Geburt des Christus Jesus abschliesst, und dann die Menschen des ersten und des zweiten christlichen Jahr­tausends, in dem wir ja selber stehen.",
        "Plato, Sokrates, vielleicht auch Thales und Perikles, das sind Menschen, die man allenfalls noch als uns ähnlich verstehen kann.",
        "Geht man aber weiter zurück, dann hört die Möglichkeit auf, Menschen zu verstehen, wenn man sie nur aus der Analogie mit den Menschen der Gegenwart verstehen will.",
        "So lässt sich etwa der ägyptische Hermes, der grosse Lehrer der ägypti­schen Kultur, nicht mehr verstehen, auch nicht Zarathustra, und nicht"
      ],
      [
        "einmal Moses.",
        "Wenn wir zurückgehen jenseits des Jahrtausends, das der christlichen Zeitrechnung vorangeht, dann müssen wir schon damit rechnen, dass überall, wo wir es mit historischen Persönlich­keiten zu tun haben, höhere Individualltäten, höhere Hierarchien hinter ihnen stehen, diese Persönlichkeiten gleichsam von sich besessen machen, im besten Sinne des Wortes allerdings.",
        "Nun zeigt sich eine eigentümliche Erscheinung, ohne deren Kenntnis wir nicht den historischen Werdegang verstehen können."
      ],
      [
        "Wir haben unterschieden bis zu unserer Zeit fünf Zeiträume.",
        "Also wir haben den ersten nachatlantischen Kulturzeitraum weit zurück­reichend in den Jahrtausenden, den indischen Zeitraum; wir haben den zweiten, den altpersischen; den dritten, den ägyptisch-chaldä­ischen; den vierten, den griechisch4ateinischen, und den fünften, unseren eigenen Zeitraum.",
        "Schon wenn wir von dem griechisch-lateinischen Charakter zurückgehen zu dem ägyptischen, da müssen wir diesen Übergang für die historische Betrachtungsweise machen, dass wir anstatt einer rein menschlichen Betrachtungsweise, wie sie uns allenfalls noch den Gestalten der griechischen Welt gegenüber bis ins Heroenzeitalter zurück dienen kann, einen anderen Maß-stab anlegen; dass wir anfangen, hinter den einzelnen Persönlich­keiten die geistigen Mächte zu suchen, die Überpersönliches darstellen, und die durch die Persönlichkeiten als ihre Instrumente wirken.",
        "Diese geistigen Individualitäten müssen wir dabei ins seelische Auge fassen; so dass wir also förmlich sehen könnten einen Menschen, der auf dem physischen Plan steht, und hinter ihm wirksam eine Wesenheit der höheren Hierarchien, die diesen Menschen gleichsam von hinten hält und ihn hinstellt auf den Platz, auf dem er zu stehen hat innerhalb der Menschheitsentwicklung."
      ],
      [
        "Nun ist es gerade schon interessant genug, von diesem Gesichts­punkt aus die Beziehungen anzuschiagen zwischen den eigentlich wichtigen Vorgängen, den historisch bestimmenden Vorgängen der ägyptisch-chaldäischen Epoche und dergnechisch-latelnischen Epoche.",
        "Das sind zwei aufeinanderfolgende Kulturepochen, und wir dringen zunächst, sagen wir, bis zum Jahre 2300, 3200 bis 3500 vor unserer Zeitrechnung, also verhältnismässig gar nicht sehr weit.",
        "Dennoch"
      ],
      [
        "werden wir nicht begreifen, was da geschehen ist, was ja auch heute schon die alte Geschichte etwas blosslegt; wir werden es nur dann begreifen, wenn wir hinter den geschichtlichen Persönlichkeiten die höheren Individualitäten sehen.",
        "Dann aber zeigt sich uns weiter, dass wir von all den wichtigen Dingen, die da im dritten Zeitraum ge­schahen, eine Art Wiederholung haben in dem vierten, im griechisch-lateinischen Zeitraum.",
        "Es ist fast so, wie wenn sozusagen das, was durch höhere Gesetze für den vorhergehenden Zeitraum erklärlich ist, durch Gesetze der physischen Welt erklärlich wird für den folgen­den; wie wenn es heruntergestiegen wäre, sich um eine Stufe ver­gröbert hätte, physischer geworden wäre: eine Art von Spiegelung in der physischen Welt zeigt sich uns für grosse Ereignisse der vorher­gehenden Zeiträume."
      ],
      [
        "Ich will Ihnen eben heute eine Einleitung geben und möchte Sie deshalb hinweisen darauf, wie uns in einem bedeutsamen Mythos eine der wichtigsten Tatsachen des ägyptisch-chaldäischen Zeitraumes gegeben ist; wie sich dann dieses Ereignis widerspiegelt, aber um eine Stufe herunterversetzt, im griechisch-latelnischen Zeitraum.",
        "Also zwei parallele Tatsachen möchte ich hinstellen, die zusammengehören in okkulter Beziehung; die eine dann gleichsam um einen halben Plan höher und die andere ganz auf der physischen Erde stehend, aber wie eine Art physisch gewordenen Schattenbildes eines geistigen Ereignisses der früheren Epoche.",
        "Äusserlich hat die Menschheit solche Ereignisse, wo Mächte der höheren Hierarchien dahinterstehen, immer nur durch Mythen erzählen können.",
        "Aber wir werden sehen, was gerade hinter dem Mythos liegt, der uns als das bedeutsamste Ereignis schildert, was aus der chaldälsehen Zeit hereinragt.",
        "Wir wollen uns nur die Hauptzüge des Mythos vor Augen stellen.",
        "Dieser Mythos besagt das folgende:"
      ],
      [
        "Da war einmal ein grosser König, namens Gilgamesch.",
        "Aber schon aus dem Namen erkennt derjenige, der solche Namen zu beurteilen vermag, dass wir es nicht bloss mit einem physischen König zu tun haben, sondern mit einer dahinterstehenden Gottheit, mit einer dahinterstehenden geistigen Individualität, von der der König von Erek besessen war, die durch ihn wirkte.",
        "Also wir haben es zu tun"
      ],
      [
        "mit dem, was wir im realen Sinne einen Gottmenschen zu nennen haben.",
        "Er bedrückt die Stadt Erek, so wird uns erzählt.",
        "Die Stadt Erek wendet sich an ihre Gottheit Aruru, und diese Gottheit lässt einen Helfer erstehen: aus der Erde heraus erwächst dieser Held.",
        "Das sind also die Bilder des Mythos; wir werden sehen, welche Tiefen von historischen Ereignissen hinter diesem Mythos liegen.",
        "Die Gott­heit lässt erstehen aus der Erde heraus Eabani, eine Art von mensch­licher Wesenheit, welche im Verhältnis zu Gilgamesch ausschaut wie eine niedere Wesenheit, denn es wird erzählt, dass er Tierfelle hatte, dass er mit Haaren bedeckt war, dass er wie ein Wilder war; aber in seiner Wildheit lebte Gottbeseeltheit, altes Heilsehen, Heliwissen, alte Hell-Erkenntnis."
      ],
      [
        "Eabani lernt eine Frau aus Erek kennen, und er wird dadurch in die Stadt gezogen.",
        "Er wird der Freund des Gilgamesch und dadurch zieht Friede in die Stadt ein.",
        "Nun herrschen sie beide zusammen, Gilgamesch und Eabani."
      ],
      [
        "Da wird durch eine Nachbarstadt die Stadt­göttin Ischtar der Stadt des Eabani und des Gilgamesch geraubt.",
        "Sie unternehmen beide einen Kriegszug gegen die räuberische Stadt.",
        "Sie überwinden den König und gewinnen die Stadtgöttin zurück."
      ],
      [
        "Nun ist die Stadtgöttin wiederum in Erek eingezogen, Gilgamesch lebt ihr gegenüber, und da tritt uns das Eigentümliche entgegen, dass Gilgamesch kein Verständnis hat für die eigenartige Natur der Stadt-göttin.",
        "Eine Szene spielt sich nun ab, die einen unmittelbar erinnert an eine biblische Szene des Johannes-Evangeliums."
      ],
      [
        "Gilgamesch steht Ischtar gegenüber.",
        "Er benimmt sich allerdings anders als der Christus Jesus; er wirft der Stadtgöttin vor, dass sie, bevor sie ihm gegenüber-getreten sei, viele andere Männer geliebt habe."
      ],
      [
        "Namentlich die Bekanntschaft mit dem letzten wirft er ihr vor.",
        "Darauf geht sie be­schwerdeführend zu derjenigen Gottheit, zu derjenigen Wesenheit der höheren Hierarchien, der gerade sie, die Stadtgöttin, zugeteilt ist."
      ],
      [
        "Sie geht zu Anu.",
        "Und nun sendet Anu einen Stier auf die Erde herab; mit diesem Stier muss Gilgamesch kämpfen.",
        "Wer sich an den stier­bekämpfenden Mithras erinnert, der findet einen Anklang daran an dieser Stelle, wo der von Anu heruntergesandte Stier bekämpft werden muss von Gilgamesch."
      ],
      [
        "Alle diese Ereignisse haben - und wir"
      ],
      [
        "werden sehen, wenn wir den Mythos erklären werden, welche Tiefen darin stecken - nun dahin geführt, dass Eabani miffierweile gestorben ist.",
        "Gilgamesch ist jetzt allein.",
        "Ihm kommt ein Gedanke, der furchtbar an seiner Seele zehrt.",
        "Unter dem Eindruck dessen, was er da erlebt hat, wird ihm der Gedanke erst bewusst, dass der Mensch doch sterb­lich ist.",
        "Ein Gedanke, den er früher nicht berücksichtigt hatte, der tritt ihm in seiner ganzen Furchtbarkeit vor die Seele.",
        "Und da ver­nimmt er von dem einzigen Erdenmenschen, der unsterblich ge­blieben ist, während alle anderen Menschen in der nachatlantischen Zeit das Bewusstsein der Sterblichkeit erlangt haben: er hört von dem unsterblichen Xisuthros weit im Westen drüben.",
        "Nun unternimmt er, weil er erforschen will die Rätsel von Leben und Tod, den schwe­ren Zug nach dem Westen. - Schon heute kann ich sagen: Dieser Zug nach dem Westen ist kein anderer, als der Zug nach den Geheim­nissen der alten Atlantis, nach den Ereignissen, die vor der grossen atlantischen Katastrophe liegen."
      ],
      [
        "Dahin unternimmt Gilgamesch den Wanderzug.",
        "Sehr interessant ist es, dass er vorbei muss an einer Pforte, die behütet ist von Skor­pionenriesen; dass ihn der Geist einführt in das Reich des Todes, dass er eintritt in das Reich des Xisuthros und dass er in diesem Reich des Xisuthros erfährt, dass alle Menschen immer mehr von dem Bewusstsein des Todes durchdrungen werden müssen in der nach-atlantischen Zeit.",
        "Nun fragt er Xisuthros, woher er denn ein Wissen habe von seinem ewigen Kern, warum er von dem Bewusstsein der Unsterblichkeit durchdrungen sei.",
        "Da sagt ihm Xisuthros: Du kannst es auch werden, aber du musst nacherleben, was ich durchleben musste durch all die Überwindungen von Furcht und Angst und Ein­samkeit, die ich durchmachen musste.",
        "Als der Gott Ea beschlossen hatte - in dem, was wir die atlantische Katastrophe nennen - unter­gehen zu lassen, was von der Menschheit nicht weiter fortleben sollte, da trug er mir auf, mich zurückzuziehen in eine Art Schiff.",
        "Hinein-nehmen sollte ich die Tiere, die übrigbleiben sollten, und diejenigen Individualitäten, die da in Wahrheit genannt werden die Meister.",
        "Mit diesem Schiff überdauerte ich die grosse Katastrophe.",
        "So erzählte Xisuthros dem Gilgamesch: Was da durchgemacht worden ist, das"
      ],
      [
        "kannst du nur im Innern erleben.",
        "Dadurch aber kannst du zum Bewusstsein der Unsterblichkeit kommen, wenn du sieben Nächte und sechs Tage nicht schläfst. - Gilgamesch will sich dieser Probe unterziehen, schiäft aber sehr bald ein.",
        "Da bäckt die Frau des Xisu­thros sieben mystische Brote, die sollen ersetzen durch ihren Genuss das, was in den sieben Nächten und sechs Tagen hätte errungen werden sollen.",
        "Nun zieht Gilgamesch weiter mit dieser Art Lebens-elixier und macht etwas durch wie ein Bad im Jungbrunnen und kommt wieder an die Küste seiner Heimat, die etwa am Euphrat und Tigris liegt.",
        "Da wird ihm die Kraft des Lebenselixiers durch eine Schlange. genommen, und er kommt also wieder ohne das Lebens-elixier in seinem Lande an, aber doch mit dem Bewusstsein, dass es eine Unsterblichkeit gibt, und von Sehnsucht erfüllt, wenigstens noch den Geist des Eabani zu sehen.",
        "Der erscheint ihm nun wirklich, und aus dem Gespräch, das sich dann abspinnt, erfahren wir die Art, wie sozusagen für die Kultur der ägyptisch-chaldäischen Zeit das Bewusst­sein des Zusammenhanges mit der geistigen Welt aufgehen konnte.",
        "Das ist wichtig, dieses Verhältnis von Gilgamesch und Eabani."
      ],
      [
        "Nun habe ich sozusagen Ihnen die Bilder eines Mythos hingestellt, des bedeutenden Gilgamesch-Mythos, des Mythos, von dem wir sehen werden, dass er uns in die spirituellen Tiefen führen wird, die hinter dem chaldäisch-babylonischen Kulturzeitraum liegen.",
        "Ich wollte Ihnen diese Bilder vorführen, die Ihnen zeigen werden, dass sozusagen zwei Individualitäten dastehen: die Individualität einer Wesenheit, die in sich hereinragen hat eine göttlich-geistige Wesenheit: Gilgamesch -und eine, die mehr Mensch ist, aber so, dass wir sie nennen möchten eine junge Seele, die noch wenige Inkarnationen durchgemacht hat und daher noch altes Hellsehen in späte Zeiten hereingetragen hat:"
      ],
      [
        "Äusserlich ist uns dieser Eabani so dargestellt, dass er in Tierfelle gekleidet ist.",
        "Es wird uns damit seine Wildheit angedeutet; aber eben durch diese Wildheit ist er noch mit alter Hellsichtigkeit begabt einerseits, und auf der anderen Seite ist er eine junge Seele, die viel weniger Inkarnationen durchlebt hat als andere auf der Höhe der Entwicklung stehende Seelen.",
        "So stellt uns Gilgamesch dar eine"
      ],
      [
        "Wesenheit, die zur Initiation reif war, die nur diese Initiation nicht mehr erreichen konnte, denn der Gang nach Westen ist der Gang zu einer Initiation, die nicht zu Ende geführt worden ist.",
        "Wir sehen auf der einen Seite den eigentlichen Inaugurator der chaldäisch­babylonischen Kultur in Gilgamesch und hinter ihm wirksam eine göttlich-geistige Wesenheit, eine Art Feuergeist, und dann neben ihm eine andere Individualität, eine junge Seele, den Eabani; eine Indivi­dualität, die spät erst zur Erdeninkarnation heruntergekommen ist. -Wenn Sie die ,,Geheimwissenschaft\" lesen, so werden Sie sehen, dass die Individualitäten erst nach und nach von den Planeten wieder heruntergekommen sind. - Von dem Austausch dessen, was diese beiden wissen, hängt die babylonisch-chaldäische Kultur ab, und wir werden sehen, dass die ganze babylonisch-chaldäische Kultur ein Ergebnis dessen ist, was von Gilgamesch und Eabani herrührt."
      ],
      [
        "Da ragt Hellsichtigkeit von dem Gottmenschen Gilgamesch und Hell­sichtigkeit von der jungen Seele Eabani in die chaldäisch-babylonische Kultur hinein.",
        "Dieser Prozess von zweien, die nebeneinander wirken, von denen der eine dem andern notwendig ist, das spiegelt sich nun ab im spätern vierten Kulturzeitraum, im griechisch-lateinischen, und zwar auf dem physischen Plan."
      ],
      [
        "Zum vollen Verständnis einer solchen Abspiegelung werden wir allerdings erst allmählich gelangen.",
        "Es spiegelt sich also ein mehr geistiger Vorgang auf dem physischen Plane ab, als die Menschheit sehr weit heruntergestiegen ist, als sie nicht mehr die Zusammengehörigkeit der menschlichen Persönlich­keit mit der geistig-göttlichen Welt fühlt."
      ],
      [
        "Diese Geheimnisse der geistig-göttlichen Welt sind bewahrt worden in den Mysterienstätten.",
        "So zum Beispiel war vieles von den alten, heiligen Geheimnissen, die da kündeten den Zusammenhang der menschlichen Seele mit den göttlich-geistigen Welten, aufbewahrt worden in dem Mysterium der Diana von Ephesus und im ephesischen Tempel.",
        "Da war vieles darinnen, was einem Zeitalter, das heraus­gegangen war zur menschlichen Persönlichkeit, nicht mehr verständ­lich war.",
        "Und wie ein Wahrzeichen des geringen Verständnisses der bloss äussern Persönlichkeit für das, was spirituell geblieben ist, steht uns die halb mythische Figur des Herostrat da, die nur auf das Äusser­lichste"
      ],
      [
        "der Persönlichkeit sieht; Herostrat, der die Feuerfackel wirft in den Tempel des Heiligtums von Ephesus.",
        "Wie ein Wahrzeichen des Zusammenstosses der Persöniichkeit mit dem, was von alten spirituellen Zeiten geblieben ist, erscheint uns diese Tat.",
        "Und an demselben Tage, wo ein Mensch, bloss um seinen Namen auf die Nachwelt zu bringen, die Feuerfackel wirft in den Tempel des Heilig­tums von Ephesus, an dem gleichen Tage wird der Mensch geboren, der zur Persönlichkeitskultur das allermeiste getan hat auf demjenigen Grund und Boden, auf dem die blosse Persönlichkeitskultur über­wunden werden soll: Herostrat wirft die Fackel an dem Tage, da Alexander der Grosse geboren wird, der Mensch, der ganz Persön­lichkeit ist.",
        "So steht Alexander der Grosse da als das Schattenbild des Gilgamesch."
      ],
      [
        "Dahinter steckt eine tiefe Wahrheit.",
        "Wie das Schattenbild des Gilgamesch steht Alexander der Grosse im vierten, im griechisch-lateinischen Zeitraum, wie die Projektion eines Geistigen auf den physischen Plan.",
        "Und der Eabani' der ist, projiziert auf den physischen Plan, Aristoteles, der Lehrer Alexanders des Grossen.",
        "So sonderbar das ist: Alexander und Aristoteles stehen nebeneinander wie Gilga­mesch und Eabani.",
        "Und wir sehen sozusagen, wie im ersten Drittel des vierten nachatlantischen Zeitraumes von Alexander dem Grossen herübergetragen wird - nur in die Gesetze des physischen Planes übersetzt - das, was von Gilgamesch der chaldäisch-babylonischen Kultur gegeben worden war.",
        "Das drückt sich wunderbar aus, indem als eine Nachwirkung der Taten Alexanders des Grossen an der Stätte des ägyptisch-chaldäischen Kulturschauplatzes Alexandria ge­gründet wird, um es, wie in ein Zentrum, gerade dort hinzusetzen, wohin der dritte Zeitraum, der ägyptisch-babylonisch-chaldäische, so mächtig gereicht hatte.",
        "Und alles sollte sich zusammenfinden in diesem alexandrinischen Kulturzentrum.",
        "Da sind nach und nach wirklich zusammengekommen all die Kulturströmungen, die sich begegnen sollten aus der nachatlantischen Zeit.",
        "Wie in einem Zentrum trafen sie sich gerade in Alexandrien, an der Stätte, die hingestellt war auf den Schauplatz des dritten Kulturzeitraums, mit dem Cha­rakter des vierten Zeitraumes.",
        "Und Alexandria überdauerte die Entstehung"
      ],
      [
        "des Christentums.",
        "Ja, in Alexandria entwickelten sich erst die wichtigsten Dinge des vierten Kulturzeitraumes, als das Christen­tum schon da war.",
        "Da waten die grossen Gelehrten tätig, da waten insbesondere die drei allerwesentlichsten Kulturströmungen zu­sammengeflos sen: die alte heidnisch-griechische, die christliche und die mosaisch-hebräische.",
        "Die waren zusammen in Alexandria, die wirkten da durcheinander.",
        "Und es ist undenkbar, dass die Kultur Alexandriens, die ganz auf Persöniichkeit gebaut war, durch irgend etwas anderes hätte inauguriert werden können als durch das mit Persönlichkeit inspirierte Wesen, wie es Alexander der Grosse war.",
        "Denn jetzt nahm gerade durch Alexandrien, durch diesen Kultur-mittelpunkt, alles das, was früher überpersönlich war, was früher überall hinaufgeragt hat von der menschlichen Persönlichkeit in die höheren geistigen Welten, einen persönlichen Charakter an.",
        "Die Per­sönlichkeiten, die da vor uns stehen, haben sozusagen alles in sich; wir sehen nurmehr ganz wenig die Mächte, die von höheren Hier­archien aus sie lenken und sie an ihren Platz stellen.",
        "All die ver­schiedenen Weisen und Philosophen, die in Alexandria gewirkt haben, sind ganz ins Menschlich-Persöniiche umgesetzte alte Weisheit; überall spricht das Persönliche aus ihnen.",
        "Das ist das Eigenartige:"
      ],
      [
        "Alles, was im alten Heidentum nur dadurch erklärlich war, dass immer darauf hingewiesen wurde, wie Götter heruntergestiegen sind und sich mit Menschentöchtern verbunden haben, um Helden zu erzeugen - all das wird umgesetzt in die persönliche Tatkraft der Menschen in Alexandria.",
        "Und was das Judentum, die mosaische Kultur in Alexandria für Formen angenommen hat, das können wir aus dem ersehen, was uns gerade die Zeiten, in denen das Christen­tum schon da war, zeigen.",
        "Da ist nichts mehr vorhanden von jenen tiefen Auffassungen eines Zusammenhanges der Menschenwelt mit der geistigen Welt, wie sie in der Prophetenzeit immerhin vorhanden war, wie sie selbst in den letzten zwei Jahrhunderten vor dem Beginne unserer Zeitrechnung noch zu finden ist: da ist auch im Judentum alles Persönlichkeit geworden.",
        "Tüchtige Menschen sind da, mit ausser-ordentlicher Vertiefung in die Geheimnisse der alten Geheimlehren... aber persönlich ist alles geworden, Persönlichkeiten wirken in"
      ],
      [
        "Alexandria.",
        "Und das Christentum tritt zuerst in Alexandria auf, man möchte sagen, wie in seiner entarteten Kindheitsstufe."
      ],
      [
        "Das Christentum, das berufen ist, das Persönliche im Menschen immer weiter hinaufzuführen in das Unpersönliche, es trat gerade in Alexandria besonders stark auf.",
        "Namentlich wirkten die christlichen Persönlichkeiten so, dass wir oftmals den Eindruck haben: es sind in ihren Taten schon Vorwegnahmen späterer Handiungen rein per­sönlich wirkender Bischöfe und Erzbischöfe.",
        "So wirkte der Erz­bischof Theophilos im vierten Jahrhundert, so wirkte sein Nach­folger und Verwandter, der heilige Kyrillos.",
        "Wir können sie sozu­sagen nur beurteilen von ihren menschlichen Schwächen aus.",
        "Das Christentum, das das Grösste der Menschheit geben soll, zeigt sich zuerst in seinen allergrössten Schwächen und von seiner persönlichen Seite.",
        "Aber es sollte in Alexandria ein Wahrzeichen vor die ganze Entwicklung der Menschheit hingestellt werden."
      ],
      [
        "Da haben wir wiederum eine solche Projektion von früherem Spirituelleren auf den äusseren physischen Plan.",
        "Es gab eine wunder­bare Persönlichkeit in den alten orphischen Mysterien; sie machte die Geheimnisse dieser Mysterien durch; sie gehörte zu den aller­sympathischsten, zu den allerinteressantesten Schülern der alten griechischen orphischen Mysterien.",
        "Sie war gut vorbereitet, nament­lich durch eine gewisse keltische Geheimschulung, die sie in früheren Inkarnationen durchgemacht hatte.",
        "Diese Individualität hat mit einer tiefen Inbrunst die Geheimnisse der otphischen Mysterien gesucht.",
        "Das sollte ja an der eigenen Seele durchlebt werden von den Schülern der orphischen Geheimnisse, was in dem Mythos enthalten ist von dem Dionysos Zagreus, der von den Titanen zerstückelt wird, dessen Leib aber Zeus zu einem höheren Leben emporführt.",
        "Als ein indivi­duelles menschliches Erlebnis sollte es gerade von den Orphikern nacherlebt werden, wie der Mensch dadurch, dass er einen gewissen Mysterienweg durchmacht, sozusagen sich auslebt in der äusseren Welt, mit seinem ganzen Wesen zerstückelt wird, aufhört, sich in sich selber zu finden."
      ],
      [
        "Während es sonst eine abstrakte Erkenntnis ist, wenn wir auf die gewöhnliche Art und Weise die Tiere, Pflanzen, Mineralien erkennen,"
      ],
      [
        "weil wir ausserhalb ihrer bleiben - so muss derjenige, der eine wirk­liche Erkenntnis im okkulten Sinn erlangen will, sich so üben, wie wenn er in den Tieren, Pflanzen, Mineralien, in Luft und Wasser, in Quellen und Bergen, in den Steinen und Sternen, in den anderen Menschen darinnen wäre, wie wenn er eins wäre mit ihnen.",
        "Und dennoch muss er die starke innere Seelenkraft entwickeln als Orphiker, um wiederhergestellt als ganz in sich geschlossene Individualität zu triumphieren über die Zerstückelung in der äusseren Welt.",
        "Es gehörte in einer gewissen Weise zum Höchsten, was man an Einweihungs-geheimnissen hat erleben können, wenn dasjenige, was ich Ihnen eben angedeutet habe, menschliches Erlebnis geworden war.",
        "Und viele Schüler der orphischen Mysterien haben solche Erlebnisse durch­gemacht, haben auf diese Weise ihre Zerstückelung in der Welt erlebt und haben damit das Höchste durchgemacht, was in vorchrist­lichen Zeiten als eine Art Vorbereitung für das Christentum hat erlebt werden können."
      ],
      [
        "Zu den orphischen Mysterienschülern gehört unter anderen auch die sympathische Persönlichkeit, die nicht mit einem äusseren Namen auf die Nachwelt gekommen ist, die sich aber deutlich zeigt als ein Schüler der orphischen Mysterien, und auf die ich jetzt hindeute.",
        "Schon als Jüngling und dann viele Jahre hindurch war diese Persön­lichkeit mit all den griechischen Orphien eng verbunden.",
        "Sie hat gewirkt in derjenigen Zeit, die der griechischen Philosophie voran­gegangen ist und die nicht mehr in den Geschichtsbüchern der Philosophie aufgezeichnet ist; denn das, was mit Thales und Heraklit aufgezeichnet ist, das ist ein Nachklang von dem, was die Mysterien-schüler früher in ihrer Art gewirkt haben.",
        "Und zu diesen Mysterien-schülern gehört derjenige, von dem ich Ihnen jetzt eben spreche als einem Schüler der orphischen Mysterien, der dann wiederum zu seinem Schüler hatte jenen Pherekydes von Syros, der in dem Münch­ner Zyklus ,,Der Orient im Lichte des Okzidents\" vom vorigen Jahre angeführt worden ist."
      ],
      [
        "Sehen Sie, diese Individualität, die in jenem Schüler der orphischen Mysterien war, sie finden wir durch Forschung in der Akasha­Chronik wiederverkörpert im vierten Jahrhundert der nachchristlichen"
      ],
      [
        "Zeit.",
        "Wir finden sie in ihrer Wiederverkörperung hineingestellt mitten in das Treiben der Kreise von Alexandria, umgesetzt die orphischen Geheimnisse in persönliche Erlebnisse, freilich höchster Art.",
        "Es ist merkwürdig, wie das alles bei der Wiederverkörperung in persönliche Erlebnisse umgesetzt war.",
        "Am Ende des vierten Jahr­hunderts der nachchristlichen Zeit als die Tochter eines grossen Mathematikers, des Theon' sehen wir diese Individualität wieder­geboren.",
        "Wir sehen, wie in ihrer Seele alles das auflebt, was man durchieben konnte von den orphischen Mysterien an der Anschauung der grossen, mathematischen, lichtvollen Zusammenhänge der Welt.",
        "Das alle& war jetzt persönliches Talent, persönliche Fähigkeit.",
        "Jetzt brauchte selbst diese Individualität einen Mathematiker zum Vater, um etwas vererbt zu erhalten; so persönlich mussten diese Fähig­keiten sein."
      ],
      [
        "So blicken wir zurück auf Zeiten, wo der Mensch noch in Zu­sammenhang war mit den geistigen Welten wie bei jener orphischen Persönlichkeit; so sehen wir ihr Schattenbild unter denjenigen, die da lehrten in Alexandria an der Grenascheide des vierten und fünften Jahrhunderts.",
        "Und noch nichts hatte diese Individualität aufgenom­men von dem, was - man könnte sagen - die Menschen damals über die Schattenseiten des christlichen Anfangs hinwegsehen liess; denn zu gross war noch in dieser Seele alles das, was ein Nachklang war aus den orphischen Mysterien, zu gross, als dass es von jenem anderen Licht, dem neuen Christus-Ereignis, hätte erleuchtet werden können.",
        "Was als Christentum ringsherum auftrat, etwa in Theophilos und Kyrillos, das war wahrhaftig so, dass jene orphische Individualität' die jetzt einen persönlichen Charakter angenommen hatte, Grösseres und Weisheitsvolleres zu sagen und zu geben hatte als diejenigen, die das Christentum in jener Zeit zu Alexandria vertraten."
      ],
      [
        "Vom tiefsten Hass erfüllt waren Theophilos sowohl als auch Kyrillos gegen alles, was nicht christlich-kirchlich war in dem engen Sinn, wie es gerade diese beiden Erzbischöfe aufgefasst haben.",
        "Ganz persönlichen Charakter hatte das Christentum da angenommen, so einen Persönlichkeitscharakter, dass diese beiden Erzbischöfe sich persönliche Söldlinge anwarben.",
        "Überall wurden die Menschen zusammengeholt,"
      ],
      [
        "die sozusagen Schutztruppen der Erzbischöfe bilden sollten.",
        "Auf Macht im persönlichsten Sinn kam es ihnen an.",
        "Und was sie ganz beseelte, das war der Hass gegen das, was aus alten Zeiten herrührte und doch so viel grösser war als das in einem Zerrbild erscheinende Neue."
      ],
      [
        "Der tiefste Hass lebte in den christlichen Würden­trägern Alexandriens namentlich gegen die Individualität des wieder­geborenen Orphikers.",
        "Und daher brauchen wir uns nicht zu ver­wundern, dass die wiederverkörperte Orphiker4ndividualität an­geschwärzt wurde als schwarze Magierin."
      ],
      [
        "Und das war genügend, um den ganzen Pöbel, der als Söldlinge angeworben war, aufzu-stacheln gegen die hehre, einzigartige Gestalt des wiederverkörperten Orpheus-Schülers.",
        "Und diese Gestalt war noch jung, und sie war trotz ihrer Jugend, trotzdem sie manches durchzumachen hatte, was auch in der damaligen Zeit einem Weibe durch lange Studien hindurch grosse Schwierigkeiten machte, sie war hinaufgestiegen zu dem Lichte, das leuchten konnte über alle Weisheit, über alle Erkenntnis der damaligen Zeiten."
      ],
      [
        "Und es war ein Wunderbares, wie in den Lehrsälen der Hypatia - denn so hiess der wiederverkörperte Orphiker -, wie da die reinste, lichtvollste Weisheit in Alexandrien zu den begeister­ten Hörern drang.",
        "Sie hat zu ihren Füssen gezwungen nicht etwa nur die alten Heiden, sondern auch solche einsichtsvolle, tiefgehende Christen wie den Synesius."
      ],
      [
        "Sie war von einem bedeutsamen Einfluss und man konnte das in die Persönlichkeit umgesetzte Wiederauf­leben der alten heidnischen Weisheit des Orpheus in Hypatia in Alexandria erleben."
      ],
      [
        "Und wahrhaftig symbolisch wirkte das Weltenkarma.",
        "Was das Geheimnis ihrer Einweihung ausmachte, es erschien wirklich hinein-projiziert, abgeschattet, auf den physischen Plan.",
        "Und damit berühren wir ein Ereignis, das symbolisch wirksam und bedeutend ist für manches, was sich in historischen Zeiten abspielt.",
        "Wir berühren eines jener Ereignisse, das scheinbar nur ein Märtyrertod ist, das aber ein Symbolum ist, in dem sich spirituelle Kräfte und Bedeutungen aus­sprechen."
      ],
      [
        "Der Wut derer, die um den Erzbischof von Alexandrien waren, verfiel an einem Märztage des Jahres 415 Hypatia.",
        "Ihrer Macht, ihrer"
      ],
      [
        "geistigen Macht wollte man sich entledigen.",
        "Die ungebildetsten, wilden Horden waren hereingehetzt auch von der Umgebung Alexandriens, und unter Vorspiegelungen holte man die jungfräuliche Weise ab.",
        "Sie bestieg den Wagen und auf ein Zeichen machten sich die aufgehetzten Leute über sie her, rissen ihr die Kleider vom Leibe, schleppten sie in eine Kirche und rissen ihr buchstäblich das Fleisch von den Knochen.",
        "Sie zerfleischten und zerstückelten sie, und die Stücke ihres Leibes wurden von den durch ihre gierigen Leiden­schaften völlig entmenschten Massen noch in der Stadt herum-geschleift.",
        "Das ist das Schicksal der grossen Philosophin Hypatia."
      ],
      [
        "Symbolisch, möchte ich sagen, ist da etwas angedeutet, das tief zusammenhängt mit der Gründung Alexanders des Grossen, Alexan­driens, wenn es auch spät erst nach der Begründung Alexandriens sich zuträgt.",
        "In diesem Ereignis sind abgespiegelt wichtige Geheim­nisse des vierten nachatlantischen Zeitalters, das so Grosses, Bedeu­tendes in sich hatte, und das auch dasjenige, was es zeigen musste als Auflösung des Alten, als Hinwegfegung des Alten, in einer so paradox grossartigen Weise vor die Welt hingestellt hat in einem so bedeut­samen Symbolum, wie es die Hinschlachtung - anders kann man es nicht nennen - der bedeutendsten Frau von der Wende des vierten und fünften Jahrhunderts, der Hypatia, war."
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "II",
    "paragraphs": [
      "Es ist gestern einleitend zunächst darauf aufmerksam gemacht worden, wie wir gewisse ältere geschichtliche Ereignisse der Mensch­heit nur dann richtig verstehen können, wenn wir nicht bloss auf die Kräfte und Fähigkeiten der Persönlichkeiten selbst blicken, sondern wenn wir voraussetzen, dass durch die betreffenden Persöniichkeiten, wie durch Werkzeuge hindurch, Wesenheiten wirken, die sozusagen ihre Taten aus höheren Welten herunterströmen lassen in unsere Welt. Wir müssen uns vorstellen, dass diese Wesenheiten hier in unserer Welt nicht unmittelbar angreifen können an unsere physischen Dinge, bei unseren physischen Tatsachen, weil sie wegen ihrer gegen­wärtigen Entwicklungsstufe sich nicht in einem physischen Leibe verkörpern können, der seine Elemente aus unserer physischen Welt nimmt. Wollen sie daher wirken innerhalb unserer physischen Welt, dann müssen sie sich des physischen Menschen bedienen, seiner Hand, aber auch seines Verstandes, seiner Auffassungsfähigkeiten. Wir finden den Einfluss und die Einwirkung solcher Wesenheiten der höheren Welten um so deutlicher ausgeprägt, je weiter wir zurück-gehen in den Zeiten der Menschheitsentwicklung. Man darf aber nicht etwa glauben, dass dieses Herunterströmen von Kräften und Wir­kungsweisen aus den höheren Welten in die physische Welt durch Menschen bis in unsere Zeit herein jemals aufgehört habe.",
      "Für den Geisteswissenschafter, der, wie wir es seit Jahren nun schon entfalten konnten, in sich aufgenommen hat, was unser Emp­finden und unser Vorstellen hinführt zu der Voraussetzung der höhe­ren Welten, für den wird ja eine solche Tatsache, wie sie eben charak­terisiert worden ist, gewiss von vorneherein etwas Verständliches haben, denn er ist gewohnt, sozusagen die Verbindungsfäden immer",
      "zu ziehen, die unsere Erkenntnis, unser Denken, unseren Willen mit den Wesenheiten der höheren Hierarchien verknüpfen. Aber der Geisteswissenschafter kommt ja zuweilen auch in die Lage, sich wehren zu müssen gegenüber den materialistischen Vorstellungen, die nun schon einmal in unserer Gegenwart vorhanden sind; gegen­über den Vorstellungen, die es den Menschen, die der spirituellen Entwicklung fernestehen, unmöglich machen, irgendwie auch nur einzugehen auf das, was über das Herunterwirken höherer Welten in unsere physische Welt gesagt werden muss.",
      "In unserer Zeit gehört es ja im Grunde genommen schon zu den veralteten Anschauungen, wenn man nur von dem Walten abstrakter Ideen innerhalb der Menschheitsereignisse, innerhalb der Geschichte spricht. Schon das gilt heute manchen Menschen für etwas ganz Unerlaubtes gegenüber wahrer Wissenschaftlichkeit, wenn man davon spricht, dass gewisse Ideen, abstrakte Ideen, die eigentlich im Grunde doch nur in unserem Verstande leben können, dass diese sich ausleben in den aufeinanderfolgenden Epochen der Geschichte.",
      "Einen letzten Schein sozusagen von Glauben an solche abstrakte Ideen wenigstens -von denen man allerdings nicht begreifen kann, wie sie wirken sollen, da es doch abstrakte Ideen sind! -, einen gewissen letzten Schein von Glauben an solche abstrakte Ideen hat ja im 19. Jahrhundert noch selbst die Geschichtsschreibung des Ranke gehabt.",
      "Aber auch dieser Glaube an wirkende Ideen der Geschichte wird nach und nach von unserer fortschreitenden materialistischen Entwicklung über Bord geworfen, und es gilt heute in gewisser Beziehung auch der Ge­schichte gegenüber für das Zeichen eines aufgeklärten Kopfes, wenn man lediglich daran glaubt, dass alles, was die Epochen charakteri­siert, was in den Epochen aufgetreten ist, im Grunde genommen nur durch das Zusammenfliessen physisch anschaulicher äusserer Taten entsteht, äusserer Bedürfnisse, äusserer Interessen und eben Ideen der physischen Menschen. Die Zeit ist ja heute schon vorüber, in der noch in einer gewissen Weise wie durch Inspiration solche Geister wie etwa Herder die Entwicklung der Menschheitsgeschichte so dar­gestellt haben, dass man überall merkt: es liegt wenigstens die Voraus­setzung lebendiger Mächte, lebendiger übersinnlicher Mächte zugrunde,",
      "die sich durch die Taten der Menschen, durch das Lehen der Menschen äussern. Und wer ein ganz gescheiter Kopf heute sein will, wird sagen: Na, so ein Mensch wie Lessing hat ja manche recht ver­nünftige Idee gehabt, aber dann kam er am Ende seines Lebens auf so konfuses Zeug, wie er es in seiner ,,Erziehung des Menschen-geschlechtes\" geschrieben hat, wo er sich nicht anders mehr zu helfen wusste, als die strenge Gesetzmässigkeit im Flusse des historischen Werdens an die Idee der Wiederverkörperung zu knüpfrn.",
      "In den letzten Sätzen seiner ,,Erziehung des Menschengeschlechts\" hat ja Lessing in der Tat zum Ausdruck gebracht, was die Geisteswissen­schaft aus den okkulten Tatsachen heraus schildert: dass Seelen, die in alten Epochen gelebt haben, die da aufgenommen haben die lebendig wirksamen Kräfte, diese Kräfte herübertragen in ihre neuen Verkörperungen, so dass nicht ein abstrakter, nicht bloss ein ideen­hafter Fortfluss vorhanden ist, sondern ein wirklicher, ein realer Fortfluss des Geistes hinter dem materiellen Geschehen. Wie gesagt, ein gescheiter Kopf wird sagen: Da ist er im Altet noch auf solche konfuse Ideen gekommen wie auf die Wiederverkörperung; über die muss man hinwegsehen. - Das erinnert einen immer wiederum an die so bitter4ronische und doch so kluge Notiz, die sich einmal Hebbel in sein Tagebuch geschrieben hat, wo er sagt, es wäre ein schönes Motiv, dass ein Gymnasiallehrer in seiner Schule den Plato durch-nimmt, dass sich der wiederverkörperte Plato unter seinen Schülern befindet, und dass der den Plato, wie ihn der Gymnasiallehrer durch-nimmt, so schlecht versteht, dass der Lehrer ihm arge Strafen auf­erlegen muss...",
      "In bezug auf die historische Auffassung der Menschheitsentwick­lung ist ja von der früheren geistigen Erfassung gar manches verloren­gegangen, und die Geisteswissenschaft wird sich wirklich wehren müssen gegenüber dem Ansturm des materialistischen Denkens, das von allen Seiten her eindringt und einfach töricht findet, was aus den geistigen Tatsachen heraus mitzuteilen ist. Wir haben es ja im Grunde genommen recht herrlich weit gebracht, zum Beispiel auch darin, wie alle jene gewaltigen Bilder, jene gewaltigen symbolischen Vor­stellungen, welche dem alten hellseherischen Erkennen der Menschen",
      "entflossen sind und die in den Mythologien, in den Heroengestalten, in den Legenden und Märchengestalten zum Ausdruck kommen, heute Erklärer sonderbarster Art finden. Das Kurioseste auf diesem Gebiete ist wohl jenes Büchlein ,,Orpheus\" von Salomon Reinach, das in vielen Kreisen Frankreichs in unserer Zeit ein gewisses Auf­sehen gemacht hat.",
      "Da wird alles das, woraus die Ideen der Demeter, des Orpheus' die Ideen anderer mythologischer Kreise ausgeflossen sem sollen, zurückgeführt auf rein materialistische Geschehnisse, und manchmal ist es urgrotesk, wie die historische Existenz dieser oder jener Gestalt abgeleitet wird, die - sagen wir - hinter dem Hermes oder dem Moses steckt, und in welch trivialer Weise diese Gestalten sozu­sagen aus freier Menschheitsdichtung, aus der Phantasie heraus zu erklären gesucht werden. Nach der Methode des Salomon Reinach würde es leicht sein, nach sechzig bis siebzig Jahren, das heisst wenn das äussere Gedächtnis an ihn ein wenig verwischt wäre, nachzu­weisen, dass es niemals einen solchen Reinach gegeben habe, sondern dass es nur die Volksdichtung ist, die die alte Idee vom Reineke Fuchs auf den Salomon Reinach übertragen hat.",
      "Das würde nach seiner Methode absolut möglich sein. So absurd ist das Ganze, was in diesem Büchlein ,,Orpheus\", wie in der Vorrede auseinander­gesetzt wird - ,,für die weitesten Kreise unserer gegenwärtigen Ge­bildeten, ja auch für die jüngsten Kreise\" geschrieben worden ist! ,,Für die jüngsten Kreise\", denn er betont, dass er alles vermieden habe - obwohl er nicht vermieden hat, die Idee der Demeter auf ein Schwein zurückzuführen -, was Anstoss erregen könnte bei jüngeren weiblichen Persönlichkeiten.",
      "Er verspricht aber, dass, wenn sein Buch den Einfluss gewinnt, den er erhofft, er dann für die Mamas eine besondere Auflage seines Büchleins schreiben wird, welche alles das enthalten soll, was man jetzt noch den Töchtern vorenthalten muss. So weit haben wir es also gebracht.",
      "Man möchte gerade die Anhänger der Geisteswissenschaft immer darauf hinweisen, dass es möglich ist, auf rein äussere Vernunfts-gründe hin das Walten geistiger Mächte, geistiger Kräfte durch Menschen bis in unser Jahrhundert herein wirklich zu beweisen; ganz abgesehen von der rein okkult-esoterischen Forschung, die uns",
      "hier hauptsächlich beschäftigen wird. Aber damit wir uns darüber verständigen, wie die Geisteswissenschaft eine gewisse Möglichkeit gewinnen kann, rein äusserlich das Walten übersinulicher Mächte in der Geschichte zu verteidigen, lassen Sie mich auf folgendes hin­weisen.",
      "Wer ein wenig Einblick gewinnt in die Entwicklung der modernen Menschheit, wie sie sich vollzogen hat etwa im 14., 15. bis ins 16. Jahrhundert hinüber, der wird wissen, dass von einer ganz un­endlich tiefen Bedeutung war, wie in diese neuzeitliche äussere Menschheitsentwicklung eine bestimmte Persönlichkeit historisch eingegriffen hat, von der man wirklich, ich möchte sagen, mit äusser­lichsten Gründen nachweisen kann, dass durch sie geistig-übersinn­liche Mächte gewirkt haben.",
      "Man kann nämlich die Frage aufwerfen, um ein klein wenig Licht hinzubreiten über okkulte Auffassung der Geschichte: Was wäre aus der Entwicklung des neueren Europa geworden, wenn im Beginne des 15. Jahrhunderts sich nicht hinein­gestellt hätte in die Entwicklung das Mädchen von Orleans, die Jung­frau von Orleans?",
      "Derjenige nämlich, welcher die Entwicklung dieser Zeit einmal auch nur ganz äusserlich ins Auge fasst, der muss sich sagen: Man streiche einmal die Taten der Jungfrau von Orleans hinweg aus dem geschichtlichen Werden, dann muss man nach dem­jenigen, was man rein nach äusseren geschichtlichen Forschungen wissen kann, sich klar sein: ohne das Wirken höherer übersinnlicher Mächte durch das Mädchen von Orleans hätte im i 5. Jahrhundert Frankreich, ja ganz Europa tatsächlich eine andere Gestalt bekommen müssen.",
      "Denn damals ging alles, was sich abspielte in den Willens-impulsen, in den Gehirnen der physischen Köpfr dahin, Europa sozusagen zu überziehen durch alle Staaten hindurch mit einer die Völkerindividualitäten ausstreichenden und auslöschenden allgemei­nen Staatsauffassung. Und unter deren Einfluss wäre ganz gewiss unendlich viel von dem unmöglich geworden, was sich in den letzten Jahrhunderten durch das Ineinanderspiel der europäischen Völker­individualitäten innerhalb Europas herausgebildet hat.",
      "Man denke sich einmal die Tat der Jungfrau von Orleans hinweg-gestrichen aus der Geschichte, man denke sich Frankreich seinem",
      "Schicksal überlassen, ohne dass sie eingegriffen hätte, man frage sich:",
      "Was wäre aus Frankreich ohne diese Tat geworden? Und dann be­denke man, welche Rolle Frankreich in den nachfolgenden Jahr-hunderten für das ganze Geistesleben der Menschheit gespielt hat! Und dazu stelle man die nicht hinwegzuleugnenden, sondern durch äussere Dokumente zu belegenden Tatsachen von der Sendung des Mädchens von Orleans! Man mache sich klar, dass dieses Mädchen mit einer wahrhaftig auch im Sinne ihrer Zeit nicht besonders hohen äus­seren Bildung plötzlich in einem Alter von noch nicht zwanzig Jahren im Herbst 1428 fühlt, wie zu ihr sprechen geistige Mächte der über­sinnlichen Welten, Mächte, denen sie allerdings die Formen zuerteilt, die ihr geläufig sind, so dass sie sie durch die Brille ihrer Vorstellungen sieht; aber das ist kein Einwand gegen die Realität dieser Mächte. Stellen Sie sich vor, dass sie weiss: übersinnliche Mächte lenken ihre Willenskraft nach einem ganz bestimmten Punkte hin - ich erzähle Ihnen zunächst von diesen Tatsachen nicht, was durch die Akasha­chronik erzählt werden kann, sondern nur das, was aktenmässig, rein historisch festgestellt ist.",
      "Wir wissen, dass dieses Mädchen von Orleans sich zunächst einem Verwandten geoffenbart hat, bei dem sie - man möchte fast sagen zufällig - Verständnis gefunden hat; dass sie nach mancherlei Um­wegen und Schwierigkeiten in das Hoflager des Königs Karl geführt wurde, der mit dem ganzen französischen Heerwesen sozusagen am Ende seines Witzes angelangt war; und wir wissen, dass sie, nachdem man ihr alles Erdenkliche in den Weg gelegt hatte, zuletzt unter einer ganzen Menge von Leuten, in die König Karl so hineingestellt war, dass er durchaus nicht für äussere Augen zu unterscheiden war, ihn richtig herausgefunden hat, indem sie kurzweg auf ihn losgegangen ist. Man weiss auch, dass sie ihm dazumal etwas anvertraut hat - er wollte sie dadurch prüfen -, wovon man sagen kann, dass nur er allein und die übersinnlichen Welten das Entsprechende gewusst haben. Und Sie wissen ja vielleicht aus der äusseren Geschichte, wie dann sie es war, die unter den fortwährenden Impulsen und unter dem fortwährenden Eindruck ihres starken Glaubens - man würde besser sagen, durch ihr unmittelbares Schauen - die Heere unter den",
      "grössten Schwierigkeiten zum Siege führte und den König zur Krönung.",
      "Wer hat dazumal eingegriffen in den Gang der historischen Ent­wicklung? Doch niemand anders als Angehörige höherer Hier­archien! Das Mädchen von Orleans war ein äusseres Werkzeug dieser Wesenheiten, und sie, diese Wesenheiten der höheren Hier­archien, haben die Taten der Geschichte gelenkt. Es mag ja sein, dass irgendein Verstand sich sagt: Hätte ich sie gelenkt, so hätte ich sie klüger gelenkt; weil er dieses oder jenes, was geschehen ist in dem Auftreten der Jungfrau von Orleans, seinem Denken nicht angemessen findet. Anhänger der Geisteswissenschaft sollen aber nicht Göttertaten durch Menschenverstand korrigieren wollen, was ja allerdings heute innerhalb unserer sogenannten Zivilisation überall vorkommt. Sehen Sie, es haben sich natürlich auch Leute gefunden, welche ganz im Sinne unserer heutigen Zeit die Geschichte der modernen Welt sozusagen entlasten wollten von den Taten der Jungfrau von Orleans. Und ein für unsere heutige Zeit charak­teristisches Werk nach dieser materialistischen Richtung hin hat Anatole France geschrieben. Man möchte eigentlich doch nur wissen, wie sich das materialistische Denken abfindet mit Mitteilungen, welche wahrhaftig - und ich rede immer noch von Dokumenten der äusseren Geschichte - recht gut begründet sind. So möchte ich, weil wir gerade hier an diesem Orte sind und ich manchmal gerne Rücksicht nehme auf lokale Verhältnisse, Ihnen anführen ein Dokument, auf das man sich schon einmal hier berufen hat.",
      "Die Stuttgarter wissen gewiss, dass hier an diesem Orte einmal ein bedeutender Evangelienforscher gelebt hat. Man braucht als Geisteswissenschafter durchaus nicht einverstanden zu sein mit dem auch mancherlei recht Gescheiten, das Gfrörer - so hiess der Evan­gelienforscher - in seiner Evangelienforschung dargeboten hat, und man kann ganz sicher sein, dass Gfrörer, wenn er hörte, was jetzt auf dem Gebiete der Geisteswissenschaft verkündet wird, diejenige Redensart gebrauchen würde, die er oftmals gebraucht hat für seine Gegner, die er mit seiner Starrköpfigkeit durchaus nicht immer leicht angelassen hat: die Redensart, dass diese Theosophen auch solche",
      "Leute seien, ,,bei denen es unter dem Hute nicht recht richtig ist\". Deshalb aber war doch dazumal die Zeit noch nicht gekommen, wo man sozusagen in rein materialistischer Weise über historische Do­kumente hinweggehen kann, wie man das heute macht, wenn diese historischen Dokumente Tatsachen betreffen, die unbequem sind, die augenscheinlich das Wirken lebendiger höherer Kräfte innerhalb unserer physischen Welt anzeigen. Und so möchte ich heute auch wiederum ein kleines Dokument zitieren, einen Brief, der in der ersten Hälfte des 19. Jahrhunderts veröffentlicht worden ist. Ich möchte Ihnen nur einige Stellen vorlesen, so wie sich dazumal zur Rechtfertigung seines Glaubens Gfrörer auf diesen Brief berufen hat. Ich möchte Ihnen eine Stelle aus einer Charakteristik der Jungfrau von Orleans vorlesen und Sie dann fragen, was eine solche lebendige Schilderung bedeutet.",
      "Nachdem der Schreiber dieses Briefes, auf den sich Gfrörer beruft, aufgezählt hat, was die Jungfrau von Orleans vollbracht hat, fährt er fort:",
      ",,Dieses und vieles andere hat die Jungfrau (von Orleans) voll­führt und mit Gottes Hilfe wird sie noch Grösseres verrichten. Das Mägdelein ist von anmutiger Schönheit und besitzt männliche Hal­tung, es spricht wenig und zeigt eine wunderbare Klugheit; in seinen Reden hat es eine gefällige, feine Stimme nach Frauenart. Es isst mässig, noch mässiger trinkt es Wein. An schönen Rossen und Waffen hat es sein Gefallen. Gewappnete und edle Männer liebt es sehr. Die Zusammenkunft und das Gespräch mit vielen ist der Jungfrau zu­wider; sie fliesst oft von Tränen über, liebt ein fröhliches Gesicht, erduldet unerhörte Arbeit, und in der Führung und Ertragung der Waffen ist sie so beharrlich, dass sie sechs Tage lang Tag und Nacht ohne Unterlass vollständig gewappnet bleibt. Sie spricht: Die Eng­lischen hätten kein Recht an Frankreich, und darum habe sie, wie sie sagt, Gott gesandt, auf dass sie jene austreibe und überwinde, jedoch erst nach vorhergeschehener Mahnung. Dem König erweist sie die höchste Verehrung; sie sagt, er sei von Gott geliebt und in besonderem Schutze, weshalb er auch erhalten werden würde. Vom Herzog von Orleans, Eurem Neffen, sagt sie, er werde auf wunderbare",
      "Weise befreit werden, doch erst, nachdem zuvor eine Mahnung an die Englischen, die ihn gefangen halten, zu seiner Befreiung ge­schehen sein werde.",
      "Und damit ich, erlauchter Fürst, meinem Bericht ein Ende mache:",
      "Noch Wunderbareres geschieht und ist geschehen, als ich Euch schreiben oder mit Worten ausdrücken kann. Während ich dieses schreibe, ist die genannte Jungfrau schon nach der Gegend der Stadt Rheims in Champagne gezogen, wohin der König eilends zu seiner Salbung und Krönung unter Gottes Beistand aufgebrochen ist. Erlauchtester und Grossmächtigster Fürst und mein höchst zu ver-ehrender Herr! ich empfrhle mich Euch sehr demütig, indem ich den Allerhöchsten bitte, dass er Euch behüte und Eure Wünsche erfülle.",
      "Geschrieben Biteromis am 21. Tage des Monats Junius.",
      "Euer demütiger Diener",
      "Herr von Bonlaninth, Rat und Kämmerer des Königs",
      "der Franzosen und des Herrn Herzogs von Orleans,",
      "Seneschal des Königs, gebürtig aus Berry.\"",
      "Einer, der das Mädchen kennt, schreibt aus unmittelbarer Nähe des Königs diesen Brief. Es ist in der Tat dann erstaunlich, wenn aus rein okkulten Gründen und Beweismitteln heraus man alle diese Sachen wiederfinden muss - denn sie sind auffindbar in der Akasha-Chronik - und sieht, wie gerade in solchen Fällen man auch äusserlich geschichtliche Dokumente durchaus beibringen kann. Kurz, es er­scheint einem fast wahnsinnig, an dem zu zweifeln, was durch die Jungfrau von Orleans wirkte. Und wenn wir dann noch in Betracht ziehen, dass durch ihre Taten die ganze Geschichte der neueren Zeit ein anderes Gesicht bekommen hat, so gibt uns das ein Recht zu sagen, dass wir hier unmittelbar hereinwirken sehen, äusserlich dokumentarisch belegbar, die übersinnliche Welt. Wenn dann der Geistesforscher weitergeht und Umschau hält auf seine Art nach dem eigentlichen Inspirator, der auf die Jungfrau von Orleans gewirkt hat, dann findet er, durchforschend die aufeinanderfolgenden Zeiten, etwas ganz Merkwürdiges. Er findet, wie derselbe Geist, der durch",
      "die Jungfrau von Orleans als sein Werkzeug dazumal gewirkt hat, sozusagen in ganz anderer Form, in ganz anderer Art inspirierend auch auf eine andere Persönlichkeit gewirkt hat, die als Philosoph am Hofe Karls des Kahlen lebte: Scotus Erigena, durch dessen philosophisch-theologische Ideen in einem frühen Zeitraum Europa so tief beeinflusst worden ist. Und so sehen wir, dass dieselben Mächte in verschiedenen Epochen in verschiedener Art durch Menschen als durch ihre Werkzeuge wirken; dass I(ontinuität, fortlaufendes Geschehen ist in dem, was wir Geschichte nennen.",
      "Nun habe ich Ihnen gestern gezeigt, wie in einem bedeutsamen Mythos aus der babylonisch-chaldäischen Zeit hingewiesen wird auf das Hereinwirken der geistigen Welten auf Menschen, von denen vieles im Verlauf der Geschichte abhing für den dritten unserer nach-atlantischen Zeiträume, wie den Verlauf des ganzen geschichtlichen Werdens im alten Chaldäa' im alten Babylonien. Wir müssen aber allerdings jetzt auch vom Standpunkt der okkulten Wissenschaft die beiden Persönlichkeiten betrachten, die sich hinter den sagen­haften Namen Gilgamesch und Eabani verbergen. Okkult-historisch haben wir in ihnen Persönlichkeiten zu sehen, die am Ausgangspunkt dessen stehen, was wir babylonische, was wir chaldäische Kultur nennen. Was von ihnen hat kommen können an Impulsen, das finden wir wieder in der Entwicklung der eigentlich geistigen Kultur des alten Babyloniens und Chaldäas. Nun war Gilgamesch eine solche Persönlichkeit, welche viele Inkarnationen in der Art hinter sich hatte, dass man gewissermassen diese Persönlichkeit als eine alte Seele innerhalb der Menschheitsentwicklung bezeichnen kann.",
      "Sie wissen ja aus der Darstellung in meiner ,,Geheimwissenschaft\", dass während des lemurischen Zeitraums der Erdentwicklung nur ganz wenige Menschen sozusagen die Ereignisse der Erdentwicklung auf der Erde selbst überdauert haben, dass nur wenige auf der Erde blieben während des lemurischen Zeitraums; dass die Mehrzahl der Seelen, bevor die eigentliche Gefahr der Mumifizierung alles Mensch­lichen begann, sich von der Erde hinweghob nach anderen Planeten und weiterlebte auf Mars, Saturn, Venus, Jupiter und so weiter; dass dann vom Ende des lemurischen Zeitraums an und während des",
      "atlantischen Zeitraums nach und nach diese Seelen wieder herunter­kamen auf die Erde, um unter den veränderten irdischen Verhält­nissen sich in irdischen Leibern zu verkörpern und in immer neuen Inkarnationen zu erscheinen. Da haben wir also solche Seelen, die verhältnismässig früh heruntergekommen sind aus der Planetenwelt, und andere, die spät, erst in späten Zeiträumen der atlantischen Ent­wicklung niedergestiegen sind. Die ersteren Seelen, die also früher heruntergekommen sind, haben mehr Inkarnationen innerhalb der Erde hinter sich als die später herniedergestiegenen, und diese können wir daher im Gegensatz zu den ersteren, jüngere Seelen nennen, Seelen, die also weniger in sich aufgenommen haben.",
      "Eine alte Seele war diejenige Individualität, die sich hinter dem Namen Gilgamesch verbirgt, und eine jüngere, die in Eabani ver­körpert war am Ausgangspunkte der babylonischen Kultur. Ja, in bezug auf dieses Jüngere oder Ältere der menschlichen Seelen zeigt sich - man möchte fast sagen selbst zur Überraschung des Okkul­tisten - etwas sehr Merkwürdiges.",
      "Wenn zum Beispiel irgend jemand heute es so weit gebracht hat, dass er die Wahrheiten der Geistes­wissenschaft ein wenig zugibt, sonst aber noch immer an den Vor-urteilen und Werturteilen der äusseren Welt hängt, dann wird es ihm ja plausibel erscheinen, dass zum Beispiel Philosophen- oder Ge­lehrtenseelen unserer heutigen Zeit zu den älteren Seelen gerechnet werden müssen. Die okkulte Forschung ergibt das gerade Gegenteil, so sonderbar es klingt; und es ist für den Okkultisten selbst über­raschend, dass zum Beispiel in Kant eine junge Seele lebte.",
      "Ja, die Tatsachen sagen es... da ist nichts dagegen zu machen. Und man könnte nun darauf hinweisen, dass die jüngeren Seelen sich allerdings in der Mehrzahl in den farbigen Rassen verkörpern, dass also die farbigen Rassen, namentlich die Negerrasse, vorzugsweise jüngere Seelen zur Verkörperung bringen.",
      "Aber gerade das Eigentümliche jener menschlichen Denkungsart, die sich in Gelehrsamkeit, in der heutigen materialistischen Wissenschaft auslebt, die bedingt jüngere Seelen. Und es ist sogar nachweisbar, dass bei mancher Persönlich­keit, bei der man es gar nicht voraussetzen würde, die vorhergehende Inkarnation durchaus bei den Wilden liegt.",
      "Ja, das sagen wieder die",
      "Tatsachen! Das alles muss durchaus festgehalten werden, es ist so. Das nimmt natürlich den Urteilen, die wir über unsere Umwelt haben, nichts von ihrer Bedeutung, nichts von ihrem Werte; dennoch muss es erfasst werden zum Gesamtverständnis dessen, um was es sich handelt. In diesem Sinne haben wir es mit Eabani im alten Baby­lonien zu tun mit einer jungen Seele, in Gilgamesch mit einer alten Seele. Eine solche alte Seele, die wird ihrer ganzen Natur nach früh erfassen, was gewissermassen nicht nur Kulturelement, Kulturfaktor der Gegenwart ist, sondern was als Kultureinschlag in die Gegenwart hereinfällt und weit hinausblicken lässt in die Perspektive der Zukunft.",
      "Es mag sich ja allerdings mancher dagegen verwahren, wenn man ihm plausibel machen würde, dass die oftmals von ihm so inferior gehaltenen Theosophen zumeist ältere Seelen sind als diejenigen, die akademische Vorträge halten. Aber die Forschung zeigt es; und wenn auch die geistige Forschung nicht etwa dazu missbraucht werden soll, die Werturteile umaustossen und Spott zu treiben mit dem, was einmal der Einschlag unserer Kultur ist, so muss man doch der Wahr­heit streng ins Auge schauen. So war denn Gilgamesch eine Persön­lichkeit, die es vermöge ihrer Seelenkonstitution mit demjenigen hielt, was zu den fortgeschrittensten Geisteselementen und Geistes-faktoren der damaligen Zeit gehörte, was für die damalige Zeit weit hineinleuchtete in die Zukunft, und was auch damals nur erreicht werden konnte dadurch, dass eine solche Persönlichkeit eine Art Initiation durchmachte. In einer gewissen Initiation, in einer Mit­teilung dessen, was man nur durch die Initiation empfangen kann, sollte dem Gilgamesch gegeben werden, was ihn befähigte, Fermente für die babylonische Kultur zu liefern. Also eine Einweihung sollte er bis zu einem gewissen Grade durchmachen.",
      "Betrachten wir ihn einmal, diesen Gilgamesch, wie er sich in die Menschheitsentwicklung hineinstellen musste vor dieser Einweihung. Da war er ein Mensch des dritten nachatlantischen Zeitraumes. In diesem Zeitraume aber war für das natürliche menschliche Hellsehen, für das, was der Mensch konnte und vermochte durch seine natür­lichen Kräfte, dazumal schon die Ahenddämmerung gekommen. Das war nicht mehr in dem Grade vorhanden, dass die Menschen in",
      "grösserer Anzahl zurückschauen konnten in ihre früheren Inkarna­tionen. Wenn wir weiter zurückgehen in den zweiten, in den ersten nachatiantischen Zeitraum, da würden wir finden, dass die Mehrzahl der Menschen auf unserer Erde noch zurückschauen konnten in ihre früheren Inkarnationen, in das Verfliessen ihres Seeleniebens vor ihrer gegenwärtigen Geburt.",
      "Aber das war allmählich verloren worden. Bei Gilgamesch war die Sache so, dass von vornherein diejenige Wesenheit, die sich durch ihn offenbaren sollte und die sich nur offen­baren konnte durch ihn, indem sie ihn nach und nach zu einer Art Initiation führte, dass diese Wesenheit sozusagen immer ihre Hand über ihn hielt.",
      "Sie stellte ihn hin auf den Platz, durch den er seine eigene Stellung in der Weltgeschichte beurteilen lernte. Es wurde sozusagen durch Ereignisse übersinnlicher Art, welche uns in dem Mythos, den ich gestern angeführt habe, in Bildern entgegentreten, ihm ein Freund an die Seite gegeben, ein Freund, dessen Barbarei, dessen Unzivilisiertheit uns dadurch angedeutet wird, dass er halb tierisch an äusserer Gestalt ist.",
      "Es wird gesagt, dass dieser Freund Tierfelle am Leibe trug, das heisst, dass er sozusagen noch wie die Menschen des Urzustandes behaart war, dass seine Seele so jung war, dass sie einen Leib sich aufbaute, der den Menschen noch in ver­wilderter Gestalt zeigt. So hatte Gilgamesch, der fortgeschrittenere, in Eabani einen Menschen neben sich, der durch seine junge Seele und seine dadurch bedingte Leibesorganisation noch ein altes Hell­sehen hatte.",
      "Um sich selber zu orientieren, war ihm dieser Freund beigegeben worden. Mit Hilfe dieses Freundes gelang es ihm dann, gewisse Dinge auszuführen, wie - sagen wir - die Zurückführung jener geistigen Macht, die uns wiederum im Mythos unter dem Bilde der Stadtgöttin von Erek, Ischtar, dargestellt wird.",
      "Ich habe Ihnen gesagt, dass die Stadtgöttin gestohlen worden war von der Nachbar­stadt und dass daher die beiden, Gilgamesch und Eabani, Krieg begannen gegen die Nachbarstadt, den König dieser Nachbarstadt besiegten und die Stadtgöttin wieder zurückführten.",
      "Wenn man solche Dinge, die uns in diesen alten Mythen dargestellt werden, richtig historisch verstehen will, dann muss man schon auf die okkulten Hintergründe der Sache eingehen. Es verbirgt sich ja",
      "hinter diesem Rauhe der Stadtgöttin etwas Ähnliches wie hinter dem Rauhe der Helena, die nach Troja entführt wird durch Paris. Wir müssen uns darüber klar sein, dass es durchaus auf guten Gründen beruht, was in meiner kleinen Schrift ,,Blut ist ein ganz besonderer Saft\"\" ausgeführt ist.",
      "Da werden Sie hingewiesen darauf, dass in den Völkern der alten Zeit ein gewisses Gesamtbewusstsein vorhanden war, dass der Mensch nicht nur sein persönliches Ich empfand inner­halb seiner Haut, sondern dass er sich als ein Glied des Stammes, der Stadtgemeinschaft empfand. So wie die einzelne menschliche Seele als Zentralfaktor für unsere Finger, Zehen, Hände, Beine, die zusammengehören, für unseren ganzen Organismus empfunden wird, so fühlte sich der Mensch in alten Zeiten gegenüber der Gruppen­seele wie ein Glied, dem er zugehörte.",
      "So etwas war in älteren Zeiten noch in den alten Stadtgemeinden, selbst in Griechenland, vorhanden. Ein gemeinschaftlicher Geist, eine Volks-lchheit, eine Stammes­Ichheit, lebte und webte durch die einzelnen Volkspersönlichkeiten hindurch.",
      "Aber dasjenige, was zum menschlichen Bewusstsein kom­men konnte von einer solchen gemeinsamen Ichheit, das musste gewissermassen in Mysterien, in geheimen Tempelstätten verwaltet werden. Da waren die alten Mysterienpriester und verwalteten die gemeinsamen spirituellen Angelegenheiten einer Stadt oder eines Stammes.",
      "Und man spricht nicht bloss figürlich, sondern in einer gewissen Weise real und richtig, wenn man sagt, eine solche Tempel­stätte war wirklich wie eine Wohnung für das Stadt-Ich, für die Gruppenseele. Da hatte sie ihren zentralen Wohnsitz und die Tempel-priester waren ihre Diener.",
      "Sie waren diejenigen, welche die Auf­träge dieser Gruppenseele durch Inspiration empfingen - was man Orakel nannte - und sie hinaustrugen in die Welt, damit dieses oder jenes geschehe; denn die Orakel sind ja damals durchaus in dem Sinne aufzufassen, den ich Ihnen jetzt charakterisiert habe.",
      "Nun war die Verwaltung solcher Tempelstätten mit gewissen Geheimnissen verbunden, und viele Kämpfe in den alten Zeiten spielten sich so ab, dass die Tempelpriester einer Stadt von der Nach­barstadt als Gefangene hinweggeschleppt wurden, dass also sozusagen mit den Tempelpriestern die wichtigsten Geheimnisse einer Stadt",
      "weggeschleppt wurden in die Nachbarstadt. Da haben Sie die reale Tatsache, welche dem Bilde entspricht, dass die Stadtgöttin Ischtar, die Volksseele von Erek, geraubt wird durch die Nachbarstadt. Die Tempeipriester, die Verwalter der Tempelgeheinmisse, waren zu Gefangenen gemacht worden, weil die Nachbarstadt hoffte, auf diese Weise in den Besitz der heiligen Geheimnisse und damit der Macht der betreffenden Stadt zu kommen. Das ist der reale Hinter­grund.",
      "Und solche Dinge konnte Gilgamesch in der Seelenverfassung, in der er sich zunächst befand, nicht selber wahrnehmen, weil er nicht hineinsah in diese Zusammenhänge; aber eine jüngere Seele konnte ihm sozusagen wie der hellseherische Sinn dienen, der ihm half, den Tempelschatz für seine Vaterstadt zurückzuerobern. Da wurde ihm, dem Gilgamesch, so recht zum Bewusstsein gebracht, dass es im menschlichen Leben gerade in Übergangszeiten so etwas gibt, wie es in der Legende von dem Blinden und dem Lahmen dar­gestellt wird, von denen jeder einzelne hilflos ist, die aber zusammen sich weiterbringen, indem der Blinde den Lahmen auf die Schulter nimmt und der Lahme dem Blinden sein Sehvermögen leiht.",
      "Da sehen wir bei Gilgamesch und Eabani ins Spirituelle umgesetzt ein solches Zusammenwirken von Menschen ganz verschiedener Begabung. Wir treffen das insbesondere in den historischen Tatsachen der älteren Zeiten auf Schritt und Tritt an.",
      "Und es ist wichtig, so etwas zu ver­stehen, denn dann erst kann man verstehen, warum uns so oft in Mythen und Sagen Freunde, die gemeinsam etwas zu vollbringen haben, vorgeführt werden: Freunde, die dann gewöhnlich so un­gleich sind in bezug auf ihre Seelenverfassung, wie es eben Gilga­mesch und Eabani waren. Das aber, was Gilgamesch ausserdem durch Eabani, seinen Freund, sich für seine Seele erobern konnte, das war, dass er gleichsam von Eabani angesteckt wurde mit einer eigenen hellseherischen Kraft, so dass er in gewisser Weise zurückschauen konnte in seine eigenen früheren Inkarnationen.",
      "So lernte Gilgamesch wirklich von Eabani das Zurückschauen in frühere Inkarnationen. Das war etwas, was schon ausserhalb der normalen Fähigkeiten des Gilgamesch lag. Und nun stellen wir uns lebendig vor, wie Gilgamesch",
      "beeinflusst gewesen sein mochte von diesem Zurückschauen in seine früheren Inkarnationen.",
      "Was konnte er sich etwa sagen von dem Tage an, da in seiner Seele die Möglichkeit auftauchte, zurückzublicken in dasjenige, was seine Seele durchlebt hatte in früherer Inkarnation? Das befremdete ihn zunächst. Er konnte sich nicht recht in seine eigene Wesenheit hinein­finden, wie sie in früheren Inkarnationen war; er erkannte sich sozu­sagen nicht so recht wieder. So würde es ja überhaupt den Menschen gehen, wenn sie anfingen, in ihre früheren Inkarnationen zurückzu­blicken. Da würde es meist anders ausschauen als in den Einbildungen, die immer wieder und wieder auftreten, wenn gesagt wird, irgendein Mensch sei eine Reinkarnation von dieser oder jener Persönlichkeit. Da kann es einem ja passieren, dass man irgendeine Persönlichkeit findet, die eine ganze Reihe von historischen, grossen Namen als diejenigen ihrer vorhergehenden Inkarnationen anführt... Es soll sogar ganze Gruppen von Menschen geben, die davon überzeugt sind, dass es unter dem Range einer Königin oder einer Prinzessin nichts in ihren früheren Inkarnationen gibt! - In diesen Dingen, mit denen es so ernst stehen sollte, darf eben keine Phantasie obwalten damit darf kein Unfug getrieben werden.",
      "Nun, derjenige, der so wie Gilgamesch damals zunächst auf die Reihenfolge seiner Inkarnationen zurückblickt, der kann wirklich zuweilen auch überrascht sein. Er blickte ja zurück auf Inkarnationen, da er noch hineinverwoben war in allerlei Zusammenhänge, die durch die Gruppenseelenhaftigkeit gegeben waren. Er hatte sich allerdings in gewisser Weise für seine Person herausgearbeitet aus diesen Zu­sammenhängen, er hatte auch erst durch Eabani den ganzen Wert erfahren können dessen, was durch die Stadtgöttin in der Mythe symbolisiert wird. Da er aber zurückschaute, da gefiel ihm manches nicht in seinen früheren Inkarnationen, da konnte er sich sagen: das ist doch nicht nach meinem Geschmack. Da fand er, dass zum Beispiel seine Seele in den Inkarnationen ganz besondere Freundschaften, ganz besondere menschliche Zusammenhänge gehabt hatte, deren er sich jetzt hätte schämen mögen. Da kam denn heraus, was uns dar­gestellt wird im Mythos, dass er demgegenüber, was ihm auf dem",
      "Umwege durch Eabani die Stadtgöttin offenbart hatte, anfing, in gewisser Weise zu schelten, dass er Vorwürfe machte seiner Seele. Im Mythos wird angedeutet, dass er der Göttin Vorwürfe machte über ihre Bekanntschaften, denn er wurde eifersüchtig auf solche Bekanntschaften.",
      "Da blickte er sozusagen auf den Horizont seiner Seele und die Schmungen standen so lebendig vor ihm, wie Menschen um einen anderen herumstehen in der äusseren physischen Welt, gegenüber denen man diese oder jene Sympathie oder Antipathie empfindet. Und in alledem, was nun Gilgamesch der Stadtgöttin an Vorwürfen macht, erkennen wir, dass er eigentlich mit demjenigen redet, was auf dem Grunde seiner Seele sich abspielt.",
      "Wenn uns also gesagt wird zum Beispiel, dass er der Stadtgöttin den Vorwurf machte, dass sie vorher Bekanntschaft gehabt hätte mit irgendeinem Menschen, der da in der Mythe Ischulanu genannt wird, so bedeutet das nichts anderes, als dass seine eigene Bekanntschaft mit einem gewissen Menschen, der der Gärtner seines Herrn in der vorher­gehenden Jnkarnation war, ihm nicht gefiel. Also dasjenige, was sich in der Seele des Gilgamesch abspielte, und wodurch er eigentlich erst jene innere Gedrungenheit, jene innere Erfülltheit seiner Seele erhielt, die er brauchte, als er der Inaugurator der babylonischen Kultur werden sollte - das alles wird uns dargestellt in dem Zurückkommen zu einer gewissen Hellsichtigkeit, in dem Hinaufsteigen in übersinn­liche Welten, was ihm, weil er eine alte Seele war, in gewisser Be­ziehung schon verloren war.",
      "Das wird uns im Mythos dargestellt.",
      "Und dann sollte er eine Art von Einweihung durchmachen da­durch, dass er zurückgeführt wurde zu jener Art von Anschauung, die seine eigene Seele während der atlantischen Inkarnationen hatte. Was uns nun der Mythos darstellt als die See- und Irrfahrten des Gilgamesch nach dem Westen, das ist nichts anderes als die innere Initiationsfahrt seiner Seele, durch die sie hinauffährt auf geistige Höhen, auf denen sie wahrnehmen kann, was um sie herum war in der alten atlantischen Zeit, da die Seele noch hellsichtig in die geistige Welt hineinschaute. Daher erzählt der Mythos, dass Gilgamesch auf dieser seiner spirituellen Fahrt zusammengebracht wurde mit der grossen atlantischen Herrscherpersönlichkeit Xisuthros. Das war eine",
      "Persönlichkeit, welche gewissen höheren Hierarchien angehörte und während der atlantischen Zeit in den Regionen der Menschheit lebte, seither aber dieser Menschheit entrückt war und in höheren Gebieten des Daseins wohnte. Diese Persönlichkeit sollte er, der Gilgamesch, kenneniernen, um aus der Anschauung ihrer Wesenheit dasjenige zu gewinnen, was notwendig war, um zu wissen, wie die Seelen sind, wenn sie hineinschauen können in die geistigen Welten.",
      "So sollte er wiederum hinaufgeführt werden in die spirituellen Sphären da­durch, dass er zurückgeführt wurde in seiner Seele bis in die atlanti­schen Zeiten hinein. Und wenn ihm aufgetragen wird, er soll sieben Nächte und sechs Tage nicht schlafen, so bedeutet das nichts anderes als eine Übung, durch welche die Seele gestaltet werden sollte, um völlig einzudringen in die entsprechenden, eben charakterisierten geistigen Regionen.",
      "Wenn uns nun gesagt wird, dass er dies nicht aushielt, dann bedeutet das wiederum etwas sehr Wichtiges: es bedeutet, dass Gilgamesch uns dargestellt werden soll als eine Persön­lichkeit, die hart an den Rand der Initiation gebracht wird, die gleich­sam durch die Pforte der Initiation hineinschauen sollte in die geistigen Geheimnisse, die aber durch die ganze Art der Zeitverhältnisse doch nicht in alle Tiefen dringen konnte. Kurz, es soll gesagt werden, dass der Inaugurator, der Einrichter der babylonischen Kultur gewisser­massen an der Pforte der Initiation stehengeblieben ist, dass er nicht ganz klar in die höheren geistigen Welten hineinschauen konnte, und dass er deshalb der babylonischen Kultur so recht das Gepräge gegeben hat, welches ein Abdruck ist von einem blossen Hinein­schauen in die Initiationsgeheimnisse.",
      "Wir werden nun sehen, wie diese äussere babylonische Kultur tat­sächlich so ist, dass sie rechtfertigt, was eben gesagt worden ist. Während uns zum Beispiel alles darauf hinweist, dass wir in Hermes eine Persönlichkeit vor uns haben, welche tief, tief hineinschaute in die heiligsten Geheimnisse der Initiation und deshalb der grosse Initiator der ägyptischen Kultur werden konnte, so müssen wir sagen, dass die äussere babylonische Kultur in einer Weise zubereitet worden ist, wie wir es eben charakterisiert haben: nämlich durch eine führende Persönlichkeit, die in ihrer Seele alle diejenigen Eigenschaften hatte,",
      "die sich entwickeln, wenn man nicht ganz in das Innerste der heiligen Geheimnisse eindringt. Deshalb haben wir in der Tat im alten Baby-ionien die historische Entwicklung so, dass wir deutlich nebeneinan­der gehend einen äusseren Kulturverlauf und einen esoterisch-inneren haben. Während im ägyptischen Leben diese beiden mehr ineinander-spielen, fallen sie gewissermassen in der alten babylonischen Kultur durchaus auseinander. Und innerhalb dessen, was wir als die baby-ionische Kultur anzusehen haben, wie sie inauguriert worden ist durch Gilgamesch, lebte dasjenige, was in den heiligsten, verborgensten Mysterien der Chaldäer liegt.",
      "Diese Initiierten der Mysterien waren allerdings in das Innerste eingeweiht, aber das zog sich doch nur wie ein kleiner Strom durch die äussere Kultur hindurch. Diese äussere Kultur war ein Ergebnis der Impulse des Gilgamesch.",
      "Nun hat sich uns ja aus all diesen Be­trachtungen ergeben, dass Gilgamesch als Persönlichkeit im Grunde genommen nicht so weit war, dass er eine völlige Einweihung hätte erleben können. Gerade dadurch aber, dass er nicht in der Zeit, in der er wirkte, sozusagen seine eigenen persönlichen Impulse auslebte, das, was seine Kraft war, der Welt mitteilte, war er ganz besonders dazu imstande, durch sich durchwirken zu lassen eine der geistigen Wesenheiten, die wir zu der Klasse der Feuergeister, also derArchange­loi, der Erzengel, rechnen.",
      "Solch eine Wesenheit wirkte durch Gilga­mesch, und die Ordnung der babylonischen Verhältnisse, die treiben­den Kräfte derselben, für die Gilgamesch das Werkzeug war, haben wir bei einem solchen Feuergeist zu suchen. So haben wir uns diesen Gilgamesch so recht vorzustellen unter einem Bilde, das uns geben konnte das Symbolum des alten Kentauren.",
      "Solche alten Symbole, sie entsprechen mehr der Wirklichkeit als man gewöhnlich denkt. Ein Kentaur, halb Tier, halb Mensch, sollte immer darstellen, wie in den mächtigeren Menschen der alten Zeiten wirklich in gewisser Weise auseinanderfiel das höchste spirituelle Menschentum und das­jenige, was die einzelnen Persönlichkeiten mit der tierischen Organi­sation verband.",
      "Wie ein Kentaur, so wirkte dieser Gilgamesch auf diejenigen, die ihn beurteilen konnten, und so wirkt er heute noch auf diejenigen, die ihn beurteilen können.",
      "Es ist sehr merkwürdig, dass gerade dieses Bild des Kentauren heute wiederum auftaucht auf dem Felde des modernen naturwissen­schaftlichen Denkens. Da ist jüngst ein Buch erschienen, das ganz auf naturwissenschaftliche Tatsachen fussen will, das aber doch in gewisser Weise vorurteilslos mit diesen Tatsachen umgeht und daher nicht so dilettantisch, so sinnlos alles durcheinanderwirft' wie es die­jenigen tun, die sich Monisten nennen.",
      "Es sucht der Verfasser wirklich den Menschen zu verstehen, wie er als selbständige seelisch-geistige Wesenheit der physischen Leibesorganisation gegenübertritt. Und da kommt ein auf naturwissenschaftliche Unterlagen sich stützender Mensch zu einem eigentümlichen Bild.",
      "Er hat ganz gewiss nicht an den Kentauren gedacht, als er sich dieses Bild ausmalte, aber er sagt zu dem, was sich aus naturwissenschaftlichen Vorstellungen ergibt über die Beziehungen der Seele zum Leibe: Das lässt sich vergleichen mit dem Reiten des Reiters auf dem Pferde. Man kann gar nicht anders sich vorstellen, wozu die wirklich verstandenen naturwissenschaft­lichen Tatsachen zwingen, als dass man sagt: Selbständig ist die Seele, die den Leib als Werkzeug benutzt wie der Reiter sein Pferd. - Der Kentaur ist wieder da, die Dinge werden tatsächlich schnell gehen, und ehe es sich die Menschen vermeinen, werden geisteswissenschaft­liche Vorstellungen unter dem Zwange gerade naturwissenschaftlicher Tatsachen sich in unsere Zeitgenossen einieben müssen.",
      "Denn noch nicht lange ist es her, da hatte ich mit einem Philosophen gesprochen, der viel auf materialistische Vorstellungen hielt und aus seinen ma­terialistischen Vorstellungen heraus mir sagte: ,,Das Bild des Kentau-ren ist natürlich so entstanden: Die alten Bewohner Griecheniands sahen gewisse Völkerschaften auf ihren Pferden vom Norden kom­men, und da es meistens neblig war, so hatten sie die Vorstellung, dass Reiter und Pferd eine einzige Gestalt seien. In ihrem Aberglauben konnten sie sich das leicht einbilden.\"",
      "In der Tat eine recht einfache Vorstellung, wenig philosophisch vielleicht, aber doch recht einfach! Diese Vorstellung des Kentauren, die nicht dadurch entstanden ist, dass die Griechen nicht haben unter­scheiden können den Reiter von seinem Pferd, sondern die dadurch entstanden ist, dass die älteren Völker wirklich die geistige Wesenheit",
      "des Menschen selbständig zu der physischen Natur haben denken müssen - diese Vorstellung taucht wieder auf in unserer Zeit, ganz selbständig aus naturwissenschaftlichen Vorstellungen heraus. So müssen wir sagen, wir sind heute schon trotz aller materialistischen Vorstellungen auf dem Wege, dass selbst der Materialismus, wenn er nur auf Tatsachen sich stützen will, nach und nach zu dem hinführt, was die Geisteswissenschaft aus ihren okkulten Quellen heraus zu sagen hat.",
      "Wollen wir aber eine solche Gestalt wie Gilgamesch, die ja auch der äusseren Forschung jetzt schon nahegetreten ist, so wie wir das für unsere Betrachtungen tun müssen, an die Spitze der okkulten Betrachtung stellen, dann müssen wir uns klar sein, dass wir es da zu tun haben mit einem Hereinwirken eines Wesens der höheren geistigen Hierarchien. So dass, wenn wir eigentlich jeden Menschen in bezug auf seine Geistigkeit hin im Bild des Kentauren anschauen müssen, wir bei einem solchen Menschen, der so wirkt wie Gilgamesch, noch insbesondere annehmen müssen, dass das Geistige des Kentauren dirigiert wird von höheren Mächten, die ihre Kräfte hereinsenden in den Fortschritt der Menschheit.",
      "Und wir werden sehen, wenn wir noch weiter hinaufgehen in der Geschichte, dass sich uns das noch deutlicher darstellen wird. Wir werden weiter sehen, wie sich das dann modifiziert bis in unsere Gegenwart herein und wie geistige Kräfte immer andere Gestalten annehmen, wenn sie durch Menschen wirken, je mehr wir in unsere unmittelbare Gegen­wart hereinkommen."
    ],
    "sentences": [
      [
        "Es ist gestern einleitend zunächst darauf aufmerksam gemacht worden, wie wir gewisse ältere geschichtliche Ereignisse der Mensch­heit nur dann richtig verstehen können, wenn wir nicht bloss auf die Kräfte und Fähigkeiten der Persönlichkeiten selbst blicken, sondern wenn wir voraussetzen, dass durch die betreffenden Persöniichkeiten, wie durch Werkzeuge hindurch, Wesenheiten wirken, die sozusagen ihre Taten aus höheren Welten herunterströmen lassen in unsere Welt.",
        "Wir müssen uns vorstellen, dass diese Wesenheiten hier in unserer Welt nicht unmittelbar angreifen können an unsere physischen Dinge, bei unseren physischen Tatsachen, weil sie wegen ihrer gegen­wärtigen Entwicklungsstufe sich nicht in einem physischen Leibe verkörpern können, der seine Elemente aus unserer physischen Welt nimmt.",
        "Wollen sie daher wirken innerhalb unserer physischen Welt, dann müssen sie sich des physischen Menschen bedienen, seiner Hand, aber auch seines Verstandes, seiner Auffassungsfähigkeiten.",
        "Wir finden den Einfluss und die Einwirkung solcher Wesenheiten der höheren Welten um so deutlicher ausgeprägt, je weiter wir zurück-gehen in den Zeiten der Menschheitsentwicklung.",
        "Man darf aber nicht etwa glauben, dass dieses Herunterströmen von Kräften und Wir­kungsweisen aus den höheren Welten in die physische Welt durch Menschen bis in unsere Zeit herein jemals aufgehört habe."
      ],
      [
        "Für den Geisteswissenschafter, der, wie wir es seit Jahren nun schon entfalten konnten, in sich aufgenommen hat, was unser Emp­finden und unser Vorstellen hinführt zu der Voraussetzung der höhe­ren Welten, für den wird ja eine solche Tatsache, wie sie eben charak­terisiert worden ist, gewiss von vorneherein etwas Verständliches haben, denn er ist gewohnt, sozusagen die Verbindungsfäden immer"
      ],
      [
        "zu ziehen, die unsere Erkenntnis, unser Denken, unseren Willen mit den Wesenheiten der höheren Hierarchien verknüpfen.",
        "Aber der Geisteswissenschafter kommt ja zuweilen auch in die Lage, sich wehren zu müssen gegenüber den materialistischen Vorstellungen, die nun schon einmal in unserer Gegenwart vorhanden sind; gegen­über den Vorstellungen, die es den Menschen, die der spirituellen Entwicklung fernestehen, unmöglich machen, irgendwie auch nur einzugehen auf das, was über das Herunterwirken höherer Welten in unsere physische Welt gesagt werden muss."
      ],
      [
        "In unserer Zeit gehört es ja im Grunde genommen schon zu den veralteten Anschauungen, wenn man nur von dem Walten abstrakter Ideen innerhalb der Menschheitsereignisse, innerhalb der Geschichte spricht.",
        "Schon das gilt heute manchen Menschen für etwas ganz Unerlaubtes gegenüber wahrer Wissenschaftlichkeit, wenn man davon spricht, dass gewisse Ideen, abstrakte Ideen, die eigentlich im Grunde doch nur in unserem Verstande leben können, dass diese sich ausleben in den aufeinanderfolgenden Epochen der Geschichte."
      ],
      [
        "Einen letzten Schein sozusagen von Glauben an solche abstrakte Ideen wenigstens -von denen man allerdings nicht begreifen kann, wie sie wirken sollen, da es doch abstrakte Ideen sind! -, einen gewissen letzten Schein von Glauben an solche abstrakte Ideen hat ja im 19.",
        "Jahrhundert noch selbst die Geschichtsschreibung des Ranke gehabt."
      ],
      [
        "Aber auch dieser Glaube an wirkende Ideen der Geschichte wird nach und nach von unserer fortschreitenden materialistischen Entwicklung über Bord geworfen, und es gilt heute in gewisser Beziehung auch der Ge­schichte gegenüber für das Zeichen eines aufgeklärten Kopfes, wenn man lediglich daran glaubt, dass alles, was die Epochen charakteri­siert, was in den Epochen aufgetreten ist, im Grunde genommen nur durch das Zusammenfliessen physisch anschaulicher äusserer Taten entsteht, äusserer Bedürfnisse, äusserer Interessen und eben Ideen der physischen Menschen.",
        "Die Zeit ist ja heute schon vorüber, in der noch in einer gewissen Weise wie durch Inspiration solche Geister wie etwa Herder die Entwicklung der Menschheitsgeschichte so dar­gestellt haben, dass man überall merkt: es liegt wenigstens die Voraus­setzung lebendiger Mächte, lebendiger übersinnlicher Mächte zugrunde,"
      ],
      [
        "die sich durch die Taten der Menschen, durch das Lehen der Menschen äussern.",
        "Und wer ein ganz gescheiter Kopf heute sein will, wird sagen: Na, so ein Mensch wie Lessing hat ja manche recht ver­nünftige Idee gehabt, aber dann kam er am Ende seines Lebens auf so konfuses Zeug, wie er es in seiner ,,Erziehung des Menschen-geschlechtes\" geschrieben hat, wo er sich nicht anders mehr zu helfen wusste, als die strenge Gesetzmässigkeit im Flusse des historischen Werdens an die Idee der Wiederverkörperung zu knüpfrn."
      ],
      [
        "In den letzten Sätzen seiner ,,Erziehung des Menschengeschlechts\" hat ja Lessing in der Tat zum Ausdruck gebracht, was die Geisteswissen­schaft aus den okkulten Tatsachen heraus schildert: dass Seelen, die in alten Epochen gelebt haben, die da aufgenommen haben die lebendig wirksamen Kräfte, diese Kräfte herübertragen in ihre neuen Verkörperungen, so dass nicht ein abstrakter, nicht bloss ein ideen­hafter Fortfluss vorhanden ist, sondern ein wirklicher, ein realer Fortfluss des Geistes hinter dem materiellen Geschehen.",
        "Wie gesagt, ein gescheiter Kopf wird sagen: Da ist er im Altet noch auf solche konfuse Ideen gekommen wie auf die Wiederverkörperung; über die muss man hinwegsehen. - Das erinnert einen immer wiederum an die so bitter4ronische und doch so kluge Notiz, die sich einmal Hebbel in sein Tagebuch geschrieben hat, wo er sagt, es wäre ein schönes Motiv, dass ein Gymnasiallehrer in seiner Schule den Plato durch-nimmt, dass sich der wiederverkörperte Plato unter seinen Schülern befindet, und dass der den Plato, wie ihn der Gymnasiallehrer durch-nimmt, so schlecht versteht, dass der Lehrer ihm arge Strafen auf­erlegen muss..."
      ],
      [
        "In bezug auf die historische Auffassung der Menschheitsentwick­lung ist ja von der früheren geistigen Erfassung gar manches verloren­gegangen, und die Geisteswissenschaft wird sich wirklich wehren müssen gegenüber dem Ansturm des materialistischen Denkens, das von allen Seiten her eindringt und einfach töricht findet, was aus den geistigen Tatsachen heraus mitzuteilen ist.",
        "Wir haben es ja im Grunde genommen recht herrlich weit gebracht, zum Beispiel auch darin, wie alle jene gewaltigen Bilder, jene gewaltigen symbolischen Vor­stellungen, welche dem alten hellseherischen Erkennen der Menschen"
      ],
      [
        "entflossen sind und die in den Mythologien, in den Heroengestalten, in den Legenden und Märchengestalten zum Ausdruck kommen, heute Erklärer sonderbarster Art finden.",
        "Das Kurioseste auf diesem Gebiete ist wohl jenes Büchlein ,,Orpheus\" von Salomon Reinach, das in vielen Kreisen Frankreichs in unserer Zeit ein gewisses Auf­sehen gemacht hat."
      ],
      [
        "Da wird alles das, woraus die Ideen der Demeter, des Orpheus' die Ideen anderer mythologischer Kreise ausgeflossen sem sollen, zurückgeführt auf rein materialistische Geschehnisse, und manchmal ist es urgrotesk, wie die historische Existenz dieser oder jener Gestalt abgeleitet wird, die - sagen wir - hinter dem Hermes oder dem Moses steckt, und in welch trivialer Weise diese Gestalten sozu­sagen aus freier Menschheitsdichtung, aus der Phantasie heraus zu erklären gesucht werden.",
        "Nach der Methode des Salomon Reinach würde es leicht sein, nach sechzig bis siebzig Jahren, das heisst wenn das äussere Gedächtnis an ihn ein wenig verwischt wäre, nachzu­weisen, dass es niemals einen solchen Reinach gegeben habe, sondern dass es nur die Volksdichtung ist, die die alte Idee vom Reineke Fuchs auf den Salomon Reinach übertragen hat."
      ],
      [
        "Das würde nach seiner Methode absolut möglich sein.",
        "So absurd ist das Ganze, was in diesem Büchlein ,,Orpheus\", wie in der Vorrede auseinander­gesetzt wird - ,,für die weitesten Kreise unserer gegenwärtigen Ge­bildeten, ja auch für die jüngsten Kreise\" geschrieben worden ist! ,,Für die jüngsten Kreise\", denn er betont, dass er alles vermieden habe - obwohl er nicht vermieden hat, die Idee der Demeter auf ein Schwein zurückzuführen -, was Anstoss erregen könnte bei jüngeren weiblichen Persönlichkeiten."
      ],
      [
        "Er verspricht aber, dass, wenn sein Buch den Einfluss gewinnt, den er erhofft, er dann für die Mamas eine besondere Auflage seines Büchleins schreiben wird, welche alles das enthalten soll, was man jetzt noch den Töchtern vorenthalten muss.",
        "So weit haben wir es also gebracht."
      ],
      [
        "Man möchte gerade die Anhänger der Geisteswissenschaft immer darauf hinweisen, dass es möglich ist, auf rein äussere Vernunfts-gründe hin das Walten geistiger Mächte, geistiger Kräfte durch Menschen bis in unser Jahrhundert herein wirklich zu beweisen; ganz abgesehen von der rein okkult-esoterischen Forschung, die uns"
      ],
      [
        "hier hauptsächlich beschäftigen wird.",
        "Aber damit wir uns darüber verständigen, wie die Geisteswissenschaft eine gewisse Möglichkeit gewinnen kann, rein äusserlich das Walten übersinulicher Mächte in der Geschichte zu verteidigen, lassen Sie mich auf folgendes hin­weisen."
      ],
      [
        "Wer ein wenig Einblick gewinnt in die Entwicklung der modernen Menschheit, wie sie sich vollzogen hat etwa im 14., 15. bis ins 16.",
        "Jahrhundert hinüber, der wird wissen, dass von einer ganz un­endlich tiefen Bedeutung war, wie in diese neuzeitliche äussere Menschheitsentwicklung eine bestimmte Persönlichkeit historisch eingegriffen hat, von der man wirklich, ich möchte sagen, mit äusser­lichsten Gründen nachweisen kann, dass durch sie geistig-übersinn­liche Mächte gewirkt haben."
      ],
      [
        "Man kann nämlich die Frage aufwerfen, um ein klein wenig Licht hinzubreiten über okkulte Auffassung der Geschichte: Was wäre aus der Entwicklung des neueren Europa geworden, wenn im Beginne des 15.",
        "Jahrhunderts sich nicht hinein­gestellt hätte in die Entwicklung das Mädchen von Orleans, die Jung­frau von Orleans?"
      ],
      [
        "Derjenige nämlich, welcher die Entwicklung dieser Zeit einmal auch nur ganz äusserlich ins Auge fasst, der muss sich sagen: Man streiche einmal die Taten der Jungfrau von Orleans hinweg aus dem geschichtlichen Werden, dann muss man nach dem­jenigen, was man rein nach äusseren geschichtlichen Forschungen wissen kann, sich klar sein: ohne das Wirken höherer übersinnlicher Mächte durch das Mädchen von Orleans hätte im i 5.",
        "Jahrhundert Frankreich, ja ganz Europa tatsächlich eine andere Gestalt bekommen müssen."
      ],
      [
        "Denn damals ging alles, was sich abspielte in den Willens-impulsen, in den Gehirnen der physischen Köpfr dahin, Europa sozusagen zu überziehen durch alle Staaten hindurch mit einer die Völkerindividualitäten ausstreichenden und auslöschenden allgemei­nen Staatsauffassung.",
        "Und unter deren Einfluss wäre ganz gewiss unendlich viel von dem unmöglich geworden, was sich in den letzten Jahrhunderten durch das Ineinanderspiel der europäischen Völker­individualitäten innerhalb Europas herausgebildet hat."
      ],
      [
        "Man denke sich einmal die Tat der Jungfrau von Orleans hinweg-gestrichen aus der Geschichte, man denke sich Frankreich seinem"
      ],
      [
        "Schicksal überlassen, ohne dass sie eingegriffen hätte, man frage sich:"
      ],
      [
        "Was wäre aus Frankreich ohne diese Tat geworden?",
        "Und dann be­denke man, welche Rolle Frankreich in den nachfolgenden Jahr-hunderten für das ganze Geistesleben der Menschheit gespielt hat!",
        "Und dazu stelle man die nicht hinwegzuleugnenden, sondern durch äussere Dokumente zu belegenden Tatsachen von der Sendung des Mädchens von Orleans!",
        "Man mache sich klar, dass dieses Mädchen mit einer wahrhaftig auch im Sinne ihrer Zeit nicht besonders hohen äus­seren Bildung plötzlich in einem Alter von noch nicht zwanzig Jahren im Herbst 1428 fühlt, wie zu ihr sprechen geistige Mächte der über­sinnlichen Welten, Mächte, denen sie allerdings die Formen zuerteilt, die ihr geläufig sind, so dass sie sie durch die Brille ihrer Vorstellungen sieht; aber das ist kein Einwand gegen die Realität dieser Mächte.",
        "Stellen Sie sich vor, dass sie weiss: übersinnliche Mächte lenken ihre Willenskraft nach einem ganz bestimmten Punkte hin - ich erzähle Ihnen zunächst von diesen Tatsachen nicht, was durch die Akasha­chronik erzählt werden kann, sondern nur das, was aktenmässig, rein historisch festgestellt ist."
      ],
      [
        "Wir wissen, dass dieses Mädchen von Orleans sich zunächst einem Verwandten geoffenbart hat, bei dem sie - man möchte fast sagen zufällig - Verständnis gefunden hat; dass sie nach mancherlei Um­wegen und Schwierigkeiten in das Hoflager des Königs Karl geführt wurde, der mit dem ganzen französischen Heerwesen sozusagen am Ende seines Witzes angelangt war; und wir wissen, dass sie, nachdem man ihr alles Erdenkliche in den Weg gelegt hatte, zuletzt unter einer ganzen Menge von Leuten, in die König Karl so hineingestellt war, dass er durchaus nicht für äussere Augen zu unterscheiden war, ihn richtig herausgefunden hat, indem sie kurzweg auf ihn losgegangen ist.",
        "Man weiss auch, dass sie ihm dazumal etwas anvertraut hat - er wollte sie dadurch prüfen -, wovon man sagen kann, dass nur er allein und die übersinnlichen Welten das Entsprechende gewusst haben.",
        "Und Sie wissen ja vielleicht aus der äusseren Geschichte, wie dann sie es war, die unter den fortwährenden Impulsen und unter dem fortwährenden Eindruck ihres starken Glaubens - man würde besser sagen, durch ihr unmittelbares Schauen - die Heere unter den"
      ],
      [
        "grössten Schwierigkeiten zum Siege führte und den König zur Krönung."
      ],
      [
        "Wer hat dazumal eingegriffen in den Gang der historischen Ent­wicklung?",
        "Doch niemand anders als Angehörige höherer Hier­archien!",
        "Das Mädchen von Orleans war ein äusseres Werkzeug dieser Wesenheiten, und sie, diese Wesenheiten der höheren Hier­archien, haben die Taten der Geschichte gelenkt.",
        "Es mag ja sein, dass irgendein Verstand sich sagt: Hätte ich sie gelenkt, so hätte ich sie klüger gelenkt; weil er dieses oder jenes, was geschehen ist in dem Auftreten der Jungfrau von Orleans, seinem Denken nicht angemessen findet.",
        "Anhänger der Geisteswissenschaft sollen aber nicht Göttertaten durch Menschenverstand korrigieren wollen, was ja allerdings heute innerhalb unserer sogenannten Zivilisation überall vorkommt.",
        "Sehen Sie, es haben sich natürlich auch Leute gefunden, welche ganz im Sinne unserer heutigen Zeit die Geschichte der modernen Welt sozusagen entlasten wollten von den Taten der Jungfrau von Orleans.",
        "Und ein für unsere heutige Zeit charak­teristisches Werk nach dieser materialistischen Richtung hin hat Anatole France geschrieben.",
        "Man möchte eigentlich doch nur wissen, wie sich das materialistische Denken abfindet mit Mitteilungen, welche wahrhaftig - und ich rede immer noch von Dokumenten der äusseren Geschichte - recht gut begründet sind.",
        "So möchte ich, weil wir gerade hier an diesem Orte sind und ich manchmal gerne Rücksicht nehme auf lokale Verhältnisse, Ihnen anführen ein Dokument, auf das man sich schon einmal hier berufen hat."
      ],
      [
        "Die Stuttgarter wissen gewiss, dass hier an diesem Orte einmal ein bedeutender Evangelienforscher gelebt hat.",
        "Man braucht als Geisteswissenschafter durchaus nicht einverstanden zu sein mit dem auch mancherlei recht Gescheiten, das Gfrörer - so hiess der Evan­gelienforscher - in seiner Evangelienforschung dargeboten hat, und man kann ganz sicher sein, dass Gfrörer, wenn er hörte, was jetzt auf dem Gebiete der Geisteswissenschaft verkündet wird, diejenige Redensart gebrauchen würde, die er oftmals gebraucht hat für seine Gegner, die er mit seiner Starrköpfigkeit durchaus nicht immer leicht angelassen hat: die Redensart, dass diese Theosophen auch solche"
      ],
      [
        "Leute seien, ,,bei denen es unter dem Hute nicht recht richtig ist\".",
        "Deshalb aber war doch dazumal die Zeit noch nicht gekommen, wo man sozusagen in rein materialistischer Weise über historische Do­kumente hinweggehen kann, wie man das heute macht, wenn diese historischen Dokumente Tatsachen betreffen, die unbequem sind, die augenscheinlich das Wirken lebendiger höherer Kräfte innerhalb unserer physischen Welt anzeigen.",
        "Und so möchte ich heute auch wiederum ein kleines Dokument zitieren, einen Brief, der in der ersten Hälfte des 19.",
        "Jahrhunderts veröffentlicht worden ist.",
        "Ich möchte Ihnen nur einige Stellen vorlesen, so wie sich dazumal zur Rechtfertigung seines Glaubens Gfrörer auf diesen Brief berufen hat.",
        "Ich möchte Ihnen eine Stelle aus einer Charakteristik der Jungfrau von Orleans vorlesen und Sie dann fragen, was eine solche lebendige Schilderung bedeutet."
      ],
      [
        "Nachdem der Schreiber dieses Briefes, auf den sich Gfrörer beruft, aufgezählt hat, was die Jungfrau von Orleans vollbracht hat, fährt er fort:"
      ],
      [
        ",,Dieses und vieles andere hat die Jungfrau (von Orleans) voll­führt und mit Gottes Hilfe wird sie noch Grösseres verrichten.",
        "Das Mägdelein ist von anmutiger Schönheit und besitzt männliche Hal­tung, es spricht wenig und zeigt eine wunderbare Klugheit; in seinen Reden hat es eine gefällige, feine Stimme nach Frauenart.",
        "Es isst mässig, noch mässiger trinkt es Wein.",
        "An schönen Rossen und Waffen hat es sein Gefallen.",
        "Gewappnete und edle Männer liebt es sehr.",
        "Die Zusammenkunft und das Gespräch mit vielen ist der Jungfrau zu­wider; sie fliesst oft von Tränen über, liebt ein fröhliches Gesicht, erduldet unerhörte Arbeit, und in der Führung und Ertragung der Waffen ist sie so beharrlich, dass sie sechs Tage lang Tag und Nacht ohne Unterlass vollständig gewappnet bleibt.",
        "Sie spricht: Die Eng­lischen hätten kein Recht an Frankreich, und darum habe sie, wie sie sagt, Gott gesandt, auf dass sie jene austreibe und überwinde, jedoch erst nach vorhergeschehener Mahnung.",
        "Dem König erweist sie die höchste Verehrung; sie sagt, er sei von Gott geliebt und in besonderem Schutze, weshalb er auch erhalten werden würde.",
        "Vom Herzog von Orleans, Eurem Neffen, sagt sie, er werde auf wunderbare"
      ],
      [
        "Weise befreit werden, doch erst, nachdem zuvor eine Mahnung an die Englischen, die ihn gefangen halten, zu seiner Befreiung ge­schehen sein werde."
      ],
      [
        "Und damit ich, erlauchter Fürst, meinem Bericht ein Ende mache:"
      ],
      [
        "Noch Wunderbareres geschieht und ist geschehen, als ich Euch schreiben oder mit Worten ausdrücken kann.",
        "Während ich dieses schreibe, ist die genannte Jungfrau schon nach der Gegend der Stadt Rheims in Champagne gezogen, wohin der König eilends zu seiner Salbung und Krönung unter Gottes Beistand aufgebrochen ist.",
        "Erlauchtester und Grossmächtigster Fürst und mein höchst zu ver-ehrender Herr! ich empfrhle mich Euch sehr demütig, indem ich den Allerhöchsten bitte, dass er Euch behüte und Eure Wünsche erfülle."
      ],
      [
        "Geschrieben Biteromis am 21.",
        "Tage des Monats Junius."
      ],
      [
        "Euer demütiger Diener"
      ],
      [
        "Herr von Bonlaninth, Rat und Kämmerer des Königs"
      ],
      [
        "der Franzosen und des Herrn Herzogs von Orleans,"
      ],
      [
        "Seneschal des Königs, gebürtig aus Berry.\""
      ],
      [
        "Einer, der das Mädchen kennt, schreibt aus unmittelbarer Nähe des Königs diesen Brief.",
        "Es ist in der Tat dann erstaunlich, wenn aus rein okkulten Gründen und Beweismitteln heraus man alle diese Sachen wiederfinden muss - denn sie sind auffindbar in der Akasha-Chronik - und sieht, wie gerade in solchen Fällen man auch äusserlich geschichtliche Dokumente durchaus beibringen kann.",
        "Kurz, es er­scheint einem fast wahnsinnig, an dem zu zweifeln, was durch die Jungfrau von Orleans wirkte.",
        "Und wenn wir dann noch in Betracht ziehen, dass durch ihre Taten die ganze Geschichte der neueren Zeit ein anderes Gesicht bekommen hat, so gibt uns das ein Recht zu sagen, dass wir hier unmittelbar hereinwirken sehen, äusserlich dokumentarisch belegbar, die übersinnliche Welt.",
        "Wenn dann der Geistesforscher weitergeht und Umschau hält auf seine Art nach dem eigentlichen Inspirator, der auf die Jungfrau von Orleans gewirkt hat, dann findet er, durchforschend die aufeinanderfolgenden Zeiten, etwas ganz Merkwürdiges.",
        "Er findet, wie derselbe Geist, der durch"
      ],
      [
        "die Jungfrau von Orleans als sein Werkzeug dazumal gewirkt hat, sozusagen in ganz anderer Form, in ganz anderer Art inspirierend auch auf eine andere Persönlichkeit gewirkt hat, die als Philosoph am Hofe Karls des Kahlen lebte: Scotus Erigena, durch dessen philosophisch-theologische Ideen in einem frühen Zeitraum Europa so tief beeinflusst worden ist.",
        "Und so sehen wir, dass dieselben Mächte in verschiedenen Epochen in verschiedener Art durch Menschen als durch ihre Werkzeuge wirken; dass I(ontinuität, fortlaufendes Geschehen ist in dem, was wir Geschichte nennen."
      ],
      [
        "Nun habe ich Ihnen gestern gezeigt, wie in einem bedeutsamen Mythos aus der babylonisch-chaldäischen Zeit hingewiesen wird auf das Hereinwirken der geistigen Welten auf Menschen, von denen vieles im Verlauf der Geschichte abhing für den dritten unserer nach-atlantischen Zeiträume, wie den Verlauf des ganzen geschichtlichen Werdens im alten Chaldäa' im alten Babylonien.",
        "Wir müssen aber allerdings jetzt auch vom Standpunkt der okkulten Wissenschaft die beiden Persönlichkeiten betrachten, die sich hinter den sagen­haften Namen Gilgamesch und Eabani verbergen.",
        "Okkult-historisch haben wir in ihnen Persönlichkeiten zu sehen, die am Ausgangspunkt dessen stehen, was wir babylonische, was wir chaldäische Kultur nennen.",
        "Was von ihnen hat kommen können an Impulsen, das finden wir wieder in der Entwicklung der eigentlich geistigen Kultur des alten Babyloniens und Chaldäas.",
        "Nun war Gilgamesch eine solche Persönlichkeit, welche viele Inkarnationen in der Art hinter sich hatte, dass man gewissermassen diese Persönlichkeit als eine alte Seele innerhalb der Menschheitsentwicklung bezeichnen kann."
      ],
      [
        "Sie wissen ja aus der Darstellung in meiner ,,Geheimwissenschaft\", dass während des lemurischen Zeitraums der Erdentwicklung nur ganz wenige Menschen sozusagen die Ereignisse der Erdentwicklung auf der Erde selbst überdauert haben, dass nur wenige auf der Erde blieben während des lemurischen Zeitraums; dass die Mehrzahl der Seelen, bevor die eigentliche Gefahr der Mumifizierung alles Mensch­lichen begann, sich von der Erde hinweghob nach anderen Planeten und weiterlebte auf Mars, Saturn, Venus, Jupiter und so weiter; dass dann vom Ende des lemurischen Zeitraums an und während des"
      ],
      [
        "atlantischen Zeitraums nach und nach diese Seelen wieder herunter­kamen auf die Erde, um unter den veränderten irdischen Verhält­nissen sich in irdischen Leibern zu verkörpern und in immer neuen Inkarnationen zu erscheinen.",
        "Da haben wir also solche Seelen, die verhältnismässig früh heruntergekommen sind aus der Planetenwelt, und andere, die spät, erst in späten Zeiträumen der atlantischen Ent­wicklung niedergestiegen sind.",
        "Die ersteren Seelen, die also früher heruntergekommen sind, haben mehr Inkarnationen innerhalb der Erde hinter sich als die später herniedergestiegenen, und diese können wir daher im Gegensatz zu den ersteren, jüngere Seelen nennen, Seelen, die also weniger in sich aufgenommen haben."
      ],
      [
        "Eine alte Seele war diejenige Individualität, die sich hinter dem Namen Gilgamesch verbirgt, und eine jüngere, die in Eabani ver­körpert war am Ausgangspunkte der babylonischen Kultur.",
        "Ja, in bezug auf dieses Jüngere oder Ältere der menschlichen Seelen zeigt sich - man möchte fast sagen selbst zur Überraschung des Okkul­tisten - etwas sehr Merkwürdiges."
      ],
      [
        "Wenn zum Beispiel irgend jemand heute es so weit gebracht hat, dass er die Wahrheiten der Geistes­wissenschaft ein wenig zugibt, sonst aber noch immer an den Vor-urteilen und Werturteilen der äusseren Welt hängt, dann wird es ihm ja plausibel erscheinen, dass zum Beispiel Philosophen- oder Ge­lehrtenseelen unserer heutigen Zeit zu den älteren Seelen gerechnet werden müssen.",
        "Die okkulte Forschung ergibt das gerade Gegenteil, so sonderbar es klingt; und es ist für den Okkultisten selbst über­raschend, dass zum Beispiel in Kant eine junge Seele lebte."
      ],
      [
        "Ja, die Tatsachen sagen es... da ist nichts dagegen zu machen.",
        "Und man könnte nun darauf hinweisen, dass die jüngeren Seelen sich allerdings in der Mehrzahl in den farbigen Rassen verkörpern, dass also die farbigen Rassen, namentlich die Negerrasse, vorzugsweise jüngere Seelen zur Verkörperung bringen."
      ],
      [
        "Aber gerade das Eigentümliche jener menschlichen Denkungsart, die sich in Gelehrsamkeit, in der heutigen materialistischen Wissenschaft auslebt, die bedingt jüngere Seelen.",
        "Und es ist sogar nachweisbar, dass bei mancher Persönlich­keit, bei der man es gar nicht voraussetzen würde, die vorhergehende Inkarnation durchaus bei den Wilden liegt."
      ],
      [
        "Ja, das sagen wieder die"
      ],
      [
        "Tatsachen!",
        "Das alles muss durchaus festgehalten werden, es ist so.",
        "Das nimmt natürlich den Urteilen, die wir über unsere Umwelt haben, nichts von ihrer Bedeutung, nichts von ihrem Werte; dennoch muss es erfasst werden zum Gesamtverständnis dessen, um was es sich handelt.",
        "In diesem Sinne haben wir es mit Eabani im alten Baby­lonien zu tun mit einer jungen Seele, in Gilgamesch mit einer alten Seele.",
        "Eine solche alte Seele, die wird ihrer ganzen Natur nach früh erfassen, was gewissermassen nicht nur Kulturelement, Kulturfaktor der Gegenwart ist, sondern was als Kultureinschlag in die Gegenwart hereinfällt und weit hinausblicken lässt in die Perspektive der Zukunft."
      ],
      [
        "Es mag sich ja allerdings mancher dagegen verwahren, wenn man ihm plausibel machen würde, dass die oftmals von ihm so inferior gehaltenen Theosophen zumeist ältere Seelen sind als diejenigen, die akademische Vorträge halten.",
        "Aber die Forschung zeigt es; und wenn auch die geistige Forschung nicht etwa dazu missbraucht werden soll, die Werturteile umaustossen und Spott zu treiben mit dem, was einmal der Einschlag unserer Kultur ist, so muss man doch der Wahr­heit streng ins Auge schauen.",
        "So war denn Gilgamesch eine Persön­lichkeit, die es vermöge ihrer Seelenkonstitution mit demjenigen hielt, was zu den fortgeschrittensten Geisteselementen und Geistes-faktoren der damaligen Zeit gehörte, was für die damalige Zeit weit hineinleuchtete in die Zukunft, und was auch damals nur erreicht werden konnte dadurch, dass eine solche Persönlichkeit eine Art Initiation durchmachte.",
        "In einer gewissen Initiation, in einer Mit­teilung dessen, was man nur durch die Initiation empfangen kann, sollte dem Gilgamesch gegeben werden, was ihn befähigte, Fermente für die babylonische Kultur zu liefern.",
        "Also eine Einweihung sollte er bis zu einem gewissen Grade durchmachen."
      ],
      [
        "Betrachten wir ihn einmal, diesen Gilgamesch, wie er sich in die Menschheitsentwicklung hineinstellen musste vor dieser Einweihung.",
        "Da war er ein Mensch des dritten nachatlantischen Zeitraumes.",
        "In diesem Zeitraume aber war für das natürliche menschliche Hellsehen, für das, was der Mensch konnte und vermochte durch seine natür­lichen Kräfte, dazumal schon die Ahenddämmerung gekommen.",
        "Das war nicht mehr in dem Grade vorhanden, dass die Menschen in"
      ],
      [
        "grösserer Anzahl zurückschauen konnten in ihre früheren Inkarna­tionen.",
        "Wenn wir weiter zurückgehen in den zweiten, in den ersten nachatiantischen Zeitraum, da würden wir finden, dass die Mehrzahl der Menschen auf unserer Erde noch zurückschauen konnten in ihre früheren Inkarnationen, in das Verfliessen ihres Seeleniebens vor ihrer gegenwärtigen Geburt."
      ],
      [
        "Aber das war allmählich verloren worden.",
        "Bei Gilgamesch war die Sache so, dass von vornherein diejenige Wesenheit, die sich durch ihn offenbaren sollte und die sich nur offen­baren konnte durch ihn, indem sie ihn nach und nach zu einer Art Initiation führte, dass diese Wesenheit sozusagen immer ihre Hand über ihn hielt."
      ],
      [
        "Sie stellte ihn hin auf den Platz, durch den er seine eigene Stellung in der Weltgeschichte beurteilen lernte.",
        "Es wurde sozusagen durch Ereignisse übersinnlicher Art, welche uns in dem Mythos, den ich gestern angeführt habe, in Bildern entgegentreten, ihm ein Freund an die Seite gegeben, ein Freund, dessen Barbarei, dessen Unzivilisiertheit uns dadurch angedeutet wird, dass er halb tierisch an äusserer Gestalt ist."
      ],
      [
        "Es wird gesagt, dass dieser Freund Tierfelle am Leibe trug, das heisst, dass er sozusagen noch wie die Menschen des Urzustandes behaart war, dass seine Seele so jung war, dass sie einen Leib sich aufbaute, der den Menschen noch in ver­wilderter Gestalt zeigt.",
        "So hatte Gilgamesch, der fortgeschrittenere, in Eabani einen Menschen neben sich, der durch seine junge Seele und seine dadurch bedingte Leibesorganisation noch ein altes Hell­sehen hatte."
      ],
      [
        "Um sich selber zu orientieren, war ihm dieser Freund beigegeben worden.",
        "Mit Hilfe dieses Freundes gelang es ihm dann, gewisse Dinge auszuführen, wie - sagen wir - die Zurückführung jener geistigen Macht, die uns wiederum im Mythos unter dem Bilde der Stadtgöttin von Erek, Ischtar, dargestellt wird."
      ],
      [
        "Ich habe Ihnen gesagt, dass die Stadtgöttin gestohlen worden war von der Nachbar­stadt und dass daher die beiden, Gilgamesch und Eabani, Krieg begannen gegen die Nachbarstadt, den König dieser Nachbarstadt besiegten und die Stadtgöttin wieder zurückführten."
      ],
      [
        "Wenn man solche Dinge, die uns in diesen alten Mythen dargestellt werden, richtig historisch verstehen will, dann muss man schon auf die okkulten Hintergründe der Sache eingehen.",
        "Es verbirgt sich ja"
      ],
      [
        "hinter diesem Rauhe der Stadtgöttin etwas Ähnliches wie hinter dem Rauhe der Helena, die nach Troja entführt wird durch Paris.",
        "Wir müssen uns darüber klar sein, dass es durchaus auf guten Gründen beruht, was in meiner kleinen Schrift ,,Blut ist ein ganz besonderer Saft\"\" ausgeführt ist."
      ],
      [
        "Da werden Sie hingewiesen darauf, dass in den Völkern der alten Zeit ein gewisses Gesamtbewusstsein vorhanden war, dass der Mensch nicht nur sein persönliches Ich empfand inner­halb seiner Haut, sondern dass er sich als ein Glied des Stammes, der Stadtgemeinschaft empfand.",
        "So wie die einzelne menschliche Seele als Zentralfaktor für unsere Finger, Zehen, Hände, Beine, die zusammengehören, für unseren ganzen Organismus empfunden wird, so fühlte sich der Mensch in alten Zeiten gegenüber der Gruppen­seele wie ein Glied, dem er zugehörte."
      ],
      [
        "So etwas war in älteren Zeiten noch in den alten Stadtgemeinden, selbst in Griechenland, vorhanden.",
        "Ein gemeinschaftlicher Geist, eine Volks-lchheit, eine Stammes­Ichheit, lebte und webte durch die einzelnen Volkspersönlichkeiten hindurch."
      ],
      [
        "Aber dasjenige, was zum menschlichen Bewusstsein kom­men konnte von einer solchen gemeinsamen Ichheit, das musste gewissermassen in Mysterien, in geheimen Tempelstätten verwaltet werden.",
        "Da waren die alten Mysterienpriester und verwalteten die gemeinsamen spirituellen Angelegenheiten einer Stadt oder eines Stammes."
      ],
      [
        "Und man spricht nicht bloss figürlich, sondern in einer gewissen Weise real und richtig, wenn man sagt, eine solche Tempel­stätte war wirklich wie eine Wohnung für das Stadt-Ich, für die Gruppenseele.",
        "Da hatte sie ihren zentralen Wohnsitz und die Tempel-priester waren ihre Diener."
      ],
      [
        "Sie waren diejenigen, welche die Auf­träge dieser Gruppenseele durch Inspiration empfingen - was man Orakel nannte - und sie hinaustrugen in die Welt, damit dieses oder jenes geschehe; denn die Orakel sind ja damals durchaus in dem Sinne aufzufassen, den ich Ihnen jetzt charakterisiert habe."
      ],
      [
        "Nun war die Verwaltung solcher Tempelstätten mit gewissen Geheimnissen verbunden, und viele Kämpfe in den alten Zeiten spielten sich so ab, dass die Tempelpriester einer Stadt von der Nach­barstadt als Gefangene hinweggeschleppt wurden, dass also sozusagen mit den Tempelpriestern die wichtigsten Geheimnisse einer Stadt"
      ],
      [
        "weggeschleppt wurden in die Nachbarstadt.",
        "Da haben Sie die reale Tatsache, welche dem Bilde entspricht, dass die Stadtgöttin Ischtar, die Volksseele von Erek, geraubt wird durch die Nachbarstadt.",
        "Die Tempeipriester, die Verwalter der Tempelgeheinmisse, waren zu Gefangenen gemacht worden, weil die Nachbarstadt hoffte, auf diese Weise in den Besitz der heiligen Geheimnisse und damit der Macht der betreffenden Stadt zu kommen.",
        "Das ist der reale Hinter­grund."
      ],
      [
        "Und solche Dinge konnte Gilgamesch in der Seelenverfassung, in der er sich zunächst befand, nicht selber wahrnehmen, weil er nicht hineinsah in diese Zusammenhänge; aber eine jüngere Seele konnte ihm sozusagen wie der hellseherische Sinn dienen, der ihm half, den Tempelschatz für seine Vaterstadt zurückzuerobern.",
        "Da wurde ihm, dem Gilgamesch, so recht zum Bewusstsein gebracht, dass es im menschlichen Leben gerade in Übergangszeiten so etwas gibt, wie es in der Legende von dem Blinden und dem Lahmen dar­gestellt wird, von denen jeder einzelne hilflos ist, die aber zusammen sich weiterbringen, indem der Blinde den Lahmen auf die Schulter nimmt und der Lahme dem Blinden sein Sehvermögen leiht."
      ],
      [
        "Da sehen wir bei Gilgamesch und Eabani ins Spirituelle umgesetzt ein solches Zusammenwirken von Menschen ganz verschiedener Begabung.",
        "Wir treffen das insbesondere in den historischen Tatsachen der älteren Zeiten auf Schritt und Tritt an."
      ],
      [
        "Und es ist wichtig, so etwas zu ver­stehen, denn dann erst kann man verstehen, warum uns so oft in Mythen und Sagen Freunde, die gemeinsam etwas zu vollbringen haben, vorgeführt werden: Freunde, die dann gewöhnlich so un­gleich sind in bezug auf ihre Seelenverfassung, wie es eben Gilga­mesch und Eabani waren.",
        "Das aber, was Gilgamesch ausserdem durch Eabani, seinen Freund, sich für seine Seele erobern konnte, das war, dass er gleichsam von Eabani angesteckt wurde mit einer eigenen hellseherischen Kraft, so dass er in gewisser Weise zurückschauen konnte in seine eigenen früheren Inkarnationen."
      ],
      [
        "So lernte Gilgamesch wirklich von Eabani das Zurückschauen in frühere Inkarnationen.",
        "Das war etwas, was schon ausserhalb der normalen Fähigkeiten des Gilgamesch lag.",
        "Und nun stellen wir uns lebendig vor, wie Gilgamesch"
      ],
      [
        "beeinflusst gewesen sein mochte von diesem Zurückschauen in seine früheren Inkarnationen."
      ],
      [
        "Was konnte er sich etwa sagen von dem Tage an, da in seiner Seele die Möglichkeit auftauchte, zurückzublicken in dasjenige, was seine Seele durchlebt hatte in früherer Inkarnation?",
        "Das befremdete ihn zunächst.",
        "Er konnte sich nicht recht in seine eigene Wesenheit hinein­finden, wie sie in früheren Inkarnationen war; er erkannte sich sozu­sagen nicht so recht wieder.",
        "So würde es ja überhaupt den Menschen gehen, wenn sie anfingen, in ihre früheren Inkarnationen zurückzu­blicken.",
        "Da würde es meist anders ausschauen als in den Einbildungen, die immer wieder und wieder auftreten, wenn gesagt wird, irgendein Mensch sei eine Reinkarnation von dieser oder jener Persönlichkeit.",
        "Da kann es einem ja passieren, dass man irgendeine Persönlichkeit findet, die eine ganze Reihe von historischen, grossen Namen als diejenigen ihrer vorhergehenden Inkarnationen anführt...",
        "Es soll sogar ganze Gruppen von Menschen geben, die davon überzeugt sind, dass es unter dem Range einer Königin oder einer Prinzessin nichts in ihren früheren Inkarnationen gibt! - In diesen Dingen, mit denen es so ernst stehen sollte, darf eben keine Phantasie obwalten damit darf kein Unfug getrieben werden."
      ],
      [
        "Nun, derjenige, der so wie Gilgamesch damals zunächst auf die Reihenfolge seiner Inkarnationen zurückblickt, der kann wirklich zuweilen auch überrascht sein.",
        "Er blickte ja zurück auf Inkarnationen, da er noch hineinverwoben war in allerlei Zusammenhänge, die durch die Gruppenseelenhaftigkeit gegeben waren.",
        "Er hatte sich allerdings in gewisser Weise für seine Person herausgearbeitet aus diesen Zu­sammenhängen, er hatte auch erst durch Eabani den ganzen Wert erfahren können dessen, was durch die Stadtgöttin in der Mythe symbolisiert wird.",
        "Da er aber zurückschaute, da gefiel ihm manches nicht in seinen früheren Inkarnationen, da konnte er sich sagen: das ist doch nicht nach meinem Geschmack.",
        "Da fand er, dass zum Beispiel seine Seele in den Inkarnationen ganz besondere Freundschaften, ganz besondere menschliche Zusammenhänge gehabt hatte, deren er sich jetzt hätte schämen mögen.",
        "Da kam denn heraus, was uns dar­gestellt wird im Mythos, dass er demgegenüber, was ihm auf dem"
      ],
      [
        "Umwege durch Eabani die Stadtgöttin offenbart hatte, anfing, in gewisser Weise zu schelten, dass er Vorwürfe machte seiner Seele.",
        "Im Mythos wird angedeutet, dass er der Göttin Vorwürfe machte über ihre Bekanntschaften, denn er wurde eifersüchtig auf solche Bekanntschaften."
      ],
      [
        "Da blickte er sozusagen auf den Horizont seiner Seele und die Schmungen standen so lebendig vor ihm, wie Menschen um einen anderen herumstehen in der äusseren physischen Welt, gegenüber denen man diese oder jene Sympathie oder Antipathie empfindet.",
        "Und in alledem, was nun Gilgamesch der Stadtgöttin an Vorwürfen macht, erkennen wir, dass er eigentlich mit demjenigen redet, was auf dem Grunde seiner Seele sich abspielt."
      ],
      [
        "Wenn uns also gesagt wird zum Beispiel, dass er der Stadtgöttin den Vorwurf machte, dass sie vorher Bekanntschaft gehabt hätte mit irgendeinem Menschen, der da in der Mythe Ischulanu genannt wird, so bedeutet das nichts anderes, als dass seine eigene Bekanntschaft mit einem gewissen Menschen, der der Gärtner seines Herrn in der vorher­gehenden Jnkarnation war, ihm nicht gefiel.",
        "Also dasjenige, was sich in der Seele des Gilgamesch abspielte, und wodurch er eigentlich erst jene innere Gedrungenheit, jene innere Erfülltheit seiner Seele erhielt, die er brauchte, als er der Inaugurator der babylonischen Kultur werden sollte - das alles wird uns dargestellt in dem Zurückkommen zu einer gewissen Hellsichtigkeit, in dem Hinaufsteigen in übersinn­liche Welten, was ihm, weil er eine alte Seele war, in gewisser Be­ziehung schon verloren war."
      ],
      [
        "Das wird uns im Mythos dargestellt."
      ],
      [
        "Und dann sollte er eine Art von Einweihung durchmachen da­durch, dass er zurückgeführt wurde zu jener Art von Anschauung, die seine eigene Seele während der atlantischen Inkarnationen hatte.",
        "Was uns nun der Mythos darstellt als die See- und Irrfahrten des Gilgamesch nach dem Westen, das ist nichts anderes als die innere Initiationsfahrt seiner Seele, durch die sie hinauffährt auf geistige Höhen, auf denen sie wahrnehmen kann, was um sie herum war in der alten atlantischen Zeit, da die Seele noch hellsichtig in die geistige Welt hineinschaute.",
        "Daher erzählt der Mythos, dass Gilgamesch auf dieser seiner spirituellen Fahrt zusammengebracht wurde mit der grossen atlantischen Herrscherpersönlichkeit Xisuthros.",
        "Das war eine"
      ],
      [
        "Persönlichkeit, welche gewissen höheren Hierarchien angehörte und während der atlantischen Zeit in den Regionen der Menschheit lebte, seither aber dieser Menschheit entrückt war und in höheren Gebieten des Daseins wohnte.",
        "Diese Persönlichkeit sollte er, der Gilgamesch, kenneniernen, um aus der Anschauung ihrer Wesenheit dasjenige zu gewinnen, was notwendig war, um zu wissen, wie die Seelen sind, wenn sie hineinschauen können in die geistigen Welten."
      ],
      [
        "So sollte er wiederum hinaufgeführt werden in die spirituellen Sphären da­durch, dass er zurückgeführt wurde in seiner Seele bis in die atlanti­schen Zeiten hinein.",
        "Und wenn ihm aufgetragen wird, er soll sieben Nächte und sechs Tage nicht schlafen, so bedeutet das nichts anderes als eine Übung, durch welche die Seele gestaltet werden sollte, um völlig einzudringen in die entsprechenden, eben charakterisierten geistigen Regionen."
      ],
      [
        "Wenn uns nun gesagt wird, dass er dies nicht aushielt, dann bedeutet das wiederum etwas sehr Wichtiges: es bedeutet, dass Gilgamesch uns dargestellt werden soll als eine Persön­lichkeit, die hart an den Rand der Initiation gebracht wird, die gleich­sam durch die Pforte der Initiation hineinschauen sollte in die geistigen Geheimnisse, die aber durch die ganze Art der Zeitverhältnisse doch nicht in alle Tiefen dringen konnte.",
        "Kurz, es soll gesagt werden, dass der Inaugurator, der Einrichter der babylonischen Kultur gewisser­massen an der Pforte der Initiation stehengeblieben ist, dass er nicht ganz klar in die höheren geistigen Welten hineinschauen konnte, und dass er deshalb der babylonischen Kultur so recht das Gepräge gegeben hat, welches ein Abdruck ist von einem blossen Hinein­schauen in die Initiationsgeheimnisse."
      ],
      [
        "Wir werden nun sehen, wie diese äussere babylonische Kultur tat­sächlich so ist, dass sie rechtfertigt, was eben gesagt worden ist.",
        "Während uns zum Beispiel alles darauf hinweist, dass wir in Hermes eine Persönlichkeit vor uns haben, welche tief, tief hineinschaute in die heiligsten Geheimnisse der Initiation und deshalb der grosse Initiator der ägyptischen Kultur werden konnte, so müssen wir sagen, dass die äussere babylonische Kultur in einer Weise zubereitet worden ist, wie wir es eben charakterisiert haben: nämlich durch eine führende Persönlichkeit, die in ihrer Seele alle diejenigen Eigenschaften hatte,"
      ],
      [
        "die sich entwickeln, wenn man nicht ganz in das Innerste der heiligen Geheimnisse eindringt.",
        "Deshalb haben wir in der Tat im alten Baby-ionien die historische Entwicklung so, dass wir deutlich nebeneinan­der gehend einen äusseren Kulturverlauf und einen esoterisch-inneren haben.",
        "Während im ägyptischen Leben diese beiden mehr ineinander-spielen, fallen sie gewissermassen in der alten babylonischen Kultur durchaus auseinander.",
        "Und innerhalb dessen, was wir als die baby-ionische Kultur anzusehen haben, wie sie inauguriert worden ist durch Gilgamesch, lebte dasjenige, was in den heiligsten, verborgensten Mysterien der Chaldäer liegt."
      ],
      [
        "Diese Initiierten der Mysterien waren allerdings in das Innerste eingeweiht, aber das zog sich doch nur wie ein kleiner Strom durch die äussere Kultur hindurch.",
        "Diese äussere Kultur war ein Ergebnis der Impulse des Gilgamesch."
      ],
      [
        "Nun hat sich uns ja aus all diesen Be­trachtungen ergeben, dass Gilgamesch als Persönlichkeit im Grunde genommen nicht so weit war, dass er eine völlige Einweihung hätte erleben können.",
        "Gerade dadurch aber, dass er nicht in der Zeit, in der er wirkte, sozusagen seine eigenen persönlichen Impulse auslebte, das, was seine Kraft war, der Welt mitteilte, war er ganz besonders dazu imstande, durch sich durchwirken zu lassen eine der geistigen Wesenheiten, die wir zu der Klasse der Feuergeister, also derArchange­loi, der Erzengel, rechnen."
      ],
      [
        "Solch eine Wesenheit wirkte durch Gilga­mesch, und die Ordnung der babylonischen Verhältnisse, die treiben­den Kräfte derselben, für die Gilgamesch das Werkzeug war, haben wir bei einem solchen Feuergeist zu suchen.",
        "So haben wir uns diesen Gilgamesch so recht vorzustellen unter einem Bilde, das uns geben konnte das Symbolum des alten Kentauren."
      ],
      [
        "Solche alten Symbole, sie entsprechen mehr der Wirklichkeit als man gewöhnlich denkt.",
        "Ein Kentaur, halb Tier, halb Mensch, sollte immer darstellen, wie in den mächtigeren Menschen der alten Zeiten wirklich in gewisser Weise auseinanderfiel das höchste spirituelle Menschentum und das­jenige, was die einzelnen Persönlichkeiten mit der tierischen Organi­sation verband."
      ],
      [
        "Wie ein Kentaur, so wirkte dieser Gilgamesch auf diejenigen, die ihn beurteilen konnten, und so wirkt er heute noch auf diejenigen, die ihn beurteilen können."
      ],
      [
        "Es ist sehr merkwürdig, dass gerade dieses Bild des Kentauren heute wiederum auftaucht auf dem Felde des modernen naturwissen­schaftlichen Denkens.",
        "Da ist jüngst ein Buch erschienen, das ganz auf naturwissenschaftliche Tatsachen fussen will, das aber doch in gewisser Weise vorurteilslos mit diesen Tatsachen umgeht und daher nicht so dilettantisch, so sinnlos alles durcheinanderwirft' wie es die­jenigen tun, die sich Monisten nennen."
      ],
      [
        "Es sucht der Verfasser wirklich den Menschen zu verstehen, wie er als selbständige seelisch-geistige Wesenheit der physischen Leibesorganisation gegenübertritt.",
        "Und da kommt ein auf naturwissenschaftliche Unterlagen sich stützender Mensch zu einem eigentümlichen Bild."
      ],
      [
        "Er hat ganz gewiss nicht an den Kentauren gedacht, als er sich dieses Bild ausmalte, aber er sagt zu dem, was sich aus naturwissenschaftlichen Vorstellungen ergibt über die Beziehungen der Seele zum Leibe: Das lässt sich vergleichen mit dem Reiten des Reiters auf dem Pferde.",
        "Man kann gar nicht anders sich vorstellen, wozu die wirklich verstandenen naturwissenschaft­lichen Tatsachen zwingen, als dass man sagt: Selbständig ist die Seele, die den Leib als Werkzeug benutzt wie der Reiter sein Pferd. - Der Kentaur ist wieder da, die Dinge werden tatsächlich schnell gehen, und ehe es sich die Menschen vermeinen, werden geisteswissenschaft­liche Vorstellungen unter dem Zwange gerade naturwissenschaftlicher Tatsachen sich in unsere Zeitgenossen einieben müssen."
      ],
      [
        "Denn noch nicht lange ist es her, da hatte ich mit einem Philosophen gesprochen, der viel auf materialistische Vorstellungen hielt und aus seinen ma­terialistischen Vorstellungen heraus mir sagte: ,,Das Bild des Kentau-ren ist natürlich so entstanden: Die alten Bewohner Griecheniands sahen gewisse Völkerschaften auf ihren Pferden vom Norden kom­men, und da es meistens neblig war, so hatten sie die Vorstellung, dass Reiter und Pferd eine einzige Gestalt seien.",
        "In ihrem Aberglauben konnten sie sich das leicht einbilden.\""
      ],
      [
        "In der Tat eine recht einfache Vorstellung, wenig philosophisch vielleicht, aber doch recht einfach!",
        "Diese Vorstellung des Kentauren, die nicht dadurch entstanden ist, dass die Griechen nicht haben unter­scheiden können den Reiter von seinem Pferd, sondern die dadurch entstanden ist, dass die älteren Völker wirklich die geistige Wesenheit"
      ],
      [
        "des Menschen selbständig zu der physischen Natur haben denken müssen - diese Vorstellung taucht wieder auf in unserer Zeit, ganz selbständig aus naturwissenschaftlichen Vorstellungen heraus.",
        "So müssen wir sagen, wir sind heute schon trotz aller materialistischen Vorstellungen auf dem Wege, dass selbst der Materialismus, wenn er nur auf Tatsachen sich stützen will, nach und nach zu dem hinführt, was die Geisteswissenschaft aus ihren okkulten Quellen heraus zu sagen hat."
      ],
      [
        "Wollen wir aber eine solche Gestalt wie Gilgamesch, die ja auch der äusseren Forschung jetzt schon nahegetreten ist, so wie wir das für unsere Betrachtungen tun müssen, an die Spitze der okkulten Betrachtung stellen, dann müssen wir uns klar sein, dass wir es da zu tun haben mit einem Hereinwirken eines Wesens der höheren geistigen Hierarchien.",
        "So dass, wenn wir eigentlich jeden Menschen in bezug auf seine Geistigkeit hin im Bild des Kentauren anschauen müssen, wir bei einem solchen Menschen, der so wirkt wie Gilgamesch, noch insbesondere annehmen müssen, dass das Geistige des Kentauren dirigiert wird von höheren Mächten, die ihre Kräfte hereinsenden in den Fortschritt der Menschheit."
      ],
      [
        "Und wir werden sehen, wenn wir noch weiter hinaufgehen in der Geschichte, dass sich uns das noch deutlicher darstellen wird.",
        "Wir werden weiter sehen, wie sich das dann modifiziert bis in unsere Gegenwart herein und wie geistige Kräfte immer andere Gestalten annehmen, wenn sie durch Menschen wirken, je mehr wir in unsere unmittelbare Gegen­wart hereinkommen."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "III",
    "paragraphs": [
      "Einiges von dem, was bis jetzt als skizzenhafter Einblick in den okkulten Verlauf der menschlichen Entwicklung gesagt worden ist, wird Sie ja schon hinweisen darauf, dass der Verlauf der Inkarnationen, wie er durch den individuellen Charakter und die individuelle Ent-wicklung der Menschen selbst gegeben ist, durch das Eingreifen geistiger Kräfte aus den höheren Hierarchien modifiziert wird. Rein­karnation ist eben kein ganz so einfaches Geschehen in der Mensch­heitsentwicklung, wie man es gerne aus einer gewissen theoretischen Bequemlichkeit heraus annehmen möchte.",
      "Gewiss, die Tatsache liegt vor, dass der Mensch sich immer wieder verkörpert, dass das, was wir seinen Wesenskern nennen, in immer neuer Inkarnation erscheint; und ebenso ist es wahr, dass ein Ursachenzusammenhang ist zwischen den Leben, die später als Inkarnationen auftreten, und den früheren Leben. Auch das Gesetz des Karma liegt vor, das sozusagen der Aus-druck ist dieses Ursachenzusammenhanges.",
      "Darüber hinausgehend aber gibt es etwas anderes, und dieses andere führt uns erst zum Ver­ständnis des historischen Entwicklungsganges der Menschheit. Die Entwicklung der Menschheit würde ganz anders ablaufen, wenn nichts anderes in Betracht käme als die Ursachenzusanunenhänge zwischen einer und der nächsten oder zwischen vorhergehenden und nach­folgenden Inkarnationen des Menschen.",
      "Fortwährend aber greifen in das menschliche Leben in jeder Inkarnation mehr oder weniger - und insbesondere bei historisch führenden Persönlichkeiten - ganz bedeut­same andere Kräfte ein und bedienen sich des Menschen als eines Werkzeuges. Daraus kann geschlossen werden, dass der eigentliche, rein im Menschen selbst liegende karraische Verlauf des Lebens durch die Inkarnationen hindurch modifiziert wird; und das ist aucb der Fall.",
      "Nun kann man von einer gewissen Gesetzmässigkeit sprechen -wir wollen uns zunächst nur auf die nachatlantischen Zeiten beschrän­ken -, von einer Gesetzmässigkeit, wie in den nachatlantischen Zeiten bis in unsere Gegenwart herein die Einflüsse anderer Welten und das individuelle Karma des Menschen zusammenhängen. Und es geht nicht anders, als durch eine schematische Zeichnung Ihnen klar­zumachen, wie diese Einflüsse sich gestalten und wie sie sich zu der Individualität des Menschen stellen. Stellen wir uns einmal vor:",
      "Diese hier in der Mitte der Tafel gezeichnete Fläche soll dasjenige sein, was wir gewöhnt sind, das menschliche Ich zu nennen, un­seren gegenwärtigen menschlichen Wesenskern. (Siehe Seite 5 z.) Und zeichnen wir nun die anderen Wesensglieder des Menschen ein, indem wir zunächst absehen von der Gliederung der Seele in Emp­findungsseele, Verstandesseele und Bewusstseinsseele. Also haben wir hier schematisch dargestellt den Astralleib, den Ätherleib, den phy­sischen Leib.",
      "Nun wollen wir, weil wir bei der nachatlantischen Entwicklung bleiben wollen, uns klarmachen, worin denn die Zukunft des Men­schen, nach dem, was wir schon an den verschiedenen Orten bespro­chen haben, zunächst bestehen wird. Wir wissen ja, dass wir mitten drinnen stehen in der nachatlantischen Entwicklung, die eigentliche Mitte allerdings schon etwas überschritten haben. Es braucht hier nur kurz wiederholt zu werden, was bei anderen Gelegenheiten gesagt worden ist: dass innerhalb der griechisch4ateinischen Kultur-epoche vorzugsweise dasjenige zu einer besonderen Entwicklung gekommen ist, was wir nennen die Verstandes- oder Gemütsseele, und dass wir jetzt in der Entwicklung der Bewusstseinsseele stehen. In der babylonisch-ägyptischen Kulturperiode ist die Empfindungs­seele zur Entwicklung gekommen; vorher in der persischen Ent­wicklungsepoche der Empfindungs- oder Astralleib und in der uralt-indischen Entwicklung der Ätherleib des Menschen. Die Anpassung des physischen Leibes an unsere nachatlantischen irdischen Verhält­nisse ist schon in den letzten Epochen vor der grossen atlantischen Katastrophe geschehen. So dass, wenn wir jetzt übergehen dazu, auch die anderen Glieder einzuzeichnen, wir sagen können: Es entwickelt",
      "sich das Ich innerhalb unserer nachatlantischen Zeit so, dass die Entwicklung während der indischen Periode vorzugsweise im Ätherleib verläuft, die der persischen im Astralleib, die der ägyptisch­chaldäischen in der Empfindungsseele, die der griechischen in der Verstandesseele und unsere Kultur in der Bewusstseinsseele, - in dem fünften Gliede des Menschen, wenn wir die einzelnen Seelenglieder rechnen. In einem sechsten Kulturzeitraum werden die Menschen sich weiter hinaufentwickeln, und es wird in gewisser Art herein­wachsen das Seelenhafte des Menschen in Manas; in einer siebenten, der letzten nachatlantischen Kulturepoche, wird dann zur Entwick­lung kommen eine Art Hineinwachsen des Menschen in den Lebens-geist oder die Buddhi; und es wird das, was hineinwachsen könnte in Atma, nach der grossen Katastrophe, die unsere nachadantische Zeit abschliessen wird, erst in einem späteren Zeitalter sich ent­wickeln.",
      "Das sind Dinge, die bekannt sind aus dem Zyklus über die Apo­kalypse. Jetzt aber müssen wir darauf Rücksicht nehmen, dass für den ersten Zeitraum, den indischen, der Mensch in bezug auf seine Entwicklung noch unterhalb dessen war, worin das Ich lebt; dass im Grunde genommen die alt-indische, die vorvedische Kultur eine im wesentlichen inspirierte Kultur war, das heisst also eine Kultur, welche gleichsam in die menschliche Seele einfioss ohne jene Arbeit des Ich, welche wir heute als unsere Gedanken- und Vorstellungs-arbeit kennen. Der Mensch muss sich seit der ägyptischen Kultur-periode sozusagen aktiv verhalten mit seinem Ich. Er muss sein Ich durch die Sinne herumwenden in dem Umkreis der Aussenwelt, damit er Eindrücke empfängt; er muss gewissermassen bei dem Sich­Fortarbeiten mit seinem eigenen Anteil aktiv dabei sein. Die alt-indische Kultur war eine mehr passive Kultur, eine Kultur, die so­zusagen errungen wurde durch eine Hingabe an das, was wie eine Inspiration in die menschliche Wesenheit hereinfloss. Daher wird es auch begreiflich erscheinen, dass wir diese altindische Kultur auf eine andere Tätigkeit zurückzuführen haben als diejenige, die heute das menschliche Ich ausführt; dass sozusagen die heutige Tätigkeit des Ich für die damalige indische Seele dadurch ersetzt werden musste,",
      "dass sich in die menschliche Wesenheit höhere Wesenheiten hinein-senkten und die menschliche Seele inspirierten.",
      "Wenn wir fragen, was damals sozusagen von aussen her in diese menschliche Seele hineingebracht wurde, was hineingesenkt wurde",
      "von Wesenheiten der höheren Hierarchien, dann können wir sagen:",
      "Es ist dasselbe, was später einmal der Mensch erringen wird als seine eigene Tätigkeit, als seine eigene Aktivität, wenn er sich empor­gehoben haben wird zu dem, was wir als Atma oder Geistesmensch bezeichnen. Mit anderen Worten, es wird sich in der Zukunft die menschliche Individualität zu einem Einarbeiten in Atma empor­heben. Dieses Einarbeiten wird eine Eigenarbeit der menschlichen Seele, des menschlichen Wesenskernes sein, etwas, was mit dem innersten Wesen unmittelbar verbunden ist. Und so wie dann der Mensch selbst in sich arbeiten wird, so arbeiteten Wesenheiten höherer Hierarchien an der indischen Seele. Wenn wir beschreiben wollen, was in den Ätherleibern der indischen Seelen vorging, so können wir sagen: Es arbeitete gleichsam noch ein verdunkeltes, im Dämmerschlummer",
      "liegendes Ichbewusstsein, es arbeitete Atma im Ätherleib. Wir können ganz gut sagen, dass die alte indische Seele ein Schau­platz war, auf dem sich im Grunde genommen eine übermenschliche Arbeit abspielte: ein Arbeiten höherer Wesenheiten innerhalb des Ätherleibes der alten Inder.",
      "Und das, was da hineinverwoben wurde in den Ätherleib, war eine Arbeit, wie sie der Mensch später in der angedeuteten Weise erreichen wird, wenn Atma am Ätherleib ar­beitet. - In der persischen Kultur war es dann so, dass Buddhi oder der Lebensgeist im Astralleib, im Empfindungsleib arbeitete. - Und in der chaldäisch-babylonisch-ägyptischen Kultur arbeitete dann Manas oder Geistselbst in der Empfindungsseele. So also ist in der ägyptisch-babylonisch-chaldäischen Kultur immer noch nicht aus­geprägt ein volles aktives Arbeiten des Ich innerhalb der Seele selbst.",
      "Der Mensch ist, wenn auch in geringerem Grade als vorher, doch noch ein passiver Schauplatz für eine Arbeit des Manas in der Emp­findungsseele. Erst in der griechisch-lateinischen Zeit tritt sozusagen der Mensch voll aktiv in sein eigenes Seelenleben ein.",
      "Wir wissen ja, dass es die Verstandesseele ist, in der sich das Ich als selbständiges inneres menschliches Glied zuerst geltend macht, und wir können deshalb sagen: Innerhalb der griechischen Kultur arbeitet in der Tat das Ich im Ich, das heisst, der Mensch als solcher im Menschen. Wir werden noch sehen im Verlaufe dieser Vorträge, dass innerhalb der griechischen Epoche das Eigenartige der darnaligen Kultur gerade dadurch hervortritt, dass das Ich im Ich arbeitet.",
      "Jetzt aber sind wir schon seit geraumer Zeit über diese Kultur-epoche hinaus; und während es in der vorgriechischen Zeit so war, dass gewissermassen höhere Wesenheiten sich hineinversenkten in den menschlichen Wesenskern und darin arbeiteten, haben wir in unserer Zeit eine entgegengesetzte Aufgabe zu erfüllen. Wir müssen das, was wir durch unser Ich erarbeitet haben, was wir imstande sind, durch unsere Aktivität aus den Eindrücken der Aussenwelt in uns aufzunehmen, zunächst auf ganz menschliche Art erwerben können. Dann aber dürfen wir nicht stehenbleiben bei dem Stand­punkte, bei dem die Menschen der griechisch4ateinischen Zeit stehen­geblieben sind, indem wir nur das Menschliche, das reine Menschentum",
      "als solches herausarbeiten. Sondern das, was wir uns erarbeiten, müssen wir hinauftragen und es einverweben dem, was da kommen soll; wir müssen sozusagen die Richtung hinauf nehmen nach dem, was später kommen soll: Manas oder Geistselbst.",
      "Das ist aber erst in der sechsten Kulturperiode zu erwarten. Jetzt stehen wir zwischen der vierten und sechsten. Die sechste verspricht der Menschheit, dass die Menschheit in der Lage sein werde, hinaufzutragen in höhere Regionen das, was erarbeitet wird durch die äusseren Eindrücke, die das Ich durch seine Sinne empfängt.",
      "In unserer fünften Kultur-epoche sind wir nur in der Lage, sozusagen den Ansturm zu unter­nehmen, alles das, was wir uns erarbeiten an äusseren Eindrücken und was wir erlangen durch Verarbeitung dieser Eindrücke, so aus­zuprägen, dass es die Richtung nach oben empfangen kann. Wir leben in dieser Beziehung wahrhaftig in einer Übergangsepoche, und wenn Sie sich daran erinnern, was gestern über die in der Jungfrau von Orleans wirksame geistige Macht gesagt worden ist, so werden Sie sehen, dass schon in der Jungfrau von Orleans etwas von dem wirkte, was sich in entgegengesetzter Richtung bewegt als die Einwirkungen höherer Mächte in der vorgriechischen Zeit.",
      "Wenn, sagen wir, irgend-ein Angehöriger der persischen Kultur den Einfluss einer übersinn­lichen Macht empfing, die sich seiner als Werkzeug bediente, so wirkte eben diese Macht in seinen menschlichen Wesenskern herein; sie lebte sich da aus, und der Mensch schaute, erlebte das, was ihm diese geistige Macht empflanzte, womit sie ihn inspirierte. Der Mensch unserer Zeit kann, wenn er zu solchen geistigen Mächten in Beziehung tritt, das, was er in der physischen Welt durch die Arbeit seines Ich, durch die Eindrücke seines Ich erlebt, sozusagen hinauftragen, er kann ihm die Richtung nach oben geben.",
      "Daher ist es bei solchen Persönlichkeiten wie bei der Jungfrau von Orleans so, dass sich die Kundgebungen, die Manifestationen jener geistigen Mächte, die zu ihr sprechen wollen, zwar in der Sphäre befinden, bis zu welcher sie aufragt, dass sich aber vor diese Offenbarung etwas hinstellt, was zwar nicht die Realität dieser Offenbarungen beeinträchtigt, was ihnen aber eine bestimmte Gestalt gibt; es ist das, was das Ich hier in der physischen Welt erlebt. Mit anderen Worten: die Jungfrau von",
      "Orleans hat Offenbarungen, aber sie kann sie nicht so unmittelbar sehen wie die Alten, sondern es stellt sich zwischen sie in ihrer Ichheit und diese objektiven Mächte die Vorstellungswelt hinein, welche die Jungfrau von Orleans aufgenommen hat in der physischen Welt:",
      "das Bild der Jungfrau Maria, des Erzengels Michael, so wie sie sie aufgenommen hat aus ihren christlichen Vorstellungen; die stellen sich dazwischen.",
      "Da haben wir zu gleicher Zeit ein Beispiel, wie wir unterscheiden müssen, wenn es sich um spirituelle Dinge handelt, zwischen der Objektivität einer Offenbarung und der Objektivität eines Bewusst­seinsinhaltes. Die Jungfrau von Orleans sah die Jungfrau Maria und den Erzengel Michael in einem gewissen Bilde.",
      "Diese Bilder dürfen wir uns nicht unmittelbar in die spirituelle Realität hineindenken; der Gestalt dieser Bilder dürfen wir nicht unmittelbare Objektivität zuschreiben. Wenn aber jemand sagen würde, es sei nur eine Ein­bildung, so ist das Unsinn.",
      "Denn es kommen der Jungfrau Offen­barungen aus der geistigen Welt entgegen, die der Mensch in der Gestalt, wie er sie sehen soll in der nachatiantischen Periode - aller­dings erst in der sechsten Kulturepoche - wird sehen können. Aber wenn auch die Jungfrau von Orleans die wahre Gestalt nicht sieht, so senkt sich diese wahre Gestalt doch auf sie nieder.",
      "Die Jungfrau von Orleans bringt ihr die religiösen Vorstellungen ihrer Zeit ent­gegen, sie deckt sie gleichsam zu; es wird aus ihr herausgefordert ihre Vorstellungswelt durch die spirituelle Macht. So ist also die Offenbarung als objektiv anzusprechen.",
      "Wenn auch in unserer Zeit irgend jemand nachweisen kann, dass bei einer Kundgebung aus der geistigen Welt subjektive Elemente einfliessen, wenn wir das Bild, das sich der Betreffende macht von der spirituellen Welt, nicht als objektiv ansehen können, wenn das auch ein Schleier ist - so dürfen wir deshalb doch nicht die objektiven Offenbarungen als solche Schleier deuten. Sie sind objektiv.",
      "Sie zaubern aus unserer eigenen Seele den Inhalt heraus. Wir müssen unterscheiden zwischen det Objektivität des Inhaltes und der der Tatsachen, die aus der geistigen Welt kommen. - Ich musste das insbesondere deshalb betonen, weil auf diesem Felde sowohl von denen, welche die spirituelle Welt anerkennen,",
      "wie auch von den Gegnern zwar entgegengesetzte, aber doch überall Fehler gemacht werden. -",
      "So also stellt uns gleichsam die Jungfrau von Orleans eine histo­rische Persönlichkeit dar, die schon ganz in dem Sinne unserer Epoche wirkt, wo ja zum Geistigen hinaufgerichtet sein muss alles das, was wir sozusagen produzieren können auf Grundiage unserer äusseren Eindrücke. Was heisst das aber, wenn wir es anwenden auf unsere Kultur? Das heisst: Wir mögen den Blick hinauswenden zunächst naiv auf unsere Umgebung. Wenn wir aber dabei bleiben, das Auge bloss auf die äusseren Eindrücke zu richten, dann tun wir nicht unsere Schuldigkeit. Wir tun sie nur dann, wenn wir uns bewusst sind, dass wir die äusseren Eindrücke beziehen müssen auf hinter ihnen stehende geistige Mächte. Wenn wir Wissenschaft treiben und machen es so wie die Gelehrsamkeit, dann tun wir nicht unsere Schuldigkeit. Wir müssen alles das, was wir erfahren können über die Gesetze der Naturerscheinungen, über die Gesetze der Seelenerscheinungen so betrachten, dass wir es wie eine Sprache anschauen, die uns hinauf-führen soll in eine göttlich-geistige Offenbarung. Wenn wir das Bewusstsein haben, dass wir alle physikalischen, chemischen, bio­logischen, physiologischen, psychologischen Gesetze so betrachten sollen, dass wir sie auf etwas Geistiges beziehen, was sich uns offen­bart, dann tun wir unsere Schuldigkeit.",
      "So ist es in bezug auf die Wissenschaften unserer Zeit, und so ist es mit der Kunst. Diejenige Kunst, die wir charakterisieren als die griechische Kunst, die sozusagen emfacher auf den Menschen reflek­tierte, die ganz und gar darstellte das bloss Menschliche, das Arbeiten des Ich mit dem Ich, insoweit sich das Ich im sinnlich-physischen Material ausdrückt, diese Kunst hat ihre Epochen gehabt. In unserer Zeit ist bei den wirklich grossen künstierischen Persönlichkeiten wie instinktiv der Drang entstanden, die Kunst zu einer Art von Opferdienst für die göttlich-geistigen Welten zu gestalten, das heisst das, was zum Beispiel in Töne gekleidet wird, anzusehen als eine Interpretation geistiger Mysterien. So wird man kulturhistorisch­okkult einmal anzuschauen haben bis in alle Einzelheiten hinein Richard Wagner. So wird man gerade ihn anzusehen haben als einen",
      "reprasentativen Menschen unseres, des fünften Kulturzeitraumes, der den Drang immer gefühlt hat, auszudrücken in dem, was in ihm in Tönen lebte, den Zug nach der spirituellen Welt, der das Kunstwerk als eine äussere Sprache der spirituellen Welt betrachtete. Und da stehen im Grunde genommen die Überbleibsel der alten Kultur und die Morgenröte einer neuen Kultur scharf, schroff selbst, in unserer Zeit sich gegenüber. Haben wir doch gesehen, wie sozusagen das rein menschliche Weben in den Tönen, die rein formale Musik, die Richard Wagner überwinden wollte, in heftiger Weise von den Gegnern Richard Wagners verteidigt wurde, weil sie nicht imstande waren, zu fühlen, dass gerade bei Richard Wagner ein neuer Impuls instinktiv wie eine Morgenröte aufging.",
      "Ich weiss nicht, ob die meisten von Ihnen wissen, dass Richard Wagner lange Zeit hindurch die herbsten, die furchtbarsten Kritiker und Ablehner gefunden hat. Diese Kritiker und Ablehner haben eine gewisse Art von Anführung gehabt in dem ausserordentlich geist­vollen musikalischen Schaffen Eduard Hanslicks in Wien, der das interessante Bücheichen ,,Vom musikalisch Schönen\" geschrieben hat.",
      "Ich weiss nicht, ob Sie wissen, dass damit dem Neuaufgehen einer historischen Morgenröte das Alte sozusagen entgegengestellt war. Dieses Buch ,,Vom musikalisch Schönen\" kann ein historisches Denkmal für die spätesten Zeiten werden.",
      "Denn was wollte Hanslick? Er sagt: Man kann nicht in dieser Weise Musik machen wie Richard Wagner; das ist gar keine Musik, denn da nimmt die Musik sozusagen den Anlauf, auf etwas hinweisen zu wollen, was ausserhalb des Musikalischen steht, auf etwas Übersinnliches.",
      "Musik sei aber ,,Ara­beske in Tönen\" - das war ein Lieblingswort des Hanslick. Das heisst, eine arabeskenartige Aneinanderfügung von Tönen, und der musi­kalisch-ästhetische Genuss kann darin bestehen, sich rein menschlich zu erfreuen an der Art und Weise, wie die Töne ineinander und nach­einander erklingen.",
      "Hanslick sagte, Richard Wagner sei überhaupt kein Musiker, er verstehe gar nicht das Wesen des Musikalischen. Das Wesen der Musik müsse liegen in einer blossen Architektonik des Tonmaterials. - Was kann man über eine solche Erscheinung sagen?",
      "Nichts anderes, als dass Hanslick im eminentesten Sinne ein",
      "Nachzügler, ein Reaktionär der vierten Kulturepoche war. Da hatte er recht - für diese Kulturepoche; aber was für eine Kulturepoche richtig ist, gilt nicht mehr für die nächste. Man kann von seinem Standpunkt aus sagen, Richard Wagner sei kein Musiker. Dann aber müsste man weiter sagen: Es ist diese Epoche jetzt vorbei, wir müssen uns nun mit dem zufriedengeben, was aus dieser Epoche stammt, wir müssen uns versöhnen damit, dass sich das im Hanslickschen Sinne Musikalische erweitert über sich selbst hinaus zu einem Neuen.",
      "Und so könnten wir auf mancherlei Gebieten diesen Zusammen­stoss des Alten und des Neuen gerade in unserer Kulturepoche studieren. Ausserordentlich interessant ist das insbesondere in den einzelnen Zweigen der Wissenschaft. Es würde viel zu weit führen, wenn wir zeigen wollten, wie es da überall Reaktionäre gibt und solche, die herausarbeiten aus den einzelnen Wissenschaften, was die Wissenschaft werden soll: der Ausdruck eines hinter den Erscheinun­gen stehenden Göttlich-Geistigen. Das Grundelement, von dem sich die Gegenwart durchdringen muss, um immer bewusster das Göttlich-Geistige zum Zielpunkte, zum Perspektivpunkt für unsere Arbeit zu machen, das soll eben die Geisteswissenschaft sein, und die Geistes­wissenschaft soll überall erwecken die Impulse von unten nach oben; sie soll überall die menschlichen Seelen auffordern zum Opfer, das heisst zum Opfern dessen, was wir durch die äusseren Eindrücke erwerben, gegenüber dem, was wir erreichen sollen im Hinauf­arbeiten in die Regionen des Geistselbstes, Lebensgeistes und Geistes­menschen.",
      "Wenn wir dieses Bild der menschlichen Geschichte, der okkulten Geschichte uns vor Augen stellen, dann werden wir es begreiflich finden, dass eine Seele, die in der indischen und dann in der persischen Epoche inkarniert war, durchdrungen sein konnte von dem inspirieren­den Elemente einer Individualität der höheren Hierarchien; dass dann aber, als sie eintrat in die grechisch-lateinische Zeit, diese Seele mit sich allein war, dass diese Seele so arbeitete, dass Ich im Ich eben arbeitete. Alles das, was in der vorgriechischen Epoche für alle einzelnen Zyklen der nachatlantischen Kulturen wie eine göttliche Eingebung, wie eine Offenbarung von oben erscheint - und es gilt",
      "das auch noch im Beginne der griechischen Kulturperiode für das neunte, zehnte, elfte Jahrhundert der vorchristlichen Zeit -, was sich uns darstellt als eine inspirierte Kultur, in die von aussen einifiesst, was sie geistig erhalten soll, das gestaltet sich immer mehr und mehr dazu, rein menschlich-persönlich sich darzuleben. Und am stärksten findet das seinen Ausdruck gerade eben im Griechentum.",
      "Einen solchen Ausdruck des äusseren Menschen, wie er sich in der physi­schen Welt darlebt, für das, was der Mensch als auf sich gestellte Ichwesenheit ist, hat keine Zeit vorher gesehen und wird keine Zeit nachher wieder sehen können. Das rein Menschlich-Persönliche, das ganz in sich abgeschlossene Menschlich-Persönliche tritt in der an­tiken Lebensweise des Griechen und in seinen Schöpfungen historisch zutage.",
      "Vergleichen wir, wie in seine Göttergestalten der griechische Plastiker hineingeheimnisst hat das Menschlich-Persönliche! Wir kön­nen sagen: So wie uns ein griechisches plastisches Kunstwerk ent­gegentritt, soweit es durch physische Mittel zu erkennen ist, so steht der Mensch ganz als Persöniichkeit vor uns.",
      "Und wenn wir bei den Kunstwerken der Griechen nicht vergessen könnten, dass dieser Inkarnation, die uns da ausgedrückt wird, andere Inkarnationen vor-angingen und andere folgen werden, wenn wir nur einen Augenblick denken würden, dass der Apollogestalt und Zeusgestalt nur eine einzelne Inkarnation aus vielen zugrundeliegt, so würden wir nicht richtig empfinden dem griechischen Kunstwerk gegenüber. Da müssen wir vergessen können, dass der Mensch in aufeinanderfolgenden Inkarnationen sich verkörperte.",
      "Da ist die Persönlichkeit ganz hinein-gegossen in die Form der einen Persönlichkeit. Und so war das ganze Leben der Griechen.",
      "Gehen wir dagegen weiter zurück, da werden die Gestalten symbolisch; da deuten die Gestalten etwas an, was nicht rein mensch­lich ist, da drücken sie etwas aus, was der Mensch noch nicht in sich selber fühlt. Da konnte er nur in Symbolen ausdrücken, was herein­kam aus göttlich-geistigen Welten. Daher die alte symbolisierende Kunst. - Und sehen wir wiederum, wie die Kunst herauf kommt gerade zu dem Volk, welches das Material hergeben soll zu unserem, zum fünften Kulturzeitraurn - wir brauchen uns da nur die ältere",
      "deutsche Kunst zu vergegenwärtigen -, da sehen wir, wie wir es nicht mit einer Symbolik, aber auch nicht mit einer Ausprägung des rem Menschlichen zu tun haben, sondern mit dem in sich vertieften Seelischen; wir sehen, wie da das Seelische sozusagen nicht ganz hineinkann in die Menschengestalt. Wer könnte gerade die Gestalten Albrecht Dürers anders charakterisieren, als dass bei ihnen dasjenige, was nach der übersinnlichen Welt im Menschen verlangt, man möchte sagen im griechischen Sinne genommen nur einen unvoll­kommenen Ausdruck findet in der äusseren Ausgestaltung derKörper­lichkeit. Daher die Vertiefung nach dem Seelischen, je weiter die Kunst heraufkommt.",
      "Und jetzt werden Sie es nicht mehr unbegreiffich finden, dass ich in der ersten Stunde sagte: Es erscheint in der physischen Welt das, was früher verkörpert war, wie ein Abbild; in die Individualität flossen herein Wesenheiten der höheren Hierarchien. So dass, wenn wir von einem Menschen der griechischen Welt in früheren Zeiten sagen müssen, er war inkarniert -, wir nicht nur diese in sich geschlossene Wesenheit sehen müssen, sondern hinter ihr stehend die Individualität einer höheren Hierarchie.",
      "So tritt uns in der griechisch-lateinischen Periode Alexander, so tritt uns Aristoteles gegenüber. Wir verfolgen ihre Individualitäten nach rückwärts. Da müssen wir von Alexander zurückgehen zu Gilgamesch und sagen: Bei Gilgamesch ist diese Individualität, die dann wie auf den physischen Plan herausprojiziert als Alexander erscheint; hinter ihr müssen wir einen Feuergeist sehen, der sich seiner als Werkzeug bedient.",
      "Und bei Aristoteles sehen wir, zurückgehend in der Zeit, die Mächte des alten Hellsehens wirken in dem Freunde des Gilgamesch. So also sehen wir sowohl junge wie alte Seelen, hinter denen früher Hellsichtigkeit stand, ganz heraus­gestellt in der griechischen Zeit auf den physischen Plan.",
      "Und so tritt uns das ganz besonders bei der grossen Mathematikerin Hypatia entgegen, bei der sozusagen die ganze mathematische und philo­sophische Weisheit ihrer Zeit als persönliches Können, als persöniiche Wissenschaft und Weisheit lebte. Das war abgeschlossen in der Per­sönlichkeit der Hypatia.",
      "Und wir werden noch sehen, wie diese Individualität gerade die weibliche Persönlichkeit annehmen musste,",
      "um eine so weiche Zusammengeschlossenheit alles dessen auszu­prägen, was sie früher aufgenommen hatte in den orphischen My­sterien, - um alles das als persönliche Wirkungsweise auszuprägen, was sie dort vermittelst der Inspiratoren als ein Schüler der orphischen Mysterien aufgenommen hatte.",
      "So sehen wir also, wie in aufeinanderfolgende Menschheitsinkarna­tionen Einflüsse aus der geistigen Welt modifizierend eintreten. Und nur hinweisen kann ich darauf, dass gerade eine solche Individualität wie diejenige, die als Hypatia inkarniert war, die also mitbrachte die Weisheit der orphischen Mysterien und sie persönlich auslebte, dann in einer nachfolgenden Inkarnation berufen war, nun den umgekehr­ten Weg einzuschlagen: alle persönliche Weisheit wiederum hinauf-zutragen zum Göttlich-Geistigen. Daher erscheint Hypatia ungefähr um die Wende des 12. und 13 Jahrhunderts als ein bedeutender, um­fassender, universeller Geist der neueren Geschichte, der einen grossen Einfluss hat auf das, was Zusammenfassung des naturwissenschaft­lichen und auch des philosophischen Erkennens ist. So also sehen wir, wie hineindringen in die aufeinanderfolgenden Inkarnationen der einzelnen Individualitäten die historischen Mächte.",
      "Wenn wir so den Verlauf der Geschichte betrachten, dann sehen wir wirklich eine Art Niederstieg aus geistigen Höhen bis in die griechisch-lateinische Zeit und dann wiederum einen Aufstieg: ein Aufsammeln des rein vom physischen Plan zu gewinnenden Materials während der griechischen Zeit - das dauert natürlich herein bis in unsere Zeit - und ein Wiederhinauftragen in die geistige Welt, zu dem ein Impuls geschaffen werden soll durch die Geisteswissenschaft, und wozu schon einen instinktiven Impuls gehabt hat eine solche Per­sönlichkeit wie Hypatia, die im ,3. Jahrhundert wieder verkörpert war.",
      "Ich möchte an dieser Stelle, meine lieben Freunde, weil die all­gemeine Theosophische Gesellschaft in gewisser Beziehung ein Tummelplatz ist von Missverständnissen, - ich möchte hinweisen darauf, dass wirklich unendlich viel von diesen Missverständnissen wie rein aus den Fingern gesogen ist. So will man gerne dasjenige, was zum Beispiel hier vorgetragen wird innerhalb unserer deutschen Bewegung, in einen gewissen Gegensatz bringen zu dem, was ursprünglich",
      "die Offenbarung der theosophischen Bewegung in der neueren Zeit war. Deshalb ergreife ich gerne die Gelegenheit, darauf hinzuweisen, wie das, was hier aus ursprünglich rosenkreuzerischem Quell gegeben wird, in Harmonie steht mit mancherlei von dem, was gerade ursprünglich der theosophischen Bewegung gegeben worden ist.",
      "Und wir haben ja in diesem Augenblick gerade Gelegen­heit, auf etwas hinzuweisen, was von dieser Art ist. Es ist also von mir gesagt und ganz unabhängig von Traditionen entwickelt worden, dass gewisse spätere historische Persöniichkeiten gleichsam die Schattenbilder sind von früheren, durch die Mythen dargestellten Persönlichkeiten, hinter denen höhere Hierarchien stehen.",
      "Solches darf man nicht in Widerspruch bringen mit denjenigen Manifestatio­nen, die durch H.P. Blavatzky in die theosophische Gesellschaft hineingebracht worden sind. Denn sonst könnte man durch ein reines Missverständnis sich sehr wohl in einen Widerspruch versetzen zu den guten alten Lehren, die durch das ausserordentliche, brauch-bare Instrument von H.P.",
      "Blavatzky der theo sophischen Bewegung zugeflossen sind. Aber in bezug auf das, was hier entwickelt worden ist, möchte ich Ihnen eine Stelle aus den späteren Schriften der Blavatzky vorlesen, wo sie auf die ,,Entschleierte Isis\", ihr ältestes okkultes Werk, hinweist.",
      "Da möchte ich die folgende Stelle Ihnen vorlesen, damit Sie sehen, wie das, was von solchem Widerspruch gesagt wird, im Grunde genommen, ich kann nicht anders sagen, aus den Fingern gesogen ist:",
      ",,Ausser dem beständigen Wiederholen der alten stets bestehenden Tatsache von Reinkarnation und Karma - und zwar in der Art, wie es die älteste Wissenschaft der Welt, nicht der Spiritismus von heute, gelehrt hat - sollten die Okkultisten eine zyklische und mit der Evo­lution Schritt haltende Reinkarnation lehren: jene Art der Wieder­geburt, geheiinnisvoll und noch unverständlich für die vielen, die nichts wissen von jener Geschichte der Welt, auf welche wir vor­sichtig hingewiesen haben in der ,Entschieierten Isis'. Eine allgemeine Wiedergeburt für jedes Individuum mit Zwischenpausen von Kama Loca und Devachan, und eine zyklische bewusste Inkarnation mit einem grossen und göttlichen Ziel für Wenige. Jene grossen Charaktere,",
      "die in der Geschichte der Menschheit gleich Riesen emporragen, wie Siddharta Buddha und Jesus auf geistigem Gebiet, wie Alexander von Mazedonien und Napoleon der Grosse auf dem Gebiete physischer Eroberungen, sind nichts als widergespiegelte Bilder grosser Urbilder, welche existierten - nicht vor zehntausend Jahren, wie in der ,Ent­schleierten Isis' vorsichtig erwähnt wurde -, sondern während Mil­lionen von aufeinanderfolgenden Jahren, vom Beginne des Manvan­tara an. Denn wie oben erklärt wurde - mit Ausnahme der wirklichen Avataras sind diese Abbilder ihrer Urbilder, ein jedes entsprechend seiner eigenen Eltern-Flamme, dieselben ungebrochenen Strahlen (Monaden), genannt Devas, Dhyan Chohans oder Dhyani Buddhas oder auch Planetengeister und so weiter, die durch äonenlange Ewig­keit gleich ihren Urbildern leuchten. Nach ihrem Bilde werden einige Menschen geboren, und wenn irgendein besonderes humanitäres Ziel in Aussicht genommen ist, werden diese letzteren hypostatisch beseelt von ihren göttlichen Urbildern, die immer wieder hervorgebracht werden durch die geheimnisvollen Mächte, welche die Schicksale der Welt leiten und lenken.\"",
      "Mehr durfte nicht gesagt werden zu der Zeit, als die ,,Entschieierte Isis\" geschrieben wurde; deshalb blieb das Gesagte beschränkt auf die blosse Bemerkung, dass ,,es keinen hervorragenden Charakter in den Annalen der heiligen oder profanen Geschichte gibt, dessen Urbild wir nicht finden könnten in den halb sagerthaften und halb realen Überlieferungen vergangener Religionen und Mythologien. So wie der Stern, der in der schrankeniosen Unendlichkeit des Him­mels in unermesslicher Entfernung über unseren Häuptern strahlt, sich spiegelt in den stillen Gewässern eines Sees, so wird wider-gespiegelt das Bild der Menschheit vorsintflutlicher Zeiten in jenen Perioden, die wir mit einem geschichtlichen Rückblick umfassen können...\"",
      "Wie gesagt, ich ergreife gerne die Gelegenheit, um die Überein­stimmung dessen, was wir in unmittelbarer Gegenwart erforschen können, mit dem, was in gewisser Beziehung ursprüngliche Offen­barung war, hervorzuheben. Sie wissen ja, dass es Grundsatz hier ist, in gewisser Hinsicht treu festzuhalten an den Traditionen der theosophischen",
      "Bewegung; dass aber auch nichts ungeprüft hier wieder­holt wird, das betone ich ausdrücklich; darauf kommt es an. Wo eine Übereinstimmung des Erkannten mit anderem betont werden kann, soll es wegen der Kontinuität der Theosophischen Gesellschaft scharf hervorgehoben werden, der Gerechtigkeit gemäss; aber ungeprüft soll nichts einfach wiederholt werden. Das hängt mit der Mission zusammen, die wir gerade innerhalb unserer deutschen theosophi­schen Bewegung haben, - eben den eigenen Einschlag hineinzutragen, den individuellen Einschlag in diese theosophische Bewegung. Aber gerade solche Beispiele können Ihnen ein Bild davon geben, wie un­begründet das Vorurteil ist, das da und dort hervorwächst, als ob wir durchaus in den Dingen immer etwas anderes haben wollten. Wir arbeiten treu weiter, wir kramen nicht sozusagen immerfort die alten Dogmen aus; wir prüfen auch das, was heute von anderer Seite geboten wird. Und wir vertreten das, was mit dem besten okkulten Gewissen gesagt werden kann auf Grundlage der ursprünglichen okkulten Forschungen und der Methoden, die uns überliefert sind durch unsere eigenen heiligen Überlieferungen des Rosenkreuzes.",
      "Es ist nun ausserordentlich interessant, an einer einzelnen Persön­lichkeit zu zeigen, wie gewissermassen das Alte, das in die Mensch­heit hereininspiriert worden ist unter dem Einfluss höherer Mächte, sozusagen einen auf den physischen Plan hingeordneten Charakter bei den Menschen des griechisch-lateinischen Zeitalters angenommen hat. Da können wir als ein Beispiel anführen, wie Eabani in derjenigen seiner Inkarnationen, die zwischen der Persönlichkeit des Eabani und des Aristoteles liegt, unter dem Einfluss der alten Mysterieniehren mit ihren aus den übersinnlichen Welten herabkommenden Kräften auf­nehmen konnte das, worauf eigentlich in gewissen Mysterienschulen die Fortentwicklung der menschlichen Seele beruht. Wir wollen jetzt nicht wiederholen, was Charaktereigentümlichkeit der verschiedenen Mysterienschulen war, wir wollen auf eine Art derselben unseren geistigen Blick richten, auf jene, wo durch die Erregung ganz be­stimmter Gefühle die Seele fortentwickelt wurde, so dass sie ein­dringen lernte in die überphysische Welt. In solchen Mysterien wurden in der Seele namentlich jene Empfindungen, jene Impulse",
      "erregt, die geeignet waren, von Grund aus allen Egoismus auszu­rotten aus der Seele. Es wurde der Seele klargemacht, wie sie im Grunde genommen immer egoistisch sein muss, wenn sie im physi­schen Leibe verkörpert ist. Es wurde der ganze Umfang und die ganze Bedeutung des Egoismus für den physischen Plan sozusagen in Im­pulsen auf die entsprechende Seele abgeladen. Und tief, tief zerknirscht fühlte sich eine solche Seele, die sich sagen musste: Ich habe bisher nichts anderes gekannt als den Egoismus, ich kann ja im physischen Leibe gar nichts anderes sein als ein Egoist. Ja, weit ist eine solche Seele entfernt worden von dem billigen Standpunkte solcher Men­schen, die als jedes zweite Wort im Munde führen: Ich will ja die Sache nicht für mich, sondern für einen andern. Den Egoismus zu überwinden und den Zug nach dem Allgemein-Menschlichen und Kosmischen sich anzueignen, ist nicht so leicht, wie mancher sich vorstellt. Diesem Aneignen muss vorangehen eine völlige Nieder­schmetterung der Seele über den Umfang des Egoismus in den Im­pulsen dieser Seele. Mitleid mit allem Menschlichen, mit allem Kosmi­schen musste die Seele lernen in den Mysterien, die ich da meine, Mitleid durch die Überwindung des physischen Planes. Dann konnte man von ihr hoffen, dass sie wieder heruntertragen würde aus den höheren Welten das wahrhafte Mitgefühl für alles Lebendige und alles Seiende.",
      "Aber noch ein anderes Gefühl sollte namentlich entwickelt werden als ein Hauptgefühl neben mancherlei anderem. Wenn der Mensch eindringen soll in die geistige Welt, dann muss er sich klar sein, dass dort alles anders ist als in der physischen Welt. Wie vor einem völlig Unbekannten muss man stehen, wenn man der geistigen Welt Auge in Auge gegenübertritt. Da ist wirklich das Gefühl vorhanden, durch das man in Gefahr gerät, das Gefühl der Furcht vor dem Unbekannten. Und deshalb musste die Seele in solchen Mysterien durchleben alles, was die Seele des Menschen überhaupt an Furcht und Angst und Schreck und Grauen erleben konnte, um sich abzugewöhnen die Gefühle von Furcht und Angst und Schreck und Grauen. Dann war der Mensch gewappnet, hinaufzusteigen in die ihrem Inhalte nach ihm unbekannte geistige Welt. So musste also die Seele des Schülers",
      "der Mysterien durchgehen durch die Erziehung zum umfassenden universellen Gefühl des Mitleides und zum universellen Gefühl der Furchtlosigkeit. Das machte jede Seele in denjenigen alten Mysterien durch, an denen Eabani teilnahin, als er wieder erschienen war in der Inkarnation, die zwischen Eabani und Aristoteles steht.",
      "Das machte auch er durch. Und nun trat das wie eine Erinnerung an frühere In­karnationen in Aristoteles zutage. Er konnte deshalb die Theorie der Tragödie geben, weil er aus solchen Erinnerungen heraus beim An­schauen der griechischen Tragödie darauf kath, wie in dieser ein Nach­klang ist, gleichsam ein äusseres, auf den physischen Plan heraus­getragenes Nachspiel der Mysterienerziehung, wo die Seele durch Mitleid und Furcht geläutert wird.",
      "So sollte der dramatische Held und der ganze Aufbau einer Tragödie vor den Zuschauern etwas darleben, woran der Zuschauer abgeschwächt erleben kann Mitleid mit dem Schicksal des tragischen Helden und Furcht vor dem Aus­gang seines Schicksals, vor dem schauervollen Tod, der ihm winkt. So war hineinverwoben in den dramatischen Fortgang der Tragödie, in das Weben und Leben der Tragödie, was in der Seele des alten Mysten vorging: die Läuterung, die Reinigung, die Katharsis durch Furcht und Mitleid.",
      "Und wie ein Nachklang sollte auf dem physischen Plan der Angehörige der griechischen Kulturperiode empfinden den Durchgang durch Furcht und Mitleid. Künstlerisch sollte man erleben, ästhetisch geniessen das, was früher ein grosses Erziehungs­prinzip war.",
      "Und als das, was Aristoteles in früheren Inkarnationen gelernt hatte, in seine Persönlichkeit kam, da war er der geeignete Mann, diese eigenartige Definition der Tragödie zu geben, die so klassisch geworden ist und so grossartig gewirkt hat, dass sie im 18. Jahrhundert noch von Lessing aufgenommen wurde und durch das ,9.",
      "Jahrhundert hindurch eine solche Rolle gespielt hat, dass über diese Definition ganze Bibliotheken geschrieben worden sind. Man würde übrigens nicht viel verlieren, wenn der grösste Teil dessen, was in den Bibliotheken liegt, verbrannt würde; denn es wurde mit einem vollständigen Verkennen dessen geschrieben, was vorhin gesagt worden ist, dass wir es nämlich damit zu tun haben, dass in die Kunst etwas herunterprojiziert wird, was im Geistigen liegt.",
      "die das schrieben, ahnten nicht, dass Aristoteles ein altes Mysterien­geheimnis gab, wenn er sagte: Eine Tragödie ist eine Zusammen-fügung aufeinanderfolgender Handlungen, die gruppiert werden um einen Helden und die geeignet sind, im Zuschauer das Gefühl von Furcht und Mitleid zu erregen, damit eine Läuterung in der Seele des Zuschauers eintreten könne.",
      "So sehen wir, dass in einer einzelnen Persönlichkeit, in dem, was sie will und sagt, abschattiert ist, was uns nur dann verständlich wird, wenn wir durch die Persönlichkeit durchblicken auf denjenigen, der dahinter steht, auf den Inspirator. Erst wenn Sie die Geschichte so betrachten, können Sie sehen, was die Persönlichkeit und was die überpersönlichen Mächte für das geschichtliche Leben bedeuten, wie da etwas hereinspielt in die individuellen Inkarnationen, was Frau Blavatzky nennt das Zusammenspiel von persönlichen individuellen Inkarnationen, und dem, was sie schildert, indem sie sagt: ,,Aber neben der alten stets bestehenden Tatsache von Reinkarnation und Karma sollten die Okkultisten eine zyklische und mit der Evolution Schritt haltende Reinkarnation verkünden\" und so weiter. Sie nennt das eine bewusste Reinkarnation, weil für die meisten Menschen doch heute die aufeinanderfolgenden Inkarnationen für das Ich unbewusst bleiben, während die geistigen Mächte, die da von oben hereinwirken, in der Tat mit Bewusstsein ihre Kraft von einem Zeitalter in das andere zyklisch hinübertragen.",
      "Das also, was da steht als eine Offenbarung dessen, was Blavatzky in ihrer ersten Zeit aus den Rosenkreuzermysterien heraus sagte, das ist durchaus zu kontrollieren und festzustellen durch ursprüngliche Forschungen. Daraus aber werden Sie sehen, dass jene bequeme Art, die eine Inkarnation immer nur als die Wirkung einer vorhergehenden Verkörperung auffasst, wesentlich modifiziert wird. Und Sie werden begreifen, dass Reinkarnation eine viel kompliziertere Tatsachenwelt ist als man gewöhnlich aunimmt, und dass wir sie vollkommen nur dann verstehen, wenn wir den Menschen angliedern an eine höhere überphysische Welt, die fortwährend in unsere Welt hereinwirkt. Wir können sagen, dass in jenem Zwischenraum, den wir als die griechisch-lateinische Kultur bezeichnen, dem Menschen Zeit gelassen wurde,",
      "alles das, was aus höheren Welten in die Seele durch lange Inkarna­tionenreihen hindurch gelegt worden war, nachzuempfinden, nach-klingen zu lassen einmal über einem rein menschlichen Ich. Was die griechisch-lateinische Welt auslebte, war wie ein menschlich-persön­liches Ausleben unendlicher Erinnerungen, die früher von höheren Welten in dieselben Individualitäten hineingelegt worden waren. Dürfen wir uns deshalb wundern, wenn die bedeutendsten Geister gerade der griechischen Welt das sich besonders zum Bewusstsein bringen? Sie sagten sich, wenn sie hineinschauten in ihre Innenwelt:",
      "Da strömt es heraus, da dehnen sich Welten in unsere Persönlichkeit hinein; die sind aber Erinnerungen an das, was früher von den geisti­gen Welten hineingegossen worden ist in uns. - Lesen Sie bei Plato, wie er das, was der Mensch erleben kann, zurückführt auf eine Erin­nerung der Seele an ihre vergangenen Erlebnisse. Da sehen Sie, wie aus einem tief realen Bewusstsein der vierten nachatlantischen Epoche heraus ein solcher Geist wie Plato geschöpft hat. Wir lernen erst verstehen, was solch ein einzelner Ausspruch einer so markanten Persönlichkeit bedeutet, wenn wir okkult hineinschauen können in den Geist der Epochen."
    ],
    "sentences": [
      [
        "Einiges von dem, was bis jetzt als skizzenhafter Einblick in den okkulten Verlauf der menschlichen Entwicklung gesagt worden ist, wird Sie ja schon hinweisen darauf, dass der Verlauf der Inkarnationen, wie er durch den individuellen Charakter und die individuelle Ent-wicklung der Menschen selbst gegeben ist, durch das Eingreifen geistiger Kräfte aus den höheren Hierarchien modifiziert wird.",
        "Rein­karnation ist eben kein ganz so einfaches Geschehen in der Mensch­heitsentwicklung, wie man es gerne aus einer gewissen theoretischen Bequemlichkeit heraus annehmen möchte."
      ],
      [
        "Gewiss, die Tatsache liegt vor, dass der Mensch sich immer wieder verkörpert, dass das, was wir seinen Wesenskern nennen, in immer neuer Inkarnation erscheint; und ebenso ist es wahr, dass ein Ursachenzusammenhang ist zwischen den Leben, die später als Inkarnationen auftreten, und den früheren Leben.",
        "Auch das Gesetz des Karma liegt vor, das sozusagen der Aus-druck ist dieses Ursachenzusammenhanges."
      ],
      [
        "Darüber hinausgehend aber gibt es etwas anderes, und dieses andere führt uns erst zum Ver­ständnis des historischen Entwicklungsganges der Menschheit.",
        "Die Entwicklung der Menschheit würde ganz anders ablaufen, wenn nichts anderes in Betracht käme als die Ursachenzusanunenhänge zwischen einer und der nächsten oder zwischen vorhergehenden und nach­folgenden Inkarnationen des Menschen."
      ],
      [
        "Fortwährend aber greifen in das menschliche Leben in jeder Inkarnation mehr oder weniger - und insbesondere bei historisch führenden Persönlichkeiten - ganz bedeut­same andere Kräfte ein und bedienen sich des Menschen als eines Werkzeuges.",
        "Daraus kann geschlossen werden, dass der eigentliche, rein im Menschen selbst liegende karraische Verlauf des Lebens durch die Inkarnationen hindurch modifiziert wird; und das ist aucb der Fall."
      ],
      [
        "Nun kann man von einer gewissen Gesetzmässigkeit sprechen -wir wollen uns zunächst nur auf die nachatlantischen Zeiten beschrän­ken -, von einer Gesetzmässigkeit, wie in den nachatlantischen Zeiten bis in unsere Gegenwart herein die Einflüsse anderer Welten und das individuelle Karma des Menschen zusammenhängen.",
        "Und es geht nicht anders, als durch eine schematische Zeichnung Ihnen klar­zumachen, wie diese Einflüsse sich gestalten und wie sie sich zu der Individualität des Menschen stellen.",
        "Stellen wir uns einmal vor:"
      ],
      [
        "Diese hier in der Mitte der Tafel gezeichnete Fläche soll dasjenige sein, was wir gewöhnt sind, das menschliche Ich zu nennen, un­seren gegenwärtigen menschlichen Wesenskern. (Siehe Seite 5 z.) Und zeichnen wir nun die anderen Wesensglieder des Menschen ein, indem wir zunächst absehen von der Gliederung der Seele in Emp­findungsseele, Verstandesseele und Bewusstseinsseele.",
        "Also haben wir hier schematisch dargestellt den Astralleib, den Ätherleib, den phy­sischen Leib."
      ],
      [
        "Nun wollen wir, weil wir bei der nachatlantischen Entwicklung bleiben wollen, uns klarmachen, worin denn die Zukunft des Men­schen, nach dem, was wir schon an den verschiedenen Orten bespro­chen haben, zunächst bestehen wird.",
        "Wir wissen ja, dass wir mitten drinnen stehen in der nachatlantischen Entwicklung, die eigentliche Mitte allerdings schon etwas überschritten haben.",
        "Es braucht hier nur kurz wiederholt zu werden, was bei anderen Gelegenheiten gesagt worden ist: dass innerhalb der griechisch4ateinischen Kultur-epoche vorzugsweise dasjenige zu einer besonderen Entwicklung gekommen ist, was wir nennen die Verstandes- oder Gemütsseele, und dass wir jetzt in der Entwicklung der Bewusstseinsseele stehen.",
        "In der babylonisch-ägyptischen Kulturperiode ist die Empfindungs­seele zur Entwicklung gekommen; vorher in der persischen Ent­wicklungsepoche der Empfindungs- oder Astralleib und in der uralt-indischen Entwicklung der Ätherleib des Menschen.",
        "Die Anpassung des physischen Leibes an unsere nachatlantischen irdischen Verhält­nisse ist schon in den letzten Epochen vor der grossen atlantischen Katastrophe geschehen.",
        "So dass, wenn wir jetzt übergehen dazu, auch die anderen Glieder einzuzeichnen, wir sagen können: Es entwickelt"
      ],
      [
        "sich das Ich innerhalb unserer nachatlantischen Zeit so, dass die Entwicklung während der indischen Periode vorzugsweise im Ätherleib verläuft, die der persischen im Astralleib, die der ägyptisch­chaldäischen in der Empfindungsseele, die der griechischen in der Verstandesseele und unsere Kultur in der Bewusstseinsseele, - in dem fünften Gliede des Menschen, wenn wir die einzelnen Seelenglieder rechnen.",
        "In einem sechsten Kulturzeitraum werden die Menschen sich weiter hinaufentwickeln, und es wird in gewisser Art herein­wachsen das Seelenhafte des Menschen in Manas; in einer siebenten, der letzten nachatlantischen Kulturepoche, wird dann zur Entwick­lung kommen eine Art Hineinwachsen des Menschen in den Lebens-geist oder die Buddhi; und es wird das, was hineinwachsen könnte in Atma, nach der grossen Katastrophe, die unsere nachadantische Zeit abschliessen wird, erst in einem späteren Zeitalter sich ent­wickeln."
      ],
      [
        "Das sind Dinge, die bekannt sind aus dem Zyklus über die Apo­kalypse.",
        "Jetzt aber müssen wir darauf Rücksicht nehmen, dass für den ersten Zeitraum, den indischen, der Mensch in bezug auf seine Entwicklung noch unterhalb dessen war, worin das Ich lebt; dass im Grunde genommen die alt-indische, die vorvedische Kultur eine im wesentlichen inspirierte Kultur war, das heisst also eine Kultur, welche gleichsam in die menschliche Seele einfioss ohne jene Arbeit des Ich, welche wir heute als unsere Gedanken- und Vorstellungs-arbeit kennen.",
        "Der Mensch muss sich seit der ägyptischen Kultur-periode sozusagen aktiv verhalten mit seinem Ich.",
        "Er muss sein Ich durch die Sinne herumwenden in dem Umkreis der Aussenwelt, damit er Eindrücke empfängt; er muss gewissermassen bei dem Sich­Fortarbeiten mit seinem eigenen Anteil aktiv dabei sein.",
        "Die alt-indische Kultur war eine mehr passive Kultur, eine Kultur, die so­zusagen errungen wurde durch eine Hingabe an das, was wie eine Inspiration in die menschliche Wesenheit hereinfloss.",
        "Daher wird es auch begreiflich erscheinen, dass wir diese altindische Kultur auf eine andere Tätigkeit zurückzuführen haben als diejenige, die heute das menschliche Ich ausführt; dass sozusagen die heutige Tätigkeit des Ich für die damalige indische Seele dadurch ersetzt werden musste,"
      ],
      [
        "dass sich in die menschliche Wesenheit höhere Wesenheiten hinein-senkten und die menschliche Seele inspirierten."
      ],
      [
        "Wenn wir fragen, was damals sozusagen von aussen her in diese menschliche Seele hineingebracht wurde, was hineingesenkt wurde"
      ],
      [
        "von Wesenheiten der höheren Hierarchien, dann können wir sagen:"
      ],
      [
        "Es ist dasselbe, was später einmal der Mensch erringen wird als seine eigene Tätigkeit, als seine eigene Aktivität, wenn er sich empor­gehoben haben wird zu dem, was wir als Atma oder Geistesmensch bezeichnen.",
        "Mit anderen Worten, es wird sich in der Zukunft die menschliche Individualität zu einem Einarbeiten in Atma empor­heben.",
        "Dieses Einarbeiten wird eine Eigenarbeit der menschlichen Seele, des menschlichen Wesenskernes sein, etwas, was mit dem innersten Wesen unmittelbar verbunden ist.",
        "Und so wie dann der Mensch selbst in sich arbeiten wird, so arbeiteten Wesenheiten höherer Hierarchien an der indischen Seele.",
        "Wenn wir beschreiben wollen, was in den Ätherleibern der indischen Seelen vorging, so können wir sagen: Es arbeitete gleichsam noch ein verdunkeltes, im Dämmerschlummer"
      ],
      [
        "liegendes Ichbewusstsein, es arbeitete Atma im Ätherleib.",
        "Wir können ganz gut sagen, dass die alte indische Seele ein Schau­platz war, auf dem sich im Grunde genommen eine übermenschliche Arbeit abspielte: ein Arbeiten höherer Wesenheiten innerhalb des Ätherleibes der alten Inder."
      ],
      [
        "Und das, was da hineinverwoben wurde in den Ätherleib, war eine Arbeit, wie sie der Mensch später in der angedeuteten Weise erreichen wird, wenn Atma am Ätherleib ar­beitet. - In der persischen Kultur war es dann so, dass Buddhi oder der Lebensgeist im Astralleib, im Empfindungsleib arbeitete. - Und in der chaldäisch-babylonisch-ägyptischen Kultur arbeitete dann Manas oder Geistselbst in der Empfindungsseele.",
        "So also ist in der ägyptisch-babylonisch-chaldäischen Kultur immer noch nicht aus­geprägt ein volles aktives Arbeiten des Ich innerhalb der Seele selbst."
      ],
      [
        "Der Mensch ist, wenn auch in geringerem Grade als vorher, doch noch ein passiver Schauplatz für eine Arbeit des Manas in der Emp­findungsseele.",
        "Erst in der griechisch-lateinischen Zeit tritt sozusagen der Mensch voll aktiv in sein eigenes Seelenleben ein."
      ],
      [
        "Wir wissen ja, dass es die Verstandesseele ist, in der sich das Ich als selbständiges inneres menschliches Glied zuerst geltend macht, und wir können deshalb sagen: Innerhalb der griechischen Kultur arbeitet in der Tat das Ich im Ich, das heisst, der Mensch als solcher im Menschen.",
        "Wir werden noch sehen im Verlaufe dieser Vorträge, dass innerhalb der griechischen Epoche das Eigenartige der darnaligen Kultur gerade dadurch hervortritt, dass das Ich im Ich arbeitet."
      ],
      [
        "Jetzt aber sind wir schon seit geraumer Zeit über diese Kultur-epoche hinaus; und während es in der vorgriechischen Zeit so war, dass gewissermassen höhere Wesenheiten sich hineinversenkten in den menschlichen Wesenskern und darin arbeiteten, haben wir in unserer Zeit eine entgegengesetzte Aufgabe zu erfüllen.",
        "Wir müssen das, was wir durch unser Ich erarbeitet haben, was wir imstande sind, durch unsere Aktivität aus den Eindrücken der Aussenwelt in uns aufzunehmen, zunächst auf ganz menschliche Art erwerben können.",
        "Dann aber dürfen wir nicht stehenbleiben bei dem Stand­punkte, bei dem die Menschen der griechisch4ateinischen Zeit stehen­geblieben sind, indem wir nur das Menschliche, das reine Menschentum"
      ],
      [
        "als solches herausarbeiten.",
        "Sondern das, was wir uns erarbeiten, müssen wir hinauftragen und es einverweben dem, was da kommen soll; wir müssen sozusagen die Richtung hinauf nehmen nach dem, was später kommen soll: Manas oder Geistselbst."
      ],
      [
        "Das ist aber erst in der sechsten Kulturperiode zu erwarten.",
        "Jetzt stehen wir zwischen der vierten und sechsten.",
        "Die sechste verspricht der Menschheit, dass die Menschheit in der Lage sein werde, hinaufzutragen in höhere Regionen das, was erarbeitet wird durch die äusseren Eindrücke, die das Ich durch seine Sinne empfängt."
      ],
      [
        "In unserer fünften Kultur-epoche sind wir nur in der Lage, sozusagen den Ansturm zu unter­nehmen, alles das, was wir uns erarbeiten an äusseren Eindrücken und was wir erlangen durch Verarbeitung dieser Eindrücke, so aus­zuprägen, dass es die Richtung nach oben empfangen kann.",
        "Wir leben in dieser Beziehung wahrhaftig in einer Übergangsepoche, und wenn Sie sich daran erinnern, was gestern über die in der Jungfrau von Orleans wirksame geistige Macht gesagt worden ist, so werden Sie sehen, dass schon in der Jungfrau von Orleans etwas von dem wirkte, was sich in entgegengesetzter Richtung bewegt als die Einwirkungen höherer Mächte in der vorgriechischen Zeit."
      ],
      [
        "Wenn, sagen wir, irgend-ein Angehöriger der persischen Kultur den Einfluss einer übersinn­lichen Macht empfing, die sich seiner als Werkzeug bediente, so wirkte eben diese Macht in seinen menschlichen Wesenskern herein; sie lebte sich da aus, und der Mensch schaute, erlebte das, was ihm diese geistige Macht empflanzte, womit sie ihn inspirierte.",
        "Der Mensch unserer Zeit kann, wenn er zu solchen geistigen Mächten in Beziehung tritt, das, was er in der physischen Welt durch die Arbeit seines Ich, durch die Eindrücke seines Ich erlebt, sozusagen hinauftragen, er kann ihm die Richtung nach oben geben."
      ],
      [
        "Daher ist es bei solchen Persönlichkeiten wie bei der Jungfrau von Orleans so, dass sich die Kundgebungen, die Manifestationen jener geistigen Mächte, die zu ihr sprechen wollen, zwar in der Sphäre befinden, bis zu welcher sie aufragt, dass sich aber vor diese Offenbarung etwas hinstellt, was zwar nicht die Realität dieser Offenbarungen beeinträchtigt, was ihnen aber eine bestimmte Gestalt gibt; es ist das, was das Ich hier in der physischen Welt erlebt.",
        "Mit anderen Worten: die Jungfrau von"
      ],
      [
        "Orleans hat Offenbarungen, aber sie kann sie nicht so unmittelbar sehen wie die Alten, sondern es stellt sich zwischen sie in ihrer Ichheit und diese objektiven Mächte die Vorstellungswelt hinein, welche die Jungfrau von Orleans aufgenommen hat in der physischen Welt:"
      ],
      [
        "das Bild der Jungfrau Maria, des Erzengels Michael, so wie sie sie aufgenommen hat aus ihren christlichen Vorstellungen; die stellen sich dazwischen."
      ],
      [
        "Da haben wir zu gleicher Zeit ein Beispiel, wie wir unterscheiden müssen, wenn es sich um spirituelle Dinge handelt, zwischen der Objektivität einer Offenbarung und der Objektivität eines Bewusst­seinsinhaltes.",
        "Die Jungfrau von Orleans sah die Jungfrau Maria und den Erzengel Michael in einem gewissen Bilde."
      ],
      [
        "Diese Bilder dürfen wir uns nicht unmittelbar in die spirituelle Realität hineindenken; der Gestalt dieser Bilder dürfen wir nicht unmittelbare Objektivität zuschreiben.",
        "Wenn aber jemand sagen würde, es sei nur eine Ein­bildung, so ist das Unsinn."
      ],
      [
        "Denn es kommen der Jungfrau Offen­barungen aus der geistigen Welt entgegen, die der Mensch in der Gestalt, wie er sie sehen soll in der nachatiantischen Periode - aller­dings erst in der sechsten Kulturepoche - wird sehen können.",
        "Aber wenn auch die Jungfrau von Orleans die wahre Gestalt nicht sieht, so senkt sich diese wahre Gestalt doch auf sie nieder."
      ],
      [
        "Die Jungfrau von Orleans bringt ihr die religiösen Vorstellungen ihrer Zeit ent­gegen, sie deckt sie gleichsam zu; es wird aus ihr herausgefordert ihre Vorstellungswelt durch die spirituelle Macht.",
        "So ist also die Offenbarung als objektiv anzusprechen."
      ],
      [
        "Wenn auch in unserer Zeit irgend jemand nachweisen kann, dass bei einer Kundgebung aus der geistigen Welt subjektive Elemente einfliessen, wenn wir das Bild, das sich der Betreffende macht von der spirituellen Welt, nicht als objektiv ansehen können, wenn das auch ein Schleier ist - so dürfen wir deshalb doch nicht die objektiven Offenbarungen als solche Schleier deuten.",
        "Sie sind objektiv."
      ],
      [
        "Sie zaubern aus unserer eigenen Seele den Inhalt heraus.",
        "Wir müssen unterscheiden zwischen det Objektivität des Inhaltes und der der Tatsachen, die aus der geistigen Welt kommen. - Ich musste das insbesondere deshalb betonen, weil auf diesem Felde sowohl von denen, welche die spirituelle Welt anerkennen,"
      ],
      [
        "wie auch von den Gegnern zwar entgegengesetzte, aber doch überall Fehler gemacht werden. -"
      ],
      [
        "So also stellt uns gleichsam die Jungfrau von Orleans eine histo­rische Persönlichkeit dar, die schon ganz in dem Sinne unserer Epoche wirkt, wo ja zum Geistigen hinaufgerichtet sein muss alles das, was wir sozusagen produzieren können auf Grundiage unserer äusseren Eindrücke.",
        "Was heisst das aber, wenn wir es anwenden auf unsere Kultur?",
        "Das heisst: Wir mögen den Blick hinauswenden zunächst naiv auf unsere Umgebung.",
        "Wenn wir aber dabei bleiben, das Auge bloss auf die äusseren Eindrücke zu richten, dann tun wir nicht unsere Schuldigkeit.",
        "Wir tun sie nur dann, wenn wir uns bewusst sind, dass wir die äusseren Eindrücke beziehen müssen auf hinter ihnen stehende geistige Mächte.",
        "Wenn wir Wissenschaft treiben und machen es so wie die Gelehrsamkeit, dann tun wir nicht unsere Schuldigkeit.",
        "Wir müssen alles das, was wir erfahren können über die Gesetze der Naturerscheinungen, über die Gesetze der Seelenerscheinungen so betrachten, dass wir es wie eine Sprache anschauen, die uns hinauf-führen soll in eine göttlich-geistige Offenbarung.",
        "Wenn wir das Bewusstsein haben, dass wir alle physikalischen, chemischen, bio­logischen, physiologischen, psychologischen Gesetze so betrachten sollen, dass wir sie auf etwas Geistiges beziehen, was sich uns offen­bart, dann tun wir unsere Schuldigkeit."
      ],
      [
        "So ist es in bezug auf die Wissenschaften unserer Zeit, und so ist es mit der Kunst.",
        "Diejenige Kunst, die wir charakterisieren als die griechische Kunst, die sozusagen emfacher auf den Menschen reflek­tierte, die ganz und gar darstellte das bloss Menschliche, das Arbeiten des Ich mit dem Ich, insoweit sich das Ich im sinnlich-physischen Material ausdrückt, diese Kunst hat ihre Epochen gehabt.",
        "In unserer Zeit ist bei den wirklich grossen künstierischen Persönlichkeiten wie instinktiv der Drang entstanden, die Kunst zu einer Art von Opferdienst für die göttlich-geistigen Welten zu gestalten, das heisst das, was zum Beispiel in Töne gekleidet wird, anzusehen als eine Interpretation geistiger Mysterien.",
        "So wird man kulturhistorisch­okkult einmal anzuschauen haben bis in alle Einzelheiten hinein Richard Wagner.",
        "So wird man gerade ihn anzusehen haben als einen"
      ],
      [
        "reprasentativen Menschen unseres, des fünften Kulturzeitraumes, der den Drang immer gefühlt hat, auszudrücken in dem, was in ihm in Tönen lebte, den Zug nach der spirituellen Welt, der das Kunstwerk als eine äussere Sprache der spirituellen Welt betrachtete.",
        "Und da stehen im Grunde genommen die Überbleibsel der alten Kultur und die Morgenröte einer neuen Kultur scharf, schroff selbst, in unserer Zeit sich gegenüber.",
        "Haben wir doch gesehen, wie sozusagen das rein menschliche Weben in den Tönen, die rein formale Musik, die Richard Wagner überwinden wollte, in heftiger Weise von den Gegnern Richard Wagners verteidigt wurde, weil sie nicht imstande waren, zu fühlen, dass gerade bei Richard Wagner ein neuer Impuls instinktiv wie eine Morgenröte aufging."
      ],
      [
        "Ich weiss nicht, ob die meisten von Ihnen wissen, dass Richard Wagner lange Zeit hindurch die herbsten, die furchtbarsten Kritiker und Ablehner gefunden hat.",
        "Diese Kritiker und Ablehner haben eine gewisse Art von Anführung gehabt in dem ausserordentlich geist­vollen musikalischen Schaffen Eduard Hanslicks in Wien, der das interessante Bücheichen ,,Vom musikalisch Schönen\" geschrieben hat."
      ],
      [
        "Ich weiss nicht, ob Sie wissen, dass damit dem Neuaufgehen einer historischen Morgenröte das Alte sozusagen entgegengestellt war.",
        "Dieses Buch ,,Vom musikalisch Schönen\" kann ein historisches Denkmal für die spätesten Zeiten werden."
      ],
      [
        "Denn was wollte Hanslick?",
        "Er sagt: Man kann nicht in dieser Weise Musik machen wie Richard Wagner; das ist gar keine Musik, denn da nimmt die Musik sozusagen den Anlauf, auf etwas hinweisen zu wollen, was ausserhalb des Musikalischen steht, auf etwas Übersinnliches."
      ],
      [
        "Musik sei aber ,,Ara­beske in Tönen\" - das war ein Lieblingswort des Hanslick.",
        "Das heisst, eine arabeskenartige Aneinanderfügung von Tönen, und der musi­kalisch-ästhetische Genuss kann darin bestehen, sich rein menschlich zu erfreuen an der Art und Weise, wie die Töne ineinander und nach­einander erklingen."
      ],
      [
        "Hanslick sagte, Richard Wagner sei überhaupt kein Musiker, er verstehe gar nicht das Wesen des Musikalischen.",
        "Das Wesen der Musik müsse liegen in einer blossen Architektonik des Tonmaterials. - Was kann man über eine solche Erscheinung sagen?"
      ],
      [
        "Nichts anderes, als dass Hanslick im eminentesten Sinne ein"
      ],
      [
        "Nachzügler, ein Reaktionär der vierten Kulturepoche war.",
        "Da hatte er recht - für diese Kulturepoche; aber was für eine Kulturepoche richtig ist, gilt nicht mehr für die nächste.",
        "Man kann von seinem Standpunkt aus sagen, Richard Wagner sei kein Musiker.",
        "Dann aber müsste man weiter sagen: Es ist diese Epoche jetzt vorbei, wir müssen uns nun mit dem zufriedengeben, was aus dieser Epoche stammt, wir müssen uns versöhnen damit, dass sich das im Hanslickschen Sinne Musikalische erweitert über sich selbst hinaus zu einem Neuen."
      ],
      [
        "Und so könnten wir auf mancherlei Gebieten diesen Zusammen­stoss des Alten und des Neuen gerade in unserer Kulturepoche studieren.",
        "Ausserordentlich interessant ist das insbesondere in den einzelnen Zweigen der Wissenschaft.",
        "Es würde viel zu weit führen, wenn wir zeigen wollten, wie es da überall Reaktionäre gibt und solche, die herausarbeiten aus den einzelnen Wissenschaften, was die Wissenschaft werden soll: der Ausdruck eines hinter den Erscheinun­gen stehenden Göttlich-Geistigen.",
        "Das Grundelement, von dem sich die Gegenwart durchdringen muss, um immer bewusster das Göttlich-Geistige zum Zielpunkte, zum Perspektivpunkt für unsere Arbeit zu machen, das soll eben die Geisteswissenschaft sein, und die Geistes­wissenschaft soll überall erwecken die Impulse von unten nach oben; sie soll überall die menschlichen Seelen auffordern zum Opfer, das heisst zum Opfern dessen, was wir durch die äusseren Eindrücke erwerben, gegenüber dem, was wir erreichen sollen im Hinauf­arbeiten in die Regionen des Geistselbstes, Lebensgeistes und Geistes­menschen."
      ],
      [
        "Wenn wir dieses Bild der menschlichen Geschichte, der okkulten Geschichte uns vor Augen stellen, dann werden wir es begreiflich finden, dass eine Seele, die in der indischen und dann in der persischen Epoche inkarniert war, durchdrungen sein konnte von dem inspirieren­den Elemente einer Individualität der höheren Hierarchien; dass dann aber, als sie eintrat in die grechisch-lateinische Zeit, diese Seele mit sich allein war, dass diese Seele so arbeitete, dass Ich im Ich eben arbeitete.",
        "Alles das, was in der vorgriechischen Epoche für alle einzelnen Zyklen der nachatlantischen Kulturen wie eine göttliche Eingebung, wie eine Offenbarung von oben erscheint - und es gilt"
      ],
      [
        "das auch noch im Beginne der griechischen Kulturperiode für das neunte, zehnte, elfte Jahrhundert der vorchristlichen Zeit -, was sich uns darstellt als eine inspirierte Kultur, in die von aussen einifiesst, was sie geistig erhalten soll, das gestaltet sich immer mehr und mehr dazu, rein menschlich-persönlich sich darzuleben.",
        "Und am stärksten findet das seinen Ausdruck gerade eben im Griechentum."
      ],
      [
        "Einen solchen Ausdruck des äusseren Menschen, wie er sich in der physi­schen Welt darlebt, für das, was der Mensch als auf sich gestellte Ichwesenheit ist, hat keine Zeit vorher gesehen und wird keine Zeit nachher wieder sehen können.",
        "Das rein Menschlich-Persönliche, das ganz in sich abgeschlossene Menschlich-Persönliche tritt in der an­tiken Lebensweise des Griechen und in seinen Schöpfungen historisch zutage."
      ],
      [
        "Vergleichen wir, wie in seine Göttergestalten der griechische Plastiker hineingeheimnisst hat das Menschlich-Persönliche!",
        "Wir kön­nen sagen: So wie uns ein griechisches plastisches Kunstwerk ent­gegentritt, soweit es durch physische Mittel zu erkennen ist, so steht der Mensch ganz als Persöniichkeit vor uns."
      ],
      [
        "Und wenn wir bei den Kunstwerken der Griechen nicht vergessen könnten, dass dieser Inkarnation, die uns da ausgedrückt wird, andere Inkarnationen vor-angingen und andere folgen werden, wenn wir nur einen Augenblick denken würden, dass der Apollogestalt und Zeusgestalt nur eine einzelne Inkarnation aus vielen zugrundeliegt, so würden wir nicht richtig empfinden dem griechischen Kunstwerk gegenüber.",
        "Da müssen wir vergessen können, dass der Mensch in aufeinanderfolgenden Inkarnationen sich verkörperte."
      ],
      [
        "Da ist die Persönlichkeit ganz hinein-gegossen in die Form der einen Persönlichkeit.",
        "Und so war das ganze Leben der Griechen."
      ],
      [
        "Gehen wir dagegen weiter zurück, da werden die Gestalten symbolisch; da deuten die Gestalten etwas an, was nicht rein mensch­lich ist, da drücken sie etwas aus, was der Mensch noch nicht in sich selber fühlt.",
        "Da konnte er nur in Symbolen ausdrücken, was herein­kam aus göttlich-geistigen Welten.",
        "Daher die alte symbolisierende Kunst. - Und sehen wir wiederum, wie die Kunst herauf kommt gerade zu dem Volk, welches das Material hergeben soll zu unserem, zum fünften Kulturzeitraurn - wir brauchen uns da nur die ältere"
      ],
      [
        "deutsche Kunst zu vergegenwärtigen -, da sehen wir, wie wir es nicht mit einer Symbolik, aber auch nicht mit einer Ausprägung des rem Menschlichen zu tun haben, sondern mit dem in sich vertieften Seelischen; wir sehen, wie da das Seelische sozusagen nicht ganz hineinkann in die Menschengestalt.",
        "Wer könnte gerade die Gestalten Albrecht Dürers anders charakterisieren, als dass bei ihnen dasjenige, was nach der übersinnlichen Welt im Menschen verlangt, man möchte sagen im griechischen Sinne genommen nur einen unvoll­kommenen Ausdruck findet in der äusseren Ausgestaltung derKörper­lichkeit.",
        "Daher die Vertiefung nach dem Seelischen, je weiter die Kunst heraufkommt."
      ],
      [
        "Und jetzt werden Sie es nicht mehr unbegreiffich finden, dass ich in der ersten Stunde sagte: Es erscheint in der physischen Welt das, was früher verkörpert war, wie ein Abbild; in die Individualität flossen herein Wesenheiten der höheren Hierarchien.",
        "So dass, wenn wir von einem Menschen der griechischen Welt in früheren Zeiten sagen müssen, er war inkarniert -, wir nicht nur diese in sich geschlossene Wesenheit sehen müssen, sondern hinter ihr stehend die Individualität einer höheren Hierarchie."
      ],
      [
        "So tritt uns in der griechisch-lateinischen Periode Alexander, so tritt uns Aristoteles gegenüber.",
        "Wir verfolgen ihre Individualitäten nach rückwärts.",
        "Da müssen wir von Alexander zurückgehen zu Gilgamesch und sagen: Bei Gilgamesch ist diese Individualität, die dann wie auf den physischen Plan herausprojiziert als Alexander erscheint; hinter ihr müssen wir einen Feuergeist sehen, der sich seiner als Werkzeug bedient."
      ],
      [
        "Und bei Aristoteles sehen wir, zurückgehend in der Zeit, die Mächte des alten Hellsehens wirken in dem Freunde des Gilgamesch.",
        "So also sehen wir sowohl junge wie alte Seelen, hinter denen früher Hellsichtigkeit stand, ganz heraus­gestellt in der griechischen Zeit auf den physischen Plan."
      ],
      [
        "Und so tritt uns das ganz besonders bei der grossen Mathematikerin Hypatia entgegen, bei der sozusagen die ganze mathematische und philo­sophische Weisheit ihrer Zeit als persönliches Können, als persöniiche Wissenschaft und Weisheit lebte.",
        "Das war abgeschlossen in der Per­sönlichkeit der Hypatia."
      ],
      [
        "Und wir werden noch sehen, wie diese Individualität gerade die weibliche Persönlichkeit annehmen musste,"
      ],
      [
        "um eine so weiche Zusammengeschlossenheit alles dessen auszu­prägen, was sie früher aufgenommen hatte in den orphischen My­sterien, - um alles das als persönliche Wirkungsweise auszuprägen, was sie dort vermittelst der Inspiratoren als ein Schüler der orphischen Mysterien aufgenommen hatte."
      ],
      [
        "So sehen wir also, wie in aufeinanderfolgende Menschheitsinkarna­tionen Einflüsse aus der geistigen Welt modifizierend eintreten.",
        "Und nur hinweisen kann ich darauf, dass gerade eine solche Individualität wie diejenige, die als Hypatia inkarniert war, die also mitbrachte die Weisheit der orphischen Mysterien und sie persönlich auslebte, dann in einer nachfolgenden Inkarnation berufen war, nun den umgekehr­ten Weg einzuschlagen: alle persönliche Weisheit wiederum hinauf-zutragen zum Göttlich-Geistigen.",
        "Daher erscheint Hypatia ungefähr um die Wende des 12. und 13 Jahrhunderts als ein bedeutender, um­fassender, universeller Geist der neueren Geschichte, der einen grossen Einfluss hat auf das, was Zusammenfassung des naturwissenschaft­lichen und auch des philosophischen Erkennens ist.",
        "So also sehen wir, wie hineindringen in die aufeinanderfolgenden Inkarnationen der einzelnen Individualitäten die historischen Mächte."
      ],
      [
        "Wenn wir so den Verlauf der Geschichte betrachten, dann sehen wir wirklich eine Art Niederstieg aus geistigen Höhen bis in die griechisch-lateinische Zeit und dann wiederum einen Aufstieg: ein Aufsammeln des rein vom physischen Plan zu gewinnenden Materials während der griechischen Zeit - das dauert natürlich herein bis in unsere Zeit - und ein Wiederhinauftragen in die geistige Welt, zu dem ein Impuls geschaffen werden soll durch die Geisteswissenschaft, und wozu schon einen instinktiven Impuls gehabt hat eine solche Per­sönlichkeit wie Hypatia, die im ,3.",
        "Jahrhundert wieder verkörpert war."
      ],
      [
        "Ich möchte an dieser Stelle, meine lieben Freunde, weil die all­gemeine Theosophische Gesellschaft in gewisser Beziehung ein Tummelplatz ist von Missverständnissen, - ich möchte hinweisen darauf, dass wirklich unendlich viel von diesen Missverständnissen wie rein aus den Fingern gesogen ist.",
        "So will man gerne dasjenige, was zum Beispiel hier vorgetragen wird innerhalb unserer deutschen Bewegung, in einen gewissen Gegensatz bringen zu dem, was ursprünglich"
      ],
      [
        "die Offenbarung der theosophischen Bewegung in der neueren Zeit war.",
        "Deshalb ergreife ich gerne die Gelegenheit, darauf hinzuweisen, wie das, was hier aus ursprünglich rosenkreuzerischem Quell gegeben wird, in Harmonie steht mit mancherlei von dem, was gerade ursprünglich der theosophischen Bewegung gegeben worden ist."
      ],
      [
        "Und wir haben ja in diesem Augenblick gerade Gelegen­heit, auf etwas hinzuweisen, was von dieser Art ist.",
        "Es ist also von mir gesagt und ganz unabhängig von Traditionen entwickelt worden, dass gewisse spätere historische Persöniichkeiten gleichsam die Schattenbilder sind von früheren, durch die Mythen dargestellten Persönlichkeiten, hinter denen höhere Hierarchien stehen."
      ],
      [
        "Solches darf man nicht in Widerspruch bringen mit denjenigen Manifestatio­nen, die durch H.P.",
        "Blavatzky in die theosophische Gesellschaft hineingebracht worden sind.",
        "Denn sonst könnte man durch ein reines Missverständnis sich sehr wohl in einen Widerspruch versetzen zu den guten alten Lehren, die durch das ausserordentliche, brauch-bare Instrument von H.P."
      ],
      [
        "Blavatzky der theo sophischen Bewegung zugeflossen sind.",
        "Aber in bezug auf das, was hier entwickelt worden ist, möchte ich Ihnen eine Stelle aus den späteren Schriften der Blavatzky vorlesen, wo sie auf die ,,Entschleierte Isis\", ihr ältestes okkultes Werk, hinweist."
      ],
      [
        "Da möchte ich die folgende Stelle Ihnen vorlesen, damit Sie sehen, wie das, was von solchem Widerspruch gesagt wird, im Grunde genommen, ich kann nicht anders sagen, aus den Fingern gesogen ist:"
      ],
      [
        ",,Ausser dem beständigen Wiederholen der alten stets bestehenden Tatsache von Reinkarnation und Karma - und zwar in der Art, wie es die älteste Wissenschaft der Welt, nicht der Spiritismus von heute, gelehrt hat - sollten die Okkultisten eine zyklische und mit der Evo­lution Schritt haltende Reinkarnation lehren: jene Art der Wieder­geburt, geheiinnisvoll und noch unverständlich für die vielen, die nichts wissen von jener Geschichte der Welt, auf welche wir vor­sichtig hingewiesen haben in der ,Entschieierten Isis'.",
        "Eine allgemeine Wiedergeburt für jedes Individuum mit Zwischenpausen von Kama Loca und Devachan, und eine zyklische bewusste Inkarnation mit einem grossen und göttlichen Ziel für Wenige.",
        "Jene grossen Charaktere,"
      ],
      [
        "die in der Geschichte der Menschheit gleich Riesen emporragen, wie Siddharta Buddha und Jesus auf geistigem Gebiet, wie Alexander von Mazedonien und Napoleon der Grosse auf dem Gebiete physischer Eroberungen, sind nichts als widergespiegelte Bilder grosser Urbilder, welche existierten - nicht vor zehntausend Jahren, wie in der ,Ent­schleierten Isis' vorsichtig erwähnt wurde -, sondern während Mil­lionen von aufeinanderfolgenden Jahren, vom Beginne des Manvan­tara an.",
        "Denn wie oben erklärt wurde - mit Ausnahme der wirklichen Avataras sind diese Abbilder ihrer Urbilder, ein jedes entsprechend seiner eigenen Eltern-Flamme, dieselben ungebrochenen Strahlen (Monaden), genannt Devas, Dhyan Chohans oder Dhyani Buddhas oder auch Planetengeister und so weiter, die durch äonenlange Ewig­keit gleich ihren Urbildern leuchten.",
        "Nach ihrem Bilde werden einige Menschen geboren, und wenn irgendein besonderes humanitäres Ziel in Aussicht genommen ist, werden diese letzteren hypostatisch beseelt von ihren göttlichen Urbildern, die immer wieder hervorgebracht werden durch die geheimnisvollen Mächte, welche die Schicksale der Welt leiten und lenken.\""
      ],
      [
        "Mehr durfte nicht gesagt werden zu der Zeit, als die ,,Entschieierte Isis\" geschrieben wurde; deshalb blieb das Gesagte beschränkt auf die blosse Bemerkung, dass ,,es keinen hervorragenden Charakter in den Annalen der heiligen oder profanen Geschichte gibt, dessen Urbild wir nicht finden könnten in den halb sagerthaften und halb realen Überlieferungen vergangener Religionen und Mythologien.",
        "So wie der Stern, der in der schrankeniosen Unendlichkeit des Him­mels in unermesslicher Entfernung über unseren Häuptern strahlt, sich spiegelt in den stillen Gewässern eines Sees, so wird wider-gespiegelt das Bild der Menschheit vorsintflutlicher Zeiten in jenen Perioden, die wir mit einem geschichtlichen Rückblick umfassen können...\""
      ],
      [
        "Wie gesagt, ich ergreife gerne die Gelegenheit, um die Überein­stimmung dessen, was wir in unmittelbarer Gegenwart erforschen können, mit dem, was in gewisser Beziehung ursprüngliche Offen­barung war, hervorzuheben.",
        "Sie wissen ja, dass es Grundsatz hier ist, in gewisser Hinsicht treu festzuhalten an den Traditionen der theosophischen"
      ],
      [
        "Bewegung; dass aber auch nichts ungeprüft hier wieder­holt wird, das betone ich ausdrücklich; darauf kommt es an.",
        "Wo eine Übereinstimmung des Erkannten mit anderem betont werden kann, soll es wegen der Kontinuität der Theosophischen Gesellschaft scharf hervorgehoben werden, der Gerechtigkeit gemäss; aber ungeprüft soll nichts einfach wiederholt werden.",
        "Das hängt mit der Mission zusammen, die wir gerade innerhalb unserer deutschen theosophi­schen Bewegung haben, - eben den eigenen Einschlag hineinzutragen, den individuellen Einschlag in diese theosophische Bewegung.",
        "Aber gerade solche Beispiele können Ihnen ein Bild davon geben, wie un­begründet das Vorurteil ist, das da und dort hervorwächst, als ob wir durchaus in den Dingen immer etwas anderes haben wollten.",
        "Wir arbeiten treu weiter, wir kramen nicht sozusagen immerfort die alten Dogmen aus; wir prüfen auch das, was heute von anderer Seite geboten wird.",
        "Und wir vertreten das, was mit dem besten okkulten Gewissen gesagt werden kann auf Grundlage der ursprünglichen okkulten Forschungen und der Methoden, die uns überliefert sind durch unsere eigenen heiligen Überlieferungen des Rosenkreuzes."
      ],
      [
        "Es ist nun ausserordentlich interessant, an einer einzelnen Persön­lichkeit zu zeigen, wie gewissermassen das Alte, das in die Mensch­heit hereininspiriert worden ist unter dem Einfluss höherer Mächte, sozusagen einen auf den physischen Plan hingeordneten Charakter bei den Menschen des griechisch-lateinischen Zeitalters angenommen hat.",
        "Da können wir als ein Beispiel anführen, wie Eabani in derjenigen seiner Inkarnationen, die zwischen der Persönlichkeit des Eabani und des Aristoteles liegt, unter dem Einfluss der alten Mysterieniehren mit ihren aus den übersinnlichen Welten herabkommenden Kräften auf­nehmen konnte das, worauf eigentlich in gewissen Mysterienschulen die Fortentwicklung der menschlichen Seele beruht.",
        "Wir wollen jetzt nicht wiederholen, was Charaktereigentümlichkeit der verschiedenen Mysterienschulen war, wir wollen auf eine Art derselben unseren geistigen Blick richten, auf jene, wo durch die Erregung ganz be­stimmter Gefühle die Seele fortentwickelt wurde, so dass sie ein­dringen lernte in die überphysische Welt.",
        "In solchen Mysterien wurden in der Seele namentlich jene Empfindungen, jene Impulse"
      ],
      [
        "erregt, die geeignet waren, von Grund aus allen Egoismus auszu­rotten aus der Seele.",
        "Es wurde der Seele klargemacht, wie sie im Grunde genommen immer egoistisch sein muss, wenn sie im physi­schen Leibe verkörpert ist.",
        "Es wurde der ganze Umfang und die ganze Bedeutung des Egoismus für den physischen Plan sozusagen in Im­pulsen auf die entsprechende Seele abgeladen.",
        "Und tief, tief zerknirscht fühlte sich eine solche Seele, die sich sagen musste: Ich habe bisher nichts anderes gekannt als den Egoismus, ich kann ja im physischen Leibe gar nichts anderes sein als ein Egoist.",
        "Ja, weit ist eine solche Seele entfernt worden von dem billigen Standpunkte solcher Men­schen, die als jedes zweite Wort im Munde führen: Ich will ja die Sache nicht für mich, sondern für einen andern.",
        "Den Egoismus zu überwinden und den Zug nach dem Allgemein-Menschlichen und Kosmischen sich anzueignen, ist nicht so leicht, wie mancher sich vorstellt.",
        "Diesem Aneignen muss vorangehen eine völlige Nieder­schmetterung der Seele über den Umfang des Egoismus in den Im­pulsen dieser Seele.",
        "Mitleid mit allem Menschlichen, mit allem Kosmi­schen musste die Seele lernen in den Mysterien, die ich da meine, Mitleid durch die Überwindung des physischen Planes.",
        "Dann konnte man von ihr hoffen, dass sie wieder heruntertragen würde aus den höheren Welten das wahrhafte Mitgefühl für alles Lebendige und alles Seiende."
      ],
      [
        "Aber noch ein anderes Gefühl sollte namentlich entwickelt werden als ein Hauptgefühl neben mancherlei anderem.",
        "Wenn der Mensch eindringen soll in die geistige Welt, dann muss er sich klar sein, dass dort alles anders ist als in der physischen Welt.",
        "Wie vor einem völlig Unbekannten muss man stehen, wenn man der geistigen Welt Auge in Auge gegenübertritt.",
        "Da ist wirklich das Gefühl vorhanden, durch das man in Gefahr gerät, das Gefühl der Furcht vor dem Unbekannten.",
        "Und deshalb musste die Seele in solchen Mysterien durchleben alles, was die Seele des Menschen überhaupt an Furcht und Angst und Schreck und Grauen erleben konnte, um sich abzugewöhnen die Gefühle von Furcht und Angst und Schreck und Grauen.",
        "Dann war der Mensch gewappnet, hinaufzusteigen in die ihrem Inhalte nach ihm unbekannte geistige Welt.",
        "So musste also die Seele des Schülers"
      ],
      [
        "der Mysterien durchgehen durch die Erziehung zum umfassenden universellen Gefühl des Mitleides und zum universellen Gefühl der Furchtlosigkeit.",
        "Das machte jede Seele in denjenigen alten Mysterien durch, an denen Eabani teilnahin, als er wieder erschienen war in der Inkarnation, die zwischen Eabani und Aristoteles steht."
      ],
      [
        "Das machte auch er durch.",
        "Und nun trat das wie eine Erinnerung an frühere In­karnationen in Aristoteles zutage.",
        "Er konnte deshalb die Theorie der Tragödie geben, weil er aus solchen Erinnerungen heraus beim An­schauen der griechischen Tragödie darauf kath, wie in dieser ein Nach­klang ist, gleichsam ein äusseres, auf den physischen Plan heraus­getragenes Nachspiel der Mysterienerziehung, wo die Seele durch Mitleid und Furcht geläutert wird."
      ],
      [
        "So sollte der dramatische Held und der ganze Aufbau einer Tragödie vor den Zuschauern etwas darleben, woran der Zuschauer abgeschwächt erleben kann Mitleid mit dem Schicksal des tragischen Helden und Furcht vor dem Aus­gang seines Schicksals, vor dem schauervollen Tod, der ihm winkt.",
        "So war hineinverwoben in den dramatischen Fortgang der Tragödie, in das Weben und Leben der Tragödie, was in der Seele des alten Mysten vorging: die Läuterung, die Reinigung, die Katharsis durch Furcht und Mitleid."
      ],
      [
        "Und wie ein Nachklang sollte auf dem physischen Plan der Angehörige der griechischen Kulturperiode empfinden den Durchgang durch Furcht und Mitleid.",
        "Künstlerisch sollte man erleben, ästhetisch geniessen das, was früher ein grosses Erziehungs­prinzip war."
      ],
      [
        "Und als das, was Aristoteles in früheren Inkarnationen gelernt hatte, in seine Persönlichkeit kam, da war er der geeignete Mann, diese eigenartige Definition der Tragödie zu geben, die so klassisch geworden ist und so grossartig gewirkt hat, dass sie im 18.",
        "Jahrhundert noch von Lessing aufgenommen wurde und durch das ,9."
      ],
      [
        "Jahrhundert hindurch eine solche Rolle gespielt hat, dass über diese Definition ganze Bibliotheken geschrieben worden sind.",
        "Man würde übrigens nicht viel verlieren, wenn der grösste Teil dessen, was in den Bibliotheken liegt, verbrannt würde; denn es wurde mit einem vollständigen Verkennen dessen geschrieben, was vorhin gesagt worden ist, dass wir es nämlich damit zu tun haben, dass in die Kunst etwas herunterprojiziert wird, was im Geistigen liegt."
      ],
      [
        "die das schrieben, ahnten nicht, dass Aristoteles ein altes Mysterien­geheimnis gab, wenn er sagte: Eine Tragödie ist eine Zusammen-fügung aufeinanderfolgender Handlungen, die gruppiert werden um einen Helden und die geeignet sind, im Zuschauer das Gefühl von Furcht und Mitleid zu erregen, damit eine Läuterung in der Seele des Zuschauers eintreten könne."
      ],
      [
        "So sehen wir, dass in einer einzelnen Persönlichkeit, in dem, was sie will und sagt, abschattiert ist, was uns nur dann verständlich wird, wenn wir durch die Persönlichkeit durchblicken auf denjenigen, der dahinter steht, auf den Inspirator.",
        "Erst wenn Sie die Geschichte so betrachten, können Sie sehen, was die Persönlichkeit und was die überpersönlichen Mächte für das geschichtliche Leben bedeuten, wie da etwas hereinspielt in die individuellen Inkarnationen, was Frau Blavatzky nennt das Zusammenspiel von persönlichen individuellen Inkarnationen, und dem, was sie schildert, indem sie sagt: ,,Aber neben der alten stets bestehenden Tatsache von Reinkarnation und Karma sollten die Okkultisten eine zyklische und mit der Evolution Schritt haltende Reinkarnation verkünden\" und so weiter.",
        "Sie nennt das eine bewusste Reinkarnation, weil für die meisten Menschen doch heute die aufeinanderfolgenden Inkarnationen für das Ich unbewusst bleiben, während die geistigen Mächte, die da von oben hereinwirken, in der Tat mit Bewusstsein ihre Kraft von einem Zeitalter in das andere zyklisch hinübertragen."
      ],
      [
        "Das also, was da steht als eine Offenbarung dessen, was Blavatzky in ihrer ersten Zeit aus den Rosenkreuzermysterien heraus sagte, das ist durchaus zu kontrollieren und festzustellen durch ursprüngliche Forschungen.",
        "Daraus aber werden Sie sehen, dass jene bequeme Art, die eine Inkarnation immer nur als die Wirkung einer vorhergehenden Verkörperung auffasst, wesentlich modifiziert wird.",
        "Und Sie werden begreifen, dass Reinkarnation eine viel kompliziertere Tatsachenwelt ist als man gewöhnlich aunimmt, und dass wir sie vollkommen nur dann verstehen, wenn wir den Menschen angliedern an eine höhere überphysische Welt, die fortwährend in unsere Welt hereinwirkt.",
        "Wir können sagen, dass in jenem Zwischenraum, den wir als die griechisch-lateinische Kultur bezeichnen, dem Menschen Zeit gelassen wurde,"
      ],
      [
        "alles das, was aus höheren Welten in die Seele durch lange Inkarna­tionenreihen hindurch gelegt worden war, nachzuempfinden, nach-klingen zu lassen einmal über einem rein menschlichen Ich.",
        "Was die griechisch-lateinische Welt auslebte, war wie ein menschlich-persön­liches Ausleben unendlicher Erinnerungen, die früher von höheren Welten in dieselben Individualitäten hineingelegt worden waren.",
        "Dürfen wir uns deshalb wundern, wenn die bedeutendsten Geister gerade der griechischen Welt das sich besonders zum Bewusstsein bringen?",
        "Sie sagten sich, wenn sie hineinschauten in ihre Innenwelt:"
      ],
      [
        "Da strömt es heraus, da dehnen sich Welten in unsere Persönlichkeit hinein; die sind aber Erinnerungen an das, was früher von den geisti­gen Welten hineingegossen worden ist in uns. - Lesen Sie bei Plato, wie er das, was der Mensch erleben kann, zurückführt auf eine Erin­nerung der Seele an ihre vergangenen Erlebnisse.",
        "Da sehen Sie, wie aus einem tief realen Bewusstsein der vierten nachatlantischen Epoche heraus ein solcher Geist wie Plato geschöpft hat.",
        "Wir lernen erst verstehen, was solch ein einzelner Ausspruch einer so markanten Persönlichkeit bedeutet, wenn wir okkult hineinschauen können in den Geist der Epochen."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "IV",
    "paragraphs": [
      "Sie werden entnehmen können aus den Andeutungen der letzten Tage, dass die griechisch-lateinische Kultur in einer gewissen Beziehung in. der Mitte der ganzen nachatlantischen Kultur steht. Die drei vorangehenden Kulturepochen sind gleichsam die Vorbereitung zu jener Arbeit der menschlichen Seele, des Ich im Ich, wie wir das für die griechische Kultur angedeutet haben.",
      "Wie ein Herabstieg aus hellseherischen Anschauungen zu der rein menschlichen Anschau­ung im Griechentum, so nehmen sich aus die alt-lndische' persische, ägyptische Kultur. Wie ein Wiederhinaufsteigen, ein Wiedererreichen hellseherischer Kulturen muss uns das erscheinen, was mit unserem Zeitraume beginnt und was in immer ausgebreiteterem Maße in den nächsten Jahrhunderten und Jahrtausenden für die Menschheit erreicht werden muss.",
      "So müssen wir sagen: In dem ägyptisch­babylonisch-chaldäischen Kulturzeitraume haben wir sozusagen die letzte Vorbereitung für das rein menschliche Griechentum. Der Mensch steigt damals, im dritten nachatlantischen Zeitraume, gleich­sam herab von den alten hellseherischen Zuständen, durch die er noch unmittelbar hat teilnehmen können an der geistigen Welt, und bereitet vor die rein persönliche, die rein menschliche Kultur, welche sich durch eine Arbeit der Seele, die man eben nennen kann ,,Ich im Ich\", charakterisieren lässt.",
      "Daher zeigte sich uns auch, wie das mit der hellseherischen Kultur verbundene Zurückschauen in frühere Inkarnationen zunächst für Gilgamesch, den Inaugurator der baby­lonischen Kultur, undeutlich, verschwommen wurde; wie er sich selbst da nicht recht mehr auskannte, wo Eabani gewisse Fähigkeiten gleichsam auf ihn vererbte, um zurückzuschauen in frühere Inkarna­tionen. Und ganz entsprechend diesem Herabstürzen aus einer spirituellen",
      "Höhe und dem Einziehen in das bloss Persönliche des einzel­nen Menschen, ganz entsprechend dieser Eigenart der babylonischen Seele wirkt alles das, was wir durch die Arbeit dieser babylonischen Seelen auf die Nachwelt fortgepflanzt sehen.",
      "Wenn wir die Geschichte okkult betrachten wollen, so müssen wir ja sagen, dass sich uns immer mehr und mehr aufdrängt, wie die Völker mit ihrer Arbeit, mit ihrem kulturellen Schaffen keineswegs isoliert dastehen in der Weltentwicklung, im Menschheitsfortschritt. Ein jedes Volk hat seine spirituelle Aufgabe, es hat einen ganz be­stimmten Beitrag zu leisten für das, was wir den menschlichen Fort­schritt nennen. Unsere Kultur ist ja heute schon eine ganz kompli­zierte; und sie ist dadurch so kompliziert geworden, dass viele einzelne Kulturströme zusammengeflossen sind. Wir haben in unserem heuti­gen Geistesleben und in unserem äusseren Leben einen Zusammen-fluss der mannigialtigsten Völkerkulturen, die von den einzelnen Völkern mehr oder weniger einseitig, im Sinne ihrer Mission geleistet wurden und die dann in den gemeinsamen Strom hineingeflossen sind. Deshalb unterscheiden sich alle einzelnen Völker voneinander, deshalb können wir bei jedem Volke von seiner besonderen Mission sprechen. Und wir können fragen: Was können wir, die wir ja die Kulturarbeit unserer Vorfahren in unserer eigenen Kultur enthalten haben, was können wir heute aufweisen, das uns zeigt, was diese oder jene Völker uns zu geben hatten für den gemeinsamen Menschen-fortschritt?",
      "Da ist es recht interessant, gerade die Kulturaufgabe des babyloni­schen Volkes einmal ins Auge zu fassen. 0 dieses babylonische Volk, selbst dem äusseren Geschichtsschreiber hat es merkwürdige Rätsel aufgegeben in dem letzten Jahrhundert durch die Entzifferung der Keilschrift. Und auch das, was nur äusserlich hat erkundet werden können, ist schon im höchsten Grade merkwürdig. Denn der äussere Forscher kann heute sagen: Das, was man früher Geschichte genannt hat, das hat sich fast verdoppelt in bezug auf die Zeit durch das, was man mit der Entzifferung der Keilschrift gelernt hat. Schon die äussere Geschichtsforschung sieht an der Hand äusserer Urkunden förmlich zurück auf fünf- bis sechstausend Jahre vor der christlichen",
      "Zeitrechnung und kann sagen: In dieser ganzen Zeit war in den Gegenden, in denen später die Babylonier, die Assyrer wirkten, eine mächtige, eine bedeutungsvolle Kultur vorhanden. Da finden wir vor allen Dingen in den ältesten Zeiten ein höchst merkwürdiges Volk, Sumerer wird es in der Geschichte genannt, und sein Wohnsitz war in den Gegenden des Euphrat und Tigris, mehr in den oberen Partien, aber auch gegen den unteren Lauf zu. Wir können, weil wir dazu die Zeit nicht haben, hier nicht so sehr auf die äusseren geschicht­lichen Urkunden eingehen, wir müssen uns mehr mit dem beschäf­tigen, was die okkulte Geschichte uns lehren kann.",
      "Dieses Volk, es gehörte mit allem, was es denken und geistig schaffen konnte, und auch mit dem, was es äusserlich wirkte, einer verhältnismässig sehr frühen Kulturstufe der nachatlantischen Ent­wicklung an. Und je weiter wir zurückgehen in der Geschichte der Sumerer, die wir als die Vorbabylonier bezeichnen könnten, desto mehr wird uns klar, dass innerhalb dieses Volkes hochbedeutsame geistige Überlieferungen lebten, dass eine bedeutungsvolle spirituelle Weisheit vorhanden war, eine Weisheit, die wir etwa so charakteri­sieren können, dass wir sagen: Die ganze Art des Lebens, die ganze Art nicht allein zu denken, sondern überhaupt zu leben in der Seele und im Geiste, war bei diesem Volk eine ganz andere als bei den späteren Menschen der Weltgeschichte.",
      "Für Menschen der späteren Weltgeschichte stellte es sich zum Beispiel überall heraus, dass ein gewisser Abstand ist zwischen dem Gedachten und dem Gesproche­nen. Wer sollte heute nicht wissen, dass Denken und Sprechen doch zwei ganz verschiedene Dinge sind, dass die Sprache in gewisser Beziehung in konventionellen Ausdrucksmitteln für das besteht, was die Menschen denken.",
      "Das geht schon daraus hervor, dass wir eben viele Sprachen haben und im Grunde genommen doch eine grosse Anzahl gemeinsamer Vorstellungen in diesen verschiedenen Sprachen der Erde zum Ausdruck bringen. Also es ist ein gewisser Zwischen­raum zwischen dem Denken und dem Sprechen vorhanden.",
      "So war es bei diesem alten Volke eigentlich nicht, sondern es hatte eine Sprache, die im Grunde genommen zur Seele ganz anders stand als alle späteren Sprachen. Namentlich wenn wir in recht alte Zeiten",
      "zurückgehen, finden wir da wirklich etwas - wenn auch nicht mehr ganz rein erhalten - wie eine Art Ursprache der Menschheit. Zwar finden wir die Sprache der einzelnen Stämme und Rassen im weitesten Umkreise Europas, Asiens und Afrikas schon in gewisser Weise differenziert; aber eine Art gemeinsamen Sprachelements, das auf dem ganzen damals bekannten Erdkreis, namentlich von dem tieferen geistigen Menschen, verstanden werden konnte, war gerade bei den Sumerern vorhanden. Woher kam das? Weil die Seele dieser Menschen bei dem Tone, bei dem Laute etwas ganz Bestimmtes fühlte und ein­deutig ausdrücken musste, was bei irgendeinem Gedanken und zu gleicher Zeit bei einem Laute gefühlt werden kann.",
      "Sehen Sie, das, was damit gesagt worden ist, das möchte ich zu-nächst so ausdrücken, dass selbst noch in jenen Namen, die ich Ihnen bei der Besprechung des Gilgamesch-Epos anführen musste, selbst da noch auffällige Laute vorhanden sind: Ischtar, Ischulan und der­gleichen. Wenn man diese Laute ausspricht und den Lautwert in okkulter Beziehung kennt, dann weiss man, dass im Grunde genom­men das Namen sind, die keine anderen Laute enthalten können, wenn sie die betreffenden Wesenheiten bezeichnen sollen, weil sich ein U, ein J' ein A nur auf etwas ganz Bestimmtes eindeutig beziehen kann.",
      "Das eben ist ja der Fortgang der Sprache gewesen, dass die Menschen das Gefühl dafür verloren haben, wie diese Dinge, die Laute - Mitlaute, Selbstlaute - in eindeutiger Weise sich auf irgend etwas beziehen können, so dass man ein Ding in diesen alten Zeiten gar nicht anders hat bezeichnen können als mit einer ganz bestimmten Lautzusammenfügung. Ebensowenig wie wir im Grunde genommen heute, wenn wir ein Ding meinen, einen anderen Ge­danken darüber in England oder in Deutschland haben können, ebensowenig hat man damals, weil man noch das unmittelbare spiri­tuelle alte Gefühl hatte für den Laut, irgendein Ding oder Wesen anders als mit einer eindeutigen Lautzusammenfügung bezeichnen können.",
      "So dass die Sprache in alten Zeiten - und die alte sumerische Sprache hatte eben einen Nachklang dieser alten Zeiten - eine ganz bestimmte war, die einfach durch die Natur der Seele für denjenigen, der sie hörte, begreiflich war. Wenn wir so von der Sprache sprechen,",
      "müssen wir zurückweisen in die allerersten Zeiten der nachatlanti­schen Kulturen.",
      "Dann aber hatte gerade das babylonische Volk die Aufgabe, diesen lebendigen spirituellen Zusammenhang des Menschen mit der geisti­gen Welt herunterzuführen in das Persönliche, da wo die Persönlich­keit auf sich gestellt ist in ihrer Einzelheit, in ihrer Sonderheit. Das war die Aufgabe der Babylonier, die spirituelle Welt in den physi­schen Plan hinunterzuführen.",
      "Und verbunden damit ist, dass dieses lebendige Gefühl, dieses spirituelle Gefühl für die Sprache aufhört und die Sprache sich richtet nach Klima, nach geographischer Lage, nach der Volksrasse und dergleichen. Daher schildert uns die Bibel, die über diese Dinge Richtigeres erzählt als die Phantastereien des sich Sprachforscher nennenden Herrn Fritz Mauthner, daher schildert sie uns diese wichtige Tatsache in dem babylonischen Turmbau' wo alle eine gemeinsame Sprache sprechenden Menschen der Erde zer­streut werden.",
      "Auch diesen babylonischen Turmbau können wir spirituell verstehen, wenn wir wissen, wie in alten Zeiten gebaut wurde. Solche Gebäude, welche zu dem Zwecke gebaut wurden, gewisse der heiligen Weisheit gewidmete Handlungen vorzunehmen, oder welche Wahrzeichen sein sollten für die heiligen Wahrheiten, solche Gebäude wurden in alten Zeiten in den Maßen gebaut, die entweder vom Himmel oder vom Menschen genommen waren.",
      "Und das ist im Grunde genommen dasselbe; denn der Mensch ist als Mikrokosmos eine Nachbildung des Makrokosmos, so dass die Maße, welche in die Pyramide hineingeheimnisst sind, vom Himmel und vom Menschen genommen sind.",
      "Wenn wir also in alte Zeiten zurückgehen könnten, in verhältnis­mässig frühe Zeiten, da würden wir bei den Kultbauten überall finden symbolische Nachahmungen der Menschen- oder Himmels-maße. Länge, Breite und Tiefe, die Art und Weise, wie das Innere architektonisch gestaltet wurde, alles das war nachgebildet den Himmelsmaßen oder denen des menschlichen Leibes. Aber es war das eben so geschehen: Wo man ein lebendiges Bewusstsein hatte von dem Zusammenhang des Menschen mit der spirituellen Welt, da waren die Maße heruntergeholt aus der spirituellen Welt. Wie",
      "musste es denn in der Zeit werden, in welcher heruntergeführt werden sollte die menschliche Erkenntnis sozusagen vom Himmel auf die Erde? Von dem allgemeinen Spirituell-Menschlichen zu dem Menschlich-Persönlichen? Da konnten die Maße nurmehr genommen werden vom Menschen selbst, von der menschlichen Persönlichkeit, insofern sie Ausdruck ist der einzelnen Ichheit. Das aber musste der babylonische Turm werden, die Kultstätte derjenigen, die nurmehr von der Persönlichkeit die Maße hernehmen sollten. Aber zu gleicher Zeit musste gezeigt werden, dass die Persönlichkeit erst nach und nach reif werden muss, wiederum hinaufzusteigen in die geistigen Welten. Wir haben gesehen, es musste erst durch den vierten und fünften Zeitraum durchgegangen werden, um wiederum hinaufzu­steigen. Damals war es nicht möglich gewesen, in die Welt der spiri­tuellen Regionen einfach wieder hinaufzusteigen. Das ist damit gemeint, dass der babylonische Turmbau eine missglückte Sache sein musste, dass man den Himmel noch nicht mit dem erreichen konnte, was aus der menschlichen Persönlichkeit genommen werden konnte. Ungeheuer Tiefes liegt in diesem Weltsymbolum, in dem babylonischen Turmbau' durch den die Menschen auf ihre einzelne menschliche Persönlichkeit beschränkt worden sind, auf das, was die Persönlichkeit in irgendeinem Volke unter einzelnen besonderen Verhältnissen werden konnte.",
      "So wurden die Babylonier heruntergewiesen aus der spirituellen Welt auf unsere Erde; da war ihre Mission, da war ihre Aufgabe. Aber, wie ich schon erwähnt habe, der äusseren babylonischen Kultur lag zugrunde eine chaldäische Mysterienkultur, die esoterisch blieb, die aber doch in ganz bestimmter Weise einfloss in die äussere Kultur. Und daher sehen wir überall noch die uralte Weisheit durchschim­mern in dem, was die Babylonier als Massnahmen treffen konnten. Aber sie mussten das so tun, dass es nicht mit ihnen hinaufstieg in die spirituellen Regionen, sondern dass sie es anwendeten auf unsere Erde. Und was in dieser Art in der Mission der Babylonier lag, das hat sich einverleibt der Kultur und ist bis in unsere Zeiten herunter-gekommen. Das können wir zeigen. Wir müssen da nur ein wenig Respekt bekommen vor jener immerhin noch grossen, gewaltigen",
      "Aufschau in die spirituelien Welten, die noch die alten Traditionen in der Seele hegte und erst in der Abenddämmerung angekommen war. Wir müssen Respekt bekommen vor der tiefen Himmelskunde der Babylonier und vor ihrer gewaltigen Mission, die darin bestand, aus dem, was der Menschheit durch die spirituelle Welt bekannt war, aus den Maßen des Himmels, alles das herauszuholen, was für das äussere praktische Leben notwendig der menschlichen Kultur ein­verleibt werden musste. Aber sie hatten zu gleicher Zeit die Mission, alles auf den Menschen zu beziehen. Und da ist es interessant, dass gewisse Vorstellungen bis in unsere Zeiten herein gelebt haben, die gleichsam ein Nachklang jener eigentümlichen Gefühle waren, die die Babylonier noch lebendig empfanden: Gefühle von einem Herein-fliessen des ganzen Makrokosmos in den Menschen, von einer mensch­lichen Gesetzmässigkeit des irdischen persönlichen Menschen, der nachbildet die grosse Himmelsgesetzmässigkeit.",
      "So gab es im alten Babylonien einen Spruch, der da sagt: ,,Sieh dir an den Menschen, der da geht, nicht wie ein Greis und nicht wie ein Kind, der da geht als ein Gesunder und nicht als ein Kranker, der da nicht zu schnell läuft und nicht zu langsam schreitet, und du wirst sehen das Maß des Sonnenganges.\" Ein merkwürdiger Ausspruch, der uns aber tief, tief hineinweisen kann in die Seelen der alten Baby­lonier. Denn sie stellten sich vor, dass ein Mensch mit einem guten, gesunden Schritt, ein Mensch, der eine Schnelligkeit einhält in seinem Gehen, die der Gesundheit des Lebens entspringt, dass ein solcher Mensch, wenn er nicht zu schnell und nicht zu langsam um die Erde herumgehen würde, zu einem solchen Rundgange 365 1/4 Tage brau­chen würde - und das stimmt ungefähr, vorausgesetzt, dass er Tag und Nacht ununterbrochen wanderte. Und so sagten sie sich: Das ist die Zeit, in der ein gesunder Mensch die Erde umkreisen könnte, und auch die gleiche Zeit - denn sie glaubten ja an die scheinbare Bewegung der Sonne um die Erde -, in welcher die Sonne herumgeht um die Erde. Gehst du also als ein gesunder Mensch, nicht zu schnell, nicht zu langsam, um die Erde herum, so hältst du das Tempo ein des Sonnenganges um die Erde. Das heisst: ,,Mensch, es ist deiner Gesund­heit eingepflanzt, den Gang der Sonne um die Erde nachzugehen.\"",
      "Das ist allerdings etwas, was uns Respekt einfiössen kann vor der gewaltigen kosmischen Anschauung dieses babylonischen Volkes. Denn davon ausgehend haben sie dann geschaffen eine Einteilung dieses Umzuges des Menschen um die Erde. Sie haben nach gewissen Teilmaßen gerechnet und haben dann etwas herausbekommen, was ungefähr der Weg ist, den der Mensch zurücklegt, wenn er zwei Wegstunden weit geht; dies aber kommt einer Meile gleich. Am gesunden Gang rechneten sie dieses Maß heraus und nahmen es als eine Art Normalmaß, um den Boden zu messen in grösserem Maß­stab. Und dieses Maß, meine lieben Freunde, ist vorhanden geblieben bis vor kurzer Zeit - wo in der Menschenentwicklung alles ins Abstrakte gegangen ist - in der deutschen Meile, die man ungefähr in zwei Stunden zurücklegen kann. So hat sich bis ins 19. Jahrhundert herein etwas erhalten, was herstammt aus der Mission der alten Babylonier, die sich das vom Kosmos heruntergeholt, die es dem Laufe der Sonne nachgerechnet hatten.",
      "Erst unsere Zeit hatte die Notwendigkeit, diese vom Menschen hergenommenen Maße zurückzuführen auf abstrakte Maße, die von etwas Totem hergenommen sind. Denn bekanntlich ist das gegen­wärtige Maß ein abstraktes gegenüber den konkreten, unmittelbar an dem Menschen und an der Himmelserscheinung anknüpfenden Maßen, die im Grunde genommen alle auf die Mission des alten babylonischen Volkes zurückführen. Auch bei anderen Maßen, wie zum Beispiel bei dem ,,Fuss\" - dieses war hergenommen von einem menschlichen Glied -, oder bei der ,,Elle\" - die hat man abgemessen an Hand und Arm des Menschen -, überall könnten wir finden, dass da etwas zugrunde liegt, was am Menschen, am Mikrokosmos als Gesetzmässigkeit gefunden wurde. Und im Grunde genommen lag auch noch bis vor kurzem die ganze Denkweise der alten Babylonier unserem Maßsystem zugrunde. Die zwölf Tierkreisbilder und die fünf Planeten gaben ihnen fünf mal zwölf = sechzig; das ist eine Grundzahl. Gezählt haben die alten Babylonier überhaupt bis sechzig. Bei sechzig fingen sie wieder von neuem an. Bei allem, was sie in den alltäglichen Dingen zählten, legten sie die Zahl zwölf zugrunde, welche deshalb, weil sie aus den Gesetzen des Kosmos heraus ist,",
      "sich tatsächlich viel konkreter allen äusseren konkreten Verhältnissen anschmiegt. Denn die Zahl hat zwölf Teile. Zwölf war ja das Dut­zend, und das Dutzend ist nichts anderes als eine Gabe aus der Mission der Babylonier heraus. Wir haben überall die Zehn zugrunde liegen, eine Zahl, die uns grosse Schwierigkeiten bereitet, wenn wir sie in Teile zerlegen wollen, während das Dutzend auch in seiner Beziehung zu sechzig und in seiner verschiedenen Teilbarkeit als die Grundlage eines Zahl- und Maßsystems in hohem Maße sich konkret in die Verhältnisse hineinschmiegt.",
      "Das soll nicht eine Kritik unserer Zeit sein, wenn gesagt wird, dass die Menschheit ins Abstrakte, selbst in bezug auf Rechnen und Zählen hineingegangen ist, denn es kann eben eine Epoche nicht dasselbe tun wie die vorhergehende. Wenn wir uns den Lauf der Kultur von der atlantischen Katastrophe bis in die griechische Zeit und von da weiter durch die unsrige darstellen wollen, können wir sagen: Die indische, persische, ägyptische steigen herunter; in der griechischen Kultur ist der Punkt, wo das reine Menschentum im physischen Plane ausgebildet wird; dann beginnt wiederum das Hinaufsteigen.",
      "Aber dieses Hinaufsteigen ist so, dass es sozusagen nur einen Ast darstellt der wirklichen Entwicklung und dass allerdings ein fortlaufendes Sinken in den Materialismus auf der anderen Seite vorhanden ist. Daher haben wir in unserer Zeit neben dem energischen spirituellen Streben nach aufwärts den krassesten Materialismus, der tief in die Materie hineingeht.",
      "Diese Dinge gehen natürlich nebeneinander. Wie ein Widerstand, der zu überwinden ist zur Entwicklung einer höheren Kraft, so muss diese materialistische Strömung vorhanden sein. Im Sinne dieser Strömung liegt es aber, alles abstrakt zu machen; denn das ganze Dezimalsystem ist ein abstraktes System.",
      "Das ist keine Kritik, sondern nur eine Charakteristik. Und so will man das Konkrete sonst auch überwinden. Was sind nicht alles für Vorschläge gemacht worden, zum Beispiel das Osterfest auf einen festen Tag des Aprils zu verlegen, damit die Unbequemlichkeiten für Handel und Industrie vermieden würden!",
      "Man beachtet nicht, dass wir da noch etwas haben, was hereinragt aus alten Zeiten in seiner Bestimmung nach dem Sternenhimmel. Alles soll ins Abstrakte einiaufen' und nur wie",
      "ein dünner Bach zieht sich zunächst das Konkrete, das wiederum dem Spirituellen zueilt, in unsere Kultur hinein.",
      "Es ist ausserordentlich interessant, wie nicht nur innerhalb der Geisteswissenschaft, sondern auch ausserhalb derselben die Mensch­heit instinktiv getrieben wird, den Weg nach aufwärts zu machen, wiederum hinaufzusteigen, sagen wir zu einer ähnlichen Anschmie­gung an Maß und Zahl und Form, wie es bei den alten Babyloniern und Ägyptern der Fall war. Denn in der Tat ist in unserer Zeit eine Art Wiederholung der babylonischen und ägyptischen Kultur da; es wiederholen sich ja die Zeiträume der Vorzeit, der ägyptische Zeitraum in dem unsrigen, der persische im sechsten, der indische im siebenten Zeitraum. Es entspricht der erste dem siebenten, der zweite dem sechsten, der dritte unserem fünften, der vierte steht für sich da, die Mitte bildend. Daher wiederholt sich so vieles instinktiv, was Anschauung der alten Ägypter war. Da können merkwürdige Sachen vorkommen. Es können Menschen ganz drinnenstehen in urmaterialistischen Vorstellungen, urmaterialistischen Begriffen, und dennoch können sie durch die Macht der Tatsachen - nicht durch naturwissenschaftliche Theorien, denn die sind heute alle materia­listisch - ins spirituelle Leben geführt werden.",
      "Sehen Sie, da gibt es zum Beispiel einen interessanten Berliner Arzt, der hat eine merkwürdige Beobachtung gemacht. Ich will Ihnen das hier einmal auf der Tafel vorführen; das ist also eine rein tatsächliche Beobachtung, die gemacht worden ist, abgesehen von aller Theorie. Nehmen wir an, in diesem Punkte wäre uns schematisch gegeben das Todesdatum irgendeiner Frau - also ich verzeichne nicht irgend etwas, was ausgedacht ist, sondern was beobachtet ist -, diese Frau ist die Grossmutter einer Familie. Eine bestimmte Anzahl von Tagen vor dem Tode dieser Grossmutter der Familie wird ein Enkelkind geboren, die Anzahl der Tage beträgt 1428. Merkwürdigerweise wird 1428 Tage nach dem Tode der Grossmutter wiederum ein Enkelkind geboren, und ein Urenkel wird geboren 9996 Tage nach dem Tode der Grossmutter. Dividieren Sie 9996 durch 1428: Sie erhalten 7. Das heisst, in einem Zeitraum, der das Siebenfache ist von dem Zeitraum zwischen der Enkelgeburt und dem Tode der Grossmutter,",
      "wird ein Urenkel geboren. Und nun zeigt derselbe Arzt, dass dies nicht ein vereinzelter Fall ist, sondern dass sich ganze Familien durchgehen lassen, und man immer in bezug auf Tod und Geburt absolut bestimmte Zahienverhälmisse antrifft. Und das Interessanteste ist: Wenn Sie zum Beispiel nehmen die Zahl 1428, so haben Sie darin wiederum sieben als eine darin aufgehende Zahl. Kurz, die Tatsachen zwingen heute die Leute dazu, gewisse Regelmässigkeiten, Periodizi-täten, die mit den alten heiligen Zahlen zusammenhängen, in der Aufeinanderfolge der äusseren Geschehnisse wiederzufinden. Und heute ist schon die Zahl der tatsächlich von Fliess - so heisst der Berliner Arzt - und von seinen Schülern zusammengestellten Ergeb­nisse in dieser Richtung ein Beweis dafür, dass ganz bestimmte Zahlen die regulativen Faktoren sind, die da regeln das gesetzmässige Ablaufen solcher Ereignisse. Diese zusammengestellten Zahlen sind heute schon in überwältigender Menge vorhanden. Die Auslegung ist dabei eine durchaus materialistische, aber die Macht der Tatsachen zwingt, an das Wirken der Zahl beim Weltgeschehen zu glauben. Ich bemerke ausdrücklich, dass es ausserordentlich falsch ist, wie von Fliess und seinen Schülern dieses Prinzip noch benützt wird. Wie er seine Hauptzahlen' namentlich 23 und 28, die er auch wieder findet",
      "- 28 = 4 X 7 - wie er diese Zahlen verwendet, das wird noch viel­fache Verbesserungen erfahren müssen. Dennoch aber sehen wir in einer solchen Betrachtung etwas wie ein instinktives Auftauchen der alten babylonischen Kultur beim Aufstiege der Menschheit. Natürlich, die grosse Masse der Menschen hat kein Gefühl, keinen Sinn für solche Dinge; sie bleiben vereinzelt in engeren Kreisen. Aber merk­würdig muss es uns erscheinen, wenn wir sehen, dass jene Leute, wie zum Beispiel die Schüler des Fliess, die solche Dinge finden, dann eigentümliche Gedanken und Gefühle bekommen. So sagt einer dieser Schüler des Fliess: ,,Was würden, wenn diese Dinge in älteren Zeiten gewusst worden wären\" - sie sind eben gewusst worden! -, ,,was würden die betreffenden Menschen sagen?\" Und eine besonders charakteristische Stelle scheint mir die folgende zu sein.",
      "Nachdem der Schüler von Fliess vieles in dieser Weise zusammen-gestellt hat, sagt er: ,,Zeiträume von der klarsten mathematischen",
      "Struktur werden hier der Natur entnommen und solche Dinge sind den viel Schwierigeres gewöhnten, begabten Köpfen zu allen Zeiten unerreichbar gewesen. Mit welcher religiösen Inbrunst hätten die rechnenden Babylonier hier geforscht und mit welchem Zauber wären die Fragen umgeben worden.\" - Also wie weit ist man schon im Ahnen dessen, was wirklich geschieht!",
      "Wie arbeitet der Instinkt des Menschen wiederum nach dem spirituellen Leben! Gerade dort aber, wo die landläufige Wissenschaft unserer Zeit gewöhnlich blind vorübergeht, gerade dort ist vielfach das zu suchen, was tief licht­bringend ist für die okkulte Kraft, deren sich die Leute gar nicht bewusst sind.",
      "Denn diejenigen, die hier auf dieses eigentümliche Zahlengesetz hinweisen, die erklären es ganz materialistisch. Aber die Macht der Tatsachen zwingt heute schon die Menschen wiederum, die spirituelle, mathematische Gesetzmässigkeit in den Dingen anzu­erkennen.",
      "So sehen wir in der Tat, wie tief wahr es ist, dass im Grunde genommen alles das, was später in dem Verlauf der Entwicklung der Menschheit auf persönliche Art sich ausdrückt, wie es ein Schat­tenbild ist dessen, was früher in elementarer, ursprünglicher Grösse vorhanden war, weil eben noch der Zusammenhang mit der spiri­tuellen Welt bestand. Das möchte ich betonen, damit es sich in Ihre Seelen schreibt, dass die Babylonier bei ihrem Übergang zu dem vierten Kulturzeitraum es waren, die sozusagen den Himmel auf die Erde herunterzutragen hatten, die das Himmlische noch hinein­zugeheimnissen hatten in Maß, Zahl, Gewicht; und dass wir bis in unsere Tage herein die Nachklänge davon gespürt haben, dass wir wieder zurückkehren werden zu dieser Zahlentechnik, dass sie sich mehr und mehr wieder geltend machen muss, wenn auch auf anderen Gebieten des Lebens ein abstraktes Maß- und Zahlensystem selbst­verständlich das Richtige ist.",
      "So also können wir auch hier wiederum sehen, wie beim Herabsteigen ein gewisser Punkt erreicht worden ist in der griechisch-lateinischen Kultur des reinen Menschentums, des Ausprägens der Persönlichkeit auf dem physischen Plan, und wie dann aufs neue ein Aufstieg stattfindet. So dass also in der Tat auch in bezug auf den Gang der nachatlantischen Kultur das Griechentum wie in der Mitte dasteht.",
      "Nun müssen wir uns doch vor Augen führen, dass hereinbrach in dieser griechischen Epoche der Impuls des Christentums, der die Menschheit immer mehr und mehr hinaufführen soll in andere Regionen. Wir haben aber schon gesehen, wie dieses Christentum in den ersten Zeiten seiner Entwicklung nicht etwa gleich mit all seiner Bedeutung, seinem spirituellen Gehalt aufgetreten ist.",
      "Wir haben es an dem Benehmen der alexandrjnischen Menschen gegen die Hypatia uns veranschaulicht, mit welchen Schwächen und Schatten­seiten zunächst das Christentum behaftet war. Ja, wir haben es oft­mals betont, dass die Zeiten, wo man das Christentum verstehen wird in seiner ganzen Tiefe, eben erst kommen werden, dass das Christen­tum noch unendliche Tiefen in sich hat und dass es sozusagen mehr der Zukunft als der Gegenwart, geschweige denn der Vergangenheit der Menschen angehört.",
      "So sehen wir, wie ein im Anfange Begriffenes im Christentum sich hineinstellt in das, was im Grunde genommen die Erbschaft angetreten hat einer Urwelts-Weisheit und Geistigkeit. Denn das, was das Griechentum empfangen hatte, was es in sich trug, war wirklich etwas wie ein Erbgut dessen, was die Menschen sich in unzähligen Inkarnationen erworben hatten durch ihren lebendigen Zusammenhang mit der spirituellen Welt.",
      "Die ganze Spiritualität, die in den Vorzeiten erlebt worden war, hatte sich hineingesenkt in die Seelen und Herzen der Griechen und lebte sich in ihnen aus. Daher können wir begreifen, dass es Menschen hat geben können, welche beim Einleben des Christentums, besonders angesichts dessen, was in den ersten Jahrhunderten aus dem christlichen Impulse geworden war, dieses Ereignis nicht so hoch schätzen konnten wie das, was mit überwältigender Grösse, überwältigender Geistigkeit als altes Erbgut von Jahrtausenden ins Griechentum sich herein vererbt hat.",
      "Und eine ganz besonders charakteristische Persönlichkeit gab es, die sozusagen in der eigenen Brust diesen Kampf des Alten mit dem Neuen erlebte; diesen Kampf urältester Weisheitsschätze, urältester spiritueller Schätze mit dem, was erst im Anfange war und schwach rieselte. Diese Persönlichkeit der griechisch-lateinischen Zeit vom vierten Jahrhundert, die solches auf dem Schauplatze ihrer Seele erlebte, war Julian Apostata.",
      "O, es ist interessant, das Leben des Julianus, des römischen Kalsers, zu verfolgen. Als Neffe des chrgeizigen und rachsüchtigen Kaisers Konstantin geboren, war eigentlich Julianus schon als Kind dazu bestimmt, getötet zu werden mit seinem Bruder. Nur weil man glaubte, dass mit der Tötung doch zu grosses Aufsehen erregt würde, und weil man hoffte, das, was er schaden könnte, später hintanhalten zu können, liess man ihn am Leben. Und unter mancherlei Irrfahrten zu diesen und jenen Menschengemeinschaften musste Julianus seine Erziehung durchmachen. Und es wurde streng darauf gesehen, dass er das in seine Seele aufnahm, was dazumal in Rom und von Rom, von dem römischen Kalserreiche aus Opportunitätsgründen als christliche Entwicklung genommen wurde. Das aber war ein buntes Gemisch von dem, was sich alimältlich als katholische Kirche heraus-arbeitete, und dem, was als Arianismus lebte; man wollte es sozusagen mit keinem von beiden verderben. Und so hatte man gerade damals ziemlich stark das alte hellenistisch-heidnische Ideal, die alten Götter und die alten Mysterien in jeder Weise bekämpft. Alles, wie gesagt, wurde aufgeboten, um Julianus, von dem man doch hoffen konnte, dass er einmal auf den Thron der Cäsaren kommen würde, um Julianus sozusagen gut christlich zu machen.",
      "Ein merkwürdiger Drang aber sprach sich in dieser Seele aus. Niemals konnte diese Seele so recht tiefes Verständnis gewinnen für das Christentum. Überall da, wo dieses Kind hingebracht wurde, und wo noch Überreste waren nicht nur alten Heidentums, sondern alter Spiritualität, da ging diesem Knaben das Herz auf. Er sog ein, was in der Kultur des vierten Zeitraumes an uralten, heiligen Über­lieferungen und Einrichtungen lebte. Und so kam es denn, dass er auf seinen verschiedentlichsten Irrfahrten, zu denen die Verfolgungen durch seinen Oheim, den Kaiser, ihn trieben, dennoch in die Nähe von Lehrern der sogenannten neuplatonischen Schule kam und zu den Schülern der Alexandriner, die von Alexandria aus die alten Überlieferungen empfangen hatten. Da wurde erst recht Julianus' Herz genährt mit dem, wozu er solch tiefen Drang empfand. Und dann lernte er kennen, was noch an solch alten Weisheitsschätzen in Griechenland selber vorhanden war. Und mit all dem, was Griechenland",
      "ihm gab, was ihm die alte Welt an Weisheit gab, musste Julianus ein lebendiges Gefühl verbinden für die Sprache des Sternerhimmels, für die Geheimnisse, die in der Schrift des Sternerhimmels aus dem Weltenraume zu uns heruntersprechen. Und dann kam für ihn die Zeit, da er durch einen der letzten Hierophanten eingeweiht wurde in die eleusinischen Mysterien. Und wir haben in Julianus das eigen­tümliche Schauspiel, dass ein Inspirierter der alten Mysterien, der ganz drinnensteht in dem, was man erhalten kann, wenn das spirituelle Leben durch die Mysterien zur Wirklichkeit wird, wir haben das Schauspiel, dass ein solcher Eingeweihter auf dem Throne der römi­schen Cäsaren sitzt. Und so sehr auch in der Schrift gegen die Christen, die von Julianus erhalten ist, sich Missverständnisse ein­geschlichen haben, so wissen wir doch, welche Grösse in der Welt­anschauung des Julianus lebte, da, wo er aus der Grösse seiner Initiation heraus spricht.",
      "Aber als ein Schüler der Mysterien, die schon in der Abendröte waren, wusste er sich nicht recht in die Zeit hineinzustellen, deshalb ging er dem Märtyrertum eines Inspirierten entgegen, der nicht mehr recht weiss, welche Geheimnisse geheimgehalten werden müssen und welche mitgeteilt werden dürfen. Aus dem Eifer und Enthusiasmus, den Julianus aufgenommen hatte durch seine hellenistische Erziehung und durch die Einweihung, aus den grossartigen Erfahrungen, die er an der Hand seines Hierophanten hatte machen können, entwickelte sich in ihm der Wille, wiederherzustellen, was er als das lebendige Leben und Weben der alten Spiritualität sah. Und so sehen wir, wie er durch viele Massnahmen versucht, die alten Götter wiederum ein­zuführen in die Kultur, in die sich das Christentum hineingestellt hatte. Er ging sowohl in dem Aussprechen von Mysteriengeheim­nissen, wie auch in dieser Stellung zum Christentum zu weit. Daher kam es, dass er im Jahre 363, als er einen Kriegszug unternehmen musste gegen die Perser, von seinem Schicksal da ereilt wurde. Wie noch jeder, der unbefugt ausgesprochen hat, was nicht ausgesprochen werden darf, ereilt worden ist von seinem Schicksal, so geschah es auch dem Julianus, und es kann historisch belegt werden, dass Ju­lianus durch Christenhand auf diesem Zuge gegen die Perser gefallen",
      "ist. Denn nicht nur, dass sich diese Kunde sehr bald hinterher ver­breitete und niemals von irgendeinem der bedeutenden christlichen Schriftsteller desavouiert worden ist: es wäre auch höchst auffällig, wenn die Perser den Tod ihres Erzfeindes herbeigeführt und sich dieses Todes nicht gerühmt hätten; aber auch bei ihnen entstand gleich nachher die Anschauung, dass er von Christenhand gefallen sei. Das war wirklich etwas wie ein Sturm, der da ausging von dieser inspirierten Seele, von dem Enthusiasmus, den Julian Apostata gewonnen hatte aus seiner Einweihung in die schon ihrer Abend-dämmerung entgegengehenden eleusinischen Mysterien. So war das Schicksal eines Menschen aus dem vierten Jahrhundert, eines ganz persönlichen Menschen, dessen Weltenkarma im Grunde genommen darin bestand, dass er in persönlichem Zorn, in persönlichem Groll, in persönlichem Enthusiasmus ausleben sollte, was er als ein Erbe empfangen hatte. Das war das Grundgesetz seines Lebens.",
      "Es ist nun interessant, gerade dieses Leben, gerade diese Individuali­tät zum Zwecke okkulter Geschichtsbetrachtung im späteren Verlaufe zu betrachten. Da wird geboren im 16. Jahrhundert, im Jahre 1546, ein merkwürdiger Mensch, der aus einem adeligen Geschlechte des nördlichen Europa stammt, dem sozusagen in die Wiege gelegt war alles, was ihn zu hohen Würden im Sinne des damaligen traditionellen Lebens hätte führen können, hineingeboren sogar in eine reiche Familie. Weil er im Sinne der Familientradition ein Mensch in hervor­ragender staatlicher oder sonstiger hoher Stellung werden sollte, war er selbstverständlich für den juristischen Beruf bestimmt und mit einem Hauslehrer nach der Universität Leipzig geschickt worden, um Jurisprudenz zu studieren. Der Hauslehrer quälte den Knaben",
      "- denn er war noch ein Knabe, als er Jura studieren sollte -, er quälte den Knaben, solange es Tag war. Wenn aber der Hauslehrer den Schlaf des Gerechten schlief und über die juristischen Theorien träumte, da stahl sich der Knabe aus seinem Bett und beobachtete mit den sehr einfachen Instrumenten, die er sich selber konstruiert hatte, in der Nacht die Sterne. Und er brachte es sehr bald dahin, mehr über die Geheimnisse des Sternenhimmels zu wissen, nicht nur als irgendwelche Lehrer, sondern mehr noch, als damals in allen",
      "Büchern stand. Denn so zum Beispiel bemerkte er sehr bald eine ganz bestimmte Stellung von Saturn und Jupiter im Sternbilde des Löwen, schaute nach in den Büchern und fand, dass es dort ganz falsch ver­zeichnet war. Da entstand in ihm die Sehnsucht, möglichst genau vor allen Dingen kennenzulernen diese Sternenschrift, möglichst genau zu verzeichnen die Bahn der Sterne. Und was wunder, dass dieser Mensch sehr bald trotz allen Widerstandes von seiner Familie sich die Erlaubnis auswirkte, Naturforscher und Astronom zu werden und nicht über den juristischen Büchern und Doktrinen sein Leben zu verträumen. Und da er bedeutende Mittel flottmachen konnte, so war es ihm möglich, eine ganze Anstalt sich anzulegen.",
      "Dieses Institut war merkwürdig eingerichtet; in seinen oberen Stockwerken enthielt es Instrumente, dazu bestimmt, die Geheimnisse des Sternenhimmels zu beobachten, und im Keller Apparate, um die verschiedenen Mischungen und Entmischungen der Stoffe, der Ma­terien zu formen. Und da arbeitete er, seine Zeit teilend zwischen den Beobachtungen in den oberen Stockwerken und dem Kochen und Sieden und Mischen und Wiegen unten in den Kellern. Da arbeitete dieser Geist, um zu zeigen nach und nach, wie die Gesetze, die in den Sternen geschrieben sind, die planetarischen und Fixsterngesetze, die makrokosmischen Gesetze, sich mikrokosmisch wiederfinden in den mathematischen Zahlen, die den Mischungen und Entmischungen der Stoffe zugrunde liegen. Und das, was er als ein lebendiges Ver­hältnis zwischen Himmlischem und Irdischem fand, das wandte er an auf die Arzneikunde und suchte Arzneien herzustellen, die nament­lich deshalb so Böses wirkten um ihn herum, weil er sie umsonst an diejenigen abgab, denen er helfen wollte. Denn diejenigen, die dazumal als Ärzte darauf bedacht waren, hohe Preise einzunehmen, wüteten gegen diesen Mann, der so ,,Schauderhaftes\" bewirkte mit dem, was er sich herunterholen wollte vom Himmel auf die Erde.",
      "Zum Glück hatte durch ein bestimmtes Ereignis dieser Mann die Gunst des dänischen Königs Friedrich II., und solange er in dieser Gunst stehen konnte, so lange ging es gut, so lange wurde in der Tat Ungeheures geleistet an Einsichten in das spirituelle Wirken der Weitgesetze in dem Sinne, wie ich es eben charakterisiert habe. Ja,",
      "dieser Mann kannte etwas von dem spirituellen Verlauf der Welt-gesetze. Er hat die Welt durch Dinge verblülft, die heute allerdings nicht mehr ganz solchen Glauben finden würden. Denn als er einmal in Rostock war, da prophezeite er aus der Sternenkonstellation heraus den Tod des Sultans Soliman, und der traf ein bis auf wenige Tage, eine Nachricht, die den Namen Tycho de Brahe populär machte innerhalb Europas.",
      "Heute weiss die Welt von jenem Tycho de Brahe, dessen Leben eigentlich so kurze Zeit hinter uns liegt, kaum mehr, als dass er noch etwas einfältig gewesen war, dass er noch nicht ganz auf dem hohen materialistischen Standpunkte unserer Zeit gestanden hatte. Er hat zwar tausend Sterne neu eingezeichnet in die Sternkarte, hat auch damals jene epochemachende Entdeckung eines aufleuchtenden und wieder verschwindenden Sternes gemacht und ihn beschrieben, den Nova-Stella, aber diese Dinge werden meistens verschwiegen.",
      "Die Welt weiss eigentlich nichts anderes, als dass er noch so dumm war, ein Weltsystem auszudenken, wonach die Erde stillsteht und die Sonne mit den Planeten sich um die Erde dreht; das weiss die Welt heute. Dass wir es mit einer bedeutsamen Persönlichkeit des 16.",
      "Jahrhunderts zu tun haben, mit einer Persön­lichkeit, welche Unendliches, auch heute noch Brauchbares für die Astronomie geleistet hat, dass eine Unsumme von tiefer Weisheit in dem liegt, was er gegeben hat, das wird gewöhnlich nicht ver­zeichnet, einfach aus dem Grunde nicht, weil Tycho de Brahe bei der Aufstellung des genauen Systems aus eigenem tiefen Wissen heraus Schwierigkeiten sah, die Kopernikus nicht sah. Und wenn es gesagt werden darf - es erscheint zwar paradox -: aber mit dem Kopernikanischen Weltensystem ist auch noch nicht das letzte Wort gesprochen.",
      "Und der Streit zwischen beiden Systemen wird die spätere Menschheit noch beschäftigen. Doch das nur nebenbei, weil es zu paradox ist für die heutige Zeit.",
      "Erst unter dem Nachfolger seines ihm geneigten Königs gelang es den Gegnern Tycho de Brahes, die sich von allen Seiten auftaten -den damaligen Ärzten, den Professoren der Kopenhagener Uni­versität -, den Nachfolger seines Gönners gegen ihn aufzuhetzen. Und so wurde Tycho de Brahe vertrieben aus seinem Vaterlande und",
      "musste wiederum nach dem Süden ziehen. Er hatte schon einmal in Augsburg sein erstes grosses Planiglob aufgestellt und den vergolde­ten Globus, auf den er immer wieder die neuen Sterne einzeichnete, die er entdeckte und deren zuletzt tausend geworden sind. In der Ver­bannung, in Prag musste dann dieser Mann seinen Tod finden. Wir können heute noch, wenn wir nicht die gebräuchlichen Lehrbücher nehmen, sondern zu den Quellen gehen und etwa aus Kepler stu­dieren, wir können heute noch sehen, wie Kepler zu seinen Gesetzen gerade dadurch gekommen ist, dass ihm Tycho de Brahe in so sorg­fältigen astronomischen Beobachtungen vorgearbeitet hatte. Das war eine Persönlichkeit, die wiederum, aber im grossen Stile, ganz das Gepräge dessen trug, was gross und bedeutend an Weisheit vor seiner Zeit war; die sich noch nicht hineinfinden konnte in das, was gleich nachher populär geworden ist in der materialistischen Weltanschauung. Nicht wahr, ein eigentümliches Schicksal, dieser Tycho de Brahe!",
      "Und nun denken Sie einmal nach, wenn Sie diese beiden persön­lichen Schicksale nebeneinanderstellen, wie unendlich lehrreich es ist, wenn wir wissen aus der Akashachronik, dass die Individualität Julian Apostatas wiederum auftaucht in Tycho de Brahe, dass Tycho de Brahe gewissermassen die Reinkarnation Julians des Abtrünnigen ist. So merkwürdig, so paradox spielt das Reinkarnationsgesetz, wenn sich modifizieren die karmischen Zusammenhänge des einzelnen Menschen durch das, was welthistorisches Karma ist; wenn die Weltenmächte selber die menschliche Individualität ergreifen, um sich ihrer als Werkzeug zu bedienen.",
      "Ich möchte allerdings ausdrücklich bemerken, dass ich solche Dinge wie den Zusammenhang zwischen Julianus und Tycho de Brahe nicht sage, damit sie morgen von allen Dächern gepfiffen und an allen Speise- und Kaffeetischen besprochen werden, sondern damit sie hier sich senken als Lehre der okkulten Weisheit in mancherlei Seelen hinein und wir immer mehr und mehr verstehen lernen, was alles Übersinnliches dem Sinnlich-Physischen des Menschen in Wahr­heit zugrunde liegt."
    ],
    "sentences": [
      [
        "Sie werden entnehmen können aus den Andeutungen der letzten Tage, dass die griechisch-lateinische Kultur in einer gewissen Beziehung in. der Mitte der ganzen nachatlantischen Kultur steht.",
        "Die drei vorangehenden Kulturepochen sind gleichsam die Vorbereitung zu jener Arbeit der menschlichen Seele, des Ich im Ich, wie wir das für die griechische Kultur angedeutet haben."
      ],
      [
        "Wie ein Herabstieg aus hellseherischen Anschauungen zu der rein menschlichen Anschau­ung im Griechentum, so nehmen sich aus die alt-lndische' persische, ägyptische Kultur.",
        "Wie ein Wiederhinaufsteigen, ein Wiedererreichen hellseherischer Kulturen muss uns das erscheinen, was mit unserem Zeitraume beginnt und was in immer ausgebreiteterem Maße in den nächsten Jahrhunderten und Jahrtausenden für die Menschheit erreicht werden muss."
      ],
      [
        "So müssen wir sagen: In dem ägyptisch­babylonisch-chaldäischen Kulturzeitraume haben wir sozusagen die letzte Vorbereitung für das rein menschliche Griechentum.",
        "Der Mensch steigt damals, im dritten nachatlantischen Zeitraume, gleich­sam herab von den alten hellseherischen Zuständen, durch die er noch unmittelbar hat teilnehmen können an der geistigen Welt, und bereitet vor die rein persönliche, die rein menschliche Kultur, welche sich durch eine Arbeit der Seele, die man eben nennen kann ,,Ich im Ich\", charakterisieren lässt."
      ],
      [
        "Daher zeigte sich uns auch, wie das mit der hellseherischen Kultur verbundene Zurückschauen in frühere Inkarnationen zunächst für Gilgamesch, den Inaugurator der baby­lonischen Kultur, undeutlich, verschwommen wurde; wie er sich selbst da nicht recht mehr auskannte, wo Eabani gewisse Fähigkeiten gleichsam auf ihn vererbte, um zurückzuschauen in frühere Inkarna­tionen.",
        "Und ganz entsprechend diesem Herabstürzen aus einer spirituellen"
      ],
      [
        "Höhe und dem Einziehen in das bloss Persönliche des einzel­nen Menschen, ganz entsprechend dieser Eigenart der babylonischen Seele wirkt alles das, was wir durch die Arbeit dieser babylonischen Seelen auf die Nachwelt fortgepflanzt sehen."
      ],
      [
        "Wenn wir die Geschichte okkult betrachten wollen, so müssen wir ja sagen, dass sich uns immer mehr und mehr aufdrängt, wie die Völker mit ihrer Arbeit, mit ihrem kulturellen Schaffen keineswegs isoliert dastehen in der Weltentwicklung, im Menschheitsfortschritt.",
        "Ein jedes Volk hat seine spirituelle Aufgabe, es hat einen ganz be­stimmten Beitrag zu leisten für das, was wir den menschlichen Fort­schritt nennen.",
        "Unsere Kultur ist ja heute schon eine ganz kompli­zierte; und sie ist dadurch so kompliziert geworden, dass viele einzelne Kulturströme zusammengeflossen sind.",
        "Wir haben in unserem heuti­gen Geistesleben und in unserem äusseren Leben einen Zusammen-fluss der mannigialtigsten Völkerkulturen, die von den einzelnen Völkern mehr oder weniger einseitig, im Sinne ihrer Mission geleistet wurden und die dann in den gemeinsamen Strom hineingeflossen sind.",
        "Deshalb unterscheiden sich alle einzelnen Völker voneinander, deshalb können wir bei jedem Volke von seiner besonderen Mission sprechen.",
        "Und wir können fragen: Was können wir, die wir ja die Kulturarbeit unserer Vorfahren in unserer eigenen Kultur enthalten haben, was können wir heute aufweisen, das uns zeigt, was diese oder jene Völker uns zu geben hatten für den gemeinsamen Menschen-fortschritt?"
      ],
      [
        "Da ist es recht interessant, gerade die Kulturaufgabe des babyloni­schen Volkes einmal ins Auge zu fassen. 0 dieses babylonische Volk, selbst dem äusseren Geschichtsschreiber hat es merkwürdige Rätsel aufgegeben in dem letzten Jahrhundert durch die Entzifferung der Keilschrift.",
        "Und auch das, was nur äusserlich hat erkundet werden können, ist schon im höchsten Grade merkwürdig.",
        "Denn der äussere Forscher kann heute sagen: Das, was man früher Geschichte genannt hat, das hat sich fast verdoppelt in bezug auf die Zeit durch das, was man mit der Entzifferung der Keilschrift gelernt hat.",
        "Schon die äussere Geschichtsforschung sieht an der Hand äusserer Urkunden förmlich zurück auf fünf- bis sechstausend Jahre vor der christlichen"
      ],
      [
        "Zeitrechnung und kann sagen: In dieser ganzen Zeit war in den Gegenden, in denen später die Babylonier, die Assyrer wirkten, eine mächtige, eine bedeutungsvolle Kultur vorhanden.",
        "Da finden wir vor allen Dingen in den ältesten Zeiten ein höchst merkwürdiges Volk, Sumerer wird es in der Geschichte genannt, und sein Wohnsitz war in den Gegenden des Euphrat und Tigris, mehr in den oberen Partien, aber auch gegen den unteren Lauf zu.",
        "Wir können, weil wir dazu die Zeit nicht haben, hier nicht so sehr auf die äusseren geschicht­lichen Urkunden eingehen, wir müssen uns mehr mit dem beschäf­tigen, was die okkulte Geschichte uns lehren kann."
      ],
      [
        "Dieses Volk, es gehörte mit allem, was es denken und geistig schaffen konnte, und auch mit dem, was es äusserlich wirkte, einer verhältnismässig sehr frühen Kulturstufe der nachatlantischen Ent­wicklung an.",
        "Und je weiter wir zurückgehen in der Geschichte der Sumerer, die wir als die Vorbabylonier bezeichnen könnten, desto mehr wird uns klar, dass innerhalb dieses Volkes hochbedeutsame geistige Überlieferungen lebten, dass eine bedeutungsvolle spirituelle Weisheit vorhanden war, eine Weisheit, die wir etwa so charakteri­sieren können, dass wir sagen: Die ganze Art des Lebens, die ganze Art nicht allein zu denken, sondern überhaupt zu leben in der Seele und im Geiste, war bei diesem Volk eine ganz andere als bei den späteren Menschen der Weltgeschichte."
      ],
      [
        "Für Menschen der späteren Weltgeschichte stellte es sich zum Beispiel überall heraus, dass ein gewisser Abstand ist zwischen dem Gedachten und dem Gesproche­nen.",
        "Wer sollte heute nicht wissen, dass Denken und Sprechen doch zwei ganz verschiedene Dinge sind, dass die Sprache in gewisser Beziehung in konventionellen Ausdrucksmitteln für das besteht, was die Menschen denken."
      ],
      [
        "Das geht schon daraus hervor, dass wir eben viele Sprachen haben und im Grunde genommen doch eine grosse Anzahl gemeinsamer Vorstellungen in diesen verschiedenen Sprachen der Erde zum Ausdruck bringen.",
        "Also es ist ein gewisser Zwischen­raum zwischen dem Denken und dem Sprechen vorhanden."
      ],
      [
        "So war es bei diesem alten Volke eigentlich nicht, sondern es hatte eine Sprache, die im Grunde genommen zur Seele ganz anders stand als alle späteren Sprachen.",
        "Namentlich wenn wir in recht alte Zeiten"
      ],
      [
        "zurückgehen, finden wir da wirklich etwas - wenn auch nicht mehr ganz rein erhalten - wie eine Art Ursprache der Menschheit.",
        "Zwar finden wir die Sprache der einzelnen Stämme und Rassen im weitesten Umkreise Europas, Asiens und Afrikas schon in gewisser Weise differenziert; aber eine Art gemeinsamen Sprachelements, das auf dem ganzen damals bekannten Erdkreis, namentlich von dem tieferen geistigen Menschen, verstanden werden konnte, war gerade bei den Sumerern vorhanden.",
        "Woher kam das?",
        "Weil die Seele dieser Menschen bei dem Tone, bei dem Laute etwas ganz Bestimmtes fühlte und ein­deutig ausdrücken musste, was bei irgendeinem Gedanken und zu gleicher Zeit bei einem Laute gefühlt werden kann."
      ],
      [
        "Sehen Sie, das, was damit gesagt worden ist, das möchte ich zu-nächst so ausdrücken, dass selbst noch in jenen Namen, die ich Ihnen bei der Besprechung des Gilgamesch-Epos anführen musste, selbst da noch auffällige Laute vorhanden sind: Ischtar, Ischulan und der­gleichen.",
        "Wenn man diese Laute ausspricht und den Lautwert in okkulter Beziehung kennt, dann weiss man, dass im Grunde genom­men das Namen sind, die keine anderen Laute enthalten können, wenn sie die betreffenden Wesenheiten bezeichnen sollen, weil sich ein U, ein J' ein A nur auf etwas ganz Bestimmtes eindeutig beziehen kann."
      ],
      [
        "Das eben ist ja der Fortgang der Sprache gewesen, dass die Menschen das Gefühl dafür verloren haben, wie diese Dinge, die Laute - Mitlaute, Selbstlaute - in eindeutiger Weise sich auf irgend etwas beziehen können, so dass man ein Ding in diesen alten Zeiten gar nicht anders hat bezeichnen können als mit einer ganz bestimmten Lautzusammenfügung.",
        "Ebensowenig wie wir im Grunde genommen heute, wenn wir ein Ding meinen, einen anderen Ge­danken darüber in England oder in Deutschland haben können, ebensowenig hat man damals, weil man noch das unmittelbare spiri­tuelle alte Gefühl hatte für den Laut, irgendein Ding oder Wesen anders als mit einer eindeutigen Lautzusammenfügung bezeichnen können."
      ],
      [
        "So dass die Sprache in alten Zeiten - und die alte sumerische Sprache hatte eben einen Nachklang dieser alten Zeiten - eine ganz bestimmte war, die einfach durch die Natur der Seele für denjenigen, der sie hörte, begreiflich war.",
        "Wenn wir so von der Sprache sprechen,"
      ],
      [
        "müssen wir zurückweisen in die allerersten Zeiten der nachatlanti­schen Kulturen."
      ],
      [
        "Dann aber hatte gerade das babylonische Volk die Aufgabe, diesen lebendigen spirituellen Zusammenhang des Menschen mit der geisti­gen Welt herunterzuführen in das Persönliche, da wo die Persönlich­keit auf sich gestellt ist in ihrer Einzelheit, in ihrer Sonderheit.",
        "Das war die Aufgabe der Babylonier, die spirituelle Welt in den physi­schen Plan hinunterzuführen."
      ],
      [
        "Und verbunden damit ist, dass dieses lebendige Gefühl, dieses spirituelle Gefühl für die Sprache aufhört und die Sprache sich richtet nach Klima, nach geographischer Lage, nach der Volksrasse und dergleichen.",
        "Daher schildert uns die Bibel, die über diese Dinge Richtigeres erzählt als die Phantastereien des sich Sprachforscher nennenden Herrn Fritz Mauthner, daher schildert sie uns diese wichtige Tatsache in dem babylonischen Turmbau' wo alle eine gemeinsame Sprache sprechenden Menschen der Erde zer­streut werden."
      ],
      [
        "Auch diesen babylonischen Turmbau können wir spirituell verstehen, wenn wir wissen, wie in alten Zeiten gebaut wurde.",
        "Solche Gebäude, welche zu dem Zwecke gebaut wurden, gewisse der heiligen Weisheit gewidmete Handlungen vorzunehmen, oder welche Wahrzeichen sein sollten für die heiligen Wahrheiten, solche Gebäude wurden in alten Zeiten in den Maßen gebaut, die entweder vom Himmel oder vom Menschen genommen waren."
      ],
      [
        "Und das ist im Grunde genommen dasselbe; denn der Mensch ist als Mikrokosmos eine Nachbildung des Makrokosmos, so dass die Maße, welche in die Pyramide hineingeheimnisst sind, vom Himmel und vom Menschen genommen sind."
      ],
      [
        "Wenn wir also in alte Zeiten zurückgehen könnten, in verhältnis­mässig frühe Zeiten, da würden wir bei den Kultbauten überall finden symbolische Nachahmungen der Menschen- oder Himmels-maße.",
        "Länge, Breite und Tiefe, die Art und Weise, wie das Innere architektonisch gestaltet wurde, alles das war nachgebildet den Himmelsmaßen oder denen des menschlichen Leibes.",
        "Aber es war das eben so geschehen: Wo man ein lebendiges Bewusstsein hatte von dem Zusammenhang des Menschen mit der spirituellen Welt, da waren die Maße heruntergeholt aus der spirituellen Welt."
      ],
      [
        "musste es denn in der Zeit werden, in welcher heruntergeführt werden sollte die menschliche Erkenntnis sozusagen vom Himmel auf die Erde?",
        "Von dem allgemeinen Spirituell-Menschlichen zu dem Menschlich-Persönlichen?",
        "Da konnten die Maße nurmehr genommen werden vom Menschen selbst, von der menschlichen Persönlichkeit, insofern sie Ausdruck ist der einzelnen Ichheit.",
        "Das aber musste der babylonische Turm werden, die Kultstätte derjenigen, die nurmehr von der Persönlichkeit die Maße hernehmen sollten.",
        "Aber zu gleicher Zeit musste gezeigt werden, dass die Persönlichkeit erst nach und nach reif werden muss, wiederum hinaufzusteigen in die geistigen Welten.",
        "Wir haben gesehen, es musste erst durch den vierten und fünften Zeitraum durchgegangen werden, um wiederum hinaufzu­steigen.",
        "Damals war es nicht möglich gewesen, in die Welt der spiri­tuellen Regionen einfach wieder hinaufzusteigen.",
        "Das ist damit gemeint, dass der babylonische Turmbau eine missglückte Sache sein musste, dass man den Himmel noch nicht mit dem erreichen konnte, was aus der menschlichen Persönlichkeit genommen werden konnte.",
        "Ungeheuer Tiefes liegt in diesem Weltsymbolum, in dem babylonischen Turmbau' durch den die Menschen auf ihre einzelne menschliche Persönlichkeit beschränkt worden sind, auf das, was die Persönlichkeit in irgendeinem Volke unter einzelnen besonderen Verhältnissen werden konnte."
      ],
      [
        "So wurden die Babylonier heruntergewiesen aus der spirituellen Welt auf unsere Erde; da war ihre Mission, da war ihre Aufgabe.",
        "Aber, wie ich schon erwähnt habe, der äusseren babylonischen Kultur lag zugrunde eine chaldäische Mysterienkultur, die esoterisch blieb, die aber doch in ganz bestimmter Weise einfloss in die äussere Kultur.",
        "Und daher sehen wir überall noch die uralte Weisheit durchschim­mern in dem, was die Babylonier als Massnahmen treffen konnten.",
        "Aber sie mussten das so tun, dass es nicht mit ihnen hinaufstieg in die spirituellen Regionen, sondern dass sie es anwendeten auf unsere Erde.",
        "Und was in dieser Art in der Mission der Babylonier lag, das hat sich einverleibt der Kultur und ist bis in unsere Zeiten herunter-gekommen.",
        "Das können wir zeigen.",
        "Wir müssen da nur ein wenig Respekt bekommen vor jener immerhin noch grossen, gewaltigen"
      ],
      [
        "Aufschau in die spirituelien Welten, die noch die alten Traditionen in der Seele hegte und erst in der Abenddämmerung angekommen war.",
        "Wir müssen Respekt bekommen vor der tiefen Himmelskunde der Babylonier und vor ihrer gewaltigen Mission, die darin bestand, aus dem, was der Menschheit durch die spirituelle Welt bekannt war, aus den Maßen des Himmels, alles das herauszuholen, was für das äussere praktische Leben notwendig der menschlichen Kultur ein­verleibt werden musste.",
        "Aber sie hatten zu gleicher Zeit die Mission, alles auf den Menschen zu beziehen.",
        "Und da ist es interessant, dass gewisse Vorstellungen bis in unsere Zeiten herein gelebt haben, die gleichsam ein Nachklang jener eigentümlichen Gefühle waren, die die Babylonier noch lebendig empfanden: Gefühle von einem Herein-fliessen des ganzen Makrokosmos in den Menschen, von einer mensch­lichen Gesetzmässigkeit des irdischen persönlichen Menschen, der nachbildet die grosse Himmelsgesetzmässigkeit."
      ],
      [
        "So gab es im alten Babylonien einen Spruch, der da sagt: ,,Sieh dir an den Menschen, der da geht, nicht wie ein Greis und nicht wie ein Kind, der da geht als ein Gesunder und nicht als ein Kranker, der da nicht zu schnell läuft und nicht zu langsam schreitet, und du wirst sehen das Maß des Sonnenganges.\" Ein merkwürdiger Ausspruch, der uns aber tief, tief hineinweisen kann in die Seelen der alten Baby­lonier.",
        "Denn sie stellten sich vor, dass ein Mensch mit einem guten, gesunden Schritt, ein Mensch, der eine Schnelligkeit einhält in seinem Gehen, die der Gesundheit des Lebens entspringt, dass ein solcher Mensch, wenn er nicht zu schnell und nicht zu langsam um die Erde herumgehen würde, zu einem solchen Rundgange 365 1/4 Tage brau­chen würde - und das stimmt ungefähr, vorausgesetzt, dass er Tag und Nacht ununterbrochen wanderte.",
        "Und so sagten sie sich: Das ist die Zeit, in der ein gesunder Mensch die Erde umkreisen könnte, und auch die gleiche Zeit - denn sie glaubten ja an die scheinbare Bewegung der Sonne um die Erde -, in welcher die Sonne herumgeht um die Erde.",
        "Gehst du also als ein gesunder Mensch, nicht zu schnell, nicht zu langsam, um die Erde herum, so hältst du das Tempo ein des Sonnenganges um die Erde.",
        "Das heisst: ,,Mensch, es ist deiner Gesund­heit eingepflanzt, den Gang der Sonne um die Erde nachzugehen.\""
      ],
      [
        "Das ist allerdings etwas, was uns Respekt einfiössen kann vor der gewaltigen kosmischen Anschauung dieses babylonischen Volkes.",
        "Denn davon ausgehend haben sie dann geschaffen eine Einteilung dieses Umzuges des Menschen um die Erde.",
        "Sie haben nach gewissen Teilmaßen gerechnet und haben dann etwas herausbekommen, was ungefähr der Weg ist, den der Mensch zurücklegt, wenn er zwei Wegstunden weit geht; dies aber kommt einer Meile gleich.",
        "Am gesunden Gang rechneten sie dieses Maß heraus und nahmen es als eine Art Normalmaß, um den Boden zu messen in grösserem Maß­stab.",
        "Und dieses Maß, meine lieben Freunde, ist vorhanden geblieben bis vor kurzer Zeit - wo in der Menschenentwicklung alles ins Abstrakte gegangen ist - in der deutschen Meile, die man ungefähr in zwei Stunden zurücklegen kann.",
        "So hat sich bis ins 19.",
        "Jahrhundert herein etwas erhalten, was herstammt aus der Mission der alten Babylonier, die sich das vom Kosmos heruntergeholt, die es dem Laufe der Sonne nachgerechnet hatten."
      ],
      [
        "Erst unsere Zeit hatte die Notwendigkeit, diese vom Menschen hergenommenen Maße zurückzuführen auf abstrakte Maße, die von etwas Totem hergenommen sind.",
        "Denn bekanntlich ist das gegen­wärtige Maß ein abstraktes gegenüber den konkreten, unmittelbar an dem Menschen und an der Himmelserscheinung anknüpfenden Maßen, die im Grunde genommen alle auf die Mission des alten babylonischen Volkes zurückführen.",
        "Auch bei anderen Maßen, wie zum Beispiel bei dem ,,Fuss\" - dieses war hergenommen von einem menschlichen Glied -, oder bei der ,,Elle\" - die hat man abgemessen an Hand und Arm des Menschen -, überall könnten wir finden, dass da etwas zugrunde liegt, was am Menschen, am Mikrokosmos als Gesetzmässigkeit gefunden wurde.",
        "Und im Grunde genommen lag auch noch bis vor kurzem die ganze Denkweise der alten Babylonier unserem Maßsystem zugrunde.",
        "Die zwölf Tierkreisbilder und die fünf Planeten gaben ihnen fünf mal zwölf = sechzig; das ist eine Grundzahl.",
        "Gezählt haben die alten Babylonier überhaupt bis sechzig.",
        "Bei sechzig fingen sie wieder von neuem an.",
        "Bei allem, was sie in den alltäglichen Dingen zählten, legten sie die Zahl zwölf zugrunde, welche deshalb, weil sie aus den Gesetzen des Kosmos heraus ist,"
      ],
      [
        "sich tatsächlich viel konkreter allen äusseren konkreten Verhältnissen anschmiegt.",
        "Denn die Zahl hat zwölf Teile.",
        "Zwölf war ja das Dut­zend, und das Dutzend ist nichts anderes als eine Gabe aus der Mission der Babylonier heraus.",
        "Wir haben überall die Zehn zugrunde liegen, eine Zahl, die uns grosse Schwierigkeiten bereitet, wenn wir sie in Teile zerlegen wollen, während das Dutzend auch in seiner Beziehung zu sechzig und in seiner verschiedenen Teilbarkeit als die Grundlage eines Zahl- und Maßsystems in hohem Maße sich konkret in die Verhältnisse hineinschmiegt."
      ],
      [
        "Das soll nicht eine Kritik unserer Zeit sein, wenn gesagt wird, dass die Menschheit ins Abstrakte, selbst in bezug auf Rechnen und Zählen hineingegangen ist, denn es kann eben eine Epoche nicht dasselbe tun wie die vorhergehende.",
        "Wenn wir uns den Lauf der Kultur von der atlantischen Katastrophe bis in die griechische Zeit und von da weiter durch die unsrige darstellen wollen, können wir sagen: Die indische, persische, ägyptische steigen herunter; in der griechischen Kultur ist der Punkt, wo das reine Menschentum im physischen Plane ausgebildet wird; dann beginnt wiederum das Hinaufsteigen."
      ],
      [
        "Aber dieses Hinaufsteigen ist so, dass es sozusagen nur einen Ast darstellt der wirklichen Entwicklung und dass allerdings ein fortlaufendes Sinken in den Materialismus auf der anderen Seite vorhanden ist.",
        "Daher haben wir in unserer Zeit neben dem energischen spirituellen Streben nach aufwärts den krassesten Materialismus, der tief in die Materie hineingeht."
      ],
      [
        "Diese Dinge gehen natürlich nebeneinander.",
        "Wie ein Widerstand, der zu überwinden ist zur Entwicklung einer höheren Kraft, so muss diese materialistische Strömung vorhanden sein.",
        "Im Sinne dieser Strömung liegt es aber, alles abstrakt zu machen; denn das ganze Dezimalsystem ist ein abstraktes System."
      ],
      [
        "Das ist keine Kritik, sondern nur eine Charakteristik.",
        "Und so will man das Konkrete sonst auch überwinden.",
        "Was sind nicht alles für Vorschläge gemacht worden, zum Beispiel das Osterfest auf einen festen Tag des Aprils zu verlegen, damit die Unbequemlichkeiten für Handel und Industrie vermieden würden!"
      ],
      [
        "Man beachtet nicht, dass wir da noch etwas haben, was hereinragt aus alten Zeiten in seiner Bestimmung nach dem Sternenhimmel.",
        "Alles soll ins Abstrakte einiaufen' und nur wie"
      ],
      [
        "ein dünner Bach zieht sich zunächst das Konkrete, das wiederum dem Spirituellen zueilt, in unsere Kultur hinein."
      ],
      [
        "Es ist ausserordentlich interessant, wie nicht nur innerhalb der Geisteswissenschaft, sondern auch ausserhalb derselben die Mensch­heit instinktiv getrieben wird, den Weg nach aufwärts zu machen, wiederum hinaufzusteigen, sagen wir zu einer ähnlichen Anschmie­gung an Maß und Zahl und Form, wie es bei den alten Babyloniern und Ägyptern der Fall war.",
        "Denn in der Tat ist in unserer Zeit eine Art Wiederholung der babylonischen und ägyptischen Kultur da; es wiederholen sich ja die Zeiträume der Vorzeit, der ägyptische Zeitraum in dem unsrigen, der persische im sechsten, der indische im siebenten Zeitraum.",
        "Es entspricht der erste dem siebenten, der zweite dem sechsten, der dritte unserem fünften, der vierte steht für sich da, die Mitte bildend.",
        "Daher wiederholt sich so vieles instinktiv, was Anschauung der alten Ägypter war.",
        "Da können merkwürdige Sachen vorkommen.",
        "Es können Menschen ganz drinnenstehen in urmaterialistischen Vorstellungen, urmaterialistischen Begriffen, und dennoch können sie durch die Macht der Tatsachen - nicht durch naturwissenschaftliche Theorien, denn die sind heute alle materia­listisch - ins spirituelle Leben geführt werden."
      ],
      [
        "Sehen Sie, da gibt es zum Beispiel einen interessanten Berliner Arzt, der hat eine merkwürdige Beobachtung gemacht.",
        "Ich will Ihnen das hier einmal auf der Tafel vorführen; das ist also eine rein tatsächliche Beobachtung, die gemacht worden ist, abgesehen von aller Theorie.",
        "Nehmen wir an, in diesem Punkte wäre uns schematisch gegeben das Todesdatum irgendeiner Frau - also ich verzeichne nicht irgend etwas, was ausgedacht ist, sondern was beobachtet ist -, diese Frau ist die Grossmutter einer Familie.",
        "Eine bestimmte Anzahl von Tagen vor dem Tode dieser Grossmutter der Familie wird ein Enkelkind geboren, die Anzahl der Tage beträgt 1428.",
        "Merkwürdigerweise wird 1428 Tage nach dem Tode der Grossmutter wiederum ein Enkelkind geboren, und ein Urenkel wird geboren 9996 Tage nach dem Tode der Grossmutter.",
        "Dividieren Sie 9996 durch 1428: Sie erhalten 7.",
        "Das heisst, in einem Zeitraum, der das Siebenfache ist von dem Zeitraum zwischen der Enkelgeburt und dem Tode der Grossmutter,"
      ],
      [
        "wird ein Urenkel geboren.",
        "Und nun zeigt derselbe Arzt, dass dies nicht ein vereinzelter Fall ist, sondern dass sich ganze Familien durchgehen lassen, und man immer in bezug auf Tod und Geburt absolut bestimmte Zahienverhälmisse antrifft.",
        "Und das Interessanteste ist: Wenn Sie zum Beispiel nehmen die Zahl 1428, so haben Sie darin wiederum sieben als eine darin aufgehende Zahl.",
        "Kurz, die Tatsachen zwingen heute die Leute dazu, gewisse Regelmässigkeiten, Periodizi-täten, die mit den alten heiligen Zahlen zusammenhängen, in der Aufeinanderfolge der äusseren Geschehnisse wiederzufinden.",
        "Und heute ist schon die Zahl der tatsächlich von Fliess - so heisst der Berliner Arzt - und von seinen Schülern zusammengestellten Ergeb­nisse in dieser Richtung ein Beweis dafür, dass ganz bestimmte Zahlen die regulativen Faktoren sind, die da regeln das gesetzmässige Ablaufen solcher Ereignisse.",
        "Diese zusammengestellten Zahlen sind heute schon in überwältigender Menge vorhanden.",
        "Die Auslegung ist dabei eine durchaus materialistische, aber die Macht der Tatsachen zwingt, an das Wirken der Zahl beim Weltgeschehen zu glauben.",
        "Ich bemerke ausdrücklich, dass es ausserordentlich falsch ist, wie von Fliess und seinen Schülern dieses Prinzip noch benützt wird.",
        "Wie er seine Hauptzahlen' namentlich 23 und 28, die er auch wieder findet"
      ],
      [
        "- 28 = 4 X 7 - wie er diese Zahlen verwendet, das wird noch viel­fache Verbesserungen erfahren müssen.",
        "Dennoch aber sehen wir in einer solchen Betrachtung etwas wie ein instinktives Auftauchen der alten babylonischen Kultur beim Aufstiege der Menschheit.",
        "Natürlich, die grosse Masse der Menschen hat kein Gefühl, keinen Sinn für solche Dinge; sie bleiben vereinzelt in engeren Kreisen.",
        "Aber merk­würdig muss es uns erscheinen, wenn wir sehen, dass jene Leute, wie zum Beispiel die Schüler des Fliess, die solche Dinge finden, dann eigentümliche Gedanken und Gefühle bekommen.",
        "So sagt einer dieser Schüler des Fliess: ,,Was würden, wenn diese Dinge in älteren Zeiten gewusst worden wären\" - sie sind eben gewusst worden! -, ,,was würden die betreffenden Menschen sagen?\" Und eine besonders charakteristische Stelle scheint mir die folgende zu sein."
      ],
      [
        "Nachdem der Schüler von Fliess vieles in dieser Weise zusammen-gestellt hat, sagt er: ,,Zeiträume von der klarsten mathematischen"
      ],
      [
        "Struktur werden hier der Natur entnommen und solche Dinge sind den viel Schwierigeres gewöhnten, begabten Köpfen zu allen Zeiten unerreichbar gewesen.",
        "Mit welcher religiösen Inbrunst hätten die rechnenden Babylonier hier geforscht und mit welchem Zauber wären die Fragen umgeben worden.\" - Also wie weit ist man schon im Ahnen dessen, was wirklich geschieht!"
      ],
      [
        "Wie arbeitet der Instinkt des Menschen wiederum nach dem spirituellen Leben!",
        "Gerade dort aber, wo die landläufige Wissenschaft unserer Zeit gewöhnlich blind vorübergeht, gerade dort ist vielfach das zu suchen, was tief licht­bringend ist für die okkulte Kraft, deren sich die Leute gar nicht bewusst sind."
      ],
      [
        "Denn diejenigen, die hier auf dieses eigentümliche Zahlengesetz hinweisen, die erklären es ganz materialistisch.",
        "Aber die Macht der Tatsachen zwingt heute schon die Menschen wiederum, die spirituelle, mathematische Gesetzmässigkeit in den Dingen anzu­erkennen."
      ],
      [
        "So sehen wir in der Tat, wie tief wahr es ist, dass im Grunde genommen alles das, was später in dem Verlauf der Entwicklung der Menschheit auf persönliche Art sich ausdrückt, wie es ein Schat­tenbild ist dessen, was früher in elementarer, ursprünglicher Grösse vorhanden war, weil eben noch der Zusammenhang mit der spiri­tuellen Welt bestand.",
        "Das möchte ich betonen, damit es sich in Ihre Seelen schreibt, dass die Babylonier bei ihrem Übergang zu dem vierten Kulturzeitraum es waren, die sozusagen den Himmel auf die Erde herunterzutragen hatten, die das Himmlische noch hinein­zugeheimnissen hatten in Maß, Zahl, Gewicht; und dass wir bis in unsere Tage herein die Nachklänge davon gespürt haben, dass wir wieder zurückkehren werden zu dieser Zahlentechnik, dass sie sich mehr und mehr wieder geltend machen muss, wenn auch auf anderen Gebieten des Lebens ein abstraktes Maß- und Zahlensystem selbst­verständlich das Richtige ist."
      ],
      [
        "So also können wir auch hier wiederum sehen, wie beim Herabsteigen ein gewisser Punkt erreicht worden ist in der griechisch-lateinischen Kultur des reinen Menschentums, des Ausprägens der Persönlichkeit auf dem physischen Plan, und wie dann aufs neue ein Aufstieg stattfindet.",
        "So dass also in der Tat auch in bezug auf den Gang der nachatlantischen Kultur das Griechentum wie in der Mitte dasteht."
      ],
      [
        "Nun müssen wir uns doch vor Augen führen, dass hereinbrach in dieser griechischen Epoche der Impuls des Christentums, der die Menschheit immer mehr und mehr hinaufführen soll in andere Regionen.",
        "Wir haben aber schon gesehen, wie dieses Christentum in den ersten Zeiten seiner Entwicklung nicht etwa gleich mit all seiner Bedeutung, seinem spirituellen Gehalt aufgetreten ist."
      ],
      [
        "Wir haben es an dem Benehmen der alexandrjnischen Menschen gegen die Hypatia uns veranschaulicht, mit welchen Schwächen und Schatten­seiten zunächst das Christentum behaftet war.",
        "Ja, wir haben es oft­mals betont, dass die Zeiten, wo man das Christentum verstehen wird in seiner ganzen Tiefe, eben erst kommen werden, dass das Christen­tum noch unendliche Tiefen in sich hat und dass es sozusagen mehr der Zukunft als der Gegenwart, geschweige denn der Vergangenheit der Menschen angehört."
      ],
      [
        "So sehen wir, wie ein im Anfange Begriffenes im Christentum sich hineinstellt in das, was im Grunde genommen die Erbschaft angetreten hat einer Urwelts-Weisheit und Geistigkeit.",
        "Denn das, was das Griechentum empfangen hatte, was es in sich trug, war wirklich etwas wie ein Erbgut dessen, was die Menschen sich in unzähligen Inkarnationen erworben hatten durch ihren lebendigen Zusammenhang mit der spirituellen Welt."
      ],
      [
        "Die ganze Spiritualität, die in den Vorzeiten erlebt worden war, hatte sich hineingesenkt in die Seelen und Herzen der Griechen und lebte sich in ihnen aus.",
        "Daher können wir begreifen, dass es Menschen hat geben können, welche beim Einleben des Christentums, besonders angesichts dessen, was in den ersten Jahrhunderten aus dem christlichen Impulse geworden war, dieses Ereignis nicht so hoch schätzen konnten wie das, was mit überwältigender Grösse, überwältigender Geistigkeit als altes Erbgut von Jahrtausenden ins Griechentum sich herein vererbt hat."
      ],
      [
        "Und eine ganz besonders charakteristische Persönlichkeit gab es, die sozusagen in der eigenen Brust diesen Kampf des Alten mit dem Neuen erlebte; diesen Kampf urältester Weisheitsschätze, urältester spiritueller Schätze mit dem, was erst im Anfange war und schwach rieselte.",
        "Diese Persönlichkeit der griechisch-lateinischen Zeit vom vierten Jahrhundert, die solches auf dem Schauplatze ihrer Seele erlebte, war Julian Apostata."
      ],
      [
        "O, es ist interessant, das Leben des Julianus, des römischen Kalsers, zu verfolgen.",
        "Als Neffe des chrgeizigen und rachsüchtigen Kaisers Konstantin geboren, war eigentlich Julianus schon als Kind dazu bestimmt, getötet zu werden mit seinem Bruder.",
        "Nur weil man glaubte, dass mit der Tötung doch zu grosses Aufsehen erregt würde, und weil man hoffte, das, was er schaden könnte, später hintanhalten zu können, liess man ihn am Leben.",
        "Und unter mancherlei Irrfahrten zu diesen und jenen Menschengemeinschaften musste Julianus seine Erziehung durchmachen.",
        "Und es wurde streng darauf gesehen, dass er das in seine Seele aufnahm, was dazumal in Rom und von Rom, von dem römischen Kalserreiche aus Opportunitätsgründen als christliche Entwicklung genommen wurde.",
        "Das aber war ein buntes Gemisch von dem, was sich alimältlich als katholische Kirche heraus-arbeitete, und dem, was als Arianismus lebte; man wollte es sozusagen mit keinem von beiden verderben.",
        "Und so hatte man gerade damals ziemlich stark das alte hellenistisch-heidnische Ideal, die alten Götter und die alten Mysterien in jeder Weise bekämpft.",
        "Alles, wie gesagt, wurde aufgeboten, um Julianus, von dem man doch hoffen konnte, dass er einmal auf den Thron der Cäsaren kommen würde, um Julianus sozusagen gut christlich zu machen."
      ],
      [
        "Ein merkwürdiger Drang aber sprach sich in dieser Seele aus.",
        "Niemals konnte diese Seele so recht tiefes Verständnis gewinnen für das Christentum.",
        "Überall da, wo dieses Kind hingebracht wurde, und wo noch Überreste waren nicht nur alten Heidentums, sondern alter Spiritualität, da ging diesem Knaben das Herz auf.",
        "Er sog ein, was in der Kultur des vierten Zeitraumes an uralten, heiligen Über­lieferungen und Einrichtungen lebte.",
        "Und so kam es denn, dass er auf seinen verschiedentlichsten Irrfahrten, zu denen die Verfolgungen durch seinen Oheim, den Kaiser, ihn trieben, dennoch in die Nähe von Lehrern der sogenannten neuplatonischen Schule kam und zu den Schülern der Alexandriner, die von Alexandria aus die alten Überlieferungen empfangen hatten.",
        "Da wurde erst recht Julianus' Herz genährt mit dem, wozu er solch tiefen Drang empfand.",
        "Und dann lernte er kennen, was noch an solch alten Weisheitsschätzen in Griechenland selber vorhanden war.",
        "Und mit all dem, was Griechenland"
      ],
      [
        "ihm gab, was ihm die alte Welt an Weisheit gab, musste Julianus ein lebendiges Gefühl verbinden für die Sprache des Sternerhimmels, für die Geheimnisse, die in der Schrift des Sternerhimmels aus dem Weltenraume zu uns heruntersprechen.",
        "Und dann kam für ihn die Zeit, da er durch einen der letzten Hierophanten eingeweiht wurde in die eleusinischen Mysterien.",
        "Und wir haben in Julianus das eigen­tümliche Schauspiel, dass ein Inspirierter der alten Mysterien, der ganz drinnensteht in dem, was man erhalten kann, wenn das spirituelle Leben durch die Mysterien zur Wirklichkeit wird, wir haben das Schauspiel, dass ein solcher Eingeweihter auf dem Throne der römi­schen Cäsaren sitzt.",
        "Und so sehr auch in der Schrift gegen die Christen, die von Julianus erhalten ist, sich Missverständnisse ein­geschlichen haben, so wissen wir doch, welche Grösse in der Welt­anschauung des Julianus lebte, da, wo er aus der Grösse seiner Initiation heraus spricht."
      ],
      [
        "Aber als ein Schüler der Mysterien, die schon in der Abendröte waren, wusste er sich nicht recht in die Zeit hineinzustellen, deshalb ging er dem Märtyrertum eines Inspirierten entgegen, der nicht mehr recht weiss, welche Geheimnisse geheimgehalten werden müssen und welche mitgeteilt werden dürfen.",
        "Aus dem Eifer und Enthusiasmus, den Julianus aufgenommen hatte durch seine hellenistische Erziehung und durch die Einweihung, aus den grossartigen Erfahrungen, die er an der Hand seines Hierophanten hatte machen können, entwickelte sich in ihm der Wille, wiederherzustellen, was er als das lebendige Leben und Weben der alten Spiritualität sah.",
        "Und so sehen wir, wie er durch viele Massnahmen versucht, die alten Götter wiederum ein­zuführen in die Kultur, in die sich das Christentum hineingestellt hatte.",
        "Er ging sowohl in dem Aussprechen von Mysteriengeheim­nissen, wie auch in dieser Stellung zum Christentum zu weit.",
        "Daher kam es, dass er im Jahre 363, als er einen Kriegszug unternehmen musste gegen die Perser, von seinem Schicksal da ereilt wurde.",
        "Wie noch jeder, der unbefugt ausgesprochen hat, was nicht ausgesprochen werden darf, ereilt worden ist von seinem Schicksal, so geschah es auch dem Julianus, und es kann historisch belegt werden, dass Ju­lianus durch Christenhand auf diesem Zuge gegen die Perser gefallen"
      ],
      [
        "ist.",
        "Denn nicht nur, dass sich diese Kunde sehr bald hinterher ver­breitete und niemals von irgendeinem der bedeutenden christlichen Schriftsteller desavouiert worden ist: es wäre auch höchst auffällig, wenn die Perser den Tod ihres Erzfeindes herbeigeführt und sich dieses Todes nicht gerühmt hätten; aber auch bei ihnen entstand gleich nachher die Anschauung, dass er von Christenhand gefallen sei.",
        "Das war wirklich etwas wie ein Sturm, der da ausging von dieser inspirierten Seele, von dem Enthusiasmus, den Julian Apostata gewonnen hatte aus seiner Einweihung in die schon ihrer Abend-dämmerung entgegengehenden eleusinischen Mysterien.",
        "So war das Schicksal eines Menschen aus dem vierten Jahrhundert, eines ganz persönlichen Menschen, dessen Weltenkarma im Grunde genommen darin bestand, dass er in persönlichem Zorn, in persönlichem Groll, in persönlichem Enthusiasmus ausleben sollte, was er als ein Erbe empfangen hatte.",
        "Das war das Grundgesetz seines Lebens."
      ],
      [
        "Es ist nun interessant, gerade dieses Leben, gerade diese Individuali­tät zum Zwecke okkulter Geschichtsbetrachtung im späteren Verlaufe zu betrachten.",
        "Da wird geboren im 16.",
        "Jahrhundert, im Jahre 1546, ein merkwürdiger Mensch, der aus einem adeligen Geschlechte des nördlichen Europa stammt, dem sozusagen in die Wiege gelegt war alles, was ihn zu hohen Würden im Sinne des damaligen traditionellen Lebens hätte führen können, hineingeboren sogar in eine reiche Familie.",
        "Weil er im Sinne der Familientradition ein Mensch in hervor­ragender staatlicher oder sonstiger hoher Stellung werden sollte, war er selbstverständlich für den juristischen Beruf bestimmt und mit einem Hauslehrer nach der Universität Leipzig geschickt worden, um Jurisprudenz zu studieren.",
        "Der Hauslehrer quälte den Knaben"
      ],
      [
        "- denn er war noch ein Knabe, als er Jura studieren sollte -, er quälte den Knaben, solange es Tag war.",
        "Wenn aber der Hauslehrer den Schlaf des Gerechten schlief und über die juristischen Theorien träumte, da stahl sich der Knabe aus seinem Bett und beobachtete mit den sehr einfachen Instrumenten, die er sich selber konstruiert hatte, in der Nacht die Sterne.",
        "Und er brachte es sehr bald dahin, mehr über die Geheimnisse des Sternenhimmels zu wissen, nicht nur als irgendwelche Lehrer, sondern mehr noch, als damals in allen"
      ],
      [
        "Büchern stand.",
        "Denn so zum Beispiel bemerkte er sehr bald eine ganz bestimmte Stellung von Saturn und Jupiter im Sternbilde des Löwen, schaute nach in den Büchern und fand, dass es dort ganz falsch ver­zeichnet war.",
        "Da entstand in ihm die Sehnsucht, möglichst genau vor allen Dingen kennenzulernen diese Sternenschrift, möglichst genau zu verzeichnen die Bahn der Sterne.",
        "Und was wunder, dass dieser Mensch sehr bald trotz allen Widerstandes von seiner Familie sich die Erlaubnis auswirkte, Naturforscher und Astronom zu werden und nicht über den juristischen Büchern und Doktrinen sein Leben zu verträumen.",
        "Und da er bedeutende Mittel flottmachen konnte, so war es ihm möglich, eine ganze Anstalt sich anzulegen."
      ],
      [
        "Dieses Institut war merkwürdig eingerichtet; in seinen oberen Stockwerken enthielt es Instrumente, dazu bestimmt, die Geheimnisse des Sternenhimmels zu beobachten, und im Keller Apparate, um die verschiedenen Mischungen und Entmischungen der Stoffe, der Ma­terien zu formen.",
        "Und da arbeitete er, seine Zeit teilend zwischen den Beobachtungen in den oberen Stockwerken und dem Kochen und Sieden und Mischen und Wiegen unten in den Kellern.",
        "Da arbeitete dieser Geist, um zu zeigen nach und nach, wie die Gesetze, die in den Sternen geschrieben sind, die planetarischen und Fixsterngesetze, die makrokosmischen Gesetze, sich mikrokosmisch wiederfinden in den mathematischen Zahlen, die den Mischungen und Entmischungen der Stoffe zugrunde liegen.",
        "Und das, was er als ein lebendiges Ver­hältnis zwischen Himmlischem und Irdischem fand, das wandte er an auf die Arzneikunde und suchte Arzneien herzustellen, die nament­lich deshalb so Böses wirkten um ihn herum, weil er sie umsonst an diejenigen abgab, denen er helfen wollte.",
        "Denn diejenigen, die dazumal als Ärzte darauf bedacht waren, hohe Preise einzunehmen, wüteten gegen diesen Mann, der so ,,Schauderhaftes\" bewirkte mit dem, was er sich herunterholen wollte vom Himmel auf die Erde."
      ],
      [
        "Zum Glück hatte durch ein bestimmtes Ereignis dieser Mann die Gunst des dänischen Königs Friedrich II., und solange er in dieser Gunst stehen konnte, so lange ging es gut, so lange wurde in der Tat Ungeheures geleistet an Einsichten in das spirituelle Wirken der Weitgesetze in dem Sinne, wie ich es eben charakterisiert habe."
      ],
      [
        "dieser Mann kannte etwas von dem spirituellen Verlauf der Welt-gesetze.",
        "Er hat die Welt durch Dinge verblülft, die heute allerdings nicht mehr ganz solchen Glauben finden würden.",
        "Denn als er einmal in Rostock war, da prophezeite er aus der Sternenkonstellation heraus den Tod des Sultans Soliman, und der traf ein bis auf wenige Tage, eine Nachricht, die den Namen Tycho de Brahe populär machte innerhalb Europas."
      ],
      [
        "Heute weiss die Welt von jenem Tycho de Brahe, dessen Leben eigentlich so kurze Zeit hinter uns liegt, kaum mehr, als dass er noch etwas einfältig gewesen war, dass er noch nicht ganz auf dem hohen materialistischen Standpunkte unserer Zeit gestanden hatte.",
        "Er hat zwar tausend Sterne neu eingezeichnet in die Sternkarte, hat auch damals jene epochemachende Entdeckung eines aufleuchtenden und wieder verschwindenden Sternes gemacht und ihn beschrieben, den Nova-Stella, aber diese Dinge werden meistens verschwiegen."
      ],
      [
        "Die Welt weiss eigentlich nichts anderes, als dass er noch so dumm war, ein Weltsystem auszudenken, wonach die Erde stillsteht und die Sonne mit den Planeten sich um die Erde dreht; das weiss die Welt heute.",
        "Dass wir es mit einer bedeutsamen Persönlichkeit des 16."
      ],
      [
        "Jahrhunderts zu tun haben, mit einer Persön­lichkeit, welche Unendliches, auch heute noch Brauchbares für die Astronomie geleistet hat, dass eine Unsumme von tiefer Weisheit in dem liegt, was er gegeben hat, das wird gewöhnlich nicht ver­zeichnet, einfach aus dem Grunde nicht, weil Tycho de Brahe bei der Aufstellung des genauen Systems aus eigenem tiefen Wissen heraus Schwierigkeiten sah, die Kopernikus nicht sah.",
        "Und wenn es gesagt werden darf - es erscheint zwar paradox -: aber mit dem Kopernikanischen Weltensystem ist auch noch nicht das letzte Wort gesprochen."
      ],
      [
        "Und der Streit zwischen beiden Systemen wird die spätere Menschheit noch beschäftigen.",
        "Doch das nur nebenbei, weil es zu paradox ist für die heutige Zeit."
      ],
      [
        "Erst unter dem Nachfolger seines ihm geneigten Königs gelang es den Gegnern Tycho de Brahes, die sich von allen Seiten auftaten -den damaligen Ärzten, den Professoren der Kopenhagener Uni­versität -, den Nachfolger seines Gönners gegen ihn aufzuhetzen.",
        "Und so wurde Tycho de Brahe vertrieben aus seinem Vaterlande und"
      ],
      [
        "musste wiederum nach dem Süden ziehen.",
        "Er hatte schon einmal in Augsburg sein erstes grosses Planiglob aufgestellt und den vergolde­ten Globus, auf den er immer wieder die neuen Sterne einzeichnete, die er entdeckte und deren zuletzt tausend geworden sind.",
        "In der Ver­bannung, in Prag musste dann dieser Mann seinen Tod finden.",
        "Wir können heute noch, wenn wir nicht die gebräuchlichen Lehrbücher nehmen, sondern zu den Quellen gehen und etwa aus Kepler stu­dieren, wir können heute noch sehen, wie Kepler zu seinen Gesetzen gerade dadurch gekommen ist, dass ihm Tycho de Brahe in so sorg­fältigen astronomischen Beobachtungen vorgearbeitet hatte.",
        "Das war eine Persönlichkeit, die wiederum, aber im grossen Stile, ganz das Gepräge dessen trug, was gross und bedeutend an Weisheit vor seiner Zeit war; die sich noch nicht hineinfinden konnte in das, was gleich nachher populär geworden ist in der materialistischen Weltanschauung.",
        "Nicht wahr, ein eigentümliches Schicksal, dieser Tycho de Brahe!"
      ],
      [
        "Und nun denken Sie einmal nach, wenn Sie diese beiden persön­lichen Schicksale nebeneinanderstellen, wie unendlich lehrreich es ist, wenn wir wissen aus der Akashachronik, dass die Individualität Julian Apostatas wiederum auftaucht in Tycho de Brahe, dass Tycho de Brahe gewissermassen die Reinkarnation Julians des Abtrünnigen ist.",
        "So merkwürdig, so paradox spielt das Reinkarnationsgesetz, wenn sich modifizieren die karmischen Zusammenhänge des einzelnen Menschen durch das, was welthistorisches Karma ist; wenn die Weltenmächte selber die menschliche Individualität ergreifen, um sich ihrer als Werkzeug zu bedienen."
      ],
      [
        "Ich möchte allerdings ausdrücklich bemerken, dass ich solche Dinge wie den Zusammenhang zwischen Julianus und Tycho de Brahe nicht sage, damit sie morgen von allen Dächern gepfiffen und an allen Speise- und Kaffeetischen besprochen werden, sondern damit sie hier sich senken als Lehre der okkulten Weisheit in mancherlei Seelen hinein und wir immer mehr und mehr verstehen lernen, was alles Übersinnliches dem Sinnlich-Physischen des Menschen in Wahr­heit zugrunde liegt."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "V",
    "paragraphs": [
      "Der Einblick in den Entwicklungsgang solcher Individualitäten, wie wir sie gestern sozusagen durch zwei Inkarnationen hindurch haben verfolgen können, gestattet uns, in das geheirnnisvolle Werden und Weben der Weltengeister während der Menschheitsentwicklung, wäh­rend der Menschengeschichte etwas hineinzuschauen. Denn wenn wir uns die Bilder vor Augen halten, die uns gestern wenigstens skizzen­haft vor die Seele ziehen konnten, die Bilder von Julian dem Abtrün-nigen und von der nächsten Ausprägung dieser selben Individualität im Verlaufe des Menschheitswerdens als Tycho de Brahe, als der grosse Astronom, dann kann uns eines besonders auffallen. Gerade bei solchen Persönlichkeiten, die innerhalb der Geschichte etwas bedeuten, können wir beobachten, dass sozusagen das Eigentümliche ihrer Individualität von einer Inkarnation in die andere hinüberwirkt; dass aber modifi­zierend in diesem reinen Reinkarnationsgang dasjenige sich geltend macht, was höhere geistige Individualitäten der oberen Hierarchien in der Geschichte vollbringen wollen, und zu dem sie sich nur der einzel­nen Menschen als Werkzeuge bedienen. Denn wir müssen uns ja sagen:",
      "Die Individualität, die da auftrat als Julianus Apostata, hatte im vierten nachchristlichen Jahrhundert die Aufgabe, gewissermassen einen letz­ten Anstoss dazu zu geben, die spirituellen Weisheitsschätze früherer Epochen der Menschheitsentwicklung ein letztes Mal zum gewaltigen Auffiammen zu bringen und sie so zu bewahren vor dem Schicksal, das sie leicht hätten finden können, wenn es nur dem aufstrebenden Chri­stentum überlassen geblieben wäre, mit diesem Weisheitsschatz zu wirtschaften. Und auf der anderen Seite müssen wir uns sagen, dass eine Individualität, die in einer Persönlichkeit inkarniert war, welche das Glück hatte, sogar in die eleusinischen Mysterien eingeweiht zu werden,",
      "bei ihrer Wiederinkarnation die Bedingungen hatte, auf sich wirken zu lassen eine unendliche Fülle von Zeitenkräften und von Wesenheiten, die in die Zeit hereinwirken, -wie das ja im 16. Jahrhundert geschehen sollte. Und wir werden in der Tat völlig verständlich finden das Grosse und Gewaltige, das uns gestern an der Persönlichkeit Tycho de Brahes vor Augen getreten ist und das ja seine Erklärung darin findet, dass eine Unsumme von makrokosmischer Wissenschaft in Verbindung mit dem Mikrokosmos bei Tycho de Brahe auftreten konnte, weil er eben ein Eingeweihter in einer früheren Inkarnation gewesen war. So werden wir gewahr durch solche Betrachtungen der okkulten Geschichte, dass es alierdingsunmittelbar die Menschen sind, welcheGeschichte machen, dass aber letzten Grundes doch nur die Geschichte verständlich werden kann, wenn wir den Zusammenhang finden zwischen den einzelnen in der Geschichte auftretenden und absterbenden Persönlichkeiten und den individuellenFäden, die sozusagen durch die ganze Menschheitsent-wicklung durchgehen und sich in den Persöniichkeiten reinkarnieren. Aber wir müssen immer damit zusammenhalten dasjenige, was aus anderen, aus überphysischen Welten hereinströmt durch die Mächte anderer Hierarchien, wenn wir das Menschentum auf unserer Erdober­fläche im Laufe der Geschichte verstehen wollen.",
      "Nun ist uns ja bei unserer Betrachtung vor Augen getreten, wie in all den Kulturzeiträumen nach der atlantischen Katastrophe gewisse übergeordnete Mächte aus den höheren Hierarchien durch die Men­schen hereingewirkt haben. Wir haben gesagt: Am stärksten tritt das hervor bei der altindischen Seele, die sozusagen nur ein Schauplatz ist für das Hereinwirken höherer, geistiger Wesenheiten. Etwas mehr tritt es zurück dann in der Seele des Urpersers. Und dann haben wir gesehen, dass bei der ägyptisch-chaldäischen Kultur die Seele schon die Aufgabe hatte - und das tritt uns besonders bei der Betrachtung der babyloni­schen Seele entgegen - herunterzutragen das Überpersönliche in das Persöniiche, das Spirituelle auf den physischen Plan. Die Persönlich­keit gewinnt also immer mehr Bedeutung, je mehr wir uns der griechi­schen Zeit nähern, und in dieser, mussten wir sagen, haben wir das Weben des Ich im Ich, die völlige Ausprägung der Persönlichkeit bei den starken und kräftigen Gestalten, die uns im griechischen Zeitraum",
      "entgegentreten. In den Griechen und später bei den Römern trat am meisten das zurück, was nur der Individualität aus höheren Welten zu­nächst gegeben werden kann; dagegen trat das hervor, was der Mensch als sein eigentlich Menschliches in seiner Persönlichkeit ausprägt.",
      "Nun kann ja die Frage entstehen, und die Beantwortung dieser Frage wird uns erst den ganzen okkulten Gang der Geschichte tiefer begreif­lich machen können: Was sind denn das eigentlich für Geister, welche durch die Inder, die Urperser, durch die Babylonier, Chaldäer und Ägypter gewirkt haben, welchen Hierarchien gehören sie an? Wir können aus den Forschungen, die uns durch die okkulten Quellen möglich sind, allerdings in einer gewissenWeise sagen, welche Indivi­dualitäten der höheren Hierarchien sich in jeder dieser genannten Zeit­läufe der Menschen als Werkzeuge bedienten, um durch sie zu wirken.",
      "In die alte indische Seele herein, also in jene Seele, die sozusagen kultur-schöpferisch war unmittelbar nach der atlantischen Katastrophe, in diese ergossen ihre Kräfte herein diejenigen Wesenheiten, die wir ge­wohnt sind Angeloi oder Engel zu nennen. So dass wir in einer ge­wissen Beziehung recht haben, wenn wir sagen: Wenn ein alter Inder sprach, wenn er das, was seine Seele bewegte, ausdrückte, so ist es so, dass durch seine Seele nicht seine eigene Ichheit direkt sprach, sondern ein Engel, ein Angelos.",
      "Weil nun der Engel nur eine Stufe über der Menschheit steht, so ist er das dem Menschen verwandteste Wesen der höheren Hierarchien, und daher konnte er sich sozusagen am meisten in seiner Eigenart aussprechen. Es kommt am meisten das menschlich Fremde gerade in der indischen Ausdrucksweise zustande, weil der Engel am verwandtesten dem Menschen ist, und sich daher am deut­lichsten als Engel aussprechen kann.",
      "Schon weniger war es jenen Wesen der höheren Hierarchien mög­lich, sich in ihrer unmittelbaren Eigenart auszusprechen, die sich durch die Urperser aussprachen. Denn das waren Wesenheiten der nächst­höheren Stufe, das waren die Erzengel, die durch die Seele des ur­persischen Volkes sprachen. Und weil diese eben um zwei Stufen höher stehen als der Mensch, so ist das, was sie mit den menschlichen Werkzeugen aussprechen können, ihrem eigenen Wesen fremder als das, was die Engel durch die Inder aussprechen konnten. So wird",
      "Stufe um Stufe die Sache immer menschlicher. Dennoch aber ist es immer vorhanden, dieses Herunterfliessen aus den höheren Hierar­chien. Durch die Seele der babylonischen, der chaldäischen, der ägyp­tischen Bevölkerung sprechen sich aus die Geister der Persönlichkeit. Da kommt deshalb auch die Persönlichkeit am allermeisten heraus, und da ist das, was der Mensch noch zu geben vermag aus dem, was herunterfliesst, seinem Ursprunge am fremdesten und wird am aller­meisten menschlich-persönlich. So haben wir, wenn wir fortschreiten bis herein zum babylonisch-ägyptischen Zeitraum, eine fortdauernde Offenbarung der Engel, der Erzengel und der Geister der Persönlich­keit.",
      "Wir können insbesondere bei den Persern genau verfolgen, wie sie ein Bewusstsein davon hatten, dass da hereinwirkten als die haupt­sächlichsten Geister die Archangeloi in das, was wir den menschlichen Organismus, den Gesamtorganismus nennen können. Allerdings müs­sen wir da nicht einen Durchschnittsperser nehmen, wenn wir das Her-einströmen dessen, was aus den höheren Hierarchien herunterfliesst, in Betracht ziehen wollen.",
      "Es strömte auch auf den Durchschnitts­perser herein; aber wissen, wie das geschieht, die Sache durchschauen, das konnten nur diejenigen, welche die unmittelbaren Schüler waren des Inspirators der Urperserkultur, des Zarathustra selber. Und die wussten es in der Tat; denn Sie werden sich vielleicht erinnern aus mancherlei Darstellungen der Zarathustralehre, die ich selbst schon gegeben habe, oder auch aus dem, was exoterisch überliefert ist, dass sich in der Anschauung der Urperser das Urgöttliche, Zervan Akarana offenbart durch die beiden gegensätzlichen Mächte Ormuzd und Ahriman.",
      "Nun waren sich die alten Perser klar darüber, dass alle solche Dinge, die sich im Menschen offenbaren, aus dem Makrokos­mos herstammen, und dass die Erscheinungen des Makrokosmos, namentlich also die Bewegungen und Stellungen der Sterne, einen ge­heirnnisvollen Zusammenhang haben mit dem, was im Mikrokosmos, im Menschen liegt. Daher sahen die Schüler des Zarathustra den äusseren Ausdruck, das Bild für Zervan Akarana, für dasjenige, was durch alle Zeiten als Urwesen ewig webt und lebt, in dem Tierkreis, und das Wort ,,Zodiakus\" erinnert noch an das Wort Zervan Akarana.",
      "Also in dem Tierkreise sahen sie es, und aus den zwölf Richtungen des Tierkreises sahen die Schüler des Zarathustra herkommen zwölf Mächte, von denen die eine Hälfte nach der lichten Seite, gleichsam nach der Lichtseite des Tierkreises, da, wo die Sonne oben bei Tag durchläuft, gerichtet war; die andere Hälfte war der finsteren Seite des Tierkreises, dem Ahriman - wie sie sagten - zugewendet. Also von zwölf Seiten des Weltenalls herkommend und in die Menschen­organisation eindringend, so dachte sich der Perser die makrokosmi­schen Kräfte; die strömten ein in die Menschheitsorganisation, wirk­ten und arbeiteten in ihr, so dass sie im Menschen präsent, gegenwärtig sind. Daher muss sich der menschlichen Intelligenz das, was sich her­anentwickelt durch die Zwölfzahl' auch mikrokosmisch offenbaren; das heisst es muss sich das durch die Zwölfzahi der Amshaspands (Erzengel) auch im Mikrokosmos ausdrücken, und zwar als eine letzte Manifestation sozusagen dieser zwölf geistigen makrokosmischen Wesenheiten, die schon früher gewirkt haben, die vorbereitet haben, was nur eine letzte Ausbildung während der persischen Kultur ge­funden hat.",
      "Die heutige Physiologie könnte wissen, wo die zwölf mikrokosmi­schen Gegenbilder der zwölf Amshaspands sind. Das sind die zwölf Ilauptnerven' die aus dem Haupte entspringen; die sind nichts anderes als etwas, was durch das Hereinstrahlen der zwölf makrokosmischen Mächte in den Menschen entstanden ist und im Menschen sich mate­riell verdichtet hat. Von den zwölf Seiten des Tierkreises aus wirkten die zwölf Erzengel-Wesen - so haben die alten Perser es sich vorge­stellt; und um allmählich das hervorzubringen, was heute unsere In­telligenz ist, wirkten sie in zwölf Strahlen herein in das menschliche Haupt. Natürlich wirkten sie in der urpersischen Zeit nicht zum erstenmal in den Menschen herein, sondern zuletzt so, dass wir zwölf kosmische Strahlungen, zwölf Erzengel-Strahlungen haben, die sich dann im Haupte des Menschen verdichtet haben zu den zwölf Haupt­gehirnnerven, wie wenn sie da drin materiell gefroren wären. Und da man in späterer Zeit selbstverständlich immer auch das weiss, was man früher schon gewusst hat, so konnten die Perser auch wissen, dass niedrigere Geister als die Erzengel früher in der indischen Kultur gewirkt",
      "hatten. Die nächste Stufe unter den Amshaspands, unter den Erzengeln, nannten die Perser Izads, und von denen unterschieden sie 28 bis 31. Die sind also das, was weniger hohe Tätigkeit, was seeli­sche Tätigkeit im Menschen bewirkt. Das sind diejenigen, die ihre Strahlen hereinsenden und die den 28, beziehungsweise 30 bis 31 Rückenmarksnerven des Menschen entsprechen. So dass Sie unsere moderne Physiologie ins Geistige, in Spirituelles makrokosmisch um­gesetzt haben in den zwölf Amshaspands des Zarathustrismus und in den 28 bis 31 Izads der nächst niedrigeren Hierarchie.",
      "In der Tat ist es ja so in der historischen Entwicklung der Mensch­heit, dass das, was ursprünglich spirituell aufgetreten ist, uns wieder­um durch anatomisches Zerschnitzeln vor Augen tritt, weil die Dinge, die früher dem hellseherischen Schauen spirituell zugänglich waren, in späteren Zeitaltern materialistisch zum Vorschein kommen. In der Tat, hier zeigt sich eine wunderbare Brücke zwischen Zarathustrismus in seiner Spiritualität und unserer modernen Physiologie in ihrem Materialismus. Es wird ja allerdings das Schicksal des grössten Teiles der Menschheit sein, dass eine solche Idee von dem Zusammenhange der persischen Amshaspands und Izads mit unseren Nerven als Wahnsinn insbesondere diejenigen betrachten, die heute materialisti­sche Physiologie studieren. Aber wir haben Zeit, denn der persische Zeitraum wird sich erst im sechsten, in dem Zeitraum, der nach dem unsrigen kommt, vollständig wiederholen. Da wird erst die Grund­bedingung gegeben sein, dass bei einem grossen Teile der Menschheit solche Dinge verstanden werden können. Daher müssen wir uns da­mit begnügen, dass wir heute auf solche Dinge innerhalb der geistes-wissenschaftlichen Weltanschauung hindeuten können. Aber solche Hinweise müssen heute auch erfolgen, wenn im wahren Sinne des Wortes von geisteswissenschaftlicher Weltanschauung geredet werden soll, und wenn man nicht bloss allgemein phrasenhaft darauf aufmerk­sam machen will, dass der Mensch eine mikrokosmische Wieder­holung des Makrokosmos ist.",
      "Auch in anderen Gegenden hat man gewusst, dass das, was im Menschen sich ausdrückt, von aussen hereinfliesst. Daher hat man zum Beispiel in gewissen Zeiten der germanischen Mythologie von",
      "zwölf Strömen gesprochen, welche von Nifiheim nach Muspelheim fliessen. Die zwölf Ströme sind nicht im physisch-materiellen Sinne ge-meint, sondern sie sind das, was, heliseherisch geschaut, als ein ge­wisser Abglanz vom Makrokosmos hereinhiesst in den menschlichen Mikrokosmos, in das Wesen, das auf der Erde herumwandelt und sich durch makrokosmische Kräfte entwickeln soll.",
      "Und das muss ja aller­dings betont werden, dass diese Strömungen heute im Grunde ge­nommen als astralische Ströme zu sehen sind, während sie in den atlantischen Zeiten, die unmittelbar auf Lemurien folgten, und in Lemurien selbst als ätherische Strömungen gesehen werden konnten. Daher muss ein mit der Erde verwandter Planet, der nur in einem früheren Stadium der Entwicklung ist, so etwas Ähnliches zeigen.",
      "Und da man aus der Ferne oft Dinge beobachten kann, die sich in der Nähe wegen der Vereinzelung unserem Wahrnehmen entziehen, so könnte man bei einem ähnlichen Planeten wie die Erde, wenn er ge­nügend weit entfernt ist und solche früheren Entwicklungsstufen unserer Erde durchmacht' diese zwölf Strömungen eventuell heute noch beobachten. Allerdings werden sie etwas anders ausschauen, als es einmal auf der Erde ausgeschaut hat; allerdings ist die Entfernung notwendig, denn wenn Sie zum Beispiel innerhalb eines Mücken­schwarmes stehen, so erscheint Ihnen auch der Schwarm nicht mit den wolkenartigen Abschattierungen; die nehmen Sie nur wahr, wenn Sie ihn von ferneher sehen.",
      "Das, was ich jetzt gesagt habe, liegt jenen Beobachtungen zugrunde, die von Marskanälen sprechen. Dem, was man als Marskanäle beschreibt, liegt in Wahrheit das zugrunde, was ich Ihnen eben angedeutet habe; man hat es da zu tun mit gewissen Kraftströmungen' die einem früheren Zustande der Erde entsprechen und die in der altgermanischen Mythe als Strömungen beschrieben sind, die von Nifiheim nach Muspelheim flossen.",
      "Das ist allerdings eine arge Ketzerei für die heutige Schulphysiologie und Schulastro­nomie; aber diese werden sich ja schon im Laufe der nächsten Jahr­tausende manche Korrektur gefallen lassen müssen.",
      "Das alles kann uns darauf hinweisen, in welchen Abgrund von tiefer Weisheit wir ahnend hineinblicken, wenn der einfache Satz ausge­sprochen wird: Der menschliche Mikrokosmos ist eine Art Spiegelbild",
      "des Makrokosmos. Solche Sätze machen uns so recht darauf auf­merksam, dass diese Phrase sich unmittelbar berührt mit den tiefsten Weistümern; denn der Satz, der Mensch sei ein Mikrokosmos gegen­über dem Makrokosmos, kann wirklich eine blosse triviale Phrase sein, - richtig erfasst aber kann sie uns darstel]en die Zusammenfas­sung von Millionen und Abermillionen einzelner konkreter Weis­tümer. Und das sollte hervorgehoben werden, um Ihnen zu zeigen, wie die Konfiguration war bei den Seelen der urpersischen Menschen-kultur. Da war, namentlich bei den leitenden Persöniichkeiten, eine lebendige Empfindung von diesem Zusammenhange des Menschen mit dem Makrokosmos vorhanden.",
      "Nachdem nun bis zur babylonisch-ägyptischen Kultur hin jene Wesenheiten gewirkt hatten, welche wir der Reihe nach bezeichnet haben als Engel, Erzengel und Geister der Persönlichkeit, folgte dann jene merkwürdige griechisch-lateinische Kultur, welche die Persön­lichkeit als solche, das Weben des Ich im Ich ganz besonders zum Ausdrucke gebracht hat. Da offenbarten sich auch gewisse Wesen­heiten, die auf einer Stufe höher sind als die Geister der Persönlich­keit; es offenbarten sich die Geister der Form.",
      "Aber die Offenbarung dieser Geister der Form geschah auf eine andere Art als die der Geister der Persönlichkeit, der Erzengel und Engel. Wie offenbaren sich Engel, Erzengel und Geister der Persönlichkeit in unserer nach-atlantischen Zeit?",
      "Sie wirken in das menschliche Innere herein; die Engel für den Inder inspirierend, die Erzengel auch noch ähnlich so bei dem Urperser, aber doch in einer Weise, dass das ,,Menschliche\" etwas mehr schon zur Geltung kommt; der Geist der Persönlichkeit aber stand gleichsam hinter den Seelen der Ägypter, sie antreibend, herauszustellen auf den physischen Plan das Spirituelle. Anders offen­baren sich die Geister der Form.",
      "Die offenbaren sich von unten nach oben als viel mächtigere Geister, die nicht darauf angewiesen sind, sich des Menschen bloss als Werkzeug zu bedienen; sie offenbaren sich in den Reichen der Natur, die um uns herum sind, in der Konfigura­tion der Wesen des mineralischen, pflanzlichen, tierischen Reiches. Und da muss der Mensch, wenn er die Geister der Form an ihrer Offenbarung erkennen will, sein Auge nach aussen richten, muss die",
      "Natur beobachten, muss ergründen, was die Geister der Form in die Natur hineingeheinanisst haben. Daher empfängt der Mensch in dem griechischen Zeitraum, wo vorzugsweise die Geister der Form sich manifestieren, keinen direkten Einfluss, der inspirierend wirkt.",
      "Die Einwirkung der Geister der Form vollzieht sich vielmehr so, dass der Mensch durch das Äussere der Sinnenwelt gereizt wird, dass seine Sinne mit Freude, mit Beseeligung sich hinwenden auf das, was rings­herum ausgebreitet ist, dass er versucht zu idealisieren, auszugestalten, was ausgebreitet ist. Also von aussen her reizen die Geister der Form.",
      "Und einer der hauptsächlichsten Geister der Form ist derjenige, der sich hinter Jahve oder Jehovah verbirgt. Und obzwar die Geister der Form sieben an der Zahl sind und in den verschiedenen Naturreichen wirken, so ist doch eine Empfindungsfählgkeit der gegenwärtigen Menschen eigentlich nur für den einen Geist vorhanden, den wir als Jahve bezeichnen.",
      "Wenn wir das alles bedenken, so erscheint es uns begreiflich, dass gegen den vierten Zeitraum hin der Mensch mehr oder weniger verlassen wird der Hauptsache nach von diesen dirigierenden Mächten, von den Engeln, Erzengeln und Geistern der Persönlich­keit, und dass er seinen Blick ganz herauswendet auf die äussere Welt, auf den physischen Horizont, wo sich die Geister der Form offenbaren. Hinter dieser physischen Welt haben sie freilich auch schon früher gesteckt, sie haben sich sozusagen nur nicht zu erkennen gegeben für das menschliche Erkennen.",
      "In dem Zeitraum, der unmittelbar der atlantischen Katastrophe folgte, wirkten die Geister der Form; sie wirkten in den Naturreichen, in den Gesetzen von Wind und Wetter, in den Gesetzen von Pflanze, Tier und Mineral. Sie haben auch in noch älteren Zeiten gewirkt.",
      "Aber der Mensch lenkte nicht hin den Blick auf das, was ihm da äusserlich entgegentrat, denn er war innerlich inspiriert von den anderen. Er war abgelenkt von der äusseren Welt. Woher kam das?",
      "Wie haben wir es zu verstehen, dass diese anderen Hierarchien, die, wie wir wissen, niedriger stehen als die Geister der Form, dem damals schon bestehenden Wirken der Geister der Form gegenüber ihren Einfluss in so beherrschender Weise geltend machten? Das hängt zu­sammen mit einer ganz bestimmten periodischen Entwicklung unserer",
      "gesamten Erde. Diese Dinge sind für den hellseherischen Blick, der mit Hilfe der Akashachronik nach rückwärts schaut, ganz anders als sie sich ausnehmen für die Spekulationen, die auf Grundlage der heutigen geologischen Tatsachen gemacht werden. Wenn wir da zu­rückgehen hinter der Wirksamkeit der Geister der Persönlichkeit in der chaldäischen Periode, hinter die der Erzengel in der persischen und der Engel in der altindischen Periode, so kommen wir ja zu dem Zeitraum unserer Erde, in dem die atlantische Katastrophe am aller­ärgsten wütete. Wir kommen allmählich ganz in die atlantische Kata­strophe hinein. Es ist die Zeit, auf welche hinweisen die Sintflutsagen der verschiedenen Völker, und in der Tat hat es damals anders ausge­sehen als die geologischen Hypothesen der gegenwärtigen Zeit es aus­malen. In der noch früheren atlantischen Zeit, da hat es wiederum ganz anders ausgeschaut. Der Mensch war ein verwandelbares Wesen. Das ganze Antlitz der Erde war vor dieser Katastrophe anders als es sich",
      "die Menschen jetzt träumen lassen. Nun können Sie sich denken, dass damals in noch höherem Masse geistige Hierarchien auf die Erde her­eingewirkt haben.",
      "Wir haben gleichsam eine Grenze zwischen den alten Einwirkungen in der atlantischen Zeit und denen in der nachatlantischen Zeit, eine Grenze, die ausgefüllt ist von der atlantischen Katastrophe, von jenen Vorgängen, die das Antlitz unserer Erde in bezug auf Verteilung von Wasser und Land total verändert haben. Solche Zeiten und ihre Ver­änderungen hängen zusammen mit grossen Vorgängen in der Kon­stellation, in der Lage und Bewegung der mit der Sonne zusammen­hängenden Weltenkörper.",
      "Und in der Tat wird aus demMakrokosmos­raum hereindirigiert das, was sich als solche Perioden in der Erde ab­spielt. Es würde heute zu weit führen, wenn ich Ihnen auseinandersetzen wollte, wie diese aufeinanderfolgenden Perioden dirigiert werden, eingeteilt werden von dem, was man heute in der Astronomie nennt das Vorrücken der Tag- und Nachtgleiche.",
      "Das hängt zusammen mit der Stellung der Erdachse zur Achse der Ekliptik, das hängt mit grossen Vorgängen in der Konstellation unserer benachbarten Welten-körper zusammen, und da gibt es in der Tat ganz bestimmte Zeiten, in denen durch die eigentümliche Stellung der Erde in ihrer Achse zu den anderen Körpern ihres Systems eine ganz andere Verteilung von Hitze und Kälte auf unserer Erde vorhanden ist als sonst. Es ändern sich die klimatischen Verhältnisse durch diese Stellung der Erdachse zu den Nachbarsternen.",
      "Und in der Tat: Im Laufe von etwas über 25000 Jahren beschreibt unsere Erdachse eine Art von Kegel oder Kreis-bewegung, so dass unsere Erde Zustände, die sie in einer gewissen Zeit erlebt, in einer anderen Form nach 25000 bis 26000 Jahren wieder erlebt, gerade auf höherer Stufe. Immer aber zwischen diesen grossen Zeitabschnitten liegen kleinere Abschnitte.",
      "Und die Sache geht auch nicht durchaus kontinuierlich fort, sondern so, dass ge-wisse Jahre Knotenpunkte, tiefe Einschnitte sind, in denen Wichtiges geschieht. Und da dürfen wir insbesondere darauf hinweisen, weil es für die ganze geschichtliche Entwicklung unserer Erdenmenschheit wesentlich bedeutsam ist, dass im 7.",
      "Jahrtausend vor Christo ein ganz besonders wichtiger astronomischer Zeitpunkt war - wichtig,",
      "weil er sich durch die Konstellation der Erdachse zu den Nachbar­sternen in einer solchen Verteilung der klimatischen Verhältnisse auf Erden ausdrückte, dass eben dazumal die atlantische Katastrophe wirkte, 6 bis 7 bis 8 Tausend Jahre vor unserer Zeitrechnung - sie wirkte ja durch lange Zeiten hindurch. Wir können hier nur das be­tonen, was richtig ist und nicht die phantastischen Zeiträume, die an­gegeben werden, denn es liegt viel weniger weit hinter uns, als ge­wöhnlich geglaubt wird. In diesem Zeitraum wirkten allerdings die makrokosmischen Verhältnisse so ins Physische hinein, dass sich die Wirkung ausprägte in diesen gewaltigen physischen Revolutionen unserer Erde, die uns als die atlantische Katastrophe entgegentreten und das Äntlitz der Erde vollständig veränderten. Das war die stärkste physische Umänderung, das war die stärkste Einwirkung vom Makro-kosmos auf die Erde. Dafür war damals der Einfluss von dieser Seite her auf den Geist der Menschen am geringsten; deshalb konnten in diesem Zeitraum die weniger starken Mächte der Hierarchien be­ginnen, einen starken Einfluss auf den Menschen auszuüben, der dann allmählich wieder abflutete.",
      "Also da, wo die Geister der Form mächtig revoltierend herein-wirkten auf das Physische, da haben sie nicht so viel Zeit gehabt, auch noch auf den Geist der Menschen zu wirken, so dass das Physische dem Menschen sozusagen unter den Füssen entschwunden ist. Dafür aber war der Mensch gerade während der atlantischen Katastrophe am meisten geistentrückt und kam erst allmählich wiederum in die physische Welt herein in der nachatlantischen Zeit. Nun wird es Ihnen nicht schwer werden, sich vorzustellen - wenn Sie sich also denken, dass der geringste Einfluss auf den menschlichen Geist ausgeübt worden ist in dieser Zeit, also etwa 6 bis 7 bis 8 Tausend Jahre vor unserer christlichen Zeitrechnung, und der grösste Einfluss auf die physischen Verhältnisse der Erde -, dass es einen anderen Zeitpunkt geben kann, wo das Gegenteil der Fall ist: wo diejenigen, die eine solche Sache wissen können, in umgekehrter Art den geringsten Ein­fluss auf das Physische, dafür aber gerade von den Geistern der Form den grössten Einfluss auf den menschlichen Geist verspüren. Sie können sich zunächst einmal hypothetisch in der Seele konstruieren,",
      "dass es einen Punkt geben kann in der Geschichte, wo das Umgekehrte von der grossen atlantischen Katastrophe der Fall ist. Das wird natürlich nicht so leicht zu bemerken sein, denn dem in unserer nach-atlantischen Zeit ja sehr auf das Physische veranlagten Menschen, dem wird die atlantische Katastrophe, in der Erdenteile zugrunde gehen, sehr stark auffallen.",
      "Weniger wird ihm auffallen, wenn die Geister der Form einen starken Einfluss auf die menschliche Persönlichkeit haben und einen geringen Einfluss nur auf das, was äusserlich sich abspielt. Dieser Zeitpunkt, wo das eingetreten ist, was also naturge­mäss die Menschen weniger bemerken, das ist das Jahr 1250 der nach­christlichen Aera.",
      "Und dieses Jahr 1250 ist in der Tat ein ausser-ordentliches, historisch wichtiges Jahr. Das fiel in einen Zeitraum hinein, den man etwa so charakterisieren kann: Die Geister fühlten sich sozusagen gedrängt, auf das genaueste die Art und Weise zum Ausdruck zu bringen, wie man zu den über den andern Hierarchien stehenden höheren göttlichen Wesenheiten hinaufblickt, wie man zu diesen Wesenheiten, die man zunächst als Einheit, erst durch Jahve, dann durch Christus empfindet, ein Verhältnis zu gewinnen sucht und alles menschliche Wissen dazu anwendet, um die Mysterien von dem Christus Jesus zu enthüllen.",
      "Das war ein Zeitpunkt, der insbesondere geeignet war, der Menschheit die Mysterien zu überbringen, die sich unmittelbar im Zusammenhang des Geistigen mit dem Natur-wirken ausprägen. Daher sehen wir, dass dieses Jahr der Ausgangs­punkt ist für grosse präzise Verarbeitungen dessen, was früher nur geglaubt, nur geahnt wurde: der Ausgangspunkt der heute viel zu wenig gewürdigten Scholastik.",
      "Dann aber war es auch der Ausgangs-punkt jener Offenbarung, die in Geistern wie zum Beispiel Agrippa von Nettesheim zum Ausdruck kam, und die am tiefsten in der ganzen Rosenkreuzerei sich ausprägte. Dies weist uns also darauf hin, dass, wenn man die tieferen Kräfte der geschichtlichen Entwicklung suchen will, man doch noch auf ganz andere Verhältnisse eingehen muss als die äusserlich zutage liegenden.",
      "Ja, hinter dem, was ich jetzt gesagt habe, verbergen sich zum Beispiel auch diejenigen Kräfte, die in den schon bestehenden und abflutenden Kreuzzügen wirksam sind. Die ganze europäische Geschichte, namentlich das, was sich abspielt",
      "zwischen Orient und Okzident, ist nur dadurch ermöglicht, dass Kräfte so dahinterstehen, wie ich sie jetzt beschrieben habe.",
      "Wir können also sagen: Es gibt zwei Zeitpunkte, von denen der eine bezeichnet werden kann als eine grosse Umwälzung auf dem äusseren physischen Plan, der andere als der Übergangspunkt von all dem, was in den Mysterien rumoren musste. Aber wir müssen daran festhalten, dass in der Tat für alle solche Dinge wiederum andere Gesetze bestehen, welche die Hauptgesetze durchkreuzen.",
      "Und so begreifen wir, dass in diese Zeit hinein der Ausgangspunkt für grosse Offenbarungen fällt; dass diese Zeit so recht geeignet ist für das Auf­treten eines Menschen, der wie Julianus Apostata einmal inspiriert worden ist in den eleusinischen Mysterien. Er hat dann auf seine Seele wirken lassen, was da herausgekommen ist als die Offenbarungen der Geister der Form.",
      "Aber ungefähr vierhundert Jahre sind es auch im­mer, in denen der erste Ansturm irgendeines gewaltigen Einflusses wirkt; dann beginnt ein Abfluten, dann beginnen sozusagen die Ströme sich zu trennen. Daher wirkte das, was damals geschaut wurde als ein Spirituelles hinter den Naturerscheinungen so, dass man das Spirituelle vergass und nur die Naturerscheinung behielt.",
      "Das ist das Moderne. Und Tycho de Brahe ist zu gleicher Zeit einer der letzten, die noch das Spirituelle hinter demjenigen, was äussere Naturwissen­schaft ist, erfassen. Und gerade Tycho de Brahe ist deshalb eine so wunderbare Persönlichkeit, weil er die äussere Astronomie in so hohem Grade beherrscht, dass er Tausende von Sternen entdeckt und so weiter, und dabei das spirituelle Walten der grossen Mächte wieder­um so in der Seele trägt, dass er in der Tat ganz Europa erstaunen machen kann, als er kühn und keck den Tod des Sultans Soliman vor­aussagte.",
      "Wir sehen: Aus dem spirituellen Naturwissen, das 1250 an­fängt und das uns äusserlich entgegentritt bei solchen Geistern wie Agrippa von Nettesheim, schält sich allmählich heraus dasjenige, was später nur äusseres Naturwirken ist; während das Innere, das Spiri­tuelle, in jener geheimnisvollen Strömung verbleibt, die uns als Rosenkreuzerei bekannt ist. Da fliessen dann die beiden Ströme dahin.",
      "Ja, es ist merkwürdig, wie sich sogar innerhalb von Persönlich­keiten dieses Auseinanderschälen zeigt. Ich habe schon einmal, ziemlich",
      "am Anfange unserer deutschen Bewegung, darauf aufmerksam gemacht, wie in einer Persönlichkeit des ,5. Jahrhunderts das auf­tritt, was sich hier als spirituelle Bewegung fortzieht, noch mit einem gewissen Naturwissen verbunden, wie dann das Spirituelle abgewor­fen wird und rein äusserlich weiterlebt.",
      "An einer einzelnen Individualität können wir das verfolgen; an der des Nikolaus Cusanus (1401-1464). Wenn wir ihn nur lesen - man kann noch mehr tun als lesen bei ihm -schon durch das Lesen stellt sich heraus, wie bei ihm noch verbunden war tiefstes spirituelles Anschauen mit dem äusseren Naturwissen, namentlich wo dieses sich in mathematische Formen kleidet.",
      "Und weil er eine Einsicht davon hatte, wie schwer das zu erreichen ist in einer Zeit, die immer mehr und mehr nach der äusseren Gelehrsam­keit sich hinbewegt, nannte er sein Werk aus einer welthistorischen Bescheidenheit heraus ,,Gelehrte Unwissenheit\", ,,docta ignorantia\". Natürlich wollte er damit nicht ausdrücken, dass er ein ganz besonders dummer Kerl sei, sondern dass das, was er zu sagen hatte, über dem liegt, was sich nunmehr entwickeln wird als blosse äussere Gelehrsam­keit.",
      "Wenn wir mit einem heute beliebt gewordenen Worte reden wollen, so können wir sagen: Diese ,,Gelehrte Unwissenheit\" ist eine Übergelehrsamkeit. - Dann wurde er, wie Sie wissen, wiedergeboren, und zwar sehr bald in diesem Falle, als Nikolaus Kopernikus. Dieselbe Wesenheit, die in Nikolaus Cusanus war, wirkte weiter in Nikolaus Kopernikus.",
      "Aber es zeigt sich, wie gerade in jenen Zeiten die Mensch­heitsorganisation so nach dem Physischen hin vorgerückt ist, dass die ganze Tiefe des Nikolaus Cusanus in Kopernikus nur so wirken konnte, dass eben das äussere physische Weltensystem zustande kam. Was in Cusanus lebte, wurde gleichsam flitriert, das Spirituelle abge­worfen und umgewandelt zu äusserem Wissen.",
      "Da sehen wir hand­greiflich, wie in kurzer Zeit wirken sollte jener mächtige Impuls vom Jahre 1250, wo er seinen Zeitmittelpunkt hatte. Und das, was da hereinströmte auf unsere Erde in diesem Punkt, das wirkte in seiner Art durchaus weiter fort.",
      "Es wirkte in diesen beiden Strömungen fort, von denen die eine materialistisch ist und. noch materialistischer werden wird, die andere nach dem Spirituellen trachtet und sich ins­besondere in dem kundgab, was wir als Rosenkreuzeroffenbarung",
      "kennen, die am intensivsten eben von diesem Ausgangspunkte aus floss, wenn sie sich auch vorher schon vorbereitet hatte.",
      "So sehen Sie, dass wir sozusagen eine Art 6 bis 7 bis 8 Jahrtausende dauernden Zeitraum haben, in dem die Erdentwicklung einen wichti­gen Zyklus durchläuft in bezug auf die historischen Tatsachen, in welche die Menschenentwicklung hineinverwoben ist. Solche Zyklen werden wiederum von anderen durchschnitten, denn es wirken eben die verschiedensten periodischen Kräfte auf unsere Erdentwicklung ein. Nur dann, wenn wir auseinanderlegen - wenn wir die einzelnen Kräfte kennenlernen und sozusagen nachsehen, wie sie sich zusammen gestalten, nur dann können wir allmählich dahinterkommen, wie die Dinge auf der Erde geschehen. Durch alle solche Kräfte und Gesetz­mässigkeiten wird eigentlich die Menschheit vorwärtsgebracht' wird der menschliche Fortschritt bewirkt. Wissen Sie doch, dass von einer anderen Strömung her ein wichtiger Knotenpunkt in unser Jahrhun­dert gelegt ist, der in dem Rosenkreuzermysterium angedeutet ist: Das Wiederhineinsehen in die ätherische Welt und die Offenbarung des Christus innerhalb der ätherischen Welt. Das gehört aber einer anderen Strömung an. Ich spreche jetzt mehr von Kräften, die in die breite Basis des historischen Geschehens hineinwirken.",
      "Wenn wir aber vollständig das historische Geschehen verstehen wollen, dann müssen wir noch berücksichtigen, dass solche Knoten-punkte der Entwicklung stets mit gewissen Stellungen der Sterne zu­sammenhängen, und dass unsere Erdachse im Jahre 1250 auch in einer gewissen Stellung war, so dass die sogenannte kleine Achse der Eklip­tik eine ganz besondere Lage hatte zu der Erdachse. Wenn wir also be­rücksichtigen, dass das, was auf der Erde geschieht, durch grosse Himmelsverhältnisse bewirkt wird, dann können wir schon an den äusseren klimatischen Verhältnissen sehen, dass innerhalb der Erde wieder spezialisiert und differenziert wird. Nicht wahr, dadurch, dass aus dem Kosmos heraus die Kräfte in gewisser Weise wirken, ist es um den Gürtel der Erde so, dass wir dort die heisse Zone haben, dann kommt die gemässigte, dann die kalte. Das kann als eine Art von Bei­spiel genommen werden dafür, wie auf dem physischen Plane sich geltend macht, was aus der Sonne und anderen Verhältnissen heraus",
      "durch das geistige Geschehen bewirkt wird. Aber nun wird wiederum innerhalb der Erde selber differenziert; das Klima ist ein anderes, wenn man in der heissen Zone es zu tun hat mit Tiefen oder Höhen; auf den Höhen kann es trotzdem sehr kalt sein. Daher ist unter denselben Graden ganz anders klimatisch das Verhältnis verteilt, wenn wir in Afrika oder Amerika die Dinge betrachten. Aber es gibt auch etwas in der geistigen Entwicklung, was sich mit dieser Art von Differenzie­rung vergleichen lässt, so dass in der Tat in Zeiträumen, in denen viel­leicht weithin auf der Erde ein ganz bestimmter Charakter durch die Sternkonstellation herrscht, Modifikationen in den Geistern und See­len der Menschen, Spezialverhältnisse eintreten. Das ist besonders wichtig, denn es muss in der Tat zuweilen geschehen, dass für weit hinaus gesorgt wird.",
      "Denken Sie sich doch einmal, dass die weise Weltenlenkung - es ist das natürlich nur vergleichsweise gesprochen - sich sozusagen vor Jahrtausenden vornehmen musste: Da ist eine Gruppe von Seelen, die muss ich vorbereiten, dass sie in der nächsten Inkarnation diese oder jene Aufgabe vollziehen können. Da müssen Zusammenhänge ge­schaffen werden, so dass vielleicht eine kleine Gruppe von Menschen, die gerade etwas ganz Bestimmtes erfahren haben, die zusammen auf einem kleinen Fleck der Erde inkarniert sind, etwas durchmachen können, was für diesen Zeitpunkt unbedeutend erscheint; wenn man aber den Blick darauf hinwendet, wie solche Menschen, die auf einen kleinen Raum zusammengedrängt sind, in ihrer nächsten Verkörpe­rung auseinandergeworfen werden und gerade das, was sie auf dem engen Raum erhalten haben, später für die gesamte Menschheit wirken, dann gewinnt die Sache ein anderes Ansehen. Und so können wir be­greifen, dass in Zeiten, wo der Gesamtcharakter der Menschheit ein ganz bestimmter ist, in abgesonderten Teilen der Kultur etwas auf­tritt, was ganz auffallend sich ausnimmt, was sich von diesem Gesamt-charakter durchaus unterscheidet. Sehen Sie, so etwas möchte ich Ihnen erwähnen, weil es unserer Zeit ziemlich nahe liegt.",
      "Im Steinthal bei Strassburg hat Oberlin gelebt. Es hat insbesondere der tiefsinnige deutsche Psychologe und Forscher Schubert immer auf diesen Oberlin hingewiesen. Es war eine eigenartige Persönlichkeit,",
      "dieser Oberlin, und er hat in eigenartiger Weise auf die Seelen ge­wirkt. Er war eine hellsichtige Persönlichkeit - ich kann dies nur an­deuten - und war wirklich in der Lage, nachdem er verhältnismässig früh die Gattin verloren hatte, mit der Individualität der Gattin so zusammenzuleben, wie man mit einem Lebenden zusammenlebt.",
      "Und nun notierte er sich Tag für Tag, was da oben, wo seine Gattin lebte, geschah; und er legte das auch in einer Landkarte des Himmels dar und zeigte es den Leuten, die um ihn herum waren, so dass in der Tat eine ganze Gemeinde da war, die teilnahm an dem Leben, das Oberlin mit seiner verstorbenen Gattin führte. Es ist eine eigenartige, de­placierte Sache, dass in die Wende des 18. und 19.",
      "Jahrhunderts so etwas hineingestellt ist. Aber wenn Sie in Betracht ziehen, was ich ge­sagt habe, so werden Sie den Sinn einer solchen Sache erblicken. Und solche Dinge, wie sie sich dem Oberlin geoffenbart haben, gehören zum Bedeutsamsten, was auf diesem Gebiete in der neueren Zeit her­ausgekommen ist.",
      "Ich darf vielleicht Sie darauf aufmerksam machen, dass wir jetzt ein sehr schönes kulturhistorisches Werk haben, das diese Verhältnisse von Oberlin behandelt, den Roman von Fritz Lien­hard. Sie werden darin ausserordentlich anregende Lektüre, nicht nur in bezug auf die Person dieses Pfarrers, sondern auch auf die anderen damaligen Kulturverhältnisse finden.",
      "Aus solchen Dingen heraus, die man leicht unterschätzt und als ,,zufällig\" betrachtet, können wir sehen, wie ein solches Geschehen sich hineinstellt in unsere Entwick­lung, wie es wirken kann im gesamten Zusammenhang der Mensch­heits entwicklung. Denn die Menschen, die in solcherWeise zusammen­gewürfelt sind, die sich um eine Persönlichkeit scharen, die als ihr Führer wirkt, solche Menschen sind dazu bestimmt, in späteren In­karnationen gewisse Aufgaben zu übernehmen.",
      "So sehen Sie - das wollte ich heute Ihnen vor Ihre Seele bringen -wie sozusagen das grösste, das makrokosmische Hereinwirken aus Weltenfernen in die Menschenseelen zusammenhängt mit dem, was sich im kleinsten Raum abspielen kann. Insbesondere interessant werden diese Dinge aber, wenn man ein anderes Gesetz mit solchen Dingen verbindet, mit solchen grossen Knotenpunkten der Entwicklung, wie ein solcher 1250 war. Damals ist am stärksten in die Menschenseele",
      "hereingewirkt worden - und das kann man weniger bemerken als das Rumoren in Kontinenten. Während der atlantischen Katastrophe ist von den Geistern der Form am wenigsten in Menschenseelen ge­wirkt worden; daher haben die jüngeren Hierarchien sozusagen das Feld damals beherrscht. Und so verteilen sich überhaupt die Tätig­keiten der verschiedenen Klassen von hierarchischen Wesenheiten. Wichtig ist es nun, dass wir erkennen, dass in diesen zyklischen Be­wegungen wiederum gewisse Gesetze des Aufstiegs und des Verfalls stecken. Etwas davon habe ich schon angedeutet, als ich sagte, dass ein Ansturm im Jahre 1250 war, dass dann ein Verfall eintrat, der sich in der rein materialistischen Strömung kundgab. Solches können wir öfter bemerken. Und es ist interessant zu sehen, wie aufsteigende und absteigende Zyklen abwechseln in dem, was sich als Menschheits­geschichte vollzieht."
    ],
    "sentences": [
      [
        "Der Einblick in den Entwicklungsgang solcher Individualitäten, wie wir sie gestern sozusagen durch zwei Inkarnationen hindurch haben verfolgen können, gestattet uns, in das geheirnnisvolle Werden und Weben der Weltengeister während der Menschheitsentwicklung, wäh­rend der Menschengeschichte etwas hineinzuschauen.",
        "Denn wenn wir uns die Bilder vor Augen halten, die uns gestern wenigstens skizzen­haft vor die Seele ziehen konnten, die Bilder von Julian dem Abtrün-nigen und von der nächsten Ausprägung dieser selben Individualität im Verlaufe des Menschheitswerdens als Tycho de Brahe, als der grosse Astronom, dann kann uns eines besonders auffallen.",
        "Gerade bei solchen Persönlichkeiten, die innerhalb der Geschichte etwas bedeuten, können wir beobachten, dass sozusagen das Eigentümliche ihrer Individualität von einer Inkarnation in die andere hinüberwirkt; dass aber modifi­zierend in diesem reinen Reinkarnationsgang dasjenige sich geltend macht, was höhere geistige Individualitäten der oberen Hierarchien in der Geschichte vollbringen wollen, und zu dem sie sich nur der einzel­nen Menschen als Werkzeuge bedienen.",
        "Denn wir müssen uns ja sagen:"
      ],
      [
        "Die Individualität, die da auftrat als Julianus Apostata, hatte im vierten nachchristlichen Jahrhundert die Aufgabe, gewissermassen einen letz­ten Anstoss dazu zu geben, die spirituellen Weisheitsschätze früherer Epochen der Menschheitsentwicklung ein letztes Mal zum gewaltigen Auffiammen zu bringen und sie so zu bewahren vor dem Schicksal, das sie leicht hätten finden können, wenn es nur dem aufstrebenden Chri­stentum überlassen geblieben wäre, mit diesem Weisheitsschatz zu wirtschaften.",
        "Und auf der anderen Seite müssen wir uns sagen, dass eine Individualität, die in einer Persönlichkeit inkarniert war, welche das Glück hatte, sogar in die eleusinischen Mysterien eingeweiht zu werden,"
      ],
      [
        "bei ihrer Wiederinkarnation die Bedingungen hatte, auf sich wirken zu lassen eine unendliche Fülle von Zeitenkräften und von Wesenheiten, die in die Zeit hereinwirken, -wie das ja im 16.",
        "Jahrhundert geschehen sollte.",
        "Und wir werden in der Tat völlig verständlich finden das Grosse und Gewaltige, das uns gestern an der Persönlichkeit Tycho de Brahes vor Augen getreten ist und das ja seine Erklärung darin findet, dass eine Unsumme von makrokosmischer Wissenschaft in Verbindung mit dem Mikrokosmos bei Tycho de Brahe auftreten konnte, weil er eben ein Eingeweihter in einer früheren Inkarnation gewesen war.",
        "So werden wir gewahr durch solche Betrachtungen der okkulten Geschichte, dass es alierdingsunmittelbar die Menschen sind, welcheGeschichte machen, dass aber letzten Grundes doch nur die Geschichte verständlich werden kann, wenn wir den Zusammenhang finden zwischen den einzelnen in der Geschichte auftretenden und absterbenden Persönlichkeiten und den individuellenFäden, die sozusagen durch die ganze Menschheitsent-wicklung durchgehen und sich in den Persöniichkeiten reinkarnieren.",
        "Aber wir müssen immer damit zusammenhalten dasjenige, was aus anderen, aus überphysischen Welten hereinströmt durch die Mächte anderer Hierarchien, wenn wir das Menschentum auf unserer Erdober­fläche im Laufe der Geschichte verstehen wollen."
      ],
      [
        "Nun ist uns ja bei unserer Betrachtung vor Augen getreten, wie in all den Kulturzeiträumen nach der atlantischen Katastrophe gewisse übergeordnete Mächte aus den höheren Hierarchien durch die Men­schen hereingewirkt haben.",
        "Wir haben gesagt: Am stärksten tritt das hervor bei der altindischen Seele, die sozusagen nur ein Schauplatz ist für das Hereinwirken höherer, geistiger Wesenheiten.",
        "Etwas mehr tritt es zurück dann in der Seele des Urpersers.",
        "Und dann haben wir gesehen, dass bei der ägyptisch-chaldäischen Kultur die Seele schon die Aufgabe hatte - und das tritt uns besonders bei der Betrachtung der babyloni­schen Seele entgegen - herunterzutragen das Überpersönliche in das Persöniiche, das Spirituelle auf den physischen Plan.",
        "Die Persönlich­keit gewinnt also immer mehr Bedeutung, je mehr wir uns der griechi­schen Zeit nähern, und in dieser, mussten wir sagen, haben wir das Weben des Ich im Ich, die völlige Ausprägung der Persönlichkeit bei den starken und kräftigen Gestalten, die uns im griechischen Zeitraum"
      ],
      [
        "entgegentreten.",
        "In den Griechen und später bei den Römern trat am meisten das zurück, was nur der Individualität aus höheren Welten zu­nächst gegeben werden kann; dagegen trat das hervor, was der Mensch als sein eigentlich Menschliches in seiner Persönlichkeit ausprägt."
      ],
      [
        "Nun kann ja die Frage entstehen, und die Beantwortung dieser Frage wird uns erst den ganzen okkulten Gang der Geschichte tiefer begreif­lich machen können: Was sind denn das eigentlich für Geister, welche durch die Inder, die Urperser, durch die Babylonier, Chaldäer und Ägypter gewirkt haben, welchen Hierarchien gehören sie an?",
        "Wir können aus den Forschungen, die uns durch die okkulten Quellen möglich sind, allerdings in einer gewissenWeise sagen, welche Indivi­dualitäten der höheren Hierarchien sich in jeder dieser genannten Zeit­läufe der Menschen als Werkzeuge bedienten, um durch sie zu wirken."
      ],
      [
        "In die alte indische Seele herein, also in jene Seele, die sozusagen kultur-schöpferisch war unmittelbar nach der atlantischen Katastrophe, in diese ergossen ihre Kräfte herein diejenigen Wesenheiten, die wir ge­wohnt sind Angeloi oder Engel zu nennen.",
        "So dass wir in einer ge­wissen Beziehung recht haben, wenn wir sagen: Wenn ein alter Inder sprach, wenn er das, was seine Seele bewegte, ausdrückte, so ist es so, dass durch seine Seele nicht seine eigene Ichheit direkt sprach, sondern ein Engel, ein Angelos."
      ],
      [
        "Weil nun der Engel nur eine Stufe über der Menschheit steht, so ist er das dem Menschen verwandteste Wesen der höheren Hierarchien, und daher konnte er sich sozusagen am meisten in seiner Eigenart aussprechen.",
        "Es kommt am meisten das menschlich Fremde gerade in der indischen Ausdrucksweise zustande, weil der Engel am verwandtesten dem Menschen ist, und sich daher am deut­lichsten als Engel aussprechen kann."
      ],
      [
        "Schon weniger war es jenen Wesen der höheren Hierarchien mög­lich, sich in ihrer unmittelbaren Eigenart auszusprechen, die sich durch die Urperser aussprachen.",
        "Denn das waren Wesenheiten der nächst­höheren Stufe, das waren die Erzengel, die durch die Seele des ur­persischen Volkes sprachen.",
        "Und weil diese eben um zwei Stufen höher stehen als der Mensch, so ist das, was sie mit den menschlichen Werkzeugen aussprechen können, ihrem eigenen Wesen fremder als das, was die Engel durch die Inder aussprechen konnten.",
        "So wird"
      ],
      [
        "Stufe um Stufe die Sache immer menschlicher.",
        "Dennoch aber ist es immer vorhanden, dieses Herunterfliessen aus den höheren Hierar­chien.",
        "Durch die Seele der babylonischen, der chaldäischen, der ägyp­tischen Bevölkerung sprechen sich aus die Geister der Persönlichkeit.",
        "Da kommt deshalb auch die Persönlichkeit am allermeisten heraus, und da ist das, was der Mensch noch zu geben vermag aus dem, was herunterfliesst, seinem Ursprunge am fremdesten und wird am aller­meisten menschlich-persönlich.",
        "So haben wir, wenn wir fortschreiten bis herein zum babylonisch-ägyptischen Zeitraum, eine fortdauernde Offenbarung der Engel, der Erzengel und der Geister der Persönlich­keit."
      ],
      [
        "Wir können insbesondere bei den Persern genau verfolgen, wie sie ein Bewusstsein davon hatten, dass da hereinwirkten als die haupt­sächlichsten Geister die Archangeloi in das, was wir den menschlichen Organismus, den Gesamtorganismus nennen können.",
        "Allerdings müs­sen wir da nicht einen Durchschnittsperser nehmen, wenn wir das Her-einströmen dessen, was aus den höheren Hierarchien herunterfliesst, in Betracht ziehen wollen."
      ],
      [
        "Es strömte auch auf den Durchschnitts­perser herein; aber wissen, wie das geschieht, die Sache durchschauen, das konnten nur diejenigen, welche die unmittelbaren Schüler waren des Inspirators der Urperserkultur, des Zarathustra selber.",
        "Und die wussten es in der Tat; denn Sie werden sich vielleicht erinnern aus mancherlei Darstellungen der Zarathustralehre, die ich selbst schon gegeben habe, oder auch aus dem, was exoterisch überliefert ist, dass sich in der Anschauung der Urperser das Urgöttliche, Zervan Akarana offenbart durch die beiden gegensätzlichen Mächte Ormuzd und Ahriman."
      ],
      [
        "Nun waren sich die alten Perser klar darüber, dass alle solche Dinge, die sich im Menschen offenbaren, aus dem Makrokos­mos herstammen, und dass die Erscheinungen des Makrokosmos, namentlich also die Bewegungen und Stellungen der Sterne, einen ge­heirnnisvollen Zusammenhang haben mit dem, was im Mikrokosmos, im Menschen liegt.",
        "Daher sahen die Schüler des Zarathustra den äusseren Ausdruck, das Bild für Zervan Akarana, für dasjenige, was durch alle Zeiten als Urwesen ewig webt und lebt, in dem Tierkreis, und das Wort ,,Zodiakus\" erinnert noch an das Wort Zervan Akarana."
      ],
      [
        "Also in dem Tierkreise sahen sie es, und aus den zwölf Richtungen des Tierkreises sahen die Schüler des Zarathustra herkommen zwölf Mächte, von denen die eine Hälfte nach der lichten Seite, gleichsam nach der Lichtseite des Tierkreises, da, wo die Sonne oben bei Tag durchläuft, gerichtet war; die andere Hälfte war der finsteren Seite des Tierkreises, dem Ahriman - wie sie sagten - zugewendet.",
        "Also von zwölf Seiten des Weltenalls herkommend und in die Menschen­organisation eindringend, so dachte sich der Perser die makrokosmi­schen Kräfte; die strömten ein in die Menschheitsorganisation, wirk­ten und arbeiteten in ihr, so dass sie im Menschen präsent, gegenwärtig sind.",
        "Daher muss sich der menschlichen Intelligenz das, was sich her­anentwickelt durch die Zwölfzahl' auch mikrokosmisch offenbaren; das heisst es muss sich das durch die Zwölfzahi der Amshaspands (Erzengel) auch im Mikrokosmos ausdrücken, und zwar als eine letzte Manifestation sozusagen dieser zwölf geistigen makrokosmischen Wesenheiten, die schon früher gewirkt haben, die vorbereitet haben, was nur eine letzte Ausbildung während der persischen Kultur ge­funden hat."
      ],
      [
        "Die heutige Physiologie könnte wissen, wo die zwölf mikrokosmi­schen Gegenbilder der zwölf Amshaspands sind.",
        "Das sind die zwölf Ilauptnerven' die aus dem Haupte entspringen; die sind nichts anderes als etwas, was durch das Hereinstrahlen der zwölf makrokosmischen Mächte in den Menschen entstanden ist und im Menschen sich mate­riell verdichtet hat.",
        "Von den zwölf Seiten des Tierkreises aus wirkten die zwölf Erzengel-Wesen - so haben die alten Perser es sich vorge­stellt; und um allmählich das hervorzubringen, was heute unsere In­telligenz ist, wirkten sie in zwölf Strahlen herein in das menschliche Haupt.",
        "Natürlich wirkten sie in der urpersischen Zeit nicht zum erstenmal in den Menschen herein, sondern zuletzt so, dass wir zwölf kosmische Strahlungen, zwölf Erzengel-Strahlungen haben, die sich dann im Haupte des Menschen verdichtet haben zu den zwölf Haupt­gehirnnerven, wie wenn sie da drin materiell gefroren wären.",
        "Und da man in späterer Zeit selbstverständlich immer auch das weiss, was man früher schon gewusst hat, so konnten die Perser auch wissen, dass niedrigere Geister als die Erzengel früher in der indischen Kultur gewirkt"
      ],
      [
        "hatten.",
        "Die nächste Stufe unter den Amshaspands, unter den Erzengeln, nannten die Perser Izads, und von denen unterschieden sie 28 bis 31.",
        "Die sind also das, was weniger hohe Tätigkeit, was seeli­sche Tätigkeit im Menschen bewirkt.",
        "Das sind diejenigen, die ihre Strahlen hereinsenden und die den 28, beziehungsweise 30 bis 31 Rückenmarksnerven des Menschen entsprechen.",
        "So dass Sie unsere moderne Physiologie ins Geistige, in Spirituelles makrokosmisch um­gesetzt haben in den zwölf Amshaspands des Zarathustrismus und in den 28 bis 31 Izads der nächst niedrigeren Hierarchie."
      ],
      [
        "In der Tat ist es ja so in der historischen Entwicklung der Mensch­heit, dass das, was ursprünglich spirituell aufgetreten ist, uns wieder­um durch anatomisches Zerschnitzeln vor Augen tritt, weil die Dinge, die früher dem hellseherischen Schauen spirituell zugänglich waren, in späteren Zeitaltern materialistisch zum Vorschein kommen.",
        "In der Tat, hier zeigt sich eine wunderbare Brücke zwischen Zarathustrismus in seiner Spiritualität und unserer modernen Physiologie in ihrem Materialismus.",
        "Es wird ja allerdings das Schicksal des grössten Teiles der Menschheit sein, dass eine solche Idee von dem Zusammenhange der persischen Amshaspands und Izads mit unseren Nerven als Wahnsinn insbesondere diejenigen betrachten, die heute materialisti­sche Physiologie studieren.",
        "Aber wir haben Zeit, denn der persische Zeitraum wird sich erst im sechsten, in dem Zeitraum, der nach dem unsrigen kommt, vollständig wiederholen.",
        "Da wird erst die Grund­bedingung gegeben sein, dass bei einem grossen Teile der Menschheit solche Dinge verstanden werden können.",
        "Daher müssen wir uns da­mit begnügen, dass wir heute auf solche Dinge innerhalb der geistes-wissenschaftlichen Weltanschauung hindeuten können.",
        "Aber solche Hinweise müssen heute auch erfolgen, wenn im wahren Sinne des Wortes von geisteswissenschaftlicher Weltanschauung geredet werden soll, und wenn man nicht bloss allgemein phrasenhaft darauf aufmerk­sam machen will, dass der Mensch eine mikrokosmische Wieder­holung des Makrokosmos ist."
      ],
      [
        "Auch in anderen Gegenden hat man gewusst, dass das, was im Menschen sich ausdrückt, von aussen hereinfliesst.",
        "Daher hat man zum Beispiel in gewissen Zeiten der germanischen Mythologie von"
      ],
      [
        "zwölf Strömen gesprochen, welche von Nifiheim nach Muspelheim fliessen.",
        "Die zwölf Ströme sind nicht im physisch-materiellen Sinne ge-meint, sondern sie sind das, was, heliseherisch geschaut, als ein ge­wisser Abglanz vom Makrokosmos hereinhiesst in den menschlichen Mikrokosmos, in das Wesen, das auf der Erde herumwandelt und sich durch makrokosmische Kräfte entwickeln soll."
      ],
      [
        "Und das muss ja aller­dings betont werden, dass diese Strömungen heute im Grunde ge­nommen als astralische Ströme zu sehen sind, während sie in den atlantischen Zeiten, die unmittelbar auf Lemurien folgten, und in Lemurien selbst als ätherische Strömungen gesehen werden konnten.",
        "Daher muss ein mit der Erde verwandter Planet, der nur in einem früheren Stadium der Entwicklung ist, so etwas Ähnliches zeigen."
      ],
      [
        "Und da man aus der Ferne oft Dinge beobachten kann, die sich in der Nähe wegen der Vereinzelung unserem Wahrnehmen entziehen, so könnte man bei einem ähnlichen Planeten wie die Erde, wenn er ge­nügend weit entfernt ist und solche früheren Entwicklungsstufen unserer Erde durchmacht' diese zwölf Strömungen eventuell heute noch beobachten.",
        "Allerdings werden sie etwas anders ausschauen, als es einmal auf der Erde ausgeschaut hat; allerdings ist die Entfernung notwendig, denn wenn Sie zum Beispiel innerhalb eines Mücken­schwarmes stehen, so erscheint Ihnen auch der Schwarm nicht mit den wolkenartigen Abschattierungen; die nehmen Sie nur wahr, wenn Sie ihn von ferneher sehen."
      ],
      [
        "Das, was ich jetzt gesagt habe, liegt jenen Beobachtungen zugrunde, die von Marskanälen sprechen.",
        "Dem, was man als Marskanäle beschreibt, liegt in Wahrheit das zugrunde, was ich Ihnen eben angedeutet habe; man hat es da zu tun mit gewissen Kraftströmungen' die einem früheren Zustande der Erde entsprechen und die in der altgermanischen Mythe als Strömungen beschrieben sind, die von Nifiheim nach Muspelheim flossen."
      ],
      [
        "Das ist allerdings eine arge Ketzerei für die heutige Schulphysiologie und Schulastro­nomie; aber diese werden sich ja schon im Laufe der nächsten Jahr­tausende manche Korrektur gefallen lassen müssen."
      ],
      [
        "Das alles kann uns darauf hinweisen, in welchen Abgrund von tiefer Weisheit wir ahnend hineinblicken, wenn der einfache Satz ausge­sprochen wird: Der menschliche Mikrokosmos ist eine Art Spiegelbild"
      ],
      [
        "des Makrokosmos.",
        "Solche Sätze machen uns so recht darauf auf­merksam, dass diese Phrase sich unmittelbar berührt mit den tiefsten Weistümern; denn der Satz, der Mensch sei ein Mikrokosmos gegen­über dem Makrokosmos, kann wirklich eine blosse triviale Phrase sein, - richtig erfasst aber kann sie uns darstel]en die Zusammenfas­sung von Millionen und Abermillionen einzelner konkreter Weis­tümer.",
        "Und das sollte hervorgehoben werden, um Ihnen zu zeigen, wie die Konfiguration war bei den Seelen der urpersischen Menschen-kultur.",
        "Da war, namentlich bei den leitenden Persöniichkeiten, eine lebendige Empfindung von diesem Zusammenhange des Menschen mit dem Makrokosmos vorhanden."
      ],
      [
        "Nachdem nun bis zur babylonisch-ägyptischen Kultur hin jene Wesenheiten gewirkt hatten, welche wir der Reihe nach bezeichnet haben als Engel, Erzengel und Geister der Persönlichkeit, folgte dann jene merkwürdige griechisch-lateinische Kultur, welche die Persön­lichkeit als solche, das Weben des Ich im Ich ganz besonders zum Ausdrucke gebracht hat.",
        "Da offenbarten sich auch gewisse Wesen­heiten, die auf einer Stufe höher sind als die Geister der Persönlich­keit; es offenbarten sich die Geister der Form."
      ],
      [
        "Aber die Offenbarung dieser Geister der Form geschah auf eine andere Art als die der Geister der Persönlichkeit, der Erzengel und Engel.",
        "Wie offenbaren sich Engel, Erzengel und Geister der Persönlichkeit in unserer nach-atlantischen Zeit?"
      ],
      [
        "Sie wirken in das menschliche Innere herein; die Engel für den Inder inspirierend, die Erzengel auch noch ähnlich so bei dem Urperser, aber doch in einer Weise, dass das ,,Menschliche\" etwas mehr schon zur Geltung kommt; der Geist der Persönlichkeit aber stand gleichsam hinter den Seelen der Ägypter, sie antreibend, herauszustellen auf den physischen Plan das Spirituelle.",
        "Anders offen­baren sich die Geister der Form."
      ],
      [
        "Die offenbaren sich von unten nach oben als viel mächtigere Geister, die nicht darauf angewiesen sind, sich des Menschen bloss als Werkzeug zu bedienen; sie offenbaren sich in den Reichen der Natur, die um uns herum sind, in der Konfigura­tion der Wesen des mineralischen, pflanzlichen, tierischen Reiches.",
        "Und da muss der Mensch, wenn er die Geister der Form an ihrer Offenbarung erkennen will, sein Auge nach aussen richten, muss die"
      ],
      [
        "Natur beobachten, muss ergründen, was die Geister der Form in die Natur hineingeheinanisst haben.",
        "Daher empfängt der Mensch in dem griechischen Zeitraum, wo vorzugsweise die Geister der Form sich manifestieren, keinen direkten Einfluss, der inspirierend wirkt."
      ],
      [
        "Die Einwirkung der Geister der Form vollzieht sich vielmehr so, dass der Mensch durch das Äussere der Sinnenwelt gereizt wird, dass seine Sinne mit Freude, mit Beseeligung sich hinwenden auf das, was rings­herum ausgebreitet ist, dass er versucht zu idealisieren, auszugestalten, was ausgebreitet ist.",
        "Also von aussen her reizen die Geister der Form."
      ],
      [
        "Und einer der hauptsächlichsten Geister der Form ist derjenige, der sich hinter Jahve oder Jehovah verbirgt.",
        "Und obzwar die Geister der Form sieben an der Zahl sind und in den verschiedenen Naturreichen wirken, so ist doch eine Empfindungsfählgkeit der gegenwärtigen Menschen eigentlich nur für den einen Geist vorhanden, den wir als Jahve bezeichnen."
      ],
      [
        "Wenn wir das alles bedenken, so erscheint es uns begreiflich, dass gegen den vierten Zeitraum hin der Mensch mehr oder weniger verlassen wird der Hauptsache nach von diesen dirigierenden Mächten, von den Engeln, Erzengeln und Geistern der Persönlich­keit, und dass er seinen Blick ganz herauswendet auf die äussere Welt, auf den physischen Horizont, wo sich die Geister der Form offenbaren.",
        "Hinter dieser physischen Welt haben sie freilich auch schon früher gesteckt, sie haben sich sozusagen nur nicht zu erkennen gegeben für das menschliche Erkennen."
      ],
      [
        "In dem Zeitraum, der unmittelbar der atlantischen Katastrophe folgte, wirkten die Geister der Form; sie wirkten in den Naturreichen, in den Gesetzen von Wind und Wetter, in den Gesetzen von Pflanze, Tier und Mineral.",
        "Sie haben auch in noch älteren Zeiten gewirkt."
      ],
      [
        "Aber der Mensch lenkte nicht hin den Blick auf das, was ihm da äusserlich entgegentrat, denn er war innerlich inspiriert von den anderen.",
        "Er war abgelenkt von der äusseren Welt.",
        "Woher kam das?"
      ],
      [
        "Wie haben wir es zu verstehen, dass diese anderen Hierarchien, die, wie wir wissen, niedriger stehen als die Geister der Form, dem damals schon bestehenden Wirken der Geister der Form gegenüber ihren Einfluss in so beherrschender Weise geltend machten?",
        "Das hängt zu­sammen mit einer ganz bestimmten periodischen Entwicklung unserer"
      ],
      [
        "gesamten Erde.",
        "Diese Dinge sind für den hellseherischen Blick, der mit Hilfe der Akashachronik nach rückwärts schaut, ganz anders als sie sich ausnehmen für die Spekulationen, die auf Grundlage der heutigen geologischen Tatsachen gemacht werden.",
        "Wenn wir da zu­rückgehen hinter der Wirksamkeit der Geister der Persönlichkeit in der chaldäischen Periode, hinter die der Erzengel in der persischen und der Engel in der altindischen Periode, so kommen wir ja zu dem Zeitraum unserer Erde, in dem die atlantische Katastrophe am aller­ärgsten wütete.",
        "Wir kommen allmählich ganz in die atlantische Kata­strophe hinein.",
        "Es ist die Zeit, auf welche hinweisen die Sintflutsagen der verschiedenen Völker, und in der Tat hat es damals anders ausge­sehen als die geologischen Hypothesen der gegenwärtigen Zeit es aus­malen.",
        "In der noch früheren atlantischen Zeit, da hat es wiederum ganz anders ausgeschaut.",
        "Der Mensch war ein verwandelbares Wesen.",
        "Das ganze Antlitz der Erde war vor dieser Katastrophe anders als es sich"
      ],
      [
        "die Menschen jetzt träumen lassen.",
        "Nun können Sie sich denken, dass damals in noch höherem Masse geistige Hierarchien auf die Erde her­eingewirkt haben."
      ],
      [
        "Wir haben gleichsam eine Grenze zwischen den alten Einwirkungen in der atlantischen Zeit und denen in der nachatlantischen Zeit, eine Grenze, die ausgefüllt ist von der atlantischen Katastrophe, von jenen Vorgängen, die das Antlitz unserer Erde in bezug auf Verteilung von Wasser und Land total verändert haben.",
        "Solche Zeiten und ihre Ver­änderungen hängen zusammen mit grossen Vorgängen in der Kon­stellation, in der Lage und Bewegung der mit der Sonne zusammen­hängenden Weltenkörper."
      ],
      [
        "Und in der Tat wird aus demMakrokosmos­raum hereindirigiert das, was sich als solche Perioden in der Erde ab­spielt.",
        "Es würde heute zu weit führen, wenn ich Ihnen auseinandersetzen wollte, wie diese aufeinanderfolgenden Perioden dirigiert werden, eingeteilt werden von dem, was man heute in der Astronomie nennt das Vorrücken der Tag- und Nachtgleiche."
      ],
      [
        "Das hängt zusammen mit der Stellung der Erdachse zur Achse der Ekliptik, das hängt mit grossen Vorgängen in der Konstellation unserer benachbarten Welten-körper zusammen, und da gibt es in der Tat ganz bestimmte Zeiten, in denen durch die eigentümliche Stellung der Erde in ihrer Achse zu den anderen Körpern ihres Systems eine ganz andere Verteilung von Hitze und Kälte auf unserer Erde vorhanden ist als sonst.",
        "Es ändern sich die klimatischen Verhältnisse durch diese Stellung der Erdachse zu den Nachbarsternen."
      ],
      [
        "Und in der Tat: Im Laufe von etwas über 25000 Jahren beschreibt unsere Erdachse eine Art von Kegel oder Kreis-bewegung, so dass unsere Erde Zustände, die sie in einer gewissen Zeit erlebt, in einer anderen Form nach 25000 bis 26000 Jahren wieder erlebt, gerade auf höherer Stufe.",
        "Immer aber zwischen diesen grossen Zeitabschnitten liegen kleinere Abschnitte."
      ],
      [
        "Und die Sache geht auch nicht durchaus kontinuierlich fort, sondern so, dass ge-wisse Jahre Knotenpunkte, tiefe Einschnitte sind, in denen Wichtiges geschieht.",
        "Und da dürfen wir insbesondere darauf hinweisen, weil es für die ganze geschichtliche Entwicklung unserer Erdenmenschheit wesentlich bedeutsam ist, dass im 7."
      ],
      [
        "Jahrtausend vor Christo ein ganz besonders wichtiger astronomischer Zeitpunkt war - wichtig,"
      ],
      [
        "weil er sich durch die Konstellation der Erdachse zu den Nachbar­sternen in einer solchen Verteilung der klimatischen Verhältnisse auf Erden ausdrückte, dass eben dazumal die atlantische Katastrophe wirkte, 6 bis 7 bis 8 Tausend Jahre vor unserer Zeitrechnung - sie wirkte ja durch lange Zeiten hindurch.",
        "Wir können hier nur das be­tonen, was richtig ist und nicht die phantastischen Zeiträume, die an­gegeben werden, denn es liegt viel weniger weit hinter uns, als ge­wöhnlich geglaubt wird.",
        "In diesem Zeitraum wirkten allerdings die makrokosmischen Verhältnisse so ins Physische hinein, dass sich die Wirkung ausprägte in diesen gewaltigen physischen Revolutionen unserer Erde, die uns als die atlantische Katastrophe entgegentreten und das Äntlitz der Erde vollständig veränderten.",
        "Das war die stärkste physische Umänderung, das war die stärkste Einwirkung vom Makro-kosmos auf die Erde.",
        "Dafür war damals der Einfluss von dieser Seite her auf den Geist der Menschen am geringsten; deshalb konnten in diesem Zeitraum die weniger starken Mächte der Hierarchien be­ginnen, einen starken Einfluss auf den Menschen auszuüben, der dann allmählich wieder abflutete."
      ],
      [
        "Also da, wo die Geister der Form mächtig revoltierend herein-wirkten auf das Physische, da haben sie nicht so viel Zeit gehabt, auch noch auf den Geist der Menschen zu wirken, so dass das Physische dem Menschen sozusagen unter den Füssen entschwunden ist.",
        "Dafür aber war der Mensch gerade während der atlantischen Katastrophe am meisten geistentrückt und kam erst allmählich wiederum in die physische Welt herein in der nachatlantischen Zeit.",
        "Nun wird es Ihnen nicht schwer werden, sich vorzustellen - wenn Sie sich also denken, dass der geringste Einfluss auf den menschlichen Geist ausgeübt worden ist in dieser Zeit, also etwa 6 bis 7 bis 8 Tausend Jahre vor unserer christlichen Zeitrechnung, und der grösste Einfluss auf die physischen Verhältnisse der Erde -, dass es einen anderen Zeitpunkt geben kann, wo das Gegenteil der Fall ist: wo diejenigen, die eine solche Sache wissen können, in umgekehrter Art den geringsten Ein­fluss auf das Physische, dafür aber gerade von den Geistern der Form den grössten Einfluss auf den menschlichen Geist verspüren.",
        "Sie können sich zunächst einmal hypothetisch in der Seele konstruieren,"
      ],
      [
        "dass es einen Punkt geben kann in der Geschichte, wo das Umgekehrte von der grossen atlantischen Katastrophe der Fall ist.",
        "Das wird natürlich nicht so leicht zu bemerken sein, denn dem in unserer nach-atlantischen Zeit ja sehr auf das Physische veranlagten Menschen, dem wird die atlantische Katastrophe, in der Erdenteile zugrunde gehen, sehr stark auffallen."
      ],
      [
        "Weniger wird ihm auffallen, wenn die Geister der Form einen starken Einfluss auf die menschliche Persönlichkeit haben und einen geringen Einfluss nur auf das, was äusserlich sich abspielt.",
        "Dieser Zeitpunkt, wo das eingetreten ist, was also naturge­mäss die Menschen weniger bemerken, das ist das Jahr 1250 der nach­christlichen Aera."
      ],
      [
        "Und dieses Jahr 1250 ist in der Tat ein ausser-ordentliches, historisch wichtiges Jahr.",
        "Das fiel in einen Zeitraum hinein, den man etwa so charakterisieren kann: Die Geister fühlten sich sozusagen gedrängt, auf das genaueste die Art und Weise zum Ausdruck zu bringen, wie man zu den über den andern Hierarchien stehenden höheren göttlichen Wesenheiten hinaufblickt, wie man zu diesen Wesenheiten, die man zunächst als Einheit, erst durch Jahve, dann durch Christus empfindet, ein Verhältnis zu gewinnen sucht und alles menschliche Wissen dazu anwendet, um die Mysterien von dem Christus Jesus zu enthüllen."
      ],
      [
        "Das war ein Zeitpunkt, der insbesondere geeignet war, der Menschheit die Mysterien zu überbringen, die sich unmittelbar im Zusammenhang des Geistigen mit dem Natur-wirken ausprägen.",
        "Daher sehen wir, dass dieses Jahr der Ausgangs­punkt ist für grosse präzise Verarbeitungen dessen, was früher nur geglaubt, nur geahnt wurde: der Ausgangspunkt der heute viel zu wenig gewürdigten Scholastik."
      ],
      [
        "Dann aber war es auch der Ausgangs-punkt jener Offenbarung, die in Geistern wie zum Beispiel Agrippa von Nettesheim zum Ausdruck kam, und die am tiefsten in der ganzen Rosenkreuzerei sich ausprägte.",
        "Dies weist uns also darauf hin, dass, wenn man die tieferen Kräfte der geschichtlichen Entwicklung suchen will, man doch noch auf ganz andere Verhältnisse eingehen muss als die äusserlich zutage liegenden."
      ],
      [
        "Ja, hinter dem, was ich jetzt gesagt habe, verbergen sich zum Beispiel auch diejenigen Kräfte, die in den schon bestehenden und abflutenden Kreuzzügen wirksam sind.",
        "Die ganze europäische Geschichte, namentlich das, was sich abspielt"
      ],
      [
        "zwischen Orient und Okzident, ist nur dadurch ermöglicht, dass Kräfte so dahinterstehen, wie ich sie jetzt beschrieben habe."
      ],
      [
        "Wir können also sagen: Es gibt zwei Zeitpunkte, von denen der eine bezeichnet werden kann als eine grosse Umwälzung auf dem äusseren physischen Plan, der andere als der Übergangspunkt von all dem, was in den Mysterien rumoren musste.",
        "Aber wir müssen daran festhalten, dass in der Tat für alle solche Dinge wiederum andere Gesetze bestehen, welche die Hauptgesetze durchkreuzen."
      ],
      [
        "Und so begreifen wir, dass in diese Zeit hinein der Ausgangspunkt für grosse Offenbarungen fällt; dass diese Zeit so recht geeignet ist für das Auf­treten eines Menschen, der wie Julianus Apostata einmal inspiriert worden ist in den eleusinischen Mysterien.",
        "Er hat dann auf seine Seele wirken lassen, was da herausgekommen ist als die Offenbarungen der Geister der Form."
      ],
      [
        "Aber ungefähr vierhundert Jahre sind es auch im­mer, in denen der erste Ansturm irgendeines gewaltigen Einflusses wirkt; dann beginnt ein Abfluten, dann beginnen sozusagen die Ströme sich zu trennen.",
        "Daher wirkte das, was damals geschaut wurde als ein Spirituelles hinter den Naturerscheinungen so, dass man das Spirituelle vergass und nur die Naturerscheinung behielt."
      ],
      [
        "Das ist das Moderne.",
        "Und Tycho de Brahe ist zu gleicher Zeit einer der letzten, die noch das Spirituelle hinter demjenigen, was äussere Naturwissen­schaft ist, erfassen.",
        "Und gerade Tycho de Brahe ist deshalb eine so wunderbare Persönlichkeit, weil er die äussere Astronomie in so hohem Grade beherrscht, dass er Tausende von Sternen entdeckt und so weiter, und dabei das spirituelle Walten der grossen Mächte wieder­um so in der Seele trägt, dass er in der Tat ganz Europa erstaunen machen kann, als er kühn und keck den Tod des Sultans Soliman vor­aussagte."
      ],
      [
        "Wir sehen: Aus dem spirituellen Naturwissen, das 1250 an­fängt und das uns äusserlich entgegentritt bei solchen Geistern wie Agrippa von Nettesheim, schält sich allmählich heraus dasjenige, was später nur äusseres Naturwirken ist; während das Innere, das Spiri­tuelle, in jener geheimnisvollen Strömung verbleibt, die uns als Rosenkreuzerei bekannt ist.",
        "Da fliessen dann die beiden Ströme dahin."
      ],
      [
        "Ja, es ist merkwürdig, wie sich sogar innerhalb von Persönlich­keiten dieses Auseinanderschälen zeigt.",
        "Ich habe schon einmal, ziemlich"
      ],
      [
        "am Anfange unserer deutschen Bewegung, darauf aufmerksam gemacht, wie in einer Persönlichkeit des ,5.",
        "Jahrhunderts das auf­tritt, was sich hier als spirituelle Bewegung fortzieht, noch mit einem gewissen Naturwissen verbunden, wie dann das Spirituelle abgewor­fen wird und rein äusserlich weiterlebt."
      ],
      [
        "An einer einzelnen Individualität können wir das verfolgen; an der des Nikolaus Cusanus (1401-1464).",
        "Wenn wir ihn nur lesen - man kann noch mehr tun als lesen bei ihm -schon durch das Lesen stellt sich heraus, wie bei ihm noch verbunden war tiefstes spirituelles Anschauen mit dem äusseren Naturwissen, namentlich wo dieses sich in mathematische Formen kleidet."
      ],
      [
        "Und weil er eine Einsicht davon hatte, wie schwer das zu erreichen ist in einer Zeit, die immer mehr und mehr nach der äusseren Gelehrsam­keit sich hinbewegt, nannte er sein Werk aus einer welthistorischen Bescheidenheit heraus ,,Gelehrte Unwissenheit\", ,,docta ignorantia\".",
        "Natürlich wollte er damit nicht ausdrücken, dass er ein ganz besonders dummer Kerl sei, sondern dass das, was er zu sagen hatte, über dem liegt, was sich nunmehr entwickeln wird als blosse äussere Gelehrsam­keit."
      ],
      [
        "Wenn wir mit einem heute beliebt gewordenen Worte reden wollen, so können wir sagen: Diese ,,Gelehrte Unwissenheit\" ist eine Übergelehrsamkeit. - Dann wurde er, wie Sie wissen, wiedergeboren, und zwar sehr bald in diesem Falle, als Nikolaus Kopernikus.",
        "Dieselbe Wesenheit, die in Nikolaus Cusanus war, wirkte weiter in Nikolaus Kopernikus."
      ],
      [
        "Aber es zeigt sich, wie gerade in jenen Zeiten die Mensch­heitsorganisation so nach dem Physischen hin vorgerückt ist, dass die ganze Tiefe des Nikolaus Cusanus in Kopernikus nur so wirken konnte, dass eben das äussere physische Weltensystem zustande kam.",
        "Was in Cusanus lebte, wurde gleichsam flitriert, das Spirituelle abge­worfen und umgewandelt zu äusserem Wissen."
      ],
      [
        "Da sehen wir hand­greiflich, wie in kurzer Zeit wirken sollte jener mächtige Impuls vom Jahre 1250, wo er seinen Zeitmittelpunkt hatte.",
        "Und das, was da hereinströmte auf unsere Erde in diesem Punkt, das wirkte in seiner Art durchaus weiter fort."
      ],
      [
        "Es wirkte in diesen beiden Strömungen fort, von denen die eine materialistisch ist und. noch materialistischer werden wird, die andere nach dem Spirituellen trachtet und sich ins­besondere in dem kundgab, was wir als Rosenkreuzeroffenbarung"
      ],
      [
        "kennen, die am intensivsten eben von diesem Ausgangspunkte aus floss, wenn sie sich auch vorher schon vorbereitet hatte."
      ],
      [
        "So sehen Sie, dass wir sozusagen eine Art 6 bis 7 bis 8 Jahrtausende dauernden Zeitraum haben, in dem die Erdentwicklung einen wichti­gen Zyklus durchläuft in bezug auf die historischen Tatsachen, in welche die Menschenentwicklung hineinverwoben ist.",
        "Solche Zyklen werden wiederum von anderen durchschnitten, denn es wirken eben die verschiedensten periodischen Kräfte auf unsere Erdentwicklung ein.",
        "Nur dann, wenn wir auseinanderlegen - wenn wir die einzelnen Kräfte kennenlernen und sozusagen nachsehen, wie sie sich zusammen gestalten, nur dann können wir allmählich dahinterkommen, wie die Dinge auf der Erde geschehen.",
        "Durch alle solche Kräfte und Gesetz­mässigkeiten wird eigentlich die Menschheit vorwärtsgebracht' wird der menschliche Fortschritt bewirkt.",
        "Wissen Sie doch, dass von einer anderen Strömung her ein wichtiger Knotenpunkt in unser Jahrhun­dert gelegt ist, der in dem Rosenkreuzermysterium angedeutet ist: Das Wiederhineinsehen in die ätherische Welt und die Offenbarung des Christus innerhalb der ätherischen Welt.",
        "Das gehört aber einer anderen Strömung an.",
        "Ich spreche jetzt mehr von Kräften, die in die breite Basis des historischen Geschehens hineinwirken."
      ],
      [
        "Wenn wir aber vollständig das historische Geschehen verstehen wollen, dann müssen wir noch berücksichtigen, dass solche Knoten-punkte der Entwicklung stets mit gewissen Stellungen der Sterne zu­sammenhängen, und dass unsere Erdachse im Jahre 1250 auch in einer gewissen Stellung war, so dass die sogenannte kleine Achse der Eklip­tik eine ganz besondere Lage hatte zu der Erdachse.",
        "Wenn wir also be­rücksichtigen, dass das, was auf der Erde geschieht, durch grosse Himmelsverhältnisse bewirkt wird, dann können wir schon an den äusseren klimatischen Verhältnissen sehen, dass innerhalb der Erde wieder spezialisiert und differenziert wird.",
        "Nicht wahr, dadurch, dass aus dem Kosmos heraus die Kräfte in gewisser Weise wirken, ist es um den Gürtel der Erde so, dass wir dort die heisse Zone haben, dann kommt die gemässigte, dann die kalte.",
        "Das kann als eine Art von Bei­spiel genommen werden dafür, wie auf dem physischen Plane sich geltend macht, was aus der Sonne und anderen Verhältnissen heraus"
      ],
      [
        "durch das geistige Geschehen bewirkt wird.",
        "Aber nun wird wiederum innerhalb der Erde selber differenziert; das Klima ist ein anderes, wenn man in der heissen Zone es zu tun hat mit Tiefen oder Höhen; auf den Höhen kann es trotzdem sehr kalt sein.",
        "Daher ist unter denselben Graden ganz anders klimatisch das Verhältnis verteilt, wenn wir in Afrika oder Amerika die Dinge betrachten.",
        "Aber es gibt auch etwas in der geistigen Entwicklung, was sich mit dieser Art von Differenzie­rung vergleichen lässt, so dass in der Tat in Zeiträumen, in denen viel­leicht weithin auf der Erde ein ganz bestimmter Charakter durch die Sternkonstellation herrscht, Modifikationen in den Geistern und See­len der Menschen, Spezialverhältnisse eintreten.",
        "Das ist besonders wichtig, denn es muss in der Tat zuweilen geschehen, dass für weit hinaus gesorgt wird."
      ],
      [
        "Denken Sie sich doch einmal, dass die weise Weltenlenkung - es ist das natürlich nur vergleichsweise gesprochen - sich sozusagen vor Jahrtausenden vornehmen musste: Da ist eine Gruppe von Seelen, die muss ich vorbereiten, dass sie in der nächsten Inkarnation diese oder jene Aufgabe vollziehen können.",
        "Da müssen Zusammenhänge ge­schaffen werden, so dass vielleicht eine kleine Gruppe von Menschen, die gerade etwas ganz Bestimmtes erfahren haben, die zusammen auf einem kleinen Fleck der Erde inkarniert sind, etwas durchmachen können, was für diesen Zeitpunkt unbedeutend erscheint; wenn man aber den Blick darauf hinwendet, wie solche Menschen, die auf einen kleinen Raum zusammengedrängt sind, in ihrer nächsten Verkörpe­rung auseinandergeworfen werden und gerade das, was sie auf dem engen Raum erhalten haben, später für die gesamte Menschheit wirken, dann gewinnt die Sache ein anderes Ansehen.",
        "Und so können wir be­greifen, dass in Zeiten, wo der Gesamtcharakter der Menschheit ein ganz bestimmter ist, in abgesonderten Teilen der Kultur etwas auf­tritt, was ganz auffallend sich ausnimmt, was sich von diesem Gesamt-charakter durchaus unterscheidet.",
        "Sehen Sie, so etwas möchte ich Ihnen erwähnen, weil es unserer Zeit ziemlich nahe liegt."
      ],
      [
        "Im Steinthal bei Strassburg hat Oberlin gelebt.",
        "Es hat insbesondere der tiefsinnige deutsche Psychologe und Forscher Schubert immer auf diesen Oberlin hingewiesen.",
        "Es war eine eigenartige Persönlichkeit,"
      ],
      [
        "dieser Oberlin, und er hat in eigenartiger Weise auf die Seelen ge­wirkt.",
        "Er war eine hellsichtige Persönlichkeit - ich kann dies nur an­deuten - und war wirklich in der Lage, nachdem er verhältnismässig früh die Gattin verloren hatte, mit der Individualität der Gattin so zusammenzuleben, wie man mit einem Lebenden zusammenlebt."
      ],
      [
        "Und nun notierte er sich Tag für Tag, was da oben, wo seine Gattin lebte, geschah; und er legte das auch in einer Landkarte des Himmels dar und zeigte es den Leuten, die um ihn herum waren, so dass in der Tat eine ganze Gemeinde da war, die teilnahm an dem Leben, das Oberlin mit seiner verstorbenen Gattin führte.",
        "Es ist eine eigenartige, de­placierte Sache, dass in die Wende des 18. und 19."
      ],
      [
        "Jahrhunderts so etwas hineingestellt ist.",
        "Aber wenn Sie in Betracht ziehen, was ich ge­sagt habe, so werden Sie den Sinn einer solchen Sache erblicken.",
        "Und solche Dinge, wie sie sich dem Oberlin geoffenbart haben, gehören zum Bedeutsamsten, was auf diesem Gebiete in der neueren Zeit her­ausgekommen ist."
      ],
      [
        "Ich darf vielleicht Sie darauf aufmerksam machen, dass wir jetzt ein sehr schönes kulturhistorisches Werk haben, das diese Verhältnisse von Oberlin behandelt, den Roman von Fritz Lien­hard.",
        "Sie werden darin ausserordentlich anregende Lektüre, nicht nur in bezug auf die Person dieses Pfarrers, sondern auch auf die anderen damaligen Kulturverhältnisse finden."
      ],
      [
        "Aus solchen Dingen heraus, die man leicht unterschätzt und als ,,zufällig\" betrachtet, können wir sehen, wie ein solches Geschehen sich hineinstellt in unsere Entwick­lung, wie es wirken kann im gesamten Zusammenhang der Mensch­heits entwicklung.",
        "Denn die Menschen, die in solcherWeise zusammen­gewürfelt sind, die sich um eine Persönlichkeit scharen, die als ihr Führer wirkt, solche Menschen sind dazu bestimmt, in späteren In­karnationen gewisse Aufgaben zu übernehmen."
      ],
      [
        "So sehen Sie - das wollte ich heute Ihnen vor Ihre Seele bringen -wie sozusagen das grösste, das makrokosmische Hereinwirken aus Weltenfernen in die Menschenseelen zusammenhängt mit dem, was sich im kleinsten Raum abspielen kann.",
        "Insbesondere interessant werden diese Dinge aber, wenn man ein anderes Gesetz mit solchen Dingen verbindet, mit solchen grossen Knotenpunkten der Entwicklung, wie ein solcher 1250 war.",
        "Damals ist am stärksten in die Menschenseele"
      ],
      [
        "hereingewirkt worden - und das kann man weniger bemerken als das Rumoren in Kontinenten.",
        "Während der atlantischen Katastrophe ist von den Geistern der Form am wenigsten in Menschenseelen ge­wirkt worden; daher haben die jüngeren Hierarchien sozusagen das Feld damals beherrscht.",
        "Und so verteilen sich überhaupt die Tätig­keiten der verschiedenen Klassen von hierarchischen Wesenheiten.",
        "Wichtig ist es nun, dass wir erkennen, dass in diesen zyklischen Be­wegungen wiederum gewisse Gesetze des Aufstiegs und des Verfalls stecken.",
        "Etwas davon habe ich schon angedeutet, als ich sagte, dass ein Ansturm im Jahre 1250 war, dass dann ein Verfall eintrat, der sich in der rein materialistischen Strömung kundgab.",
        "Solches können wir öfter bemerken.",
        "Und es ist interessant zu sehen, wie aufsteigende und absteigende Zyklen abwechseln in dem, was sich als Menschheits­geschichte vollzieht."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "VI",
    "paragraphs": [
      "Ich habe Sie gestern darauf aufmerksam gemacht, wie im Verlauf der menschlichen Entwicklung die verschiedensten historischen Mächte eingreifen. Dadurch, und auch durch das Durchkreuzen einer mäch­tigen Strömung durch die andere, entstehen gewisse Zeiten des Auf­ganges in bestimmten Kulturrichtungen und ebenso Zeiten des Ab­flutens; und es spielt sich das so ab, dass, während noch alte Kulturen abfluten' während sozusagen alte Kulturen in die Äusserlichkeit über­gehen, langsam und allmählich sich dasjenige vorbereitet, was die späteren Kulturen inaugurieren, was die späteren Kulturen eigentlich beleben, gebären soll.",
      "So dass wir in der Regel den Verlauf des mensch­lichen Kulturlebens schematisch so darstellen könnten: Wir finden aus unbestimmten Tiefen heraufgehend ein Aufsteigen der menschlichen Kultur bis zu gewissen Höhepunkten, finden dann, wie dieses Kultur­leben abflutet, und zwar langsamer als es anstieg. Dasjenige, was eine bestimmte Kulturepoche gebracht hat, lebt lange nach, lebt sich ein in die verschiedensten nachherigen Strömungen und Völkerkulturen, und verliert sich, wie ein Strom sich verlieren würde, der sich nicht ins Meer ergiesst, sondern in der Ebene ausrieselt.",
      "Während aber noch das hier verrieselt, bereiten sich die neuen Kulturen vor, die sozusagen während des Niederganges der alten Kulturen noch nicht zu bemerken waren, um dann ihrerseits ihre Entwicklung, ihren Aufstieg zu be­ginnen und in derselben oder in ähnlicher Weise zum Fortschritte der Menschheit beizutragen. Wenn wir uns einen im eminentesten Sinne charakteristischen Kulturfortschritt denken wollen, so können wir ja ahnen, dass es ein solcher sein muss, in dem das Allgemein-Menschliche, das Weben des Ich im Ich am auffallendsten herausge­kommen ist.",
      "Das war der Fall beim alten Griechentum, wie wir gezeigt",
      "haben. Nun, wenn wir dies betrachten, dann kann sich uns ge-rade hier so recht zeigen, wie in charakteristischem Sinne eine Kultur verläuft; denn was in den drei vorhergehenden Kulturen sich voll­zog, und dasjenige, was nachfolgt, ist in ganz anderer Weise von dem, was ausserhalb des Menschen liegt, modifiziert. Daher ist das, was im Menschen selber liegt, wodurch sozusagen der Mensch auf der Welt wirkt, in allem, was von übersinnlichen Mächten sich in ihm am menschenähnlichsten ausdrücken kann, uns im mittleren, im vierten Kulturzeitraume gegeben.",
      "Nun müssen wir aber auch in bezug auf das Griechentum folgendes sagen. Ihm ging der dritte Zeitraum voran; er flutete ab, und während er abflutete, bereitete sich das Griechentum vor. Es steckt also wäh­rend des Abflutens der babylonischen Kultur, die sich vom Osten nach dem Westen ergoss, auf dieser kleinen südlichen europäischen Halb­insel, die wir die griechische nennen, sozusagen der Keim zu dem, was als der Strom eines neuen Lebens sich in die Menschheit hineinsenken sollte. Nun müssen wir ja zwar sagen, dass dieses griechische Leben das reine Menschentum, das, was der Mensch ganz in sich selber finden kann, im eminentesten Sinne zum Ausdruck brachte; aber man darf nicht glauben, dass solche Dinge nicht vorbereitet werden müssen. Auch das, was wir als reines Menschentum bezeichnen, auch das musste sozusagen erst von übersinnlichen Mächten durch die Myste­rien den Menschen gelehrt werden, geradeso, wie jetzt auch jene noch höhere Freiheit, die vorzubereiten ist für die sechste Kulturepoche, in übersinnlichen Welten von den entsprechenden Führern der mensch­lichen Entwicklung getragen und gelehrt wird.",
      "Wir müssen also sagen: Da, wo das Griechentum der äusseren Betrachtung so erscheint, als ob bei ihm alles nur aus dem rein Menschlichen hervorspringt, da hat das Griechentum schon eine Zeit hinter sich, in der es sozusagen unter dem Einfluss der Lehre höherer spiritueller Wesenheiten war. Diese höheren spirituellen Wesenheiten haben ihm erst möglich gemacht, sich zu seiner rein menschlichen Höhe zu erheben. Und deshalb verliert sich auch das, was wir heute die griechische Kultur nennen, wenn wir sie zurückverfolgen, in Abgründe von vorhistorischen Zeiten, in denen als die Grundlage der",
      "griechischen Kultur in den Tempelstätten der Mysterien das betrieben wurde, was dann in grandioser Weise wie ein Erbgut der alten Tempel-weisheit in dichterische Form gebracht worden ist von Homer, von Aeschylos. Und wir müssen also dasjenige, was so grandios uns ent­gegentritt in diesen unerreichten Gestalten, so betrachten, dass diese Menschen zwar etwas in ihrer Seele verarbeiteten, was ganz Seelen-inhalt, ganz Weben des Ich im Ich bei ihnen war, was aber zuerst in den heiligen Tempelstätten von höheren Wesenheiten in diese Seelen hineingetragen worden war. Daher erscheint es so unergründlich tief, so unergründlich gross, was in den Dichtungen Homers' in den Dich­tungen des Aeschylos lebt. Man darf diese Dichtungen des Aeschylos dann nur nicht nach der Übersetzung von Wilamowitz nehmen, son­dern sich klar sein darüber, dass die volle Grösse dessen, was inAeschy­los lebte, noch nicht ausgeschöpft ist in einer modernen Sprache, und dass es der schlechteste Weg ist zum Verständnis des Aeschylos, der von einem dieser neuesten Übersetzer eingeschlagen worden ist.",
      "Wenn wir diese griechische Kultur also auf dem Grunde tiefer Mysterienheiligtümer betrachten, dann können wir eine Ahnung von dem Wesen dieser griechischen Kultur bekommen. Und indem die Geheimnisse des Lebens der übersinnlichen Welt in einer gewissen menschlichen Art den griechischen Künstlern überbracht wurden, konnte auch die griechische Plastik das in Marmor oder in Erz giessen, was ursprünglich Tempelgeheimnis war. Ja, auch das, was uns in der griechischen Philosophie entgegentritt, zeigt uns so recht mit Klar­heit, wie das Beste, was diese griechische Philosophie geben konnte, eigentlich nur in Intelligenz, in Verstandeserfassen umgesetzte alte Mysterienweistümer waren. Symbolisch wird uns ja so etwas ausge­drückt dadurch, dass uns gesagt wird: Der grosse Heraklit brachte sein Werk über die Natur dar im Tempel der Diana von Ephesus. Das heisst nichts anderes als: Er stellte das, was er sagen konnte aus eigenem Weben des Ich-im-Ich, so hin, dass er es als Opfer zu bringen hatte den geistigen, den spirituellen Mächten der vorhergehenden Zeit, mit denen er sich im Zusammenhange wusste. Und von einem solchen Gesichtspunkte aus verstehen wir auch den tiefsinnigen Ausspruch des Plato, der eine so tiefe Philosophie den Griechen hat geben können",
      "und trotzdem sich gezwungen sah, zu sagen, dass alle Philosophie seiner Zeit nichts mebr sei gegenüber der alten Weisheit, die von den Vorvätern noch empfangen worden ist aus den Reichen der spirituel­len Welten selber. Und bei Aristoteles erscheint uns schon alles wie in logische Formen hinein - man kann in diesem Falle nur sagen -verabstrahiertes altes Weisheitsgut, in Begriffe gebrachte lebendige Welten.",
      "Trotzdem atmet, weil Aristoteles sozusagen eben an dem Schlusstor der alten Strömung steht, trotzdem atmet in Aristoteles noch etwas von dem, was altes Weisheitsgut war. In seinen Begriffen, in seinen Ideen ist, obwohl sie abstrakt sind, eben noch ein Nachkiang zu vernehmen der vollkommenen Töne, die aus den Tempelstätten herausgetönt haben und die das eigentlich Inspirierende waren nicht nur der griechischen Weisheit, sondern auch der griechischen Kunst, des ganzen griechischen Volkscharakters.",
      "Denn es ist das Eigenartige einer jeden solchen Kultur beim Aufgange, dass sie nicht allein das Wissen, nicht allein die Kunst ergreift, sondern den ganzen Menschen; so dass der ganze Mensch ein Abdruck dessen ist, was als Weisheit, was als Spirituelles in ihm lebt. Und wenn wir uns vorstellen, dass aus unbekannten Tiefen, noch während die babylonische Kultur ab-flutet, hinansteigt die griechische Kultur, dann können wir das völlige Auswirken alles dessen erkennen, was die alten Tempel dem griechi­schen Charakter gebracht haben im Zeitalter der Perserkriege; denn in diesen Perserkriegen sehen wir, wie die Helden des Griechentums in flammender Begeisterung für dasjenige, was sie empfangen hatten von ihren Vorvätern, sich entgegenwerfen der Strömung, die sozu­sagen als die verfallende Strömung des Morgenlandes sich ihnen ent­gegenwälzt.",
      "Und was jenes damalige Entgegenwerfen bedeutet, wo die griechische Tempelweisheit, wo die Lehrer der alten griechischen Mysterien in den Seelen der Helden der Perserkriege kämpften gegen die abflutende Kultur des Morgenlandes, gegen die babylonische Kultur, wie sie die späteren Perser übernommen hatten, - was das bedeutet, das kann die Menschenseele erfassen, wenn einmal die Frage aufgeworfen wird von dieser Menschenseele: Was hätte werden müs­sen aus dem südlichen Europa und damit aus dem ganzen späteren Europa, wenn dazumal der Anprall der grossen physischen Massen",
      "aus dem Orient nicht von dem kleinen Griechenvolke zurückgeschla­gen worden wäre? Mit demjenigen, was daa:umal die Griechen getan haben, war der Keim gelegt zu allem Späteren, was sich bis in unsere Zeiten herein innerhalb der europäischen Kulturen entwickelt hat.",
      "Und selbst das, was sich für das Morgenland aus dem entwickelt hat, was Alexander dann wiederum zurücktrug - wenn auch in einer Art, die sich in gewisser Beziehung nicht rechtfertigen lässt - aus dem Okzident in den Orient, auch das hat sich nur entwickeln können, nachdem zuerst das dem Verfall Geweihte auch in bezug auf seine physische Kraft zurückgeschlagen war von dem, was als flammender Enthusiasmus für die Tempelschätze in den Seelen der Griechen lebte. Wenn wir das erfassen, dann werden wir nicht nur nachwirken sehen die Weisheit vom Feuer des Heraklit, die grossen Ideen des Anaxagoras, wir werden nicht nur nachwirken sehen die umfassenden Ideen des Thales, sondern auch die realen Lehren der Hüter der Tempelweisheit im vorhistorischen Griechentum.",
      "Das wer­den wir empfinden als ein Ergebnis spiritueller Mächte, die dem Griechentum das gebracht haben, was ihm gebracht werden musste. Wir werden das alles fühlen in den Seelen der griechischen Helden, die gegen die Perser in den verschiedenen Schlachten standen.",
      "So muss man lernen Geschichte fühlen, meine lieben Freunde, denn das, was uns sonst als Geschichte gegeben wird, ist ja nur ein leeres Abstraktum von Ideen - wenn es hoch kommt. Was im Späteren von dem Früheren wirkt, das kann man nur beobachten, wenn man auf das zurückgeht, was den Menschenseelen vielleicht durch Jahr­tausende gegeben ist, und was dann reale Formen annimmt in einer gewissen Zeit.",
      "Woran lag es, dass bei diesem Aufstieg die alten Tempelschätze so Grosses den Griechen geben konnten? Das lag in dem Universellen, Umfassenden und in dem um alles andere unbe­kümmerten Charakter dieser Tempelschätze.",
      "Es war etwas, was als ein Ursprüngliches gegeben war, was ausfüllen konnte den ganzen Menschen, was sozusagen eine unmittelbar richtunggebende Kraft hatte.",
      "Und da kommen wir an das eigentliche Charakteristikon derjenigen Kulturen, die zunächst im Aufstiege begriffen sind bis zu ihrem Höhepunkt.",
      "In diesen Kulturen wird alles, was im Menschen lebendig tätig ist - da wird Schönheit, da wird Tugend, da wird das Nützliche, das Zweckmässige, alles das, was der Mensch im Leben tun und realisieren will -, alles das wird gesehen als ein aus dem Weisheits­vollen, aus dem Spirituellen unmittelbar Hervorgehendes. Und die Wdsheit ist dasjenige, was die Tugend, die Schönheit, was alles Übrige enthält.",
      "Wenn der Mensch von den Tempeiweistümern durchsetzt, inspiriert ist, dann ergibt sich alles andere von selbst; so ist das Gefühl für solche aufsteigende Zeiten. In dem Augenblick aber, wo die Fragen, wo die Empfindungen auseinanderfallen, wo zum Beispiel die Frage nach dem Guten oder nach dem Schönen selb­ständig wird gegenüber der Frage nach dem göttlichen Urgrunde, da beginnen die Zeiten des Verfalls.",
      "Daher können wir sicher sein, dass wir immer in einer Verfallszeit leben, wenn betont wird, dass neben dem ursprünglich Spirituellen noch besonders gepflegt werden soll dieses oder jenes, dass dieses oder jenes die Hauptsache sein soll. Wenn man nicht das Vertrauen hat zu dem Spirituellen, dass es alles das, was für das Menschenleben notwendig ist, aus sich heraus gebären kann, dann zerfallen die einheitlichen Kulturströme, die beim Aufsteigen eine Einheit bilden, in Einzelströmungen.",
      "Und das sehen wir da, wo sich ausserhalb der Weisheit, ausserhalb des spiri­tuellen Schwunges befindliche Interessen hineinmischen in das grie­chische Leben; das sehen wir im staatlichen Leben, wir sehen es auch in demjenigen Teile des griechischen Lebens, der uns besonders interessiert, im Geistigen unmittelbar hinter Aristoteles. Da beginnt neben der Frage: Was ist das Wahre?, in der enthalten ist die Frage:",
      "Was ist das Gute und Zweckmässige?  da beginnt die letztere Frage eine selbständige zu werden. Man fragt: Wie soll unser Wissen be­schaffen sein, damit man ein Mensch werden kann, der ein praktisches Lebensziel erreicht? Und so sehen wir eine Strömung in der Verfalls­zeit aufblühen' die wir den Stoizismus nennen. Bei Plato und Ari­stoteles war in dem Weisen zugleich das Gute enthalten; aller Schwung für das Gute konnte nur aus dem Weisen herauskommen. Die Stoiker fragen: Was muss der Mensch tun, um ein für das Leben, für die Lebenspraxis weiser, um ein zweckmässig gut lebender Mensch zu",
      "werden? Praktische Lebensziele mischen sich hinein in dasjenige, was universeller Schwung der Wahrheit ehedem war.",
      "Beim Epikureismus mischt sich dann etwas hinein, was wir so bezeichnen können: Die Menschen fragen, wie muss ich mich ein­richten intellektuell, damit dieses Leben möglichst beseligend, mög­lichst innerlich harmonisch verlaufen kann? Auf diese Frage würden Thales, Plato, bis zu Aristoteles geantwortet haben: Suche nach der Wahrheit, und diese wird dir geben, was die grösste Seligkeit ist, was der Keim der Liebe ist.",
      "Jetzt aber trennt man die eine Frage von der Wahrheitsfrage ab, und es entsteht eine Strömung des Nieder­ganges. So ist das, was man Stoizismus und Epikureismus nennt, Strömung des Niederganges. So etwas hat dann immer im Gefolge, dass die Wahrheit fragwürdig wird für die Menschen, dass sie alle Kraft verliert.",
      "Daher tritt gleichzeitig mit dem Stoizismus und Epi­kureismus in der Verfallszeit der Skeptizismus, die Zweifelsucht gegen­über der Wahrheit auf. Und wenn Skeptizismus, Zweifelsucht, wenn Stoizismus' wenn Epikureismus ihr Wesen eine Zeitlang getrieben haben, dann fühlt sich der Mensch, der doch nach dem Wahren strebt, sozusagen wie aus der Weltenseele herausgeworfen und auf die eigene Seele zurückgewiesen.",
      "Dann schaut er sich um und sagt sich: Jetzt ist keine Weltepoche da, wo durch den fortwirkenden Strom der geistigen Mächte selber die Impulse in die Menschheit einströmen. Dann ist der Mensch auf sein eigenes inneres Leben, auf sein Subjekt zurückgewiesen.",
      "Das tritt uns im weiteren Verlaufe des griechischen Lebens im Neuplatonismus entgegen, in jener Philosophie, die keinen Zusammenhang mehr hat mit dem äusseren Leben, die in sich hineinblickt und im mystischen Aufstiege des Einzelnen zum Wahren hinaufstreben will. So haben wir eine ansteigende Kultur, so haben wir eine stufenweis absteigende.",
      "Und das, was sich herausgebildet hat im Aufstiege, das verrinnt und verrieselt dann langsam und allmählich, bis gegen das Heranrücken des Jahres 1250 eine allerdings nicht leicht bemerkbare, aber deshalb nicht minder grosse Inspiration für die Menschheit beginnt, die ich ja gestern in gewisser Weise charakterisiert habe und deren Abrieseln wir jetzt wieder seit dem 16. Jahrhundert haben.",
      "Denn seit jener Zeit treten",
      "im Grunde genommen wiederum alle die Spezialfragen auf neben den Wahrheitsfragen; da wird wiederum ein Standpunkt genommen, der die Frage nach dem Guten, die Frage nach dem äusserlich Zweck­mässigen abtrennen will von der einen grossen Wahrheitsfrage. Und während diejenigen geistigen führenden Persönlichkeiten, die unter den Impulsen des Jahres 1250 standen, alle menschlichen Strömungen innerhalb der Wahrheit geschaut haben, sehen wir, wie jetzt im ganz eminenten Sinne auftritt das prinzipielle Trennen der praktischen Fragen des Lebens von den eigentlichen Wahrheitsfragen.",
      "Und an der Eingangspforte der neuen Verfallszeit, derjenigen Zeit, welche so recht bedeutet für das spirituelle Leben des Hinuntersausen - an der Eingangspforte steht Kant. In seiner Vorrede zu der zweiten Auflage der ,,Kritik der reinen Vernunft\" sagt er ausdrücklich: Ich musste das Streben nach der Wahrheit auf seine Grenzen zurückweisen, damit ich frei bekam das Feld für das, was die praktische Religion will.",
      "Und deshalb jene strenge Trennung der praktischen Vernunft von der theoretischen Vernunft. In der praktischen Vernunft die Postulate von Gott, Freiheit und Unsterblichkeit, rein hingeordnet auf das Gute; in der theoretischen Vernunft die Zertrümmerung jeder Erkenntnis-möglichkeit, um in irgendeine spirituelle Welt hineinzukommen.",
      "So stellen sich die Dinge welthistorisch. Und gewiss, auf den Spuren Kants wird noch lange das, was Weisheitsstreben unserer Zeit ist, verlaufen. Und wenn hingewiesen wird von unserer wirklich spiri­tuellen Strömung auf jene Erweiterung des Erkenntnisvermögens, auf jene Erhöhung des Erkenntnisvermögens über sich selbst hinaus, durch die es eindringen kann in übersinnliche Welten, dann wird man noch lange, lange hören können, dass es von allen Seiten tönt: ,,Ja, aber Kant sagt ...!,, In solchen Antithesen spielt sich in der Tat der historische Werdegang des Menschen ab.",
      "Und in dem, was instinktiv hervortritt wie eine Ahnung, da zeigt sich dann, dass unter dem, was eine blosse Maja ist und was hingenommen wird wie die Wahrheit, dass da unter dem Strome der Maja für die Menscheninstinkte doch das Richtige zu einem grossen Teil fliesst. Denn es ist ausserordentlich interessant, dass wir den absteigenden Gang der menschlichen Ent­wicklung bis zu der griechisch-lateinischen Zeit und das von uns",
      "geforderte Wiederum-Hinaufsteigen in gewissen Ahnungen sehen, welche aus den Volksinstinkten heraus für das praktische Leben ge­geben worden sind.",
      "Wie mussten denn die Menschen, die ein Gefühl hatten für so etwas, denken? Wenn sie zurückschauten auf die grossen führenden Gestalten der Menschheitsgeschichte in der vorchristlichen Zeit oder - sagen wir besser - in der vorgriechischen Zeit, wie mussten sie zurück­schauen auf alle diejenigen, die wir charakterisieren konnten als die Instrumente für die Wesenheiten höherer Hierarchien?",
      "Sie mussten sich sagen, selbst noch die Griechen: Das ist uns gekommen durch Menschen, in die eingeflossen sind übermenschliche göttliche Kräfte. -Und das sehen wir im Bewusstsein aller alten Zeiten leben: Die führen­den Persönlichkeiten, bis zu den Heroengestalten herunter, ja bis zu Plato, wurden als Söhne der Götter angesehen; das heisst hinter diesen Persönlichkeiten, die in der Geschichte auftreten, sahen die Menschen, wenn sie hinaufschauten in die Vorzeit, wenn sie den Blick immer wei­ter und weiter erhoben, sie sahen das Göttliche; und was da auftritt als Plato und in den Heroengestalten' das sahen sie an als herunter-gestiegen, ja selbst als geboren aus göttlichen Wesenheiten. Das war so recht die Anschauung, wie sich die Söhne der Götter mit den Töchtern der Menschen verbinden, um herunterzubringen das Spiri­tuelle auf den physischen Plan.",
      "Göttersöhne, Göttermenschen, das heisst solche, die eine Verbindung ihres Wesens mit dem Göttlichen hatten, sah man in diesen alten Zeiten. Dagegen in dem Moment, wo die Griechen fühlten: Jetzt können wir von dem Weben des Ich-im-Ich reden, von dem, was innerhalb der menschlichen Persönlichkeit liegt, - da reden sie von ihren höchsten Führern als von den sieben Weisen, und bezeichnen damit dasjenige, was sozusagen aus den Göttersöhnen zum rein Menschlichen geworden ist.",
      "Wie musste es nun weiter werden in den Instinkten der Völker in den nachgriechischen Zeiten? Da müsste dargestellt werden, was der Mensch ausbildet auf dem physischen Plan, und wie er das mit seiner vollen Frucht hinaufträgt in die spirituelleWelt.Wenn also ganz früher empfunden wurde: Man muss das Spirituelle vor dem physischen Menschen sehen und den physischen Menschen als Schattenbild, -",
      "wenn man wahrend der griechischen Zeit Weise gesehen hat, die so­zusagen als Ich-im-Ich lebten, so musste man In der nachgriechischen Zeit Persönlichkeiten sehen, die auf dem physischen Plan leben und dann sich hinaufleben in das Spirituelle durch das, was im Physischen lebt. Dieser Begriff ist aus dem Instinkte eines Wissens herausgebildet. So wie die vorgriechische Zeit Göttersöhne und die Griechen Weise hatten, so haben die nachgriechischen Völker Heilige, die sich hin-aufleben in das spirituelle Leben durch das, was sie im physischen Plane erwirken. Da lebt etwas im Volksinstinkte, und da können wir hineinschauen, wie allerdings hinter der Maja etwas ist, was historisch doch die Menschheit vorwärtstreibt.",
      "Und wenn wir das erkennen, dann leuchtet das, was in diesen Zeiten lebt, herein in die einzelne Menschenseele, und wir begreifen, wie sich modifizieren muss das Gruppenkarma dadurch, dass die Menschen zugleich Werkzeuge des historischen Werdeganges sind. Und wir können so begreifen, was die Akashachronik zeigt: Wie wir in Novalis zum Beispiel etwas zu sehen haben, was zurückgeht bis zum alten Elias.",
      "Es ist das eine ausserordentlich interessante Inkar-nationenfolge. Da sehen wir, wie in Elias auftaucht das prophetische Element, denn die Hebräer hatten die Mission, vorzubereiten das­jenige, was später kommen sollte.",
      "Und sie bereiteten es vor in dem Übergang von ihren Patriarchen zu den Propheten, durch die Gestalt des Moses hindurchgehend. Während wir in Abraham noch sehen, wie der Hebräer das Nachwirken des Gottes in sich, in seinem Blute fühlt, sehen wir bei Elias den Übergang zur Entrückung in die spirituellen Welten.",
      "Alles bereitet sich nach und nach vor. In Elias lebt eine Individualität, die sich in den alten Zeiten schon erfüllt mit dem, was da in der Zukunft kommen soll. Und dann sehen wir, wie diese Individualität ein Werkzeug sein soll, um vorzubereiten das Verständnis für den Christusimpuls.",
      "Wir sehen, wie die Individualität des Elias in Johannes dem Täufer wiedergeboren wird; dieser ist das Werkzeug für ein Höheres. Es lebt in ihm eine Individualität, die Johannes den Täufer zum Werkzeuge macht; aber notwendig war die hohe Individualität des Elias, um dann als solches Instrument zu dienen.",
      "Wir sehen dann später, wie diese Individualität geeignet ist, das, was in die Zukunft hineinwirken soll, in Formen zu giessen, welche nur möglich waren unter dem Einnusse des vierten nachatlantischen Kulturzeitraumes. So taucht denn diese Individualität, so merkwürdig uns das erscheint, in Raphael wieder auf und verbindet das, was als christlicher Impuls für alle Zeiten wirken soll, mit den wunderbaren Formen des Griechentums in der Malerei. Und da können wir er­kennen, wie sich das individuelle Karma dieser Entelechle verhält zu der äusseren Inkarnation. Für die äussere Inkarnation wird verlangt, dass eine Zeitenmacht in Raphael sich aussprechen kann; für diese Zeitenmacht ist die Elias-Johannes-Individualität die geeignete. Aber die Zeit kann nur einen physischen Leib hergeben, der unter solcher Macht zerbrechlich sein muss; daher stirbt er so früh.",
      "Die andere Seite ihres Wesens muss diese Individualität ausprägen in einer Zeit, wo schon wieder die einzelnen Strömungen auseinander-fallen; da taucht sie wieder auf als Novalis. Da sehen wir, wie in diesem Novalis wirklich schon alles das in einer eigenartigen Gestalt lebt, was uns jetzt durch die Geisteswissenschaft gegeben wird. Denn so treffende Aussprüche über das Verhältnis des astralischen zum ätherischen und physischen Leib, von Wachsein und Schlafen, sind ausserhalb der Geisteswissenschaft von keinem gegeben worden als von Novalis, dem wiederauferstandenen Raphael. Das sind die Dinge, die uns zeigen, wie die Individualitäten die Werkzeuge sind des fort-fliessenden Stromes der Menschheitsentwicklung. Und wenn wir das menschliche Werden sehen, wenn wir hinschauen auf diesen rätsel-vollen Wechsel in dem, was historisch geschieht, dann können wir dasjenige ahnen, was von tiefen spirituellen Mächten in ihm lebt. In einer merkwürdigen Weise geht das Frühere in das Spätere über.",
      "Für einige von Ihnen habe ich es ja schon gesagt, dass man einen merkwürdigen historischen Ausblick konstatieren kann beim Über­gang von Michelangelo zu Galilei. Und ein sonst sehr gescheiter Mann - wohlgemerkt, ich sage nicht, dass es sich hier um eine Rein­karnation handelt, sondern um einen historischen Fortgang - eine sehr gescheite Persönlichkeit machte darauf aufmerksam, wie es doch sonderbar ist, wenn wir beim Anblick der wunderbaren Architektonik",
      "der Petersklrche sehen, wie der menschliche Geist in sie hineinver­woben hat das, was er mechanische Wissenschaft nennt. 0, in diesen grandiosen Formen der Petersklrche sehen wir verkörpert die me­chanischen Gedanken, die der menschliche Intellekt fassen konnte, noch dazu umgesetzt ins Schöne, ins Grandiose: Michelangelos Ge­danke! Wie der Anblick der Peterskirche wirken kann, meine lieben Freunde, das tritt in den mannigfaltigsten Beziehungen auf, und viel-leicht hat ein jeder so ein bisschen von dem erlebt, was der Wiener Bildhauer Natter erlebte - oder was mit ihm erlebt worden ist.",
      "Er fuhr mit einem Freunde gegen die Petersklrche hin; sie hatten sie noch nicht erblickt, plötzlich hört der andere, dass Natter, indem er von seinem Sitze aufspringt, ganz ausser sich kommt und sagt: Mir wird angst! Denn in diesem Augenblick hat er die Petersklrche er­blickt ... er wollte sich später daran gar nicht erinnern.",
      "Etwas Ähnli­ches kann ja schliesslich jeder Mensch erleben, wenn er so etwas Grandioses sieht. Und nun machte ein sehr gescheiter Mann, der Professor Müllner' in einer Rektoratsrede darauf aufmerksam, dass der grosse Denker mechanischer Gedanken, Galilei, intellektuell für die Menschheit das gelehrt hat, was hineingebaut hat in die räumlichen Formen Michelangelo in die Peterskirche.",
      "So dass uns in Galileis Ge­danken intellektuell das wieder entgegentritt, was wie kristallisiert als Mechanik, als menschliche Mechanik in der Petersklrche dasteht. Aber sonderbar ist es dabei, dass derselbe Mann in diesem Vortrag darauf aufmerksam machen musste, der Todestag des Michelangelo sei der Geburtstag des Galilei.",
      "Das heisst, dass das Intellektuelle, die Gedanken, die mechanisch durch Galilei in Intellektualität geprägt worden sind, aufgetaucht sind in einer Persönlichkeit, die geboren ist an dem Todestage dessen, der sie in den Raum hineingestellt hat. Und so sollte man fragen: Wer hat durch Michelangelo die Mechanik, welche die Menschheit erst durch Galilei nachher bekommen hat, in die Peterskirche hineingebaut?",
      "Wenn durch die ja ganz aphoristischen und vereinzelten Gedanken, die in Anlehnung an den historischen Werdegang der Menschheit hier vorgebracht werden durften, wenn aus diesen in ihrem Zusammen­schluss in Ihren Herzen ein Gefühl davon hervorgeht, wie die wirklichen,",
      "die realen geistigen Mächte durch ihre Werkzeuge in der Ge­schichte wirken, dann werden Sie in richtiger Weise diese Ausfüh­rungen entgegengenommen haben. Und dann könnte man dieses Ge­fühl als das bezeichnen, was aus der okkult-hlstorischen Betrachtung als ein rechtes Gefühl für das Werden in der Zeit, für den Fortgang in der Zeit in unsere Herzen kommen kann. Und heute, an einem kleinen Wendepunkt der Zeit, mag es angemessen sein, einmal die Meditation hinzulenken auf solches Fühlen des Menschenfortganges und des Götterfortganges in der Zeit. Und wenn von Ihnen, meine lieben Freunde, jedes Herz das aufnehmen möchte - dieses Gefühl für die Umsetzung der Wissenschaft vom okkulten Fortschritte in der Zeit - in Empfindung für das Weben und Schaffen im Werden, im Menschenfortschritt' in den wir hineingestellt sind, - wenn jede Seele von Ihnen das aufnehmen möchte als ein lebendiges Gefühl, so dürfte vielleicht in diesem Gefühl auch ein Neujahrswunsch in der Seele von Ihnen allen leben. Und diesen Neujahrswnnsch möchte ich am Schlusse dieses Zyklus von dieser Stätte hier in Ihre Seelen hinein-gesenkt sein lassen: Betrachten Sie das, was gesprochen worden ist, als etwas, was den Ausgang bilden soll für ein Zeitgefühl. Und in ge­wisser Weise mag es symbolisch sein, dass wir einen kleinen Übergang von einem Zeitabschnitt zu einem anderen dazu benutzen konnten, um solche die Zeitenübergänge umspannenden Ideen in unserer Seele einmal wirken zu lassen."
    ],
    "sentences": [
      [
        "Ich habe Sie gestern darauf aufmerksam gemacht, wie im Verlauf der menschlichen Entwicklung die verschiedensten historischen Mächte eingreifen.",
        "Dadurch, und auch durch das Durchkreuzen einer mäch­tigen Strömung durch die andere, entstehen gewisse Zeiten des Auf­ganges in bestimmten Kulturrichtungen und ebenso Zeiten des Ab­flutens; und es spielt sich das so ab, dass, während noch alte Kulturen abfluten' während sozusagen alte Kulturen in die Äusserlichkeit über­gehen, langsam und allmählich sich dasjenige vorbereitet, was die späteren Kulturen inaugurieren, was die späteren Kulturen eigentlich beleben, gebären soll."
      ],
      [
        "So dass wir in der Regel den Verlauf des mensch­lichen Kulturlebens schematisch so darstellen könnten: Wir finden aus unbestimmten Tiefen heraufgehend ein Aufsteigen der menschlichen Kultur bis zu gewissen Höhepunkten, finden dann, wie dieses Kultur­leben abflutet, und zwar langsamer als es anstieg.",
        "Dasjenige, was eine bestimmte Kulturepoche gebracht hat, lebt lange nach, lebt sich ein in die verschiedensten nachherigen Strömungen und Völkerkulturen, und verliert sich, wie ein Strom sich verlieren würde, der sich nicht ins Meer ergiesst, sondern in der Ebene ausrieselt."
      ],
      [
        "Während aber noch das hier verrieselt, bereiten sich die neuen Kulturen vor, die sozusagen während des Niederganges der alten Kulturen noch nicht zu bemerken waren, um dann ihrerseits ihre Entwicklung, ihren Aufstieg zu be­ginnen und in derselben oder in ähnlicher Weise zum Fortschritte der Menschheit beizutragen.",
        "Wenn wir uns einen im eminentesten Sinne charakteristischen Kulturfortschritt denken wollen, so können wir ja ahnen, dass es ein solcher sein muss, in dem das Allgemein-Menschliche, das Weben des Ich im Ich am auffallendsten herausge­kommen ist."
      ],
      [
        "Das war der Fall beim alten Griechentum, wie wir gezeigt"
      ],
      [
        "haben.",
        "Nun, wenn wir dies betrachten, dann kann sich uns ge-rade hier so recht zeigen, wie in charakteristischem Sinne eine Kultur verläuft; denn was in den drei vorhergehenden Kulturen sich voll­zog, und dasjenige, was nachfolgt, ist in ganz anderer Weise von dem, was ausserhalb des Menschen liegt, modifiziert.",
        "Daher ist das, was im Menschen selber liegt, wodurch sozusagen der Mensch auf der Welt wirkt, in allem, was von übersinnlichen Mächten sich in ihm am menschenähnlichsten ausdrücken kann, uns im mittleren, im vierten Kulturzeitraume gegeben."
      ],
      [
        "Nun müssen wir aber auch in bezug auf das Griechentum folgendes sagen.",
        "Ihm ging der dritte Zeitraum voran; er flutete ab, und während er abflutete, bereitete sich das Griechentum vor.",
        "Es steckt also wäh­rend des Abflutens der babylonischen Kultur, die sich vom Osten nach dem Westen ergoss, auf dieser kleinen südlichen europäischen Halb­insel, die wir die griechische nennen, sozusagen der Keim zu dem, was als der Strom eines neuen Lebens sich in die Menschheit hineinsenken sollte.",
        "Nun müssen wir ja zwar sagen, dass dieses griechische Leben das reine Menschentum, das, was der Mensch ganz in sich selber finden kann, im eminentesten Sinne zum Ausdruck brachte; aber man darf nicht glauben, dass solche Dinge nicht vorbereitet werden müssen.",
        "Auch das, was wir als reines Menschentum bezeichnen, auch das musste sozusagen erst von übersinnlichen Mächten durch die Myste­rien den Menschen gelehrt werden, geradeso, wie jetzt auch jene noch höhere Freiheit, die vorzubereiten ist für die sechste Kulturepoche, in übersinnlichen Welten von den entsprechenden Führern der mensch­lichen Entwicklung getragen und gelehrt wird."
      ],
      [
        "Wir müssen also sagen: Da, wo das Griechentum der äusseren Betrachtung so erscheint, als ob bei ihm alles nur aus dem rein Menschlichen hervorspringt, da hat das Griechentum schon eine Zeit hinter sich, in der es sozusagen unter dem Einfluss der Lehre höherer spiritueller Wesenheiten war.",
        "Diese höheren spirituellen Wesenheiten haben ihm erst möglich gemacht, sich zu seiner rein menschlichen Höhe zu erheben.",
        "Und deshalb verliert sich auch das, was wir heute die griechische Kultur nennen, wenn wir sie zurückverfolgen, in Abgründe von vorhistorischen Zeiten, in denen als die Grundlage der"
      ],
      [
        "griechischen Kultur in den Tempelstätten der Mysterien das betrieben wurde, was dann in grandioser Weise wie ein Erbgut der alten Tempel-weisheit in dichterische Form gebracht worden ist von Homer, von Aeschylos.",
        "Und wir müssen also dasjenige, was so grandios uns ent­gegentritt in diesen unerreichten Gestalten, so betrachten, dass diese Menschen zwar etwas in ihrer Seele verarbeiteten, was ganz Seelen-inhalt, ganz Weben des Ich im Ich bei ihnen war, was aber zuerst in den heiligen Tempelstätten von höheren Wesenheiten in diese Seelen hineingetragen worden war.",
        "Daher erscheint es so unergründlich tief, so unergründlich gross, was in den Dichtungen Homers' in den Dich­tungen des Aeschylos lebt.",
        "Man darf diese Dichtungen des Aeschylos dann nur nicht nach der Übersetzung von Wilamowitz nehmen, son­dern sich klar sein darüber, dass die volle Grösse dessen, was inAeschy­los lebte, noch nicht ausgeschöpft ist in einer modernen Sprache, und dass es der schlechteste Weg ist zum Verständnis des Aeschylos, der von einem dieser neuesten Übersetzer eingeschlagen worden ist."
      ],
      [
        "Wenn wir diese griechische Kultur also auf dem Grunde tiefer Mysterienheiligtümer betrachten, dann können wir eine Ahnung von dem Wesen dieser griechischen Kultur bekommen.",
        "Und indem die Geheimnisse des Lebens der übersinnlichen Welt in einer gewissen menschlichen Art den griechischen Künstlern überbracht wurden, konnte auch die griechische Plastik das in Marmor oder in Erz giessen, was ursprünglich Tempelgeheimnis war.",
        "Ja, auch das, was uns in der griechischen Philosophie entgegentritt, zeigt uns so recht mit Klar­heit, wie das Beste, was diese griechische Philosophie geben konnte, eigentlich nur in Intelligenz, in Verstandeserfassen umgesetzte alte Mysterienweistümer waren.",
        "Symbolisch wird uns ja so etwas ausge­drückt dadurch, dass uns gesagt wird: Der grosse Heraklit brachte sein Werk über die Natur dar im Tempel der Diana von Ephesus.",
        "Das heisst nichts anderes als: Er stellte das, was er sagen konnte aus eigenem Weben des Ich-im-Ich, so hin, dass er es als Opfer zu bringen hatte den geistigen, den spirituellen Mächten der vorhergehenden Zeit, mit denen er sich im Zusammenhange wusste.",
        "Und von einem solchen Gesichtspunkte aus verstehen wir auch den tiefsinnigen Ausspruch des Plato, der eine so tiefe Philosophie den Griechen hat geben können"
      ],
      [
        "und trotzdem sich gezwungen sah, zu sagen, dass alle Philosophie seiner Zeit nichts mebr sei gegenüber der alten Weisheit, die von den Vorvätern noch empfangen worden ist aus den Reichen der spirituel­len Welten selber.",
        "Und bei Aristoteles erscheint uns schon alles wie in logische Formen hinein - man kann in diesem Falle nur sagen -verabstrahiertes altes Weisheitsgut, in Begriffe gebrachte lebendige Welten."
      ],
      [
        "Trotzdem atmet, weil Aristoteles sozusagen eben an dem Schlusstor der alten Strömung steht, trotzdem atmet in Aristoteles noch etwas von dem, was altes Weisheitsgut war.",
        "In seinen Begriffen, in seinen Ideen ist, obwohl sie abstrakt sind, eben noch ein Nachkiang zu vernehmen der vollkommenen Töne, die aus den Tempelstätten herausgetönt haben und die das eigentlich Inspirierende waren nicht nur der griechischen Weisheit, sondern auch der griechischen Kunst, des ganzen griechischen Volkscharakters."
      ],
      [
        "Denn es ist das Eigenartige einer jeden solchen Kultur beim Aufgange, dass sie nicht allein das Wissen, nicht allein die Kunst ergreift, sondern den ganzen Menschen; so dass der ganze Mensch ein Abdruck dessen ist, was als Weisheit, was als Spirituelles in ihm lebt.",
        "Und wenn wir uns vorstellen, dass aus unbekannten Tiefen, noch während die babylonische Kultur ab-flutet, hinansteigt die griechische Kultur, dann können wir das völlige Auswirken alles dessen erkennen, was die alten Tempel dem griechi­schen Charakter gebracht haben im Zeitalter der Perserkriege; denn in diesen Perserkriegen sehen wir, wie die Helden des Griechentums in flammender Begeisterung für dasjenige, was sie empfangen hatten von ihren Vorvätern, sich entgegenwerfen der Strömung, die sozu­sagen als die verfallende Strömung des Morgenlandes sich ihnen ent­gegenwälzt."
      ],
      [
        "Und was jenes damalige Entgegenwerfen bedeutet, wo die griechische Tempelweisheit, wo die Lehrer der alten griechischen Mysterien in den Seelen der Helden der Perserkriege kämpften gegen die abflutende Kultur des Morgenlandes, gegen die babylonische Kultur, wie sie die späteren Perser übernommen hatten, - was das bedeutet, das kann die Menschenseele erfassen, wenn einmal die Frage aufgeworfen wird von dieser Menschenseele: Was hätte werden müs­sen aus dem südlichen Europa und damit aus dem ganzen späteren Europa, wenn dazumal der Anprall der grossen physischen Massen"
      ],
      [
        "aus dem Orient nicht von dem kleinen Griechenvolke zurückgeschla­gen worden wäre?",
        "Mit demjenigen, was daa:umal die Griechen getan haben, war der Keim gelegt zu allem Späteren, was sich bis in unsere Zeiten herein innerhalb der europäischen Kulturen entwickelt hat."
      ],
      [
        "Und selbst das, was sich für das Morgenland aus dem entwickelt hat, was Alexander dann wiederum zurücktrug - wenn auch in einer Art, die sich in gewisser Beziehung nicht rechtfertigen lässt - aus dem Okzident in den Orient, auch das hat sich nur entwickeln können, nachdem zuerst das dem Verfall Geweihte auch in bezug auf seine physische Kraft zurückgeschlagen war von dem, was als flammender Enthusiasmus für die Tempelschätze in den Seelen der Griechen lebte.",
        "Wenn wir das erfassen, dann werden wir nicht nur nachwirken sehen die Weisheit vom Feuer des Heraklit, die grossen Ideen des Anaxagoras, wir werden nicht nur nachwirken sehen die umfassenden Ideen des Thales, sondern auch die realen Lehren der Hüter der Tempelweisheit im vorhistorischen Griechentum."
      ],
      [
        "Das wer­den wir empfinden als ein Ergebnis spiritueller Mächte, die dem Griechentum das gebracht haben, was ihm gebracht werden musste.",
        "Wir werden das alles fühlen in den Seelen der griechischen Helden, die gegen die Perser in den verschiedenen Schlachten standen."
      ],
      [
        "So muss man lernen Geschichte fühlen, meine lieben Freunde, denn das, was uns sonst als Geschichte gegeben wird, ist ja nur ein leeres Abstraktum von Ideen - wenn es hoch kommt.",
        "Was im Späteren von dem Früheren wirkt, das kann man nur beobachten, wenn man auf das zurückgeht, was den Menschenseelen vielleicht durch Jahr­tausende gegeben ist, und was dann reale Formen annimmt in einer gewissen Zeit."
      ],
      [
        "Woran lag es, dass bei diesem Aufstieg die alten Tempelschätze so Grosses den Griechen geben konnten?",
        "Das lag in dem Universellen, Umfassenden und in dem um alles andere unbe­kümmerten Charakter dieser Tempelschätze."
      ],
      [
        "Es war etwas, was als ein Ursprüngliches gegeben war, was ausfüllen konnte den ganzen Menschen, was sozusagen eine unmittelbar richtunggebende Kraft hatte."
      ],
      [
        "Und da kommen wir an das eigentliche Charakteristikon derjenigen Kulturen, die zunächst im Aufstiege begriffen sind bis zu ihrem Höhepunkt."
      ],
      [
        "In diesen Kulturen wird alles, was im Menschen lebendig tätig ist - da wird Schönheit, da wird Tugend, da wird das Nützliche, das Zweckmässige, alles das, was der Mensch im Leben tun und realisieren will -, alles das wird gesehen als ein aus dem Weisheits­vollen, aus dem Spirituellen unmittelbar Hervorgehendes.",
        "Und die Wdsheit ist dasjenige, was die Tugend, die Schönheit, was alles Übrige enthält."
      ],
      [
        "Wenn der Mensch von den Tempeiweistümern durchsetzt, inspiriert ist, dann ergibt sich alles andere von selbst; so ist das Gefühl für solche aufsteigende Zeiten.",
        "In dem Augenblick aber, wo die Fragen, wo die Empfindungen auseinanderfallen, wo zum Beispiel die Frage nach dem Guten oder nach dem Schönen selb­ständig wird gegenüber der Frage nach dem göttlichen Urgrunde, da beginnen die Zeiten des Verfalls."
      ],
      [
        "Daher können wir sicher sein, dass wir immer in einer Verfallszeit leben, wenn betont wird, dass neben dem ursprünglich Spirituellen noch besonders gepflegt werden soll dieses oder jenes, dass dieses oder jenes die Hauptsache sein soll.",
        "Wenn man nicht das Vertrauen hat zu dem Spirituellen, dass es alles das, was für das Menschenleben notwendig ist, aus sich heraus gebären kann, dann zerfallen die einheitlichen Kulturströme, die beim Aufsteigen eine Einheit bilden, in Einzelströmungen."
      ],
      [
        "Und das sehen wir da, wo sich ausserhalb der Weisheit, ausserhalb des spiri­tuellen Schwunges befindliche Interessen hineinmischen in das grie­chische Leben; das sehen wir im staatlichen Leben, wir sehen es auch in demjenigen Teile des griechischen Lebens, der uns besonders interessiert, im Geistigen unmittelbar hinter Aristoteles.",
        "Da beginnt neben der Frage: Was ist das Wahre?, in der enthalten ist die Frage:"
      ],
      [
        "Was ist das Gute und Zweckmässige? da beginnt die letztere Frage eine selbständige zu werden.",
        "Man fragt: Wie soll unser Wissen be­schaffen sein, damit man ein Mensch werden kann, der ein praktisches Lebensziel erreicht?",
        "Und so sehen wir eine Strömung in der Verfalls­zeit aufblühen' die wir den Stoizismus nennen.",
        "Bei Plato und Ari­stoteles war in dem Weisen zugleich das Gute enthalten; aller Schwung für das Gute konnte nur aus dem Weisen herauskommen.",
        "Die Stoiker fragen: Was muss der Mensch tun, um ein für das Leben, für die Lebenspraxis weiser, um ein zweckmässig gut lebender Mensch zu"
      ],
      [
        "werden?",
        "Praktische Lebensziele mischen sich hinein in dasjenige, was universeller Schwung der Wahrheit ehedem war."
      ],
      [
        "Beim Epikureismus mischt sich dann etwas hinein, was wir so bezeichnen können: Die Menschen fragen, wie muss ich mich ein­richten intellektuell, damit dieses Leben möglichst beseligend, mög­lichst innerlich harmonisch verlaufen kann?",
        "Auf diese Frage würden Thales, Plato, bis zu Aristoteles geantwortet haben: Suche nach der Wahrheit, und diese wird dir geben, was die grösste Seligkeit ist, was der Keim der Liebe ist."
      ],
      [
        "Jetzt aber trennt man die eine Frage von der Wahrheitsfrage ab, und es entsteht eine Strömung des Nieder­ganges.",
        "So ist das, was man Stoizismus und Epikureismus nennt, Strömung des Niederganges.",
        "So etwas hat dann immer im Gefolge, dass die Wahrheit fragwürdig wird für die Menschen, dass sie alle Kraft verliert."
      ],
      [
        "Daher tritt gleichzeitig mit dem Stoizismus und Epi­kureismus in der Verfallszeit der Skeptizismus, die Zweifelsucht gegen­über der Wahrheit auf.",
        "Und wenn Skeptizismus, Zweifelsucht, wenn Stoizismus' wenn Epikureismus ihr Wesen eine Zeitlang getrieben haben, dann fühlt sich der Mensch, der doch nach dem Wahren strebt, sozusagen wie aus der Weltenseele herausgeworfen und auf die eigene Seele zurückgewiesen."
      ],
      [
        "Dann schaut er sich um und sagt sich: Jetzt ist keine Weltepoche da, wo durch den fortwirkenden Strom der geistigen Mächte selber die Impulse in die Menschheit einströmen.",
        "Dann ist der Mensch auf sein eigenes inneres Leben, auf sein Subjekt zurückgewiesen."
      ],
      [
        "Das tritt uns im weiteren Verlaufe des griechischen Lebens im Neuplatonismus entgegen, in jener Philosophie, die keinen Zusammenhang mehr hat mit dem äusseren Leben, die in sich hineinblickt und im mystischen Aufstiege des Einzelnen zum Wahren hinaufstreben will.",
        "So haben wir eine ansteigende Kultur, so haben wir eine stufenweis absteigende."
      ],
      [
        "Und das, was sich herausgebildet hat im Aufstiege, das verrinnt und verrieselt dann langsam und allmählich, bis gegen das Heranrücken des Jahres 1250 eine allerdings nicht leicht bemerkbare, aber deshalb nicht minder grosse Inspiration für die Menschheit beginnt, die ich ja gestern in gewisser Weise charakterisiert habe und deren Abrieseln wir jetzt wieder seit dem 16.",
        "Jahrhundert haben."
      ],
      [
        "Denn seit jener Zeit treten"
      ],
      [
        "im Grunde genommen wiederum alle die Spezialfragen auf neben den Wahrheitsfragen; da wird wiederum ein Standpunkt genommen, der die Frage nach dem Guten, die Frage nach dem äusserlich Zweck­mässigen abtrennen will von der einen grossen Wahrheitsfrage.",
        "Und während diejenigen geistigen führenden Persönlichkeiten, die unter den Impulsen des Jahres 1250 standen, alle menschlichen Strömungen innerhalb der Wahrheit geschaut haben, sehen wir, wie jetzt im ganz eminenten Sinne auftritt das prinzipielle Trennen der praktischen Fragen des Lebens von den eigentlichen Wahrheitsfragen."
      ],
      [
        "Und an der Eingangspforte der neuen Verfallszeit, derjenigen Zeit, welche so recht bedeutet für das spirituelle Leben des Hinuntersausen - an der Eingangspforte steht Kant.",
        "In seiner Vorrede zu der zweiten Auflage der ,,Kritik der reinen Vernunft\" sagt er ausdrücklich: Ich musste das Streben nach der Wahrheit auf seine Grenzen zurückweisen, damit ich frei bekam das Feld für das, was die praktische Religion will."
      ],
      [
        "Und deshalb jene strenge Trennung der praktischen Vernunft von der theoretischen Vernunft.",
        "In der praktischen Vernunft die Postulate von Gott, Freiheit und Unsterblichkeit, rein hingeordnet auf das Gute; in der theoretischen Vernunft die Zertrümmerung jeder Erkenntnis-möglichkeit, um in irgendeine spirituelle Welt hineinzukommen."
      ],
      [
        "So stellen sich die Dinge welthistorisch.",
        "Und gewiss, auf den Spuren Kants wird noch lange das, was Weisheitsstreben unserer Zeit ist, verlaufen.",
        "Und wenn hingewiesen wird von unserer wirklich spiri­tuellen Strömung auf jene Erweiterung des Erkenntnisvermögens, auf jene Erhöhung des Erkenntnisvermögens über sich selbst hinaus, durch die es eindringen kann in übersinnliche Welten, dann wird man noch lange, lange hören können, dass es von allen Seiten tönt: ,,Ja, aber Kant sagt ...!,, In solchen Antithesen spielt sich in der Tat der historische Werdegang des Menschen ab."
      ],
      [
        "Und in dem, was instinktiv hervortritt wie eine Ahnung, da zeigt sich dann, dass unter dem, was eine blosse Maja ist und was hingenommen wird wie die Wahrheit, dass da unter dem Strome der Maja für die Menscheninstinkte doch das Richtige zu einem grossen Teil fliesst.",
        "Denn es ist ausserordentlich interessant, dass wir den absteigenden Gang der menschlichen Ent­wicklung bis zu der griechisch-lateinischen Zeit und das von uns"
      ],
      [
        "geforderte Wiederum-Hinaufsteigen in gewissen Ahnungen sehen, welche aus den Volksinstinkten heraus für das praktische Leben ge­geben worden sind."
      ],
      [
        "Wie mussten denn die Menschen, die ein Gefühl hatten für so etwas, denken?",
        "Wenn sie zurückschauten auf die grossen führenden Gestalten der Menschheitsgeschichte in der vorchristlichen Zeit oder - sagen wir besser - in der vorgriechischen Zeit, wie mussten sie zurück­schauen auf alle diejenigen, die wir charakterisieren konnten als die Instrumente für die Wesenheiten höherer Hierarchien?"
      ],
      [
        "Sie mussten sich sagen, selbst noch die Griechen: Das ist uns gekommen durch Menschen, in die eingeflossen sind übermenschliche göttliche Kräfte. -Und das sehen wir im Bewusstsein aller alten Zeiten leben: Die führen­den Persönlichkeiten, bis zu den Heroengestalten herunter, ja bis zu Plato, wurden als Söhne der Götter angesehen; das heisst hinter diesen Persönlichkeiten, die in der Geschichte auftreten, sahen die Menschen, wenn sie hinaufschauten in die Vorzeit, wenn sie den Blick immer wei­ter und weiter erhoben, sie sahen das Göttliche; und was da auftritt als Plato und in den Heroengestalten' das sahen sie an als herunter-gestiegen, ja selbst als geboren aus göttlichen Wesenheiten.",
        "Das war so recht die Anschauung, wie sich die Söhne der Götter mit den Töchtern der Menschen verbinden, um herunterzubringen das Spiri­tuelle auf den physischen Plan."
      ],
      [
        "Göttersöhne, Göttermenschen, das heisst solche, die eine Verbindung ihres Wesens mit dem Göttlichen hatten, sah man in diesen alten Zeiten.",
        "Dagegen in dem Moment, wo die Griechen fühlten: Jetzt können wir von dem Weben des Ich-im-Ich reden, von dem, was innerhalb der menschlichen Persönlichkeit liegt, - da reden sie von ihren höchsten Führern als von den sieben Weisen, und bezeichnen damit dasjenige, was sozusagen aus den Göttersöhnen zum rein Menschlichen geworden ist."
      ],
      [
        "Wie musste es nun weiter werden in den Instinkten der Völker in den nachgriechischen Zeiten?",
        "Da müsste dargestellt werden, was der Mensch ausbildet auf dem physischen Plan, und wie er das mit seiner vollen Frucht hinaufträgt in die spirituelleWelt.Wenn also ganz früher empfunden wurde: Man muss das Spirituelle vor dem physischen Menschen sehen und den physischen Menschen als Schattenbild, -"
      ],
      [
        "wenn man wahrend der griechischen Zeit Weise gesehen hat, die so­zusagen als Ich-im-Ich lebten, so musste man In der nachgriechischen Zeit Persönlichkeiten sehen, die auf dem physischen Plan leben und dann sich hinaufleben in das Spirituelle durch das, was im Physischen lebt.",
        "Dieser Begriff ist aus dem Instinkte eines Wissens herausgebildet.",
        "So wie die vorgriechische Zeit Göttersöhne und die Griechen Weise hatten, so haben die nachgriechischen Völker Heilige, die sich hin-aufleben in das spirituelle Leben durch das, was sie im physischen Plane erwirken.",
        "Da lebt etwas im Volksinstinkte, und da können wir hineinschauen, wie allerdings hinter der Maja etwas ist, was historisch doch die Menschheit vorwärtstreibt."
      ],
      [
        "Und wenn wir das erkennen, dann leuchtet das, was in diesen Zeiten lebt, herein in die einzelne Menschenseele, und wir begreifen, wie sich modifizieren muss das Gruppenkarma dadurch, dass die Menschen zugleich Werkzeuge des historischen Werdeganges sind.",
        "Und wir können so begreifen, was die Akashachronik zeigt: Wie wir in Novalis zum Beispiel etwas zu sehen haben, was zurückgeht bis zum alten Elias."
      ],
      [
        "Es ist das eine ausserordentlich interessante Inkar-nationenfolge.",
        "Da sehen wir, wie in Elias auftaucht das prophetische Element, denn die Hebräer hatten die Mission, vorzubereiten das­jenige, was später kommen sollte."
      ],
      [
        "Und sie bereiteten es vor in dem Übergang von ihren Patriarchen zu den Propheten, durch die Gestalt des Moses hindurchgehend.",
        "Während wir in Abraham noch sehen, wie der Hebräer das Nachwirken des Gottes in sich, in seinem Blute fühlt, sehen wir bei Elias den Übergang zur Entrückung in die spirituellen Welten."
      ],
      [
        "Alles bereitet sich nach und nach vor.",
        "In Elias lebt eine Individualität, die sich in den alten Zeiten schon erfüllt mit dem, was da in der Zukunft kommen soll.",
        "Und dann sehen wir, wie diese Individualität ein Werkzeug sein soll, um vorzubereiten das Verständnis für den Christusimpuls."
      ],
      [
        "Wir sehen, wie die Individualität des Elias in Johannes dem Täufer wiedergeboren wird; dieser ist das Werkzeug für ein Höheres.",
        "Es lebt in ihm eine Individualität, die Johannes den Täufer zum Werkzeuge macht; aber notwendig war die hohe Individualität des Elias, um dann als solches Instrument zu dienen."
      ],
      [
        "Wir sehen dann später, wie diese Individualität geeignet ist, das, was in die Zukunft hineinwirken soll, in Formen zu giessen, welche nur möglich waren unter dem Einnusse des vierten nachatlantischen Kulturzeitraumes.",
        "So taucht denn diese Individualität, so merkwürdig uns das erscheint, in Raphael wieder auf und verbindet das, was als christlicher Impuls für alle Zeiten wirken soll, mit den wunderbaren Formen des Griechentums in der Malerei.",
        "Und da können wir er­kennen, wie sich das individuelle Karma dieser Entelechle verhält zu der äusseren Inkarnation.",
        "Für die äussere Inkarnation wird verlangt, dass eine Zeitenmacht in Raphael sich aussprechen kann; für diese Zeitenmacht ist die Elias-Johannes-Individualität die geeignete.",
        "Aber die Zeit kann nur einen physischen Leib hergeben, der unter solcher Macht zerbrechlich sein muss; daher stirbt er so früh."
      ],
      [
        "Die andere Seite ihres Wesens muss diese Individualität ausprägen in einer Zeit, wo schon wieder die einzelnen Strömungen auseinander-fallen; da taucht sie wieder auf als Novalis.",
        "Da sehen wir, wie in diesem Novalis wirklich schon alles das in einer eigenartigen Gestalt lebt, was uns jetzt durch die Geisteswissenschaft gegeben wird.",
        "Denn so treffende Aussprüche über das Verhältnis des astralischen zum ätherischen und physischen Leib, von Wachsein und Schlafen, sind ausserhalb der Geisteswissenschaft von keinem gegeben worden als von Novalis, dem wiederauferstandenen Raphael.",
        "Das sind die Dinge, die uns zeigen, wie die Individualitäten die Werkzeuge sind des fort-fliessenden Stromes der Menschheitsentwicklung.",
        "Und wenn wir das menschliche Werden sehen, wenn wir hinschauen auf diesen rätsel-vollen Wechsel in dem, was historisch geschieht, dann können wir dasjenige ahnen, was von tiefen spirituellen Mächten in ihm lebt.",
        "In einer merkwürdigen Weise geht das Frühere in das Spätere über."
      ],
      [
        "Für einige von Ihnen habe ich es ja schon gesagt, dass man einen merkwürdigen historischen Ausblick konstatieren kann beim Über­gang von Michelangelo zu Galilei.",
        "Und ein sonst sehr gescheiter Mann - wohlgemerkt, ich sage nicht, dass es sich hier um eine Rein­karnation handelt, sondern um einen historischen Fortgang - eine sehr gescheite Persönlichkeit machte darauf aufmerksam, wie es doch sonderbar ist, wenn wir beim Anblick der wunderbaren Architektonik"
      ],
      [
        "der Petersklrche sehen, wie der menschliche Geist in sie hineinver­woben hat das, was er mechanische Wissenschaft nennt. 0, in diesen grandiosen Formen der Petersklrche sehen wir verkörpert die me­chanischen Gedanken, die der menschliche Intellekt fassen konnte, noch dazu umgesetzt ins Schöne, ins Grandiose: Michelangelos Ge­danke!",
        "Wie der Anblick der Peterskirche wirken kann, meine lieben Freunde, das tritt in den mannigfaltigsten Beziehungen auf, und viel-leicht hat ein jeder so ein bisschen von dem erlebt, was der Wiener Bildhauer Natter erlebte - oder was mit ihm erlebt worden ist."
      ],
      [
        "Er fuhr mit einem Freunde gegen die Petersklrche hin; sie hatten sie noch nicht erblickt, plötzlich hört der andere, dass Natter, indem er von seinem Sitze aufspringt, ganz ausser sich kommt und sagt: Mir wird angst!",
        "Denn in diesem Augenblick hat er die Petersklrche er­blickt ... er wollte sich später daran gar nicht erinnern."
      ],
      [
        "Etwas Ähnli­ches kann ja schliesslich jeder Mensch erleben, wenn er so etwas Grandioses sieht.",
        "Und nun machte ein sehr gescheiter Mann, der Professor Müllner' in einer Rektoratsrede darauf aufmerksam, dass der grosse Denker mechanischer Gedanken, Galilei, intellektuell für die Menschheit das gelehrt hat, was hineingebaut hat in die räumlichen Formen Michelangelo in die Peterskirche."
      ],
      [
        "So dass uns in Galileis Ge­danken intellektuell das wieder entgegentritt, was wie kristallisiert als Mechanik, als menschliche Mechanik in der Petersklrche dasteht.",
        "Aber sonderbar ist es dabei, dass derselbe Mann in diesem Vortrag darauf aufmerksam machen musste, der Todestag des Michelangelo sei der Geburtstag des Galilei."
      ],
      [
        "Das heisst, dass das Intellektuelle, die Gedanken, die mechanisch durch Galilei in Intellektualität geprägt worden sind, aufgetaucht sind in einer Persönlichkeit, die geboren ist an dem Todestage dessen, der sie in den Raum hineingestellt hat.",
        "Und so sollte man fragen: Wer hat durch Michelangelo die Mechanik, welche die Menschheit erst durch Galilei nachher bekommen hat, in die Peterskirche hineingebaut?"
      ],
      [
        "Wenn durch die ja ganz aphoristischen und vereinzelten Gedanken, die in Anlehnung an den historischen Werdegang der Menschheit hier vorgebracht werden durften, wenn aus diesen in ihrem Zusammen­schluss in Ihren Herzen ein Gefühl davon hervorgeht, wie die wirklichen,"
      ],
      [
        "die realen geistigen Mächte durch ihre Werkzeuge in der Ge­schichte wirken, dann werden Sie in richtiger Weise diese Ausfüh­rungen entgegengenommen haben.",
        "Und dann könnte man dieses Ge­fühl als das bezeichnen, was aus der okkult-hlstorischen Betrachtung als ein rechtes Gefühl für das Werden in der Zeit, für den Fortgang in der Zeit in unsere Herzen kommen kann.",
        "Und heute, an einem kleinen Wendepunkt der Zeit, mag es angemessen sein, einmal die Meditation hinzulenken auf solches Fühlen des Menschenfortganges und des Götterfortganges in der Zeit.",
        "Und wenn von Ihnen, meine lieben Freunde, jedes Herz das aufnehmen möchte - dieses Gefühl für die Umsetzung der Wissenschaft vom okkulten Fortschritte in der Zeit - in Empfindung für das Weben und Schaffen im Werden, im Menschenfortschritt' in den wir hineingestellt sind, - wenn jede Seele von Ihnen das aufnehmen möchte als ein lebendiges Gefühl, so dürfte vielleicht in diesem Gefühl auch ein Neujahrswunsch in der Seele von Ihnen allen leben.",
        "Und diesen Neujahrswnnsch möchte ich am Schlusse dieses Zyklus von dieser Stätte hier in Ihre Seelen hinein-gesenkt sein lassen: Betrachten Sie das, was gesprochen worden ist, als etwas, was den Ausgang bilden soll für ein Zeitgefühl.",
        "Und in ge­wisser Weise mag es symbolisch sein, dass wir einen kleinen Übergang von einem Zeitabschnitt zu einem anderen dazu benutzen konnten, um solche die Zeitenübergänge umspannenden Ideen in unserer Seele einmal wirken zu lassen."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Seite 11    Vorträge in verschiedenen Arbeitsgruppen: Vgl. Rudolf Steiner, Das Matthäus-Evangelium, Dornach ,949, sowie Exkurse in das Gebiet des Markus-Evangeliums, Dornach 1947.",
      "Seite 13    Vortrag in ier Weihnachtsfeier: Die Juliestxeit, die Christfest-Symbole und die weithistorische Stimmung anthroposophischer Vorstellungsart, Dornach",
      "Seite 25 ff.    Theophilos, Patriarch von Alexandrien 385-412. Verfolgte die Anhänger des Origenes.",
      "Kyrillos (Cyrillus), Patriarch von Alexandrien, folgte 412 auf Theophilos. Kirchenvater, war noch am Konril zu Ephesos 431 maßgebend beteiligt.",
      "Seite 29    Herder über die Geschichte: J. G. Herder, Ideen zur Geschichte der Philosophie der Menschheit (1784-1791).",
      "Seite 30    G. E. Lessing, Die Erziehung des Menschengeschlechts (1780).",
      "Hehhel-Tagebnch: «Nach der Seelenwanderung ist es möglich, daß Plato jetzt wieder auf der Schulbank Prügel bekommt, weil er - den Plato nicht versteht» (Hebbels Tagebücher Nr.1335).",
      "Seite 31    Salomon Reinach, Orpheus, Allgemeine Geschichte der Religion, 4. Aufl. Wien 1911.",
      "Seite 34    Anatole France, Vie dc Jeanne d'Arc, 2 Bände, 49. Aufl. Paris 1927. Gfrorer, Augnct Friedrich (1803-1861).",
      "Seite 35    Brief des Pereeval von Boulainvilliers vom 21. Juni 1429, vgl. Procés de condam-nation et de réabilitation de Jeanne d'Arc, éd. Quicherat, Tome V p.115 ff., Paris 1849. Die Quelle des hier wiedergegebenen deutschen Textes des Briefes lag dem Herausgeber nicht vor; vgl. dazu Quicherat a. a. O. p. 114. Der Name Boulainvilliers wurde in den alten Übersetzungen auf verschiedene Weise falsch wiedergegeben.",
      "Seite 41    «Blut ist ein ganz besonderer Saft», erschien 1907, 20. Tausend. Dornach 1940.",
      "Seite 51    Zyklus über die Apokalypse: Rudolf Steiner, Die Apokalypse des Johannes (Zyklus 6), Dornach 1954.",
      "Seite 57    Edsard Hanslick, Vom Mnsikalisch-Schönen. Ein Beitrag zur Revision der Ästhetik der Tonkunst. Leipzig 1854.",
      "Seite 62    Stelle aus Blavatsky: H. P. Blavatsky, Thc Seeret Doctrine III, London 1897. Die bier in Übersetzung wiedergegebene Stelle steht auf S. 370.",
      "Seite 72    Fritz Mauthner (1849-1923), Schriftsteller, Journalist, Verfasser von philo­sophischen Werken, insbesondere über die Sprache. Wird oft von Rudolf Steiner erwähnt.",
      "Seite 78 f.    Berliner Arzt: Wilhelm Fließ (1858 geb.). Schrieb u. a.: Der Ablauf des Lebens. Grundlegung zur exakten Biologie, Leipzig und Wien 1906; Das",
      "Jahr im Lebendigen, Jena 1918.",
      "Seite 81    Julian Apostata (331-363), regierte 361-363.",
      "Seite 84ff.    Tycho de Brabe (1546-1601).",
      "Seite 92    Amshaspands: Vgl. hierzu auch Rudolf Steiner, Mythen und Zeichen (Vor-träge aus dem Jahre 1907), Dornach 1951, sowie Wendepunkte des Geistes­lebens (Vortrage aus dem Jahre 1911), 1. Vortrag, Freiburg i. Br. 1954.",
      "Seite 100    Zum Jahre 1250: Vgl. auch Rudolf Steiner, Die geistige Führung des Men­",
      "schen und der Menschheit, Freiburg i. Br. 1955.",
      "Seite 102    Nicolaus Gusanus (1401-1464), schrieb 1440 sein Werk «De docta ignorantia». Vgl. auch Rudolf Steiner, Das Leben zwischen dem Tode und der neuen Geburt im Verhältnis zu den kosnischen Tatsachen (Zyklus 37), 5. Vortrag, Dornach 1936. - Der Vortrag, auf den Rudolf Steiner hinweist, wurde gehalten an der Generalversanunlung der deutschen Sektion der Theosophi-sehen Gesellschaft in Berlin am 18. Oktober 1903 (Autoreferat in «Luzifer» Nr.6, Berlin 1903).",
      "Seite 103    Rosenkreuzermysterium: Rudolf Steiner, Die Pforte der Einweihung, ein Rosenkreuzermysterium Erschien 1910, letzte Auflage Dornach 1956. Vgl. hierzu auch Rudolf Steiner, Das Wiedererscheinen des Christus im Ätheri­schen, Dornach 2936.",
      "Seite 104    Oherlin: G. H. v. Schubert, Züge aus dem Leben des Job. Friedr. Oberlin, gewesenen Pfarrers im Steinthal, Nürnberg 1832.",
      "Seite 105  Roman von Fritz Lienhard: Oberlin (84. Aufl. Stuttgart 1920).",
      "Seite 110/11    Vgl. hierzu Rudolf Steiner, Weltenwunder, Seelenprüfugen und Geistes-offenbarungen (Zyklus 18), 6.Vortrag, Dornach 1932.",
      "Seite 114    Kant: «Ich mußte das Wissen aufheben, um zum Glauben Platz zu bekom­men...» (aus der Vorrede zur 2. Aufl. der «Kritik der reinen Vernunft»).",
      "Seite 116    Novalis, Elias: Vgl. hierzu auch Rudolf Steiner, Der irdische und der kos­ruische Mensch (Zyklus 36), 4. Vortrag, Dornach 1932.",
      "Seite 117    Für einige habe ich es gesagt  . Siehe Rudolf Steiner, Menschengeist ud Tier-geist (Berlin, 17. November 1910), in Die Drei, 9. Jahrgang Heft 4, Stuttgart",
      "Seite 118    Heinrich Natter, Bildhauer (1846-1892).",
      "Mnliners Rektoratsrede: Lauremt Müliner, Die Bedeutung Calileis für die",
      "Philosophie. Wien 1894, wiederabgedruckt in <{Anthroposophie» 16. Jahrgang",
      "Buch 1 S. 29 ff., Stuttgart 1933."
    ],
    "sentences": [
      [
        "Seite 11 Vorträge in verschiedenen Arbeitsgruppen: Vgl.",
        "Rudolf Steiner, Das Matthäus-Evangelium, Dornach ,949, sowie Exkurse in das Gebiet des Markus-Evangeliums, Dornach 1947."
      ],
      [
        "Seite 13 Vortrag in ier Weihnachtsfeier: Die Juliestxeit, die Christfest-Symbole und die weithistorische Stimmung anthroposophischer Vorstellungsart, Dornach"
      ],
      [
        "Seite 25 ff.",
        "Theophilos, Patriarch von Alexandrien 385-412.",
        "Verfolgte die Anhänger des Origenes."
      ],
      [
        "Kyrillos (Cyrillus), Patriarch von Alexandrien, folgte 412 auf Theophilos.",
        "Kirchenvater, war noch am Konril zu Ephesos 431 maßgebend beteiligt."
      ],
      [
        "Seite 29 Herder über die Geschichte: J.",
        "Herder, Ideen zur Geschichte der Philosophie der Menschheit (1784-1791)."
      ],
      [
        "Seite 30 G.",
        "Lessing, Die Erziehung des Menschengeschlechts (1780)."
      ],
      [
        "Hehhel-Tagebnch: «Nach der Seelenwanderung ist es möglich, daß Plato jetzt wieder auf der Schulbank Prügel bekommt, weil er - den Plato nicht versteht» (Hebbels Tagebücher Nr.1335)."
      ],
      [
        "Seite 31 Salomon Reinach, Orpheus, Allgemeine Geschichte der Religion, 4.",
        "Aufl.",
        "Wien 1911."
      ],
      [
        "Seite 34 Anatole France, Vie dc Jeanne d'Arc, 2 Bände, 49.",
        "Aufl.",
        "Paris 1927.",
        "Gfrorer, Augnct Friedrich (1803-1861)."
      ],
      [
        "Seite 35 Brief des Pereeval von Boulainvilliers vom 21.",
        "Juni 1429, vgl.",
        "Procés de condam-nation et de réabilitation de Jeanne d'Arc, éd.",
        "Quicherat, Tome V p.115 ff., Paris 1849.",
        "Die Quelle des hier wiedergegebenen deutschen Textes des Briefes lag dem Herausgeber nicht vor; vgl. dazu Quicherat a. a.",
        "O. p. 114.",
        "Der Name Boulainvilliers wurde in den alten Übersetzungen auf verschiedene Weise falsch wiedergegeben."
      ],
      [
        "Seite 41 «Blut ist ein ganz besonderer Saft», erschien 1907, 20.",
        "Tausend.",
        "Dornach 1940."
      ],
      [
        "Seite 51 Zyklus über die Apokalypse: Rudolf Steiner, Die Apokalypse des Johannes (Zyklus 6), Dornach 1954."
      ],
      [
        "Seite 57 Edsard Hanslick, Vom Mnsikalisch-Schönen.",
        "Ein Beitrag zur Revision der Ästhetik der Tonkunst.",
        "Leipzig 1854."
      ],
      [
        "Seite 62 Stelle aus Blavatsky: H.",
        "Blavatsky, Thc Seeret Doctrine III, London 1897.",
        "Die bier in Übersetzung wiedergegebene Stelle steht auf S. 370."
      ],
      [
        "Seite 72 Fritz Mauthner (1849-1923), Schriftsteller, Journalist, Verfasser von philo­sophischen Werken, insbesondere über die Sprache.",
        "Wird oft von Rudolf Steiner erwähnt."
      ],
      [
        "Seite 78 f.",
        "Berliner Arzt: Wilhelm Fließ (1858 geb.).",
        "Schrieb u. a.: Der Ablauf des Lebens.",
        "Grundlegung zur exakten Biologie, Leipzig und Wien 1906; Das"
      ],
      [
        "Jahr im Lebendigen, Jena 1918."
      ],
      [
        "Seite 81 Julian Apostata (331-363), regierte 361-363."
      ],
      [
        "Seite 84ff.",
        "Tycho de Brabe (1546-1601)."
      ],
      [
        "Seite 92 Amshaspands: Vgl. hierzu auch Rudolf Steiner, Mythen und Zeichen (Vor-träge aus dem Jahre 1907), Dornach 1951, sowie Wendepunkte des Geistes­lebens (Vortrage aus dem Jahre 1911), 1.",
        "Vortrag, Freiburg i.",
        "Br. 1954."
      ],
      [
        "Seite 100 Zum Jahre 1250: Vgl. auch Rudolf Steiner, Die geistige Führung des Men­"
      ],
      [
        "schen und der Menschheit, Freiburg i.",
        "Br. 1955."
      ],
      [
        "Seite 102 Nicolaus Gusanus (1401-1464), schrieb 1440 sein Werk «De docta ignorantia».",
        "Vgl. auch Rudolf Steiner, Das Leben zwischen dem Tode und der neuen Geburt im Verhältnis zu den kosnischen Tatsachen (Zyklus 37), 5.",
        "Vortrag, Dornach 1936. - Der Vortrag, auf den Rudolf Steiner hinweist, wurde gehalten an der Generalversanunlung der deutschen Sektion der Theosophi-sehen Gesellschaft in Berlin am 18.",
        "Oktober 1903 (Autoreferat in «Luzifer» Nr.6, Berlin 1903)."
      ],
      [
        "Seite 103 Rosenkreuzermysterium: Rudolf Steiner, Die Pforte der Einweihung, ein Rosenkreuzermysterium Erschien 1910, letzte Auflage Dornach 1956.",
        "Vgl. hierzu auch Rudolf Steiner, Das Wiedererscheinen des Christus im Ätheri­schen, Dornach 2936."
      ],
      [
        "Seite 104 Oherlin: G.",
        "H. v.",
        "Schubert, Züge aus dem Leben des Job.",
        "Friedr.",
        "Oberlin, gewesenen Pfarrers im Steinthal, Nürnberg 1832."
      ],
      [
        "Seite 105 Roman von Fritz Lienhard: Oberlin (84.",
        "Aufl.",
        "Stuttgart 1920)."
      ],
      [
        "Seite 110/11 Vgl. hierzu Rudolf Steiner, Weltenwunder, Seelenprüfugen und Geistes-offenbarungen (Zyklus 18), 6.Vortrag, Dornach 1932."
      ],
      [
        "Seite 114 Kant: «Ich mußte das Wissen aufheben, um zum Glauben Platz zu bekom­men...» (aus der Vorrede zur 2.",
        "Aufl. der «Kritik der reinen Vernunft»)."
      ],
      [
        "Seite 116 Novalis, Elias: Vgl. hierzu auch Rudolf Steiner, Der irdische und der kos­ruische Mensch (Zyklus 36), 4.",
        "Vortrag, Dornach 1932."
      ],
      [
        "Seite 117 Für einige habe ich es gesagt .",
        "Siehe Rudolf Steiner, Menschengeist ud Tier-geist (Berlin, 17.",
        "November 1910), in Die Drei, 9.",
        "Jahrgang Heft 4, Stuttgart"
      ],
      [
        "Seite 118 Heinrich Natter, Bildhauer (1846-1892)."
      ],
      [
        "Mnliners Rektoratsrede: Lauremt Müliner, Die Bedeutung Calileis für die"
      ],
      [
        "Philosophie.",
        "Wien 1894, wiederabgedruckt in <{Anthroposophie» 16.",
        "Jahrgang"
      ],
      [
        "Buch 1 S. 29 ff., Stuttgart 1933."
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
