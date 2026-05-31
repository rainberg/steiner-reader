#!/usr/bin/env python3
"""Standalone import script for GA128 — GA128 - Eine okkulte Physiologie"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA128 - Eine okkulte Physiologie"""
GA_NUMBER = "GA128"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "ERSTER VORTRAG Prag, 20. März 1911",
    "paragraphs": [
      "In diesem Vortragszyklus, der auf Veranlassung unserer Prager Freunde gehalten wird, soll ein Thema behandelt werden, welches dem Menschen ungeheuer naheliegt, weil es ja das genauere Wesen des Menschen unmittelbar berührt und von dem handelt, was sich auf sein physisches Leben selber bezieht. Wenn dieses Thema auch auf der einen Seite dem Menschen so naheliegt, weil es ihn ja selbst betrifft, so darf man doch sagen, daß es auf der anderen Seite ein sehr schwer zugängliches Thema ist.",
      "Denn schon der Blick auf die durch alle Zeiten, man möchte sagen, aus mystisch-okkulten Höhen an den Menschen dringende Forderung «Erkenne dich selbst» zeigt uns die Tatsache, daß Selbsterkenntnis, wirkliche, wahre Selbsterkenntnis, im Grunde genommen dem Menschen recht schwierig ist, und das bezieht sich nicht nur auf die individuelle, persönliche Selbsterkennt­nis, sondern vor allen Dingen auch auf die Erkenntnis der mensch­lichen Wesenheit überhaupt. Und weil der Mensch - wie man sehen kann aus dieser ewigen Forderung «Erkenne dich selbst» - sich selbst seiner Wesenheit nach so sehr fernsteht, einen so weiten Weg hat, um sich selbst zu verstehen, deshalb wird in einer gewissen Beziehung das, was Gegenstand der folgenden Betrachtungen dieser Tage wer­den wird, als etwas Fernliegendes erscheinen, zu dessen Verständnis sehr Verschiedenes notwendig ist.",
      "Nicht ohne Grund ging ich selbst erst nach längerer Zeit und reiflicher Überlegung daran, auch einmal über dieses Thema zu sprechen. Denn es ist ein Thema, demgegen­über - soll man zu einer wahren, wahrhaften Betrachtung kommen -etwas unbedingt notwendig ist, was bei einer gewöhnlichen wissen­schaftlichen Betrachtung so oft außer acht gelassen wird: Notwendig ist, daß man vor der Wesenheit des Menschen - wohlgemerkt, nicht vor der Wesenheit des einzelnen Menschen, insbesondere dann nicht, wenn dieser einzelne Mensch wir selber sind -, daß man vor dem Wesen des Menschen im allgemeinen Ehrfurcht habe.",
      "Und es muß als eine Grundbedingung für unsere folgenden Betrachtungen angesehen",
      "werden, daß man Ehrfurcht habe vor dem, was die menschliche Wesenheit in Wahrheit bedeutet.",
      "Wie kann man denn davor wahrhafte Ehrfurcht haben? Auf keine andere Art, als daß man zunächst absieht von dem, wie der Mensch -ganz gleichgültig, ob wir selbst oder ein anderer - uns im alltäglichen Leben erscheint, und indem man sich aufschwingt zu der Anschau­ung: Dieser Mensch mit seiner gesamten Entwickelung ist nicht um seiner selbst willen da, er ist da zur Offenbarung des Geistes, der ganzen Welt des Göttlich-Geistigen, er ist eine Offenbarung der Weltengottheit, des Weltengeistes.",
      "Und für diejenigen, die erkennen, daß alles, was uns umgibt, Ausdruck ist für göttlich-geistige Kräfte, für die ist es auch möglich, diese Ehrfurcht zu empfinden, nicht nur für das Göttlich-Geistige selbst, sondern auch für die Offenbarungen dieses Göttlich-Geistigen. Und wenn wir davon sprechen, daß der Mensch nach immer vollkommenerer Selbsterkenntnis trachte, so sollen wir uns darüber klar sein, daß nicht bloß Neugierde, meinet-willen auch Wißbegierde, uns veranlassen soll, nach Selbsterkenntnis zu streben, sondern daß wir es als Pflicht empfinden müssen, die Erkenntnis der Offenbarungen des Weltengeistes durch den Men­schen immer vollkommener und vollkommener zu gestalten.",
      "In die­sem Sinne sind die Worte zu verstehen: Unwissend zu bleiben, wo Erkenntnis möglich ist, bedeutet eine Versündigung gegen die göttli­che Bestimmung des Menschen. Denn der Weltengeist hat in uns die Kraft gelegt, wissend zu werden; und wenn wir nicht erkennend werden wollen, so lehnen wir es ab - was wir eigentlich nicht dürf­ten -, eine Offenbarung des Weltengeistes zu sein, und stellen immer mehr und mehr nicht eine Offenbarung des Weltengeistes dar, son­dern eine Karikatur, ein Zerrbild von ihm.",
      "Es ist unsere Pflicht, nach Erkenntnis zu streben, um immer mehr und mehr ein Bild des Weltengeistes zu werden. Erst wenn wir mit diesen Worten einen Sinn verbinden können, «ein Bild des Weltengeistes zu werden», erst wenn es uns bedeutungsvoll wird, in diesem Sinne zu sagen: Wir müssen erkennen, es ist unsere Pflicht zu erkennen -, erst dann können wir das vorhin geforderte Gefühl von Ehrfurcht gegenüber der Wesenheit des Menschen so recht empfinden.",
      "Und für den, der",
      "im okkulten Sinne das Leben des Menschen, das Wesen des Men­schen betrachten will, für den ist diese Durchdringung mit Ehrfurcht vor der menschlichen Natur schon deshalb eine unbedingte Notwen­digkeit, weil diese Durchdringung mit Ehrfurcht einzig und allein geeignet ist, unsere geistigen Augen und unsere geistigen Ohren, unser ganzes geistiges Schauvermögen wachzurufen, das heißt dieje­nigen Kräfte, die uns eindringen lassen in die geistigen Untergründe der menschlichen Natur. Wer als Seher, als Geistesforscher nicht im höchsten Grade Ehrfurcht haben könnte vor der menschlichen Natur, wer sich nicht durchdringen kann bis in die innersten Fibern seiner Seele mit dem Gefühl von Ehrfurcht gegenüber der Menschen-natur, dem Abbild des Geistes, dem bliebe das Auge, wenn es noch so geöffnet ist für diese oder jene geistigen Geheimnisse der Welt, verschlossen für alles das, was sich auf die eigentlich tiefere Wesen­heit des Menschen selber bezieht. Und es mag viele Hellseher geben, welche dieses oder jenes schauen können in dem geistigen Umkreis unseres Daseins: Wenn ihnen diese Ehrfurcht fehlt, dann fehlt ihnen das Vermögen, in die Tiefen der menschlichen Natur hineinzu­schauen, und sie werden nichts Richtiges über das zu sagen wissen, was des Menschen Wesenheit ist.",
      "Man nennt ja die Lehre von den Lebensvorgängen des Menschen «Physiologie». Diese Lehre soll hier nicht in der Weise betrachtet werden, wie es in der äußeren Wissenschaft geschieht, sondern so, wie sie dem geistigen Auge sich darbietet, so daß wir von den äußeren Gestaltungen des Menschen, von der Form und den Lebensvorgän­gen seiner Organe immer hinblicken auf die geistige, übersinnliche Grundlage der Organe, der Lebensformen, der Lebensprozesse. Und da nicht die Absicht besteht, diese «okkulte Physiologie», wie man auch sagen könnte, in irgendeiner unsachlichen Weise hier zu treiben, so wird es notwendig sein, daß in einer gewissen unbefangenen Weise an manchen Stellen Hindeutungen gemacht werden auf Dinge, wel­che dem mehr oder weniger Außenstehenden am Anfang recht unwahrscheinlich klingen werden. Es muß ausdrücklich betont wer­den, daß dieser Vortragszyklus, noch mehr als mancher andere, den ich gehalten habe, ein Ganzes bildet und daß aus einzelnen Vorträgen,",
      "insbesondere aus den Anfangsvorträgen, nichts aus dem Zusam­menhang herausgerissen beurteilt werden kann, weil manches unbe­fangen wird gesagt werden müssen. Und erst, wenn man die Schluß-vorträge gehört haben wird, wird man sich ein Urteil bilden können über das, was eigentlich gesagt werden soll. Denn das Thema wird hier in einer etwas anderen Weise behandelt werden als in der äuße­ren Physiologie. Die Anfangsgründe werden sich auch bestätigen durch das, was uns zuletzt entgegentreten wird. Wir werden sozu­sagen nicht eine gerade Linie vom Anfang bis zum Ende zu be­schreiben haben, sondern wir werden in einer Kreislinie vorgehen, so daß wir am Ende dort wieder ankommen, von wo wir ausgegan­gen sind.",
      "Eine Betrachtung des Menschen soll es sein, was hier dargeboten wird. Zunächst tritt uns dieser Mensch für die äußeren Sinne seiner äußeren Form nach entgegen. Wir wissen ja, daß zu dem, was zunächst die reine äußere laienhafte Betrachtung über den Menschen wissen kann, heute schon sehr vieles kommt, was die Wissenschaft hinzuerforscht hat. Daher müssen wir das, was wir in äußerer Weise, aus der äußeren Erfahrung und Beobachtung über den Menschen heute wissen können, notwendigerweise zusammenstellen aus dem, was schon der Laie an sich und an anderen Menschen zu beobachten in der Lage ist, und dem, was der Wissenschaft gelungen ist zu erforschen, welche durch bewunderungswürdige Methoden, durch bewunderungswürdige Instrumente zu ihren Resultaten über die Leiblichkeit des Menschen kommt.",
      "Wenn man alles zusammenhält, was man als Laie rein äußerlich am Menschen sehen kann, was man vielleicht auch schon aus irgendwel­chen populären Beschreibungen kennengelernt hat, dann wird es vielleicht nicht unverständlich sein, wenn darauf aufmerksam gemacht wird, daß schon die äußere Gestalt des Menschen, wie sie uns in der Außenwelt entgegentritt, aus einer Zweiheit besteht. Für den, der in die Tiefen der Menschennatur eindringen will, ist es durchaus notwendig, sich bewußt zu werden, daß schon der äußere Mensch seiner Form und Gestaltung nach im Grunde genommen eine Zweiheit darstellt.",
      "Das eine, das wir am Menschen deutlich unterscheiden können, ist alles das, was sich als eingeschlossen erweist in Organe, die den größtmöglichen Schutz gegen die Außenwelt gewähren. Es ist alles das, was wir zählen können zum Bereich des Gehirns und des Rük­kenmarkes. Alles, was in dieser Beziehung zur menschlichen Natur gehört, zu Gehirn und Rückenmark, ist fest umschlossen von siche­ren, Schutz gewährenden Knochengebilden. Wenn wir schematisch darstellen wollen, was zu diesen beiden Bereichen gehört, so können wir uns das in folgender Weise veranschaulichen: Wenn a (siehe Zeichnung) schematisch darstellt die Summe der übereinandergelagerten",
      "# Bild s. 15",
      "Wirbelknochen, die längs des Rückenmarkes verlaufen, b die Schädeldecke und die Schädelknochen, so ist eingeschlossen inner­halb des Kanales, der gebildet wird durch die übereinandergelagerten Wirbelknochen sowie durch die Knochen des Schädels, alles, was in den Bereich des Gehirns und des Rückenmarkes gehört. Man kann den Menschen nicht betrachten, ohne sich bewußt zu werden, daß alles, was in diesen Bereich gehört, im Grunde genommen eine in sich geschlossene Ganzheit bildet und daß alles übrige vom Menschen, das wir in verschiedenster Weise physiologisch angliedern können -Hals, Rumpf, Gliedmaßengebilde -, mit Gehirn und Rückenmark in Verbindung steht durch, bildlich gesprochen, mehr oder weniger fadenförmige oder bandförmige Gebilde. Diese müssen erst die",
      "Schutzhülle durchbrechen, damit eine Verbindung hergestellt werden kann mit dem innerhalb dieser Knochengebilde eingeschlossenen Teil. So können wir sagen: Es erweist sich schon einer oberflächli­chen Betrachtung gegenüber alles, was am Menschen ist, als eine Zweiheit; das eine liegt innerhalb der charakterisierten Knochen-gebilde in festen und sicheren Schutzhüllen, das andere außerhalb derselben.",
      "Nun müssen wir zunächst einen ganz oberflächlichen Blick auf das werfen, was innerhalb dieser Knochengebilde liegt. Da können wir wieder leicht unterscheiden zwischen jener großen Masse, die in die Schädelknochen eingebettet ist als Gehirn, und dem anderen Teil, der wie ein Stiel oder Strang daranhängt, der in organischer Verbindung mit dem Gehirn steht und sich wie eine Art fadenförmiger Auswuchs desselben in den Rückgratkanal hineinstreckt, das Rückenmark.",
      "Wenn wir diese zwei Gebilde voneinander unterscheiden, dann müs­sen wir schon auf etwas aufmerksam machen, worauf die äußere Wissenschaft nicht aufmerksam zu machen braucht, worauf aber die okkulte Wissenschaft, die in die Tiefe des Wesens der Dinge einzu­dringen hat, wohl aufmerksam machen muß. Es muß darauf auf­merksam gemacht werden, daß alles, was wir auf dem Boden einer Betrachtung über den Menschen sagen, sich zunächst nur auf den Menschen bezieht.",
      "Denn in dem Augenblick, wo man in die tieferen Gründe der einzelnen Organe eindringt, wird man gewahr - wir werden im Laufe der Vorträge schon sehen, daß es so ist -, daß ein Organ eine ganz andere Aufgabe haben kann in seiner tieferen Bedeutung beim Menschen als ein ähnliches oder gleichartiges Organ in der tierischen Welt. Wer in der gewöhnlichen äußeren Wissen­schaft die Dinge betrachtet, wird sagen: Was du uns hier gesagt hast, kann man ja auch sagen in bezug auf die Säugetiere. - Aber, was über die Bedeutung der Organe in bezug auf den Menschen gesagt wird, das kann nicht, wenn man tiefer in die Sache dringt, in gleicher Weise für die Tiere gesagt werden, sondern die okkulte Wissenschaft hat die Aufgabe, die Tiere für sich zu betrachten und nachzusehen, ob dasselbe, was für den Menschen in bezug auf Rückenmark und Gehirn zu sagen ist, auch für die Tiere gilt.",
      "Denn daß die Tiere, die",
      "dem Menschen nahestehen, auch Rückenmark und Gehirn haben, das beweist noch nicht, daß diese Organe für Mensch und Tier dieselben Aufgaben haben, so wie man, um einen Vergleich zu gebrauchen, ein Messer in der Hand haben kann, um damit meinet­willen ein Kalb zu tranchieren oder auch um damit zu radieren. Beide Male hat man es mit einem Messer zu tun, und wer nur Rücksicht nimmt auf die Form des Messers, der wird glauben, daß es sich in beiden Fällen um dasselbe handelt. In derselben Lage wäre derjenige, welcher glaubt, weil sich bei Mensch und Tier dieselben Organe -Gehirn und Rückenmark - finden, so würden diese zu denselben Verrichtungen dienen. Das ist aber nicht wahr. Das ist etwas, was in der äußeren Wissenschaft gang und gäbe geworden ist und zu gewis­sen Ungenauigkeiten geführt hat und was nur wird korrigiert werden können, wenn sich die äußere Wissenschaft dazu bequemen wird, allmählich auf das einzugehen, was aus den Tiefen der übersinnlichen Forschung über die Charaktere der Wesenheiten gesagt werden kann.",
      "Wenn wir nun betrachten das Rückenmark auf der einen Seite, das Gehirn auf der anderen Seite, so werden wir leicht sehen, daß das eine gewisse Wahrheit hat, worauf denkende Naturbetrachter schon seit mehr als hundert Jahren aufmerksam gemacht haben. Es hat eine gewisse Richtigkeit zu sagen: Wenn man das Gehirn betrachtet, so sieht es gleichsam aus wie ein umgebildetes Rückenmark. - Das wird ja noch leichter begreiflich, wenn man sich daran erinnert, daß Goe­the, Oken und andere Naturbetrachter vor allen Dingen den Blick darauf gerichtet haben, daß die Schädelknochen gewisse Formälin­lichkeiten haben mit den Wirbelknochen des Rückgrates. Es war Goethe, der die Formähnlichkeiten der Organe aufmerksam betrach­tet hat, sehr früh in seinen Betrachtungen aufgefallen, daß, wenn man einzelne Wirbelknochen sich umgestaltet denkt, verflacht und aufge­trieben, daß man dann durch eine solche Umgestaltung der Wirbel­knochen zum Kopfknochen, zum Schädelknochen kommt. Gleich­sam dadurch, daß man einen Wirbelknochen nach allen Seiten auf-bläst, so daß er flach wird in seinen Ausdehnungen, wird man nach und nach aus einem Wirbelknochen die Form des Schädelknochens ableiten können. So kann man in einer gewissen Beziehung die Schädelknochen",
      "umgestaltete Wirbelknochen nennen. Geradeso nun, wie man die Schädelknochen, die das Gehirn umschließen, als umgebil­dete Wirbelknochen ansehen kann, so kann man sich die Masse des Rückenmarkes gleichsam aufgetrieben denken, differenzierter, kom­plizierter gemacht, und man bekommt aus dem Rückmark, gewisser­maßen durch Umwandlung, das Gehirn. So etwa, wie eine Pflanze, die zunächst nur grüne Blätter hat, diese umbildet, differenziert, um buntfarbige Blütenblätter hervorzubringen, wie also die Blüten diffe­renzierte Blätter sind, so können wir uns denken, daß durch Umge­staltung, durch Differenzierung der Form, durch Heraufheben des Rückenmarkes auf eine höhere Stufe, das Gehirn gebildet werden konnte. Man kann sich also vorstellen, daß wir in unserem Gehirn ein differenziertes Rückenmark sehen können.",
      "Nun schauen wir von diesem Gesichtspunkt aus uns die beiden Organe an. Welches dieser Organe müssen wir auf natürliche Weise als das jüngere betrachten? Das ist die Frage, die wir uns vorlegen mussen. Doch zweifellos nicht dasjenige, welches die abgeleitete Form zeigt, sondern das, welches die ursprüngliche Form hat. Das heißt, wir müssen uns denken, das Rückenmark steht auf einer ersten Stufe der Entwickelung, es ist jünger, und das Gehirn steht auf einer zweiten Stufe. Es hat zuerst die Stufe des Rückenmarkes durchge­macht, es ist ein verwandeltes Rückenmark und ist also als das ältere Organ zu betrachten. Mit anderen Worten, wenn wir diese neue Zweiheit, die uns am Menschen als Gehirn und Rückenmark entge­gentritt, ins Auge fassen, so können wir sagen: Es müssen alle Kräfte, die zur Gehirnbildung führten, ältere Kräfte sein, denn sie mussen auf einer früheren Stufe erst die Anlage zum Rückenmark gebildet haben und dann weitergewirkt haben zur Umbildung des Rücken­markes zum Gehirn. Es muß also gleichsam ein zweiter Ansatz gemacht worden sein in unserem Rückenmark, das als solches noch nicht so weit fortgeschritten ist, sondern eben stehengeblieben ist auf einer früheren Stufe der Entwickelung. Wir haben also, wenn wir uns jetzt pedantisch genau ausdrücken wollen, in dem Rückenmark-Nervensystem ein Rückenmark erster Ordnung zu sehen und in unserem Gehirn ein Rückenmark zweiter Ordnung, ein umgebildetes",
      "älteres Rückenmark, ein Rückenmark, das einmal ein solches war, aber zum Gehirn umgebildet worden ist.",
      "Damit haben wir zunächst in ganz genauer Weise auf das hinge­wiesen, was notwendig in Betracht zu ziehen ist, wenn wir die Organmassen, welche innerhalb dieser Knochenschutzhüllen einge­schlossen sind, sachgemäß ins Auge fassen wollen. Nun aber kommt etwas anderes in Betracht, was uns erst auf dem Felde des Okkultis­mus entgegentreten kann. Man kann eine Frage aufwerfen, nämlich:",
      "Wenn eine solche Umbildung stattfindet von einer Organanlage erster Stufe zu einer Organanlage zweiter Stufe, ist dann der Entwik­kelungsprozeß ein fortschreitender oder ein rückläufiger? Das heißt, kann es ein solcher Prozeß sein, der zu höheren Vollkommenheits­stufen eines Organes führt, oder aber ein solcher Prozeß, der das Organ zum Degenerieren, zum allmählichen Absterben bringt? -Betrachten wir ein Organ wie zum Beispiel unser Rückenmark.",
      "So wie es jetzt ist, so erscheint es uns als ein verhältnismäßig wenig fortgeschrittenes Organ, man könnte es als jung bezeichnen, denn es hat es noch nicht dahin gebracht, ein Gehirn zu werden. Wir können aber in zweifacher Weise über dieses Rückenmark denken.",
      "Einmal können wir uns denken, es habe in sich die Kräfte, auch einmal ein Gehirn zu werden, dann ist es in fortschreitender Entwickelung. Oder es habe gar nicht die Anlage dazu, diese zweite Stufe je zu erreichen, dann wäre es in absteigender Entwickelung, es würde in die Dekadenz gehen und bestimmt sein, die erste Stufe anzudeuten, jedoch nicht zur zweiten Stufe zu kommen.",
      "Wenn wir uns nun denken, daß unserem jetzigen Gehirn einmal ein Rückenmark zugrunde gelegen hat, so hat das damalige Rückenmark zweifellos fortschreitende Kräfte gehabt, denn es ist ja zum Gehirn geworden. Fragen wir uns aber jetzt nach unserem jetzigen Rückenmark, dann sagt uns die okkulte Betrachtungsweise: So wie unser Rückenmark heute ist, hat es in der Tat nicht in sich die Anlage zu einer fortschrei­tenden Entwickelung, sondern es bereitet sich vor, seine Entwicke­lung auf der gegenwärtigen Stufe abzuschließen. - Wenn ich mich grotesk ausdrücken darf: Der Mensch hat nicht zu glauben, daß er einmal sein Rückenmark, wie es heute ist in Form eines dünnen",
      "Stranges, so aufgeplustert haben wird wie das heutige Gehirn. Wir werden noch sehen, was der okkulten Betrachtung zugrunde liegt, um so etwas sagen zu können. Schon aus einem reinen Vergleiche der Form dieses Organes, des Rückenmarkes, wie es beim Menschen auftritt und wie beim Tiere, sehen Sie eine äußere Hindeutung auf das, was jetzt gesagt worden ist. Da sehen Sie, wenn Sie zum Beispiel eine Schlange nehmen, wie in unzähligen Ringen hinter dem Kopf das Rückgrat ansetzt, ausgefüllt ist vom Rückenmark und wie das Rückgrat in einer Art gebildet ist, die fast endlos so weiter verlaufen könnte. Beim Menschen sehen wir, wie das Rückenmark von der Stelle, wo es sich an das Gehirn ansetzt, nach unten zu verlaufend, in der Tat immer mehr und mehr sich zusammenschließt und nach unten hin immer undeutlicher und undeutlicher jene Bildung zeigt, die es in den oberen Partien aufweist. So kann auch durch die äußere Betrachtung schon auffallen, wie das, was sich bei der Schlange nach rückwärts fortsetzt, beim Menschen einem Abschluß, einer Art Degeneration zueilt. Das ist zunächst eine äußere vergleichende Betrachtungsweise. Wir werden sehen, wie sich die okkulte Betrach­tung ausnimmt.",
      "Wenn wir dies jetzt zusammenhalten, so dürfen wir sagen: Wir haben eingeschlossen in jenes Knochengebilde des Schädels ein Rük­kenmark, das in fortschreitender Bildung zum Gehirn geworden ist, das auf einer zweiten Stufe seiner Entwickelung steht. Und wir haben gleichsam noch einmal einen Versuch, ein solches Gehirn zu bilden in unserem Rückenmark, aber einen Versuch, der schon jetzt zeigt, daß er nicht gelingen wird.",
      "Sehen wir jetzt von dieser Betrachtung ab und gehen zu dem über, was wir auch wieder schon aus einer äußeren laienhaften Betrachtung kennen: zu den Aufgaben, die Gehirn und Rückenmark zu erfüllen haben. Es ist ja jedem mehr oder weniger bekannt, daß das Werkzeug für die sogenannten höheren Seelentätigkeiten das Gehirn ist, daß diese höheren Seelentätigkeiten von dem Organ des Gehirns dirigiert werden. Es ist weiterhin jedem bekannt, daß die mehr unbewußten Seelentätigkeiten vom Rückenmark und den sich anschließenden Nerven dirigiert werden, diejenigen Seelentätigkeiten nämlich, bei",
      "welchen zwischen dem äußeren Eindruck und der Handlung, die auf den äußeren Eindruck folgt, wenig Überlegung sich einschiebt. Wenn Sie zum Beispiel von einem Insekt in die Hand gestochen werden, ziehen Sie die Hand zurück, Sie zucken zurück; da schiebt sich zwischen Stich und Zurückziehen der Hand keine große Überle­gung ein.",
      "Diese Seelentätigkeiten werden mit Recht schon von der äußeren Wissenschaft so angesehen, daß ihnen als ihr Werkzeug das Rückenmark zugeteilt ist. Wir haben andere Seelentätigkeiten, bei denen sich zwischen den äußeren Eindruck und das, was zuletzt zur Handlung führt, eine reichere Überlegung einschiebt; diese haben ihr Organ im Gehirn.",
      "Denken Sie, um gleich ein markantes Beispiel zu nehmen, an einen Künstler, der die äußere Natur betrachtet, der seine Sinne anstrengt und unzählige Eindrücke sammelt; dann geht eine lange Zeit vorüber, in der er diese Eindrücke in seiner Seele verarbei­tet. Endlich, oft erst nach Jahren, geht er dazu über, das, was aus den äußeren Eindrücken in langer Seelentätigkeit geworden ist, durch äußere Handlungen zu fixieren.",
      "Da schiebt sich zwischen äußeren Eindruck und das, was durch den Menschen aus dem äußeren Ein­druck gemacht wird, eine reichere Seelentätigkeit ein. Dasselbe ist auch beim wissenschaftlichen Forscher der Fall, aber auch bei jedem Menschen, der sich die Dinge, die er tun will, überlegt und nicht wild darauflosstürzt wie ein Stier, wenn er rote Farbe sieht.",
      "Überall, wo der Mensch nicht aus einer Reflexbewegung handelt, sondern sich seine Handlungen überlegt, sprechen wir vom Gehirn als einem Werkzeug der Seelentätigkeit.",
      "Wenn wir noch tiefer auf diese Sache eingehen, werden wir uns fragen: Ja, wie zeigt sich denn diese unsere Seelentätigkeit, für welche wir das Gehirn als Werkzeug in Anspruch nehmen? Sie zeigt sich in zweifacher Art. Zunächst werden wir sie gewahr in unserem wachen Tagesleben. Was tun wir da? Wir sammeln durch die Sinne die äußeren Eindrücke und verarbeiten diese durch das Gehirn durch vernünftige Überlegung. Wir müssen uns vorstellen, daß die äußeren Eindrücke durch die Tore der Sinne in uns hineinwandern und gewisse Prozesse in unserem Gehirn anregen. Wenn wir hineinblik­ken könnten in das Gehirn und in das. was da geschieht, so würden",
      "wir sehen, wie unser Gehirn in Tätigkeit versetzt wird durch den sich hineinergießenden Strom der äußeren Eindrücke, und wir würden sehen, was aus diesen Eindrücken wird durch das, was die menschli­che Überlegung bewirkt. Wir würden dann sehen, wie sich hinzuge­sellen auch die weniger von Überlegung beeinflußten Folgen dieser Eindrücke, das heißt Taten und Handlungen, die wir mehr seinem Werkzeug, dem Rückenmark, zuzuschreiben haben.",
      "Jetzt müssen wir unsere Aufmerksamkeit richten auf die zwei Zustände, in welchen der heutige Mensch das ganze Leben hindurch abwechselnd lebt, das wache Tagesleben und das bewußtlose Schlaf-leben. Aus früheren Vorträgen ist es uns geläufig, daß am Tage die vier Wesensglieder des Menschen zusammen sind, während beim Schlafen Astralleib und Ich sich herausheben.",
      "Nun kennen wir alle jenen eigentümlichen Zustand, der sich mischt zwischen das wache Tagesleben und das bewußtlose Schlafleben: das Traumleben. Es soll zunächst in keiner anderen Weise über das Traumleben gesprochen werden als so, wie es der Laie beobachten kann.",
      "Wir sehen, daß das Traumleben eine merkwürdige Ähnlichkeit hat mit jener untergeord­neten Seelentätigkeit, die wir an das Rückenmark knüpfen. Denn wenn die Traumbilder auftreten in unserer Seele, treten sie nicht auf als Vorstellungen, die der Überlegung entspringen, sondern sie treten mit Notwendigkeit auf, ähnlich wie etwa die unwillkürliche Handbe­wegung auftritt, wenn wir eine Fliege verjagen, die sich auf unsere Hand setzt; als unmittelbare, notwendige Abwehrbewegung tritt da eine Handlung auf.",
      "Beim Traumleben ist es etwas anders; es kommt nicht zu einer Handlung, aber mit einer ebenso unmittelbaren Not­wendigkeit treten Bilder in unseren Seelenhorizont hinein. Aber so wenig, wie wir im wachen Tagesleben einen Überlegungseinfluß haben auf die Handbewegung, die wir machen, wenn sich eine Fliege auf unsere Hand setzt, ebensowenig haben wir einen Einfluß auf die chaotisch in uns auf- und abwogenden Traumbilder.",
      "Daher können wir sagen: Wenn wir einen Menschen im wachen Tagesleben erblik­ken und absehen von alle dem, was in ihm vorgeht, wenn wir nur seine Reflexbewegungen betrachten, alle Gesten und physiognomi­schen Ausdrücke, die er nur auf äußere Eindrücke hin, also ohne",
      "Überlegung vollbringt, so haben wir da eine Summe von solchen Handlungen vor uns, die aus Notwendigkeit beim Menschen eintre­ten. Erblicken wir dagegen einen träumenden Menschen, so sehen wir eine Summe von Bildern in das Wesen des Menschen hineinwir­ken, die jetzt nicht zu Handlungen führen, sondern nur Bildcharak­ter haben. Wie im wachen Tagesleben die ohne Überlegungen vor sich gehenden Handlungen des Menschen sich vollziehen, so erscheint im Menschen die Bilderwelt der chaotisch ineinander­wogenden Traumvorstellungen.",
      "Wenn wir nun hinblicken auf unser Gehirn und es auch ansehen wollen als ein Werkzeug des Traumbewußtseins, was müssen wir da tun? Wir müssen uns denken, daß in diesem Gehirn etwas drinnen ist, was sich in gewisser Weise ähnlich benimmt wie unser Rücken­mark, das zu den unbewußten Handlungen führt.",
      "Wir haben ja das Gehirn zunächst anzusehen als Werkzeug des wachen Seelenlebens, wo wir unsere überlegten Vorstellungen schaffen. Wir müßten nun finden, wie den Traumvorstellungen gleichsam ein geheimnisvolles Rückenmark zugrundeliegt, das wie eingepreßt im Gehirn sitzt, das es aber nicht zu Handlungen bringt, sondern nur zu Bildern.",
      "Wäh­rend unser Rückenmark es zu Handlungen bringt, wenn sie auch nicht durch Überlegung zustande kommen, bringt es das Gehirn in diesem Falle bloß zu Bildern. Es bleibt gewissermaßen auf halbem Wege stehen; es ist etwas im Gehirn wie eine geheimnisvolle Unter­lage für eine unbewußte Seelentätigkeit, das wie eine Art Einschiebsel mit dem Charakter des Rückenmarks sich vorstellen läßt.",
      "Könnten wir also nicht sagen: Die Traumwelt führt uns in merkwürdiger Weise dazu, geheimnisvoll hindeuten zu können auf jenes alte Rük­kenmark, das einst dem Gehirn zugrundelag? - Wenn wir unser Gehirn betrachten, wie es heute ausgebildet ist als Werkzeug des wachen Tageslebens, so ist es uns so bekannt, wie es erscheint, wenn wir es aus der Schädelhöhle herausnehmen. Aber es muß etwas darinnen eingeschlossen sein, das auftritt, wenn das wache Tagesle­ben ausgelöscht ist.",
      "Und das zeigt die okkulte Betrachtung, daß in dem Gehirn ein geheimnisvolles Rückenmark darinnen ist als das Werkzeug des Traumlebens (siehe Zeichnung S.24, schraffiert).",
      "Wenn wir es uns schematisch zeichnen wollen, könnten wir es so darstellen, daß in dem Gehirn der Vorstellungswelt des wachen Tageslebens ein für die äußere Wahrnehmung unsichtbares geheim­nisvolles altes Rückenmark liegt, das irgendwie da hineingeheimnißt",
      "# Bild s. 24",
      "ist. Ich will es zunächst ganz hypothetisch aussprechen, daß dieses Rückenmark dann in Tätigkeit kommt, wenn der Mensch schläft und träumt, und dann so tätig ist, wie es sich für ein Rückenmark schickt, nämlich so, daß es mit Notwendigkeit seine Wirkungen hervor­bringt. Aber weil es eingepreßt ist in das Gehirn, führt es nicht zu Handlungen, sondern zu bloßen Bildern, zu Bildhandlungen; denn wir handeln ja im Traume nur in Bildern. So hätten wir auch aus diesem eigentümlichen, sonderbaren chaotischen Leben heraus, das wir im Traume führen, Hinweise darauf, daß unserem Werkzeug des wachen Tageslebens, als welches wir mit Recht unser Gehirn betrachten, ein geheimnisvolles Organ zugrundeliegt, das vielleicht eine ältere Bildung ist, aus der es sich herausentwickelt hat. Wenn die Neubildung, das heutige Gehirn, schweigt, dann zeigt sich das, was das Gehirn einmal war; da zaubert dieses alte Rückenmark das her­aus, was es kann. Aber weil es eingeschlossen ist, bringt es dieses alte Rückenmark nicht zu Handlungen, sondern bloß zu Bildern.",
      "So also trennt uns die Betrachtung des Lebens selbst das Gehirn in zwei Stufen. Die Tatsache, daß wir träumen können, weist darauf hin, daß das Gehirn eine Entwicklung durchgemacht hat, in der es noch auf der Stufe des heutigen Rückenmarks stand, bevor es sich entwickelt hat zum Werkzeug des wachen Tageslebens. Wenn aber",
      "das wache Tagesleben schweigt, dann macht sich das alte Organ noch geltend.",
      "So haben wir durch das bisher Gesagte schon etwas Typisches gewonnen, das sich durch eine äußere Betrachtung der Formen schon nachweisen läßt: Das wache Tagesleben verhält sich zum Traumleben wie das ausgebildete Gehirn zum Rückenmark. Wenn wir nun fort­schreiten zu einer seherischen Betrachtung, können wir zu dem, was uns die Formbetrachtung geben kann, etwas hinzufügen. In welcher Weise das okkulte Schauen, das seherische Auge als Unterlage dienen kann für die ganz wesenhafte Betrachtung der menschlichen Natur und auf welche okkulte Forschung sich die Anschauungen über die im Schädel und in der Wirbelsäule eingeschlossenen Organe stützen, werden wir später noch sehen.",
      "Nun wissen wir ja aus früheren Betrachtungen, daß des Menschen sichtbarer Leib nur ein Teil der gesamten Wesenheit des Menschen ist. In dem Augenblick, wo sich das hellseherische Auge öffnet, macht man die Erfahrung, daß dieser physische Leib sich einge­schlossen, eingebettet zeigt in einen übersinnlichen Organismus, in das, was man, grob gesprochen, die menschliche Aura nennt. Es wird dies hier zunächst wie eine Tatsache angeführt, und wir werden später darauf zurückkommen, inwiefern sie sich rechtfertigen läßt. Diese menschliche Aura, in welcher der physische Mensch nur wie ein Kern drinnen ist, zeigt sich für das seherische Auge als ein Farbengebilde, in dem verschiedene Farben auf- und abfluten. Man darf sich aber nicht vorstellen, daß man diese Aura malen könnte. Man kann sie nicht mit gewöhnlichen Farben wiedergeben, denn die Farben der Aura sind in fortwährender Bewegung, in fortwährendem Entstehen und Vergehen begriffen. Jedes Bild, das man von ihr malen wollte, könnte nur annähernd richtig sein, so wie auch niemand einen Blitz richtig malen kann, es würde nur ein starres Gebilde werden. Wie man den Blitz nicht richtig malen kann, so kann man das noch weniger bei der Aura, denn die aurischen Farben sind ungemein labil und beweglich, sie entstehen und vergehen fortwährend.",
      "Nun ziehen sich die aurischen Farben in merkwürdigster Weise verschieden über den ganzen menschlichen Organismus hin; und es",
      "ist interessant, auf das aurische Bild hinzuweisen, das sich für das hellseherische Auge ergibt, wenn wir Schädeldecke und Rückgrat von rückwärts betrachten. Wenn wir uns den Teil der Aura vorstellen",
      "- von rückwärts betrachtet -, in den Schädel und Rückgrat, also Gehirn und Rückenmark, eingebettet sind, so zeigt sich, daß wir für den Teil der Aura, der zu den unteren Partien des Rückenmarks gehört, eine besonders deutliche Grundfarbe angeben können: er zeigt sich grünlich. Und wir können wiederum eine deutliche Farbe angeben, die in ihrer Art in keinem anderen Teile des Körpers zutage tritt, für die oberen Partien des Kopfes, wo das Gehirn ist: es ist eine Art Violettblau. Diese Farbe legt sich gleich einer Kappe oder einem Helm von rückwärts nach vorne über den Schädel.",
      "# Bild s. 26",
      "Unterhalb der violettblauen Partien sieht man in der Regel eine Nuance, von der Sie sich am ehesten eine Vorstellung machen kön­nen, wenn Sie sie mit der Farbe einer jungen Pfirsichblüte verglei­chen. Zwischen dieser Farbe und der grünlichen Farbe der unteren Teile des Rückgrats haben wir im mittleren Teil des Rückens andere, unbestimmte Farbnuancen, die außerordentlich schwer zu beschrei­ben sind, weil sie unter den gewöhnlichen, uns aus unserer sinnlichen Umwelt bekannten Farben nicht vorkommen. So schließt sich an das",
      "Grün eine Farbe an, die nicht grün, nicht blau und nicht gelb ist, sondern wie ein Gemisch von allen dreien; es zeigen sich Farben zwischen Gehirn und Rückgratende, die es im Grunde genommen innerhalb der physisch-sinnlichen Welt überhaupt nicht gibt. Wenn das nun auch schwierig zu beschreiben ist, so ist doch eines mit Bestimmtheit zu sagen, daß wir oben bei jenem sozusagen aufgebla­senen Rückenmark ein Violettblau haben und, hinuntergehend zum Ende des Rückgrates, zu einem deutlich grünlichen Farbton kommen.",
      "Wir haben also heute an eine rein äußere Betrachtung der mensch­lichen Gestalt einige Tatsachen angeknüpft, die nur die hellseherische Forschung lehrt. Morgen soll nun versucht werden, auch die anderen Teile des physischen Menschenleibes, die sich an die bereits bespro­chenen angliedern, in ihrer Zweiheit zu betrachten, damit wir dann weiter vorgehen können und sehen, wie die ganze menschliche Wesenheit sich uns darstellt."
    ],
    "sentences": [
      [
        "In diesem Vortragszyklus, der auf Veranlassung unserer Prager Freunde gehalten wird, soll ein Thema behandelt werden, welches dem Menschen ungeheuer naheliegt, weil es ja das genauere Wesen des Menschen unmittelbar berührt und von dem handelt, was sich auf sein physisches Leben selber bezieht.",
        "Wenn dieses Thema auch auf der einen Seite dem Menschen so naheliegt, weil es ihn ja selbst betrifft, so darf man doch sagen, daß es auf der anderen Seite ein sehr schwer zugängliches Thema ist."
      ],
      [
        "Denn schon der Blick auf die durch alle Zeiten, man möchte sagen, aus mystisch-okkulten Höhen an den Menschen dringende Forderung «Erkenne dich selbst» zeigt uns die Tatsache, daß Selbsterkenntnis, wirkliche, wahre Selbsterkenntnis, im Grunde genommen dem Menschen recht schwierig ist, und das bezieht sich nicht nur auf die individuelle, persönliche Selbsterkennt­nis, sondern vor allen Dingen auch auf die Erkenntnis der mensch­lichen Wesenheit überhaupt.",
        "Und weil der Mensch - wie man sehen kann aus dieser ewigen Forderung «Erkenne dich selbst» - sich selbst seiner Wesenheit nach so sehr fernsteht, einen so weiten Weg hat, um sich selbst zu verstehen, deshalb wird in einer gewissen Beziehung das, was Gegenstand der folgenden Betrachtungen dieser Tage wer­den wird, als etwas Fernliegendes erscheinen, zu dessen Verständnis sehr Verschiedenes notwendig ist."
      ],
      [
        "Nicht ohne Grund ging ich selbst erst nach längerer Zeit und reiflicher Überlegung daran, auch einmal über dieses Thema zu sprechen.",
        "Denn es ist ein Thema, demgegen­über - soll man zu einer wahren, wahrhaften Betrachtung kommen -etwas unbedingt notwendig ist, was bei einer gewöhnlichen wissen­schaftlichen Betrachtung so oft außer acht gelassen wird: Notwendig ist, daß man vor der Wesenheit des Menschen - wohlgemerkt, nicht vor der Wesenheit des einzelnen Menschen, insbesondere dann nicht, wenn dieser einzelne Mensch wir selber sind -, daß man vor dem Wesen des Menschen im allgemeinen Ehrfurcht habe."
      ],
      [
        "Und es muß als eine Grundbedingung für unsere folgenden Betrachtungen angesehen"
      ],
      [
        "werden, daß man Ehrfurcht habe vor dem, was die menschliche Wesenheit in Wahrheit bedeutet."
      ],
      [
        "Wie kann man denn davor wahrhafte Ehrfurcht haben?",
        "Auf keine andere Art, als daß man zunächst absieht von dem, wie der Mensch -ganz gleichgültig, ob wir selbst oder ein anderer - uns im alltäglichen Leben erscheint, und indem man sich aufschwingt zu der Anschau­ung: Dieser Mensch mit seiner gesamten Entwickelung ist nicht um seiner selbst willen da, er ist da zur Offenbarung des Geistes, der ganzen Welt des Göttlich-Geistigen, er ist eine Offenbarung der Weltengottheit, des Weltengeistes."
      ],
      [
        "Und für diejenigen, die erkennen, daß alles, was uns umgibt, Ausdruck ist für göttlich-geistige Kräfte, für die ist es auch möglich, diese Ehrfurcht zu empfinden, nicht nur für das Göttlich-Geistige selbst, sondern auch für die Offenbarungen dieses Göttlich-Geistigen.",
        "Und wenn wir davon sprechen, daß der Mensch nach immer vollkommenerer Selbsterkenntnis trachte, so sollen wir uns darüber klar sein, daß nicht bloß Neugierde, meinet-willen auch Wißbegierde, uns veranlassen soll, nach Selbsterkenntnis zu streben, sondern daß wir es als Pflicht empfinden müssen, die Erkenntnis der Offenbarungen des Weltengeistes durch den Men­schen immer vollkommener und vollkommener zu gestalten."
      ],
      [
        "In die­sem Sinne sind die Worte zu verstehen: Unwissend zu bleiben, wo Erkenntnis möglich ist, bedeutet eine Versündigung gegen die göttli­che Bestimmung des Menschen.",
        "Denn der Weltengeist hat in uns die Kraft gelegt, wissend zu werden; und wenn wir nicht erkennend werden wollen, so lehnen wir es ab - was wir eigentlich nicht dürf­ten -, eine Offenbarung des Weltengeistes zu sein, und stellen immer mehr und mehr nicht eine Offenbarung des Weltengeistes dar, son­dern eine Karikatur, ein Zerrbild von ihm."
      ],
      [
        "Es ist unsere Pflicht, nach Erkenntnis zu streben, um immer mehr und mehr ein Bild des Weltengeistes zu werden.",
        "Erst wenn wir mit diesen Worten einen Sinn verbinden können, «ein Bild des Weltengeistes zu werden», erst wenn es uns bedeutungsvoll wird, in diesem Sinne zu sagen: Wir müssen erkennen, es ist unsere Pflicht zu erkennen -, erst dann können wir das vorhin geforderte Gefühl von Ehrfurcht gegenüber der Wesenheit des Menschen so recht empfinden."
      ],
      [
        "Und für den, der"
      ],
      [
        "im okkulten Sinne das Leben des Menschen, das Wesen des Men­schen betrachten will, für den ist diese Durchdringung mit Ehrfurcht vor der menschlichen Natur schon deshalb eine unbedingte Notwen­digkeit, weil diese Durchdringung mit Ehrfurcht einzig und allein geeignet ist, unsere geistigen Augen und unsere geistigen Ohren, unser ganzes geistiges Schauvermögen wachzurufen, das heißt dieje­nigen Kräfte, die uns eindringen lassen in die geistigen Untergründe der menschlichen Natur.",
        "Wer als Seher, als Geistesforscher nicht im höchsten Grade Ehrfurcht haben könnte vor der menschlichen Natur, wer sich nicht durchdringen kann bis in die innersten Fibern seiner Seele mit dem Gefühl von Ehrfurcht gegenüber der Menschen-natur, dem Abbild des Geistes, dem bliebe das Auge, wenn es noch so geöffnet ist für diese oder jene geistigen Geheimnisse der Welt, verschlossen für alles das, was sich auf die eigentlich tiefere Wesen­heit des Menschen selber bezieht.",
        "Und es mag viele Hellseher geben, welche dieses oder jenes schauen können in dem geistigen Umkreis unseres Daseins: Wenn ihnen diese Ehrfurcht fehlt, dann fehlt ihnen das Vermögen, in die Tiefen der menschlichen Natur hineinzu­schauen, und sie werden nichts Richtiges über das zu sagen wissen, was des Menschen Wesenheit ist."
      ],
      [
        "Man nennt ja die Lehre von den Lebensvorgängen des Menschen «Physiologie».",
        "Diese Lehre soll hier nicht in der Weise betrachtet werden, wie es in der äußeren Wissenschaft geschieht, sondern so, wie sie dem geistigen Auge sich darbietet, so daß wir von den äußeren Gestaltungen des Menschen, von der Form und den Lebensvorgän­gen seiner Organe immer hinblicken auf die geistige, übersinnliche Grundlage der Organe, der Lebensformen, der Lebensprozesse.",
        "Und da nicht die Absicht besteht, diese «okkulte Physiologie», wie man auch sagen könnte, in irgendeiner unsachlichen Weise hier zu treiben, so wird es notwendig sein, daß in einer gewissen unbefangenen Weise an manchen Stellen Hindeutungen gemacht werden auf Dinge, wel­che dem mehr oder weniger Außenstehenden am Anfang recht unwahrscheinlich klingen werden.",
        "Es muß ausdrücklich betont wer­den, daß dieser Vortragszyklus, noch mehr als mancher andere, den ich gehalten habe, ein Ganzes bildet und daß aus einzelnen Vorträgen,"
      ],
      [
        "insbesondere aus den Anfangsvorträgen, nichts aus dem Zusam­menhang herausgerissen beurteilt werden kann, weil manches unbe­fangen wird gesagt werden müssen.",
        "Und erst, wenn man die Schluß-vorträge gehört haben wird, wird man sich ein Urteil bilden können über das, was eigentlich gesagt werden soll.",
        "Denn das Thema wird hier in einer etwas anderen Weise behandelt werden als in der äuße­ren Physiologie.",
        "Die Anfangsgründe werden sich auch bestätigen durch das, was uns zuletzt entgegentreten wird.",
        "Wir werden sozu­sagen nicht eine gerade Linie vom Anfang bis zum Ende zu be­schreiben haben, sondern wir werden in einer Kreislinie vorgehen, so daß wir am Ende dort wieder ankommen, von wo wir ausgegan­gen sind."
      ],
      [
        "Eine Betrachtung des Menschen soll es sein, was hier dargeboten wird.",
        "Zunächst tritt uns dieser Mensch für die äußeren Sinne seiner äußeren Form nach entgegen.",
        "Wir wissen ja, daß zu dem, was zunächst die reine äußere laienhafte Betrachtung über den Menschen wissen kann, heute schon sehr vieles kommt, was die Wissenschaft hinzuerforscht hat.",
        "Daher müssen wir das, was wir in äußerer Weise, aus der äußeren Erfahrung und Beobachtung über den Menschen heute wissen können, notwendigerweise zusammenstellen aus dem, was schon der Laie an sich und an anderen Menschen zu beobachten in der Lage ist, und dem, was der Wissenschaft gelungen ist zu erforschen, welche durch bewunderungswürdige Methoden, durch bewunderungswürdige Instrumente zu ihren Resultaten über die Leiblichkeit des Menschen kommt."
      ],
      [
        "Wenn man alles zusammenhält, was man als Laie rein äußerlich am Menschen sehen kann, was man vielleicht auch schon aus irgendwel­chen populären Beschreibungen kennengelernt hat, dann wird es vielleicht nicht unverständlich sein, wenn darauf aufmerksam gemacht wird, daß schon die äußere Gestalt des Menschen, wie sie uns in der Außenwelt entgegentritt, aus einer Zweiheit besteht.",
        "Für den, der in die Tiefen der Menschennatur eindringen will, ist es durchaus notwendig, sich bewußt zu werden, daß schon der äußere Mensch seiner Form und Gestaltung nach im Grunde genommen eine Zweiheit darstellt."
      ],
      [
        "Das eine, das wir am Menschen deutlich unterscheiden können, ist alles das, was sich als eingeschlossen erweist in Organe, die den größtmöglichen Schutz gegen die Außenwelt gewähren.",
        "Es ist alles das, was wir zählen können zum Bereich des Gehirns und des Rük­kenmarkes.",
        "Alles, was in dieser Beziehung zur menschlichen Natur gehört, zu Gehirn und Rückenmark, ist fest umschlossen von siche­ren, Schutz gewährenden Knochengebilden.",
        "Wenn wir schematisch darstellen wollen, was zu diesen beiden Bereichen gehört, so können wir uns das in folgender Weise veranschaulichen: Wenn a (siehe Zeichnung) schematisch darstellt die Summe der übereinandergelagerten"
      ],
      [
        "# Bild s. 15"
      ],
      [
        "Wirbelknochen, die längs des Rückenmarkes verlaufen, b die Schädeldecke und die Schädelknochen, so ist eingeschlossen inner­halb des Kanales, der gebildet wird durch die übereinandergelagerten Wirbelknochen sowie durch die Knochen des Schädels, alles, was in den Bereich des Gehirns und des Rückenmarkes gehört.",
        "Man kann den Menschen nicht betrachten, ohne sich bewußt zu werden, daß alles, was in diesen Bereich gehört, im Grunde genommen eine in sich geschlossene Ganzheit bildet und daß alles übrige vom Menschen, das wir in verschiedenster Weise physiologisch angliedern können -Hals, Rumpf, Gliedmaßengebilde -, mit Gehirn und Rückenmark in Verbindung steht durch, bildlich gesprochen, mehr oder weniger fadenförmige oder bandförmige Gebilde.",
        "Diese müssen erst die"
      ],
      [
        "Schutzhülle durchbrechen, damit eine Verbindung hergestellt werden kann mit dem innerhalb dieser Knochengebilde eingeschlossenen Teil.",
        "So können wir sagen: Es erweist sich schon einer oberflächli­chen Betrachtung gegenüber alles, was am Menschen ist, als eine Zweiheit; das eine liegt innerhalb der charakterisierten Knochen-gebilde in festen und sicheren Schutzhüllen, das andere außerhalb derselben."
      ],
      [
        "Nun müssen wir zunächst einen ganz oberflächlichen Blick auf das werfen, was innerhalb dieser Knochengebilde liegt.",
        "Da können wir wieder leicht unterscheiden zwischen jener großen Masse, die in die Schädelknochen eingebettet ist als Gehirn, und dem anderen Teil, der wie ein Stiel oder Strang daranhängt, der in organischer Verbindung mit dem Gehirn steht und sich wie eine Art fadenförmiger Auswuchs desselben in den Rückgratkanal hineinstreckt, das Rückenmark."
      ],
      [
        "Wenn wir diese zwei Gebilde voneinander unterscheiden, dann müs­sen wir schon auf etwas aufmerksam machen, worauf die äußere Wissenschaft nicht aufmerksam zu machen braucht, worauf aber die okkulte Wissenschaft, die in die Tiefe des Wesens der Dinge einzu­dringen hat, wohl aufmerksam machen muß.",
        "Es muß darauf auf­merksam gemacht werden, daß alles, was wir auf dem Boden einer Betrachtung über den Menschen sagen, sich zunächst nur auf den Menschen bezieht."
      ],
      [
        "Denn in dem Augenblick, wo man in die tieferen Gründe der einzelnen Organe eindringt, wird man gewahr - wir werden im Laufe der Vorträge schon sehen, daß es so ist -, daß ein Organ eine ganz andere Aufgabe haben kann in seiner tieferen Bedeutung beim Menschen als ein ähnliches oder gleichartiges Organ in der tierischen Welt.",
        "Wer in der gewöhnlichen äußeren Wissen­schaft die Dinge betrachtet, wird sagen: Was du uns hier gesagt hast, kann man ja auch sagen in bezug auf die Säugetiere. - Aber, was über die Bedeutung der Organe in bezug auf den Menschen gesagt wird, das kann nicht, wenn man tiefer in die Sache dringt, in gleicher Weise für die Tiere gesagt werden, sondern die okkulte Wissenschaft hat die Aufgabe, die Tiere für sich zu betrachten und nachzusehen, ob dasselbe, was für den Menschen in bezug auf Rückenmark und Gehirn zu sagen ist, auch für die Tiere gilt."
      ],
      [
        "Denn daß die Tiere, die"
      ],
      [
        "dem Menschen nahestehen, auch Rückenmark und Gehirn haben, das beweist noch nicht, daß diese Organe für Mensch und Tier dieselben Aufgaben haben, so wie man, um einen Vergleich zu gebrauchen, ein Messer in der Hand haben kann, um damit meinet­willen ein Kalb zu tranchieren oder auch um damit zu radieren.",
        "Beide Male hat man es mit einem Messer zu tun, und wer nur Rücksicht nimmt auf die Form des Messers, der wird glauben, daß es sich in beiden Fällen um dasselbe handelt.",
        "In derselben Lage wäre derjenige, welcher glaubt, weil sich bei Mensch und Tier dieselben Organe -Gehirn und Rückenmark - finden, so würden diese zu denselben Verrichtungen dienen.",
        "Das ist aber nicht wahr.",
        "Das ist etwas, was in der äußeren Wissenschaft gang und gäbe geworden ist und zu gewis­sen Ungenauigkeiten geführt hat und was nur wird korrigiert werden können, wenn sich die äußere Wissenschaft dazu bequemen wird, allmählich auf das einzugehen, was aus den Tiefen der übersinnlichen Forschung über die Charaktere der Wesenheiten gesagt werden kann."
      ],
      [
        "Wenn wir nun betrachten das Rückenmark auf der einen Seite, das Gehirn auf der anderen Seite, so werden wir leicht sehen, daß das eine gewisse Wahrheit hat, worauf denkende Naturbetrachter schon seit mehr als hundert Jahren aufmerksam gemacht haben.",
        "Es hat eine gewisse Richtigkeit zu sagen: Wenn man das Gehirn betrachtet, so sieht es gleichsam aus wie ein umgebildetes Rückenmark. - Das wird ja noch leichter begreiflich, wenn man sich daran erinnert, daß Goe­the, Oken und andere Naturbetrachter vor allen Dingen den Blick darauf gerichtet haben, daß die Schädelknochen gewisse Formälin­lichkeiten haben mit den Wirbelknochen des Rückgrates.",
        "Es war Goethe, der die Formähnlichkeiten der Organe aufmerksam betrach­tet hat, sehr früh in seinen Betrachtungen aufgefallen, daß, wenn man einzelne Wirbelknochen sich umgestaltet denkt, verflacht und aufge­trieben, daß man dann durch eine solche Umgestaltung der Wirbel­knochen zum Kopfknochen, zum Schädelknochen kommt.",
        "Gleich­sam dadurch, daß man einen Wirbelknochen nach allen Seiten auf-bläst, so daß er flach wird in seinen Ausdehnungen, wird man nach und nach aus einem Wirbelknochen die Form des Schädelknochens ableiten können.",
        "So kann man in einer gewissen Beziehung die Schädelknochen"
      ],
      [
        "umgestaltete Wirbelknochen nennen.",
        "Geradeso nun, wie man die Schädelknochen, die das Gehirn umschließen, als umgebil­dete Wirbelknochen ansehen kann, so kann man sich die Masse des Rückenmarkes gleichsam aufgetrieben denken, differenzierter, kom­plizierter gemacht, und man bekommt aus dem Rückmark, gewisser­maßen durch Umwandlung, das Gehirn.",
        "So etwa, wie eine Pflanze, die zunächst nur grüne Blätter hat, diese umbildet, differenziert, um buntfarbige Blütenblätter hervorzubringen, wie also die Blüten diffe­renzierte Blätter sind, so können wir uns denken, daß durch Umge­staltung, durch Differenzierung der Form, durch Heraufheben des Rückenmarkes auf eine höhere Stufe, das Gehirn gebildet werden konnte.",
        "Man kann sich also vorstellen, daß wir in unserem Gehirn ein differenziertes Rückenmark sehen können."
      ],
      [
        "Nun schauen wir von diesem Gesichtspunkt aus uns die beiden Organe an.",
        "Welches dieser Organe müssen wir auf natürliche Weise als das jüngere betrachten?",
        "Das ist die Frage, die wir uns vorlegen mussen.",
        "Doch zweifellos nicht dasjenige, welches die abgeleitete Form zeigt, sondern das, welches die ursprüngliche Form hat.",
        "Das heißt, wir müssen uns denken, das Rückenmark steht auf einer ersten Stufe der Entwickelung, es ist jünger, und das Gehirn steht auf einer zweiten Stufe.",
        "Es hat zuerst die Stufe des Rückenmarkes durchge­macht, es ist ein verwandeltes Rückenmark und ist also als das ältere Organ zu betrachten.",
        "Mit anderen Worten, wenn wir diese neue Zweiheit, die uns am Menschen als Gehirn und Rückenmark entge­gentritt, ins Auge fassen, so können wir sagen: Es müssen alle Kräfte, die zur Gehirnbildung führten, ältere Kräfte sein, denn sie mussen auf einer früheren Stufe erst die Anlage zum Rückenmark gebildet haben und dann weitergewirkt haben zur Umbildung des Rücken­markes zum Gehirn.",
        "Es muß also gleichsam ein zweiter Ansatz gemacht worden sein in unserem Rückenmark, das als solches noch nicht so weit fortgeschritten ist, sondern eben stehengeblieben ist auf einer früheren Stufe der Entwickelung.",
        "Wir haben also, wenn wir uns jetzt pedantisch genau ausdrücken wollen, in dem Rückenmark-Nervensystem ein Rückenmark erster Ordnung zu sehen und in unserem Gehirn ein Rückenmark zweiter Ordnung, ein umgebildetes"
      ],
      [
        "älteres Rückenmark, ein Rückenmark, das einmal ein solches war, aber zum Gehirn umgebildet worden ist."
      ],
      [
        "Damit haben wir zunächst in ganz genauer Weise auf das hinge­wiesen, was notwendig in Betracht zu ziehen ist, wenn wir die Organmassen, welche innerhalb dieser Knochenschutzhüllen einge­schlossen sind, sachgemäß ins Auge fassen wollen.",
        "Nun aber kommt etwas anderes in Betracht, was uns erst auf dem Felde des Okkultis­mus entgegentreten kann.",
        "Man kann eine Frage aufwerfen, nämlich:"
      ],
      [
        "Wenn eine solche Umbildung stattfindet von einer Organanlage erster Stufe zu einer Organanlage zweiter Stufe, ist dann der Entwik­kelungsprozeß ein fortschreitender oder ein rückläufiger?",
        "Das heißt, kann es ein solcher Prozeß sein, der zu höheren Vollkommenheits­stufen eines Organes führt, oder aber ein solcher Prozeß, der das Organ zum Degenerieren, zum allmählichen Absterben bringt? -Betrachten wir ein Organ wie zum Beispiel unser Rückenmark."
      ],
      [
        "So wie es jetzt ist, so erscheint es uns als ein verhältnismäßig wenig fortgeschrittenes Organ, man könnte es als jung bezeichnen, denn es hat es noch nicht dahin gebracht, ein Gehirn zu werden.",
        "Wir können aber in zweifacher Weise über dieses Rückenmark denken."
      ],
      [
        "Einmal können wir uns denken, es habe in sich die Kräfte, auch einmal ein Gehirn zu werden, dann ist es in fortschreitender Entwickelung.",
        "Oder es habe gar nicht die Anlage dazu, diese zweite Stufe je zu erreichen, dann wäre es in absteigender Entwickelung, es würde in die Dekadenz gehen und bestimmt sein, die erste Stufe anzudeuten, jedoch nicht zur zweiten Stufe zu kommen."
      ],
      [
        "Wenn wir uns nun denken, daß unserem jetzigen Gehirn einmal ein Rückenmark zugrunde gelegen hat, so hat das damalige Rückenmark zweifellos fortschreitende Kräfte gehabt, denn es ist ja zum Gehirn geworden.",
        "Fragen wir uns aber jetzt nach unserem jetzigen Rückenmark, dann sagt uns die okkulte Betrachtungsweise: So wie unser Rückenmark heute ist, hat es in der Tat nicht in sich die Anlage zu einer fortschrei­tenden Entwickelung, sondern es bereitet sich vor, seine Entwicke­lung auf der gegenwärtigen Stufe abzuschließen. - Wenn ich mich grotesk ausdrücken darf: Der Mensch hat nicht zu glauben, daß er einmal sein Rückenmark, wie es heute ist in Form eines dünnen"
      ],
      [
        "Stranges, so aufgeplustert haben wird wie das heutige Gehirn.",
        "Wir werden noch sehen, was der okkulten Betrachtung zugrunde liegt, um so etwas sagen zu können.",
        "Schon aus einem reinen Vergleiche der Form dieses Organes, des Rückenmarkes, wie es beim Menschen auftritt und wie beim Tiere, sehen Sie eine äußere Hindeutung auf das, was jetzt gesagt worden ist.",
        "Da sehen Sie, wenn Sie zum Beispiel eine Schlange nehmen, wie in unzähligen Ringen hinter dem Kopf das Rückgrat ansetzt, ausgefüllt ist vom Rückenmark und wie das Rückgrat in einer Art gebildet ist, die fast endlos so weiter verlaufen könnte.",
        "Beim Menschen sehen wir, wie das Rückenmark von der Stelle, wo es sich an das Gehirn ansetzt, nach unten zu verlaufend, in der Tat immer mehr und mehr sich zusammenschließt und nach unten hin immer undeutlicher und undeutlicher jene Bildung zeigt, die es in den oberen Partien aufweist.",
        "So kann auch durch die äußere Betrachtung schon auffallen, wie das, was sich bei der Schlange nach rückwärts fortsetzt, beim Menschen einem Abschluß, einer Art Degeneration zueilt.",
        "Das ist zunächst eine äußere vergleichende Betrachtungsweise.",
        "Wir werden sehen, wie sich die okkulte Betrach­tung ausnimmt."
      ],
      [
        "Wenn wir dies jetzt zusammenhalten, so dürfen wir sagen: Wir haben eingeschlossen in jenes Knochengebilde des Schädels ein Rük­kenmark, das in fortschreitender Bildung zum Gehirn geworden ist, das auf einer zweiten Stufe seiner Entwickelung steht.",
        "Und wir haben gleichsam noch einmal einen Versuch, ein solches Gehirn zu bilden in unserem Rückenmark, aber einen Versuch, der schon jetzt zeigt, daß er nicht gelingen wird."
      ],
      [
        "Sehen wir jetzt von dieser Betrachtung ab und gehen zu dem über, was wir auch wieder schon aus einer äußeren laienhaften Betrachtung kennen: zu den Aufgaben, die Gehirn und Rückenmark zu erfüllen haben.",
        "Es ist ja jedem mehr oder weniger bekannt, daß das Werkzeug für die sogenannten höheren Seelentätigkeiten das Gehirn ist, daß diese höheren Seelentätigkeiten von dem Organ des Gehirns dirigiert werden.",
        "Es ist weiterhin jedem bekannt, daß die mehr unbewußten Seelentätigkeiten vom Rückenmark und den sich anschließenden Nerven dirigiert werden, diejenigen Seelentätigkeiten nämlich, bei"
      ],
      [
        "welchen zwischen dem äußeren Eindruck und der Handlung, die auf den äußeren Eindruck folgt, wenig Überlegung sich einschiebt.",
        "Wenn Sie zum Beispiel von einem Insekt in die Hand gestochen werden, ziehen Sie die Hand zurück, Sie zucken zurück; da schiebt sich zwischen Stich und Zurückziehen der Hand keine große Überle­gung ein."
      ],
      [
        "Diese Seelentätigkeiten werden mit Recht schon von der äußeren Wissenschaft so angesehen, daß ihnen als ihr Werkzeug das Rückenmark zugeteilt ist.",
        "Wir haben andere Seelentätigkeiten, bei denen sich zwischen den äußeren Eindruck und das, was zuletzt zur Handlung führt, eine reichere Überlegung einschiebt; diese haben ihr Organ im Gehirn."
      ],
      [
        "Denken Sie, um gleich ein markantes Beispiel zu nehmen, an einen Künstler, der die äußere Natur betrachtet, der seine Sinne anstrengt und unzählige Eindrücke sammelt; dann geht eine lange Zeit vorüber, in der er diese Eindrücke in seiner Seele verarbei­tet.",
        "Endlich, oft erst nach Jahren, geht er dazu über, das, was aus den äußeren Eindrücken in langer Seelentätigkeit geworden ist, durch äußere Handlungen zu fixieren."
      ],
      [
        "Da schiebt sich zwischen äußeren Eindruck und das, was durch den Menschen aus dem äußeren Ein­druck gemacht wird, eine reichere Seelentätigkeit ein.",
        "Dasselbe ist auch beim wissenschaftlichen Forscher der Fall, aber auch bei jedem Menschen, der sich die Dinge, die er tun will, überlegt und nicht wild darauflosstürzt wie ein Stier, wenn er rote Farbe sieht."
      ],
      [
        "Überall, wo der Mensch nicht aus einer Reflexbewegung handelt, sondern sich seine Handlungen überlegt, sprechen wir vom Gehirn als einem Werkzeug der Seelentätigkeit."
      ],
      [
        "Wenn wir noch tiefer auf diese Sache eingehen, werden wir uns fragen: Ja, wie zeigt sich denn diese unsere Seelentätigkeit, für welche wir das Gehirn als Werkzeug in Anspruch nehmen?",
        "Sie zeigt sich in zweifacher Art.",
        "Zunächst werden wir sie gewahr in unserem wachen Tagesleben.",
        "Was tun wir da?",
        "Wir sammeln durch die Sinne die äußeren Eindrücke und verarbeiten diese durch das Gehirn durch vernünftige Überlegung.",
        "Wir müssen uns vorstellen, daß die äußeren Eindrücke durch die Tore der Sinne in uns hineinwandern und gewisse Prozesse in unserem Gehirn anregen.",
        "Wenn wir hineinblik­ken könnten in das Gehirn und in das. was da geschieht, so würden"
      ],
      [
        "wir sehen, wie unser Gehirn in Tätigkeit versetzt wird durch den sich hineinergießenden Strom der äußeren Eindrücke, und wir würden sehen, was aus diesen Eindrücken wird durch das, was die menschli­che Überlegung bewirkt.",
        "Wir würden dann sehen, wie sich hinzuge­sellen auch die weniger von Überlegung beeinflußten Folgen dieser Eindrücke, das heißt Taten und Handlungen, die wir mehr seinem Werkzeug, dem Rückenmark, zuzuschreiben haben."
      ],
      [
        "Jetzt müssen wir unsere Aufmerksamkeit richten auf die zwei Zustände, in welchen der heutige Mensch das ganze Leben hindurch abwechselnd lebt, das wache Tagesleben und das bewußtlose Schlaf-leben.",
        "Aus früheren Vorträgen ist es uns geläufig, daß am Tage die vier Wesensglieder des Menschen zusammen sind, während beim Schlafen Astralleib und Ich sich herausheben."
      ],
      [
        "Nun kennen wir alle jenen eigentümlichen Zustand, der sich mischt zwischen das wache Tagesleben und das bewußtlose Schlafleben: das Traumleben.",
        "Es soll zunächst in keiner anderen Weise über das Traumleben gesprochen werden als so, wie es der Laie beobachten kann."
      ],
      [
        "Wir sehen, daß das Traumleben eine merkwürdige Ähnlichkeit hat mit jener untergeord­neten Seelentätigkeit, die wir an das Rückenmark knüpfen.",
        "Denn wenn die Traumbilder auftreten in unserer Seele, treten sie nicht auf als Vorstellungen, die der Überlegung entspringen, sondern sie treten mit Notwendigkeit auf, ähnlich wie etwa die unwillkürliche Handbe­wegung auftritt, wenn wir eine Fliege verjagen, die sich auf unsere Hand setzt; als unmittelbare, notwendige Abwehrbewegung tritt da eine Handlung auf."
      ],
      [
        "Beim Traumleben ist es etwas anders; es kommt nicht zu einer Handlung, aber mit einer ebenso unmittelbaren Not­wendigkeit treten Bilder in unseren Seelenhorizont hinein.",
        "Aber so wenig, wie wir im wachen Tagesleben einen Überlegungseinfluß haben auf die Handbewegung, die wir machen, wenn sich eine Fliege auf unsere Hand setzt, ebensowenig haben wir einen Einfluß auf die chaotisch in uns auf- und abwogenden Traumbilder."
      ],
      [
        "Daher können wir sagen: Wenn wir einen Menschen im wachen Tagesleben erblik­ken und absehen von alle dem, was in ihm vorgeht, wenn wir nur seine Reflexbewegungen betrachten, alle Gesten und physiognomi­schen Ausdrücke, die er nur auf äußere Eindrücke hin, also ohne"
      ],
      [
        "Überlegung vollbringt, so haben wir da eine Summe von solchen Handlungen vor uns, die aus Notwendigkeit beim Menschen eintre­ten.",
        "Erblicken wir dagegen einen träumenden Menschen, so sehen wir eine Summe von Bildern in das Wesen des Menschen hineinwir­ken, die jetzt nicht zu Handlungen führen, sondern nur Bildcharak­ter haben.",
        "Wie im wachen Tagesleben die ohne Überlegungen vor sich gehenden Handlungen des Menschen sich vollziehen, so erscheint im Menschen die Bilderwelt der chaotisch ineinander­wogenden Traumvorstellungen."
      ],
      [
        "Wenn wir nun hinblicken auf unser Gehirn und es auch ansehen wollen als ein Werkzeug des Traumbewußtseins, was müssen wir da tun?",
        "Wir müssen uns denken, daß in diesem Gehirn etwas drinnen ist, was sich in gewisser Weise ähnlich benimmt wie unser Rücken­mark, das zu den unbewußten Handlungen führt."
      ],
      [
        "Wir haben ja das Gehirn zunächst anzusehen als Werkzeug des wachen Seelenlebens, wo wir unsere überlegten Vorstellungen schaffen.",
        "Wir müßten nun finden, wie den Traumvorstellungen gleichsam ein geheimnisvolles Rückenmark zugrundeliegt, das wie eingepreßt im Gehirn sitzt, das es aber nicht zu Handlungen bringt, sondern nur zu Bildern."
      ],
      [
        "Wäh­rend unser Rückenmark es zu Handlungen bringt, wenn sie auch nicht durch Überlegung zustande kommen, bringt es das Gehirn in diesem Falle bloß zu Bildern.",
        "Es bleibt gewissermaßen auf halbem Wege stehen; es ist etwas im Gehirn wie eine geheimnisvolle Unter­lage für eine unbewußte Seelentätigkeit, das wie eine Art Einschiebsel mit dem Charakter des Rückenmarks sich vorstellen läßt."
      ],
      [
        "Könnten wir also nicht sagen: Die Traumwelt führt uns in merkwürdiger Weise dazu, geheimnisvoll hindeuten zu können auf jenes alte Rük­kenmark, das einst dem Gehirn zugrundelag? - Wenn wir unser Gehirn betrachten, wie es heute ausgebildet ist als Werkzeug des wachen Tageslebens, so ist es uns so bekannt, wie es erscheint, wenn wir es aus der Schädelhöhle herausnehmen.",
        "Aber es muß etwas darinnen eingeschlossen sein, das auftritt, wenn das wache Tagesle­ben ausgelöscht ist."
      ],
      [
        "Und das zeigt die okkulte Betrachtung, daß in dem Gehirn ein geheimnisvolles Rückenmark darinnen ist als das Werkzeug des Traumlebens (siehe Zeichnung S.24, schraffiert)."
      ],
      [
        "Wenn wir es uns schematisch zeichnen wollen, könnten wir es so darstellen, daß in dem Gehirn der Vorstellungswelt des wachen Tageslebens ein für die äußere Wahrnehmung unsichtbares geheim­nisvolles altes Rückenmark liegt, das irgendwie da hineingeheimnißt"
      ],
      [
        "# Bild s. 24"
      ],
      [
        "ist.",
        "Ich will es zunächst ganz hypothetisch aussprechen, daß dieses Rückenmark dann in Tätigkeit kommt, wenn der Mensch schläft und träumt, und dann so tätig ist, wie es sich für ein Rückenmark schickt, nämlich so, daß es mit Notwendigkeit seine Wirkungen hervor­bringt.",
        "Aber weil es eingepreßt ist in das Gehirn, führt es nicht zu Handlungen, sondern zu bloßen Bildern, zu Bildhandlungen; denn wir handeln ja im Traume nur in Bildern.",
        "So hätten wir auch aus diesem eigentümlichen, sonderbaren chaotischen Leben heraus, das wir im Traume führen, Hinweise darauf, daß unserem Werkzeug des wachen Tageslebens, als welches wir mit Recht unser Gehirn betrachten, ein geheimnisvolles Organ zugrundeliegt, das vielleicht eine ältere Bildung ist, aus der es sich herausentwickelt hat.",
        "Wenn die Neubildung, das heutige Gehirn, schweigt, dann zeigt sich das, was das Gehirn einmal war; da zaubert dieses alte Rückenmark das her­aus, was es kann.",
        "Aber weil es eingeschlossen ist, bringt es dieses alte Rückenmark nicht zu Handlungen, sondern bloß zu Bildern."
      ],
      [
        "So also trennt uns die Betrachtung des Lebens selbst das Gehirn in zwei Stufen.",
        "Die Tatsache, daß wir träumen können, weist darauf hin, daß das Gehirn eine Entwicklung durchgemacht hat, in der es noch auf der Stufe des heutigen Rückenmarks stand, bevor es sich entwickelt hat zum Werkzeug des wachen Tageslebens.",
        "Wenn aber"
      ],
      [
        "das wache Tagesleben schweigt, dann macht sich das alte Organ noch geltend."
      ],
      [
        "So haben wir durch das bisher Gesagte schon etwas Typisches gewonnen, das sich durch eine äußere Betrachtung der Formen schon nachweisen läßt: Das wache Tagesleben verhält sich zum Traumleben wie das ausgebildete Gehirn zum Rückenmark.",
        "Wenn wir nun fort­schreiten zu einer seherischen Betrachtung, können wir zu dem, was uns die Formbetrachtung geben kann, etwas hinzufügen.",
        "In welcher Weise das okkulte Schauen, das seherische Auge als Unterlage dienen kann für die ganz wesenhafte Betrachtung der menschlichen Natur und auf welche okkulte Forschung sich die Anschauungen über die im Schädel und in der Wirbelsäule eingeschlossenen Organe stützen, werden wir später noch sehen."
      ],
      [
        "Nun wissen wir ja aus früheren Betrachtungen, daß des Menschen sichtbarer Leib nur ein Teil der gesamten Wesenheit des Menschen ist.",
        "In dem Augenblick, wo sich das hellseherische Auge öffnet, macht man die Erfahrung, daß dieser physische Leib sich einge­schlossen, eingebettet zeigt in einen übersinnlichen Organismus, in das, was man, grob gesprochen, die menschliche Aura nennt.",
        "Es wird dies hier zunächst wie eine Tatsache angeführt, und wir werden später darauf zurückkommen, inwiefern sie sich rechtfertigen läßt.",
        "Diese menschliche Aura, in welcher der physische Mensch nur wie ein Kern drinnen ist, zeigt sich für das seherische Auge als ein Farbengebilde, in dem verschiedene Farben auf- und abfluten.",
        "Man darf sich aber nicht vorstellen, daß man diese Aura malen könnte.",
        "Man kann sie nicht mit gewöhnlichen Farben wiedergeben, denn die Farben der Aura sind in fortwährender Bewegung, in fortwährendem Entstehen und Vergehen begriffen.",
        "Jedes Bild, das man von ihr malen wollte, könnte nur annähernd richtig sein, so wie auch niemand einen Blitz richtig malen kann, es würde nur ein starres Gebilde werden.",
        "Wie man den Blitz nicht richtig malen kann, so kann man das noch weniger bei der Aura, denn die aurischen Farben sind ungemein labil und beweglich, sie entstehen und vergehen fortwährend."
      ],
      [
        "Nun ziehen sich die aurischen Farben in merkwürdigster Weise verschieden über den ganzen menschlichen Organismus hin; und es"
      ],
      [
        "ist interessant, auf das aurische Bild hinzuweisen, das sich für das hellseherische Auge ergibt, wenn wir Schädeldecke und Rückgrat von rückwärts betrachten.",
        "Wenn wir uns den Teil der Aura vorstellen"
      ],
      [
        "- von rückwärts betrachtet -, in den Schädel und Rückgrat, also Gehirn und Rückenmark, eingebettet sind, so zeigt sich, daß wir für den Teil der Aura, der zu den unteren Partien des Rückenmarks gehört, eine besonders deutliche Grundfarbe angeben können: er zeigt sich grünlich.",
        "Und wir können wiederum eine deutliche Farbe angeben, die in ihrer Art in keinem anderen Teile des Körpers zutage tritt, für die oberen Partien des Kopfes, wo das Gehirn ist: es ist eine Art Violettblau.",
        "Diese Farbe legt sich gleich einer Kappe oder einem Helm von rückwärts nach vorne über den Schädel."
      ],
      [
        "# Bild s. 26"
      ],
      [
        "Unterhalb der violettblauen Partien sieht man in der Regel eine Nuance, von der Sie sich am ehesten eine Vorstellung machen kön­nen, wenn Sie sie mit der Farbe einer jungen Pfirsichblüte verglei­chen.",
        "Zwischen dieser Farbe und der grünlichen Farbe der unteren Teile des Rückgrats haben wir im mittleren Teil des Rückens andere, unbestimmte Farbnuancen, die außerordentlich schwer zu beschrei­ben sind, weil sie unter den gewöhnlichen, uns aus unserer sinnlichen Umwelt bekannten Farben nicht vorkommen.",
        "So schließt sich an das"
      ],
      [
        "Grün eine Farbe an, die nicht grün, nicht blau und nicht gelb ist, sondern wie ein Gemisch von allen dreien; es zeigen sich Farben zwischen Gehirn und Rückgratende, die es im Grunde genommen innerhalb der physisch-sinnlichen Welt überhaupt nicht gibt.",
        "Wenn das nun auch schwierig zu beschreiben ist, so ist doch eines mit Bestimmtheit zu sagen, daß wir oben bei jenem sozusagen aufgebla­senen Rückenmark ein Violettblau haben und, hinuntergehend zum Ende des Rückgrates, zu einem deutlich grünlichen Farbton kommen."
      ],
      [
        "Wir haben also heute an eine rein äußere Betrachtung der mensch­lichen Gestalt einige Tatsachen angeknüpft, die nur die hellseherische Forschung lehrt.",
        "Morgen soll nun versucht werden, auch die anderen Teile des physischen Menschenleibes, die sich an die bereits bespro­chenen angliedern, in ihrer Zweiheit zu betrachten, damit wir dann weiter vorgehen können und sehen, wie die ganze menschliche Wesenheit sich uns darstellt."
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ZWEITER VORTRAG Prag, 21. März 1911",
    "paragraphs": [
      "Wir werden zwar innerhalb dieser Betrachtungen immer wieder in die Schwierigkeit versetzt werden, den äußeren menschlichen Orga­nismus genauer ins Auge zu fassen, um sozusagen das Vergängliche, das Zerbrechliche zu erkennen. Aber wir werden auch sehen, daß gerade dieser Weg uns führen wird zu einer Erkenntnis des Bleiben­den, des Unvergänglichen, des Ewigen in der menschlichen Natur. Allerdings ist es notwendig, wenn unsere Betrachtungen dieses Ziel haben sollen, daß wir das streng einhalten, was gestern schon in der Einleitung bemerkt worden ist: den Gesichtspunkt, den äußeren physischen Organismus in aller Ehrfurcht als eine Offenbarung aus geistigen Welten zu betrachten.",
      "Wenn wir uns schon einigermaßen mit geisteswissenschaftlichen Begriffen und Empfindungen durchdrungen haben, können wir uns ja sehr leicht in den Gedanken hineinfinden, daß der menschliche Organismus in seiner ungeheuren Kompliziertheit der bedeutsamste Ausdruck, die größte und bedeutendste Offenbarung der Kräfte sein muß, die als geistige Kräfte die Welt durchweben und durchleben. Wir werden allerdings sozusagen vom Äußeren immer mehr und mehr in das Innere aufzusteigen haben.",
      "Wir haben gestern schon gesehen, wie uns die äußerliche Betrach­tung sowohl des Laien als auch der Wissenschaft dazu führen muß, den Menschen gewissermaßen als eine Zweiheit anzusehen. Wir haben diese Zweiheit der menschlichen Wesenheit gestern schon flüchtig charakterisiert - wir werden darauf noch genauer einzugehen haben -, und wir haben dasjenige an der menschlichen Wesenheit genauer betrachtet, was eingeschlossen ist in die schützende Kno­chenhülle des Schädels und der Rückenwirbel. Dabei haben wir gesehen, wie wir, wenn wir ausgehen von der äußeren Gestaltung und Form dieses Teils des Menschen, schon einen vorläufigen Aus­blick gewinnen können in den Zusammenhang desjenigen Lebens, das wir unser waches Tagesleben nennen, mit jenem anderen,",
      "zunächst für uns natürlich sehr von Zweifeln durchwobenen Leben, das wir das Traumleben nennen. Wir haben gesehen, daß schon die äußeren Formen des charakterisierten Teiles der Menschennatur eine Art Abbild geben, eine Art Offenbarung bedeuten: auf der einen Seite des Traumlebens, dieses chaotischen Bilderlebens, und auf der anderen Seite des mit scharf umrissener Beobachtung ausgestatteten wachen Tageslebens. Heute werden wir zunächst einen flüchtigen Blick zu werfen haben auf das andere Glied der menschlichen Zwei­heit, das sich gewissermaßen außerhalb des Bereiches befindet, den wir gestern ins Auge gefaßt haben. Schon der alleroberflächlichste Blick auf diesen zweiten Teil der menschlichen Wesenheit kann uns darüber belehren, daß dieser in gewisser Beziehung das entgegenge­setzte Bild dessen zeigt, was wir bei Gehirn und Rückenmark ins Auge gefaßt haben. Gehirn und Rückenmark sind von Knochenbil­dungen als schützender Hülle umschlossen. Betrachten wir den ande­ren Teil der menschlichen Natur, so müssen wir entschieden sagen, daß wir hier die Knochenbildung mehr in den Organismus hineinge-gliedert finden. Doch das wäre nur eine ganz oberflächliche Betrach­tung. Tiefer hinein in das Gefüge dieses anderen Teiles der Men­schennatur werden wir schon geführt, wenn wir die bedeutendsten Organsysteme auseinanderhalten und sie zunächst äußerlich verglei­chen mit dem, was wir gestern kennengelernt haben.",
      "Diejenigen Organsysteme, Werkzeugsysteme des menschlichen Organismus, welche dabei zuerst in Betracht kommen werden, sollen sein der Ernährungsapparat und alles das, was zwischen dem Ernäh­rungsapparat und jenem wunderbaren Gebilde liegt, das wir unschwer wie eine Art Mittelpunkt der ganzen menschlichen Orga­nisation empfinden können, dem Herzen. Da zeigt uns gleich der oberflächliche Blick, daß der Ernährungsapparat - wie man ihn im populären Sinne nennen kann - dazu bestimmt ist, die Stoffe unserer äußeren irdischen Umwelt aufzunehmen und für die weitere Verar­beitung im physischen Organismus des Menschen vorzubereiten. Wir wissen, daß dieser Verdauungsapparat zunächst von unserem Munde aus röhrenförmig zu dem Organ sich erstreckt, das jeder als den Magen kennt. Und schon eine oberflächliche Betrachtung lehrt",
      "uns, daß von jenen Nahrungsmitteln, die durch diesen Kanal in den Magen eingeführt werden, gewissermaßen unverwendete Teile ein­fach abgesondert werden, während andere Teile von den weiteren Verdauungsorganen in den menschlichen Leibesorganismus überge­führt werden. Es ist ja auch wohl bekannt, daß an den eigentlichen Verdauungsapparat im engeren Sinne sich das anschließt, was wir das Lymphsystem nennen - ich will jetzt zunächst nur schematisch spre­chen -, um die vom Verdauungsapparat hineingelieferten Nahrungs­stoffe in verwandeltem Zustande aufzunehmen.",
      "So daß wir sagen können, daß an den Verdauungsapparat, soweit er sich an den Magen angliedert, ein Organsystem sich anschließt, das Lymphsystem, als eine Summe von Kanälen, die durch den ganzen Körper gehen, ein System, welches das übernimmt, was durch den Verdauungsapparat verarbeitet ist, und die umgewandelten Stoffe abliefert an das Blut. Und dann haben wir das dritte Glied der Menschennatur, das Blutge­fäßsystem selber mit seinen weiteren oder engeren Röhren, wie es sich durch den ganzen menschlichen Organismus zieht und das zum Mittelpunkte seines ganzen Wirkens das Herz hat.",
      "Wir wissen ja, daß vom Herzen diejenigen bluterfüllten Gefäße ausgehen, die wir die Arterien nennen, und daß diese nach allen Teilen unseres Organis­mus das sogenannte rote Blut hinführen. Das Blut macht einen gewissen Prozeß in den einzelnen Gliedern des menschlichen Orga­nismus durch, wird dann wiederum zurückgeführt durch andere Gefäße, die Venen, die es aber jetzt in verändertem, verwandeltem Zustande als sogenanntes blaues Blut zu dem Herzen zurückbringen.",
      "Wir wissen auch, daß dieses verwandelte, unbrauchbar gewordene Blut von dem Herzen in die Lunge geleitet wird, daß es dort in Berührung kommt mit dem von außen aufgenommenen Sauerstoff der Luft, daß es dadurch erneuert und dann wiederum in Venen zum Herzen zurückgeleitet wird, um von neuem den Umlauf durch den ganzen menschlichen Organismus zu beginnen.",
      "Um diese komplizierten Systeme zu betrachten, wollen wir uns, damit wir in der äußeren Betrachtungsweise gleich eine Grundlage haben für die okkulte Betrachtungsweise, zunächst an dasjenige System halten, das von vornherein jedem als das eigentliche Mittelpunktsystem",
      "des ganzen menschlichen Organismus erscheinen muß:",
      "das Blut-Herzsystem. Wir wollen dabei zunächst ins Auge fassen, wie das Blut, nachdem es als verbrauchtes Blut in der Lunge aufge­frischt ist, also aus dem sogenannten blauen Blut wieder in rotes Blut verwandelt worden ist, wieder zum Herzen zurückkehrt und dann vom Herzen als rotes Blut wiederum ausströmt in den Organismus, um hier verwendet zu werden. (Es wird an die Tafel gezeichnet.) Beachten Sie, daß alles, was ich hier zeichne, nur ganz schematisch ist.",
      "Rufen wir uns kurz ins Gedächtnis, daß das menschliche Herz ein Organ ist, das eigentlich aus vier Gliedern zunächst besteht, aus vier Kammern, die durch Innenwände so abgegrenzt sind, daß man unter­scheiden kann zwei größere Räume nach unten gelegen und zwei kleinere nach oben gelegen, die beiden unteren die beiden Herzkam­mern, wie man sie gewöhnlich nennt, während die oberen die Vor-kammern genannt werden. Ich will heute noch nicht von den Herz-klappen sprechen, sondern den Gang der wichtigsten Organtätigkei­ten ganz schematisch ins Auge fassen.",
      "Da zeigt sich zunächst, daß das Blut, nachdem es aus der linken Vorkammer in die linke Herzkam­mer geströmt ist, durch eine große Schlagader abfließt und von da aus in den ganzen Organismus geleitet wird. Nun wollen wir ins Auge fassen, daß dieses Blut zunächst in alle einzelnen Organe des Orga­nismus sich verteilt, daß es dann im Organismus verbraucht wird, wodurch es in das sogenannte blaue Blut verwandelt wird und als solches wieder zum Herzen in die rechte Vorkammer zurückkehrt, von dort in die rechte Herzkammer fließt, um von hier aus wieder in die Lunge zu gehen, wieder erneuert zu werden und den Gang durch den Organismus von neuem zu machen.",
      "Wenn wir uns dies vorstellen, so ist es zur Grundlage einer okkul­ten Betrachtungsweise wichtig zu bedenken, daß sehr früh von der Hauptschlagader eine Nebenströmung abgeht, welche ins Gehirn führt, die oberen Organe des Menschen versorgt und von dort als verbrauchtes Blut wieder zurückfließt in die rechte Vorkammer, und daß es als das Gehirn passiert habendes Blut ebenso verwandelt wird wie das Blut, das aus den übrigen Gliedern des Organismus kommt. Wir haben also einen kleineren Nebenkreislauf des Blutes, in welchen",
      "# Bild s.032",
      "das Gehirn eingeschaltet ist, abgetrennt von dem anderen, großen Kreislauf, der den ganzen übrigen Organismus versorgt. Nun ist es außerordentlich wichtig, daß wir gerade diese Tatsache ins Auge fassen. Denn wir bekommen eine richtige Vorstellung, die uns eine Grundlage geben kann für alles, was uns möglich machen wird, in die okkulten Höhen hinaufzusteigen, nur dann, wenn wir uns die Frage stellen: Ist denn - in ähnlicher Weise, wie in den kleinen Blutkreislauf die oberen Organe eingeschaltet sind, namentlich das Gehirn - in den großen Blutkreislauf, der den übrigen Organismus versorgt, etwas ähnliches eingeschaltet? - Da kommen wir in der Tat zu dem Ergeb­nis, das schon die äußere oberflächliche Betrachtungsweise liefern kann, daß in den großen Blutkreislauf zunächst das Organ eingeschaltet",
      "ist, welches wir die Milz nennen, daß weiter darin einge­schaltet ist die Leber und jenes Organ, welches die von der Leber zubereitete Galle enthält. Diese Organe sind alle in den großen Blutkreislauf eingeschaltet.",
      "Wenn wir jetzt nach der Aufgabe dieser Organe fragen, so gibt uns die äußere Wissenschaft darauf die Antwort, daß die Leber die Galle bereitet, daß die Galle über die Gallenwege abfließt in den Verdau­ungskanal und an der Verarbeitung der Nahrungsmittel so mitwirkt, daß diese dann aufgenommen werden können vom Lymphsystem und übergeleitet werden können in das Blut. Weniger Genaues sagt die äußere Wissenschaft über die Milz.",
      "Wenn wir diese Organe betrachten, haben wir nun zunächst den Blick darauf zu richten, daß dieselben sich sozusagen zu beschäftigen haben mit der Umwandlung der Nahrung für den menschlichen Organismus, daß aber auf der anderen Seite alle drei Organe eingeschaltet sind in den großen Blut­kreislauf. In diesen sind sie nun nicht umsonst eingeschaltet.",
      "Denn insofern die Nahrungsstoffe aufgenommen werden in das Blut, um durch das Blut dem menschlichen Organismus zugeführt zu werden und demselben die Baustoffe fortwährend zu ersetzen, da beteiligen sich diese drei Organe an der notwendigen Verarbeitung der Nah­rungsstoffe. Es ist nun die Frage: Können wir aus einer äußeren Beobachtung schon entnehmen, wie sich diese drei Organe an der Gesamttätigkeit des menschlichen Organismus beteiligen? - Richten wir dazu den Blick zunächst auf eine Äußerlichkeit, darauf, daß diese Organe so eingeschaltet sind in den unteren Blutkreislauf, wie das Gehirn in den oberen Kreislauf eingeschaltet ist; und fragen wir einmal - wenn wir uns zunächst wirklich an diese äußerliche Betrach­tungsweise halten, die später vertieft werden soll -, ob diese Organe möglicherweise eine ähnliche, eine verwandte Aufgabe haben könn­ten wie das Gehirn oder überhaupt wie die höhergelegenen Teile des menschlichen Organismus.",
      "Worin könnte diese Aufgabe bestehen?",
      "Betrachten wir einmal diese höheren Teile des menschlichen Orga­nismus; es sind ja die Organe, welche die äußeren Sinneseindrücke aufnehmen und das Material unserer Sinneswahrnehmung verarbei­ten. Daher können wir sagen: Was im menschlichen Haupt, in den",
      "oberen Partien des menschlichen Organismus geschieht, das ist Ver­arbeitung der Außenwelt, Verarbeitung jener Eindrücke, die von außen durch die Sinnesorgane einfließen. Die wesentlichen Ursachen für das, was in den oberen Partien des Menschen geschieht, haben wir zu sehen in den äußeren Impressionen, in den äußeren Eindrücken.",
      "Indem diese äußeren Eindrücke ihre Wirkungen hineinsenden in die oberen Organe des menschlichen Organismus, verändern sie das Blut oder tragen jedenfalls dazu bei und senden dieses Blut ebenso verän­dert zum Herzen zurück, wie aus dem übrigen Organismus das Blut verändert zum Herzen zurückgesandt wird. Liegt es nun nicht nahe, daran zu denken, daß das, was durch das Tor der Sinnesorgane von der Außenwelt in den oberen Teil des menschlichen Organismus hereinwirkt, in gewisser Weise demjenigen entspricht, was aus den im Innern gelegenen Organen - Milz, Leber, Galle - heraus wirkt?",
      "Der obere Teil des menschlichen Organismus schließt sich nach außen auf, um die Wirkungen der Außenwelt zu empfangen, und während das Blut nach oben strömt, um diese Eindrücke der Außen­welt aufzunehmen, strömt es nach unten, um dasjenige aufzuneh­men, was von den unteren Organen kommt. Wie wir gesagt haben, werden von der Umwelt durch die Sinne Wirkungen auf unsere obere Organisation ausgeübt.",
      "Denken wir uns dies einmal zusammengezo­gen, zusammengepreßt in einem Zentrum, so können wir darin etwas Analoges sehen zu dem, was durch Leber, Galle und Milz bewirkt wird: Umwandlung von Stoffen, die der Außenwelt entnommen sind. Wenn wir näher darauf eingehen, werden Sie sehen, daß das keine so ganz absonderliche Betrachtungsweise ist.",
      "Denken Sie sich die verschiedenen hereinfließenden Sinnesein­drücke der Außenwelt wie zusammengezogen, gleichsam zu Orga­nen verdichtet, ins Innere des Menschen verlegt und eingeschaltet in das Blut, so bietet sich der obere Teil des menschlichen Organismus dem Blute ebenso dar, wie sich von innen die Organe Leber, Galle, Milz dem Blute darbieten. Also wir haben die Außenwelt, die oben unsere Sinne umgibt, gleichsam in Organe zusammengedrängt und ins Innere des Menschen verlegt, so daß wir sagen können: Einmal berührt uns die Welt von außen, sie strömt durch die Sinnesorgane in",
      "unseren oberen Organismus ein und wirkt auf unser Blut, und einmal wirkt auf geheimnisvolle Weise die Welt von innen in Organen, in die sich erst zusammengezogen hat, was draußen im Makrokosmos vor­geht, und wirkt da entgegen unserem Blut, das sich ihm ebenso darbietet. Wenn wir das schematisch zeichnen wollten, könnten wir also sagen: Denken wir uns auf der einen Seite die Welt, von allen Seiten wirkend auf die Sinne, und das Blut, wie eine Tafel den Eindrücken der Außenwelt sich darbietend, so haben wir unsere",
      "# Bild s. 35",
      "obere Organisation. Denken wir uns jetzt, wir könnten diese ganze Welt zusammenziehen, in einzelne Organe zusammenziehen, einen Extrakt dieser Welt bilden, und könnten ihn in das Innere herein verlegen, so daß gewissermaßen die ganze Welt auf die andere Seite des Blutes wirkt, dann hätten wir ein schematisches Bild des Außen und des Innen des menschlichen Organismus in einer ganz sonder­baren Weise geformt. So könnten wir in einer gewissen Weise schon sagen: Es entspricht das Gehirn eigentlich unserer Innenorganisa­tion; insoweit sie Brust- und Bauchhöhle ausfüllt, ist gleichsam die Außenwelt in unser Inneres verlegt.",
      "Schon in dieser Organisation, die wir ja als eine untergeordnete erkennen, die hauptsächlich der Fortführung des Ernährungsprozes­ses dient, haben wir etwas so Geheimnisvolles wie eine Zusammenfü­gung der ganzen Außenwelt in eine Summe von inneren Organen, von inneren Werkzeugen. Und wenn wir nun diese Organe Leber,",
      "Galle, Milz einmal näher betrachten, können wir sagen: Zunächst ist es die Milz, die sich der Blutströmung darbietet. Die Milz ist ein sonderbares Organ, in der in blutreiche Gewebe eingebettet ist eine ganze Summe von kleinen Körnchen, die sich gegenüber der übrigen Gewebemasse weiß ausnehmen. Wenn wir das Blut im Verhältnis zur Milz betrachten, erscheint uns die Milz wie ein Sieb, durch welches das Blut hindurchgeht, um sich einem solchen Organ darzubieten, das in gewisser Weise ein zusammengeschrumpfter Teil des Makro-kosmos ist. Als nächste Stufe sehen wir dann, wie sich das Blut der Leber darbietet und wie die Leber ihrerseits die Galle absondert, die in einem besonderen Organ aufbewahrt wird, dann in die Nahrungs­stoffe übergeht und von dort aus mit den verwandelten Nahrungs-stoffen in das Blut gelangt.",
      "Dieses innere Sichdarbieten des Blutes an die drei Organe können wir uns nicht anders als in folgender Weise vorstellen: Das erste Organ, das sich dem Blut entgegenstellt, ist die Milz, das zweite die Leber, und das dritte, das eigentlich ein sehr kompliziertes Verhältnis schon zum gesamten Blutsystem hat, ist die Galle. Weil die Galle den Nahrungsstoffen dargeboten wird und an der Verarbeitung derselben beteiligt ist, wird sie als besonderes Organ gezählt. Aus bestimmten Gründen haben die Okkultisten aller Zeiten diesen Organen gewisse Namen gegeben. Ich bitte Sie nun recht sehr, vorläufig bei diesen Na­men, die diesen Organen gegeben sind, an nichts Besonderes zu den­ken und davon abzusehen, daß diese Namen noch etwas anderes in der großen Welt bedeuten. Wir werden später noch sehen, warum ge­rade diese Namen genommen wurden. Weil die Milz sich dem Blut zu­erst darbietet - so können wir rein äußerlich vergleichsweise sagen -, erschien sie den alten Okkultisten am besten mit jenem Namen bezeichnet, der dem Stern zukommt, der sich im Weltenraum zuerst im Sonnensystem darbietet; deshalb nannten sie die Milz Saturnus oder einen inneren Saturn im Menschen. In ähnlicher Weise nannten sie die Leber einen inneren Jupiter und die Galle einen inneren Mars. Wollen wir zunächst bei diesen Namen uns gar nichts anderes den­ken, als daß wir sie aus dem Grunde wählen, weil wir die Anschau­ung gewonnen haben, zunächst hypothetisch, daß die äußeren Welten,",
      "die sonst unseren Sinnen zugänglich sind, zusammengezogen sind in diesen Organen und uns gleichsam als innere Welten entge­gentreten, wie uns äußerliche Welten in den Planeten entgegentreten. Wir würden aber jetzt schon sagen können: Wie die äußeren Welten unseren Sinnen erscheinen, indem sie von außen eindringen und auf das Blut wirken, so erscheinen uns die Innenwelten wirksam auf das Blut, indem sie dasselbe ebenfalls beeinflussen.",
      "Wir werden nun allerdings einen bedeutungsvollen Unterschied finden zwischen dem, was wir gestern besprochen haben als Eigen­tümlichkeiten des menschlichen Gehirns, und dem, was wie eine Art inneres Weltensystem auf unser Blut wirkt. Dieser Unterschied liegt einfach darin, daß der Mensch zunächst nichts von dem weiß, was sich innerhalb seines unteren Organismus abspielt; das heißt, er weiß nichts von den Eindrücken, welche die innere Welt - gleichsam die inneren Planeten - auf ihn machen, wogegen es ja gerade charakteri­stisch ist, daß die äußeren Welten auf sein Bewußtsein ihre Eindrücke machen. In einer gewissen Beziehung dürfen wir also diese innere Welt als die Welt des Unbewußten bezeichnen gegenüber der bewuß­ten Welt, welche wir im Gehirnleben kennengelernt haben.",
      "Nun wird sich uns gerade das, was in diesem Bewußten und Unbewußten liegt, dadurch näher aufklären, daß wir etwas anderes zu Hilfe nehmen. Sie wissen alle, daß die äußere Wissenschaft davon spricht, daß das Nervensystem das Organ des Bewußtseins ist mit allem, was dazugehört. Nun müssen wir als Grundlage für unsere okkulten Betrachtungen eine gewisse Beziehung ins Auge fassen, die das Nervensystem zum Blutsystem hat, das heißt zu dem, was wir ja heute schematisch ins Auge gefaßt haben. Da sehen wir, daß unser Nervensystem überall in gewisse Beziehungen tritt zu unserem Blut-system, daß das Blut überall an unser Nervensystem herandringt. Dabei müssen wir nun zunächst auf das Rücksicht nehmen, was die äußere Wissenschaft diesbezüglich für etwas Ausgemachtes hält. Sie hält das für ausgemacht, daß im Nervensystem der gesamte Regulator liege aller Bewußtseinstätigkeit, alles dessen, was wir als bewußtes Seelenleben bezeichnen. Wir können nicht umhin - zunächst auch nur andeutungsweise, um es später zu belegen -, uns zum Bewußtsein",
      "zu bringen, daß das Nervensystem für den Okkultisten nur wie eine Art von Grundlage des Bewußtseins dasteht. Denn gerade so, wie sich in unseren Organismus eingliedert das Nervensystem und berührt wird oder wenigstens in einem gewissen Verhältnis steht zum Blutsystem, so gliedert sich in die Gesamtwesenheit des Menschen dasjenige ein, was wir nennen des Menschen astralischen Leib und des Menschen Ich.",
      "Und schon eine äußerliche Betrachtung kann uns zeigen - und ich habe ja öfter in meinen Vorträgen darüber gespro­chen -, daß das Nervensystem in einer gewissen Weise eine Offenba­rung des Astralleibes ist und das Blut eine Offenbarung des Ich. Wenn wir in die unbelebte Natur gehen, so sehen wir ja, wie wir den Gesteinen, Mineralien und so weiter nur einen physischen Leib zuzuschreiben haben in den Teilen, die sie uns darbieten.",
      "Wenn wir dann von den unbelebten, unorganischen Naturkörpern zu den belebten Naturkörpern aufsteigen zu den Organismen, so müssen wir uns denken, daß diese Organismen durchsetzt sind von dem sogenannten Ätherleib oder Lebensleib, der in sich die Ursachen der Lebenserscheinungen enthält. Wir werden später schon sehen, daß die Geisteswissenschaft von diesem Äther- oder Lebensleib nicht so spricht, wie die äußere Wissenschaft von einer spekulativen Lebenskraft gesprochen hat.",
      "Wenn die Geisteswissenschaft vom Ätherleibe spricht, spricht sie von etwas, was das geistige Auge wirklich sieht, also von einem Realen, das dem äußeren, physischen Leibe zugrundeliegt. Wenn wir die Pflanzen betrachten, müssen wir ihnen einen Ätherleib zuschreiben.",
      "Steigen wir hinauf von den Pflan­zen zu den empfindenden Wesen, den Tieren, so ist es das Element des Empfindens, des inneren Erlebens, welches das Tier von der Pflanze unterscheidet. Wenn wir uns nun fragen, was muß sich eingliedern dem tierischen Organismus, damit er hinaufgehoben wer­den kann von den bloßen Lebensvorgängen zu Empfindungen, die die Pflanzen noch nicht haben, so ist die Antwort: Soll die bloße Lebenstätigkeit, die sich noch nicht verinnerlichen kann, noch nicht zur Empfindung entzünden kann, sich zur Empfindung, zum inner­lichen Erleben entzünden können, so muß sich in den tierischen Organismus eingliedern der Astralleib.",
      "Und in dem Nervensystem,",
      "das die Pflanzen noch nicht haben, müssen wir den äußeren Aus­druck, das Werkzeug des Astralleibes sehen. Der Astralleib ist das geistige Urbild des Nervensystems. Wie das Urbild zu seiner Offen­barung, zu seinem Abbild, so verhält sich der Astralleib zu dem Nervensystem.",
      "Wenn wir nun mit unserer Betrachtung beim Menschen einset­zen - und ich habe schon gestern gesagt, daß wir es im Okkultismus nicht so gut haben wie die äußere wissenschaftliche Betrachtungs­weise, daß wir nicht sozusagen alles durcheinanderwerfen können -, dann müssen wir, wenn wir die menschlichen Organe betrachten, uns immer bewußt sein, daß diese Organe oder Organsysteme zu etwas gebraucht werden können, wozu die analogen Organsysteme im tierischen Organismus, wenn sie auch ähnlich ausschauen, nicht gebraucht werden können. Beim Menschen müssen wir das Blut als äußeres Werkzeug für das Ich ansehen, für alles, was wir als unser innerstes Seelenzentrum, das Ich, bezeichnen.",
      "So haben wir im Ner­vensystem ein äußeres Werkzeug des Astralleibes und in unserem Blut ein äußeres Werkzeug des Ich. Geradeso wie das Nervensystem im Organismus in gewisse Beziehungen tritt zum Blut, so treten diejenigen inneren Seelengebilde, die wir als unsere Vorstellungen, Wahrnehmungen, Empfindungen und so weiter erleben, in eine Beziehung zu unserem Ich.",
      "Das Nervensystem ist in der mannigfal­tigsten Weise im menschlichen Organismus differenziert. Es zeigt sich uns als die inneren Nervenstränge, da, wo es sich aufschließt zum Beispiel zu Gehörnerven, Gesichtsnerven und so weiter.",
      "Das Nervensystem ist also etwas, was sich durch den Organismus so hinerstreckt, daß es in der mannigfaltigsten Weise differenziert ist, innere Mannigfaltigkeiten enthält. Wenn wir das Blut, durch den Organismus durchströmend, betrachten, so zeigt es sich uns - wenn wir absehen wollen von der Veränderung von rotem in blaues Blut -im ganzen Organismus doch als einheitliches Blut.",
      "Als ein solches Einheitliches tritt es dem differenzierten Nervensystem entgegen, wie das Ich dem Seelenleben entgegentritt, das sich gliedert in Vor­stellungen, Empfindungen, Willensimpulse, Gefühle und derglei­chen. Je weiter Sie diesen Vergleich verfolgen werden - und das soll ja",
      "zunächst auch nur vergleichsweise gesagt sein -, desto mehr wird sich Ihnen zeigen, daß eine weitgehende Ähnlichkeit besteht in der Bezie­hung der beiden Urbilder Ich und Astralleib zu ihren Abbildern, ihren Werkzeugen: Blutsystem und Nervensystem. Nun können wir allerdings sagen: Blut ist überall Blut, aber indem es durch den Organismus strömt, verändert es sich.",
      "Wir können diese Verände­rungen des Blutes in Parallele bringen mit den Veränderungen, die das Ich durch die verschiedenen Seelenerlebnisse erfährt. Auch unser Ich ist ein Einheitliches. So weit wir zurückdenken können im Leben zwischen Geburt und Tod, können wir von uns sagen: Ich war da!",
      "In unserem fünften Jahr wie in unserem sechsten Jahr, gestern wie heute ist es dasselbe Ich. - Aber wenn wir jetzt auf den Inhalt eingehen, auf das, was dieses Ich enthält, so werden wir finden, daß dieses Ich, wie es in mir lebt, angefüllt ist mit einer größeren oder kleineren Summe von Vorstellungen, Empfindungen, Gefühlen und so weiter, die dem Astralleibe zuzuschreiben sind und mit dem Ich in Berührung kom­men. Vor einem Jahre war unser Ich mit einem anderen Inhalt erfüllt, gestern hatte es einen anderen Inhalt und heute wieder einen anderen.",
      "Das Ich kommt also mit dem gesamten Seeleninhalt in Berührung, durchströmt diesen gesamten Seeleninhalt. Geradeso wie das Blut den ganzen Organismus durchströmt und überall mit dem differen­zierten Nervensystem in Berührung kommt, so kommt das Ich zusammen mit dem differenzierten Leben der Seele, mit Vorstellun­gen, Gefühlen, Willensimpulsen und dergleichen.",
      "So also zeigt uns schon diese nur vergleichsweise Betrachtung, daß eine gewisse Berechtigung existiert, in dem Blutsystem ein Abbild des Ich zu sehen und in dem Nervensystem ein Abbild des Astralleibes, die­ser beiden höheren, übersinnlichen Glieder der menschlichen Natur, während der Ätherleib sich mehr an den physischen Leib anschließt.",
      "Nun ist es notwendig, uns zu erinnern, daß das Blut, welches in der angedeuteten Weise durch den Organismus strömt, auf der einen Seite sich darbietet der Außenwelt, vergleichsweise wie eine Tafel den Eindrücken der Außenwelt entgegentritt, auf der anderen Seite sich dem entgegenhält, was wir die innere Welt genannt haben. Ja, so ist es",
      "auch mit unserem Ich. Wir richten unser Ich zunächst auf die Außen­welt, nehmen die äußeren Eindrücke auf. Da ergibt sich ein mannig­faltiger Inhalt in unserem Ich; es wird erfüllt von den Impressionen, die von außen kommen. Dann gibt es auch diejenigen Augenblicke, wo das Ich sozusagen in sich selber bleibt, wo es hingegeben ist seinem Schmerz, seinem Leid, an Lust und Freude, an die inneren Gefühle und so weiter, wo es sogar aus dem Gedächtnis aufsteigen läßt, was es jetzt nicht unmittelbar durch die Berührung mit der Außenwelt empfängt, sondern das, was es in sich trägt. Also auch in dieser Beziehung ist das Ich zu parallelisieren mit dem Blut, daß es sich wie eine Tafel darbietet einmal der äußeren Welt und einmal der inneren Welt; und wir könnten dieses Ich genauso schematisch dar­stellen, wie wir das Blut schematisch dargestellt haben (siehe Zeich­nung Seite 42). Wir können die äußeren Eindrücke, die das Ich bekommt, indem es sie als Vorstellungen, als Seelengebilde faßt, in dieselbe Beziehung bringen zum Ich, wie wir die realen, durch die Sinne zu uns kommenden äußeren Vorgänge zum Blut in Beziehung gebracht haben; wir können also die Seelenereignisse, genauso wie beim körperlichen Leben, auf der einen Seite zum Blut, auf der anderen Seite zum Ich in Beziehung bringen.",
      "Betrachten wir von diesem Gesichtspunkt aus das Zusammenwir­ken und das Einander-Entgegenwirken von Blut und Nerven. Wenn wir zum Beispiel unser Auge auf die Außenwelt hinwenden, so wirken die äußeren Impressionen - Farben, Lichteindrücke und so weiter - auf die Sehnerven. Solange wir die Augen auf die Außenwelt richten, so lange können wir auch davon sprechen, daß die Eindrücke der Außenwelt auf unsere Sehnerven, also das Werkzeug des Astral­leibes, eine Wirkung haben. In dem Augenblick, wo ein Verhältnis eintritt zwischen Nerven und Blut, können wir davon sprechen, daß der parallele Seelenvorgang der ist, daß die mannigfaltigen Vorstel­lungen des Seelenlebens zu dem Ich in Beziehung treten. Wir müssen also, wenn wir das schematisch zeichnen wollen, uns das Verhältnis von Nerven und Blut so denken, wie wenn das, was durch die Nerven von außen einströmt, in Beziehung tritt zu den Blutläufen, die in die Nähe der Sehnerven kommen.",
      "Diese Beziehung ist nun etwas außerordentlich Wichtiges, wenn man den menschlichen Organismus so betrachten will, daß die Be­trachtung eine Grundlage für die okkulte Anschauung der mensch­lichen Natur ergeben kann. Dann müssen wir uns sagen: Beim ge­wöhnlichen Leben, wie es im allgemeinen verfließt, geschieht der Vorgang so, daß eine Wirkung, die durch den Nerv sich fortpflanzt, in das Blut sich einschreibt wie in eine Tafel und dadurch in das",
      "# Bild s.042a",
      "Werkzeug des Ich sich eingeschrieben hat. Nehmen wir aber einmal an, wir würden die Beziehung zwischen Blutlauf und Nerv künstlich unterbrechen, das heißt, wir würden also künstlich den Menschen in eine solche Lage bringen, daß gleichsam der Nerv in seiner Wirk­samkeit von dem Blutlauf entfernt wird, so daß sie nicht mehr aufeinander wirken können. Das kann man schematisch in der Wei­se zeichnen, daß man die beiden Glieder weiter auseinander zeichnet, so daß eine Wechselwirkung zwischen Nerv und Blut nicht mehr stattfinden kann. Da kann die Sache so liegen, daß zunächst auf den Nerven kein Eindruck gemacht wird. So etwas kann man ja",
      "# Bild s.042b",
      "erreichen, indem man zum Beispiel den Nerv durchschneidet. Wenn es auf irgendeine Weise zustande kommt, daß ein Nerv durchschnit­ten ist, daß also auf den Nerv kein Eindruck gemacht wird, dann ist es ja nicht weiter wunderbar, daß der Mensch auch nichts Besonderes durch diesen Nerv erleben kann.",
      "Nehmen wir aber an, es werde -trotzdem die Beziehung zwischen Nerv und Blut unterbrochen ist -ein gewisser Eindruck gemacht. Im äußeren Experiment kann das ja dadurch herbeigeführt werden, daß man zum Beispiel durch einen elektrischen Strom den Nerv reizt.",
      "Diese äußere Beeinflussung des Nervs geht uns hier aber nichts an. Es gibt aber noch eine andere Beeinflussung des Nervs, die zu einem Zustande führt, wo er auf die Blutbahn nicht wirken kann. Dieser Zustand kann für den menschli­chen Organismus herbeigeführt werden - und er wird auch herbeige­führt - durch gewisse Vorstellungen, gewisse Ideen, Empfindungen und Gefühle, die der Mensch erlebt und sich angeeignet hat und die, damit ein solches Experiment gelinge, höhere moralische oder intel­lektuelle Vorstellungen sein sollten.",
      "Wenn der Mensch sich solche Vorstellungen macht, zum Beispiel von Sinnbildern, und sich in scharfer innerer Konzentration der Seele übt, dann bewirkt das, daß er gleichsam den Nerv voll in Anspruch nimmt und ihn dadurch zurückzieht vom Blutlaufe. Wenn der Mensch im wachen Bewußt­sein sich den normalen äußeren Eindrücken überläßt, wie sie gerade kommen, dann ist die natürliche Verbindung zwischen Nerv und Blutlauf da.",
      "Wenn der Mensch aber sich durch scharfe innere Kon­zentration von der Wirkung der äußeren Eindrücke abzieht, dann hat er ja das in der Seele, was erst im Bewußtsein entsteht; was Inhalt des Bewußtseins ist, nimmt den Nerv vorzugsweise in Anspruch und trennt dadurch die Nerventätigkeit ab von der Bluttätigkeit. Die Folge einer solchen inneren Konzentration, die - wenn sie stark genug ist - wirklich die Leitung zwischen Nerv und Blut unterbricht, ist, daß der Nerv in einer gewissen Weise befreit wird von dem Zusammenhang mit dem Blutsystem, ja auch befreit wird von dem, wofür das Blutsystem das äußere Werkzeug ist, das heißt also befreit wird von den gewöhnlichen Erlebnissen des Ich.",
      "Und es ist in der Tat so - und das kann vollständig experimentell belegt werden -, daß",
      "durch die Erlebnisse der geistigen Schulung, die in die höheren Welten hinaufführen soll, durch die anhaltende scharfe Konzentra­tion das gesamte Nervensystem zeitweise dem gewöhnlichen Zusam­menhang mit dem Blutsystem und dessen Aufgaben für das Ich entrückt wird. Da tritt nun eine gewisse Folge ein, nämlich die, daß das Nervensystem, das früher seine Wirkung auf die Tafel des Blutes geschrieben hat, nunmehr das, was es als Wirkung in sich enthält, in sich selbst zurücklaufen läßt, in sich zurücknimmt und diese Wir­kung nicht bis zum Blut hinkommen läßt. Es ist also möglich, rein durch Vorgänge innerer Konzentration, sein Blutsystem von dem Nervensystem gleichsam abzutrennen und dadurch dasjenige, was sonst in das Ich - bildlich gesprochen - hineingeflossen wäre, zum Zurücklaufen in das Nervensystem zu bringen.",
      "Nun ist das Eigentümliche, daß der Mensch, wenn er durch innere Seelentätigkeit wirklich so etwas bewirkt, dann eine ganz andere Art des inneren Erlebens hat und damit vor einem vollständig veränder­ten Bewußtseinshorizont steht. Wir können sagen: Wenn Nerven und Blut in der gewöhnlichen Weise miteinander in Wechselwirkung stehen, wie es im normalen Leben der Fall ist, dann bezieht der Mensch die Eindrücke, die von außen kommen, auf sein Ich. Wenn er aber durch innere Konzentration, durch innere Seelentätigkeit sein Nervensystem heraushebt aus der Wirkung auf sein Blutsystem, dann lebt er auch nicht in seinem bisherigen gewöhnlichen Ich; er kann dann nicht in demselben Sinne zu dem, was er jetzt als sein Selbst hat, «Ich» sagen. Der Mensch erscheint sich dann so, wie wenn er einen Teil seiner Wesenheit ganz bewußt aus sich herausgehoben hätte, abgesondert von seinem Blutsystem; es ist so, wie wenn etwas, was man sonst nicht sieht, ein Übersinnliches, in unsere Nerven hereinwirkt, das sich nicht auf unsere Bluttafel abdruckt und auf unser gewöhnliches Ich keinen Eindruck macht. Der Mensch fühlt sich hinweggehoben von dem ganzen Blutsystem, gleichsam heraus­gehoben aus dem Organismus. Es ist ein bewußtes Herausheben des Ich aus dem Wirkungsbereich des Astralleibes. Während nun früher die Nerventätigkeit im Blutsystem abgebildet wurde, wird sie jetzt in sich selbst zurückreflektiert; jetzt lebt der Mensch in etwas anderem,",
      "da empfindet er sich in einem anderen Ich, in einem [makrokosmi­schen] Ich, das früher nur geahnt werden konnte: Er fühlt das Her­einragen einer übersinnlichen Welt.",
      "Wenn wir noch einmal die Beziehung zwischen dem Nerv oder dem gesamten Nervensystem, wie es die Eindrücke einer äußeren Welt in sich hereinnimmt, zum Blut genauer schematisch zeichnen wollen, so kann es in folgender Weise geschehen:",
      "# Bild s.045",
      "Würden äußere Eindrücke, äußere Erlebnisse einfließen, dann würden sie sich abdrücken im Blutsystem. Haben wir aber das Ner­vensystem herausgehoben aus dem Blutsystem, dann fließt alles innerhalb des Nervensystems zurück, dann ergießt sich eine Welt, von der wir früher keine Ahnung hatten, gleichsam bis an die Enden unseres Nervensystems, und das fühlen wir als Rückstoß. Während es beim gewöhnlichen Bewußtsein so ist, daß man eine Welt auf­nimmt, die hineingeht bis zum Blutsystem, dem Blutsystem wie auf einer Tafel eingeschrieben wird, geht man nunmehr mit den Eindrük­ken nur bis dahin, wo die Nerven endigen und in sich selbst einen Widerstand finden. An diesen Nervenendungen prallt man gleichsam zurück und lebt sich hinaus in die übersinnliche Welt. Wenn wir einen Farbeneindruck haben, den wir durch das Auge empfangen, so geht er in unseren Sehnerv hinein, drückt sich ab auf der Tafel des Blutes, und wir fühlen das, was wir mit den Worten ausdrücken: Ich",
      "# Bild s.046",
      "sehe rot. - Nehmen wir aber an, wir gehen mit unseren Eindrücken nicht bis zum Blut hin, sondern nur bis zur Endung des Nervs, prallen da zurück, so leben wir im Grunde genommen bis zu unse­rem Sehnerv hin. Wir prallen vor dem körperlichen Ausdruck unse­res Blutes zurück, leben außerhalb unserer selbst; wir sind eigentlich in den Strahlen des Lichtes, die sonst den Eindruck «rot» in uns hervorriefen, darinnen. Wir sind also wirklich aus uns herausgekom­men, und zwar dadurch, daß wir nicht so tief in unser Inneres hereindringen, wie wir es sonst tun, sondern daß wir nur bis zu den Nervenenden gehen. Das bewirkt aber ein solches Seelenleben, das den physischen Menschen wie etwas Äußerliches empfindet und sich nicht länger mit ihm identifiziert. Das normale Bewußtsein geht bis zum Blute hin. Wenn wir aber die Seele so entwickelt haben, daß wir gleichsam an den Nervenenden kehrtmachen, dann haben wir das Blut ausgeschaltet von dem, was wir den höheren Menschen nennen, zu dem wir kommen können, wenn wir von uns selber loskommen.",
      "Durch diese Betrachtungen haben wir zunächst eine Anschauung von den Vorgängen gewonnen, die eintreten, wenn wir das Blutsy­stem, welches wir betrachtet haben wie eine Art Tafel, die sich auf der einen Seite den äußeren, auf der anderen Seite den inneren Ein­drücken darbietet, ausgeschaltet haben von dem, was wir nennen können den höheren Menschen, zu dem wir uns entwickeln können, wenn wir von uns selber loskommen und frei werden von den Einwirkungen des gewöhnlichen Ich. Wir werden nun am besten die ganze innere Natur dieses Blutsystems studieren können, wenn wir",
      "uns nicht in allgemeinen Phrasen bewegen, sondern das am Men­schen betrachten, was real ist, den übersinnlichen, unsichtbaren Men­schen, zu dem wir uns selber aufschwingen können. Wenn wir diesen übersinnlichen Menschen so betrachten, wie er sich hineinbegibt bis zum Blute hin, dann werden wir zu dem Gedanken vorrücken kön­nen, daß der Mensch in der Außenwelt leben kann, daß er sich ergießen kann über die ganze Außenwelt, aufgehen kann in dieser Außenwelt und daß er gleichsam den umgekehrten Standpunkt ein­nehmen kann zu seinem inneren Wesen. Kurz, wir werden die Funk­tionen des Blutes und der Organe, die in den Blutkreislauf einge­schaltet sind, dadurch kennenlernen, daß wir die Frage beantworten:",
      "Wie muß nun diese höhere Welt, zu der sich der Mensch aufschwin­gen kann, die er genau kennenlernen kann, sich auf die Tafel des Blutes abmalen? - Da wird sich uns das ganze differenzierte Blutle­ben als der Mittelpunkt des Menschen ergeben, wenn wir unmittelbar die Beziehungen dieses wunderbaren Systems zu einer höheren Welt betrachten. Denn das wird ja unsere Aufgabe sein, daß wir den Menschen ansehen können als eine Offenbarung des Übersinnlichen, daß wir den äußeren Menschen ansehen können als ein Abbild desje­nigen Menschen, der in der geistigen Welt wurzelt. Dadurch werden wir den menschlichen Organismus erkennen können als ein getreues Abbild des Geistes."
    ],
    "sentences": [
      [
        "Wir werden zwar innerhalb dieser Betrachtungen immer wieder in die Schwierigkeit versetzt werden, den äußeren menschlichen Orga­nismus genauer ins Auge zu fassen, um sozusagen das Vergängliche, das Zerbrechliche zu erkennen.",
        "Aber wir werden auch sehen, daß gerade dieser Weg uns führen wird zu einer Erkenntnis des Bleiben­den, des Unvergänglichen, des Ewigen in der menschlichen Natur.",
        "Allerdings ist es notwendig, wenn unsere Betrachtungen dieses Ziel haben sollen, daß wir das streng einhalten, was gestern schon in der Einleitung bemerkt worden ist: den Gesichtspunkt, den äußeren physischen Organismus in aller Ehrfurcht als eine Offenbarung aus geistigen Welten zu betrachten."
      ],
      [
        "Wenn wir uns schon einigermaßen mit geisteswissenschaftlichen Begriffen und Empfindungen durchdrungen haben, können wir uns ja sehr leicht in den Gedanken hineinfinden, daß der menschliche Organismus in seiner ungeheuren Kompliziertheit der bedeutsamste Ausdruck, die größte und bedeutendste Offenbarung der Kräfte sein muß, die als geistige Kräfte die Welt durchweben und durchleben.",
        "Wir werden allerdings sozusagen vom Äußeren immer mehr und mehr in das Innere aufzusteigen haben."
      ],
      [
        "Wir haben gestern schon gesehen, wie uns die äußerliche Betrach­tung sowohl des Laien als auch der Wissenschaft dazu führen muß, den Menschen gewissermaßen als eine Zweiheit anzusehen.",
        "Wir haben diese Zweiheit der menschlichen Wesenheit gestern schon flüchtig charakterisiert - wir werden darauf noch genauer einzugehen haben -, und wir haben dasjenige an der menschlichen Wesenheit genauer betrachtet, was eingeschlossen ist in die schützende Kno­chenhülle des Schädels und der Rückenwirbel.",
        "Dabei haben wir gesehen, wie wir, wenn wir ausgehen von der äußeren Gestaltung und Form dieses Teils des Menschen, schon einen vorläufigen Aus­blick gewinnen können in den Zusammenhang desjenigen Lebens, das wir unser waches Tagesleben nennen, mit jenem anderen,"
      ],
      [
        "zunächst für uns natürlich sehr von Zweifeln durchwobenen Leben, das wir das Traumleben nennen.",
        "Wir haben gesehen, daß schon die äußeren Formen des charakterisierten Teiles der Menschennatur eine Art Abbild geben, eine Art Offenbarung bedeuten: auf der einen Seite des Traumlebens, dieses chaotischen Bilderlebens, und auf der anderen Seite des mit scharf umrissener Beobachtung ausgestatteten wachen Tageslebens.",
        "Heute werden wir zunächst einen flüchtigen Blick zu werfen haben auf das andere Glied der menschlichen Zwei­heit, das sich gewissermaßen außerhalb des Bereiches befindet, den wir gestern ins Auge gefaßt haben.",
        "Schon der alleroberflächlichste Blick auf diesen zweiten Teil der menschlichen Wesenheit kann uns darüber belehren, daß dieser in gewisser Beziehung das entgegenge­setzte Bild dessen zeigt, was wir bei Gehirn und Rückenmark ins Auge gefaßt haben.",
        "Gehirn und Rückenmark sind von Knochenbil­dungen als schützender Hülle umschlossen.",
        "Betrachten wir den ande­ren Teil der menschlichen Natur, so müssen wir entschieden sagen, daß wir hier die Knochenbildung mehr in den Organismus hineinge-gliedert finden.",
        "Doch das wäre nur eine ganz oberflächliche Betrach­tung.",
        "Tiefer hinein in das Gefüge dieses anderen Teiles der Men­schennatur werden wir schon geführt, wenn wir die bedeutendsten Organsysteme auseinanderhalten und sie zunächst äußerlich verglei­chen mit dem, was wir gestern kennengelernt haben."
      ],
      [
        "Diejenigen Organsysteme, Werkzeugsysteme des menschlichen Organismus, welche dabei zuerst in Betracht kommen werden, sollen sein der Ernährungsapparat und alles das, was zwischen dem Ernäh­rungsapparat und jenem wunderbaren Gebilde liegt, das wir unschwer wie eine Art Mittelpunkt der ganzen menschlichen Orga­nisation empfinden können, dem Herzen.",
        "Da zeigt uns gleich der oberflächliche Blick, daß der Ernährungsapparat - wie man ihn im populären Sinne nennen kann - dazu bestimmt ist, die Stoffe unserer äußeren irdischen Umwelt aufzunehmen und für die weitere Verar­beitung im physischen Organismus des Menschen vorzubereiten.",
        "Wir wissen, daß dieser Verdauungsapparat zunächst von unserem Munde aus röhrenförmig zu dem Organ sich erstreckt, das jeder als den Magen kennt.",
        "Und schon eine oberflächliche Betrachtung lehrt"
      ],
      [
        "uns, daß von jenen Nahrungsmitteln, die durch diesen Kanal in den Magen eingeführt werden, gewissermaßen unverwendete Teile ein­fach abgesondert werden, während andere Teile von den weiteren Verdauungsorganen in den menschlichen Leibesorganismus überge­führt werden.",
        "Es ist ja auch wohl bekannt, daß an den eigentlichen Verdauungsapparat im engeren Sinne sich das anschließt, was wir das Lymphsystem nennen - ich will jetzt zunächst nur schematisch spre­chen -, um die vom Verdauungsapparat hineingelieferten Nahrungs­stoffe in verwandeltem Zustande aufzunehmen."
      ],
      [
        "So daß wir sagen können, daß an den Verdauungsapparat, soweit er sich an den Magen angliedert, ein Organsystem sich anschließt, das Lymphsystem, als eine Summe von Kanälen, die durch den ganzen Körper gehen, ein System, welches das übernimmt, was durch den Verdauungsapparat verarbeitet ist, und die umgewandelten Stoffe abliefert an das Blut.",
        "Und dann haben wir das dritte Glied der Menschennatur, das Blutge­fäßsystem selber mit seinen weiteren oder engeren Röhren, wie es sich durch den ganzen menschlichen Organismus zieht und das zum Mittelpunkte seines ganzen Wirkens das Herz hat."
      ],
      [
        "Wir wissen ja, daß vom Herzen diejenigen bluterfüllten Gefäße ausgehen, die wir die Arterien nennen, und daß diese nach allen Teilen unseres Organis­mus das sogenannte rote Blut hinführen.",
        "Das Blut macht einen gewissen Prozeß in den einzelnen Gliedern des menschlichen Orga­nismus durch, wird dann wiederum zurückgeführt durch andere Gefäße, die Venen, die es aber jetzt in verändertem, verwandeltem Zustande als sogenanntes blaues Blut zu dem Herzen zurückbringen."
      ],
      [
        "Wir wissen auch, daß dieses verwandelte, unbrauchbar gewordene Blut von dem Herzen in die Lunge geleitet wird, daß es dort in Berührung kommt mit dem von außen aufgenommenen Sauerstoff der Luft, daß es dadurch erneuert und dann wiederum in Venen zum Herzen zurückgeleitet wird, um von neuem den Umlauf durch den ganzen menschlichen Organismus zu beginnen."
      ],
      [
        "Um diese komplizierten Systeme zu betrachten, wollen wir uns, damit wir in der äußeren Betrachtungsweise gleich eine Grundlage haben für die okkulte Betrachtungsweise, zunächst an dasjenige System halten, das von vornherein jedem als das eigentliche Mittelpunktsystem"
      ],
      [
        "des ganzen menschlichen Organismus erscheinen muß:"
      ],
      [
        "das Blut-Herzsystem.",
        "Wir wollen dabei zunächst ins Auge fassen, wie das Blut, nachdem es als verbrauchtes Blut in der Lunge aufge­frischt ist, also aus dem sogenannten blauen Blut wieder in rotes Blut verwandelt worden ist, wieder zum Herzen zurückkehrt und dann vom Herzen als rotes Blut wiederum ausströmt in den Organismus, um hier verwendet zu werden. (Es wird an die Tafel gezeichnet.) Beachten Sie, daß alles, was ich hier zeichne, nur ganz schematisch ist."
      ],
      [
        "Rufen wir uns kurz ins Gedächtnis, daß das menschliche Herz ein Organ ist, das eigentlich aus vier Gliedern zunächst besteht, aus vier Kammern, die durch Innenwände so abgegrenzt sind, daß man unter­scheiden kann zwei größere Räume nach unten gelegen und zwei kleinere nach oben gelegen, die beiden unteren die beiden Herzkam­mern, wie man sie gewöhnlich nennt, während die oberen die Vor-kammern genannt werden.",
        "Ich will heute noch nicht von den Herz-klappen sprechen, sondern den Gang der wichtigsten Organtätigkei­ten ganz schematisch ins Auge fassen."
      ],
      [
        "Da zeigt sich zunächst, daß das Blut, nachdem es aus der linken Vorkammer in die linke Herzkam­mer geströmt ist, durch eine große Schlagader abfließt und von da aus in den ganzen Organismus geleitet wird.",
        "Nun wollen wir ins Auge fassen, daß dieses Blut zunächst in alle einzelnen Organe des Orga­nismus sich verteilt, daß es dann im Organismus verbraucht wird, wodurch es in das sogenannte blaue Blut verwandelt wird und als solches wieder zum Herzen in die rechte Vorkammer zurückkehrt, von dort in die rechte Herzkammer fließt, um von hier aus wieder in die Lunge zu gehen, wieder erneuert zu werden und den Gang durch den Organismus von neuem zu machen."
      ],
      [
        "Wenn wir uns dies vorstellen, so ist es zur Grundlage einer okkul­ten Betrachtungsweise wichtig zu bedenken, daß sehr früh von der Hauptschlagader eine Nebenströmung abgeht, welche ins Gehirn führt, die oberen Organe des Menschen versorgt und von dort als verbrauchtes Blut wieder zurückfließt in die rechte Vorkammer, und daß es als das Gehirn passiert habendes Blut ebenso verwandelt wird wie das Blut, das aus den übrigen Gliedern des Organismus kommt.",
        "Wir haben also einen kleineren Nebenkreislauf des Blutes, in welchen"
      ],
      [
        "# Bild s.032"
      ],
      [
        "das Gehirn eingeschaltet ist, abgetrennt von dem anderen, großen Kreislauf, der den ganzen übrigen Organismus versorgt.",
        "Nun ist es außerordentlich wichtig, daß wir gerade diese Tatsache ins Auge fassen.",
        "Denn wir bekommen eine richtige Vorstellung, die uns eine Grundlage geben kann für alles, was uns möglich machen wird, in die okkulten Höhen hinaufzusteigen, nur dann, wenn wir uns die Frage stellen: Ist denn - in ähnlicher Weise, wie in den kleinen Blutkreislauf die oberen Organe eingeschaltet sind, namentlich das Gehirn - in den großen Blutkreislauf, der den übrigen Organismus versorgt, etwas ähnliches eingeschaltet? - Da kommen wir in der Tat zu dem Ergeb­nis, das schon die äußere oberflächliche Betrachtungsweise liefern kann, daß in den großen Blutkreislauf zunächst das Organ eingeschaltet"
      ],
      [
        "ist, welches wir die Milz nennen, daß weiter darin einge­schaltet ist die Leber und jenes Organ, welches die von der Leber zubereitete Galle enthält.",
        "Diese Organe sind alle in den großen Blutkreislauf eingeschaltet."
      ],
      [
        "Wenn wir jetzt nach der Aufgabe dieser Organe fragen, so gibt uns die äußere Wissenschaft darauf die Antwort, daß die Leber die Galle bereitet, daß die Galle über die Gallenwege abfließt in den Verdau­ungskanal und an der Verarbeitung der Nahrungsmittel so mitwirkt, daß diese dann aufgenommen werden können vom Lymphsystem und übergeleitet werden können in das Blut.",
        "Weniger Genaues sagt die äußere Wissenschaft über die Milz."
      ],
      [
        "Wenn wir diese Organe betrachten, haben wir nun zunächst den Blick darauf zu richten, daß dieselben sich sozusagen zu beschäftigen haben mit der Umwandlung der Nahrung für den menschlichen Organismus, daß aber auf der anderen Seite alle drei Organe eingeschaltet sind in den großen Blut­kreislauf.",
        "In diesen sind sie nun nicht umsonst eingeschaltet."
      ],
      [
        "Denn insofern die Nahrungsstoffe aufgenommen werden in das Blut, um durch das Blut dem menschlichen Organismus zugeführt zu werden und demselben die Baustoffe fortwährend zu ersetzen, da beteiligen sich diese drei Organe an der notwendigen Verarbeitung der Nah­rungsstoffe.",
        "Es ist nun die Frage: Können wir aus einer äußeren Beobachtung schon entnehmen, wie sich diese drei Organe an der Gesamttätigkeit des menschlichen Organismus beteiligen? - Richten wir dazu den Blick zunächst auf eine Äußerlichkeit, darauf, daß diese Organe so eingeschaltet sind in den unteren Blutkreislauf, wie das Gehirn in den oberen Kreislauf eingeschaltet ist; und fragen wir einmal - wenn wir uns zunächst wirklich an diese äußerliche Betrach­tungsweise halten, die später vertieft werden soll -, ob diese Organe möglicherweise eine ähnliche, eine verwandte Aufgabe haben könn­ten wie das Gehirn oder überhaupt wie die höhergelegenen Teile des menschlichen Organismus."
      ],
      [
        "Worin könnte diese Aufgabe bestehen?"
      ],
      [
        "Betrachten wir einmal diese höheren Teile des menschlichen Orga­nismus; es sind ja die Organe, welche die äußeren Sinneseindrücke aufnehmen und das Material unserer Sinneswahrnehmung verarbei­ten.",
        "Daher können wir sagen: Was im menschlichen Haupt, in den"
      ],
      [
        "oberen Partien des menschlichen Organismus geschieht, das ist Ver­arbeitung der Außenwelt, Verarbeitung jener Eindrücke, die von außen durch die Sinnesorgane einfließen.",
        "Die wesentlichen Ursachen für das, was in den oberen Partien des Menschen geschieht, haben wir zu sehen in den äußeren Impressionen, in den äußeren Eindrücken."
      ],
      [
        "Indem diese äußeren Eindrücke ihre Wirkungen hineinsenden in die oberen Organe des menschlichen Organismus, verändern sie das Blut oder tragen jedenfalls dazu bei und senden dieses Blut ebenso verän­dert zum Herzen zurück, wie aus dem übrigen Organismus das Blut verändert zum Herzen zurückgesandt wird.",
        "Liegt es nun nicht nahe, daran zu denken, daß das, was durch das Tor der Sinnesorgane von der Außenwelt in den oberen Teil des menschlichen Organismus hereinwirkt, in gewisser Weise demjenigen entspricht, was aus den im Innern gelegenen Organen - Milz, Leber, Galle - heraus wirkt?"
      ],
      [
        "Der obere Teil des menschlichen Organismus schließt sich nach außen auf, um die Wirkungen der Außenwelt zu empfangen, und während das Blut nach oben strömt, um diese Eindrücke der Außen­welt aufzunehmen, strömt es nach unten, um dasjenige aufzuneh­men, was von den unteren Organen kommt.",
        "Wie wir gesagt haben, werden von der Umwelt durch die Sinne Wirkungen auf unsere obere Organisation ausgeübt."
      ],
      [
        "Denken wir uns dies einmal zusammengezo­gen, zusammengepreßt in einem Zentrum, so können wir darin etwas Analoges sehen zu dem, was durch Leber, Galle und Milz bewirkt wird: Umwandlung von Stoffen, die der Außenwelt entnommen sind.",
        "Wenn wir näher darauf eingehen, werden Sie sehen, daß das keine so ganz absonderliche Betrachtungsweise ist."
      ],
      [
        "Denken Sie sich die verschiedenen hereinfließenden Sinnesein­drücke der Außenwelt wie zusammengezogen, gleichsam zu Orga­nen verdichtet, ins Innere des Menschen verlegt und eingeschaltet in das Blut, so bietet sich der obere Teil des menschlichen Organismus dem Blute ebenso dar, wie sich von innen die Organe Leber, Galle, Milz dem Blute darbieten.",
        "Also wir haben die Außenwelt, die oben unsere Sinne umgibt, gleichsam in Organe zusammengedrängt und ins Innere des Menschen verlegt, so daß wir sagen können: Einmal berührt uns die Welt von außen, sie strömt durch die Sinnesorgane in"
      ],
      [
        "unseren oberen Organismus ein und wirkt auf unser Blut, und einmal wirkt auf geheimnisvolle Weise die Welt von innen in Organen, in die sich erst zusammengezogen hat, was draußen im Makrokosmos vor­geht, und wirkt da entgegen unserem Blut, das sich ihm ebenso darbietet.",
        "Wenn wir das schematisch zeichnen wollten, könnten wir also sagen: Denken wir uns auf der einen Seite die Welt, von allen Seiten wirkend auf die Sinne, und das Blut, wie eine Tafel den Eindrücken der Außenwelt sich darbietend, so haben wir unsere"
      ],
      [
        "# Bild s. 35"
      ],
      [
        "obere Organisation.",
        "Denken wir uns jetzt, wir könnten diese ganze Welt zusammenziehen, in einzelne Organe zusammenziehen, einen Extrakt dieser Welt bilden, und könnten ihn in das Innere herein verlegen, so daß gewissermaßen die ganze Welt auf die andere Seite des Blutes wirkt, dann hätten wir ein schematisches Bild des Außen und des Innen des menschlichen Organismus in einer ganz sonder­baren Weise geformt.",
        "So könnten wir in einer gewissen Weise schon sagen: Es entspricht das Gehirn eigentlich unserer Innenorganisa­tion; insoweit sie Brust- und Bauchhöhle ausfüllt, ist gleichsam die Außenwelt in unser Inneres verlegt."
      ],
      [
        "Schon in dieser Organisation, die wir ja als eine untergeordnete erkennen, die hauptsächlich der Fortführung des Ernährungsprozes­ses dient, haben wir etwas so Geheimnisvolles wie eine Zusammenfü­gung der ganzen Außenwelt in eine Summe von inneren Organen, von inneren Werkzeugen.",
        "Und wenn wir nun diese Organe Leber,"
      ],
      [
        "Galle, Milz einmal näher betrachten, können wir sagen: Zunächst ist es die Milz, die sich der Blutströmung darbietet.",
        "Die Milz ist ein sonderbares Organ, in der in blutreiche Gewebe eingebettet ist eine ganze Summe von kleinen Körnchen, die sich gegenüber der übrigen Gewebemasse weiß ausnehmen.",
        "Wenn wir das Blut im Verhältnis zur Milz betrachten, erscheint uns die Milz wie ein Sieb, durch welches das Blut hindurchgeht, um sich einem solchen Organ darzubieten, das in gewisser Weise ein zusammengeschrumpfter Teil des Makro-kosmos ist.",
        "Als nächste Stufe sehen wir dann, wie sich das Blut der Leber darbietet und wie die Leber ihrerseits die Galle absondert, die in einem besonderen Organ aufbewahrt wird, dann in die Nahrungs­stoffe übergeht und von dort aus mit den verwandelten Nahrungs-stoffen in das Blut gelangt."
      ],
      [
        "Dieses innere Sichdarbieten des Blutes an die drei Organe können wir uns nicht anders als in folgender Weise vorstellen: Das erste Organ, das sich dem Blut entgegenstellt, ist die Milz, das zweite die Leber, und das dritte, das eigentlich ein sehr kompliziertes Verhältnis schon zum gesamten Blutsystem hat, ist die Galle.",
        "Weil die Galle den Nahrungsstoffen dargeboten wird und an der Verarbeitung derselben beteiligt ist, wird sie als besonderes Organ gezählt.",
        "Aus bestimmten Gründen haben die Okkultisten aller Zeiten diesen Organen gewisse Namen gegeben.",
        "Ich bitte Sie nun recht sehr, vorläufig bei diesen Na­men, die diesen Organen gegeben sind, an nichts Besonderes zu den­ken und davon abzusehen, daß diese Namen noch etwas anderes in der großen Welt bedeuten.",
        "Wir werden später noch sehen, warum ge­rade diese Namen genommen wurden.",
        "Weil die Milz sich dem Blut zu­erst darbietet - so können wir rein äußerlich vergleichsweise sagen -, erschien sie den alten Okkultisten am besten mit jenem Namen bezeichnet, der dem Stern zukommt, der sich im Weltenraum zuerst im Sonnensystem darbietet; deshalb nannten sie die Milz Saturnus oder einen inneren Saturn im Menschen.",
        "In ähnlicher Weise nannten sie die Leber einen inneren Jupiter und die Galle einen inneren Mars.",
        "Wollen wir zunächst bei diesen Namen uns gar nichts anderes den­ken, als daß wir sie aus dem Grunde wählen, weil wir die Anschau­ung gewonnen haben, zunächst hypothetisch, daß die äußeren Welten,"
      ],
      [
        "die sonst unseren Sinnen zugänglich sind, zusammengezogen sind in diesen Organen und uns gleichsam als innere Welten entge­gentreten, wie uns äußerliche Welten in den Planeten entgegentreten.",
        "Wir würden aber jetzt schon sagen können: Wie die äußeren Welten unseren Sinnen erscheinen, indem sie von außen eindringen und auf das Blut wirken, so erscheinen uns die Innenwelten wirksam auf das Blut, indem sie dasselbe ebenfalls beeinflussen."
      ],
      [
        "Wir werden nun allerdings einen bedeutungsvollen Unterschied finden zwischen dem, was wir gestern besprochen haben als Eigen­tümlichkeiten des menschlichen Gehirns, und dem, was wie eine Art inneres Weltensystem auf unser Blut wirkt.",
        "Dieser Unterschied liegt einfach darin, daß der Mensch zunächst nichts von dem weiß, was sich innerhalb seines unteren Organismus abspielt; das heißt, er weiß nichts von den Eindrücken, welche die innere Welt - gleichsam die inneren Planeten - auf ihn machen, wogegen es ja gerade charakteri­stisch ist, daß die äußeren Welten auf sein Bewußtsein ihre Eindrücke machen.",
        "In einer gewissen Beziehung dürfen wir also diese innere Welt als die Welt des Unbewußten bezeichnen gegenüber der bewuß­ten Welt, welche wir im Gehirnleben kennengelernt haben."
      ],
      [
        "Nun wird sich uns gerade das, was in diesem Bewußten und Unbewußten liegt, dadurch näher aufklären, daß wir etwas anderes zu Hilfe nehmen.",
        "Sie wissen alle, daß die äußere Wissenschaft davon spricht, daß das Nervensystem das Organ des Bewußtseins ist mit allem, was dazugehört.",
        "Nun müssen wir als Grundlage für unsere okkulten Betrachtungen eine gewisse Beziehung ins Auge fassen, die das Nervensystem zum Blutsystem hat, das heißt zu dem, was wir ja heute schematisch ins Auge gefaßt haben.",
        "Da sehen wir, daß unser Nervensystem überall in gewisse Beziehungen tritt zu unserem Blut-system, daß das Blut überall an unser Nervensystem herandringt.",
        "Dabei müssen wir nun zunächst auf das Rücksicht nehmen, was die äußere Wissenschaft diesbezüglich für etwas Ausgemachtes hält.",
        "Sie hält das für ausgemacht, daß im Nervensystem der gesamte Regulator liege aller Bewußtseinstätigkeit, alles dessen, was wir als bewußtes Seelenleben bezeichnen.",
        "Wir können nicht umhin - zunächst auch nur andeutungsweise, um es später zu belegen -, uns zum Bewußtsein"
      ],
      [
        "zu bringen, daß das Nervensystem für den Okkultisten nur wie eine Art von Grundlage des Bewußtseins dasteht.",
        "Denn gerade so, wie sich in unseren Organismus eingliedert das Nervensystem und berührt wird oder wenigstens in einem gewissen Verhältnis steht zum Blutsystem, so gliedert sich in die Gesamtwesenheit des Menschen dasjenige ein, was wir nennen des Menschen astralischen Leib und des Menschen Ich."
      ],
      [
        "Und schon eine äußerliche Betrachtung kann uns zeigen - und ich habe ja öfter in meinen Vorträgen darüber gespro­chen -, daß das Nervensystem in einer gewissen Weise eine Offenba­rung des Astralleibes ist und das Blut eine Offenbarung des Ich.",
        "Wenn wir in die unbelebte Natur gehen, so sehen wir ja, wie wir den Gesteinen, Mineralien und so weiter nur einen physischen Leib zuzuschreiben haben in den Teilen, die sie uns darbieten."
      ],
      [
        "Wenn wir dann von den unbelebten, unorganischen Naturkörpern zu den belebten Naturkörpern aufsteigen zu den Organismen, so müssen wir uns denken, daß diese Organismen durchsetzt sind von dem sogenannten Ätherleib oder Lebensleib, der in sich die Ursachen der Lebenserscheinungen enthält.",
        "Wir werden später schon sehen, daß die Geisteswissenschaft von diesem Äther- oder Lebensleib nicht so spricht, wie die äußere Wissenschaft von einer spekulativen Lebenskraft gesprochen hat."
      ],
      [
        "Wenn die Geisteswissenschaft vom Ätherleibe spricht, spricht sie von etwas, was das geistige Auge wirklich sieht, also von einem Realen, das dem äußeren, physischen Leibe zugrundeliegt.",
        "Wenn wir die Pflanzen betrachten, müssen wir ihnen einen Ätherleib zuschreiben."
      ],
      [
        "Steigen wir hinauf von den Pflan­zen zu den empfindenden Wesen, den Tieren, so ist es das Element des Empfindens, des inneren Erlebens, welches das Tier von der Pflanze unterscheidet.",
        "Wenn wir uns nun fragen, was muß sich eingliedern dem tierischen Organismus, damit er hinaufgehoben wer­den kann von den bloßen Lebensvorgängen zu Empfindungen, die die Pflanzen noch nicht haben, so ist die Antwort: Soll die bloße Lebenstätigkeit, die sich noch nicht verinnerlichen kann, noch nicht zur Empfindung entzünden kann, sich zur Empfindung, zum inner­lichen Erleben entzünden können, so muß sich in den tierischen Organismus eingliedern der Astralleib."
      ],
      [
        "Und in dem Nervensystem,"
      ],
      [
        "das die Pflanzen noch nicht haben, müssen wir den äußeren Aus­druck, das Werkzeug des Astralleibes sehen.",
        "Der Astralleib ist das geistige Urbild des Nervensystems.",
        "Wie das Urbild zu seiner Offen­barung, zu seinem Abbild, so verhält sich der Astralleib zu dem Nervensystem."
      ],
      [
        "Wenn wir nun mit unserer Betrachtung beim Menschen einset­zen - und ich habe schon gestern gesagt, daß wir es im Okkultismus nicht so gut haben wie die äußere wissenschaftliche Betrachtungs­weise, daß wir nicht sozusagen alles durcheinanderwerfen können -, dann müssen wir, wenn wir die menschlichen Organe betrachten, uns immer bewußt sein, daß diese Organe oder Organsysteme zu etwas gebraucht werden können, wozu die analogen Organsysteme im tierischen Organismus, wenn sie auch ähnlich ausschauen, nicht gebraucht werden können.",
        "Beim Menschen müssen wir das Blut als äußeres Werkzeug für das Ich ansehen, für alles, was wir als unser innerstes Seelenzentrum, das Ich, bezeichnen."
      ],
      [
        "So haben wir im Ner­vensystem ein äußeres Werkzeug des Astralleibes und in unserem Blut ein äußeres Werkzeug des Ich.",
        "Geradeso wie das Nervensystem im Organismus in gewisse Beziehungen tritt zum Blut, so treten diejenigen inneren Seelengebilde, die wir als unsere Vorstellungen, Wahrnehmungen, Empfindungen und so weiter erleben, in eine Beziehung zu unserem Ich."
      ],
      [
        "Das Nervensystem ist in der mannigfal­tigsten Weise im menschlichen Organismus differenziert.",
        "Es zeigt sich uns als die inneren Nervenstränge, da, wo es sich aufschließt zum Beispiel zu Gehörnerven, Gesichtsnerven und so weiter."
      ],
      [
        "Das Nervensystem ist also etwas, was sich durch den Organismus so hinerstreckt, daß es in der mannigfaltigsten Weise differenziert ist, innere Mannigfaltigkeiten enthält.",
        "Wenn wir das Blut, durch den Organismus durchströmend, betrachten, so zeigt es sich uns - wenn wir absehen wollen von der Veränderung von rotem in blaues Blut -im ganzen Organismus doch als einheitliches Blut."
      ],
      [
        "Als ein solches Einheitliches tritt es dem differenzierten Nervensystem entgegen, wie das Ich dem Seelenleben entgegentritt, das sich gliedert in Vor­stellungen, Empfindungen, Willensimpulse, Gefühle und derglei­chen.",
        "Je weiter Sie diesen Vergleich verfolgen werden - und das soll ja"
      ],
      [
        "zunächst auch nur vergleichsweise gesagt sein -, desto mehr wird sich Ihnen zeigen, daß eine weitgehende Ähnlichkeit besteht in der Bezie­hung der beiden Urbilder Ich und Astralleib zu ihren Abbildern, ihren Werkzeugen: Blutsystem und Nervensystem.",
        "Nun können wir allerdings sagen: Blut ist überall Blut, aber indem es durch den Organismus strömt, verändert es sich."
      ],
      [
        "Wir können diese Verände­rungen des Blutes in Parallele bringen mit den Veränderungen, die das Ich durch die verschiedenen Seelenerlebnisse erfährt.",
        "Auch unser Ich ist ein Einheitliches.",
        "So weit wir zurückdenken können im Leben zwischen Geburt und Tod, können wir von uns sagen: Ich war da!"
      ],
      [
        "In unserem fünften Jahr wie in unserem sechsten Jahr, gestern wie heute ist es dasselbe Ich. - Aber wenn wir jetzt auf den Inhalt eingehen, auf das, was dieses Ich enthält, so werden wir finden, daß dieses Ich, wie es in mir lebt, angefüllt ist mit einer größeren oder kleineren Summe von Vorstellungen, Empfindungen, Gefühlen und so weiter, die dem Astralleibe zuzuschreiben sind und mit dem Ich in Berührung kom­men.",
        "Vor einem Jahre war unser Ich mit einem anderen Inhalt erfüllt, gestern hatte es einen anderen Inhalt und heute wieder einen anderen."
      ],
      [
        "Das Ich kommt also mit dem gesamten Seeleninhalt in Berührung, durchströmt diesen gesamten Seeleninhalt.",
        "Geradeso wie das Blut den ganzen Organismus durchströmt und überall mit dem differen­zierten Nervensystem in Berührung kommt, so kommt das Ich zusammen mit dem differenzierten Leben der Seele, mit Vorstellun­gen, Gefühlen, Willensimpulsen und dergleichen."
      ],
      [
        "So also zeigt uns schon diese nur vergleichsweise Betrachtung, daß eine gewisse Berechtigung existiert, in dem Blutsystem ein Abbild des Ich zu sehen und in dem Nervensystem ein Abbild des Astralleibes, die­ser beiden höheren, übersinnlichen Glieder der menschlichen Natur, während der Ätherleib sich mehr an den physischen Leib anschließt."
      ],
      [
        "Nun ist es notwendig, uns zu erinnern, daß das Blut, welches in der angedeuteten Weise durch den Organismus strömt, auf der einen Seite sich darbietet der Außenwelt, vergleichsweise wie eine Tafel den Eindrücken der Außenwelt entgegentritt, auf der anderen Seite sich dem entgegenhält, was wir die innere Welt genannt haben.",
        "Ja, so ist es"
      ],
      [
        "auch mit unserem Ich.",
        "Wir richten unser Ich zunächst auf die Außen­welt, nehmen die äußeren Eindrücke auf.",
        "Da ergibt sich ein mannig­faltiger Inhalt in unserem Ich; es wird erfüllt von den Impressionen, die von außen kommen.",
        "Dann gibt es auch diejenigen Augenblicke, wo das Ich sozusagen in sich selber bleibt, wo es hingegeben ist seinem Schmerz, seinem Leid, an Lust und Freude, an die inneren Gefühle und so weiter, wo es sogar aus dem Gedächtnis aufsteigen läßt, was es jetzt nicht unmittelbar durch die Berührung mit der Außenwelt empfängt, sondern das, was es in sich trägt.",
        "Also auch in dieser Beziehung ist das Ich zu parallelisieren mit dem Blut, daß es sich wie eine Tafel darbietet einmal der äußeren Welt und einmal der inneren Welt; und wir könnten dieses Ich genauso schematisch dar­stellen, wie wir das Blut schematisch dargestellt haben (siehe Zeich­nung Seite 42).",
        "Wir können die äußeren Eindrücke, die das Ich bekommt, indem es sie als Vorstellungen, als Seelengebilde faßt, in dieselbe Beziehung bringen zum Ich, wie wir die realen, durch die Sinne zu uns kommenden äußeren Vorgänge zum Blut in Beziehung gebracht haben; wir können also die Seelenereignisse, genauso wie beim körperlichen Leben, auf der einen Seite zum Blut, auf der anderen Seite zum Ich in Beziehung bringen."
      ],
      [
        "Betrachten wir von diesem Gesichtspunkt aus das Zusammenwir­ken und das Einander-Entgegenwirken von Blut und Nerven.",
        "Wenn wir zum Beispiel unser Auge auf die Außenwelt hinwenden, so wirken die äußeren Impressionen - Farben, Lichteindrücke und so weiter - auf die Sehnerven.",
        "Solange wir die Augen auf die Außenwelt richten, so lange können wir auch davon sprechen, daß die Eindrücke der Außenwelt auf unsere Sehnerven, also das Werkzeug des Astral­leibes, eine Wirkung haben.",
        "In dem Augenblick, wo ein Verhältnis eintritt zwischen Nerven und Blut, können wir davon sprechen, daß der parallele Seelenvorgang der ist, daß die mannigfaltigen Vorstel­lungen des Seelenlebens zu dem Ich in Beziehung treten.",
        "Wir müssen also, wenn wir das schematisch zeichnen wollen, uns das Verhältnis von Nerven und Blut so denken, wie wenn das, was durch die Nerven von außen einströmt, in Beziehung tritt zu den Blutläufen, die in die Nähe der Sehnerven kommen."
      ],
      [
        "Diese Beziehung ist nun etwas außerordentlich Wichtiges, wenn man den menschlichen Organismus so betrachten will, daß die Be­trachtung eine Grundlage für die okkulte Anschauung der mensch­lichen Natur ergeben kann.",
        "Dann müssen wir uns sagen: Beim ge­wöhnlichen Leben, wie es im allgemeinen verfließt, geschieht der Vorgang so, daß eine Wirkung, die durch den Nerv sich fortpflanzt, in das Blut sich einschreibt wie in eine Tafel und dadurch in das"
      ],
      [
        "# Bild s.042a"
      ],
      [
        "Werkzeug des Ich sich eingeschrieben hat.",
        "Nehmen wir aber einmal an, wir würden die Beziehung zwischen Blutlauf und Nerv künstlich unterbrechen, das heißt, wir würden also künstlich den Menschen in eine solche Lage bringen, daß gleichsam der Nerv in seiner Wirk­samkeit von dem Blutlauf entfernt wird, so daß sie nicht mehr aufeinander wirken können.",
        "Das kann man schematisch in der Wei­se zeichnen, daß man die beiden Glieder weiter auseinander zeichnet, so daß eine Wechselwirkung zwischen Nerv und Blut nicht mehr stattfinden kann.",
        "Da kann die Sache so liegen, daß zunächst auf den Nerven kein Eindruck gemacht wird.",
        "So etwas kann man ja"
      ],
      [
        "# Bild s.042b"
      ],
      [
        "erreichen, indem man zum Beispiel den Nerv durchschneidet.",
        "Wenn es auf irgendeine Weise zustande kommt, daß ein Nerv durchschnit­ten ist, daß also auf den Nerv kein Eindruck gemacht wird, dann ist es ja nicht weiter wunderbar, daß der Mensch auch nichts Besonderes durch diesen Nerv erleben kann."
      ],
      [
        "Nehmen wir aber an, es werde -trotzdem die Beziehung zwischen Nerv und Blut unterbrochen ist -ein gewisser Eindruck gemacht.",
        "Im äußeren Experiment kann das ja dadurch herbeigeführt werden, daß man zum Beispiel durch einen elektrischen Strom den Nerv reizt."
      ],
      [
        "Diese äußere Beeinflussung des Nervs geht uns hier aber nichts an.",
        "Es gibt aber noch eine andere Beeinflussung des Nervs, die zu einem Zustande führt, wo er auf die Blutbahn nicht wirken kann.",
        "Dieser Zustand kann für den menschli­chen Organismus herbeigeführt werden - und er wird auch herbeige­führt - durch gewisse Vorstellungen, gewisse Ideen, Empfindungen und Gefühle, die der Mensch erlebt und sich angeeignet hat und die, damit ein solches Experiment gelinge, höhere moralische oder intel­lektuelle Vorstellungen sein sollten."
      ],
      [
        "Wenn der Mensch sich solche Vorstellungen macht, zum Beispiel von Sinnbildern, und sich in scharfer innerer Konzentration der Seele übt, dann bewirkt das, daß er gleichsam den Nerv voll in Anspruch nimmt und ihn dadurch zurückzieht vom Blutlaufe.",
        "Wenn der Mensch im wachen Bewußt­sein sich den normalen äußeren Eindrücken überläßt, wie sie gerade kommen, dann ist die natürliche Verbindung zwischen Nerv und Blutlauf da."
      ],
      [
        "Wenn der Mensch aber sich durch scharfe innere Kon­zentration von der Wirkung der äußeren Eindrücke abzieht, dann hat er ja das in der Seele, was erst im Bewußtsein entsteht; was Inhalt des Bewußtseins ist, nimmt den Nerv vorzugsweise in Anspruch und trennt dadurch die Nerventätigkeit ab von der Bluttätigkeit.",
        "Die Folge einer solchen inneren Konzentration, die - wenn sie stark genug ist - wirklich die Leitung zwischen Nerv und Blut unterbricht, ist, daß der Nerv in einer gewissen Weise befreit wird von dem Zusammenhang mit dem Blutsystem, ja auch befreit wird von dem, wofür das Blutsystem das äußere Werkzeug ist, das heißt also befreit wird von den gewöhnlichen Erlebnissen des Ich."
      ],
      [
        "Und es ist in der Tat so - und das kann vollständig experimentell belegt werden -, daß"
      ],
      [
        "durch die Erlebnisse der geistigen Schulung, die in die höheren Welten hinaufführen soll, durch die anhaltende scharfe Konzentra­tion das gesamte Nervensystem zeitweise dem gewöhnlichen Zusam­menhang mit dem Blutsystem und dessen Aufgaben für das Ich entrückt wird.",
        "Da tritt nun eine gewisse Folge ein, nämlich die, daß das Nervensystem, das früher seine Wirkung auf die Tafel des Blutes geschrieben hat, nunmehr das, was es als Wirkung in sich enthält, in sich selbst zurücklaufen läßt, in sich zurücknimmt und diese Wir­kung nicht bis zum Blut hinkommen läßt.",
        "Es ist also möglich, rein durch Vorgänge innerer Konzentration, sein Blutsystem von dem Nervensystem gleichsam abzutrennen und dadurch dasjenige, was sonst in das Ich - bildlich gesprochen - hineingeflossen wäre, zum Zurücklaufen in das Nervensystem zu bringen."
      ],
      [
        "Nun ist das Eigentümliche, daß der Mensch, wenn er durch innere Seelentätigkeit wirklich so etwas bewirkt, dann eine ganz andere Art des inneren Erlebens hat und damit vor einem vollständig veränder­ten Bewußtseinshorizont steht.",
        "Wir können sagen: Wenn Nerven und Blut in der gewöhnlichen Weise miteinander in Wechselwirkung stehen, wie es im normalen Leben der Fall ist, dann bezieht der Mensch die Eindrücke, die von außen kommen, auf sein Ich.",
        "Wenn er aber durch innere Konzentration, durch innere Seelentätigkeit sein Nervensystem heraushebt aus der Wirkung auf sein Blutsystem, dann lebt er auch nicht in seinem bisherigen gewöhnlichen Ich; er kann dann nicht in demselben Sinne zu dem, was er jetzt als sein Selbst hat, «Ich» sagen.",
        "Der Mensch erscheint sich dann so, wie wenn er einen Teil seiner Wesenheit ganz bewußt aus sich herausgehoben hätte, abgesondert von seinem Blutsystem; es ist so, wie wenn etwas, was man sonst nicht sieht, ein Übersinnliches, in unsere Nerven hereinwirkt, das sich nicht auf unsere Bluttafel abdruckt und auf unser gewöhnliches Ich keinen Eindruck macht.",
        "Der Mensch fühlt sich hinweggehoben von dem ganzen Blutsystem, gleichsam heraus­gehoben aus dem Organismus.",
        "Es ist ein bewußtes Herausheben des Ich aus dem Wirkungsbereich des Astralleibes.",
        "Während nun früher die Nerventätigkeit im Blutsystem abgebildet wurde, wird sie jetzt in sich selbst zurückreflektiert; jetzt lebt der Mensch in etwas anderem,"
      ],
      [
        "da empfindet er sich in einem anderen Ich, in einem [makrokosmi­schen] Ich, das früher nur geahnt werden konnte: Er fühlt das Her­einragen einer übersinnlichen Welt."
      ],
      [
        "Wenn wir noch einmal die Beziehung zwischen dem Nerv oder dem gesamten Nervensystem, wie es die Eindrücke einer äußeren Welt in sich hereinnimmt, zum Blut genauer schematisch zeichnen wollen, so kann es in folgender Weise geschehen:"
      ],
      [
        "# Bild s.045"
      ],
      [
        "Würden äußere Eindrücke, äußere Erlebnisse einfließen, dann würden sie sich abdrücken im Blutsystem.",
        "Haben wir aber das Ner­vensystem herausgehoben aus dem Blutsystem, dann fließt alles innerhalb des Nervensystems zurück, dann ergießt sich eine Welt, von der wir früher keine Ahnung hatten, gleichsam bis an die Enden unseres Nervensystems, und das fühlen wir als Rückstoß.",
        "Während es beim gewöhnlichen Bewußtsein so ist, daß man eine Welt auf­nimmt, die hineingeht bis zum Blutsystem, dem Blutsystem wie auf einer Tafel eingeschrieben wird, geht man nunmehr mit den Eindrük­ken nur bis dahin, wo die Nerven endigen und in sich selbst einen Widerstand finden.",
        "An diesen Nervenendungen prallt man gleichsam zurück und lebt sich hinaus in die übersinnliche Welt.",
        "Wenn wir einen Farbeneindruck haben, den wir durch das Auge empfangen, so geht er in unseren Sehnerv hinein, drückt sich ab auf der Tafel des Blutes, und wir fühlen das, was wir mit den Worten ausdrücken: Ich"
      ],
      [
        "# Bild s.046"
      ],
      [
        "sehe rot. - Nehmen wir aber an, wir gehen mit unseren Eindrücken nicht bis zum Blut hin, sondern nur bis zur Endung des Nervs, prallen da zurück, so leben wir im Grunde genommen bis zu unse­rem Sehnerv hin.",
        "Wir prallen vor dem körperlichen Ausdruck unse­res Blutes zurück, leben außerhalb unserer selbst; wir sind eigentlich in den Strahlen des Lichtes, die sonst den Eindruck «rot» in uns hervorriefen, darinnen.",
        "Wir sind also wirklich aus uns herausgekom­men, und zwar dadurch, daß wir nicht so tief in unser Inneres hereindringen, wie wir es sonst tun, sondern daß wir nur bis zu den Nervenenden gehen.",
        "Das bewirkt aber ein solches Seelenleben, das den physischen Menschen wie etwas Äußerliches empfindet und sich nicht länger mit ihm identifiziert.",
        "Das normale Bewußtsein geht bis zum Blute hin.",
        "Wenn wir aber die Seele so entwickelt haben, daß wir gleichsam an den Nervenenden kehrtmachen, dann haben wir das Blut ausgeschaltet von dem, was wir den höheren Menschen nennen, zu dem wir kommen können, wenn wir von uns selber loskommen."
      ],
      [
        "Durch diese Betrachtungen haben wir zunächst eine Anschauung von den Vorgängen gewonnen, die eintreten, wenn wir das Blutsy­stem, welches wir betrachtet haben wie eine Art Tafel, die sich auf der einen Seite den äußeren, auf der anderen Seite den inneren Ein­drücken darbietet, ausgeschaltet haben von dem, was wir nennen können den höheren Menschen, zu dem wir uns entwickeln können, wenn wir von uns selber loskommen und frei werden von den Einwirkungen des gewöhnlichen Ich.",
        "Wir werden nun am besten die ganze innere Natur dieses Blutsystems studieren können, wenn wir"
      ],
      [
        "uns nicht in allgemeinen Phrasen bewegen, sondern das am Men­schen betrachten, was real ist, den übersinnlichen, unsichtbaren Men­schen, zu dem wir uns selber aufschwingen können.",
        "Wenn wir diesen übersinnlichen Menschen so betrachten, wie er sich hineinbegibt bis zum Blute hin, dann werden wir zu dem Gedanken vorrücken kön­nen, daß der Mensch in der Außenwelt leben kann, daß er sich ergießen kann über die ganze Außenwelt, aufgehen kann in dieser Außenwelt und daß er gleichsam den umgekehrten Standpunkt ein­nehmen kann zu seinem inneren Wesen.",
        "Kurz, wir werden die Funk­tionen des Blutes und der Organe, die in den Blutkreislauf einge­schaltet sind, dadurch kennenlernen, daß wir die Frage beantworten:"
      ],
      [
        "Wie muß nun diese höhere Welt, zu der sich der Mensch aufschwin­gen kann, die er genau kennenlernen kann, sich auf die Tafel des Blutes abmalen? - Da wird sich uns das ganze differenzierte Blutle­ben als der Mittelpunkt des Menschen ergeben, wenn wir unmittelbar die Beziehungen dieses wunderbaren Systems zu einer höheren Welt betrachten.",
        "Denn das wird ja unsere Aufgabe sein, daß wir den Menschen ansehen können als eine Offenbarung des Übersinnlichen, daß wir den äußeren Menschen ansehen können als ein Abbild desje­nigen Menschen, der in der geistigen Welt wurzelt.",
        "Dadurch werden wir den menschlichen Organismus erkennen können als ein getreues Abbild des Geistes."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "DRITTER VORTRAG Prag, 22. März 1911",
    "paragraphs": [
      "Diese drei ersten Vorträge, einschließlich des heutigen, sind dazu bestimmt, uns im allgemeinen über das zu orientieren, was für das Leben, für die Wesenheit des Menschen in Betracht kommt. Daher werden in diesen ersten Vorträgen zunächst einige wichtige Begriffe gegeben werden, die ja sonst, weil die genaueren Ausführungen natürlich erst folgen sollen, ein bißchen in der Luft hängen würden. Es ist besser, wenn wir uns erst einen Überblick über die ganze Art aneignen, wie man den Menschen im okkulten Sinne zu betrachten hat, um dann in diese Betrachtung, die wir vorläufig als eine hypo­thetische hinnehmen, das hineinzubauen, was uns als die tieferen Gründe erscheinen kann.",
      "Nun habe ich am Ende des gestrigen Vortrages bereits eines ausge­führt. Ich versuchte zu zeigen, daß der Mensch durch gewisse Seelenübungen, durch starke Gedanken- und Empfindungskonzentration eine andere Art seines Lebenszustandes hervorrufen kann, als es die gewöhnliche ist. Der gewöhnliche Lebenszustand drückt sich ja da­durch aus, daß wir im wachen Tagesleben eine enge Verbindung haben zwischen Nerven und Blut. Wenn wir uns schematisch ausdrücken wollen, können wir so sagen: Was durch die Nerven geschieht, schreibt sich ein in die Tafel des Blutes. Durch Seelenübungen bringt man es nun dahin, die Nerven so stark anzuspannen, daß deren Tätigkeit sich nicht mehr hineinerstreckt bis ins Blut, sondern daß diese Tätigkeit wie in den Nerv selber zurückgeworfen wird. Weil nun das Blut das Werkzeug unseres Ich ist, fühlt sich dann ein Mensch, welcher durch starke Empfindungs- und Gedankenkonzentration gleichsam sein Nervensystem freigemacht hat vom Blute, wie entfrem­det seiner eigenen gewöhnlichen Wesenheit, wie herausgehoben aus ihr, er fühlt sich gleichsam ihr gegenüberstehend, so daß er zu dieser seiner gewöhnlichen Wesenheit nicht mehr sagen kann: das bin ich -, sondern sagen kann: das bist du. Er tritt also sich selbst so gegenüber wie einer fremden, in der physischen Welt lebenden Persönlichkeit.",
      "Wenn wir einmal ein wenig auf den Lebenszustand eines solchen, in einer gewissen Art hellsichtig gewordenen Menschen eingehen, so müssen wir sagen: Ein solcher fühlt sich so, wie wenn eine höhere Wesenheit in sein Seelenleben hineinragen würde. - Es ist dies ein ganz anderes Gefühl, als man es hat, wenn man im normalen Lebenszustand der Außenwelt gegenübersteht. Im gewöhnlichen Leben fühlt man sich den Dingen und Wesenheiten der äußeren Welt, Tieren, Pflanzen und so weiter, gegenüber fremd, man fühlt sich als ein Wesen neben ihnen oder außerhalb ihrer stehend. Man weiß ganz genau, wenn man eine Blume vor sich hat: Die Blume ist dort, und ich bin hier. - Anders ist das, wenn man auf die gekennzeichnete Art sich aus seinem sub­jektiven Ich heraushebt, wenn man durch Losreißen seines Nerven­systems vom Blutsystem in die geistige Welt hinaufsteigt. Dann fühlt man nicht mehr: da ist das fremde Wesen, das uns gegenübertritt, und hier sind wir -, sondern dann ist es so, wie wenn das andere Wesen in uns eindringen würde und wir uns mit ihm eins fühlten. So darf man sagen: Der hellsichtig werdende Mensch beginnt bei fortgeschrittener Beobachtung die geistige Welt kennenzulernen, jene geistige Welt, mit der der Mensch in steter Verbindung steht und die ja auch im gewöhn­lichen Leben durch unser Nervensystem auf dem Umwege durch die Sinneseindrücke zu uns kommt.",
      "Diese geistige Welt also, von welcher der Mensch im normalen Bewußtseinszustand zunächst nichts weiß, ist es, die sich dann einschreibt in unsere Bluttafel und dadurch in unser individuelles Ich. Wir dürfen nämlich sagen: Alle dem, was uns äußerlich in der Sinneswelt umgibt, liegt eine geistige Welt zugrunde, die wir nur wie durch einen Schleier sehen, der durch die Sinneseindrücke gewoben wird. Im normalen Bewußtsein sehen wir diese geistige Welt nicht, über die der Horizont des individuellen Ich einen Schleier ausspannt. In dem Augenblick aber, wo wir von dem Ich frei werden, erlöschen auch die gewöhnlichen Sinneseindrücke, die haben wir dann nicht. Wir leben uns hinauf in eine geistige Welt, und das ist dieselbe geistige Welt, die eigentlich hinter den Sinneseindrücken ist, mit der wir eins werden, wenn wir unser Nervensystem herausheben aus unserem gewöhn­lichen Blutorganismus.",
      "Nun haben wir mit diesen Betrachtungen gewissermaßen das menschliche Leben verfolgt, wie es von außen angeregt wird und durch die Nerven auf das Blut wirkt. Wir haben aber schon gestern darauf aufmerksam gemacht, daß wir in dem rein organischen phy­sischen Innenleben des Menschen eine Art zusammengedrückte Außenwelt sehen können, und wir haben namentlich darauf hinge­wiesen, wie eine Art in Organe zusammengedrängte Außenwelt vor­handen ist in unserer Leber, Galle und Milz. Wir können sagen: Wie das Blut nach der einen, der oberen Seite unseres Organismus das Gehirn durchläuft, um dort mit der Außenwelt in Berührung zu kommen - und das geschieht, indem auf das Gehirn die äußeren Sinneseindrücke wirken -, so kommt das Blut, wenn es sich durch den Körper bewegt, in Beziehung zu den inneren Organen, von denen wir zunächst Leber, Galle und Milz betrachtet haben. Und daß in ihnen das Blut nicht mit irgendeiner Außenwelt in Berührung kommt, dafür sorgt die Tatsache, daß diese Organe sich nicht wie Sinnesorgane nach außen aufschließen, sondern in den Organismus eingeschlossen und von allen Seiten zugedeckt sind, so daß sie nur ein inneres Leben entfalten. Diese Organe können alle auch auf das Blut nur so wirken, wie sie selbst ihrer Eigenart nach sind. Leber, Galle und Milz bekommen nicht wie das Auge oder das Ohr äußere Ein­drücke, können also auch nicht an das Blut Wirkungen weitergeben, welche von außen angeregt sind, sondern sie können in der Wirkung,",
      "# Bild s.050",
      "welche sie auf das Blut haben, nur ihre eigene Natur zum Ausdruck bringen. Wenn wir also die innere Welt betrachten, in die die Außenwelt",
      "gleichsam wie zusammengedrängt ist, so können wir sagen: Hier wirkt eine verinnerlichte Außenwelt auf das menschliche Blut. Wenn wir uns das wieder schematisch zeichnen wollen, so können wir durch den schrägen Strich A-B (siehe Zeichnung Seite 50) die Tafel des Blutes angeben, durch die oberen Pfeile können wir alles das veranschaulichen, was von außen kommend an die Bluttafel heran­dringt, und durch die unteren Pfeile alles, was von innen kommend sich der Bluttafel einschreibt. Oder, wenn wir die Sache etwas weni­ger schematisch ansehen wollen, so können wir sagen: Wenn wir das menschliche Haupt und das hindurchgehende Blut betrachten, wie es",
      "# Bild s.051",
      "beschrieben wird von außen durch die Sinnesorgane, so wirkt das Gehirn in seiner Arbeit in derselben Weise umwandelnd auf das Blut, wie die inneren Organe auf das Blut umwandelnd wirken. Denn diese drei Organe, Leber, Galle, Milz, wirken von der anderen Seite her auf",
      "das Blut, welches wir hier so zeichnen wollen, als ob es die Organe umflösse. So also würde das Blut gleichsam Strahlungen, Wirkungen empfangen können von den inneren Organen und würde damit so-zusagen als Werkzeug des Ich in diesem Ich das innere Leben dieser Organe zum Ausdruck bringen, so wie in unserem Gehirnleben das zum Ausdruck kommt, was uns in der Welt umgibt.",
      "Da müssen wir uns allerdings klar sein, daß noch etwas ganz Bestimmtes eintreten muß, damit diese Wirkungen der Organe auf das Blut möglich sind. Erinnern wir uns daran, daß wir sagten, daß in der Wechselwirkung von Nerv und Blutlauf überhaupt erst die Mög­lichkeit liegt, daß auf das Blut eine Wirkung ausgeübt, daß in das Blut sozusagen etwas eingeschrieben werden kann. Wenn von der Seite der inneren Organe her Wirkungen auf das Blut ausgeübt werden sollen, wenn gleichsam das innere Weltsystem des Menschen auf das Blut wirken soll, so muß zwischen diesen Organen und dem Blut etwas eingeschaltet sein wie ein Nervensystem. Es muß die innere Welt zuerst auf ein Nervensystem wirken können, um dann ihre Wirkungen auf das Blut übertragen zu können.",
      "So sehen wir, einfach aus einem Vergleich des unteren Teiles des Menschen mit dem oberen, daß die Voraussetzung gemacht werden muß, daß zwischen unseren inneren Organen - als deren Repräsen­tanten wir diese drei Organe: Leber, Galle, Milz haben - und dem Blutkreislauf etwas eingeschaltet sein muß wie ein Nervensystem. Fragen wir die äußere Beobachtung, so zeigt sie uns in der Tat, daß in alle diese Organe das eingeschaltet ist, was wir das sympathische Nervensystem nennen, welches die Körperhöhle des Menschen aus­füllt und welches in einem analogen Verhältnisse zu der mensch­lichen Innenwelt und dem Blutkreislauf steht, wie andererseits das Rückenmark-Nervensystem zwischen der äußeren großen Welt und dem Blutumlauf des Menschen steht. Von diesem sympathischen Nervensystem, das ja zunächst längs des Rückgrates verläuft, dann, von dort ausgehend die verschiedensten Teile des Organismus durch­zieht und sich ausbreitet, auch netzförmige Ausbreitungen zeigt, namentlich in der Bauchhöhle, wo man einen Teil dieses Systems populär auch das Sonnengeflecht nennt, von diesem sympathischen",
      "Nervensystem werden wir zu erwarten haben, daß es in einer gewis­sen Weise von dem anderen Nervensystem abweicht. Und es ist immerhin interessant - wenn es auch nicht zu einem Beweise dienen soll -, sich zu fragen: Wie könnte denn dieses Nervensystem gestaltet sein im Verhältnis zum Rückenmark-Nervensystem, wenn diese Bedingungen erfüllt würden, die wir jetzt hypothetisch gestellt haben? - Sie könnten einsehen: Wie sich das Rückenmark-Nerven­system öffnen muß dem Umkreis des Raumes, so muß dieses sympa­thische Nervensystem demjenigen zugeneigt sein, was zusammen­gedrängt ist in die innere Organisation. So verhält sich, wenn unseren Voraussetzungen entsprochen werden soll, das sympathische Ner­vensystem zu dem Rückenmark-Nervensystem etwa so, wie sich verhalten die Radien eines Kreises, die vom Mittelpunkt zur Periphe­rie gerichtet sind (siehe Zeichnung a), zu den sich von der Peripherie",
      "# Bild s.053",
      "aus nach außen fortsetzenden Radien (b). Also in einer gewissen Weise müßte ein Gegensatz vorhanden sein zwischen dem sympathi­schen Nervensystem und zwischen dem Nervensystem des Gehirnes und Rückenmarkes. Dieser Gegensatz ist auch in der Wirklichkeit vorhanden. Und da sehen wir, wie schon darin vieles für uns liegen kann, daß wir imstande sind nachzuweisen: Wenn unsere Vorausset­zungen richtig sind, dann muß die äußere Beobachtung sie in einer gewissen Weise bestätigen, und es zeigt sich, daß die äußere Beobach­tung tatsächlich bestätigt, was wir als Voraussetzung gemacht haben. Während beim sympathischen Nervensystem im wesentlichen eine Art starke Nervenknoten vorhanden sind und die Ausstrahlungen",
      "dieser Nervenknoten, die verbindenden Fäden, verhältnismäßig dünn sind und wenig in Betracht kommen gegenüber den Nervenknoten, ist bei dem Gehirn-Rückenmark-Nervensystem gerade das Umge­kehrte der Fall, da sind die verbindenden Fäden das Wesentliche, während die Nervenknoten nur eine untergeordnete Bedeutung haben. So bestätigt uns die Beobachtung in der Tat das, was wir als Voraussetzung annahmen. Wenn das sympathische Nervensystem die Aufgabe hat, die es nach dem, was wir gesagt haben, haben muß, dann muß sich das innere Leben unseres Organismus, das in der Durchnährung und Durchwärmung des Organismus zum Ausdruck kommt, gleichsam in dieses sympathische Nervensystem hineinergie­ßen, und dieses Nervensystem müßte es auf die Bluttafel geradeso übertragen, wie die äußeren Eindrücke durch das Gehirn-Rücken-mark-Nervensystem auf das Blut übertragen werden. So bekommen wir in das individuelle Ich hinein, durch das Instrument des Ich, das Blut - auf dem Umwege durch das sympathische Nervensystem -, die Eindrücke unseres eigenen körperlichen Inneren. Da aber unser körperliches Innere wie alles Physische aus dem Geiste heraus aufer­baut ist, so bekommen wir das, was sich als geistige Welt zusammen­gedrängt hat in den entsprechenden Organen des inneren Menschen, herauf in unser [waches] Ich auf dem Umwege durch das sympathi­sche Nervensystem.",
      "So sehen wir auch hier, wie sich diese Zweiheit im Menschen noch genauer ausdrückt, von der wir in unseren Betrachtungen ausgegan­gen sind. Wir sehen die Welt einmal draußen, wir sehen sie einmal drinnen wirken; beide Male sehen wir diese Welt so wirken, daß zu dieser Wirkung einmal das eine, einmal das andere Nervensystem als Werkzeug dient. Wir sehen, wie in die Mitte zwischen Außenwelt und Innenwelt hineingestellt ist unser Blutsystem, das sich wie eine Tafel von zwei Seiten beschreiben läßt, einmal von außen, einmal von innen.",
      "Nun haben wir gestern gesagt, und es heute der Deutlichkeit wegen wiederholt, daß der Mensch imstande ist, seine Nerven, inso­fern sie in die Sinneswelt hinausführen, sozusagen frei zu machen von den Wirkungen der Außenwelt auf das Blutsystem. Die Frage müssen",
      "wir uns nun vorlegen, ob auch nach der entgegengesetzten Rich­tung hin etwas Ähnliches möglich ist? Und wir werden später sehen, daß in der Tat auch solche Übungen der Seele möglich sind, welche dieselbe Wirkung, von der wir heute und gestern gesprochen haben, nach der anderen Richtung möglich machen.",
      "Jedoch besteht hier ein gewisser Unterschied. Während wir durch Gedankenkonzentration, durch Gefühlskonzentration, durch okkulte Übungen die Nerven unseres Gehirns und Rückenmarkes vom Blute losbekommen kön­nen, können wir durch solche Konzentrationen, welche gleichsam in unser Innenleben, in unsere Innenwelt hineingehen - und es sind dies namentlich diejenigen Konzentrationen, die man zusammenfassen kann unter dem Namen «mystisches Leben» -, so tief in uns eindrin­gen, daß wir allerdings unser Ich dabei, also auch sein Werkzeug, das Blut, keineswegs unberücksichtigt lassen.",
      "Die mystische Versenkung, von der wir ja wissen - was später noch genauer ausgeführt werden soll -, daß der Mensch durch sie gleichsam untertaucht in seine eigene göttliche Wesenheit, in seine eigene Geistigkeit, insofern sie in ihm liegt, diese mystische Versenkung ist nicht zunächst ein Herausheben aus dem Ich. Sie ist im Gegenteil ein Sichhineinversenken in das Ich, eine Verstärkung, ein Energischermachen, eine Steigerung der Ich-Empfindung.",
      "Davon können wir uns überzeugen, wenn wir - abge­sehen von dem, was die Mystiker der Gegenwart sagen - uns ein wenig einlassen auf ältere Mystiker. Diese älteren Mystiker, gleich­gültig, ob sie auf einem mehr oder weniger religiösen Boden stehen, sind vor allen Dingen bemüht, in ihr eigenes Ich hineinzudringen und abzusehen von alle dem, was die Außenwelt uns geben kann, um frei zu werden von allen äußeren Eindrücken und ganz in sich selber unterzutauchen.",
      "Diese innere Einkehr, dieses Untertauchen in das eigene Ich ist zunächst wie ein Zusammenziehen der ganzen Gewalt und Energie des Ich in den eigenen Organismus hinein. Das wirkt nun auf die ganze Organisation des Menschen weiter, und wir kön­nen sagen: Diese innere Versenkung, dieser im eigentlichen Sinne so zu nennende «mystische Weg» ist - im Gegensatz zu dem anderen Weg, den wir beschrieben haben - so, daß wir das Werkzeug des Ich, das Blut, nicht abziehen von dem Nerv, sondern es gerade mehr",
      "hinstoßen zum Nerv, zum sympathischen Nervensystem. Während wir also die Verbindung von Nerv und Blut lösen bei dem Vorgang, den wir gestern besprochen haben, machen wir im Gegensatz dazu durch die mystische Versenkung die Verbindung zwischen dem Blut und dem sympathischen Nervensystem stärker. Das ist das physio­logische Gegenbild: Bei der mystischen Versenkung wird das Blut tiefer hineingedrängt zu dem sympathischen Nervensystem, während bei der anderen Art seelischer Übungen das Blut vom Nerv abge­drängt wird. Es ist also wie ein Eindrücken des Blutes in das sympa­thische Nervensystem, was in der mystischen Versenkung vor sich geht.",
      "Nehmen wir nun an, wir könnten für eine Weile von dem absehen, daß der Mensch, wenn er in mystischer Versenkung in sein Inneres hineingeht, nicht loskommt von seinem Ich, sondern es im Gegenteil tiefer hineindrängt in sein Inneres und dabei alle schlechten, alle minder guten Eigenschaften, die er hat, mitnimmt. Wenn man sich in sein Inneres hineinversenkt, ist man sich zunächst nicht klar, daß man auch alle minder guten Eigenschaften hineindrückt in dieses Innere, mit anderen Worten, daß alles, was im leidenschaftlichen Blute ist, mit hineingeprägt wird in das sympathische Nervensystem.",
      "Aber nehmen wir an, wir könnten eine Weile davon absehen und uns sagen, der Mystiker habe Sorge getragen, bevor er zu einer solchen mystischen Versenkung gekommen ist, daß die minder guten Eigen­schaften immer mehr und mehr verschwunden sind und daß anstelle der egoistischen Eigenschaften selbstlose, altruistische Gefühle getre­ten sind, er habe sich dadurch vorbereitet, daß er versuchte, das Gefühl des Mitleides mit allen Wesen in sich rege zu machen, um die Eigenschaften, die nur auf das Ich hinspekulieren, zu paralysieren durch selbstloses Mitgefühl für alle Wesen. Nehmen wir also an, der Mensch habe sich genügend sorgfältig vorbereitet, um sich in sein Inneres hinein zu versenken.",
      "Trägt der Mensch dann das Ich durch das Werkzeug seines Blutes in seine innere Welt hinein, dann kommt es dazu, daß dieses innere Nervensystem, das sympathische Nerven­system, von dem der Mensch im normalen Bewußtsein natürlich nichts weiß, hereinrückt in das Ich-Bewußtsein, daß er anfängt zu",
      "wissen: Du hast da in dir etwas, das dir ein Ähnliches von deiner inneren Welt vermitteln kann, wie dein Gehirn-Rückenmark-Ner­vensystem dir die äußere Welt vermittelt. - Man wird gewahr seines sympathischen Nervensystems, und wie man durch das Gehirn­Rückenmark-Nervensystem die äußere Welt erkennen kann, so kommt einem jetzt entgegen die innere Welt. Aber wie wir bei den äußeren Eindrücken auch nicht die Nerven selbst sehen, sondern durch die Sehnerven die äußere Welt in unser Bewußtsein herein­dringt, so dringen bei der mystischen Versenkung auch nicht die inneren Nerven ins Bewußtsein herein; der Mensch wird nur gewahr, daß er in ihnen ein Instrument hat, durch das er in das Innere schauen kann. Es tritt etwas ganz anderes ein, es tritt vor dem nach innen zu hellsichtig gewordenen menschlichen Erkenntnisvermögen die innere Welt auf. Wie uns der Blick nach außen die Außenwelt erschließt, und uns dabei nicht unsere Nerven zum Bewußtsein kommen, so kommt uns auch nicht unser sympathisches Nervensystem zum Bewußtsein, wohl aber das, was sich uns als Innenwelt entgegenstellt. Nur müssen wir sehen, daß diese Innenwelt, die uns da zum Bewußt­sein kommt, eigentlich wir selbst als physischer Mensch sind.",
      "Vielleicht liegt es nicht besonders nahe, aber ich möchte doch sagen: Einem ein klein wenig materialistischen Denker könnte eine Art von Horror aufsteigen, wenn er sich sagen sollte, daß er seinen eigenen Organismus von innen sehen kann, und er könnte vielleicht meinen: Da sehe ich aber auch etwas Rechtes, wenn ich durch mein sympathisches Nervensystem hellsichtig werde und meine Leber, Galle und Milz zu sehen bekomme! - Ich meine, es muß ja nicht besonders naheliegen, aber man könnte es sich doch sagen. So ist die Sache aber nicht. Denn bei einem solchen Einwand würde man nicht berücksichtigen, daß der Mensch im gewöhnlichen Leben seine Leber, Galle und Milz und so weiter von außen anschaut wie die anderen äußeren Gegenstände auch. So wie Sie in der Anatomie, in der gewöhnlichen Physiologie Leber, Galle, Milz und so weiter kennenlernen, wenn Sie einen Menschen aufschneiden, sind diese Organe natürlich durch die äußeren Sinne, durch das Gehirn-Rük­kenmark-Nervensystem angeschaut, geradeso wie irgend etwas anderes.",
      "Aber in einer ganz anderen Lage ist der Mensch, wenn er versucht, sein sympathisches Nervensystem zu gebrauchen, um nach innen hellsichtig zu werden. Da sieht er keineswegs dasselbe, was er von außen sehen kann, sondern da sieht er das, um dessentwillen die Hellseher aller Zeiten so sonderbare Namen für diese Organe gewählt haben, wie ich sie Ihnen im zweiten Vortrage angeführt habe.",
      "Da wird er nämlich gewahr, daß in der Tat dem äußeren Anschauen durch das Gehirn-Rückenmark-Nervensystem diese Organe als Maja, in äußerer Illusion erscheinen in dem Anblick, den sie nach außen bieten, nicht in ihrer inneren wesenhaften Bedeutung. Man sieht in der Tat etwas ganz anderes, wenn man mit dem nach innen gewendeten Auge diese seine innere Welt hellseherisch belau­schen kann.",
      "Da wird man nach und nach gewahr, warum die Hellse­her aller Zeiten einen Zusammenhang der Organe mit den Wirkun­gen der Planeten gesehen haben. Wie wir gestern gesagt haben, wurde die Milzwirkung mit dem Namen des Saturn, die Leberwirkung mit dem Jupiter und die Gallewirkung mit dem Mars in Zusammenhang gebracht.",
      "Denn was man im eigenen Inneren sieht, das ist in der Tat grundverschieden von dem, was sich dem äußeren Anblick darbietet. Da wird man gewahr, daß man wirklich in den inneren Organen umgrenzte, zusammengeschlossene Partien der Außenwelt vor sich hat.",
      "Vor allem wird eines klar, was uns zunächst als ein Beispiel dienen soll: Durch diese Art zu einer Erkenntnis zu kommen, die über das gewöhnliche Anschauen hinausführt, können wir uns davon überzeugen, daß die menschliche Milz ein sehr bedeutungsvolles Organ ist. Dieses Organ erscheint ja der inneren Betrachtung wirk­lich so, als wenn es nicht aus äußerer Substanz, aus fleischlicher Materie bestehen würde, sondern - wenn der Ausdruck gestattet ist, obwohl er nur annähernd das wiedergeben kann, was gesehen wird -die Milz erscheint tatsächlich wie ein leuchtender Weltenkörper im kleinen mit allem möglichen inneren Leben, das sehr kompliziert ist.",
      "Ich habe Sie gestern darauf aufmerksam gemacht, daß die Milz, äußerlich betrachtet, beschrieben werden kann als ein blutreiches Gewebe, eingebettet darin die erwähnten weißen Körperchen. So daß",
      "man von einer äußeren physiologischen Betrachtung ausgehend sa­gen kann, daß das Blut, welches sich durch die Milz ergießt, durch sie wie durch ein Sieb durchgesiebt wird. Der inneren Betrachtung aber stellt sich die Milz dar als ein Organ, das durch mannigfache innere Kräfte in eine beständige rhythmische Bewegung gebracht wird.",
      "Wir überzeugen uns schon bei einem solchen Organ davon, daß im Grunde genommen in der Welt ungeheuer viel auf Rhythmus ankommt. Eine Ahnung von der Bedeutung des Rhythmus im Gesamtleben der Welt können wir ja bekommen, wenn wir den äußeren Rhythmus des Kosmos wiedererkennen im Blut-Pulsschlag.",
      "Auch äußerlich können wir den Rhythmus in den Organen, auch in dem Organ der Milz, ziemlich genau verfolgen. Für den, der mit nach innen gewendetem hellseherischen Blick die Organe anschaut, dem offenbaren sich die Differenzierungen der Milz wie in einem Licht-körper, sie sind dazu da, um der Milz einen gewissen Rhythmus im Leben zu geben.",
      "Dieser Rhythmus unterscheidet sich von anderen Rhythmen, die wir sonst gewahr werden, ganz beträchtlich. Und gerade bei der Milz ist es interessant zu studieren, wie sich dieser Rhythmus der Milz ganz beträchtlich unterscheidet von jedem ande­ren Rhythmus; er ist nämlich weit weniger regelmäßig als andere Rhythmen.",
      "Warum? Dies ist aus dem Grunde der Fall, weil die Milz in einer gewissen Weise naheliegt dem menschlichen Ernährungsap­parat und mit demselben etwas zu tun hat. Das werden Sie gleich verstehen, wenn wir ein wenig darauf Rücksicht nehmen, wie unge­heuer regelmäßig beim Menschen der Rhythmus des Blutes sein muß, damit das Leben in einer richtigen Weise aufrechterhalten werden kann.",
      "Das muß ein sehr regelmäßiger Rhythmus sein. Aber es gibt einen anderen Rhythmus, und der ist nur in geringem Maße regelmä­ßig, obwohl von ihm zu wünschen wäre, daß er durch die Selbster­ziehung der Menschen immer regelmäßiger und regelmäßiger würde, namentlich in dem kindlichen Lebensalter: das ist der Rhythmus, in dem wir uns ernähren, der Rhythmus von Essen und Trinken.",
      "Einen gewissen Rhythmus hält darin ja wohl ein einigermaßen ordentlicher Mensch ein; er nimmt zu bestimmten Zeiten seine Tagesmahlzeiten, das Frühstück, das Mittagessen und das Nachtmahl ein, so daß er",
      "dadurch doch einen gewissen Rhythmus hat. Aber wie ist es mit diesem Rhythmus eigentlich bestellt? In vieler Hinsicht - das ist ja traurig bekannt - wird diese Regelmäßigkeit durchbrochen durch das Entgegenkommen vieler Eltern gegenüber der Genäschigkeit ihrer Kinder, denen man einfach dann etwas gibt, wenn sie gerade danach Verlangen haben, wobei abgesehen wird von allem Rhythmus.",
      "Und auch die Erwachsenen sind nicht gerade so ungeheuer darauf aus, immer einen genauen Rhythmus in bezug auf Essen und Trinken einzuhalten. Das soll gar nicht in pedantischer oder moralisierender Weise gemeint sein, denn das moderne Leben macht das nicht immer möglich.",
      "Wie unregelmäßig die Nahrung in den Menschen hineinge-stopft wird, wie unregelmäßig namentlich getrunken wird, das ist ja hinlänglich bekannt und soll nicht getadelt, sondern nur erwähnt werden. Es muß aber das, was wir in einer mangelhaften rhythmi­schen Art unserem Organismus zuführen, allmählich so umrhythmi­siert werden, daß es sich in den regelmäßigeren Rhythmus des Orga­nismus einfügt; es muß so umgeschaltet werden, daß wenigstens die gröbsten Unregelmäßigkeiten in der Nahrungsaufnahme beseitigt werden.",
      "Nehmen wir an, ein Mensch sei durch seinen Beruf gezwun­gen, um acht Uhr morgens zu frühstücken und um ein oder zwei Uhr zu Mittag zu essen, und diese regelmäßige Tageseinteilung sei ihm eine Gewohnheit. Nun nehmen wir weiter an, er würde zu einem guten Freunde gehen, und da gebiete es ihm die sonst ja nicht genug zu lobende Höflichkeit, zwischen diesen beiden Mahlzeiten eine Erfrischung zu sich zu nehmen.",
      "Damit hat er den gewohnten Rhyth­mus seiner Nahrungsaufnahme in einer ganz erheblichen Weise durchbrochen, und dadurch wird auf den Rhythmus seines Organis­mus eine ganz bestimmte Wirkung ausgeübt. Es muß nun etwas da sein im Organismus, das in entsprechender Weise dasjenige stärker macht, was regelmäßig im Rhythmus ist und was die Wirkung dessen abschwächen muß, was unregelmäßig ist.",
      "Es müssen die gröbsten Unregelmäßigkeiten ausgeglichen werden, so daß beim Übergehen der Nahrungsmittel auf das Blutsystem ein Organ eingeschaltet sein muß, das die Unregelmäßigkeit des Ernährungsrhythmus ausgleicht gegenüber der notwendigen Regelmäßigkeit des Blutrhythmus.",
      "dieses Organ ist die Milz. So können wir an ganz bestimmten rhyth­mischen Vorgängen, wie es jetzt charakterisiert worden ist, einen Begriff dafür erhalten, daß die Milz ein Umschalter ist, um Unregel­mäßigkeiten im Verdauungskanal so auszugleichen, daß sie zu Regel­mäßigkeiten werden in der Blutzirkulation. Denn es wäre in der Tat eine ganz fatale Sache, wenn gewisse Unregelmäßigkeiten in dem Aufnehmen von Nahrungsstoffen - namentlich in der Studentenzeit oder auch zu anderen Zeiten - ihre ganze Wirkung fortsetzen müßten in das Blut hinein. Da ist viel auszugleichen, und es ist nur so viel auf das Blut überzuleiten, als diesem zuträglich ist. Diese Aufgabe hat das in die Blutbahn eingeschaltete Milzorgan, das seine rhythmisie­rende Wirkung so ausstrahlt über den ganzen menschlichen Organis­mus, daß das zustande kommt, was jetzt beschrieben worden ist.",
      "Was wir jetzt hervorgeholt haben aus dem Einblick des hellsehend gewordenen Auges, zeigt sich auch der äußeren Beobachtung, näm­lich daß die Milz einen gewissen Rhythmus einhält. Es ist außeror­dentlich schwierig, durch die äußeren physiologischen Untersuchun­gen allein diese Aufgabe der Milz herauszufinden, man kann aber durch äußerliche Beobachtung feststellen, daß die Milz gewisse Stun­den hindurch nach einer reichlich genossenen Mahlzeit angeschwol­len ist und daß sie, wenn nicht wieder nachgeschoben wird, sich wieder zusammenzieht, wenn eine angemessene Zeit vergangen ist. Durch eine gewisse Ausdehnung und Zusammenziehung dieses Organs wird die Unregelmäßigkeit in der Nahrungsaufnahme auf den Rhythmus des Blutes umgeschaltet. Und wenn Sie sich dessen bewußt sind, daß der menschliche Organismus nicht bloß das ist, als was man ihn oft beschreibt, nämlich eine Summe seiner Organe, sondern daß alle Organe ihre geheimen Wirkungen nach allen Teilen des Organismus hinschicken, so werden Sie sich auch vorstellen können, daß die rhythmische Tätigkeit der Milz von der Außenwelt, nämlich von der Zuführung der Nahrungsmittel abhängt, und daß diese rhythmischen Bewegungen der Milz ausstrahlen in den ganzen Organismus und über den ganzen Organismus hin ausgleichend wirken können. Das ist zwar nur eine Art, wie die Milz wirkt; denn es ist unmöglich, alle Arten gleich anzuführen.",
      "Es wäre nun in der Tat außerordentlich interessant zu sehen, ob die äußere Physiologie solche Dinge, wie sie eben ausgesprochen wur­den, bestätigen würde, wenn sie dieselben - da ja nicht alle Menschen gleich hellsehend werden können - hinnehmen würde, ich möchte sagen, wie eine «hingeworfene Idee», wenn also zunächst gesagt würde: Ich will mir einmal vorstellen, daß es doch nicht so ganz verdrehtes Zeug ist, was die Okkultisten sagen, ich will es einmal weder glauben noch nicht glauben, sondern es als Idee dahingestellt sein lassen und prüfen, ob sich davon irgend etwas durch die äußere Physiologie beweisen läßt. - Dann könnten Untersuchungen der äußeren Physiologie angestellt werden, die den Beweis erbringen könnten für das, was aus hellseherischer Beobachtung heraus gewon­nen wurde.",
      "Eine solche Bestätigung haben wir ja schon genannt, das Ausdeh­nen und Zusammenziehen der Milz. Es zeigt sich, weil die Ausdeh­nung der Milz auf die Einnahme einer Mahlzeit folgt, daß sie von der Nahrungsaufnahme abhängig ist. So haben wir in der Milz ein Organ gefunden, das nach der einen Seite hin von menschlicher Willkür abhängig ist, auf der anderen Seite, nach der Blutseite hin, die Unre­gelmäßigkeiten der menschlichen Willkür beseitigt, sie ablähmt, das heißt sie umschaltet auf den Rhythmus des Blutes, und dadurch das Physische des Menschen sozusagen erst seiner Wesenheit gemäß gestaltet werden kann. Denn soll der Mensch seiner Wesenheit gemäß gestaltet sein, dann muß ja namentlich das Mittelpunktswerk-zeug seiner Wesenheit, das Blut, in der richtigen Weise seine Wir­kung ausüben können, in dem eigenen Blutrhythmus. Es muß der Mensch, insofern er Träger seines Blutkreislaufes ist, in sich abgeson­dert, isoliert sein von dem, was draußen in der Außenwelt unregel­mäßig vorgeht, und von dem, was auf den Menschen dadurch ein­wirkt, daß er völlig unrhythmisch sich seine Nahrung einverleibt.",
      "Es ist also ein Isolieren, ein Unabhängigmachen der menschlichen Wesenheit von der Außenwelt. Jedes solches Individualisieren, SeIb­ständigmachen einer Wesenheit nennt man im Okkultismus «Satur­nisch», etwas, das durch Saturnwirkung herbeigeführt wird. Das ist die ursprüngliche Idee, das Wesentliche des Saturnischen: daß aus",
      "einem umfassenden Gesamtorganismus ein Wesen herausgestellt, iso­liert, individualisiert wird, so daß es in sich selber eine gesonderte Regelmäßigkeit entfalten kann. Ich will jetzt davon absehen, daß ja von unserer heutigen Astronomie außerhalb der Saturnbahn noch Uranus und Neptun zu unserem Sonnensystem gerechnet werden. Für den Okkultisten ist alles das, was an Kräften vorhanden ist, um unser Sonnensystem aus der übrigen Welt herauszuheben, abzuson­dern, zu isolieren und zu individualisieren, ihm eine Eigengesetzlich­keit zu geben, in den Saturnkräften gegeben.",
      "# Bild s.063",
      "Alle diese Kräfte sind in dem gegeben, was in unserem Sonnen­system der äußerste Planet ist. Wenn man sich die Welt vorstellt, könnte man sagen, daß innerhalb der Kreisbahn des Saturns das Sonnensystem so darinnen ist, daß es innerhalb dieser Bahn seinen eigenen Gesetzen folgen kann und sich unabhängig machen kann, indem es sich herausreißt aus der Umwelt und den gestaltenden Kräften der Umwelt. Aus diesem Grunde sahen die Okkultisten aller Zeiten in den saturnhaften Kräften das, was unser Sonnensystem in",
      "sich selber abschließt, was es dem Sonnensystem möglich macht, einen eigenen Rhythmus zu entfalten, der nicht derselbe ist wie der Rhythmus draußen, der außerhalb der Welt unseres Sonnensystems herrscht.",
      "Etwas Ähnlichem begegnen wir in unserem Organismus bei der Milz. In unserem Organismus haben wir es zwar nicht zu tun mit einem Absondern gegen die ganze äußere Welt, sondern nur von einer Umwelt, insofern sie die Nahrungsmittel für unseren Organis­mus enthält. In der Milz haben wir dasjenige Organ im Körper zu sehen, das alles, was von draußen kommt, so behandelt, wie das innerhalb der Saturnbahn des Sonnensystems Liegende von den Saturnkräften behandelt wird: daß es zuerst umrhythmisiert wird in den Rhythmus und die Gesetzmäßigkeit des Menschen. Was durch die Milz geschieht, das isoliert unseren Blutkreislauf von allen äuße­ren Wirkungen, das macht ihn zu einem in sich selber regelmäßigen System, das seinen eigenen Rhythmus haben kann.",
      "Damit kommen wir schon den Gründen etwas näher, die im Okkultismus für die Wahl von Planetennamen für die Organe maß­gebend waren. In den okkulten Schulen wurden diese Namen ursprünglich nicht bloß auf die einzelnen physisch sichtbaren Plane­ten angewendet. Der Name «Saturn» zum Beispiel wurde ja, wie schon gesagt, auf alles angewendet, was bewirkt, daß sich etwas aus einer größeren Gesamtheit aussondert und sich abschließt zu einem System, das in sich selber rhythmisch gestaltet ist. Daß ein System sich abschließt und sich in sich selbständig rhythmisch gestaltet, hat einen gewissen Nachteil für die gesamte Weltentwickelung, und das hat immer die Okkultisten ein wenig bekümmert. Es ist ja leicht verständlich, daß in der kleinen und in der großen Welt alle Wirkun­gen zueinander in Beziehungen stehen, daß alle sich aufeinander beziehen. Wenn nun irgend etwas, sei es ein Sonnensystem, sei es das Blutsystem des Menschen, sich herausgliedert aus der ganzen Umwelt und einer Eigengesetzmäßigkeit folgt, so bedeutet das, daß ein solches System die äußeren umfassenden Gesetze durchbricht, verletzt, daß es sich verselbständigt gegenüber den äußeren Gesetzen und sich eigene innere Gesetze und einen eigenen Rhythmus schafft,",
      "welche denen der Umwelt zunächst widersprechen. Wir werden sehen, wie das auch auf den physischen Menschen bezogen werden kann, obwohl es uns nach den ganzen Auseinandersetzungen des heutigen Vortrages klar sein muß, daß es zunächst für den Menschen segensreich ist, daß er diesen durch das Saturnische der Milz geschaf­fenen inneren Rhythmus erhalten hat.",
      "Aber wir werden doch sehen, daß ein Wesen, sei es ein Planet, sei es ein Mensch, durch das Sich­abschließen in sich selber sich in einen Widerspruch bringt zur umliegenden Welt. Es ist ein Widerspruch geschaffen zwischen dem, was um uns ist, und dem, was in uns ist.",
      "Dieser Widerspruch, der nun einmal vorhanden ist, kann nicht früher ausgeglichen werden, als bis sich der im Inneren hergestellte Rhythmus dem äußeren Rhythmus wieder völlig angepaßt hat. Wir werden noch sehen, wie dies auch auf den physischen Menschen bezogen wird; denn so, wie es jetzt gesagt worden ist, sieht es aus, als ob der Mensch sich anpassen müßte an die Unregelmäßigkeit.",
      "Wir werden aber sehen, daß es anders ist. Der innere Rhythmus muß, nachdem er sich hergestellt hat, danach stre­ben, sich wiederum mit der ganzen äußeren Welt gleich zu gestalten, das heißt, sich selber aufzuheben.",
      "Das heißt also: Die Wesenheit, die im Inneren entsteht und selbständig arbeitet, muß das Bestreben haben, sich wiederum an die Außenwelt anzupassen und dieser Außenwelt gegenüber so zu werden, wie diese selber ist. Mit anderen Worten: Alles, was durch eine saturnische Wirkung verselbständigt wird, das wird zugleich durch diese saturnische Wirkung dazu ver­urteilt, sich selber wieder zu zerstören.",
      "Der Mythos drückt das im Bilde aus: Saturn - oder Kronos - verzehrt seine eigenen Kinder.",
      "So sehen Sie einen tiefen Einklang herrschen zwischen einer okkul­ten Idee und einem Mythos, der dasselbe ausdrückt im Bilde, im Symbol: Kronos verzehrt seinen eigenen Kinder. - Wenn man solche Dinge in immer größerer und größerer Zahl auf sich wirken läßt, so bildet sich für die Beziehungen der angedeuteten Art ein feines Gefühl heraus, und dann wird es nach einiger Zeit nicht mehr so leicht möglich sein, wie es die äußerliche Aufklärung tun möchte, zu sagen: Nun ja, da träumen einige Phantasten davon, daß in den alten Mythen und Sagen bildliche Ausprägungen tiefer Weisheiten enthalten",
      "seien. - Wenn man zwei, drei oder auch zehn solcher Entspre­chungen hört, noch dazu so, wie sie oft in der Literatur dargeboten werden, nämlich in recht äußerlicher Weise, dann kann man sich ganz gewiß dagegen auflehnen, daß in Mythen und Sagen tiefere Weisheiten enthalten seien als in der äußeren Wissenschaft. Aber wer tiefer auf die Sache eingeht, der findet bewahrheitet, daß Mythen und Sagen tiefer hineinführen in das wirkliche Wesen der Welt und der Organbildung, als es der äußeren wissenschaftlichen Betrachtungs­weise möglich ist.",
      "Wer immer wieder solche Bilder auf sich wirken läßt, wie sie in den wunderbaren Mythen und Sagen über den ganzen Erdkreis hin verstreut sind, der kann bei liebevollem Eingehen auf diese Bilder in dem ganzen Fühlen und Denken der Völker, in den bildhaften Vorstellungen der Menschen, die Umgestaltung tiefster Weisheiten finden. Dann begreift man, warum einige Okkultisten sagen können, derjenige habe erst Mythen und Sagen wirklich begrif­fen, der durch sie in die okkulte Physiologie der menschlichen Natur eingedrungen sei. - Mehr als die äußere Wissenschaft erfaßt, enthal­ten Mythen und Sagen wirkliche Weisheiten über das menschliche Wesen, wirkliche Physiologie.",
      "Wenn die Menschen einmal ergründen werden, wieviel Physiologie zum Beispiel in solchen Namen wie Kain und Abel und ihrer Nachfolgeschaft liegt - diese alten Namen rühren ja aus Zeiten her, in denen man in die Namen noch einen inneren Sinn hineinprägte -, dann werden die Menschen einen unge­heuren Respekt, eine ungeheure Ehrfurcht bekommen vor alle dem, was im Laufe des geschichtlichen Werdens von weisheitsvollen Men­schen ersonnen worden ist, um da, wo in die geistigen Welten noch nicht hineingeschaut werden kann, die Seelen durch Bilder ihren Zusammenhang mit diesen geistigen Welten erleben zu lassen. Da wird einem gründlich vertrieben der Hochmut, der in dem Worte steckt, das in unserer Zeit eine viel zu große Rolle spielt: Wie haben wir es heute so herrlich weit gebracht! -, womit man meint: Wie haben wir abgestreift die alten bildhaften Ausdrücke der Urmensch­heitsweistümer.",
      "Die streift man gründlich ab, wenn man sich nicht mit inniger Liebe in den Gang der Menschheitsentwickelung durch die verschiedenen",
      "Epochen hindurch versenkt. Was der Hellseher mit dem geöff­neten inneren Auge als die innere Natur der menschlichen Organe physiologisch ergründet, das drückt sich in Bildern aus und läßt ihn sehen, daß die Mythen und Sagen gleichsam die menschliche Her­kunft enthalten. Der Hellseher sieht in den Mythen und Sagen ausge­drückt diesen Wunderprozeß, daß Welten zusammengedrängt wor­den sind in menschliche Organe. Er sieht, wie sich im Laufe unend­lich langer Zeiten die Organe zusammenkristallisiert haben, um zu dem werden zu können, was als Milz, als Leber, als Galle in uns wirkt. Wir werden morgen noch weiter darüber sprechen. Um das alles in Bildern ausdrücken zu können, dazu gehört wahrhaftig eine tiefe Weisheit, ein tiefes Wissen von dem, was wir durch die okkulte Wissenschaft erst erahnen. Was in unserem inneren menschlichen Organismus wirkt, das ist aus Welten herausgeboren wie ein Mikro-kosmos aus dem Makrokosmos, und wir sehen alle diese ungeheuren Weistümer ausgedrückt in Mythen und Sagen. Deshalb haben jene Okkultisten Recht, die in den Namen der Mythen und Sagen erst einen Sinn finden, wenn sie darin die Physiologie erkennen.",
      "Darauf sollte heute nur hingedeutet werden, weil es dazu dienen kann, uns jene Ehrfurcht anzueignen, von der in der ersten Stunde gesprochen worden ist. Wenn wir eine solche Betrachtungsweise üben, können wir wirklich hinweisen auf das, was sich einer tieferen Erforschung des geistigen Inhaltes der menschlichen Organe darbie­tet. Auch wenn wir das nur für ganz weniges darstellen können, so wird sich uns doch schon zeigen, welcher Wunderbau dieser mensch­liche Organismus ist. Und ein wenig werden wir gerade in diesem Vortragszyklus hineinzuleuchten versuchen in diese innere Wesen­heit des Menschen."
    ],
    "sentences": [
      [
        "Diese drei ersten Vorträge, einschließlich des heutigen, sind dazu bestimmt, uns im allgemeinen über das zu orientieren, was für das Leben, für die Wesenheit des Menschen in Betracht kommt.",
        "Daher werden in diesen ersten Vorträgen zunächst einige wichtige Begriffe gegeben werden, die ja sonst, weil die genaueren Ausführungen natürlich erst folgen sollen, ein bißchen in der Luft hängen würden.",
        "Es ist besser, wenn wir uns erst einen Überblick über die ganze Art aneignen, wie man den Menschen im okkulten Sinne zu betrachten hat, um dann in diese Betrachtung, die wir vorläufig als eine hypo­thetische hinnehmen, das hineinzubauen, was uns als die tieferen Gründe erscheinen kann."
      ],
      [
        "Nun habe ich am Ende des gestrigen Vortrages bereits eines ausge­führt.",
        "Ich versuchte zu zeigen, daß der Mensch durch gewisse Seelenübungen, durch starke Gedanken- und Empfindungskonzentration eine andere Art seines Lebenszustandes hervorrufen kann, als es die gewöhnliche ist.",
        "Der gewöhnliche Lebenszustand drückt sich ja da­durch aus, daß wir im wachen Tagesleben eine enge Verbindung haben zwischen Nerven und Blut.",
        "Wenn wir uns schematisch ausdrücken wollen, können wir so sagen: Was durch die Nerven geschieht, schreibt sich ein in die Tafel des Blutes.",
        "Durch Seelenübungen bringt man es nun dahin, die Nerven so stark anzuspannen, daß deren Tätigkeit sich nicht mehr hineinerstreckt bis ins Blut, sondern daß diese Tätigkeit wie in den Nerv selber zurückgeworfen wird.",
        "Weil nun das Blut das Werkzeug unseres Ich ist, fühlt sich dann ein Mensch, welcher durch starke Empfindungs- und Gedankenkonzentration gleichsam sein Nervensystem freigemacht hat vom Blute, wie entfrem­det seiner eigenen gewöhnlichen Wesenheit, wie herausgehoben aus ihr, er fühlt sich gleichsam ihr gegenüberstehend, so daß er zu dieser seiner gewöhnlichen Wesenheit nicht mehr sagen kann: das bin ich -, sondern sagen kann: das bist du.",
        "Er tritt also sich selbst so gegenüber wie einer fremden, in der physischen Welt lebenden Persönlichkeit."
      ],
      [
        "Wenn wir einmal ein wenig auf den Lebenszustand eines solchen, in einer gewissen Art hellsichtig gewordenen Menschen eingehen, so müssen wir sagen: Ein solcher fühlt sich so, wie wenn eine höhere Wesenheit in sein Seelenleben hineinragen würde. - Es ist dies ein ganz anderes Gefühl, als man es hat, wenn man im normalen Lebenszustand der Außenwelt gegenübersteht.",
        "Im gewöhnlichen Leben fühlt man sich den Dingen und Wesenheiten der äußeren Welt, Tieren, Pflanzen und so weiter, gegenüber fremd, man fühlt sich als ein Wesen neben ihnen oder außerhalb ihrer stehend.",
        "Man weiß ganz genau, wenn man eine Blume vor sich hat: Die Blume ist dort, und ich bin hier. - Anders ist das, wenn man auf die gekennzeichnete Art sich aus seinem sub­jektiven Ich heraushebt, wenn man durch Losreißen seines Nerven­systems vom Blutsystem in die geistige Welt hinaufsteigt.",
        "Dann fühlt man nicht mehr: da ist das fremde Wesen, das uns gegenübertritt, und hier sind wir -, sondern dann ist es so, wie wenn das andere Wesen in uns eindringen würde und wir uns mit ihm eins fühlten.",
        "So darf man sagen: Der hellsichtig werdende Mensch beginnt bei fortgeschrittener Beobachtung die geistige Welt kennenzulernen, jene geistige Welt, mit der der Mensch in steter Verbindung steht und die ja auch im gewöhn­lichen Leben durch unser Nervensystem auf dem Umwege durch die Sinneseindrücke zu uns kommt."
      ],
      [
        "Diese geistige Welt also, von welcher der Mensch im normalen Bewußtseinszustand zunächst nichts weiß, ist es, die sich dann einschreibt in unsere Bluttafel und dadurch in unser individuelles Ich.",
        "Wir dürfen nämlich sagen: Alle dem, was uns äußerlich in der Sinneswelt umgibt, liegt eine geistige Welt zugrunde, die wir nur wie durch einen Schleier sehen, der durch die Sinneseindrücke gewoben wird.",
        "Im normalen Bewußtsein sehen wir diese geistige Welt nicht, über die der Horizont des individuellen Ich einen Schleier ausspannt.",
        "In dem Augenblick aber, wo wir von dem Ich frei werden, erlöschen auch die gewöhnlichen Sinneseindrücke, die haben wir dann nicht.",
        "Wir leben uns hinauf in eine geistige Welt, und das ist dieselbe geistige Welt, die eigentlich hinter den Sinneseindrücken ist, mit der wir eins werden, wenn wir unser Nervensystem herausheben aus unserem gewöhn­lichen Blutorganismus."
      ],
      [
        "Nun haben wir mit diesen Betrachtungen gewissermaßen das menschliche Leben verfolgt, wie es von außen angeregt wird und durch die Nerven auf das Blut wirkt.",
        "Wir haben aber schon gestern darauf aufmerksam gemacht, daß wir in dem rein organischen phy­sischen Innenleben des Menschen eine Art zusammengedrückte Außenwelt sehen können, und wir haben namentlich darauf hinge­wiesen, wie eine Art in Organe zusammengedrängte Außenwelt vor­handen ist in unserer Leber, Galle und Milz.",
        "Wir können sagen: Wie das Blut nach der einen, der oberen Seite unseres Organismus das Gehirn durchläuft, um dort mit der Außenwelt in Berührung zu kommen - und das geschieht, indem auf das Gehirn die äußeren Sinneseindrücke wirken -, so kommt das Blut, wenn es sich durch den Körper bewegt, in Beziehung zu den inneren Organen, von denen wir zunächst Leber, Galle und Milz betrachtet haben.",
        "Und daß in ihnen das Blut nicht mit irgendeiner Außenwelt in Berührung kommt, dafür sorgt die Tatsache, daß diese Organe sich nicht wie Sinnesorgane nach außen aufschließen, sondern in den Organismus eingeschlossen und von allen Seiten zugedeckt sind, so daß sie nur ein inneres Leben entfalten.",
        "Diese Organe können alle auch auf das Blut nur so wirken, wie sie selbst ihrer Eigenart nach sind.",
        "Leber, Galle und Milz bekommen nicht wie das Auge oder das Ohr äußere Ein­drücke, können also auch nicht an das Blut Wirkungen weitergeben, welche von außen angeregt sind, sondern sie können in der Wirkung,"
      ],
      [
        "# Bild s.050"
      ],
      [
        "welche sie auf das Blut haben, nur ihre eigene Natur zum Ausdruck bringen.",
        "Wenn wir also die innere Welt betrachten, in die die Außenwelt"
      ],
      [
        "gleichsam wie zusammengedrängt ist, so können wir sagen: Hier wirkt eine verinnerlichte Außenwelt auf das menschliche Blut.",
        "Wenn wir uns das wieder schematisch zeichnen wollen, so können wir durch den schrägen Strich A-B (siehe Zeichnung Seite 50) die Tafel des Blutes angeben, durch die oberen Pfeile können wir alles das veranschaulichen, was von außen kommend an die Bluttafel heran­dringt, und durch die unteren Pfeile alles, was von innen kommend sich der Bluttafel einschreibt.",
        "Oder, wenn wir die Sache etwas weni­ger schematisch ansehen wollen, so können wir sagen: Wenn wir das menschliche Haupt und das hindurchgehende Blut betrachten, wie es"
      ],
      [
        "# Bild s.051"
      ],
      [
        "beschrieben wird von außen durch die Sinnesorgane, so wirkt das Gehirn in seiner Arbeit in derselben Weise umwandelnd auf das Blut, wie die inneren Organe auf das Blut umwandelnd wirken.",
        "Denn diese drei Organe, Leber, Galle, Milz, wirken von der anderen Seite her auf"
      ],
      [
        "das Blut, welches wir hier so zeichnen wollen, als ob es die Organe umflösse.",
        "So also würde das Blut gleichsam Strahlungen, Wirkungen empfangen können von den inneren Organen und würde damit so-zusagen als Werkzeug des Ich in diesem Ich das innere Leben dieser Organe zum Ausdruck bringen, so wie in unserem Gehirnleben das zum Ausdruck kommt, was uns in der Welt umgibt."
      ],
      [
        "Da müssen wir uns allerdings klar sein, daß noch etwas ganz Bestimmtes eintreten muß, damit diese Wirkungen der Organe auf das Blut möglich sind.",
        "Erinnern wir uns daran, daß wir sagten, daß in der Wechselwirkung von Nerv und Blutlauf überhaupt erst die Mög­lichkeit liegt, daß auf das Blut eine Wirkung ausgeübt, daß in das Blut sozusagen etwas eingeschrieben werden kann.",
        "Wenn von der Seite der inneren Organe her Wirkungen auf das Blut ausgeübt werden sollen, wenn gleichsam das innere Weltsystem des Menschen auf das Blut wirken soll, so muß zwischen diesen Organen und dem Blut etwas eingeschaltet sein wie ein Nervensystem.",
        "Es muß die innere Welt zuerst auf ein Nervensystem wirken können, um dann ihre Wirkungen auf das Blut übertragen zu können."
      ],
      [
        "So sehen wir, einfach aus einem Vergleich des unteren Teiles des Menschen mit dem oberen, daß die Voraussetzung gemacht werden muß, daß zwischen unseren inneren Organen - als deren Repräsen­tanten wir diese drei Organe: Leber, Galle, Milz haben - und dem Blutkreislauf etwas eingeschaltet sein muß wie ein Nervensystem.",
        "Fragen wir die äußere Beobachtung, so zeigt sie uns in der Tat, daß in alle diese Organe das eingeschaltet ist, was wir das sympathische Nervensystem nennen, welches die Körperhöhle des Menschen aus­füllt und welches in einem analogen Verhältnisse zu der mensch­lichen Innenwelt und dem Blutkreislauf steht, wie andererseits das Rückenmark-Nervensystem zwischen der äußeren großen Welt und dem Blutumlauf des Menschen steht.",
        "Von diesem sympathischen Nervensystem, das ja zunächst längs des Rückgrates verläuft, dann, von dort ausgehend die verschiedensten Teile des Organismus durch­zieht und sich ausbreitet, auch netzförmige Ausbreitungen zeigt, namentlich in der Bauchhöhle, wo man einen Teil dieses Systems populär auch das Sonnengeflecht nennt, von diesem sympathischen"
      ],
      [
        "Nervensystem werden wir zu erwarten haben, daß es in einer gewis­sen Weise von dem anderen Nervensystem abweicht.",
        "Und es ist immerhin interessant - wenn es auch nicht zu einem Beweise dienen soll -, sich zu fragen: Wie könnte denn dieses Nervensystem gestaltet sein im Verhältnis zum Rückenmark-Nervensystem, wenn diese Bedingungen erfüllt würden, die wir jetzt hypothetisch gestellt haben? - Sie könnten einsehen: Wie sich das Rückenmark-Nerven­system öffnen muß dem Umkreis des Raumes, so muß dieses sympa­thische Nervensystem demjenigen zugeneigt sein, was zusammen­gedrängt ist in die innere Organisation.",
        "So verhält sich, wenn unseren Voraussetzungen entsprochen werden soll, das sympathische Ner­vensystem zu dem Rückenmark-Nervensystem etwa so, wie sich verhalten die Radien eines Kreises, die vom Mittelpunkt zur Periphe­rie gerichtet sind (siehe Zeichnung a), zu den sich von der Peripherie"
      ],
      [
        "# Bild s.053"
      ],
      [
        "aus nach außen fortsetzenden Radien (b).",
        "Also in einer gewissen Weise müßte ein Gegensatz vorhanden sein zwischen dem sympathi­schen Nervensystem und zwischen dem Nervensystem des Gehirnes und Rückenmarkes.",
        "Dieser Gegensatz ist auch in der Wirklichkeit vorhanden.",
        "Und da sehen wir, wie schon darin vieles für uns liegen kann, daß wir imstande sind nachzuweisen: Wenn unsere Vorausset­zungen richtig sind, dann muß die äußere Beobachtung sie in einer gewissen Weise bestätigen, und es zeigt sich, daß die äußere Beobach­tung tatsächlich bestätigt, was wir als Voraussetzung gemacht haben.",
        "Während beim sympathischen Nervensystem im wesentlichen eine Art starke Nervenknoten vorhanden sind und die Ausstrahlungen"
      ],
      [
        "dieser Nervenknoten, die verbindenden Fäden, verhältnismäßig dünn sind und wenig in Betracht kommen gegenüber den Nervenknoten, ist bei dem Gehirn-Rückenmark-Nervensystem gerade das Umge­kehrte der Fall, da sind die verbindenden Fäden das Wesentliche, während die Nervenknoten nur eine untergeordnete Bedeutung haben.",
        "So bestätigt uns die Beobachtung in der Tat das, was wir als Voraussetzung annahmen.",
        "Wenn das sympathische Nervensystem die Aufgabe hat, die es nach dem, was wir gesagt haben, haben muß, dann muß sich das innere Leben unseres Organismus, das in der Durchnährung und Durchwärmung des Organismus zum Ausdruck kommt, gleichsam in dieses sympathische Nervensystem hineinergie­ßen, und dieses Nervensystem müßte es auf die Bluttafel geradeso übertragen, wie die äußeren Eindrücke durch das Gehirn-Rücken-mark-Nervensystem auf das Blut übertragen werden.",
        "So bekommen wir in das individuelle Ich hinein, durch das Instrument des Ich, das Blut - auf dem Umwege durch das sympathische Nervensystem -, die Eindrücke unseres eigenen körperlichen Inneren.",
        "Da aber unser körperliches Innere wie alles Physische aus dem Geiste heraus aufer­baut ist, so bekommen wir das, was sich als geistige Welt zusammen­gedrängt hat in den entsprechenden Organen des inneren Menschen, herauf in unser [waches] Ich auf dem Umwege durch das sympathi­sche Nervensystem."
      ],
      [
        "So sehen wir auch hier, wie sich diese Zweiheit im Menschen noch genauer ausdrückt, von der wir in unseren Betrachtungen ausgegan­gen sind.",
        "Wir sehen die Welt einmal draußen, wir sehen sie einmal drinnen wirken; beide Male sehen wir diese Welt so wirken, daß zu dieser Wirkung einmal das eine, einmal das andere Nervensystem als Werkzeug dient.",
        "Wir sehen, wie in die Mitte zwischen Außenwelt und Innenwelt hineingestellt ist unser Blutsystem, das sich wie eine Tafel von zwei Seiten beschreiben läßt, einmal von außen, einmal von innen."
      ],
      [
        "Nun haben wir gestern gesagt, und es heute der Deutlichkeit wegen wiederholt, daß der Mensch imstande ist, seine Nerven, inso­fern sie in die Sinneswelt hinausführen, sozusagen frei zu machen von den Wirkungen der Außenwelt auf das Blutsystem.",
        "Die Frage müssen"
      ],
      [
        "wir uns nun vorlegen, ob auch nach der entgegengesetzten Rich­tung hin etwas Ähnliches möglich ist?",
        "Und wir werden später sehen, daß in der Tat auch solche Übungen der Seele möglich sind, welche dieselbe Wirkung, von der wir heute und gestern gesprochen haben, nach der anderen Richtung möglich machen."
      ],
      [
        "Jedoch besteht hier ein gewisser Unterschied.",
        "Während wir durch Gedankenkonzentration, durch Gefühlskonzentration, durch okkulte Übungen die Nerven unseres Gehirns und Rückenmarkes vom Blute losbekommen kön­nen, können wir durch solche Konzentrationen, welche gleichsam in unser Innenleben, in unsere Innenwelt hineingehen - und es sind dies namentlich diejenigen Konzentrationen, die man zusammenfassen kann unter dem Namen «mystisches Leben» -, so tief in uns eindrin­gen, daß wir allerdings unser Ich dabei, also auch sein Werkzeug, das Blut, keineswegs unberücksichtigt lassen."
      ],
      [
        "Die mystische Versenkung, von der wir ja wissen - was später noch genauer ausgeführt werden soll -, daß der Mensch durch sie gleichsam untertaucht in seine eigene göttliche Wesenheit, in seine eigene Geistigkeit, insofern sie in ihm liegt, diese mystische Versenkung ist nicht zunächst ein Herausheben aus dem Ich.",
        "Sie ist im Gegenteil ein Sichhineinversenken in das Ich, eine Verstärkung, ein Energischermachen, eine Steigerung der Ich-Empfindung."
      ],
      [
        "Davon können wir uns überzeugen, wenn wir - abge­sehen von dem, was die Mystiker der Gegenwart sagen - uns ein wenig einlassen auf ältere Mystiker.",
        "Diese älteren Mystiker, gleich­gültig, ob sie auf einem mehr oder weniger religiösen Boden stehen, sind vor allen Dingen bemüht, in ihr eigenes Ich hineinzudringen und abzusehen von alle dem, was die Außenwelt uns geben kann, um frei zu werden von allen äußeren Eindrücken und ganz in sich selber unterzutauchen."
      ],
      [
        "Diese innere Einkehr, dieses Untertauchen in das eigene Ich ist zunächst wie ein Zusammenziehen der ganzen Gewalt und Energie des Ich in den eigenen Organismus hinein.",
        "Das wirkt nun auf die ganze Organisation des Menschen weiter, und wir kön­nen sagen: Diese innere Versenkung, dieser im eigentlichen Sinne so zu nennende «mystische Weg» ist - im Gegensatz zu dem anderen Weg, den wir beschrieben haben - so, daß wir das Werkzeug des Ich, das Blut, nicht abziehen von dem Nerv, sondern es gerade mehr"
      ],
      [
        "hinstoßen zum Nerv, zum sympathischen Nervensystem.",
        "Während wir also die Verbindung von Nerv und Blut lösen bei dem Vorgang, den wir gestern besprochen haben, machen wir im Gegensatz dazu durch die mystische Versenkung die Verbindung zwischen dem Blut und dem sympathischen Nervensystem stärker.",
        "Das ist das physio­logische Gegenbild: Bei der mystischen Versenkung wird das Blut tiefer hineingedrängt zu dem sympathischen Nervensystem, während bei der anderen Art seelischer Übungen das Blut vom Nerv abge­drängt wird.",
        "Es ist also wie ein Eindrücken des Blutes in das sympa­thische Nervensystem, was in der mystischen Versenkung vor sich geht."
      ],
      [
        "Nehmen wir nun an, wir könnten für eine Weile von dem absehen, daß der Mensch, wenn er in mystischer Versenkung in sein Inneres hineingeht, nicht loskommt von seinem Ich, sondern es im Gegenteil tiefer hineindrängt in sein Inneres und dabei alle schlechten, alle minder guten Eigenschaften, die er hat, mitnimmt.",
        "Wenn man sich in sein Inneres hineinversenkt, ist man sich zunächst nicht klar, daß man auch alle minder guten Eigenschaften hineindrückt in dieses Innere, mit anderen Worten, daß alles, was im leidenschaftlichen Blute ist, mit hineingeprägt wird in das sympathische Nervensystem."
      ],
      [
        "Aber nehmen wir an, wir könnten eine Weile davon absehen und uns sagen, der Mystiker habe Sorge getragen, bevor er zu einer solchen mystischen Versenkung gekommen ist, daß die minder guten Eigen­schaften immer mehr und mehr verschwunden sind und daß anstelle der egoistischen Eigenschaften selbstlose, altruistische Gefühle getre­ten sind, er habe sich dadurch vorbereitet, daß er versuchte, das Gefühl des Mitleides mit allen Wesen in sich rege zu machen, um die Eigenschaften, die nur auf das Ich hinspekulieren, zu paralysieren durch selbstloses Mitgefühl für alle Wesen.",
        "Nehmen wir also an, der Mensch habe sich genügend sorgfältig vorbereitet, um sich in sein Inneres hinein zu versenken."
      ],
      [
        "Trägt der Mensch dann das Ich durch das Werkzeug seines Blutes in seine innere Welt hinein, dann kommt es dazu, daß dieses innere Nervensystem, das sympathische Nerven­system, von dem der Mensch im normalen Bewußtsein natürlich nichts weiß, hereinrückt in das Ich-Bewußtsein, daß er anfängt zu"
      ],
      [
        "wissen: Du hast da in dir etwas, das dir ein Ähnliches von deiner inneren Welt vermitteln kann, wie dein Gehirn-Rückenmark-Ner­vensystem dir die äußere Welt vermittelt. - Man wird gewahr seines sympathischen Nervensystems, und wie man durch das Gehirn­Rückenmark-Nervensystem die äußere Welt erkennen kann, so kommt einem jetzt entgegen die innere Welt.",
        "Aber wie wir bei den äußeren Eindrücken auch nicht die Nerven selbst sehen, sondern durch die Sehnerven die äußere Welt in unser Bewußtsein herein­dringt, so dringen bei der mystischen Versenkung auch nicht die inneren Nerven ins Bewußtsein herein; der Mensch wird nur gewahr, daß er in ihnen ein Instrument hat, durch das er in das Innere schauen kann.",
        "Es tritt etwas ganz anderes ein, es tritt vor dem nach innen zu hellsichtig gewordenen menschlichen Erkenntnisvermögen die innere Welt auf.",
        "Wie uns der Blick nach außen die Außenwelt erschließt, und uns dabei nicht unsere Nerven zum Bewußtsein kommen, so kommt uns auch nicht unser sympathisches Nervensystem zum Bewußtsein, wohl aber das, was sich uns als Innenwelt entgegenstellt.",
        "Nur müssen wir sehen, daß diese Innenwelt, die uns da zum Bewußt­sein kommt, eigentlich wir selbst als physischer Mensch sind."
      ],
      [
        "Vielleicht liegt es nicht besonders nahe, aber ich möchte doch sagen: Einem ein klein wenig materialistischen Denker könnte eine Art von Horror aufsteigen, wenn er sich sagen sollte, daß er seinen eigenen Organismus von innen sehen kann, und er könnte vielleicht meinen: Da sehe ich aber auch etwas Rechtes, wenn ich durch mein sympathisches Nervensystem hellsichtig werde und meine Leber, Galle und Milz zu sehen bekomme! - Ich meine, es muß ja nicht besonders naheliegen, aber man könnte es sich doch sagen.",
        "So ist die Sache aber nicht.",
        "Denn bei einem solchen Einwand würde man nicht berücksichtigen, daß der Mensch im gewöhnlichen Leben seine Leber, Galle und Milz und so weiter von außen anschaut wie die anderen äußeren Gegenstände auch.",
        "So wie Sie in der Anatomie, in der gewöhnlichen Physiologie Leber, Galle, Milz und so weiter kennenlernen, wenn Sie einen Menschen aufschneiden, sind diese Organe natürlich durch die äußeren Sinne, durch das Gehirn-Rük­kenmark-Nervensystem angeschaut, geradeso wie irgend etwas anderes."
      ],
      [
        "Aber in einer ganz anderen Lage ist der Mensch, wenn er versucht, sein sympathisches Nervensystem zu gebrauchen, um nach innen hellsichtig zu werden.",
        "Da sieht er keineswegs dasselbe, was er von außen sehen kann, sondern da sieht er das, um dessentwillen die Hellseher aller Zeiten so sonderbare Namen für diese Organe gewählt haben, wie ich sie Ihnen im zweiten Vortrage angeführt habe."
      ],
      [
        "Da wird er nämlich gewahr, daß in der Tat dem äußeren Anschauen durch das Gehirn-Rückenmark-Nervensystem diese Organe als Maja, in äußerer Illusion erscheinen in dem Anblick, den sie nach außen bieten, nicht in ihrer inneren wesenhaften Bedeutung.",
        "Man sieht in der Tat etwas ganz anderes, wenn man mit dem nach innen gewendeten Auge diese seine innere Welt hellseherisch belau­schen kann."
      ],
      [
        "Da wird man nach und nach gewahr, warum die Hellse­her aller Zeiten einen Zusammenhang der Organe mit den Wirkun­gen der Planeten gesehen haben.",
        "Wie wir gestern gesagt haben, wurde die Milzwirkung mit dem Namen des Saturn, die Leberwirkung mit dem Jupiter und die Gallewirkung mit dem Mars in Zusammenhang gebracht."
      ],
      [
        "Denn was man im eigenen Inneren sieht, das ist in der Tat grundverschieden von dem, was sich dem äußeren Anblick darbietet.",
        "Da wird man gewahr, daß man wirklich in den inneren Organen umgrenzte, zusammengeschlossene Partien der Außenwelt vor sich hat."
      ],
      [
        "Vor allem wird eines klar, was uns zunächst als ein Beispiel dienen soll: Durch diese Art zu einer Erkenntnis zu kommen, die über das gewöhnliche Anschauen hinausführt, können wir uns davon überzeugen, daß die menschliche Milz ein sehr bedeutungsvolles Organ ist.",
        "Dieses Organ erscheint ja der inneren Betrachtung wirk­lich so, als wenn es nicht aus äußerer Substanz, aus fleischlicher Materie bestehen würde, sondern - wenn der Ausdruck gestattet ist, obwohl er nur annähernd das wiedergeben kann, was gesehen wird -die Milz erscheint tatsächlich wie ein leuchtender Weltenkörper im kleinen mit allem möglichen inneren Leben, das sehr kompliziert ist."
      ],
      [
        "Ich habe Sie gestern darauf aufmerksam gemacht, daß die Milz, äußerlich betrachtet, beschrieben werden kann als ein blutreiches Gewebe, eingebettet darin die erwähnten weißen Körperchen.",
        "So daß"
      ],
      [
        "man von einer äußeren physiologischen Betrachtung ausgehend sa­gen kann, daß das Blut, welches sich durch die Milz ergießt, durch sie wie durch ein Sieb durchgesiebt wird.",
        "Der inneren Betrachtung aber stellt sich die Milz dar als ein Organ, das durch mannigfache innere Kräfte in eine beständige rhythmische Bewegung gebracht wird."
      ],
      [
        "Wir überzeugen uns schon bei einem solchen Organ davon, daß im Grunde genommen in der Welt ungeheuer viel auf Rhythmus ankommt.",
        "Eine Ahnung von der Bedeutung des Rhythmus im Gesamtleben der Welt können wir ja bekommen, wenn wir den äußeren Rhythmus des Kosmos wiedererkennen im Blut-Pulsschlag."
      ],
      [
        "Auch äußerlich können wir den Rhythmus in den Organen, auch in dem Organ der Milz, ziemlich genau verfolgen.",
        "Für den, der mit nach innen gewendetem hellseherischen Blick die Organe anschaut, dem offenbaren sich die Differenzierungen der Milz wie in einem Licht-körper, sie sind dazu da, um der Milz einen gewissen Rhythmus im Leben zu geben."
      ],
      [
        "Dieser Rhythmus unterscheidet sich von anderen Rhythmen, die wir sonst gewahr werden, ganz beträchtlich.",
        "Und gerade bei der Milz ist es interessant zu studieren, wie sich dieser Rhythmus der Milz ganz beträchtlich unterscheidet von jedem ande­ren Rhythmus; er ist nämlich weit weniger regelmäßig als andere Rhythmen."
      ],
      [
        "Warum?",
        "Dies ist aus dem Grunde der Fall, weil die Milz in einer gewissen Weise naheliegt dem menschlichen Ernährungsap­parat und mit demselben etwas zu tun hat.",
        "Das werden Sie gleich verstehen, wenn wir ein wenig darauf Rücksicht nehmen, wie unge­heuer regelmäßig beim Menschen der Rhythmus des Blutes sein muß, damit das Leben in einer richtigen Weise aufrechterhalten werden kann."
      ],
      [
        "Das muß ein sehr regelmäßiger Rhythmus sein.",
        "Aber es gibt einen anderen Rhythmus, und der ist nur in geringem Maße regelmä­ßig, obwohl von ihm zu wünschen wäre, daß er durch die Selbster­ziehung der Menschen immer regelmäßiger und regelmäßiger würde, namentlich in dem kindlichen Lebensalter: das ist der Rhythmus, in dem wir uns ernähren, der Rhythmus von Essen und Trinken."
      ],
      [
        "Einen gewissen Rhythmus hält darin ja wohl ein einigermaßen ordentlicher Mensch ein; er nimmt zu bestimmten Zeiten seine Tagesmahlzeiten, das Frühstück, das Mittagessen und das Nachtmahl ein, so daß er"
      ],
      [
        "dadurch doch einen gewissen Rhythmus hat.",
        "Aber wie ist es mit diesem Rhythmus eigentlich bestellt?",
        "In vieler Hinsicht - das ist ja traurig bekannt - wird diese Regelmäßigkeit durchbrochen durch das Entgegenkommen vieler Eltern gegenüber der Genäschigkeit ihrer Kinder, denen man einfach dann etwas gibt, wenn sie gerade danach Verlangen haben, wobei abgesehen wird von allem Rhythmus."
      ],
      [
        "Und auch die Erwachsenen sind nicht gerade so ungeheuer darauf aus, immer einen genauen Rhythmus in bezug auf Essen und Trinken einzuhalten.",
        "Das soll gar nicht in pedantischer oder moralisierender Weise gemeint sein, denn das moderne Leben macht das nicht immer möglich."
      ],
      [
        "Wie unregelmäßig die Nahrung in den Menschen hineinge-stopft wird, wie unregelmäßig namentlich getrunken wird, das ist ja hinlänglich bekannt und soll nicht getadelt, sondern nur erwähnt werden.",
        "Es muß aber das, was wir in einer mangelhaften rhythmi­schen Art unserem Organismus zuführen, allmählich so umrhythmi­siert werden, daß es sich in den regelmäßigeren Rhythmus des Orga­nismus einfügt; es muß so umgeschaltet werden, daß wenigstens die gröbsten Unregelmäßigkeiten in der Nahrungsaufnahme beseitigt werden."
      ],
      [
        "Nehmen wir an, ein Mensch sei durch seinen Beruf gezwun­gen, um acht Uhr morgens zu frühstücken und um ein oder zwei Uhr zu Mittag zu essen, und diese regelmäßige Tageseinteilung sei ihm eine Gewohnheit.",
        "Nun nehmen wir weiter an, er würde zu einem guten Freunde gehen, und da gebiete es ihm die sonst ja nicht genug zu lobende Höflichkeit, zwischen diesen beiden Mahlzeiten eine Erfrischung zu sich zu nehmen."
      ],
      [
        "Damit hat er den gewohnten Rhyth­mus seiner Nahrungsaufnahme in einer ganz erheblichen Weise durchbrochen, und dadurch wird auf den Rhythmus seines Organis­mus eine ganz bestimmte Wirkung ausgeübt.",
        "Es muß nun etwas da sein im Organismus, das in entsprechender Weise dasjenige stärker macht, was regelmäßig im Rhythmus ist und was die Wirkung dessen abschwächen muß, was unregelmäßig ist."
      ],
      [
        "Es müssen die gröbsten Unregelmäßigkeiten ausgeglichen werden, so daß beim Übergehen der Nahrungsmittel auf das Blutsystem ein Organ eingeschaltet sein muß, das die Unregelmäßigkeit des Ernährungsrhythmus ausgleicht gegenüber der notwendigen Regelmäßigkeit des Blutrhythmus."
      ],
      [
        "dieses Organ ist die Milz.",
        "So können wir an ganz bestimmten rhyth­mischen Vorgängen, wie es jetzt charakterisiert worden ist, einen Begriff dafür erhalten, daß die Milz ein Umschalter ist, um Unregel­mäßigkeiten im Verdauungskanal so auszugleichen, daß sie zu Regel­mäßigkeiten werden in der Blutzirkulation.",
        "Denn es wäre in der Tat eine ganz fatale Sache, wenn gewisse Unregelmäßigkeiten in dem Aufnehmen von Nahrungsstoffen - namentlich in der Studentenzeit oder auch zu anderen Zeiten - ihre ganze Wirkung fortsetzen müßten in das Blut hinein.",
        "Da ist viel auszugleichen, und es ist nur so viel auf das Blut überzuleiten, als diesem zuträglich ist.",
        "Diese Aufgabe hat das in die Blutbahn eingeschaltete Milzorgan, das seine rhythmisie­rende Wirkung so ausstrahlt über den ganzen menschlichen Organis­mus, daß das zustande kommt, was jetzt beschrieben worden ist."
      ],
      [
        "Was wir jetzt hervorgeholt haben aus dem Einblick des hellsehend gewordenen Auges, zeigt sich auch der äußeren Beobachtung, näm­lich daß die Milz einen gewissen Rhythmus einhält.",
        "Es ist außeror­dentlich schwierig, durch die äußeren physiologischen Untersuchun­gen allein diese Aufgabe der Milz herauszufinden, man kann aber durch äußerliche Beobachtung feststellen, daß die Milz gewisse Stun­den hindurch nach einer reichlich genossenen Mahlzeit angeschwol­len ist und daß sie, wenn nicht wieder nachgeschoben wird, sich wieder zusammenzieht, wenn eine angemessene Zeit vergangen ist.",
        "Durch eine gewisse Ausdehnung und Zusammenziehung dieses Organs wird die Unregelmäßigkeit in der Nahrungsaufnahme auf den Rhythmus des Blutes umgeschaltet.",
        "Und wenn Sie sich dessen bewußt sind, daß der menschliche Organismus nicht bloß das ist, als was man ihn oft beschreibt, nämlich eine Summe seiner Organe, sondern daß alle Organe ihre geheimen Wirkungen nach allen Teilen des Organismus hinschicken, so werden Sie sich auch vorstellen können, daß die rhythmische Tätigkeit der Milz von der Außenwelt, nämlich von der Zuführung der Nahrungsmittel abhängt, und daß diese rhythmischen Bewegungen der Milz ausstrahlen in den ganzen Organismus und über den ganzen Organismus hin ausgleichend wirken können.",
        "Das ist zwar nur eine Art, wie die Milz wirkt; denn es ist unmöglich, alle Arten gleich anzuführen."
      ],
      [
        "Es wäre nun in der Tat außerordentlich interessant zu sehen, ob die äußere Physiologie solche Dinge, wie sie eben ausgesprochen wur­den, bestätigen würde, wenn sie dieselben - da ja nicht alle Menschen gleich hellsehend werden können - hinnehmen würde, ich möchte sagen, wie eine «hingeworfene Idee», wenn also zunächst gesagt würde: Ich will mir einmal vorstellen, daß es doch nicht so ganz verdrehtes Zeug ist, was die Okkultisten sagen, ich will es einmal weder glauben noch nicht glauben, sondern es als Idee dahingestellt sein lassen und prüfen, ob sich davon irgend etwas durch die äußere Physiologie beweisen läßt. - Dann könnten Untersuchungen der äußeren Physiologie angestellt werden, die den Beweis erbringen könnten für das, was aus hellseherischer Beobachtung heraus gewon­nen wurde."
      ],
      [
        "Eine solche Bestätigung haben wir ja schon genannt, das Ausdeh­nen und Zusammenziehen der Milz.",
        "Es zeigt sich, weil die Ausdeh­nung der Milz auf die Einnahme einer Mahlzeit folgt, daß sie von der Nahrungsaufnahme abhängig ist.",
        "So haben wir in der Milz ein Organ gefunden, das nach der einen Seite hin von menschlicher Willkür abhängig ist, auf der anderen Seite, nach der Blutseite hin, die Unre­gelmäßigkeiten der menschlichen Willkür beseitigt, sie ablähmt, das heißt sie umschaltet auf den Rhythmus des Blutes, und dadurch das Physische des Menschen sozusagen erst seiner Wesenheit gemäß gestaltet werden kann.",
        "Denn soll der Mensch seiner Wesenheit gemäß gestaltet sein, dann muß ja namentlich das Mittelpunktswerk-zeug seiner Wesenheit, das Blut, in der richtigen Weise seine Wir­kung ausüben können, in dem eigenen Blutrhythmus.",
        "Es muß der Mensch, insofern er Träger seines Blutkreislaufes ist, in sich abgeson­dert, isoliert sein von dem, was draußen in der Außenwelt unregel­mäßig vorgeht, und von dem, was auf den Menschen dadurch ein­wirkt, daß er völlig unrhythmisch sich seine Nahrung einverleibt."
      ],
      [
        "Es ist also ein Isolieren, ein Unabhängigmachen der menschlichen Wesenheit von der Außenwelt.",
        "Jedes solches Individualisieren, SeIb­ständigmachen einer Wesenheit nennt man im Okkultismus «Satur­nisch», etwas, das durch Saturnwirkung herbeigeführt wird.",
        "Das ist die ursprüngliche Idee, das Wesentliche des Saturnischen: daß aus"
      ],
      [
        "einem umfassenden Gesamtorganismus ein Wesen herausgestellt, iso­liert, individualisiert wird, so daß es in sich selber eine gesonderte Regelmäßigkeit entfalten kann.",
        "Ich will jetzt davon absehen, daß ja von unserer heutigen Astronomie außerhalb der Saturnbahn noch Uranus und Neptun zu unserem Sonnensystem gerechnet werden.",
        "Für den Okkultisten ist alles das, was an Kräften vorhanden ist, um unser Sonnensystem aus der übrigen Welt herauszuheben, abzuson­dern, zu isolieren und zu individualisieren, ihm eine Eigengesetzlich­keit zu geben, in den Saturnkräften gegeben."
      ],
      [
        "# Bild s.063"
      ],
      [
        "Alle diese Kräfte sind in dem gegeben, was in unserem Sonnen­system der äußerste Planet ist.",
        "Wenn man sich die Welt vorstellt, könnte man sagen, daß innerhalb der Kreisbahn des Saturns das Sonnensystem so darinnen ist, daß es innerhalb dieser Bahn seinen eigenen Gesetzen folgen kann und sich unabhängig machen kann, indem es sich herausreißt aus der Umwelt und den gestaltenden Kräften der Umwelt.",
        "Aus diesem Grunde sahen die Okkultisten aller Zeiten in den saturnhaften Kräften das, was unser Sonnensystem in"
      ],
      [
        "sich selber abschließt, was es dem Sonnensystem möglich macht, einen eigenen Rhythmus zu entfalten, der nicht derselbe ist wie der Rhythmus draußen, der außerhalb der Welt unseres Sonnensystems herrscht."
      ],
      [
        "Etwas Ähnlichem begegnen wir in unserem Organismus bei der Milz.",
        "In unserem Organismus haben wir es zwar nicht zu tun mit einem Absondern gegen die ganze äußere Welt, sondern nur von einer Umwelt, insofern sie die Nahrungsmittel für unseren Organis­mus enthält.",
        "In der Milz haben wir dasjenige Organ im Körper zu sehen, das alles, was von draußen kommt, so behandelt, wie das innerhalb der Saturnbahn des Sonnensystems Liegende von den Saturnkräften behandelt wird: daß es zuerst umrhythmisiert wird in den Rhythmus und die Gesetzmäßigkeit des Menschen.",
        "Was durch die Milz geschieht, das isoliert unseren Blutkreislauf von allen äuße­ren Wirkungen, das macht ihn zu einem in sich selber regelmäßigen System, das seinen eigenen Rhythmus haben kann."
      ],
      [
        "Damit kommen wir schon den Gründen etwas näher, die im Okkultismus für die Wahl von Planetennamen für die Organe maß­gebend waren.",
        "In den okkulten Schulen wurden diese Namen ursprünglich nicht bloß auf die einzelnen physisch sichtbaren Plane­ten angewendet.",
        "Der Name «Saturn» zum Beispiel wurde ja, wie schon gesagt, auf alles angewendet, was bewirkt, daß sich etwas aus einer größeren Gesamtheit aussondert und sich abschließt zu einem System, das in sich selber rhythmisch gestaltet ist.",
        "Daß ein System sich abschließt und sich in sich selbständig rhythmisch gestaltet, hat einen gewissen Nachteil für die gesamte Weltentwickelung, und das hat immer die Okkultisten ein wenig bekümmert.",
        "Es ist ja leicht verständlich, daß in der kleinen und in der großen Welt alle Wirkun­gen zueinander in Beziehungen stehen, daß alle sich aufeinander beziehen.",
        "Wenn nun irgend etwas, sei es ein Sonnensystem, sei es das Blutsystem des Menschen, sich herausgliedert aus der ganzen Umwelt und einer Eigengesetzmäßigkeit folgt, so bedeutet das, daß ein solches System die äußeren umfassenden Gesetze durchbricht, verletzt, daß es sich verselbständigt gegenüber den äußeren Gesetzen und sich eigene innere Gesetze und einen eigenen Rhythmus schafft,"
      ],
      [
        "welche denen der Umwelt zunächst widersprechen.",
        "Wir werden sehen, wie das auch auf den physischen Menschen bezogen werden kann, obwohl es uns nach den ganzen Auseinandersetzungen des heutigen Vortrages klar sein muß, daß es zunächst für den Menschen segensreich ist, daß er diesen durch das Saturnische der Milz geschaf­fenen inneren Rhythmus erhalten hat."
      ],
      [
        "Aber wir werden doch sehen, daß ein Wesen, sei es ein Planet, sei es ein Mensch, durch das Sich­abschließen in sich selber sich in einen Widerspruch bringt zur umliegenden Welt.",
        "Es ist ein Widerspruch geschaffen zwischen dem, was um uns ist, und dem, was in uns ist."
      ],
      [
        "Dieser Widerspruch, der nun einmal vorhanden ist, kann nicht früher ausgeglichen werden, als bis sich der im Inneren hergestellte Rhythmus dem äußeren Rhythmus wieder völlig angepaßt hat.",
        "Wir werden noch sehen, wie dies auch auf den physischen Menschen bezogen wird; denn so, wie es jetzt gesagt worden ist, sieht es aus, als ob der Mensch sich anpassen müßte an die Unregelmäßigkeit."
      ],
      [
        "Wir werden aber sehen, daß es anders ist.",
        "Der innere Rhythmus muß, nachdem er sich hergestellt hat, danach stre­ben, sich wiederum mit der ganzen äußeren Welt gleich zu gestalten, das heißt, sich selber aufzuheben."
      ],
      [
        "Das heißt also: Die Wesenheit, die im Inneren entsteht und selbständig arbeitet, muß das Bestreben haben, sich wiederum an die Außenwelt anzupassen und dieser Außenwelt gegenüber so zu werden, wie diese selber ist.",
        "Mit anderen Worten: Alles, was durch eine saturnische Wirkung verselbständigt wird, das wird zugleich durch diese saturnische Wirkung dazu ver­urteilt, sich selber wieder zu zerstören."
      ],
      [
        "Der Mythos drückt das im Bilde aus: Saturn - oder Kronos - verzehrt seine eigenen Kinder."
      ],
      [
        "So sehen Sie einen tiefen Einklang herrschen zwischen einer okkul­ten Idee und einem Mythos, der dasselbe ausdrückt im Bilde, im Symbol: Kronos verzehrt seinen eigenen Kinder. - Wenn man solche Dinge in immer größerer und größerer Zahl auf sich wirken läßt, so bildet sich für die Beziehungen der angedeuteten Art ein feines Gefühl heraus, und dann wird es nach einiger Zeit nicht mehr so leicht möglich sein, wie es die äußerliche Aufklärung tun möchte, zu sagen: Nun ja, da träumen einige Phantasten davon, daß in den alten Mythen und Sagen bildliche Ausprägungen tiefer Weisheiten enthalten"
      ],
      [
        "seien. - Wenn man zwei, drei oder auch zehn solcher Entspre­chungen hört, noch dazu so, wie sie oft in der Literatur dargeboten werden, nämlich in recht äußerlicher Weise, dann kann man sich ganz gewiß dagegen auflehnen, daß in Mythen und Sagen tiefere Weisheiten enthalten seien als in der äußeren Wissenschaft.",
        "Aber wer tiefer auf die Sache eingeht, der findet bewahrheitet, daß Mythen und Sagen tiefer hineinführen in das wirkliche Wesen der Welt und der Organbildung, als es der äußeren wissenschaftlichen Betrachtungs­weise möglich ist."
      ],
      [
        "Wer immer wieder solche Bilder auf sich wirken läßt, wie sie in den wunderbaren Mythen und Sagen über den ganzen Erdkreis hin verstreut sind, der kann bei liebevollem Eingehen auf diese Bilder in dem ganzen Fühlen und Denken der Völker, in den bildhaften Vorstellungen der Menschen, die Umgestaltung tiefster Weisheiten finden.",
        "Dann begreift man, warum einige Okkultisten sagen können, derjenige habe erst Mythen und Sagen wirklich begrif­fen, der durch sie in die okkulte Physiologie der menschlichen Natur eingedrungen sei. - Mehr als die äußere Wissenschaft erfaßt, enthal­ten Mythen und Sagen wirkliche Weisheiten über das menschliche Wesen, wirkliche Physiologie."
      ],
      [
        "Wenn die Menschen einmal ergründen werden, wieviel Physiologie zum Beispiel in solchen Namen wie Kain und Abel und ihrer Nachfolgeschaft liegt - diese alten Namen rühren ja aus Zeiten her, in denen man in die Namen noch einen inneren Sinn hineinprägte -, dann werden die Menschen einen unge­heuren Respekt, eine ungeheure Ehrfurcht bekommen vor alle dem, was im Laufe des geschichtlichen Werdens von weisheitsvollen Men­schen ersonnen worden ist, um da, wo in die geistigen Welten noch nicht hineingeschaut werden kann, die Seelen durch Bilder ihren Zusammenhang mit diesen geistigen Welten erleben zu lassen.",
        "Da wird einem gründlich vertrieben der Hochmut, der in dem Worte steckt, das in unserer Zeit eine viel zu große Rolle spielt: Wie haben wir es heute so herrlich weit gebracht! -, womit man meint: Wie haben wir abgestreift die alten bildhaften Ausdrücke der Urmensch­heitsweistümer."
      ],
      [
        "Die streift man gründlich ab, wenn man sich nicht mit inniger Liebe in den Gang der Menschheitsentwickelung durch die verschiedenen"
      ],
      [
        "Epochen hindurch versenkt.",
        "Was der Hellseher mit dem geöff­neten inneren Auge als die innere Natur der menschlichen Organe physiologisch ergründet, das drückt sich in Bildern aus und läßt ihn sehen, daß die Mythen und Sagen gleichsam die menschliche Her­kunft enthalten.",
        "Der Hellseher sieht in den Mythen und Sagen ausge­drückt diesen Wunderprozeß, daß Welten zusammengedrängt wor­den sind in menschliche Organe.",
        "Er sieht, wie sich im Laufe unend­lich langer Zeiten die Organe zusammenkristallisiert haben, um zu dem werden zu können, was als Milz, als Leber, als Galle in uns wirkt.",
        "Wir werden morgen noch weiter darüber sprechen.",
        "Um das alles in Bildern ausdrücken zu können, dazu gehört wahrhaftig eine tiefe Weisheit, ein tiefes Wissen von dem, was wir durch die okkulte Wissenschaft erst erahnen.",
        "Was in unserem inneren menschlichen Organismus wirkt, das ist aus Welten herausgeboren wie ein Mikro-kosmos aus dem Makrokosmos, und wir sehen alle diese ungeheuren Weistümer ausgedrückt in Mythen und Sagen.",
        "Deshalb haben jene Okkultisten Recht, die in den Namen der Mythen und Sagen erst einen Sinn finden, wenn sie darin die Physiologie erkennen."
      ],
      [
        "Darauf sollte heute nur hingedeutet werden, weil es dazu dienen kann, uns jene Ehrfurcht anzueignen, von der in der ersten Stunde gesprochen worden ist.",
        "Wenn wir eine solche Betrachtungsweise üben, können wir wirklich hinweisen auf das, was sich einer tieferen Erforschung des geistigen Inhaltes der menschlichen Organe darbie­tet.",
        "Auch wenn wir das nur für ganz weniges darstellen können, so wird sich uns doch schon zeigen, welcher Wunderbau dieser mensch­liche Organismus ist.",
        "Und ein wenig werden wir gerade in diesem Vortragszyklus hineinzuleuchten versuchen in diese innere Wesen­heit des Menschen."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "VIERTER VORTRAG Prag, 23. März 1911",
    "paragraphs": [
      "Die gestrige Auseinandersetzung über die Bedeutung zunächst eines derjenigen Organe, welche gleichsam ein inneres Weltsystem des Menschen darstellen, soll heute fortgesetzt werden. Dann soll der Übergang gefunden werden zur Beschreibung der Aufgaben anderer Organe und Organsysteme des Menschen.",
      "Es ist mir gestern in Anknüpfung an das, was hier über das Organ der Milz vorgetragen wurde, gesagt worden, daß sich doch ein scheinbarer Widerspruch ergeben könnte gegenüber jener wichtigen Aufgabe, die dem Organ der Milz im Gesamtwesen des Menschen gestern zugeschrieben worden ist. Dieser Widerspruch könnte sich ergeben, wenn man bedenkt, daß es ja möglich ist, die Milz aus dem Körper herauszunehmen, sie also aus dem Körper zu entfernen, ohne durch diese Entfernung der Milz den Menschen lebensunfähig zu machen.",
      "Ein solcher Einwand ist natürlich einer derjenigen, die von unse­rem gegenwärtigen zeitgenössischen Standpunkte aus voll berechtigt sind und die gerade denjenigen gewisse Schwierigkeiten bieten, wel­che in ganz ehrlich suchender Art an die geisteswissenschaftliche Weltanschauung herankommen. Nur im allgemeinen konnte ja in dem ersten öffentlichen Vortrage darauf hingewiesen werden, wie unsere heutigen Zeitgenossen - namentlich dann, wenn sie ein durch die wissenschaftlichen Methoden geschultes Gewissen haben -Schwierigkeiten zu überwinden haben, wenn sie sich auf den Weg begeben, dasjenige zu verstehen, was aus den okkulten Untergründen des Weltwesens dargestellt wird. Nun werden wir ja im Laufe der Vorträge im Prinzip von selber sehen, wie sich ein solcher Einwand beheben läßt. Ich will aber doch heute schon vorbemerkend darauf aufmerksam machen, daß die Entfernung der Milz aus dem mensch­lichen Organismus durchaus vereinbar ist mit dem, was gestern aus­einandergesetzt worden ist. Wenn Sie wirklich aufsteigen wollen zu den geisteswissenschaftlichen Wahrheiten, müssen Sie sich ja allmählich",
      "dareinfinden, daß dasjenige, was wir den menschlichen Organis­mus nennen, was wir durch unsere äußeren Sinne wahrnehmen, was wir substantiell, materiell an diesem menschlichen Organismus sehen, daß dies nicht der ganze Mensch ist, sondern daß dem physi­schen Organismus - das werden wir noch weiter auszuführen haben",
      "zugrundeliegen höhere, übersinnliche Organisationen: der Äther-leib oder Lebensleib, der astralische Leib und das Ich, und daß wir im physischen Organismus nur den äußeren, den physischen Ausdruck haben für die entsprechende Gestaltung, für die entsprechenden Vor­gänge des Ätherleibes, des Astralleibes und des Ich. Wenn wir auf ein solches Organ hinweisen wie die Milz, so meinen wir es im geistes-wissenschaftlichen Sinne so, daß im Grunde genommen nicht nur in der äußeren physischen Milz etwas vor sich geht, sondern daß das, was in der physischen Milz vorgeht, nur der physische Ausdruck ist für entsprechende Vorgänge im Ätherleibe oder im Astralleibe.",
      "Und man könnte sagen: Je mehr ein Organ der unmittelbare physische Ausdruck eines Geistigen ist, desto weniger ist die physische Form des Organs, also das, was wir physisch-substantiell vor uns haben, das eigentlich Maßgebende. Wenn wir ein Pendel ansehen, so ist die Pendelbewegung nur der physische Ausdruck für die Schwerkraft.",
      "Ebenso ist ein physisches Organ nur der physische Ausdruck für übersinnliche Kraft- und Formwirkungen. Nun ist allerdings ein Unterschied zwischen den Folgen der Schwerkraft, welche sich in der Pendelbewegung zeigen, und den Folgen, welche entstehen durch die Wirkungen des Äther- und Astralleibes auf die Milz.",
      "Nimmt man das Pendel weg, so ist kein Objekt mehr vorhanden, an welchem sich der durch die Schwerkraft bewirkte Rhythmus zeigen kann. So ist es bei der unbelebten, anorganischen Natur, beim belebten Organismus ist es anders.",
      "Wenn nicht Gründe vorliegen, von denen wir noch spre­chen werden, so hören mit der Wegnahme des physischen Organs nicht notwendigerweise auch die geistigen Wirkungen der höheren Organisationen auf.",
      "Wenn wir also den Menschen in bezug auf seine Milz ansehen, so haben wir es zunächst zu tun mit der physischen Milz, und dann mit einem System von Kraftwirkungen, die in der Milz nur ihren physischen",
      "Ausdruck haben. Wenn man die Milz wegnimmt, dann sind diese Kraftwirkungen, die einmal dem menschlichen Organismus eingegliedert wurden, noch da, sie hören nicht auf. Es kann unter Umständen sogar sein, daß durch die Anwesenheit eines erkrankten physischen Organs ein viel größeres Hindernis eintritt für die Fort­dauer der geistigen Wirkungen als durch die Herausnahme des betreffenden Organs.",
      "Das kann zum Beispiel bei einer schweren Erkrankung der Milz der Fall sein. Wenn es bei einer schweren Erkrankung eines Organs möglich ist, das Organ zu entfernen, so ist unter Umständen das Fehlen dieses Organs ein geringeres Hindernis für die Entfaltung der geistigen Wirkungen als die Anwesenheit des erkrankten Organs, das ein fortwährender Störenfried ist für die Entwickelung der geistigen Kraftwirkungen.",
      "Daher gehört ein sol­cher Einwand, wie der angeführte, zu denjenigen, welche man gewiß macht, wenn man noch nicht tiefer in das eigentliche Wesen des geisteswissenschaftlichen Erkennens eingedrungen ist. Ein ganz begreiflicher Einwand ist es, aber zu gleicher Zeit einer derjenigen, die ganz von selbst verschwinden, wenn man sich Zeit läßt und Geduld hat, um tiefer in die Sache einzudringen.",
      "Diese Erfahrung werden Sie überhaupt machen: Wenn man mit einem gewissen Wis­sen, das aus den Anschauungen der heutigen materialistischen Wis­senschaft geschöpft ist, an das Studium der Geisteswissenschaft her­antritt, da kann sich Widerspruch auf Widerspruch ergeben, so daß man gar nicht zurechtkommen kann. Und wenn man da schnell fertig ist mit dem Urteilen, so wird man ja allerdings zu keinem anderen Ergebnis kommen können als zu dem, daß Geisteswissenschaft etwas Hirnverbranntes sei, das nicht im geringsten übereinstimme mit den Ergebnissen der äußeren Wissenschaft. - Wenn man aber sich mit Geduld und Zeit auf die Sache einläßt, dann wird man sehen, daß es keinen Widerspruch, auch nicht geringfügigster Art, gibt zwischen dem, was aus der Geisteswissenschaft kommt, und dem, was sich aus der äußeren wissenschaftlichen Forschung ergibt.",
      "Die Schwierigkeit, die da vorliegt, ist die, daß das Ges amtgebiet des anthroposophischen oder geisteswissenschaftlichen Erkennens ein so weites ist, daß man immer nur Teile geben kann. Und wenn die Leute an diese Teile",
      "herantreten, können sie leicht solche Widersprüche fühlen wie diesen charakterisierten.",
      "Aber das darf uns nicht zurückschrecken, man würde ja sonst gar nicht anfangen können mit dem notwendigen Hereinbringen anthro­posophischer Weltanschauung in die Gesamtbildung und in das Gesamtwissen unserer Zeit.",
      "Gestern versuchte ich Ihnen darzulegen jene Umrhythmisierung, welche durch die Milz bewirkt wird gegenüber dem äußeren rhyth­muslosen Ernähren des Menschen. Ich bin davon ausgegangen, weil es von allen Funktionen, welche die Milz hat, die am leichtesten verständliche ist.",
      "Aber obzwar es die am leichtesten verständliche ist, ist sie nicht die allerwichtigste und auch nicht die, welche die Haupt­sache bildet. Denn man könnte ja sagen: Nun ja, wenn der Mensch sich bemühen würde, den richtigen Rhythmus für seine Ernährung zu erkennen, so würde in dieser Hinsicht die Tätigkeit der Milz nach und nach eine unnötige werden müssen. - Schon daraus ersieht man, daß diese Funktion, von der wir gestern gesprochen haben, die geringfügigste ist.",
      "Weit wichtiger ist die Tatsache, daß wir bei unserer Ernährung den Nahrungsmitteln als äußeren Stoffen, in der Art und Weise ihrer Zusammensetzung, wie sie sich in unserer Umgebung vorfinden, gegenüberstehen. Solange man freilich die Anschauung hat, daß diese Nahrungsmittel tote Stoffe seien oder höchstens von dem Leben erfüllt, das man in den Pflanzen voraussetzt, solange man dies annimmt, könnte es allerdings scheinen, als ob der äußere Stoff, der da als Nahrung aufgenommen wird in den Organismus, durch das verarbeitet wird, was man im weitesten Sinne die Verdauung nennt.",
      "Gewiß stellen sich ja auch viele Menschen die Sache so vor, daß man es mit einem bestimmungslosen Stoff zu tun hat, den wir als unsere Nahrung aufnehmen, mit einem Stoff, der ganz gleichgültig ist gegen uns selbst und der nur darauf wartet, wenn wir ihn aufgenom­men haben, daß wir ihn auch verarbeiten können. So ist es aber nicht.",
      "Die Nahrungsstoffe sind doch nicht wie Ziegelsteine, die es sich gefallen lassen müssen, in jeder Art als Bausteine an einem Bau zu dienen, der eben aufgeführt werden soll. Die Ziegelsteine lassen es sich gefallen, in beliebiger Weise nach dem Plan des Architekten",
      "einem Bau eingefügt zu werden, weil sie eine in sich ungefügte, leblose Masse darstellen, wenigstens in bezug auf den Bau. So ist es aber nicht bei den Nahrungsmitteln in bezug auf den Menschen. Denn ein jedes Substantielle, das wir in unserer Umgebung haben, hat gewisse innere Kräfte, hat eine innere Gesetzmäßigkeit.",
      "Und das ist das Wesentliche eines Stoffes, daß er innere Gesetzmäßigkeiten, innere Regsamkeiten hat. Wenn wir also die äußeren Nahrungsstoffe in unseren Organismus hineinbringen, sie sozusagen unserer eigenen inneren Regsamkeit einfügen wollen, so lassen sie sich das nicht ohne weiteres gefallen, sondern legen es zunächst darauf an, ihre eigenen Gesetze, ihre eigenen Rhythmen und ihre eigenen inneren Bewe­gungsformen zu behalten.",
      "Und will der menschliche Organismus sie für seine Zwecke gebrauchen, so muß er zunächst die eigene Regsam­keit dieser Stoffe vernichten, er muß sie aufheben. Er muß nicht bloß ein gleichgültiges Material verarbeiten, sondern er muß der eigenen Gesetzmäßigkeit der Stoffe entgegenarbeiten.",
      "Daß diese Stoffe eine Eigengesetzmäßigkeit haben, das kann der Mensch zum Beispiel bald spüren, wenn er ein starkes Gift zu sich nimmt. Da wird er bald sehen, daß die Eigengesetzmäßigkeit des Giftes sich geltend macht und Herr über ihn wird.",
      "So wie aber ein Gift eine innere Gesetzmä­ßigkeit hat, durch die es eine Attacke auf den Organismus ausführt, so ist es mit jedem Nahrungsstoff, den wir zu uns nehmen. Er ist nicht etwas Gleichgültiges, sondern er macht sich in seiner eigenen Natur, in seiner eigenen Wesenheit geltend; er hat seinen eigenen Rhythmus.",
      "Und diesem Rhythmus muß vom Menschen entgegenge­arbeitet werden, so daß nicht nur gleichgültige Baumaterialien zu verarbeiten sind in der inneren Organisation des Menschen, sondern es muß zuerst die eigene Natur dieser Baumaterialien überwunden werden.",
      "So können wir sagen, daß wir in den Organen, denen unsere Nahrungsstoffe im Inneren des Menschen zuerst entgegentreten, die Werkzeuge haben, um demjenigen entgegenzuarbeiten, was Eigen­leben der Nahrungsstoffe ist - jetzt «Leben» im weitesten Sinne auf­gefaßt. Nicht nur das, was wir durch unregelmäßigen Rhythmus in der Ernährung selber bewirken, sondern auch das, was die Nahrungsstoffe",
      "an eigenem Rhythmus in sich haben, welcher dem menschli­chen Rhythmus widerspricht, das muß umrhythmisiert werden. Von den Organen, die dies bewirken, ist die Milz das äußerste Organ. Aber an diesem Umrhythmisieren, an diesem Umgestalten und Abwehren arbeiten die anderen genannten Organe wesentlich mit, so daß wir in Milz, Leber und Galle ein zusammenwirkendes Organ-system haben, welches im wesentlichen dazu bestimmt ist, bei der Aufnahme der Nahrungsmittel in den Organismus dasjenige zurück­zuschieben, was Eigennatur dieser Nahrungsmittel ist.",
      "Alle Tätigkeit, welche im Magen entfaltet wird, oder auch schon, bevor die Speise in den Magen gelangt, ferner das, was dann bewirkt wird durch die Absonderung der Galle, was dann weiter durch die Tätigkeit von Leber und Milz geschieht, das alles gibt eben diese Abwehr der Eigennatur der äußeren Nahrungsstoffe. Daher sind also unsere Nahrungsmittel erst dann dem inneren Rhythmus des menschlichen Organismus angepaßt, wenn ihnen die Wirksamkeiten dieser Organe entgegengetreten sind.",
      "Und erst dann, wenn wir die in uns aufge­nommenen Nahrungsmittel den Wirksamkeiten dieser Organe aus­gesetzt und sie umgewandelt haben, haben wir dasjenige in uns, was fähig ist, in jenes Organsystem aufgenommen zu werden, das der Träger, das Werkzeug unseres Ich ist, in das Blut. Bevor irgendein äußerer Nahrungsstoff in unser Blut aufgenommen werden kann, so daß dieses unser Blut die Fähigkeit erhält, Werkzeug zu sein für unser Ich, müssen all die Eigengesetzlichkeiten der Außenwelt abge­streift sein, und das Blut muß die Nahrungsstoffe in einer solchen Gestalt empfangen, die der eigenen Natur des menschlichen Organis­mus entspricht.",
      "Daher können wir sagen: In Milz, Leber und Galle und in ihrem Zurückwirken auf den Magen haben wir diejenigen Organe, welche die Gesetze der äußeren Welt, aus der wir unsere Nahrung entnehmen, anpassen der inneren Organisation, dem inne­ren Rhythmus des Menschen.",
      "Nun steht aber diese menschliche Natur, wie sie als Ganzes wirkt, mit allen ihren Gliedern nicht bloß der inneren Welt gegenüber, sondern diese innere menschliche Natur muß in einer fortwährenden Korrespondenz, in einem fortwährenden lebendigen Wechselwirken",
      "mit der Außenwelt sein. Dieses lebendige Wechselwirken mit der Außenwelt wird ja gerade dadurch abgeschnitten, daß den Gesetzen der Außenwelt, insofern wir mit ihr in Beziehung treten durch die Nahrungsstoffe, entgegengestellt werden die drei Organsysteme Leber, Galle, Milz.",
      "Durch diese wird die äußere Gesetzmäßigkeit weggenommen von innen her. Und es würde der menschliche Orga­nismus, wenn er nur diesen Organsystemen ausgesetzt wäre, sich von der Außenwelt vollständig abschließen, er würde ein vollkommen in sich isoliertes Wesen sein.",
      "Daher ist ein anderes ebenso notwendig. Wie der Mensch auf der einen Seite solche Organsysteme braucht, durch welche die Außenwelt so umgestaltet wird, daß sie seiner Innenwelt gemäß wird, so muß er auf der anderen Seite auch in der Lage sein, unmittelbar mit dem Werkzeug seines Ich der Außenwelt entgegenzutreten, unmittelbar also seinen Organismus, der sonst eine in sich isolierte Wesenheit wäre, mit der Außenwelt in Beziehung zu setzen.",
      "Während das Blut auf der einen Seite mit der Außenwelt nur so in Beziehung tritt, daß es von dieser Außenwelt nur das erhält, dem alle Eigengesetzmäßigkeit abgestreift ist, tritt es auf der anderen Seite mit der Außenwelt so in Beziehung, daß es unmittelbar an sie herantreten kann. Das geschieht, wenn das Blut durch die Lungen fließt und mit der äußeren Luft in Berührung kommt.",
      "Da wird es durch den Sauerstoff der äußeren Luft aufgefrischt und in einer solchen Weise gestaltet, daß jetzt dieser Gestaltung nichts abschwä­chend gegenübertritt, so daß in der Tat der Sauerstoff der Luft so herantritt an das Werkzeug des menschlichen Ich, wie es dessen eigenster Natur und Wesenheit entspricht. So sehen wir jene ganz merkwürdige Tatsache vor unser Auge treten, daß das edelste Werk­zeug, das der Mensch hat, das Blut, das Werkzeug seines Ich, wie ein Wesen dasteht, welches alle Nahrung sorgfältig filtriert erhält durch die früher charakterisierten Organsysteme.",
      "Dadurch ist das Blut in die Fähigkeit versetzt, ganz und gar ein Ausdruck der inneren Orga­nisation des Menschen zu werden, des inneren Rhythmus des Men­schen. Dadurch aber, daß das Blut unmittelbar in Berührung tritt mit denjenigen Stoffen der Außenwelt, die in seine innere Gesetzmäßig­keit und Regsamkeit aufgenommen werden dürfen, ohne daß sie",
      "unmittelbar bekämpft zu werden brauchen, dadurch ist diese menschliche Organisation nichts in sich Abgeschlossenes, sondern mit der Außenwelt voll in Berührung.",
      "So haben wir im menschlichen Blutorganismus auch von diesem Gesichtspunkte aus etwas ganz Wunderbares vor uns. Wir haben in ihm ein wirkliches, echtes Ausdrucksmittel des menschlichen Ich, das ja in der Tat auf der einen Seite der Außenwelt zugekehrt ist, auf der anderen Seite dem eigenen Innenleben zugekehrt ist.",
      "So wie wir gesehen haben, daß der Mensch durch sein Nervensystem den Impressionen der Außenwelt zugewendet ist, also die Außenwelt sozusagen auf dem Umwege durch die Nerven in sich aufnimmt, so kommt er in eine unmittelbare Berührung mit der Außenwelt durch sein Blut, indem das Blut den Sauerstoff der Luft durch die Lungen aufnimmt. Daher können wir also sagen: In dem, was uns gegeben ist auf der einen Seite in dem Milz-Leber-Gallesystem und auf der anderen Seite in dem Lungensystem, haben wir zwei einander entge­genwirkende Systeme, die sich gleichsam berühren in dem Blut.",
      "Außenwelt und Innenwelt berühren sich durch das Blut ganz unmit­telbar im menschlichen Organismus, indem das Blut von der einen Seite her mit der äußeren Luft in Berührung kommt und von der anderen Seite her mit den Nahrungsmitteln, denen ihre eigene Natur genommen ist. Es stoßen also, möchte man sagen, wie positive und negative Elektrizität, hier zwei Weltenwirkungen im Menschen zusammen.",
      "Und wir können uns sehr leicht vorstellen, wo das Organsystem liegt, welches bestimmt und geeignet ist, das Aufeinan­derprallen dieser beiden Weltenkraftsysteme auf sich wirken zu las­sen. Bis zum Herzen herauf, insofern das Blut durch das Herz strömt, wirken die umgewandelten Nahrungssäfte.",
      "Bis zum Herzen herein, insofern es vom Blute durchflossen wird, wirkt der Sauerstoff der Luft, der unmittelbar aus der Außenwelt in unser Blut tritt, so daß wir im Herzen dasjenige Organ haben, in dem sich diese zwei Systeme begegnen, in die der Mensch hineinverwoben ist, an denen er nach zwei Seiten hängt. Es ist mit diesem menschlichen Herzen so, daß wir sagen könnten: An ihm hängt auf der einen Seite der ganze menschliche innere Organismus, und auf der anderen Seite ist der",
      "Mensch durch das Herz unmittelbar angeknüpft an den Rhythmus, an die Regsamkeit der äußeren Welt.",
      "Wenn nun zwei solche Systeme zusammenstoßen, so könnte es ja sein, daß ihr Zusammenwirken eine unmittelbare Harmonie ergäbe. Wir könnten uns vorstellen, daß diese zwei Systeme - das System der großen Welt, das durch den aufgenommenen Sauerstoff oder die Luft überhaupt in uns hineinwirkt, und das System der kleinen Welt, unseres eigenen inneren Organismus, das uns die Nahrungsmittel umwandelt -, daß sich diese Systeme im Blute, indem es das Herz durchströmt, einen harmonischen Ausgleich schaffen. Wenn es so wäre, dann wäre der Mensch eingespannt in zwei Welten, die sozusa­gen sein inneres Gleichgewicht schüfen. Nun werden wir im Laufe dieser Vorträge noch sehen, daß es sich mit der Beziehung der Welt zur menschlichen Wesenheit nicht so verhält. Es ist vielmehr so, daß die Welt sich sozusagen ganz passiv verhält, daß sie nur ihre Kräfte aussendet und es dem Menschen überläßt, durch eigene innere Tätig­keit den Ausgleich zu schaffen zwischen den zweierlei Systemen, in deren Wirkungen wir eingespannt sind. Wir werden es immer mehr und mehr als das Wesentliche erkennen lernen, daß dem Menschen zuletzt immer ein Rest bleibt für seine innere Tätigkeit, daß es ihm -bis in seine Organe hinein - überlassen ist, den Ausgleich, das innere Gleichgewicht selber zu schaffen. So müssen wir auch im menschli­chen Organismus selber den Ausgleich, die Harmonisierung dieser beiden Weltsysteme suchen. Wir müssen uns von vornherein sagen:",
      "Durch die Gesetzmäßigkeiten der Außenwelt, die direkt in den Men­schen hineintreten, und durch die eigenen inneren Gesetzmäßigkei­ten des Menschen, in die er die Gesetzmäßigkeiten der Außenwelt umwandelt, welche er aufnimmt durch die Nahrung, ist noch nicht ohne weiteres die Harmonisierung der beiden Systeme gegeben. Die Harmonisierung muß sich erst durch ein besonderes eigenes Organ-system vollziehen. Der Mensch muß in sich selber die Harmonisie­rung herbeiführen. Das geschieht nicht in bewußten Vorgängen, sondern durch Vorgänge, die sich ganz unbewußt innerhalb des menschlichen Organismus abspielen. Dieser Ausgleich zwischen die­sen beiden Systemen wird dadurch herbeigeführt, daß zwischen dem",
      "Milz-Leber-Gallesystem auf der einen Seite und dem Lungensystem auf der anderen Seite, die sich in dem das Herz durchströmenden Blute gegenüberstehen, eingeschaltet ist dasjenige, was wir das Nie­rensystem nennen, das auch in inniger Verbindung steht mit dem Blutkreislauf.",
      "Im Nierensystem haben wir dasjenige, was sozusagen harmonisiert jene äußeren Wirkungen, die von dem unmittelbaren Berühren des Blutes mit der Luft herrühren, mit den Wirkungen, die von denjeni­gen inneren Organen des Menschen ausgehen, durch die die Nah­rungsstoffe erst zubereitet werden müssen, damit ihre Eigennatur abgestreift wird. In dem Nierensystem haben wir also ein solches ausgleichendes System, durch das der Organismus in die Lage kommt, den Überschuß abzugeben, der sich ergeben würde durch ein unharmonisches Zusammenwirken der beiden anderen Systeme.",
      "Damit haben wir der ganzen inneren Organisation - den Organen des Verdauungsapparates einschließlich derjenigen Organe, die wir dazurechnen müssen, wie Leber, Galle und Milz - dasjenige gegen­übergestellt, wofür diese Organe zunächst ihre vorbereitende Tätig­keit entwickelt haben, das Blutsystem. Und wir haben auf der ande­ren Seite diesem Blutsystem diejenigen Organe gegenübergestellt, durch welche der einseitigen Isolierung entgegengearbeitet und damit der Ausgleich geschaffen wird zwischen dem genannten inneren System und dem, was von außen her kommt. Wenn wir also - und wir werden noch sehen, wie sehr das berechtigt ist - das Blutsystem mit seinem Mittelpunkt, dem Herzen, uns in die Mitte des Organis­mus hineingestellt denken, so haben wir, sich angliedernd an dieses Blut-Herzsystem, auf der einen Seite das Leber-Galle-Milzsystem, auf der anderen Seite - und auf andere Weise mit dem Herzen in Verbindung stehend - das Lungensystem. Dazwischen ist das Nie­rensystem angeordnet. Wir werden später noch sehen, wie ungemein interessant der Zusammenhang ist zwischen dem Lungensystem und dem Nierensystem. Jetzt wollen wir darauf zunächst nicht näher eingehen, sondern das Ganze im Zusammenhang betrachten. Wenn wir die Systeme einfach ganz schematisch nebeneinander zeichnen (Zeichnung Seite 78 links), dann erkennen wir schon aus dieser",
      "schematischen Darstellung, wie die menschliche innere Organisation in einem gewissen Zusammenhange steht, und wir haben diesen Zusammenhang so dargestellt, daß wir in dem Herzen mit dem dazugehörigen Blutsystem das Allerwichtigste zu sehen haben.",
      "# Bild s.078",
      "Nun habe ich schon darauf hingewiesen - und wir werden noch im genaueren sehen, inwiefern eine solche Namengebung gerechtfertigt ist -, daß im Okkultismus die Milzwirkung als eine saturnische Wirkung bezeichnet wird, die Leberwirkung als eine Jupiter- und die der Galle als eine Marswirkung. Aus demselben Grunde sieht nun die okkulte Erkenntnis in dem Herzen und dem dazugehörigen Blutsy­stem dasjenige, was den Namen «Sonne» im menschlichen Organis­mus ebenso verdient wie die Sonne draußen innerhalb des Planeten-systems. Das Lungensystem bezeichnet der Okkultist nach demsel­ben Prinzip als «Merkur» und das Nierensystem mit dem Namen «Venus». So haben wir schon in der Benennung dieser Systeme des menschlichen Organismus - wenn wir jetzt auch gar nicht eingehen auf eine Rechtfertigung dieser Namen - etwas angedeutet wie ein inneres Weltsystem, was wir noch dadurch ergänzt haben, daß wir uns in die Lage versetzten, auch den Zusammenhang der beiden Organsysteme zu betrachten, die zum Blutsystem in Beziehung ste­hen. Erst wenn wir die Zusammenhänge in diesem Sinne betrachten,",
      "tritt uns das in einer Vollständigkeit entgegen, was wir die eigentliche menschliche innere Welt nennen können. Ich werde Ihnen nun in den folgenden Vorträgen auch noch zu zeigen haben, daß tatsächlich der Okkultist Gründe hat, das Verhältnis der Sonne zu Merkur und Venus in einer ähnlichen Weise sich vorzustellen, wie im menschli­chen Organismus das Verhältnis zwischen Herz, Lungen und Nieren gedacht werden muß.",
      "Wir sehen daraus, daß in dem Werkzeug unseres Ich, in unserem Blutsystem, das seinen Rhythmus im Herzen zum Ausdruck bringt, etwas gegeben ist, was gewissermaßen in seiner ganzen Gestaltung, in seiner inneren Natur und Wesenheit durch das innere Weltsystem des Menschen bestimmt wird, und daß es in ein solches [makrokos­misches] Gesamtsystem eingebettet sein muß, damit es so leben kann, wie es eben lebt. In diesem menschlichen Blutsystem - das habe ich schon öfter erwähnt - haben wir zu sehen das physische Werkzeug unseres Ich.",
      "Wir wissen ja, daß unser Ich, so wie wir es haben, nur dadurch möglich ist, daß dieses Ich aufgebaut ist auf Grundlage eines physischen Leibes, eines Ätherleibes und eines Astralleibes. Ein frei in der Welt herumfliegendes menschliches Ich ist innerhalb der Welt, die unsere Welt ist, nicht denkbar.",
      "Ein menschliches Ich setzt voraus als Grundlage einen Astralleib, einen Ätherleib und einen physischen Leib. Wie nun dieses Ich in geistiger Beziehung die drei genannten Wesensglieder des Menschen voraussetzt, so setzt sein physisches Organ, das Blutsystem, auch physisch solche Abbilder des astrali­schen und des ätherischen Leibes voraus.",
      "Das Blutsystem kann sich also nur auf der Grundlage von etwas anderem entwickeln. Während die Pflanze sich einfach entwickelt auf der Grundlage der sie umge­benden unorganischen Natur, indem sie gleichsam aus derselben herauswächst, müssen wir sagen, daß für den menschlichen Blutorga­nismus als Grundlage nicht ohne weiteres bloß die äußere Natur als Unterlage nötig ist, sondern es muß diese äußere Natur erst noch eine Umgestaltung erfahren.",
      "Wie der physische Leib des Menschen erst einen Ätherleib und einen Astralleib haben muß, so muß das, was an Nahrungsstoffen einströmt, erst umgestaltet werden. damit es dem menschlichen Ich als Werkzeug dienen kann.",
      "Wenn wir nun auch sagen können, daß dieses physische Werkzeug des menschlichen Ich, das Blut, durch die Lunge von außen bestimmt wird, so ist die Lunge selber doch ein Organ der physischen Leibes-Organisation, das heißt, es ist nicht dieses Organ, sondern die durch dasselbe eingeatmete Luft, welche es möglich macht, mit einem äuße­ren Rhythmus auf das Blut einzuwirken. Wir müssen unterscheiden zwischen dem, was von außen an den Menschen herankommt in Form der Luft, die eingeatmet wird und die es dem Menschen mög­lich macht, mit einem äußeren Rhythmus unmittelbar sein Blutsy­stem zu durchdringen, und dem, was nicht unmittelbar an das leben­dige Werkzeug des Ich im Organismus, an das Blut, herantritt, sondern was herantritt - in der Art, wie es schon charakterisiert worden ist - auf dem Umwege durch die Seele, was der Mensch also dadurch aufnimmt, daß er die Eindrücke der Außenwelt durch die Sinne empfängt und diese Sinne dann ihre Eindrücke auch vermitteln bis zur Bluttafel hin.",
      "Deshalb werden wir sagen können: Der Mensch tritt nicht bloß mit der Außenwelt unmittelbar stofflich in Berührung durch die Atmungsluft, indem diese Berührung hereinwirkt bis auf sein Blut, sondern er tritt durch die Sinnesorgane mit der Außenwelt auch so in Berührung, daß diese Berührung eine nichtstoffliche ist, wie sie in dem Prozeß der Wahrnehmung stattfindet, den die Seele entfaltet, wenn sie zur Umwelt in Beziehung tritt. Da haben wir etwas, was sich als ein höherer Prozeß hinzufügt zum Atmungspro­zeß, wir haben etwas wie einen vergeistigten Atmungsprozeß.",
      "Wäh­rend wir durch den Atmungsprozeß die Außenwelt stofflich aufneh­men, nehmen wir im Wahrnehmungsprozeß - und ich meine jetzt mit «Wahrnehmung» alles, was der Mensch an äußeren Impressionen verarbeitet - etwas durch einen vergeistigten Atmungsprozeß in unseren Organismus auf. Und es entsteht jetzt die Frage: Wie wirken diese beiden Prozesse zusammen?",
      "Denn im menschlichen Organis­mus muß alles aufeinander einwirken.",
      "Legen wir uns einmal diese Frage genauer vor - denn es wird Wesentliches davon abhängen, daß wir sie uns genau vorlegen -, um uns die heute zunächst hypothetisch zu gebende Antwort vor unsere Seele führen zu können. Wir müssen uns darüber klar werden, wie",
      "ein Zusammenwirken, ein Wechselwirken stattfinden kann zwischen alle dem, was durch das Blut wirkt und was es geworden ist dadurch, daß alle diese inneren Organprozesse stattgefunden haben, und dem, was das Blut wird, indem wir äußere Wahrnehmungsprozesse voll­ziehen. Wir müssen sehen, daß da eine Wechselwirkung stattfinden kann.",
      "Das Blut ist, trotzdem es so eingehend und so vielseitig filtriert ist, trotzdem so vieles dafür gesorgt hat, daß es ein so wunderbar organisierter Stoff ist, der Werkzeug unseres Ich sein kann, das Blut ist trotzdem eine physische Substanz und gehört als solche zum physischen Leibe. Daher können wir sagen: Zunächst erscheint uns ein weiter, weiter Abstand zwischen dem, was im menschlichen Blute an physischen Prozessen wirkt, und dem, was wir als unsere Wahr-nehmungsprozesse kennen, die die Seele vollzieht.",
      "Das ist eine nicht abzuleugnende Realität; denn der Mensch müßte ja auf sonderbare Weise nicht zu denken verstehen, der ableugnen wollte, daß Wahr­nehmungen, Begriffe, Ideen, Gefühle, Willensimpulse ebenso etwas Reales sind wie Blutsubstanz, Nervensubstanz, Lebersubstanz, Gal­lensubstanz und so weiter. Wie diese Dinge zusammenhängen, dar­über können sich die Weltanschauungen streiten; sie können sich darüber streiten, ob die Gedanken bloß irgendwelche Wirkungen, sagen wir, der Nervensubstanz oder dergleichen seien.",
      "Da kann vielleicht ein Streiten der Weltanschauungen beginnen. Aber keinen Streit kann es darüber geben, weil es eine selbstverständliche Sache ist, daß unser Seeleninnenleben, unser Gedankenleben, unser Gefühlsleben, alles was sich aufbaut auf Grund der äußeren Wahr­nehmungen und Eindrücke, eine Realität für sich darstellt.",
      "Wohlge­merkt, ich sage nicht: eine abgesonderte Realität -, sondern: eine Realität für sich, denn nichts ist in der Welt abgesondert. Mit «Reali­tät für sich» soll nur angedeutet werden, was real beobachtet werden kann, und dazu gehören Gedanken, Gefühle und so weiter ebenso wie Magen, Leber, Galle und Milz.",
      "Aber ein anderes kann uns auffallen, wenn wir diese zwei Realitä­ten nebeneinanderstellen: Auf der einen Seite alles, was ein selbst noch so stark filtriertes Materielles, Physisches ist wie das Blut, und auf der anderen Seite das, was ja mit einem Physischen gar nichts zu",
      "tun zu haben scheint zunächst, nämlich die Inhalte der Seele, die Gefühle, Gedanken und so weiter. In der Tat bietet der Anblick dieser zweierlei Arten von Realitäten für den Menschen solche Schwierigkeiten, daß sich an diesen Anblick angegliedert haben die allermannigfaltigsten Antworten aus den verschiedensten Weltan­schauungen heraus.",
      "Da gibt es Weltanschauungen, welche eine unmittelbare Einwirkung des Seelischen, des Gedanklichen, des Gefühlsmäßigen auf die physische Substanz annehmen, wie wenn der Gedanke unmittelbar auf die physische Substanz wirken könnte. Denen stehen andere gegenüber, die materialistischen, die annehmen, daß Gedanken, Gefühle und so weiter einfach produziert werden aus den Vorgängen des Physisch-Substantiellen heraus.",
      "Der Streit dieser beiden Weltanschauungen hat ja in der äußeren Welt - nicht für den Okkultisten, für den dieser Streit ein Streit mit leeren Worten ist -durch lange Zeiten hindurch eine große Rolle gespielt. Und als man endlich gar nicht mehr zurechtgekommen ist, da ist in der neueren Zeit noch etwas anderes aufgetreten, was den sonderbaren Namen «psychophysischer Parallelismus» führt.",
      "Weil man sich gar nicht mehr zu helfen wußte, welcher nun von den beiden Gedanken der richtige ist - entweder wirkt der Geist auf die leiblichen Prozesse, oder es wirken die leiblichen Prozesse auf den Geist -, so sagte man eben einfach, das seien zwei Vorgänge, die parallel ablaufen. Man sagte sich: Während der Mensch denkt, fühlt und so weiter, laufen parallel in seinen physischen Organsystemen ganz bestimmte Vorgänge ab. - Die Wahrnehmung «Ich sehe Rot» würde also entspre­chen irgendeinem materiellen Vorgang innerhalb des Nervensystems.",
      "Was wir empfinden bei einem roten Eindruck, was wir fühlen an Freude oder Schmerz bei ihm, entspricht einem materiellen Vorgang. Aber weiter geht man nicht, als zu sagen, daß er eben «entspricht». Diese Theorie hebt in der Tat die ganzen Schwierigkeiten auf, indem sie diese einfach wegexpliziert.",
      "Nun, alle Streitereien, die sich auf diesem Boden entsponnen haben und auch die Hilflosigkeit des psychophy­sischen Parallelismus ergeben sich daraus, daß man diese Fragen entscheiden will auf einem Boden, auf dem sie gar nicht ausgetragen werden können. Wir haben es mit nichtmateriellen Vorgängen zu",
      "tun, wenn wir die Tätigkeiten unseres inneren Seelenlebens ins Auge fassen, und wir haben es mit materiellen Vorgängen zu tun, wenn wir, selbst über etwas so fein organisiertes wie es das Blut ist, unsere Betrachtungen anstellen. Wenn man diese zwei Dinge einfach gegen­überstellt - physische Betätigung und seelische Betätigung - und jetzt durch Nachdenken herausbekommen will, wie diese beiden aufein­ander wirken, so ergibt dieses Nachdenken eben gar nichts. Durch Nachdenken kann man alle willkürlichen Lösungen oder Nichtlö­sungen finden. Erst dadurch wird über diese Fragen etwas entschie­den werden können, daß wir uns wirklich eine höhere Erkenntnis aneignen, die weder stehenbleibt bei dem physischen Anschauen der Außenwelt noch bei dem an die bloße physische Außenwelt gebun­denen Denken. Wir müssen eine Form der Erkenntnis finden, die sich erhebt zu dem, was über das Physische hinaus in die überphysi­sche Welt führt. Wir müssen auf der einen Seite von dem Materiellen hinaufsteigen zu dem Übermateriellen, zu dem Überphysischen, wir müssen aber auf der anderen Seite auch von dem Seelenleben, das sich in der physischen Welt abspielt, hinaufsteigen zu dem, was unserem Seelenleben zugrundeliegt in der überphysischen Welt, denn mit unserem Seelenleben, mit allen unseren Gefühlen und so weiter leben wir ja auch in der physischen Welt. Wir müssen also von zwei Seiten her aufsteigen zu einer überphysischen Welt.",
      "Um von der materiellen Seite her in die überphysische Welt aufzu­steigen, dazu sind jene Seelenübungen notwendig, welche es dem Menschen möglich machen, hinter das äußere Sinnliche zu schauen, hinter den Schleier, von dem ich gesprochen habe, in welchen unsere Sinneseindrücke hineinverwoben sind. Solche Sinneseindrücke haben wir ja auch dann vor uns, wenn wir den äußeren menschlichen Organismus betrachten, auch bei dem am feinsten Organisierten des menschlichen Organismus, dem Blute, haben wir es mit einem Phy­sisch-Sinnlichen zu tun. Es sind Seelenübungen notwendig, um den Menschen in die übersinnliche Welt hineinzuführen. Zunächst muß er eine Stufe tiefersteigen als dort, wo er war, als er die Seelenein­drücke in sich aufnehmen konnte, unter den Plan des Physischen. In den Untergründen der physisch-sinnlichen Welt, da tritt ihm als das",
      "Übersinnliche der menschlichen Organisation der Ätherleib entge­gen. Dieser Ätherleib - wir werden ihn noch genauer besprechen gerade vom okkult-physiologischen Standpunkte aus - ist eine über­sinnliche Organisation, die wir uns zunächst einfach denken als die übersinnliche Grundsubstanz, aus der sich der sinnliche Organismus des Menschen herausgliedert und von dem er ein Abbild, ein Abdruck ist. Von diesem Ätherleibe ist selbstverständlich auch das Blut ein Abdruck. Wir haben also jetzt hier, indem wir um eine Stufe hinter den physisch-sinnlichen Organismus getreten sind, ein über-sinnliches Glied in dem menschlichen Ätherleibe gefunden. Und es fragt sich nun: Können wir an dieses Übersinnliche, an diesen Äther-leib, nun auch herankommen von der anderen Seite her, von der Seite des Seelischen her, von unseren Empfindungen, Gedanken, Gefühlen her, die wir uns aufbauen aus Eindrücken der Außenwelt?",
      "Da stellt sich nun allerdings heraus: So unmittelbar, wie wir unser Seelenleben haben, kommen wir nicht gleich an den Ätherorganis­mus heran. Aber - und damit lassen Sie mich die heutige Betrachtung ausklingen - wenn wir in unserer Seele arbeiten, so geschieht das ja so, daß wir zunächst die äußeren Eindrücke bekommen, auf die Sinne wirkt die äußere Welt, dann verarbeiten wir in unserer Seele die äußeren Eindrücke; aber wir tun noch mehr, wir speichern gleichsam diese empfangenen Eindrücke in uns selber auf. Denken Sie nur einmal nach über die einfache Erscheinung des Gedächtnisses, der Erinnerung. Wenn Sie sich an etwas erinnern, woran Sie vor Jahren auf Grundlage äußerer Wahrnehmungen Eindrücke gewonnen haben, sich Vorstellungen gebildet haben, die Sie heute aus den Untergründen Ihrer Seele heraufholen, und es kommt Ihnen die Erinnerung, sagen wir an etwas ganz einfaches, einen Baum oder einen Geruch, da müssen Sie sagen, Sie haben in Ihrer Seele etwas aufgespeichert, was Ihnen hat bleiben können von dem äußeren Eindruck. Nun zeigt uns aber eine wiederum nur durch Übungen der Seele zu gewinnende Betrachtung des Seelenlebens selber, daß in dem Augenblick, wo wir unser Seelenleben soweit haben, daß wir aufge­speicherte Eindrücke als Erinnerungsvorstellungen zurückrufen kön­nen, wir mit unseren seelischen Erlebnissen nicht nur in unserem Ich",
      "wirken. Zunächst tun wir das ja, indem wir mit unserem Ich der Außenwelt gegenübertreten, Eindrücke aus ihr aufnehmen und sie verarbeiten im Astralleibe. Würden wir aber nur das tun, so würden wir alles gleich wieder vergessen. Wenn wir Schlüsse ziehen, arbeiten wir im Astralleib. Wenn wir aber die Eindrücke in uns so fest machen, daß wir sie nach einiger Zeit - ja, oder auch nur nach Minuten - wieder heraufholen können, dann prägen wir die Ein­drücke, die wir durch unser Ich gewonnen und durch unseren Astral­leib verarbeitet haben, in unseren Ätherleib ein; so daß wir also in den Gedächtnisvorstellungen vom Ich aus hineingepreßt haben in den Atherleib dasjenige, was wir als seelische Betätigung in der Berührung mit der Außenwelt gewonnen haben. Wenn wir nun die Fähigkeit haben, von unserer Seele her in den Ätherleib hineinzu­pressen unsere Erinnerungsvorstellungen, und wenn wir den Äther-leib auf der anderen Seite anerkennen als den nächsten übersinnlichen Ausdruck unseres Organismus, so fragt es sich nun: Wie geschieht dieses Hineinpressen? Wie geht das vor sich, daß der Mensch tatsäch­lich das, was vom Astralleibe verarbeitet ist, jetzt wirklich in den Ätherleib hineinbringt? Wie kann er es in den Ätherleib überleiten?",
      "Diese Überleitung geschieht auf eine sehr merkwürdige Weise. Wenn wir zunächst ganz schematisch den Verlauf des Blutes durch den ganzen menschlichen Körper betrachten und dieses Blut als den äußeren physischen Ausdruck des menschlichen Ich fassen, so sehen wir - wenn wir das jetzt so betrachten, als ob wir im Ätherleibe drinnen stünden -, wie das Ich arbeitet in Korrespondenz mit der Außenwelt, wie es Impressionen empfängt und diese zu Vorstellun­gen verdichtet, und wir sehen, wie dabei in der Tat unser Blut nicht nur tätig ist, sondern wie unser Blut im ganzen Verlauf, namentlich nach oben zu - nach unten weniger-, überall den Ätherleib erregt, so daß wir überall im Ätherleibe Strömungen sich entwickeln sehen, die einen ganz bestimmten Verlauf nehmen. Sie erscheinen so, als ob sie sich an das Blut anschließen würden, vom Herzen nach dem Kopfe gehen und sich im Kopfe sammeln würden. Sie sammeln sich unge­fähr so - wenn ich jetzt einen äußeren Vergleich gebrauchen darf -, wie etwa Ströme von Elektrizität einer Spitze zugehen, der eine",
      "andere Spitze entgegengestellt ist, und so zum Ausgleich von positi­ver und negativer Elektrizität hinstreben.",
      "Wenn wir diesen Vorgang okkult betrachten mit entsprechend geübter Seele, so sehen wir, wie in einem Punkte sich jene Äther-kräfte unter einer gewaltigen Spannung zusammendrängen, welche hervorgerufen sind durch die Eindrücke, die jetzt gewisse Vorstel­lungen werden wollen, Gedächtnisvorstellungen, die sich in den Ätherleib einprägen wollen. Man sieht es den Ätherkräften an, daß sie Gedächtniskräfte werden wollen. Ich will die letzten Ausläufer dieser Ätherströmungen nach dem Gehirn herauf und das Sich­zusammendrängen so zeichnen, wie es sich etwa wirklich darstellen",
      "# Bild s.086",
      "würde. Wir sehen da eine mächtige Spannung, die sich an einer Stelle sammelt und gleichsam sagt: Ich will in den Ätherleib hinein! - Wir sehen nun, wie dieser Ätherströmung des Kopfes andere Strömungen entgegenkommen, die ausgehen namentlich von den Lymphgefäßen und die sich so sammeln, daß sie sich der ersten Strömung entgegen­stellen. So haben wir im Gehirn, wenn sich eine Gedächtnisvorstel­lung bilden will, einander gegenüberstehen zwei Ätherströmungen, die sich mit größtmöglicher Kraft konzentrieren, etwa so wie positive und negative Elektrizität sich an ihren Polen mit größter Spannung konzentrieren und nach Ausgleich streben. Ein Ausgleich zwischen den beiden Ätherströmungen geschieht in der Tat, und wenn er vollzogen ist, dann ist eine Vorstellung Gedächtnisvorstellung geworden und hat sich dem Ätherleibe einverleibt.",
      "# Bild s.087a",
      "Solche übersinnlichen Realitäten, solche übersinnlichen Strömun­gen im menschlichen Organismus drücken sich dadurch aus, daß sie sich auch ein physisch-sinnliches Organ schaffen, welches wir wie eine Versinnlichung solcher Strömungen anzusehen haben. So haben wir ein Organ, welches sich im mittleren Gehirn befindet, das der physisch-sinnliche Ausdruck ist für das, was als Gedächtnisvorstel­lung sich bilden will. Dem stellt sich gegenüber ein anderes Organ im Gehirn, das der Ausdruck ist für diejenigen Strömungen im Äther­leib, die von den unteren Organen kommen. Diese beiden Organe im menschlichen Gehirn sind der physisch-sinnliche Ausdruck für diese beiden Strömungen im menschlichen Ätherleibe, sie sind etwas wie letzte Anzeichen dafür, daß solche Strömungen im Ätherleibe statt­finden. Es verdichten sich gleichsam diese Strömungen so stark, daß sie die menschliche Leibessubstanz ergreifen und zu diesen Organen verdichten, so daß wir in der Tat den Eindruck haben, wie wenn von dem einen Organ helle Lichtströmungen ausstrahlen, die zu dem anderen Organ überfließen. Das physische Organ, das die Gedächt­nisvorstellung bilden will, ist die Zirbeldrüse, der aufnehmende Teil ist der Gehirnanhang, Hypophysis.",
      "# Bild s.087b",
      "Hier haben Sie an einer ganz bestimmten Stelle des physischen Organismus den äußeren physischen Ausdruck für das Zusammen­wirken des Seelischen mit dem Leiblichen!",
      "Es soll das zunächst nur wie eine prinzipielle Darstellung sein, womit wir unsere heutige Betrachtung ausklingen lassen wollen, die wir morgen weiter ausführen wollen und an die wir Genaueres und Beweisbares anknüpfen wollen. Es ist wichtig, daß wir den Gedan­ken genau festhalten, daß wir im Übersinnlichen forschen können, und uns dann fragen können, ob der zu erwartende physische Aus­druck für das Übersinnliche auch vorhanden ist. Wir sahen hier, daß das der Fall ist. Da es sich aber hier um die Eingangspforte vom Sinnlichen zum Übersinnlichen handelt, so werden Sie es begreifen, daß diese Organe für die physische Wissenschaft höchst zweifelhafte Organe sind, und daß Sie über diese Organe von der äußeren Wissen­schaft nur außerordentlich unzureichende und ungenügende Aus­kunft erhalten können."
    ],
    "sentences": [
      [
        "Die gestrige Auseinandersetzung über die Bedeutung zunächst eines derjenigen Organe, welche gleichsam ein inneres Weltsystem des Menschen darstellen, soll heute fortgesetzt werden.",
        "Dann soll der Übergang gefunden werden zur Beschreibung der Aufgaben anderer Organe und Organsysteme des Menschen."
      ],
      [
        "Es ist mir gestern in Anknüpfung an das, was hier über das Organ der Milz vorgetragen wurde, gesagt worden, daß sich doch ein scheinbarer Widerspruch ergeben könnte gegenüber jener wichtigen Aufgabe, die dem Organ der Milz im Gesamtwesen des Menschen gestern zugeschrieben worden ist.",
        "Dieser Widerspruch könnte sich ergeben, wenn man bedenkt, daß es ja möglich ist, die Milz aus dem Körper herauszunehmen, sie also aus dem Körper zu entfernen, ohne durch diese Entfernung der Milz den Menschen lebensunfähig zu machen."
      ],
      [
        "Ein solcher Einwand ist natürlich einer derjenigen, die von unse­rem gegenwärtigen zeitgenössischen Standpunkte aus voll berechtigt sind und die gerade denjenigen gewisse Schwierigkeiten bieten, wel­che in ganz ehrlich suchender Art an die geisteswissenschaftliche Weltanschauung herankommen.",
        "Nur im allgemeinen konnte ja in dem ersten öffentlichen Vortrage darauf hingewiesen werden, wie unsere heutigen Zeitgenossen - namentlich dann, wenn sie ein durch die wissenschaftlichen Methoden geschultes Gewissen haben -Schwierigkeiten zu überwinden haben, wenn sie sich auf den Weg begeben, dasjenige zu verstehen, was aus den okkulten Untergründen des Weltwesens dargestellt wird.",
        "Nun werden wir ja im Laufe der Vorträge im Prinzip von selber sehen, wie sich ein solcher Einwand beheben läßt.",
        "Ich will aber doch heute schon vorbemerkend darauf aufmerksam machen, daß die Entfernung der Milz aus dem mensch­lichen Organismus durchaus vereinbar ist mit dem, was gestern aus­einandergesetzt worden ist.",
        "Wenn Sie wirklich aufsteigen wollen zu den geisteswissenschaftlichen Wahrheiten, müssen Sie sich ja allmählich"
      ],
      [
        "dareinfinden, daß dasjenige, was wir den menschlichen Organis­mus nennen, was wir durch unsere äußeren Sinne wahrnehmen, was wir substantiell, materiell an diesem menschlichen Organismus sehen, daß dies nicht der ganze Mensch ist, sondern daß dem physi­schen Organismus - das werden wir noch weiter auszuführen haben"
      ],
      [
        "zugrundeliegen höhere, übersinnliche Organisationen: der Äther-leib oder Lebensleib, der astralische Leib und das Ich, und daß wir im physischen Organismus nur den äußeren, den physischen Ausdruck haben für die entsprechende Gestaltung, für die entsprechenden Vor­gänge des Ätherleibes, des Astralleibes und des Ich.",
        "Wenn wir auf ein solches Organ hinweisen wie die Milz, so meinen wir es im geistes-wissenschaftlichen Sinne so, daß im Grunde genommen nicht nur in der äußeren physischen Milz etwas vor sich geht, sondern daß das, was in der physischen Milz vorgeht, nur der physische Ausdruck ist für entsprechende Vorgänge im Ätherleibe oder im Astralleibe."
      ],
      [
        "Und man könnte sagen: Je mehr ein Organ der unmittelbare physische Ausdruck eines Geistigen ist, desto weniger ist die physische Form des Organs, also das, was wir physisch-substantiell vor uns haben, das eigentlich Maßgebende.",
        "Wenn wir ein Pendel ansehen, so ist die Pendelbewegung nur der physische Ausdruck für die Schwerkraft."
      ],
      [
        "Ebenso ist ein physisches Organ nur der physische Ausdruck für übersinnliche Kraft- und Formwirkungen.",
        "Nun ist allerdings ein Unterschied zwischen den Folgen der Schwerkraft, welche sich in der Pendelbewegung zeigen, und den Folgen, welche entstehen durch die Wirkungen des Äther- und Astralleibes auf die Milz."
      ],
      [
        "Nimmt man das Pendel weg, so ist kein Objekt mehr vorhanden, an welchem sich der durch die Schwerkraft bewirkte Rhythmus zeigen kann.",
        "So ist es bei der unbelebten, anorganischen Natur, beim belebten Organismus ist es anders."
      ],
      [
        "Wenn nicht Gründe vorliegen, von denen wir noch spre­chen werden, so hören mit der Wegnahme des physischen Organs nicht notwendigerweise auch die geistigen Wirkungen der höheren Organisationen auf."
      ],
      [
        "Wenn wir also den Menschen in bezug auf seine Milz ansehen, so haben wir es zunächst zu tun mit der physischen Milz, und dann mit einem System von Kraftwirkungen, die in der Milz nur ihren physischen"
      ],
      [
        "Ausdruck haben.",
        "Wenn man die Milz wegnimmt, dann sind diese Kraftwirkungen, die einmal dem menschlichen Organismus eingegliedert wurden, noch da, sie hören nicht auf.",
        "Es kann unter Umständen sogar sein, daß durch die Anwesenheit eines erkrankten physischen Organs ein viel größeres Hindernis eintritt für die Fort­dauer der geistigen Wirkungen als durch die Herausnahme des betreffenden Organs."
      ],
      [
        "Das kann zum Beispiel bei einer schweren Erkrankung der Milz der Fall sein.",
        "Wenn es bei einer schweren Erkrankung eines Organs möglich ist, das Organ zu entfernen, so ist unter Umständen das Fehlen dieses Organs ein geringeres Hindernis für die Entfaltung der geistigen Wirkungen als die Anwesenheit des erkrankten Organs, das ein fortwährender Störenfried ist für die Entwickelung der geistigen Kraftwirkungen."
      ],
      [
        "Daher gehört ein sol­cher Einwand, wie der angeführte, zu denjenigen, welche man gewiß macht, wenn man noch nicht tiefer in das eigentliche Wesen des geisteswissenschaftlichen Erkennens eingedrungen ist.",
        "Ein ganz begreiflicher Einwand ist es, aber zu gleicher Zeit einer derjenigen, die ganz von selbst verschwinden, wenn man sich Zeit läßt und Geduld hat, um tiefer in die Sache einzudringen."
      ],
      [
        "Diese Erfahrung werden Sie überhaupt machen: Wenn man mit einem gewissen Wis­sen, das aus den Anschauungen der heutigen materialistischen Wis­senschaft geschöpft ist, an das Studium der Geisteswissenschaft her­antritt, da kann sich Widerspruch auf Widerspruch ergeben, so daß man gar nicht zurechtkommen kann.",
        "Und wenn man da schnell fertig ist mit dem Urteilen, so wird man ja allerdings zu keinem anderen Ergebnis kommen können als zu dem, daß Geisteswissenschaft etwas Hirnverbranntes sei, das nicht im geringsten übereinstimme mit den Ergebnissen der äußeren Wissenschaft. - Wenn man aber sich mit Geduld und Zeit auf die Sache einläßt, dann wird man sehen, daß es keinen Widerspruch, auch nicht geringfügigster Art, gibt zwischen dem, was aus der Geisteswissenschaft kommt, und dem, was sich aus der äußeren wissenschaftlichen Forschung ergibt."
      ],
      [
        "Die Schwierigkeit, die da vorliegt, ist die, daß das Ges amtgebiet des anthroposophischen oder geisteswissenschaftlichen Erkennens ein so weites ist, daß man immer nur Teile geben kann.",
        "Und wenn die Leute an diese Teile"
      ],
      [
        "herantreten, können sie leicht solche Widersprüche fühlen wie diesen charakterisierten."
      ],
      [
        "Aber das darf uns nicht zurückschrecken, man würde ja sonst gar nicht anfangen können mit dem notwendigen Hereinbringen anthro­posophischer Weltanschauung in die Gesamtbildung und in das Gesamtwissen unserer Zeit."
      ],
      [
        "Gestern versuchte ich Ihnen darzulegen jene Umrhythmisierung, welche durch die Milz bewirkt wird gegenüber dem äußeren rhyth­muslosen Ernähren des Menschen.",
        "Ich bin davon ausgegangen, weil es von allen Funktionen, welche die Milz hat, die am leichtesten verständliche ist."
      ],
      [
        "Aber obzwar es die am leichtesten verständliche ist, ist sie nicht die allerwichtigste und auch nicht die, welche die Haupt­sache bildet.",
        "Denn man könnte ja sagen: Nun ja, wenn der Mensch sich bemühen würde, den richtigen Rhythmus für seine Ernährung zu erkennen, so würde in dieser Hinsicht die Tätigkeit der Milz nach und nach eine unnötige werden müssen. - Schon daraus ersieht man, daß diese Funktion, von der wir gestern gesprochen haben, die geringfügigste ist."
      ],
      [
        "Weit wichtiger ist die Tatsache, daß wir bei unserer Ernährung den Nahrungsmitteln als äußeren Stoffen, in der Art und Weise ihrer Zusammensetzung, wie sie sich in unserer Umgebung vorfinden, gegenüberstehen.",
        "Solange man freilich die Anschauung hat, daß diese Nahrungsmittel tote Stoffe seien oder höchstens von dem Leben erfüllt, das man in den Pflanzen voraussetzt, solange man dies annimmt, könnte es allerdings scheinen, als ob der äußere Stoff, der da als Nahrung aufgenommen wird in den Organismus, durch das verarbeitet wird, was man im weitesten Sinne die Verdauung nennt."
      ],
      [
        "Gewiß stellen sich ja auch viele Menschen die Sache so vor, daß man es mit einem bestimmungslosen Stoff zu tun hat, den wir als unsere Nahrung aufnehmen, mit einem Stoff, der ganz gleichgültig ist gegen uns selbst und der nur darauf wartet, wenn wir ihn aufgenom­men haben, daß wir ihn auch verarbeiten können.",
        "So ist es aber nicht."
      ],
      [
        "Die Nahrungsstoffe sind doch nicht wie Ziegelsteine, die es sich gefallen lassen müssen, in jeder Art als Bausteine an einem Bau zu dienen, der eben aufgeführt werden soll.",
        "Die Ziegelsteine lassen es sich gefallen, in beliebiger Weise nach dem Plan des Architekten"
      ],
      [
        "einem Bau eingefügt zu werden, weil sie eine in sich ungefügte, leblose Masse darstellen, wenigstens in bezug auf den Bau.",
        "So ist es aber nicht bei den Nahrungsmitteln in bezug auf den Menschen.",
        "Denn ein jedes Substantielle, das wir in unserer Umgebung haben, hat gewisse innere Kräfte, hat eine innere Gesetzmäßigkeit."
      ],
      [
        "Und das ist das Wesentliche eines Stoffes, daß er innere Gesetzmäßigkeiten, innere Regsamkeiten hat.",
        "Wenn wir also die äußeren Nahrungsstoffe in unseren Organismus hineinbringen, sie sozusagen unserer eigenen inneren Regsamkeit einfügen wollen, so lassen sie sich das nicht ohne weiteres gefallen, sondern legen es zunächst darauf an, ihre eigenen Gesetze, ihre eigenen Rhythmen und ihre eigenen inneren Bewe­gungsformen zu behalten."
      ],
      [
        "Und will der menschliche Organismus sie für seine Zwecke gebrauchen, so muß er zunächst die eigene Regsam­keit dieser Stoffe vernichten, er muß sie aufheben.",
        "Er muß nicht bloß ein gleichgültiges Material verarbeiten, sondern er muß der eigenen Gesetzmäßigkeit der Stoffe entgegenarbeiten."
      ],
      [
        "Daß diese Stoffe eine Eigengesetzmäßigkeit haben, das kann der Mensch zum Beispiel bald spüren, wenn er ein starkes Gift zu sich nimmt.",
        "Da wird er bald sehen, daß die Eigengesetzmäßigkeit des Giftes sich geltend macht und Herr über ihn wird."
      ],
      [
        "So wie aber ein Gift eine innere Gesetzmä­ßigkeit hat, durch die es eine Attacke auf den Organismus ausführt, so ist es mit jedem Nahrungsstoff, den wir zu uns nehmen.",
        "Er ist nicht etwas Gleichgültiges, sondern er macht sich in seiner eigenen Natur, in seiner eigenen Wesenheit geltend; er hat seinen eigenen Rhythmus."
      ],
      [
        "Und diesem Rhythmus muß vom Menschen entgegenge­arbeitet werden, so daß nicht nur gleichgültige Baumaterialien zu verarbeiten sind in der inneren Organisation des Menschen, sondern es muß zuerst die eigene Natur dieser Baumaterialien überwunden werden."
      ],
      [
        "So können wir sagen, daß wir in den Organen, denen unsere Nahrungsstoffe im Inneren des Menschen zuerst entgegentreten, die Werkzeuge haben, um demjenigen entgegenzuarbeiten, was Eigen­leben der Nahrungsstoffe ist - jetzt «Leben» im weitesten Sinne auf­gefaßt.",
        "Nicht nur das, was wir durch unregelmäßigen Rhythmus in der Ernährung selber bewirken, sondern auch das, was die Nahrungsstoffe"
      ],
      [
        "an eigenem Rhythmus in sich haben, welcher dem menschli­chen Rhythmus widerspricht, das muß umrhythmisiert werden.",
        "Von den Organen, die dies bewirken, ist die Milz das äußerste Organ.",
        "Aber an diesem Umrhythmisieren, an diesem Umgestalten und Abwehren arbeiten die anderen genannten Organe wesentlich mit, so daß wir in Milz, Leber und Galle ein zusammenwirkendes Organ-system haben, welches im wesentlichen dazu bestimmt ist, bei der Aufnahme der Nahrungsmittel in den Organismus dasjenige zurück­zuschieben, was Eigennatur dieser Nahrungsmittel ist."
      ],
      [
        "Alle Tätigkeit, welche im Magen entfaltet wird, oder auch schon, bevor die Speise in den Magen gelangt, ferner das, was dann bewirkt wird durch die Absonderung der Galle, was dann weiter durch die Tätigkeit von Leber und Milz geschieht, das alles gibt eben diese Abwehr der Eigennatur der äußeren Nahrungsstoffe.",
        "Daher sind also unsere Nahrungsmittel erst dann dem inneren Rhythmus des menschlichen Organismus angepaßt, wenn ihnen die Wirksamkeiten dieser Organe entgegengetreten sind."
      ],
      [
        "Und erst dann, wenn wir die in uns aufge­nommenen Nahrungsmittel den Wirksamkeiten dieser Organe aus­gesetzt und sie umgewandelt haben, haben wir dasjenige in uns, was fähig ist, in jenes Organsystem aufgenommen zu werden, das der Träger, das Werkzeug unseres Ich ist, in das Blut.",
        "Bevor irgendein äußerer Nahrungsstoff in unser Blut aufgenommen werden kann, so daß dieses unser Blut die Fähigkeit erhält, Werkzeug zu sein für unser Ich, müssen all die Eigengesetzlichkeiten der Außenwelt abge­streift sein, und das Blut muß die Nahrungsstoffe in einer solchen Gestalt empfangen, die der eigenen Natur des menschlichen Organis­mus entspricht."
      ],
      [
        "Daher können wir sagen: In Milz, Leber und Galle und in ihrem Zurückwirken auf den Magen haben wir diejenigen Organe, welche die Gesetze der äußeren Welt, aus der wir unsere Nahrung entnehmen, anpassen der inneren Organisation, dem inne­ren Rhythmus des Menschen."
      ],
      [
        "Nun steht aber diese menschliche Natur, wie sie als Ganzes wirkt, mit allen ihren Gliedern nicht bloß der inneren Welt gegenüber, sondern diese innere menschliche Natur muß in einer fortwährenden Korrespondenz, in einem fortwährenden lebendigen Wechselwirken"
      ],
      [
        "mit der Außenwelt sein.",
        "Dieses lebendige Wechselwirken mit der Außenwelt wird ja gerade dadurch abgeschnitten, daß den Gesetzen der Außenwelt, insofern wir mit ihr in Beziehung treten durch die Nahrungsstoffe, entgegengestellt werden die drei Organsysteme Leber, Galle, Milz."
      ],
      [
        "Durch diese wird die äußere Gesetzmäßigkeit weggenommen von innen her.",
        "Und es würde der menschliche Orga­nismus, wenn er nur diesen Organsystemen ausgesetzt wäre, sich von der Außenwelt vollständig abschließen, er würde ein vollkommen in sich isoliertes Wesen sein."
      ],
      [
        "Daher ist ein anderes ebenso notwendig.",
        "Wie der Mensch auf der einen Seite solche Organsysteme braucht, durch welche die Außenwelt so umgestaltet wird, daß sie seiner Innenwelt gemäß wird, so muß er auf der anderen Seite auch in der Lage sein, unmittelbar mit dem Werkzeug seines Ich der Außenwelt entgegenzutreten, unmittelbar also seinen Organismus, der sonst eine in sich isolierte Wesenheit wäre, mit der Außenwelt in Beziehung zu setzen."
      ],
      [
        "Während das Blut auf der einen Seite mit der Außenwelt nur so in Beziehung tritt, daß es von dieser Außenwelt nur das erhält, dem alle Eigengesetzmäßigkeit abgestreift ist, tritt es auf der anderen Seite mit der Außenwelt so in Beziehung, daß es unmittelbar an sie herantreten kann.",
        "Das geschieht, wenn das Blut durch die Lungen fließt und mit der äußeren Luft in Berührung kommt."
      ],
      [
        "Da wird es durch den Sauerstoff der äußeren Luft aufgefrischt und in einer solchen Weise gestaltet, daß jetzt dieser Gestaltung nichts abschwä­chend gegenübertritt, so daß in der Tat der Sauerstoff der Luft so herantritt an das Werkzeug des menschlichen Ich, wie es dessen eigenster Natur und Wesenheit entspricht.",
        "So sehen wir jene ganz merkwürdige Tatsache vor unser Auge treten, daß das edelste Werk­zeug, das der Mensch hat, das Blut, das Werkzeug seines Ich, wie ein Wesen dasteht, welches alle Nahrung sorgfältig filtriert erhält durch die früher charakterisierten Organsysteme."
      ],
      [
        "Dadurch ist das Blut in die Fähigkeit versetzt, ganz und gar ein Ausdruck der inneren Orga­nisation des Menschen zu werden, des inneren Rhythmus des Men­schen.",
        "Dadurch aber, daß das Blut unmittelbar in Berührung tritt mit denjenigen Stoffen der Außenwelt, die in seine innere Gesetzmäßig­keit und Regsamkeit aufgenommen werden dürfen, ohne daß sie"
      ],
      [
        "unmittelbar bekämpft zu werden brauchen, dadurch ist diese menschliche Organisation nichts in sich Abgeschlossenes, sondern mit der Außenwelt voll in Berührung."
      ],
      [
        "So haben wir im menschlichen Blutorganismus auch von diesem Gesichtspunkte aus etwas ganz Wunderbares vor uns.",
        "Wir haben in ihm ein wirkliches, echtes Ausdrucksmittel des menschlichen Ich, das ja in der Tat auf der einen Seite der Außenwelt zugekehrt ist, auf der anderen Seite dem eigenen Innenleben zugekehrt ist."
      ],
      [
        "So wie wir gesehen haben, daß der Mensch durch sein Nervensystem den Impressionen der Außenwelt zugewendet ist, also die Außenwelt sozusagen auf dem Umwege durch die Nerven in sich aufnimmt, so kommt er in eine unmittelbare Berührung mit der Außenwelt durch sein Blut, indem das Blut den Sauerstoff der Luft durch die Lungen aufnimmt.",
        "Daher können wir also sagen: In dem, was uns gegeben ist auf der einen Seite in dem Milz-Leber-Gallesystem und auf der anderen Seite in dem Lungensystem, haben wir zwei einander entge­genwirkende Systeme, die sich gleichsam berühren in dem Blut."
      ],
      [
        "Außenwelt und Innenwelt berühren sich durch das Blut ganz unmit­telbar im menschlichen Organismus, indem das Blut von der einen Seite her mit der äußeren Luft in Berührung kommt und von der anderen Seite her mit den Nahrungsmitteln, denen ihre eigene Natur genommen ist.",
        "Es stoßen also, möchte man sagen, wie positive und negative Elektrizität, hier zwei Weltenwirkungen im Menschen zusammen."
      ],
      [
        "Und wir können uns sehr leicht vorstellen, wo das Organsystem liegt, welches bestimmt und geeignet ist, das Aufeinan­derprallen dieser beiden Weltenkraftsysteme auf sich wirken zu las­sen.",
        "Bis zum Herzen herauf, insofern das Blut durch das Herz strömt, wirken die umgewandelten Nahrungssäfte."
      ],
      [
        "Bis zum Herzen herein, insofern es vom Blute durchflossen wird, wirkt der Sauerstoff der Luft, der unmittelbar aus der Außenwelt in unser Blut tritt, so daß wir im Herzen dasjenige Organ haben, in dem sich diese zwei Systeme begegnen, in die der Mensch hineinverwoben ist, an denen er nach zwei Seiten hängt.",
        "Es ist mit diesem menschlichen Herzen so, daß wir sagen könnten: An ihm hängt auf der einen Seite der ganze menschliche innere Organismus, und auf der anderen Seite ist der"
      ],
      [
        "Mensch durch das Herz unmittelbar angeknüpft an den Rhythmus, an die Regsamkeit der äußeren Welt."
      ],
      [
        "Wenn nun zwei solche Systeme zusammenstoßen, so könnte es ja sein, daß ihr Zusammenwirken eine unmittelbare Harmonie ergäbe.",
        "Wir könnten uns vorstellen, daß diese zwei Systeme - das System der großen Welt, das durch den aufgenommenen Sauerstoff oder die Luft überhaupt in uns hineinwirkt, und das System der kleinen Welt, unseres eigenen inneren Organismus, das uns die Nahrungsmittel umwandelt -, daß sich diese Systeme im Blute, indem es das Herz durchströmt, einen harmonischen Ausgleich schaffen.",
        "Wenn es so wäre, dann wäre der Mensch eingespannt in zwei Welten, die sozusa­gen sein inneres Gleichgewicht schüfen.",
        "Nun werden wir im Laufe dieser Vorträge noch sehen, daß es sich mit der Beziehung der Welt zur menschlichen Wesenheit nicht so verhält.",
        "Es ist vielmehr so, daß die Welt sich sozusagen ganz passiv verhält, daß sie nur ihre Kräfte aussendet und es dem Menschen überläßt, durch eigene innere Tätig­keit den Ausgleich zu schaffen zwischen den zweierlei Systemen, in deren Wirkungen wir eingespannt sind.",
        "Wir werden es immer mehr und mehr als das Wesentliche erkennen lernen, daß dem Menschen zuletzt immer ein Rest bleibt für seine innere Tätigkeit, daß es ihm -bis in seine Organe hinein - überlassen ist, den Ausgleich, das innere Gleichgewicht selber zu schaffen.",
        "So müssen wir auch im menschli­chen Organismus selber den Ausgleich, die Harmonisierung dieser beiden Weltsysteme suchen.",
        "Wir müssen uns von vornherein sagen:"
      ],
      [
        "Durch die Gesetzmäßigkeiten der Außenwelt, die direkt in den Men­schen hineintreten, und durch die eigenen inneren Gesetzmäßigkei­ten des Menschen, in die er die Gesetzmäßigkeiten der Außenwelt umwandelt, welche er aufnimmt durch die Nahrung, ist noch nicht ohne weiteres die Harmonisierung der beiden Systeme gegeben.",
        "Die Harmonisierung muß sich erst durch ein besonderes eigenes Organ-system vollziehen.",
        "Der Mensch muß in sich selber die Harmonisie­rung herbeiführen.",
        "Das geschieht nicht in bewußten Vorgängen, sondern durch Vorgänge, die sich ganz unbewußt innerhalb des menschlichen Organismus abspielen.",
        "Dieser Ausgleich zwischen die­sen beiden Systemen wird dadurch herbeigeführt, daß zwischen dem"
      ],
      [
        "Milz-Leber-Gallesystem auf der einen Seite und dem Lungensystem auf der anderen Seite, die sich in dem das Herz durchströmenden Blute gegenüberstehen, eingeschaltet ist dasjenige, was wir das Nie­rensystem nennen, das auch in inniger Verbindung steht mit dem Blutkreislauf."
      ],
      [
        "Im Nierensystem haben wir dasjenige, was sozusagen harmonisiert jene äußeren Wirkungen, die von dem unmittelbaren Berühren des Blutes mit der Luft herrühren, mit den Wirkungen, die von denjeni­gen inneren Organen des Menschen ausgehen, durch die die Nah­rungsstoffe erst zubereitet werden müssen, damit ihre Eigennatur abgestreift wird.",
        "In dem Nierensystem haben wir also ein solches ausgleichendes System, durch das der Organismus in die Lage kommt, den Überschuß abzugeben, der sich ergeben würde durch ein unharmonisches Zusammenwirken der beiden anderen Systeme."
      ],
      [
        "Damit haben wir der ganzen inneren Organisation - den Organen des Verdauungsapparates einschließlich derjenigen Organe, die wir dazurechnen müssen, wie Leber, Galle und Milz - dasjenige gegen­übergestellt, wofür diese Organe zunächst ihre vorbereitende Tätig­keit entwickelt haben, das Blutsystem.",
        "Und wir haben auf der ande­ren Seite diesem Blutsystem diejenigen Organe gegenübergestellt, durch welche der einseitigen Isolierung entgegengearbeitet und damit der Ausgleich geschaffen wird zwischen dem genannten inneren System und dem, was von außen her kommt.",
        "Wenn wir also - und wir werden noch sehen, wie sehr das berechtigt ist - das Blutsystem mit seinem Mittelpunkt, dem Herzen, uns in die Mitte des Organis­mus hineingestellt denken, so haben wir, sich angliedernd an dieses Blut-Herzsystem, auf der einen Seite das Leber-Galle-Milzsystem, auf der anderen Seite - und auf andere Weise mit dem Herzen in Verbindung stehend - das Lungensystem.",
        "Dazwischen ist das Nie­rensystem angeordnet.",
        "Wir werden später noch sehen, wie ungemein interessant der Zusammenhang ist zwischen dem Lungensystem und dem Nierensystem.",
        "Jetzt wollen wir darauf zunächst nicht näher eingehen, sondern das Ganze im Zusammenhang betrachten.",
        "Wenn wir die Systeme einfach ganz schematisch nebeneinander zeichnen (Zeichnung Seite 78 links), dann erkennen wir schon aus dieser"
      ],
      [
        "schematischen Darstellung, wie die menschliche innere Organisation in einem gewissen Zusammenhange steht, und wir haben diesen Zusammenhang so dargestellt, daß wir in dem Herzen mit dem dazugehörigen Blutsystem das Allerwichtigste zu sehen haben."
      ],
      [
        "# Bild s.078"
      ],
      [
        "Nun habe ich schon darauf hingewiesen - und wir werden noch im genaueren sehen, inwiefern eine solche Namengebung gerechtfertigt ist -, daß im Okkultismus die Milzwirkung als eine saturnische Wirkung bezeichnet wird, die Leberwirkung als eine Jupiter- und die der Galle als eine Marswirkung.",
        "Aus demselben Grunde sieht nun die okkulte Erkenntnis in dem Herzen und dem dazugehörigen Blutsy­stem dasjenige, was den Namen «Sonne» im menschlichen Organis­mus ebenso verdient wie die Sonne draußen innerhalb des Planeten-systems.",
        "Das Lungensystem bezeichnet der Okkultist nach demsel­ben Prinzip als «Merkur» und das Nierensystem mit dem Namen «Venus».",
        "So haben wir schon in der Benennung dieser Systeme des menschlichen Organismus - wenn wir jetzt auch gar nicht eingehen auf eine Rechtfertigung dieser Namen - etwas angedeutet wie ein inneres Weltsystem, was wir noch dadurch ergänzt haben, daß wir uns in die Lage versetzten, auch den Zusammenhang der beiden Organsysteme zu betrachten, die zum Blutsystem in Beziehung ste­hen.",
        "Erst wenn wir die Zusammenhänge in diesem Sinne betrachten,"
      ],
      [
        "tritt uns das in einer Vollständigkeit entgegen, was wir die eigentliche menschliche innere Welt nennen können.",
        "Ich werde Ihnen nun in den folgenden Vorträgen auch noch zu zeigen haben, daß tatsächlich der Okkultist Gründe hat, das Verhältnis der Sonne zu Merkur und Venus in einer ähnlichen Weise sich vorzustellen, wie im menschli­chen Organismus das Verhältnis zwischen Herz, Lungen und Nieren gedacht werden muß."
      ],
      [
        "Wir sehen daraus, daß in dem Werkzeug unseres Ich, in unserem Blutsystem, das seinen Rhythmus im Herzen zum Ausdruck bringt, etwas gegeben ist, was gewissermaßen in seiner ganzen Gestaltung, in seiner inneren Natur und Wesenheit durch das innere Weltsystem des Menschen bestimmt wird, und daß es in ein solches [makrokos­misches] Gesamtsystem eingebettet sein muß, damit es so leben kann, wie es eben lebt.",
        "In diesem menschlichen Blutsystem - das habe ich schon öfter erwähnt - haben wir zu sehen das physische Werkzeug unseres Ich."
      ],
      [
        "Wir wissen ja, daß unser Ich, so wie wir es haben, nur dadurch möglich ist, daß dieses Ich aufgebaut ist auf Grundlage eines physischen Leibes, eines Ätherleibes und eines Astralleibes.",
        "Ein frei in der Welt herumfliegendes menschliches Ich ist innerhalb der Welt, die unsere Welt ist, nicht denkbar."
      ],
      [
        "Ein menschliches Ich setzt voraus als Grundlage einen Astralleib, einen Ätherleib und einen physischen Leib.",
        "Wie nun dieses Ich in geistiger Beziehung die drei genannten Wesensglieder des Menschen voraussetzt, so setzt sein physisches Organ, das Blutsystem, auch physisch solche Abbilder des astrali­schen und des ätherischen Leibes voraus."
      ],
      [
        "Das Blutsystem kann sich also nur auf der Grundlage von etwas anderem entwickeln.",
        "Während die Pflanze sich einfach entwickelt auf der Grundlage der sie umge­benden unorganischen Natur, indem sie gleichsam aus derselben herauswächst, müssen wir sagen, daß für den menschlichen Blutorga­nismus als Grundlage nicht ohne weiteres bloß die äußere Natur als Unterlage nötig ist, sondern es muß diese äußere Natur erst noch eine Umgestaltung erfahren."
      ],
      [
        "Wie der physische Leib des Menschen erst einen Ätherleib und einen Astralleib haben muß, so muß das, was an Nahrungsstoffen einströmt, erst umgestaltet werden. damit es dem menschlichen Ich als Werkzeug dienen kann."
      ],
      [
        "Wenn wir nun auch sagen können, daß dieses physische Werkzeug des menschlichen Ich, das Blut, durch die Lunge von außen bestimmt wird, so ist die Lunge selber doch ein Organ der physischen Leibes-Organisation, das heißt, es ist nicht dieses Organ, sondern die durch dasselbe eingeatmete Luft, welche es möglich macht, mit einem äuße­ren Rhythmus auf das Blut einzuwirken.",
        "Wir müssen unterscheiden zwischen dem, was von außen an den Menschen herankommt in Form der Luft, die eingeatmet wird und die es dem Menschen mög­lich macht, mit einem äußeren Rhythmus unmittelbar sein Blutsy­stem zu durchdringen, und dem, was nicht unmittelbar an das leben­dige Werkzeug des Ich im Organismus, an das Blut, herantritt, sondern was herantritt - in der Art, wie es schon charakterisiert worden ist - auf dem Umwege durch die Seele, was der Mensch also dadurch aufnimmt, daß er die Eindrücke der Außenwelt durch die Sinne empfängt und diese Sinne dann ihre Eindrücke auch vermitteln bis zur Bluttafel hin."
      ],
      [
        "Deshalb werden wir sagen können: Der Mensch tritt nicht bloß mit der Außenwelt unmittelbar stofflich in Berührung durch die Atmungsluft, indem diese Berührung hereinwirkt bis auf sein Blut, sondern er tritt durch die Sinnesorgane mit der Außenwelt auch so in Berührung, daß diese Berührung eine nichtstoffliche ist, wie sie in dem Prozeß der Wahrnehmung stattfindet, den die Seele entfaltet, wenn sie zur Umwelt in Beziehung tritt.",
        "Da haben wir etwas, was sich als ein höherer Prozeß hinzufügt zum Atmungspro­zeß, wir haben etwas wie einen vergeistigten Atmungsprozeß."
      ],
      [
        "Wäh­rend wir durch den Atmungsprozeß die Außenwelt stofflich aufneh­men, nehmen wir im Wahrnehmungsprozeß - und ich meine jetzt mit «Wahrnehmung» alles, was der Mensch an äußeren Impressionen verarbeitet - etwas durch einen vergeistigten Atmungsprozeß in unseren Organismus auf.",
        "Und es entsteht jetzt die Frage: Wie wirken diese beiden Prozesse zusammen?"
      ],
      [
        "Denn im menschlichen Organis­mus muß alles aufeinander einwirken."
      ],
      [
        "Legen wir uns einmal diese Frage genauer vor - denn es wird Wesentliches davon abhängen, daß wir sie uns genau vorlegen -, um uns die heute zunächst hypothetisch zu gebende Antwort vor unsere Seele führen zu können.",
        "Wir müssen uns darüber klar werden, wie"
      ],
      [
        "ein Zusammenwirken, ein Wechselwirken stattfinden kann zwischen alle dem, was durch das Blut wirkt und was es geworden ist dadurch, daß alle diese inneren Organprozesse stattgefunden haben, und dem, was das Blut wird, indem wir äußere Wahrnehmungsprozesse voll­ziehen.",
        "Wir müssen sehen, daß da eine Wechselwirkung stattfinden kann."
      ],
      [
        "Das Blut ist, trotzdem es so eingehend und so vielseitig filtriert ist, trotzdem so vieles dafür gesorgt hat, daß es ein so wunderbar organisierter Stoff ist, der Werkzeug unseres Ich sein kann, das Blut ist trotzdem eine physische Substanz und gehört als solche zum physischen Leibe.",
        "Daher können wir sagen: Zunächst erscheint uns ein weiter, weiter Abstand zwischen dem, was im menschlichen Blute an physischen Prozessen wirkt, und dem, was wir als unsere Wahr-nehmungsprozesse kennen, die die Seele vollzieht."
      ],
      [
        "Das ist eine nicht abzuleugnende Realität; denn der Mensch müßte ja auf sonderbare Weise nicht zu denken verstehen, der ableugnen wollte, daß Wahr­nehmungen, Begriffe, Ideen, Gefühle, Willensimpulse ebenso etwas Reales sind wie Blutsubstanz, Nervensubstanz, Lebersubstanz, Gal­lensubstanz und so weiter.",
        "Wie diese Dinge zusammenhängen, dar­über können sich die Weltanschauungen streiten; sie können sich darüber streiten, ob die Gedanken bloß irgendwelche Wirkungen, sagen wir, der Nervensubstanz oder dergleichen seien."
      ],
      [
        "Da kann vielleicht ein Streiten der Weltanschauungen beginnen.",
        "Aber keinen Streit kann es darüber geben, weil es eine selbstverständliche Sache ist, daß unser Seeleninnenleben, unser Gedankenleben, unser Gefühlsleben, alles was sich aufbaut auf Grund der äußeren Wahr­nehmungen und Eindrücke, eine Realität für sich darstellt."
      ],
      [
        "Wohlge­merkt, ich sage nicht: eine abgesonderte Realität -, sondern: eine Realität für sich, denn nichts ist in der Welt abgesondert.",
        "Mit «Reali­tät für sich» soll nur angedeutet werden, was real beobachtet werden kann, und dazu gehören Gedanken, Gefühle und so weiter ebenso wie Magen, Leber, Galle und Milz."
      ],
      [
        "Aber ein anderes kann uns auffallen, wenn wir diese zwei Realitä­ten nebeneinanderstellen: Auf der einen Seite alles, was ein selbst noch so stark filtriertes Materielles, Physisches ist wie das Blut, und auf der anderen Seite das, was ja mit einem Physischen gar nichts zu"
      ],
      [
        "tun zu haben scheint zunächst, nämlich die Inhalte der Seele, die Gefühle, Gedanken und so weiter.",
        "In der Tat bietet der Anblick dieser zweierlei Arten von Realitäten für den Menschen solche Schwierigkeiten, daß sich an diesen Anblick angegliedert haben die allermannigfaltigsten Antworten aus den verschiedensten Weltan­schauungen heraus."
      ],
      [
        "Da gibt es Weltanschauungen, welche eine unmittelbare Einwirkung des Seelischen, des Gedanklichen, des Gefühlsmäßigen auf die physische Substanz annehmen, wie wenn der Gedanke unmittelbar auf die physische Substanz wirken könnte.",
        "Denen stehen andere gegenüber, die materialistischen, die annehmen, daß Gedanken, Gefühle und so weiter einfach produziert werden aus den Vorgängen des Physisch-Substantiellen heraus."
      ],
      [
        "Der Streit dieser beiden Weltanschauungen hat ja in der äußeren Welt - nicht für den Okkultisten, für den dieser Streit ein Streit mit leeren Worten ist -durch lange Zeiten hindurch eine große Rolle gespielt.",
        "Und als man endlich gar nicht mehr zurechtgekommen ist, da ist in der neueren Zeit noch etwas anderes aufgetreten, was den sonderbaren Namen «psychophysischer Parallelismus» führt."
      ],
      [
        "Weil man sich gar nicht mehr zu helfen wußte, welcher nun von den beiden Gedanken der richtige ist - entweder wirkt der Geist auf die leiblichen Prozesse, oder es wirken die leiblichen Prozesse auf den Geist -, so sagte man eben einfach, das seien zwei Vorgänge, die parallel ablaufen.",
        "Man sagte sich: Während der Mensch denkt, fühlt und so weiter, laufen parallel in seinen physischen Organsystemen ganz bestimmte Vorgänge ab. - Die Wahrnehmung «Ich sehe Rot» würde also entspre­chen irgendeinem materiellen Vorgang innerhalb des Nervensystems."
      ],
      [
        "Was wir empfinden bei einem roten Eindruck, was wir fühlen an Freude oder Schmerz bei ihm, entspricht einem materiellen Vorgang.",
        "Aber weiter geht man nicht, als zu sagen, daß er eben «entspricht».",
        "Diese Theorie hebt in der Tat die ganzen Schwierigkeiten auf, indem sie diese einfach wegexpliziert."
      ],
      [
        "Nun, alle Streitereien, die sich auf diesem Boden entsponnen haben und auch die Hilflosigkeit des psychophy­sischen Parallelismus ergeben sich daraus, daß man diese Fragen entscheiden will auf einem Boden, auf dem sie gar nicht ausgetragen werden können.",
        "Wir haben es mit nichtmateriellen Vorgängen zu"
      ],
      [
        "tun, wenn wir die Tätigkeiten unseres inneren Seelenlebens ins Auge fassen, und wir haben es mit materiellen Vorgängen zu tun, wenn wir, selbst über etwas so fein organisiertes wie es das Blut ist, unsere Betrachtungen anstellen.",
        "Wenn man diese zwei Dinge einfach gegen­überstellt - physische Betätigung und seelische Betätigung - und jetzt durch Nachdenken herausbekommen will, wie diese beiden aufein­ander wirken, so ergibt dieses Nachdenken eben gar nichts.",
        "Durch Nachdenken kann man alle willkürlichen Lösungen oder Nichtlö­sungen finden.",
        "Erst dadurch wird über diese Fragen etwas entschie­den werden können, daß wir uns wirklich eine höhere Erkenntnis aneignen, die weder stehenbleibt bei dem physischen Anschauen der Außenwelt noch bei dem an die bloße physische Außenwelt gebun­denen Denken.",
        "Wir müssen eine Form der Erkenntnis finden, die sich erhebt zu dem, was über das Physische hinaus in die überphysi­sche Welt führt.",
        "Wir müssen auf der einen Seite von dem Materiellen hinaufsteigen zu dem Übermateriellen, zu dem Überphysischen, wir müssen aber auf der anderen Seite auch von dem Seelenleben, das sich in der physischen Welt abspielt, hinaufsteigen zu dem, was unserem Seelenleben zugrundeliegt in der überphysischen Welt, denn mit unserem Seelenleben, mit allen unseren Gefühlen und so weiter leben wir ja auch in der physischen Welt.",
        "Wir müssen also von zwei Seiten her aufsteigen zu einer überphysischen Welt."
      ],
      [
        "Um von der materiellen Seite her in die überphysische Welt aufzu­steigen, dazu sind jene Seelenübungen notwendig, welche es dem Menschen möglich machen, hinter das äußere Sinnliche zu schauen, hinter den Schleier, von dem ich gesprochen habe, in welchen unsere Sinneseindrücke hineinverwoben sind.",
        "Solche Sinneseindrücke haben wir ja auch dann vor uns, wenn wir den äußeren menschlichen Organismus betrachten, auch bei dem am feinsten Organisierten des menschlichen Organismus, dem Blute, haben wir es mit einem Phy­sisch-Sinnlichen zu tun.",
        "Es sind Seelenübungen notwendig, um den Menschen in die übersinnliche Welt hineinzuführen.",
        "Zunächst muß er eine Stufe tiefersteigen als dort, wo er war, als er die Seelenein­drücke in sich aufnehmen konnte, unter den Plan des Physischen.",
        "In den Untergründen der physisch-sinnlichen Welt, da tritt ihm als das"
      ],
      [
        "Übersinnliche der menschlichen Organisation der Ätherleib entge­gen.",
        "Dieser Ätherleib - wir werden ihn noch genauer besprechen gerade vom okkult-physiologischen Standpunkte aus - ist eine über­sinnliche Organisation, die wir uns zunächst einfach denken als die übersinnliche Grundsubstanz, aus der sich der sinnliche Organismus des Menschen herausgliedert und von dem er ein Abbild, ein Abdruck ist.",
        "Von diesem Ätherleibe ist selbstverständlich auch das Blut ein Abdruck.",
        "Wir haben also jetzt hier, indem wir um eine Stufe hinter den physisch-sinnlichen Organismus getreten sind, ein über-sinnliches Glied in dem menschlichen Ätherleibe gefunden.",
        "Und es fragt sich nun: Können wir an dieses Übersinnliche, an diesen Äther-leib, nun auch herankommen von der anderen Seite her, von der Seite des Seelischen her, von unseren Empfindungen, Gedanken, Gefühlen her, die wir uns aufbauen aus Eindrücken der Außenwelt?"
      ],
      [
        "Da stellt sich nun allerdings heraus: So unmittelbar, wie wir unser Seelenleben haben, kommen wir nicht gleich an den Ätherorganis­mus heran.",
        "Aber - und damit lassen Sie mich die heutige Betrachtung ausklingen - wenn wir in unserer Seele arbeiten, so geschieht das ja so, daß wir zunächst die äußeren Eindrücke bekommen, auf die Sinne wirkt die äußere Welt, dann verarbeiten wir in unserer Seele die äußeren Eindrücke; aber wir tun noch mehr, wir speichern gleichsam diese empfangenen Eindrücke in uns selber auf.",
        "Denken Sie nur einmal nach über die einfache Erscheinung des Gedächtnisses, der Erinnerung.",
        "Wenn Sie sich an etwas erinnern, woran Sie vor Jahren auf Grundlage äußerer Wahrnehmungen Eindrücke gewonnen haben, sich Vorstellungen gebildet haben, die Sie heute aus den Untergründen Ihrer Seele heraufholen, und es kommt Ihnen die Erinnerung, sagen wir an etwas ganz einfaches, einen Baum oder einen Geruch, da müssen Sie sagen, Sie haben in Ihrer Seele etwas aufgespeichert, was Ihnen hat bleiben können von dem äußeren Eindruck.",
        "Nun zeigt uns aber eine wiederum nur durch Übungen der Seele zu gewinnende Betrachtung des Seelenlebens selber, daß in dem Augenblick, wo wir unser Seelenleben soweit haben, daß wir aufge­speicherte Eindrücke als Erinnerungsvorstellungen zurückrufen kön­nen, wir mit unseren seelischen Erlebnissen nicht nur in unserem Ich"
      ],
      [
        "wirken.",
        "Zunächst tun wir das ja, indem wir mit unserem Ich der Außenwelt gegenübertreten, Eindrücke aus ihr aufnehmen und sie verarbeiten im Astralleibe.",
        "Würden wir aber nur das tun, so würden wir alles gleich wieder vergessen.",
        "Wenn wir Schlüsse ziehen, arbeiten wir im Astralleib.",
        "Wenn wir aber die Eindrücke in uns so fest machen, daß wir sie nach einiger Zeit - ja, oder auch nur nach Minuten - wieder heraufholen können, dann prägen wir die Ein­drücke, die wir durch unser Ich gewonnen und durch unseren Astral­leib verarbeitet haben, in unseren Ätherleib ein; so daß wir also in den Gedächtnisvorstellungen vom Ich aus hineingepreßt haben in den Atherleib dasjenige, was wir als seelische Betätigung in der Berührung mit der Außenwelt gewonnen haben.",
        "Wenn wir nun die Fähigkeit haben, von unserer Seele her in den Ätherleib hineinzu­pressen unsere Erinnerungsvorstellungen, und wenn wir den Äther-leib auf der anderen Seite anerkennen als den nächsten übersinnlichen Ausdruck unseres Organismus, so fragt es sich nun: Wie geschieht dieses Hineinpressen?",
        "Wie geht das vor sich, daß der Mensch tatsäch­lich das, was vom Astralleibe verarbeitet ist, jetzt wirklich in den Ätherleib hineinbringt?",
        "Wie kann er es in den Ätherleib überleiten?"
      ],
      [
        "Diese Überleitung geschieht auf eine sehr merkwürdige Weise.",
        "Wenn wir zunächst ganz schematisch den Verlauf des Blutes durch den ganzen menschlichen Körper betrachten und dieses Blut als den äußeren physischen Ausdruck des menschlichen Ich fassen, so sehen wir - wenn wir das jetzt so betrachten, als ob wir im Ätherleibe drinnen stünden -, wie das Ich arbeitet in Korrespondenz mit der Außenwelt, wie es Impressionen empfängt und diese zu Vorstellun­gen verdichtet, und wir sehen, wie dabei in der Tat unser Blut nicht nur tätig ist, sondern wie unser Blut im ganzen Verlauf, namentlich nach oben zu - nach unten weniger-, überall den Ätherleib erregt, so daß wir überall im Ätherleibe Strömungen sich entwickeln sehen, die einen ganz bestimmten Verlauf nehmen.",
        "Sie erscheinen so, als ob sie sich an das Blut anschließen würden, vom Herzen nach dem Kopfe gehen und sich im Kopfe sammeln würden.",
        "Sie sammeln sich unge­fähr so - wenn ich jetzt einen äußeren Vergleich gebrauchen darf -, wie etwa Ströme von Elektrizität einer Spitze zugehen, der eine"
      ],
      [
        "andere Spitze entgegengestellt ist, und so zum Ausgleich von positi­ver und negativer Elektrizität hinstreben."
      ],
      [
        "Wenn wir diesen Vorgang okkult betrachten mit entsprechend geübter Seele, so sehen wir, wie in einem Punkte sich jene Äther-kräfte unter einer gewaltigen Spannung zusammendrängen, welche hervorgerufen sind durch die Eindrücke, die jetzt gewisse Vorstel­lungen werden wollen, Gedächtnisvorstellungen, die sich in den Ätherleib einprägen wollen.",
        "Man sieht es den Ätherkräften an, daß sie Gedächtniskräfte werden wollen.",
        "Ich will die letzten Ausläufer dieser Ätherströmungen nach dem Gehirn herauf und das Sich­zusammendrängen so zeichnen, wie es sich etwa wirklich darstellen"
      ],
      [
        "# Bild s.086"
      ],
      [
        "würde.",
        "Wir sehen da eine mächtige Spannung, die sich an einer Stelle sammelt und gleichsam sagt: Ich will in den Ätherleib hinein! - Wir sehen nun, wie dieser Ätherströmung des Kopfes andere Strömungen entgegenkommen, die ausgehen namentlich von den Lymphgefäßen und die sich so sammeln, daß sie sich der ersten Strömung entgegen­stellen.",
        "So haben wir im Gehirn, wenn sich eine Gedächtnisvorstel­lung bilden will, einander gegenüberstehen zwei Ätherströmungen, die sich mit größtmöglicher Kraft konzentrieren, etwa so wie positive und negative Elektrizität sich an ihren Polen mit größter Spannung konzentrieren und nach Ausgleich streben.",
        "Ein Ausgleich zwischen den beiden Ätherströmungen geschieht in der Tat, und wenn er vollzogen ist, dann ist eine Vorstellung Gedächtnisvorstellung geworden und hat sich dem Ätherleibe einverleibt."
      ],
      [
        "# Bild s.087a"
      ],
      [
        "Solche übersinnlichen Realitäten, solche übersinnlichen Strömun­gen im menschlichen Organismus drücken sich dadurch aus, daß sie sich auch ein physisch-sinnliches Organ schaffen, welches wir wie eine Versinnlichung solcher Strömungen anzusehen haben.",
        "So haben wir ein Organ, welches sich im mittleren Gehirn befindet, das der physisch-sinnliche Ausdruck ist für das, was als Gedächtnisvorstel­lung sich bilden will.",
        "Dem stellt sich gegenüber ein anderes Organ im Gehirn, das der Ausdruck ist für diejenigen Strömungen im Äther­leib, die von den unteren Organen kommen.",
        "Diese beiden Organe im menschlichen Gehirn sind der physisch-sinnliche Ausdruck für diese beiden Strömungen im menschlichen Ätherleibe, sie sind etwas wie letzte Anzeichen dafür, daß solche Strömungen im Ätherleibe statt­finden.",
        "Es verdichten sich gleichsam diese Strömungen so stark, daß sie die menschliche Leibessubstanz ergreifen und zu diesen Organen verdichten, so daß wir in der Tat den Eindruck haben, wie wenn von dem einen Organ helle Lichtströmungen ausstrahlen, die zu dem anderen Organ überfließen.",
        "Das physische Organ, das die Gedächt­nisvorstellung bilden will, ist die Zirbeldrüse, der aufnehmende Teil ist der Gehirnanhang, Hypophysis."
      ],
      [
        "# Bild s.087b"
      ],
      [
        "Hier haben Sie an einer ganz bestimmten Stelle des physischen Organismus den äußeren physischen Ausdruck für das Zusammen­wirken des Seelischen mit dem Leiblichen!"
      ],
      [
        "Es soll das zunächst nur wie eine prinzipielle Darstellung sein, womit wir unsere heutige Betrachtung ausklingen lassen wollen, die wir morgen weiter ausführen wollen und an die wir Genaueres und Beweisbares anknüpfen wollen.",
        "Es ist wichtig, daß wir den Gedan­ken genau festhalten, daß wir im Übersinnlichen forschen können, und uns dann fragen können, ob der zu erwartende physische Aus­druck für das Übersinnliche auch vorhanden ist.",
        "Wir sahen hier, daß das der Fall ist.",
        "Da es sich aber hier um die Eingangspforte vom Sinnlichen zum Übersinnlichen handelt, so werden Sie es begreifen, daß diese Organe für die physische Wissenschaft höchst zweifelhafte Organe sind, und daß Sie über diese Organe von der äußeren Wissen­schaft nur außerordentlich unzureichende und ungenügende Aus­kunft erhalten können."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "FÜNFTER VORTRAG Prag, 24. März 1911",
    "paragraphs": [
      "Es wird heute meine Aufgabe sein, bevor wir in unseren Betrachtun­gen weiterschreiten, einige Begriffe herbeizutragen, die wir in der weiteren Folge unserer Darstellungen notwendig brauchen werden. Da wird es insbesondere wichtig sein, daß wir uns verständigen über die Bedeutung dessen, was wir im geisteswissenschaftlichen, anthro­posophischen Sinne ein physisches Organ nennen oder vielmehr den physischen Ausdruck eines Organs. Denn Sie haben ja schon gese­hen, daß wir zum Beispiel über die Milz so reden können, daß die physische Milz sogar materiell entfernt werden kann oder unbrauch­bar werden kann, ohne daß dasjenige, was wir im anthroposophi­schen Sinne die «Milz» nennen, von seiner Tätigkeit ausgeschaltet wird. Es bleibt dennoch, wenn wir ein solches physisches Organ ausgeschaltet, entfernt haben, im Organismus die Tätigkeit, die innere Regsamkeit, die durch das Organ ausgeübt worden war, immer noch übrig. Daraus sehen wir - und ich bitte Sie recht sehr, sich einen solchen Begriff für das folgende anzueignen -, daß wir alles, was physisch anschaubar, was physisch wahrnehmbar ist bei einem solchen Organ, uns wegdenken können - natürlich kann man das nicht von jedem Organ sagen -, und es bleibt doch die bestim­mungsgemäße Funktion des Organs; und das, was dann bleibt, was die Funktion weiter fortführt, das müssen wir zu dem Übersinnli­chen des menschlichen Organismus rechnen.",
      "Nun sprechen wir aber überhaupt, wenn wir im Sinne unserer Geisteswissenschaft von solchen Organen sprechen wie Milz, Leber, Galle, Nieren, Lungen und so weiter, indem wir diese Namen aus­sprechen, zunächst gar nicht von dem, was man physisch sehen kann, sondern wir bezeichnen damit die in diesen Organen wirkenden Kraftsysteme, die übersinnlicher Natur sind. Daher werden wir, und das ist in besonderem Grade bei der Milz der Fall, wenn wir geistes-wissenschaftlich davon sprechen, zunächst ein äußerlich physisch nicht sichtbares Kraftsystem uns denken müssen. Denken wir also in",
      "dem, was ich hier zeichne, ein physisch nicht sichtbares Kraftsystem, das nur anschaubar werden könnte für ein übersinnliches Schauen.",
      "# Bild s.090",
      "Ein solches wäre also zum Beispiel in der Gegend unserer Milz nur als übersinnliches Kraftsystem sichtbar. Wenn wir nun ins Auge fassen, daß ja im wirklichen uns vorliegenden menschlichen Organis­mus dieses übersinnliche Kraftsystem ausgefüllt ist mit sinnlicher Materie, so müssen wir uns fragen: Wie haben wir uns nun das Verhältnis dieses übersinnlichen Kraftsystems zu dem, was sinnliche Materie ist, zu denken?",
      "Ich glaube, es wird Ihnen nicht schwierig werden, zu denken, daß Kräfte durch den Raum gehen können, welche zunächst nicht sinn­lich anschaubar sind. Man braucht sich nur an folgendes zu erinnern:",
      "Wer zum Beispiel niemals etwas von der Realität der Luft in einer von Wasser entleerten Flasche gehört hat, der wird der Meinung sein, die Flasche sei ganz leer. Ein solcher physikalisch Unkundiger wird",
      "einigermaßen erstaunt sein zu sehen, daß, wenn wir eine leere Was­serflasche auf den Tisch stellen, einen gut anschließenden enghalsigen Trichter aufsetzen und rasch Wasser in den Trichter eingießen, wir das Wasser im Trichter behalten und es nicht in die Flasche hinein-fließen kann, weil es durch den Gegendruck der Luft verhindert wird, in die Flasche einzudringen. Ein solcher Mensch wird dann gewahr, daß doch ein für ihn Unsichtbares in der Flasche darinnen ist, welches das Wasser zurückhält.",
      "Denken Sie sich diesen Begriff etwas erweitert, so wird es auch nicht schwierig sein, sich vorzustel­len, daß der Raum von Kraftsystemen durchdrungen sein kann, welche zunächst übersinnlicher Natur sind, so daß wir sie nicht mit dem Messer durchschneiden können und daß sie auch nicht ange­griffen werden können, wenn ein physisches Organ, das ihr materiel­ler Ausdruck ist, zum Beispiel die Milz, erkranken sollte. Wir haben uns zu denken, daß ein übersinnliches Kraftsystem zu dem, was wir als physisch-sinnliches Organ sehen, in einem solchen Verhältnis steht, daß physische Materie sich in dieses Kraftsystem einlagert, angezogen von den Kraftpunkten und Kraftlinien, und dadurch zu einem physischen Organ wird.",
      "Wir können sagen: Der Grund, warum zum Beispiel an der Stelle der Milz ein physisch-sinnliches Organ sichtbar ist, ist also der, daß dort in einer ganz bestimmten Weise Kraftsysteme den Raum ausfüllen, welche die Materie so heranziehen, daß sie sich in einer solchen Weise einlagert, wie wir es an dem äußeren Organ der Milz sehen, wenn wir es anatomisch betrachten.",
      "So können Sie sich die verschiedensten Organe im menschlichen Organismus denken. Sie sind zuerst übersinnlich veranlagt und dann ausgefüllt unter dem Einfluß der verschiedensten übersinnlichen Kraftsysteme von physischer Materie. Daher müssen wir in diesen Kraftsystemen zunächst einen übersinnlichen Organismus sehen, der in sich differenziert ist, der in den verschiedensten Weisen die physi­sche Materie sich eingliedert und dessen Kompliziertheit das physi­sche, ihm eingegliederte Organ nur unvollständig zu folgen vermag. Damit haben wir nicht nur den Begriff des Verhältnisses der über­sinnlichen Kraftsysteme zu den eingelagerten physisch-materiellen Organen gewonnen, sondern zugleich auch einen anderen Begriff,",
      "den der Ernährung des Gesamtorganismus. Worin besteht denn diese Ernährung des Gesamtorganismus? Sie besteht in nichts anderem als darin, daß die aufgenommenen Nahrungsstoffe so vorbereitet wer­den, daß es möglich ist, sie hinzuleiten nach den verschiedenen Organen, und diese sich dann die Stoffe eingliedern. Wir werden in den folgenden Vorträgen noch sehen, wie dieser allgemeine Begriff der Ernährung, der sich zeigt als eine Anziehungskraft der verschie­denen Organsysteme für die Nahrungsstoffe, sich verhält zur Entste­hung des einzelnen Menschen, zur Keimesgeschichte des einzelnen Menschen, die vor der Geburt liegt. Der umfassendste Begriff der Ernährung ist also der, daß durch übersinnliche Kraftsysteme, durch einen übersinnlichen Organismus die einzelnen Nahrungsstoffe ein-gesogen und in der verschiedensten Weise dem physischen Organis­mus eingegliedert werden.",
      "Nun müssen wir uns klar sein, daß der Ätherleib des Menschen, der das nächste übersinnliche Glied in der menschlichen Organisa­tion ist nach dem physischen Leibe, daß dieser Ätherleib, wenn er auch das gröbste der übersinnlichen Glieder ist, wie ein übersinnli­ches Urbild dem gesamten Organismus zugrundeliegt, daß er in sich gegliedert, differenziert ist und die mannigfaltigsten Kraftsysteme enthält, um sich die durch die Ernährung aufgenommenen Stoffe einzugliedern. Wir haben nun aber nach diesem ätherischen Leib, den wir als das Urbild des menschlichen Organismus betrachten können, als das nächsthöhere Glied der menschlichen Wesenheit den soge­nannten Astralleib. Wie sich diese beiden zusammenschließen, wer­den uns die nächsten Vorträge noch zeigen. Der Astralleib ist das, was sich erst eingliedern kann, wenn sowohl der physische Organis­mus als auch der ätherische Organismus ihrer Anlage nach schon vorbereitet sind; er setzt die beiden anderen Organismen voraus. Ferner haben wir das, was wir das menschliche Ich nennen, so daß die gesamte menschliche Wesenheit sich zusammenschließt aus die­sen vier Gliedern. Wir können uns nun vorstellen, daß schon im Ätherleib selbst gewisse Kraftsysteme sind, die die Nahrungsstoffe an sich ziehen und sie dann im physischen Organismus in einer ganz bestimmten Weise gestalten. Wir können uns aber auch vorstellen,",
      "daß ein solches Kraftsystem nicht nur durch den Ätherleib bestimmt ist, sondern auch durch den Astralleib und daß dieser seine Kräfte da hineinsendet, so daß, wenn wir uns das physische Organ wegdenken, wir zunächst das ätherische Kraftsystem haben würden, dann das astralische Kraftsystem, welches das ätherische Kraftsystem in einer ganz bestimmten Weise durchdringt, und wir können uns vorstellen, daß da auch noch Strahlungen vom Ich hineindringen.",
      "Es kann nun Organe geben, welche so in den Organismus einge­gliedert sind, daß ihr Wesentlichstes darauf beruht, daß die ätheri­schen Strömungen in ihrer Eigenart noch sehr wenig bestimmend gewirkt haben, so daß, wenn wir den Raum okkult untersuchen, in dem ein betreffendes Organ sich befindet, wir finden würden, daß der ätherische Teil dieses Organs recht wenig durch sich selber differenziert ist, nur wenig von diesen Kraftsystemen enthält, daß aber dafür dieser Teil des Ätherleibes durch starke astralische Kräfte beeinflußt wird. Dann wird, wenn die physische Materie sich einem solchen Organ eingliedert, der Ätherleib nur eine geringe Anzie­hungskraft auf die einzugliedernden Stoffe ausüben, die hauptsäch­lichste Anziehungskraft wird dann vom Astralleib auf das betref­fende Organ ausgeübt, und zwar so, als ob die betreffenden Stoffe direkt von dem Astralleibe hereingeholt würden in das betreffende Organ.",
      "Daraus sehen Sie, daß die Organe des Menschen von ganz verschiedener Wertigkeit sind. Es gibt solche Organe, von denen man sagen muß, daß sie hauptsächlich bestimmt sind durch Kraftsysteme des Ätherleibes, andere, die mehr bestimmt sind durch Strömungen oder Kräfte des Astralleibes, während noch andere mehr bestimmt sind durch Strömungen des Ich.",
      "Aus den Ausführungen, die in den Vorträgen gemacht worden sind, können Sie sich schon sagen, daß insbesondere das Organsystem, das unser Blut führt, im wesentlichen von solchen Strahlungen abhängt, die von unserem Ich ausgehen, daß also das menschliche Blut im wesentlichen mit Strömungen und Strahlungen des menschlichen Ich zusammenhängt. Die anderen Organsysteme und ihre Inhalte sind in den verschiedensten Abstu­fungen von den übersinnlichen Gliedern der menschlichen Natur bestimmt.",
      "Aber es kann auch der umgekehrte Fall eintreten, wenn wir nam­lich den physischen Leib an sich nehmen, der ja - jetzt abgesehen von seinen höheren Gliedern - auch ein Kraftsystem darstellt. Er stellt zunächst das dar, was man sich zusammengesetzt denken kann aus Stoffen der äußeren Welt, die auch ihre inneren Gesetze haben, die aber umgewandelt dem physischen Leibe eingefügt sind.",
      "Der physi­sche Leib ist also auch ein Kraftsystem So daß Sie sich auch den Fall denken können, daß der physische Organismus wieder zurückwirkt auf das ätherische oder bis auf das astralische Kraftsystem oder sogar bis ins Ich-System hinein. Wir müssen uns denken, daß das ätheri­sche Kraftsystem nicht nur eingefangen wird von dem astralischen oder vom Ich-System, sondern daß es auch Organe gibt, bei denen die ätherischen Kräfte von der Seite des physischen Kraftsystems derart eingespannt werden, daß das physische Kraftsystem über­wiegt.",
      "Solche Organe, bei denen der physische Leib das Überwie­gende ist, die also nur in geringerem Maße beeinflußt werden von den höheren Gliedern der menschlichen Organisation, das sind haupt­sächlich diejenigen Organe, welche im weitesten Sinne als Absonde­rungsorgane zu bezeichnen sind, alle drüsigen Organe, alle Absonde­rungsorgane überhaupt. Alle Absonderungsorgane, alle Organe, wel­che direkt Stoffe absondern, werden zu diesen Stoffabsonderungen -also zu einem Vorgang, der innerhalb der rein physischen Welt seine wesentliche Bedeutung hat - hauptsächlich durch die Kräfte des physischen Organismus veranlaßt.",
      "Wo immer im menschlichen Organismus solche Organe sind, wenn sie vorzugsweise zum Abson­dern des Stofflichen bestimmt sind, müssen wir uns klar sein, daß solche Organe, die hauptsächlich Werkzeuge der physischen Kraft-systeme sind, durch Erkrankung, durch Unbrauchbarwerden oder durch ihre Entfernung den Organismus unfehlbar zum Verfall brin­gen, so daß er dann nicht mehr in entsprechender Weise sich entwik­keIn und zuletzt nicht mehr leben kann. Sie sehen an einem solchen Organ, wie es die Milz ist, von der wir gestern gesprochen haben, daß deren Erkranken, deren sonstiges Unbrauchbarwerden oder opera­tive Entfernung den physischen Körper in seinen Funktionen weit weniger stort, als dies bei anderen Organen der Fall ist, weil sie in",
      "besonders starker Weise beeinflußt wird von den übersinnlichen Teilen der menschlichen Natur, vom Ätherleibe, namentlich aber vom Astralleibe. Anders ist es bei den Organen, wo das physische Kraftsystem überwiegt. Eine Erkrankung der Schilddrüse zum Bei­spiel, die sich bei bestimmten Erkrankungen manchmal vergrößert zur sogenannten Kropfbildung, kann auf den ganzen Organismus sehr schädlich wirken. Sie darf aber nicht vollständig unbrauchbar werden oder vollständig entfernt werden, und zwar deshalb nicht, weil sie ihre Wirkungen so zu äußern hat, daß das, was als physischer Vorgang durch sie bewirkt wird, im Gesamthaushalt des mensch­lichen Organismus ganz wesentlich ist.",
      "Nun kann es solche Organe geben, die in hohem Maße abhängen von den übersinnlichen Kraftsystemen der menschlichen Organisa­tion, die aber doch eingespannt sind in den physischen Organismus und durch dessen Kräfte veranlaßt werden, Stoffliches abzusondern. Ein solches Organ ist zum Beispiel die Leber, ebenso sind es die Nieren. Das sind Organe, die, geradeso wie die Milz, abhängig sind von den übersinnlichen Gliedern der menschlichen Organisation, vom Ätherleibe und Astralleibe, die aber sozusagen eingefangen sind von den Kräften des physischen Organismus, heruntergezogen sind in ihren Wirkungen bis zu den Kräften des Physischen. Daher kommt es bei ihnen in einem viel höheren Grade darauf an, daß sie als physische Organe in gesundem Zustande sind, als zum Beispiel bei der Milz, bei welcher die Sache so liegt, daß das Physische sehr wenig in Betracht kommt und weit überwogen wird von dem, was von den übersinnlichen Gliedern der menschlichen Organisation herkommt. Wir können von der Milz sagen, daß sie ein sehr geistiges Organ ist, denn der physische Teil dieses Organs macht den geringsten Teil seiner Bedeutung aus. Aus diesem Grunde wurde die Milz zu allen Zeiten in der okkulten Literatur, die entsprungen ist aus Kreisen, wo man wirklich etwas über diese Sachen gewußt hat, immer als ein besonders geistiges Organ angesehen und geschildert.",
      "So also haben wir jetzt gewissermaßen den Begriff des Gesamtor­ganismus gewonnen, dessen einzelnes Organ angesehen werden kann als ein übersinnliches Kraftsystem, in das gleichsam die stoffliche",
      "Materie durch den gesamten Ernährungsprozeß hineingelagert wird. Ein anderer Begriff, den wir uns aneignen müssen, ist der: Was bedeutet überhaupt für den Menschen die Aufnahme - sei es eines Stoffes oder sei es die Aufnahme eines Geistigen, die durch unsere Seelentätigkeit bewirkt wird, zum Beispiel bei der Wahrnehmung? Und was bedeutet die Absonderung, die Abgabe eines Stoffes?",
      "Gehen wir da zunächst aus von dem Absonderungsprozeß im weitesten Umfange. Wir wissen ja, daß von den aufgenommenen Nahrungsmitteln schon ein großer Teil des Stofflichen vom Verdau­ungskanal abgesondert wird. Wir wissen ferner, daß durch die Lun­gen aus dem menschlichen Organismus die Kohlensäure ausgeschie­den wird. Dann haben wir einen Absonderungsprozeß durch die Nieren, ein weiterer Absonderungsprozeß geschieht durch die Haut. In diesem letzteren, der zunächst in der Schweißbildung verläuft, aber auch in allem, was im umfänglichen Sinne als Absonderungspro­zeß durch die Haut zu gelten hat, haben wir jene Absonderung zu sehen - und ich bitte, darauf zu achten -, die beim Menschen an dem äußersten Umfange, an der äußersten Peripherie seines Leibes er­folgt. Nun fragen wir uns zunächst einmal: Was bedeutet denn überhaupt ein Absonderungsprozeß für den Menschen?",
      "Wir werden uns die Bedeutung eines Absonderungsprozesses nur klarmachen können auf folgende Weise. Sie werden sehen, daß wir ohne die Begriffe, die wir heute entwickelt haben, überhaupt nicht weiterkommen können in der Betrachtung des menschlichen Orga­nismus. Ich möchte Ihnen, um unsere Gedanken allmählich hinüber-zuführen zu der wesentlichen Natur eines Absonderungsprozesses, zunächst einen anderen Begriff vorführen, der allerdings nur eine entfernte Ähnlichkeit mit dem Absonderungsprozesse hat, der uns aber dazu hinüberführen kann, nämlich den Begriff des Gewahrwer­dens unseres Selbst. Bedenken Sie einmal, wie Sie im Grunde genom­men doch sagen können, daß es eine Art Gewahrwerden Ihres Selb­stes ist, wenn Sie in einem Raume gehen und sich unvorsichtigerweise an einem harten Gegenstande stoßen. Dieses Anstoßen ist im Grunde genommen ein Gewahrwerden des eigenen Selbstes. Es ist ein Gewahrwerden des eigenen Selbstes auf die Art, daß Ihnen das",
      "Ereignis, das sich durch den Stoß vollzogen hat, zu einem inneren Ereignis geworden ist. Denn was ist für Sie der Zusammenstoß mit einem fremden Gegenstande? Er ist die Ursache eines Wehetuns, eines Schmerzes. Der Schmerzvorgang spielt sich rein in Ihrem Inne­ren ab. Also ein innerer Vorgang wird dadurch hervorgerufen, daß Sie sich in Berührung bringen mit einem fremden Gegenstand, der Ihnen als Hindernis im Weg liegt. Das Gewahrwerden dieses Hin­dernisses ist das, was den inneren Prozeß hervorruft, der als Schmerz beim Sichstoßen auftritt. Im Grunde genommen können Sie sich leicht vorstellen, daß Sie überhaupt nichts anderes zu wissen brau­chen, um das Gewahrwerden Ihres eigenen Seibstes zu erleben, als den inneren Schmerz, der durch das Anstoßen an einen äußeren Gegenstand bewirkt wird. Denken Sie sich, daß Sie im Finstern an einen Gegenstand stoßen, von dem Sie gar nicht wissen, was er ist, und nehmen Sie an, Sie stoßen sich so stark, daß Sie auch gar nicht darauf schließen können, wie der Gegenstand beschaffen sein könnte, sondern Sie spüren nur die Wirkung des Stoßes als Schmerz. Sie haben den Stoß in seiner Wirkung so empfunden, daß Sie den Vor­gang in sich selbst erlebten. Sie erleben gar nichts anderes als einen inneren Vorgang, und das ist das Wesentliche. Wenn Sie allerdings auch sagen: Ich habe mich an einem äußeren Gegenstand gestoßen -, so ist das mehr oder weniger ein unbewußter Schluß von einem inneren Erlebnis auf ein äußeres Hindernis.",
      "Daraus können Sie sehen, daß der Mensch seines Inneren gewahr wird durch das Finden eines Widerstandes. Diesen Begriff müssen wir haben: das Gewahrwerden des Selbstes, das Erleben des Inneren, das Ausgefülltsein mit realen Erlebnissen im Inneren durch das Fin­den eines Widerstandes. Dies ist ein Begriff, den ich, ich möchte sagen, in aller Grobheit entwickelt habe, um von ihm den Übergang machen zu können zu einem anderen Begriffe, dem der Absonderun­gen im menschlichen Organismus. Denken wir uns einmal, der menschliche Organismus nehme in sich selber in irgendein Organ-system, meinetwegen in den Magen, eine gewisse Stofflichkeit auf und das Organsystem sei so eingerichtet, daß es durch seine Tätigkeit aus diesem Stoffe, der da aufgenommen ist, etwas aussondert, etwas",
      "gleichsam separiert, wegnimmt von dem Gesamtstoff, so daß durch diese Tätigkeit des Organs der Gesamtstoff zerfällt in einen feineren, gleichsam filtrierten Teil und in einen gröberen Teil, der ausgeson­dert wird. Es wird also eine Differenzierung des Stoffes vorgenom­men in einen solchen, der in einen weiter brauchbaren, für andere Organe aufzunehmenden Stoff umgewandelt wird und in einen sol­chen, der erst abgesondert und dann ausgeschieden wird.",
      "# Bild s.098",
      "Hier an dieser Stelle, wo die unbrauchbaren Teile der Stofflichkeit abgestoßen werden gegenüber den brauchbaren Stoffen, hier haben Sie in modifizierter Forin etwas wie ein Sichanstoßen an einen äußeren Gegenstand, wie ich es eben dargestellt habe. Es stößt der aufgenommene Stoffstrom, indem er an ein Organ herankommt, sozusagen auf einen Widerstand; er kann nicht. so bleiben, wie er ist, er muß sich ändern. Es wird ihm gleichsam durch das Organ gesagt:",
      "So kannst du nicht bleiben, wie du bist, du mußt dich ändern. - Es wird also dem Stoff ein Widerstand entgegengestellt, er muß als ein anderer Stoff weiterverbraucht werden, und er muß gewisse Teile abstoßen. In unserem Innern stellt sich das Organ dem Stofflauf so entgegen, wie sich der äußere Gegenstand uns entgegenstellt, an dem wir uns stoßen. Solche Widerstände finden sich innerhalb des Gesamtorganismus in den mannigfachsten Organen. Und erst dadurch, daß überhaupt in unserem Organismus abgesondert wird, erst dadurch, daß wir Absonderungsorgane haben, dadurch ist die Möglichkeit gegeben, daß unser Organismus eine in sich abgeschlos­sene, sich selbst erlebende Wesenheit ist. Denn Erleben kann sich eine Wesenheit nur dadurch, daß sie auf Widerstand stößt. So haben",
      "wir in den Absonderungsprozessen wichtige Prozesse des menschli­chen Lebens, nämlich diejenigen Prozesse, wodurch sich der leben­dige Organismus in sich selber abschließt. Der Mensch wäre kein in sich abgeschlossenes Wesen, wenn solche Absonderungsprozesse nicht vorhanden wären.",
      "Denken Sie sich einmal, der aufgenommene Nahrungsstrom oder der Sauerstoffstrom würden durch den menschlichen Organismus wie durch einen Schlauch glatt hindurchgehen und es gäbe keinen Widerstand durch die Organe. Die Folge davon wäre, daß der menschliche Organismus sich nicht in sich selbst erleben könnte, sondern er würde sich nur erleben als angehörig der gesamten großen Welt. Wir könnten uns ja allerdings auch vorstellen, daß innerhalb des menschlichen Organismus die gröbste Art dieses Widerstandbie­tens eintreten würde, daß der Stoffstrom sich an einer festen Wan­dung stoßen und reflektieren, zurückkehren würde. Das würde aber das innere Erleben des menschlichen Organismus nicht berühren,",
      "# Bild s.099",
      "denn ob der Nahrungsstrom oder der Sauerstoffstrom durch den menschlichen Organismus wie durch einen Schlauch hindurchginge, auf der einen Seite hinein, auf der anderen wieder hinaus, oder ob er reflektiert würde, das würde für das innere Erleben nichts ausma­chen. Daß das so ist, können Sie schon daraus entnehmen, daß - wie wir schon gesagt haben -, wenn wir es in unserem Nervensystem dazu bringen, daß eine Vorstellung in sich selbst zurückkehrt, wir dann geradezu unser Nervensystem herausheben aus dem Erleben des inneren Organismus. Es macht also keinen Unterschied, ob völlige",
      "Reflexion oder bloßes Hindurchgleiten der von außen hineinge­henden Ströme durch den menschlichen Organismus vorliegt. Was den menschlichen Organismus in sich selbst erlebbar macht, das sind die Absonderungen.",
      "Wenn Sie dasjenige Organ betrachten, welches wir als das Mittel­punktsorgan für den menschlichen Organismus ansehen müssen, das Blutsystem, wenn Sie sehen, wie auf der einen Seite das Blut immer­fort durch Aufnehmen von Sauerstoff sich auffrischt, und wenn Sie auf der anderen Seite das Blutsystem als das Werkzeug des menschli­chen Ich betrachten, so können wir sagen: Wenn das Blut unverän­dert durch den menschlichen Organismus hindurchgehen würde, so könnte es nicht das Organ des menschlichen Ich sein, das im eminen­testen Sinne das Organ ist, welches den Menschen sich innerlich erlebbar macht. Nur dadurch, daß das Blut in sich selber Verände­rungen durchmacht und als ein anderes wieder zurückkehrt, daß also Absonderungen geschehen von verändertem Blut, nur dadurch ist es möglich, daß der Mensch das Ich nicht nur hat, sondern es auch erleben kann mit Hilfe seines sinnlich-physischen Werkzeuges, des Blutes.",
      "Daraus hat sich uns nun dieser Begriff der Absonderung ergeben. Und jetzt werden wir uns zu fragen haben: Wie steht es nun mit jener Absonderung, welche wir vorhin bezeichnet haben als der äußersten Peripherie des menschlichen Organismus angehörig? - Es wird uns ja unschwer sein, uns vorzustellen, wie der Gesamtorganismus des Menschen wirken muß, damit diese Absonderung an der Peripherie geschehen kann. Dazu ist es notwendig, daß den gesamten Strömun­gen des menschlichen Organismus entgegengestellt werde ein Organ, welches in Zusammenhang steht gerade mit diesem umfänglichsten Absonderungsprozeß. Und dieses Organ, das ja, wie Sie sich leicht denken können, die Haut ist, mit allem, was zu ihr gehört im umfänglichsten Sinne, das ist zugleich dasjenige, was schon für den unmittelbaren äußeren Anblick als das Wesentliche der menschlichen Gestalt, der menschlichen Form sich darbietet. Wenn wir uns also vorstellen, daß der menschliche Organismus, der sich selbst erleben kann an seinem äußeren Umfange, dies nur dadurch kann, daß er das",
      "Organ der Haut seinen gesamten Strömungen entgegenstellt, so müs­sen wir in der eigenartigen Formung der Haut einen der Ausdrücke sehen für die innersten Kräfte des menschlichen Organismus.",
      "Wir werden uns nun zu fragen haben: Wie haben wir uns denn dieses Hautorgan zu denken? Wie haben wir uns die Haut mit allem, was dazugehört, zu denken? Wir werden schon sehen, was im einzel­nen dazugehört, wir wollen es aber heute nur im großen und ganzen charakterisieren.",
      "Da müssen wir uns zunächst darüber klar sein, daß in dem, was zu unserem bewußten Erleben gehört, wovon wir eine Erkenntnis haben können durch irgendeine Selbstbeobachtung, jene Gestaltung nicht einbegriffen ist, welche in der Formung unserer Haut zum Ausdruck kommt. Selbst wenn wir in begrenztem Umfange mittätig sind an der Gestaltung unserer äußeren Körper-oberfläche, so ist sie doch etwas, das sich der unmittelbaren Willkür in vollkommenster Weise entzieht.",
      "Nur in bezug auf die Beweglich­keit unserer Haut, in bezug auf Mienenspiel, Gesten und so weiter, haben wir ja einen Einfluß, der noch an das heranreicht, was wir bewußte Tätigkeit nennen können; aber auf die Gestalt, auf die Form unserer Körperoberfläche haben wir keinen Einfluß mehr. Es muß freilich zugegeben werden, daß der Mensch zwischen Geburt und Tod einen gewissen Einfluß auf seine äußere Leibesform in engeren Grenzen hat.",
      "Davon kann sich jeder überzeugen, der einen Menschen kennengelernt hat in einem bestimmten Lebensalter und ihn viel­leicht nach zehn oder zwanzig Jahren wiedersieht, insbesondere wenn dieser Mensch in diesen Jahren durchgegangen ist durch tiefere innere Erlebnisse, namentlich durch Erkenntniserlebnisse, die nicht Gegenstand der äußeren Wissenschaft sind, sondern durch solche, die «Blut kosten», die zusammenhängen mit unserem ganzen Lebensschicksal. Dann sehen wir allerdings innerhalb enger Gren­zen, wie die Physiognomie sich ändert, wie also der Mensch inner-halb dieser Grenzen einen Einfluß hat auf die Gestaltung seines Leibes.",
      "Aber er hat ihn nur in geringem Maße, und das wird jeder zugeben müssen; denn das Hauptsächlichste in der menschlichen Gestalt ist durchaus nicht in unsere Willkür gegeben und nicht durch unser Bewußtsein bestimmt. Dennoch müssen wir sagen: Die ganze",
      "menschliche Gestalt ist angepaßt der menschlichen Wesenheit; und wer auf die Dinge eingeht, wird sich niemals vorstellen können, daß dasjenige, was wir den ganzen Umfang der menschlichen Fähigkeiten nennen, sich entwickeln könnte in einem Wesen von einer anderen Gestalt, als es die heutige Menschengestalt ist. Alles, was an Fähigkei­ten im Menschen ist, hängt zusammen mit dieser Menschengestalt.",
      "Denken Sie sich nur einmal, daß etwa das Stirnbein in einer irgendwie anderen Lage wäre zu dem Gesamtorganismus, als es ist, so würde diese Gestaltänderung ganz andere Fähigkeiten und Kräfte im Men­schen voraussetzen. Darüber könnten ja Studien gemacht werden, indem man sich klarmacht, wie andere Fähigkeiten vorhanden wären bei Menschen mit verschiedener äußerer Gestaltung des Kopfes, des Schädelbaus und so weiter.",
      "So müssen wir uns einen Begriff verschaf­fen von dem Angepaßtsein der menschlichen Gestalt an die gesamte innere menschliche Wesenheit, ja, von einem völligen Sichentspre­chen der äußeren Gestalt und der inneren Wesenheit des Menschen. Was in den Kräften dieser Anpassung liegt, hat nichts zu tun mit dem, was in die eigene, vom Bewußtsein umspannte Tätigkeit des Menschen hereingehört.",
      "Da aber die Gestalt des Menschen zusam­menhängt mit seiner geistigen Betätigung und auch mit seinem seeli­schen Leben, so können Sie es sich leicht vorstellen, daß in den Kräften, welche die physische Gestalt des Menschen zustande brin­gen, solche Kräfte liegen, die gleichsam von einer anderen Seite entgegenkommen denjenigen Kräften, die der Mensch in sich selbst entwickelt. Kräfte der Intelligenz, Gefühlskräfte, Gemütskräfte und so weiter, die kann der Mensch nur entwickeln in der physischen Welt unter der Voraussetzung seiner besonderen Gestalt.",
      "Diese Gestalt muß ihm gegeben sein. Er muß also diese Gestalt für seine Fähigkeiten zubereitet erhalten - wenn ich mich so ausdrücken darf -von Kräften entsprechend ähnlicher Art wie die, die von der anderen Seite her diese Gestalt erst aufbauen, damit sie dann zu dem gebraucht werden kann, wozu sie verwendet werden soll.",
      "Es ist unschwer, sich diesen Begriff zu verschaffen, denn man braucht nur daran zu denken, daß eine Maschine, die wir zu einer Tätigkeit verwenden wollen, für diese Tätigkeit intelligent und zweckmäßig",
      "eingerichtet sein muß. Damit eine solche Maschine zustande komme, ist es notwendig, daß zuerst ähnliche Verrichtungen vollführt wer­den, wie sie dann von der Maschine ausgeführt werden sollen, und danach die Teile der Maschine herzustellen und zusammenzuglie­dern, welche der Maschine ihre Form geben. Wenn wir eine fertige Maschine vor uns haben, so ist sie für uns ganz mechanisch erklärbar, wenn wir ihre Wirksamkeit sehen und verstehen. Als denkende Beobachter werden wir uns aber fragen: Wer ist es, der sie gebaut hat? - Denn ihre Zusammensetzung weist auf eine zielbewußte gei­stige Tätigkeit hin, welche diese Maschine zu einem bestimmten Zwecke hergestellt hat. Diese geistige Tätigkeit braucht nicht mehr da zu sein, wenn wir die Maschine mechanisch erklären wollen, aber sie steht hinter der Maschine, sie hat sie erst zustande gebracht.",
      "Ebenso können wir sagen: Alles, was an Formsystemen in der Gestaltung unseres Organismus liegt, das ist uns in erster Linie gegeben, damit wir unsere Fähigkeiten und Kräfte als Menschen entwickeln. Aber es muß hinter dieser Gestaltung des Menschen gestaltunggebende, formgebende Kräfte geben, die wir ebensowenig in der fertigen Gestalt finden, wie wir in der Maschine den Maschi­nenbauer finden.",
      "Mit dieser Idee wird Ihnen zugleich etwas anderes völlig einleuch­tend sein. Ein materialistischer Denker könnte sagen: Wozu braucht man intelligente Kräfte und bewußt schaffende Wesenheiten anzu­nehmen hinter unserer physischen Welt? Wir können ja die physi­sche Welt aus sich selbst, aus ihren eigenen Gesetzen erklären. Eine Uhr, eine Maschine kann aus ihren eigenen Gesetzen heraus erklärt werden. - Hier stehen wir an einem Punkte, wo hüben und drüben die schlimmsten Fehler gemacht werden, sowohl bei solchen, die auf dem Boden einer spirituellen Weltanschauung stehen, wie auch auf der Seite der Materialisten. Wenn zum Beispiel von einer geisteswis­senschaftlichen Weltanschauung bestritten würde, daß der menschli­che Organismus, wie er seiner Form nach vorliegt, nicht rein mecha­nisch oder mechanistisch durch seine eigenen Gesetze erklärbar wäre, so würde das selbstverständlich zu weit gehen und ganz unberechtigt sein. Der menschliche Organismus ist ganz und gar aus seinen eigenen",
      "Gesetzen heraus erklärbar, wie die Uhr auch. Aber daraus, daß die Uhr aus ihren eigenen Gesetzen erklärbar ist, folgt nicht, daß hinter der Uhr nicht der Erfinder der Uhr stand, der Uhrmacher und seine geistige Tätigkeit. Dieser Einwand, der von materialistischer Seite aus gemacht werden kann, erledigt sich dadurch. Aber der Geistesforscher muß auch zugeben, daß der menschliche Organis­mus, so wie er vor uns steht, aus seinen eigenen Gesetzen erklärt werden kann. Aber wenn wir wirklich geisteswissenschaftlich den­ken, haben wir hinter der Gesamtgestaltung des menschlichen Or­ganismus zu suchen die gestaltenden Wesenheiten, dasjenige also, was der gesamten Form der menschlichen Wesenheit zugrundeliegt. Wenn wir uns nun einen Begriff davon bilden wollen, wie überhaupt die menschliche Form zustande kommt, so müssen wir uns denken, daß sie auf der einen Seite dadurch bewirkt wird, daß die formgeben­den Kräfte sich entfalten und daß sie den Menschen dadurch auf­bauen, daß sie sich an den Grenzen der menschlichen Form selbst abschließen. Wir haben in der Hautbildung das am reinsten gegeben, was das räumliche Sichabschließen der formgebenden Kräfte im Menschen bedeutet. Wenn wir das schematisch zeichnen, können wir uns denken, daß die formgebenden Kräfte zur Peripherie dahinflie­ßen und sich da abschließen in der äußeren Form, die in der Linie A-B nur angedeutet werden soll.",
      "# Bild s. 104",
      "Wir werden nun sehen, wie wir diesen Begriff wiederum brauchen, um alles das erkennen zu können, was innerhalb der Haut geschieht. Weiter aber werden wir uns darüber klar werden müssen, daß wir",
      "nun nicht bloß in der menschlichen Haut solche Abschlüsse vor uns haben, sondern daß wir auch innerhalb des menschlichen Organis­mus selber solches Abschließen der von außen wirkenden Tätigkeit und Wesenhaftigkeit finden. Sie brauchen sich nur zu überlegen, was bisher gesagt worden ist, dann werden Sie darauf kommen, daß wir auch im Inneren des Menschen solche sich abschließenden Tätigkei­ten vor uns haben, an denen wir ebenso unbeteiligt sind wie an unserer Oberflächengestaltung, und das sind gerade diejenigen Betä­tigungen, die zustande kommen in den Organen Leber, Galle, Milz und so weiter. Da wird das aufgehalten, was durch die Kräfte, die in den Nahrungsmitteln sitzen, in den Organismus einströmt, dem wird etwas entgegengeschoben, wird ein Widerstand entgegengesetzt, das heißt, es wird in diesen Organen die äußere, die eigene Regsamkeit der Stoffe umgeändert. Während also bei den formgebenden Kräften",
      "# Bild s. 105",
      "die Sache so ist, daß wir uns diese formenden Kräfte wirksam zu denken haben bis zur Haut hin und außerhalb der Haut nichts mehr von formgebenden Kräften haben, müssen wir uns vorstellen, daß bei denjenigen Kräften, die mit dem Nahrungs- oder Luftstrom nach unserem Inneren gehen, nicht ein vollständiges Abschließen dessen vorhanden ist, was als Strömungen von außen eindringt, sondern es tritt da eine Umgestaltung ein. Diese Organe müssen wir uns so denken, daß sie nicht, wie es bei der Haut ist, sich abschließen, so daß außerhalb nichts mehr ist, sondern so, daß die Regsamkeit der Stoffe",
      "umgeändert wird durch sie derart, daß der Nahrungsstrom, der von der Seite dieser Organe her aufgenommen ist (siehe Zeichnung, a), in einer anderen Weise weitergeleitet wird (b), nachdem ihm ein Wider­stand entgegengesetzt worden ist. Hier haben wir es also mit einer Umänderung zu tun, und das betrifft vor allem diejenigen Organe, welche wir als ein inneres Weltsystem des Menschen bezeichnet haben. Die ändern die äußere Regsamkeit der Stoffe um. Es sind Kräfte, die wir im Gegensatz zu den Formkräften, die den gesamten Organismus bilden, Bewegungskräfte nennen können. In unserem inneren Weltsystem werden diese Kräfte, welche die innere Regsam­keit der Nahrungsstoffe umgestalten, dann Bewegung, so daß wir hier von Bewegungskräften in den Organen sprechen können.",
      "Wir sind jetzt so weit vorgeschritten in den Betrachtungen des menschlichen Organismus, daß wir sagen können: In den menschli­chen Organismus wirken von außen Kräfte herein, deren Tätigkeit wir mit unserem Bewußtsein nicht wahrnehmen. Das alles geht unterhalb unseres Bewußtseinshorizontes vor sich, was wir da als Tätigkeit ausführen; niemand kann im normalen Bewußtsein die Tätigkeit seiner Leber, Galle, Milz und so weiter beobachten. Nun entsteht die Frage: Wodurch werden wir denn verhindert, etwas zu wissen von den Form- und Bewegungskräften, die sich in unseren inneren Organen abspielen, da doch unser Seelenleben dem Organis­mus eingegliedert ist? Da gehen ja in unserem Innern gewaltige Tätigkeiten vor sich. Woher kommt es, daß wir davon nichts wissen?",
      "Nun, genau ebenso wie unser Gehirn-Rückenmark-Nervensystem dazu bestimmt ist, die äußeren Eindrücke, die wir durch unsere Sinne erhalten, bis zum Blute hinzuleiten, das heißt, die Impressionen von äußeren Vorgängen in unser Blut, in das Werkzeug des Ich, aufzu­nehmen, ebenso wie also das Gehirn-Rückenmark-Nervensystem dazu bestimmt ist, im normalen Bewußtsein dem Ich zu dienen, gerade so ist das sympathische Nervensystem, das sich mit seinen Knoten und Verzweigungen dem inneren Weltsystem gleichsam vor-lagert, dazu ausersehen, die Vorgänge, die sich im Innern des Orga­nismus abspielen, nicht an das Blut, das Werkzeug des Ich, heran-zulassen, sondern sie vom Blut zurückzuhalten.",
      "# Bild s. 107",
      "So sehen Sie, daß das sympathische Nervensystem eine entgegen­gesetzte Aufgabe hat wie das Gehirn-Rückenmark-Nervensystem, und hier haben wir eine Erklärung für den Unterschied in Bau und Beschaffenheit dieser beiden Systeme. Während das Gehirn-Rücken-mark-Nervensystem sich anstrengen muß, um möglichst gut die äußeren Eindrücke zum Blut überzuleiten, muß durch das entgegen­gesetzt wirkende sympathische Nervensystem vom Blut - als dem Werkzeug des Ich - fortwährend zurückgestaut werden die Eigen-regsamkeit der aufgenommenen Stoffe. Wenn wir den Verdauungs­prozeß betrachten, so haben wir zuerst das Aufnehmen der äußeren Nahrungsstoffe, dann das Zurückstauen der Eigenregsamkeit der Nahrungsstoffe und dann die Umwandlung dieser Regsamkeiten durch das innere Weltsystem des Menschen. Damit wir nicht fort-während, wie wir so dastehen in der Welt, alles das wahrnehmen, was in unseren inneren Organen bewirkt wird, muß der ganze Strom der Vorgänge durch das sympathische Nervensystem zurückgestaut wer­den vom Blut, geradeso wie durch das Gehirn-Rückenmark-Nerven­system das zum Blute hingetragen wird, was von außen aufgenom­men wird. Da haben Sie die Aufgabe des sympathischen Nerven­systems, unsere inneren Vorgänge in uns zu halten, sie nicht bis zum Blut, dem Werkzeug des Ich, hinaufdringen zu lassen, um das Ein-treten dieser inneren Vorgänge in das Ichbewußtsein zu verhindern.",
      "Ich habe schon gestern darauf hingewiesen, daß das Außenleben und das Innenleben des Menschen, wie es sich im Ätherleibe auslebt,",
      "in einem Gegensatz zueinander stehen und daß dieser Gegensatz von Außenleben und Innenleben in Spannungen zum Ausdruck kommt, die, wie wir gesehen haben, am stärksten werden in den Organen des Gehirnes, die wir als Zirbeldrüse und Gehirnanhang bezeichnen.",
      "Wenn Sie nun die heutige und die gestrige Ausführung zusammen­nehmen, so werden Sie sich leicht denken können, daß alles, was von außen hereinströmt, um in möglichst engen Kontakt mit der Blutzir­kulation zu treten, darnach strebt, sich zu vereinigen mit seinem Gegensatze, mit dem, was von innen kommt und zurückgehalten wird durch das sympathische Nervensystem. In der Zirbeldrüse haben wir die Stelle, wo das durch das Gehirn-Rückenmark-Nerven­system an das Blut von außen Herangebrachte sich vereinigen will mit dem, was von der anderen Seite kommt, und der Hirnanhang ist gleichsam der letzte Vorposten, um das nicht heranzulassen an das Blut, was menschliches Innenleben ist.",
      "Es stehen sich an dieser Stelle im Gehirn zwei wichtige Organe gegenüber. Das gesamte innere Erleben bleibt unter unserem Bewußtsein; es würde uns ja auch in einer furchtbaren Weise stören, wenn wir bewußt mitmachen wür­den unsere ganzen Ernährungsprozesse; das wird zurückgehalten durch das sympathische Nervensystem.",
      "Nur wenn dieses gegensei­tige Verhältnis zwischen den beiden Nervensystemen, wie es sich ausdrückt in dem Spannungsverhältnis zwischen Zirbeldrüse und Hirnanhang, nicht in Ordnung ist, stellt sich das heraus, was wir nennen können ein Durchschimmern der einen Seite in die andere hinein, ein Gestörtwerden der einen Seite von der anderen Seite her. Das tritt zum Beispiel schon dann ein, wenn eine unregelmäßige Tätigkeit unserer Verdauungsorgane uns in unbehaglichen Gefühlen zum Bewußtsein kommt.",
      "Da haben wir ein - allerdings noch sehr unbestimmtes - Hereinstrahlen des sonst unbewußten menschlichen Innenlebens in das Bewußtsein, das sich aber auf diesem Wege bedeutend umgewandelt hat, also im Bewußtsein nicht so erscheint, wie es sich abgespielt hat. Oder wir haben in besonderen Affekten, Zorn, Wut, Schrecken und dergleichen, die ihren Ursprung im Bewußtsein haben, ein besonders starkes Hereinstrahlen von der Seite des inneren menschlichen Organismus; da haben wir den Fall,",
      "daß Affekte, besondere innere Erregungen der Seele, die Verdauung, das Atmungssystem und dadurch auch die Blutzirkulation und alles, was unterhalb des Bewußtseins liegt, in besonders schädigender Weise beeinflussen können. So können diese zwei Seiten der mensch­lichen Natur dennoch aufeinander wirken.",
      "So stehen wir als Menschen in der Tat als eine Zweiheit in der Welt, und wir haben heute diese Zweiheit gesehen: Auf der einen Seite bewußtes Erleben der Außenwelt durch das Gehirn-Rücken-mark-Nervensystem, welches die äußeren Eindrücke bis zum Blut, dem Werkzeuge des Ich, bringt; auf der anderen Seite unbewußtes Erleben der Innenwelt, unbewußt, weil es durch das sympathische Nervensystem vom Blute zurückgehalten wird. Diese beiden Gegen­sätze stehen sich auf der ganzen Linie gegenüber. Aber wir finden ihren besonderen Ausdruck in der Spannung zwischen diesen beiden Organen, von denen wir gesprochen haben: der Zirbeldrüse und dem Hirnanhang.",
      "Von diesem Punkte aus wollen wir das nächste Mal unsere Betrachtungen fortsetzen."
    ],
    "sentences": [
      [
        "Es wird heute meine Aufgabe sein, bevor wir in unseren Betrachtun­gen weiterschreiten, einige Begriffe herbeizutragen, die wir in der weiteren Folge unserer Darstellungen notwendig brauchen werden.",
        "Da wird es insbesondere wichtig sein, daß wir uns verständigen über die Bedeutung dessen, was wir im geisteswissenschaftlichen, anthro­posophischen Sinne ein physisches Organ nennen oder vielmehr den physischen Ausdruck eines Organs.",
        "Denn Sie haben ja schon gese­hen, daß wir zum Beispiel über die Milz so reden können, daß die physische Milz sogar materiell entfernt werden kann oder unbrauch­bar werden kann, ohne daß dasjenige, was wir im anthroposophi­schen Sinne die «Milz» nennen, von seiner Tätigkeit ausgeschaltet wird.",
        "Es bleibt dennoch, wenn wir ein solches physisches Organ ausgeschaltet, entfernt haben, im Organismus die Tätigkeit, die innere Regsamkeit, die durch das Organ ausgeübt worden war, immer noch übrig.",
        "Daraus sehen wir - und ich bitte Sie recht sehr, sich einen solchen Begriff für das folgende anzueignen -, daß wir alles, was physisch anschaubar, was physisch wahrnehmbar ist bei einem solchen Organ, uns wegdenken können - natürlich kann man das nicht von jedem Organ sagen -, und es bleibt doch die bestim­mungsgemäße Funktion des Organs; und das, was dann bleibt, was die Funktion weiter fortführt, das müssen wir zu dem Übersinnli­chen des menschlichen Organismus rechnen."
      ],
      [
        "Nun sprechen wir aber überhaupt, wenn wir im Sinne unserer Geisteswissenschaft von solchen Organen sprechen wie Milz, Leber, Galle, Nieren, Lungen und so weiter, indem wir diese Namen aus­sprechen, zunächst gar nicht von dem, was man physisch sehen kann, sondern wir bezeichnen damit die in diesen Organen wirkenden Kraftsysteme, die übersinnlicher Natur sind.",
        "Daher werden wir, und das ist in besonderem Grade bei der Milz der Fall, wenn wir geistes-wissenschaftlich davon sprechen, zunächst ein äußerlich physisch nicht sichtbares Kraftsystem uns denken müssen.",
        "Denken wir also in"
      ],
      [
        "dem, was ich hier zeichne, ein physisch nicht sichtbares Kraftsystem, das nur anschaubar werden könnte für ein übersinnliches Schauen."
      ],
      [
        "# Bild s.090"
      ],
      [
        "Ein solches wäre also zum Beispiel in der Gegend unserer Milz nur als übersinnliches Kraftsystem sichtbar.",
        "Wenn wir nun ins Auge fassen, daß ja im wirklichen uns vorliegenden menschlichen Organis­mus dieses übersinnliche Kraftsystem ausgefüllt ist mit sinnlicher Materie, so müssen wir uns fragen: Wie haben wir uns nun das Verhältnis dieses übersinnlichen Kraftsystems zu dem, was sinnliche Materie ist, zu denken?"
      ],
      [
        "Ich glaube, es wird Ihnen nicht schwierig werden, zu denken, daß Kräfte durch den Raum gehen können, welche zunächst nicht sinn­lich anschaubar sind.",
        "Man braucht sich nur an folgendes zu erinnern:"
      ],
      [
        "Wer zum Beispiel niemals etwas von der Realität der Luft in einer von Wasser entleerten Flasche gehört hat, der wird der Meinung sein, die Flasche sei ganz leer.",
        "Ein solcher physikalisch Unkundiger wird"
      ],
      [
        "einigermaßen erstaunt sein zu sehen, daß, wenn wir eine leere Was­serflasche auf den Tisch stellen, einen gut anschließenden enghalsigen Trichter aufsetzen und rasch Wasser in den Trichter eingießen, wir das Wasser im Trichter behalten und es nicht in die Flasche hinein-fließen kann, weil es durch den Gegendruck der Luft verhindert wird, in die Flasche einzudringen.",
        "Ein solcher Mensch wird dann gewahr, daß doch ein für ihn Unsichtbares in der Flasche darinnen ist, welches das Wasser zurückhält."
      ],
      [
        "Denken Sie sich diesen Begriff etwas erweitert, so wird es auch nicht schwierig sein, sich vorzustel­len, daß der Raum von Kraftsystemen durchdrungen sein kann, welche zunächst übersinnlicher Natur sind, so daß wir sie nicht mit dem Messer durchschneiden können und daß sie auch nicht ange­griffen werden können, wenn ein physisches Organ, das ihr materiel­ler Ausdruck ist, zum Beispiel die Milz, erkranken sollte.",
        "Wir haben uns zu denken, daß ein übersinnliches Kraftsystem zu dem, was wir als physisch-sinnliches Organ sehen, in einem solchen Verhältnis steht, daß physische Materie sich in dieses Kraftsystem einlagert, angezogen von den Kraftpunkten und Kraftlinien, und dadurch zu einem physischen Organ wird."
      ],
      [
        "Wir können sagen: Der Grund, warum zum Beispiel an der Stelle der Milz ein physisch-sinnliches Organ sichtbar ist, ist also der, daß dort in einer ganz bestimmten Weise Kraftsysteme den Raum ausfüllen, welche die Materie so heranziehen, daß sie sich in einer solchen Weise einlagert, wie wir es an dem äußeren Organ der Milz sehen, wenn wir es anatomisch betrachten."
      ],
      [
        "So können Sie sich die verschiedensten Organe im menschlichen Organismus denken.",
        "Sie sind zuerst übersinnlich veranlagt und dann ausgefüllt unter dem Einfluß der verschiedensten übersinnlichen Kraftsysteme von physischer Materie.",
        "Daher müssen wir in diesen Kraftsystemen zunächst einen übersinnlichen Organismus sehen, der in sich differenziert ist, der in den verschiedensten Weisen die physi­sche Materie sich eingliedert und dessen Kompliziertheit das physi­sche, ihm eingegliederte Organ nur unvollständig zu folgen vermag.",
        "Damit haben wir nicht nur den Begriff des Verhältnisses der über­sinnlichen Kraftsysteme zu den eingelagerten physisch-materiellen Organen gewonnen, sondern zugleich auch einen anderen Begriff,"
      ],
      [
        "den der Ernährung des Gesamtorganismus.",
        "Worin besteht denn diese Ernährung des Gesamtorganismus?",
        "Sie besteht in nichts anderem als darin, daß die aufgenommenen Nahrungsstoffe so vorbereitet wer­den, daß es möglich ist, sie hinzuleiten nach den verschiedenen Organen, und diese sich dann die Stoffe eingliedern.",
        "Wir werden in den folgenden Vorträgen noch sehen, wie dieser allgemeine Begriff der Ernährung, der sich zeigt als eine Anziehungskraft der verschie­denen Organsysteme für die Nahrungsstoffe, sich verhält zur Entste­hung des einzelnen Menschen, zur Keimesgeschichte des einzelnen Menschen, die vor der Geburt liegt.",
        "Der umfassendste Begriff der Ernährung ist also der, daß durch übersinnliche Kraftsysteme, durch einen übersinnlichen Organismus die einzelnen Nahrungsstoffe ein-gesogen und in der verschiedensten Weise dem physischen Organis­mus eingegliedert werden."
      ],
      [
        "Nun müssen wir uns klar sein, daß der Ätherleib des Menschen, der das nächste übersinnliche Glied in der menschlichen Organisa­tion ist nach dem physischen Leibe, daß dieser Ätherleib, wenn er auch das gröbste der übersinnlichen Glieder ist, wie ein übersinnli­ches Urbild dem gesamten Organismus zugrundeliegt, daß er in sich gegliedert, differenziert ist und die mannigfaltigsten Kraftsysteme enthält, um sich die durch die Ernährung aufgenommenen Stoffe einzugliedern.",
        "Wir haben nun aber nach diesem ätherischen Leib, den wir als das Urbild des menschlichen Organismus betrachten können, als das nächsthöhere Glied der menschlichen Wesenheit den soge­nannten Astralleib.",
        "Wie sich diese beiden zusammenschließen, wer­den uns die nächsten Vorträge noch zeigen.",
        "Der Astralleib ist das, was sich erst eingliedern kann, wenn sowohl der physische Organis­mus als auch der ätherische Organismus ihrer Anlage nach schon vorbereitet sind; er setzt die beiden anderen Organismen voraus.",
        "Ferner haben wir das, was wir das menschliche Ich nennen, so daß die gesamte menschliche Wesenheit sich zusammenschließt aus die­sen vier Gliedern.",
        "Wir können uns nun vorstellen, daß schon im Ätherleib selbst gewisse Kraftsysteme sind, die die Nahrungsstoffe an sich ziehen und sie dann im physischen Organismus in einer ganz bestimmten Weise gestalten.",
        "Wir können uns aber auch vorstellen,"
      ],
      [
        "daß ein solches Kraftsystem nicht nur durch den Ätherleib bestimmt ist, sondern auch durch den Astralleib und daß dieser seine Kräfte da hineinsendet, so daß, wenn wir uns das physische Organ wegdenken, wir zunächst das ätherische Kraftsystem haben würden, dann das astralische Kraftsystem, welches das ätherische Kraftsystem in einer ganz bestimmten Weise durchdringt, und wir können uns vorstellen, daß da auch noch Strahlungen vom Ich hineindringen."
      ],
      [
        "Es kann nun Organe geben, welche so in den Organismus einge­gliedert sind, daß ihr Wesentlichstes darauf beruht, daß die ätheri­schen Strömungen in ihrer Eigenart noch sehr wenig bestimmend gewirkt haben, so daß, wenn wir den Raum okkult untersuchen, in dem ein betreffendes Organ sich befindet, wir finden würden, daß der ätherische Teil dieses Organs recht wenig durch sich selber differenziert ist, nur wenig von diesen Kraftsystemen enthält, daß aber dafür dieser Teil des Ätherleibes durch starke astralische Kräfte beeinflußt wird.",
        "Dann wird, wenn die physische Materie sich einem solchen Organ eingliedert, der Ätherleib nur eine geringe Anzie­hungskraft auf die einzugliedernden Stoffe ausüben, die hauptsäch­lichste Anziehungskraft wird dann vom Astralleib auf das betref­fende Organ ausgeübt, und zwar so, als ob die betreffenden Stoffe direkt von dem Astralleibe hereingeholt würden in das betreffende Organ."
      ],
      [
        "Daraus sehen Sie, daß die Organe des Menschen von ganz verschiedener Wertigkeit sind.",
        "Es gibt solche Organe, von denen man sagen muß, daß sie hauptsächlich bestimmt sind durch Kraftsysteme des Ätherleibes, andere, die mehr bestimmt sind durch Strömungen oder Kräfte des Astralleibes, während noch andere mehr bestimmt sind durch Strömungen des Ich."
      ],
      [
        "Aus den Ausführungen, die in den Vorträgen gemacht worden sind, können Sie sich schon sagen, daß insbesondere das Organsystem, das unser Blut führt, im wesentlichen von solchen Strahlungen abhängt, die von unserem Ich ausgehen, daß also das menschliche Blut im wesentlichen mit Strömungen und Strahlungen des menschlichen Ich zusammenhängt.",
        "Die anderen Organsysteme und ihre Inhalte sind in den verschiedensten Abstu­fungen von den übersinnlichen Gliedern der menschlichen Natur bestimmt."
      ],
      [
        "Aber es kann auch der umgekehrte Fall eintreten, wenn wir nam­lich den physischen Leib an sich nehmen, der ja - jetzt abgesehen von seinen höheren Gliedern - auch ein Kraftsystem darstellt.",
        "Er stellt zunächst das dar, was man sich zusammengesetzt denken kann aus Stoffen der äußeren Welt, die auch ihre inneren Gesetze haben, die aber umgewandelt dem physischen Leibe eingefügt sind."
      ],
      [
        "Der physi­sche Leib ist also auch ein Kraftsystem So daß Sie sich auch den Fall denken können, daß der physische Organismus wieder zurückwirkt auf das ätherische oder bis auf das astralische Kraftsystem oder sogar bis ins Ich-System hinein.",
        "Wir müssen uns denken, daß das ätheri­sche Kraftsystem nicht nur eingefangen wird von dem astralischen oder vom Ich-System, sondern daß es auch Organe gibt, bei denen die ätherischen Kräfte von der Seite des physischen Kraftsystems derart eingespannt werden, daß das physische Kraftsystem über­wiegt."
      ],
      [
        "Solche Organe, bei denen der physische Leib das Überwie­gende ist, die also nur in geringerem Maße beeinflußt werden von den höheren Gliedern der menschlichen Organisation, das sind haupt­sächlich diejenigen Organe, welche im weitesten Sinne als Absonde­rungsorgane zu bezeichnen sind, alle drüsigen Organe, alle Absonde­rungsorgane überhaupt.",
        "Alle Absonderungsorgane, alle Organe, wel­che direkt Stoffe absondern, werden zu diesen Stoffabsonderungen -also zu einem Vorgang, der innerhalb der rein physischen Welt seine wesentliche Bedeutung hat - hauptsächlich durch die Kräfte des physischen Organismus veranlaßt."
      ],
      [
        "Wo immer im menschlichen Organismus solche Organe sind, wenn sie vorzugsweise zum Abson­dern des Stofflichen bestimmt sind, müssen wir uns klar sein, daß solche Organe, die hauptsächlich Werkzeuge der physischen Kraft-systeme sind, durch Erkrankung, durch Unbrauchbarwerden oder durch ihre Entfernung den Organismus unfehlbar zum Verfall brin­gen, so daß er dann nicht mehr in entsprechender Weise sich entwik­keIn und zuletzt nicht mehr leben kann.",
        "Sie sehen an einem solchen Organ, wie es die Milz ist, von der wir gestern gesprochen haben, daß deren Erkranken, deren sonstiges Unbrauchbarwerden oder opera­tive Entfernung den physischen Körper in seinen Funktionen weit weniger stort, als dies bei anderen Organen der Fall ist, weil sie in"
      ],
      [
        "besonders starker Weise beeinflußt wird von den übersinnlichen Teilen der menschlichen Natur, vom Ätherleibe, namentlich aber vom Astralleibe.",
        "Anders ist es bei den Organen, wo das physische Kraftsystem überwiegt.",
        "Eine Erkrankung der Schilddrüse zum Bei­spiel, die sich bei bestimmten Erkrankungen manchmal vergrößert zur sogenannten Kropfbildung, kann auf den ganzen Organismus sehr schädlich wirken.",
        "Sie darf aber nicht vollständig unbrauchbar werden oder vollständig entfernt werden, und zwar deshalb nicht, weil sie ihre Wirkungen so zu äußern hat, daß das, was als physischer Vorgang durch sie bewirkt wird, im Gesamthaushalt des mensch­lichen Organismus ganz wesentlich ist."
      ],
      [
        "Nun kann es solche Organe geben, die in hohem Maße abhängen von den übersinnlichen Kraftsystemen der menschlichen Organisa­tion, die aber doch eingespannt sind in den physischen Organismus und durch dessen Kräfte veranlaßt werden, Stoffliches abzusondern.",
        "Ein solches Organ ist zum Beispiel die Leber, ebenso sind es die Nieren.",
        "Das sind Organe, die, geradeso wie die Milz, abhängig sind von den übersinnlichen Gliedern der menschlichen Organisation, vom Ätherleibe und Astralleibe, die aber sozusagen eingefangen sind von den Kräften des physischen Organismus, heruntergezogen sind in ihren Wirkungen bis zu den Kräften des Physischen.",
        "Daher kommt es bei ihnen in einem viel höheren Grade darauf an, daß sie als physische Organe in gesundem Zustande sind, als zum Beispiel bei der Milz, bei welcher die Sache so liegt, daß das Physische sehr wenig in Betracht kommt und weit überwogen wird von dem, was von den übersinnlichen Gliedern der menschlichen Organisation herkommt.",
        "Wir können von der Milz sagen, daß sie ein sehr geistiges Organ ist, denn der physische Teil dieses Organs macht den geringsten Teil seiner Bedeutung aus.",
        "Aus diesem Grunde wurde die Milz zu allen Zeiten in der okkulten Literatur, die entsprungen ist aus Kreisen, wo man wirklich etwas über diese Sachen gewußt hat, immer als ein besonders geistiges Organ angesehen und geschildert."
      ],
      [
        "So also haben wir jetzt gewissermaßen den Begriff des Gesamtor­ganismus gewonnen, dessen einzelnes Organ angesehen werden kann als ein übersinnliches Kraftsystem, in das gleichsam die stoffliche"
      ],
      [
        "Materie durch den gesamten Ernährungsprozeß hineingelagert wird.",
        "Ein anderer Begriff, den wir uns aneignen müssen, ist der: Was bedeutet überhaupt für den Menschen die Aufnahme - sei es eines Stoffes oder sei es die Aufnahme eines Geistigen, die durch unsere Seelentätigkeit bewirkt wird, zum Beispiel bei der Wahrnehmung?",
        "Und was bedeutet die Absonderung, die Abgabe eines Stoffes?"
      ],
      [
        "Gehen wir da zunächst aus von dem Absonderungsprozeß im weitesten Umfange.",
        "Wir wissen ja, daß von den aufgenommenen Nahrungsmitteln schon ein großer Teil des Stofflichen vom Verdau­ungskanal abgesondert wird.",
        "Wir wissen ferner, daß durch die Lun­gen aus dem menschlichen Organismus die Kohlensäure ausgeschie­den wird.",
        "Dann haben wir einen Absonderungsprozeß durch die Nieren, ein weiterer Absonderungsprozeß geschieht durch die Haut.",
        "In diesem letzteren, der zunächst in der Schweißbildung verläuft, aber auch in allem, was im umfänglichen Sinne als Absonderungspro­zeß durch die Haut zu gelten hat, haben wir jene Absonderung zu sehen - und ich bitte, darauf zu achten -, die beim Menschen an dem äußersten Umfange, an der äußersten Peripherie seines Leibes er­folgt.",
        "Nun fragen wir uns zunächst einmal: Was bedeutet denn überhaupt ein Absonderungsprozeß für den Menschen?"
      ],
      [
        "Wir werden uns die Bedeutung eines Absonderungsprozesses nur klarmachen können auf folgende Weise.",
        "Sie werden sehen, daß wir ohne die Begriffe, die wir heute entwickelt haben, überhaupt nicht weiterkommen können in der Betrachtung des menschlichen Orga­nismus.",
        "Ich möchte Ihnen, um unsere Gedanken allmählich hinüber-zuführen zu der wesentlichen Natur eines Absonderungsprozesses, zunächst einen anderen Begriff vorführen, der allerdings nur eine entfernte Ähnlichkeit mit dem Absonderungsprozesse hat, der uns aber dazu hinüberführen kann, nämlich den Begriff des Gewahrwer­dens unseres Selbst.",
        "Bedenken Sie einmal, wie Sie im Grunde genom­men doch sagen können, daß es eine Art Gewahrwerden Ihres Selb­stes ist, wenn Sie in einem Raume gehen und sich unvorsichtigerweise an einem harten Gegenstande stoßen.",
        "Dieses Anstoßen ist im Grunde genommen ein Gewahrwerden des eigenen Selbstes.",
        "Es ist ein Gewahrwerden des eigenen Selbstes auf die Art, daß Ihnen das"
      ],
      [
        "Ereignis, das sich durch den Stoß vollzogen hat, zu einem inneren Ereignis geworden ist.",
        "Denn was ist für Sie der Zusammenstoß mit einem fremden Gegenstande?",
        "Er ist die Ursache eines Wehetuns, eines Schmerzes.",
        "Der Schmerzvorgang spielt sich rein in Ihrem Inne­ren ab.",
        "Also ein innerer Vorgang wird dadurch hervorgerufen, daß Sie sich in Berührung bringen mit einem fremden Gegenstand, der Ihnen als Hindernis im Weg liegt.",
        "Das Gewahrwerden dieses Hin­dernisses ist das, was den inneren Prozeß hervorruft, der als Schmerz beim Sichstoßen auftritt.",
        "Im Grunde genommen können Sie sich leicht vorstellen, daß Sie überhaupt nichts anderes zu wissen brau­chen, um das Gewahrwerden Ihres eigenen Seibstes zu erleben, als den inneren Schmerz, der durch das Anstoßen an einen äußeren Gegenstand bewirkt wird.",
        "Denken Sie sich, daß Sie im Finstern an einen Gegenstand stoßen, von dem Sie gar nicht wissen, was er ist, und nehmen Sie an, Sie stoßen sich so stark, daß Sie auch gar nicht darauf schließen können, wie der Gegenstand beschaffen sein könnte, sondern Sie spüren nur die Wirkung des Stoßes als Schmerz.",
        "Sie haben den Stoß in seiner Wirkung so empfunden, daß Sie den Vor­gang in sich selbst erlebten.",
        "Sie erleben gar nichts anderes als einen inneren Vorgang, und das ist das Wesentliche.",
        "Wenn Sie allerdings auch sagen: Ich habe mich an einem äußeren Gegenstand gestoßen -, so ist das mehr oder weniger ein unbewußter Schluß von einem inneren Erlebnis auf ein äußeres Hindernis."
      ],
      [
        "Daraus können Sie sehen, daß der Mensch seines Inneren gewahr wird durch das Finden eines Widerstandes.",
        "Diesen Begriff müssen wir haben: das Gewahrwerden des Selbstes, das Erleben des Inneren, das Ausgefülltsein mit realen Erlebnissen im Inneren durch das Fin­den eines Widerstandes.",
        "Dies ist ein Begriff, den ich, ich möchte sagen, in aller Grobheit entwickelt habe, um von ihm den Übergang machen zu können zu einem anderen Begriffe, dem der Absonderun­gen im menschlichen Organismus.",
        "Denken wir uns einmal, der menschliche Organismus nehme in sich selber in irgendein Organ-system, meinetwegen in den Magen, eine gewisse Stofflichkeit auf und das Organsystem sei so eingerichtet, daß es durch seine Tätigkeit aus diesem Stoffe, der da aufgenommen ist, etwas aussondert, etwas"
      ],
      [
        "gleichsam separiert, wegnimmt von dem Gesamtstoff, so daß durch diese Tätigkeit des Organs der Gesamtstoff zerfällt in einen feineren, gleichsam filtrierten Teil und in einen gröberen Teil, der ausgeson­dert wird.",
        "Es wird also eine Differenzierung des Stoffes vorgenom­men in einen solchen, der in einen weiter brauchbaren, für andere Organe aufzunehmenden Stoff umgewandelt wird und in einen sol­chen, der erst abgesondert und dann ausgeschieden wird."
      ],
      [
        "# Bild s.098"
      ],
      [
        "Hier an dieser Stelle, wo die unbrauchbaren Teile der Stofflichkeit abgestoßen werden gegenüber den brauchbaren Stoffen, hier haben Sie in modifizierter Forin etwas wie ein Sichanstoßen an einen äußeren Gegenstand, wie ich es eben dargestellt habe.",
        "Es stößt der aufgenommene Stoffstrom, indem er an ein Organ herankommt, sozusagen auf einen Widerstand; er kann nicht. so bleiben, wie er ist, er muß sich ändern.",
        "Es wird ihm gleichsam durch das Organ gesagt:"
      ],
      [
        "So kannst du nicht bleiben, wie du bist, du mußt dich ändern. - Es wird also dem Stoff ein Widerstand entgegengestellt, er muß als ein anderer Stoff weiterverbraucht werden, und er muß gewisse Teile abstoßen.",
        "In unserem Innern stellt sich das Organ dem Stofflauf so entgegen, wie sich der äußere Gegenstand uns entgegenstellt, an dem wir uns stoßen.",
        "Solche Widerstände finden sich innerhalb des Gesamtorganismus in den mannigfachsten Organen.",
        "Und erst dadurch, daß überhaupt in unserem Organismus abgesondert wird, erst dadurch, daß wir Absonderungsorgane haben, dadurch ist die Möglichkeit gegeben, daß unser Organismus eine in sich abgeschlos­sene, sich selbst erlebende Wesenheit ist.",
        "Denn Erleben kann sich eine Wesenheit nur dadurch, daß sie auf Widerstand stößt.",
        "So haben"
      ],
      [
        "wir in den Absonderungsprozessen wichtige Prozesse des menschli­chen Lebens, nämlich diejenigen Prozesse, wodurch sich der leben­dige Organismus in sich selber abschließt.",
        "Der Mensch wäre kein in sich abgeschlossenes Wesen, wenn solche Absonderungsprozesse nicht vorhanden wären."
      ],
      [
        "Denken Sie sich einmal, der aufgenommene Nahrungsstrom oder der Sauerstoffstrom würden durch den menschlichen Organismus wie durch einen Schlauch glatt hindurchgehen und es gäbe keinen Widerstand durch die Organe.",
        "Die Folge davon wäre, daß der menschliche Organismus sich nicht in sich selbst erleben könnte, sondern er würde sich nur erleben als angehörig der gesamten großen Welt.",
        "Wir könnten uns ja allerdings auch vorstellen, daß innerhalb des menschlichen Organismus die gröbste Art dieses Widerstandbie­tens eintreten würde, daß der Stoffstrom sich an einer festen Wan­dung stoßen und reflektieren, zurückkehren würde.",
        "Das würde aber das innere Erleben des menschlichen Organismus nicht berühren,"
      ],
      [
        "# Bild s.099"
      ],
      [
        "denn ob der Nahrungsstrom oder der Sauerstoffstrom durch den menschlichen Organismus wie durch einen Schlauch hindurchginge, auf der einen Seite hinein, auf der anderen wieder hinaus, oder ob er reflektiert würde, das würde für das innere Erleben nichts ausma­chen.",
        "Daß das so ist, können Sie schon daraus entnehmen, daß - wie wir schon gesagt haben -, wenn wir es in unserem Nervensystem dazu bringen, daß eine Vorstellung in sich selbst zurückkehrt, wir dann geradezu unser Nervensystem herausheben aus dem Erleben des inneren Organismus.",
        "Es macht also keinen Unterschied, ob völlige"
      ],
      [
        "Reflexion oder bloßes Hindurchgleiten der von außen hineinge­henden Ströme durch den menschlichen Organismus vorliegt.",
        "Was den menschlichen Organismus in sich selbst erlebbar macht, das sind die Absonderungen."
      ],
      [
        "Wenn Sie dasjenige Organ betrachten, welches wir als das Mittel­punktsorgan für den menschlichen Organismus ansehen müssen, das Blutsystem, wenn Sie sehen, wie auf der einen Seite das Blut immer­fort durch Aufnehmen von Sauerstoff sich auffrischt, und wenn Sie auf der anderen Seite das Blutsystem als das Werkzeug des menschli­chen Ich betrachten, so können wir sagen: Wenn das Blut unverän­dert durch den menschlichen Organismus hindurchgehen würde, so könnte es nicht das Organ des menschlichen Ich sein, das im eminen­testen Sinne das Organ ist, welches den Menschen sich innerlich erlebbar macht.",
        "Nur dadurch, daß das Blut in sich selber Verände­rungen durchmacht und als ein anderes wieder zurückkehrt, daß also Absonderungen geschehen von verändertem Blut, nur dadurch ist es möglich, daß der Mensch das Ich nicht nur hat, sondern es auch erleben kann mit Hilfe seines sinnlich-physischen Werkzeuges, des Blutes."
      ],
      [
        "Daraus hat sich uns nun dieser Begriff der Absonderung ergeben.",
        "Und jetzt werden wir uns zu fragen haben: Wie steht es nun mit jener Absonderung, welche wir vorhin bezeichnet haben als der äußersten Peripherie des menschlichen Organismus angehörig? - Es wird uns ja unschwer sein, uns vorzustellen, wie der Gesamtorganismus des Menschen wirken muß, damit diese Absonderung an der Peripherie geschehen kann.",
        "Dazu ist es notwendig, daß den gesamten Strömun­gen des menschlichen Organismus entgegengestellt werde ein Organ, welches in Zusammenhang steht gerade mit diesem umfänglichsten Absonderungsprozeß.",
        "Und dieses Organ, das ja, wie Sie sich leicht denken können, die Haut ist, mit allem, was zu ihr gehört im umfänglichsten Sinne, das ist zugleich dasjenige, was schon für den unmittelbaren äußeren Anblick als das Wesentliche der menschlichen Gestalt, der menschlichen Form sich darbietet.",
        "Wenn wir uns also vorstellen, daß der menschliche Organismus, der sich selbst erleben kann an seinem äußeren Umfange, dies nur dadurch kann, daß er das"
      ],
      [
        "Organ der Haut seinen gesamten Strömungen entgegenstellt, so müs­sen wir in der eigenartigen Formung der Haut einen der Ausdrücke sehen für die innersten Kräfte des menschlichen Organismus."
      ],
      [
        "Wir werden uns nun zu fragen haben: Wie haben wir uns denn dieses Hautorgan zu denken?",
        "Wie haben wir uns die Haut mit allem, was dazugehört, zu denken?",
        "Wir werden schon sehen, was im einzel­nen dazugehört, wir wollen es aber heute nur im großen und ganzen charakterisieren."
      ],
      [
        "Da müssen wir uns zunächst darüber klar sein, daß in dem, was zu unserem bewußten Erleben gehört, wovon wir eine Erkenntnis haben können durch irgendeine Selbstbeobachtung, jene Gestaltung nicht einbegriffen ist, welche in der Formung unserer Haut zum Ausdruck kommt.",
        "Selbst wenn wir in begrenztem Umfange mittätig sind an der Gestaltung unserer äußeren Körper-oberfläche, so ist sie doch etwas, das sich der unmittelbaren Willkür in vollkommenster Weise entzieht."
      ],
      [
        "Nur in bezug auf die Beweglich­keit unserer Haut, in bezug auf Mienenspiel, Gesten und so weiter, haben wir ja einen Einfluß, der noch an das heranreicht, was wir bewußte Tätigkeit nennen können; aber auf die Gestalt, auf die Form unserer Körperoberfläche haben wir keinen Einfluß mehr.",
        "Es muß freilich zugegeben werden, daß der Mensch zwischen Geburt und Tod einen gewissen Einfluß auf seine äußere Leibesform in engeren Grenzen hat."
      ],
      [
        "Davon kann sich jeder überzeugen, der einen Menschen kennengelernt hat in einem bestimmten Lebensalter und ihn viel­leicht nach zehn oder zwanzig Jahren wiedersieht, insbesondere wenn dieser Mensch in diesen Jahren durchgegangen ist durch tiefere innere Erlebnisse, namentlich durch Erkenntniserlebnisse, die nicht Gegenstand der äußeren Wissenschaft sind, sondern durch solche, die «Blut kosten», die zusammenhängen mit unserem ganzen Lebensschicksal.",
        "Dann sehen wir allerdings innerhalb enger Gren­zen, wie die Physiognomie sich ändert, wie also der Mensch inner-halb dieser Grenzen einen Einfluß hat auf die Gestaltung seines Leibes."
      ],
      [
        "Aber er hat ihn nur in geringem Maße, und das wird jeder zugeben müssen; denn das Hauptsächlichste in der menschlichen Gestalt ist durchaus nicht in unsere Willkür gegeben und nicht durch unser Bewußtsein bestimmt.",
        "Dennoch müssen wir sagen: Die ganze"
      ],
      [
        "menschliche Gestalt ist angepaßt der menschlichen Wesenheit; und wer auf die Dinge eingeht, wird sich niemals vorstellen können, daß dasjenige, was wir den ganzen Umfang der menschlichen Fähigkeiten nennen, sich entwickeln könnte in einem Wesen von einer anderen Gestalt, als es die heutige Menschengestalt ist.",
        "Alles, was an Fähigkei­ten im Menschen ist, hängt zusammen mit dieser Menschengestalt."
      ],
      [
        "Denken Sie sich nur einmal, daß etwa das Stirnbein in einer irgendwie anderen Lage wäre zu dem Gesamtorganismus, als es ist, so würde diese Gestaltänderung ganz andere Fähigkeiten und Kräfte im Men­schen voraussetzen.",
        "Darüber könnten ja Studien gemacht werden, indem man sich klarmacht, wie andere Fähigkeiten vorhanden wären bei Menschen mit verschiedener äußerer Gestaltung des Kopfes, des Schädelbaus und so weiter."
      ],
      [
        "So müssen wir uns einen Begriff verschaf­fen von dem Angepaßtsein der menschlichen Gestalt an die gesamte innere menschliche Wesenheit, ja, von einem völligen Sichentspre­chen der äußeren Gestalt und der inneren Wesenheit des Menschen.",
        "Was in den Kräften dieser Anpassung liegt, hat nichts zu tun mit dem, was in die eigene, vom Bewußtsein umspannte Tätigkeit des Menschen hereingehört."
      ],
      [
        "Da aber die Gestalt des Menschen zusam­menhängt mit seiner geistigen Betätigung und auch mit seinem seeli­schen Leben, so können Sie es sich leicht vorstellen, daß in den Kräften, welche die physische Gestalt des Menschen zustande brin­gen, solche Kräfte liegen, die gleichsam von einer anderen Seite entgegenkommen denjenigen Kräften, die der Mensch in sich selbst entwickelt.",
        "Kräfte der Intelligenz, Gefühlskräfte, Gemütskräfte und so weiter, die kann der Mensch nur entwickeln in der physischen Welt unter der Voraussetzung seiner besonderen Gestalt."
      ],
      [
        "Diese Gestalt muß ihm gegeben sein.",
        "Er muß also diese Gestalt für seine Fähigkeiten zubereitet erhalten - wenn ich mich so ausdrücken darf -von Kräften entsprechend ähnlicher Art wie die, die von der anderen Seite her diese Gestalt erst aufbauen, damit sie dann zu dem gebraucht werden kann, wozu sie verwendet werden soll."
      ],
      [
        "Es ist unschwer, sich diesen Begriff zu verschaffen, denn man braucht nur daran zu denken, daß eine Maschine, die wir zu einer Tätigkeit verwenden wollen, für diese Tätigkeit intelligent und zweckmäßig"
      ],
      [
        "eingerichtet sein muß.",
        "Damit eine solche Maschine zustande komme, ist es notwendig, daß zuerst ähnliche Verrichtungen vollführt wer­den, wie sie dann von der Maschine ausgeführt werden sollen, und danach die Teile der Maschine herzustellen und zusammenzuglie­dern, welche der Maschine ihre Form geben.",
        "Wenn wir eine fertige Maschine vor uns haben, so ist sie für uns ganz mechanisch erklärbar, wenn wir ihre Wirksamkeit sehen und verstehen.",
        "Als denkende Beobachter werden wir uns aber fragen: Wer ist es, der sie gebaut hat? - Denn ihre Zusammensetzung weist auf eine zielbewußte gei­stige Tätigkeit hin, welche diese Maschine zu einem bestimmten Zwecke hergestellt hat.",
        "Diese geistige Tätigkeit braucht nicht mehr da zu sein, wenn wir die Maschine mechanisch erklären wollen, aber sie steht hinter der Maschine, sie hat sie erst zustande gebracht."
      ],
      [
        "Ebenso können wir sagen: Alles, was an Formsystemen in der Gestaltung unseres Organismus liegt, das ist uns in erster Linie gegeben, damit wir unsere Fähigkeiten und Kräfte als Menschen entwickeln.",
        "Aber es muß hinter dieser Gestaltung des Menschen gestaltunggebende, formgebende Kräfte geben, die wir ebensowenig in der fertigen Gestalt finden, wie wir in der Maschine den Maschi­nenbauer finden."
      ],
      [
        "Mit dieser Idee wird Ihnen zugleich etwas anderes völlig einleuch­tend sein.",
        "Ein materialistischer Denker könnte sagen: Wozu braucht man intelligente Kräfte und bewußt schaffende Wesenheiten anzu­nehmen hinter unserer physischen Welt?",
        "Wir können ja die physi­sche Welt aus sich selbst, aus ihren eigenen Gesetzen erklären.",
        "Eine Uhr, eine Maschine kann aus ihren eigenen Gesetzen heraus erklärt werden. - Hier stehen wir an einem Punkte, wo hüben und drüben die schlimmsten Fehler gemacht werden, sowohl bei solchen, die auf dem Boden einer spirituellen Weltanschauung stehen, wie auch auf der Seite der Materialisten.",
        "Wenn zum Beispiel von einer geisteswis­senschaftlichen Weltanschauung bestritten würde, daß der menschli­che Organismus, wie er seiner Form nach vorliegt, nicht rein mecha­nisch oder mechanistisch durch seine eigenen Gesetze erklärbar wäre, so würde das selbstverständlich zu weit gehen und ganz unberechtigt sein.",
        "Der menschliche Organismus ist ganz und gar aus seinen eigenen"
      ],
      [
        "Gesetzen heraus erklärbar, wie die Uhr auch.",
        "Aber daraus, daß die Uhr aus ihren eigenen Gesetzen erklärbar ist, folgt nicht, daß hinter der Uhr nicht der Erfinder der Uhr stand, der Uhrmacher und seine geistige Tätigkeit.",
        "Dieser Einwand, der von materialistischer Seite aus gemacht werden kann, erledigt sich dadurch.",
        "Aber der Geistesforscher muß auch zugeben, daß der menschliche Organis­mus, so wie er vor uns steht, aus seinen eigenen Gesetzen erklärt werden kann.",
        "Aber wenn wir wirklich geisteswissenschaftlich den­ken, haben wir hinter der Gesamtgestaltung des menschlichen Or­ganismus zu suchen die gestaltenden Wesenheiten, dasjenige also, was der gesamten Form der menschlichen Wesenheit zugrundeliegt.",
        "Wenn wir uns nun einen Begriff davon bilden wollen, wie überhaupt die menschliche Form zustande kommt, so müssen wir uns denken, daß sie auf der einen Seite dadurch bewirkt wird, daß die formgeben­den Kräfte sich entfalten und daß sie den Menschen dadurch auf­bauen, daß sie sich an den Grenzen der menschlichen Form selbst abschließen.",
        "Wir haben in der Hautbildung das am reinsten gegeben, was das räumliche Sichabschließen der formgebenden Kräfte im Menschen bedeutet.",
        "Wenn wir das schematisch zeichnen, können wir uns denken, daß die formgebenden Kräfte zur Peripherie dahinflie­ßen und sich da abschließen in der äußeren Form, die in der Linie A-B nur angedeutet werden soll."
      ],
      [
        "# Bild s. 104"
      ],
      [
        "Wir werden nun sehen, wie wir diesen Begriff wiederum brauchen, um alles das erkennen zu können, was innerhalb der Haut geschieht.",
        "Weiter aber werden wir uns darüber klar werden müssen, daß wir"
      ],
      [
        "nun nicht bloß in der menschlichen Haut solche Abschlüsse vor uns haben, sondern daß wir auch innerhalb des menschlichen Organis­mus selber solches Abschließen der von außen wirkenden Tätigkeit und Wesenhaftigkeit finden.",
        "Sie brauchen sich nur zu überlegen, was bisher gesagt worden ist, dann werden Sie darauf kommen, daß wir auch im Inneren des Menschen solche sich abschließenden Tätigkei­ten vor uns haben, an denen wir ebenso unbeteiligt sind wie an unserer Oberflächengestaltung, und das sind gerade diejenigen Betä­tigungen, die zustande kommen in den Organen Leber, Galle, Milz und so weiter.",
        "Da wird das aufgehalten, was durch die Kräfte, die in den Nahrungsmitteln sitzen, in den Organismus einströmt, dem wird etwas entgegengeschoben, wird ein Widerstand entgegengesetzt, das heißt, es wird in diesen Organen die äußere, die eigene Regsamkeit der Stoffe umgeändert.",
        "Während also bei den formgebenden Kräften"
      ],
      [
        "# Bild s. 105"
      ],
      [
        "die Sache so ist, daß wir uns diese formenden Kräfte wirksam zu denken haben bis zur Haut hin und außerhalb der Haut nichts mehr von formgebenden Kräften haben, müssen wir uns vorstellen, daß bei denjenigen Kräften, die mit dem Nahrungs- oder Luftstrom nach unserem Inneren gehen, nicht ein vollständiges Abschließen dessen vorhanden ist, was als Strömungen von außen eindringt, sondern es tritt da eine Umgestaltung ein.",
        "Diese Organe müssen wir uns so denken, daß sie nicht, wie es bei der Haut ist, sich abschließen, so daß außerhalb nichts mehr ist, sondern so, daß die Regsamkeit der Stoffe"
      ],
      [
        "umgeändert wird durch sie derart, daß der Nahrungsstrom, der von der Seite dieser Organe her aufgenommen ist (siehe Zeichnung, a), in einer anderen Weise weitergeleitet wird (b), nachdem ihm ein Wider­stand entgegengesetzt worden ist.",
        "Hier haben wir es also mit einer Umänderung zu tun, und das betrifft vor allem diejenigen Organe, welche wir als ein inneres Weltsystem des Menschen bezeichnet haben.",
        "Die ändern die äußere Regsamkeit der Stoffe um.",
        "Es sind Kräfte, die wir im Gegensatz zu den Formkräften, die den gesamten Organismus bilden, Bewegungskräfte nennen können.",
        "In unserem inneren Weltsystem werden diese Kräfte, welche die innere Regsam­keit der Nahrungsstoffe umgestalten, dann Bewegung, so daß wir hier von Bewegungskräften in den Organen sprechen können."
      ],
      [
        "Wir sind jetzt so weit vorgeschritten in den Betrachtungen des menschlichen Organismus, daß wir sagen können: In den menschli­chen Organismus wirken von außen Kräfte herein, deren Tätigkeit wir mit unserem Bewußtsein nicht wahrnehmen.",
        "Das alles geht unterhalb unseres Bewußtseinshorizontes vor sich, was wir da als Tätigkeit ausführen; niemand kann im normalen Bewußtsein die Tätigkeit seiner Leber, Galle, Milz und so weiter beobachten.",
        "Nun entsteht die Frage: Wodurch werden wir denn verhindert, etwas zu wissen von den Form- und Bewegungskräften, die sich in unseren inneren Organen abspielen, da doch unser Seelenleben dem Organis­mus eingegliedert ist?",
        "Da gehen ja in unserem Innern gewaltige Tätigkeiten vor sich.",
        "Woher kommt es, daß wir davon nichts wissen?"
      ],
      [
        "Nun, genau ebenso wie unser Gehirn-Rückenmark-Nervensystem dazu bestimmt ist, die äußeren Eindrücke, die wir durch unsere Sinne erhalten, bis zum Blute hinzuleiten, das heißt, die Impressionen von äußeren Vorgängen in unser Blut, in das Werkzeug des Ich, aufzu­nehmen, ebenso wie also das Gehirn-Rückenmark-Nervensystem dazu bestimmt ist, im normalen Bewußtsein dem Ich zu dienen, gerade so ist das sympathische Nervensystem, das sich mit seinen Knoten und Verzweigungen dem inneren Weltsystem gleichsam vor-lagert, dazu ausersehen, die Vorgänge, die sich im Innern des Orga­nismus abspielen, nicht an das Blut, das Werkzeug des Ich, heran-zulassen, sondern sie vom Blut zurückzuhalten."
      ],
      [
        "# Bild s. 107"
      ],
      [
        "So sehen Sie, daß das sympathische Nervensystem eine entgegen­gesetzte Aufgabe hat wie das Gehirn-Rückenmark-Nervensystem, und hier haben wir eine Erklärung für den Unterschied in Bau und Beschaffenheit dieser beiden Systeme.",
        "Während das Gehirn-Rücken-mark-Nervensystem sich anstrengen muß, um möglichst gut die äußeren Eindrücke zum Blut überzuleiten, muß durch das entgegen­gesetzt wirkende sympathische Nervensystem vom Blut - als dem Werkzeug des Ich - fortwährend zurückgestaut werden die Eigen-regsamkeit der aufgenommenen Stoffe.",
        "Wenn wir den Verdauungs­prozeß betrachten, so haben wir zuerst das Aufnehmen der äußeren Nahrungsstoffe, dann das Zurückstauen der Eigenregsamkeit der Nahrungsstoffe und dann die Umwandlung dieser Regsamkeiten durch das innere Weltsystem des Menschen.",
        "Damit wir nicht fort-während, wie wir so dastehen in der Welt, alles das wahrnehmen, was in unseren inneren Organen bewirkt wird, muß der ganze Strom der Vorgänge durch das sympathische Nervensystem zurückgestaut wer­den vom Blut, geradeso wie durch das Gehirn-Rückenmark-Nerven­system das zum Blute hingetragen wird, was von außen aufgenom­men wird.",
        "Da haben Sie die Aufgabe des sympathischen Nerven­systems, unsere inneren Vorgänge in uns zu halten, sie nicht bis zum Blut, dem Werkzeug des Ich, hinaufdringen zu lassen, um das Ein-treten dieser inneren Vorgänge in das Ichbewußtsein zu verhindern."
      ],
      [
        "Ich habe schon gestern darauf hingewiesen, daß das Außenleben und das Innenleben des Menschen, wie es sich im Ätherleibe auslebt,"
      ],
      [
        "in einem Gegensatz zueinander stehen und daß dieser Gegensatz von Außenleben und Innenleben in Spannungen zum Ausdruck kommt, die, wie wir gesehen haben, am stärksten werden in den Organen des Gehirnes, die wir als Zirbeldrüse und Gehirnanhang bezeichnen."
      ],
      [
        "Wenn Sie nun die heutige und die gestrige Ausführung zusammen­nehmen, so werden Sie sich leicht denken können, daß alles, was von außen hereinströmt, um in möglichst engen Kontakt mit der Blutzir­kulation zu treten, darnach strebt, sich zu vereinigen mit seinem Gegensatze, mit dem, was von innen kommt und zurückgehalten wird durch das sympathische Nervensystem.",
        "In der Zirbeldrüse haben wir die Stelle, wo das durch das Gehirn-Rückenmark-Nerven­system an das Blut von außen Herangebrachte sich vereinigen will mit dem, was von der anderen Seite kommt, und der Hirnanhang ist gleichsam der letzte Vorposten, um das nicht heranzulassen an das Blut, was menschliches Innenleben ist."
      ],
      [
        "Es stehen sich an dieser Stelle im Gehirn zwei wichtige Organe gegenüber.",
        "Das gesamte innere Erleben bleibt unter unserem Bewußtsein; es würde uns ja auch in einer furchtbaren Weise stören, wenn wir bewußt mitmachen wür­den unsere ganzen Ernährungsprozesse; das wird zurückgehalten durch das sympathische Nervensystem."
      ],
      [
        "Nur wenn dieses gegensei­tige Verhältnis zwischen den beiden Nervensystemen, wie es sich ausdrückt in dem Spannungsverhältnis zwischen Zirbeldrüse und Hirnanhang, nicht in Ordnung ist, stellt sich das heraus, was wir nennen können ein Durchschimmern der einen Seite in die andere hinein, ein Gestörtwerden der einen Seite von der anderen Seite her.",
        "Das tritt zum Beispiel schon dann ein, wenn eine unregelmäßige Tätigkeit unserer Verdauungsorgane uns in unbehaglichen Gefühlen zum Bewußtsein kommt."
      ],
      [
        "Da haben wir ein - allerdings noch sehr unbestimmtes - Hereinstrahlen des sonst unbewußten menschlichen Innenlebens in das Bewußtsein, das sich aber auf diesem Wege bedeutend umgewandelt hat, also im Bewußtsein nicht so erscheint, wie es sich abgespielt hat.",
        "Oder wir haben in besonderen Affekten, Zorn, Wut, Schrecken und dergleichen, die ihren Ursprung im Bewußtsein haben, ein besonders starkes Hereinstrahlen von der Seite des inneren menschlichen Organismus; da haben wir den Fall,"
      ],
      [
        "daß Affekte, besondere innere Erregungen der Seele, die Verdauung, das Atmungssystem und dadurch auch die Blutzirkulation und alles, was unterhalb des Bewußtseins liegt, in besonders schädigender Weise beeinflussen können.",
        "So können diese zwei Seiten der mensch­lichen Natur dennoch aufeinander wirken."
      ],
      [
        "So stehen wir als Menschen in der Tat als eine Zweiheit in der Welt, und wir haben heute diese Zweiheit gesehen: Auf der einen Seite bewußtes Erleben der Außenwelt durch das Gehirn-Rücken-mark-Nervensystem, welches die äußeren Eindrücke bis zum Blut, dem Werkzeuge des Ich, bringt; auf der anderen Seite unbewußtes Erleben der Innenwelt, unbewußt, weil es durch das sympathische Nervensystem vom Blute zurückgehalten wird.",
        "Diese beiden Gegen­sätze stehen sich auf der ganzen Linie gegenüber.",
        "Aber wir finden ihren besonderen Ausdruck in der Spannung zwischen diesen beiden Organen, von denen wir gesprochen haben: der Zirbeldrüse und dem Hirnanhang."
      ],
      [
        "Von diesem Punkte aus wollen wir das nächste Mal unsere Betrachtungen fortsetzen."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "SECHSTER VORTRAG Prag, 26. März 1911",
    "paragraphs": [
      "Aus den letzten Vorträgen konnten wir ersehen, daß der Mensch als physische Organisation sich gewissermaßen durch seine Haut nach außen abgrenzt. Wenn wir den menschlichen Organismus ganz in dem Sinne auffassen, wie wir das nach den bisherigen Erörterungen tun müssen, dann ist es notwendig, daß wir uns sagen: Es ist der menschliche Organismus mit seinen verschiedenen Kraftsystemen selber, der sich in der Haut nach außen einen bestimmten Abschluß gibt.",
      "Mit anderen Worten: Uns muß klar sein, daß im menschlichen Organismus ein solches Gesamtsystem von Kräften ist, welche sich durch ihr Zusammenwirken so bestimmen, daß sie sich genau den Formumriß geben, der durch die Haut als äußere Begrenzung der Menschengestalt zum Vorschein kommt. So müssen wir eigentlich sagen, daß für den Lebensprozeß des Menschen die interessante Tatsache vorliegt, daß uns in der äußeren Formbegrenzung ein gleichsam bildhafter Ausdruck gegeben ist für die gesamte Wirksam­keit der Kraftsysteme im Organismus.",
      "Wenn nun in der Haut selber ein solcher Ausdruck des Organismus gegeben werden soll, so müs­sen wir voraussetzen, daß innerhalb der Haut eigentlich in einer gewissen Weise der ganze Mensch irgendwie zu finden sein muß. Denn, wenn der Mensch, so wie er ist, so gebildet sein soll, daß die äußere Haut als Formbegrenzung das ausdrückt, was er ist, so muß in der Haut alles das gefunden werden können, was im Menschen zur Gesamtorganisation gehört.",
      "Und in der Tat, wenn wir auf dasjenige eingehen, was zur Gesamtorganisation des Menschen gehört, so kön­nen wir finden, wie sehr eigentlich dasjenige innerhalb der Haut vorhanden ist, was in den Kraftsystemen des Gesamtorganismus veranlagt ist.",
      "Da haben wir zunächst gesehen, daß der Gesamtmensch, wie er uns als Erdenmensch entgegentritt, das Werkzeug seines Ich in sei­nem Blutsystem hat, so daß der Mensch dadurch Mensch ist, daß er in sich ein Ich birgt, und dieses Ich sich bis zum physischen System",
      "herunter einen Ausdruck, ein Werkzeug schaffen kann im Blut. Ist nun unsere Körperoberfläche, unsere Formbegrenzung ein wesentli­ches Glied unserer Gesamtorganisation, so müssen wir sagen: Diese Gesamtorganisation muß durch das Blut bis in die Haut hinein wirken, damit in der Haut ein Ausdruck der ganzen menschlichen Wesenheit, insofern sie physisch ist, vorhanden sein kann.",
      "Betrachten wir die Haut, wie sie sich, aus mehreren Schichten bestehend, über die ganze Oberfläche des Leibes spannt, so finden wir, daß in der Tat in diese Haut feine Blutgefäße hineingehen. Durch diese feinen Blut­gefäße kann das Ich seine Kräfte senden und sich bis in die Haut hinein einen Ausdruck der menschlichen Wesenheit schaffen.",
      "Wir wissen ferner, daß für alles, was wir als Bewußtsein zu bezeichnen haben, das Nervensystem das physische Werkzeug ist. Wenn nun die Körperoberflächenbegrenzung ein Ausdruck der Gesamtorganisa­tion des Menschen ist, so müssen auch die Nerven bis in die Haut hinein sich erstrecken, damit das menschliche Bewußtsein bis in dieses Organ gehen kann.",
      "Wir sehen daher neben den feinen Blut­gefäßen innerhalb der Hautschichten die mannigfaltigsten Nerven­endungen verlaufen, die man ja gewöhnlich - obwohl nicht mit vol­lem Recht - die Tastkörperchen nennt, weil man annimmt, daß der Mensch mit Hilfe dieser Tastkörperchen die äußere Welt durch den Tastsinn wahrnimmt, so wie er durch Augen und Ohren Licht und Schall wahrnimmt. Es ist das aber nicht eigentlich der Fall.",
      "Genauer betrachtet ist dieser Tastsinn der Ausdruck verschiedener Sinnestä­tigkeiten, zum Beispiel Wärmesinn und andere. Wir werden noch sehen, wie die Sache liegt. Wir finden also in der Haut dasjenige, was Ausdruck oder körperliches Organ des menschlichen Ich ist: das Blut.",
      "Wir sehen aber auch dasjenige, was Ausdruck des menschlichen Bewußtseins ist: das Nervensystem, das seine Ausläufer bis in die Haut hineinerstreckt.",
      "Nun müssen wir uns umsehen nach dem Ausdruck dessen, was wir überhaupt betrachten können als das wesentliche Instrument des Lebensprozesses. Wir haben schon im letzten Vortrage auf dieses Instrument des Lebensprozesses aufmerksam gemacht bei der Besprechung der Absonderung. In der Absonderung, bei der, wie wir",
      "gesehen haben, gleichsam eine Art von Hemmnis auftritt, haben wir insofern den Ausdruck des Lebensprozesses zu sehen, als ein leben­diges Wesen, das in der Welt existieren will, notwendig hat, sich nach außen abzuschließen. Das kann nur dadurch geschehen, daß es in sich selber ein Hemmnis erlebt. Dieses Erleben eines Hemmnisses in sich selber wird vermittelt durch Absonderungsorgane, die man im weite­sten Umfange als Drüsen bezeichnen kann. Drüsen sind Absonde­rungsorgane, und das Hemmnis tritt dadurch ein, daß sie den an sie herandrängenden Nahrungsstoffen sozusagen inneren Widerstand entgegensetzen. Wir müssen also voraussetzen, daß solche Abson­derungsorgane, ebenso wie wir sie sonst im Organismus verteilt ha­ben, auch der Haut angehören. Und sie gehören der Haut an; denn wir finden auch in der Haut Absonderungsorgane, Drüsen der ver­schiedensten Art, Schweißdrüsen, Talgdrüsen, welche dieses Abson­derungsgeschäft - also einen Lebensprozeß - innerhalb der Haut betreiben.",
      "Und wenn wir endlich nach dem fragen, was unterhalb des Lebensprozesses liegt, so werden wir da dasjenige finden, was wir nennen können den reinen Stoffprozeß, das Überleiten der Stoffe von einem Organ zum anderen. Ich möchte Sie jetzt an dieser Stelle bitten, genau zu unterscheiden zwischen einem solchen Absonde­rungsprozeß, der ein inneres Hemmnis schafft, der den Lebenspro­zessen angehört, und denjenigen Prozessen, die rein stoffliche Umla­gerungen bewirken, also bloßes Transportieren der Stoffe von einem Orte zum anderen. Denn das ist nicht dasselbe. Für eine materialisti­sche Anschauung könnte es so aussehen, aber für eine lebensvolle Erfassung der Wirklichkeit ist es nicht so. Wir haben es im menschli­chen Organismus nicht bloß zu tun mit einer bloßen Transportierung der Stoffe. Allerdings findet überall ein Hinleiten der Stoffe, der Ernährungsprodukte, zu den einzelnen Organen statt. Aber in dem Augenblick, wo die Nahrungsstoffe aufgenommen werden, haben wir es mit einem Lebensprozesse zu tun, mit Absonderungsprozes­sen, die zugleich innere Hemmnisse schaffen. Es ist notwendig, dies zu unterscheiden von dem Prozeß der bloßen Stoffumlagerung. Wir steigen von dem Lebensprozeß hinunter zu den Prozessen des eigentlichen",
      "Physischen, wenn wir sagen, es sieht sich so an, wie wenn die aufgenommenen Nahrungsstoffe in die verschiedensten Teile des physischen Leibes transportiert würden. Es ist aber eine lebendige Tätigkeit, gleichsam ein Sichgewahrwerden des Organismus in sei­nem eigenen Innern, in dem durch die Absonderungsorgane innere Hemmnisse geschaffen werden.",
      "Mit den Lebensvorgängen findet zugleich ein Transport der Stoffe statt, und das ist in der Haut ebenso wie in den anderen Teilen des Organismus. Durch die Haut werden die Abfälle der Nahrungsstoffe ausgeschieden, abgesondert, nach außen getragen durch den Prozeß der Schweißabsonderung, des Schwitzens, so daß auch hier ein rein physisches Transportieren der Stoffe vorhanden ist.",
      "Damit haben wir im wesentlichen charakterisiert, daß in dem äußeren Organ der Haut sich finden sowohl das Blutsystem als Ausdruck des Ich als auch das Nervensystem als Ausdruck des Bewußtseins. Ich will jetzt nach und nach dazu überleiten, daß wir ein Recht haben, alle Bewußtseinserscheinungen zusammenzufassen mit dem Ausdruck «Astralleib», daß wir also das Nervensystem bezeichnen können als einen Ausdruck des Astralleibes, das Drüsen­system als einen Ausdruck des Äther- oder Lebensleibes und daß wir den eigentlichen Ernährungs-Umlagerungsprozeß bezeichnen können als einen Ausdruck des physischen Leibes. Insofern sind alle einzelnen Gliederungen der menschlichen Organisation in dem Hautsystem, durch das sich der Mensch nach außen abschließt, tat­sächlich vorhanden. Nun müssen wir allerdings berücksichtigen, daß alle Gliederungen der menschlichen Organisation, Blutsystem, Ner­vensystem, Ernährungssystem und so weiter, in ihren gegenseitigen Beziehungen ein Ganzes ausmachen und daß wir gleichsam, indem wir diese vier Systeme der menschlichen Organisation betrachten und sie am physischen Leibe uns vor Augen führen, den menschli­chen Organismus von zwei Seiten vor uns haben. Wir haben ihn tatsächlich von zwei Seiten, und zwar zunächst so, daß wir sagen können: Der menschliche Organismus hat innerhalb des Erdenda­seins nur einen Sinn, wenn er als Gesamtorganismus das Werkzeug unseres Ich ist. Das kann er aber nur sein, wenn das nächste Werkzeug,",
      "dessen sich das menschliche Ich bedienen kann, das Blut­system, in ihm vorhanden ist. Nun ist aber das Blutsystem nur möglich, wenn ihm die anderen Systeme in ihrer Bildung vorangehen. Das Blut ist nicht nur im Sinne des Dichterwortes «ein ganz besonderer Saft», sondern es ist leicht einzusehen, daß es so, wie es ist, überhaupt nicht existieren kann, ohne daß es sich einlagert dem ganzen übrigen Organismus des Menschen; es ist nötig, daß es in seiner Existenz vorbereitet ist durch den ganzen übrigen menschlichen Organismus. Das Blut, so wie der Mensch es hat, kann nirgends vorkommen als im menschlichen Organismus. Wir dürfen durchaus nicht das, was für das Blut des Menschen gesagt worden ist, ohne weiteres auf ein anderes Lebewesen der Erde übertragen. Ich werde vielleicht später noch Gelegenheit haben, über das Verhältnis von menschlichem Blut zu tierischem Blut zu sprechen. Das wird eine sehr wichtige Betrach­tung sein, weil die äußere Wissenschaft auf diesen Unterschied wenig Rücksicht nimmt. Heute wollen wir nur hinweisen auf das Blut als Ausdruck des menschlichen Ich. Ist einmal der ganze übrige Orga­nismus des Menschen aufgebaut, so ist er erst fähig, Blut zu tragen, den Blutkreislauf in sich aufzunehmen, erst dann kann er in sich das Instrument haben, welches als Werkzeug unserem Ich dient. Dazu muß aber der Gesamtorganismus des Menschen erst aufgebaut sein.",
      "Sie wissen, daß es auch andere Wesenheiten neben dem Menschen auf der Erde gibt, die in einer gewissen Verwandtschaft mit dem Menschen augenscheinlich stehen, die aber nicht in der Lage sind, ein menschliches Ich zum Ausdruck zu bringen. Bei diesen ist offenbar dasjenige, was in den entsprechenden Systemen der menschlichen Anlage ähnlich sieht, doch anders aufgebaut als beim Menschen. In allen diesen Systemen, die dem Blutsystem vorausgehen, muß schon die Möglichkeit veranlagt sein, das Blut aufnehmen zu können. Das heißt, wir müssen erst ein solches Nervensystem haben, welches ein Blutsystem im Sinne des menschlichen Blutsystems aufnehmen kann; wir mussen ein solches Drüsensystem haben und ebenso ein solches Ernährungssystem, die vorgebildet sein müssen für die Aufnahme eines menschlichen Blutsystems. Das bedeutet, es muß zum Beispiel schon auf der Seite des menschlichen Organismus, die wir bezeichnet",
      "haben als den eigentlichen Ausdruck des physischen Leibes des Men­schen, beim Ernährungssystem, das Ich veranlagt sein. Es muß gleichsam der Prozeß der Bildung des Ernährungssystems durch den Organismus so gelenkt und geleitet sein, daß zuletzt das Blut sich in den richtigen Bahnen bewegen kann. Was heißt das?",
      "Das bedeutet, daß der Blutkreislauf in seiner Gestaltung, in der ganzen Art seiner Regsamkeit, bedingt ist durch die Ich-Wesenheit des Menschen. Denken wir uns den Blutkreislauf in dieser ovalen Linie völlig schematisch angedeutet (siehe Zeichnung), so müssen wir",
      "# Bild s. 115",
      "sagen, es muß ja der Blutkreislauf von dem übrigen Organismus aufgenommen werden, das heißt, alle Organsysteme müssen so ange­ordnet sein, daß der Blutkreislauf sich eingliedern kann. Wir könnten das ganze Gewebe unserer Blutgefäße - sei es am Kopfe oder an einem anderen Teil unseres Organismus - nicht so haben, wie es ist, wenn nicht überall dahin, wo das Blut kreisen soll, die entsprechen­den Dinge geleitet werden, die da sein müssen. Das heißt, die Kraft­systeme müssen im menschlichen Organismus, vom Ernährungs­system angefangen, so wirken, daß sie an die betreffenden Orte das notwendige Ernährungsmaterial hintragen und es zugleich so gestal­ten, so vorbilden, daß an diesen Orten das Blut genau die Form seines",
      "Verlaufs einhalten kann, deren es bedarf, um ein Ausdruck des Ich werden zu können. Es muß daher in alle Impulse unseres Ernäh­rungsapparates, also des untersten Systems unseres Organismus, schon dasjenige hineingelegt sein, was den Menschen zu einem Ich-Wesen macht. Die ganze Form, die der Mensch zuletzt in seiner physischen Vollendung zeigt, muß schon hineingegliedert sein in die Organsysteme bis in das hinein, was die verschiedenen Ernährungs­prozesse des Menschen sind. Da sehen wir von dem Blute hinunter in die den Blutkreislauf vorbereitenden Organsysteme zu den Prozes­sen, die weitab von unserem Ich im Dunkel unseres Organismus sich abspielen. Während das Blut der Ausdruck unserer Ich-Tätigkeit ist, also Ausdruck des Bewußtesten ist, was wir haben, sind wir nicht fähig, hinunterzusehen in die unbekannten Tiefen des physischen Leibes. Wir wissen nicht, wie die Stoffe hingeleitet, hingetragen werden zu den einzelnen Orten unseres Organismus, wo sie verwen­det werden müssen, um ihn aufzubauen und zu formen, damit er Werkzeug unseres Ich sein kann. Das zeigt uns, daß schon von Anfang an bei der Ernährung alle Gesetze im Organismus des Men­schen liegen, die zuletzt zur Gestaltung des Blutkreislaufes führen.",
      "Das Blut als solches stellt sich uns nun dar als das beweglichste, als das regsamste aller unserer Systeme. Und wir wissen ja, wenn wir auch nur in geringem Maße irgendwie eingreifen in die Blutbahn, so nimmt das Blut sogleich andere Wege. Wir brauchen uns nur an irgendeiner Stelle zu stechen, so nimmt das Blut gleich einen anderen Weg als sonst. Das ist unendlich wichtig zu berücksichtigen, denn daraus können wir ersehen, daß das Blut das bestimmbarste Element im menschlichen Leibe ist. Es hat seine gute Unterlage an den ande­ren Organsystemen, aber es ist zugleich das aller bestimmbarste, das die wenigste innere Stetigkeit hat. Das Blut kann ungeheuer bestimmt werden durch die Erlebnisse des bewußten Ich. Ich will dabei nicht eingehen auf die phantastischen Theorien, die von seiten der äußeren Wissenschaft über das Erröten oder Erbleichen bei Scham- oder Angstgefühlen aufgestellt werden, ich will nur hinweisen auf die rein äußere Tatsache, daß solchen Erlebnissen wie Furcht oder Angst und Schamgefühl Ich-Erlebnisse zugrunde liegen, die in ihrer Wirkung auf",
      "das Blut erkennbar sind. Beim Furcht- und Angstgefühl ist es so, daß wir uns gleichsam schützen wollen vor irgend etwas, von dem wir glauben, daß es gegen uns wirkt; wir zucken da gleichsam mit unse­rem Ich zurück. Beim Schamgefühl ist es so, daß wir uns am liebsten verstecken möchten, uns sozusagen hinter das Blut zurückziehen, unser Ich auslöschen möchten. Beide Male - ich will dabei nur auf die äußeren Tatsachen eingehen - folgt das Blut materiell, als äußeres materielles Werkzeug dem, was das Ich in sich erlebt. Beim Furcht­und Angstgefühl, wo der Mensch sich so stark in sich zurückziehen möchte vor etwas, von dem er sich bedroht fühlt, da wird er bleich; das Blut zieht sich zurück von der Oberfläche zum Zentrum, nach innen. Wenn sich der Mensch beim Schamgefühl verstecken möchte, sich auslöschen möchte, wenn er am liebsten nicht wäre und irgendwo hineinschlüpfen möchte, da drängt sich das Blut unter dem Eindrucke dessen, was das Ich erlebt, bis zur Peripherie des Organis­mus, und der Mensch wird rot. So sehen wir, daß das Blut das am leichtesten bestimmbare System im menschlichen Organismus ist und den Erlebnissen des Ich am schnellsten folgen kann.",
      "Je weiter wir hinunterrücken in unseren Organsystemen, desto weniger folgen die Anordnungen der Systeme unserem Ich, desto weniger sind sie geneigt, sich den Erlebnissen des Ich anzupassen. Was das Nervensystem anbelangt, so wissen wir, daß es angeordnet ist in bestimmten Nervenbahnen und daß diese in ihrem Verlauf etwas verhältnismäßig Festes darstellen. Während das Blut regsam ist und je nach den inneren Erlebnissen des Ich von einem Körperteil zum anderen bis in die Peripherie geführt werden kann, ist es bei den Nerven so, daß den Nervenbahnen entlang diejenigen Kräfte verlau­fen, welche wir als «Bewußtseinskräfte» zusammenfassen können, und daß diese nicht die Nervenmaterie von einem Orte zum anderen tragen können, wie das mit dem Blut in seinen Bahnen möglich ist. Das Nervensystem ist also schon weniger bestimmbar als das Blut; und noch weniger bestimmbar ist das Drüsensystem, das uns die Drüsen zeigt für ganz bestimmte Verrichtungen an ganz bestimmten Orten des Organismus. Wenn eine Drüse durch irgend etwas tätig gemacht werden soll zu einem bestimmten Zwecke, so kann sie nicht",
      "erregt werden durch einen Strang ähnlich dem Nervenstrang, son­muß diese Drüse an dem Orte, wo sie eben ist, erregt werden. Es ist also das Drüsensystem noch weniger bestimmbar, wir mussen die Drüsen da erregen, wo sie sind. Während wir die Nerventätigkeit den Nervensträngen entlang leiten können - wir haben da noch Verbin­dungsfasern, welche die einzelnen Nervenknoten miteinander ver­binden -, kann die Drüse nur an dem Ort zu einer Tätigkeit erregt werden, wo sie ist. Noch mehr aber ist dieser gleichsam Verfesti­gungsprozeß, dieser Prozeß des inneren Bestimmtseins, des Nicht­Bestimmbarseins ausgesprochen in alle dem, was zum Ernährungs­system gehört, durch das der Mensch sich direkt die Stoffe eingliedert, um ein physisch-sinnliches Wesen zu sein. Dennoch muß in der Eigenart dieser Stoffeingliederung eine völlige Vorbereitung für das Werkzeug des Ich gegeben sein.",
      "Betrachten wir nun einmal den menschlichen Organismus in bezug auf sein unterstes System, das Ernährungssystem im umfassendsten Sinne, durch das die Stoffe nach allen Gliedern des Organismus transportiert werden, so muß die Anordnung dieser Stoffe so gesche­hen, daß die Formung, der äußere Aufbau des Menschen so vor sich gehen kann, daß zuletzt der Ausdruck des Ich im menschlichen Organismus möglich ist. Dazu ist vieles notwendig. Nicht nur, daß die Ernährungsstoffe in der verschiedensten Weise transportiert und an die verschiedensten Orte des Organismus gelagert werden, son­dern auch, daß alle möglichen Vorkehrungen getroffen werden, um die äußere Form des menschlichen Organismus zu bedingen.",
      "Nun ist es wichtig, daß wir uns folgendes klarmachen. In dem, was wir die Haut genannt haben, sind zwar alle Systeme des menschli­chen Organismus vertreten, bis zum untersten System, dem Ernäh­rungssystem, und wir konnten sagen: In die Haut wird alles ergos­sen, was im eminentesten Sinne zum physischen System des Men­schen gehört. Aber Sie können sich leicht denken, daß diese Haut -trotzdem sie alle diese Systeme in sich hat - für sich einen großen Fehler hat, so paradox das auch klingt. Sie hat zwar so wie sie am Menschen ist, die Form des menschlichen Organismus, diese Form würde sie aber durch sich selber nicht haben; durch sich selber würde",
      "sie nicht in der Lage sein, dem Menschen seine charakteristische Formbegrenzung zu geben. Ohne Unterstützung würde die Haut in sich selber zusammensinken; da würde der Mensch sich nicht auf­recht halten können. Daraus sehen wir, daß nicht bloß diejenigen Ernährungsprozesse stattfinden müssen, welche die Haut erhalten, sondern es müssen auch die mannigfaltigsten anderen Prozesse statt­finden und zusammenwirken, welche die Gesamtform des Menschen-Organismus bilden. Da wird es uns nicht schwer sein zu begreifen, daß wir auch als solche umgewandelten Ernährungsprozesse diejeni­gen Prozesse anzusehen haben, die vor sich gehen in den Knorpeln und in den Knochen. Was sind das für Prozesse?",
      "Wenn das Material unserer Nahrungsstoffe bis zu einem Knorpel oder Knochen geleitet wird, so ist im Grunde genommen auch nur physisches Material dahin transportiert. Was wir zuletzt im Knorpel oder Knochen finden, ist ja nichts anderes als die umgewandelten Nahrungsstoffe; aber sie sind in anderer Art umgewandelt als zum Beispiel in der Haut. Daher können wir sagen: Wir haben in der Haut zwar die umgewandelten Nahrungsstoffe zu sehen, die sich in der äußersten Formumgrenzung unseres Leibes ablagern. In der Art aber, wie im Knochen das Ernährungsmaterial abgelagert wird, haben wir einen solchen Ernährungsprozeß zu sehen, wo das Mate­rial sich rundet zur menschlichen Form. Es ist also ein umgekehrter Ernährungsprozeß wie derjenige in der menschlichen Haut. Nun wird es uns gar nicht mehr schwierig sein, gleichsam nach dem Muster der Betrachtungen, die wir für das Nervensystem angestellt haben, uns auch diesen gesamten Ernährungsprozeß, das Transpor­tierungssystem der Nahrungsmittel zu denken.",
      "Wenn wir die Haut anschauen und auf die Ernährungsstoffe sehen, welche sie zustande bringen, diesen äußeren Abschluß, der dem Menschen die Oberfläche gibt, aber niemals selber die menschliche Form hervorbringen könnte, so wird es uns klar sein, daß die Haut-ernährung die jüngste Art der Ernährung ist im Menschenorganis­mus; und wir erkennen, daß wir in der Art, wie die Knochen ernährt werden, einen analogen Prozeß zu sehen haben, der in einem ähnli­chen Verhältnis zur Hauternährung steht, wie wir den Prozeß der",
      "Gehirnbildung in ein Verhältnis setzen konnten zum Prozeß der Rückenmarksbildung. Wir werden dasselbe Recht haben zu sagen:",
      "Dasjenige, was wir zunächst äußerlich im Hauternährungsprozeß auftreten sehen, können wir auf einer späteren, das heißt hier höhe­ren Stufe umgewandelt sehen in der festen Form der Knochenbil­dung. - Es weist uns eine solche Betrachtung des menschlichen Organismus darauf hin, daß unser Knochensystem früher als weiche Substanz bestanden hat und sich erst im Laufe der Entwickelung verfestigt hat. Das kann auch durch die äußere Wissenschaft nachge­wiesen werden, die uns lehren kann, wie gewisse Gebilde, die später deutlich Knochen sind, im kindlichen Alter noch weich, knorpelhaft auftreten und daß erst nach und nach aus einer weicheren, knorpel-mäßigen Masse durch Einlagerung von Ernährungsmaterial sich die Knochenmasse bildet.",
      "Da haben wir ein Hinüberführen von einer weichen in eine festere Substanz, wie es auch beim einzelnen Men­schen sich vollzieht. Wir haben also im Knorpel eine Vorstufe des Knochens zu sehen und können sagen, daß uns die ganze Einlage­rung des Knochensystems in den Organismus als etwas erscheint, was sozusagen ein letztes Resultat derjenigen Prozesse darstellt, die uns in der Hauternährung vor Augen treten.",
      "Es werden also zuerst in einfachster Weise die Ernährungsstoffe umgewandelt zu einer wei­chen, biegsamen Substanz, und dann, wenn dies vorbereitet ist, kann der Ernährungsprozeß sich abspielen, durch den gewisse Teile sich erst verhärten zu Knochenmaterie, damit zuletzt die Form des menschlichen Gesamtorganismus zum Vorschein kommt. Die Art, wie uns die Knochen entgegentreten, gibt uns Anlaß zu sagen: Über die Knochenbildung hinaus haben wir eigentlich dann kein weiteres Fortschreiten der Ernährungsprozesse zur Verfestigung, soweit der Mensch der gegenwärtigen Entwickelungsstufe in Betracht kommt.",
      "Während wir auf der einen Seite im Blut die bestimmbarste, wand­lungsfähigste Substanz im Menschen haben, können wir andererseits in der Knochensubstanz dasjenige erblicken, was völlig unbestimm­bar ist, was bis zu einem letzten Punkte sich verhärtet, verfestigt hat, uber den hinaus es keine weitere Umwandlung mehr gibt; sie hat es bis zur starrsten Form gebracht. Wenn wir nun die früheren Betrachtungen",
      "fortsetzen, dann müssen wir sagen: Das Blut ist das bestimm­barste Werkzeug des Ich im Menschen, die Nerven sind es schon weniger, die Drüsen noch weniger, und im Knochensystem haben wir das, was am letzten Punkte seiner Evolution angelangt ist, was ein letztes Umwandlungsprodukt darstellt in bezug auf die Bestimm­barkeit durch das Ich. Deshalb geschieht alles, was zur Formung des Knochensystems gehört, in der Weise, daß zuletzt die Knochen Träger und Stütze eines weicheren Organismus sein können, in wel­chem Lebens- und Ernährungsvorgänge so ablaufen, daß das Blut in seinen Bahnen in der rechten Weise verlaufen kann, damit das menschliche Ich in ihm ein Werkzeug haben kann.",
      "Ich möchte wissen, wer nicht mit höchster Bewunderung und Ehrfurcht erfüllt würde, wenn er hineinblickt in den menschlichen Organismus und sich vorzustellen versucht: Im Knochensystem habe ich dasjenige vor mir, was die meisten Verwandlungen, die meisten Stufen durchgemacht haben muß, was von den untersten Stufen aufgestiegen ist durch viele, viele Epochen hindurch bis zum heu­tigen Knochensystem; es ist zuletzt so gestaltet worden, daß es der feste Träger, die feste Stütze des Ich sein kann. Wenn man gewahr wird, wie bis in die Bildungen der einzelnen Knochen hinein die Tendenz des Ich wirkt, wer könnte da nicht mit tiefster Bewunde­rung erfüllt werden gegenüber diesem Bau des menschlichen Orga­nismus.",
      "Sehen wir diesen Menschen an, so haben wir zwei Pole des physi­schen Daseins gegeben, einmal im Blutsystem, das das bestimmbarste Werkzeug des Ich ist, und dann im Knochensystem, das in äußerer Form und innerer Struktur am meisten fest ist, am unbestimmbar­sten, am wenigsten wandlungsfähig, das in der Unbestimmbarkeit am weitesten vorgeschritten ist. Wir dürfen daher sagen: Im Knochen­system hat die physische Organisation des Menschen vorläufig ihren letzten Ausdruck, ihren Abschluß gefunden, während sie in dem Blutsystem in einem gewissen Sinne einen neuen Anfang genom­men hat. Schauen wir auf unser Knochensystem hin, so können wir sagen: Wir verehren in diesem Knochensystem einen letzten Ab­schluß der menschlichen physischen Organisation. - Und schauen",
      "wir auf unser Blutsystem, so können wir sagen: Wir sehen in ihm einen Anfang, etwas, das erst anfangen konnte, nachdem alle ande­ren Systeme vorangegangen sind. - Vom Knochensystem können wir sagen: Eine gewisse erste Anlage, die ersten Kräfte zur Bil­dung des Knochensystems mußten schon vorhanden gewesen sein, bevor Drüsen- und Nervensystem im Organismus zur Entwicke­lung kamen, denn diese mußten durch das Knochensystem ihre ent­sprechenden Orte angewiesen erhalten. Das älteste der Kraft-systeme des menschlichen Organismus haben wir im Knochen-system in uns.",
      "Wenn wir nun das Blutsystem und das Knochensystem als zwei Pole bezeichnet haben, so wollten wir damit bildlich ausdrücken, daß in ihnen gleichsam die beiden äußersten Enden der menschlichen Organisation zu sehen sind. Im Blutsystem haben wir das beweglich­ste Element vor uns, das so regsam ist, daß es jeder Regung unseres Ich folgt.",
      "Und im Knochensystem haben wir dasjenige, was fast ganz dem Einfluß unseres Ich entzogen ist, wo wir nicht mehr hinunterrei­chen mit unserem Ich; dennoch aber liegt in seiner Form schon die ganze Organisation des Ich darinnen. Es stehen damit schon rein äußerlich betrachtet Blutsystem und Knochensystem im Menschen wie ein Anfang und ein Abschluß einander gegenüber.",
      "Und wenn wir so unser Blutsystem anschauen, das fortwährend allen Regungen des Ich folgt, so sagen wir uns: Im regsamen Blut drückt sich uns so recht das menschliche Leben aus. - Wenn wir auf unser Knochensystem schauen, sagen wir uns: Es symbolisiert alles das, was sich unserem Leben entzieht und dem Organismus nur als Stütze dient. - Unser pulsierendes Blut ist unser Leben; unser Knochensystem ist dasje­nige, was sich dem unmittelbaren Leben schon entzogen hat - weil es ein so alter Herr ist -, was sich schon ausgeschaltet hat und nur noch als Stütze dienen will, nur noch Form geben will. Während wir in unserem Blute am meisten organisch leben, sind wir im Grunde genommen in unserem Knochensystem schon gestorben.",
      "Und ich bitte Sie, diesen Ausspruch wie ein Leitmotiv für die folgenden Vorträge zu betrachten, denn es werden sich wichtige physiologische Dinge daraus ergeben. Während wir in unserem Blute leben, sind wir",
      "in unserem Knochensystem eigentlich schon gestorben. Unser Kno­chensystem ist wie ein Gerüst, es ist das am wenigsten Lebendige, es ist nur das uns stützende Gerüst in uns.",
      "Wir haben schon am Anfang dieser Vortragsreihe im Menschen eine Zweiheit gesehen; jetzt tritt uns diese Zweiheit noch einmal in einer anderen Weise entgegen. Auf der einen Seite das Regsamste, Lebendigste im Blut, auf der anderen Seite etwas wie ein sich der organischen Regsamkeit am meisten Entziehendes, den Tod eigent­lich schon in sich Tragendes im Knochensystem.",
      "Unser Knochen-system hat einen gewissen Abschluß schon erhalten - in seiner Aus­formung wenigstens, wenn es auch nachher noch wächst - bis zu der Lebenszeit des Menschen, wo die Ich-Erlebnisse beginnen regsam zu werden. Bis zum Zahnwechsel im siebten Lebensjahr hat das Kno­chensystem sich im wesentlichen seine Form gegeben.",
      "Gerade in der Zeit also findet die Hauptentwickelung unseres Knochensystems statt, wo wir selber noch der Regsamkeit unseres Ich in hohem Maße entzogen sind. In dieser Zeit, wo das Knochensystem sich aufbaut aus den dunklen Untergründen und Kräften unseres Organismus heraus, können auch die meisten Fehler in der Ernährung gemacht werden.",
      "Gerade in diesen ersten sieben Lebensjahren können in der Ernährung des Kindes besonders folgenschwere Fehler gemacht wer­den, die sich auf das Knochensystem übel auswirken, zum Beispiel in rachitischen Erkrankungen, die namentlich davon herrühren, daß die Ernährungsprozesse in diesen Jahren nicht in der richtigen Weise geleitet werden, zum Beispiel wenn man der Naschhaftigkeit der Kinder nachgibt und ihnen alles mögliche gibt, wonach sie Verlangen tragen. So sehen wir das, was dem Ich entzogen ist, in unser Kno­chensystem hineinwirken.",
      "Ganz anders ist es beim Blutsystem, welches regsam folgt unserem einzelmenschlichen Leben und mehr als alles andere abhängig ist von den Prozessen unseres inneren Erlebens. Es ist nur eine Art von Kurzsichtigkeit seitens der äußeren Wissenschaft, zu glauben, daß von den inneren Erlebnissen das Nervensystem mehr abhängig wäre als das Blutsystem. Ich will nur darauf hinweisen, daß wir die ein­fachste Art der Beeinflussung des Blutsystems durch die Ich-Erlebnisse",
      "in der Scham und in der Furcht haben, wo eine Umlagerung des Blutes stattfindet, die deutlich ausdrückt die Ich-Erlebnisse in dem Werkzeuge des Ich, dem Blut. Sie können sich also denken, wenn sich schon vorübergehende Prozesse so ausdrücken, wie sich dann dauernde oder gewohnheitsmäßige Erlebnisse des Ich ausdrücken mussen in dem erregsamen Elemente des Blutes. Es gibt keine Lei­denschaft, keinen Trieb oder Affekt, ob wir sie gewohnheitsmäßig haben oder ob sie explosionsartig zum Ausdruck kommen, die nicht als innere Erlebnisse übertragen werden auf das Blut als Instrument des Ich. Alle ungesunden Elemente des Ich-Erlebens kommen im Blutsystem zum Ausdruck.",
      "Und überall, wo wir irgend etwas verstehen wollen, was im Blut­system vorgeht, da ist es wichtig, nicht bloß zu fragen nach dem Ernährungsprozeß, sondern vielmehr nach den seelischen Prozessen zu suchen, insofern sie Ich-Erlebnisse sind, wie Stimmungen, dau­ernde Leidenschaften, Affekte und so weiter. Nur eine materialisti­sche Gesinnung wird bei Störungen im Blutsystem das Hauptaugen­merk auf die Ernährung lenken; denn die Bluternährung baut sich auf auf die Ernährung des physischen Systems, des Drüsensystems, des Nervensystems und so weiter, und im Grunde genommen sind die Nahrungsstoffe schon sehr filtriert, wenn sie an das Blut herankom­men. Wenn daher das Blut von dieser Seite her beeinträchtigt werden soll, muß schon eine ganz wesentliche Erkrankung des Organismus aufgetreten sein; dagegen wirken alle seelischen, alle Ich-Prozesse in unmittelbarer Weise auf das Blut zurück.",
      "So entzieht sich unser Knochensystem am meisten den Vorgängen unseres Ich, und so fügt sich unser Blutsystem am allermeisten den Vorgängen unseres Ich. Ja, dieses Knochensystem ist am allerwenig­sten veranlagt, dem Ich zu folgen, man möchte sagen, es ist ganz unabhängig vom Ich, aber doch ist es für das Ich organisiert.",
      "Nur ein kleiner Teil des Knochensystems macht von der Unbe­stimmbarkeit durch das Ich eine Ausnahme und zeigt eine individu­elle Prägung, nämlich die Schädelknochen, besonders der obere Teil des Schädels. Diese Tatsache hat zu verschiedenem Unfug Veranlas­sung gegeben.",
      "Sie wissen, daß es eine Phrenologie, eine Schädelknochenunter­suchung, gibt. Diese hat nach und nach, trotzdem sie von materiali­stischer Seite als Aberglaube angesehen wird, nach den allgemeinen Gepflogenheiten unserer Zeit eine materialistische Nuance angenom­men. Wenn wir grob charakterisieren wollen, können wir sagen: Im allgemeinen wird Phrenologie so beschrieben, daß in den Formen unserer Schädelbildung der Ausdruck gesucht wird für die innere Beschaffenheit unseres Ich, indem gleichsam allgemeine Gesichts­punkte aufgestellt werden und erklärt wird, der eine Höcker bedeute dies, der andere das und so weiter. Da will man die menschlichen Eigenschaften auffinden an den verschiedenen Höckern, die sich an unserem Schädel zeigen. In dem Knochensystem des Schädels wird also von der Phrenologie gesucht eine Art plastischer Ausdruck für unser Ich. Nun ist das aber, wenn es so getrieben wird, auch wenn scheinbar geistige Ausdrücke im Bau der einzelnen Knochen gesucht werden, doch ein Unfug. Denn wer wirklich ein feiner Beobachter ist, der weiß, daß kein einziger menschlicher Schädel dem anderen gleicht und daß man niemals Erhöhungen oder Vertiefungen an­geben könnte, die für diese oder jene Eigenschaft allgemein typisch sind, sondern daß ein jeder Schädel sich unterscheidet von dem an­deren, so daß wir bei jedem Menschenschädel andere Formen vor uns haben.",
      "Nun haben wir gesagt, daß sich unserem Ich, dem das Blut in seiner Regsamkeit am meisten folgt, der Knochenbau entzieht, ihm am wenigsten folgt. Es ist merkwürdig, daß uns dennoch die Bildung des Schädels und der Gesichtsknochen dem Ich entsprechend gestal­tet erscheinen, während der Knochenbau mehr allgemein typisch erscheint. Wer den Schädelbau betrachtet, der weiß: So wahr der Mensch selber individuell ist, so wahr ist auch sein Schädelbau individuell.",
      "Wie kommt es, daß diese wunderbare Konfiguration des Schädels von Anfang an der einzelnen menschlichen Individualität entspre­chend angelegt ist, wenn doch das Ich keinen Einfluß auf den Kno­chenbau hat? Woher kommt es, daß der Schädel, der sich so entwik­keIn muß, wie die anderen Knochen auch, anders ist bei jedem",
      "Menschen? Woher kommt das? Das kommt einfach aus demselben Grunde, aus dem die individuellen Eigenschaften des Menschen sich überhaupt entwickeln, nämlich daher, daß das individuelle menschli­che Gesamtleben nicht nur verläuft von der Geburt bis zum Tode, sondern verläuft in vielen Inkarnationen. Während unser Ich also in der gegenwärtigen Inkarnation keinen Einfluß hat auf den Schädel-bau, hat es durch die Erlebnisse seiner vorangegangenen Inkarnation die Kräfte entwickelt, die in der Zeit zwischen dem Tode und der nächsten Geburt die Konfiguration des Schädelbaues, die Schädel-form, in dieser Inkarnation bestimmen. Wie das Ich in der vorherigen Inkarnation war, das bestimmt die Schädelform in der jetzigen Inkar­nation, so daß wir in dem Bau unseres Schädels einen äußeren plasti­schen Ausdruck haben für die Art und Weise, wie wir, jeder einzelne, als Individualität, in der vorhergehenden Inkarnation gelebt und gewirkt haben. Während alle anderen Knochen bei uns etwas Allge­mein-Menschliches ausdrücken, drückt der Schädel in seiner äußeren Form das aus, was wir waren und was wir getan haben in der vorigen Inkarnation.",
      "Das äußerst regsame Element des Blutes kann also bestimmt wer­den vom Ich in dieser Inkarnation. Unsere Knochen aber haben sich in dieser Inkarnation dem Einfluß des Ich schon ganz entzogen, bis auf den letzten Rest, den Schädelknochen, der aber dem Ich auch nicht mehr in dieser Inkarnation folgen kann. Der Schädelknochen, der aus der Weiche der Keimessubstanz heraus sich entwickelt hat, wo das Ich noch gestaltend einwirken konnte, gibt einen Ausdruck dafür, wie wir in der vorherigen Inkarnation waren. Eine allgemeine Phrenologie gibt es nicht. Wenn wir Phrenologie überhaupt in Betracht ziehen wollen, so darf sie keine schematisierende Wissen­schaft sein, sondern sie sollte auf eine künstlerische Art und Weise die plastischen Eigentümlichkeiten des Schädelbaues betrachten. Wir müssen unseren Schädelbau beurteilen wie ein Kunstwerk. Wir müs­sen allerdings in dem Schädelbau etwas Individuelles sehen, aber etwas Individuelles, das ein Ausdruck der Geschichte des Ich ist in einer vorhergehenden Inkarnation. So sehen wir, daß selbst diese Form des Knochenbaus, wie sie uns im Schädelbau entgegentritt,",
      "dem Ich soweit entzogen ist, daß es in der gegenwärtigen Inkarnation darauf keinen Einfluß mehr hat. Aber es hat noch Einfluß darauf beim Durchgang zwischen Tod und neuer Geburt, wo es in gewissem Sinne die Kräfte wieder aufnimmt, die sich ihm im vergangenen Leben schon entzogen hatten und welche unter seinem Einfluß für das nächste Leben das Knochensystem und besonders den Schädel aufbauen.",
      "Wenn daher von der Wiederverkörperungsidee gesprochen und gesagt wird, das sei eine Sache, die sich im allgemeinen der Beurtei­lung durch unsere Vernunft entziehe, da müsse man eben das glau­ben, was der Geistesforscher sagt-, so ist das nicht richtig. Man kann darauf erwidern: Ihr könnt euch handgreiflich davon überzeugen, daß das menschliche Ich in einer vorhergehenden Inkarnation dage­wesen sein muß; im menschlichen Schädel hat man handgreiflich den Beweis vor sich, wie der Mensch in der vorhergehenden Inkarnation war.",
      "Wer das nicht zugibt, wer darin etwas Paradoxes sieht, daß man aus der Art, wie etwas äußerlich geformt ist, schließen muß auf etwas früher Lebendiges, das aus seinem früheren Leben heraus das Äußere geformt hat, der hat auch kein Recht, sonstwie auf ein früher Leben­diges zu schließen, wenn ihm irgendwo eine plastische Gestalt entge­gentritt. Wer nicht den Schluß zugibt als einen streng logischen, daß in der individuellen Schädelform, die wir haben, sich die Konfigura­tion des Ich aus früheren Inkarnationen ausdrückt, der hat auch kein Recht, wenn er zum Beispiel irgendwo auf der Erde eine leere Muschel findet, aus der äußeren Form dieser Muschel schließen zu wollen, daß da einmal ein Lebewesen drin war.",
      "Wer aus der toten Muschel schließen will auf ein Lebewesen, das einmal da drinnen war und die Muschel geformt hat, der darf den logisch ganz gleichwerti­gen Schluß nicht abweisen, daß in der individuellen Ausgestaltung unseres Schädels der unmittelbare Beweis gegeben ist für das Herein­wirken eines früheren Lebens in dieses Leben.",
      "So sehen Sie, daß wir hier eines der Tore haben, durch die wir physiologisch hineinleuchten können in die Reinkarnationsidee. Sol­che Tore gibt es viele; man muß sich nur Zeit lassen. Wenn man geduldig ist und wartet, dann wird man die Stellen finden, wo die",
      "Beweise erbracht werden können und wie sie zu erbringen sind. Und wer leugnen wollte, daß in dem, was jetzt gesagt worden ist, Logik liegt, der müßte auch die gesamte Paläontologie leugnen, denn sie beruht auf denselben Schlußfolgerungen. So sehen wir, wie wir durch Eindringen in die Formen des menschlichen Organismus diesen auf seine geistigen Grundlagen zurückführen können."
    ],
    "sentences": [
      [
        "Aus den letzten Vorträgen konnten wir ersehen, daß der Mensch als physische Organisation sich gewissermaßen durch seine Haut nach außen abgrenzt.",
        "Wenn wir den menschlichen Organismus ganz in dem Sinne auffassen, wie wir das nach den bisherigen Erörterungen tun müssen, dann ist es notwendig, daß wir uns sagen: Es ist der menschliche Organismus mit seinen verschiedenen Kraftsystemen selber, der sich in der Haut nach außen einen bestimmten Abschluß gibt."
      ],
      [
        "Mit anderen Worten: Uns muß klar sein, daß im menschlichen Organismus ein solches Gesamtsystem von Kräften ist, welche sich durch ihr Zusammenwirken so bestimmen, daß sie sich genau den Formumriß geben, der durch die Haut als äußere Begrenzung der Menschengestalt zum Vorschein kommt.",
        "So müssen wir eigentlich sagen, daß für den Lebensprozeß des Menschen die interessante Tatsache vorliegt, daß uns in der äußeren Formbegrenzung ein gleichsam bildhafter Ausdruck gegeben ist für die gesamte Wirksam­keit der Kraftsysteme im Organismus."
      ],
      [
        "Wenn nun in der Haut selber ein solcher Ausdruck des Organismus gegeben werden soll, so müs­sen wir voraussetzen, daß innerhalb der Haut eigentlich in einer gewissen Weise der ganze Mensch irgendwie zu finden sein muß.",
        "Denn, wenn der Mensch, so wie er ist, so gebildet sein soll, daß die äußere Haut als Formbegrenzung das ausdrückt, was er ist, so muß in der Haut alles das gefunden werden können, was im Menschen zur Gesamtorganisation gehört."
      ],
      [
        "Und in der Tat, wenn wir auf dasjenige eingehen, was zur Gesamtorganisation des Menschen gehört, so kön­nen wir finden, wie sehr eigentlich dasjenige innerhalb der Haut vorhanden ist, was in den Kraftsystemen des Gesamtorganismus veranlagt ist."
      ],
      [
        "Da haben wir zunächst gesehen, daß der Gesamtmensch, wie er uns als Erdenmensch entgegentritt, das Werkzeug seines Ich in sei­nem Blutsystem hat, so daß der Mensch dadurch Mensch ist, daß er in sich ein Ich birgt, und dieses Ich sich bis zum physischen System"
      ],
      [
        "herunter einen Ausdruck, ein Werkzeug schaffen kann im Blut.",
        "Ist nun unsere Körperoberfläche, unsere Formbegrenzung ein wesentli­ches Glied unserer Gesamtorganisation, so müssen wir sagen: Diese Gesamtorganisation muß durch das Blut bis in die Haut hinein wirken, damit in der Haut ein Ausdruck der ganzen menschlichen Wesenheit, insofern sie physisch ist, vorhanden sein kann."
      ],
      [
        "Betrachten wir die Haut, wie sie sich, aus mehreren Schichten bestehend, über die ganze Oberfläche des Leibes spannt, so finden wir, daß in der Tat in diese Haut feine Blutgefäße hineingehen.",
        "Durch diese feinen Blut­gefäße kann das Ich seine Kräfte senden und sich bis in die Haut hinein einen Ausdruck der menschlichen Wesenheit schaffen."
      ],
      [
        "Wir wissen ferner, daß für alles, was wir als Bewußtsein zu bezeichnen haben, das Nervensystem das physische Werkzeug ist.",
        "Wenn nun die Körperoberflächenbegrenzung ein Ausdruck der Gesamtorganisa­tion des Menschen ist, so müssen auch die Nerven bis in die Haut hinein sich erstrecken, damit das menschliche Bewußtsein bis in dieses Organ gehen kann."
      ],
      [
        "Wir sehen daher neben den feinen Blut­gefäßen innerhalb der Hautschichten die mannigfaltigsten Nerven­endungen verlaufen, die man ja gewöhnlich - obwohl nicht mit vol­lem Recht - die Tastkörperchen nennt, weil man annimmt, daß der Mensch mit Hilfe dieser Tastkörperchen die äußere Welt durch den Tastsinn wahrnimmt, so wie er durch Augen und Ohren Licht und Schall wahrnimmt.",
        "Es ist das aber nicht eigentlich der Fall."
      ],
      [
        "Genauer betrachtet ist dieser Tastsinn der Ausdruck verschiedener Sinnestä­tigkeiten, zum Beispiel Wärmesinn und andere.",
        "Wir werden noch sehen, wie die Sache liegt.",
        "Wir finden also in der Haut dasjenige, was Ausdruck oder körperliches Organ des menschlichen Ich ist: das Blut."
      ],
      [
        "Wir sehen aber auch dasjenige, was Ausdruck des menschlichen Bewußtseins ist: das Nervensystem, das seine Ausläufer bis in die Haut hineinerstreckt."
      ],
      [
        "Nun müssen wir uns umsehen nach dem Ausdruck dessen, was wir überhaupt betrachten können als das wesentliche Instrument des Lebensprozesses.",
        "Wir haben schon im letzten Vortrage auf dieses Instrument des Lebensprozesses aufmerksam gemacht bei der Besprechung der Absonderung.",
        "In der Absonderung, bei der, wie wir"
      ],
      [
        "gesehen haben, gleichsam eine Art von Hemmnis auftritt, haben wir insofern den Ausdruck des Lebensprozesses zu sehen, als ein leben­diges Wesen, das in der Welt existieren will, notwendig hat, sich nach außen abzuschließen.",
        "Das kann nur dadurch geschehen, daß es in sich selber ein Hemmnis erlebt.",
        "Dieses Erleben eines Hemmnisses in sich selber wird vermittelt durch Absonderungsorgane, die man im weite­sten Umfange als Drüsen bezeichnen kann.",
        "Drüsen sind Absonde­rungsorgane, und das Hemmnis tritt dadurch ein, daß sie den an sie herandrängenden Nahrungsstoffen sozusagen inneren Widerstand entgegensetzen.",
        "Wir müssen also voraussetzen, daß solche Abson­derungsorgane, ebenso wie wir sie sonst im Organismus verteilt ha­ben, auch der Haut angehören.",
        "Und sie gehören der Haut an; denn wir finden auch in der Haut Absonderungsorgane, Drüsen der ver­schiedensten Art, Schweißdrüsen, Talgdrüsen, welche dieses Abson­derungsgeschäft - also einen Lebensprozeß - innerhalb der Haut betreiben."
      ],
      [
        "Und wenn wir endlich nach dem fragen, was unterhalb des Lebensprozesses liegt, so werden wir da dasjenige finden, was wir nennen können den reinen Stoffprozeß, das Überleiten der Stoffe von einem Organ zum anderen.",
        "Ich möchte Sie jetzt an dieser Stelle bitten, genau zu unterscheiden zwischen einem solchen Absonde­rungsprozeß, der ein inneres Hemmnis schafft, der den Lebenspro­zessen angehört, und denjenigen Prozessen, die rein stoffliche Umla­gerungen bewirken, also bloßes Transportieren der Stoffe von einem Orte zum anderen.",
        "Denn das ist nicht dasselbe.",
        "Für eine materialisti­sche Anschauung könnte es so aussehen, aber für eine lebensvolle Erfassung der Wirklichkeit ist es nicht so.",
        "Wir haben es im menschli­chen Organismus nicht bloß zu tun mit einer bloßen Transportierung der Stoffe.",
        "Allerdings findet überall ein Hinleiten der Stoffe, der Ernährungsprodukte, zu den einzelnen Organen statt.",
        "Aber in dem Augenblick, wo die Nahrungsstoffe aufgenommen werden, haben wir es mit einem Lebensprozesse zu tun, mit Absonderungsprozes­sen, die zugleich innere Hemmnisse schaffen.",
        "Es ist notwendig, dies zu unterscheiden von dem Prozeß der bloßen Stoffumlagerung.",
        "Wir steigen von dem Lebensprozeß hinunter zu den Prozessen des eigentlichen"
      ],
      [
        "Physischen, wenn wir sagen, es sieht sich so an, wie wenn die aufgenommenen Nahrungsstoffe in die verschiedensten Teile des physischen Leibes transportiert würden.",
        "Es ist aber eine lebendige Tätigkeit, gleichsam ein Sichgewahrwerden des Organismus in sei­nem eigenen Innern, in dem durch die Absonderungsorgane innere Hemmnisse geschaffen werden."
      ],
      [
        "Mit den Lebensvorgängen findet zugleich ein Transport der Stoffe statt, und das ist in der Haut ebenso wie in den anderen Teilen des Organismus.",
        "Durch die Haut werden die Abfälle der Nahrungsstoffe ausgeschieden, abgesondert, nach außen getragen durch den Prozeß der Schweißabsonderung, des Schwitzens, so daß auch hier ein rein physisches Transportieren der Stoffe vorhanden ist."
      ],
      [
        "Damit haben wir im wesentlichen charakterisiert, daß in dem äußeren Organ der Haut sich finden sowohl das Blutsystem als Ausdruck des Ich als auch das Nervensystem als Ausdruck des Bewußtseins.",
        "Ich will jetzt nach und nach dazu überleiten, daß wir ein Recht haben, alle Bewußtseinserscheinungen zusammenzufassen mit dem Ausdruck «Astralleib», daß wir also das Nervensystem bezeichnen können als einen Ausdruck des Astralleibes, das Drüsen­system als einen Ausdruck des Äther- oder Lebensleibes und daß wir den eigentlichen Ernährungs-Umlagerungsprozeß bezeichnen können als einen Ausdruck des physischen Leibes.",
        "Insofern sind alle einzelnen Gliederungen der menschlichen Organisation in dem Hautsystem, durch das sich der Mensch nach außen abschließt, tat­sächlich vorhanden.",
        "Nun müssen wir allerdings berücksichtigen, daß alle Gliederungen der menschlichen Organisation, Blutsystem, Ner­vensystem, Ernährungssystem und so weiter, in ihren gegenseitigen Beziehungen ein Ganzes ausmachen und daß wir gleichsam, indem wir diese vier Systeme der menschlichen Organisation betrachten und sie am physischen Leibe uns vor Augen führen, den menschli­chen Organismus von zwei Seiten vor uns haben.",
        "Wir haben ihn tatsächlich von zwei Seiten, und zwar zunächst so, daß wir sagen können: Der menschliche Organismus hat innerhalb des Erdenda­seins nur einen Sinn, wenn er als Gesamtorganismus das Werkzeug unseres Ich ist.",
        "Das kann er aber nur sein, wenn das nächste Werkzeug,"
      ],
      [
        "dessen sich das menschliche Ich bedienen kann, das Blut­system, in ihm vorhanden ist.",
        "Nun ist aber das Blutsystem nur möglich, wenn ihm die anderen Systeme in ihrer Bildung vorangehen.",
        "Das Blut ist nicht nur im Sinne des Dichterwortes «ein ganz besonderer Saft», sondern es ist leicht einzusehen, daß es so, wie es ist, überhaupt nicht existieren kann, ohne daß es sich einlagert dem ganzen übrigen Organismus des Menschen; es ist nötig, daß es in seiner Existenz vorbereitet ist durch den ganzen übrigen menschlichen Organismus.",
        "Das Blut, so wie der Mensch es hat, kann nirgends vorkommen als im menschlichen Organismus.",
        "Wir dürfen durchaus nicht das, was für das Blut des Menschen gesagt worden ist, ohne weiteres auf ein anderes Lebewesen der Erde übertragen.",
        "Ich werde vielleicht später noch Gelegenheit haben, über das Verhältnis von menschlichem Blut zu tierischem Blut zu sprechen.",
        "Das wird eine sehr wichtige Betrach­tung sein, weil die äußere Wissenschaft auf diesen Unterschied wenig Rücksicht nimmt.",
        "Heute wollen wir nur hinweisen auf das Blut als Ausdruck des menschlichen Ich.",
        "Ist einmal der ganze übrige Orga­nismus des Menschen aufgebaut, so ist er erst fähig, Blut zu tragen, den Blutkreislauf in sich aufzunehmen, erst dann kann er in sich das Instrument haben, welches als Werkzeug unserem Ich dient.",
        "Dazu muß aber der Gesamtorganismus des Menschen erst aufgebaut sein."
      ],
      [
        "Sie wissen, daß es auch andere Wesenheiten neben dem Menschen auf der Erde gibt, die in einer gewissen Verwandtschaft mit dem Menschen augenscheinlich stehen, die aber nicht in der Lage sind, ein menschliches Ich zum Ausdruck zu bringen.",
        "Bei diesen ist offenbar dasjenige, was in den entsprechenden Systemen der menschlichen Anlage ähnlich sieht, doch anders aufgebaut als beim Menschen.",
        "In allen diesen Systemen, die dem Blutsystem vorausgehen, muß schon die Möglichkeit veranlagt sein, das Blut aufnehmen zu können.",
        "Das heißt, wir müssen erst ein solches Nervensystem haben, welches ein Blutsystem im Sinne des menschlichen Blutsystems aufnehmen kann; wir mussen ein solches Drüsensystem haben und ebenso ein solches Ernährungssystem, die vorgebildet sein müssen für die Aufnahme eines menschlichen Blutsystems.",
        "Das bedeutet, es muß zum Beispiel schon auf der Seite des menschlichen Organismus, die wir bezeichnet"
      ],
      [
        "haben als den eigentlichen Ausdruck des physischen Leibes des Men­schen, beim Ernährungssystem, das Ich veranlagt sein.",
        "Es muß gleichsam der Prozeß der Bildung des Ernährungssystems durch den Organismus so gelenkt und geleitet sein, daß zuletzt das Blut sich in den richtigen Bahnen bewegen kann.",
        "Was heißt das?"
      ],
      [
        "Das bedeutet, daß der Blutkreislauf in seiner Gestaltung, in der ganzen Art seiner Regsamkeit, bedingt ist durch die Ich-Wesenheit des Menschen.",
        "Denken wir uns den Blutkreislauf in dieser ovalen Linie völlig schematisch angedeutet (siehe Zeichnung), so müssen wir"
      ],
      [
        "# Bild s. 115"
      ],
      [
        "sagen, es muß ja der Blutkreislauf von dem übrigen Organismus aufgenommen werden, das heißt, alle Organsysteme müssen so ange­ordnet sein, daß der Blutkreislauf sich eingliedern kann.",
        "Wir könnten das ganze Gewebe unserer Blutgefäße - sei es am Kopfe oder an einem anderen Teil unseres Organismus - nicht so haben, wie es ist, wenn nicht überall dahin, wo das Blut kreisen soll, die entsprechen­den Dinge geleitet werden, die da sein müssen.",
        "Das heißt, die Kraft­systeme müssen im menschlichen Organismus, vom Ernährungs­system angefangen, so wirken, daß sie an die betreffenden Orte das notwendige Ernährungsmaterial hintragen und es zugleich so gestal­ten, so vorbilden, daß an diesen Orten das Blut genau die Form seines"
      ],
      [
        "Verlaufs einhalten kann, deren es bedarf, um ein Ausdruck des Ich werden zu können.",
        "Es muß daher in alle Impulse unseres Ernäh­rungsapparates, also des untersten Systems unseres Organismus, schon dasjenige hineingelegt sein, was den Menschen zu einem Ich-Wesen macht.",
        "Die ganze Form, die der Mensch zuletzt in seiner physischen Vollendung zeigt, muß schon hineingegliedert sein in die Organsysteme bis in das hinein, was die verschiedenen Ernährungs­prozesse des Menschen sind.",
        "Da sehen wir von dem Blute hinunter in die den Blutkreislauf vorbereitenden Organsysteme zu den Prozes­sen, die weitab von unserem Ich im Dunkel unseres Organismus sich abspielen.",
        "Während das Blut der Ausdruck unserer Ich-Tätigkeit ist, also Ausdruck des Bewußtesten ist, was wir haben, sind wir nicht fähig, hinunterzusehen in die unbekannten Tiefen des physischen Leibes.",
        "Wir wissen nicht, wie die Stoffe hingeleitet, hingetragen werden zu den einzelnen Orten unseres Organismus, wo sie verwen­det werden müssen, um ihn aufzubauen und zu formen, damit er Werkzeug unseres Ich sein kann.",
        "Das zeigt uns, daß schon von Anfang an bei der Ernährung alle Gesetze im Organismus des Men­schen liegen, die zuletzt zur Gestaltung des Blutkreislaufes führen."
      ],
      [
        "Das Blut als solches stellt sich uns nun dar als das beweglichste, als das regsamste aller unserer Systeme.",
        "Und wir wissen ja, wenn wir auch nur in geringem Maße irgendwie eingreifen in die Blutbahn, so nimmt das Blut sogleich andere Wege.",
        "Wir brauchen uns nur an irgendeiner Stelle zu stechen, so nimmt das Blut gleich einen anderen Weg als sonst.",
        "Das ist unendlich wichtig zu berücksichtigen, denn daraus können wir ersehen, daß das Blut das bestimmbarste Element im menschlichen Leibe ist.",
        "Es hat seine gute Unterlage an den ande­ren Organsystemen, aber es ist zugleich das aller bestimmbarste, das die wenigste innere Stetigkeit hat.",
        "Das Blut kann ungeheuer bestimmt werden durch die Erlebnisse des bewußten Ich.",
        "Ich will dabei nicht eingehen auf die phantastischen Theorien, die von seiten der äußeren Wissenschaft über das Erröten oder Erbleichen bei Scham- oder Angstgefühlen aufgestellt werden, ich will nur hinweisen auf die rein äußere Tatsache, daß solchen Erlebnissen wie Furcht oder Angst und Schamgefühl Ich-Erlebnisse zugrunde liegen, die in ihrer Wirkung auf"
      ],
      [
        "das Blut erkennbar sind.",
        "Beim Furcht- und Angstgefühl ist es so, daß wir uns gleichsam schützen wollen vor irgend etwas, von dem wir glauben, daß es gegen uns wirkt; wir zucken da gleichsam mit unse­rem Ich zurück.",
        "Beim Schamgefühl ist es so, daß wir uns am liebsten verstecken möchten, uns sozusagen hinter das Blut zurückziehen, unser Ich auslöschen möchten.",
        "Beide Male - ich will dabei nur auf die äußeren Tatsachen eingehen - folgt das Blut materiell, als äußeres materielles Werkzeug dem, was das Ich in sich erlebt.",
        "Beim Furcht­und Angstgefühl, wo der Mensch sich so stark in sich zurückziehen möchte vor etwas, von dem er sich bedroht fühlt, da wird er bleich; das Blut zieht sich zurück von der Oberfläche zum Zentrum, nach innen.",
        "Wenn sich der Mensch beim Schamgefühl verstecken möchte, sich auslöschen möchte, wenn er am liebsten nicht wäre und irgendwo hineinschlüpfen möchte, da drängt sich das Blut unter dem Eindrucke dessen, was das Ich erlebt, bis zur Peripherie des Organis­mus, und der Mensch wird rot.",
        "So sehen wir, daß das Blut das am leichtesten bestimmbare System im menschlichen Organismus ist und den Erlebnissen des Ich am schnellsten folgen kann."
      ],
      [
        "Je weiter wir hinunterrücken in unseren Organsystemen, desto weniger folgen die Anordnungen der Systeme unserem Ich, desto weniger sind sie geneigt, sich den Erlebnissen des Ich anzupassen.",
        "Was das Nervensystem anbelangt, so wissen wir, daß es angeordnet ist in bestimmten Nervenbahnen und daß diese in ihrem Verlauf etwas verhältnismäßig Festes darstellen.",
        "Während das Blut regsam ist und je nach den inneren Erlebnissen des Ich von einem Körperteil zum anderen bis in die Peripherie geführt werden kann, ist es bei den Nerven so, daß den Nervenbahnen entlang diejenigen Kräfte verlau­fen, welche wir als «Bewußtseinskräfte» zusammenfassen können, und daß diese nicht die Nervenmaterie von einem Orte zum anderen tragen können, wie das mit dem Blut in seinen Bahnen möglich ist.",
        "Das Nervensystem ist also schon weniger bestimmbar als das Blut; und noch weniger bestimmbar ist das Drüsensystem, das uns die Drüsen zeigt für ganz bestimmte Verrichtungen an ganz bestimmten Orten des Organismus.",
        "Wenn eine Drüse durch irgend etwas tätig gemacht werden soll zu einem bestimmten Zwecke, so kann sie nicht"
      ],
      [
        "erregt werden durch einen Strang ähnlich dem Nervenstrang, son­muß diese Drüse an dem Orte, wo sie eben ist, erregt werden.",
        "Es ist also das Drüsensystem noch weniger bestimmbar, wir mussen die Drüsen da erregen, wo sie sind.",
        "Während wir die Nerventätigkeit den Nervensträngen entlang leiten können - wir haben da noch Verbin­dungsfasern, welche die einzelnen Nervenknoten miteinander ver­binden -, kann die Drüse nur an dem Ort zu einer Tätigkeit erregt werden, wo sie ist.",
        "Noch mehr aber ist dieser gleichsam Verfesti­gungsprozeß, dieser Prozeß des inneren Bestimmtseins, des Nicht­Bestimmbarseins ausgesprochen in alle dem, was zum Ernährungs­system gehört, durch das der Mensch sich direkt die Stoffe eingliedert, um ein physisch-sinnliches Wesen zu sein.",
        "Dennoch muß in der Eigenart dieser Stoffeingliederung eine völlige Vorbereitung für das Werkzeug des Ich gegeben sein."
      ],
      [
        "Betrachten wir nun einmal den menschlichen Organismus in bezug auf sein unterstes System, das Ernährungssystem im umfassendsten Sinne, durch das die Stoffe nach allen Gliedern des Organismus transportiert werden, so muß die Anordnung dieser Stoffe so gesche­hen, daß die Formung, der äußere Aufbau des Menschen so vor sich gehen kann, daß zuletzt der Ausdruck des Ich im menschlichen Organismus möglich ist.",
        "Dazu ist vieles notwendig.",
        "Nicht nur, daß die Ernährungsstoffe in der verschiedensten Weise transportiert und an die verschiedensten Orte des Organismus gelagert werden, son­dern auch, daß alle möglichen Vorkehrungen getroffen werden, um die äußere Form des menschlichen Organismus zu bedingen."
      ],
      [
        "Nun ist es wichtig, daß wir uns folgendes klarmachen.",
        "In dem, was wir die Haut genannt haben, sind zwar alle Systeme des menschli­chen Organismus vertreten, bis zum untersten System, dem Ernäh­rungssystem, und wir konnten sagen: In die Haut wird alles ergos­sen, was im eminentesten Sinne zum physischen System des Men­schen gehört.",
        "Aber Sie können sich leicht denken, daß diese Haut -trotzdem sie alle diese Systeme in sich hat - für sich einen großen Fehler hat, so paradox das auch klingt.",
        "Sie hat zwar so wie sie am Menschen ist, die Form des menschlichen Organismus, diese Form würde sie aber durch sich selber nicht haben; durch sich selber würde"
      ],
      [
        "sie nicht in der Lage sein, dem Menschen seine charakteristische Formbegrenzung zu geben.",
        "Ohne Unterstützung würde die Haut in sich selber zusammensinken; da würde der Mensch sich nicht auf­recht halten können.",
        "Daraus sehen wir, daß nicht bloß diejenigen Ernährungsprozesse stattfinden müssen, welche die Haut erhalten, sondern es müssen auch die mannigfaltigsten anderen Prozesse statt­finden und zusammenwirken, welche die Gesamtform des Menschen-Organismus bilden.",
        "Da wird es uns nicht schwer sein zu begreifen, daß wir auch als solche umgewandelten Ernährungsprozesse diejeni­gen Prozesse anzusehen haben, die vor sich gehen in den Knorpeln und in den Knochen.",
        "Was sind das für Prozesse?"
      ],
      [
        "Wenn das Material unserer Nahrungsstoffe bis zu einem Knorpel oder Knochen geleitet wird, so ist im Grunde genommen auch nur physisches Material dahin transportiert.",
        "Was wir zuletzt im Knorpel oder Knochen finden, ist ja nichts anderes als die umgewandelten Nahrungsstoffe; aber sie sind in anderer Art umgewandelt als zum Beispiel in der Haut.",
        "Daher können wir sagen: Wir haben in der Haut zwar die umgewandelten Nahrungsstoffe zu sehen, die sich in der äußersten Formumgrenzung unseres Leibes ablagern.",
        "In der Art aber, wie im Knochen das Ernährungsmaterial abgelagert wird, haben wir einen solchen Ernährungsprozeß zu sehen, wo das Mate­rial sich rundet zur menschlichen Form.",
        "Es ist also ein umgekehrter Ernährungsprozeß wie derjenige in der menschlichen Haut.",
        "Nun wird es uns gar nicht mehr schwierig sein, gleichsam nach dem Muster der Betrachtungen, die wir für das Nervensystem angestellt haben, uns auch diesen gesamten Ernährungsprozeß, das Transpor­tierungssystem der Nahrungsmittel zu denken."
      ],
      [
        "Wenn wir die Haut anschauen und auf die Ernährungsstoffe sehen, welche sie zustande bringen, diesen äußeren Abschluß, der dem Menschen die Oberfläche gibt, aber niemals selber die menschliche Form hervorbringen könnte, so wird es uns klar sein, daß die Haut-ernährung die jüngste Art der Ernährung ist im Menschenorganis­mus; und wir erkennen, daß wir in der Art, wie die Knochen ernährt werden, einen analogen Prozeß zu sehen haben, der in einem ähnli­chen Verhältnis zur Hauternährung steht, wie wir den Prozeß der"
      ],
      [
        "Gehirnbildung in ein Verhältnis setzen konnten zum Prozeß der Rückenmarksbildung.",
        "Wir werden dasselbe Recht haben zu sagen:"
      ],
      [
        "Dasjenige, was wir zunächst äußerlich im Hauternährungsprozeß auftreten sehen, können wir auf einer späteren, das heißt hier höhe­ren Stufe umgewandelt sehen in der festen Form der Knochenbil­dung. - Es weist uns eine solche Betrachtung des menschlichen Organismus darauf hin, daß unser Knochensystem früher als weiche Substanz bestanden hat und sich erst im Laufe der Entwickelung verfestigt hat.",
        "Das kann auch durch die äußere Wissenschaft nachge­wiesen werden, die uns lehren kann, wie gewisse Gebilde, die später deutlich Knochen sind, im kindlichen Alter noch weich, knorpelhaft auftreten und daß erst nach und nach aus einer weicheren, knorpel-mäßigen Masse durch Einlagerung von Ernährungsmaterial sich die Knochenmasse bildet."
      ],
      [
        "Da haben wir ein Hinüberführen von einer weichen in eine festere Substanz, wie es auch beim einzelnen Men­schen sich vollzieht.",
        "Wir haben also im Knorpel eine Vorstufe des Knochens zu sehen und können sagen, daß uns die ganze Einlage­rung des Knochensystems in den Organismus als etwas erscheint, was sozusagen ein letztes Resultat derjenigen Prozesse darstellt, die uns in der Hauternährung vor Augen treten."
      ],
      [
        "Es werden also zuerst in einfachster Weise die Ernährungsstoffe umgewandelt zu einer wei­chen, biegsamen Substanz, und dann, wenn dies vorbereitet ist, kann der Ernährungsprozeß sich abspielen, durch den gewisse Teile sich erst verhärten zu Knochenmaterie, damit zuletzt die Form des menschlichen Gesamtorganismus zum Vorschein kommt.",
        "Die Art, wie uns die Knochen entgegentreten, gibt uns Anlaß zu sagen: Über die Knochenbildung hinaus haben wir eigentlich dann kein weiteres Fortschreiten der Ernährungsprozesse zur Verfestigung, soweit der Mensch der gegenwärtigen Entwickelungsstufe in Betracht kommt."
      ],
      [
        "Während wir auf der einen Seite im Blut die bestimmbarste, wand­lungsfähigste Substanz im Menschen haben, können wir andererseits in der Knochensubstanz dasjenige erblicken, was völlig unbestimm­bar ist, was bis zu einem letzten Punkte sich verhärtet, verfestigt hat, uber den hinaus es keine weitere Umwandlung mehr gibt; sie hat es bis zur starrsten Form gebracht.",
        "Wenn wir nun die früheren Betrachtungen"
      ],
      [
        "fortsetzen, dann müssen wir sagen: Das Blut ist das bestimm­barste Werkzeug des Ich im Menschen, die Nerven sind es schon weniger, die Drüsen noch weniger, und im Knochensystem haben wir das, was am letzten Punkte seiner Evolution angelangt ist, was ein letztes Umwandlungsprodukt darstellt in bezug auf die Bestimm­barkeit durch das Ich.",
        "Deshalb geschieht alles, was zur Formung des Knochensystems gehört, in der Weise, daß zuletzt die Knochen Träger und Stütze eines weicheren Organismus sein können, in wel­chem Lebens- und Ernährungsvorgänge so ablaufen, daß das Blut in seinen Bahnen in der rechten Weise verlaufen kann, damit das menschliche Ich in ihm ein Werkzeug haben kann."
      ],
      [
        "Ich möchte wissen, wer nicht mit höchster Bewunderung und Ehrfurcht erfüllt würde, wenn er hineinblickt in den menschlichen Organismus und sich vorzustellen versucht: Im Knochensystem habe ich dasjenige vor mir, was die meisten Verwandlungen, die meisten Stufen durchgemacht haben muß, was von den untersten Stufen aufgestiegen ist durch viele, viele Epochen hindurch bis zum heu­tigen Knochensystem; es ist zuletzt so gestaltet worden, daß es der feste Träger, die feste Stütze des Ich sein kann.",
        "Wenn man gewahr wird, wie bis in die Bildungen der einzelnen Knochen hinein die Tendenz des Ich wirkt, wer könnte da nicht mit tiefster Bewunde­rung erfüllt werden gegenüber diesem Bau des menschlichen Orga­nismus."
      ],
      [
        "Sehen wir diesen Menschen an, so haben wir zwei Pole des physi­schen Daseins gegeben, einmal im Blutsystem, das das bestimmbarste Werkzeug des Ich ist, und dann im Knochensystem, das in äußerer Form und innerer Struktur am meisten fest ist, am unbestimmbar­sten, am wenigsten wandlungsfähig, das in der Unbestimmbarkeit am weitesten vorgeschritten ist.",
        "Wir dürfen daher sagen: Im Knochen­system hat die physische Organisation des Menschen vorläufig ihren letzten Ausdruck, ihren Abschluß gefunden, während sie in dem Blutsystem in einem gewissen Sinne einen neuen Anfang genom­men hat.",
        "Schauen wir auf unser Knochensystem hin, so können wir sagen: Wir verehren in diesem Knochensystem einen letzten Ab­schluß der menschlichen physischen Organisation. - Und schauen"
      ],
      [
        "wir auf unser Blutsystem, so können wir sagen: Wir sehen in ihm einen Anfang, etwas, das erst anfangen konnte, nachdem alle ande­ren Systeme vorangegangen sind. - Vom Knochensystem können wir sagen: Eine gewisse erste Anlage, die ersten Kräfte zur Bil­dung des Knochensystems mußten schon vorhanden gewesen sein, bevor Drüsen- und Nervensystem im Organismus zur Entwicke­lung kamen, denn diese mußten durch das Knochensystem ihre ent­sprechenden Orte angewiesen erhalten.",
        "Das älteste der Kraft-systeme des menschlichen Organismus haben wir im Knochen-system in uns."
      ],
      [
        "Wenn wir nun das Blutsystem und das Knochensystem als zwei Pole bezeichnet haben, so wollten wir damit bildlich ausdrücken, daß in ihnen gleichsam die beiden äußersten Enden der menschlichen Organisation zu sehen sind.",
        "Im Blutsystem haben wir das beweglich­ste Element vor uns, das so regsam ist, daß es jeder Regung unseres Ich folgt."
      ],
      [
        "Und im Knochensystem haben wir dasjenige, was fast ganz dem Einfluß unseres Ich entzogen ist, wo wir nicht mehr hinunterrei­chen mit unserem Ich; dennoch aber liegt in seiner Form schon die ganze Organisation des Ich darinnen.",
        "Es stehen damit schon rein äußerlich betrachtet Blutsystem und Knochensystem im Menschen wie ein Anfang und ein Abschluß einander gegenüber."
      ],
      [
        "Und wenn wir so unser Blutsystem anschauen, das fortwährend allen Regungen des Ich folgt, so sagen wir uns: Im regsamen Blut drückt sich uns so recht das menschliche Leben aus. - Wenn wir auf unser Knochensystem schauen, sagen wir uns: Es symbolisiert alles das, was sich unserem Leben entzieht und dem Organismus nur als Stütze dient. - Unser pulsierendes Blut ist unser Leben; unser Knochensystem ist dasje­nige, was sich dem unmittelbaren Leben schon entzogen hat - weil es ein so alter Herr ist -, was sich schon ausgeschaltet hat und nur noch als Stütze dienen will, nur noch Form geben will.",
        "Während wir in unserem Blute am meisten organisch leben, sind wir im Grunde genommen in unserem Knochensystem schon gestorben."
      ],
      [
        "Und ich bitte Sie, diesen Ausspruch wie ein Leitmotiv für die folgenden Vorträge zu betrachten, denn es werden sich wichtige physiologische Dinge daraus ergeben.",
        "Während wir in unserem Blute leben, sind wir"
      ],
      [
        "in unserem Knochensystem eigentlich schon gestorben.",
        "Unser Kno­chensystem ist wie ein Gerüst, es ist das am wenigsten Lebendige, es ist nur das uns stützende Gerüst in uns."
      ],
      [
        "Wir haben schon am Anfang dieser Vortragsreihe im Menschen eine Zweiheit gesehen; jetzt tritt uns diese Zweiheit noch einmal in einer anderen Weise entgegen.",
        "Auf der einen Seite das Regsamste, Lebendigste im Blut, auf der anderen Seite etwas wie ein sich der organischen Regsamkeit am meisten Entziehendes, den Tod eigent­lich schon in sich Tragendes im Knochensystem."
      ],
      [
        "Unser Knochen-system hat einen gewissen Abschluß schon erhalten - in seiner Aus­formung wenigstens, wenn es auch nachher noch wächst - bis zu der Lebenszeit des Menschen, wo die Ich-Erlebnisse beginnen regsam zu werden.",
        "Bis zum Zahnwechsel im siebten Lebensjahr hat das Kno­chensystem sich im wesentlichen seine Form gegeben."
      ],
      [
        "Gerade in der Zeit also findet die Hauptentwickelung unseres Knochensystems statt, wo wir selber noch der Regsamkeit unseres Ich in hohem Maße entzogen sind.",
        "In dieser Zeit, wo das Knochensystem sich aufbaut aus den dunklen Untergründen und Kräften unseres Organismus heraus, können auch die meisten Fehler in der Ernährung gemacht werden."
      ],
      [
        "Gerade in diesen ersten sieben Lebensjahren können in der Ernährung des Kindes besonders folgenschwere Fehler gemacht wer­den, die sich auf das Knochensystem übel auswirken, zum Beispiel in rachitischen Erkrankungen, die namentlich davon herrühren, daß die Ernährungsprozesse in diesen Jahren nicht in der richtigen Weise geleitet werden, zum Beispiel wenn man der Naschhaftigkeit der Kinder nachgibt und ihnen alles mögliche gibt, wonach sie Verlangen tragen.",
        "So sehen wir das, was dem Ich entzogen ist, in unser Kno­chensystem hineinwirken."
      ],
      [
        "Ganz anders ist es beim Blutsystem, welches regsam folgt unserem einzelmenschlichen Leben und mehr als alles andere abhängig ist von den Prozessen unseres inneren Erlebens.",
        "Es ist nur eine Art von Kurzsichtigkeit seitens der äußeren Wissenschaft, zu glauben, daß von den inneren Erlebnissen das Nervensystem mehr abhängig wäre als das Blutsystem.",
        "Ich will nur darauf hinweisen, daß wir die ein­fachste Art der Beeinflussung des Blutsystems durch die Ich-Erlebnisse"
      ],
      [
        "in der Scham und in der Furcht haben, wo eine Umlagerung des Blutes stattfindet, die deutlich ausdrückt die Ich-Erlebnisse in dem Werkzeuge des Ich, dem Blut.",
        "Sie können sich also denken, wenn sich schon vorübergehende Prozesse so ausdrücken, wie sich dann dauernde oder gewohnheitsmäßige Erlebnisse des Ich ausdrücken mussen in dem erregsamen Elemente des Blutes.",
        "Es gibt keine Lei­denschaft, keinen Trieb oder Affekt, ob wir sie gewohnheitsmäßig haben oder ob sie explosionsartig zum Ausdruck kommen, die nicht als innere Erlebnisse übertragen werden auf das Blut als Instrument des Ich.",
        "Alle ungesunden Elemente des Ich-Erlebens kommen im Blutsystem zum Ausdruck."
      ],
      [
        "Und überall, wo wir irgend etwas verstehen wollen, was im Blut­system vorgeht, da ist es wichtig, nicht bloß zu fragen nach dem Ernährungsprozeß, sondern vielmehr nach den seelischen Prozessen zu suchen, insofern sie Ich-Erlebnisse sind, wie Stimmungen, dau­ernde Leidenschaften, Affekte und so weiter.",
        "Nur eine materialisti­sche Gesinnung wird bei Störungen im Blutsystem das Hauptaugen­merk auf die Ernährung lenken; denn die Bluternährung baut sich auf auf die Ernährung des physischen Systems, des Drüsensystems, des Nervensystems und so weiter, und im Grunde genommen sind die Nahrungsstoffe schon sehr filtriert, wenn sie an das Blut herankom­men.",
        "Wenn daher das Blut von dieser Seite her beeinträchtigt werden soll, muß schon eine ganz wesentliche Erkrankung des Organismus aufgetreten sein; dagegen wirken alle seelischen, alle Ich-Prozesse in unmittelbarer Weise auf das Blut zurück."
      ],
      [
        "So entzieht sich unser Knochensystem am meisten den Vorgängen unseres Ich, und so fügt sich unser Blutsystem am allermeisten den Vorgängen unseres Ich.",
        "Ja, dieses Knochensystem ist am allerwenig­sten veranlagt, dem Ich zu folgen, man möchte sagen, es ist ganz unabhängig vom Ich, aber doch ist es für das Ich organisiert."
      ],
      [
        "Nur ein kleiner Teil des Knochensystems macht von der Unbe­stimmbarkeit durch das Ich eine Ausnahme und zeigt eine individu­elle Prägung, nämlich die Schädelknochen, besonders der obere Teil des Schädels.",
        "Diese Tatsache hat zu verschiedenem Unfug Veranlas­sung gegeben."
      ],
      [
        "Sie wissen, daß es eine Phrenologie, eine Schädelknochenunter­suchung, gibt.",
        "Diese hat nach und nach, trotzdem sie von materiali­stischer Seite als Aberglaube angesehen wird, nach den allgemeinen Gepflogenheiten unserer Zeit eine materialistische Nuance angenom­men.",
        "Wenn wir grob charakterisieren wollen, können wir sagen: Im allgemeinen wird Phrenologie so beschrieben, daß in den Formen unserer Schädelbildung der Ausdruck gesucht wird für die innere Beschaffenheit unseres Ich, indem gleichsam allgemeine Gesichts­punkte aufgestellt werden und erklärt wird, der eine Höcker bedeute dies, der andere das und so weiter.",
        "Da will man die menschlichen Eigenschaften auffinden an den verschiedenen Höckern, die sich an unserem Schädel zeigen.",
        "In dem Knochensystem des Schädels wird also von der Phrenologie gesucht eine Art plastischer Ausdruck für unser Ich.",
        "Nun ist das aber, wenn es so getrieben wird, auch wenn scheinbar geistige Ausdrücke im Bau der einzelnen Knochen gesucht werden, doch ein Unfug.",
        "Denn wer wirklich ein feiner Beobachter ist, der weiß, daß kein einziger menschlicher Schädel dem anderen gleicht und daß man niemals Erhöhungen oder Vertiefungen an­geben könnte, die für diese oder jene Eigenschaft allgemein typisch sind, sondern daß ein jeder Schädel sich unterscheidet von dem an­deren, so daß wir bei jedem Menschenschädel andere Formen vor uns haben."
      ],
      [
        "Nun haben wir gesagt, daß sich unserem Ich, dem das Blut in seiner Regsamkeit am meisten folgt, der Knochenbau entzieht, ihm am wenigsten folgt.",
        "Es ist merkwürdig, daß uns dennoch die Bildung des Schädels und der Gesichtsknochen dem Ich entsprechend gestal­tet erscheinen, während der Knochenbau mehr allgemein typisch erscheint.",
        "Wer den Schädelbau betrachtet, der weiß: So wahr der Mensch selber individuell ist, so wahr ist auch sein Schädelbau individuell."
      ],
      [
        "Wie kommt es, daß diese wunderbare Konfiguration des Schädels von Anfang an der einzelnen menschlichen Individualität entspre­chend angelegt ist, wenn doch das Ich keinen Einfluß auf den Kno­chenbau hat?",
        "Woher kommt es, daß der Schädel, der sich so entwik­keIn muß, wie die anderen Knochen auch, anders ist bei jedem"
      ],
      [
        "Menschen?",
        "Woher kommt das?",
        "Das kommt einfach aus demselben Grunde, aus dem die individuellen Eigenschaften des Menschen sich überhaupt entwickeln, nämlich daher, daß das individuelle menschli­che Gesamtleben nicht nur verläuft von der Geburt bis zum Tode, sondern verläuft in vielen Inkarnationen.",
        "Während unser Ich also in der gegenwärtigen Inkarnation keinen Einfluß hat auf den Schädel-bau, hat es durch die Erlebnisse seiner vorangegangenen Inkarnation die Kräfte entwickelt, die in der Zeit zwischen dem Tode und der nächsten Geburt die Konfiguration des Schädelbaues, die Schädel-form, in dieser Inkarnation bestimmen.",
        "Wie das Ich in der vorherigen Inkarnation war, das bestimmt die Schädelform in der jetzigen Inkar­nation, so daß wir in dem Bau unseres Schädels einen äußeren plasti­schen Ausdruck haben für die Art und Weise, wie wir, jeder einzelne, als Individualität, in der vorhergehenden Inkarnation gelebt und gewirkt haben.",
        "Während alle anderen Knochen bei uns etwas Allge­mein-Menschliches ausdrücken, drückt der Schädel in seiner äußeren Form das aus, was wir waren und was wir getan haben in der vorigen Inkarnation."
      ],
      [
        "Das äußerst regsame Element des Blutes kann also bestimmt wer­den vom Ich in dieser Inkarnation.",
        "Unsere Knochen aber haben sich in dieser Inkarnation dem Einfluß des Ich schon ganz entzogen, bis auf den letzten Rest, den Schädelknochen, der aber dem Ich auch nicht mehr in dieser Inkarnation folgen kann.",
        "Der Schädelknochen, der aus der Weiche der Keimessubstanz heraus sich entwickelt hat, wo das Ich noch gestaltend einwirken konnte, gibt einen Ausdruck dafür, wie wir in der vorherigen Inkarnation waren.",
        "Eine allgemeine Phrenologie gibt es nicht.",
        "Wenn wir Phrenologie überhaupt in Betracht ziehen wollen, so darf sie keine schematisierende Wissen­schaft sein, sondern sie sollte auf eine künstlerische Art und Weise die plastischen Eigentümlichkeiten des Schädelbaues betrachten.",
        "Wir müssen unseren Schädelbau beurteilen wie ein Kunstwerk.",
        "Wir müs­sen allerdings in dem Schädelbau etwas Individuelles sehen, aber etwas Individuelles, das ein Ausdruck der Geschichte des Ich ist in einer vorhergehenden Inkarnation.",
        "So sehen wir, daß selbst diese Form des Knochenbaus, wie sie uns im Schädelbau entgegentritt,"
      ],
      [
        "dem Ich soweit entzogen ist, daß es in der gegenwärtigen Inkarnation darauf keinen Einfluß mehr hat.",
        "Aber es hat noch Einfluß darauf beim Durchgang zwischen Tod und neuer Geburt, wo es in gewissem Sinne die Kräfte wieder aufnimmt, die sich ihm im vergangenen Leben schon entzogen hatten und welche unter seinem Einfluß für das nächste Leben das Knochensystem und besonders den Schädel aufbauen."
      ],
      [
        "Wenn daher von der Wiederverkörperungsidee gesprochen und gesagt wird, das sei eine Sache, die sich im allgemeinen der Beurtei­lung durch unsere Vernunft entziehe, da müsse man eben das glau­ben, was der Geistesforscher sagt-, so ist das nicht richtig.",
        "Man kann darauf erwidern: Ihr könnt euch handgreiflich davon überzeugen, daß das menschliche Ich in einer vorhergehenden Inkarnation dage­wesen sein muß; im menschlichen Schädel hat man handgreiflich den Beweis vor sich, wie der Mensch in der vorhergehenden Inkarnation war."
      ],
      [
        "Wer das nicht zugibt, wer darin etwas Paradoxes sieht, daß man aus der Art, wie etwas äußerlich geformt ist, schließen muß auf etwas früher Lebendiges, das aus seinem früheren Leben heraus das Äußere geformt hat, der hat auch kein Recht, sonstwie auf ein früher Leben­diges zu schließen, wenn ihm irgendwo eine plastische Gestalt entge­gentritt.",
        "Wer nicht den Schluß zugibt als einen streng logischen, daß in der individuellen Schädelform, die wir haben, sich die Konfigura­tion des Ich aus früheren Inkarnationen ausdrückt, der hat auch kein Recht, wenn er zum Beispiel irgendwo auf der Erde eine leere Muschel findet, aus der äußeren Form dieser Muschel schließen zu wollen, daß da einmal ein Lebewesen drin war."
      ],
      [
        "Wer aus der toten Muschel schließen will auf ein Lebewesen, das einmal da drinnen war und die Muschel geformt hat, der darf den logisch ganz gleichwerti­gen Schluß nicht abweisen, daß in der individuellen Ausgestaltung unseres Schädels der unmittelbare Beweis gegeben ist für das Herein­wirken eines früheren Lebens in dieses Leben."
      ],
      [
        "So sehen Sie, daß wir hier eines der Tore haben, durch die wir physiologisch hineinleuchten können in die Reinkarnationsidee.",
        "Sol­che Tore gibt es viele; man muß sich nur Zeit lassen.",
        "Wenn man geduldig ist und wartet, dann wird man die Stellen finden, wo die"
      ],
      [
        "Beweise erbracht werden können und wie sie zu erbringen sind.",
        "Und wer leugnen wollte, daß in dem, was jetzt gesagt worden ist, Logik liegt, der müßte auch die gesamte Paläontologie leugnen, denn sie beruht auf denselben Schlußfolgerungen.",
        "So sehen wir, wie wir durch Eindringen in die Formen des menschlichen Organismus diesen auf seine geistigen Grundlagen zurückführen können."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "SIEBENTER VORTRAG Prag, 27. März 1911",
    "paragraphs": [
      "Wir haben im Verlaufe dieser Vorträge wohl den Eindruck bekom­men können, daß sich die verschiedenen Organsysteme und Gliede­rungen des menschlichen Organismus in der allerverschiedensten Weise beteiligen an dem Gesamtprozesse dieses menschlichen Orga­nismus. Wir haben auf verschiedenes in dieser Richtung hinweisen können und uns schon im Verlaufe der bisherigen Vorträge bemüßigt gesehen, die Tätigkeiten, die in den verschiedenen Organsystemen wirken, vorläufig einmal zuzuteilen höheren, übersinnlichen Glie­dern der menschlichen Organisation.",
      "So zum Beispiel mußten wir sagen, daß mit dem, was wir das menschliche Ich nennen, in einem innigen Zusammenhange steht der menschliche Blutkreislauf, so daß wir das Blut ansprechen konnten als ein Werkzeug des menschlichen Ich. Wir haben ferner das, was wir Bewußtseinsleben nennen, zutei­len können dem Nervensystem.",
      "Wir haben aber auch gezeigt, wie ein besonderer Teil des Nervensystems - das sympathische Nervensy­stern - in gewisser Weise eine entgegengesetzte Aufgabe hat wie der andere Teil des Nervensystems, eine Aufgabe, welche darin besteht, alles, was in den Tiefen des Organismus des Menschen sich abspielt, was hervorgerufen wird durch die Tätigkeit des inneren Weltsystems, sozusagen zurückzuhalten, so daß es bei normaler körperlicher Ver­fassung nicht bis zum Horizonte des Ich, also bis ins Tagesbewußt­sein heraufdringt. Wir haben gestern ferner versucht, wenigstens annähernd zu erkennen, daß sich dem bewußten Leben des Men­schen am meisten das entzieht, was sich in dem festen Knochengerüst aufbaut; wir haben aber doch betonen müssen, wie schon in diesem festen Knochengerüst des Menschen tätig sein muß ein solches Wesenhaftes, das zuletzt den Menschen fähig macht, das Organ seines bewußten Ich-Lebens, den Blutkreislauf, zu entfalten.",
      "So kön­nen wir auch sagen: die Einlagerung des menschlichen Knochen-systems bedeutet für den Gesamtorganismus des Menschen, daß er überhaupt eine menschliche Form erhalten kann und daß alles, was",
      "vorgeht innerhalb der Prozesse, die sich in dem festen Knochen­system abspielen, unterhalb der Schwelle des Bewußtseins gehalten wird. Immer haben wir es in der menschlichen Organisation mit etwas ähnlichem zu tun, nämlich damit - wir wollen uns insbeson­dere in diesem Punkte richtig verstehen -, daß das, was innerhalb dieser menschlichen Organisation ist, gleichsam behütet wird vor den Einflüssen, die in unserem Umkreise und in der großen Welt des Kosmos sich abspielen.",
      "Wir haben gesagt, daß die Glieder des inne­ren Weltsystems, jene sieben Organe, die gewissermaßen das äußere Planetensystem in unserem Innern spiegeln - insbesondere die Milz -, die äußeren Gesetze dessen, was wir als Nahrung aufnehmen, zurückhalten, gleichsam von diesen Gesetzen befreien, und daß die Nahrungsstoffe so in den menschlichen Organismus aufgenommen werden, daß sie sich als filtriert erweisen, so daß sie nicht in einer solchen Gestalt in den menschlichen Organismus hineinkommen, daß sie innerhalb desselben in einer eigenen Gesetzmäßigkeit und eigenen Regsamkeit walten können. In der, ich möchte sagen, gröb­sten Weise haben wir für den Menschen und die höheren Tiere dieses Behüten innerer Vorgänge gegenüber den äußeren Einflüssen ja schon in der Blutwärme gegeben.",
      "Diese Blutwärme, die innerhalb enger Temperaturgrenzen liegt, wird durch eine innere Gesetzmäßig­keit erhalten und ist unabhängig von den Wärmevorgängen des Makrokosmos, der großen Welt, die um uns herum sich abspielen. Hier haben Sie recht anschaulich eine Art von Grundphänomen in dieser Konstanz der Blutwärme.",
      "So müssen wir immer darauf hin­weisen, wie ein Wesentlichstes der inneren Organisation des Men­schen darin besteht, daß ein begrenztes Wesenhaftes abgeschlossen wird gegenüber dem Makrokosmos und seine eigenen Regsamkeiten entwickelt.",
      "Nun werden wir heute gut tun, um dem menschlichen Organismus noch weiter beizukommen, ein wenig von der anderen Seite auszu­gehen und auf das bewußte Leben einen kurzen Blick zu werfen. Wir wissen schon aus den vorhergehenden Vorträgen, wie das bewußte Leben des Menschen sich der Werkzeuge des Blutes und des Nerven­systems bedient, wir konnten aber noch nicht auf die feineren Vorgänge",
      "eingehen. Was ich jetzt sagen werde, ist etwas, was geeignet ist, die äußere Welt, die heute gebräuchliche Wissenschaft - das sei ganz offen gestanden - noch in hohem Grade zu schockieren. Aber ein jeder, der auf dem Boden des echten, wahren Okkultismus wahrhaft steht, wird Ihnen sagen, daß die Tendenz der Wissenschaft dahin geht, daß durch sie im Verlaufe von wenigen Dezennien aüch diejeni­gen Dinge bestätigt und anerkannt werden, die wir heute noch nur aus okkulten Beobachtungen heraus sagen können. Wenn ich statt einer so kurzen Reihe von Vorträgen ein halbes Jahr über diese Dinge hier sprechen könnte, so wäre es möglich, aus den Ergebnissen der heutigeri Wissenschaft alles das herbeizutragen, was geeignet ist, auch äußerlich zu belegen, was im heutigen Vortrag gesagt werden soll. Aber ich muß da manches schon dem eigenen guten Willen und den Fähigkeiten der verehrten Zuhörer überlassen. Es ist ja überall mög­lich, die Wege zu suchen zur äußeren Wissenschaft, die, wenn sie nicht von theoretischen Vorurteilen, sondern von den Tatsachen ausgeht, auch heute schon überall Bestätigungen finden kann für das, was auf dem Felde des Okkultismus gesagt wird. Ich bitte, alle diese Ausführungen in diesem Sinne zu nehmen.",
      "Wenn wir von unserem bewußten Leben ausgehen, namentlich wenn wir das Verhältnis unseres bewußten Seelenlebens zu unserem Organismus betrachten, ist es zunächst notwendig, alles das ins Auge zu fassen, was wir unsere Denktätigkeit im umfassendsten Sinne nennen. Wir brauchen uns dabei nicht einzulassen auf feinere logi­sche oder psychologische Unterscheidungen, wir brauchen uns zunächst nur vor unsere Seele zu stellen, daß wir es zu tun haben mit dem denkerischen Leben des Menschen, mit dem Gefühlsleben und mit dem Willensleben des Menschen.",
      "Nun werden Sie unter denjenigen, die auf dem Boden des wahren Okkultismus stehen, niemals einen Widerspruch finden, wenn gesagt wird, daß durch alle solche Prozesse, die sich in unserem Seelenleben im wachen Tagesbewußtsein abspielen und die unter die Kategorien des Denkerischen, des Gefühlsmäßigen oder des Willensimpulsrnäßi­gen fallen, im Organismus wirklich materielle - sei es belebte oder andere - Vorgänge bewirkt werden, so daß wir überall für ein jegliches,",
      "was in unserer Seele vorgeht, die entsprechenden materiellen Prozesse in unserem Organismus finden können. Das ist von aller­höchstem Interesse. Denn erst in unserer Zeit wird es aus gewissen Tendenzen, die erst heute in der Wissenschaft vorhanden sind, in den nächsten Jahrzehnten möglich sein, diese Entsprechungen von See­lenvorgängen und physiologischen Vorgängen im Organismus wirk­lich herauszufinden und das aus dem Okkultismus Gewonnene zu bestätigen.",
      "Jedem denkerischen Vorgange entspricht ein Vorgang in unserem Organismus, ebenso jedem Gefühlsvorgange und ebenso jedem Vor-gange, der mit dem Ausdruck Willensimpuls bezeichnet werden muß. Gleichsam könnten wir sagen: Wenn in unserem Seelenleben etwas vorgeht, wird eine Welle angeschlagen, die sich bis hinunter in den physischen Organismus fortpflanzt. - Nehmen wir zunächst den Vorgang des Denkens.",
      "Da ist es am besten, einen solchen Gedanken-prozeß ins Auge zu fassen, der wie das rein mathematische Denken oder ein ähnliches objektives Denken unsere Gefühle und unseren Willen unbeeinflußt läßt. Solche Gedankenprozesse, die denkerische Prozesse «in Reinkultur» sind, wollen wir zunächst ins Auge fassen.",
      "Was geht in unserem Organismus vor, wenn sich solche Gedanken-prozesse in unserem Seelenleben abspielen? Jedesmal, wenn wir den­ken, wenn wir Gedanken fassen, findet in unserem Organismus ein Prozeß statt, den wir vergleichen können - ich sage das nicht als Analogie, sondern als eine Tatsache, der Vergleich soll uns auf Tatsa­chen führen -, den wir vergleichen können mit dem Prozeß einer Kristallisation.",
      "Wenn wir in einem Glase Wasser haben, das bis zu einem gewissen Grade erwärmt ist, und darin irgendein Salz, Stein­salz zum Beispiel, aufgelöst haben und bringen nun durch Abküh­lung des Wassers dieses aufgelöste Salz zur Kristallisation, dann vollzieht sich der der Auflösung entgegengesetzte Prozeß. Wenn das Salz ganz aufgelöst ist, ist das Wasser durchsichtig.",
      "Wenn aber das Wasser wieder abgekühlt wird und der der Auflösung entgegenge­setzte Prozeß im Wasser sich vollzieht, dann wird das Salz wieder herauskristallisiert aus dem Wasser; es geschieht eine Salzrückbil­dung, eine Salzeinlagerung im Wasser. Der Prozeß stellt sich also so",
      "dar, daß wir sehen: In dem vorher warmen Wasser entsteht, wenn wir es abkühlen, ein Festes; es lagert sich im Flüssigen ein Festes ein, eine Salzablagerung. Wie gesagt, ich habe vorausgesetzt, daß durch die Angaben okkulter Resultate derjenige, der nur pedantisch im rein philiströsen Sinne die Tatsachen zugeben will, die von der Wissen­schaft registriert sind, zunächst schockiert werden kann.",
      "Ein ganz gleicher Prozeß spielt sich nun ab in unserem Organis­mus, wenn wir denken. Es ist der Prozeß des Denkens entsprechend einem Einlagerungsprozeß von Salzen, der ausgeht von einer Wir­kung unseres Blutes und der irritierend zurückwirkt auf unser Ner­vensystem, ein organischer Prozeß also, der sich abspielt an der Grenze unseres Blutes und unseres Nervensystems. Und geradeso, wie wir beim Anschauen des Wassers in dem Wasserglase das Aus­kristallisieren des Salzes beobachten können, so können wir sehen, wenn wir einen Menschen beobachten, der in der befriedigenden Lage ist zu denken, wie sich in der Tat - für das hellseherische Auge sehr genau übersinnlich wahrnehmbar - ein solcher Prozeß abspielt. So haben wir das physische Korrelat des Denkprozesses einmal vor unsere Seele hingestellt.",
      "Fragen wir uns jetzt: Wie nimmt sich das Entsprechende beim Fühlen aus? - Beim Fühlen haben wir es nicht mit einer Einlagerung von festwerdenden Salzen, also nicht mit einem umgekehrten Auflö­sungsprozeß zu tun, sondern es finden in unserem Organismus feine Prozesse statt, die sich etwa so abspielen, wie wenn ein Flüssiges halbfest wird. Denken Sie sich: Ein Flüssiges wird so halbfest wie etwa flüssiges Eiweiß, es koaguliert zur Konsistenz von verdicktem Eiweiß; also es findet ein Festwerden eines Flüssigen statt. Während wir es beim Denkprozeß zu tun haben mit einem Herausholen eines Festen, Salzartigen aus einem Flüssigen, das sich ablagert, haben wir es beim Gefühlsmäßigen zu tun mit einem Übergehen gewisser Teil­chen im Blut aus einem mehr flüssigen Zustand in einen dichteren Zustand. Die Substanz selber wird durch eine Art Gerinnung in einen dichteren Zustand gebracht. Dem hellseherischen Auge zeigt sich das wie ein Sichbilden kleiner Flöckchen, geradeso, wie Sie in einem Glase, in welchem eine bestimmte Flüssigkeit ist, durch",
      "bestimmte Vorgänge einen Prozeß innerer Flockenbildung bewirken können, ein Ausscheiden quellbarer kleiner Tröpfchen aus einer flüssigen Substanz.",
      "Wenn wir jetzt übergehen zu dem, was wir unsere Willensimpulse nennen können, so ist das physische Korrelat dafür wiederum anders. Das ist nun sogar leichter zu fassen, denn da kommen wir nach der Seite, wo die Sache schon etwas offenbarer wird. Der unseren Wil­lensimpulsen entsprechende physische Prozeß ist eine Art Erwär­mungsprozeß, der Temperaturerhöhungen im Organismus hervor­ruft, eine Art Heißwerden des Organismus in gewisser Beziehung. Da nun diese Erwärmung eng mit der ganzen Pulsation des Blutes zusammenhängt, so können wir sagen, daß die Willensimpulse mit einer Temperatursteigerung des Blutes verbunden sind. Dazu gehört nicht viel; wenn man nur einigermaßen Sinn hat für wirkliche Beob­achtungen, kann man auch schon am tierischen Organismus beob­achten, daß die Willensimpulse in der Erwärmung des Blutes ihr physisches Korrelat haben.",
      "So können wir die physischen Korrelate, die sich abspielen bei inneren, seelischen Vorgängen, einigermaßen charakterisieren. Was ich Ihnen jetzt charakterisiert habe, ist natürlich nicht etwas, was sich sehr im groben abspielt, sondern das sind außerordentlich feine, minuziöse Prozesse, Prozesse von einer Feinheit, von welcher man sich allerdings gewöhnlich gar keine Vorstellung machen kann. Aber mit Ausnahme der Erwärmungsprozesse spielen sich diese Prozesse so ab, daß sie in bezug auf alles, was wir an ähnlichen Prozessen in der äußeren physischen Welt kennen, eben eine ungeheure Feinheit darbieten. Alles dieses sind Prozesse, die der Organismus durch seine gesamten Kräfte ausführt, wenn das Ich in Tätigkeit ist, mit Hilfe des Instrumentes des Blutes. Von der Salzablagerung bis zur Quellbar­keit und zur Erwärmung spielen sich diese Prozesse so ab, daß der ganze Organismus ergriffen wird oder auch, zum Beispiel beim denkerischen Prozeß, hauptsächlich ein Teil unseres Organismus, Gehirn und Rückenmarksystem. In der mannigfaltigsten Weise im menschlichen Organismus verteilt sind diese Prozesse, welche Folgen der Einwirkung der seelischen Prozesse sind. Wenn man diese Dinge",
      "allmählich als Tatsachen kennenlernt, kommt man dahin, allerdings zugeben zu müssen, daß das, was man Gedanken oder Gefühle oder Willensimpulse nennt, reale Kräfte sind, die reale Wirkungen haben innerhalb des physischen Organismus und sich in realen Wirkungen aussprechen. Wir müssen rein aus der okkulten Beobachtung heraus sprechen von einer realen Wirkung der Seele auf den menschlichen Organismus. Es werden sich diese realen Wirkungen auf den menschlichen Organismus nach und nach in den folgenden Jahrzehn­ten der Wissenschaft schon enthüllen. Diese feinen Prozesse im Organismus werden den sorgfältigeren und subtileren Untersu­chungsmethoden der Wissenschaft schon zugänglich werden; und dann wird jenes Sträuben mehr und mehr von selber aufhören, das heute - nicht aus den Tatsachen, die die Wissenschaft erforscht hat, wohl aber aus gewissen vorurteilsvollen Theorien, die an diese Tatsa­chen sich anknüpfen - sich erhebt gegen Behauptungen, die aus der okkulten Erkenntnis gemacht werden können.",
      "Nun haben wir noch darauf hingewiesen, daß das, was wir als eine bewußte Tätigkeit des Ich auffassen, im Grunde genommen nur ein Teil der menschlichen Wesenheit ist und daß unter der Schwelle dessen, was auf diese Art in unseren Bewußtseinshorizont herein-dringt, Prozesse sich abspielen, die unterhalb des Bewußtseins liegen und die gleichsam ferngehalten werden von unserem Bewußtsein durch das sympathische Nervensystem. Wir haben von verschiede­nen Seiten her darauf hinweisen können, wie das, was wir dergestalt unbewußt in uns tragen, auch in einer gewissen Art im Zusammen-hange steht mit unserem Ich. Wir haben von dem Unbewußtesten, von unserem Knochensystem, gesagt, daß es von vornherein so orga­nisiert ist, daß es dem Werkzeuge des bewußten Ich geradezu die Grundlage geben kann. So wächst aus dem Unbewußten heraus eine unbewußte Ich-Organisation der bewußten Ich-Organisation entge­gen. Gleichsam teilt sich für uns der Mensch in zwei Teile: Es wirkt von der einen Seite her die bewußte Ich-Organisation und von der anderen Seite her die unbewußte Ich-Organisation in den Menschen hinein (siehe Zeichnung S.136). Wir haben in dieser Beziehung gese­hen, daß Blutsystem und Knochensystem einen gewissen Gegensatz",
      "# Bild s. 136",
      "bilden, sich wie entgegengesetzte Pole ausnehmen. Während das Blut in seiner inneren Regsamkeit als ein schmiegsames Werkzeug der Tätigkeit des Ich folgt, entzieht sich der andere Pol, das Knochensy­stem, der Regsamkeit des Ich so, daß von allem, was im Knochensy­stern geschieht, das Ich kein Bewußtsein hat, das heißt, daß alle im Knochensystem vorgehenden Prozesse vollständig unter der Ober­fläche der eigentlichen bewußten Ich-Geschehnisse ablaufen. Es sind zwar Prozesse, welche unserer Ich-Tätigkeit entsprechen, aber sie sind ebenso tot, wie unsere Blutprozesse lebendig sind; sie sind damit im Grunde genommen ein Teil solcher Prozesse, die dem Ich unbe­wußt bleiben, die sich nur stufenweise herauferheben aus dem Unbe­wußten zum Bewußtsein.",
      "Wenn wir das Knochensystem in seiner Gesamtfunktion im menschlichen Organismus einmal eingehend betrachten, so muß uns ja überall auffallen, daß es sich allem bewußten Leben entzieht, und zwar am stärksten von allen Organsystemen. Wenn wir aber nun vom Knochensystem übergehen zu den Organsystemen, die wir das innere Weltsystem des Menschen genannt haben, zum Leber-Galle­Milzsystem, zum Lungen-Herzsystem und so weiter, so müssen wir nach dem in den früheren Vorträgen hierüber Mitgeteilten sagen: In hohem Grade sind die Vorgänge innerhalb dieser Systeme auch unse­rem Bewußtsein entzogen, aber doch nicht ganz so, wie die Vorgänge in unserem Knochensystem. An unser Knochensystem brauchen wir",
      "doch viel weniger zu denken, auf dasselbe zu achten als auf die Organe, die eben genannt worden sind. Einige dieser genannten Organe geben sich dem Menschen sogar sehr deutlich in ihren Funk­tionen kund als etwas, was über das Unbewußte herausragt.",
      "Es ist etwa so, wie wenn ein Gegenstand, der im Wasser des Meeres schwimmt, teilweise heraufstößt und wie eine Insel über der Oberflä­che sichtbar wird. So dringt zum Beispiel manches von dem, was im Herzen vorgeht, in das Bewußtsein herauf.",
      "Sie wissen ja aus Erfah­rung, wie besonders hypochondrische Naturen - zu ihrem Schaden natürlich - etwas von den Dingen verspüren, die in ihren inneren Organen vorgehen, allerdings wird es ihnen ganz anders bewußt, als es drinnen vorgeht, aber sie empfinden es doch. Ich spreche jetzt nicht davon, wie es ist, wenn ein gewisser Grad von Erkrankung in den Organen schon eingetreten ist.",
      "Beim Krankwerden nämlich wird man sich der Organe bewußt; da liegt aber eine wirkliche Ursache vor, wodurch die Wirkungen der inneren Weltsysteme heraufsteigen bis in das Bewußtsein; sondern ich spreche davon, daß lange nicht diese Grenze erreicht zu werden braucht, welche ein gesunder Mensch gegenüber dem Kranksein hat. Diese Grenze verschiebt sich aber leider recht oft.",
      "Was oft schon als Krankheit angesprochen wird, kann durchaus als ein geringerer oder höherer Grad des Hinaufdrin­gens innerer Vorgänge in das Bewußtsein angesehen werden. Wir müssen also wirklich die Ursachen der verschiedenen Krankheiten immer so untersuchen, daß wir uns fragen: Liegen die Ursachen der Schmerzen in Krankheiten der Organe, oder haben wir sie anderswo zu suchen? - Wir wissen ja, daß wir vor dem Ins-Bewußtsein-Treten dessen, was sich da unten im Organismus abspielt, geschützt sind durch das sympathische Nervensystem.",
      "Wenn wir im Knochensystem etwas sehen, was den Menschen seiner Form, seiner Gestaltung nach so aufbaut, daß das Blutsystem darin in der entsprechenden Weise ein Werkzeug für sein Ich sein kann, so müssen wir uns nach dem, was eben jetzt gesagt worden ist, darüber klar sein, daß auch die anderen Organsysteme in einer gewis­sen Weise dem bewußten Leben des Menschen, das sich zuletzt wie eine Blüte entfalten soll, entgegenwachsen. Wir müssen uns klar sein,",
      "daß alle diese Organe auch schon, obwohl sie nicht durchdrungen sind von vollbewußtem Leben, das enthalten, was unserem bewußten Seelenleben entgegenwächst, so wie wir gesehen haben, daß unser Knochensystem entgegenwächst dem Ich-Leben.",
      "Wir müssen uns nun die Frage vorlegen: In welchem Grade wächst denn dieses innere System, das wir als ein inneres Weltsystem bezeichnet haben, dem bewußten Seelenleben des Menschen entge­gen? - Wenn wir auf der einen Seite bedenken, daß wir in dem Kno­chensystem die festeste Stütze in unserem physischen Körper haben, die dem Blutsystem so seine Anordnung gibt, daß es an den richtigen Orten wirkt, um sich als Werkzeug des Ich entfalten zu können, so mussen wir auf der anderen Seite auch sagen, daß das Knochensystem diejenigen Organe stützt und in der richtigen Lage hält, die wir früher als innere Weltsysteme bezeichnet haben. Denn was mit dem Blute geschieht, das kommt auch diesen Organen zugute.",
      "Wenn Sie alle diese Organsysteme betrachten, wird Ihnen auffallen, daß Sie in deren Anordnung nichts entdecken können, was so wesentlich und innig mit der äußeren Form des Menschen zusammenhängt wie das Knochensystem. Es ist die Grundlage der menschlichen Form, und was sich um das Knochensystem herum hineinbaut und auflagert, das kann sich nur so hineinbauen und auflagern, weil das Knochensystem die Grundform abgibt.",
      "Auch die Haut als äußere Körperbegrenzung ist gleichsam vorgebildet durch die ganze Gestaltung des Knochensy­stems. Goethe hat das in einem schönen Ausspruch gesagt, nicht bloß vom ästhetischen, sondern auch vom wissenschaftlichen Standpunkt aus: «Es ist nichts in der Haut, was nicht im Knochen ist.» Das heißt, in der äußeren Hautgestaltung drückt sich dasjenige aus, was schon durch das Knochensystem vorgebildet ist.",
      "Dasselbe können wir von unserem inneren Weltsystem nicht sagen. Andererseits zeigt aber gerade das Heraufrücken der Wirkungen des inneren Weltsystems zu niederen Graden des Bewußtseins, daß dieses innere Weltsystem etwas zu tun hat mit unserem Astralleib; denn der Astralleib ist der Träger des Bewußtseins.",
      "So müssen wir daher sagen, daß zwar dieses innere Weltsystem uns nicht erscheinen kann als ein Ausdruck des unterbewußten Ich, des in tiefen Untergründen gelegenen formbildenden",
      "Ich, daß es uns aber als das erscheinen kann, was uns durch den ganzen Weltenprozeß als Ausdruck der Umwelt so eingegliedert ist, daß es einen ähnlichen Bezug hat zu unserem Astralleib, wie das Knochensystem die Grundlage abgibt zu der das Ich umfassenden menschlichen Form. Wir können daher sagen: Wir haben im Kno­chensystem schon vorgebildet, tief unten im Unterbewußten, das menschliche Ich, und in dem, was wir unser inneres Weltsystem nennen, haben wir dasjenige vorgebildet, was wir unseren Astralleib nennen.",
      "Nun stammt dieses innere Weltsystem in seiner ganzen Organisa­tion, weil es eben noch unter dem Bewußtsein liegt, gar nicht aus dem bewußten Seelenleben; es ist unserem Organismus eingefügt aus dem Makrokosmos. Es ist also damit dem Menschen etwas, was wir ein kosmisches Astrales nennen können, so eingefügt, daß es sich aus­drückt als unser inneres Weltsystem. Und in unserem Knochensy­stern haben wir wiederum in unseren Organismus etwas eingegliedert bekommen aus unserer Umgebung, aus dem großen Weltsystem, und weil das zusammenhängt mit der gesamten Form unseres physischen Organismus, müssen wir sagen: Dieses Knochensystem ist eigentlich dadurch die Grundlage für unser Ich in unserem physischen Leib, weil es ein makrokosmisches oder schlechtweg ein kosmisches System ist, das uns zu diesem physisch gestalteten Menschen macht. Neben diesem Knochensystem wird uns eingelagert ein makrokos­misches astrales Weltsystem als unser inneres Weltsystem. Insofern unser Ich als bewußtes Ich auftritt, hat es zum Werkzeug das Blut-system, insofern unser Ich vorgebildet ist als Form und Gestalt, liegt ihm zugrunde ein kosmisches Kraftsystem, das hindrängt zur festen Gestaltung, das sich am dichtesten zum Ausdruck bringt in unserem Knochensystem.",
      "Fassen wir die Sache noch von einem anderen Gesichtspunkt ins Auge. Wir wissen ja jetzt, daß alles, was wir als bewußte Denktätig­keit, die vom Ich bewirkt wird, bezeichnet haben, sich zum Aus­druck bringt durch eine Art von feinster Salzablagerung im Blut. Es gibt sich also das bewußte Denken zu erkennen durch eine Art von innerer Salzablagerung. Wir können daher also erwarten, daß da, wo",
      "aus dem Kosmischen heraus unser Knochensystem vorgebildet wird, so daß der Organismus die materielle Stütze bilden kann für den Menschen als denkerisches Wesen, wir auch den physischen Prozeß einer Salzablagerung finden müßten. Wir müßten also Salzablagerun-gen im Knochensystem finden können; und tatsächlich bestehen die Knochen zum Teil aus phosphorsaurem und kohlensaurem Kalk, also aus abgelagerten Kalksalzen.",
      "So haben wir auch hier die beiden entgegengesetzten Pole. Indem der Mensch denkerisch tätig ist, sind die Gedankenprozesse dasje­nige, was uns innerlich zu einem festen Wesen macht. Unsere Gedan­ken sind in einer gewissen Weise unser inneres Knochengerüst.",
      "Der Mensch hat bestimmte scharfumrissene Gedanken; unsere Gefühle dagegen sind unbestimmt, lavierend, bei jedem Menschen mehr oder weniger anders. Die Gedanken bilden feste Einschlüsse im Gefühls­system.",
      "Während diese festen Einschlüsse im bewußten Leben sich ausdrücken im Blut durch eine Art von regsamem, beweglichem Salzablagerungsprozeß, drückt sich das, was das Ich vorbereitet, im Knochensystem so aus, daß der Makrokosmos unser Knochensystem so bildet, daß es zum größten Teil aus abgelagerten Salzen aufgebaut ist. Diese sind nun das ruhende Element in uns, der andere, der entgegengesetzte Pol zu den Vorgängen der inneren Regsamkeit, welche in den Salzablagerungsprozessen im Blut sich abspielen.",
      "So werden wir als Menschen von zwei Seiten her in unserer Organisa­tion zum Denker gemacht, von der einen Seite her unbewußt, indem unser Knochensystem aufgebaut wird, von der anderen Seite aus bewußt, indem wir - nach dem Muster unseres Knochenaufbaupro­zesses - dieselben Prozesse bewußt vollziehen, die sich im Organis­mus als solche Salzablagerungsprozesse zeigen, von denen wir sagen können, daß sie innerlich regsame sind. Die beim Denken gebildeten Salze müssen sogleich durch den Schlaf wieder aufgelöst, fortgeräumt werden, sonst würden sie etwas wie Zersetzungsprozesse, Auflö­sungsprozesse im Organismus herbeiführen.",
      "Wir haben also im Den­ken einen wirklichen Zerstörungsprozeß zu sehen. Und durch den wohltätigen Schlaf wird ein Rückbildungsprozeß ausgeübt, der bewirkt, daß das Blut wieder frei wird von Salzablagerungen, so",
      "daß wir von neuem bewußte Gedanken im wachen Tagesleben ent­wickeln können.",
      "Es geht aber nicht an, daß man nun einfach sagt: Denken ist ein Salzbildungsprozeß -, denn wenn die Menschen das nicht in der richtigen Weise verstehen, könnte wohl jemand sagen, die Geistes­wissenschaft behaupte das dümmste Zeug",
      "Gehen wir nun weiter. Wir können uns denken, daß zwischen diesen beiden äußersten Polen der Salzbildung sich alle anderen Prozesse im menschlichen Organismus abspielen, und zwar im wesentlichen diejenigen, auf die wir schon hingewiesen haben. Wie wir regsaine Salzbildungsprozesse haben durch das Denken, die ihren Gegenpol haben im Salzbildungsprozeß in den Knochen, der bis zu einem gewissen Grade zur Ruhe gekommen ist, so haben wir auch einen Gegenpol zu demjenigen, was wir bezeichnet haben als den innerlichen Quellungsprozeß, als Koagulation, als Flockenbildungs­prozeß, als etwas Ähnliches wie eiweißartige Einschlüsse, welche unter dem Einflusse unseres Gefühlslebens entstehen, als äußeren Ausdruck unseres Gefühlslebens. Dieser Gegenpol zeigt sich in dem, was mehr innere Prozesse unseres Organismus sind, und nimmt teil an einem solchen unbewußten Quellen, an einem Dichterwerden von Substanzen, welche sich bilden und einlagern als Wirkung des makrokosmischen Astralsystems. Es ist der Knochenleim, der teil­nimmt an dem Knochenbildungsprozeß und der den anderen Kno­chensubstanzen eingefügt wird. Das ist der andere Pol des Quel­lungsprozesses gegenüber dem, was als physisches Korrelat durch unser Gefühl entsteht.",
      "Unsere Willensimpulse drücken sich ja organisch in einem Wärme-prozeß, in einem inneren Erwärmungsprozeß aus. Verbindungen, die sich bilden und die wir bezeichnen können als Produkte innerer Verbrennungsprozesse, als innere Oxidationsprozesse, finden sich durch unseren ganzen Organismus hindurch. Und insofern sie unter der Schwelle des Bewußtseins verlaufen und nichts zu tun haben mit dem bewußten Leben, gehören sie der anderen Seite an, dem Gegen­pol, der abgeschlossen ist von dem, wovon das bewußte Leben Einflüsse erhalten kann. Dadurch ist der Mensch durch einen Teil",
      "seines Organismus innerlich geschützt vor Störungen, damit sich innerhalb desselben Prozesse vollziehen können, die von größter Zartheit sind, die von dem Seelenleben veranlaßt sind.",
      "Wie wir erfahren haben, finden also in unserem Organismus solche physiologische Vorgänge wie Salzbildung, Quellbildung und Wär­mebildung statt, die unserem bewußten Leben folgen, und solche Prozesse, die außerhalb unseres bewußten Lebens sich so abspielen, daß sie erst die Grundlage abgeben für das, was sich vorbereitet im menschlichen Organismus, damit das bewußte Leben sich überhaupt entfalten kann. So also ist unser gesamter Organismus ein Durchein­anderweben von Prozessen, die wir als unserem bewußten Leben zugehörig, und solchen, die wir als unserem unbewußten Leben zugehörig zu bezeichnen haben. Das ist eine außerordentlich bedeu­tungsvolle Tatsache, daß unser Organismus wirklich etwas darstellt wie ein Zusammengehöriges aus zwei Polaritäten: daß sich gleich­artige Prozesse einmal so vollziehen, daß sie hereinragen in den Organismus aus dem Makrokosmos und gleichsam im gröberen sich abspielen, und auf der anderen Seite solche Prozesse, welche als Folgen des bewußten Lebens des Menschen im feineren vor sich gehen können.",
      "Nun ist im heutigen fertigen Organismus die Sache so, daß alle diese Prozesse durchaus ineinanderspielen und daß wir sie, so wie der Organismus vor uns steht, nicht eigentlich so voneinander trennen können, daß wir überall bestimmte Grenzen zu bezeichnen vermöch­ten; der eine Prozeß spielt in den anderen hinein. Sie brauchen nur das Blutsystem, das regsamste, feinste Element zu betrachten. Im Blut sehen Sie sowohl den Erreger der Salzablagerungsprozesse wie auch der Prozesse der Koagulierung einer flüssigen Substanz und auch der Erwärmungsprozesse. In ähnlicher Art finden wir diese Prozesse auch bei anderen Organsystemen miteinander in enger Beziehung stehend. Wenn wir zum Beispiel Nahrungsmittel von außen in unseren Verdauungskanal aufnehmen, so haben diese Nah­rungsmittel noch das, was ich als ihre äußere Regsamkeit bezeichnet habe. Sie machen eine erste Stufe der Durchsiebung durch, indem sie aufgenommen werden im Munde und durch den Kauprozeß vorbereitet",
      "werden für den Verdauungsprozeß im Magen; in weiterer Stufenfolge werden sie verarbeitet durch die Organe, die wir als das innere Weltsystem bezeichnet haben, und endlich werden sie heran­geführt bis dahin, wo sie das feinste Instrument des menschlichen Organismus, das Blut, ernähren können. Nachdem wir so in gewisser Beziehung eine Stufenfolge der Durchsiebung der Nahrungsstoffe durch die inneren Organsysteme angedeutet haben, können wir uns jetzt leicht denken, daß in der Tat das feinste System, das Blutsystem, sozusagen die durchgesiebtesten Nahrungsregsamkeiten in sich auf­nehmen muß und daß das, was an das Blut herantritt, schon am allerwenigsten von demjenigen enthält, was die Nahrungsstoffe an eigener Regsamkeit in sich hatten, als sie aufgenommen wurden.",
      "Wenn die Stoffe aufgenommen werden, haben sie noch ein gut Teil ihrer eigenen Natur und Gesetzmäßigkeit. Sie haben diese im Magen und den weiteren Organsystemen, die sie passierten, aufgeben müs­sen, und soweit sie sich im Blut befinden, sind sie zu etwas vollstän­dig Neuem geworden.",
      "Daher ist das Blut auch dasjenige Organ, das am meisten von allen geschützt ist gegen die Eindrücke der Außen­welt, das seine Prozesse am meisten unabhängig von der Außenwelt vollzieht. Das ist die eine Seite; aber wir haben schon eingehend gezeigt, daß das Blut nach zwei Seiten sich wendet, daß es wie eine Tafel sowohl nach der einen wie nach der anderen Seite hin Ein­wirkungen ausgesetzt ist.",
      "Das Blut wird auf der einen Seite ja zu den­jenigen Organen in den tieferen Regionen des menschlichen Orga­nismus hingeführt, wo alles, was an Prozessen vorgeht, durch das sympathische Nervensystem zurückgehalten, abgewehrt wird, so daß es nicht zum Bewußtsein kommt. Nun muß das Blut sich ja auch der anderen Seite zuwenden, den Erlebnissen des bewußten Seelen­lebens.",
      "Es muß nicht nur die unbewußten Vorgänge aufnehmen, sondern es muß auch das bewußte Ich sich einprägen dem Blut. Unsere bewußten Seelentätigkeiten müssen sich so wandeln kön­nen, bis sie das Blut erreichen, damit sie in diesem Blute zum Aus­druck werden für das, was wir um uns haben.",
      "Was haben wir denn um uns? Die physisch-sinnliche Welt; denn das, was der Pflanzen­welt eingegliedert ist - der Ätherleib -, das ist für das normale",
      "Bewußtsein nicht da. Für das helle Tagesbewußtsein gehört der Mensch nur der physischen Welt an; die Lebenswelt ist für uns unsichtbar.",
      "So stehen wir mit der anderen Seite der Blutstafel der physisch-sinnlichen Welt gegenüber. Das ganze Seelenleben, wie es verläuft unter den Eindrücken der physisch-sinnlichen Welt, wie es zu Gedanken erregt wird, wie es zu Gefühlen entflammt wird, wie es zu Willensimpulsen angeregt wird, das muß alles im Blutsystem sein Werkzeug finden können, insofern es bewußtes Ich-Leben ist. Das alles muß im Blut pulsieren können. Was heißt das? Das heißt nichts anderes, als daß wir in unserem Blut nicht nur dasjenige haben dürfen, was aus den Nahrungsstoffen ist, nachdem sie in hohem Grade filtriert, ihrer Eigenregsamkeit enteignet, geschützt von allen makrokosmischen Gesetzen sind, sondern es muß - damit das Ein­schreiben auf die Blutstafel auch von der anderen Seite möglich ist -in dem Blut auch etwas zu finden sein, was verwandt ist mit dem Physisch-Sinnlichen, mit dem Unlebendigen der physisch-sinnlichen Welt. Was das Leben ausmacht, kann ja für das gewöhnliche Bewußt­sein nur durch Kombination der physisch-sinnlichen Eindrücke erkannt werden, in seiner Wirklichkeit kann es erst erkannt werden durch das unterste übersinnliche Glied der menschlichen Wesenheit, durch den Ätherleib.",
      "Das Blut muß also verwandt sein mit der physisch-sinnlichen Welt, so wie diese unmittelbar ist. Wir werden nun sehen, daß sich dem Blute etwas eingliedert, wovon wir sagen können: Das ist nun nicht so in unserem Blut, wie wenn es bestimmt würde durch die Prozesse, die aus unserem Wesen, aus den Tiefen unseres Organismus beraufdringen zum Blut, deren Gesetzmäßigkeit also der unsrigen angepaßt ist, sondern es ist so, als ob es durch die Wirkungen äußerer makrokosmischer Gesetzmäßigkeiten und Regsamkeiten unserem Blut eingegliedert würde. Wir müssen in unserem Blut etwas haben, was so ist und so wirkt wie unmittelbare äußere Prozesse, die aber innerlich sich geradeso abspielen wie äußerlich im Makrokosmos, die also ihre Eigengesetzmäßigkeit nicht verlieren. Es müssen also in unser Blut physische, chemische, anorganische Prozesse hineinspie­len;",
      "die sind notwendig, damit unser Ich Teilnehmer werden kann an der physischen Welt. Wir werden also in dem Blut solche Stoffe zu suchen haben, die so wirken können, daß ihr physischer Charakter, ihre Eigengesetzmäßigkeit beibehalten wird. Das finden wir in der Tat im Blut. In unseren roten Blutkörperchen ist uns etwas gegeben, das deutlich zeigt, daß es eben erst zu leben anfängt und an dem Punkte ist, wo es vom Leben in die Leblosigkeit übergeht. Auf der anderen Seite haben wir dem Blut eingegliedert einen fortwähren­den Erwärmungsprozeß, der sich vergleichen läßt mit einem äuße­ren Verbrennungsprozeß, wo der Oxidationsprozeß wieder neue Lebensmoglichkeiten gibt. Wir haben also dem Blute eingeordnet dasjenige, was den Menschen zu einem physisch-sinnlichen Wesen macht.",
      "So zeigt sich uns bis in die Organisation des Blutes hinein, wie bedeutsam die physische, die chemische Untersuchung erleuchtet werden kann durch das, was aus okkulter Anschauung mitgeteilt werden kann, und wie diese erst verständlich macht, was sich dem unmittelbaren äußeren Anblick darbietet.",
      "So können wir sagen: Wir haben im menschlichen Organismus, im Blut, Prozesse, die angeregt werden durch die Einwirkung der Außenwelt, die physisch-sinnlicher Art sind; wir haben außerdem aber auch solche Prozesse im Blut, die von der inneren Seite her heraufreichen und die auf der Einlagerung der bis zum äußersten Grade filtrierten und veränderten Nahrungsstoffe beruhen. Wenn wir das ins Auge fassen, so wird uns das Blut erst recht bedeutungs­voll als «ein ganz besonderer Saft» erscheinen, kehrt es doch auf der einen Seite seine Wesenheit dem niedersten, untersten uns bekannten Reiche zu und zeigt sich als eine Materie, die fähig ist, äußere chemi­sche Prozesse auszuführen, um dadurch ein Werkzeug sein zu kön­nen für das Ich. Auf der anderen Seite ist das Blut jene Substanz, die am geschütztesten ist, um innerliche Prozesse auszuführen, die sonst nirgends ausgeführt werden können, weil alle übrigen Organprozesse dazu als Voraussetzung notwendig sind.",
      "Die feinsten, die höchsten Prozesse, die angeregt werden aus den Tiefen unseres Organismus, verbinden sich in unserem Blut mit",
      "physikalisch-chemischen Prozessen, wie wir sie überall in der Welt vor Augen haben. In keiner anderen Substanz trifft so unmittelbar die physisch-sinnliche materielle Welt mit einer anderen, inneren Welt zusammen, die voraussetzt das Dasein, die Tätigkeit von über­sinnlichen Kraftsystemen, wie in unserer Blutsubstanz.",
      "Das tritt in keiner anderen Substanz so zutage wie in dem Blut, das unseren Organismus durchfließt. Dieses Blut ist in der Tat etwas, worin sich das Niederste, das der Mensch um sich herum schauen kann, zusam­menfügt mit dem Höchsten, das sich in seiner Natur organisch ausbilden kann.",
      "Daher wird es uns wohl klar sein, daß wir in bezug auf diese im Blut sich abspielenden komplizierten Vorgänge etwas vor uns haben, das, wenn es etwas unregelmäßig wird oder Störungen eintreten, in einem hohen Maße Unregelmäßigkeiten in unserem Gesamtorganismus hervorrufen muß. Und daß wir da, wo solche Unregelmäßigkeiten sich zeigen, immer überlegen müssen, wie diese entstanden sind.",
      "Es wird schwierig sein, auseinanderzuhalten, ob wir diese Unregelmäßigkeiten im einzelnen Falle solchen Prozessen zuzuschreiben haben, die nach dem Muster physischer chemischer Prozesse verlaufen, oder ob sie anderen Prozessen des Blutes entspre­chen. Wenn die Unregelmäßigkeiten verlaufen nach dem Muster physisch-chemischer Prozesse, dann müssen wir uns klar sein, daß ihnen begegnet werden muß von der Seite des Bewußtseins her, und zwar in dem Sinne, wie das Bewußtsein mit dem physischen Plan zusammenhängt.",
      "Hier eröffnet sich ein therapeutisches Gebiet, des­sen Charakteristisches ist, darauf zu achten, ob gewisse Unregel­mäßigkeiten zusammenhängen mit solchen Prozessen, die wir als physisch-chemische bezeichnen können. Bei dieser Voraussetzung ist es günstig, einzugreifen durcla äußere Impressionen, durch ent­sprechende Regelung der äußeren Eindrücke, welche diese phy­sisch-chemischen Prozesse hervorrufen können.",
      "Damit sind weniger seelisch-geistige Impressionen gemeint, dagegen namentlich alles dasjenige, was wir bewirken können durch eine Regelung des Atmungsprozesses und durch Überwachung der Prozesse der Wechselwirkung des inneren Organismus mit der Außenwelt durch die Haut.",
      "Dann können wir aber auch von der anderen Seite her im Blut die feinsten organischen Vorgänge feststellen, und wir werden uns klar sein müssen, daß wir darin sozusagen die dritte Stufe der Verfeine­rung unserer vorverarbeiteten Nahrungsstoffe zu sehen haben. Wenn im Blutorganismus jene feinen Prozesse der Salzbildung, der Quell­barkeit, der Wärme hervorgerufen werden durch äußere Vorgänge, also von außen in ihrem chemischen Verlauf bestimmt werden, so dürfen wir auf der anderen Seite fragen, wodurch die Prozesse im Blut von der inneren Seite her bestimmt werden.",
      "Wir müssen da unterscheiden zwischen der Aufgabe, die das Blut hat, und der Tat­sache, daß es so ernährt werden muß wie jedes andere Organ auch. Zugleich müssen wir es auch als das Organ erkennen, das auf der höchsten Stufe der organischen Tätigkeit steht.",
      "Es kommt hier dasje­nige in Betracht, was wir als die innerliche Stütze des menschlichen Lebens bezeichnen können. Das Blut muß vor allen Dingen davor geschützt werden, daß die äußere Welt auf dem Wege der Nahrungs­stoffe unmittelbar in das Blut hineinwirkt, es wird sonst seine Tätig­keit als Werkzeug unseres Denkens unterbunden, es wird der Vor­gang gestört, den wir als einen Prozeß der Salzablagerung früher bezeichnet haben.",
      "Dieser Schutz muß vom Blute selbst ausgehen; es muß imstande sein, nach der geistigen Seite hin gerichtet gleichsam ein geistiges Knochensystem aufzubauen durch die sich täglich wie­derholenden Salzablagerungsprozesse. Das ist eine Aufgabe des Blu­tes, die es unterscheidet von anderen Organen.",
      "Von den anderen Organen des menschlichen Organismus erhält es dabei am wenigsten Unterstützung. Am wenigsten spielen die anderen Organe in diesen Salzbildungsprozeß des Blutes herein, so daß das Blut in bezug auf die durch das Denken bedingten Prozesse am meisten verinnerlicht ist, wie ja in der Tat unsere Gedanken das Innerlichste sind, was wir haben.",
      "Mit unseren Gefühlen stehen wir an der Grenze von außen und innen, und mit seinen Willensimpulsen strömt der Mensch so stark nach außen, daß er sich unter Umständen gar nicht wiederer­kennt. In seinem Denken wird sich der Mensch immer wiedererken­nen, aber in seinen Willensimpulsen nicht.",
      "Daß es nicht so klar ist, wie die Willensimpulse entspringen, das können Sie schon daraus",
      "sehen, daß in bezug auf Freiheit und Unfreiheit des menschlichen Willens so viel in der Welt gestritten wird. In unserem Denken haben wir also das Innerlichste dessen, was das Blut als Werkzeug des Ich zu verrichten hat. Und weil nun der Prozeß der Salzablagerung am meisten verinnerlicht ist und auch am meisten geschützt sein muß, so kann durch Unregelmäßigkeiten oder Abnormitäten des Blutes auch diese Tätigkeit des Blutes am meisten behindert werden. Und wenn wir merken, daß das Blut so behindert ist, daß es nach dieser Rich­tung hin seine Tätigkeiten nicht mehr zeigt, so müssen wir uns darüber klar sein, daß es angeregt werden muß zu einer regelmäßigen Tätigkeit, wenn sein Eigenleben unter eine gewisse Grenze herunter-gesunken ist.",
      "Es kann aber auch der andere Fall eintreten, daß die innere Reg­samkeit des Blutes über ein gewisses Maß hinausgeht, daß dieses Eigenleben stürmischer wird. Das ist der weitaus wichtigere Fall, weil er bei Erkrankungen viel häufiger vorkommt. In den seltensten Fällen haben wir es mit dem Entgegengesetzten zu tun. Meist haben wir es damit zu tun, daß die Tätigkeit der sonst geschützten inneren Organe zu stark angeregt wird und in gleichem Sinne auf das Blut­system wirkt. Wenn sich das Blut so zeigt, daß es übermäßig nach der Richtung der Willenstätigkeit sich entfalten will, dann muß diesem Drang therapeutisch entgegengewirkt werden. Das können wir tun durch die Zuführung von solchen Substanzen, die zur normalen Salzbildung, zur normalen Salzablagerung im Sinne von seelisch-gedanklichen Prozessen führen. Das führt uns dazu einzusehen, daß ein gewisses System hineingebracht werden kann in die Art, wie wir solchen Unregelmäßigkeiten unseres Organismus entgegenwirken können. Es kann hier natürlich nur darauf hingewiesen werden, eine genauere Angabe würde über die Grenzen dieses Vortragszyklus hinausgehen.",
      "Wie wir Erkrankungen einer zu großen Regsamkeit im Blutsystem zuschreiben mußten, so können wir uns auch fragen, wie wir den Organen unserer inneren astralischen Welt, unseres inneren Welt-systems, Milz, Leber, Galle und so weiter, beikommen können, wenn sie in ihrer Tätigkeit in einer zu großen inneren Regsamkeit sind. Da",
      "müssen wir uns vor allen Dingen vor die Seele führen, daß diese Organe ja bestimmt sind, heraufzuwirken bis zur Blutzirkulation, daß sie die Nahrungsstoffe so zu übernehmen haben, wie sie vom Verdauungskanal zugeführt werden, und diese hinzuleiten haben in umgewandelter Regsamkeit bis zum Blut, daß sie also die Vermittler zwischen diesen beiden Systemen sind. Wie das Blutsystem sich als Werkzeug erweist der größten inneren Regsamkeit, des bewußten denkerischen Lebens, so wird es auch zu einer Tätigkeit angeregt, die sich als zusammenhängend zeigt mit unserem Gefühlsleben, das wir schon beschrieben haben als Prozeß des inneren Verdichtens, des inneren Quellens.",
      "Hier wird das Blut - abgesehen von äußeren Einwirkungen - angeregt von der Tätigkeit der inneren Weltsysteme, die in ihrer charakteristischen Eigenart ihre Wirkungen in das Blut hineinstrahlen können. Wir haben hier auf eine Tätigkeit im Blut hingewiesen, die schon über das Eigenleben des Blutes hinausgehen, deren Ursache aber dem inneren Weltsystem angehört.",
      "Wir können nun die Frage aufwerfen: Können nicht auch diese Organe - Leber, Galle, Milz, Nieren, Lunge, Herz - eine zu große Regsamkeit, ein überquellendes Leben und damit eine unregelmäßige Einwirkung auf das Blut entwickeln? Und wenn sie das tun, wie können wir -in ähnlicher Weise wie beim Blut - die zu große Regsamkeit dieser Organe therapeutisch paralysieren?",
      "Da müssen wir - da diese Organe in direktem Zusammenhang stehen mit dem kosmischen Astral­system - solche Stoffe zuführen, die die Regsamkeit des kosmischen Lebens entfalten. So wie wir durch Zuführen von salzhaltigen Stoffen die innere übertriebene Regsamkeit des Blutes verhindern können, so können wir die krankhafte Regsamkeit der inneren Organe abdämp­fen und ihr entgegenwirken, indem wir Stoffe zuführen, deren Ener­gie derjenigen der betreffenden Organe entspricht und die geeignet sind, sie wieder in Zusammenklang zu bringen mit der allgemeinen Gesetzmäßigkeit.",
      "Für uns entsteht also jetzt die Frage: Wie können wir auf diese Organe einwirken? Wie können wir den Unregelmäßigkeiten der einzelnen Organsysteme und auch dem Verdauungssystem beikom­men? Damit stellt sich die Frage überhaupt: Wie stellt sich uns ein",
      "Krankheitsbild im okkult-physiologischen Sinne dar, und wie sind die Krankheitserscheinungen zu heilen? - Wir werden morgen darauf zu antworten haben und dabei auch Rücksicht nehmen zum Beispiel auf das Muskelsystem. Unsere Betrachtungen werden darin ausklin­gen, daß wir zeigen, wie das, was als bewundernswerter fertiger Organismus uns entgegentritt, sich als werdender Organismus im Keimesleben deutlich ankündigt. Dann wird sich uns ganz von selbst ergeben, wie sich die übersinnlichen Glieder beteiligen an der menschlichen Organisation."
    ],
    "sentences": [
      [
        "Wir haben im Verlaufe dieser Vorträge wohl den Eindruck bekom­men können, daß sich die verschiedenen Organsysteme und Gliede­rungen des menschlichen Organismus in der allerverschiedensten Weise beteiligen an dem Gesamtprozesse dieses menschlichen Orga­nismus.",
        "Wir haben auf verschiedenes in dieser Richtung hinweisen können und uns schon im Verlaufe der bisherigen Vorträge bemüßigt gesehen, die Tätigkeiten, die in den verschiedenen Organsystemen wirken, vorläufig einmal zuzuteilen höheren, übersinnlichen Glie­dern der menschlichen Organisation."
      ],
      [
        "So zum Beispiel mußten wir sagen, daß mit dem, was wir das menschliche Ich nennen, in einem innigen Zusammenhange steht der menschliche Blutkreislauf, so daß wir das Blut ansprechen konnten als ein Werkzeug des menschlichen Ich.",
        "Wir haben ferner das, was wir Bewußtseinsleben nennen, zutei­len können dem Nervensystem."
      ],
      [
        "Wir haben aber auch gezeigt, wie ein besonderer Teil des Nervensystems - das sympathische Nervensy­stern - in gewisser Weise eine entgegengesetzte Aufgabe hat wie der andere Teil des Nervensystems, eine Aufgabe, welche darin besteht, alles, was in den Tiefen des Organismus des Menschen sich abspielt, was hervorgerufen wird durch die Tätigkeit des inneren Weltsystems, sozusagen zurückzuhalten, so daß es bei normaler körperlicher Ver­fassung nicht bis zum Horizonte des Ich, also bis ins Tagesbewußt­sein heraufdringt.",
        "Wir haben gestern ferner versucht, wenigstens annähernd zu erkennen, daß sich dem bewußten Leben des Men­schen am meisten das entzieht, was sich in dem festen Knochengerüst aufbaut; wir haben aber doch betonen müssen, wie schon in diesem festen Knochengerüst des Menschen tätig sein muß ein solches Wesenhaftes, das zuletzt den Menschen fähig macht, das Organ seines bewußten Ich-Lebens, den Blutkreislauf, zu entfalten."
      ],
      [
        "So kön­nen wir auch sagen: die Einlagerung des menschlichen Knochen-systems bedeutet für den Gesamtorganismus des Menschen, daß er überhaupt eine menschliche Form erhalten kann und daß alles, was"
      ],
      [
        "vorgeht innerhalb der Prozesse, die sich in dem festen Knochen­system abspielen, unterhalb der Schwelle des Bewußtseins gehalten wird.",
        "Immer haben wir es in der menschlichen Organisation mit etwas ähnlichem zu tun, nämlich damit - wir wollen uns insbeson­dere in diesem Punkte richtig verstehen -, daß das, was innerhalb dieser menschlichen Organisation ist, gleichsam behütet wird vor den Einflüssen, die in unserem Umkreise und in der großen Welt des Kosmos sich abspielen."
      ],
      [
        "Wir haben gesagt, daß die Glieder des inne­ren Weltsystems, jene sieben Organe, die gewissermaßen das äußere Planetensystem in unserem Innern spiegeln - insbesondere die Milz -, die äußeren Gesetze dessen, was wir als Nahrung aufnehmen, zurückhalten, gleichsam von diesen Gesetzen befreien, und daß die Nahrungsstoffe so in den menschlichen Organismus aufgenommen werden, daß sie sich als filtriert erweisen, so daß sie nicht in einer solchen Gestalt in den menschlichen Organismus hineinkommen, daß sie innerhalb desselben in einer eigenen Gesetzmäßigkeit und eigenen Regsamkeit walten können.",
        "In der, ich möchte sagen, gröb­sten Weise haben wir für den Menschen und die höheren Tiere dieses Behüten innerer Vorgänge gegenüber den äußeren Einflüssen ja schon in der Blutwärme gegeben."
      ],
      [
        "Diese Blutwärme, die innerhalb enger Temperaturgrenzen liegt, wird durch eine innere Gesetzmäßig­keit erhalten und ist unabhängig von den Wärmevorgängen des Makrokosmos, der großen Welt, die um uns herum sich abspielen.",
        "Hier haben Sie recht anschaulich eine Art von Grundphänomen in dieser Konstanz der Blutwärme."
      ],
      [
        "So müssen wir immer darauf hin­weisen, wie ein Wesentlichstes der inneren Organisation des Men­schen darin besteht, daß ein begrenztes Wesenhaftes abgeschlossen wird gegenüber dem Makrokosmos und seine eigenen Regsamkeiten entwickelt."
      ],
      [
        "Nun werden wir heute gut tun, um dem menschlichen Organismus noch weiter beizukommen, ein wenig von der anderen Seite auszu­gehen und auf das bewußte Leben einen kurzen Blick zu werfen.",
        "Wir wissen schon aus den vorhergehenden Vorträgen, wie das bewußte Leben des Menschen sich der Werkzeuge des Blutes und des Nerven­systems bedient, wir konnten aber noch nicht auf die feineren Vorgänge"
      ],
      [
        "eingehen.",
        "Was ich jetzt sagen werde, ist etwas, was geeignet ist, die äußere Welt, die heute gebräuchliche Wissenschaft - das sei ganz offen gestanden - noch in hohem Grade zu schockieren.",
        "Aber ein jeder, der auf dem Boden des echten, wahren Okkultismus wahrhaft steht, wird Ihnen sagen, daß die Tendenz der Wissenschaft dahin geht, daß durch sie im Verlaufe von wenigen Dezennien aüch diejeni­gen Dinge bestätigt und anerkannt werden, die wir heute noch nur aus okkulten Beobachtungen heraus sagen können.",
        "Wenn ich statt einer so kurzen Reihe von Vorträgen ein halbes Jahr über diese Dinge hier sprechen könnte, so wäre es möglich, aus den Ergebnissen der heutigeri Wissenschaft alles das herbeizutragen, was geeignet ist, auch äußerlich zu belegen, was im heutigen Vortrag gesagt werden soll.",
        "Aber ich muß da manches schon dem eigenen guten Willen und den Fähigkeiten der verehrten Zuhörer überlassen.",
        "Es ist ja überall mög­lich, die Wege zu suchen zur äußeren Wissenschaft, die, wenn sie nicht von theoretischen Vorurteilen, sondern von den Tatsachen ausgeht, auch heute schon überall Bestätigungen finden kann für das, was auf dem Felde des Okkultismus gesagt wird.",
        "Ich bitte, alle diese Ausführungen in diesem Sinne zu nehmen."
      ],
      [
        "Wenn wir von unserem bewußten Leben ausgehen, namentlich wenn wir das Verhältnis unseres bewußten Seelenlebens zu unserem Organismus betrachten, ist es zunächst notwendig, alles das ins Auge zu fassen, was wir unsere Denktätigkeit im umfassendsten Sinne nennen.",
        "Wir brauchen uns dabei nicht einzulassen auf feinere logi­sche oder psychologische Unterscheidungen, wir brauchen uns zunächst nur vor unsere Seele zu stellen, daß wir es zu tun haben mit dem denkerischen Leben des Menschen, mit dem Gefühlsleben und mit dem Willensleben des Menschen."
      ],
      [
        "Nun werden Sie unter denjenigen, die auf dem Boden des wahren Okkultismus stehen, niemals einen Widerspruch finden, wenn gesagt wird, daß durch alle solche Prozesse, die sich in unserem Seelenleben im wachen Tagesbewußtsein abspielen und die unter die Kategorien des Denkerischen, des Gefühlsmäßigen oder des Willensimpulsrnäßi­gen fallen, im Organismus wirklich materielle - sei es belebte oder andere - Vorgänge bewirkt werden, so daß wir überall für ein jegliches,"
      ],
      [
        "was in unserer Seele vorgeht, die entsprechenden materiellen Prozesse in unserem Organismus finden können.",
        "Das ist von aller­höchstem Interesse.",
        "Denn erst in unserer Zeit wird es aus gewissen Tendenzen, die erst heute in der Wissenschaft vorhanden sind, in den nächsten Jahrzehnten möglich sein, diese Entsprechungen von See­lenvorgängen und physiologischen Vorgängen im Organismus wirk­lich herauszufinden und das aus dem Okkultismus Gewonnene zu bestätigen."
      ],
      [
        "Jedem denkerischen Vorgange entspricht ein Vorgang in unserem Organismus, ebenso jedem Gefühlsvorgange und ebenso jedem Vor-gange, der mit dem Ausdruck Willensimpuls bezeichnet werden muß.",
        "Gleichsam könnten wir sagen: Wenn in unserem Seelenleben etwas vorgeht, wird eine Welle angeschlagen, die sich bis hinunter in den physischen Organismus fortpflanzt. - Nehmen wir zunächst den Vorgang des Denkens."
      ],
      [
        "Da ist es am besten, einen solchen Gedanken-prozeß ins Auge zu fassen, der wie das rein mathematische Denken oder ein ähnliches objektives Denken unsere Gefühle und unseren Willen unbeeinflußt läßt.",
        "Solche Gedankenprozesse, die denkerische Prozesse «in Reinkultur» sind, wollen wir zunächst ins Auge fassen."
      ],
      [
        "Was geht in unserem Organismus vor, wenn sich solche Gedanken-prozesse in unserem Seelenleben abspielen?",
        "Jedesmal, wenn wir den­ken, wenn wir Gedanken fassen, findet in unserem Organismus ein Prozeß statt, den wir vergleichen können - ich sage das nicht als Analogie, sondern als eine Tatsache, der Vergleich soll uns auf Tatsa­chen führen -, den wir vergleichen können mit dem Prozeß einer Kristallisation."
      ],
      [
        "Wenn wir in einem Glase Wasser haben, das bis zu einem gewissen Grade erwärmt ist, und darin irgendein Salz, Stein­salz zum Beispiel, aufgelöst haben und bringen nun durch Abküh­lung des Wassers dieses aufgelöste Salz zur Kristallisation, dann vollzieht sich der der Auflösung entgegengesetzte Prozeß.",
        "Wenn das Salz ganz aufgelöst ist, ist das Wasser durchsichtig."
      ],
      [
        "Wenn aber das Wasser wieder abgekühlt wird und der der Auflösung entgegenge­setzte Prozeß im Wasser sich vollzieht, dann wird das Salz wieder herauskristallisiert aus dem Wasser; es geschieht eine Salzrückbil­dung, eine Salzeinlagerung im Wasser.",
        "Der Prozeß stellt sich also so"
      ],
      [
        "dar, daß wir sehen: In dem vorher warmen Wasser entsteht, wenn wir es abkühlen, ein Festes; es lagert sich im Flüssigen ein Festes ein, eine Salzablagerung.",
        "Wie gesagt, ich habe vorausgesetzt, daß durch die Angaben okkulter Resultate derjenige, der nur pedantisch im rein philiströsen Sinne die Tatsachen zugeben will, die von der Wissen­schaft registriert sind, zunächst schockiert werden kann."
      ],
      [
        "Ein ganz gleicher Prozeß spielt sich nun ab in unserem Organis­mus, wenn wir denken.",
        "Es ist der Prozeß des Denkens entsprechend einem Einlagerungsprozeß von Salzen, der ausgeht von einer Wir­kung unseres Blutes und der irritierend zurückwirkt auf unser Ner­vensystem, ein organischer Prozeß also, der sich abspielt an der Grenze unseres Blutes und unseres Nervensystems.",
        "Und geradeso, wie wir beim Anschauen des Wassers in dem Wasserglase das Aus­kristallisieren des Salzes beobachten können, so können wir sehen, wenn wir einen Menschen beobachten, der in der befriedigenden Lage ist zu denken, wie sich in der Tat - für das hellseherische Auge sehr genau übersinnlich wahrnehmbar - ein solcher Prozeß abspielt.",
        "So haben wir das physische Korrelat des Denkprozesses einmal vor unsere Seele hingestellt."
      ],
      [
        "Fragen wir uns jetzt: Wie nimmt sich das Entsprechende beim Fühlen aus? - Beim Fühlen haben wir es nicht mit einer Einlagerung von festwerdenden Salzen, also nicht mit einem umgekehrten Auflö­sungsprozeß zu tun, sondern es finden in unserem Organismus feine Prozesse statt, die sich etwa so abspielen, wie wenn ein Flüssiges halbfest wird.",
        "Denken Sie sich: Ein Flüssiges wird so halbfest wie etwa flüssiges Eiweiß, es koaguliert zur Konsistenz von verdicktem Eiweiß; also es findet ein Festwerden eines Flüssigen statt.",
        "Während wir es beim Denkprozeß zu tun haben mit einem Herausholen eines Festen, Salzartigen aus einem Flüssigen, das sich ablagert, haben wir es beim Gefühlsmäßigen zu tun mit einem Übergehen gewisser Teil­chen im Blut aus einem mehr flüssigen Zustand in einen dichteren Zustand.",
        "Die Substanz selber wird durch eine Art Gerinnung in einen dichteren Zustand gebracht.",
        "Dem hellseherischen Auge zeigt sich das wie ein Sichbilden kleiner Flöckchen, geradeso, wie Sie in einem Glase, in welchem eine bestimmte Flüssigkeit ist, durch"
      ],
      [
        "bestimmte Vorgänge einen Prozeß innerer Flockenbildung bewirken können, ein Ausscheiden quellbarer kleiner Tröpfchen aus einer flüssigen Substanz."
      ],
      [
        "Wenn wir jetzt übergehen zu dem, was wir unsere Willensimpulse nennen können, so ist das physische Korrelat dafür wiederum anders.",
        "Das ist nun sogar leichter zu fassen, denn da kommen wir nach der Seite, wo die Sache schon etwas offenbarer wird.",
        "Der unseren Wil­lensimpulsen entsprechende physische Prozeß ist eine Art Erwär­mungsprozeß, der Temperaturerhöhungen im Organismus hervor­ruft, eine Art Heißwerden des Organismus in gewisser Beziehung.",
        "Da nun diese Erwärmung eng mit der ganzen Pulsation des Blutes zusammenhängt, so können wir sagen, daß die Willensimpulse mit einer Temperatursteigerung des Blutes verbunden sind.",
        "Dazu gehört nicht viel; wenn man nur einigermaßen Sinn hat für wirkliche Beob­achtungen, kann man auch schon am tierischen Organismus beob­achten, daß die Willensimpulse in der Erwärmung des Blutes ihr physisches Korrelat haben."
      ],
      [
        "So können wir die physischen Korrelate, die sich abspielen bei inneren, seelischen Vorgängen, einigermaßen charakterisieren.",
        "Was ich Ihnen jetzt charakterisiert habe, ist natürlich nicht etwas, was sich sehr im groben abspielt, sondern das sind außerordentlich feine, minuziöse Prozesse, Prozesse von einer Feinheit, von welcher man sich allerdings gewöhnlich gar keine Vorstellung machen kann.",
        "Aber mit Ausnahme der Erwärmungsprozesse spielen sich diese Prozesse so ab, daß sie in bezug auf alles, was wir an ähnlichen Prozessen in der äußeren physischen Welt kennen, eben eine ungeheure Feinheit darbieten.",
        "Alles dieses sind Prozesse, die der Organismus durch seine gesamten Kräfte ausführt, wenn das Ich in Tätigkeit ist, mit Hilfe des Instrumentes des Blutes.",
        "Von der Salzablagerung bis zur Quellbar­keit und zur Erwärmung spielen sich diese Prozesse so ab, daß der ganze Organismus ergriffen wird oder auch, zum Beispiel beim denkerischen Prozeß, hauptsächlich ein Teil unseres Organismus, Gehirn und Rückenmarksystem.",
        "In der mannigfaltigsten Weise im menschlichen Organismus verteilt sind diese Prozesse, welche Folgen der Einwirkung der seelischen Prozesse sind.",
        "Wenn man diese Dinge"
      ],
      [
        "allmählich als Tatsachen kennenlernt, kommt man dahin, allerdings zugeben zu müssen, daß das, was man Gedanken oder Gefühle oder Willensimpulse nennt, reale Kräfte sind, die reale Wirkungen haben innerhalb des physischen Organismus und sich in realen Wirkungen aussprechen.",
        "Wir müssen rein aus der okkulten Beobachtung heraus sprechen von einer realen Wirkung der Seele auf den menschlichen Organismus.",
        "Es werden sich diese realen Wirkungen auf den menschlichen Organismus nach und nach in den folgenden Jahrzehn­ten der Wissenschaft schon enthüllen.",
        "Diese feinen Prozesse im Organismus werden den sorgfältigeren und subtileren Untersu­chungsmethoden der Wissenschaft schon zugänglich werden; und dann wird jenes Sträuben mehr und mehr von selber aufhören, das heute - nicht aus den Tatsachen, die die Wissenschaft erforscht hat, wohl aber aus gewissen vorurteilsvollen Theorien, die an diese Tatsa­chen sich anknüpfen - sich erhebt gegen Behauptungen, die aus der okkulten Erkenntnis gemacht werden können."
      ],
      [
        "Nun haben wir noch darauf hingewiesen, daß das, was wir als eine bewußte Tätigkeit des Ich auffassen, im Grunde genommen nur ein Teil der menschlichen Wesenheit ist und daß unter der Schwelle dessen, was auf diese Art in unseren Bewußtseinshorizont herein-dringt, Prozesse sich abspielen, die unterhalb des Bewußtseins liegen und die gleichsam ferngehalten werden von unserem Bewußtsein durch das sympathische Nervensystem.",
        "Wir haben von verschiede­nen Seiten her darauf hinweisen können, wie das, was wir dergestalt unbewußt in uns tragen, auch in einer gewissen Art im Zusammen-hange steht mit unserem Ich.",
        "Wir haben von dem Unbewußtesten, von unserem Knochensystem, gesagt, daß es von vornherein so orga­nisiert ist, daß es dem Werkzeuge des bewußten Ich geradezu die Grundlage geben kann.",
        "So wächst aus dem Unbewußten heraus eine unbewußte Ich-Organisation der bewußten Ich-Organisation entge­gen.",
        "Gleichsam teilt sich für uns der Mensch in zwei Teile: Es wirkt von der einen Seite her die bewußte Ich-Organisation und von der anderen Seite her die unbewußte Ich-Organisation in den Menschen hinein (siehe Zeichnung S.136).",
        "Wir haben in dieser Beziehung gese­hen, daß Blutsystem und Knochensystem einen gewissen Gegensatz"
      ],
      [
        "# Bild s. 136"
      ],
      [
        "bilden, sich wie entgegengesetzte Pole ausnehmen.",
        "Während das Blut in seiner inneren Regsamkeit als ein schmiegsames Werkzeug der Tätigkeit des Ich folgt, entzieht sich der andere Pol, das Knochensy­stem, der Regsamkeit des Ich so, daß von allem, was im Knochensy­stern geschieht, das Ich kein Bewußtsein hat, das heißt, daß alle im Knochensystem vorgehenden Prozesse vollständig unter der Ober­fläche der eigentlichen bewußten Ich-Geschehnisse ablaufen.",
        "Es sind zwar Prozesse, welche unserer Ich-Tätigkeit entsprechen, aber sie sind ebenso tot, wie unsere Blutprozesse lebendig sind; sie sind damit im Grunde genommen ein Teil solcher Prozesse, die dem Ich unbe­wußt bleiben, die sich nur stufenweise herauferheben aus dem Unbe­wußten zum Bewußtsein."
      ],
      [
        "Wenn wir das Knochensystem in seiner Gesamtfunktion im menschlichen Organismus einmal eingehend betrachten, so muß uns ja überall auffallen, daß es sich allem bewußten Leben entzieht, und zwar am stärksten von allen Organsystemen.",
        "Wenn wir aber nun vom Knochensystem übergehen zu den Organsystemen, die wir das innere Weltsystem des Menschen genannt haben, zum Leber-Galle­Milzsystem, zum Lungen-Herzsystem und so weiter, so müssen wir nach dem in den früheren Vorträgen hierüber Mitgeteilten sagen: In hohem Grade sind die Vorgänge innerhalb dieser Systeme auch unse­rem Bewußtsein entzogen, aber doch nicht ganz so, wie die Vorgänge in unserem Knochensystem.",
        "An unser Knochensystem brauchen wir"
      ],
      [
        "doch viel weniger zu denken, auf dasselbe zu achten als auf die Organe, die eben genannt worden sind.",
        "Einige dieser genannten Organe geben sich dem Menschen sogar sehr deutlich in ihren Funk­tionen kund als etwas, was über das Unbewußte herausragt."
      ],
      [
        "Es ist etwa so, wie wenn ein Gegenstand, der im Wasser des Meeres schwimmt, teilweise heraufstößt und wie eine Insel über der Oberflä­che sichtbar wird.",
        "So dringt zum Beispiel manches von dem, was im Herzen vorgeht, in das Bewußtsein herauf."
      ],
      [
        "Sie wissen ja aus Erfah­rung, wie besonders hypochondrische Naturen - zu ihrem Schaden natürlich - etwas von den Dingen verspüren, die in ihren inneren Organen vorgehen, allerdings wird es ihnen ganz anders bewußt, als es drinnen vorgeht, aber sie empfinden es doch.",
        "Ich spreche jetzt nicht davon, wie es ist, wenn ein gewisser Grad von Erkrankung in den Organen schon eingetreten ist."
      ],
      [
        "Beim Krankwerden nämlich wird man sich der Organe bewußt; da liegt aber eine wirkliche Ursache vor, wodurch die Wirkungen der inneren Weltsysteme heraufsteigen bis in das Bewußtsein; sondern ich spreche davon, daß lange nicht diese Grenze erreicht zu werden braucht, welche ein gesunder Mensch gegenüber dem Kranksein hat.",
        "Diese Grenze verschiebt sich aber leider recht oft."
      ],
      [
        "Was oft schon als Krankheit angesprochen wird, kann durchaus als ein geringerer oder höherer Grad des Hinaufdrin­gens innerer Vorgänge in das Bewußtsein angesehen werden.",
        "Wir müssen also wirklich die Ursachen der verschiedenen Krankheiten immer so untersuchen, daß wir uns fragen: Liegen die Ursachen der Schmerzen in Krankheiten der Organe, oder haben wir sie anderswo zu suchen? - Wir wissen ja, daß wir vor dem Ins-Bewußtsein-Treten dessen, was sich da unten im Organismus abspielt, geschützt sind durch das sympathische Nervensystem."
      ],
      [
        "Wenn wir im Knochensystem etwas sehen, was den Menschen seiner Form, seiner Gestaltung nach so aufbaut, daß das Blutsystem darin in der entsprechenden Weise ein Werkzeug für sein Ich sein kann, so müssen wir uns nach dem, was eben jetzt gesagt worden ist, darüber klar sein, daß auch die anderen Organsysteme in einer gewis­sen Weise dem bewußten Leben des Menschen, das sich zuletzt wie eine Blüte entfalten soll, entgegenwachsen.",
        "Wir müssen uns klar sein,"
      ],
      [
        "daß alle diese Organe auch schon, obwohl sie nicht durchdrungen sind von vollbewußtem Leben, das enthalten, was unserem bewußten Seelenleben entgegenwächst, so wie wir gesehen haben, daß unser Knochensystem entgegenwächst dem Ich-Leben."
      ],
      [
        "Wir müssen uns nun die Frage vorlegen: In welchem Grade wächst denn dieses innere System, das wir als ein inneres Weltsystem bezeichnet haben, dem bewußten Seelenleben des Menschen entge­gen? - Wenn wir auf der einen Seite bedenken, daß wir in dem Kno­chensystem die festeste Stütze in unserem physischen Körper haben, die dem Blutsystem so seine Anordnung gibt, daß es an den richtigen Orten wirkt, um sich als Werkzeug des Ich entfalten zu können, so mussen wir auf der anderen Seite auch sagen, daß das Knochensystem diejenigen Organe stützt und in der richtigen Lage hält, die wir früher als innere Weltsysteme bezeichnet haben.",
        "Denn was mit dem Blute geschieht, das kommt auch diesen Organen zugute."
      ],
      [
        "Wenn Sie alle diese Organsysteme betrachten, wird Ihnen auffallen, daß Sie in deren Anordnung nichts entdecken können, was so wesentlich und innig mit der äußeren Form des Menschen zusammenhängt wie das Knochensystem.",
        "Es ist die Grundlage der menschlichen Form, und was sich um das Knochensystem herum hineinbaut und auflagert, das kann sich nur so hineinbauen und auflagern, weil das Knochensystem die Grundform abgibt."
      ],
      [
        "Auch die Haut als äußere Körperbegrenzung ist gleichsam vorgebildet durch die ganze Gestaltung des Knochensy­stems.",
        "Goethe hat das in einem schönen Ausspruch gesagt, nicht bloß vom ästhetischen, sondern auch vom wissenschaftlichen Standpunkt aus: «Es ist nichts in der Haut, was nicht im Knochen ist.» Das heißt, in der äußeren Hautgestaltung drückt sich dasjenige aus, was schon durch das Knochensystem vorgebildet ist."
      ],
      [
        "Dasselbe können wir von unserem inneren Weltsystem nicht sagen.",
        "Andererseits zeigt aber gerade das Heraufrücken der Wirkungen des inneren Weltsystems zu niederen Graden des Bewußtseins, daß dieses innere Weltsystem etwas zu tun hat mit unserem Astralleib; denn der Astralleib ist der Träger des Bewußtseins."
      ],
      [
        "So müssen wir daher sagen, daß zwar dieses innere Weltsystem uns nicht erscheinen kann als ein Ausdruck des unterbewußten Ich, des in tiefen Untergründen gelegenen formbildenden"
      ],
      [
        "Ich, daß es uns aber als das erscheinen kann, was uns durch den ganzen Weltenprozeß als Ausdruck der Umwelt so eingegliedert ist, daß es einen ähnlichen Bezug hat zu unserem Astralleib, wie das Knochensystem die Grundlage abgibt zu der das Ich umfassenden menschlichen Form.",
        "Wir können daher sagen: Wir haben im Kno­chensystem schon vorgebildet, tief unten im Unterbewußten, das menschliche Ich, und in dem, was wir unser inneres Weltsystem nennen, haben wir dasjenige vorgebildet, was wir unseren Astralleib nennen."
      ],
      [
        "Nun stammt dieses innere Weltsystem in seiner ganzen Organisa­tion, weil es eben noch unter dem Bewußtsein liegt, gar nicht aus dem bewußten Seelenleben; es ist unserem Organismus eingefügt aus dem Makrokosmos.",
        "Es ist also damit dem Menschen etwas, was wir ein kosmisches Astrales nennen können, so eingefügt, daß es sich aus­drückt als unser inneres Weltsystem.",
        "Und in unserem Knochensy­stern haben wir wiederum in unseren Organismus etwas eingegliedert bekommen aus unserer Umgebung, aus dem großen Weltsystem, und weil das zusammenhängt mit der gesamten Form unseres physischen Organismus, müssen wir sagen: Dieses Knochensystem ist eigentlich dadurch die Grundlage für unser Ich in unserem physischen Leib, weil es ein makrokosmisches oder schlechtweg ein kosmisches System ist, das uns zu diesem physisch gestalteten Menschen macht.",
        "Neben diesem Knochensystem wird uns eingelagert ein makrokos­misches astrales Weltsystem als unser inneres Weltsystem.",
        "Insofern unser Ich als bewußtes Ich auftritt, hat es zum Werkzeug das Blut-system, insofern unser Ich vorgebildet ist als Form und Gestalt, liegt ihm zugrunde ein kosmisches Kraftsystem, das hindrängt zur festen Gestaltung, das sich am dichtesten zum Ausdruck bringt in unserem Knochensystem."
      ],
      [
        "Fassen wir die Sache noch von einem anderen Gesichtspunkt ins Auge.",
        "Wir wissen ja jetzt, daß alles, was wir als bewußte Denktätig­keit, die vom Ich bewirkt wird, bezeichnet haben, sich zum Aus­druck bringt durch eine Art von feinster Salzablagerung im Blut.",
        "Es gibt sich also das bewußte Denken zu erkennen durch eine Art von innerer Salzablagerung.",
        "Wir können daher also erwarten, daß da, wo"
      ],
      [
        "aus dem Kosmischen heraus unser Knochensystem vorgebildet wird, so daß der Organismus die materielle Stütze bilden kann für den Menschen als denkerisches Wesen, wir auch den physischen Prozeß einer Salzablagerung finden müßten.",
        "Wir müßten also Salzablagerun-gen im Knochensystem finden können; und tatsächlich bestehen die Knochen zum Teil aus phosphorsaurem und kohlensaurem Kalk, also aus abgelagerten Kalksalzen."
      ],
      [
        "So haben wir auch hier die beiden entgegengesetzten Pole.",
        "Indem der Mensch denkerisch tätig ist, sind die Gedankenprozesse dasje­nige, was uns innerlich zu einem festen Wesen macht.",
        "Unsere Gedan­ken sind in einer gewissen Weise unser inneres Knochengerüst."
      ],
      [
        "Der Mensch hat bestimmte scharfumrissene Gedanken; unsere Gefühle dagegen sind unbestimmt, lavierend, bei jedem Menschen mehr oder weniger anders.",
        "Die Gedanken bilden feste Einschlüsse im Gefühls­system."
      ],
      [
        "Während diese festen Einschlüsse im bewußten Leben sich ausdrücken im Blut durch eine Art von regsamem, beweglichem Salzablagerungsprozeß, drückt sich das, was das Ich vorbereitet, im Knochensystem so aus, daß der Makrokosmos unser Knochensystem so bildet, daß es zum größten Teil aus abgelagerten Salzen aufgebaut ist.",
        "Diese sind nun das ruhende Element in uns, der andere, der entgegengesetzte Pol zu den Vorgängen der inneren Regsamkeit, welche in den Salzablagerungsprozessen im Blut sich abspielen."
      ],
      [
        "So werden wir als Menschen von zwei Seiten her in unserer Organisa­tion zum Denker gemacht, von der einen Seite her unbewußt, indem unser Knochensystem aufgebaut wird, von der anderen Seite aus bewußt, indem wir - nach dem Muster unseres Knochenaufbaupro­zesses - dieselben Prozesse bewußt vollziehen, die sich im Organis­mus als solche Salzablagerungsprozesse zeigen, von denen wir sagen können, daß sie innerlich regsame sind.",
        "Die beim Denken gebildeten Salze müssen sogleich durch den Schlaf wieder aufgelöst, fortgeräumt werden, sonst würden sie etwas wie Zersetzungsprozesse, Auflö­sungsprozesse im Organismus herbeiführen."
      ],
      [
        "Wir haben also im Den­ken einen wirklichen Zerstörungsprozeß zu sehen.",
        "Und durch den wohltätigen Schlaf wird ein Rückbildungsprozeß ausgeübt, der bewirkt, daß das Blut wieder frei wird von Salzablagerungen, so"
      ],
      [
        "daß wir von neuem bewußte Gedanken im wachen Tagesleben ent­wickeln können."
      ],
      [
        "Es geht aber nicht an, daß man nun einfach sagt: Denken ist ein Salzbildungsprozeß -, denn wenn die Menschen das nicht in der richtigen Weise verstehen, könnte wohl jemand sagen, die Geistes­wissenschaft behaupte das dümmste Zeug"
      ],
      [
        "Gehen wir nun weiter.",
        "Wir können uns denken, daß zwischen diesen beiden äußersten Polen der Salzbildung sich alle anderen Prozesse im menschlichen Organismus abspielen, und zwar im wesentlichen diejenigen, auf die wir schon hingewiesen haben.",
        "Wie wir regsaine Salzbildungsprozesse haben durch das Denken, die ihren Gegenpol haben im Salzbildungsprozeß in den Knochen, der bis zu einem gewissen Grade zur Ruhe gekommen ist, so haben wir auch einen Gegenpol zu demjenigen, was wir bezeichnet haben als den innerlichen Quellungsprozeß, als Koagulation, als Flockenbildungs­prozeß, als etwas Ähnliches wie eiweißartige Einschlüsse, welche unter dem Einflusse unseres Gefühlslebens entstehen, als äußeren Ausdruck unseres Gefühlslebens.",
        "Dieser Gegenpol zeigt sich in dem, was mehr innere Prozesse unseres Organismus sind, und nimmt teil an einem solchen unbewußten Quellen, an einem Dichterwerden von Substanzen, welche sich bilden und einlagern als Wirkung des makrokosmischen Astralsystems.",
        "Es ist der Knochenleim, der teil­nimmt an dem Knochenbildungsprozeß und der den anderen Kno­chensubstanzen eingefügt wird.",
        "Das ist der andere Pol des Quel­lungsprozesses gegenüber dem, was als physisches Korrelat durch unser Gefühl entsteht."
      ],
      [
        "Unsere Willensimpulse drücken sich ja organisch in einem Wärme-prozeß, in einem inneren Erwärmungsprozeß aus.",
        "Verbindungen, die sich bilden und die wir bezeichnen können als Produkte innerer Verbrennungsprozesse, als innere Oxidationsprozesse, finden sich durch unseren ganzen Organismus hindurch.",
        "Und insofern sie unter der Schwelle des Bewußtseins verlaufen und nichts zu tun haben mit dem bewußten Leben, gehören sie der anderen Seite an, dem Gegen­pol, der abgeschlossen ist von dem, wovon das bewußte Leben Einflüsse erhalten kann.",
        "Dadurch ist der Mensch durch einen Teil"
      ],
      [
        "seines Organismus innerlich geschützt vor Störungen, damit sich innerhalb desselben Prozesse vollziehen können, die von größter Zartheit sind, die von dem Seelenleben veranlaßt sind."
      ],
      [
        "Wie wir erfahren haben, finden also in unserem Organismus solche physiologische Vorgänge wie Salzbildung, Quellbildung und Wär­mebildung statt, die unserem bewußten Leben folgen, und solche Prozesse, die außerhalb unseres bewußten Lebens sich so abspielen, daß sie erst die Grundlage abgeben für das, was sich vorbereitet im menschlichen Organismus, damit das bewußte Leben sich überhaupt entfalten kann.",
        "So also ist unser gesamter Organismus ein Durchein­anderweben von Prozessen, die wir als unserem bewußten Leben zugehörig, und solchen, die wir als unserem unbewußten Leben zugehörig zu bezeichnen haben.",
        "Das ist eine außerordentlich bedeu­tungsvolle Tatsache, daß unser Organismus wirklich etwas darstellt wie ein Zusammengehöriges aus zwei Polaritäten: daß sich gleich­artige Prozesse einmal so vollziehen, daß sie hereinragen in den Organismus aus dem Makrokosmos und gleichsam im gröberen sich abspielen, und auf der anderen Seite solche Prozesse, welche als Folgen des bewußten Lebens des Menschen im feineren vor sich gehen können."
      ],
      [
        "Nun ist im heutigen fertigen Organismus die Sache so, daß alle diese Prozesse durchaus ineinanderspielen und daß wir sie, so wie der Organismus vor uns steht, nicht eigentlich so voneinander trennen können, daß wir überall bestimmte Grenzen zu bezeichnen vermöch­ten; der eine Prozeß spielt in den anderen hinein.",
        "Sie brauchen nur das Blutsystem, das regsamste, feinste Element zu betrachten.",
        "Im Blut sehen Sie sowohl den Erreger der Salzablagerungsprozesse wie auch der Prozesse der Koagulierung einer flüssigen Substanz und auch der Erwärmungsprozesse.",
        "In ähnlicher Art finden wir diese Prozesse auch bei anderen Organsystemen miteinander in enger Beziehung stehend.",
        "Wenn wir zum Beispiel Nahrungsmittel von außen in unseren Verdauungskanal aufnehmen, so haben diese Nah­rungsmittel noch das, was ich als ihre äußere Regsamkeit bezeichnet habe.",
        "Sie machen eine erste Stufe der Durchsiebung durch, indem sie aufgenommen werden im Munde und durch den Kauprozeß vorbereitet"
      ],
      [
        "werden für den Verdauungsprozeß im Magen; in weiterer Stufenfolge werden sie verarbeitet durch die Organe, die wir als das innere Weltsystem bezeichnet haben, und endlich werden sie heran­geführt bis dahin, wo sie das feinste Instrument des menschlichen Organismus, das Blut, ernähren können.",
        "Nachdem wir so in gewisser Beziehung eine Stufenfolge der Durchsiebung der Nahrungsstoffe durch die inneren Organsysteme angedeutet haben, können wir uns jetzt leicht denken, daß in der Tat das feinste System, das Blutsystem, sozusagen die durchgesiebtesten Nahrungsregsamkeiten in sich auf­nehmen muß und daß das, was an das Blut herantritt, schon am allerwenigsten von demjenigen enthält, was die Nahrungsstoffe an eigener Regsamkeit in sich hatten, als sie aufgenommen wurden."
      ],
      [
        "Wenn die Stoffe aufgenommen werden, haben sie noch ein gut Teil ihrer eigenen Natur und Gesetzmäßigkeit.",
        "Sie haben diese im Magen und den weiteren Organsystemen, die sie passierten, aufgeben müs­sen, und soweit sie sich im Blut befinden, sind sie zu etwas vollstän­dig Neuem geworden."
      ],
      [
        "Daher ist das Blut auch dasjenige Organ, das am meisten von allen geschützt ist gegen die Eindrücke der Außen­welt, das seine Prozesse am meisten unabhängig von der Außenwelt vollzieht.",
        "Das ist die eine Seite; aber wir haben schon eingehend gezeigt, daß das Blut nach zwei Seiten sich wendet, daß es wie eine Tafel sowohl nach der einen wie nach der anderen Seite hin Ein­wirkungen ausgesetzt ist."
      ],
      [
        "Das Blut wird auf der einen Seite ja zu den­jenigen Organen in den tieferen Regionen des menschlichen Orga­nismus hingeführt, wo alles, was an Prozessen vorgeht, durch das sympathische Nervensystem zurückgehalten, abgewehrt wird, so daß es nicht zum Bewußtsein kommt.",
        "Nun muß das Blut sich ja auch der anderen Seite zuwenden, den Erlebnissen des bewußten Seelen­lebens."
      ],
      [
        "Es muß nicht nur die unbewußten Vorgänge aufnehmen, sondern es muß auch das bewußte Ich sich einprägen dem Blut.",
        "Unsere bewußten Seelentätigkeiten müssen sich so wandeln kön­nen, bis sie das Blut erreichen, damit sie in diesem Blute zum Aus­druck werden für das, was wir um uns haben."
      ],
      [
        "Was haben wir denn um uns?",
        "Die physisch-sinnliche Welt; denn das, was der Pflanzen­welt eingegliedert ist - der Ätherleib -, das ist für das normale"
      ],
      [
        "Bewußtsein nicht da.",
        "Für das helle Tagesbewußtsein gehört der Mensch nur der physischen Welt an; die Lebenswelt ist für uns unsichtbar."
      ],
      [
        "So stehen wir mit der anderen Seite der Blutstafel der physisch-sinnlichen Welt gegenüber.",
        "Das ganze Seelenleben, wie es verläuft unter den Eindrücken der physisch-sinnlichen Welt, wie es zu Gedanken erregt wird, wie es zu Gefühlen entflammt wird, wie es zu Willensimpulsen angeregt wird, das muß alles im Blutsystem sein Werkzeug finden können, insofern es bewußtes Ich-Leben ist.",
        "Das alles muß im Blut pulsieren können.",
        "Was heißt das?",
        "Das heißt nichts anderes, als daß wir in unserem Blut nicht nur dasjenige haben dürfen, was aus den Nahrungsstoffen ist, nachdem sie in hohem Grade filtriert, ihrer Eigenregsamkeit enteignet, geschützt von allen makrokosmischen Gesetzen sind, sondern es muß - damit das Ein­schreiben auf die Blutstafel auch von der anderen Seite möglich ist -in dem Blut auch etwas zu finden sein, was verwandt ist mit dem Physisch-Sinnlichen, mit dem Unlebendigen der physisch-sinnlichen Welt.",
        "Was das Leben ausmacht, kann ja für das gewöhnliche Bewußt­sein nur durch Kombination der physisch-sinnlichen Eindrücke erkannt werden, in seiner Wirklichkeit kann es erst erkannt werden durch das unterste übersinnliche Glied der menschlichen Wesenheit, durch den Ätherleib."
      ],
      [
        "Das Blut muß also verwandt sein mit der physisch-sinnlichen Welt, so wie diese unmittelbar ist.",
        "Wir werden nun sehen, daß sich dem Blute etwas eingliedert, wovon wir sagen können: Das ist nun nicht so in unserem Blut, wie wenn es bestimmt würde durch die Prozesse, die aus unserem Wesen, aus den Tiefen unseres Organismus beraufdringen zum Blut, deren Gesetzmäßigkeit also der unsrigen angepaßt ist, sondern es ist so, als ob es durch die Wirkungen äußerer makrokosmischer Gesetzmäßigkeiten und Regsamkeiten unserem Blut eingegliedert würde.",
        "Wir müssen in unserem Blut etwas haben, was so ist und so wirkt wie unmittelbare äußere Prozesse, die aber innerlich sich geradeso abspielen wie äußerlich im Makrokosmos, die also ihre Eigengesetzmäßigkeit nicht verlieren.",
        "Es müssen also in unser Blut physische, chemische, anorganische Prozesse hineinspie­len;"
      ],
      [
        "die sind notwendig, damit unser Ich Teilnehmer werden kann an der physischen Welt.",
        "Wir werden also in dem Blut solche Stoffe zu suchen haben, die so wirken können, daß ihr physischer Charakter, ihre Eigengesetzmäßigkeit beibehalten wird.",
        "Das finden wir in der Tat im Blut.",
        "In unseren roten Blutkörperchen ist uns etwas gegeben, das deutlich zeigt, daß es eben erst zu leben anfängt und an dem Punkte ist, wo es vom Leben in die Leblosigkeit übergeht.",
        "Auf der anderen Seite haben wir dem Blut eingegliedert einen fortwähren­den Erwärmungsprozeß, der sich vergleichen läßt mit einem äuße­ren Verbrennungsprozeß, wo der Oxidationsprozeß wieder neue Lebensmoglichkeiten gibt.",
        "Wir haben also dem Blute eingeordnet dasjenige, was den Menschen zu einem physisch-sinnlichen Wesen macht."
      ],
      [
        "So zeigt sich uns bis in die Organisation des Blutes hinein, wie bedeutsam die physische, die chemische Untersuchung erleuchtet werden kann durch das, was aus okkulter Anschauung mitgeteilt werden kann, und wie diese erst verständlich macht, was sich dem unmittelbaren äußeren Anblick darbietet."
      ],
      [
        "So können wir sagen: Wir haben im menschlichen Organismus, im Blut, Prozesse, die angeregt werden durch die Einwirkung der Außenwelt, die physisch-sinnlicher Art sind; wir haben außerdem aber auch solche Prozesse im Blut, die von der inneren Seite her heraufreichen und die auf der Einlagerung der bis zum äußersten Grade filtrierten und veränderten Nahrungsstoffe beruhen.",
        "Wenn wir das ins Auge fassen, so wird uns das Blut erst recht bedeutungs­voll als «ein ganz besonderer Saft» erscheinen, kehrt es doch auf der einen Seite seine Wesenheit dem niedersten, untersten uns bekannten Reiche zu und zeigt sich als eine Materie, die fähig ist, äußere chemi­sche Prozesse auszuführen, um dadurch ein Werkzeug sein zu kön­nen für das Ich.",
        "Auf der anderen Seite ist das Blut jene Substanz, die am geschütztesten ist, um innerliche Prozesse auszuführen, die sonst nirgends ausgeführt werden können, weil alle übrigen Organprozesse dazu als Voraussetzung notwendig sind."
      ],
      [
        "Die feinsten, die höchsten Prozesse, die angeregt werden aus den Tiefen unseres Organismus, verbinden sich in unserem Blut mit"
      ],
      [
        "physikalisch-chemischen Prozessen, wie wir sie überall in der Welt vor Augen haben.",
        "In keiner anderen Substanz trifft so unmittelbar die physisch-sinnliche materielle Welt mit einer anderen, inneren Welt zusammen, die voraussetzt das Dasein, die Tätigkeit von über­sinnlichen Kraftsystemen, wie in unserer Blutsubstanz."
      ],
      [
        "Das tritt in keiner anderen Substanz so zutage wie in dem Blut, das unseren Organismus durchfließt.",
        "Dieses Blut ist in der Tat etwas, worin sich das Niederste, das der Mensch um sich herum schauen kann, zusam­menfügt mit dem Höchsten, das sich in seiner Natur organisch ausbilden kann."
      ],
      [
        "Daher wird es uns wohl klar sein, daß wir in bezug auf diese im Blut sich abspielenden komplizierten Vorgänge etwas vor uns haben, das, wenn es etwas unregelmäßig wird oder Störungen eintreten, in einem hohen Maße Unregelmäßigkeiten in unserem Gesamtorganismus hervorrufen muß.",
        "Und daß wir da, wo solche Unregelmäßigkeiten sich zeigen, immer überlegen müssen, wie diese entstanden sind."
      ],
      [
        "Es wird schwierig sein, auseinanderzuhalten, ob wir diese Unregelmäßigkeiten im einzelnen Falle solchen Prozessen zuzuschreiben haben, die nach dem Muster physischer chemischer Prozesse verlaufen, oder ob sie anderen Prozessen des Blutes entspre­chen.",
        "Wenn die Unregelmäßigkeiten verlaufen nach dem Muster physisch-chemischer Prozesse, dann müssen wir uns klar sein, daß ihnen begegnet werden muß von der Seite des Bewußtseins her, und zwar in dem Sinne, wie das Bewußtsein mit dem physischen Plan zusammenhängt."
      ],
      [
        "Hier eröffnet sich ein therapeutisches Gebiet, des­sen Charakteristisches ist, darauf zu achten, ob gewisse Unregel­mäßigkeiten zusammenhängen mit solchen Prozessen, die wir als physisch-chemische bezeichnen können.",
        "Bei dieser Voraussetzung ist es günstig, einzugreifen durcla äußere Impressionen, durch ent­sprechende Regelung der äußeren Eindrücke, welche diese phy­sisch-chemischen Prozesse hervorrufen können."
      ],
      [
        "Damit sind weniger seelisch-geistige Impressionen gemeint, dagegen namentlich alles dasjenige, was wir bewirken können durch eine Regelung des Atmungsprozesses und durch Überwachung der Prozesse der Wechselwirkung des inneren Organismus mit der Außenwelt durch die Haut."
      ],
      [
        "Dann können wir aber auch von der anderen Seite her im Blut die feinsten organischen Vorgänge feststellen, und wir werden uns klar sein müssen, daß wir darin sozusagen die dritte Stufe der Verfeine­rung unserer vorverarbeiteten Nahrungsstoffe zu sehen haben.",
        "Wenn im Blutorganismus jene feinen Prozesse der Salzbildung, der Quell­barkeit, der Wärme hervorgerufen werden durch äußere Vorgänge, also von außen in ihrem chemischen Verlauf bestimmt werden, so dürfen wir auf der anderen Seite fragen, wodurch die Prozesse im Blut von der inneren Seite her bestimmt werden."
      ],
      [
        "Wir müssen da unterscheiden zwischen der Aufgabe, die das Blut hat, und der Tat­sache, daß es so ernährt werden muß wie jedes andere Organ auch.",
        "Zugleich müssen wir es auch als das Organ erkennen, das auf der höchsten Stufe der organischen Tätigkeit steht."
      ],
      [
        "Es kommt hier dasje­nige in Betracht, was wir als die innerliche Stütze des menschlichen Lebens bezeichnen können.",
        "Das Blut muß vor allen Dingen davor geschützt werden, daß die äußere Welt auf dem Wege der Nahrungs­stoffe unmittelbar in das Blut hineinwirkt, es wird sonst seine Tätig­keit als Werkzeug unseres Denkens unterbunden, es wird der Vor­gang gestört, den wir als einen Prozeß der Salzablagerung früher bezeichnet haben."
      ],
      [
        "Dieser Schutz muß vom Blute selbst ausgehen; es muß imstande sein, nach der geistigen Seite hin gerichtet gleichsam ein geistiges Knochensystem aufzubauen durch die sich täglich wie­derholenden Salzablagerungsprozesse.",
        "Das ist eine Aufgabe des Blu­tes, die es unterscheidet von anderen Organen."
      ],
      [
        "Von den anderen Organen des menschlichen Organismus erhält es dabei am wenigsten Unterstützung.",
        "Am wenigsten spielen die anderen Organe in diesen Salzbildungsprozeß des Blutes herein, so daß das Blut in bezug auf die durch das Denken bedingten Prozesse am meisten verinnerlicht ist, wie ja in der Tat unsere Gedanken das Innerlichste sind, was wir haben."
      ],
      [
        "Mit unseren Gefühlen stehen wir an der Grenze von außen und innen, und mit seinen Willensimpulsen strömt der Mensch so stark nach außen, daß er sich unter Umständen gar nicht wiederer­kennt.",
        "In seinem Denken wird sich der Mensch immer wiedererken­nen, aber in seinen Willensimpulsen nicht."
      ],
      [
        "Daß es nicht so klar ist, wie die Willensimpulse entspringen, das können Sie schon daraus"
      ],
      [
        "sehen, daß in bezug auf Freiheit und Unfreiheit des menschlichen Willens so viel in der Welt gestritten wird.",
        "In unserem Denken haben wir also das Innerlichste dessen, was das Blut als Werkzeug des Ich zu verrichten hat.",
        "Und weil nun der Prozeß der Salzablagerung am meisten verinnerlicht ist und auch am meisten geschützt sein muß, so kann durch Unregelmäßigkeiten oder Abnormitäten des Blutes auch diese Tätigkeit des Blutes am meisten behindert werden.",
        "Und wenn wir merken, daß das Blut so behindert ist, daß es nach dieser Rich­tung hin seine Tätigkeiten nicht mehr zeigt, so müssen wir uns darüber klar sein, daß es angeregt werden muß zu einer regelmäßigen Tätigkeit, wenn sein Eigenleben unter eine gewisse Grenze herunter-gesunken ist."
      ],
      [
        "Es kann aber auch der andere Fall eintreten, daß die innere Reg­samkeit des Blutes über ein gewisses Maß hinausgeht, daß dieses Eigenleben stürmischer wird.",
        "Das ist der weitaus wichtigere Fall, weil er bei Erkrankungen viel häufiger vorkommt.",
        "In den seltensten Fällen haben wir es mit dem Entgegengesetzten zu tun.",
        "Meist haben wir es damit zu tun, daß die Tätigkeit der sonst geschützten inneren Organe zu stark angeregt wird und in gleichem Sinne auf das Blut­system wirkt.",
        "Wenn sich das Blut so zeigt, daß es übermäßig nach der Richtung der Willenstätigkeit sich entfalten will, dann muß diesem Drang therapeutisch entgegengewirkt werden.",
        "Das können wir tun durch die Zuführung von solchen Substanzen, die zur normalen Salzbildung, zur normalen Salzablagerung im Sinne von seelisch-gedanklichen Prozessen führen.",
        "Das führt uns dazu einzusehen, daß ein gewisses System hineingebracht werden kann in die Art, wie wir solchen Unregelmäßigkeiten unseres Organismus entgegenwirken können.",
        "Es kann hier natürlich nur darauf hingewiesen werden, eine genauere Angabe würde über die Grenzen dieses Vortragszyklus hinausgehen."
      ],
      [
        "Wie wir Erkrankungen einer zu großen Regsamkeit im Blutsystem zuschreiben mußten, so können wir uns auch fragen, wie wir den Organen unserer inneren astralischen Welt, unseres inneren Welt-systems, Milz, Leber, Galle und so weiter, beikommen können, wenn sie in ihrer Tätigkeit in einer zu großen inneren Regsamkeit sind."
      ],
      [
        "müssen wir uns vor allen Dingen vor die Seele führen, daß diese Organe ja bestimmt sind, heraufzuwirken bis zur Blutzirkulation, daß sie die Nahrungsstoffe so zu übernehmen haben, wie sie vom Verdauungskanal zugeführt werden, und diese hinzuleiten haben in umgewandelter Regsamkeit bis zum Blut, daß sie also die Vermittler zwischen diesen beiden Systemen sind.",
        "Wie das Blutsystem sich als Werkzeug erweist der größten inneren Regsamkeit, des bewußten denkerischen Lebens, so wird es auch zu einer Tätigkeit angeregt, die sich als zusammenhängend zeigt mit unserem Gefühlsleben, das wir schon beschrieben haben als Prozeß des inneren Verdichtens, des inneren Quellens."
      ],
      [
        "Hier wird das Blut - abgesehen von äußeren Einwirkungen - angeregt von der Tätigkeit der inneren Weltsysteme, die in ihrer charakteristischen Eigenart ihre Wirkungen in das Blut hineinstrahlen können.",
        "Wir haben hier auf eine Tätigkeit im Blut hingewiesen, die schon über das Eigenleben des Blutes hinausgehen, deren Ursache aber dem inneren Weltsystem angehört."
      ],
      [
        "Wir können nun die Frage aufwerfen: Können nicht auch diese Organe - Leber, Galle, Milz, Nieren, Lunge, Herz - eine zu große Regsamkeit, ein überquellendes Leben und damit eine unregelmäßige Einwirkung auf das Blut entwickeln?",
        "Und wenn sie das tun, wie können wir -in ähnlicher Weise wie beim Blut - die zu große Regsamkeit dieser Organe therapeutisch paralysieren?"
      ],
      [
        "Da müssen wir - da diese Organe in direktem Zusammenhang stehen mit dem kosmischen Astral­system - solche Stoffe zuführen, die die Regsamkeit des kosmischen Lebens entfalten.",
        "So wie wir durch Zuführen von salzhaltigen Stoffen die innere übertriebene Regsamkeit des Blutes verhindern können, so können wir die krankhafte Regsamkeit der inneren Organe abdämp­fen und ihr entgegenwirken, indem wir Stoffe zuführen, deren Ener­gie derjenigen der betreffenden Organe entspricht und die geeignet sind, sie wieder in Zusammenklang zu bringen mit der allgemeinen Gesetzmäßigkeit."
      ],
      [
        "Für uns entsteht also jetzt die Frage: Wie können wir auf diese Organe einwirken?",
        "Wie können wir den Unregelmäßigkeiten der einzelnen Organsysteme und auch dem Verdauungssystem beikom­men?",
        "Damit stellt sich die Frage überhaupt: Wie stellt sich uns ein"
      ],
      [
        "Krankheitsbild im okkult-physiologischen Sinne dar, und wie sind die Krankheitserscheinungen zu heilen? - Wir werden morgen darauf zu antworten haben und dabei auch Rücksicht nehmen zum Beispiel auf das Muskelsystem.",
        "Unsere Betrachtungen werden darin ausklin­gen, daß wir zeigen, wie das, was als bewundernswerter fertiger Organismus uns entgegentritt, sich als werdender Organismus im Keimesleben deutlich ankündigt.",
        "Dann wird sich uns ganz von selbst ergeben, wie sich die übersinnlichen Glieder beteiligen an der menschlichen Organisation."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "ACHTER VORTRAG Prag, 28. März 1911",
    "paragraphs": [
      "Es wird heute in diesem letzten Vortrage meine Aufgabe sein, die Betrachtungen der letzten Tage über okkulte Physiologie, die man­ches, wenn auch zum Teil recht skizzenhaft, von den Vorgängen der menschlichen Organisation darzustellen versuchten, zu einer Art von Gesamtbild zu vereinigen, das ja wieder nur skizzenhaft sein kann, durch das wir in den Stand gesetzt werden können, eine Anschauung zu bekommen von dem lebendigen Leben und Weben des mensch­lichen Organismus. Wir werden dabei am besten tun, wieder von dem gröbsten auszugehen, von der Wechselbeziehung zwischen dem menschlichen Organismus und der äußeren Welt, unserer physischen Erde, in der Aufnahme der Nahrungsstoffe.",
      "Diese Nahrungsstoffe werden ja, nachdem sie aufgenommen sind, in der mannigfaltigsten Weise umgewandelt und stufenweise so umgeändert durch die verschiedenen Organwirkungen, daß sie hin-geleitet werden können zu den einzelnen Gliedern des menschlichen Organismus, zu den einzelnen Systemen der menschlichen physi­schen Wesenheit. Es ist ja nicht schwer einzusehen, daß alles, was aus den Nahrungsstoffen im menschlichen Organismus wird, im Grunde genommen den Menschen, wie er vor uns steht in der physischen Welt, eigentlich erst zum physischen Menschen macht. Es liegt hier ja allerdings eine gewisse Schwierigkeit für das Verständnis vor. Allein, wenn wir Ernst machen mit den bisher eingehaltenen Prinzipien und die übersinnliche Erkenntnis wirklich auf die Betrachtung des Men­schen anwenden, so müssen wir sagen, daß es nur die Nahrungsstoffe sind, die von der äußeren Welt substantiell in den menschlichen Organismus aufgenommen werden. Alle übrigen auf den Menschen einwirkenden Einflüsse haben wir uns im Grund genommen zu denken als übersinnliche, unsichtbare Kräfte. Wenn sie sich für einen Moment alles wegdenken, was den menschlichen Organismus, von den Nahrungsstoffen herrührend, ausfüllt, so behalten Sie in phy­sischer Beziehung noch weniger - verzeihen Sie den trivialen Ausdruck-,",
      "viel weniger übrig als einen leeren Sack, nämlich gar nichts. Denn auch was an Haut, an Umhüllung des physischen Organismus vorhanden ist, ist nur dadurch vorhanden, weil entsprechend verar­beitete Ernährungsstoffe an die betreffenden Partien hingeführt wor­den sind.",
      "Rechnen Sie die Nahrungsstoffe und was aus ihnen wird, weg, so haben Sie dahinter den menschlichen Organismus nur als ein übersinnliches Kraftsystem zu denken, das die Verteilung der assimi­lierten Nahrungsstoffe nach allen Richtungen hin bewirkt. Wenn Sie diesen Gedanken, wie er jetzt ausgesprochen worden ist, sich so richtig vor die Seele stellen, so werden Sie sich sagen: Eines ist aber eigentlich die Voraussetzung, bevor irgend etwas, auch das kleinste, von den Nahrungsstoffen aufgenommen werden kann, denn diese Stoffe können nicht von der Außenwelt in jedes beliebige Wesen bineinbefördert werden, damit dasjenige in ihm vorgehe, was im menschlichen Organismus vorgeht.",
      "Es muß der Mensch schon bei der allerersten Nahrungsaufnahme den physischen Nahrungsstoffen eine innere Kraftwirkung entgegenstellen können, welche aus der übersinnlichen Welt stammt, und es muß in diesem inneren Kräfte-system der Mensch als solcher schon enthalten sein. Im Okkultismus nennen wir dasjenige, was so den eigentlichen physischen Ausfül­lungsmaterialien vom Menschen zunächst entgegengehalten wird, was durchaus schon übersinnlich zu denken ist, das nennen wir im umfassendsten Sinne die menschliche Form.",
      "Wenn wir uns die aller-unterste Grenze der menschlichen Organisation denken, so müssen wir uns vorstellen, daß sich gegenüberstehen die physische Materie und die übersinnliche Form, welche als ein aus den übersinnlichen Welten herausgeborenes Kraftsystem dazu bestimmt ist, die Materie aufzunehmen - nicht wie ein physischer Sack oder BaIg, sondern wie ein Überphysisches, ein Übersinnliches - und dasjenige herauszubil­den, was überhaupt den Menschen erst physisch-sinnlich erscheinen läßt. Erst dadurch, daß sich dieser übersinnlichen Form eingliedert das assimilierte Ernährungsmaterial, wird der sonst rein übersinnli­che menschliche Organismus zu einem physisch-sinnlichen Organis­mus, den man mit Augen sehen und mit Händen greifen kann.",
      "Man nennt das, was so entgegengehalten wird der physischen Materie, aus",
      "dem Grunde «Form», weil eigentlich in aller Natur ein solches Gesetz wirkt, ein genau gleiches Gesetz, das überall «Formprinzip» genannt wird. Wenn wir die äußere Welt betrachten, so finden wir, daß bis zum Kristall hinunter überall das Formprinzip tätig ist. Die Substanzen, welche in den Kristall eintreten, müssen, um das zu werden, als was der Kristall sich darstellt, gleichsam eingefangen werden von dem Formprinzip, und dieses macht mit Hilfe der Sub­stanzen den Kristall erst zu dem, was er ist. Nehmen Sie zum Beispiel das Kochsalz, Chlornatrium, so haben Sie als physische Substanzen miteinander verbunden Chlor und Natrium, ein Gas und ein Metall. Sie werden leicht einsehen, daß diese beiden Stoffe, so wie sie sind, bevor sie eingefangen werden durch eine formende Wesenheit und dadurch erst zu einer chemischen Verbindung in Würfeln kristalli­siert erscheinen, jede für sich völlig andere Formen zeigt. Bevor sie eintreten in dieses Formprinzip, haben sie nichts Gemeinsames; aber sie werden eingespannt, aufgenommen von diesem Formprinzip, und dieses bildet den physischen Körper Kochsalz.",
      "So setzt auch alles, was als umgewandelte Nahrungsstoffe im menschlichen Organismus erscheint, die unterste übersinnliche Wesenheit, die übersinnliche Form voraus. Wenn nun neue Ernäh­rungsstoffe in den menschlichen Organismus eintreten sollen, der durch das Wirken des Formprinzips bereits nach außen abgegrenzt ist, so müssen sie unter normalen Verhältnissen durch den Mund in den Ernährungskanal aufgenommen werden. Dabei machen sie gleich schon vom Munde ab die allererste Umwandlung durch. Durch den Ernährungskanal werden weitere Umwandlungen bewirkt. Diese Umwandlungen kompliziertester Art könnten nicht bewirkt werden, wenn nicht dem menschlichen Organismus ein höheres Prinzip ein­gegliedert wäre, das wir Formprinzip genannt haben, durch dessen Wirksamkeit die Nahrungsstoffe - die zunächst, wenn sie aufgenom­men werden, sich zueinander neutral, gleichgültig verhalten - modifi­ziert würden, so daß sie in die Lage kommen, lebendige Organe zu bilden. Wir können uns, obgleich es beim Menschen ein ganz anderer Prozeß ist, weil er auf einer anderen Stufe geschieht, diese Umwand­lung der Nahrungsstoffe im menschlichen Verdauungskanal vergleichsweise",
      "so vorstellen, wie wenn die Pflanzen ihre Ernährungs­stoffe aufnehmen aus dem mineralischen Boden und sie dergestalt umwandeln, daß sie sich zu der Form der betreffenden Pflanze aufbauen. Da ist nur möglich, weil bei der Pflanze der Ernährungs­strom von einem Lebensprozeß oder, wie wir im Okkultismus sagen, vom Ätherleib als dem ersten übersinnlichen Prinzip aufgenommen wird.",
      "So werden auch beim Menschen die in den Organismus eintre­tenden Nahrungsstoffe vom Ätherleibe bearbeitet, das heißt, der Ätherleib sorgt für ihre Umwandlung, für ihre Eingliederung in die inneren Gesetzmäßigkeiten des menschlichen Organismus. So haben wir also dieses erste übersinnliche Glied des Menschen, den Äther-leib, anzusehen als den Erreger der ersten Umwandlung der Nah­rungsstoffe.",
      "Wenn nun diese Nahrungsstoffe soweit umgewandelt sind, daß sie in den Lebensprozeß aufgenommen sind, dann müssen sie in dem Sinne, wie wir es in den vorhergehenden Vorträgen geschildert haben, weiter verarbeitet und dem menschlichen Organis­mus angepaßt werden. Sie müssen so verarbeitet werden, daß sie nach und nach denjenigen Organen im menschlichen Organismus dienen können, die ein Ausdruck der höheren übersinnlichen Prinzipien sind, des Astralleibes und des Ich.",
      "Kurz, wir müssen uns klar sein, daß die höheren Prinzipien, Astralleib und Ich, die eigentümliche Art ihrer Regsamkeit hinuntersenden müssen bis zu den Vorgängen in den Organen des Ernährungs- und Verdauungsapparates und daß sie bis in die verwandelten Nahrungsstoffe hinab wirken müssen.",
      "Da stellen sich nun dem Nahrungsstrom diejenigen Organe entge­gen, welche uns schon bekannt sind, die wir bezeichnet haben als die sieben Organe des inneren Weltsystems. Wir zeichnen nochmals ganz schematisch das innere Weltsystem des Menschen:",
      "Die Nahrungsstoffe werden also aufgenommen und zunächst in der mannigfaltigsten Weise umgearbeitet im Verdauungskanal, dann stellen sich ihnen entgegen Leber, Galle, Milz, Herz, Lunge, Nieren und so weiter. Wenn wir uns nun darüber klar sind, daß diese Or­gane durch die ihnen entsprechenden Kraftsysteme dazu bestimmt sind, den Nahrungsstrom weiter umzuarbeiten, so können wir fra­gen: Welches ist der Sinn dieser weiteren Umwandlung? - Wenn der",
      "# Bild s. 155",
      "Nahrungsstrom nur so weit bearbeitet würde, wie es im Verdauungs-kanal geschieht, um der Lebensform dienen zu können, so würde der Mensch nur ein unbewußtes Pflanzendasein führen können, denn er hätte es nicht zur Ausbildung solcher Organe gebracht, die Werk­zeuge sein können für seine höheren Fähigkeiten. Die sieben Organe wandeln den Ernährungsstrom aber weiter um, und wir wissen, daß diese Vorgänge durch das sympathische Nervensystem davon abge­halten werden, in das menschliche Bewußtsein einzutreten. Daher haben wir in dem sympathischen Nervensystem mit den sieben Organen zusammen dasjenige, was sich dem Nahrungsstrom entge­genstellt.",
      "Damit sind wir schon bis zu einem hohen Grade von außen in das Innere des menschlichen Organismus hineingedrungen. Aber das, was da drinnen vorgeht, man möchte sagen als die gegenseitige Ange­legenheit der sieben Organe, da ist etwas, was nirgends in unserer Erdenwelt so vorgehen könnte wie da drinnen. Es kann nur dadurch so vorgehen, daß dieses Innere von der Außenwelt völlig abgeschlos­sen ist und für diese Tätigkeit des Innern die Stoffe vorbereitet sind",
      "durch den Verdauungskanal. Also wir stehen darnit schon im Inneren des menschlichen Organismus darinnen.",
      "Nun haben wir das Eigentümliche zu verzeichnen, daß, indem wir so im Innern des Organismus darinnenstehen, der Organismus sich ja selbst innerlich organisieren, sich selbst innerlich differenzieren muß. Um allen diesen an ihn herantretenden Anforderungen zu genügen, muß der Organismus eine Vielheit zusammenwirkender Organe her-ausbilden.",
      "Für die mannigfaltigen inneren Verrichtungen ist gerade diese Vielheit der Organe notwendig. Was durch diese erreicht wer­den muß, werden wir im folgenden sehen. Wenn wir uns denken, daß nur der Nahrungsstrom umgewandelt würde durch die sieben Organe des inneren Weltsystems, da würde der Mensch nimmermehr sein Wesen dem Bewußtsein aufschließen können.",
      "Er würde nicht einmal die dumpfeste Form des Bewußtseins haben können, weil ja alles, was da vorgeht, verhüllt wird, abgehalten wird vom Bewußtsein durch das sympathische Nervensystem. Es ist also eine Verbindung notwendig zwischen diesen sozusagen von außen her aufgebauten inneren Organsystemen und dem, was weiter im Inneren des menschlichen Organismus ist.",
      "Diese Verbindung wird dadurch her­gestellt, daß in der Tat durch alles das, was der Ernährungsprozeß in seiner Ganzheit gibt, die gesamte Form des menschlichen Organis­mus durchzogen wird von dem, was wir im weitesten Sinne Gewebe nennen. Eine gewisse Art von Gewebe einfachster Organisation durchzieht alle einzelnen Glieder der menschlichen Wesenheit, das fähig ist, sich so umzuwandeln und auszugestalten, daß sich die verschiedensten Organe herausbilden können.",
      "Gewisse Arten des Gewebes zum Beispiel bilden sich so um, daß sie sich durch Einlage­rung besonderer Zellen zu den Muskeln umgestalten; andere bilden sich so um, daß sie fest werden und sich die Knochenzellen einlagern, indem sie die entsprechenden Substanzen sich aneignen. So daß wir in den einzelnen Organen des menschlichen Organismus stets an das zu denken haben, was ihnen zugrundeliegt, nämlich das den Körper nach allen Richtungen durchziehende Gewebe, aus dem die einzelnen Organe sich herausbilden.",
      "Dieses bildungsfähige Gewebe würde aber, wenn es noch so sehr zu wachsen und die verschiedensten",
      "Organe aus sich herauszubilden imstande wäre, doch nichts anderes darstellen als im Grunde nur etwas Pflanzenhaftes; denn das ist ja das Wesentliche des Pflanzenhafte, daß die pflanzlichen Wesen wach­sen, daß sie aus sich Organe hervortreiben und dergleichen. Indem sich aber der Mensch über das Pflanzenhafte hinaus erhebt, muß sich uns ein ganz neues Element darbieten, durch welches der Mensch in die Lage kommt, zu dem Pflanzenleben dasjenige hinzuzufügen, was ihn über das Pflanzenleben hinaushebt. Der Mensch muß hinzufügen das Bewußtsein, zunächst die einfachste Form des Bewußtseins, das dumpfe Bewußtsein, das ihn fähig macht, das eigene innere Leben wahrzunehmen. Solange nicht ein Wesen das eigene innere Leben bewußt miterlebt, solange es noch nicht in der Lage ist, sich innerlich gleichsam zu durchspiegeln, um dieses eigene innere Leben mitzuer­leben, so lange können wir nicht sagen, daß es sich über die Pflanzen­haftigkeit hinauferhebt. Erst dadurch erhebt sich ein Wesen über die Pflanzenhaftigkeit hinauf, daß es nicht bloß in sich Leben hat, son­dern dieses Leben bewußt erlebt, daß es zunächst diese inneren Vorgänge durchspiegelt und miterlebt.",
      "Wodurch kommt nun überhaupt Erleben zustande? Dafür haben wir uns schon den Begriff gebildet. Wir haben ja in den früheren Vorträgen schon gezeigt, daß Erleben zustande kommt durch Absonderungsprozesse. Deshalb werden wir als die Grundlagen des inneren Erlebens, des dumpfen, die inneren Lebensprozesse durch-ziehenden Bewußtseinserlebens,  Absonderungsprozesse suchen müssen. Wir werden voraussetzen müssen, daß überall aus den Geweben heraus Absonderungsprozesse stattfinden; und in der Tat treten uns diese Absonderungsprozesse schon bei der äußeren Betrachtung des menschlichen Organismus entgegen, wenn wir sehen, wie fortwährend Stoffe aus allen Teilen des Gewebes aufge­nommen werden durch das, was wir die Lymphgefäße nennen, die wie eine Art anderes System neben dem Blutsystem den ganzen Organismus durchziehen. In das Lymphgefäßsystem münden sozu­sagen von allen Bezirken des menschlichen Organismus diejenigen Absonderungsprozesse, welche das dumpfe innere Erleben vermit­teln. Könnten wir uns einmal in abstracto das gesamte Blutsystem",
      "wegdenken und könnten wir uns das Gewebe so denken, daß es nichts mehr hat von blutartigem Charakter, so würden wir uns vorzustellen haben, daß im Blutsystem sich höhere Prozesse abspie­len gegenüber den Prozessen des Lymphsystems. In diesen Absonde­rungen fühlt der Mensch gleichsam in einem dumpfen tierischen Bewußtsein seinen eigenen physischen Leib. Dumpf durchspiegelt er seine Organisation. Und ebenso wie auf der einen Seite durch das sympathische Nervensystem von dem Bewußtsein alles abgehalten wird, was vom Verdauungs- und Ernährungsprozeß und den sieben Organen heraufdringen will, so wird auf der anderen Seite gleich­sam durch Rückstrahlung der Tätigkeit des sympathischen Nerven­systems, durch Verbindung und Wechselwirkung mit den Lymph­bahnen, ein für den heutigen Menschen allerdings vom hellen Tages­bewußtsein überstrahltes dumpfes Bewußtsein ausgebildet. Es wird überstrahlt vom hellen Tagesbewußtsein des Ich, wie ein schwaches Licht überstrahlt wird durch ein starkes. Dieses dumpfe Bewußtsein ist gleichsam die andere Seite jenes Bewußtseins, das sich des sym­pathischen Nervensystems als seines Werkzeuges bedient.",
      "Würde der Mensch seinen Organismus nur entwickelt haben bis zur Bildung des Körpergewebes und der Organe, die für die inneren Verdauungsvorgänge und für die Absonderungen in die Lymphbah­nen notwendig sind, so würde er nur ein dumpfes Bewußtsein seines [nnenlebens vermittelt erhalten können. Er würde aber nicht eine Ausbildung des Ich-Bewußtseins erreichen können; das kann er nur erwerben, wenn er sich nicht bloß in seinem Inneren erlebt, sondern sich auch nach außen aufschließt. Hier haben wir wiederum ein Sich-aufschließen nach außen zu verzeichnen. Wir haben ja schon früher davon gesprochen, wie es dem Menschen durch die Atmung möglich wird, unmittelbar mit der Außenwelt in Verbindung zu treten. Jetzt konnen wir weitergehen und sagen: Sofern wir den inneren Men­schen betrachten, dürfen wir eigentlich nur bis zum Verdauungs-system gehen, denn wir können sagen: Insofern Ausläufer der Orga­ne des inneren Weltsystems bis zum Verdauungskanal sich hinwen­den, haben wir in diesem Anstoßen des inneren Weltsystems an den Verdauungskanal schon ein Sichaufschließen nach außen zu sehen,",
      "denn der Mensch ist gleichsam bereit, Nahrungsstoffe von außen aufzunehmen. Indem er mit aus der Umwelt entnommenen Nah­rungsstoffen in enge Berührung tritt, ist er eigentlich schon nicht mehr nur innerlich. Ein weiteres Sichaufschließen nach außen haben wir kennengelernt in der Atmung, und in noch höherem Maße ist es zu erkennen in jenen Organen, die den seelischen Funktionen dienen.",
      "So also sehen wir, wie dem bewußten Leben des Menschen zugrundeliegt einerseits ein dumpfes Innenleben, andererseits die Fähigkeit, sich der Außenwelt aufzuschließen, mit der Außenwelt Verbindung zu haben. Dadurch erst kann der Mensch ein Ich-Wesen sein.",
      "Nür dadurch, daß er nicht nur die Widerstände in seinem eigenen Innern in seinen Absonderungsprozessen spürt, sondern auch die Widerstände, die die Außenwelt ihm entgegensetzt, kann der Mensch sein Ich-Bewußtsein entwickeln. So ist in der Tatsache, daß sich der Mensch auch wieder nach außen aufschließen kann, die Grundlage gegeben für die physische Ichheit des Menschen.",
      "Damit aber muß der Mensch auch die Möglichkeit haben, in der mannigfal­tigsten Weise das Organ dieser Ichheit auszubilden. Und wir haben ja gesehen, wie in der Tat das Organ der Ichheit, das Blut, sich einglie­dert in den Organismus und wie der Blutkreislauf alle Organe durch­zieht, um ein Werkzeug zu sein für die Ichheit.",
      "So wie die Ichheit geistig-seelisch den gesamten Menschen durchlebt und durchwebt, so durchzieht physisch der Blutkreislauf den gesamten menschlichen Organismus und wendet sich dabei gleichsam nach zwei Seiten, nach dem Innenwesen des Menschen mit den sieben Organen und so weiter, und dann haben wir wieder ein Sichaufschließen nach außen, ein In-Verbindung-Treten mit der äußeren Welt. Wir können also im höchsten Sinne des Wortes von einem Kreislauf der Kräfte sprechen, welche hinter den physischen Erscheinungen stehen und welche durch das Ich einen Verbindungspunkt finden.",
      "Nun müssen wir uns einmal mit den einzelnen Phasen dieses Kreislaufes noch etwas beschäftigen. Da handelt es sich ja zunächst darum, daß wir noch einmal den Ernährungsprozeß verfolgen, das Aufnehmen der Nahrungsstoffe, welche dadurch, daß sie vom Äther-leibe oder vielmehr von der Kraft des Ätherleibes ergriffen werden,",
      "zu einem lebendigen Strom im menschlichen Organismus werden; dann stellt sich ihnen gegenüber das innere Weltsystem, die sieben Organe, und zwar deshalb, weil - wie wir schon gesehen haben - der Mensch sonst nicht hinauskommen würde über das pflanzenhafte Dasein. Auf einer weiteren, höheren Stufe ist es notwendig, daß sich entgegenstellen dem Nahrungsstrom die Funktionen dieser sieben Organe. So wirkt also das, was aus der eigentlichen astralischen Natur des Menschen kommt, dem belebten Nahrungsstrom entge­gen; der Nahrungsstrom kommt von außen, und das, was die innere Menschennatur ist, wirkt dem entgegen. Zunächst begegnet dem Nahrungsstrom, also der aufgenommenen Außenwelt, der Ätherleib, der die Nahrungs stoffe umwandelt im Verdauungs system; dann tritt ihm entgegen der Astralleib des Menschen, wandelt die Nahrungs­stoffe weiter um und gliedert sie so ein, daß sie immer mehr und mehr der inneren Regsamkeit des Organismus angepaßt werden. In seinem weiteren Verlauf muß der Nahrungsstrom auch erfaßt werden von den Kräften des Ich, des Blutes selber. Das heißt, es muß das Werkzeug des Ich mit seinem Wirken herunterreichen bis dahin, wo der Ernährungsstrom aufgenommen wird. Tut dies das Blut? Bewahrheitet sich das, was wir aus der okkulten Anschauung heraus sagen müssen?",
      "Ja, das Blut wird heruntergetrieben in die Ernährungsorgane ebenso wie in alle anderen Organe. Es macht in den Ernährungsorga­nen einen Prozeß durch, durch den es erst das vollständige Werkzeug des menschlichen Ich in der physischen Welt sein kann. Wir wissen, daß das Blut als Werkzeug des menschlichen Ich den Übergang durchmachen muß von dem sogenannten roten in blaues Blut. Das Ich wirkt mit seinem Werkzeuge, dem Blut, bis herunter zu den Anfängen der Verdauungs- und Ernährungsprozesse. Da haben wir es nun auch wieder mit einem Widerstand zu tun. Wie geschieht das? Das geschieht, indem das Blut durch das Pfortadersystem in die Leber eintritt und dort aus sozusagen verändertem Blut die Galle bereitet wird und die Galle sich wiederum unmittelbar dem Nah­rungsstrom entgegenstellt. Hier in der Galle haben wir eine wun­derbare Verbindung der beiden Enden der inneren menschlichen",
      "Organisation. Auf der einen Seite stellt der vom Verdauungskanal aufgenommene Nahrungsstrom das äußerste Materielle dar, was in unseren physischen Organismus hineingelangt, auf der anderen Seite steht das Ich, das Edelste, was der Mensch innerhalb der Erdenwelt haben kann, mit seinem Werkzeug, dem Blut. Das Ich stellt eine un­mittelbare Verbindung her mit dem äußersten Materiellen, indem es am Ende des Blutprozesses auf dem Umwege über die Leber die Galle bereitet, und in der Galle stemmt sich - in dem umgewandelten, veränderten Blut - dem Nahrungsstrom entgegen das Ich.",
      "Da sehen wir das Ich hinunterwirken bis in das gröbste Materielle und dann wieder hochorganisierte Stoffe wie die Galle aus sich heraussetzen. Und wer diese intimen Vorgänge zwischen Blut, Galle und Ernährungsprozeß verstehen will, der kann gerade in diesen Tatsachen etwas finden, was ihm viele Geheimnisse des menschlichen Organismus klarer erscheinen läßt; und er kann, wenn er diese Pro­zesse weiterverfolgt, zum Beispiel auch abnorme Prozesse, wie sie sich aus einer Rückstauung der Galle, einer Rückergießung der Galle ins Blut bei der sogenannten Gelbsucht ergeben, richtiger beurteilen und behandeln. Doch das würde heute zu weit führen, wenn wir solche Dinge auch noch ausführten.",
      "So sehen wir, wie in der Tat die sieben Organe sich bis in das Wirken des Ätherleibes hinuntererstrecken und die Einwirkungen des Ich von oben in sich aufgenommen haben. Wir haben also in der Galle etwas, das sich unter dem Einfluß des Ich dem Nahrungsstrom direkt entgegenstellt. Will die Galle auf den Nahrungsstrom wirken, der im Verdauungsprozeß schon ein Lebendiges geworden ist, so muß sie ihm auch als eine lebendige Substanz entgegentreten können. Das geschieht dadurch, daß sie eben aus einem Organ heraus gebildet wird, welches zu den sieben Gliedern des inneren Weltsystems gehört, die das innere des Menschen beleben, so daß damit die Galle als inneres Leben dem von außen kommenden begegnet.",
      "Wie die Galle mit der Leber in Verbindung steht, so finden wir die Leber wiederum in Verbindung mit der Milz. Wenn wir diese Organe Leber, Galle, Milz ins Auge fassen, so müssen wir sagen, diese Organe sind es, welche sich dem Ernährungsstrom unmittelbar",
      "entgegensetzen und ihn so umwandeln, daß er fähig wird, zu höheren Stufen der menschlichen Organisation aufzusteigen. Sie haben aber auch diejenigen Organe zu versorgen, die sich nach außen aufschlie­ßen, und das tun das Herz, die Lungen, auch schon der Verdauungs-kanal selber, vor allen Dingen aber die Organe des Kopfes, die Sinnesorgane.",
      "Nun haben wir uns schon früher klar gemacht, daß alles innere Erleben mit Absonderungsprozessen eng verbunden ist. Deswegen haben wir auch diese Absonderungsprozesse besonders betrachtet. Leber, Galle und Milz haben im Sinne jener Vorgänge in der Gesamt-Organisation zunächst nichts unmittelbar mit Absonderungsprozes­sen zu tun, sie sondern zwar Stoffe ab, aber das hat mit der Ernäh­rung zu tun. Sie vermitteln das aufsteigende Leben, das von den niedersten Lebensformen sich hinwendet zum Organ der Bewußt­beit, zum Bewußtsein selbst. Indem aber diesen Organen als ein viertes Organ das Herz sich angliedert und das Herz durch den Blutumlauf sich auch nach außen aufschließt, erlangt der Mensch sein Ich-Bewußtsein. Er würde aber nicht in der Lage sein, dieses Ich als das zu erleben, was der Außenwelt gegenübersteht, wenn er nicht dieses nach außen schauende Ich in Beziehung bringen würde zu dem, was er als dumpfes Bewußtsein seines inneren Leibeslebens schon besitzt. Er muß zu den Absonderungsprozessen des inneren Organismus noch einen anderen hinzufügen, welcher ihm auch ein Erleben seines Inneren vermittelt mit dem Ich, das im Blute sein Werkzeug hat.",
      "Zunächst erlebt der Mensch durch die Absonderung der Lymphe sein Innenleben nur in dumpfem Bewußtsein. Dann aber muß auch aus dem Blute abgesondert werden können, und in dieser Absonde­rung wird der Mensch gewahr, daß er als Eigenwesenheit der Außen­welt gegenübersteht, als inneres Ich. Der Mensch würde aber in seinem Erleben der Außenwelt so gegenüberstehen, daß er sich selbst innerlich verlöre, würde er nicht wissen, daß das dasjenige, was da die Luft atmet und die Ernährungsstoffe von außen aufnimmt und verar­beitet, dasselbe Wesen ist wie das, welches er im Inneren erlebt. Daß der Mensch sich nicht verliert, daß er mit seinem Eigenwesen der Außenwelt gegenübersteht, das ist dadurch möglich, daß er durch die",
      "Lungen aus dem umgewandelten Blut absondert die Kohlensäure und durch die Nieren die umgewandelten Stoffe absondert, die aus dem Blut heraus kommen.",
      "Damit sind in ihrer Funktion sowohl die Organe gekennzeichnet, die einen aufsteigenden Prozeß vermitteln, Leber, Galle, Milz, wie auch diejenigen Organe, die einen absteigenden Prozeß vermitteln, Lungen und Nieren. Wir dürfen da aber nicht schematisieren - das geht bei theosophischen Betrachtungen überhaupt nicht -, wir müs­sen sehen, daß die Lungen, indem sie sich nach außen aufschließen, auch einen aufsteigenden Prozeß vermitteln.",
      "Wir sehen also, wie diese sieben wichtigsten Glieder des inneren menschlichen Weltsy­sterns zusammenhängen mit dem inneren Erleben des Menschen und mit dem Sichaufschließen nach außen. Diese sieben Glieder ver­wandeln auf der einen Seite die Eigenregsamkeit der Nahrungsstoffe in innere Regsamkeit des Organismus und versorgen mit diesen umgewandelten Stoffen den menschlichen Organismus.",
      "Sie machen es möglich, daß der Mensch sich wieder nach außen aufschließt. Sie machen es aber auch möglich, daß das, was der Mensch als eine zu starke innere Regsamkeit entwickelt, abgestoßen wird nach außen durch die Absonderungsprozesse der Lungen und Nieren.",
      "Durch die Arbeit der Lungen und Nieren haben wir also eine regelmäßige Regulierung der Regsamkeit der menschlichen Organsysteme. Dieses ganze Verhältnis, in dem die menschlichen Organsysteme zueinander stehen, das drückt sich so aus, daß man im Okkultismus in der Tat kein besseres Bild dafür geben konnte, als daß man sagte: Das Herz als Sonne steht im Mittelpunkt und beeinflußt die drei Organe des inneren Weltsystems, die die aufsteigenden Prozesse besorgen, Leber, Galle, Milz.",
      "So wie im Makrokosmos die Sonne im Planeten-system steht zu den äußeren Planeten Jupiter, Mars, Saturn, so steht im Mikrokosmos, im menschlichen Organismus, die innere Sonne, das Herz, zu Leber-Jupiter, Galle-Mars, Milz-Saturn. Ich müßte nun nicht wochenlang, sondern monatelang reden, wenn ich Ihnen alle die Gründe auseinandersetzen wollte, warum vor einem genauen und intimen okkulten Beobachten das Verhältnis der Sonne zu den äuße­ren Planeten unseres Planetensystems wirklich in Parallele gesetzt",
      "werden darf zu dem Verhältnis, das im menschlichen Organismus das Herz hat zu dem inneren Weltsystem, zu Leber, Galle und Milz. Es ist in der Tat das äußere Verhältnis absolut so hereingenommen, daß in der Wechselwirkung dieser Organe sich das widerspiegelt, was in der großen Welt des Makrokosmos, in unserem Sonnensystem vor sich geht. Und ebenso ist es berechtigt, davon zu sprechen, daß die Vorgänge, die sich abspielen zwischen der Sonne und den inneren Planeten bis zu unserer Erde herunter, sich widerspiegeln in dem Verhältnis des Herzens zu den Lungen und zu den Nieren. So haben wir in diesem inneren Weltsystem des Menschen etwas, was das äußere Weltsystem widerspiegelt.",
      "Wir haben im Verlaufe der Vorträge auch schon angedeutet, wie in der Tat, wenn wir hellseherisch hinuntertauchen in das eigene Innere, wir aufhören, unsere inneren Organe nur so wahrzunehmen, wie sie sich dem äußeren Anblick des physischen Auges darbieten. Wir mussen hinauskommen über das Phantasiebild, das sich die äußere Anatomie von unseren Organen macht, indem wir aufsteigen zur Betrachtung der wirklichen Gestalt, die diese Organe haben, wenn wir berücksichtigen, daß diese Organe ja Kraftsysteme sind. Durch die äußere Anatomie kann gar nicht das wirkliche Sein dieser Organe ergründet werden, denn sie sieht ja in ihnen nur die hinein-gestopften umgewandelten Nahrungsstoffe. Und gerade dadurch, daß die äußere Wissenschaft nur diese Anschauung gelten lassen will, kann sie nicht die inneren Kraftsysteme, welche den Organen zugrundeliegen, erkennen. Für denjenigen aber, der in der Lage ist, das, was diesen Organen als Kraftsysteme zugrundeliegt, durch hell­seherische Beobachtung zu schauen, der sieht, wie berechtigt es ist, die Organe mit den Namen der Planeten zu benennen, weil er erkennt, wie das Verhältnis zwischen den Planeten unseres äußeren Weltsystems sich wiederholt in unserem inneren Organsystem.",
      "Nun haben wir gestern gesagt, daß die Organe eine zu starke innere Regsamkeit entwickeln können. Jedes einzelne der Organe kann eine zu starke Regsamkeit entwickeln, und diese Unregelmäßig­keit kann sich so ausdrücken, daß sie sich auf den ganzen Organis­mus auswirkt. Nun habe ich schon gestern darauf hingedeutet, daß",
      "wenn durch solche zu starken inneren Regsamkeiten etwas wie ein eigensinniges Eigenleben in den inneren Organen auftritt, es notwen­dig ist, dasjenige entgegenzusetzen, was diese inneren Regsamkeiten dämpft. Das heißt, wenn die inneren Organe zu stark umsetzen, zu stark umwandeln die äußeren Regsamkeiten der Nahrungsstoffe, wenn sie ein zu starkes inneres Verwandlungsprodukt liefern, dann mussen wir ihnen etwas von außen entgegensetzen, das sie eindämmt, das die übermäßige innere Regsamkeit dämpft.",
      "Wie kann das geschehen? Wenn wir ein Organ des inneren Systems treffen wollen, das eine zu starke innere Regsamkeit entwickelt, so mussen wir in der Außenwelt dasjenige suchen, welches die entge­gengesetzte Regsamkeit hat, und dies dem Organismus zuführen, um dadurch die zu starke Regsamkeit des Organs bekämpfen zu können.",
      "Das heißt, wir müssen versuchen, jene äußeren Regsamkeiten aufzu­finden, welche den Regsamkeiten der einzelnen Organe entsprechen. Im Mittelalter haben die Menschen noch vieles davon gewußt, wie die Stoffe der Umwelt, also äußere Substanzen, der übertriebenen Regsamkeit der Organe entgegenwirken können.",
      "Für den heutigen Menschen, dem solche Dinge oft nur aus verballhornten Schriften des Mittelalters entgegentreten, in denen er nichts als bunten Aberglau­ben sehen kann, hört sich das ganz sonderbar an. Aber von der okkulten Wissenschaft ist das Entsprechen der Organe des inneren Weltsystems mit gewissen äußeren Substanzen durch Jahrtausende sorgfältig, tief und gründlich untersucht worden, und unzählige Beobachtungen, die mit dem hellsichtigen Auge gemacht worden sind, haben erwiesen, daß zum Beispiel dem übermäßig tätigen in­neren Jupiter, der Leber, Einhalt geboten werden kann durch die Metallsubstanz des Zinns.",
      "Die übermäßige innere Regsamkeit der Galle bekämpfen wir durch dasjenige, was in der Metallsubstanz des Eisens zum Ausdruck kommt. Das ist gar nicht zu verwundern, denn Eisen ist das einzige Metall, das wir in unserem Blut haben müssen als wesentlichen Bestandteil für das Werkzeug des Ich, und wir haben ja gesehen, daß in der Galle gerade dasjenige Organ vorliegt, welches vermittelt die Verbindung von dem Ich mit dem dichtesten Materiel­len, das dem Menschen eingelagert wird, dem Nahrungsstrom.",
      "Ebenso können wir sagen, daß die Milz ihre äußere Entsprechung hat in dem Metall Blei. Dem Herzen - Sonne - entspricht das Gold. Den Lungen - Merkur -, das sagt der Name selbst, entspricht das Queck­silber und den Nieren das Metall Kupfer, also die Venus. (Es wird an die Tafel geschrieben:)",
      "Saturn    Milz    Blei",
      "Jupiter    Leber    Zinn",
      "Mars    Galle    Eisen",
      "Sonne    Herz    Gold",
      "Merkur    Lungen    Quecksilber",
      "Venus    Nieren    Kupfer",
      "Nun müssen wir, wenn wir mit den Regsamkeiten, die in diesen Metallen sich finden, die überhandnehmenden Regsamkeiten des inneren Organismus bekämpfen wollen, uns darüber klar sein, daß alles im Organismus mehr oder weniger zusammenhängt und daß ja die einzelnen Organsysteme parallel miteinander gebildet werden, daß also nicht etwa der Mensch zuerst als kopfloses Wesen entstan­den ist; sondern es bilden sich natürlich diejenigen Organe, welche in Zusammenhang stehen mit dem oberen Blutkreislauf, das Gehirn­Rückenmarksystem, gleichzeitig mit den Organen des inneren Welt-systems.",
      "Wie wir gesehen haben, daß es einen nach oben gehenden und einen nach unten gehenden Blutkreislauf gibt, so haben wir auch ein Hinaufwirken des Lymphprozesses, dem wir ein dumpfes Bewußt­sein zuerkannt haben, zu den oberen Partien des menschlichen Or­ganismus. Und es besteht nun die Tatsache, daß das, was dem Blutstrom oben eingegliedert ist, in gewisser Weise demjenigen ent­spricht, was dem unteren Blutstrom eingegliedert ist, und wir können sehen, daß die vorher genannten Metalle auch eine Verwandtschaft haben zu dem oberen Organsystem des Menschen. Sie wissen, daß die Lunge sich aufschließt nach außen zum Kehlkopf, der ein Organ des oberen menschlichen Organismus ist. Wie wir für die Galle im unteren Organsystem einen Zusammenhang zu sehen haben mit dem Eisen, so können wir das Eisen im oberen Organsystem in Verbin­dung bringen mit dem Kehlkopf. Diese Dinge sind natürlich schwierig,",
      "aber ich möchte doch einiges davon andeuten. So wie wir einen Zusammenhang vermerkt haben zwischen Galle und Kehlkopf in bezug auf das Eisen, so gibt es auch in bezug auf das Zinn - Jupiter -eine gewisse Entsprechung zwischen den oberen Teiles unseres Kopfes mit allem, was als Vorderhaupt und als Gehirnbildung dazu­gehört, und der Leber; und in bezug auf das Blei - Saturn - eine Entsprechung zwischen Hinterhaupt und Milz.",
      "Auf diese Weise haben wir unsere Betrachtungen erstrecken kön­nen auf alles das, was dem menschlichen Blutkreislauf eingegliedert ist in den sieben Gliedern des inneren Weltsystems, und darauf, wie es in Zusammenhang steht mit der äußeren Welt. Für das normale wie für das abnorme Leben können wir diese Entsprechungen in Betracht ziehen. In diesen Entsprechungen der Metalle zu den inne­ren Organen haben wir eine höchst interessante Tatsache. Und wenn einmal nicht in chaotischer Weise, sondern systematisch dasjenige untersucht und zusammengestellt würde, was unsere therapeutischen Bücher an vielfachen Angaben enthalten, dann würden diese Ent­sprechungen sich schon ganz von selbst nachweisen lassen aus den äußeren Tatsachen. Und wenn heute solche Ausführungen noch als Phantasiegebilde betrachtet werden, so kann sich der Okkultist dazu ganz ruhig verhalten, denn er weiß, daß die Zeit kommen muß, wo die äußeren Tatsachen seine Behauptungen bestätigen werden.",
      "Nun dürfen wir nicht denken, daß wir zum Beispiel bei einer Nierenkrankheit ohne weiteres gewöhnliches Kupfer geben müßten; das wäre natürlich ein Fehler. Wenn wir dem Organismus metallische Substanzen zuführen wollen, so müssen wir sie erhitzen, so daß sie in eine Art Metalldampf übergehen. Dabei entwickelt sich etwas wie dampfförmige Körperchen, und in dieser Form kann die Metallität auf die inneren Organe wirken. Nehmen wir jetzt das Blutsystern, so wäre bei Erkrankungen mit Metallen nichts geholfen. Wir haben schon darauf hingewiesen, daß im Blutsystem eine Art Salzablage­rung vor sich geht. Und geradeso nun, wie auf die inneren Organe das Metallische wirkt, so wirkt auf das Blutsystem das Salzartige. Will man nun das Blutsystem durch äußere Mittel beeinflussen, so muß man ihm Salzartiges zuführen. Dies kann geschehen durch",
      "Einatmen von salzhaltiger Luft, durch Salzbäder oder dergleichen. Wir können aber auch von der anderen Seite, durch den Verdauungs-prozeß, Salze oder Salzbildendes zuführen, so daß wir in der Lage sind, von zwei Seiten her den Prozeß der Salzbildung, der Salz­einlagerung hervorzurufen.",
      "Wenn Sie sich erinnern an das, was ich gestern ausgeführt habe über die physischen Wirkungen der inneren geistig-seelischen Pro­zesse, so werden Sie sich leicht denken können, daß alles dasjenige, was im Gegensatz zu den im Metallischen wirkenden Vorgängen steht, die physische Wirkung der Gefühlsprozesse ist, denn diese Gefühlsprozesse stehen in engstem Zusammenhang mit den Quel­lungsprozessen im Blut, die aber aufgehalten werden können durch Zuführung äußerer metallischer Stoffe, welche die entgegengesetzte Regsamkeit zeigen. Wenn zum Beispiel die Verdauungstätigkeit überhand nimmt und dort, wo der Ernährungsstrom vom Ätherleib ergriffen wird, eine eigene Regsamkeit entwickelt, so können wir dieser entgegenwirken durch geeignete Salzzuführung; denn, über­treibt der Ätherleib diesen Prozeß des Ergreifens des Ernährungs­stromes, so bedeutet das ein zu starkes Aufnehmen des Salzes. Er muß abgedämpft werden durch die Zufuhr der äußeren Regsamkeit eines Salzes.",
      "Dann haben wir Prozesse, welche sich äußerlich abspielen als Verbrennungs- oder Oxydationsprozesse; das sind solche Prozesse, wo sich etwas mit dem Sauerstoff der Luft verbindet. Alle diejenigen Stoffe, die sich leicht mit dem Sauerstoff der Luft verbinden, durch-strahlen, wenn sie in den Organismus aufgenommen werden, mit ihrer Regsamkeit den Organismus am weitesten. Während Salze, wenn wir sie dem Organismus zuführen, nur bis zu einem mäßigen Grade auf den Organismus wirken, kann die Metallität bis in das innere Weltsystem hinein wirken. Und in der Luft, also in den Stoffen, die sich leicht mit dem Sauerstoff der Luft verbinden, haben wir etwas, was, wenn es in den Körper aufgenommen wird, den ganzen Organismus durchstrahlt bis in das Blutsystem hinein. So werden wir es begreiflich finden können, daß wir durch solche Vor­gänge, die eine zu starke innere Regsamkeit in der Wärmeentwickelung",
      "bilden, die ja der äußere Ausdruck der Willensimpulse ist, in unserem ganzen Organismus uns beeinflußt fühlen. Bei den organi­schen Rückwirkungen des Denkerischen ist das nicht so; wenn wir auf diese unser Augenmerk richten, fühlen wir, daß diese Wirkungen nur in gewissen Organen sich abspielen. Sie sehen daraus, wie außer­ordentlich kompliziert der ganze Apparat des menschlichen Organis­mus ist und wie kompliziert sein Verhältnis zur Außenwelt ist.",
      "So haben wir jetzt gezeigt, wie dem menschlichen Organismus mit seiner eigenen inneren Regsamkeit entgegengesetzt werden kann die äußere unorganische, unbelebte Natur, und wie durch Salze und durch verdampfte Metallität auf den Organismus eingewirkt werden kann. Aber wir haben auch die Möglichkeit, aus anderen Bereichen der Natur auf den Menschen einzuwirken.",
      "Wir können dem mensch­lichen Organismus ebenso das entgegensetzen, was die regsamen Kräfte in der Pflanzenwelt sind. Wenn wir ein pflanzliches Heilmittel einfach als Nahrung aufnehmen, so würden wir dadurch nicht viel erreichen, weil, wie wir gesehen haben, die inneren Organe dafür sorgen, daß den eingenommenen Stoffen ihre eigene Regsamkeit genommen wird.",
      "Soll also die Pflanze in den menschlichen Organis­mus so aufgenommen werden, daß sie auch in ihrer Eigenschaft als Pflanze weiterwirkt, so kann das nicht geschehen, wenn wir sie als Nahrung zu uns nehmen. Dieses Pflanzliche kann auf das Ich nicht einwirken, denn die Pflanze hat als höchstes Glied nur einen Äther­leib.",
      "Das Pflanzliche wird also einfach aufgenommen, da wo der Nahrungsstrom eingefangen wird vom Ätherleib, so daß das Pflanz-liche als Heilmittel noch nicht im Verdauungskanal in Betracht kom­men kann, sondern erst in jenen Organen, in die neben dem Äther-leib auch schon der astralische Leib des Menschen hineinwirkt. Aus diesem Grunde beginnt das Pflanzliche erst zu wirken auf das innere Weltsystem und auf das sympathische Nervensystem und das Lymphsystem.",
      "Nicht mehr erstreckt sich die Wirkung des Pflanzli­chen dahin, wo der Mensch durch das Blut sich wiederum aufschließt der äußeren Welt. Die Pflanze ist zugeordnet dem mittleren Teil des menschlichen Organismus, so daß alles, was in dem Pflanzlichen gesucht werden kann an Regsamkeit, nur wirken kann auf alles das,",
      "was zu dem inneren Weltsystem gehört und auf die entsprechenden Organe des Kopfes und des oberen Teiles des Organismus. Wenn die Tätigkeiten, die Funktionen dieser Organe gestört sind, wenn sie in einer abnormen Weise wirken, dann kommt zur Bekämpfung die Einwirkung des Pflanzenhaften in Betracht.",
      "Wir haben also gesprochen über die Wirkungen von Metallen, Salzen und Pflanzen. Es ist nun nicht angezeigt, in unseren Betrach­tungen noch auf weitere Arten der Bekämpfung von Unregelmäßig­keiten oder Störungen im menschlichen Organismus einzugehen, nicht so sehr deshalb, weil die Zeit zu kurz ist, sondern in der Hauptsache, weil sich Theosophen am besten fernhalten von all den Gebieten, die heute in den Streit der Parteien hineingezogen werden. Das, was bis jetzt aufgezählt worden ist, gehört nicht dem Streit der Parteien an; man kann es einfach aufnehmen, und dann wird man schon die Richtigkeit einsehen; oder aber die Menschen halten es eben für reinen Unsinn, für Phantasterei. Das macht nichts. Denn da müßte man als Theosoph überhaupt schweigen, wenn man alle Dinge nicht sagen wollte, die von den Menschen als Unsinn angesehen werden. Wenn wir aber die Einwirkungen tierischer Substanzen auf den Menschen untersuchen wollten, so würden wir in den Streit der Parteien hineinkommen und man könnte dann meinen, Theosophie wolle sich einmischen in diesen Streit, der sich abspielt zwischen den Vorkämpfern und den Bekämpfern der Heilmethoden auf dem Gebiete des Tierischen. Und es kann niemals Aufgabe des Theoso­phen sein, sich in solche fanatischen Streitigkeiten zu mischen, denn dann würden wir Gefahr laufen, den objektiven allgemein-mensch­lichen Standpunkt zu verlassen.",
      "Das eine aber haben wir gesehen, wenn auch die Andeutungen alle nur skizzenhaft waren, daß dieser menschliche Organismus ein kom­pliziertes System ist von einzelnen Organen, die auf verschiedenen Stufen der Entwickelung stehen und die in der mannigfaltigsten Weise unter sich und mit dem Gesamtorganismus zusammenhängen. Was als physischer Organismus des Menschen sichtbar ist, was wir mit Augen sehen, mit Händen greifen können, ist nur ein Teil der menschlichen Organisation; das Übersinnliche aber, das da hineinwirkt,",
      "das nehmen wir nicht in solcher Weise sinnlich wahr, das er­schließt sich erst dem geistigen Auge des Sehers. Wir dürfen also nicht sagen, daß alle Organe sich gleichmäßig ausgebildet haben, sondern es hat sich gezeigt, daß wir den menschlichen Organismus so anzusehen haben, daß darin Älteres und Jüngeres zu erkennen ist. Wir haben ja schon hervorgehoben, daß wir zum Beispiel das Gehirn als ein älteres, höher entwickeltes Organ anzusehen haben als das Rückenmark und daß das Gehirn früher gewissermaßen auf der Stufe des Rückenmarks gewesen ist. In analoger Weise können wir das Verdauungs- und das Blutsystem betrachten gegenüber dem Lymphsystem. Hier haben wir das Lymphsystem vergleichsweise auf die Stufe des Rückenmarks zu stellen, es ist also das jüngere, während das komplizierte Verdauungs-und das Blutsystem bereits in vielfacher Weise umgewandelt und älter sind als das Lymphsystem, das sich nicht nach außen aufschließt und seine Stoffproduktion nur nach innen in die Gewebe absondert. Das ist ein sehr wichtiger Gesichtspunkt. Wir haben also unser heutiges Lymphsystem anzusehen als etwas, das, wenn es nicht eingelagert wäre den anderen Systemen, bei fortschreitender Entwickelung zu einem Verdauungs- und Blutsystem würde.",
      "Ein einfacheres Vermittlungssystem des Bewußtseins haben wir im Lymphsystem; das, was komplizierter ist, haben wir im Verdauungs­Blutsystem. Wir haben also im menschlichen Organismus Organe zu suchen, welche aus Organsystemen hervorgegangen sind, die früher andere Aufgaben hatten. Die Mitteilungen, die hier darüber gemacht worden sind, würden auch für die äußere Wissenschaft sehr klar nachzuweisen sein, wenn man sich damit vertraut machen wollte. Alles, was über die Umwandlung der Organe gesagt worden ist, läßt sich nachweisen durch embryologische Untersuchungen. Bei einem jeglichen Lebewesen ist es so, daß dasjenige, was im Laufe der Entwickelung später erscheint, in der Keimanlage bereits vorgebildet ist. Wenn wir vom ausgebildeten Menschenorganismus bis zum befruchteten Keim zurückgehen, so könnten wir mit geeigneten Methoden die komplizierten Organsysteme in ihrer allerersten Anlage bereits angedeutet finden, und zwar so, daß sie selbst in der allerersten Anlage schon zeigen, wie sie eigentlich zueinander stehen.",
      "Wenn Sie sich einmal das anschauen, was wir als äußere Umhül­lung, als Begrenzung des Menschen vor uns haben in seiner Haut, und dann weiterhin das, was zu den ihr eingelagerten Sinnesorganen führt, so werden Sie sich sagen können, daß alles das, was da in dieser äußersten Begrenzung des Menschen vorhanden ist, schon umgewan­delt sein muß aus einem Anderen. Denn es ist schon ein sehr kompli­ziertes System, dem auch ein Gehirn angehört; und ein Gehirn ohne langwierige Vorbereitung sich zu denken ist unmöglich. Wir müssen uns also denken, daß die äußere Umhüllung des Menschen ein Umwandlungsprodukt ist, ähnlich wie wir ja das Gehirn als ein umgewandeltes Rückenmark bezeichnet haben und das Ernährungs­und Blutsystem als ein Umwandlungsprodukt des Lymphsystems. Während nun das Rückenmark und das Lymphsystem auf früheren Stufen eine aufsteigende Tendenz zeigten, müssen wir von dem heu­tigen Rückenmark- und Lymphsystern sagen, daß sie in absteigender Entwickelung begriffen sind. Man würde auch zeigen können, daß das Blut in seiner heutigen Konfiguration ein doppeltes Umwandlungs-produkt ist. Dadurch, daß sich das Verdauungs- und Blutsystem nach außen aufschließt, wird es zu einem umgewandelten Lymph­system. Wäre das Verdauungssystem mit seinen Bewegungen nur",
      "# Bild s. 172",
      "nach innen hin entwickelt, wäre es ganz nach innen abgeschlossen, hätten wir in ihm eine ähnliche Tätigkeit wie in der heutigen Lymph­tätigkeit. Bei ihr wird nur dasjenige aufgenommen, was über die Gewebe zugeführt wird.",
      "So ist auf der einen Seite in der äußeren Umgrenzung des Men­schen, im Hautsystem, ein Umgewandeltes zu sehen aus einem ande­ren System, dem Blutsystem, das ich hier so zeichnen will, und auch in dem Verdauungssystem haben wir die Umwandlung aus einem anderen System zu sehen, das heute in absteigender Entwickelung ist. Wir müssen nun festzustellen suchen, ob wir diese auf- und abstei­gende Natur von Organsystemen schon angedeutet finden in der Keimanlage. Und in der Tat zeigt sich, daß wir den Gesamtorganis­mus in der Keimanlage angedeutet finden - ich will es schematisch zeichnen - in den vier übereinanderliegenden Keimblättern, die man nennt: das äußere Keimblatt - Ektoderm -, das innere Keimblatt -Entoderm - und das Mesoderm - das äußere und das innere mittlere Keimblatt.",
      "# Bild s. 173",
      "Dabei haben wir im Sinne unserer Anschauung über die Entwicke­lung das äußere Keimblatt, das Ektoderm, das man in der heutigen Anatomie auch das Hautsinnesblatt nennt, anzusehen als ein Umwandlungsprodukt, das seine erste Anlage zeigt in dem äußeren Mittelblatt, dem äußeren Mesoderm. In diesem haben wir dasjenige als Keimanlage vor uns, was auf einer höheren Stufe in dem Hautsin­nesblatt uns vor Augen tritt. Und in dem inneren Mittelblatt, dem inneren Mesoderm, haben wir die jüngere Bildung dessen vor uns, was sich später im Entoderm, im Darmdrüsenblatt, zeigt.",
      "Wenn wir den menschlichen Keim in seiner Entwickelung betrach­ten, so haben wir die erste Anlage des Menschen in den beiden mittleren Keimblättern angedeutet, in den Mesodermen; die beiden",
      "anderen Keimblätter, Ektoderm und Entoderm, sind bereits umge­wandelt. Die beiden Mittelblätter sind also die, welche den ursprüng­lichen Zustand darstellen, während Ektoderm und Entoderm die höhere Entwickelung zeigen.",
      "Nun wissen wir, daß die entwickelungsfähige Keimanlage des Menschen zusammenfließt aus zwei Anlagen, aus der weiblichen und der männlichen Keimanlage, und daß eine Neuentwickelung nur entstehen kann durch das lebendige Zusammenwirken dieser beiden Anlagen. In den beiden Keimanlagen müssen also getrennt enthalten sein alle die Prozesse, die nur vereint die Keimanlage für den mensch­lichen Organismus bilden.",
      "Was zeigt uns nun der Okkultismus in bezug auf die hierbei obwaltenden Verhältnisse? Er zeigt uns, daß unter den heutigen physischen Bedingungen der weibliche Keim [Entoderm] nur im­stande ist, eine solche menschliche Körperanlage zu produzieren, die, wenn sie sich einzeln entwickeln wollte, nicht das entwickeln könnte, was wir das Formprinzip nennen, das zuletzt zur Einlage­rung des Knochensystems führt, das dem Menschen seine Festigkeit gibt; und auch das Hauptsinnessystem würde nicht durch den weib­lichen Keim geliefert werden können.",
      "Es ist der weibliche Keim so angelegt, daß man fast sagen könnte, das, was da entsteht, würde zu gut sein für die Welt, so wie sie heute besteht, denn es sind nicht alle Prozesse in der äußeren physischen Welt vorhanden, welche einem solchen Organismus notwendig wären. Dieser weibliche Menschen-Organismus könnte sozusagen nicht bis zu jener «Vererdigung» fort­schreiten, wie sie in dem eingelagerten Knochensystem zum Aus­druck kommt, und er hätte nicht die Möglichkeit, verbunden zu sein mit der Außenwelt durch die Sinne.",
      "Er müßte in den äußeren Bedin­gungen eine Stütze finden, um sein weicheres inneres Material, das er anstelle des festen Knochengerüstes hätte, auszugleichen; er könnte sich nicht nach außen aufschließen, sondern würde in seinem inneren Leben abgeschlossen bleiben. Das ist der weibliche Anteil an der Keimanlage; er würde über das Ziel dessen hinausschießen, was heute in unserem irdischen Dasein möglich ist, einfach weil in den heutigen physischen Erdenverhältnissen nicht die Bedingungen gegeben sind,",
      "welche ein solcher verfeinerter Organismus nötig hätte, der so wenig zur Vererdigung und zum Aufschließen nach außen angelegt ist. Ein solcher Organismus wäre unter den heutigen irdischen Verhältnissen von vornherein zum Tode bestimmt. So ist wirklich der mensch­lichen Keimanlage, gerade durch die Tendenz, daß der Mensch in seiner Fortentwickelung zu weit kommen könnte, schon die Ursache dafür eingeprägt, daß der Mensch zum Tode bestimmt ist.",
      "Der andere Anteil der Keimanlage, der männliche [Ektoderm], ist in der genau umgekehrten Lage. Wenn die männliche Keimanlage allein sich entwickeln würde, so würde dies zu mächtiger Entfaltung dessen führen, was sich kundgibt in dem Sichaufschließen nach außen im Hautsinnessystem, und dessen, was zur Verfestigung im Knochen­system führt, also nach der anderen Seite über das Ziel hinausschie­ßen.",
      "Eine solche Einseitigkeit würde ebensowenig eine lebensfähige Keimanlage hervorbringen können wie der weibliche Keim für sich, denn der Organismus, den die männliche Keimanlage entwickeln würde, würde so starke Kräfte entfalten, daß er sich selbst zerstören und zugrunde gehen müßte unter den Verhältnissen, wie sie heute auf der Erde vorhanden sind, das heißt, er würde unter diesen heutigen Verhältnissen auf der Erde als Organismus nicht bestehen können. Der männliche Keim kann daher nur dann zu einem lebensfähigen Ausdruck kommen, wenn er mit der weiblichen Keimanlage zusam­menwirkt.",
      "Nur dadurch, daß die beiden Keirnanlagen sich ausglei­chen, daß dasjenige, was in der weiblichen Keimanlage zum Tode bestimmt ist, sich ausgleicht mit dem der männlichen Keimanlage durch den Befruchtungsprozeß, ist eine lebendige Gesamtanlage des Menschen möglich. Was an Kräften zusammengedrängt vorhanden ist in der männlichen Keimanlage, das würde, wenn es für sich allein auswachsen würde, unendlich unter das Irdische hinunterführen, es würde zu einer viel größeren Verhärtung des Knochensystems füh­ren, zu einem weit größeren Sichaufschließen und Aufgehen in der Außenwelt.",
      "Diese beiden organischen Keime müssen sich schon in ihrer allerersten Entstehung zu weiterer Entwickelung zusammenfin­den, denn einzeln ist jede von ihnen zum Tode bestimmt. Nur die lebendige Wechselwirkung dessen, was nach beiden Seiten hin das",
      "Überhandnehmen des einen über das andere verhindert, ergibt die für das Erdendasein des Menschen mögliche Keimanlage.",
      "So sehen wir, wenn es auch nur in skizzenhafter Art gezeigt werden konnte, daß wir die geistigen Tatsachen bis dahin zurückver­folgen können, wo der Mensch seinesgleichen hervorbringt. Wir würden dies natürlich noch viel ausführlicher darstellen können, aber in einem kurzen Zyklus läßt sich natürlich nicht alles sagen. Wenn wir noch tiefer hineinleuchten würden, so würden wir sehen, wie sich bewahrheitet, daß auch das Minuziöseste auf geistige Tatsachen zurückgeht, bis hin zu dem, was hier über die übersinnlichen Kraft­systeme gesagt worden ist, die ihren äußeren Ausdruck finden in den Organsystemen, die der Mensch entwickelt, damit sein Geschlecht über die Erde hin lebt.",
      "Wir haben gesehen, daß die Erde als Ergebnis des dichtesten «Ver­erdigungsprozesses» in uns hervorgebracht hat das Knochensystem, und als das am wenigsten verdichtete, als das regsamste, das Blut­system. Und es soll nur noch kurz hinzugefügt werden, daß alles, was vorgeht im irdisch-physischen Menschenorganismus, hinauf-dringt bis zu den Vorgängen, die sich im Blute abspielen; das sind die Erwärmungsvorgänge. Wir haben in diesen Erwärmungsvorgängen des Blutes den unmittelbaren Ausdruck des Ich und damit das ober­ste Niveau zu sehen, und darunter sich abspielend die anderen Pro­zesse des menschlichen Organismus. Der Erwärmungsprozeß ist also das Höchste, in diesen greift unsere Ich-Seelentätigkeit unmittelbar ein. Deshalb fühlen wir auch etwas wie eine Verwandlung unserer Ich-Seelentätigkeit in ein inneres Warmwerden, das bis zum physi­schen Warmwerden im Blutprozeß gehen kann. Wir sehen also, wie das Geistig-Seelische von oben nach unten gehend durch den Erwär­mungsprozeß eingreift in das Organische, das Physiologische, und wir könnten noch an vielen anderen Tatsachen zeigen, wie das Gei­stig-Seelische sich in Erwärmungsprozessen berührt mit dem Orga­nischen. Erwärmungsprozesse haben wir auch durch die Vorgänge in den Ernährungsorganen. Durch die Tätigkeit der komplizierten Apparate des Ernährungssystems finden die mannigfaltigsten Ver­wandlungen statt, durch die es im physischen Organismus zu Erwärmungsprozessen",
      "kommt. Diese erstrecken sich von unten nach oben. Es reicht also im Erwärmungsprozeß der physische Organismus des Menschen bis hinauf ins Geistig-Seelische. Hören damit die Umwandlungen auf? Oder gehen sie weiter? Was dann folgt, kann nur angedeutet werden; es muß zunächst dem weiteren Nachdenken und namentlich Nachfühlen eines jeden Zuhörers überlassen werden. Wenn wir diese Umwandlungen mit Gefühlen wirklicher Ehrfurcht für den menschlichen Organismus betrachten können, so lernen wir einsehen, daß Physiologie nicht eine trockene Wissenschaft zu sein braucht, sondern eine Quelle höchster menschlicher Erkenntnis sein kann.",
      "Was der Organismus produziert an innerer Wärme in unserem Blut, an Wärme, die er uns durch die gesamten inneren Prozesse zuleitet, das zeigt, daß wir in den Erwärmungsvorgängen etwas zu sehen haben wie eine Blüte aller anderen Prozesse im Organismus. Die innere Wärme des Organismus dringt bis hinauf in das Geistig-Seelische und kann sich bis in Geistig-Seelisches hinein verwandeln.",
      "Das ist das Höchste, das Schönste, das durch die Kraft des Men­schenleibes Physisches umgewandelt werden kann in Geistig-Seeli­sches. Wenn alles, was im menschlichen irdischen Organismus veran­lagt ist, zu Wärme geworden ist und die Wärme vom Menschen in der rechten Weise umgewandelt wird, dann entsteht aus der inneren Wärme Mitgefühl und Interesse für andere Wesen.",
      "Wenn wir durch alle Prozesse des menschlichen Organismus hindurch aufsteigen bis zum obersten Niveau, den Erwärmungsprozessen, so schreiten wir gleichsam durch das Tor des menschlichen Organismus, das gebildet wird durch die Wärmeprozesse, hinauf bis dahin, wo die Wärme des Blutes verwertet wird durch das, was die Seele daraus macht. Durch lebendiges Interesse für alle Wesen, durch Mitgefühl für alles, was um uns herum ist, erweitern wir, indem unser physisches Leben uns bis zur Wärme hinaufführt, unser Geistig-Seelisches über das ge­samte irdische Dasein, und wir machen uns eins mit dem gesamten Dasein.",
      "Es ist eine wunderbare Tatsache, daß die Weltwesenheit den Umweg gemacht hat durch unseren physischen Organismus, um uns zuletzt die innere Wärme zu geben, die wir Menschen in der Erdenmission",
      "berufen sind umzuwandeln durch unser Ich in lebendiges Mitfühlen mit allen Wesen.",
      "Wärme wird in Mitgefühl umgewandelt in der Erdenmission!",
      "Die Tätigkeit des menschlichen Organismus benützen wir sozusa­gen als Heizwärme für den Geist. Das ist der Sinn der Erdenmission, daß der Mensch als physischer Organismus dem Erdenorganismus so eingelagert ist, daß alle physischen Prozesse zuletzt ihre Vollendung, ihre Krone in der Blutwärme finden, und daß der Mensch als Mikro­kosmos in Erfüllung seiner Bestimmung diese innere Wärme wie­derum umwandelt, um sie auszuströrnen als lebendiges Mitgefühl und Liebe für alles, was uns umgibt.",
      "Durch alles, was wir aus leben­digem Interesse in unsere Seele aufnehmen, wird unser Seelenleben erweitert. Und wenn wir dann durch viele Inkarnationen gegangen sind, in denen wir alle Wärme, die uns gegeben worden ist, verwertet haben, dann wird die Erde ihr Ziel, das innerhalb der Erdenmission zu erfüllen war, erreicht haben, dann wird sie als Erdenleichnam hinuntersinken und dem Verfall überliefert sein.",
      "Und aufsteigen wird die Gesamtheit aller jener Menschenseelen, die die physische Wärme umgewandelt haben in Herzenswärme. Wie die einzelne Seele, wenn der Mensch durch die Pforte des Todes gegangen ist, aufsteigt zu einer geistigen Welt, nachdem der physische Leichnam den Erden-kräften übergeben wurde, so wird einstmals der Erdenleichnam den Weltenkräften übergeben werden, und die einzelnen Menschenseelen werden zu neuen Daseinsstufen fortschreiten.",
      "Nichts in der Welt geht verloren. Was die Menschenseelen als Früchte auf der Erde errungen haben, das wird durch die Menschenseelen in Ewigkeiten hinübergetragen.",
      "So gestattet uns die Geisteswissenschaft, auch die physiologischen Prozesse im menschlichen Organismus anzuknüpfen an unsere Ewigkeitsbestimmung. Wenn uns die Geisteswissenschaft (Theoso­phie) nicht bloße Theorie, nicht bloß abstrakte Erkenntnis ist, son­dern wenn wir sie so betrachten, daß sie uns zeigt: wir stehen als Menschen nicht nur auf der Erde, sondern wir gehören zum gesam­ten Weltensystem -, und wenn wir lernen, so über die Bestimmung des Menschen zu denken, daß er die Kräfte von der Erde nimmt, um",
      "in die Ewigkeit hineinzuwirken, dann nehmen wir durch Geisteswis­senschaft (Theosophie) das auf, was durch sie errungen werden muß. Und wenn die Menschen, die dieses hohe Ideal ahnen oder erkennen, sich brüderlich zusammenfinden und übereinstimmen in ihrem Stre­ben, das heißt, wenn wir erkennen, daß in uns selbst die Keime zur Weiterentwickelung enthalten sind, die fruchtbar werden können für die weitere Erden- und Menschheitsentwickelung, dann können wir in aller Bescheidenheit das Gefühl haben, daß wir als Tbeosophen (Anthroposophen) durch die Entwickelung unserer eigenen Kräfte mitwirken können an der Erfüllung der Erdenmission.",
      "Wir sind hier zusammengekommen und werden nun wieder hin­ausgehen, um draußen zu leben und vielleicht manches von dem, was ja nur skizzenhaft hier als Anregung hat gegeben werden können, mit hinaus zu nehmen und weiter zur Entfaltung zu bringen. Aber auch wenn wir in der Welt zerstreut sind, so wollen wir in lebendigen Gedanken und Empfindungen und mit unserem ganzen Wollen mit­einander harmonisch zusammenwirken. In diesem Geiste wollen wir voneinander scheiden, in diesem Geiste wollen wir uns auch wieder­finden, wenn dazu Gelegenheit sein wird."
    ],
    "sentences": [
      [
        "Es wird heute in diesem letzten Vortrage meine Aufgabe sein, die Betrachtungen der letzten Tage über okkulte Physiologie, die man­ches, wenn auch zum Teil recht skizzenhaft, von den Vorgängen der menschlichen Organisation darzustellen versuchten, zu einer Art von Gesamtbild zu vereinigen, das ja wieder nur skizzenhaft sein kann, durch das wir in den Stand gesetzt werden können, eine Anschauung zu bekommen von dem lebendigen Leben und Weben des mensch­lichen Organismus.",
        "Wir werden dabei am besten tun, wieder von dem gröbsten auszugehen, von der Wechselbeziehung zwischen dem menschlichen Organismus und der äußeren Welt, unserer physischen Erde, in der Aufnahme der Nahrungsstoffe."
      ],
      [
        "Diese Nahrungsstoffe werden ja, nachdem sie aufgenommen sind, in der mannigfaltigsten Weise umgewandelt und stufenweise so umgeändert durch die verschiedenen Organwirkungen, daß sie hin-geleitet werden können zu den einzelnen Gliedern des menschlichen Organismus, zu den einzelnen Systemen der menschlichen physi­schen Wesenheit.",
        "Es ist ja nicht schwer einzusehen, daß alles, was aus den Nahrungsstoffen im menschlichen Organismus wird, im Grunde genommen den Menschen, wie er vor uns steht in der physischen Welt, eigentlich erst zum physischen Menschen macht.",
        "Es liegt hier ja allerdings eine gewisse Schwierigkeit für das Verständnis vor.",
        "Allein, wenn wir Ernst machen mit den bisher eingehaltenen Prinzipien und die übersinnliche Erkenntnis wirklich auf die Betrachtung des Men­schen anwenden, so müssen wir sagen, daß es nur die Nahrungsstoffe sind, die von der äußeren Welt substantiell in den menschlichen Organismus aufgenommen werden.",
        "Alle übrigen auf den Menschen einwirkenden Einflüsse haben wir uns im Grund genommen zu denken als übersinnliche, unsichtbare Kräfte.",
        "Wenn sie sich für einen Moment alles wegdenken, was den menschlichen Organismus, von den Nahrungsstoffen herrührend, ausfüllt, so behalten Sie in phy­sischer Beziehung noch weniger - verzeihen Sie den trivialen Ausdruck-,"
      ],
      [
        "viel weniger übrig als einen leeren Sack, nämlich gar nichts.",
        "Denn auch was an Haut, an Umhüllung des physischen Organismus vorhanden ist, ist nur dadurch vorhanden, weil entsprechend verar­beitete Ernährungsstoffe an die betreffenden Partien hingeführt wor­den sind."
      ],
      [
        "Rechnen Sie die Nahrungsstoffe und was aus ihnen wird, weg, so haben Sie dahinter den menschlichen Organismus nur als ein übersinnliches Kraftsystem zu denken, das die Verteilung der assimi­lierten Nahrungsstoffe nach allen Richtungen hin bewirkt.",
        "Wenn Sie diesen Gedanken, wie er jetzt ausgesprochen worden ist, sich so richtig vor die Seele stellen, so werden Sie sich sagen: Eines ist aber eigentlich die Voraussetzung, bevor irgend etwas, auch das kleinste, von den Nahrungsstoffen aufgenommen werden kann, denn diese Stoffe können nicht von der Außenwelt in jedes beliebige Wesen bineinbefördert werden, damit dasjenige in ihm vorgehe, was im menschlichen Organismus vorgeht."
      ],
      [
        "Es muß der Mensch schon bei der allerersten Nahrungsaufnahme den physischen Nahrungsstoffen eine innere Kraftwirkung entgegenstellen können, welche aus der übersinnlichen Welt stammt, und es muß in diesem inneren Kräfte-system der Mensch als solcher schon enthalten sein.",
        "Im Okkultismus nennen wir dasjenige, was so den eigentlichen physischen Ausfül­lungsmaterialien vom Menschen zunächst entgegengehalten wird, was durchaus schon übersinnlich zu denken ist, das nennen wir im umfassendsten Sinne die menschliche Form."
      ],
      [
        "Wenn wir uns die aller-unterste Grenze der menschlichen Organisation denken, so müssen wir uns vorstellen, daß sich gegenüberstehen die physische Materie und die übersinnliche Form, welche als ein aus den übersinnlichen Welten herausgeborenes Kraftsystem dazu bestimmt ist, die Materie aufzunehmen - nicht wie ein physischer Sack oder BaIg, sondern wie ein Überphysisches, ein Übersinnliches - und dasjenige herauszubil­den, was überhaupt den Menschen erst physisch-sinnlich erscheinen läßt.",
        "Erst dadurch, daß sich dieser übersinnlichen Form eingliedert das assimilierte Ernährungsmaterial, wird der sonst rein übersinnli­che menschliche Organismus zu einem physisch-sinnlichen Organis­mus, den man mit Augen sehen und mit Händen greifen kann."
      ],
      [
        "Man nennt das, was so entgegengehalten wird der physischen Materie, aus"
      ],
      [
        "dem Grunde «Form», weil eigentlich in aller Natur ein solches Gesetz wirkt, ein genau gleiches Gesetz, das überall «Formprinzip» genannt wird.",
        "Wenn wir die äußere Welt betrachten, so finden wir, daß bis zum Kristall hinunter überall das Formprinzip tätig ist.",
        "Die Substanzen, welche in den Kristall eintreten, müssen, um das zu werden, als was der Kristall sich darstellt, gleichsam eingefangen werden von dem Formprinzip, und dieses macht mit Hilfe der Sub­stanzen den Kristall erst zu dem, was er ist.",
        "Nehmen Sie zum Beispiel das Kochsalz, Chlornatrium, so haben Sie als physische Substanzen miteinander verbunden Chlor und Natrium, ein Gas und ein Metall.",
        "Sie werden leicht einsehen, daß diese beiden Stoffe, so wie sie sind, bevor sie eingefangen werden durch eine formende Wesenheit und dadurch erst zu einer chemischen Verbindung in Würfeln kristalli­siert erscheinen, jede für sich völlig andere Formen zeigt.",
        "Bevor sie eintreten in dieses Formprinzip, haben sie nichts Gemeinsames; aber sie werden eingespannt, aufgenommen von diesem Formprinzip, und dieses bildet den physischen Körper Kochsalz."
      ],
      [
        "So setzt auch alles, was als umgewandelte Nahrungsstoffe im menschlichen Organismus erscheint, die unterste übersinnliche Wesenheit, die übersinnliche Form voraus.",
        "Wenn nun neue Ernäh­rungsstoffe in den menschlichen Organismus eintreten sollen, der durch das Wirken des Formprinzips bereits nach außen abgegrenzt ist, so müssen sie unter normalen Verhältnissen durch den Mund in den Ernährungskanal aufgenommen werden.",
        "Dabei machen sie gleich schon vom Munde ab die allererste Umwandlung durch.",
        "Durch den Ernährungskanal werden weitere Umwandlungen bewirkt.",
        "Diese Umwandlungen kompliziertester Art könnten nicht bewirkt werden, wenn nicht dem menschlichen Organismus ein höheres Prinzip ein­gegliedert wäre, das wir Formprinzip genannt haben, durch dessen Wirksamkeit die Nahrungsstoffe - die zunächst, wenn sie aufgenom­men werden, sich zueinander neutral, gleichgültig verhalten - modifi­ziert würden, so daß sie in die Lage kommen, lebendige Organe zu bilden.",
        "Wir können uns, obgleich es beim Menschen ein ganz anderer Prozeß ist, weil er auf einer anderen Stufe geschieht, diese Umwand­lung der Nahrungsstoffe im menschlichen Verdauungskanal vergleichsweise"
      ],
      [
        "so vorstellen, wie wenn die Pflanzen ihre Ernährungs­stoffe aufnehmen aus dem mineralischen Boden und sie dergestalt umwandeln, daß sie sich zu der Form der betreffenden Pflanze aufbauen.",
        "Da ist nur möglich, weil bei der Pflanze der Ernährungs­strom von einem Lebensprozeß oder, wie wir im Okkultismus sagen, vom Ätherleib als dem ersten übersinnlichen Prinzip aufgenommen wird."
      ],
      [
        "So werden auch beim Menschen die in den Organismus eintre­tenden Nahrungsstoffe vom Ätherleibe bearbeitet, das heißt, der Ätherleib sorgt für ihre Umwandlung, für ihre Eingliederung in die inneren Gesetzmäßigkeiten des menschlichen Organismus.",
        "So haben wir also dieses erste übersinnliche Glied des Menschen, den Äther-leib, anzusehen als den Erreger der ersten Umwandlung der Nah­rungsstoffe."
      ],
      [
        "Wenn nun diese Nahrungsstoffe soweit umgewandelt sind, daß sie in den Lebensprozeß aufgenommen sind, dann müssen sie in dem Sinne, wie wir es in den vorhergehenden Vorträgen geschildert haben, weiter verarbeitet und dem menschlichen Organis­mus angepaßt werden.",
        "Sie müssen so verarbeitet werden, daß sie nach und nach denjenigen Organen im menschlichen Organismus dienen können, die ein Ausdruck der höheren übersinnlichen Prinzipien sind, des Astralleibes und des Ich."
      ],
      [
        "Kurz, wir müssen uns klar sein, daß die höheren Prinzipien, Astralleib und Ich, die eigentümliche Art ihrer Regsamkeit hinuntersenden müssen bis zu den Vorgängen in den Organen des Ernährungs- und Verdauungsapparates und daß sie bis in die verwandelten Nahrungsstoffe hinab wirken müssen."
      ],
      [
        "Da stellen sich nun dem Nahrungsstrom diejenigen Organe entge­gen, welche uns schon bekannt sind, die wir bezeichnet haben als die sieben Organe des inneren Weltsystems.",
        "Wir zeichnen nochmals ganz schematisch das innere Weltsystem des Menschen:"
      ],
      [
        "Die Nahrungsstoffe werden also aufgenommen und zunächst in der mannigfaltigsten Weise umgearbeitet im Verdauungskanal, dann stellen sich ihnen entgegen Leber, Galle, Milz, Herz, Lunge, Nieren und so weiter.",
        "Wenn wir uns nun darüber klar sind, daß diese Or­gane durch die ihnen entsprechenden Kraftsysteme dazu bestimmt sind, den Nahrungsstrom weiter umzuarbeiten, so können wir fra­gen: Welches ist der Sinn dieser weiteren Umwandlung? - Wenn der"
      ],
      [
        "# Bild s. 155"
      ],
      [
        "Nahrungsstrom nur so weit bearbeitet würde, wie es im Verdauungs-kanal geschieht, um der Lebensform dienen zu können, so würde der Mensch nur ein unbewußtes Pflanzendasein führen können, denn er hätte es nicht zur Ausbildung solcher Organe gebracht, die Werk­zeuge sein können für seine höheren Fähigkeiten.",
        "Die sieben Organe wandeln den Ernährungsstrom aber weiter um, und wir wissen, daß diese Vorgänge durch das sympathische Nervensystem davon abge­halten werden, in das menschliche Bewußtsein einzutreten.",
        "Daher haben wir in dem sympathischen Nervensystem mit den sieben Organen zusammen dasjenige, was sich dem Nahrungsstrom entge­genstellt."
      ],
      [
        "Damit sind wir schon bis zu einem hohen Grade von außen in das Innere des menschlichen Organismus hineingedrungen.",
        "Aber das, was da drinnen vorgeht, man möchte sagen als die gegenseitige Ange­legenheit der sieben Organe, da ist etwas, was nirgends in unserer Erdenwelt so vorgehen könnte wie da drinnen.",
        "Es kann nur dadurch so vorgehen, daß dieses Innere von der Außenwelt völlig abgeschlos­sen ist und für diese Tätigkeit des Innern die Stoffe vorbereitet sind"
      ],
      [
        "durch den Verdauungskanal.",
        "Also wir stehen darnit schon im Inneren des menschlichen Organismus darinnen."
      ],
      [
        "Nun haben wir das Eigentümliche zu verzeichnen, daß, indem wir so im Innern des Organismus darinnenstehen, der Organismus sich ja selbst innerlich organisieren, sich selbst innerlich differenzieren muß.",
        "Um allen diesen an ihn herantretenden Anforderungen zu genügen, muß der Organismus eine Vielheit zusammenwirkender Organe her-ausbilden."
      ],
      [
        "Für die mannigfaltigen inneren Verrichtungen ist gerade diese Vielheit der Organe notwendig.",
        "Was durch diese erreicht wer­den muß, werden wir im folgenden sehen.",
        "Wenn wir uns denken, daß nur der Nahrungsstrom umgewandelt würde durch die sieben Organe des inneren Weltsystems, da würde der Mensch nimmermehr sein Wesen dem Bewußtsein aufschließen können."
      ],
      [
        "Er würde nicht einmal die dumpfeste Form des Bewußtseins haben können, weil ja alles, was da vorgeht, verhüllt wird, abgehalten wird vom Bewußtsein durch das sympathische Nervensystem.",
        "Es ist also eine Verbindung notwendig zwischen diesen sozusagen von außen her aufgebauten inneren Organsystemen und dem, was weiter im Inneren des menschlichen Organismus ist."
      ],
      [
        "Diese Verbindung wird dadurch her­gestellt, daß in der Tat durch alles das, was der Ernährungsprozeß in seiner Ganzheit gibt, die gesamte Form des menschlichen Organis­mus durchzogen wird von dem, was wir im weitesten Sinne Gewebe nennen.",
        "Eine gewisse Art von Gewebe einfachster Organisation durchzieht alle einzelnen Glieder der menschlichen Wesenheit, das fähig ist, sich so umzuwandeln und auszugestalten, daß sich die verschiedensten Organe herausbilden können."
      ],
      [
        "Gewisse Arten des Gewebes zum Beispiel bilden sich so um, daß sie sich durch Einlage­rung besonderer Zellen zu den Muskeln umgestalten; andere bilden sich so um, daß sie fest werden und sich die Knochenzellen einlagern, indem sie die entsprechenden Substanzen sich aneignen.",
        "So daß wir in den einzelnen Organen des menschlichen Organismus stets an das zu denken haben, was ihnen zugrundeliegt, nämlich das den Körper nach allen Richtungen durchziehende Gewebe, aus dem die einzelnen Organe sich herausbilden."
      ],
      [
        "Dieses bildungsfähige Gewebe würde aber, wenn es noch so sehr zu wachsen und die verschiedensten"
      ],
      [
        "Organe aus sich herauszubilden imstande wäre, doch nichts anderes darstellen als im Grunde nur etwas Pflanzenhaftes; denn das ist ja das Wesentliche des Pflanzenhafte, daß die pflanzlichen Wesen wach­sen, daß sie aus sich Organe hervortreiben und dergleichen.",
        "Indem sich aber der Mensch über das Pflanzenhafte hinaus erhebt, muß sich uns ein ganz neues Element darbieten, durch welches der Mensch in die Lage kommt, zu dem Pflanzenleben dasjenige hinzuzufügen, was ihn über das Pflanzenleben hinaushebt.",
        "Der Mensch muß hinzufügen das Bewußtsein, zunächst die einfachste Form des Bewußtseins, das dumpfe Bewußtsein, das ihn fähig macht, das eigene innere Leben wahrzunehmen.",
        "Solange nicht ein Wesen das eigene innere Leben bewußt miterlebt, solange es noch nicht in der Lage ist, sich innerlich gleichsam zu durchspiegeln, um dieses eigene innere Leben mitzuer­leben, so lange können wir nicht sagen, daß es sich über die Pflanzen­haftigkeit hinauferhebt.",
        "Erst dadurch erhebt sich ein Wesen über die Pflanzenhaftigkeit hinauf, daß es nicht bloß in sich Leben hat, son­dern dieses Leben bewußt erlebt, daß es zunächst diese inneren Vorgänge durchspiegelt und miterlebt."
      ],
      [
        "Wodurch kommt nun überhaupt Erleben zustande?",
        "Dafür haben wir uns schon den Begriff gebildet.",
        "Wir haben ja in den früheren Vorträgen schon gezeigt, daß Erleben zustande kommt durch Absonderungsprozesse.",
        "Deshalb werden wir als die Grundlagen des inneren Erlebens, des dumpfen, die inneren Lebensprozesse durch-ziehenden Bewußtseinserlebens, Absonderungsprozesse suchen müssen.",
        "Wir werden voraussetzen müssen, daß überall aus den Geweben heraus Absonderungsprozesse stattfinden; und in der Tat treten uns diese Absonderungsprozesse schon bei der äußeren Betrachtung des menschlichen Organismus entgegen, wenn wir sehen, wie fortwährend Stoffe aus allen Teilen des Gewebes aufge­nommen werden durch das, was wir die Lymphgefäße nennen, die wie eine Art anderes System neben dem Blutsystem den ganzen Organismus durchziehen.",
        "In das Lymphgefäßsystem münden sozu­sagen von allen Bezirken des menschlichen Organismus diejenigen Absonderungsprozesse, welche das dumpfe innere Erleben vermit­teln.",
        "Könnten wir uns einmal in abstracto das gesamte Blutsystem"
      ],
      [
        "wegdenken und könnten wir uns das Gewebe so denken, daß es nichts mehr hat von blutartigem Charakter, so würden wir uns vorzustellen haben, daß im Blutsystem sich höhere Prozesse abspie­len gegenüber den Prozessen des Lymphsystems.",
        "In diesen Absonde­rungen fühlt der Mensch gleichsam in einem dumpfen tierischen Bewußtsein seinen eigenen physischen Leib.",
        "Dumpf durchspiegelt er seine Organisation.",
        "Und ebenso wie auf der einen Seite durch das sympathische Nervensystem von dem Bewußtsein alles abgehalten wird, was vom Verdauungs- und Ernährungsprozeß und den sieben Organen heraufdringen will, so wird auf der anderen Seite gleich­sam durch Rückstrahlung der Tätigkeit des sympathischen Nerven­systems, durch Verbindung und Wechselwirkung mit den Lymph­bahnen, ein für den heutigen Menschen allerdings vom hellen Tages­bewußtsein überstrahltes dumpfes Bewußtsein ausgebildet.",
        "Es wird überstrahlt vom hellen Tagesbewußtsein des Ich, wie ein schwaches Licht überstrahlt wird durch ein starkes.",
        "Dieses dumpfe Bewußtsein ist gleichsam die andere Seite jenes Bewußtseins, das sich des sym­pathischen Nervensystems als seines Werkzeuges bedient."
      ],
      [
        "Würde der Mensch seinen Organismus nur entwickelt haben bis zur Bildung des Körpergewebes und der Organe, die für die inneren Verdauungsvorgänge und für die Absonderungen in die Lymphbah­nen notwendig sind, so würde er nur ein dumpfes Bewußtsein seines [nnenlebens vermittelt erhalten können.",
        "Er würde aber nicht eine Ausbildung des Ich-Bewußtseins erreichen können; das kann er nur erwerben, wenn er sich nicht bloß in seinem Inneren erlebt, sondern sich auch nach außen aufschließt.",
        "Hier haben wir wiederum ein Sich-aufschließen nach außen zu verzeichnen.",
        "Wir haben ja schon früher davon gesprochen, wie es dem Menschen durch die Atmung möglich wird, unmittelbar mit der Außenwelt in Verbindung zu treten.",
        "Jetzt konnen wir weitergehen und sagen: Sofern wir den inneren Men­schen betrachten, dürfen wir eigentlich nur bis zum Verdauungs-system gehen, denn wir können sagen: Insofern Ausläufer der Orga­ne des inneren Weltsystems bis zum Verdauungskanal sich hinwen­den, haben wir in diesem Anstoßen des inneren Weltsystems an den Verdauungskanal schon ein Sichaufschließen nach außen zu sehen,"
      ],
      [
        "denn der Mensch ist gleichsam bereit, Nahrungsstoffe von außen aufzunehmen.",
        "Indem er mit aus der Umwelt entnommenen Nah­rungsstoffen in enge Berührung tritt, ist er eigentlich schon nicht mehr nur innerlich.",
        "Ein weiteres Sichaufschließen nach außen haben wir kennengelernt in der Atmung, und in noch höherem Maße ist es zu erkennen in jenen Organen, die den seelischen Funktionen dienen."
      ],
      [
        "So also sehen wir, wie dem bewußten Leben des Menschen zugrundeliegt einerseits ein dumpfes Innenleben, andererseits die Fähigkeit, sich der Außenwelt aufzuschließen, mit der Außenwelt Verbindung zu haben.",
        "Dadurch erst kann der Mensch ein Ich-Wesen sein."
      ],
      [
        "Nür dadurch, daß er nicht nur die Widerstände in seinem eigenen Innern in seinen Absonderungsprozessen spürt, sondern auch die Widerstände, die die Außenwelt ihm entgegensetzt, kann der Mensch sein Ich-Bewußtsein entwickeln.",
        "So ist in der Tatsache, daß sich der Mensch auch wieder nach außen aufschließen kann, die Grundlage gegeben für die physische Ichheit des Menschen."
      ],
      [
        "Damit aber muß der Mensch auch die Möglichkeit haben, in der mannigfal­tigsten Weise das Organ dieser Ichheit auszubilden.",
        "Und wir haben ja gesehen, wie in der Tat das Organ der Ichheit, das Blut, sich einglie­dert in den Organismus und wie der Blutkreislauf alle Organe durch­zieht, um ein Werkzeug zu sein für die Ichheit."
      ],
      [
        "So wie die Ichheit geistig-seelisch den gesamten Menschen durchlebt und durchwebt, so durchzieht physisch der Blutkreislauf den gesamten menschlichen Organismus und wendet sich dabei gleichsam nach zwei Seiten, nach dem Innenwesen des Menschen mit den sieben Organen und so weiter, und dann haben wir wieder ein Sichaufschließen nach außen, ein In-Verbindung-Treten mit der äußeren Welt.",
        "Wir können also im höchsten Sinne des Wortes von einem Kreislauf der Kräfte sprechen, welche hinter den physischen Erscheinungen stehen und welche durch das Ich einen Verbindungspunkt finden."
      ],
      [
        "Nun müssen wir uns einmal mit den einzelnen Phasen dieses Kreislaufes noch etwas beschäftigen.",
        "Da handelt es sich ja zunächst darum, daß wir noch einmal den Ernährungsprozeß verfolgen, das Aufnehmen der Nahrungsstoffe, welche dadurch, daß sie vom Äther-leibe oder vielmehr von der Kraft des Ätherleibes ergriffen werden,"
      ],
      [
        "zu einem lebendigen Strom im menschlichen Organismus werden; dann stellt sich ihnen gegenüber das innere Weltsystem, die sieben Organe, und zwar deshalb, weil - wie wir schon gesehen haben - der Mensch sonst nicht hinauskommen würde über das pflanzenhafte Dasein.",
        "Auf einer weiteren, höheren Stufe ist es notwendig, daß sich entgegenstellen dem Nahrungsstrom die Funktionen dieser sieben Organe.",
        "So wirkt also das, was aus der eigentlichen astralischen Natur des Menschen kommt, dem belebten Nahrungsstrom entge­gen; der Nahrungsstrom kommt von außen, und das, was die innere Menschennatur ist, wirkt dem entgegen.",
        "Zunächst begegnet dem Nahrungsstrom, also der aufgenommenen Außenwelt, der Ätherleib, der die Nahrungs stoffe umwandelt im Verdauungs system; dann tritt ihm entgegen der Astralleib des Menschen, wandelt die Nahrungs­stoffe weiter um und gliedert sie so ein, daß sie immer mehr und mehr der inneren Regsamkeit des Organismus angepaßt werden.",
        "In seinem weiteren Verlauf muß der Nahrungsstrom auch erfaßt werden von den Kräften des Ich, des Blutes selber.",
        "Das heißt, es muß das Werkzeug des Ich mit seinem Wirken herunterreichen bis dahin, wo der Ernährungsstrom aufgenommen wird.",
        "Tut dies das Blut?",
        "Bewahrheitet sich das, was wir aus der okkulten Anschauung heraus sagen müssen?"
      ],
      [
        "Ja, das Blut wird heruntergetrieben in die Ernährungsorgane ebenso wie in alle anderen Organe.",
        "Es macht in den Ernährungsorga­nen einen Prozeß durch, durch den es erst das vollständige Werkzeug des menschlichen Ich in der physischen Welt sein kann.",
        "Wir wissen, daß das Blut als Werkzeug des menschlichen Ich den Übergang durchmachen muß von dem sogenannten roten in blaues Blut.",
        "Das Ich wirkt mit seinem Werkzeuge, dem Blut, bis herunter zu den Anfängen der Verdauungs- und Ernährungsprozesse.",
        "Da haben wir es nun auch wieder mit einem Widerstand zu tun.",
        "Wie geschieht das?",
        "Das geschieht, indem das Blut durch das Pfortadersystem in die Leber eintritt und dort aus sozusagen verändertem Blut die Galle bereitet wird und die Galle sich wiederum unmittelbar dem Nah­rungsstrom entgegenstellt.",
        "Hier in der Galle haben wir eine wun­derbare Verbindung der beiden Enden der inneren menschlichen"
      ],
      [
        "Organisation.",
        "Auf der einen Seite stellt der vom Verdauungskanal aufgenommene Nahrungsstrom das äußerste Materielle dar, was in unseren physischen Organismus hineingelangt, auf der anderen Seite steht das Ich, das Edelste, was der Mensch innerhalb der Erdenwelt haben kann, mit seinem Werkzeug, dem Blut.",
        "Das Ich stellt eine un­mittelbare Verbindung her mit dem äußersten Materiellen, indem es am Ende des Blutprozesses auf dem Umwege über die Leber die Galle bereitet, und in der Galle stemmt sich - in dem umgewandelten, veränderten Blut - dem Nahrungsstrom entgegen das Ich."
      ],
      [
        "Da sehen wir das Ich hinunterwirken bis in das gröbste Materielle und dann wieder hochorganisierte Stoffe wie die Galle aus sich heraussetzen.",
        "Und wer diese intimen Vorgänge zwischen Blut, Galle und Ernährungsprozeß verstehen will, der kann gerade in diesen Tatsachen etwas finden, was ihm viele Geheimnisse des menschlichen Organismus klarer erscheinen läßt; und er kann, wenn er diese Pro­zesse weiterverfolgt, zum Beispiel auch abnorme Prozesse, wie sie sich aus einer Rückstauung der Galle, einer Rückergießung der Galle ins Blut bei der sogenannten Gelbsucht ergeben, richtiger beurteilen und behandeln.",
        "Doch das würde heute zu weit führen, wenn wir solche Dinge auch noch ausführten."
      ],
      [
        "So sehen wir, wie in der Tat die sieben Organe sich bis in das Wirken des Ätherleibes hinuntererstrecken und die Einwirkungen des Ich von oben in sich aufgenommen haben.",
        "Wir haben also in der Galle etwas, das sich unter dem Einfluß des Ich dem Nahrungsstrom direkt entgegenstellt.",
        "Will die Galle auf den Nahrungsstrom wirken, der im Verdauungsprozeß schon ein Lebendiges geworden ist, so muß sie ihm auch als eine lebendige Substanz entgegentreten können.",
        "Das geschieht dadurch, daß sie eben aus einem Organ heraus gebildet wird, welches zu den sieben Gliedern des inneren Weltsystems gehört, die das innere des Menschen beleben, so daß damit die Galle als inneres Leben dem von außen kommenden begegnet."
      ],
      [
        "Wie die Galle mit der Leber in Verbindung steht, so finden wir die Leber wiederum in Verbindung mit der Milz.",
        "Wenn wir diese Organe Leber, Galle, Milz ins Auge fassen, so müssen wir sagen, diese Organe sind es, welche sich dem Ernährungsstrom unmittelbar"
      ],
      [
        "entgegensetzen und ihn so umwandeln, daß er fähig wird, zu höheren Stufen der menschlichen Organisation aufzusteigen.",
        "Sie haben aber auch diejenigen Organe zu versorgen, die sich nach außen aufschlie­ßen, und das tun das Herz, die Lungen, auch schon der Verdauungs-kanal selber, vor allen Dingen aber die Organe des Kopfes, die Sinnesorgane."
      ],
      [
        "Nun haben wir uns schon früher klar gemacht, daß alles innere Erleben mit Absonderungsprozessen eng verbunden ist.",
        "Deswegen haben wir auch diese Absonderungsprozesse besonders betrachtet.",
        "Leber, Galle und Milz haben im Sinne jener Vorgänge in der Gesamt-Organisation zunächst nichts unmittelbar mit Absonderungsprozes­sen zu tun, sie sondern zwar Stoffe ab, aber das hat mit der Ernäh­rung zu tun.",
        "Sie vermitteln das aufsteigende Leben, das von den niedersten Lebensformen sich hinwendet zum Organ der Bewußt­beit, zum Bewußtsein selbst.",
        "Indem aber diesen Organen als ein viertes Organ das Herz sich angliedert und das Herz durch den Blutumlauf sich auch nach außen aufschließt, erlangt der Mensch sein Ich-Bewußtsein.",
        "Er würde aber nicht in der Lage sein, dieses Ich als das zu erleben, was der Außenwelt gegenübersteht, wenn er nicht dieses nach außen schauende Ich in Beziehung bringen würde zu dem, was er als dumpfes Bewußtsein seines inneren Leibeslebens schon besitzt.",
        "Er muß zu den Absonderungsprozessen des inneren Organismus noch einen anderen hinzufügen, welcher ihm auch ein Erleben seines Inneren vermittelt mit dem Ich, das im Blute sein Werkzeug hat."
      ],
      [
        "Zunächst erlebt der Mensch durch die Absonderung der Lymphe sein Innenleben nur in dumpfem Bewußtsein.",
        "Dann aber muß auch aus dem Blute abgesondert werden können, und in dieser Absonde­rung wird der Mensch gewahr, daß er als Eigenwesenheit der Außen­welt gegenübersteht, als inneres Ich.",
        "Der Mensch würde aber in seinem Erleben der Außenwelt so gegenüberstehen, daß er sich selbst innerlich verlöre, würde er nicht wissen, daß das dasjenige, was da die Luft atmet und die Ernährungsstoffe von außen aufnimmt und verar­beitet, dasselbe Wesen ist wie das, welches er im Inneren erlebt.",
        "Daß der Mensch sich nicht verliert, daß er mit seinem Eigenwesen der Außenwelt gegenübersteht, das ist dadurch möglich, daß er durch die"
      ],
      [
        "Lungen aus dem umgewandelten Blut absondert die Kohlensäure und durch die Nieren die umgewandelten Stoffe absondert, die aus dem Blut heraus kommen."
      ],
      [
        "Damit sind in ihrer Funktion sowohl die Organe gekennzeichnet, die einen aufsteigenden Prozeß vermitteln, Leber, Galle, Milz, wie auch diejenigen Organe, die einen absteigenden Prozeß vermitteln, Lungen und Nieren.",
        "Wir dürfen da aber nicht schematisieren - das geht bei theosophischen Betrachtungen überhaupt nicht -, wir müs­sen sehen, daß die Lungen, indem sie sich nach außen aufschließen, auch einen aufsteigenden Prozeß vermitteln."
      ],
      [
        "Wir sehen also, wie diese sieben wichtigsten Glieder des inneren menschlichen Weltsy­sterns zusammenhängen mit dem inneren Erleben des Menschen und mit dem Sichaufschließen nach außen.",
        "Diese sieben Glieder ver­wandeln auf der einen Seite die Eigenregsamkeit der Nahrungsstoffe in innere Regsamkeit des Organismus und versorgen mit diesen umgewandelten Stoffen den menschlichen Organismus."
      ],
      [
        "Sie machen es möglich, daß der Mensch sich wieder nach außen aufschließt.",
        "Sie machen es aber auch möglich, daß das, was der Mensch als eine zu starke innere Regsamkeit entwickelt, abgestoßen wird nach außen durch die Absonderungsprozesse der Lungen und Nieren."
      ],
      [
        "Durch die Arbeit der Lungen und Nieren haben wir also eine regelmäßige Regulierung der Regsamkeit der menschlichen Organsysteme.",
        "Dieses ganze Verhältnis, in dem die menschlichen Organsysteme zueinander stehen, das drückt sich so aus, daß man im Okkultismus in der Tat kein besseres Bild dafür geben konnte, als daß man sagte: Das Herz als Sonne steht im Mittelpunkt und beeinflußt die drei Organe des inneren Weltsystems, die die aufsteigenden Prozesse besorgen, Leber, Galle, Milz."
      ],
      [
        "So wie im Makrokosmos die Sonne im Planeten-system steht zu den äußeren Planeten Jupiter, Mars, Saturn, so steht im Mikrokosmos, im menschlichen Organismus, die innere Sonne, das Herz, zu Leber-Jupiter, Galle-Mars, Milz-Saturn.",
        "Ich müßte nun nicht wochenlang, sondern monatelang reden, wenn ich Ihnen alle die Gründe auseinandersetzen wollte, warum vor einem genauen und intimen okkulten Beobachten das Verhältnis der Sonne zu den äuße­ren Planeten unseres Planetensystems wirklich in Parallele gesetzt"
      ],
      [
        "werden darf zu dem Verhältnis, das im menschlichen Organismus das Herz hat zu dem inneren Weltsystem, zu Leber, Galle und Milz.",
        "Es ist in der Tat das äußere Verhältnis absolut so hereingenommen, daß in der Wechselwirkung dieser Organe sich das widerspiegelt, was in der großen Welt des Makrokosmos, in unserem Sonnensystem vor sich geht.",
        "Und ebenso ist es berechtigt, davon zu sprechen, daß die Vorgänge, die sich abspielen zwischen der Sonne und den inneren Planeten bis zu unserer Erde herunter, sich widerspiegeln in dem Verhältnis des Herzens zu den Lungen und zu den Nieren.",
        "So haben wir in diesem inneren Weltsystem des Menschen etwas, was das äußere Weltsystem widerspiegelt."
      ],
      [
        "Wir haben im Verlaufe der Vorträge auch schon angedeutet, wie in der Tat, wenn wir hellseherisch hinuntertauchen in das eigene Innere, wir aufhören, unsere inneren Organe nur so wahrzunehmen, wie sie sich dem äußeren Anblick des physischen Auges darbieten.",
        "Wir mussen hinauskommen über das Phantasiebild, das sich die äußere Anatomie von unseren Organen macht, indem wir aufsteigen zur Betrachtung der wirklichen Gestalt, die diese Organe haben, wenn wir berücksichtigen, daß diese Organe ja Kraftsysteme sind.",
        "Durch die äußere Anatomie kann gar nicht das wirkliche Sein dieser Organe ergründet werden, denn sie sieht ja in ihnen nur die hinein-gestopften umgewandelten Nahrungsstoffe.",
        "Und gerade dadurch, daß die äußere Wissenschaft nur diese Anschauung gelten lassen will, kann sie nicht die inneren Kraftsysteme, welche den Organen zugrundeliegen, erkennen.",
        "Für denjenigen aber, der in der Lage ist, das, was diesen Organen als Kraftsysteme zugrundeliegt, durch hell­seherische Beobachtung zu schauen, der sieht, wie berechtigt es ist, die Organe mit den Namen der Planeten zu benennen, weil er erkennt, wie das Verhältnis zwischen den Planeten unseres äußeren Weltsystems sich wiederholt in unserem inneren Organsystem."
      ],
      [
        "Nun haben wir gestern gesagt, daß die Organe eine zu starke innere Regsamkeit entwickeln können.",
        "Jedes einzelne der Organe kann eine zu starke Regsamkeit entwickeln, und diese Unregelmäßig­keit kann sich so ausdrücken, daß sie sich auf den ganzen Organis­mus auswirkt.",
        "Nun habe ich schon gestern darauf hingedeutet, daß"
      ],
      [
        "wenn durch solche zu starken inneren Regsamkeiten etwas wie ein eigensinniges Eigenleben in den inneren Organen auftritt, es notwen­dig ist, dasjenige entgegenzusetzen, was diese inneren Regsamkeiten dämpft.",
        "Das heißt, wenn die inneren Organe zu stark umsetzen, zu stark umwandeln die äußeren Regsamkeiten der Nahrungsstoffe, wenn sie ein zu starkes inneres Verwandlungsprodukt liefern, dann mussen wir ihnen etwas von außen entgegensetzen, das sie eindämmt, das die übermäßige innere Regsamkeit dämpft."
      ],
      [
        "Wie kann das geschehen?",
        "Wenn wir ein Organ des inneren Systems treffen wollen, das eine zu starke innere Regsamkeit entwickelt, so mussen wir in der Außenwelt dasjenige suchen, welches die entge­gengesetzte Regsamkeit hat, und dies dem Organismus zuführen, um dadurch die zu starke Regsamkeit des Organs bekämpfen zu können."
      ],
      [
        "Das heißt, wir müssen versuchen, jene äußeren Regsamkeiten aufzu­finden, welche den Regsamkeiten der einzelnen Organe entsprechen.",
        "Im Mittelalter haben die Menschen noch vieles davon gewußt, wie die Stoffe der Umwelt, also äußere Substanzen, der übertriebenen Regsamkeit der Organe entgegenwirken können."
      ],
      [
        "Für den heutigen Menschen, dem solche Dinge oft nur aus verballhornten Schriften des Mittelalters entgegentreten, in denen er nichts als bunten Aberglau­ben sehen kann, hört sich das ganz sonderbar an.",
        "Aber von der okkulten Wissenschaft ist das Entsprechen der Organe des inneren Weltsystems mit gewissen äußeren Substanzen durch Jahrtausende sorgfältig, tief und gründlich untersucht worden, und unzählige Beobachtungen, die mit dem hellsichtigen Auge gemacht worden sind, haben erwiesen, daß zum Beispiel dem übermäßig tätigen in­neren Jupiter, der Leber, Einhalt geboten werden kann durch die Metallsubstanz des Zinns."
      ],
      [
        "Die übermäßige innere Regsamkeit der Galle bekämpfen wir durch dasjenige, was in der Metallsubstanz des Eisens zum Ausdruck kommt.",
        "Das ist gar nicht zu verwundern, denn Eisen ist das einzige Metall, das wir in unserem Blut haben müssen als wesentlichen Bestandteil für das Werkzeug des Ich, und wir haben ja gesehen, daß in der Galle gerade dasjenige Organ vorliegt, welches vermittelt die Verbindung von dem Ich mit dem dichtesten Materiel­len, das dem Menschen eingelagert wird, dem Nahrungsstrom."
      ],
      [
        "Ebenso können wir sagen, daß die Milz ihre äußere Entsprechung hat in dem Metall Blei.",
        "Dem Herzen - Sonne - entspricht das Gold.",
        "Den Lungen - Merkur -, das sagt der Name selbst, entspricht das Queck­silber und den Nieren das Metall Kupfer, also die Venus. (Es wird an die Tafel geschrieben:)"
      ],
      [
        "Saturn Milz Blei"
      ],
      [
        "Jupiter Leber Zinn"
      ],
      [
        "Mars Galle Eisen"
      ],
      [
        "Sonne Herz Gold"
      ],
      [
        "Merkur Lungen Quecksilber"
      ],
      [
        "Venus Nieren Kupfer"
      ],
      [
        "Nun müssen wir, wenn wir mit den Regsamkeiten, die in diesen Metallen sich finden, die überhandnehmenden Regsamkeiten des inneren Organismus bekämpfen wollen, uns darüber klar sein, daß alles im Organismus mehr oder weniger zusammenhängt und daß ja die einzelnen Organsysteme parallel miteinander gebildet werden, daß also nicht etwa der Mensch zuerst als kopfloses Wesen entstan­den ist; sondern es bilden sich natürlich diejenigen Organe, welche in Zusammenhang stehen mit dem oberen Blutkreislauf, das Gehirn­Rückenmarksystem, gleichzeitig mit den Organen des inneren Welt-systems."
      ],
      [
        "Wie wir gesehen haben, daß es einen nach oben gehenden und einen nach unten gehenden Blutkreislauf gibt, so haben wir auch ein Hinaufwirken des Lymphprozesses, dem wir ein dumpfes Bewußt­sein zuerkannt haben, zu den oberen Partien des menschlichen Or­ganismus.",
        "Und es besteht nun die Tatsache, daß das, was dem Blutstrom oben eingegliedert ist, in gewisser Weise demjenigen ent­spricht, was dem unteren Blutstrom eingegliedert ist, und wir können sehen, daß die vorher genannten Metalle auch eine Verwandtschaft haben zu dem oberen Organsystem des Menschen.",
        "Sie wissen, daß die Lunge sich aufschließt nach außen zum Kehlkopf, der ein Organ des oberen menschlichen Organismus ist.",
        "Wie wir für die Galle im unteren Organsystem einen Zusammenhang zu sehen haben mit dem Eisen, so können wir das Eisen im oberen Organsystem in Verbin­dung bringen mit dem Kehlkopf.",
        "Diese Dinge sind natürlich schwierig,"
      ],
      [
        "aber ich möchte doch einiges davon andeuten.",
        "So wie wir einen Zusammenhang vermerkt haben zwischen Galle und Kehlkopf in bezug auf das Eisen, so gibt es auch in bezug auf das Zinn - Jupiter -eine gewisse Entsprechung zwischen den oberen Teiles unseres Kopfes mit allem, was als Vorderhaupt und als Gehirnbildung dazu­gehört, und der Leber; und in bezug auf das Blei - Saturn - eine Entsprechung zwischen Hinterhaupt und Milz."
      ],
      [
        "Auf diese Weise haben wir unsere Betrachtungen erstrecken kön­nen auf alles das, was dem menschlichen Blutkreislauf eingegliedert ist in den sieben Gliedern des inneren Weltsystems, und darauf, wie es in Zusammenhang steht mit der äußeren Welt.",
        "Für das normale wie für das abnorme Leben können wir diese Entsprechungen in Betracht ziehen.",
        "In diesen Entsprechungen der Metalle zu den inne­ren Organen haben wir eine höchst interessante Tatsache.",
        "Und wenn einmal nicht in chaotischer Weise, sondern systematisch dasjenige untersucht und zusammengestellt würde, was unsere therapeutischen Bücher an vielfachen Angaben enthalten, dann würden diese Ent­sprechungen sich schon ganz von selbst nachweisen lassen aus den äußeren Tatsachen.",
        "Und wenn heute solche Ausführungen noch als Phantasiegebilde betrachtet werden, so kann sich der Okkultist dazu ganz ruhig verhalten, denn er weiß, daß die Zeit kommen muß, wo die äußeren Tatsachen seine Behauptungen bestätigen werden."
      ],
      [
        "Nun dürfen wir nicht denken, daß wir zum Beispiel bei einer Nierenkrankheit ohne weiteres gewöhnliches Kupfer geben müßten; das wäre natürlich ein Fehler.",
        "Wenn wir dem Organismus metallische Substanzen zuführen wollen, so müssen wir sie erhitzen, so daß sie in eine Art Metalldampf übergehen.",
        "Dabei entwickelt sich etwas wie dampfförmige Körperchen, und in dieser Form kann die Metallität auf die inneren Organe wirken.",
        "Nehmen wir jetzt das Blutsystern, so wäre bei Erkrankungen mit Metallen nichts geholfen.",
        "Wir haben schon darauf hingewiesen, daß im Blutsystem eine Art Salzablage­rung vor sich geht.",
        "Und geradeso nun, wie auf die inneren Organe das Metallische wirkt, so wirkt auf das Blutsystem das Salzartige.",
        "Will man nun das Blutsystem durch äußere Mittel beeinflussen, so muß man ihm Salzartiges zuführen.",
        "Dies kann geschehen durch"
      ],
      [
        "Einatmen von salzhaltiger Luft, durch Salzbäder oder dergleichen.",
        "Wir können aber auch von der anderen Seite, durch den Verdauungs-prozeß, Salze oder Salzbildendes zuführen, so daß wir in der Lage sind, von zwei Seiten her den Prozeß der Salzbildung, der Salz­einlagerung hervorzurufen."
      ],
      [
        "Wenn Sie sich erinnern an das, was ich gestern ausgeführt habe über die physischen Wirkungen der inneren geistig-seelischen Pro­zesse, so werden Sie sich leicht denken können, daß alles dasjenige, was im Gegensatz zu den im Metallischen wirkenden Vorgängen steht, die physische Wirkung der Gefühlsprozesse ist, denn diese Gefühlsprozesse stehen in engstem Zusammenhang mit den Quel­lungsprozessen im Blut, die aber aufgehalten werden können durch Zuführung äußerer metallischer Stoffe, welche die entgegengesetzte Regsamkeit zeigen.",
        "Wenn zum Beispiel die Verdauungstätigkeit überhand nimmt und dort, wo der Ernährungsstrom vom Ätherleib ergriffen wird, eine eigene Regsamkeit entwickelt, so können wir dieser entgegenwirken durch geeignete Salzzuführung; denn, über­treibt der Ätherleib diesen Prozeß des Ergreifens des Ernährungs­stromes, so bedeutet das ein zu starkes Aufnehmen des Salzes.",
        "Er muß abgedämpft werden durch die Zufuhr der äußeren Regsamkeit eines Salzes."
      ],
      [
        "Dann haben wir Prozesse, welche sich äußerlich abspielen als Verbrennungs- oder Oxydationsprozesse; das sind solche Prozesse, wo sich etwas mit dem Sauerstoff der Luft verbindet.",
        "Alle diejenigen Stoffe, die sich leicht mit dem Sauerstoff der Luft verbinden, durch-strahlen, wenn sie in den Organismus aufgenommen werden, mit ihrer Regsamkeit den Organismus am weitesten.",
        "Während Salze, wenn wir sie dem Organismus zuführen, nur bis zu einem mäßigen Grade auf den Organismus wirken, kann die Metallität bis in das innere Weltsystem hinein wirken.",
        "Und in der Luft, also in den Stoffen, die sich leicht mit dem Sauerstoff der Luft verbinden, haben wir etwas, was, wenn es in den Körper aufgenommen wird, den ganzen Organismus durchstrahlt bis in das Blutsystem hinein.",
        "So werden wir es begreiflich finden können, daß wir durch solche Vor­gänge, die eine zu starke innere Regsamkeit in der Wärmeentwickelung"
      ],
      [
        "bilden, die ja der äußere Ausdruck der Willensimpulse ist, in unserem ganzen Organismus uns beeinflußt fühlen.",
        "Bei den organi­schen Rückwirkungen des Denkerischen ist das nicht so; wenn wir auf diese unser Augenmerk richten, fühlen wir, daß diese Wirkungen nur in gewissen Organen sich abspielen.",
        "Sie sehen daraus, wie außer­ordentlich kompliziert der ganze Apparat des menschlichen Organis­mus ist und wie kompliziert sein Verhältnis zur Außenwelt ist."
      ],
      [
        "So haben wir jetzt gezeigt, wie dem menschlichen Organismus mit seiner eigenen inneren Regsamkeit entgegengesetzt werden kann die äußere unorganische, unbelebte Natur, und wie durch Salze und durch verdampfte Metallität auf den Organismus eingewirkt werden kann.",
        "Aber wir haben auch die Möglichkeit, aus anderen Bereichen der Natur auf den Menschen einzuwirken."
      ],
      [
        "Wir können dem mensch­lichen Organismus ebenso das entgegensetzen, was die regsamen Kräfte in der Pflanzenwelt sind.",
        "Wenn wir ein pflanzliches Heilmittel einfach als Nahrung aufnehmen, so würden wir dadurch nicht viel erreichen, weil, wie wir gesehen haben, die inneren Organe dafür sorgen, daß den eingenommenen Stoffen ihre eigene Regsamkeit genommen wird."
      ],
      [
        "Soll also die Pflanze in den menschlichen Organis­mus so aufgenommen werden, daß sie auch in ihrer Eigenschaft als Pflanze weiterwirkt, so kann das nicht geschehen, wenn wir sie als Nahrung zu uns nehmen.",
        "Dieses Pflanzliche kann auf das Ich nicht einwirken, denn die Pflanze hat als höchstes Glied nur einen Äther­leib."
      ],
      [
        "Das Pflanzliche wird also einfach aufgenommen, da wo der Nahrungsstrom eingefangen wird vom Ätherleib, so daß das Pflanz-liche als Heilmittel noch nicht im Verdauungskanal in Betracht kom­men kann, sondern erst in jenen Organen, in die neben dem Äther-leib auch schon der astralische Leib des Menschen hineinwirkt.",
        "Aus diesem Grunde beginnt das Pflanzliche erst zu wirken auf das innere Weltsystem und auf das sympathische Nervensystem und das Lymphsystem."
      ],
      [
        "Nicht mehr erstreckt sich die Wirkung des Pflanzli­chen dahin, wo der Mensch durch das Blut sich wiederum aufschließt der äußeren Welt.",
        "Die Pflanze ist zugeordnet dem mittleren Teil des menschlichen Organismus, so daß alles, was in dem Pflanzlichen gesucht werden kann an Regsamkeit, nur wirken kann auf alles das,"
      ],
      [
        "was zu dem inneren Weltsystem gehört und auf die entsprechenden Organe des Kopfes und des oberen Teiles des Organismus.",
        "Wenn die Tätigkeiten, die Funktionen dieser Organe gestört sind, wenn sie in einer abnormen Weise wirken, dann kommt zur Bekämpfung die Einwirkung des Pflanzenhaften in Betracht."
      ],
      [
        "Wir haben also gesprochen über die Wirkungen von Metallen, Salzen und Pflanzen.",
        "Es ist nun nicht angezeigt, in unseren Betrach­tungen noch auf weitere Arten der Bekämpfung von Unregelmäßig­keiten oder Störungen im menschlichen Organismus einzugehen, nicht so sehr deshalb, weil die Zeit zu kurz ist, sondern in der Hauptsache, weil sich Theosophen am besten fernhalten von all den Gebieten, die heute in den Streit der Parteien hineingezogen werden.",
        "Das, was bis jetzt aufgezählt worden ist, gehört nicht dem Streit der Parteien an; man kann es einfach aufnehmen, und dann wird man schon die Richtigkeit einsehen; oder aber die Menschen halten es eben für reinen Unsinn, für Phantasterei.",
        "Das macht nichts.",
        "Denn da müßte man als Theosoph überhaupt schweigen, wenn man alle Dinge nicht sagen wollte, die von den Menschen als Unsinn angesehen werden.",
        "Wenn wir aber die Einwirkungen tierischer Substanzen auf den Menschen untersuchen wollten, so würden wir in den Streit der Parteien hineinkommen und man könnte dann meinen, Theosophie wolle sich einmischen in diesen Streit, der sich abspielt zwischen den Vorkämpfern und den Bekämpfern der Heilmethoden auf dem Gebiete des Tierischen.",
        "Und es kann niemals Aufgabe des Theoso­phen sein, sich in solche fanatischen Streitigkeiten zu mischen, denn dann würden wir Gefahr laufen, den objektiven allgemein-mensch­lichen Standpunkt zu verlassen."
      ],
      [
        "Das eine aber haben wir gesehen, wenn auch die Andeutungen alle nur skizzenhaft waren, daß dieser menschliche Organismus ein kom­pliziertes System ist von einzelnen Organen, die auf verschiedenen Stufen der Entwickelung stehen und die in der mannigfaltigsten Weise unter sich und mit dem Gesamtorganismus zusammenhängen.",
        "Was als physischer Organismus des Menschen sichtbar ist, was wir mit Augen sehen, mit Händen greifen können, ist nur ein Teil der menschlichen Organisation; das Übersinnliche aber, das da hineinwirkt,"
      ],
      [
        "das nehmen wir nicht in solcher Weise sinnlich wahr, das er­schließt sich erst dem geistigen Auge des Sehers.",
        "Wir dürfen also nicht sagen, daß alle Organe sich gleichmäßig ausgebildet haben, sondern es hat sich gezeigt, daß wir den menschlichen Organismus so anzusehen haben, daß darin Älteres und Jüngeres zu erkennen ist.",
        "Wir haben ja schon hervorgehoben, daß wir zum Beispiel das Gehirn als ein älteres, höher entwickeltes Organ anzusehen haben als das Rückenmark und daß das Gehirn früher gewissermaßen auf der Stufe des Rückenmarks gewesen ist.",
        "In analoger Weise können wir das Verdauungs- und das Blutsystem betrachten gegenüber dem Lymphsystem.",
        "Hier haben wir das Lymphsystem vergleichsweise auf die Stufe des Rückenmarks zu stellen, es ist also das jüngere, während das komplizierte Verdauungs-und das Blutsystem bereits in vielfacher Weise umgewandelt und älter sind als das Lymphsystem, das sich nicht nach außen aufschließt und seine Stoffproduktion nur nach innen in die Gewebe absondert.",
        "Das ist ein sehr wichtiger Gesichtspunkt.",
        "Wir haben also unser heutiges Lymphsystem anzusehen als etwas, das, wenn es nicht eingelagert wäre den anderen Systemen, bei fortschreitender Entwickelung zu einem Verdauungs- und Blutsystem würde."
      ],
      [
        "Ein einfacheres Vermittlungssystem des Bewußtseins haben wir im Lymphsystem; das, was komplizierter ist, haben wir im Verdauungs­Blutsystem.",
        "Wir haben also im menschlichen Organismus Organe zu suchen, welche aus Organsystemen hervorgegangen sind, die früher andere Aufgaben hatten.",
        "Die Mitteilungen, die hier darüber gemacht worden sind, würden auch für die äußere Wissenschaft sehr klar nachzuweisen sein, wenn man sich damit vertraut machen wollte.",
        "Alles, was über die Umwandlung der Organe gesagt worden ist, läßt sich nachweisen durch embryologische Untersuchungen.",
        "Bei einem jeglichen Lebewesen ist es so, daß dasjenige, was im Laufe der Entwickelung später erscheint, in der Keimanlage bereits vorgebildet ist.",
        "Wenn wir vom ausgebildeten Menschenorganismus bis zum befruchteten Keim zurückgehen, so könnten wir mit geeigneten Methoden die komplizierten Organsysteme in ihrer allerersten Anlage bereits angedeutet finden, und zwar so, daß sie selbst in der allerersten Anlage schon zeigen, wie sie eigentlich zueinander stehen."
      ],
      [
        "Wenn Sie sich einmal das anschauen, was wir als äußere Umhül­lung, als Begrenzung des Menschen vor uns haben in seiner Haut, und dann weiterhin das, was zu den ihr eingelagerten Sinnesorganen führt, so werden Sie sich sagen können, daß alles das, was da in dieser äußersten Begrenzung des Menschen vorhanden ist, schon umgewan­delt sein muß aus einem Anderen.",
        "Denn es ist schon ein sehr kompli­ziertes System, dem auch ein Gehirn angehört; und ein Gehirn ohne langwierige Vorbereitung sich zu denken ist unmöglich.",
        "Wir müssen uns also denken, daß die äußere Umhüllung des Menschen ein Umwandlungsprodukt ist, ähnlich wie wir ja das Gehirn als ein umgewandeltes Rückenmark bezeichnet haben und das Ernährungs­und Blutsystem als ein Umwandlungsprodukt des Lymphsystems.",
        "Während nun das Rückenmark und das Lymphsystem auf früheren Stufen eine aufsteigende Tendenz zeigten, müssen wir von dem heu­tigen Rückenmark- und Lymphsystern sagen, daß sie in absteigender Entwickelung begriffen sind.",
        "Man würde auch zeigen können, daß das Blut in seiner heutigen Konfiguration ein doppeltes Umwandlungs-produkt ist.",
        "Dadurch, daß sich das Verdauungs- und Blutsystem nach außen aufschließt, wird es zu einem umgewandelten Lymph­system.",
        "Wäre das Verdauungssystem mit seinen Bewegungen nur"
      ],
      [
        "# Bild s. 172"
      ],
      [
        "nach innen hin entwickelt, wäre es ganz nach innen abgeschlossen, hätten wir in ihm eine ähnliche Tätigkeit wie in der heutigen Lymph­tätigkeit.",
        "Bei ihr wird nur dasjenige aufgenommen, was über die Gewebe zugeführt wird."
      ],
      [
        "So ist auf der einen Seite in der äußeren Umgrenzung des Men­schen, im Hautsystem, ein Umgewandeltes zu sehen aus einem ande­ren System, dem Blutsystem, das ich hier so zeichnen will, und auch in dem Verdauungssystem haben wir die Umwandlung aus einem anderen System zu sehen, das heute in absteigender Entwickelung ist.",
        "Wir müssen nun festzustellen suchen, ob wir diese auf- und abstei­gende Natur von Organsystemen schon angedeutet finden in der Keimanlage.",
        "Und in der Tat zeigt sich, daß wir den Gesamtorganis­mus in der Keimanlage angedeutet finden - ich will es schematisch zeichnen - in den vier übereinanderliegenden Keimblättern, die man nennt: das äußere Keimblatt - Ektoderm -, das innere Keimblatt -Entoderm - und das Mesoderm - das äußere und das innere mittlere Keimblatt."
      ],
      [
        "# Bild s. 173"
      ],
      [
        "Dabei haben wir im Sinne unserer Anschauung über die Entwicke­lung das äußere Keimblatt, das Ektoderm, das man in der heutigen Anatomie auch das Hautsinnesblatt nennt, anzusehen als ein Umwandlungsprodukt, das seine erste Anlage zeigt in dem äußeren Mittelblatt, dem äußeren Mesoderm.",
        "In diesem haben wir dasjenige als Keimanlage vor uns, was auf einer höheren Stufe in dem Hautsin­nesblatt uns vor Augen tritt.",
        "Und in dem inneren Mittelblatt, dem inneren Mesoderm, haben wir die jüngere Bildung dessen vor uns, was sich später im Entoderm, im Darmdrüsenblatt, zeigt."
      ],
      [
        "Wenn wir den menschlichen Keim in seiner Entwickelung betrach­ten, so haben wir die erste Anlage des Menschen in den beiden mittleren Keimblättern angedeutet, in den Mesodermen; die beiden"
      ],
      [
        "anderen Keimblätter, Ektoderm und Entoderm, sind bereits umge­wandelt.",
        "Die beiden Mittelblätter sind also die, welche den ursprüng­lichen Zustand darstellen, während Ektoderm und Entoderm die höhere Entwickelung zeigen."
      ],
      [
        "Nun wissen wir, daß die entwickelungsfähige Keimanlage des Menschen zusammenfließt aus zwei Anlagen, aus der weiblichen und der männlichen Keimanlage, und daß eine Neuentwickelung nur entstehen kann durch das lebendige Zusammenwirken dieser beiden Anlagen.",
        "In den beiden Keimanlagen müssen also getrennt enthalten sein alle die Prozesse, die nur vereint die Keimanlage für den mensch­lichen Organismus bilden."
      ],
      [
        "Was zeigt uns nun der Okkultismus in bezug auf die hierbei obwaltenden Verhältnisse?",
        "Er zeigt uns, daß unter den heutigen physischen Bedingungen der weibliche Keim [Entoderm] nur im­stande ist, eine solche menschliche Körperanlage zu produzieren, die, wenn sie sich einzeln entwickeln wollte, nicht das entwickeln könnte, was wir das Formprinzip nennen, das zuletzt zur Einlage­rung des Knochensystems führt, das dem Menschen seine Festigkeit gibt; und auch das Hauptsinnessystem würde nicht durch den weib­lichen Keim geliefert werden können."
      ],
      [
        "Es ist der weibliche Keim so angelegt, daß man fast sagen könnte, das, was da entsteht, würde zu gut sein für die Welt, so wie sie heute besteht, denn es sind nicht alle Prozesse in der äußeren physischen Welt vorhanden, welche einem solchen Organismus notwendig wären.",
        "Dieser weibliche Menschen-Organismus könnte sozusagen nicht bis zu jener «Vererdigung» fort­schreiten, wie sie in dem eingelagerten Knochensystem zum Aus­druck kommt, und er hätte nicht die Möglichkeit, verbunden zu sein mit der Außenwelt durch die Sinne."
      ],
      [
        "Er müßte in den äußeren Bedin­gungen eine Stütze finden, um sein weicheres inneres Material, das er anstelle des festen Knochengerüstes hätte, auszugleichen; er könnte sich nicht nach außen aufschließen, sondern würde in seinem inneren Leben abgeschlossen bleiben.",
        "Das ist der weibliche Anteil an der Keimanlage; er würde über das Ziel dessen hinausschießen, was heute in unserem irdischen Dasein möglich ist, einfach weil in den heutigen physischen Erdenverhältnissen nicht die Bedingungen gegeben sind,"
      ],
      [
        "welche ein solcher verfeinerter Organismus nötig hätte, der so wenig zur Vererdigung und zum Aufschließen nach außen angelegt ist.",
        "Ein solcher Organismus wäre unter den heutigen irdischen Verhältnissen von vornherein zum Tode bestimmt.",
        "So ist wirklich der mensch­lichen Keimanlage, gerade durch die Tendenz, daß der Mensch in seiner Fortentwickelung zu weit kommen könnte, schon die Ursache dafür eingeprägt, daß der Mensch zum Tode bestimmt ist."
      ],
      [
        "Der andere Anteil der Keimanlage, der männliche [Ektoderm], ist in der genau umgekehrten Lage.",
        "Wenn die männliche Keimanlage allein sich entwickeln würde, so würde dies zu mächtiger Entfaltung dessen führen, was sich kundgibt in dem Sichaufschließen nach außen im Hautsinnessystem, und dessen, was zur Verfestigung im Knochen­system führt, also nach der anderen Seite über das Ziel hinausschie­ßen."
      ],
      [
        "Eine solche Einseitigkeit würde ebensowenig eine lebensfähige Keimanlage hervorbringen können wie der weibliche Keim für sich, denn der Organismus, den die männliche Keimanlage entwickeln würde, würde so starke Kräfte entfalten, daß er sich selbst zerstören und zugrunde gehen müßte unter den Verhältnissen, wie sie heute auf der Erde vorhanden sind, das heißt, er würde unter diesen heutigen Verhältnissen auf der Erde als Organismus nicht bestehen können.",
        "Der männliche Keim kann daher nur dann zu einem lebensfähigen Ausdruck kommen, wenn er mit der weiblichen Keimanlage zusam­menwirkt."
      ],
      [
        "Nur dadurch, daß die beiden Keirnanlagen sich ausglei­chen, daß dasjenige, was in der weiblichen Keimanlage zum Tode bestimmt ist, sich ausgleicht mit dem der männlichen Keimanlage durch den Befruchtungsprozeß, ist eine lebendige Gesamtanlage des Menschen möglich.",
        "Was an Kräften zusammengedrängt vorhanden ist in der männlichen Keimanlage, das würde, wenn es für sich allein auswachsen würde, unendlich unter das Irdische hinunterführen, es würde zu einer viel größeren Verhärtung des Knochensystems füh­ren, zu einem weit größeren Sichaufschließen und Aufgehen in der Außenwelt."
      ],
      [
        "Diese beiden organischen Keime müssen sich schon in ihrer allerersten Entstehung zu weiterer Entwickelung zusammenfin­den, denn einzeln ist jede von ihnen zum Tode bestimmt.",
        "Nur die lebendige Wechselwirkung dessen, was nach beiden Seiten hin das"
      ],
      [
        "Überhandnehmen des einen über das andere verhindert, ergibt die für das Erdendasein des Menschen mögliche Keimanlage."
      ],
      [
        "So sehen wir, wenn es auch nur in skizzenhafter Art gezeigt werden konnte, daß wir die geistigen Tatsachen bis dahin zurückver­folgen können, wo der Mensch seinesgleichen hervorbringt.",
        "Wir würden dies natürlich noch viel ausführlicher darstellen können, aber in einem kurzen Zyklus läßt sich natürlich nicht alles sagen.",
        "Wenn wir noch tiefer hineinleuchten würden, so würden wir sehen, wie sich bewahrheitet, daß auch das Minuziöseste auf geistige Tatsachen zurückgeht, bis hin zu dem, was hier über die übersinnlichen Kraft­systeme gesagt worden ist, die ihren äußeren Ausdruck finden in den Organsystemen, die der Mensch entwickelt, damit sein Geschlecht über die Erde hin lebt."
      ],
      [
        "Wir haben gesehen, daß die Erde als Ergebnis des dichtesten «Ver­erdigungsprozesses» in uns hervorgebracht hat das Knochensystem, und als das am wenigsten verdichtete, als das regsamste, das Blut­system.",
        "Und es soll nur noch kurz hinzugefügt werden, daß alles, was vorgeht im irdisch-physischen Menschenorganismus, hinauf-dringt bis zu den Vorgängen, die sich im Blute abspielen; das sind die Erwärmungsvorgänge.",
        "Wir haben in diesen Erwärmungsvorgängen des Blutes den unmittelbaren Ausdruck des Ich und damit das ober­ste Niveau zu sehen, und darunter sich abspielend die anderen Pro­zesse des menschlichen Organismus.",
        "Der Erwärmungsprozeß ist also das Höchste, in diesen greift unsere Ich-Seelentätigkeit unmittelbar ein.",
        "Deshalb fühlen wir auch etwas wie eine Verwandlung unserer Ich-Seelentätigkeit in ein inneres Warmwerden, das bis zum physi­schen Warmwerden im Blutprozeß gehen kann.",
        "Wir sehen also, wie das Geistig-Seelische von oben nach unten gehend durch den Erwär­mungsprozeß eingreift in das Organische, das Physiologische, und wir könnten noch an vielen anderen Tatsachen zeigen, wie das Gei­stig-Seelische sich in Erwärmungsprozessen berührt mit dem Orga­nischen.",
        "Erwärmungsprozesse haben wir auch durch die Vorgänge in den Ernährungsorganen.",
        "Durch die Tätigkeit der komplizierten Apparate des Ernährungssystems finden die mannigfaltigsten Ver­wandlungen statt, durch die es im physischen Organismus zu Erwärmungsprozessen"
      ],
      [
        "kommt.",
        "Diese erstrecken sich von unten nach oben.",
        "Es reicht also im Erwärmungsprozeß der physische Organismus des Menschen bis hinauf ins Geistig-Seelische.",
        "Hören damit die Umwandlungen auf?",
        "Oder gehen sie weiter?",
        "Was dann folgt, kann nur angedeutet werden; es muß zunächst dem weiteren Nachdenken und namentlich Nachfühlen eines jeden Zuhörers überlassen werden.",
        "Wenn wir diese Umwandlungen mit Gefühlen wirklicher Ehrfurcht für den menschlichen Organismus betrachten können, so lernen wir einsehen, daß Physiologie nicht eine trockene Wissenschaft zu sein braucht, sondern eine Quelle höchster menschlicher Erkenntnis sein kann."
      ],
      [
        "Was der Organismus produziert an innerer Wärme in unserem Blut, an Wärme, die er uns durch die gesamten inneren Prozesse zuleitet, das zeigt, daß wir in den Erwärmungsvorgängen etwas zu sehen haben wie eine Blüte aller anderen Prozesse im Organismus.",
        "Die innere Wärme des Organismus dringt bis hinauf in das Geistig-Seelische und kann sich bis in Geistig-Seelisches hinein verwandeln."
      ],
      [
        "Das ist das Höchste, das Schönste, das durch die Kraft des Men­schenleibes Physisches umgewandelt werden kann in Geistig-Seeli­sches.",
        "Wenn alles, was im menschlichen irdischen Organismus veran­lagt ist, zu Wärme geworden ist und die Wärme vom Menschen in der rechten Weise umgewandelt wird, dann entsteht aus der inneren Wärme Mitgefühl und Interesse für andere Wesen."
      ],
      [
        "Wenn wir durch alle Prozesse des menschlichen Organismus hindurch aufsteigen bis zum obersten Niveau, den Erwärmungsprozessen, so schreiten wir gleichsam durch das Tor des menschlichen Organismus, das gebildet wird durch die Wärmeprozesse, hinauf bis dahin, wo die Wärme des Blutes verwertet wird durch das, was die Seele daraus macht.",
        "Durch lebendiges Interesse für alle Wesen, durch Mitgefühl für alles, was um uns herum ist, erweitern wir, indem unser physisches Leben uns bis zur Wärme hinaufführt, unser Geistig-Seelisches über das ge­samte irdische Dasein, und wir machen uns eins mit dem gesamten Dasein."
      ],
      [
        "Es ist eine wunderbare Tatsache, daß die Weltwesenheit den Umweg gemacht hat durch unseren physischen Organismus, um uns zuletzt die innere Wärme zu geben, die wir Menschen in der Erdenmission"
      ],
      [
        "berufen sind umzuwandeln durch unser Ich in lebendiges Mitfühlen mit allen Wesen."
      ],
      [
        "Wärme wird in Mitgefühl umgewandelt in der Erdenmission!"
      ],
      [
        "Die Tätigkeit des menschlichen Organismus benützen wir sozusa­gen als Heizwärme für den Geist.",
        "Das ist der Sinn der Erdenmission, daß der Mensch als physischer Organismus dem Erdenorganismus so eingelagert ist, daß alle physischen Prozesse zuletzt ihre Vollendung, ihre Krone in der Blutwärme finden, und daß der Mensch als Mikro­kosmos in Erfüllung seiner Bestimmung diese innere Wärme wie­derum umwandelt, um sie auszuströrnen als lebendiges Mitgefühl und Liebe für alles, was uns umgibt."
      ],
      [
        "Durch alles, was wir aus leben­digem Interesse in unsere Seele aufnehmen, wird unser Seelenleben erweitert.",
        "Und wenn wir dann durch viele Inkarnationen gegangen sind, in denen wir alle Wärme, die uns gegeben worden ist, verwertet haben, dann wird die Erde ihr Ziel, das innerhalb der Erdenmission zu erfüllen war, erreicht haben, dann wird sie als Erdenleichnam hinuntersinken und dem Verfall überliefert sein."
      ],
      [
        "Und aufsteigen wird die Gesamtheit aller jener Menschenseelen, die die physische Wärme umgewandelt haben in Herzenswärme.",
        "Wie die einzelne Seele, wenn der Mensch durch die Pforte des Todes gegangen ist, aufsteigt zu einer geistigen Welt, nachdem der physische Leichnam den Erden-kräften übergeben wurde, so wird einstmals der Erdenleichnam den Weltenkräften übergeben werden, und die einzelnen Menschenseelen werden zu neuen Daseinsstufen fortschreiten."
      ],
      [
        "Nichts in der Welt geht verloren.",
        "Was die Menschenseelen als Früchte auf der Erde errungen haben, das wird durch die Menschenseelen in Ewigkeiten hinübergetragen."
      ],
      [
        "So gestattet uns die Geisteswissenschaft, auch die physiologischen Prozesse im menschlichen Organismus anzuknüpfen an unsere Ewigkeitsbestimmung.",
        "Wenn uns die Geisteswissenschaft (Theoso­phie) nicht bloße Theorie, nicht bloß abstrakte Erkenntnis ist, son­dern wenn wir sie so betrachten, daß sie uns zeigt: wir stehen als Menschen nicht nur auf der Erde, sondern wir gehören zum gesam­ten Weltensystem -, und wenn wir lernen, so über die Bestimmung des Menschen zu denken, daß er die Kräfte von der Erde nimmt, um"
      ],
      [
        "in die Ewigkeit hineinzuwirken, dann nehmen wir durch Geisteswis­senschaft (Theosophie) das auf, was durch sie errungen werden muß.",
        "Und wenn die Menschen, die dieses hohe Ideal ahnen oder erkennen, sich brüderlich zusammenfinden und übereinstimmen in ihrem Stre­ben, das heißt, wenn wir erkennen, daß in uns selbst die Keime zur Weiterentwickelung enthalten sind, die fruchtbar werden können für die weitere Erden- und Menschheitsentwickelung, dann können wir in aller Bescheidenheit das Gefühl haben, daß wir als Tbeosophen (Anthroposophen) durch die Entwickelung unserer eigenen Kräfte mitwirken können an der Erfüllung der Erdenmission."
      ],
      [
        "Wir sind hier zusammengekommen und werden nun wieder hin­ausgehen, um draußen zu leben und vielleicht manches von dem, was ja nur skizzenhaft hier als Anregung hat gegeben werden können, mit hinaus zu nehmen und weiter zur Entfaltung zu bringen.",
        "Aber auch wenn wir in der Welt zerstreut sind, so wollen wir in lebendigen Gedanken und Empfindungen und mit unserem ganzen Wollen mit­einander harmonisch zusammenwirken.",
        "In diesem Geiste wollen wir voneinander scheiden, in diesem Geiste wollen wir uns auch wieder­finden, wenn dazu Gelegenheit sein wird."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "SONDERVORTRAG Prag, 28. März 1911",
    "paragraphs": [
      "Im Anschluß an die öffentlichen Vorträge «Wie widerlegt man Theosophie?» und «Wie verteidigt man Theosophie?» sowie im Anschluß an die Betrachtungen, die ich in diesen Tagen in dem Vortragszyklus über «Okkulte Physiologie» gegeben habe, können sich eine Reihe von Fragen aufdrängen, und es liegt das Bedürfnis vor, über diese Fragen, die hier berührt worden sind, sich mit den verehrten Zuhö­rern ein wenig zu verständigen. Die beiden öffentlichen Vorträge hatten vor allen Dingen das Ziel, zu zeigen, wie man auf dem Boden der Geisteswissenschaft oder Theosophie sich sehr wohl bewußt sein muß der möglichen Einwände, die sich ergeben können, und wie der Okkultist das Berechtigte dieser Einwände durchaus anerkennt, und andererseits konnte Ihnen aus den Vorträgen hervorgehen eine ganz bestimmte, scharf nuancierte Stellungnahme, wie die theosophischen Wahrheiten gegenüber den gewichtigen Einwänden der Gegner zu vertreten sind.",
      "Gerade aus der Erkenntnis der gekennzeichneten Schwierigkeiten, die sich für die Theosophie ergeben, sollte sich aber bei jedem Theo­sophen das Bedürfnis bilden, daß in der Vertretung der theosophi­schen Wahrheiten möglichste Genauigkeit, höchste Präzision walten möge. Das ist etwas, dessen sich derjenige, der aus der Erkenntnis der entsprechenden Zusammenhänge heraus diese Dinge zu vertreten hat, sehr wohl bewußt ist, womit er aber - trotz alle dem, was in den öffentlichen Vorträgen hervorgehoben worden ist - unvermeidlich in Kollision mit denjenigen kommt, die auf dem Boden der heutigen Wissenschaft stehen. Deshalb erfordert Theosophie, so sonderbar das",
      "scheinen mag, auf der einen Seite zum Einkleiden der aus den höhe­ren Welten heruntergeholten Wahrheiten, auf der anderen Seite nicht minder aus der bloßen gewöhnlichen Vernünftigkeit heraus das genaueste, präziseste logische Formulieren. Und wer sich diese Auf­gabe setzt, präzis und genau logisch zu formulieren, und zu diesem Zwecke alles vermeidet, was etwa Wortfüllsel in einem Satze oder nur rhetorische Verbrämung wäre, der fühlt sehr häufig, wie leicht er mißverstanden werden kann, einfach aus dem Grunde, weil in unse­rer Zeit nicht überall das intensive Bedürfnis vorhanden ist, die vertretenen Wahrheiten ebenso genau und präzis, wie sie ausgespro­chen werden, auch hinzunehmen. Es ist in unserer Zeit die Mensch­heit, selbst da, wo sie sich wissenschaftlich betätigt, noch gar nicht gewöhnt an dieses Ganz-genau-Nehmen. Wenn man das Vorgetra­gene ganz genau nimmt, so darf man in den Sätzen nicht nur nichts ändern, sondern man muß auch genau auf die Grenze achten, die in die Formulierungen mit aufgenommen ist.",
      "Wir haben hierfür ein leichtes Beispiel, das bei dem Fragenstellen kürzlich aufgetaucht ist. Es wurde gefragt: Wenn das Traumbe­wußtsein nur eine Art Bilderbewußtsein ist, wie kommt es denn dann, daß aus diesem Traumbewußtsein heraus gewisse unterbe-wußte Handlungen, wie zum Beispiel Nachtwandeln, vollzogen wer­den können? - Da hat der Fragesteller nicht beachtet, wie ich auch damals schon erwähnt habe, daß mit dem Satze, es seien die Inhalte des Traumbewußtseins etwas Bildhaftes, nicht gemeint ist, sie seien nur Bildhaftes, sondern daß selbstverständlich, da nur von einer Seite her der Horizont des Traumbewußtseins charakterisiert worden ist, gerade aus der Natur dieser Charakteristik sich ergab: Wie unsere Tageshandlungen folgen aus unserem Tagesbewußtsein, so könnten gewisse Handlungen weniger bewußter Natur auch folgen aus dem Bilderbewußtsein des Traumes.",
      "Es soll durchaus ohne Anklage gesagt werden, daß das ungenaue Zuhören einer der hauptsächlichsten Gründe ist, warum der Theoso­phie und ihrer Vertretung heute so viele Mißverständnisse entgegen­gebracht werden. Es werden solche Mißverständnisse nicht etwa bloß von den Gegnern der Theosophie entgegengebracht, sondern in",
      "einem hohen Maße auch von denjenigen, die Bekenner dieser theoso­phischen Weltanschauung sind. Und vielleicht liegt ein großer Teil der Schuld an den Mißverständnissen, welche die Außenwelt der Geisteswissenschaft entgegenbringt, daran, daß gerade auch inner­halb der theosophischen Kreise nach der gekennzeichneten Richtung hin so viel gesündigt wird.",
      "Wenn wir nun unter den Wissenschaften, welche in unserer Zeit Geltung haben, Umschau halten, so könnte vielleicht die allgemeine Empfindung dahin gehen, daß die Theosophie am meisten Beziehun­gen hätte, am meisten verwandt wäre mit der Philosophie mit ihren verschiedenen Zweigen. Eine solche Behauptung wäre auch durchaus richtig, und man könnte eigentlich aus der Natur der Sachlage heraus voraussetzen, daß die nächste Möglichkeit, den theosophischen Erkenntnissen Verständnis entgegenzubringen, auf der Seite der Phi­losophie vorliegen würde. Aber gerade da zeigen sich wieder andere Schwierigkeiten.",
      "Philosophie, wie sie heute, man darf sagen, allüberall gepflegt wird, ist in einem viel höheren Maße eine Art Spezialwissenschaft gewor­den, als sie vor verhältnismäßig noch kurzer Zeit war. Sie ist eine Spezialwissenschaft geworden und arbeitet, wenn wir ihre praktische Arbeit heute ansehen und uns nicht auf einzelne Theorien einlassen, praktisch im wesentlichen in abstrakten Regionen. Und es ist nicht viel Neigung vorhanden, die Philosophie zu der konkreten Auffas­sung des Tatsächlichen herunterzuführen. Ja, es ergeben sich sogar Schwierigkeiten in dem heutigen Betriebe der Philosophie, wenn man mit diesem philosophischen Streben von heute die Welt des Tatsäch­lichen umfassen will. Die nach den verschiedensten Richtungen hin mit großem Scharfsinn in der zweiten Hälfte des 19. Jahrhunderts und bis in unsere Tage hinein ausgeführte Erkenntnistheorie ist ja so, wie wir sie heute haben, hauptsächlich aus dem Grunde entstan­den, weil diese Schwierigkeiten, aus den abstrakten Höhen des Den­kens, des Begriffes herab an die Tatsachen heranzudringen, gefühlt wurden.",
      "Nun fühlt man, daß gerade bei solchen Vorträgen, wie es diejeni­gen dieses Zyklus über «Okkulte Physiologie» sind, Theosophie",
      "uberall genötigt ist, mit dem, was sie als übersinnliche Bewußtseins-inhalte zu geben hat, unmittelbar heranzudringen an unsere tatsächli­che Welt. Wenn ich trivial reden darf, möchte ich sagen: Theosophie hat es nicht so gut wie die heutige Philosophie, welche sich in abstrakten Regionen hält und welche durchaus nicht sehr geneigt sein würde, in ihre Betrachtungen solche Begriffe wie, sagen wir, zum Beispiel des Blutes oder der Leber oder der Milz, also Inhalte des Tatsächlichen aufzunehmen. Es würde diese Philosophie sehr davon zurückschrecken, die Brücke von ihren abstrakten Begriffsbildungen zu schlagen nach den konkreten, unmittelbar tatsächlich an uns her­antretenden Ereignissen und Dingen. Die Theosophie ist in dieser Beziehung waghalsiger und kann gerade deshalb gegenüber der Phi­losophie sehr leicht angesehen werden als eine Geistesbetätigung, die kühn und unberechtigt eine Brücke schlägt von dem Geistigsten bis zu dem Allertatsächlichsten herunter.",
      "Nun muß es doch eigentlich interessant sein, sich einmal zu fragen:",
      "Woher kommt es denn, daß es Philosophen so schwer ist, an die Theosophie heranzukommen? - Vielleicht gerade aus diesem Grunde, weil die Philosophie es vermeidet, diese Brücke zu schlagen. Für die Theosophie selber ist diese Tatsache in gewissem Sinne eine Fatalität, ist außerordentlich fatal. Denn man stößt mit den theoso­phischen Erkenntnissen, insbesondere dann, wenn man sie herunter-führen will bis zur logischen Durcharbeitung, sehr, sehr häufig auf Widerstände. Gerade auf philosophischer Seite stößt man in dieser Beziehung auf Widerstände. Und zwar ist es sogar sehr oft vorge­kommen, daß man weniger auf Widerstände stößt, wenn man sozu­sagen lustig darauflos den Menschen sensationelle Beobachtungen aus den höhere Welten erzählt. Das verzeihen sie oftmals verhältnis­mäßig leicht, denn erstens sind diese Dinge «interessant», und zwei­tens sagen sich die Menschen: Nun, insofern wir nicht in diese Welten hinaufschauen können, sind wir gar nicht dazu aufgerufen, irgendein Urteil darüber zu fällen.",
      "Nun ist es aber das Bestreben der Theosophie, alles, was in den höheren Welten gefunden werden kann, zum vernünftigen Begreifen herunterzuführen. Gefunden sind die Tatsachen, wenn sie wirklich",
      "als solche gelten können, durch übersinnliches Forschen in den über­sinnlichen Welten. Die Form der Darstellung sollte aber in unserer Gegenwart so gegeben werden, daß alles in streng logische Formen gekleidet wird und daß an all den Stellen, wo es heute schon möglich ist, darauf hingewiesen wird, wie die allertatsächlichsten äußeren Vorgänge uns schon überall Bestätigungen für das ergeben können, was wir aus der geistigen Forschung heraus behaupten können. In diesem ganzen Vorgange, die Erkenntnisse der geistigen Welt herun­terzuholen, sie einzukleiden in logische oder sonstige Vernunftfor­men und sie so darzubieten in einer Gestalt, welche dem logischen Bedürfnisse unserer Zeit entgegenkommt, besteht nun heute eine, man darf sagen, wirklich außerordentlich begreifliche Quelle zahl-reichster Mißverständnisse.",
      "Nehmen Sie einmal das Komplizierte, was in diesen Vorträgen über «Okkulte Physiologie» gesagt worden ist, das in seinen Bestim­mungen überall nur mit Einschränkungen, mit genauen Angaben der Grenzen Hinzunehmende, nehmen Sie das ganz Komplizierte der in sich ungeheuer beweglichen und variablen Welt des Geistigen, und vergleichen Sie diese Welt des geistigen in ihrer ganzen Variabilität, in der Schwierigkeit, etwas uns aus geistigen Welten Herunterkommen­des mit groben Begriffskonturen zu umspannen, vergleichen Sie es mit der Leichtigkeit, irgendeine äußere Tatsache durch ein Experi­ment oder durch sinnliche Beobachtung zu charakterisieren und in einem logischen Stil zu beschreiben!",
      "Nun besteht aber heute überall in unserer Philosophie die Ten­denz, wo Begriffe erläutert und beschrieben werden, auf gar nichts anderes Rücksicht zu nehmen als auf solche Vorstellungen, die aus der Welt gewonnen werden, die als die sinnliche Welt vor uns liegt. Das wird in der Philosophie besonders dann fühlbar, wenn sie genö­tigt ist, zum Beispiel auf ethischem Gebiete einen anderen Ursprung für die Grundbegriffe zu finden als solche Vorstellungen, die an der äußeren Wahrnehmung der physischen Welt gewonnen werden. Wir finden - und das wäre unschwer nachzuweisen, aber natürlich nur durch ausführliche Darlegungen aus der zeitgenössischen philo­sophischen Literatur -, daß bei allem, was heute in der Philosophie",
      "verarbeitet wird, die Begriffsbestimmungen so grob sind, weil für begriffliche Bewußtseinsinhalte im Grunde genommen nur Rücksicht genoinmen wird auf die Wahrnehmungswelt, die um uns herum existiert und nur aufgrund derselben die Begriffe gebildet werden.",
      "Gibt es eigentlich einen Anhaltspunkt dafür, daß in der Philoso­phie bei der Entstehung der allerelementarsten Begriffe Bewußtseins-inhalte auch von anderer Seite gewonnen werden als von der Seite der sinnlich wahrnehmbaren Welt? - Kurz gesagt: es fehlt der zeitge­nössischen Philosophie die Möglichkeit, zu einem Verständnis der Theosophie zu kommen, weil sie mit ihren Theorien nicht anknüpfen kann an solche Begriffe, wie wir sie in unseren theosophischen Aus­einandersetzungen pflegen. Wir haben in der philosophischen Litera­tur den Bewußtseinshorizont dadurch bestimmt, daß bei dem Bilden von Begriffen überall nur Rücksicht genommen wird auf die äußere Wahrnehmungswelt und nicht auf solche Inhalte, die von anderer Seite als von der der sinnlichen Wahrnehmungen herrühren.",
      "Die Theosophie nun muß ihre Begriffe auf eine ganz andere Weise gewinnen; sie muß zu übersinnlicher Erkenntnis aufsteigen und ihre Begriffe aus dem Übesinnlichen herunterholen, sie muß aber auch in die Seite der Realität sich hineinvertiefen und muß die aus der Beob­achtung der sinnlichen Welt gewonnenen philosophischen Begriffe beherrschen. Wenn wir uns das einmal schematisch vorstellen wol­len, so haben wir auf der einen Seite in der Philosophie Begriffe, die durch äußere Wahrnehmung gewonnen werden, auf der anderen Seite die Begriffe, die aus dem Übersinnlichen durch geistige Wahr­nehmung gewonnen werden. Und wenn wir das Feld der Begriffe uns denken, durch die wir uns verständigen, so müssen wir sagen: Wenn Theosophie als etwas Berechtigtes gelten soll, dann müssen unsere Begriffe von beiden Seiten her genommen werden, auf der einen Seite von der sinnlichen Wahrnehmung, auf der anderen Seite von der geistigen Wahrnehmung, und auf dem Felde unserer Begriffe müssen diese beiden Seiten sich treffen.",
      "# Bild s. 187",
      "Es muß das Bedürfnis bestehen, gerade in theosophischen Darstel­lungen mit den aus der geistigen Welt heruntergeholten Begriffen sich mit den philosophischen Begriffen zu treffen, das heißt, daß mit un­seren Begriffen überall angeschlossen werden kann an die Begriffe, die aus der äußeren sinnlichen Wahrnehmungswelt gewonnen werden.",
      "Unsere heutigen Erkenntnistheorien sind mehr oder weniger fast ausschließlich von dem Gesichtspunkt aus aufgebaut, daß die Begriffe nur von einer Seite her genommen werden. Ich will damit nicht sagen, daß es nicht auch Erkenntnistheorien gibt, wo etwas Übersinnliches als Ursprung der Begriffe zugelassen ist. Aber über­all, wo etwas positiv bewiesen werden soll, sind die Beispiele dadurch charakterisiert, daß die Begriffe nur von der linken Seite (Schema) genommen sind, also von der Seite, auf der die Begriffe an der sinnlich-physischen Wahrnehmungswelt gewonnen werden. Das ist auch ganz natürlich, weil [in der Philosophie] geistige Tatsachen als solche nicht anerkannt werden. Man berücksichtigt eben nicht den Fall, daß geistige Tatsachen, die aus den geistigen Welten herunterge­holt werden, ebenso in Begriffe gebracht werden können, wie die Tatsachen der physischen Welt in Begriffe gebracht werden. Dieser Umstand hat dazu geführt, daß die Theosophie, wenn sie sich mit der Philosophie verständigen will, auf der Seite der Philosophie fast gar keinen vorbereiteten Boden findet und daß in der Philosophie die Art und Weise, wie in der Theosophie die Begriffe gebraucht werden, nicht leicht verstanden werden kann.",
      "Man möchte sagen: Steht man der äußeren sinnlichen Wahrneh­mungswelt gegenüber, so hat man es leicht, den Begriffen scharfe Konturen zu geben. Da haben die Dinge selbst scharfe Konturen, scharfe Grenzen, da ist man leicht imstande, auch den Begriffen",
      "scharfe Konturen zu geben. Steht man dagegen der in sich bewegli­chen und variablen geistigen Welt gegenüber, so muß oft vieles erst zusammengetragen und in den Begriffen Einschränkungen oder Erweiterungen gemacht werden, um einigermaßen charakterisieren zu können, was eigentlich gesagt werden soll. Die Erkenntnistheorie, wie sie heute getrieben wird, ist am allerwenigsten geeignet, sich auf solche Begriffe einzulassen, wie sie in der Theosophie verwendet werden. Denn indem man, um die Begriffe zu bestimmen, die Gründe für die Begriffsbestimmungen - bewußt oder unbewußt -nur von einer Seite nimmt, mischt sich in alle Begriffe, die man bildet, ohne daß man es recht weiß, etwas hinein, was zu solchen erkennt­nistheoretischen Begriffen führt, die überhaupt nicht zu brauchen sind, um in der Theosophie irgend etwas zu erläutern oder zu erklä­ren. Der Begriff, wie er von der sozusagen nichttheosophischen Welt geliefert wird, ist einfach ungeeignet als Instrument zum Charakteri­sieren dessen, was durch die Theosophie aus der geistigen Welt heruntergeholt wird.",
      "Nun gibt es insbesondere einen solchen Begriff, der auf dem Gebiet der Erkenntnistheorie ein furchtbarer Störenfried ist. Ich weiß sehr wohl, daß er gar nicht als solcher empfunden wird, aber er ist ein Störenfried. Das ist, wenn man von allen feineren Nuancierun­gen absieht, die in so scharfsinniger Weise im Verlaufe des 19. Jahr­hunderts sich herausgebildet haben, der Punkt, wo das erkenntnis­theoretische Problem so formuliert wird, daß man sagt: Wie kommt eigentlich das Ich mit seinem Bewußtseinsinhalt - oder wenn man meinetwillen es vermeiden will, vom Ich zu sprechen -, wie kommt unser Bewußtseinsinhalt dazu, von uns auf eine Realität bezogen zu werden? - Diese Gedankengänge haben mehr oder weniger - mit Ausnahme von gewissen erkenntnistheoretischen Richtungen im 19. Jahrhundert - zu einer Erkenntnistheorie geführt, welche immer wieder und wieder als eine große Schwierigkeit empfindet, die Mög­lichkeit zu sehen, wie das Transsubjektive oder Transzendente, also das, was außerhalb unseres Bewußtseins liegt, in unser Bewußtsein eintreten kann. Ich will zugeben, daß damit das Erkenntnisproblem nur grob charakterisiert ist. Aber es sind doch die Schwierigkeiten im",
      "wesentlichen damit charakterisiert, daß man sagt: Wie kann über­haupt das, was subjektiver Bewußtseinsinhalt ist, irgendwie heran an das Sein, an die Realität? Wie kann es bezogen werden auf die Realität? Denn wir mussen uns klar sein, daß, selbst wenn wir eine außerhalb unseres Bewußtseins liegende transsubjektive Realität vor­aussetzen, dasjenige, was in unserem Bewußtsein drinnen ist, nicht unmittelbar an diese Realität herantreten kann. Wir haben also - so heißt es - in uns den Bewußtseinsinhalt, und wir können uns fragen:",
      "Wie haben wir die Möglichkeit, aus diesem Bewußtseinsinhalt heraus in das Sein, in die Realität, die unabhängig ist von unserem Bewußt­sein, hineinzudringen? -Ein bedeutender Erkenntnistheoretiker der Gegenwart hat dieses",
      "Problem mit einem prägnanten Ausdruck charakterisiert: Das menschliche Ich, insofern es den Bewußtseinshorizont umfaßt, könne sich nicht selber überspringen, denn es müßte aus sich heraus­springen, wenn es in die Realität hineinspringen würde. Dann wäre es aber in der Realität und nicht im Bewußtsein. - Es scheint also für diesen Erkenntnistheoretiker klar zu sein, daß überhaupt nichts dar­über ausgemacht werden kann, wie der Bewußtseinsinhalt zur wirk­lichen Realität steht.",
      "Es ist mir vor vielen Jahren in meinen erkenntnistheoretischen Schriften darum zu tun gewesen, zunächst einmal dieses Erkenntnis-problem festzustellen - das ja auch in der Theosophie grundlegend ist - und dann die Schwierigkeiten, die sich aus einer solchen wie der eben bezeichneten Formulierung ergeben, wegzuschaffen. Dabei konnte einem allerdings sehr Merkwürdiges passieren. So zum Bei­spiel gab es in der Zeit, in welcher sich das zugetragen hat, wovon ich sprechen will, Philosophen, die von vornherein davon ausgingen -ganz ähnlich wie Schopenhauer - zu sagen: «Die Welt ist meine Vorstellung.» Das heißt, das, was im Bewußtsein gegeben ist, das ist zunächst nur Vorstellungsinhalt, und nun handelt es sich um die Frage, wie eine Brücke zu schlagen ist von der Vorstellung zu dem, was außerhalb des Vorgestellten ist, zu der transsubjektiven Realität. Nun ist eigentlich für jeden, welcher sich nicht faszinieren läßt durch Feststellungen, die angeblich auf diesem Felde gemacht worden sind,",
      "sondern der unbefangen an die Sache herantritt, eine Frage sogleich gegeben, und einer großen Menge der erkenntnistheoretischen Lite­ratur gegenüber, namentlich der, welche in den siebziger und in der ersten Hälfte der achtziger Jahre geschrieben worden ist, muß man diese Frage aufwerfen: Wenn irgend etwas «meine Vorstellung» ist, und wenn dieses Vorgestellte selbst mehr sein soll als etwas innerhalb des Bewußtseinsinhaltes Liegendes, wenn es Geltung für sich selbst haben soll, dann ist damit etwas gesagt, was im Grunde genommen nicht vor dem Ausgangspunkt der Erkenntnistheorie liegen darf, sondern etwas, was erst festgestellt werden kann, nachdem diese viel wichtigeren erkenntnistheoretischen Grundfragen erörtert worden sind. Denn wir mussen uns zuerst fragen: Warum dürfen wir über­haupt etwas, was in uns als Bewußtseinsinhalt auftritt, «meine Vor­stellung» nennen? Haben wir ein Recht zu sagen: Was auf meinem Bewußtseinshorizont auftritt, ist meine Vorstellung? - Die Erkennt­nistheorie hat durchaus nicht das Recht, auszugehen von dem Urteil, das Gegebene sei meine Vorstellung, sondern sie hat die Pflicht, wenn sie wirklich auf ihre ersten Anfänge zurückgeht, erst zu recht­fertigen, daß das, was da auftritt, der subjektive Bewußtseinsinhalt ist.",
      "Es gibt selbstverständlich mehrere hundert Einwände gegenüber dem, was jetzt gesagt worden ist, aber ich glaube nicht, daß es möglich ist, einen einzigen dieser Einwände lange festzuhalten, wenn man unbefangen auf die Sache eingeht. Aber ich habe erlebt, daß ein bekannter und bedeutender Philosoph mir eine ganz eigentümliche Antwort gab, als ich ihn auf dieses Dilemma aufmerksam machte und ihm auseinandersetzen wollte, daß es doch zuerst geprüft werden müsse, ob es erkenntnistheoretisch gerechtfertigt sei, die Vorstellung als etwas Nicht-Reales zu charakterisieren. Da sagte er: Das ist doch selbstverständlich, das liegt doch schon in der Definition des Wortes «Vorstellung», daß wir etwas vor uns stellen, was nicht real ist. - Er konnte gar nicht begreifen - so sehr waren ihm diese Vorstellungen eingewurzelt, welche im Laufe von Jahrhunderten gewachsen sind -, daß man mit dieser ersten Definition etwas noch vollständig Unbe­gründetes hinstellt.",
      "Wenn wir überhaupt innerhalb des Umfanges der Welt, in der wir drinnenstehen - wobei ich Sie bitte, die Worte «die Welt, in der wir drinnenstehen» zu verstehen als die Welt, wie wir sie im Alltag ha­ben -, wenn wir überhaupt innerhalb dieser Welt irgendeine Feststel­lung machen wollen, zum Beispiel daß dasjenige, was da als Welt gegeben ist, eine «Vorstellung» sei, so müssen wir uns klar sein, daß es ja gar nicht möglich ist, eine solche Feststellung zu machen, ohne dasjenige, was wir unsere denkerische Tätigkeit nennen, ohne Ge­danken und Begriffe. Ich will jetzt nichts darüber sagen, daß eine solche Feststellung eigentlich formallogisch schon ein «Urteil» ist. In dem Augenblick, wo wir überhaupt beginnen, irgend etwas nicht so zu lassen, wie es vor uns auftritt, sondern ihm gegenüber eine Fest­stellung machen, greifen wir mit unserem Denken ein in die Welt, die um uns herum ist. Und wenn wir irgendein Recht haben sollen, so in die Welt einzugreifen, daß wir etwas als «subjektiv» bestimmen, dann müssen wir uns bewußt sein, daß dasjenige, was bestimmt, daß etwas «subjektiv» genannt wird, selber nicht subjektiv sein darf.",
      "Denn nehmen wir an, wir hätten hier die Sphäre der Subjektivität (es wird ein Kreis an die Tafel gezeichnet und darüber das Wort «Subjektivität» geschrieben) und es ginge von derselben aus zum Beispiel die Feststellung, A sei subjektiv, sei «meine Vorstellung» oder was auch immer, dann ist diese Feststellung selber subjektiv.",
      "# Bild s. 191",
      "Die Folgerung daraus ist dann nicht etwa, daß wir diese Feststellung gelten lassen dürfen, sondern die Folgerung muß sein, daß ein solcher Schluß nicht gemacht werden darf, denn eine solche Feststellung würde sich selber aufheben. Wenn eine Subjektivität nur aus sich",
      "selbst heraus festgestellt werden kann, so wäre das eine sich selbst aufhebende Feststellung. Wenn die Feststellung «A ist subjektiv» einen Sinn haben soll, so muß sie nicht ausgehen von der Sphäre der Subjektivität, sondern von einer Realität außerhalb der Subjektivität. Das heißt, wenn das «Ich» überhaupt in der Lage sein soll, sagen zu dürfen, etwas trage einen subjektiven Charakter, zum Beispiel etwas sei «meine Vorstellung», wenn das «Ich» das Recht dazu haben soll, etwas als subjektiv zu bezeichnen, dann darf es nicht selber innerhalb der Sphäre der Subjektivität sein, sondern es muß diese Feststellung von außerhalb der Sphäre der Subjektivität machen. Wir dürfen also die Feststellung, daß etwas subjektiv sei, nicht zurückleiten auf das Ich, das selber subjektiv ist.*)",
      "Damit ergibt sich aber ein Ausweg aus der Sphäre der Subjektivität heraus, indem wir uns klar darüber werden, daß wir keine Feststel­lung darüber machen könnten, was subjektiv und was objektiv ist, und schon die allerersten Schritte des Denkens darüber überhaupt unterlassen müßten, wenn wir nicht zu Subjektivität und Objektivi­tät in einer solchen Beziehung stünden, daß beides gleichen Anteil an uns hat. Das führt uns dazu, anzuerkennen - was ich jetzt nicht weiter ausführen kann -, daß unser Ich nicht nur subjektiv genom­men werden darf, sondern umfassender ist als unsere Subjektivität. Wir haben ein Recht dazu, aus einem gewissen gegebenen Inhalte, also aus etwas Objektivem, dasjenige abzugrenzen, was subjektiv ist.",
      "Es treten uns zunächst die verschiedenen Begriffe «objektiv», «subjektiv» und «transsubjektiv» entgegen. «Objektiv» ist selbstver­ständlich etwas anderes als «transsubjektiv» [Lücke in den Nach-schriften].",
      "Nun handelt es sich darum - wenn wir diese Voraussetzungen gemacht haben -, ob wir in der Lage sind, den Stein des Anstoßes wegzuräumen, der zu den wichtigsten Hemmnissen in der Erkennt­nistheorie gehört, nämlich die Frage, ob innerhalb der Subjektivität der ganze Umfang unseres Ich gefunden werden kann oder nicht. Denn wenn das Ich auch an der Objektivität teilhaftig sein muß,",
      "*)    siehe Hinweis auf Seite 214",
      "gewinnt die Frage «Kann etwas in die Sphäre der Subjektivität her­einkommen?» eine ganz andere Gestalt. Sobald man das Ich als an der Sphäre der Objektivität teilhaftig bezeichnen darf, muß das Ich in sich gleichartige Qualitäten haben wie das Objektive; es muß etwas von der Sphäre der Objektivität auch im Ich zu finden sein. Mit anderen Worten: Wir dürfen jetzt eine Beziehung zwischen Objekti­vem und Subjektivem voraussetzen, die wesentlich abweicht von der Auffassung, daß nichts vom Transsubjektiven zum Subjektiven hin­überkommen könne.",
      "Wenn man sagt, daß nichts zum Subjektiven hinüberkommen kann, dann hat man erstens das Subjektive erkenntnistheoretisch als in sich abgeschlossen bestimmt, und zweitens hat man dabei einen Begriff verwendet, der nur für eine gewisse Sphäre der Realität Berechtigung hat, nicht aber für den ganzen Umfang der Realität Geltung haben kann. Das ist der Begriff des «Ding an sich». Dieser Begriff spielt bei vielen Erkenntnistheoretikern eine große Rolle; er ist wie ein Netz, in welchem sich das philosophische Denken selber fängt. Man merkt aber dabei gar nicht, daß dieser Begriff nur für eine gewisse Sphäre der Realität gilt und daß er aufhört Geltung zu haben, wo diese Sphäre aufhört.",
      "Im Materiellen zum Beispiel hat der Begriff Geltung. Ich möchte erinnern an das Beispiel vom Petschaft und Siegellack. Wenn Sie ein Petschaft nehmen, auf dem der Name «Müller» steht, und Sie drük­ken es in heißen Siegellack, dann können Sie mit Recht sagen: Es kann nichts von der Materie des Petschaft herüberkommen in den Siegellack. - Da haben Sie etwas, wo das Nicht-herüberkommen-Können gilt. Mit dem Namen «Müller» aber ist das anders, der kann restlos hinüberfließen in den Siegellack. Und wenn der Lack selbst sprechen könnte und betonen wollte, daß nichts von der Materie des Petschaft in ihn hineingeflossen ist, so müßte er doch zugeben, daß das, worauf es ankommt, nämlich der Name «Müller», restlos her­übergekommen ist. Da haben wir also die Sphäre überschritten, wo der Begriff des «Ding an sich» eine Berechtigung hatte.",
      "Woher ist es denn gekommen, daß dieser Begriff, der in einer gewissen feineren Weise bei Kant, ziemlich grobklotzig bei Schopenhauer,",
      "dann aber scharfsinnig beschrieben bei den verschiedensten Erkenntnistheoretikern des 19. Jahrhunderts auftritt, eine solche Bedeutung hat gewinnen können?",
      "Es ist, wenn man auf die ganze Sache näher eingeht, daher gekom­men, daß das, was die Menschen in Begriffen ausarbeiten, doch von der ganzen Art ihres Denkens abhängt. Nur in einem Zeitalter, in welchem alle Begriffe so charakterisiert werden müssen, daß sie immer an der äußeren Wahrnehmung gebildet sind, hat sich ein solcher Begriff wie der des «Ding an sich» bilden können.",
      "Die nur an der äußeren Wahrnehmung gewonnenen Begriffe sind aber nicht geeignet zur Charakterisierung des Geistigen. Würde man nicht einen solchen verkappten, man möchte sagen, gründlich mas­kierten Materialismus in die Erkenntnistheorie eingeschleppt haben -denn das ist das Faktum, worauf es ankommt: es ist ein wirklich nicht leicht zu erkennender Materialismus in die Erkenntnistheorie einge­schleppt worden -, so würde man sich darüber klar sein, daß eine Er­kenntnistheorie, die für die geistigen Gebiete gelten soll, auch solche Begriffe haben muß, die nicht in diesem groben Stile gebildet sind wie der Begriff des «Ding an sich». Für das Geistige, wo überhaupt von einem Draußen und Drinnen nicht in demselben Sinne gesprochen werden kann, muß es klar sein, daß wir feinere Begriffe brauchen.",
      "Ich konnte das nur skizzenhaft andeuten, denn ich müßte sonst ein ganzes Buch schreiben, das sehr dick werden würde und auch meh­rere Bände haben müßte, weil an die Philosophiegeschichte und an die Erkenntnistheorie sich auch metaphysische Gebiete anschließen müßten. Aber Sie können daran sehen, daß es ganz begreiflich ist, wenn diese Art des Denkens, weil sie aus tief maskierten Vorurteilen entspringt, unbrauchbar ist für alles das, was in die geistige Welt hineinreicht.",
      "Ich habe Ihnen jetzt eine Stunde lang nur über diesen allerabstrak­testen Begriff gesprochen. Ich habe mich bemüht, die Sache verständ­lich zu machen und bin mir absolut klar darüber, daß die Einwände, die mir selber deutlich vor der Seele stehen, selbstverständlich in mancher anderen Seele auch auftauchen können. Wenn es sich um eine andere Versammlung handelte, so bedürfte es vielleicht einer",
      "besonderen Rechtfertigung, daß man, man könnte sagen, seine Zuhö­rer so hintergeht, daß man statt des gewohnten Tatsachenmaterials, das erwartet wird, einmal auch in abstraktesten - wie wohl manche glauben: vertracktesten - Begriffen spricht. Nun, wir haben schon im Laufe unserer theosophischen Arbeit immer wieder gesehen, daß Theosophie auch das Gute hat, daß man innerhalb der theosophi­schen Bewegung die Pflicht zur Erkenntnis ausbildet, und daß damit nach und nach ein unartiger Begriff überwunden wird, der überall sonst existiert, ein sehr unartiger Begriff, welcher sagt: Das ist ja doch etwas, was über meinen Horizont geht, womit ich mich nicht beschäftigen will, was mir nicht interessant ist!",
      "Für manchen, der sich mit philosophischen Grundfragen beschäf­tigt und der die manchmal nur spärlich besuchten Kollegien über Erkenntnistheorie aus Erfahrung kennt, mag es überraschend sein, daß hier in unserer Bewegung so viele Menschen, die doch nach dem Urteil dieses oder jenes Erkenntnistheoretikers «gründlichste Dilet­tanten» auf dem Gebiete der Erkenntnistheorie sind, zu einer Ver­sammlung kommen, um sich ein solches Thema anzuhören. Wir haben an manchen Orten sogar eine noch größere Anzahl von Zuhö­rern gerade bei philosophischen Vorträgen gehabt, die zwischen die theosophischen eingelegt worden sind.",
      "Wenn man die Sachlage aber gründlicher betrachtet, wird man sagen dürfen, daß dies gerade eines der besten Zeugnisse für die Theosophen ist. Die Theosophen wis­sen, daß sie alles unbefangen anhören sollen, was an Einwänden vorgebracht werden kann.",
      "Sie sind ruhig dabei, denn sie wissen ganz genau, daß Einwände gegen die Forschungen in den übersinnlichen Welten zwar möglich und berechtigt sind, sie wissen aber auch, daß manches, was zunächst als unlogisch bezeichnet worden ist, sich schließlich doch als sehr logisch herausstellen kann. Der Theosoph lernt auch, es als seine Pflicht zu betrachten, Erkenntnisse in seine Seele hineinzubekommen, wenn es ihm auch Mühe macht, sich mit Erkenntnistheorie und Logik zu beschäftigen.",
      "Denn so wird er immer mehr und mehr in der Lage sein, nicht nur allgemeine theoso­phische Darstellungen anhören zu wollen, sondern auch mit logi­schen Begriffen und Begriffsgliederungen ernst in der Theosophie zu",
      "arbeiten. Es wird sich die Welt schon mit dem Gedanken bekanntma­chen müssen, daß die Philosophie in ihrem umfänglichsten Sinne innerhalb der theosophischen Bewegung wird wiedergeboren werden können. Eifer für philosophische Strenge, für gründliche logische Begriffsbildung wird sich nach und nach, wenn ich das Wort gebrau­chen darf, einnisten innerhalb der theosophischen Bewegung. Womit ich nicht gesagt haben will, daß die Resultate in dieser Beziehung bei genauem Zusehen jetzt schon sehr befriedigend sind. Wir werden das durchaus noch mit Bescheidenheit ansehen müssen, aber wir sind auf dem Wege zu diesem Ziel.",
      "Je mehr wir uns den guten Willen zum Denkerischen, zur wissen­schaftlichen Gewissenhaftigkeit, zur philosophischen Gründlichkeit aneignen, desto mehr werden wir durch die theosophische Arbeit nicht nur unsere vergänglichen persönlichen Ziele verfolgen, sondern menschheitliche Ziele erreichen können. Manches ist heute erst auf der Stufe des allerersten Wollens.",
      "Aber es zeigt sich, daß in dem Willen, der aufgewendet wird zur Erkenntnis, schon etwas liegt wie eine ethische Selbsterziehung, die erreicht wird durch das Interesse, das wir der Theosophie entgegenbringen. Und daran wird es bald nicht mehr mangeln.",
      "Wenn keine anderen Hindernisse sich finden als die, welche es heute schon gibt, so wird von der Außenwelt der Theosophie die Anerkennung nicht versagt werden können, daß der Theosoph nicht strebt nach leichter Befriedigung seiner seelischen Sehnsuchten, sondern daß sich in der Theosophie ein ernstes Streben nach philosophischer Gründlichkeit und Gewissenhaftigkeit kund-gibt, nicht ein bloßer Dilettantismus. Dieses Streben wird gerade geeignet sein, das philosophische Gewissen der Menschen zu schär­fen.",
      "Wenn wir die theosophischen Lehren nicht als Dogmen hinneh­men, sondern verstehen, was Theosophie als reale Macht in unserer Seele sein kann, dann kann das Anfeuerungsmaterial für die mensch­liche Seele sein, um immer mehr und mehr die in ihr verborgenen Kräfte zu ergreifen und um sie zum Bewußtsein ihrer Bestimmung zu führen. Deshalb wollen wir innerhalb unserer theosophischen Bewe­gungen fördern diesen Eifer für gründliche Logik und Erkenntnis­theorie, und so, indem wir fester auf dem Boden unserer physischen",
      "Welt stehen, immer klarer und ohne Schwärmerei und nebulose Mystik aufschauen lernen zu den geistigen Welten, deren Inhalt wir herunterholen und einfügen wollen in unser physisches Weltbild.",
      "Ob wir das tun wollen, davon hängt es einzig und allein ab, ob wir der Theosophie eine wirkliche Mission im Erdendasein der Mensch­heit zuschreiben können.",
      "# Bild s. 200"
    ],
    "sentences": [
      [
        "Im Anschluß an die öffentlichen Vorträge «Wie widerlegt man Theosophie?» und «Wie verteidigt man Theosophie?» sowie im Anschluß an die Betrachtungen, die ich in diesen Tagen in dem Vortragszyklus über «Okkulte Physiologie» gegeben habe, können sich eine Reihe von Fragen aufdrängen, und es liegt das Bedürfnis vor, über diese Fragen, die hier berührt worden sind, sich mit den verehrten Zuhö­rern ein wenig zu verständigen.",
        "Die beiden öffentlichen Vorträge hatten vor allen Dingen das Ziel, zu zeigen, wie man auf dem Boden der Geisteswissenschaft oder Theosophie sich sehr wohl bewußt sein muß der möglichen Einwände, die sich ergeben können, und wie der Okkultist das Berechtigte dieser Einwände durchaus anerkennt, und andererseits konnte Ihnen aus den Vorträgen hervorgehen eine ganz bestimmte, scharf nuancierte Stellungnahme, wie die theosophischen Wahrheiten gegenüber den gewichtigen Einwänden der Gegner zu vertreten sind."
      ],
      [
        "Gerade aus der Erkenntnis der gekennzeichneten Schwierigkeiten, die sich für die Theosophie ergeben, sollte sich aber bei jedem Theo­sophen das Bedürfnis bilden, daß in der Vertretung der theosophi­schen Wahrheiten möglichste Genauigkeit, höchste Präzision walten möge.",
        "Das ist etwas, dessen sich derjenige, der aus der Erkenntnis der entsprechenden Zusammenhänge heraus diese Dinge zu vertreten hat, sehr wohl bewußt ist, womit er aber - trotz alle dem, was in den öffentlichen Vorträgen hervorgehoben worden ist - unvermeidlich in Kollision mit denjenigen kommt, die auf dem Boden der heutigen Wissenschaft stehen.",
        "Deshalb erfordert Theosophie, so sonderbar das"
      ],
      [
        "scheinen mag, auf der einen Seite zum Einkleiden der aus den höhe­ren Welten heruntergeholten Wahrheiten, auf der anderen Seite nicht minder aus der bloßen gewöhnlichen Vernünftigkeit heraus das genaueste, präziseste logische Formulieren.",
        "Und wer sich diese Auf­gabe setzt, präzis und genau logisch zu formulieren, und zu diesem Zwecke alles vermeidet, was etwa Wortfüllsel in einem Satze oder nur rhetorische Verbrämung wäre, der fühlt sehr häufig, wie leicht er mißverstanden werden kann, einfach aus dem Grunde, weil in unse­rer Zeit nicht überall das intensive Bedürfnis vorhanden ist, die vertretenen Wahrheiten ebenso genau und präzis, wie sie ausgespro­chen werden, auch hinzunehmen.",
        "Es ist in unserer Zeit die Mensch­heit, selbst da, wo sie sich wissenschaftlich betätigt, noch gar nicht gewöhnt an dieses Ganz-genau-Nehmen.",
        "Wenn man das Vorgetra­gene ganz genau nimmt, so darf man in den Sätzen nicht nur nichts ändern, sondern man muß auch genau auf die Grenze achten, die in die Formulierungen mit aufgenommen ist."
      ],
      [
        "Wir haben hierfür ein leichtes Beispiel, das bei dem Fragenstellen kürzlich aufgetaucht ist.",
        "Es wurde gefragt: Wenn das Traumbe­wußtsein nur eine Art Bilderbewußtsein ist, wie kommt es denn dann, daß aus diesem Traumbewußtsein heraus gewisse unterbe-wußte Handlungen, wie zum Beispiel Nachtwandeln, vollzogen wer­den können? - Da hat der Fragesteller nicht beachtet, wie ich auch damals schon erwähnt habe, daß mit dem Satze, es seien die Inhalte des Traumbewußtseins etwas Bildhaftes, nicht gemeint ist, sie seien nur Bildhaftes, sondern daß selbstverständlich, da nur von einer Seite her der Horizont des Traumbewußtseins charakterisiert worden ist, gerade aus der Natur dieser Charakteristik sich ergab: Wie unsere Tageshandlungen folgen aus unserem Tagesbewußtsein, so könnten gewisse Handlungen weniger bewußter Natur auch folgen aus dem Bilderbewußtsein des Traumes."
      ],
      [
        "Es soll durchaus ohne Anklage gesagt werden, daß das ungenaue Zuhören einer der hauptsächlichsten Gründe ist, warum der Theoso­phie und ihrer Vertretung heute so viele Mißverständnisse entgegen­gebracht werden.",
        "Es werden solche Mißverständnisse nicht etwa bloß von den Gegnern der Theosophie entgegengebracht, sondern in"
      ],
      [
        "einem hohen Maße auch von denjenigen, die Bekenner dieser theoso­phischen Weltanschauung sind.",
        "Und vielleicht liegt ein großer Teil der Schuld an den Mißverständnissen, welche die Außenwelt der Geisteswissenschaft entgegenbringt, daran, daß gerade auch inner­halb der theosophischen Kreise nach der gekennzeichneten Richtung hin so viel gesündigt wird."
      ],
      [
        "Wenn wir nun unter den Wissenschaften, welche in unserer Zeit Geltung haben, Umschau halten, so könnte vielleicht die allgemeine Empfindung dahin gehen, daß die Theosophie am meisten Beziehun­gen hätte, am meisten verwandt wäre mit der Philosophie mit ihren verschiedenen Zweigen.",
        "Eine solche Behauptung wäre auch durchaus richtig, und man könnte eigentlich aus der Natur der Sachlage heraus voraussetzen, daß die nächste Möglichkeit, den theosophischen Erkenntnissen Verständnis entgegenzubringen, auf der Seite der Phi­losophie vorliegen würde.",
        "Aber gerade da zeigen sich wieder andere Schwierigkeiten."
      ],
      [
        "Philosophie, wie sie heute, man darf sagen, allüberall gepflegt wird, ist in einem viel höheren Maße eine Art Spezialwissenschaft gewor­den, als sie vor verhältnismäßig noch kurzer Zeit war.",
        "Sie ist eine Spezialwissenschaft geworden und arbeitet, wenn wir ihre praktische Arbeit heute ansehen und uns nicht auf einzelne Theorien einlassen, praktisch im wesentlichen in abstrakten Regionen.",
        "Und es ist nicht viel Neigung vorhanden, die Philosophie zu der konkreten Auffas­sung des Tatsächlichen herunterzuführen.",
        "Ja, es ergeben sich sogar Schwierigkeiten in dem heutigen Betriebe der Philosophie, wenn man mit diesem philosophischen Streben von heute die Welt des Tatsäch­lichen umfassen will.",
        "Die nach den verschiedensten Richtungen hin mit großem Scharfsinn in der zweiten Hälfte des 19.",
        "Jahrhunderts und bis in unsere Tage hinein ausgeführte Erkenntnistheorie ist ja so, wie wir sie heute haben, hauptsächlich aus dem Grunde entstan­den, weil diese Schwierigkeiten, aus den abstrakten Höhen des Den­kens, des Begriffes herab an die Tatsachen heranzudringen, gefühlt wurden."
      ],
      [
        "Nun fühlt man, daß gerade bei solchen Vorträgen, wie es diejeni­gen dieses Zyklus über «Okkulte Physiologie» sind, Theosophie"
      ],
      [
        "uberall genötigt ist, mit dem, was sie als übersinnliche Bewußtseins-inhalte zu geben hat, unmittelbar heranzudringen an unsere tatsächli­che Welt.",
        "Wenn ich trivial reden darf, möchte ich sagen: Theosophie hat es nicht so gut wie die heutige Philosophie, welche sich in abstrakten Regionen hält und welche durchaus nicht sehr geneigt sein würde, in ihre Betrachtungen solche Begriffe wie, sagen wir, zum Beispiel des Blutes oder der Leber oder der Milz, also Inhalte des Tatsächlichen aufzunehmen.",
        "Es würde diese Philosophie sehr davon zurückschrecken, die Brücke von ihren abstrakten Begriffsbildungen zu schlagen nach den konkreten, unmittelbar tatsächlich an uns her­antretenden Ereignissen und Dingen.",
        "Die Theosophie ist in dieser Beziehung waghalsiger und kann gerade deshalb gegenüber der Phi­losophie sehr leicht angesehen werden als eine Geistesbetätigung, die kühn und unberechtigt eine Brücke schlägt von dem Geistigsten bis zu dem Allertatsächlichsten herunter."
      ],
      [
        "Nun muß es doch eigentlich interessant sein, sich einmal zu fragen:"
      ],
      [
        "Woher kommt es denn, daß es Philosophen so schwer ist, an die Theosophie heranzukommen? - Vielleicht gerade aus diesem Grunde, weil die Philosophie es vermeidet, diese Brücke zu schlagen.",
        "Für die Theosophie selber ist diese Tatsache in gewissem Sinne eine Fatalität, ist außerordentlich fatal.",
        "Denn man stößt mit den theoso­phischen Erkenntnissen, insbesondere dann, wenn man sie herunter-führen will bis zur logischen Durcharbeitung, sehr, sehr häufig auf Widerstände.",
        "Gerade auf philosophischer Seite stößt man in dieser Beziehung auf Widerstände.",
        "Und zwar ist es sogar sehr oft vorge­kommen, daß man weniger auf Widerstände stößt, wenn man sozu­sagen lustig darauflos den Menschen sensationelle Beobachtungen aus den höhere Welten erzählt.",
        "Das verzeihen sie oftmals verhältnis­mäßig leicht, denn erstens sind diese Dinge «interessant», und zwei­tens sagen sich die Menschen: Nun, insofern wir nicht in diese Welten hinaufschauen können, sind wir gar nicht dazu aufgerufen, irgendein Urteil darüber zu fällen."
      ],
      [
        "Nun ist es aber das Bestreben der Theosophie, alles, was in den höheren Welten gefunden werden kann, zum vernünftigen Begreifen herunterzuführen.",
        "Gefunden sind die Tatsachen, wenn sie wirklich"
      ],
      [
        "als solche gelten können, durch übersinnliches Forschen in den über­sinnlichen Welten.",
        "Die Form der Darstellung sollte aber in unserer Gegenwart so gegeben werden, daß alles in streng logische Formen gekleidet wird und daß an all den Stellen, wo es heute schon möglich ist, darauf hingewiesen wird, wie die allertatsächlichsten äußeren Vorgänge uns schon überall Bestätigungen für das ergeben können, was wir aus der geistigen Forschung heraus behaupten können.",
        "In diesem ganzen Vorgange, die Erkenntnisse der geistigen Welt herun­terzuholen, sie einzukleiden in logische oder sonstige Vernunftfor­men und sie so darzubieten in einer Gestalt, welche dem logischen Bedürfnisse unserer Zeit entgegenkommt, besteht nun heute eine, man darf sagen, wirklich außerordentlich begreifliche Quelle zahl-reichster Mißverständnisse."
      ],
      [
        "Nehmen Sie einmal das Komplizierte, was in diesen Vorträgen über «Okkulte Physiologie» gesagt worden ist, das in seinen Bestim­mungen überall nur mit Einschränkungen, mit genauen Angaben der Grenzen Hinzunehmende, nehmen Sie das ganz Komplizierte der in sich ungeheuer beweglichen und variablen Welt des Geistigen, und vergleichen Sie diese Welt des geistigen in ihrer ganzen Variabilität, in der Schwierigkeit, etwas uns aus geistigen Welten Herunterkommen­des mit groben Begriffskonturen zu umspannen, vergleichen Sie es mit der Leichtigkeit, irgendeine äußere Tatsache durch ein Experi­ment oder durch sinnliche Beobachtung zu charakterisieren und in einem logischen Stil zu beschreiben!"
      ],
      [
        "Nun besteht aber heute überall in unserer Philosophie die Ten­denz, wo Begriffe erläutert und beschrieben werden, auf gar nichts anderes Rücksicht zu nehmen als auf solche Vorstellungen, die aus der Welt gewonnen werden, die als die sinnliche Welt vor uns liegt.",
        "Das wird in der Philosophie besonders dann fühlbar, wenn sie genö­tigt ist, zum Beispiel auf ethischem Gebiete einen anderen Ursprung für die Grundbegriffe zu finden als solche Vorstellungen, die an der äußeren Wahrnehmung der physischen Welt gewonnen werden.",
        "Wir finden - und das wäre unschwer nachzuweisen, aber natürlich nur durch ausführliche Darlegungen aus der zeitgenössischen philo­sophischen Literatur -, daß bei allem, was heute in der Philosophie"
      ],
      [
        "verarbeitet wird, die Begriffsbestimmungen so grob sind, weil für begriffliche Bewußtseinsinhalte im Grunde genommen nur Rücksicht genoinmen wird auf die Wahrnehmungswelt, die um uns herum existiert und nur aufgrund derselben die Begriffe gebildet werden."
      ],
      [
        "Gibt es eigentlich einen Anhaltspunkt dafür, daß in der Philoso­phie bei der Entstehung der allerelementarsten Begriffe Bewußtseins-inhalte auch von anderer Seite gewonnen werden als von der Seite der sinnlich wahrnehmbaren Welt? - Kurz gesagt: es fehlt der zeitge­nössischen Philosophie die Möglichkeit, zu einem Verständnis der Theosophie zu kommen, weil sie mit ihren Theorien nicht anknüpfen kann an solche Begriffe, wie wir sie in unseren theosophischen Aus­einandersetzungen pflegen.",
        "Wir haben in der philosophischen Litera­tur den Bewußtseinshorizont dadurch bestimmt, daß bei dem Bilden von Begriffen überall nur Rücksicht genommen wird auf die äußere Wahrnehmungswelt und nicht auf solche Inhalte, die von anderer Seite als von der der sinnlichen Wahrnehmungen herrühren."
      ],
      [
        "Die Theosophie nun muß ihre Begriffe auf eine ganz andere Weise gewinnen; sie muß zu übersinnlicher Erkenntnis aufsteigen und ihre Begriffe aus dem Übesinnlichen herunterholen, sie muß aber auch in die Seite der Realität sich hineinvertiefen und muß die aus der Beob­achtung der sinnlichen Welt gewonnenen philosophischen Begriffe beherrschen.",
        "Wenn wir uns das einmal schematisch vorstellen wol­len, so haben wir auf der einen Seite in der Philosophie Begriffe, die durch äußere Wahrnehmung gewonnen werden, auf der anderen Seite die Begriffe, die aus dem Übersinnlichen durch geistige Wahr­nehmung gewonnen werden.",
        "Und wenn wir das Feld der Begriffe uns denken, durch die wir uns verständigen, so müssen wir sagen: Wenn Theosophie als etwas Berechtigtes gelten soll, dann müssen unsere Begriffe von beiden Seiten her genommen werden, auf der einen Seite von der sinnlichen Wahrnehmung, auf der anderen Seite von der geistigen Wahrnehmung, und auf dem Felde unserer Begriffe müssen diese beiden Seiten sich treffen."
      ],
      [
        "# Bild s. 187"
      ],
      [
        "Es muß das Bedürfnis bestehen, gerade in theosophischen Darstel­lungen mit den aus der geistigen Welt heruntergeholten Begriffen sich mit den philosophischen Begriffen zu treffen, das heißt, daß mit un­seren Begriffen überall angeschlossen werden kann an die Begriffe, die aus der äußeren sinnlichen Wahrnehmungswelt gewonnen werden."
      ],
      [
        "Unsere heutigen Erkenntnistheorien sind mehr oder weniger fast ausschließlich von dem Gesichtspunkt aus aufgebaut, daß die Begriffe nur von einer Seite her genommen werden.",
        "Ich will damit nicht sagen, daß es nicht auch Erkenntnistheorien gibt, wo etwas Übersinnliches als Ursprung der Begriffe zugelassen ist.",
        "Aber über­all, wo etwas positiv bewiesen werden soll, sind die Beispiele dadurch charakterisiert, daß die Begriffe nur von der linken Seite (Schema) genommen sind, also von der Seite, auf der die Begriffe an der sinnlich-physischen Wahrnehmungswelt gewonnen werden.",
        "Das ist auch ganz natürlich, weil [in der Philosophie] geistige Tatsachen als solche nicht anerkannt werden.",
        "Man berücksichtigt eben nicht den Fall, daß geistige Tatsachen, die aus den geistigen Welten herunterge­holt werden, ebenso in Begriffe gebracht werden können, wie die Tatsachen der physischen Welt in Begriffe gebracht werden.",
        "Dieser Umstand hat dazu geführt, daß die Theosophie, wenn sie sich mit der Philosophie verständigen will, auf der Seite der Philosophie fast gar keinen vorbereiteten Boden findet und daß in der Philosophie die Art und Weise, wie in der Theosophie die Begriffe gebraucht werden, nicht leicht verstanden werden kann."
      ],
      [
        "Man möchte sagen: Steht man der äußeren sinnlichen Wahrneh­mungswelt gegenüber, so hat man es leicht, den Begriffen scharfe Konturen zu geben.",
        "Da haben die Dinge selbst scharfe Konturen, scharfe Grenzen, da ist man leicht imstande, auch den Begriffen"
      ],
      [
        "scharfe Konturen zu geben.",
        "Steht man dagegen der in sich bewegli­chen und variablen geistigen Welt gegenüber, so muß oft vieles erst zusammengetragen und in den Begriffen Einschränkungen oder Erweiterungen gemacht werden, um einigermaßen charakterisieren zu können, was eigentlich gesagt werden soll.",
        "Die Erkenntnistheorie, wie sie heute getrieben wird, ist am allerwenigsten geeignet, sich auf solche Begriffe einzulassen, wie sie in der Theosophie verwendet werden.",
        "Denn indem man, um die Begriffe zu bestimmen, die Gründe für die Begriffsbestimmungen - bewußt oder unbewußt -nur von einer Seite nimmt, mischt sich in alle Begriffe, die man bildet, ohne daß man es recht weiß, etwas hinein, was zu solchen erkennt­nistheoretischen Begriffen führt, die überhaupt nicht zu brauchen sind, um in der Theosophie irgend etwas zu erläutern oder zu erklä­ren.",
        "Der Begriff, wie er von der sozusagen nichttheosophischen Welt geliefert wird, ist einfach ungeeignet als Instrument zum Charakteri­sieren dessen, was durch die Theosophie aus der geistigen Welt heruntergeholt wird."
      ],
      [
        "Nun gibt es insbesondere einen solchen Begriff, der auf dem Gebiet der Erkenntnistheorie ein furchtbarer Störenfried ist.",
        "Ich weiß sehr wohl, daß er gar nicht als solcher empfunden wird, aber er ist ein Störenfried.",
        "Das ist, wenn man von allen feineren Nuancierun­gen absieht, die in so scharfsinniger Weise im Verlaufe des 19.",
        "Jahr­hunderts sich herausgebildet haben, der Punkt, wo das erkenntnis­theoretische Problem so formuliert wird, daß man sagt: Wie kommt eigentlich das Ich mit seinem Bewußtseinsinhalt - oder wenn man meinetwillen es vermeiden will, vom Ich zu sprechen -, wie kommt unser Bewußtseinsinhalt dazu, von uns auf eine Realität bezogen zu werden? - Diese Gedankengänge haben mehr oder weniger - mit Ausnahme von gewissen erkenntnistheoretischen Richtungen im 19.",
        "Jahrhundert - zu einer Erkenntnistheorie geführt, welche immer wieder und wieder als eine große Schwierigkeit empfindet, die Mög­lichkeit zu sehen, wie das Transsubjektive oder Transzendente, also das, was außerhalb unseres Bewußtseins liegt, in unser Bewußtsein eintreten kann.",
        "Ich will zugeben, daß damit das Erkenntnisproblem nur grob charakterisiert ist.",
        "Aber es sind doch die Schwierigkeiten im"
      ],
      [
        "wesentlichen damit charakterisiert, daß man sagt: Wie kann über­haupt das, was subjektiver Bewußtseinsinhalt ist, irgendwie heran an das Sein, an die Realität?",
        "Wie kann es bezogen werden auf die Realität?",
        "Denn wir mussen uns klar sein, daß, selbst wenn wir eine außerhalb unseres Bewußtseins liegende transsubjektive Realität vor­aussetzen, dasjenige, was in unserem Bewußtsein drinnen ist, nicht unmittelbar an diese Realität herantreten kann.",
        "Wir haben also - so heißt es - in uns den Bewußtseinsinhalt, und wir können uns fragen:"
      ],
      [
        "Wie haben wir die Möglichkeit, aus diesem Bewußtseinsinhalt heraus in das Sein, in die Realität, die unabhängig ist von unserem Bewußt­sein, hineinzudringen? -Ein bedeutender Erkenntnistheoretiker der Gegenwart hat dieses"
      ],
      [
        "Problem mit einem prägnanten Ausdruck charakterisiert: Das menschliche Ich, insofern es den Bewußtseinshorizont umfaßt, könne sich nicht selber überspringen, denn es müßte aus sich heraus­springen, wenn es in die Realität hineinspringen würde.",
        "Dann wäre es aber in der Realität und nicht im Bewußtsein. - Es scheint also für diesen Erkenntnistheoretiker klar zu sein, daß überhaupt nichts dar­über ausgemacht werden kann, wie der Bewußtseinsinhalt zur wirk­lichen Realität steht."
      ],
      [
        "Es ist mir vor vielen Jahren in meinen erkenntnistheoretischen Schriften darum zu tun gewesen, zunächst einmal dieses Erkenntnis-problem festzustellen - das ja auch in der Theosophie grundlegend ist - und dann die Schwierigkeiten, die sich aus einer solchen wie der eben bezeichneten Formulierung ergeben, wegzuschaffen.",
        "Dabei konnte einem allerdings sehr Merkwürdiges passieren.",
        "So zum Bei­spiel gab es in der Zeit, in welcher sich das zugetragen hat, wovon ich sprechen will, Philosophen, die von vornherein davon ausgingen -ganz ähnlich wie Schopenhauer - zu sagen: «Die Welt ist meine Vorstellung.» Das heißt, das, was im Bewußtsein gegeben ist, das ist zunächst nur Vorstellungsinhalt, und nun handelt es sich um die Frage, wie eine Brücke zu schlagen ist von der Vorstellung zu dem, was außerhalb des Vorgestellten ist, zu der transsubjektiven Realität.",
        "Nun ist eigentlich für jeden, welcher sich nicht faszinieren läßt durch Feststellungen, die angeblich auf diesem Felde gemacht worden sind,"
      ],
      [
        "sondern der unbefangen an die Sache herantritt, eine Frage sogleich gegeben, und einer großen Menge der erkenntnistheoretischen Lite­ratur gegenüber, namentlich der, welche in den siebziger und in der ersten Hälfte der achtziger Jahre geschrieben worden ist, muß man diese Frage aufwerfen: Wenn irgend etwas «meine Vorstellung» ist, und wenn dieses Vorgestellte selbst mehr sein soll als etwas innerhalb des Bewußtseinsinhaltes Liegendes, wenn es Geltung für sich selbst haben soll, dann ist damit etwas gesagt, was im Grunde genommen nicht vor dem Ausgangspunkt der Erkenntnistheorie liegen darf, sondern etwas, was erst festgestellt werden kann, nachdem diese viel wichtigeren erkenntnistheoretischen Grundfragen erörtert worden sind.",
        "Denn wir mussen uns zuerst fragen: Warum dürfen wir über­haupt etwas, was in uns als Bewußtseinsinhalt auftritt, «meine Vor­stellung» nennen?",
        "Haben wir ein Recht zu sagen: Was auf meinem Bewußtseinshorizont auftritt, ist meine Vorstellung? - Die Erkennt­nistheorie hat durchaus nicht das Recht, auszugehen von dem Urteil, das Gegebene sei meine Vorstellung, sondern sie hat die Pflicht, wenn sie wirklich auf ihre ersten Anfänge zurückgeht, erst zu recht­fertigen, daß das, was da auftritt, der subjektive Bewußtseinsinhalt ist."
      ],
      [
        "Es gibt selbstverständlich mehrere hundert Einwände gegenüber dem, was jetzt gesagt worden ist, aber ich glaube nicht, daß es möglich ist, einen einzigen dieser Einwände lange festzuhalten, wenn man unbefangen auf die Sache eingeht.",
        "Aber ich habe erlebt, daß ein bekannter und bedeutender Philosoph mir eine ganz eigentümliche Antwort gab, als ich ihn auf dieses Dilemma aufmerksam machte und ihm auseinandersetzen wollte, daß es doch zuerst geprüft werden müsse, ob es erkenntnistheoretisch gerechtfertigt sei, die Vorstellung als etwas Nicht-Reales zu charakterisieren.",
        "Da sagte er: Das ist doch selbstverständlich, das liegt doch schon in der Definition des Wortes «Vorstellung», daß wir etwas vor uns stellen, was nicht real ist. - Er konnte gar nicht begreifen - so sehr waren ihm diese Vorstellungen eingewurzelt, welche im Laufe von Jahrhunderten gewachsen sind -, daß man mit dieser ersten Definition etwas noch vollständig Unbe­gründetes hinstellt."
      ],
      [
        "Wenn wir überhaupt innerhalb des Umfanges der Welt, in der wir drinnenstehen - wobei ich Sie bitte, die Worte «die Welt, in der wir drinnenstehen» zu verstehen als die Welt, wie wir sie im Alltag ha­ben -, wenn wir überhaupt innerhalb dieser Welt irgendeine Feststel­lung machen wollen, zum Beispiel daß dasjenige, was da als Welt gegeben ist, eine «Vorstellung» sei, so müssen wir uns klar sein, daß es ja gar nicht möglich ist, eine solche Feststellung zu machen, ohne dasjenige, was wir unsere denkerische Tätigkeit nennen, ohne Ge­danken und Begriffe.",
        "Ich will jetzt nichts darüber sagen, daß eine solche Feststellung eigentlich formallogisch schon ein «Urteil» ist.",
        "In dem Augenblick, wo wir überhaupt beginnen, irgend etwas nicht so zu lassen, wie es vor uns auftritt, sondern ihm gegenüber eine Fest­stellung machen, greifen wir mit unserem Denken ein in die Welt, die um uns herum ist.",
        "Und wenn wir irgendein Recht haben sollen, so in die Welt einzugreifen, daß wir etwas als «subjektiv» bestimmen, dann müssen wir uns bewußt sein, daß dasjenige, was bestimmt, daß etwas «subjektiv» genannt wird, selber nicht subjektiv sein darf."
      ],
      [
        "Denn nehmen wir an, wir hätten hier die Sphäre der Subjektivität (es wird ein Kreis an die Tafel gezeichnet und darüber das Wort «Subjektivität» geschrieben) und es ginge von derselben aus zum Beispiel die Feststellung, A sei subjektiv, sei «meine Vorstellung» oder was auch immer, dann ist diese Feststellung selber subjektiv."
      ],
      [
        "# Bild s. 191"
      ],
      [
        "Die Folgerung daraus ist dann nicht etwa, daß wir diese Feststellung gelten lassen dürfen, sondern die Folgerung muß sein, daß ein solcher Schluß nicht gemacht werden darf, denn eine solche Feststellung würde sich selber aufheben.",
        "Wenn eine Subjektivität nur aus sich"
      ],
      [
        "selbst heraus festgestellt werden kann, so wäre das eine sich selbst aufhebende Feststellung.",
        "Wenn die Feststellung «A ist subjektiv» einen Sinn haben soll, so muß sie nicht ausgehen von der Sphäre der Subjektivität, sondern von einer Realität außerhalb der Subjektivität.",
        "Das heißt, wenn das «Ich» überhaupt in der Lage sein soll, sagen zu dürfen, etwas trage einen subjektiven Charakter, zum Beispiel etwas sei «meine Vorstellung», wenn das «Ich» das Recht dazu haben soll, etwas als subjektiv zu bezeichnen, dann darf es nicht selber innerhalb der Sphäre der Subjektivität sein, sondern es muß diese Feststellung von außerhalb der Sphäre der Subjektivität machen.",
        "Wir dürfen also die Feststellung, daß etwas subjektiv sei, nicht zurückleiten auf das Ich, das selber subjektiv ist.*)"
      ],
      [
        "Damit ergibt sich aber ein Ausweg aus der Sphäre der Subjektivität heraus, indem wir uns klar darüber werden, daß wir keine Feststel­lung darüber machen könnten, was subjektiv und was objektiv ist, und schon die allerersten Schritte des Denkens darüber überhaupt unterlassen müßten, wenn wir nicht zu Subjektivität und Objektivi­tät in einer solchen Beziehung stünden, daß beides gleichen Anteil an uns hat.",
        "Das führt uns dazu, anzuerkennen - was ich jetzt nicht weiter ausführen kann -, daß unser Ich nicht nur subjektiv genom­men werden darf, sondern umfassender ist als unsere Subjektivität.",
        "Wir haben ein Recht dazu, aus einem gewissen gegebenen Inhalte, also aus etwas Objektivem, dasjenige abzugrenzen, was subjektiv ist."
      ],
      [
        "Es treten uns zunächst die verschiedenen Begriffe «objektiv», «subjektiv» und «transsubjektiv» entgegen.",
        "«Objektiv» ist selbstver­ständlich etwas anderes als «transsubjektiv» [Lücke in den Nach-schriften]."
      ],
      [
        "Nun handelt es sich darum - wenn wir diese Voraussetzungen gemacht haben -, ob wir in der Lage sind, den Stein des Anstoßes wegzuräumen, der zu den wichtigsten Hemmnissen in der Erkennt­nistheorie gehört, nämlich die Frage, ob innerhalb der Subjektivität der ganze Umfang unseres Ich gefunden werden kann oder nicht.",
        "Denn wenn das Ich auch an der Objektivität teilhaftig sein muß,"
      ],
      [
        "*) siehe Hinweis auf Seite 214"
      ],
      [
        "gewinnt die Frage «Kann etwas in die Sphäre der Subjektivität her­einkommen?» eine ganz andere Gestalt.",
        "Sobald man das Ich als an der Sphäre der Objektivität teilhaftig bezeichnen darf, muß das Ich in sich gleichartige Qualitäten haben wie das Objektive; es muß etwas von der Sphäre der Objektivität auch im Ich zu finden sein.",
        "Mit anderen Worten: Wir dürfen jetzt eine Beziehung zwischen Objekti­vem und Subjektivem voraussetzen, die wesentlich abweicht von der Auffassung, daß nichts vom Transsubjektiven zum Subjektiven hin­überkommen könne."
      ],
      [
        "Wenn man sagt, daß nichts zum Subjektiven hinüberkommen kann, dann hat man erstens das Subjektive erkenntnistheoretisch als in sich abgeschlossen bestimmt, und zweitens hat man dabei einen Begriff verwendet, der nur für eine gewisse Sphäre der Realität Berechtigung hat, nicht aber für den ganzen Umfang der Realität Geltung haben kann.",
        "Das ist der Begriff des «Ding an sich».",
        "Dieser Begriff spielt bei vielen Erkenntnistheoretikern eine große Rolle; er ist wie ein Netz, in welchem sich das philosophische Denken selber fängt.",
        "Man merkt aber dabei gar nicht, daß dieser Begriff nur für eine gewisse Sphäre der Realität gilt und daß er aufhört Geltung zu haben, wo diese Sphäre aufhört."
      ],
      [
        "Im Materiellen zum Beispiel hat der Begriff Geltung.",
        "Ich möchte erinnern an das Beispiel vom Petschaft und Siegellack.",
        "Wenn Sie ein Petschaft nehmen, auf dem der Name «Müller» steht, und Sie drük­ken es in heißen Siegellack, dann können Sie mit Recht sagen: Es kann nichts von der Materie des Petschaft herüberkommen in den Siegellack. - Da haben Sie etwas, wo das Nicht-herüberkommen-Können gilt.",
        "Mit dem Namen «Müller» aber ist das anders, der kann restlos hinüberfließen in den Siegellack.",
        "Und wenn der Lack selbst sprechen könnte und betonen wollte, daß nichts von der Materie des Petschaft in ihn hineingeflossen ist, so müßte er doch zugeben, daß das, worauf es ankommt, nämlich der Name «Müller», restlos her­übergekommen ist.",
        "Da haben wir also die Sphäre überschritten, wo der Begriff des «Ding an sich» eine Berechtigung hatte."
      ],
      [
        "Woher ist es denn gekommen, daß dieser Begriff, der in einer gewissen feineren Weise bei Kant, ziemlich grobklotzig bei Schopenhauer,"
      ],
      [
        "dann aber scharfsinnig beschrieben bei den verschiedensten Erkenntnistheoretikern des 19.",
        "Jahrhunderts auftritt, eine solche Bedeutung hat gewinnen können?"
      ],
      [
        "Es ist, wenn man auf die ganze Sache näher eingeht, daher gekom­men, daß das, was die Menschen in Begriffen ausarbeiten, doch von der ganzen Art ihres Denkens abhängt.",
        "Nur in einem Zeitalter, in welchem alle Begriffe so charakterisiert werden müssen, daß sie immer an der äußeren Wahrnehmung gebildet sind, hat sich ein solcher Begriff wie der des «Ding an sich» bilden können."
      ],
      [
        "Die nur an der äußeren Wahrnehmung gewonnenen Begriffe sind aber nicht geeignet zur Charakterisierung des Geistigen.",
        "Würde man nicht einen solchen verkappten, man möchte sagen, gründlich mas­kierten Materialismus in die Erkenntnistheorie eingeschleppt haben -denn das ist das Faktum, worauf es ankommt: es ist ein wirklich nicht leicht zu erkennender Materialismus in die Erkenntnistheorie einge­schleppt worden -, so würde man sich darüber klar sein, daß eine Er­kenntnistheorie, die für die geistigen Gebiete gelten soll, auch solche Begriffe haben muß, die nicht in diesem groben Stile gebildet sind wie der Begriff des «Ding an sich».",
        "Für das Geistige, wo überhaupt von einem Draußen und Drinnen nicht in demselben Sinne gesprochen werden kann, muß es klar sein, daß wir feinere Begriffe brauchen."
      ],
      [
        "Ich konnte das nur skizzenhaft andeuten, denn ich müßte sonst ein ganzes Buch schreiben, das sehr dick werden würde und auch meh­rere Bände haben müßte, weil an die Philosophiegeschichte und an die Erkenntnistheorie sich auch metaphysische Gebiete anschließen müßten.",
        "Aber Sie können daran sehen, daß es ganz begreiflich ist, wenn diese Art des Denkens, weil sie aus tief maskierten Vorurteilen entspringt, unbrauchbar ist für alles das, was in die geistige Welt hineinreicht."
      ],
      [
        "Ich habe Ihnen jetzt eine Stunde lang nur über diesen allerabstrak­testen Begriff gesprochen.",
        "Ich habe mich bemüht, die Sache verständ­lich zu machen und bin mir absolut klar darüber, daß die Einwände, die mir selber deutlich vor der Seele stehen, selbstverständlich in mancher anderen Seele auch auftauchen können.",
        "Wenn es sich um eine andere Versammlung handelte, so bedürfte es vielleicht einer"
      ],
      [
        "besonderen Rechtfertigung, daß man, man könnte sagen, seine Zuhö­rer so hintergeht, daß man statt des gewohnten Tatsachenmaterials, das erwartet wird, einmal auch in abstraktesten - wie wohl manche glauben: vertracktesten - Begriffen spricht.",
        "Nun, wir haben schon im Laufe unserer theosophischen Arbeit immer wieder gesehen, daß Theosophie auch das Gute hat, daß man innerhalb der theosophi­schen Bewegung die Pflicht zur Erkenntnis ausbildet, und daß damit nach und nach ein unartiger Begriff überwunden wird, der überall sonst existiert, ein sehr unartiger Begriff, welcher sagt: Das ist ja doch etwas, was über meinen Horizont geht, womit ich mich nicht beschäftigen will, was mir nicht interessant ist!"
      ],
      [
        "Für manchen, der sich mit philosophischen Grundfragen beschäf­tigt und der die manchmal nur spärlich besuchten Kollegien über Erkenntnistheorie aus Erfahrung kennt, mag es überraschend sein, daß hier in unserer Bewegung so viele Menschen, die doch nach dem Urteil dieses oder jenes Erkenntnistheoretikers «gründlichste Dilet­tanten» auf dem Gebiete der Erkenntnistheorie sind, zu einer Ver­sammlung kommen, um sich ein solches Thema anzuhören.",
        "Wir haben an manchen Orten sogar eine noch größere Anzahl von Zuhö­rern gerade bei philosophischen Vorträgen gehabt, die zwischen die theosophischen eingelegt worden sind."
      ],
      [
        "Wenn man die Sachlage aber gründlicher betrachtet, wird man sagen dürfen, daß dies gerade eines der besten Zeugnisse für die Theosophen ist.",
        "Die Theosophen wis­sen, daß sie alles unbefangen anhören sollen, was an Einwänden vorgebracht werden kann."
      ],
      [
        "Sie sind ruhig dabei, denn sie wissen ganz genau, daß Einwände gegen die Forschungen in den übersinnlichen Welten zwar möglich und berechtigt sind, sie wissen aber auch, daß manches, was zunächst als unlogisch bezeichnet worden ist, sich schließlich doch als sehr logisch herausstellen kann.",
        "Der Theosoph lernt auch, es als seine Pflicht zu betrachten, Erkenntnisse in seine Seele hineinzubekommen, wenn es ihm auch Mühe macht, sich mit Erkenntnistheorie und Logik zu beschäftigen."
      ],
      [
        "Denn so wird er immer mehr und mehr in der Lage sein, nicht nur allgemeine theoso­phische Darstellungen anhören zu wollen, sondern auch mit logi­schen Begriffen und Begriffsgliederungen ernst in der Theosophie zu"
      ],
      [
        "arbeiten.",
        "Es wird sich die Welt schon mit dem Gedanken bekanntma­chen müssen, daß die Philosophie in ihrem umfänglichsten Sinne innerhalb der theosophischen Bewegung wird wiedergeboren werden können.",
        "Eifer für philosophische Strenge, für gründliche logische Begriffsbildung wird sich nach und nach, wenn ich das Wort gebrau­chen darf, einnisten innerhalb der theosophischen Bewegung.",
        "Womit ich nicht gesagt haben will, daß die Resultate in dieser Beziehung bei genauem Zusehen jetzt schon sehr befriedigend sind.",
        "Wir werden das durchaus noch mit Bescheidenheit ansehen müssen, aber wir sind auf dem Wege zu diesem Ziel."
      ],
      [
        "Je mehr wir uns den guten Willen zum Denkerischen, zur wissen­schaftlichen Gewissenhaftigkeit, zur philosophischen Gründlichkeit aneignen, desto mehr werden wir durch die theosophische Arbeit nicht nur unsere vergänglichen persönlichen Ziele verfolgen, sondern menschheitliche Ziele erreichen können.",
        "Manches ist heute erst auf der Stufe des allerersten Wollens."
      ],
      [
        "Aber es zeigt sich, daß in dem Willen, der aufgewendet wird zur Erkenntnis, schon etwas liegt wie eine ethische Selbsterziehung, die erreicht wird durch das Interesse, das wir der Theosophie entgegenbringen.",
        "Und daran wird es bald nicht mehr mangeln."
      ],
      [
        "Wenn keine anderen Hindernisse sich finden als die, welche es heute schon gibt, so wird von der Außenwelt der Theosophie die Anerkennung nicht versagt werden können, daß der Theosoph nicht strebt nach leichter Befriedigung seiner seelischen Sehnsuchten, sondern daß sich in der Theosophie ein ernstes Streben nach philosophischer Gründlichkeit und Gewissenhaftigkeit kund-gibt, nicht ein bloßer Dilettantismus.",
        "Dieses Streben wird gerade geeignet sein, das philosophische Gewissen der Menschen zu schär­fen."
      ],
      [
        "Wenn wir die theosophischen Lehren nicht als Dogmen hinneh­men, sondern verstehen, was Theosophie als reale Macht in unserer Seele sein kann, dann kann das Anfeuerungsmaterial für die mensch­liche Seele sein, um immer mehr und mehr die in ihr verborgenen Kräfte zu ergreifen und um sie zum Bewußtsein ihrer Bestimmung zu führen.",
        "Deshalb wollen wir innerhalb unserer theosophischen Bewe­gungen fördern diesen Eifer für gründliche Logik und Erkenntnis­theorie, und so, indem wir fester auf dem Boden unserer physischen"
      ],
      [
        "Welt stehen, immer klarer und ohne Schwärmerei und nebulose Mystik aufschauen lernen zu den geistigen Welten, deren Inhalt wir herunterholen und einfügen wollen in unser physisches Weltbild."
      ],
      [
        "Ob wir das tun wollen, davon hängt es einzig und allein ab, ob wir der Theosophie eine wirkliche Mission im Erdendasein der Mensch­heit zuschreiben können."
      ],
      [
        "# Bild s. 200"
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Zu dieser Ausgabe",
      "Die in diesem Band enthaltenen Vorträge hielt Rudolf Steiner im Jahr 1911 auf Einladung von Prager Theosophen.",
      "In Prag - das damals als Hauptstadt des Königreiches Böhmen zur Österrei­chisch-Ungarischen Monarchie gehörte - gab es in diesen Jahren vor dem ersten Weltkrieg drei verschiedene theosophische Gruppierungen. Neben der «Böhmi­schen Sektion Prag der Theosophischen Gesellschaft (Adyar)» hatte sich eine Gruppe von Tschechen unter der Leitung von Jan Bedrnicek schon seit dem Jahr 1906 direkt an den von Rudolf Steiner geleiteten Besant-Zweig in Berlin ange­schlossen; sie führte offiziell den Namen «Abteilung Prag des Besant-Zweiges, Berlin». Außerdem gab es eine unabhängige theosophische Arbeitsgruppe etwa seit 1909, die «Bolzano-Gruppe», die sich im Jahr 1912 als «Bolzano-Zweig» ebenfalls der Deutschen Sektion und später der Anthroposophischen Gesell­schaft anschloß. Die Leiterin dieser Gruppe war Berta Fanta.",
      "Die Initiative, Rudolf Steiner zu einem Vortragszyklus nach Prag zu bitten, ging von der tschechischen Gruppe aus. Am 25. Mai 1910 fuhr deren Leiter Jan Bedrnicek nach Hamburg, um mit Rudolf Steiner, der dort die Vortragsreihe über «Die Offenbarungen des Karma» hielt, Termin und Themen zu besprechen. Zwischen den verschiedenen theosophischen Gruppierungen hat es damals eine gute Zusammenarbeit gegeben. So trat als offizieller Veranstalter von Rudolf Steiners Vorträgen die «Böhmische Sektion» auf, die die Einladungen verschickte (siehe Seite 200) und die Vorträge im «Prager Tagblatt» Nr.74 vom 15. März 1911 mit folgender Anzeige ankündigte:",
      "Die Theosopbische Gesellschaft in Prag veranstaltet im laufenden Monate einen öffentlichen Vortragszyklus, gehalten von dem hervorragenden Philo­sophen und Okkultisten Dr. Rudolf Steiner über «okkulte Physiologie> und zwar vom 19. bis 28. März (präzise 8 Uhr abends) im Saale des kaufmänni­schen Vereins «Merkur», Niklasstraße. Anmeldungen an das Sekretariat der Sektion Prag, Weinberge, Bocelgasse 2, 2. St.",
      "Das Thema «Eine okkulte Physiologie» geht mit Sicherheit auf Rudolf Steiner selbst zurück, hatte er sich doch schon seit Jahren mit einer okkulten Betrach­tung des menschlichen Organismus beschäftigt. So sagte er zum Beispiel in einem Vortrag, der anläßlich der 5. Generalversammlung der Deutschen Sektion der Theosophischen Gesellschaft gehalten wurde (Berlin, 21. Oktober 1907 vormittags, in GA 101):",
      "«Es ist... möglich, die Organe des Menschen zu studieren in ihrer verschiede­nen Wertigkeit, wenn man zurückgeht auf die Urgründe, die in den geistigen Welten zu finden sind. Wir finden, daß Leber, Galle, Milz und so weiter etwas",
      "ganz anderes sind, wenn man weiß, wie verschiedene Welten an ihrer Gestal­tung beteiligt sind. ... Sie sind Erbteile aus der geistigen Welt heraus. Es müssen alle Organe beim Menschen aus ihren geistigen Ursprüngen heraus von uns betrachtet werden, wenn wir deren Bedeutung richtig verstehen wollen. Da sehen wir hin auf eine zukünftige Behandlungsweise des menschli­chen Leibes, wo man sich dieses geistigen Ursprunges der Organe bewußt sein wird und diese Erkenntnisse anwenden wird in der alltäglichen Medizin.»",
      "und in München - nachdem das Thema für den Prager Zyklus schon feststand -am 26. August 1910 (in GA 125):",
      "»Es wäre im Sinne dessen, was ich selbst als geisteswissenschaftliche Bewe­gung ansehen muß, mein dringendster Wunsch, daß diejenigen, welche eine physiologisch-ärztliche Vorbildung haben, sich so weit mit den Tatsachen der Geisteswissenschaft bekanntmachen, daß sie in bezug auf ihren Tatsachencha­rakter die Ergebnisse der Physiologie einmal durcharbeiten können. Ich werde selbst im nächsten Frühjahr nur höchstens die Grundlinien dieser geisteswis­senschaftlichen Physiologie ziehen können...»",
      "Über die Teilnehmer an dem Prager Vortragszyklus ist nur wenig bekannt; insbesondere konnte bisher nicht herausgefunden werden, welche Ärzte teilge­nommen haben. Nur einige wenige Namen sind dokumentarisch gesichert: Dr. Ludwig Noll aus Kassel, der während dieser Zeit die erkrankte Marie von Sivers behandelte (siehe «Marie Steiner-von Sivers - Ein Leben für die Anthroposo­phie», Seite 201ff.), sowie die drei Münchner Ärzte Dr. Felix Peipers - der selbst in theosophischen Zusammenhängen schon Vorträge gehalten hatte über okkulte Anatomie und Medizin -, Dr. Max Hermann und Dr. Hanns Rascher.",
      "Ein Wiener Mitglied berichtet:",
      "«Ein finanziell glücklicher Zufall machte es mir damals möglich, verspätet zu dem Vortragszyklus Dr. Steiners über okkulte Physiologie nach Prag zu fahren. Die Vorträge, denen ein großer Teil der Prager Intelligenzkreise beiwohnen konnte, gaben den ersten Ausblick in eine neue Betrachtungsweise des Menschen. Die Stimmung dieses Neuen herrschte namentlich unter den anthroposophischen Wissenschaftlern und Ärzten (darunter Dr. Peipers und Dr. Hermann). An den öffentlichen Vorträgen «Wie widerlegt man Theoso­phie?» und «Wie verteidigt man Theosophie» nahmen auch viele Menschen der Zionistischen Bewegung teil und ich kam bei dieser Gelegenheit in nahen Kontakt zu dem jungen Philosophen Hugo Bergmann (jetzt Professor in Jerusalem), dessen Schwiegermutter und Tante (Frau Fanta und Frau Freund) im Mittelpunkt der theosophischen Bewegung in Prag standen. ... Die Tage von Prag, an denen fast alle Wiener Theosophen teilnahmen, bekamen noch ihren besonderen Glanz durch den Eindruck einer in der Einheit des theoso­phischen Strehens gegründeten echten Verbindung zwischen Deutschen und Tschechen. Dies gab eine innere Wärme, in der auch Dr. Steiner sich beson­ders wohl zu fühlen schien. Unter den tschechischen Theosophen fiel besonders",
      "ein greiser Musikprofessor auf, dessen Äußeres stark an Leo Tolstoi erinnerte.» (Aus einem undatierten Manuskript «Erinnerungen» von Dr. Ernst Müller, Wien.)",
      "Am Schluß der Veranstaltungen fand noch ein ursprünglich im Programm nicht vorgesehener Vortrag Rudolf Steiners statt über die Beziehung der Theoso­phie zur Philosophie. Dieser Vortrag liegt bereits gedruckt vor im Band der Gesamtausgabe «Die Mission der neuen Geistesoffenbarung», GA 127, wird aber wegen seiner direkten Beziehung zu den Vorträgen über okkulte Physiolo­gie in den hier vorliegenden Band mit aufgenommen. Die beiden öffentlichen Vorträge vom 19. und 25. März 1911 «Wie widerlegt man Theosophie?» und «Wie verteidigt man Theosophie?» sind in der Gesamtausgabe noch nicht erschienen, sie waren - nach einer mangelhaften Nachschrift - abgedruckt in «Mensch und Welt», Blätter für Anthroposophie 1968, Nrn. 1-4.",
      "Zu der Zeit, als Rudolf Steiner diese Vorträge hielt, stand er mit seiner Geisteswissenschaft noch innerhalb der Theosophischen Gesellschaft. Er ver­wendete die Worte «Theosophie» und «theosophisch» jedoch immer im Sinne seiner später «Anthroposophie» genannten Geisteswissenschaft. Die Ausdrücke «Theosophie», «Geisteswissenschaft» oder «Geistesforschung» sind hier jeweils so wiedergegeben, wie sie von den Stenographen festgehalten wurden.",
      "Der Titel des Vortragszyklus ist von Ruddolf Steiner.",
      "Die Zeichnungen im Text wurden von Hedwig Frey und Leonore Uhlig nach den Skizzen der Stenographen ausgeführt. Originaltafelzeichnungen sind nicht erhalten.",
      "Textunterla gen: Eine wortwörtliche stenographische Mitschrift dieser Prager Vorträge Rudolf Steiners gibt es nicht. Wohl haben verschiedene Teilnehmer mitgeschrieben, doch reichten ihre stenographischen Fähigkeiten nicht aus, um einen ganzen Vortrag durchgehend wörtlich festhalten zu können.",
      "Von den vorliegenden Unterlagen - es sind insgesamt neun verschiedene Textfassungen - sind acht sogenannte Ausarbeitungen (die neunte besteht nur aus stichwortartigen Notizen), das heißt, sie geben nicht nur die ursprünglich stenographisch oder handschriftlich festgehaltenen Wortlaute wieder, sondern sie sind von den jeweiligen Schreibern mehr oder weniger bearbeitet worden (stilistisch zu einem lesbaren Text formuliert, Interpunktion eingefügt, gelegent­lich inhaltlich ergänzt, Lücken nach eigenem Verständnis oder Gedächtnis aus­gefüllt und anders mehr). Da sich keinerlei Originalstenogramme erhalten haben, ist es schwierig, den Grad der «Bearbeitung» im einzelnen festzustellen. Deshalb wurden bei den Vorarbeiten für die Neuausgabe 1991 zunächst alle vorliegenden Textfassungen Satz für Satz miteinander verglichen, woraus sich folgendes Bild ergibt:",
      "Vier Stenographen (Walter Vegelahn, Fritz Mitscher, Wilhelm Friedrich und ein unbekannter) haben sich bemüht - entsprechend ihren individuellen Fähig­keiten -, die Vorträge weitgehend wörtlich mitzuschreiben. Ihre Klartextübertragungen",
      "wurden in unterschiedlicher Weise und zum Teil mehrmals bearbeitet und zwar von den Nachsehreibern selbst. Die übrigen Nachschriften sind Zusammenfassungen der Vortragsinhalte. Im einzelnen liegen vor:",
      "-    Nachsehrift Walter Vegelahn in zwei stark voneinander abweichenden",
      "a)    Erstübertragung des Stenogramms, geringfügig bearbeitet (maschine-geschrieben)",
      "b)    von Vegelahn selbst überarbeitete Fassung von a), durch dessen eigene Einfügungen oft stark verändert (maschinegeschrieben)",
      "-    Nachsehrift Fritz Mitscher in zwei Fassungen:",
      "a)    Erstübertragung des Stenogramms (handschriftlich)",
      "b)    bearbeitete Fassung, zum Teil unter Berücksichtigung des Vegelahn­textes (maschinegeschrieben)",
      "-    Nachschrift Wilhelm Friedrich (handschriftliche Übertragung des Steno­grammtextes)",
      "-    Nachschrift eines unbekannten Stenographen (handschriftlich)",
      "-    Kurznachschrift (referatartig) von Jan van Leer (maschinegeschrieben)",
      "-    Kurznachschrift (referatartig) von Fritz Rascher (maschinegeschrieben)",
      "-    Kurznotizen von unbekannter Hand (handschriftlich).",
      "Als offizieller Stenograph war der Berliner Walter Vegelahn, der schon mehr­jährige Etfahrungen im Mitschreiben von Vorträgen hatte, mit nach Prag gereist. Jedoch gelang es ihm diesmal nicht - aus welchen Gründen auch immer -, die Vorträge wirklich wörtlich mitzuschreiben. Vielleicht waren ihm die Thematik und das Vokabular ungewohnt, vielleicht waren die räumlichen oder akustischen Verhältnisse ungünstig, vielleicht lag auch eine persönliche Indisposition vor - all das läßt sich heute nicht mehr feststellen. Das Ergebnis seiner Mitschrift, die Übertragung des Stenogramms, war jedenfalls sehr unbefriedigend.",
      "Am 2. Mai 1911 schrieb Marie von Sivers aus Portorose, wo sie und Rudolf Steiner sich damals aufhielten, an die Leiterin des Philosophisch-Theosophischen Verlages, Johanna Mücke: «Der Doktor möchte doch gern alle Vorträge über Vegelahn, der sich über die Mangelhaftigkeit seiner Nachschriften wohl selbst klar war, hat diese später noch einmal überarbeitet und so eine zweite Textfas­sung erstellt, die sich von der ersten dadurch unterscheidet, daß er dem Wortlaut seines ursprünglichen Stenogrammteztes alle möglichen Zutaten beifügte (Füll­worte, Wiederholungen vorangegangener Satzpassagen oder Gedankengänge, Nachahmung bestimmter Eigentümlichkeiten von Rudolf Steiners Sprechstil",
      "und so weiter). Die auf diese Weise entstandenen Satzkonstruktionen sind häufig so unklar gegliedert, daß ihr Sinn nur schwer verständlich ist. Solche Satzkon­struktionen stammen also nicht von Rudolf Steiner, sondern sind durch die nachträgliche Bearbeitung Vegelahns entstanden.",
      "Erst im Jahr 1927 wurden die Vorträge erstmals gedruckt und zwar als Manuskriptdruck für Mitglieder, bezeichnet als «Zyklus OP». Sowohl dieser Erstdruck wie auch die folgenden Auflagen innerhalb der Gesamtausgabe basier­ten auf der oben beschriebenen Textbearbeitung Vegelahns, können also nicht als die authentische Wiedergabe des Wortlautes Rudolf Steiners angesehen werden.",
      "«erfordert Theosophie ... das genaueste, präziseste logische Formulieren», so sagt Rudolf Steiner im Vortrag vom 28. März 1911 (siehe Seite 181/182), und nach Ausführungen über «Wortfüllsel» und «rhetorische Verbrämungen» fügt er hinzu: «Wenn man das Vorgetragene ganz genau nimmt, so darf man in den Sätzen nicht nur nichts ändern, sondern man muß auch genau auf die Grenze achten, die in die Formulierungen mit aufgenommen ist.» -Bald nach dem Erscheinen von «Zyklus OP» im Jahr 1927 meldeten sich eine",
      "Reihe von Arzten, die auf Fehler in den Texten aufmerksam machten und entsprechende Korrekturen vorschlugen. Für die späteren Auflagen 1957 und 1971 konnte der Herausgeber Dr. med. H. W Zbinden durch Prüfung der damals vorliegenden Nachschriften einige sachliche Korrekturen durchführen; die Vegelahnsche Textbearbeitung wurde dadurch jedoch nicht grundsätzlich in Frage gestellt. Die Tatsache, daß es sich bei dieser keineswegs um den originalen Wortlaut Rudolf Steiners handelt, konnte erst in jüngster Zeit festgestellt werden durch einen genauen Vergleich mit den anderen, auf Stenogramme zurückgehen-den Nachschriften. Einige dieser Unterlagen hat die Nachlaßverwaltung erst in den letzten Jahren erhalten.",
      "Trotz der zahfreichen Differenzen in den einzelnen Wortlauten der verschie­denen Nachschriften sind Inhalt, Aufbau und Verlauf der Vorträge von allen Nachschreibern gleich wiedergegeben. Diese Tatsache ermöglichte es, nunmehr für die Neuausgabe 1991 eine neue Textfassung zu erarbeiten, deren Grundlage die am wenigsten bearbeiteten Niederschriften der Stenographen sind:",
      "- die Erstausschriften von Walter Vegelahn und Fritz Mitscher, sowie die handschriftlichen Stenogrammübertragungen von Wilhelm Friedrich und von Unbekannt. Die Referate von van Leer und von Fritz Rascher wurden inhaltlich mit beigezogen. Auch diese verbesserte Textfassung enthält Unklares und Lük­kenhaftes, das mangels eines wortgetreuen Stenogrammes nicht rekonstruiert werden kann. Inhalt und Aufbau der Vorträge sind jedoch durch die zahlreichen Unterlagen gesichert.",
      "Hinweise zum Text",
      "Werke Rudolf Steiners innerhalb der Gesamtausgabe (GA) werden in den Hinweisen mit der Bibliographie-Nummer angegeben. Siehe auch die Übersicht am Schluß des Bandes.",
      "13    die geistige, übersinnliche Grundlage der Organe, der Lebensformen, der Lebensprozesse: In seiner Schrift «Anthroposophie - Ein Fragment aus dem Jahre 1910» (GA 45) gibt Rudolf Steiner im Kapitel IV «Die Lebensvor­gänge» eine Schilderung des Sinneslebens des Menschen im Verhältnis zu seinem inneren Leibesleben. Diese inneren Lebensvorgänge werden dort charakterisiert als Atmen, Wärmung, Ernährung, Absonderung, Erhaltung, Wachstum und Hervorbringung. Erweiterte und modifizierte Darstellungen finden sich in den Vorträgen vom 12. August 1916, enthalten im Band «Das Rätsel des Menschen» (GA 170), und vom 29. Oktober 1921, enthalten im Band «Anthroposophie als Kosmosophie - Zweiter Teil» (GA 208). Siehe hierzu auch in Heft Nr.58/59 der «Beiträge zur Rudolf Steiner Gesamtaus­gabe» die Aufzeichnungen Rudolf Steiners zu den Sinnesbereichen und Lebensstufen, mit einem Vorwort von Hendrik Knobel.",
      "16    was über die Bedeutung der Organe in bezug auf den Menschen gesagt wird, das kann nicht... in gleicher Weise für die Tiere gesagt werden: Ausführliche Darstellungen darüber gibt Rudolf Steiner u. a. in folgenden Berliner Vorträ­gen: «Menschenseele und Tierseele», «Menschengeist und Tiergeist», am 10. und 17. November 1910, beide enthalten im Band «Antworten der Geistes­wissenschaft auf die großen Fragen des Daseins« (GA 60), «Der Ursprung der Tierwelt im Lichte der Geisteswissenschaft» am 18. Januar 1912, enthal­ten im Band «Menschengeschichte im Lichte der Geistesforschung» (GA 61), »Menschenwelt und Tierwelt nach Ursprung und Entwickelung dargestellt im Lichte der Geisteswissenschaft» am 15. April 1918, enthalten im Band «Das Ewige in der Menschenseele» (GA 67), sowie am 28. Juli 1922 in Dornach, enthalten in dem Band «Das Geheimnis der Trinität» (GA 214).",
      "17    daß Goethe, ....... den Blick darauf gerichtet haben, daß die Schädelkno­chen gewisse Formähnlichkeiten haben mit den Wirbelknochen des Rückgra­tes: Lorenz Oken (1779-1851), Professor in Jena und München, ab 1832 in Zürich, veröffentlichte 1807 beim Antritt seiner Professur in Jena ein Pro­gramm: «Über die Bedeutung der Schädelknochen», in dem er die von Goethe 1790 entdeckte Wirbeltheorie als seine Entdeckung vortrug.",
      "Goethe hatte seine Wirbeltheorie des Schädels schon 1790 im Freundes-kreise vorgetragen, sie jedoch erst nach Oken veröffentlicht. Siehe hierzu in «Goethes naturwissenschaftliche Schriften», 5 Bände, herausgegeben und kommentiert von Rudolf Steiner in Kürschners «Deutsche National-Littera­tur», GA la-e, in Band 1 »Bildung und Umbildung organischer Naturen» die Aufsätze Goethes «Zwischenknochen», Abschnitt VIII, und «Das Schädelge­rüst aus sechs Wirbelknochen auferbaut», sowie die dazugehörigen Fußnoten Rudolf Steiners (a.a.O. Seite 316-323). Goethe schreibt dort: «... ein solches Gewahrwerden, Auffassen, Vorstellen, Begriff, Idee, wie man es nennen mag,",
      "behält immerfort, man gebärde sich, wie man will, eine esoterische Eigen-schaft; im ganzen läßt sich's aussprechen, aber nicht beweisen...» - und Rudolf Steiner in einer Fußnote dazu:",
      "«Eine solche ideelle Wahrheit kann und muß zunächst ganz allgemein, abgesehen von jedem einzelnen Falle, aufgefaßt werden. Daß sie sich als solche nun nicht beweisen läßt, hat seinen guten Grund. Ein Beweis kann immer nur die Begründung irgend eines Satzes durch etwas anderes sein. Jene Wahrheit trägt aber ihre Gewähr in sich selbst, kann also nicht durch etwas anderes begründet werden. Dies zu erkennen, geht nun freilich jenen ab, welche glauben, allgemeine Wahrheiten seien nur abstrakte Sätze aus unzähli­gen Beobachtungen abgeleitet. Die Aufgabe der empirischen Wissenschaft kann nur sein, zu zeigen, wie sich eine allgemeine, ihre Gewähr in sich selbst tragende Wahrheit in ihrer Verwirklichung im Individuellen darstellt.»",
      "18    in unserem Gehirn ein dzfferenziertes Rückenmark: Ergänzende Ausführun­",
      "gen in bezug auf die kosmische Evolution des Hauptes, wenn man zurück­",
      "geht bis zur Mondenentwickelung, finden sich u. a. in folgenden Vorträgen:",
      "Am 20. Dezember 1914, enthalten im Band «Okkultes Lesen und okkultes",
      "Hören» (GA 156); am 26. und 27. November 1920, enthalten im Band «Die",
      "Brücke zwischen der Weltgeistigkeit und dem Physischen des Menschen»",
      "(GA 202); am 12. Januar 1924, enthalten im Band «Mysterienstätten des",
      "Mittelalters» (GA 233 a), sowie in den Vorträgen des Bandes «Die Sendung",
      "Michaels» (GA 194).",
      "Siehe: Rudolf Steiners Aufsatz «Goethes Naturanschauung gemäß den",
      "neuesten Veröffentlichungen des Goethe-Archivs» (heute enthalten in GA",
      "30), worin er über eine Tagebuchaufzeichnung Goethes aus dem Jahr 1790",
      "berichtet. «Das Hirn selbst ist nur ein großes Hauptganglion. Die Organisa­",
      "tion des Gehirns wird in jedem Ganglion wiederholt, so daß jedes Ganglion",
      "als ein Meines subordiniertes Gehirn anzusehen ist.»",
      "25    die menschliche Aura: Ausführlich dargestellt in Rudolf Steiners «Theoso­",
      "phie» (GA 9), im Kapitel «Von den Gedankenforsien und der menschlichen",
      "Aura», sowie in dem Aufsatz «Von der Aura des Menschen», enthalten im",
      "Band «Lucifer - Gnosis. Grundlegende Aufsätze zur Anthroposophie» (GA",
      "30    ,ogenanntes blaues Blut: Die populäre Vereinfachung, das venöse Blut als",
      "«blau» und das arterielle Blut als »rot» zu bezeichnen, läßt sich nicht auf den",
      "Lungenkreislauf anwenden: hier führen die vom Herzen zur Lunge gehenden",
      "Arterien «blaues» Blut, die von der Lunge zum Herzen führenden Arterien",
      "dagegen «rotes» Blut. Über die Besonderheiten des Lungenkreislaufes sagt",
      "Rudolf Steiner am 26. Mai 1922 (in «Menschliches Seelenleben und Geistes-",
      "streben» (GA 212): «Das Ich... schlüpft in die Organe der Lunge hinein; mit",
      "den Adern, die von der Lunge zum Herzen hineingehen, nähert sich das Ich",
      "immer mehr dem Herzen. Das Ich folgt immer mehr und mehr, ... innig",
      "verbunden mit dem Blutkreislauf, dem Wege dieses Blutkreislaufes. So",
      "daß... das Ich eingreift in dasjenige, was aus dem ZusammenscMuß des",
      "ätherischen und des astralischen Herzens gebildet worden ist.»",
      "Nebenströmung  ...., welche ins Gebirn führt: Gemeint sind die beiden Kopf-schlagadern.",
      "wie die äußere Wissenschaft von einer spekulativen Lebenskrafi gesprochen hat: Die Anschauung von der Lebenskraft, der «vis vitalis», welche bis über die Mitte des 19. Jahrhunderts verbreitet war, ist ein Produkt rein spekulati­ven Denkens; sein eigentliches Wesen, das «vitale Prinzip», ist unbekannt, unbegründbar und phänomenologisch nicht zu erfassen. Daß mit der Bezeichnung »Ätherleib» etwas ganz anderes gemeint ist als mit der »Lebens­kraft» der älteren Naturwissenschaft, schreibt Rudolf Steiner in seinem Buch »Theosophie» (GA 9) in einer Fußnote zum Kapitel «Das Wesen des Men­schen», in Abschnitt IV Leib, Seele und Geist. Ergänzendes u. a. in den Vorträgen vom 7. Februar 1918 in »Das Ewige in der Menschenseele» (GA 67) und vom 6. April 1921 in »Die befruchtende Wirkung der Anthroposo­phie auf die Fachwissenschaften» (GA 76).",
      "40    in dem Blutsystem ein Abbild des Ich... und in dem Nervensystem ein Abbild des Astralleibes: Siehe hierzu auch Rudolf Steiners Ausführungen im Vortrag vom 21. Oktober 1907 vormittags, enthalten im Band «Mythen und Sagen» (GA 101).",
      "52    was wir das sympathische Nervensystem nennen: Siehe hierzu: Dr. Rudolf Steiner / Dr. Ita Wegman «Grundlegendes für eine Erweiterung der Heil-kunst nach geisteswissenschaftlichen Erkenntnissen» (GA 27), Kapitel VI. Blut und Nerv. Man unterscheidet ein sympathisches und ein parasympathi­sches System und faßt beide als vegetatives bzw. autonomes Nervensystem zusammen. Es bestehen jedoch weniger anatomische als physiologische Unterscheidungsmerkmale. Der Ausdruck «parasympathisches Nervensy­stem» wurde erst im Jahr 1905 eingeführt, es findet in den Darstellungen Rudolf Steiners keine Erwähnung.",
      "Sonnengeflecht:    Das mächtigste Geflecht des Sympathikus wird als Plexus solaris bzw. Plexus coeliacus bezeichnet und befindet sich im Oberbauch. Ergänzende Ausführungen Rudolf Steiners über das Sonnengeflecht finden sich u. a. in folgenden Vorträgen: 26. September und 7. Oktober 1905 im Band »Grundelemente der Esoterik» (GA 93 a), und 8. Juni1912 im Band »Der Mensch im Lichte von Okkultismus, Theosophie und Philosophie»",
      "56    die mystische Versenkung: Ausführlich dargestellt in den Vorträgen vom März 1910 im Band «Makrokosmos und Mikrokosmos» (GA 119).",
      "daß alles, was im leidenschaftlichen Blute ist, mit bineingeprägt wird in das sympathische Nervensystem: Siehe hierzu Rudolf Steiners Vortrag vom 14. Januar 1917, enthalten im Band »Zeitgeschichtliche Betrachtungen - Zweiter Teil» (GA 174): «Das wirkliche Ich greift als bildsame Kraft durch das Sonnengeflecht in die ganze Organisation des Menschen ein. ... Da das Gangliensystem die ganze Zirkulation des Blutes mitbedingt, so widerspricht das auch nicht der Tatsache, daß das Ich im Blute seinen Ausdruck hat. ... Was nun als Gangliensystem, als Sonnengeflecht im Menschen lebt, iSt schon vor der Mondenentwickelung herübergekommen und stellt gewisser­maßen das Haus für das Ich dar.»",
      "57    wenn ich durch mein sympathisches Nervensystem hellsichtig werde: In späte-ren Jahren spricht Rudolf Steiner von «Bauchhellsehen». Siehe hierzu u. a. die Vorträge vom 27. März und vom 1. Mai 1915, beide enthalten im Band «Wege der geistigen Erkenntnis und der Erneuerung künstlerischer Weltan­schauung» (GA 161), vom 4. Januar 1915 (2. Teil des Vortrages), enthalten in «Kunst im Lichte der Mysterienweisheit» (GA 275), vom 15. Februar 1915 im Band »Die geistigen Hintergründe des ersten Weltkrieges» (GA 174 b), vom 2. März 1915 im Band »Menschenschicksale und Völkerschicksale» (GA 157).",
      "59    wenn wir den äußeren Rhythmus des Kosmos wiedererkennen im Blut­Pulsschlag: Der Frühlingsaufgangspunkt der Sonne - also der Punkt inner­halb des Tierkreises, an dem die Sonne zum Zeitpunkt der Tag- und Nacht­gleiche im Frühling aufgeht - bleibt bekanntlich nicht immer der gleiche, es verschiebt sich dieser Punkt vielmehr im Verlaufe von 72 Jahren um ein Grad. Der Zeitraum, in welchem die Sonne so den ganzen Tierkreis durch­läuft, beträgt etwa 25 920 Jahre. Man nennt dies ein Weltenjahr oder ein platonisches Jahr. - Der Mensch atmet innerhalb einer Minute normalerweise 18mal, das sind in einer Stunde 1080, in einem Tage = 25920 Atemzüge.",
      "25 920 Erdentage wiederum sind die durchschnittliche Lebensdauer des Men­schen, etwa 72 Jahre. Rudolf Steiner hat auf diese Zusammenhänge häufig aufmerksam gemacht, besonders ausführlich in den Vorträgen vom 28. Januar 1917 im Band «Zeitgeschichtliche Betrachtungen - Zweiter Teil» (GA 174), vom 13. Februar 1917 im Band «Bausteine zu einer Erkenntnis des Mysteriums von Golgatha» (GA 175) und vom 24. September 1924 im Band «Die Schöpfung der Welt und des Menschen» (GA 354).",
      "Es wäre nun... interessant zu sehen, ob die äußere Physiologie solche Dinge... bestätigen würde: Ein erster Versuch der experiementellen Bestäti­gung dieser Anschauungen wurde von Lilly Kolisko unternommen mit ihrer Arbeit «Milzfunktion und Plättchenfrage», Stuttgart 1922. In späteren Kur­sen für Ärzte hat Rudolf Steiner wiederholt auf diese Arbeit hingewiesen.",
      "64    Daß ein System sich abschließt: Vom kosmologischen Aspekt aus hat Rudolf",
      "Steiner auf diese Probleme hingewiesen in den Vorträgen «Die Evolution",
      "vom Gesichtspunkt des Wahrhaftigen» (GA 132), ergänzend zu dem in dem",
      "Buch «Die Geheimwissenschaft im Umriß» (GA 13) Dargestellten.",
      "66    enthalten Mythen und Sagen wirkliche Weisheiten über das menschliche Wesen, wirkliche Physiologie: Siehe hierzu die Vorträge vom Oktober 1907 im Band «Mythen und Sagen» (GA 101).",
      "Namen wie Kain und Abel: Siehe hierzu die Vorträge vom 27. März 1913",
      "enthalten im Band «Welche Bedeutung hat die okkulte Entwickelung des",
      "Menschen für seine Hüllen und sein Selbst?» (GA 145) sowie vom 10. Juni",
      "1904 im Band »Die Tempellegende und die Goldene Legende» (GA 93).",
      "Wie haben wir es heute so herrlich weit gebracht!: Nach Goethes «Faust«, I. Teil, Nacht (Zeile 573): Und wie wirs dann zuletzt so herrlich weit gebracht.",
      "67    in den Namen der Mythen und Sagen erst einen Sinn finden, wenn sie darin die Physiologie erkennen: Siehe Hinweise zu Seite 66. Anhand der griechi­schen Mythologie wurde dies dargelegt in den Vorträgen vom August 1911 in dem Band «Weltenwunder, Seelenprüfungen und Geistesoffenbarungen»",
      "68    in dem ersten öffentlichen Vortrage: «Wie widerlegt man Theosophie?», Vortrag vom 19. März 1911, in der Gesamtausgabe noch nicbt erschienen, nach einer mangelhaften Nachschrift abgedruckt in «Mensch und Welt. Blätter für Anthroposophie» 1968, Nr.1-2.",
      "80    Während wir durch den Atmungsprozeß die Außenwelt stofflich aufnehmen, nehmen wir im Wahrnehmungsprozeß... etwas durch einen vergeistigten Atmungsprozeß in unseren Organismen auf Ergänzende Gesichtspunkte hierzu gibt R. Steiner u. a. in folgenden Vorträgen: Am 16. April 1921, im Band »Geisteswissenschaftliche Gesichtspunkte zur Therapie» (GA 313):",
      "»Das Sinneswahrnehmen ist nichts anderes als ein verfeinerter, das heißt ein ins Ätherische hineingetriebener Atmungsprozeß.» - Am 21. Juli 1924, im Band «Anthroposophische Menschenerkenntnis und Medizin» (GA 319):",
      "«So haben wir also in der Atmung gegeben einen gröberen Prozeß, wo der eingeatmete Sauerstoff sich mit dem Kohlenstoff unseres Organismus verbin­det und als Kohlensäure ausgeatmet wird. Daneben haben wir einen feineren Prozeß, wo sich der Sauerstoff mit dem Silizium zu Kieselsäure verbindet und als solche in die menschliche Organisation hinein abgesondert wird.» -Am 28. August 1924 in dem gleichen Band: «Diese Kieselsäure ist das äußerliche Korrelat, die Wirksamkeit nach außen für die Ich-Organisation. Astralischer Leib: das innerlich Spirituelle; Kohlensäureprozeß: das äußer­liche Physische...».",
      "82    Denen stehen andere [Weltanschauungen] gegenüber» die materialistischen:",
      "Carl Vogt, 1817-1895: «Physiologische Briefe für Gebildete aller Stände» (1845, Seite 206): »Ein jeder Naturforscher wird wohl denke ich bei einiger­maßen folgerichtigem Denken auf die Ansicht kommen, daß alle jene Fähig­keiten, die wir unter dem Namen der Seelentätigkeiten begreifen, nur Funk­tionen der Gehirnsubstanz sind; oder, um mich einigermaßen grob hier auszudrücken: daß die Gedanken in demselben Verhältnis etwa zu dem Gehirn stehen, wie die Galle zu der Leber oder der Urin zu den Nieren. Eine Seele anzunehmen, die sich des Gehirns wie eines Instrumentes bedient, mit dem sie arbeiten kann, wie es ihr gefällt, ist reiner Unsinn.»",
      "Jacob Moleschott, 1822-1893. In «Der Kreislauf des Lebens» (1852, Seite",
      "402) schließt sich dieser der Ansicht Carl Vogts an: «Der Vergleich ist",
      "unangreifbar, wenn man versteht, wohin Vogt den Vergleichspunkt verlegt.",
      "Das Gehirn ist zur Erzeugung der Gedanken ebenso unerläßlich, wie die",
      "Leber zur Bereitung der Galle und die Niere zur Abscheidung des Harns.» Demgegenüber sagt Rudolf Steiner im Vortrag vom 30. Januar 1921,",
      "enthalten im Band »Die Verantwortung des Menschen für die Weltentwicke­lung» (GA 203): »Es ist ein Unsinn, denn das Umgekehrte ist richtig, daß nämlich von den Gedanken das Gehirn abgeschieden wird, natürlich immer",
      "neu abgeschieden wird, weil es immer wiederum vom Stoffwechselorganis­mus aus ersetzt wird.»",
      "82    Psychophysischer Parallelismus: Eine 1860 von Gustav Theodor Fechner",
      "(1801-1887) begründete psychologische Teilwissenschaft, nach der Leib und",
      "Seele als zwei getrennte. doch einander korrespondierende Erscheinungen",
      "zusammenhängen.",
      "83    Es sind Seelenübun gen notwendig, um den Menschen in die übersinnliche Welt hineinzuführen: Siehe «Wie erlangt man Erkenntnisse der höheren Welten» (GA 10) und «Die Geheimwissenschaft im Umriß» (GA 13), Kapitel «Zur Erlangung übersinnlicher Erkenntnisse».",
      "85    überall im Ätherleibe Strömungen sich entwickeln: Ergänzendes hierzu u. a. im Vortrag vom 25. August 1911, enthalten in «Weltenwunder, Seelenprü­fungen und Geistesoffenbarungen» (GA 129) und vom I. Oktober 1911 »Die Ätherisation des Blutes», enthalten in «Das esoterische Christentum und die geistige Führung der Menschheit» (GA 130).",
      "wurde die Milz zu allen Zeiten in der okkulten Literatur... immer als ein besonders geistiges Organ angesehen und geschildert: Z.B. in H.P Blavat­skys «Geheimlehre».",
      "107    daß das Außenleben und das Innenleben des Menschen... in einem Gegen­",
      "satz zueinander stehen und... in Spannungen zum Ausdruck kommt ... in",
      "den Organen des Gehirnes, die wir als Zirbeldrüse und Gehirnanhang",
      "bezeichnen: Die Zirbeldrüse (Corpus pineale, Glandula pinealis, Epiphysis",
      "cerebri) ist schon beim Embryo mit 12 Wochen deutlich zu identifizieren.",
      "Die in ihr stattfindenden Mineralisierungsprozesse sind mit Beginn der",
      "Pubertät so weit vorgeschritten, daß sich der sogenannte «Himsand» nach­",
      "weisen läßt, der biochemisch aus Kalk- und Magnesiumsalzen besteht. Die",
      "Epiphyse ist stark von Fasern des sympathischen Nervensystems durchdrun­",
      "gen und ist stark durchblutet. Eine intensive wissenschaftliche Erforschung",
      "der Zirbeldrüse setzte etwa 1959 ein; übereinstimmend wurde eine Abhän­",
      "gigkeit von Lichtverhältnissen und eine Tages- und jahreszeitliche Rhythmik",
      "des Organs festgestellt.",
      "Die Hirnanhangdrüse (Hypophyse, Glandula Pituitaria - Schleimdrüse) ist",
      "ein an der Hirnbasis in den Türkensattel des Keilbeins eingelagertes inkreto­",
      "risches Organ, welches im wesentlichen die Funktionen der übrigen Hor­",
      "mondrüsen des Körpers reguliert. Sie hat die Größe einer Haselnuß. Es lassen",
      "sich insgesamt etwa 20 verschiedene Hypophysenhormone nachweisen, wel­",
      "che aus dem Vorderlappen (Adenohypophyse) und dem Hinterlappen (Neu­",
      "rohypophyse) ins Blut abgesondert werden. - Im Jahr 1911 - als diese",
      "Vorträge gehalten wurden - stand die Erforschung der Hypophyse noch",
      "ganz in den Anfängen. (Literatur: Dietrich Boie: «Das erste Auge», Stuttgart",
      "114    Das Blut ist nicht nur im Sinne des Dichterwortes «ein ganz besonderer Saft>:",
      "In Goethes «Faust» sagt Mephistopheles, nachdem Faust den Vertrag mit",
      "Blut unterzeichnet hat: «Blut ist ein ganz besondrer Saft» (Faust I, Studier­zimmer, Zeile 1740). Rudolf Steiner hielt einen Vortrag mit diesem Titel am 25. Oktober 1906, enthalten im Band «Die Erkenntnis des Übersinnlichen in unserer Zeit» (GA 55).",
      "114    das Verhältnis von menschlichem Blut zu tierischem Blut: Schon im Vortrag vom 21. Oktober 1907 vormittags hatte Rudolf Steiner ausgeführt: »Ich­Wesen sind die Bildner und Baumeister dieses roten Blutes (beim Menschen). Sie wirkten von außen, damit das Ich sieh in den Menschen versenken konnte. Die Tiere haben das Ich noch nicht. Wo beim Tier rotes Blut ist, da wirken Wesen von außen; die Tiere sind vom roten Blute «besessen». Der Mensch aber kommt dadurch zur Freiheit, daß er von seinem Ich, von sich selbst »besessen» ist. Er mußte von sich selbst Besitz ergreifen, um die Herr­schaft über sein Blut erlangen zu können.»",
      "125    Phrenologie: Begründer der sogenannten Sehädellehre (Phrenologie) war Franz Joseph Gall (1758-1828). Er glaubte, psychologische Eigenarten und moralische Qualitäten kämen in der Hirnoberfläche zum Ausdruck und ihre Über- oder Unterentwieklung könne durch Palpation des äußeren knöcher­nen Schädels festgestellt werden. Galls Lehre fand zu seiner Zeit weite Verbreitung, er trug sie 1805 auch in Gegenwart Goethes vor; in weiten Kreisen wurde die Phrenologie allerdings als Modetorheit aufgefäßt. - Nach Aussagen Rudolf Steiners Ist eine individuelle Berechtigung der Phrenologie insofern gegeben, als sich Kräfte, die in einem vorangegangenen Leben erworben wurden, in den Höckerbildungen des Schädels ausdrücken:",
      "«.. das, was die Individualität während des vorhergehenden Lebens ... oft mit sich verbunden hat und was doch den Kopf nicht mehr hat umbilden können, das drückt sich da aus.» - Siehe hierzu auch die Ausführungen Rudolf Steiners im Vortrag vom 27. Juni 1916 im Band «Weliwesen und Ichheit» (GA 169) und im 3. Vortrag des »Heilpädagogischen Kurses» (GA 317).",
      "131    Wenn ich... ein halbes Jahr über diese Dinge hier sprechen könnte: Erst vom Jahr 1920 an hat Rudolf Steiner auf Bitten von Ärzten viele Vorträge über Medizin gehalten: «Geisteswissenschaft und Medizin» 1920 (GA 312); »Gei­steswissenschaftliche Gesichtspunkte zur Therapie» 1921 (GA 313); »Phy­siologisch-Therapeutisches  auf  Grundlage  der  Geisteswissenschaft» 1920 (GA 314); »Heileutythmie» 1921 (GA 315); »Meditative Betrachtungen und Anleitungen zur Vertiefung der Heilkunst» 1924 (GA 316); »Heilpädagogischer Kurs» 1924 (GA 317); »Das Zusammenwirken von Arzten und Seelsorgern» 1924 (GA 318); »Anthroposophische Menschener­kenntnis und Medizin» 1923 (GA 319).",
      "138    «Es ist nichts in der Haut, was nicht im Knochen ist»: Goethe, im Gedicht «Typus»:",
      "Es ist nichts in der Haut,",
      "Was nicht im Knochen ist.",
      "Vor schlechtem Gebilde jedem graut,",
      "Das ein Augenschmerz ihm ist.",
      "Was freut denn jeden? Blühen zu sehen",
      "Das von innen schon gut gestaltet;",
      "Außen mag's in Glätte, mag in Farben gehen:",
      "Es ist ihm schon voran gewaltet.",
      "140    bestehen die Knochen zum Teil aus pbospborsaurem und koblensaurem Kalk:",
      "Hierzu sagt Rudolf Steiner im Vortrag vom 4. Januar 1924, enthalten im Band «Meditative Betrachtungen und Anleitungen zur Vertiefung der Heil­kunst» (GA 316): «... Der kohlensaure Kalk bildet für die Erde den substan­tiellen Angriffspunkt, um nach ihren Bildungslträften den Knochen zu for­men. Der phosphorsaure Kalk bildet für den Kosmos den Angriffspunkt, um den Knochen zu formen.»",
      "152    die übersinnliche Form, welche als ein aus den übersinnlichen Welten heraus­geborenes Krafisystem dazu bestimmt ist, die Materie aufzunehmen: In ande­rem Zusammenhang spricht Rudolf Steiner von «der Formgestalt des physi­schen Leibes, welche als ein Geistgewebe die physischen Stoffe und Kräfte verarbeitet, so daß sie in die Foim hineinkommen, die uns als der Mensch auf dem physischen Plane entgegentritt» und nennt diese Formgestalt das «Phan­tom» des Menschen (im Vortrag vom 10. Oktober 1911, enthalten im Band «Von Jesus zu Christus», GA 131). Die verschiedenen Angaben Rudolf Steiners hierüber wurden von Maximilian Rebholz dargestellt in seinem Aufsatz «Beiträge zum Phantom-Problem». erschienen 1957 in »Studien zur Geisteswissenschaft».",
      "167    eine Art Metalldampf Durch Kondensation von Metalldämpfen an einer gekühlten, glatten Oberfläche werden Metallspiegel gewonnen. Indem das Metallwesen dem Kosmos durch diesen Destillationsprozeß angenähert wird, wird die Heilwirkung der Metalle gesteigert.",
      "171    Alles, was über die Umwandlung der Organe gesagt worden ist, laßt sich nachweisen durch embryologische Untersuchungen: Siehe hierzu die Arbeiten von Erich Blechschmidt. »Die vorgeburtlichen Entwicklungsstadien des Menschen. Eine Einführung in die Humanembryologie», 1960, und «Der menschliche Embryo. Dokumentation zur kinetischen Anatomie», 1963.",
      "172    Während nun das Rückenmark und das Lympbsystem auf früheren Stufen eine aufsteigende Tendenz zeigten, müssen wir von dem heutigen Rücken­mark und Lymphsystem sagen, daß sie in absteigender Entwickelung begrif­fen sind: Siehe hierzu den Vortrag vom 21. Oktober 1907 vormittags, enthal­ten im Band «Mythen und Sagen» (GA 101).",
      "die ... Menschenseelen werden zu neuen Daseinsstufen fortschreiten: Siehe hierzu »Die Geheimwissenschaft im Umriß» (GA 13), Kapitel: «Gegenwart und Zukunft der Welt- und Menschheitsentwickelung».",
      "181          lm Anschluß an die öffentlichen Vorträge «Wie widerlegt man Theosophie?»",
      "und «Wie verteidigt man Theosophie?»: Die Vorträge wurd:n am 19. und 25.",
      "März 1911 gehalten und sind in der Gesamtausgabe noch nicht erschienen.",
      "Sie sind 1968 veröffentlicht worden in »Mensch und Welt», Blätter für",
      "Anthroposophie, Nrn. 1-4, allerdings nach einer mangelhaften Nachsehrift.",
      "182    Es wurde gefragt...: Hiervon liegt keine Nachschrift vor.",
      "189    Ein bedeutender Erkenntnistheoreti&er der Gegenwart: Otto Liebmann (1840-1912) in seinem Werk «Zur Analysis der Wirklichkeit. Eine Erörte­rung der Grundprobleme der Philosophie», 3. Aufl., Sträßburg 1900, S.28. Wörtlich heißt es: «Gerade deshalb, weil in der Tat kein vorstellendes Sub­jekt aus der Sphäre seines subjektiven Vorstellens hinaus kann, gerade des­halb, weil es nie und nimmermehr mit Überspringung des eigenen Bewußt­seins, unter Emanzipation von sich selber, dasjenige zu erfassen und zu konstatieren imstande ist, was jenseits und außerhalb seiner Subjektivität existieren oder nicht existieren mag, gerade deshalb ist es ungereimt, behaup­ten zu wollen, daß das vorgestellte Objekt außerhalb der subjektiven Vorstel­lung nicht da sei.«",
      "in meinen erkenntnistheoretischen Schriften: Siehe «Grundlinien einer Erkenntnistheorie der Goetheschen Weltanschauung mit besonderer Rück­sicht auf Schiller« (1886) GA 2, sowie «Wahrheit und Wissenschaft« (1892) GA 3.",
      "190    ein bekannter und bedeutender Philosoph: Eduard von Hartmann,",
      "1842-1906.    Siehe Rudolf Steiner «Mein Lebenigang«, GA 28, Kapitel IX, und den Aufsatz «Philosophie und Anthroposophie« im Band mit dem gleichen Titel, GA 35.",
      "192    *) In der Nachschrift ist vermerkt, daß Rudolf Steiner an dieser Stelle hinwies auf die Begriffe «Ich« und «Nicht-Ich»», wie sie von Carl Unger behandelt wurden in seiner Schrift «Das Ich und das Wesen des Menschen«, die kurz zuvor im Philosophisch-Theophischen Verlag erschienen war. Dieser Auf­satz ist heute zugänglich in «Carl Unger, Schriften«, Erster Band."
    ],
    "sentences": [
      [
        "Zu dieser Ausgabe"
      ],
      [
        "Die in diesem Band enthaltenen Vorträge hielt Rudolf Steiner im Jahr 1911 auf Einladung von Prager Theosophen."
      ],
      [
        "In Prag - das damals als Hauptstadt des Königreiches Böhmen zur Österrei­chisch-Ungarischen Monarchie gehörte - gab es in diesen Jahren vor dem ersten Weltkrieg drei verschiedene theosophische Gruppierungen.",
        "Neben der «Böhmi­schen Sektion Prag der Theosophischen Gesellschaft (Adyar)» hatte sich eine Gruppe von Tschechen unter der Leitung von Jan Bedrnicek schon seit dem Jahr 1906 direkt an den von Rudolf Steiner geleiteten Besant-Zweig in Berlin ange­schlossen; sie führte offiziell den Namen «Abteilung Prag des Besant-Zweiges, Berlin».",
        "Außerdem gab es eine unabhängige theosophische Arbeitsgruppe etwa seit 1909, die «Bolzano-Gruppe», die sich im Jahr 1912 als «Bolzano-Zweig» ebenfalls der Deutschen Sektion und später der Anthroposophischen Gesell­schaft anschloß.",
        "Die Leiterin dieser Gruppe war Berta Fanta."
      ],
      [
        "Die Initiative, Rudolf Steiner zu einem Vortragszyklus nach Prag zu bitten, ging von der tschechischen Gruppe aus.",
        "Am 25.",
        "Mai 1910 fuhr deren Leiter Jan Bedrnicek nach Hamburg, um mit Rudolf Steiner, der dort die Vortragsreihe über «Die Offenbarungen des Karma» hielt, Termin und Themen zu besprechen.",
        "Zwischen den verschiedenen theosophischen Gruppierungen hat es damals eine gute Zusammenarbeit gegeben.",
        "So trat als offizieller Veranstalter von Rudolf Steiners Vorträgen die «Böhmische Sektion» auf, die die Einladungen verschickte (siehe Seite 200) und die Vorträge im «Prager Tagblatt» Nr.74 vom 15.",
        "März 1911 mit folgender Anzeige ankündigte:"
      ],
      [
        "Die Theosopbische Gesellschaft in Prag veranstaltet im laufenden Monate einen öffentlichen Vortragszyklus, gehalten von dem hervorragenden Philo­sophen und Okkultisten Dr.",
        "Rudolf Steiner über «okkulte Physiologie> und zwar vom 19. bis 28.",
        "März (präzise 8 Uhr abends) im Saale des kaufmänni­schen Vereins «Merkur», Niklasstraße.",
        "Anmeldungen an das Sekretariat der Sektion Prag, Weinberge, Bocelgasse 2, 2."
      ],
      [
        "Das Thema «Eine okkulte Physiologie» geht mit Sicherheit auf Rudolf Steiner selbst zurück, hatte er sich doch schon seit Jahren mit einer okkulten Betrach­tung des menschlichen Organismus beschäftigt.",
        "So sagte er zum Beispiel in einem Vortrag, der anläßlich der 5.",
        "Generalversammlung der Deutschen Sektion der Theosophischen Gesellschaft gehalten wurde (Berlin, 21.",
        "Oktober 1907 vormittags, in GA 101):"
      ],
      [
        "«Es ist... möglich, die Organe des Menschen zu studieren in ihrer verschiede­nen Wertigkeit, wenn man zurückgeht auf die Urgründe, die in den geistigen Welten zu finden sind.",
        "Wir finden, daß Leber, Galle, Milz und so weiter etwas"
      ],
      [
        "ganz anderes sind, wenn man weiß, wie verschiedene Welten an ihrer Gestal­tung beteiligt sind. ...",
        "Sie sind Erbteile aus der geistigen Welt heraus.",
        "Es müssen alle Organe beim Menschen aus ihren geistigen Ursprüngen heraus von uns betrachtet werden, wenn wir deren Bedeutung richtig verstehen wollen.",
        "Da sehen wir hin auf eine zukünftige Behandlungsweise des menschli­chen Leibes, wo man sich dieses geistigen Ursprunges der Organe bewußt sein wird und diese Erkenntnisse anwenden wird in der alltäglichen Medizin.»"
      ],
      [
        "und in München - nachdem das Thema für den Prager Zyklus schon feststand -am 26.",
        "August 1910 (in GA 125):"
      ],
      [
        "»Es wäre im Sinne dessen, was ich selbst als geisteswissenschaftliche Bewe­gung ansehen muß, mein dringendster Wunsch, daß diejenigen, welche eine physiologisch-ärztliche Vorbildung haben, sich so weit mit den Tatsachen der Geisteswissenschaft bekanntmachen, daß sie in bezug auf ihren Tatsachencha­rakter die Ergebnisse der Physiologie einmal durcharbeiten können.",
        "Ich werde selbst im nächsten Frühjahr nur höchstens die Grundlinien dieser geisteswis­senschaftlichen Physiologie ziehen können...»"
      ],
      [
        "Über die Teilnehmer an dem Prager Vortragszyklus ist nur wenig bekannt; insbesondere konnte bisher nicht herausgefunden werden, welche Ärzte teilge­nommen haben.",
        "Nur einige wenige Namen sind dokumentarisch gesichert: Dr.",
        "Ludwig Noll aus Kassel, der während dieser Zeit die erkrankte Marie von Sivers behandelte (siehe «Marie Steiner-von Sivers - Ein Leben für die Anthroposo­phie», Seite 201ff.), sowie die drei Münchner Ärzte Dr.",
        "Felix Peipers - der selbst in theosophischen Zusammenhängen schon Vorträge gehalten hatte über okkulte Anatomie und Medizin -, Dr.",
        "Max Hermann und Dr.",
        "Hanns Rascher."
      ],
      [
        "Ein Wiener Mitglied berichtet:"
      ],
      [
        "«Ein finanziell glücklicher Zufall machte es mir damals möglich, verspätet zu dem Vortragszyklus Dr.",
        "Steiners über okkulte Physiologie nach Prag zu fahren.",
        "Die Vorträge, denen ein großer Teil der Prager Intelligenzkreise beiwohnen konnte, gaben den ersten Ausblick in eine neue Betrachtungsweise des Menschen.",
        "Die Stimmung dieses Neuen herrschte namentlich unter den anthroposophischen Wissenschaftlern und Ärzten (darunter Dr.",
        "Peipers und Dr.",
        "Hermann).",
        "An den öffentlichen Vorträgen «Wie widerlegt man Theoso­phie?» und «Wie verteidigt man Theosophie» nahmen auch viele Menschen der Zionistischen Bewegung teil und ich kam bei dieser Gelegenheit in nahen Kontakt zu dem jungen Philosophen Hugo Bergmann (jetzt Professor in Jerusalem), dessen Schwiegermutter und Tante (Frau Fanta und Frau Freund) im Mittelpunkt der theosophischen Bewegung in Prag standen. ...",
        "Die Tage von Prag, an denen fast alle Wiener Theosophen teilnahmen, bekamen noch ihren besonderen Glanz durch den Eindruck einer in der Einheit des theoso­phischen Strehens gegründeten echten Verbindung zwischen Deutschen und Tschechen.",
        "Dies gab eine innere Wärme, in der auch Dr.",
        "Steiner sich beson­ders wohl zu fühlen schien.",
        "Unter den tschechischen Theosophen fiel besonders"
      ],
      [
        "ein greiser Musikprofessor auf, dessen Äußeres stark an Leo Tolstoi erinnerte.» (Aus einem undatierten Manuskript «Erinnerungen» von Dr.",
        "Ernst Müller, Wien.)"
      ],
      [
        "Am Schluß der Veranstaltungen fand noch ein ursprünglich im Programm nicht vorgesehener Vortrag Rudolf Steiners statt über die Beziehung der Theoso­phie zur Philosophie.",
        "Dieser Vortrag liegt bereits gedruckt vor im Band der Gesamtausgabe «Die Mission der neuen Geistesoffenbarung», GA 127, wird aber wegen seiner direkten Beziehung zu den Vorträgen über okkulte Physiolo­gie in den hier vorliegenden Band mit aufgenommen.",
        "Die beiden öffentlichen Vorträge vom 19. und 25.",
        "März 1911 «Wie widerlegt man Theosophie?» und «Wie verteidigt man Theosophie?» sind in der Gesamtausgabe noch nicht erschienen, sie waren - nach einer mangelhaften Nachschrift - abgedruckt in «Mensch und Welt», Blätter für Anthroposophie 1968, Nrn. 1-4."
      ],
      [
        "Zu der Zeit, als Rudolf Steiner diese Vorträge hielt, stand er mit seiner Geisteswissenschaft noch innerhalb der Theosophischen Gesellschaft.",
        "Er ver­wendete die Worte «Theosophie» und «theosophisch» jedoch immer im Sinne seiner später «Anthroposophie» genannten Geisteswissenschaft.",
        "Die Ausdrücke «Theosophie», «Geisteswissenschaft» oder «Geistesforschung» sind hier jeweils so wiedergegeben, wie sie von den Stenographen festgehalten wurden."
      ],
      [
        "Der Titel des Vortragszyklus ist von Ruddolf Steiner."
      ],
      [
        "Die Zeichnungen im Text wurden von Hedwig Frey und Leonore Uhlig nach den Skizzen der Stenographen ausgeführt.",
        "Originaltafelzeichnungen sind nicht erhalten."
      ],
      [
        "Textunterla gen: Eine wortwörtliche stenographische Mitschrift dieser Prager Vorträge Rudolf Steiners gibt es nicht.",
        "Wohl haben verschiedene Teilnehmer mitgeschrieben, doch reichten ihre stenographischen Fähigkeiten nicht aus, um einen ganzen Vortrag durchgehend wörtlich festhalten zu können."
      ],
      [
        "Von den vorliegenden Unterlagen - es sind insgesamt neun verschiedene Textfassungen - sind acht sogenannte Ausarbeitungen (die neunte besteht nur aus stichwortartigen Notizen), das heißt, sie geben nicht nur die ursprünglich stenographisch oder handschriftlich festgehaltenen Wortlaute wieder, sondern sie sind von den jeweiligen Schreibern mehr oder weniger bearbeitet worden (stilistisch zu einem lesbaren Text formuliert, Interpunktion eingefügt, gelegent­lich inhaltlich ergänzt, Lücken nach eigenem Verständnis oder Gedächtnis aus­gefüllt und anders mehr).",
        "Da sich keinerlei Originalstenogramme erhalten haben, ist es schwierig, den Grad der «Bearbeitung» im einzelnen festzustellen.",
        "Deshalb wurden bei den Vorarbeiten für die Neuausgabe 1991 zunächst alle vorliegenden Textfassungen Satz für Satz miteinander verglichen, woraus sich folgendes Bild ergibt:"
      ],
      [
        "Vier Stenographen (Walter Vegelahn, Fritz Mitscher, Wilhelm Friedrich und ein unbekannter) haben sich bemüht - entsprechend ihren individuellen Fähig­keiten -, die Vorträge weitgehend wörtlich mitzuschreiben.",
        "Ihre Klartextübertragungen"
      ],
      [
        "wurden in unterschiedlicher Weise und zum Teil mehrmals bearbeitet und zwar von den Nachsehreibern selbst.",
        "Die übrigen Nachschriften sind Zusammenfassungen der Vortragsinhalte.",
        "Im einzelnen liegen vor:"
      ],
      [
        "- Nachsehrift Walter Vegelahn in zwei stark voneinander abweichenden"
      ],
      [
        "a) Erstübertragung des Stenogramms, geringfügig bearbeitet (maschine-geschrieben)"
      ],
      [
        "b) von Vegelahn selbst überarbeitete Fassung von a), durch dessen eigene Einfügungen oft stark verändert (maschinegeschrieben)"
      ],
      [
        "- Nachsehrift Fritz Mitscher in zwei Fassungen:"
      ],
      [
        "a) Erstübertragung des Stenogramms (handschriftlich)"
      ],
      [
        "b) bearbeitete Fassung, zum Teil unter Berücksichtigung des Vegelahn­textes (maschinegeschrieben)"
      ],
      [
        "- Nachschrift Wilhelm Friedrich (handschriftliche Übertragung des Steno­grammtextes)"
      ],
      [
        "- Nachschrift eines unbekannten Stenographen (handschriftlich)"
      ],
      [
        "- Kurznachschrift (referatartig) von Jan van Leer (maschinegeschrieben)"
      ],
      [
        "- Kurznachschrift (referatartig) von Fritz Rascher (maschinegeschrieben)"
      ],
      [
        "- Kurznotizen von unbekannter Hand (handschriftlich)."
      ],
      [
        "Als offizieller Stenograph war der Berliner Walter Vegelahn, der schon mehr­jährige Etfahrungen im Mitschreiben von Vorträgen hatte, mit nach Prag gereist.",
        "Jedoch gelang es ihm diesmal nicht - aus welchen Gründen auch immer -, die Vorträge wirklich wörtlich mitzuschreiben.",
        "Vielleicht waren ihm die Thematik und das Vokabular ungewohnt, vielleicht waren die räumlichen oder akustischen Verhältnisse ungünstig, vielleicht lag auch eine persönliche Indisposition vor - all das läßt sich heute nicht mehr feststellen.",
        "Das Ergebnis seiner Mitschrift, die Übertragung des Stenogramms, war jedenfalls sehr unbefriedigend."
      ],
      [
        "Am 2.",
        "Mai 1911 schrieb Marie von Sivers aus Portorose, wo sie und Rudolf Steiner sich damals aufhielten, an die Leiterin des Philosophisch-Theosophischen Verlages, Johanna Mücke: «Der Doktor möchte doch gern alle Vorträge über Vegelahn, der sich über die Mangelhaftigkeit seiner Nachschriften wohl selbst klar war, hat diese später noch einmal überarbeitet und so eine zweite Textfas­sung erstellt, die sich von der ersten dadurch unterscheidet, daß er dem Wortlaut seines ursprünglichen Stenogrammteztes alle möglichen Zutaten beifügte (Füll­worte, Wiederholungen vorangegangener Satzpassagen oder Gedankengänge, Nachahmung bestimmter Eigentümlichkeiten von Rudolf Steiners Sprechstil"
      ],
      [
        "und so weiter).",
        "Die auf diese Weise entstandenen Satzkonstruktionen sind häufig so unklar gegliedert, daß ihr Sinn nur schwer verständlich ist.",
        "Solche Satzkon­struktionen stammen also nicht von Rudolf Steiner, sondern sind durch die nachträgliche Bearbeitung Vegelahns entstanden."
      ],
      [
        "Erst im Jahr 1927 wurden die Vorträge erstmals gedruckt und zwar als Manuskriptdruck für Mitglieder, bezeichnet als «Zyklus OP».",
        "Sowohl dieser Erstdruck wie auch die folgenden Auflagen innerhalb der Gesamtausgabe basier­ten auf der oben beschriebenen Textbearbeitung Vegelahns, können also nicht als die authentische Wiedergabe des Wortlautes Rudolf Steiners angesehen werden."
      ],
      [
        "«erfordert Theosophie ... das genaueste, präziseste logische Formulieren», so sagt Rudolf Steiner im Vortrag vom 28.",
        "März 1911 (siehe Seite 181/182), und nach Ausführungen über «Wortfüllsel» und «rhetorische Verbrämungen» fügt er hinzu: «Wenn man das Vorgetragene ganz genau nimmt, so darf man in den Sätzen nicht nur nichts ändern, sondern man muß auch genau auf die Grenze achten, die in die Formulierungen mit aufgenommen ist.» -Bald nach dem Erscheinen von «Zyklus OP» im Jahr 1927 meldeten sich eine"
      ],
      [
        "Reihe von Arzten, die auf Fehler in den Texten aufmerksam machten und entsprechende Korrekturen vorschlugen.",
        "Für die späteren Auflagen 1957 und 1971 konnte der Herausgeber Dr. med.",
        "W Zbinden durch Prüfung der damals vorliegenden Nachschriften einige sachliche Korrekturen durchführen; die Vegelahnsche Textbearbeitung wurde dadurch jedoch nicht grundsätzlich in Frage gestellt.",
        "Die Tatsache, daß es sich bei dieser keineswegs um den originalen Wortlaut Rudolf Steiners handelt, konnte erst in jüngster Zeit festgestellt werden durch einen genauen Vergleich mit den anderen, auf Stenogramme zurückgehen-den Nachschriften.",
        "Einige dieser Unterlagen hat die Nachlaßverwaltung erst in den letzten Jahren erhalten."
      ],
      [
        "Trotz der zahfreichen Differenzen in den einzelnen Wortlauten der verschie­denen Nachschriften sind Inhalt, Aufbau und Verlauf der Vorträge von allen Nachschreibern gleich wiedergegeben.",
        "Diese Tatsache ermöglichte es, nunmehr für die Neuausgabe 1991 eine neue Textfassung zu erarbeiten, deren Grundlage die am wenigsten bearbeiteten Niederschriften der Stenographen sind:"
      ],
      [
        "- die Erstausschriften von Walter Vegelahn und Fritz Mitscher, sowie die handschriftlichen Stenogrammübertragungen von Wilhelm Friedrich und von Unbekannt.",
        "Die Referate von van Leer und von Fritz Rascher wurden inhaltlich mit beigezogen.",
        "Auch diese verbesserte Textfassung enthält Unklares und Lük­kenhaftes, das mangels eines wortgetreuen Stenogrammes nicht rekonstruiert werden kann.",
        "Inhalt und Aufbau der Vorträge sind jedoch durch die zahlreichen Unterlagen gesichert."
      ],
      [
        "Hinweise zum Text"
      ],
      [
        "Werke Rudolf Steiners innerhalb der Gesamtausgabe (GA) werden in den Hinweisen mit der Bibliographie-Nummer angegeben.",
        "Siehe auch die Übersicht am Schluß des Bandes."
      ],
      [
        "13 die geistige, übersinnliche Grundlage der Organe, der Lebensformen, der Lebensprozesse: In seiner Schrift «Anthroposophie - Ein Fragment aus dem Jahre 1910» (GA 45) gibt Rudolf Steiner im Kapitel IV «Die Lebensvor­gänge» eine Schilderung des Sinneslebens des Menschen im Verhältnis zu seinem inneren Leibesleben.",
        "Diese inneren Lebensvorgänge werden dort charakterisiert als Atmen, Wärmung, Ernährung, Absonderung, Erhaltung, Wachstum und Hervorbringung.",
        "Erweiterte und modifizierte Darstellungen finden sich in den Vorträgen vom 12.",
        "August 1916, enthalten im Band «Das Rätsel des Menschen» (GA 170), und vom 29.",
        "Oktober 1921, enthalten im Band «Anthroposophie als Kosmosophie - Zweiter Teil» (GA 208).",
        "Siehe hierzu auch in Heft Nr.58/59 der «Beiträge zur Rudolf Steiner Gesamtaus­gabe» die Aufzeichnungen Rudolf Steiners zu den Sinnesbereichen und Lebensstufen, mit einem Vorwort von Hendrik Knobel."
      ],
      [
        "16 was über die Bedeutung der Organe in bezug auf den Menschen gesagt wird, das kann nicht... in gleicher Weise für die Tiere gesagt werden: Ausführliche Darstellungen darüber gibt Rudolf Steiner u. a. in folgenden Berliner Vorträ­gen: «Menschenseele und Tierseele», «Menschengeist und Tiergeist», am 10. und 17.",
        "November 1910, beide enthalten im Band «Antworten der Geistes­wissenschaft auf die großen Fragen des Daseins« (GA 60), «Der Ursprung der Tierwelt im Lichte der Geisteswissenschaft» am 18.",
        "Januar 1912, enthal­ten im Band «Menschengeschichte im Lichte der Geistesforschung» (GA 61), »Menschenwelt und Tierwelt nach Ursprung und Entwickelung dargestellt im Lichte der Geisteswissenschaft» am 15.",
        "April 1918, enthalten im Band «Das Ewige in der Menschenseele» (GA 67), sowie am 28.",
        "Juli 1922 in Dornach, enthalten in dem Band «Das Geheimnis der Trinität» (GA 214)."
      ],
      [
        "17 daß Goethe, ....... den Blick darauf gerichtet haben, daß die Schädelkno­chen gewisse Formähnlichkeiten haben mit den Wirbelknochen des Rückgra­tes: Lorenz Oken (1779-1851), Professor in Jena und München, ab 1832 in Zürich, veröffentlichte 1807 beim Antritt seiner Professur in Jena ein Pro­gramm: «Über die Bedeutung der Schädelknochen», in dem er die von Goethe 1790 entdeckte Wirbeltheorie als seine Entdeckung vortrug."
      ],
      [
        "Goethe hatte seine Wirbeltheorie des Schädels schon 1790 im Freundes-kreise vorgetragen, sie jedoch erst nach Oken veröffentlicht.",
        "Siehe hierzu in «Goethes naturwissenschaftliche Schriften», 5 Bände, herausgegeben und kommentiert von Rudolf Steiner in Kürschners «Deutsche National-Littera­tur», GA la-e, in Band 1 »Bildung und Umbildung organischer Naturen» die Aufsätze Goethes «Zwischenknochen», Abschnitt VIII, und «Das Schädelge­rüst aus sechs Wirbelknochen auferbaut», sowie die dazugehörigen Fußnoten Rudolf Steiners (a.a.O.",
        "Seite 316-323).",
        "Goethe schreibt dort: «... ein solches Gewahrwerden, Auffassen, Vorstellen, Begriff, Idee, wie man es nennen mag,"
      ],
      [
        "behält immerfort, man gebärde sich, wie man will, eine esoterische Eigen-schaft; im ganzen läßt sich's aussprechen, aber nicht beweisen...» - und Rudolf Steiner in einer Fußnote dazu:"
      ],
      [
        "«Eine solche ideelle Wahrheit kann und muß zunächst ganz allgemein, abgesehen von jedem einzelnen Falle, aufgefaßt werden.",
        "Daß sie sich als solche nun nicht beweisen läßt, hat seinen guten Grund.",
        "Ein Beweis kann immer nur die Begründung irgend eines Satzes durch etwas anderes sein.",
        "Jene Wahrheit trägt aber ihre Gewähr in sich selbst, kann also nicht durch etwas anderes begründet werden.",
        "Dies zu erkennen, geht nun freilich jenen ab, welche glauben, allgemeine Wahrheiten seien nur abstrakte Sätze aus unzähli­gen Beobachtungen abgeleitet.",
        "Die Aufgabe der empirischen Wissenschaft kann nur sein, zu zeigen, wie sich eine allgemeine, ihre Gewähr in sich selbst tragende Wahrheit in ihrer Verwirklichung im Individuellen darstellt.»"
      ],
      [
        "18 in unserem Gehirn ein dzfferenziertes Rückenmark: Ergänzende Ausführun­"
      ],
      [
        "gen in bezug auf die kosmische Evolution des Hauptes, wenn man zurück­"
      ],
      [
        "geht bis zur Mondenentwickelung, finden sich u. a. in folgenden Vorträgen:"
      ],
      [
        "Am 20.",
        "Dezember 1914, enthalten im Band «Okkultes Lesen und okkultes"
      ],
      [
        "Hören» (GA 156); am 26. und 27.",
        "November 1920, enthalten im Band «Die"
      ],
      [
        "Brücke zwischen der Weltgeistigkeit und dem Physischen des Menschen»"
      ],
      [
        "(GA 202); am 12.",
        "Januar 1924, enthalten im Band «Mysterienstätten des"
      ],
      [
        "Mittelalters» (GA 233 a), sowie in den Vorträgen des Bandes «Die Sendung"
      ],
      [
        "Michaels» (GA 194)."
      ],
      [
        "Siehe: Rudolf Steiners Aufsatz «Goethes Naturanschauung gemäß den"
      ],
      [
        "neuesten Veröffentlichungen des Goethe-Archivs» (heute enthalten in GA"
      ],
      [
        "30), worin er über eine Tagebuchaufzeichnung Goethes aus dem Jahr 1790"
      ],
      [
        "berichtet.",
        "«Das Hirn selbst ist nur ein großes Hauptganglion.",
        "Die Organisa­"
      ],
      [
        "tion des Gehirns wird in jedem Ganglion wiederholt, so daß jedes Ganglion"
      ],
      [
        "als ein Meines subordiniertes Gehirn anzusehen ist.»"
      ],
      [
        "25 die menschliche Aura: Ausführlich dargestellt in Rudolf Steiners «Theoso­"
      ],
      [
        "phie» (GA 9), im Kapitel «Von den Gedankenforsien und der menschlichen"
      ],
      [
        "Aura», sowie in dem Aufsatz «Von der Aura des Menschen», enthalten im"
      ],
      [
        "Band «Lucifer - Gnosis.",
        "Grundlegende Aufsätze zur Anthroposophie» (GA"
      ],
      [
        "30 ,ogenanntes blaues Blut: Die populäre Vereinfachung, das venöse Blut als"
      ],
      [
        "«blau» und das arterielle Blut als »rot» zu bezeichnen, läßt sich nicht auf den"
      ],
      [
        "Lungenkreislauf anwenden: hier führen die vom Herzen zur Lunge gehenden"
      ],
      [
        "Arterien «blaues» Blut, die von der Lunge zum Herzen führenden Arterien"
      ],
      [
        "dagegen «rotes» Blut.",
        "Über die Besonderheiten des Lungenkreislaufes sagt"
      ],
      [
        "Rudolf Steiner am 26.",
        "Mai 1922 (in «Menschliches Seelenleben und Geistes-"
      ],
      [
        "streben» (GA 212): «Das Ich... schlüpft in die Organe der Lunge hinein; mit"
      ],
      [
        "den Adern, die von der Lunge zum Herzen hineingehen, nähert sich das Ich"
      ],
      [
        "immer mehr dem Herzen.",
        "Das Ich folgt immer mehr und mehr, ... innig"
      ],
      [
        "verbunden mit dem Blutkreislauf, dem Wege dieses Blutkreislaufes."
      ],
      [
        "daß... das Ich eingreift in dasjenige, was aus dem ZusammenscMuß des"
      ],
      [
        "ätherischen und des astralischen Herzens gebildet worden ist.»"
      ],
      [
        "Nebenströmung ...., welche ins Gebirn führt: Gemeint sind die beiden Kopf-schlagadern."
      ],
      [
        "wie die äußere Wissenschaft von einer spekulativen Lebenskrafi gesprochen hat: Die Anschauung von der Lebenskraft, der «vis vitalis», welche bis über die Mitte des 19.",
        "Jahrhunderts verbreitet war, ist ein Produkt rein spekulati­ven Denkens; sein eigentliches Wesen, das «vitale Prinzip», ist unbekannt, unbegründbar und phänomenologisch nicht zu erfassen.",
        "Daß mit der Bezeichnung »Ätherleib» etwas ganz anderes gemeint ist als mit der »Lebens­kraft» der älteren Naturwissenschaft, schreibt Rudolf Steiner in seinem Buch »Theosophie» (GA 9) in einer Fußnote zum Kapitel «Das Wesen des Men­schen», in Abschnitt IV Leib, Seele und Geist.",
        "Ergänzendes u. a. in den Vorträgen vom 7.",
        "Februar 1918 in »Das Ewige in der Menschenseele» (GA 67) und vom 6.",
        "April 1921 in »Die befruchtende Wirkung der Anthroposo­phie auf die Fachwissenschaften» (GA 76)."
      ],
      [
        "40 in dem Blutsystem ein Abbild des Ich... und in dem Nervensystem ein Abbild des Astralleibes: Siehe hierzu auch Rudolf Steiners Ausführungen im Vortrag vom 21.",
        "Oktober 1907 vormittags, enthalten im Band «Mythen und Sagen» (GA 101)."
      ],
      [
        "52 was wir das sympathische Nervensystem nennen: Siehe hierzu: Dr.",
        "Rudolf Steiner / Dr.",
        "Ita Wegman «Grundlegendes für eine Erweiterung der Heil-kunst nach geisteswissenschaftlichen Erkenntnissen» (GA 27), Kapitel VI.",
        "Blut und Nerv.",
        "Man unterscheidet ein sympathisches und ein parasympathi­sches System und faßt beide als vegetatives bzw. autonomes Nervensystem zusammen.",
        "Es bestehen jedoch weniger anatomische als physiologische Unterscheidungsmerkmale.",
        "Der Ausdruck «parasympathisches Nervensy­stem» wurde erst im Jahr 1905 eingeführt, es findet in den Darstellungen Rudolf Steiners keine Erwähnung."
      ],
      [
        "Sonnengeflecht: Das mächtigste Geflecht des Sympathikus wird als Plexus solaris bzw.",
        "Plexus coeliacus bezeichnet und befindet sich im Oberbauch.",
        "Ergänzende Ausführungen Rudolf Steiners über das Sonnengeflecht finden sich u. a. in folgenden Vorträgen: 26.",
        "September und 7.",
        "Oktober 1905 im Band »Grundelemente der Esoterik» (GA 93 a), und 8.",
        "Juni1912 im Band »Der Mensch im Lichte von Okkultismus, Theosophie und Philosophie»"
      ],
      [
        "56 die mystische Versenkung: Ausführlich dargestellt in den Vorträgen vom März 1910 im Band «Makrokosmos und Mikrokosmos» (GA 119)."
      ],
      [
        "daß alles, was im leidenschaftlichen Blute ist, mit bineingeprägt wird in das sympathische Nervensystem: Siehe hierzu Rudolf Steiners Vortrag vom 14.",
        "Januar 1917, enthalten im Band »Zeitgeschichtliche Betrachtungen - Zweiter Teil» (GA 174): «Das wirkliche Ich greift als bildsame Kraft durch das Sonnengeflecht in die ganze Organisation des Menschen ein. ...",
        "Da das Gangliensystem die ganze Zirkulation des Blutes mitbedingt, so widerspricht das auch nicht der Tatsache, daß das Ich im Blute seinen Ausdruck hat. ...",
        "Was nun als Gangliensystem, als Sonnengeflecht im Menschen lebt, iSt schon vor der Mondenentwickelung herübergekommen und stellt gewisser­maßen das Haus für das Ich dar.»"
      ],
      [
        "57 wenn ich durch mein sympathisches Nervensystem hellsichtig werde: In späte-ren Jahren spricht Rudolf Steiner von «Bauchhellsehen».",
        "Siehe hierzu u. a. die Vorträge vom 27.",
        "März und vom 1.",
        "Mai 1915, beide enthalten im Band «Wege der geistigen Erkenntnis und der Erneuerung künstlerischer Weltan­schauung» (GA 161), vom 4.",
        "Januar 1915 (2.",
        "Teil des Vortrages), enthalten in «Kunst im Lichte der Mysterienweisheit» (GA 275), vom 15.",
        "Februar 1915 im Band »Die geistigen Hintergründe des ersten Weltkrieges» (GA 174 b), vom 2.",
        "März 1915 im Band »Menschenschicksale und Völkerschicksale» (GA 157)."
      ],
      [
        "59 wenn wir den äußeren Rhythmus des Kosmos wiedererkennen im Blut­Pulsschlag: Der Frühlingsaufgangspunkt der Sonne - also der Punkt inner­halb des Tierkreises, an dem die Sonne zum Zeitpunkt der Tag- und Nacht­gleiche im Frühling aufgeht - bleibt bekanntlich nicht immer der gleiche, es verschiebt sich dieser Punkt vielmehr im Verlaufe von 72 Jahren um ein Grad.",
        "Der Zeitraum, in welchem die Sonne so den ganzen Tierkreis durch­läuft, beträgt etwa 25 920 Jahre.",
        "Man nennt dies ein Weltenjahr oder ein platonisches Jahr. - Der Mensch atmet innerhalb einer Minute normalerweise 18mal, das sind in einer Stunde 1080, in einem Tage = 25920 Atemzüge."
      ],
      [
        "25 920 Erdentage wiederum sind die durchschnittliche Lebensdauer des Men­schen, etwa 72 Jahre.",
        "Rudolf Steiner hat auf diese Zusammenhänge häufig aufmerksam gemacht, besonders ausführlich in den Vorträgen vom 28.",
        "Januar 1917 im Band «Zeitgeschichtliche Betrachtungen - Zweiter Teil» (GA 174), vom 13.",
        "Februar 1917 im Band «Bausteine zu einer Erkenntnis des Mysteriums von Golgatha» (GA 175) und vom 24.",
        "September 1924 im Band «Die Schöpfung der Welt und des Menschen» (GA 354)."
      ],
      [
        "Es wäre nun... interessant zu sehen, ob die äußere Physiologie solche Dinge... bestätigen würde: Ein erster Versuch der experiementellen Bestäti­gung dieser Anschauungen wurde von Lilly Kolisko unternommen mit ihrer Arbeit «Milzfunktion und Plättchenfrage», Stuttgart 1922.",
        "In späteren Kur­sen für Ärzte hat Rudolf Steiner wiederholt auf diese Arbeit hingewiesen."
      ],
      [
        "64 Daß ein System sich abschließt: Vom kosmologischen Aspekt aus hat Rudolf"
      ],
      [
        "Steiner auf diese Probleme hingewiesen in den Vorträgen «Die Evolution"
      ],
      [
        "vom Gesichtspunkt des Wahrhaftigen» (GA 132), ergänzend zu dem in dem"
      ],
      [
        "Buch «Die Geheimwissenschaft im Umriß» (GA 13) Dargestellten."
      ],
      [
        "66 enthalten Mythen und Sagen wirkliche Weisheiten über das menschliche Wesen, wirkliche Physiologie: Siehe hierzu die Vorträge vom Oktober 1907 im Band «Mythen und Sagen» (GA 101)."
      ],
      [
        "Namen wie Kain und Abel: Siehe hierzu die Vorträge vom 27.",
        "März 1913"
      ],
      [
        "enthalten im Band «Welche Bedeutung hat die okkulte Entwickelung des"
      ],
      [
        "Menschen für seine Hüllen und sein Selbst?» (GA 145) sowie vom 10.",
        "Juni"
      ],
      [
        "1904 im Band »Die Tempellegende und die Goldene Legende» (GA 93)."
      ],
      [
        "Wie haben wir es heute so herrlich weit gebracht!: Nach Goethes «Faust«, I.",
        "Teil, Nacht (Zeile 573): Und wie wirs dann zuletzt so herrlich weit gebracht."
      ],
      [
        "67 in den Namen der Mythen und Sagen erst einen Sinn finden, wenn sie darin die Physiologie erkennen: Siehe Hinweise zu Seite 66.",
        "Anhand der griechi­schen Mythologie wurde dies dargelegt in den Vorträgen vom August 1911 in dem Band «Weltenwunder, Seelenprüfungen und Geistesoffenbarungen»"
      ],
      [
        "68 in dem ersten öffentlichen Vortrage: «Wie widerlegt man Theosophie?», Vortrag vom 19.",
        "März 1911, in der Gesamtausgabe noch nicbt erschienen, nach einer mangelhaften Nachschrift abgedruckt in «Mensch und Welt.",
        "Blätter für Anthroposophie» 1968, Nr.1-2."
      ],
      [
        "80 Während wir durch den Atmungsprozeß die Außenwelt stofflich aufnehmen, nehmen wir im Wahrnehmungsprozeß... etwas durch einen vergeistigten Atmungsprozeß in unseren Organismen auf Ergänzende Gesichtspunkte hierzu gibt R.",
        "Steiner u. a. in folgenden Vorträgen: Am 16.",
        "April 1921, im Band »Geisteswissenschaftliche Gesichtspunkte zur Therapie» (GA 313):"
      ],
      [
        "»Das Sinneswahrnehmen ist nichts anderes als ein verfeinerter, das heißt ein ins Ätherische hineingetriebener Atmungsprozeß.» - Am 21.",
        "Juli 1924, im Band «Anthroposophische Menschenerkenntnis und Medizin» (GA 319):"
      ],
      [
        "«So haben wir also in der Atmung gegeben einen gröberen Prozeß, wo der eingeatmete Sauerstoff sich mit dem Kohlenstoff unseres Organismus verbin­det und als Kohlensäure ausgeatmet wird.",
        "Daneben haben wir einen feineren Prozeß, wo sich der Sauerstoff mit dem Silizium zu Kieselsäure verbindet und als solche in die menschliche Organisation hinein abgesondert wird.» -Am 28.",
        "August 1924 in dem gleichen Band: «Diese Kieselsäure ist das äußerliche Korrelat, die Wirksamkeit nach außen für die Ich-Organisation.",
        "Astralischer Leib: das innerlich Spirituelle; Kohlensäureprozeß: das äußer­liche Physische...»."
      ],
      [
        "82 Denen stehen andere [Weltanschauungen] gegenüber» die materialistischen:"
      ],
      [
        "Carl Vogt, 1817-1895: «Physiologische Briefe für Gebildete aller Stände» (1845, Seite 206): »Ein jeder Naturforscher wird wohl denke ich bei einiger­maßen folgerichtigem Denken auf die Ansicht kommen, daß alle jene Fähig­keiten, die wir unter dem Namen der Seelentätigkeiten begreifen, nur Funk­tionen der Gehirnsubstanz sind; oder, um mich einigermaßen grob hier auszudrücken: daß die Gedanken in demselben Verhältnis etwa zu dem Gehirn stehen, wie die Galle zu der Leber oder der Urin zu den Nieren.",
        "Eine Seele anzunehmen, die sich des Gehirns wie eines Instrumentes bedient, mit dem sie arbeiten kann, wie es ihr gefällt, ist reiner Unsinn.»"
      ],
      [
        "Jacob Moleschott, 1822-1893.",
        "In «Der Kreislauf des Lebens» (1852, Seite"
      ],
      [
        "402) schließt sich dieser der Ansicht Carl Vogts an: «Der Vergleich ist"
      ],
      [
        "unangreifbar, wenn man versteht, wohin Vogt den Vergleichspunkt verlegt."
      ],
      [
        "Das Gehirn ist zur Erzeugung der Gedanken ebenso unerläßlich, wie die"
      ],
      [
        "Leber zur Bereitung der Galle und die Niere zur Abscheidung des Harns.» Demgegenüber sagt Rudolf Steiner im Vortrag vom 30.",
        "Januar 1921,"
      ],
      [
        "enthalten im Band »Die Verantwortung des Menschen für die Weltentwicke­lung» (GA 203): »Es ist ein Unsinn, denn das Umgekehrte ist richtig, daß nämlich von den Gedanken das Gehirn abgeschieden wird, natürlich immer"
      ],
      [
        "neu abgeschieden wird, weil es immer wiederum vom Stoffwechselorganis­mus aus ersetzt wird.»"
      ],
      [
        "82 Psychophysischer Parallelismus: Eine 1860 von Gustav Theodor Fechner"
      ],
      [
        "(1801-1887) begründete psychologische Teilwissenschaft, nach der Leib und"
      ],
      [
        "Seele als zwei getrennte. doch einander korrespondierende Erscheinungen"
      ],
      [
        "zusammenhängen."
      ],
      [
        "83 Es sind Seelenübun gen notwendig, um den Menschen in die übersinnliche Welt hineinzuführen: Siehe «Wie erlangt man Erkenntnisse der höheren Welten» (GA 10) und «Die Geheimwissenschaft im Umriß» (GA 13), Kapitel «Zur Erlangung übersinnlicher Erkenntnisse»."
      ],
      [
        "85 überall im Ätherleibe Strömungen sich entwickeln: Ergänzendes hierzu u. a. im Vortrag vom 25.",
        "August 1911, enthalten in «Weltenwunder, Seelenprü­fungen und Geistesoffenbarungen» (GA 129) und vom I.",
        "Oktober 1911 »Die Ätherisation des Blutes», enthalten in «Das esoterische Christentum und die geistige Führung der Menschheit» (GA 130)."
      ],
      [
        "wurde die Milz zu allen Zeiten in der okkulten Literatur... immer als ein besonders geistiges Organ angesehen und geschildert: Z.B. in H.P Blavat­skys «Geheimlehre»."
      ],
      [
        "107 daß das Außenleben und das Innenleben des Menschen... in einem Gegen­"
      ],
      [
        "satz zueinander stehen und... in Spannungen zum Ausdruck kommt ... in"
      ],
      [
        "den Organen des Gehirnes, die wir als Zirbeldrüse und Gehirnanhang"
      ],
      [
        "bezeichnen: Die Zirbeldrüse (Corpus pineale, Glandula pinealis, Epiphysis"
      ],
      [
        "cerebri) ist schon beim Embryo mit 12 Wochen deutlich zu identifizieren."
      ],
      [
        "Die in ihr stattfindenden Mineralisierungsprozesse sind mit Beginn der"
      ],
      [
        "Pubertät so weit vorgeschritten, daß sich der sogenannte «Himsand» nach­"
      ],
      [
        "weisen läßt, der biochemisch aus Kalk- und Magnesiumsalzen besteht."
      ],
      [
        "Epiphyse ist stark von Fasern des sympathischen Nervensystems durchdrun­"
      ],
      [
        "gen und ist stark durchblutet.",
        "Eine intensive wissenschaftliche Erforschung"
      ],
      [
        "der Zirbeldrüse setzte etwa 1959 ein; übereinstimmend wurde eine Abhän­"
      ],
      [
        "gigkeit von Lichtverhältnissen und eine Tages- und jahreszeitliche Rhythmik"
      ],
      [
        "des Organs festgestellt."
      ],
      [
        "Die Hirnanhangdrüse (Hypophyse, Glandula Pituitaria - Schleimdrüse) ist"
      ],
      [
        "ein an der Hirnbasis in den Türkensattel des Keilbeins eingelagertes inkreto­"
      ],
      [
        "risches Organ, welches im wesentlichen die Funktionen der übrigen Hor­"
      ],
      [
        "mondrüsen des Körpers reguliert.",
        "Sie hat die Größe einer Haselnuß.",
        "Es lassen"
      ],
      [
        "sich insgesamt etwa 20 verschiedene Hypophysenhormone nachweisen, wel­"
      ],
      [
        "che aus dem Vorderlappen (Adenohypophyse) und dem Hinterlappen (Neu­"
      ],
      [
        "rohypophyse) ins Blut abgesondert werden. - Im Jahr 1911 - als diese"
      ],
      [
        "Vorträge gehalten wurden - stand die Erforschung der Hypophyse noch"
      ],
      [
        "ganz in den Anfängen. (Literatur: Dietrich Boie: «Das erste Auge», Stuttgart"
      ],
      [
        "114 Das Blut ist nicht nur im Sinne des Dichterwortes «ein ganz besonderer Saft>:"
      ],
      [
        "In Goethes «Faust» sagt Mephistopheles, nachdem Faust den Vertrag mit"
      ],
      [
        "Blut unterzeichnet hat: «Blut ist ein ganz besondrer Saft» (Faust I, Studier­zimmer, Zeile 1740).",
        "Rudolf Steiner hielt einen Vortrag mit diesem Titel am 25.",
        "Oktober 1906, enthalten im Band «Die Erkenntnis des Übersinnlichen in unserer Zeit» (GA 55)."
      ],
      [
        "114 das Verhältnis von menschlichem Blut zu tierischem Blut: Schon im Vortrag vom 21.",
        "Oktober 1907 vormittags hatte Rudolf Steiner ausgeführt: »Ich­Wesen sind die Bildner und Baumeister dieses roten Blutes (beim Menschen).",
        "Sie wirkten von außen, damit das Ich sieh in den Menschen versenken konnte.",
        "Die Tiere haben das Ich noch nicht.",
        "Wo beim Tier rotes Blut ist, da wirken Wesen von außen; die Tiere sind vom roten Blute «besessen».",
        "Der Mensch aber kommt dadurch zur Freiheit, daß er von seinem Ich, von sich selbst »besessen» ist.",
        "Er mußte von sich selbst Besitz ergreifen, um die Herr­schaft über sein Blut erlangen zu können.»"
      ],
      [
        "125 Phrenologie: Begründer der sogenannten Sehädellehre (Phrenologie) war Franz Joseph Gall (1758-1828).",
        "Er glaubte, psychologische Eigenarten und moralische Qualitäten kämen in der Hirnoberfläche zum Ausdruck und ihre Über- oder Unterentwieklung könne durch Palpation des äußeren knöcher­nen Schädels festgestellt werden.",
        "Galls Lehre fand zu seiner Zeit weite Verbreitung, er trug sie 1805 auch in Gegenwart Goethes vor; in weiten Kreisen wurde die Phrenologie allerdings als Modetorheit aufgefäßt. - Nach Aussagen Rudolf Steiners Ist eine individuelle Berechtigung der Phrenologie insofern gegeben, als sich Kräfte, die in einem vorangegangenen Leben erworben wurden, in den Höckerbildungen des Schädels ausdrücken:"
      ],
      [
        "«.. das, was die Individualität während des vorhergehenden Lebens ... oft mit sich verbunden hat und was doch den Kopf nicht mehr hat umbilden können, das drückt sich da aus.» - Siehe hierzu auch die Ausführungen Rudolf Steiners im Vortrag vom 27.",
        "Juni 1916 im Band «Weliwesen und Ichheit» (GA 169) und im 3.",
        "Vortrag des »Heilpädagogischen Kurses» (GA 317)."
      ],
      [
        "131 Wenn ich... ein halbes Jahr über diese Dinge hier sprechen könnte: Erst vom Jahr 1920 an hat Rudolf Steiner auf Bitten von Ärzten viele Vorträge über Medizin gehalten: «Geisteswissenschaft und Medizin» 1920 (GA 312); »Gei­steswissenschaftliche Gesichtspunkte zur Therapie» 1921 (GA 313); »Phy­siologisch-Therapeutisches auf Grundlage der Geisteswissenschaft» 1920 (GA 314); »Heileutythmie» 1921 (GA 315); »Meditative Betrachtungen und Anleitungen zur Vertiefung der Heilkunst» 1924 (GA 316); »Heilpädagogischer Kurs» 1924 (GA 317); »Das Zusammenwirken von Arzten und Seelsorgern» 1924 (GA 318); »Anthroposophische Menschener­kenntnis und Medizin» 1923 (GA 319)."
      ],
      [
        "138 «Es ist nichts in der Haut, was nicht im Knochen ist»: Goethe, im Gedicht «Typus»:"
      ],
      [
        "Es ist nichts in der Haut,"
      ],
      [
        "Was nicht im Knochen ist."
      ],
      [
        "Vor schlechtem Gebilde jedem graut,"
      ],
      [
        "Das ein Augenschmerz ihm ist."
      ],
      [
        "Was freut denn jeden?",
        "Blühen zu sehen"
      ],
      [
        "Das von innen schon gut gestaltet;"
      ],
      [
        "Außen mag's in Glätte, mag in Farben gehen:"
      ],
      [
        "Es ist ihm schon voran gewaltet."
      ],
      [
        "140 bestehen die Knochen zum Teil aus pbospborsaurem und koblensaurem Kalk:"
      ],
      [
        "Hierzu sagt Rudolf Steiner im Vortrag vom 4.",
        "Januar 1924, enthalten im Band «Meditative Betrachtungen und Anleitungen zur Vertiefung der Heil­kunst» (GA 316): «...",
        "Der kohlensaure Kalk bildet für die Erde den substan­tiellen Angriffspunkt, um nach ihren Bildungslträften den Knochen zu for­men.",
        "Der phosphorsaure Kalk bildet für den Kosmos den Angriffspunkt, um den Knochen zu formen.»"
      ],
      [
        "152 die übersinnliche Form, welche als ein aus den übersinnlichen Welten heraus­geborenes Krafisystem dazu bestimmt ist, die Materie aufzunehmen: In ande­rem Zusammenhang spricht Rudolf Steiner von «der Formgestalt des physi­schen Leibes, welche als ein Geistgewebe die physischen Stoffe und Kräfte verarbeitet, so daß sie in die Foim hineinkommen, die uns als der Mensch auf dem physischen Plane entgegentritt» und nennt diese Formgestalt das «Phan­tom» des Menschen (im Vortrag vom 10.",
        "Oktober 1911, enthalten im Band «Von Jesus zu Christus», GA 131).",
        "Die verschiedenen Angaben Rudolf Steiners hierüber wurden von Maximilian Rebholz dargestellt in seinem Aufsatz «Beiträge zum Phantom-Problem». erschienen 1957 in »Studien zur Geisteswissenschaft»."
      ],
      [
        "167 eine Art Metalldampf Durch Kondensation von Metalldämpfen an einer gekühlten, glatten Oberfläche werden Metallspiegel gewonnen.",
        "Indem das Metallwesen dem Kosmos durch diesen Destillationsprozeß angenähert wird, wird die Heilwirkung der Metalle gesteigert."
      ],
      [
        "171 Alles, was über die Umwandlung der Organe gesagt worden ist, laßt sich nachweisen durch embryologische Untersuchungen: Siehe hierzu die Arbeiten von Erich Blechschmidt. »Die vorgeburtlichen Entwicklungsstadien des Menschen.",
        "Eine Einführung in die Humanembryologie», 1960, und «Der menschliche Embryo.",
        "Dokumentation zur kinetischen Anatomie», 1963."
      ],
      [
        "172 Während nun das Rückenmark und das Lympbsystem auf früheren Stufen eine aufsteigende Tendenz zeigten, müssen wir von dem heutigen Rücken­mark und Lymphsystem sagen, daß sie in absteigender Entwickelung begrif­fen sind: Siehe hierzu den Vortrag vom 21.",
        "Oktober 1907 vormittags, enthal­ten im Band «Mythen und Sagen» (GA 101)."
      ],
      [
        "die ...",
        "Menschenseelen werden zu neuen Daseinsstufen fortschreiten: Siehe hierzu »Die Geheimwissenschaft im Umriß» (GA 13), Kapitel: «Gegenwart und Zukunft der Welt- und Menschheitsentwickelung»."
      ],
      [
        "181 lm Anschluß an die öffentlichen Vorträge «Wie widerlegt man Theosophie?»"
      ],
      [
        "und «Wie verteidigt man Theosophie?»: Die Vorträge wurd:n am 19. und 25."
      ],
      [
        "März 1911 gehalten und sind in der Gesamtausgabe noch nicht erschienen."
      ],
      [
        "Sie sind 1968 veröffentlicht worden in »Mensch und Welt», Blätter für"
      ],
      [
        "Anthroposophie, Nrn. 1-4, allerdings nach einer mangelhaften Nachsehrift."
      ],
      [
        "182 Es wurde gefragt...: Hiervon liegt keine Nachschrift vor."
      ],
      [
        "189 Ein bedeutender Erkenntnistheoreti&er der Gegenwart: Otto Liebmann (1840-1912) in seinem Werk «Zur Analysis der Wirklichkeit.",
        "Eine Erörte­rung der Grundprobleme der Philosophie», 3.",
        "Aufl., Sträßburg 1900, S.28.",
        "Wörtlich heißt es: «Gerade deshalb, weil in der Tat kein vorstellendes Sub­jekt aus der Sphäre seines subjektiven Vorstellens hinaus kann, gerade des­halb, weil es nie und nimmermehr mit Überspringung des eigenen Bewußt­seins, unter Emanzipation von sich selber, dasjenige zu erfassen und zu konstatieren imstande ist, was jenseits und außerhalb seiner Subjektivität existieren oder nicht existieren mag, gerade deshalb ist es ungereimt, behaup­ten zu wollen, daß das vorgestellte Objekt außerhalb der subjektiven Vorstel­lung nicht da sei.«"
      ],
      [
        "in meinen erkenntnistheoretischen Schriften: Siehe «Grundlinien einer Erkenntnistheorie der Goetheschen Weltanschauung mit besonderer Rück­sicht auf Schiller« (1886) GA 2, sowie «Wahrheit und Wissenschaft« (1892) GA 3."
      ],
      [
        "190 ein bekannter und bedeutender Philosoph: Eduard von Hartmann,"
      ],
      [
        "1842-1906.",
        "Siehe Rudolf Steiner «Mein Lebenigang«, GA 28, Kapitel IX, und den Aufsatz «Philosophie und Anthroposophie« im Band mit dem gleichen Titel, GA 35."
      ],
      [
        "192 *) In der Nachschrift ist vermerkt, daß Rudolf Steiner an dieser Stelle hinwies auf die Begriffe «Ich« und «Nicht-Ich»», wie sie von Carl Unger behandelt wurden in seiner Schrift «Das Ich und das Wesen des Menschen«, die kurz zuvor im Philosophisch-Theophischen Verlag erschienen war.",
        "Dieser Auf­satz ist heute zugänglich in «Carl Unger, Schriften«, Erster Band."
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
