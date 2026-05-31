#!/usr/bin/env python3
"""Standalone import script for GA055 — GA055 - Die Erkenntnis des Übersinnlichen in unserer Zeit (1906/07)"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA055 - Die Erkenntnis des Übersinnlichen in unserer Zeit (1906/07)"""
GA_NUMBER = "GA055"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "ZUR EINFÜHRUNG",
    "paragraphs": [
      "Wir übergeben der Öffentlichkeit eine Anzahl von Vorträgen, die Rudolf Steiner in Berlin für das große Publikum gehalten hat. Berlin war der Ausgangspunkt für diese öffent­liche Vortragstätigkeit gewesen. Was in anderen Städten mehr in einzelnen Vorträgen behandelt wurde, konnte hier in einer zusammenhängenden Vortragsreihe zum Ausdruck gebracht werden, deren Themen ineinander übergriffen. Sie erhielten dadurch den Charakter einer sorgfältig fundierten methodischen Einführung in die Geisteswissenschaft und konnten auf ein regelmäßig wiederkehrendes Publikum rechnen, dem es darauf ankam, immer tiefer in die neu sich erschließenden Wissensgebiete einzudringen, während den neu Hinzukommenden die Grundlagen für das Verständnis des Gebotenen immer wieder gegeben wurden."
    ],
    "sentences": [
      [
        "Wir übergeben der Öffentlichkeit eine Anzahl von Vorträgen, die Rudolf Steiner in Berlin für das große Publikum gehalten hat.",
        "Berlin war der Ausgangspunkt für diese öffent­liche Vortragstätigkeit gewesen.",
        "Was in anderen Städten mehr in einzelnen Vorträgen behandelt wurde, konnte hier in einer zusammenhängenden Vortragsreihe zum Ausdruck gebracht werden, deren Themen ineinander übergriffen.",
        "Sie erhielten dadurch den Charakter einer sorgfältig fundierten methodischen Einführung in die Geisteswissenschaft und konnten auf ein regelmäßig wiederkehrendes Publikum rechnen, dem es darauf ankam, immer tiefer in die neu sich erschließenden Wissensgebiete einzudringen, während den neu Hinzukommenden die Grundlagen für das Verständnis des Gebotenen immer wieder gegeben wurden."
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "DIE ERKENNTNIS DES ÜBERSINNLICHEN IN UNSERER ZEIT UND DEREN BEDEUTUNG FÜR DAS HEUTIGE LEBEN Berlin, 11. Oktober 1906",
    "paragraphs": [
      "Der heutige Vortrag ist eine Art Programm, und die fol­genden sollen zwei Ziele verfolgen: Das erste Ziel ist, die Zuhörer bekannt zu machen mit dem, was die Geistesforschung über die Welt des Geistes in bezug auf den Men­schen, in bezug auf die Entwicklung des Menschen, in bezug auf Leben und Bestimmung des Menschen, in bezug auf Geburt und Tod, Ursprung des Lebens, Ursprung des Bösen, Gesundheit und Krankheit und in bezug auf Erziehungs­fragen bieten kann. So daß im Laufe des Winters der Um­fang dieser Geistesforschung sich vor unsere Seele stellen soll.",
      "Andererseits aber sind die Vorträge so eingerichtet, daß die Beziehung der gegenwärtigen geisteswissenschaftlichen Forschung zu den großen Kulturaufgaben, zu den brennen­den Zeitfragen, zu den großen Lebensfragen des Daseins, wie sie von der Gegenwart gestellt werden, besprochen wird. Es soll die Geisteswissenschaft nicht wie irgendeine Theorie hingestellt werden, sondern sie soll als etwas er­kannt werden, das sich in das ganze Leben eines Gegen-wartsmenschen mit einer gewissen inneren Notwendigkeit hineinstellt. So sehr auch das Alter der Zuhörer verschieden sein wird, durch die Mannigfaltigkeit der Themata wird vielleicht doch für jeden etwas Interessantes dargeboten werden können.",
      "Ich möchte nun, bevor ich zum Vortrage selbst übergehe,",
      "die einzelnen Themen, die als Einzelvorträge etwas in sich Abgeschlossenes und auf der anderen Seite doch ein zusam­menhängendes Ganzes bilden sollen, nochmals erwähnen. Vorerst wollen wir diesmal, weil es nicht so bequem ist wie im vergangenen Winter, sehr darauf achten, daß die Vorträge stattfinden werden am zweiten und dritten Donnerstag eines jeden Monats. Am 25. werden wir zu sprechen haben über das Thema «Blut ist ein ganz besonderer Saft». Da werden wichtige Kulturfragen der Menschheitsentwicklung zur Sprache kommen, im Anschlusse an eine vielleicht nur vom geisteswissenschaftlichen Standpunkte aus zu beleuch­tende intime Lebensfrage. Es ist dabei nicht darauf ab­gesehen, eine sensationell aussehende Frage aufs Tablett zu heben. Dann folgt «Der Lebenslauf des Menschen vom gei­steswissenschaftlichen Standpunkt», dann «Wer sind die Rosenkreuzer?», dann «Richard Wagner und die Mystik», dann «Was wissen unsere Gelehrten von der Theosophie?» und dann die religiöse Frage «Bibel und Weisheit».",
      "Diejenigen der verehrten Zuhörer, welche im verflossenen Winter schon hier versammelt waren zu den geisteswissen­schaftlichen Vorträgen, werden manches Bekannte in etwas anderer Beleuchtung finden. Aber die Dinge der geistes-wissenschaftlichen Forschung werden der Seele erst ganz zu eigen, wenn sie von den verschiedenen Seiten beleuchtet werden. Deshalb bitte ich, wenn Sie Bekanntes hören, es hinzunehmen, da es sich um den einführenden Vortrag zu dem ganzen Programm des Winters handelt. Dieser heutige Vortrag soll eine Art Versprechen sein. Es soll versprochen werden, was die folgenden Vorträge einlösen sollen. Es soll hingewiesen werden auf das, was man geisteswissenschaft­liche Forschung innerhalb der Gegenwart nennt, und dar­auf, daß diese Erforschung des geistigen, übersinnlichen Lebens eine große einschneidende Bedeutung für unsere",
      "Gegenwart hat und berufen ist, eine immer einschneiden­dere Bedeutung für das Leben der Menschen in der Zukunft zu bekommen.",
      "Es ist erst dreißig Jahre her, seit eine theosophische Be­wegung durch die Welt geht. Und nach diesen dreißig Jah­ren ist die Theosophie nicht etwa eine geistige Bewegung, die sonderlich angesehen ist. In den weitesten Kreisen drau­ßen versteht man unter Theosophie nicht irgend etwas, was man als auf wirklichem, tatsächlichem Boden stehend an­sieht. Viele sind unter unseren Zeitgenossen, die die Theo-sophie als etwas Phantastisches, als etwas, was sich in einem Wolkenkuckucksheim ergeht, ansehen. Nicht zu leugnen ist, daß die Theosophie, durch unkundige und vielleicht auch durch vorschnelle, dilettantische Persönlichkeiten, vielleicht sogar durch scharlatanhafte Seelen mit einem gewissen Recht an ihrem Ansehen verloren hat. Die Frage, was die Theo-sophie dem Menschen der Gegenwart aber doch bedeuten kann, soll uns heute hauptsächlich beschäftigen.",
      "Manche große Vorurteile sind verbreitet gegenüber der theosophischen Weltanschauung. Da sagt der eine: Ach, die Theosophie ist etwas, was so ähnlich ist wie der Spiri tismus, also etwas, was sich mit unserer heutigen abgeklär­ten, wissenschaftlichen Weltanschauung durchaus nicht ver­trägt. Die Theosophie ist etwas, was höchstens für Träumer eine Bedeutung haben kann, was aber mit den wissenschaft­lichen, logischen Gesetzen in Widerspruch steht. So sagen diejenigen, welche entweder selber auf dem Boden der Wis­senschaft stehen, oder welche sich sagen: Wissenschaft ist die Losung der Zeit, wir müssen auf sie hören, sie zeigt uns die tiefen Fragen des Daseins, und es ist eine Versündigung, wenn wir gegen die wohlbegründeten Ansprüche der Wis­senschaft verstoßen und uns dem hingeben, was unwissen­schaftlich ist.",
      "Ein anderes Vorurteil kommt von der religiösen Seite, sei es von solchen, die durch ihren Beruf für die Religion sein wollen oder sollen, oder von anderen, welche glauben, mit ihrem religiösen Gewissen in Zwiespalt zu kommen, wenn sie sich der Theosophie zuwenden. Wie eine neue Sekte, wie eine neue Religionsstiftung betrachtet man das, was die Theosophie bringt. Immer und immer wieder wird der hier oft erwähnte, mißverständliche Gedanke geäußert: die Theosophie sei so etwas wie eine Auffrischung uralter buddhistischer Wissenschaft, statt dem Christentum solle der Welt eine Art Neubuddhismus eingeimpft werden. Was auch immer gesagt werden mag: diese drei Vorurteile er­heben sich immer wieder.",
      "Die Theosophie würde sich an ihrem ersten Grundsatz versündigen, der verlangt, die Eigentümlichkeit einer jeden Geisteskultur zu verstehen, wenn sie eine fremde Geistes-kultur, ein uraltes Religionssystem nach Europa verpflanzen wollte. Jedes Weltanschauungssystem wächst heraus aus den ganzen Bedingungen einer gewissen Volkskultur und kann nicht in eine ganz andere Kultur hinein verpflanzt werden. Wollen wir einen wirklichen geistigen Fortschritt innerhalb unserer Welt, wollen wir der Menschheit mit der euro­päisch-amerikanischen Kultur die Quellen eröffnen für einen Fortschritt in die Zukunft hinein, wollen wir dem modernen Menschen etwas bieten, dann können wir nicht mit Anschauungen und Ideen einer längst verbrauchten Zeit kommen, dann müssen wir alles, was wir an Motiven, an Fragen, an Vorstellungen aufbringen können, dem lebendigen Leben unserer Gegenwart selbst entnehmen. Dann müssen wir da anknüpfen, wo unsere eigene Seele lebt, wo unsere eigene Seele wurzelt.",
      "Nichts Fremdes soll in unsere Kultur verpflanzt werden. Lediglich darum handelt es sich, einzusehen, daß unsere",
      "Kultur einer Vertiefung fähig ist und daß das, was be­gonnen ist mit der äußeren Kultur, bewußt fortentwickelt wird. Jede Kultur ist so anzusehen, daß sie in sich voll ent­wickelte Triebe, gereifte Pflanzen und Früchte enthält, und daneben Keime, die der Mensch fühlt. Der Mensch der Ge­genwart fühlt solche Keime. Diese Keime sitzen in seiner Seele als brennende Zeitfragen, als etwas, was er ersehnt und erhofft in der Zukunft, als Rätsel, die sich ihm auf die Seele legen. Das alles ist in den Seelen der Gegenwarts­menschen verschlossen. Der Keim, der noch eingepflanzt ist in die Erde, muß heraus. Vieles sitzt noch verborgen in der Seele der Gegenwartsmenschen. Es kann um nichts anderes zu tun sein, als das herauszuholen, was in den Seelen der gegenwartigen Menschen ist.",
      "Aber auch mit einem gegenwärtigen Religionsbekenntnis kommt die geisteswissenschaftliche Weltanschauung nicht in Widerspruch. Sie versucht jedes Religionsbekenntnis zu ver­stehen und zu zeigen, wie in allen großen Weitreligionen die eine Urwahrheit der Menschheit lebt. Aber sie geht nicht herum und sucht eklektisch aus den verschiedenen Religio­nen einen Wahrheitskern heraus. Nicht ist sie eine Samm­lerin, diese Geisteswissenschaft, sondern sie ist etwas, was auf eigenem Grund und Boden wächst: etwas, was, wie wir nachher gleich hören werden, nur in der verschiedensten Spiegelung wiedergefunden werden kann in den einzelnen großen Weltreligionen. Nicht herausgeholt aus den großen Weltreligionen ist die Geisteswissenschaft, sondern in den besten Religionen findet man in verschiedener Art das aus­gebildet, was die geisteswissenschaftliche Weisheit uns heute geben kann. Sie soll es uns für die Gegenwart so geben, daß wir es nicht bloß zum Verständnis für die Vergangenheit und Gegenwart haben, sondern daß wir etwas zum Hin­einleben in die Zukunft, zum wahren geistigen Menschheitsfortschritt",
      "haben. Die Geisteswissenschaft will keine neue Religionsstiftung sein.",
      "Lassen Sie uns unbefangen einmal den Gedanken betrach­ten, inwiefern sie keine Religionsstiftung sein kann und warum sie nicht daran denken kann, eine neue Sekte zu stiften. Immer genauer werden die Vorträge dieses Winters zeigen, daß die Zeit der Religionsstiftungen, die Art und Weise, wie die Wahrheit in den Religionen zum Ausdruck gekommen ist, vorüber ist, oder mit anderen Worten, daß die Zeit, wo neue Religionen begründet werden können, vorbei ist. Diese Zeit hat abgeschlossen mit der Zentral-religion des Christentums, denn das Christentum ist einer unendlichen Vertiefung, einer unendlichen Ausbildung für die fernste Zeit der Zukunft fähig. Und die Geisteswissen­schaft wird das Instrument, das Mittel bilden, dieses Chri­stentum den aufgeklärtesten und wissenschaftlichsten Men­schen immer mehr zugänglich zu machen. Zum Verständnis der Religion soll diese Geisteswissenschaft beitragen. Die Weisheit, die in den Religionen liegt, soll sie darbieten. So wird sie das Instrument und das Mittel sein, sich innerhalb des geistigen Lebens zurechtzufinden. Man braucht in der Zukunft keine neuen Religionen. Die alten enthalten das, was sie enthalten können. Weisheit enthalten sie. Aber man braucht die Weisheit in einer neuen Form. Dann wird man die alten Formen auch wieder verstehen, dann werden die alten Religionen durch die Geisteswissenschaft wieder zur wahren Geltung kommen. Jeder Mensch wird wieder zu seiner Religion kommen können.",
      "Bisher hat es in der Gegenwart ein Gefühl gegeben, das sich in den verschiedenen Religionen herangebildet hat:",
      "man hat von Toleranz gesprochen gegenüber den verschie­denen Religionen. Den Menschen, die mit der Gegenwart fühlen, frommt es nicht mehr, mit Haß, Verachtung und",
      "Verfolgung den anderen Religionen zu begegnen. Das ist zu einer Unmöglichkeit geworden. Der Gegenwartsmensch kann die Zeit des Hasses und der Intoleranz nicht mehr recht verstehen, wo im Dienste der Religion ungeheuer viel Blut geflos sen ist.",
      "Zu dulden und zu tolerieren, ist die jetzige Tendenz; das wird eine Zeitlang so gehen. Aber es wird auch eine Zeit kommen, wo dieses Gefühl zu schwach und zu matt ist, um einen wirklichen Fortschritt in die Zukunft zu bewirken.",
      "Für die Zeit des Ubergangs, für das letzte Jahrhundert war dieses Gefühl in gewisser Beziehung ein Segen. Die Duldung ist durchaus berechtigt. Wahre Men­schenliebe und echte Humanität wurden herausgebildet.",
      "Aber was für eine Zeit gut ist, das ist es noch nicht für alle Zeiten. Die verschiedenen Epochen der Weltentwicklung haben verschiedene Aufgaben. Ein Gefühl, das für das neunzehnte Jahrhundert voll berechtigt war, das für das neunzehnte Jahrhundert edle Hoffnungen in den Seelen gestiftet hat, das wird sich matt und unwirksam erweisen für das zwanzigste Jahrhundert.",
      "Dieses zwanzigste Jahr­hundert wird sich zu etwas anderem fähig erweisen. Nicht nur gegenseitige Toleranz und Duldung, sondern vollstän­diges gegenseitiges Verstehen wird es brauchen. Oder war es nicht so, daß bis heute der Christ gesagt hat: Ich ver­stehe nicht den Muselmann, ich verstehe nicht den Be-kenner des jüdischen Glaubensbekenntnisses bis ins Innere, aber wir dulden uns gegenseitig. - Das wird künftig nicht mehr die Menschen trennen.",
      "Künftig wird es nötig sein, sich gegenseitig zu verstehen und sich zu sagen: Ich habe mein Bekenntnis, das aus einer Kulturströmung heraus-gewachsen ist, die mir die Anschauungen, Gedanken und Ideale in mein Seelenblut verpflanzt hat, aber ich muß auch mit anderen menschlichen Geistern im Verkehr sein, muß sie ganz verstehen können. Die Wahrheit, die ich bei mir",
      "finde, soll nicht nur tolerieren und dulden, sondern ein­dringen in das, was die andere Seele fühlt und empfindet. Sie soll Verständnis haben für jedes andere Bekenntnis. -Das ist noch etwas ganz anderes. Das ist eine Aufgabe der geisteswissenschaftlichen Weltanschauung: über die Dul­dung hinauszuschreiten zum völligen gegenseitigen Ver­ständnis. Dann wird der Bekenner einer Religion oder Konfession sich sagen: Die Wahrheit ist mir in einer be­stimmten Form bekannt geworden. Die Wahrheit lebt aber in anderen Seelen in anderer Form. Die Formen haben ge­wiß ihre Berechtigung, sie sollen uns aber nicht trennen. Das, was an Weisheit darin liegt, soll uns verbinden. - In positivem Sinne soll es eine Humanitätsidee sein, die auf Grund von einsichtiger Menschenliebe verbindet und nicht bloß auf Grund von Toleranz. Einsicht ist mehr als Tole­ranz. Einsicht adelt den Menschen mehr als Duldung.",
      "Die Theosophie ist nicht unwissenschaftlich. Als die Theo-sophie vor dreißig Jahren zum ersten Male in die Welt trat, war bei der Gründerin die Aufgabe so gedacht: Dem Menschen der Gegenwart, wie jeder Menschenseele, ist es selbstverständlich, daß man sich die Rätselfragen vorlegt nach dem Unendlichen und Ewigen, die Rätselfragen nach der Bestimmung des Menschen, nach dem Schicksal, die Rätselfragen nach Geburt und Tod und nach dem, was nach dem Tode sein wird, die Rätselfragen: Was bleibt von dem Menschen, wenn er dem physischen Leben abstirbt, woher kommt Krankheit, woher das Leiden? Oh, es gibt keinen Menschen, der diese Fragen nicht aufwerfen müßte. Reli­gionen waren immer dazu da, um geistigen Inhalt zur Be­antwortung dieser Welträtsel in die Seelen zu gießen, damit nicht nur das theoretische Bedürfnis befriedigt werde, son­dern damit die Antwort für die Menschen Kraft, Trost und Zuversicht sei. Oder mit anderen Worten: Der Mensch sollte",
      "aus der Religion eine Antwort bekommen auf die brennen­den Daseinsfragen, damit er mit Ruhe und Sicherheit im Leben sich bewegt, damit er weiß: ich vollbringe, was ich zu vollbringen habe, aber ich sehe auch auf zu den großen Tatsachen der Unsterblichkeit, die jenseits des Alltags lie­gen. Nur ein Mensch - und das wird jeder zugeben müssen, der eine Empfindung hat für die tiefsten Impulse der Seele-, der innerlich befriedigt ist, der harmonisch sich so aufzu­klären weiß, daß diese Rätsel der Welt nicht als bange Sorge und als Unsicherheit in seiner Seele leben, sondern der über die höchsten Fragen der Seele ruhig sein kann, ist stark und hat die Kraft zu leben. Unwissenschaft, Unweis­heit schwächt und macht den Menschen gegenüber der All-tagsarbeit und ebenso gegenüber den wichtigsten Aufgaben des Lebens irre.",
      "Man wird immer mehr und mehr einsehen, daß die Grundlage von Kraft, die Grundlage von Lebensenergie die Weisheit ist, und daß die Weisheit die einzige Grund­lage ist. Zur Erkenntnis dieser Tatsache und zur Befrie­digung der in dieser Tatsache liegenden Fragen ist die theo­sophische Bewegung da. Warum aber, wenn die Religionen in den verschiedensten Zeiten der Weltentwicklung diese brennenden Fragen der Menschheit befriedigt haben, war­um brauchen wir da Geisteswissenschaft? Eben darum, weil die Zeiten sich unterscheiden, weil unsere Vorfahren durch andere seelische Mittel befriedigt werden konnten, als die Menschen der Gegenwart und der Zukunft befriedigt wer­den müssen. Oder war es nicht so und ist es nicht jeden Tag mehr so, daß sie sagen: In der Religion werden viele Fragen des Daseins beantwortet, aber unser Gefühl kann sich nicht mehr befriedigen an der Art, wie sie beantwortet werden. Sie sind hingegangen zu den verschiedenen Religions- und wissenschaftlichen Bekenntnissen. Zahlreiche unserer Zeitgenossen",
      "haben versucht, aus der Naturwissenschaft, aus der Geschichte eine Art Ersatz zu bilden für diejenigen, die vermöge ihres modernen Gewissens sich nicht mehr befrie­digt erklären können von der früheren Art, die Rätselfragen zu lösen. Gar manche, die unbefriedigt sind von der Bibel und der Religion, suchen sehnsüchtig in der heutigen Wis­senschaft. Aber immer mehr und mehr müssen diese letz­teren erkennen, daß für die höchsten Fragen des Daseins gerade die heutige Wissenschaft - deren Größe nicht ver­unglimpft werden soll durch die geisteswissenschaftliche Weltanschauung, sondern vielmehr anerkannt werden soll, da sie so Gewaltiges leistet für die sinnlichen Tatsachen -versagt gegenüber den wichtigsten Fragen des Daseins. So sagt sich mancher: Wenn es sich darum handelt, unsere Erde durch ein Kulturnetz zu umspannen, wenn es gilt, die Erde zu durchforschen bis in die kleinsten Lebewesen hinein, lie­fert uns die moderne Wissenschaft wunderbare Erkennt­nisse. Wenn aber die Menschen fragen nach der Zukunft des Lebens, nach dem eigentlichen Sinn des Daseins, da versagt die Wissenschaft, ja, sie versagt stark. Diejenigen, die es noch nicht probiert haben - und es werden mehr und mehr Menschen versucht haben, mit Hilfe der Wissenschaft das zu probieren, was sie mit Hilfe der Religion nicht erreichen können -, werden es noch einsehen, daß die Wissenschaft in den wichtigsten Daseinsfragen versagt.",
      "Bietet aber nun die Geisteswissenschaft in dieser Richtung etwas? Ja, die geisteswissenschaftliche Weltanschauung ist für die zuletzt angedeuteten Fragen da. Wer sich noch innerhalb der religiösen Traditionen befriedigt fühlt, der wird sich unbefriedigt fühlen von der Geisteswissenschaft, weil er glaubt, daß sie ihm nichts bieten kann, weil er sich einhüllt in das, was ihm die religiöse Tradition geben kann. Was aber heute noch gut für ihn ist, kann es schon morgen",
      "nicht mehr sein. Das war das Ideal der Gründerin der theo­sophischen Bewegung: sichere Erkenntnis über die höchsten Probleme des Daseins zu geben. Wer sich tiefer einläßt in die geisteswissenschaftliche Forschung und Betrachtung, wird sehen, wie keiner wissenschaftlichen Anforderung gegen­über gerade diese geisteswissenschaftliche Forschung sich irgendwie zurückziehen muß. Auf wissenschaftlicher Grund­lage eine allgemein verständliche Weltanschauung zu geben, die für die aufgeklärtesten und auch für die schlichtesten Menschen etwas bieten kann, das wird die geisteswissen­schaftliche Weltanschauung leisten.",
      "Aber man könnte vielleicht doch die Theosophie als eine Art Störenfried ansehen. Sie können vielleicht sagen: Laßt uns doch nur bei unserem alten Glauben, ja, tut etwas dazu, diesen alten Glauben wiederherzustellen! Die Wissenschaft vermag doch keine Antwort zu geben, versucht es doch, wieder den alten Glauben zu stützen! - Solche Menschen be­achten nicht, was um sie vorgeht. Sie sind die wahren Phan­tasten. Die Theosophie will mit offenen Augen in unseren Kulturprozeß hineinsehen. Wir brauchen nur ein Bild vor uns hinzustellen, und es kann ein Beweis sein für die Not-wendigkeit der geisteswissenschaftlichen Weltanschauung.",
      "Werfen wir für zwei Minuten den Blick auf das merk-würdige Land, das eine so eigentumliche religiose Entwick­lung durchgemacht hat im Laufe der letzten Jahrhunderte, auf Spanien. Schauen wir Spanien an, diesen Hort einer orthodox-religiösen Welteinrichtung, nicht nur Weltan­schauung. Dieses Land, wo ein uraltes Religionsbekenntnis eingegriffen hat in die alleralltäglichste Einrichtung, be­findet sich in einer Umbildung. Wer hat denn vor einigen Jahren noch geglaubt, daß in Spanien das eintreten könnte, was wir heute dort sich abspielen sehen. Denken Sie nur einmal daran, daß vor ganz kurzer Zeit in Spanien die",
      "regierenden Mächte nichts haben wissen wollen von irgend­welchen sogenannten modernen Ideen, von irgendwelchen aufklärerischen Ideen, denken Sie an das feste orthodoxe Bekenntnis derjenigen Frau, die als Königin-Mutter dem gegenwärtigen jungen König von Spanien vorangegangen ist, wie wenig sie geneigt war, auch nur ein Tüpfelchen ab­zugehen von dem, was sich seit Jahrhunderten fest ein­gebaut hat in das Gefüge eines ganzen Staates. Denken Sie sich den Kontrast: Diese Frau sitzt in Lourdes, da, wo sie Befriedigung in der alten Weise in vollen Zügen zu schlür­fen versucht und die alten Wahrheiten an sich herantreten läßt - und in Spanien muß der junge König es zugeben, daß mitten in das feste Gefüge hinein neue Ideen eintreten.",
      "Er mußte es zugeben, daß ein liberaler Minister an den Ein­richtungen rüttelt, daß an der Unterrichts- und Ehegesetz­gebung gerüttelt wird, und, wie es scheint, in unbarmherzi­ger Weise. Das sind die Zeitströmungen, und gegen solche Zeitströmungen vermag keine menschliche Meinung etwas.",
      "Dagegen vermag nur das Verständnis etwas. Wie lassen doch die Menschen heute diese Zeitströmungen an sich heran­kommen. Wie stehen manche mit verbundenen Augen sol­chen Erscheinungen gegenüber, ganz unvorbereitet, wie las­sen sie sich überraschen, frappieren und schockieren.",
      "Wie üben sie Kritik an den Zeitströmungen, wie kommen sie nicht weiter, als daß sie sagen: wir müssen die alten Formen stützen. Wie begreifen sie gar nicht, daß die Zeitströmungen stärker sind als die phantastischsten Meinungen.",
      "Sie be­greifen nicht, daß es nötig ist, mit hellem Blick und offenem Auge zu sehen, was die Menschen nötig haben. Die Men­schen sind heute nicht mehr so unbewußt, alles über sich ergehen zu lassen. Sie sind dazu berufen, diese Zeitbewegun­gen zu verstehen und ihnen selbst die Richtung zu geben.",
      "Jeder einzelne ist dazu berufen, erkennen zu lernen, was in",
      "solchen Zeitströmungen liegt und wie diese zu einem ge­deihlichen Fortschritt in der Zukunft gebracht werden kön­nen. Die Menschen machen Geschichte, und wenn gegen die Menschen Geschichte gemacht werden soll, so kommt das Chaos. Nur aus dem Miteinander kann Recht und Har­monie kommen. Die Zeit gibt schon die Notwendigkeiten:",
      "an den Menschen ist es, sie zu verstehen. Nicht in bequemer Weise soll der Mensch die Dinge an sich herankommen lassen. Da würde er nur zu Ballast in der Entwicklung. Die Zeitströmungen kann man aber nicht übersehen, wenn man nicht einen Blick in das Übersinnliche hinein zu tun ver­mag. Der Mensch ist dazu berufen, das Übersinnliche in sein Herz, in sein Gemüt und in seine Seele aufzunehmen, so daß es durch ihn in der Welt wirkt.",
      "Nun versuchen wir einmal, uns diese Frage, die sich aus der eben gemachten Betrachtung ergibt, so recht vor die Seele hinzumalen. Was ergibt sich für den denkenden Men­schen aus dem, was wir gehört haben? Es ergibt sich sehr viel daraus. Wer eine Einsicht hat in das geistige Leben, der weiß eines: daß es keine gedeihliche materielle Kultur geben kann ohne die Grundlage eines wirklichen geistigen Lebens. Nie hat es einen Staat, nie hat es eine Volksgemeinschaft gegeben ohne eine wirkliche religiöse Grundlage. Es sollte nur jemand einmal ernstlich versuchen, eine Kolonie zu begründen mit Menschen, die nur matierelle Interessen haben und die nur eine materialistische Weltanschauung haben, die also nichts mitbringen als das, was man heute innerhalb der materialistischen Weltanschauung gelten las­sen will, die nichts von dem Übersinnlichen kennt. Man versuche eine solche Kolonie zu begründen. Allerdings, es bringen die Menschen ja doch die Reste idealer Gedanken und Ideen mit. Wären die nicht mehr da, so würde es schnell in ein vollständiges Chaos ausarten. Sie können kein",
      "soziales Leben begründen ohne weisheitsvolle religiöse Grundlage. Der ist ein schlechter Praktiker, der mit der Praxis allein auszukommen glaubt. Wollen Sie das mate­rielle Dasein der Menschen immer mehr fördern, so müssen Sie daran denken, daß die Seele jeder materiellen Kultur nur die Religions- und Erkenntnisgrundlage sein kann. Wenn Sie den Menschen Brot geben wollen, so müssen Sie ihnen zuerst etwas geben für die Seele. In der Zeitschrift «Luzifer» habe ich den scheinbar grotesken Satz ausgespro­chen, daß man niemand Brot geben kann, ohne daß man ihm Weltanschauung gibt, da das Brotgeben ohne geistige Nah­rung zum Unheil führt. In jenem Aufsatz haben Sie das mehr oder weniger bewiesen.",
      "Wie müßte es aber in der Gegenwart sein, wenn ein ge­deihlicher Fortschritt stattfinden sollte angesichts des Ereig­nisses in Spanien, welches nur in besonderer Weise das zum Ausdruck bringt, was sich überall vollzieht, was aber nur der übersehen könnte, der den Kopf gegenüber dem Leben in den Kultursand stecken würde wie der Vogel Strauß. Ebenso wie es auf allen Lebensgebieten Kundige gibt, die uns mit Kleidern versorgen und andere Bedürfnisse des Lebens befriedigen helfen, so gibt es auch Kundige auf dem Gebiete des Seelenlebens, auf dem Gebiete des Übersinn­lichen. Das Vertrauen zu den Priestern und Weisen war es, was die Kulturen begründete. Nicht haben wir ein Recht, die verflossene Kultur zu kritisieren. Sie war so gut, wie sie für ihre Epoche sein konnte. Wenn die Kulturen jetzt nicht mehr passen, so liegt es nicht daran, daß sie zu bekämpfen sind, sondern daran, daß die Menschheit eine Fortentwick­lung braucht in der geistigen Wahrheit, weil die Menschen nicht mehr unter den alten Formen des geistigen Lebens leben können. Ebenso wie der Mensch, der früher zu dem Priester ging, Worte des Trostes und der Sicherheit erhielt,",
      "ebenso müßte es in unserer Zeit Menschen und Forscher geben - ja, es muß sie geben -, an die man sich zu halten hat, die einem die Wahrheit in der neuen, der Gegenwart entsprechenden Form sagen können, die einem wieder etwas sagen können von dem Übersinnlichen, in einer Form, wie der moderne Mensch es glauben kann.",
      "Fragen wir uns einmal, wie könnte sich die Gegenwart in bezug auf diese Sache stellen, wenn alles so bliebe, wie es von zahlreichen unserer Zeitgenossen für richtig befunden wird. Sie sehen da etwas, was als Symptom in bezug auf Spanien erwähnt worden ist. Sie sagen vielleicht: die alten Formen werden sich auflösen, und der Mensch wird in neue Ordnungen hineinwachsen. Diese neuen Ordnungen werden aber nie gedeihen können, wenn nicht ein Seelisches hinein-kommt, wie das Lebensblut, wenn nicht etwas Geistiges unsere ganze Kultur durchpulsen kann. Können die Men­schen, die sich heute voneinander entfernen in bezug auf ihre Meinungen über die Seele und in bezug auf die Ein­richtungen, an einen Ort hingehen und sich Rat holen in",
      "bezug auf die höchsten Fragen des Daseins?",
      "Betrachten wir die Sache an einem charakteristischen Symptom unserer Zeit. Von der Naturwissenschaft, von der Erkenntnis der äußeren sinnlichen Tatsachen, der positiven Tatsachen, erwarten viele einen Ersatz für die alte religiöse Anschauung. Vor einigen Tagen hat eine Naturforscherver­sammlung in Stuttgart stattgefunden. Können wir uns sagen, daß der moderne Mensch, mit seinen Bedürfnissen und Sehnsüchten gegenüber dem Ewigen, gegenüber dem, was der Tod besagt, hinschauen kann zu dem modernen Areopag des Geisteslebens, wenn er Antwort braucht und wenn die geistige Entwicklung ihren Fortgang nehmen soll? Es sind gewaltige Fragen besprochen worden auf dem Kon­greß in Stuttgart. In den erstaunlichsten Dingen lebt sich",
      "der menschliche physische Forschergeist bei einer solchen Gelegenheit aus. Für den, der eine Empfindung dafür hat, sei es erwähnt: man sprach über solche Vorstellungen wie die Verpflanzung eines Organs des einen Lebewesens auf ein anderes. Es wurde genau besprochen, wie die Verpflan­zung eines Bestandteiles eines Lebewesens in ein anderes Lebewesen hinein stattfinden kann, dem dieser Bestandteil fehlt. Oder ist es nicht interessant, zu sehen, wie die Natur­forschung durch die Errungenschaft des Mikroskopes alles bisher Dagewesene überboten hat? Ist es nicht bewunderns­wert, zu sehen, wie aus gewissen Mischungen und Lösungen heraus man aus der toten Substanz etwas entstehen läßt, was, mit dem Schein des Lebens begabt, sich herausent­wickelt aus der toten Substanz wie der scheinbar tote Kri­stall. Vieles ließe sich noch anführen, was uns zeigen könnte, welchen Respekt und welche Achtung uns diese moderne Naturforschung abnötigen kann.",
      "Nun aber kommt der Mensch heran und fragt sich: Wozu ist dieses ganze Leben? Welches ist der Sinn von alledem, was sich in so wunderbaren Formen für die physischen For­scher darstellt? Gibt es in dem Reiche derjenigen, die in dem Areopag des Geisteslebens sind, auch solche, die Antwort geben auf die letzten Fragen?",
      "Auf dem letzten Naturforscher-Kongreß hatte man auf solche Fragen keine Rücksicht genommen. Noch vor zwei Jahren hat ein Breslauer Chemiker eine merkwürdige Rede gehalten, wonach alles abgelehnt werden soll, was dem Menschen in psychischer Weise zu erforschen möglich ist. Das war Ledebur, der Breslauer Chemiker. Theodor Lipps durfte jetzt über Naturwissenschaft und Philosophie spre­chen. Das ist ein beachtliches Zeichen, daß es möglich war, in einer naturwissenschaftlichen Versammlung das zu bieten, was Lipps geboten hat. Es war ihm möglich, mitten in diese",
      "rein positive Forschung solche Worte hineinzuwerfen wie:",
      "Die Naturwissenschaft kann sich niemals zu einer Welt­anschauung erheben, wenn sie nicht zu einer geistigen Durch­dringung der menschlichen Erscheinung kommt. Wenn der Mensch in sich hineinsieht, so findet er das Ich, und wenn er das dann ausdehnt zu einem Welten-Ich, dann kann er zu einiger Befriedigung kommen.",
      "Es ist ein sonderbares Gefühl, das derjenige, der sich mit diesen Dingen beschäftigt hat, gegenüber einer solchen Tat­sache haben muß. Da gibt es seit dreißig Jahren eine theo­sophische Bewegung, die nicht bloß in ganz allgemeiner, platter Weise die großen Fragen beantwortet, sondern in konkreter Weise sich einläßt auf das Schicksal des Menschen vor der Geburt und nach dem Tode, sich einläßt auf das, was sich dem Menschen bietet in der geistigen Welt, wenn ihm das Auge dafür geöffnet ist. Kurz, nachdem es dreißig Jahre eine solche Vertiefung gegeben hat, kommt einer ein­mal zum Wort, der in den allerelementarsten und aller­trivialsten Begriffen etwas bietet, was überhaupt noch kei­nem Menschen eine Befriedigung geben kann, weil es sich gegenüber den unmittelbaren großen Lebensfragen wie ein Begriffsgespinst, wie etwas ganz Abstraktes, Weltfernes ausnimmt. Wer sich nicht mit Fachphilosophie beschäftigt hat - welchen Begriff die Philosophie erst herausgearbeitet hat-, für den ist das nichts anderes als ein abstraktes Wort-gespinst, bei dem er sich nichts denken kann. So sehen Sie, daß im offiziellen Leben, wo die Menschen dennoch Trost und Lösung suchen für die Lebensrätsel, nichts geboten werden kann, aus Unvermögen, aus Unverständnis gegen­über den wirklich höchsten Fragen.",
      "Und doch, es muß für die äußere Kultur, die alle Formen zersprengt, ein solches Lebenszentrum geben, aus dem gei­stiger Inhalt herkommen kann, nicht bloß wertlose Wortgespinste,",
      "sondern lebendige Erkenntnis des Übersinnlichen. Diese muß, von den geistigen Führern der Gegenwart her, eindringen in das, was sich als Rest des geistigen Inhalts in den alten Formen erhalten hat. Wenn von einer solchen Stätte aus, in derselben logischen Weise, in der die Wissen­schaft spricht, über die übersinnliche Welt eine entsprechende Botschaft verkündigt werden kann, dann wird sich das -wie die alten Religionen sich ergossen haben - ergießen in die Seelen und äußeren Einrichtungen. Dann werden - das werden Sie sehen - die vermaterialisierten alten Religions­formen verschwinden und neue Formen werden sich bilden.",
      "Man soll sich aber keiner Illusion hingeben über die Be­deutung dieser geistigen Kultur. Es gibt viele - und in Frankreich ist das Wort dieser vielen tonangebend gewor­den -, die sa sagen, der Mensch braucht seine Moral gar nicht aus etwas wie Religion heraus zu bilden. Sie sagen:",
      "Es gibt eine menschliche Moral und die kann begründet werden ohne ein Religionsbekenntnis. Die, welche so spre­chen, haben die eigentlichen geistigen Gesetze wenig kennen­gelernt. Wenn Sie den Gang der Geisteskultur seit alten Zeiten verfolgen, so werden Sie sich sagen können: Die verschiedenen aufeinanderfolgenden Kulturepochen der Menschheit haben der Menschheit verschiedene Inhalte ge­bracht. Was hat die Hermes-Kultur den Agyptern, was die Kultur der indischen Rishis den Hindus, was der Zarathu­strismus den Persern, was die Kultur des Moses den Juden gebracht, und was endlich die Kultur des Christus Jesus, des größten Religionsstifters, der modernen Zeit? Jede Kultur-strömung hat ihre Bedeutung in ihrer Zeit gehabt. Und groß sind sie gewesen, weil ihre Missionare es verstanden haben, die Bedürfnisse ihrer Zeit zu verstehen. Richtig wer­den die Missionare der Zukunft wirken, welche die Herzen der Menschen wieder verstehen und in sie hineinwirken",
      "können. Verschiedene Formen haben wir für die verschie­denen Zeiten, in immer neuer Gestalt erscheinen die alten Wahrheiten.",
      "Das erste, was jeder neuen Gestalt einer Kultur zugrunde liegt, ist ein Bekenntnis, eine Summe von Anschauungen, von Empfindungen und Vorstellungen über das Höchste und das Übersinnliche, ein Wissen des Menschen von den göttlichen Grundlagen der Welt, ein Wissen des Menschen über das, was den Tod besiegt. Und jede große Kultur-epoche hat aus diesen Grundlagen heraus die Kraft zum geistigen Schaffen gezogen. Niemals wäre das zustande ge­kommen, was im alten Agypten, in Indien und Vorderasien, in Griechenland und endlich in den christlichen Zeiten ent­standen ist, wenn es nicht aus dem herausgewachsen wäre, was die Menschen geglaubt und gedacht haben. Das Aller­materiellste ist nur ein Ergebnis dessen, was der Mensch weiß über das Übersinnliche. Das erste in jeder Kultur-strömung ist also das Bekenntnis.",
      "Das zweite ist, wie dieses Bekenntnis auf das Gefühl und die Gemüter wirkt. Die Gedanken und die Vorstellungen, die sich der Mensch macht über das Übersinnliche, üben einen Eindruck auf die Seele aus und erheben sie, und alle höhere Lebensfroheit und Harmonie gießt sich in die Seele unter dem Einflusse des Bekenntnisses. Wo jemals Menschen froh gewesen sind im höchsten Sinne, wo sie jemals Sicherheit gehabt, jemals in ihre Empfindungen sich etwas hinein-gegossen haben, so daß sie sich sagen konnten, ich weiß, daß ich eine höhere Bestimmung habe, und wo sich dieses Wissen umgewandelt hat in ihrer Seele in eine befriedigende Le­bensfreude und Lebenszuversicht, da war es immer unter dem Eindruck eines Bekenntnisses.",
      "Das erste also ist das Bekenntnis selbst, das zweite ist die Welt der Gefühle: Erhebung, Lebensfreude und Lebenssicherheit.",
      "Und so ist das dritte die Welt der Willens-impulse, die Welt der Moral und der Ethik. Die Sitten-lehren bilden die Kunst - etwas, was zum zweiten Teil gehört -, das Moralische und das Willenselement, die Welt der Sittlichkeit und Gesetzgebung und alles staatlichen Zu­sammenlebens. Es ist eine große Täuschung, wenn jemand sich dem Glauben hingibt, daß es jemals eine Sittlichkeit, eine Moral geben kann, die nicht herausgewachsen ist aus der Grundlage eines Bekenntnisses, aus der Grundlage der Gefühlssphäre. Als erstes hat der Mensch eine Meinung über das Übersinnliche, als zweites Lebensfroheit und Zuver­sicht, und als drittes die Impulse für seine Handlungen, das, was ihm sagt: das ist gut, das ist böse.",
      "Wie kommt es, daß viele den Glauben haben - was eine Illusion ist -, daß man Moral begründen kann ohne Be­kenntnis, das heißt eine bodenlose Moral? Das kommt davon her, daß die Moral, dieses dritte in einer Kultur-strömung, das letzte ist, was verschwindet. Wenn eine Kulturströmung abflutet, flutet zuerst das Bekenntnis ab. Zuerst glaubt man nicht mehr die Dinge, die in dem Be­kenntnis gegeben werden. Wenn aber lange schon nicht mehr der lebendige Glaube da ist, der den Menschen mit absoluter Sicherheit auf die Formen hinblicken läßt, dann sind noch immer die Empfindungen und Gefühle da, die sich in diesem Glauben ausgebildet haben. Und wenn auch diese Gefühle nicht mehr da sind, wenn der Mensch nicht mehr die ererbte Freudigkeit haben kann, dann ist noch immer die Moral da. Heute stehen die, welche glauben, eine solche bodenlose Moral gründen zu können, nicht auf dem Boden einer bodenlosen Moral. In Wahrheit leben sie unter den Resten der Moral und der Weltanschauung, die ihnen aus dem Bekenntnis geblieben sind als ererbte Stücke der Kultur.",
      "Diejenigen, welche sagen, alles Übersinnliche sei unzu­gänglich für den Menschen, alles Übersinnliche sei phan­tastisch, die handeln so, wie sie es tun, weil in ihnen noch die Moral der Vorzeit lebt. Viele Menschen gibt es, die das Bekenntnis glauben überwunden zu haben, doch stehen sie alle noch unter der Moral, die ihnen das Bekenntnis ge­geben hat.",
      "Es gibt viele Sozialisten, die eine Moral begründen wol­len, eine Moral, die aus dem Nichts heraus geboren ist. Warum können sie aber überhaupt über Moral reden? Warum verschwindet denn nicht alle Moral in ein Chaos hinein? Weil sie die alte Moral, die sie bekämpfen, noch in ihren Gliedern haben, weil sie eben staatliche Anderungen auf der Grundlage der überkommenen staatlichen Moral herbeiführen wollen. Sie ist hervorgewachsen aus der Ver­gangenheit. Daher wird ein Fortschritt erst unter der Er­neuerung der Erkenntnis des Übersinnlichen möglich sein, der übersinnlichen Welt, wenn es möglich ist, dem Menschen etwas zu geben, was ihn hinaufweist in die übersinnliche Welt, was ihn bekannt macht mit den Kräften, die uns um­geben und die hineinspielen in die Welt, die um uns ist. Ist es möglich, ihm diese Weisheit des Übersinnlichen zu ver­mitteln, dann wird dies eine Gefühlswelt der Lebenssicher­heit und eine Moral begründen mit Impulsen für das Han­deln. Dann leben wir nicht mehr von ererbten Gütern, son­dern von dem, was aus der Zeit, in der wir leben, selbst entsprießen kann.",
      "Diese Erkenntnis des Übersinnlichen, welche die geistes­wissenschaftliche Weltanschauung geben will, verstößt gegen keine Logik. In welchem Sinne spricht sie von einem Über­sinnlichen? Spricht sie davon, daß in einem Jenseits oder an einem unbekannten Orte das Geistige ist? Merkwürdig, es werden Weltanschauungen gestiftet, die behaupten, daß ein",
      "Jenseitsglaube alle Kultur vernichten müsse. Nun, alle solche Anschauungen wissen nicht, in welchem Sinne die wirkliche Geistesforschung von diesem Übersinnlichen spricht. Öfters ist das hier schon durch Vergleiche klargemacht worden, wie und in welchem Sinne die Geistesforschung von einem sol­chen Übersinnlichen spricht. Dieser Vergleich soll zum Schluß noch einmal vor unsere Seele hintreten.",
      "Für einen Menschen, der blind geboren ist, ist die Welt der Farben und des Lichtes ein Jenseits der für ihn wahr­nehmbaren Welt. Wodurch ist eine Welt für den Menschen da? Lediglich dadurch, daß er Organe hat für diese Welt. In dem Augenblicke, wo dem Blindgeborenen das Auge geöffnet wird, muß er sich nicht mehr bloß von anderen Menschen sagen lassen, es gibt Licht und Farbe, sondern da tritt eine neue Welt, die immer da war, vor sein Auge. Nichts anderes sagt die Geisteswissenschaft, und von nichts anderem handelt sie. Wenn sie von anderen Welten spricht, so spricht sie davon in genau demselben Sinne wie in dem Vergleich von der Welt der Farben und des Lichtes gegen­über dem Blindgeborenen. Der Geistesforscher sagt, daß eine Welt für ihn dann da ist, wenn ein Organ für sie da ist. Die übersinnliche Welt ist dem Menschen der Gegen­wart verschlossen, weil bei ihm keine Organe dafür vor­handen sind. Sie verhält sich nicht anders für ihn, als sich die Welt der Farben und des Lichtes für den Blindgebore­nen verhält.",
      "Hier sind nicht nur Gegenstände, die der Mensch mit dem Verstande und mit den Sinnen erfassen kann, hier sind noch ganz andere Wesenheiten. Indem Sie durch den Saal schreiten, schreiten Sie durch eine Welt des Geistigen, wie der Blinde, der die Stühle und Bänke nur tasten kann, durch eine Welt von Farben und Licht schreitet, ohne sie sehen zu können. Wie es von einem Blinden ein logisches Unding",
      "wäre, nachdem er gehört hat, daß es Farbe und Licht gibt, zu sagen, das sei Phantasterei, ebenso ist es unlogisch, daß der, welcher nicht übersinnlich sieht, sagt, es sei Phan­tasterei. Es hat immer Leute gegeben, welche mehr sehen konnten als die Mitmenschen. Eingeweihte oder Initiierte hat man solche Menschen genannt. Es sind das Menschen, die eine Art geistiger Neugeburt erlebt haben und von denen in allen Religionen erzählt wird. Es gibt einen gei­stigen Augenblick im Leben eines solchen Menschen, der eine viele größere Bedeutung hat als die physische Geburt. Dieser geistige Augenblick besteht darin, daß der Mensch, der sein geistiges Auge und sein geistiges Ohr eröffnet hat, eine ganz neue Welt wahrnehmen kann, daß er sich bis zur übersinnlichen Welt hinaufentwickelt hat. Diejenigen, welche von der übersinnlichen Welt zu sprechen berechtigt sind - die Stifter der Religionen -, haben zu den Menschen in demselben Sinne gesprochen, wie der Sehende zu dem Blinden vom Licht spricht und ihm davon erzählt.",
      "Neuerdings dringt die Botschaft von der übersinnlichen Welt wieder an die Menschen heran durch die Geisteswissen­schaft. Dies geschieht in keinem anderen Sinn, als indem sie den Menschen zeigt, daß es immer Erleuchtete, Erfahrenere gegeben hat, die hineinschauen konnten in die übersinnliche Welt, und daß es heute noch Menschen gibt, die das geistige Auge offen haben, die die geistigen Eigenschaften der sinn­lichen Dinge sehen. Sie zeigt, daß es Menschen gibt, die hinter die Pforte des Todes schauen können, die sehen können, welches der unsterbliche Teil des Menschen ist, was übrigbleibt von dem Menschen, wenn er durch die Pforte des Todes schreitet. Über dieses alles in Einzelheiten aus der For­schung heraus Nachricht zu geben, ist unsere Aufgabe. Sie sind dazu berufen, einen neuen Mittelpunkt zu bilden, von dem aus die Menschen hören werden von der geistigen Welt.",
      "Es ist billig zu sagen: Gebt mir die Mittel, selbst hinein-zuschauen. Jeder kann die Mittel haben, wenn er sich an die richtige Quelle wendet. Durch die geisteswissenschaftliche Weltanschauung wird jedem die Möglichkeit geboten.",
      "Die erste Stufe ist aber, mit der heutigen Anschauungsweise sich zu erheben zu folgendem Gedanken, der sich in dem Men­schen ausbildet: Ich höre von einem Mitmenschen, daß er hineinschauen kann in die übersinnliche Welt, ich höre, daß er mir sehr viel zu sagen versteht über die übersinnliche Welt, er erzählt im einzelnen, wie es nach dem Tode aus­schaut, wie Kräfte und Wesenheiten die Welt durchpulsen, Kräfte und Wesenheiten, die dem gewöhnlichen Auge noch verschlossen sind. Ich kann zwar noch nicht hineinschauen in diese Welt, aber ich will meine Ahnung fragen, ob der Mann mir etwas Unwahrscheinliches sagt.",
      "Ich will meine Empfindung fragen, ob das nicht höchst wahrscheinlich klingt, wenn ich mich nicht durch materialistische Anschau­ungen abhalten lasse, ob das unbefangen klingt, was der Betreffende sagt. Dann will ich die Gedankenlogik zu Hilfe nehmen und sehen, ob er nicht etwas sagt, was das Leben erklärlich machen kann.",
      "Dann will ich noch weiter gehen. Ich will sagen, ich habe dich ruhig angehört, denn du hast etwas gesagt, was mit der Logik stimmt. Jetzt will ich das Schicksal des Menschen betrachten, will sehen, ob es mir erklärlich wird, wenn ich so die Welt betrachte.",
      "Indem ich mir also sage: nehmen wir einmal an, die Anschauung der Geisteswissenschaft wäre richtig, erklärt sie das Leben, wird das Leben verständlich? so prägen sich die Gedanken in meine Seele ein: ich will versuchen, im Leben zu erproben, ob sie Lebensfroheit, Lebenssicherheit, Lebenskraft gibt. So will ich Stück für Stück erproben, ob eine innere Möglich­keit besteht, das anzunehmen, was der Eingeweihte sagt.",
      "Ich will mich auf einen solchen Standpunkt stellen, wie sich",
      "eine merkwürdige Persönlichkeit in bezug auf die gewöhn­liche Welt des Lichtes und der Farben gestellt hat.",
      "Öfters wurde schon das Leben der taubstummen und blin­den Helen Keller erwähnt. Das ist eine Persönlichkeit, die mit sieben Jahren noch wie ein kleines wildes Tier war, die aber eine geniale Erzieherin gefunden hat, so daß sie so weit gekommen ist, daß sie nicht nur eine Durchschnitts­bildung hatte, sondern sich messen konnte mit manchem gebildeten Menschen. Niemals ist sie imstande gewesen, Töne zu hören, Farben zu sehen, Licht wahrzunehmen. Fin­sternis und Stummheit lagerte um ihre Seele. Aber sie hat das, was andere Menschen von Farbe, Licht und Ton wahr­genommen haben, auf ihre Seele wirken lassen. Von ihr ist ein neues Büchelchen erschienen: «Optimismus». Sie zeigt darin, daß sie nicht nur unser Wissen aufgenommen hat, sondern auch von der Sprache und dem Wissen der Griechen und Römer. Sie spricht von den schönsten Schöpfungen des Hörens und Sehens, obgleich sie selbst nichts wahrgenom­men hat. In ihrer Seele hat sich nicht nur so etwas aus­gebildet wie Wortvorstellungen, sondern das Büchelchen über den Optimismus zeigt, daß sie Kraft und Sicherheit erhalten konnte aus den Mitteilungen der Sehenden um sie herum.",
      "So vermag der Mensch, wenn er sich nicht verschließt gegenüber den geistig Sehenden und Hörenden, Kraft und Sicherheit und Hoffnung für die Zukunft zu erhalten. Dis­harmonie macht schwach und kraftlos für das Leben. Sehend wird der Mensch für seine Umgebung, wenn er auf die Sehenden hört. Wissend wird er und frei handelnd, wenn er denen, die Kunde geben können, folgen kann. Das Leben vermag er in den Dienst des Übersinnlichen zu stellen. Eine neue Kultur aus dem Übersinnlichen heraus muß, wie das Lebensblut, den Staat und die gesellschaftlichen Formen",
      "durchdringen. So hängt die Erkenntnis des Übersinnlichen in der Gegenwart mit großen Lebensfragen zusammen. Wenn die großen Lebensfragen in den verschiedensten For­men von allen Seiten uns entgegendrängen, dann muß man erkennen, daß man etwas braucht, was einen tiefer hinein-führt in das Verständnis des Lebens. Aus einer propheti-schen Voraussicht gegenüber dem, was kommen muß, ist die geisteswissenschaftliche Weltanschauung herausgegriffen, herausgeschaffen. Das soll uns die Serie von Vorträgen des Winters zeigen in bezug auf die Fragen der großen Kultur-strömungen und auch in bezug auf die einzelne Seele, die still und schlicht im häuslichen Heim schaffen muß vom Morgen bis zum Abend. Jede Seele findet in der Geistes-forschung etwas, wodurch sie Kraft und Sicherheit, innere Befriedigung, Lebensmut und Lebensfreude finden kann und auch das Notwendige zu einem wirklich gedeihlichen Menschheitsfortschritte.",
      "Wenn auch noch manche da sind, welche über die geistes-wissenschaftliche Erkenntnis des Übersinnlichen lächeln und als Praktiker, die sie sein wollen, sagen: was haben wir zu tun mit dem unpraktischen Zeug - die geisteswissenschaft­liche Bewegung wird arbeiten und eine Zeit wird kommen, wo auch solche, die heute noch zu den Zweiflern und Klein­mütigen und Ungläubigen gehören, hinsehen werden auf diejenigen, die als Samen gesät worden sind, weil sie ge­braucht werden zur Lösung der großen Fragen und Rätsel, die auf der Seele lasten werden. Immer mehr und mehr werden sie gebraucht werden für den Menschheits fortschritt schon in der nächsten Zukunft für die Fragen, die nicht menschlich willkürlich sind, sondern durch das Leben mit starker Kraft gestellt werden."
    ],
    "sentences": [
      [
        "Der heutige Vortrag ist eine Art Programm, und die fol­genden sollen zwei Ziele verfolgen: Das erste Ziel ist, die Zuhörer bekannt zu machen mit dem, was die Geistesforschung über die Welt des Geistes in bezug auf den Men­schen, in bezug auf die Entwicklung des Menschen, in bezug auf Leben und Bestimmung des Menschen, in bezug auf Geburt und Tod, Ursprung des Lebens, Ursprung des Bösen, Gesundheit und Krankheit und in bezug auf Erziehungs­fragen bieten kann.",
        "So daß im Laufe des Winters der Um­fang dieser Geistesforschung sich vor unsere Seele stellen soll."
      ],
      [
        "Andererseits aber sind die Vorträge so eingerichtet, daß die Beziehung der gegenwärtigen geisteswissenschaftlichen Forschung zu den großen Kulturaufgaben, zu den brennen­den Zeitfragen, zu den großen Lebensfragen des Daseins, wie sie von der Gegenwart gestellt werden, besprochen wird.",
        "Es soll die Geisteswissenschaft nicht wie irgendeine Theorie hingestellt werden, sondern sie soll als etwas er­kannt werden, das sich in das ganze Leben eines Gegen-wartsmenschen mit einer gewissen inneren Notwendigkeit hineinstellt.",
        "So sehr auch das Alter der Zuhörer verschieden sein wird, durch die Mannigfaltigkeit der Themata wird vielleicht doch für jeden etwas Interessantes dargeboten werden können."
      ],
      [
        "Ich möchte nun, bevor ich zum Vortrage selbst übergehe,"
      ],
      [
        "die einzelnen Themen, die als Einzelvorträge etwas in sich Abgeschlossenes und auf der anderen Seite doch ein zusam­menhängendes Ganzes bilden sollen, nochmals erwähnen.",
        "Vorerst wollen wir diesmal, weil es nicht so bequem ist wie im vergangenen Winter, sehr darauf achten, daß die Vorträge stattfinden werden am zweiten und dritten Donnerstag eines jeden Monats.",
        "Am 25. werden wir zu sprechen haben über das Thema «Blut ist ein ganz besonderer Saft».",
        "Da werden wichtige Kulturfragen der Menschheitsentwicklung zur Sprache kommen, im Anschlusse an eine vielleicht nur vom geisteswissenschaftlichen Standpunkte aus zu beleuch­tende intime Lebensfrage.",
        "Es ist dabei nicht darauf ab­gesehen, eine sensationell aussehende Frage aufs Tablett zu heben.",
        "Dann folgt «Der Lebenslauf des Menschen vom gei­steswissenschaftlichen Standpunkt», dann «Wer sind die Rosenkreuzer?», dann «Richard Wagner und die Mystik», dann «Was wissen unsere Gelehrten von der Theosophie?» und dann die religiöse Frage «Bibel und Weisheit»."
      ],
      [
        "Diejenigen der verehrten Zuhörer, welche im verflossenen Winter schon hier versammelt waren zu den geisteswissen­schaftlichen Vorträgen, werden manches Bekannte in etwas anderer Beleuchtung finden.",
        "Aber die Dinge der geistes-wissenschaftlichen Forschung werden der Seele erst ganz zu eigen, wenn sie von den verschiedenen Seiten beleuchtet werden.",
        "Deshalb bitte ich, wenn Sie Bekanntes hören, es hinzunehmen, da es sich um den einführenden Vortrag zu dem ganzen Programm des Winters handelt.",
        "Dieser heutige Vortrag soll eine Art Versprechen sein.",
        "Es soll versprochen werden, was die folgenden Vorträge einlösen sollen.",
        "Es soll hingewiesen werden auf das, was man geisteswissenschaft­liche Forschung innerhalb der Gegenwart nennt, und dar­auf, daß diese Erforschung des geistigen, übersinnlichen Lebens eine große einschneidende Bedeutung für unsere"
      ],
      [
        "Gegenwart hat und berufen ist, eine immer einschneiden­dere Bedeutung für das Leben der Menschen in der Zukunft zu bekommen."
      ],
      [
        "Es ist erst dreißig Jahre her, seit eine theosophische Be­wegung durch die Welt geht.",
        "Und nach diesen dreißig Jah­ren ist die Theosophie nicht etwa eine geistige Bewegung, die sonderlich angesehen ist.",
        "In den weitesten Kreisen drau­ßen versteht man unter Theosophie nicht irgend etwas, was man als auf wirklichem, tatsächlichem Boden stehend an­sieht.",
        "Viele sind unter unseren Zeitgenossen, die die Theo-sophie als etwas Phantastisches, als etwas, was sich in einem Wolkenkuckucksheim ergeht, ansehen.",
        "Nicht zu leugnen ist, daß die Theosophie, durch unkundige und vielleicht auch durch vorschnelle, dilettantische Persönlichkeiten, vielleicht sogar durch scharlatanhafte Seelen mit einem gewissen Recht an ihrem Ansehen verloren hat.",
        "Die Frage, was die Theo-sophie dem Menschen der Gegenwart aber doch bedeuten kann, soll uns heute hauptsächlich beschäftigen."
      ],
      [
        "Manche große Vorurteile sind verbreitet gegenüber der theosophischen Weltanschauung.",
        "Da sagt der eine: Ach, die Theosophie ist etwas, was so ähnlich ist wie der Spiri tismus, also etwas, was sich mit unserer heutigen abgeklär­ten, wissenschaftlichen Weltanschauung durchaus nicht ver­trägt.",
        "Die Theosophie ist etwas, was höchstens für Träumer eine Bedeutung haben kann, was aber mit den wissenschaft­lichen, logischen Gesetzen in Widerspruch steht.",
        "So sagen diejenigen, welche entweder selber auf dem Boden der Wis­senschaft stehen, oder welche sich sagen: Wissenschaft ist die Losung der Zeit, wir müssen auf sie hören, sie zeigt uns die tiefen Fragen des Daseins, und es ist eine Versündigung, wenn wir gegen die wohlbegründeten Ansprüche der Wis­senschaft verstoßen und uns dem hingeben, was unwissen­schaftlich ist."
      ],
      [
        "Ein anderes Vorurteil kommt von der religiösen Seite, sei es von solchen, die durch ihren Beruf für die Religion sein wollen oder sollen, oder von anderen, welche glauben, mit ihrem religiösen Gewissen in Zwiespalt zu kommen, wenn sie sich der Theosophie zuwenden.",
        "Wie eine neue Sekte, wie eine neue Religionsstiftung betrachtet man das, was die Theosophie bringt.",
        "Immer und immer wieder wird der hier oft erwähnte, mißverständliche Gedanke geäußert: die Theosophie sei so etwas wie eine Auffrischung uralter buddhistischer Wissenschaft, statt dem Christentum solle der Welt eine Art Neubuddhismus eingeimpft werden.",
        "Was auch immer gesagt werden mag: diese drei Vorurteile er­heben sich immer wieder."
      ],
      [
        "Die Theosophie würde sich an ihrem ersten Grundsatz versündigen, der verlangt, die Eigentümlichkeit einer jeden Geisteskultur zu verstehen, wenn sie eine fremde Geistes-kultur, ein uraltes Religionssystem nach Europa verpflanzen wollte.",
        "Jedes Weltanschauungssystem wächst heraus aus den ganzen Bedingungen einer gewissen Volkskultur und kann nicht in eine ganz andere Kultur hinein verpflanzt werden.",
        "Wollen wir einen wirklichen geistigen Fortschritt innerhalb unserer Welt, wollen wir der Menschheit mit der euro­päisch-amerikanischen Kultur die Quellen eröffnen für einen Fortschritt in die Zukunft hinein, wollen wir dem modernen Menschen etwas bieten, dann können wir nicht mit Anschauungen und Ideen einer längst verbrauchten Zeit kommen, dann müssen wir alles, was wir an Motiven, an Fragen, an Vorstellungen aufbringen können, dem lebendigen Leben unserer Gegenwart selbst entnehmen.",
        "Dann müssen wir da anknüpfen, wo unsere eigene Seele lebt, wo unsere eigene Seele wurzelt."
      ],
      [
        "Nichts Fremdes soll in unsere Kultur verpflanzt werden.",
        "Lediglich darum handelt es sich, einzusehen, daß unsere"
      ],
      [
        "Kultur einer Vertiefung fähig ist und daß das, was be­gonnen ist mit der äußeren Kultur, bewußt fortentwickelt wird.",
        "Jede Kultur ist so anzusehen, daß sie in sich voll ent­wickelte Triebe, gereifte Pflanzen und Früchte enthält, und daneben Keime, die der Mensch fühlt.",
        "Der Mensch der Ge­genwart fühlt solche Keime.",
        "Diese Keime sitzen in seiner Seele als brennende Zeitfragen, als etwas, was er ersehnt und erhofft in der Zukunft, als Rätsel, die sich ihm auf die Seele legen.",
        "Das alles ist in den Seelen der Gegenwarts­menschen verschlossen.",
        "Der Keim, der noch eingepflanzt ist in die Erde, muß heraus.",
        "Vieles sitzt noch verborgen in der Seele der Gegenwartsmenschen.",
        "Es kann um nichts anderes zu tun sein, als das herauszuholen, was in den Seelen der gegenwartigen Menschen ist."
      ],
      [
        "Aber auch mit einem gegenwärtigen Religionsbekenntnis kommt die geisteswissenschaftliche Weltanschauung nicht in Widerspruch.",
        "Sie versucht jedes Religionsbekenntnis zu ver­stehen und zu zeigen, wie in allen großen Weitreligionen die eine Urwahrheit der Menschheit lebt.",
        "Aber sie geht nicht herum und sucht eklektisch aus den verschiedenen Religio­nen einen Wahrheitskern heraus.",
        "Nicht ist sie eine Samm­lerin, diese Geisteswissenschaft, sondern sie ist etwas, was auf eigenem Grund und Boden wächst: etwas, was, wie wir nachher gleich hören werden, nur in der verschiedensten Spiegelung wiedergefunden werden kann in den einzelnen großen Weltreligionen.",
        "Nicht herausgeholt aus den großen Weltreligionen ist die Geisteswissenschaft, sondern in den besten Religionen findet man in verschiedener Art das aus­gebildet, was die geisteswissenschaftliche Weisheit uns heute geben kann.",
        "Sie soll es uns für die Gegenwart so geben, daß wir es nicht bloß zum Verständnis für die Vergangenheit und Gegenwart haben, sondern daß wir etwas zum Hin­einleben in die Zukunft, zum wahren geistigen Menschheitsfortschritt"
      ],
      [
        "haben.",
        "Die Geisteswissenschaft will keine neue Religionsstiftung sein."
      ],
      [
        "Lassen Sie uns unbefangen einmal den Gedanken betrach­ten, inwiefern sie keine Religionsstiftung sein kann und warum sie nicht daran denken kann, eine neue Sekte zu stiften.",
        "Immer genauer werden die Vorträge dieses Winters zeigen, daß die Zeit der Religionsstiftungen, die Art und Weise, wie die Wahrheit in den Religionen zum Ausdruck gekommen ist, vorüber ist, oder mit anderen Worten, daß die Zeit, wo neue Religionen begründet werden können, vorbei ist.",
        "Diese Zeit hat abgeschlossen mit der Zentral-religion des Christentums, denn das Christentum ist einer unendlichen Vertiefung, einer unendlichen Ausbildung für die fernste Zeit der Zukunft fähig.",
        "Und die Geisteswissen­schaft wird das Instrument, das Mittel bilden, dieses Chri­stentum den aufgeklärtesten und wissenschaftlichsten Men­schen immer mehr zugänglich zu machen.",
        "Zum Verständnis der Religion soll diese Geisteswissenschaft beitragen.",
        "Die Weisheit, die in den Religionen liegt, soll sie darbieten.",
        "So wird sie das Instrument und das Mittel sein, sich innerhalb des geistigen Lebens zurechtzufinden.",
        "Man braucht in der Zukunft keine neuen Religionen.",
        "Die alten enthalten das, was sie enthalten können.",
        "Weisheit enthalten sie.",
        "Aber man braucht die Weisheit in einer neuen Form.",
        "Dann wird man die alten Formen auch wieder verstehen, dann werden die alten Religionen durch die Geisteswissenschaft wieder zur wahren Geltung kommen.",
        "Jeder Mensch wird wieder zu seiner Religion kommen können."
      ],
      [
        "Bisher hat es in der Gegenwart ein Gefühl gegeben, das sich in den verschiedenen Religionen herangebildet hat:"
      ],
      [
        "man hat von Toleranz gesprochen gegenüber den verschie­denen Religionen.",
        "Den Menschen, die mit der Gegenwart fühlen, frommt es nicht mehr, mit Haß, Verachtung und"
      ],
      [
        "Verfolgung den anderen Religionen zu begegnen.",
        "Das ist zu einer Unmöglichkeit geworden.",
        "Der Gegenwartsmensch kann die Zeit des Hasses und der Intoleranz nicht mehr recht verstehen, wo im Dienste der Religion ungeheuer viel Blut geflos sen ist."
      ],
      [
        "Zu dulden und zu tolerieren, ist die jetzige Tendenz; das wird eine Zeitlang so gehen.",
        "Aber es wird auch eine Zeit kommen, wo dieses Gefühl zu schwach und zu matt ist, um einen wirklichen Fortschritt in die Zukunft zu bewirken."
      ],
      [
        "Für die Zeit des Ubergangs, für das letzte Jahrhundert war dieses Gefühl in gewisser Beziehung ein Segen.",
        "Die Duldung ist durchaus berechtigt.",
        "Wahre Men­schenliebe und echte Humanität wurden herausgebildet."
      ],
      [
        "Aber was für eine Zeit gut ist, das ist es noch nicht für alle Zeiten.",
        "Die verschiedenen Epochen der Weltentwicklung haben verschiedene Aufgaben.",
        "Ein Gefühl, das für das neunzehnte Jahrhundert voll berechtigt war, das für das neunzehnte Jahrhundert edle Hoffnungen in den Seelen gestiftet hat, das wird sich matt und unwirksam erweisen für das zwanzigste Jahrhundert."
      ],
      [
        "Dieses zwanzigste Jahr­hundert wird sich zu etwas anderem fähig erweisen.",
        "Nicht nur gegenseitige Toleranz und Duldung, sondern vollstän­diges gegenseitiges Verstehen wird es brauchen.",
        "Oder war es nicht so, daß bis heute der Christ gesagt hat: Ich ver­stehe nicht den Muselmann, ich verstehe nicht den Be-kenner des jüdischen Glaubensbekenntnisses bis ins Innere, aber wir dulden uns gegenseitig. - Das wird künftig nicht mehr die Menschen trennen."
      ],
      [
        "Künftig wird es nötig sein, sich gegenseitig zu verstehen und sich zu sagen: Ich habe mein Bekenntnis, das aus einer Kulturströmung heraus-gewachsen ist, die mir die Anschauungen, Gedanken und Ideale in mein Seelenblut verpflanzt hat, aber ich muß auch mit anderen menschlichen Geistern im Verkehr sein, muß sie ganz verstehen können.",
        "Die Wahrheit, die ich bei mir"
      ],
      [
        "finde, soll nicht nur tolerieren und dulden, sondern ein­dringen in das, was die andere Seele fühlt und empfindet.",
        "Sie soll Verständnis haben für jedes andere Bekenntnis. -Das ist noch etwas ganz anderes.",
        "Das ist eine Aufgabe der geisteswissenschaftlichen Weltanschauung: über die Dul­dung hinauszuschreiten zum völligen gegenseitigen Ver­ständnis.",
        "Dann wird der Bekenner einer Religion oder Konfession sich sagen: Die Wahrheit ist mir in einer be­stimmten Form bekannt geworden.",
        "Die Wahrheit lebt aber in anderen Seelen in anderer Form.",
        "Die Formen haben ge­wiß ihre Berechtigung, sie sollen uns aber nicht trennen.",
        "Das, was an Weisheit darin liegt, soll uns verbinden. - In positivem Sinne soll es eine Humanitätsidee sein, die auf Grund von einsichtiger Menschenliebe verbindet und nicht bloß auf Grund von Toleranz.",
        "Einsicht ist mehr als Tole­ranz.",
        "Einsicht adelt den Menschen mehr als Duldung."
      ],
      [
        "Die Theosophie ist nicht unwissenschaftlich.",
        "Als die Theo-sophie vor dreißig Jahren zum ersten Male in die Welt trat, war bei der Gründerin die Aufgabe so gedacht: Dem Menschen der Gegenwart, wie jeder Menschenseele, ist es selbstverständlich, daß man sich die Rätselfragen vorlegt nach dem Unendlichen und Ewigen, die Rätselfragen nach der Bestimmung des Menschen, nach dem Schicksal, die Rätselfragen nach Geburt und Tod und nach dem, was nach dem Tode sein wird, die Rätselfragen: Was bleibt von dem Menschen, wenn er dem physischen Leben abstirbt, woher kommt Krankheit, woher das Leiden?",
        "Oh, es gibt keinen Menschen, der diese Fragen nicht aufwerfen müßte.",
        "Reli­gionen waren immer dazu da, um geistigen Inhalt zur Be­antwortung dieser Welträtsel in die Seelen zu gießen, damit nicht nur das theoretische Bedürfnis befriedigt werde, son­dern damit die Antwort für die Menschen Kraft, Trost und Zuversicht sei.",
        "Oder mit anderen Worten: Der Mensch sollte"
      ],
      [
        "aus der Religion eine Antwort bekommen auf die brennen­den Daseinsfragen, damit er mit Ruhe und Sicherheit im Leben sich bewegt, damit er weiß: ich vollbringe, was ich zu vollbringen habe, aber ich sehe auch auf zu den großen Tatsachen der Unsterblichkeit, die jenseits des Alltags lie­gen.",
        "Nur ein Mensch - und das wird jeder zugeben müssen, der eine Empfindung hat für die tiefsten Impulse der Seele-, der innerlich befriedigt ist, der harmonisch sich so aufzu­klären weiß, daß diese Rätsel der Welt nicht als bange Sorge und als Unsicherheit in seiner Seele leben, sondern der über die höchsten Fragen der Seele ruhig sein kann, ist stark und hat die Kraft zu leben.",
        "Unwissenschaft, Unweis­heit schwächt und macht den Menschen gegenüber der All-tagsarbeit und ebenso gegenüber den wichtigsten Aufgaben des Lebens irre."
      ],
      [
        "Man wird immer mehr und mehr einsehen, daß die Grundlage von Kraft, die Grundlage von Lebensenergie die Weisheit ist, und daß die Weisheit die einzige Grund­lage ist.",
        "Zur Erkenntnis dieser Tatsache und zur Befrie­digung der in dieser Tatsache liegenden Fragen ist die theo­sophische Bewegung da.",
        "Warum aber, wenn die Religionen in den verschiedensten Zeiten der Weltentwicklung diese brennenden Fragen der Menschheit befriedigt haben, war­um brauchen wir da Geisteswissenschaft?",
        "Eben darum, weil die Zeiten sich unterscheiden, weil unsere Vorfahren durch andere seelische Mittel befriedigt werden konnten, als die Menschen der Gegenwart und der Zukunft befriedigt wer­den müssen.",
        "Oder war es nicht so und ist es nicht jeden Tag mehr so, daß sie sagen: In der Religion werden viele Fragen des Daseins beantwortet, aber unser Gefühl kann sich nicht mehr befriedigen an der Art, wie sie beantwortet werden.",
        "Sie sind hingegangen zu den verschiedenen Religions- und wissenschaftlichen Bekenntnissen.",
        "Zahlreiche unserer Zeitgenossen"
      ],
      [
        "haben versucht, aus der Naturwissenschaft, aus der Geschichte eine Art Ersatz zu bilden für diejenigen, die vermöge ihres modernen Gewissens sich nicht mehr befrie­digt erklären können von der früheren Art, die Rätselfragen zu lösen.",
        "Gar manche, die unbefriedigt sind von der Bibel und der Religion, suchen sehnsüchtig in der heutigen Wis­senschaft.",
        "Aber immer mehr und mehr müssen diese letz­teren erkennen, daß für die höchsten Fragen des Daseins gerade die heutige Wissenschaft - deren Größe nicht ver­unglimpft werden soll durch die geisteswissenschaftliche Weltanschauung, sondern vielmehr anerkannt werden soll, da sie so Gewaltiges leistet für die sinnlichen Tatsachen -versagt gegenüber den wichtigsten Fragen des Daseins.",
        "So sagt sich mancher: Wenn es sich darum handelt, unsere Erde durch ein Kulturnetz zu umspannen, wenn es gilt, die Erde zu durchforschen bis in die kleinsten Lebewesen hinein, lie­fert uns die moderne Wissenschaft wunderbare Erkennt­nisse.",
        "Wenn aber die Menschen fragen nach der Zukunft des Lebens, nach dem eigentlichen Sinn des Daseins, da versagt die Wissenschaft, ja, sie versagt stark.",
        "Diejenigen, die es noch nicht probiert haben - und es werden mehr und mehr Menschen versucht haben, mit Hilfe der Wissenschaft das zu probieren, was sie mit Hilfe der Religion nicht erreichen können -, werden es noch einsehen, daß die Wissenschaft in den wichtigsten Daseinsfragen versagt."
      ],
      [
        "Bietet aber nun die Geisteswissenschaft in dieser Richtung etwas?",
        "Ja, die geisteswissenschaftliche Weltanschauung ist für die zuletzt angedeuteten Fragen da.",
        "Wer sich noch innerhalb der religiösen Traditionen befriedigt fühlt, der wird sich unbefriedigt fühlen von der Geisteswissenschaft, weil er glaubt, daß sie ihm nichts bieten kann, weil er sich einhüllt in das, was ihm die religiöse Tradition geben kann.",
        "Was aber heute noch gut für ihn ist, kann es schon morgen"
      ],
      [
        "nicht mehr sein.",
        "Das war das Ideal der Gründerin der theo­sophischen Bewegung: sichere Erkenntnis über die höchsten Probleme des Daseins zu geben.",
        "Wer sich tiefer einläßt in die geisteswissenschaftliche Forschung und Betrachtung, wird sehen, wie keiner wissenschaftlichen Anforderung gegen­über gerade diese geisteswissenschaftliche Forschung sich irgendwie zurückziehen muß.",
        "Auf wissenschaftlicher Grund­lage eine allgemein verständliche Weltanschauung zu geben, die für die aufgeklärtesten und auch für die schlichtesten Menschen etwas bieten kann, das wird die geisteswissen­schaftliche Weltanschauung leisten."
      ],
      [
        "Aber man könnte vielleicht doch die Theosophie als eine Art Störenfried ansehen.",
        "Sie können vielleicht sagen: Laßt uns doch nur bei unserem alten Glauben, ja, tut etwas dazu, diesen alten Glauben wiederherzustellen!",
        "Die Wissenschaft vermag doch keine Antwort zu geben, versucht es doch, wieder den alten Glauben zu stützen! - Solche Menschen be­achten nicht, was um sie vorgeht.",
        "Sie sind die wahren Phan­tasten.",
        "Die Theosophie will mit offenen Augen in unseren Kulturprozeß hineinsehen.",
        "Wir brauchen nur ein Bild vor uns hinzustellen, und es kann ein Beweis sein für die Not-wendigkeit der geisteswissenschaftlichen Weltanschauung."
      ],
      [
        "Werfen wir für zwei Minuten den Blick auf das merk-würdige Land, das eine so eigentumliche religiose Entwick­lung durchgemacht hat im Laufe der letzten Jahrhunderte, auf Spanien.",
        "Schauen wir Spanien an, diesen Hort einer orthodox-religiösen Welteinrichtung, nicht nur Weltan­schauung.",
        "Dieses Land, wo ein uraltes Religionsbekenntnis eingegriffen hat in die alleralltäglichste Einrichtung, be­findet sich in einer Umbildung.",
        "Wer hat denn vor einigen Jahren noch geglaubt, daß in Spanien das eintreten könnte, was wir heute dort sich abspielen sehen.",
        "Denken Sie nur einmal daran, daß vor ganz kurzer Zeit in Spanien die"
      ],
      [
        "regierenden Mächte nichts haben wissen wollen von irgend­welchen sogenannten modernen Ideen, von irgendwelchen aufklärerischen Ideen, denken Sie an das feste orthodoxe Bekenntnis derjenigen Frau, die als Königin-Mutter dem gegenwärtigen jungen König von Spanien vorangegangen ist, wie wenig sie geneigt war, auch nur ein Tüpfelchen ab­zugehen von dem, was sich seit Jahrhunderten fest ein­gebaut hat in das Gefüge eines ganzen Staates.",
        "Denken Sie sich den Kontrast: Diese Frau sitzt in Lourdes, da, wo sie Befriedigung in der alten Weise in vollen Zügen zu schlür­fen versucht und die alten Wahrheiten an sich herantreten läßt - und in Spanien muß der junge König es zugeben, daß mitten in das feste Gefüge hinein neue Ideen eintreten."
      ],
      [
        "Er mußte es zugeben, daß ein liberaler Minister an den Ein­richtungen rüttelt, daß an der Unterrichts- und Ehegesetz­gebung gerüttelt wird, und, wie es scheint, in unbarmherzi­ger Weise.",
        "Das sind die Zeitströmungen, und gegen solche Zeitströmungen vermag keine menschliche Meinung etwas."
      ],
      [
        "Dagegen vermag nur das Verständnis etwas.",
        "Wie lassen doch die Menschen heute diese Zeitströmungen an sich heran­kommen.",
        "Wie stehen manche mit verbundenen Augen sol­chen Erscheinungen gegenüber, ganz unvorbereitet, wie las­sen sie sich überraschen, frappieren und schockieren."
      ],
      [
        "Wie üben sie Kritik an den Zeitströmungen, wie kommen sie nicht weiter, als daß sie sagen: wir müssen die alten Formen stützen.",
        "Wie begreifen sie gar nicht, daß die Zeitströmungen stärker sind als die phantastischsten Meinungen."
      ],
      [
        "Sie be­greifen nicht, daß es nötig ist, mit hellem Blick und offenem Auge zu sehen, was die Menschen nötig haben.",
        "Die Men­schen sind heute nicht mehr so unbewußt, alles über sich ergehen zu lassen.",
        "Sie sind dazu berufen, diese Zeitbewegun­gen zu verstehen und ihnen selbst die Richtung zu geben."
      ],
      [
        "Jeder einzelne ist dazu berufen, erkennen zu lernen, was in"
      ],
      [
        "solchen Zeitströmungen liegt und wie diese zu einem ge­deihlichen Fortschritt in der Zukunft gebracht werden kön­nen.",
        "Die Menschen machen Geschichte, und wenn gegen die Menschen Geschichte gemacht werden soll, so kommt das Chaos.",
        "Nur aus dem Miteinander kann Recht und Har­monie kommen.",
        "Die Zeit gibt schon die Notwendigkeiten:"
      ],
      [
        "an den Menschen ist es, sie zu verstehen.",
        "Nicht in bequemer Weise soll der Mensch die Dinge an sich herankommen lassen.",
        "Da würde er nur zu Ballast in der Entwicklung.",
        "Die Zeitströmungen kann man aber nicht übersehen, wenn man nicht einen Blick in das Übersinnliche hinein zu tun ver­mag.",
        "Der Mensch ist dazu berufen, das Übersinnliche in sein Herz, in sein Gemüt und in seine Seele aufzunehmen, so daß es durch ihn in der Welt wirkt."
      ],
      [
        "Nun versuchen wir einmal, uns diese Frage, die sich aus der eben gemachten Betrachtung ergibt, so recht vor die Seele hinzumalen.",
        "Was ergibt sich für den denkenden Men­schen aus dem, was wir gehört haben?",
        "Es ergibt sich sehr viel daraus.",
        "Wer eine Einsicht hat in das geistige Leben, der weiß eines: daß es keine gedeihliche materielle Kultur geben kann ohne die Grundlage eines wirklichen geistigen Lebens.",
        "Nie hat es einen Staat, nie hat es eine Volksgemeinschaft gegeben ohne eine wirkliche religiöse Grundlage.",
        "Es sollte nur jemand einmal ernstlich versuchen, eine Kolonie zu begründen mit Menschen, die nur matierelle Interessen haben und die nur eine materialistische Weltanschauung haben, die also nichts mitbringen als das, was man heute innerhalb der materialistischen Weltanschauung gelten las­sen will, die nichts von dem Übersinnlichen kennt.",
        "Man versuche eine solche Kolonie zu begründen.",
        "Allerdings, es bringen die Menschen ja doch die Reste idealer Gedanken und Ideen mit.",
        "Wären die nicht mehr da, so würde es schnell in ein vollständiges Chaos ausarten.",
        "Sie können kein"
      ],
      [
        "soziales Leben begründen ohne weisheitsvolle religiöse Grundlage.",
        "Der ist ein schlechter Praktiker, der mit der Praxis allein auszukommen glaubt.",
        "Wollen Sie das mate­rielle Dasein der Menschen immer mehr fördern, so müssen Sie daran denken, daß die Seele jeder materiellen Kultur nur die Religions- und Erkenntnisgrundlage sein kann.",
        "Wenn Sie den Menschen Brot geben wollen, so müssen Sie ihnen zuerst etwas geben für die Seele.",
        "In der Zeitschrift «Luzifer» habe ich den scheinbar grotesken Satz ausgespro­chen, daß man niemand Brot geben kann, ohne daß man ihm Weltanschauung gibt, da das Brotgeben ohne geistige Nah­rung zum Unheil führt.",
        "In jenem Aufsatz haben Sie das mehr oder weniger bewiesen."
      ],
      [
        "Wie müßte es aber in der Gegenwart sein, wenn ein ge­deihlicher Fortschritt stattfinden sollte angesichts des Ereig­nisses in Spanien, welches nur in besonderer Weise das zum Ausdruck bringt, was sich überall vollzieht, was aber nur der übersehen könnte, der den Kopf gegenüber dem Leben in den Kultursand stecken würde wie der Vogel Strauß.",
        "Ebenso wie es auf allen Lebensgebieten Kundige gibt, die uns mit Kleidern versorgen und andere Bedürfnisse des Lebens befriedigen helfen, so gibt es auch Kundige auf dem Gebiete des Seelenlebens, auf dem Gebiete des Übersinn­lichen.",
        "Das Vertrauen zu den Priestern und Weisen war es, was die Kulturen begründete.",
        "Nicht haben wir ein Recht, die verflossene Kultur zu kritisieren.",
        "Sie war so gut, wie sie für ihre Epoche sein konnte.",
        "Wenn die Kulturen jetzt nicht mehr passen, so liegt es nicht daran, daß sie zu bekämpfen sind, sondern daran, daß die Menschheit eine Fortentwick­lung braucht in der geistigen Wahrheit, weil die Menschen nicht mehr unter den alten Formen des geistigen Lebens leben können.",
        "Ebenso wie der Mensch, der früher zu dem Priester ging, Worte des Trostes und der Sicherheit erhielt,"
      ],
      [
        "ebenso müßte es in unserer Zeit Menschen und Forscher geben - ja, es muß sie geben -, an die man sich zu halten hat, die einem die Wahrheit in der neuen, der Gegenwart entsprechenden Form sagen können, die einem wieder etwas sagen können von dem Übersinnlichen, in einer Form, wie der moderne Mensch es glauben kann."
      ],
      [
        "Fragen wir uns einmal, wie könnte sich die Gegenwart in bezug auf diese Sache stellen, wenn alles so bliebe, wie es von zahlreichen unserer Zeitgenossen für richtig befunden wird.",
        "Sie sehen da etwas, was als Symptom in bezug auf Spanien erwähnt worden ist.",
        "Sie sagen vielleicht: die alten Formen werden sich auflösen, und der Mensch wird in neue Ordnungen hineinwachsen.",
        "Diese neuen Ordnungen werden aber nie gedeihen können, wenn nicht ein Seelisches hinein-kommt, wie das Lebensblut, wenn nicht etwas Geistiges unsere ganze Kultur durchpulsen kann.",
        "Können die Men­schen, die sich heute voneinander entfernen in bezug auf ihre Meinungen über die Seele und in bezug auf die Ein­richtungen, an einen Ort hingehen und sich Rat holen in"
      ],
      [
        "bezug auf die höchsten Fragen des Daseins?"
      ],
      [
        "Betrachten wir die Sache an einem charakteristischen Symptom unserer Zeit.",
        "Von der Naturwissenschaft, von der Erkenntnis der äußeren sinnlichen Tatsachen, der positiven Tatsachen, erwarten viele einen Ersatz für die alte religiöse Anschauung.",
        "Vor einigen Tagen hat eine Naturforscherver­sammlung in Stuttgart stattgefunden.",
        "Können wir uns sagen, daß der moderne Mensch, mit seinen Bedürfnissen und Sehnsüchten gegenüber dem Ewigen, gegenüber dem, was der Tod besagt, hinschauen kann zu dem modernen Areopag des Geisteslebens, wenn er Antwort braucht und wenn die geistige Entwicklung ihren Fortgang nehmen soll?",
        "Es sind gewaltige Fragen besprochen worden auf dem Kon­greß in Stuttgart.",
        "In den erstaunlichsten Dingen lebt sich"
      ],
      [
        "der menschliche physische Forschergeist bei einer solchen Gelegenheit aus.",
        "Für den, der eine Empfindung dafür hat, sei es erwähnt: man sprach über solche Vorstellungen wie die Verpflanzung eines Organs des einen Lebewesens auf ein anderes.",
        "Es wurde genau besprochen, wie die Verpflan­zung eines Bestandteiles eines Lebewesens in ein anderes Lebewesen hinein stattfinden kann, dem dieser Bestandteil fehlt.",
        "Oder ist es nicht interessant, zu sehen, wie die Natur­forschung durch die Errungenschaft des Mikroskopes alles bisher Dagewesene überboten hat?",
        "Ist es nicht bewunderns­wert, zu sehen, wie aus gewissen Mischungen und Lösungen heraus man aus der toten Substanz etwas entstehen läßt, was, mit dem Schein des Lebens begabt, sich herausent­wickelt aus der toten Substanz wie der scheinbar tote Kri­stall.",
        "Vieles ließe sich noch anführen, was uns zeigen könnte, welchen Respekt und welche Achtung uns diese moderne Naturforschung abnötigen kann."
      ],
      [
        "Nun aber kommt der Mensch heran und fragt sich: Wozu ist dieses ganze Leben?",
        "Welches ist der Sinn von alledem, was sich in so wunderbaren Formen für die physischen For­scher darstellt?",
        "Gibt es in dem Reiche derjenigen, die in dem Areopag des Geisteslebens sind, auch solche, die Antwort geben auf die letzten Fragen?"
      ],
      [
        "Auf dem letzten Naturforscher-Kongreß hatte man auf solche Fragen keine Rücksicht genommen.",
        "Noch vor zwei Jahren hat ein Breslauer Chemiker eine merkwürdige Rede gehalten, wonach alles abgelehnt werden soll, was dem Menschen in psychischer Weise zu erforschen möglich ist.",
        "Das war Ledebur, der Breslauer Chemiker.",
        "Theodor Lipps durfte jetzt über Naturwissenschaft und Philosophie spre­chen.",
        "Das ist ein beachtliches Zeichen, daß es möglich war, in einer naturwissenschaftlichen Versammlung das zu bieten, was Lipps geboten hat.",
        "Es war ihm möglich, mitten in diese"
      ],
      [
        "rein positive Forschung solche Worte hineinzuwerfen wie:"
      ],
      [
        "Die Naturwissenschaft kann sich niemals zu einer Welt­anschauung erheben, wenn sie nicht zu einer geistigen Durch­dringung der menschlichen Erscheinung kommt.",
        "Wenn der Mensch in sich hineinsieht, so findet er das Ich, und wenn er das dann ausdehnt zu einem Welten-Ich, dann kann er zu einiger Befriedigung kommen."
      ],
      [
        "Es ist ein sonderbares Gefühl, das derjenige, der sich mit diesen Dingen beschäftigt hat, gegenüber einer solchen Tat­sache haben muß.",
        "Da gibt es seit dreißig Jahren eine theo­sophische Bewegung, die nicht bloß in ganz allgemeiner, platter Weise die großen Fragen beantwortet, sondern in konkreter Weise sich einläßt auf das Schicksal des Menschen vor der Geburt und nach dem Tode, sich einläßt auf das, was sich dem Menschen bietet in der geistigen Welt, wenn ihm das Auge dafür geöffnet ist.",
        "Kurz, nachdem es dreißig Jahre eine solche Vertiefung gegeben hat, kommt einer ein­mal zum Wort, der in den allerelementarsten und aller­trivialsten Begriffen etwas bietet, was überhaupt noch kei­nem Menschen eine Befriedigung geben kann, weil es sich gegenüber den unmittelbaren großen Lebensfragen wie ein Begriffsgespinst, wie etwas ganz Abstraktes, Weltfernes ausnimmt.",
        "Wer sich nicht mit Fachphilosophie beschäftigt hat - welchen Begriff die Philosophie erst herausgearbeitet hat-, für den ist das nichts anderes als ein abstraktes Wort-gespinst, bei dem er sich nichts denken kann.",
        "So sehen Sie, daß im offiziellen Leben, wo die Menschen dennoch Trost und Lösung suchen für die Lebensrätsel, nichts geboten werden kann, aus Unvermögen, aus Unverständnis gegen­über den wirklich höchsten Fragen."
      ],
      [
        "Und doch, es muß für die äußere Kultur, die alle Formen zersprengt, ein solches Lebenszentrum geben, aus dem gei­stiger Inhalt herkommen kann, nicht bloß wertlose Wortgespinste,"
      ],
      [
        "sondern lebendige Erkenntnis des Übersinnlichen.",
        "Diese muß, von den geistigen Führern der Gegenwart her, eindringen in das, was sich als Rest des geistigen Inhalts in den alten Formen erhalten hat.",
        "Wenn von einer solchen Stätte aus, in derselben logischen Weise, in der die Wissen­schaft spricht, über die übersinnliche Welt eine entsprechende Botschaft verkündigt werden kann, dann wird sich das -wie die alten Religionen sich ergossen haben - ergießen in die Seelen und äußeren Einrichtungen.",
        "Dann werden - das werden Sie sehen - die vermaterialisierten alten Religions­formen verschwinden und neue Formen werden sich bilden."
      ],
      [
        "Man soll sich aber keiner Illusion hingeben über die Be­deutung dieser geistigen Kultur.",
        "Es gibt viele - und in Frankreich ist das Wort dieser vielen tonangebend gewor­den -, die sa sagen, der Mensch braucht seine Moral gar nicht aus etwas wie Religion heraus zu bilden.",
        "Sie sagen:"
      ],
      [
        "Es gibt eine menschliche Moral und die kann begründet werden ohne ein Religionsbekenntnis.",
        "Die, welche so spre­chen, haben die eigentlichen geistigen Gesetze wenig kennen­gelernt.",
        "Wenn Sie den Gang der Geisteskultur seit alten Zeiten verfolgen, so werden Sie sich sagen können: Die verschiedenen aufeinanderfolgenden Kulturepochen der Menschheit haben der Menschheit verschiedene Inhalte ge­bracht.",
        "Was hat die Hermes-Kultur den Agyptern, was die Kultur der indischen Rishis den Hindus, was der Zarathu­strismus den Persern, was die Kultur des Moses den Juden gebracht, und was endlich die Kultur des Christus Jesus, des größten Religionsstifters, der modernen Zeit?",
        "Jede Kultur-strömung hat ihre Bedeutung in ihrer Zeit gehabt.",
        "Und groß sind sie gewesen, weil ihre Missionare es verstanden haben, die Bedürfnisse ihrer Zeit zu verstehen.",
        "Richtig wer­den die Missionare der Zukunft wirken, welche die Herzen der Menschen wieder verstehen und in sie hineinwirken"
      ],
      [
        "können.",
        "Verschiedene Formen haben wir für die verschie­denen Zeiten, in immer neuer Gestalt erscheinen die alten Wahrheiten."
      ],
      [
        "Das erste, was jeder neuen Gestalt einer Kultur zugrunde liegt, ist ein Bekenntnis, eine Summe von Anschauungen, von Empfindungen und Vorstellungen über das Höchste und das Übersinnliche, ein Wissen des Menschen von den göttlichen Grundlagen der Welt, ein Wissen des Menschen über das, was den Tod besiegt.",
        "Und jede große Kultur-epoche hat aus diesen Grundlagen heraus die Kraft zum geistigen Schaffen gezogen.",
        "Niemals wäre das zustande ge­kommen, was im alten Agypten, in Indien und Vorderasien, in Griechenland und endlich in den christlichen Zeiten ent­standen ist, wenn es nicht aus dem herausgewachsen wäre, was die Menschen geglaubt und gedacht haben.",
        "Das Aller­materiellste ist nur ein Ergebnis dessen, was der Mensch weiß über das Übersinnliche.",
        "Das erste in jeder Kultur-strömung ist also das Bekenntnis."
      ],
      [
        "Das zweite ist, wie dieses Bekenntnis auf das Gefühl und die Gemüter wirkt.",
        "Die Gedanken und die Vorstellungen, die sich der Mensch macht über das Übersinnliche, üben einen Eindruck auf die Seele aus und erheben sie, und alle höhere Lebensfroheit und Harmonie gießt sich in die Seele unter dem Einflusse des Bekenntnisses.",
        "Wo jemals Menschen froh gewesen sind im höchsten Sinne, wo sie jemals Sicherheit gehabt, jemals in ihre Empfindungen sich etwas hinein-gegossen haben, so daß sie sich sagen konnten, ich weiß, daß ich eine höhere Bestimmung habe, und wo sich dieses Wissen umgewandelt hat in ihrer Seele in eine befriedigende Le­bensfreude und Lebenszuversicht, da war es immer unter dem Eindruck eines Bekenntnisses."
      ],
      [
        "Das erste also ist das Bekenntnis selbst, das zweite ist die Welt der Gefühle: Erhebung, Lebensfreude und Lebenssicherheit."
      ],
      [
        "Und so ist das dritte die Welt der Willens-impulse, die Welt der Moral und der Ethik.",
        "Die Sitten-lehren bilden die Kunst - etwas, was zum zweiten Teil gehört -, das Moralische und das Willenselement, die Welt der Sittlichkeit und Gesetzgebung und alles staatlichen Zu­sammenlebens.",
        "Es ist eine große Täuschung, wenn jemand sich dem Glauben hingibt, daß es jemals eine Sittlichkeit, eine Moral geben kann, die nicht herausgewachsen ist aus der Grundlage eines Bekenntnisses, aus der Grundlage der Gefühlssphäre.",
        "Als erstes hat der Mensch eine Meinung über das Übersinnliche, als zweites Lebensfroheit und Zuver­sicht, und als drittes die Impulse für seine Handlungen, das, was ihm sagt: das ist gut, das ist böse."
      ],
      [
        "Wie kommt es, daß viele den Glauben haben - was eine Illusion ist -, daß man Moral begründen kann ohne Be­kenntnis, das heißt eine bodenlose Moral?",
        "Das kommt davon her, daß die Moral, dieses dritte in einer Kultur-strömung, das letzte ist, was verschwindet.",
        "Wenn eine Kulturströmung abflutet, flutet zuerst das Bekenntnis ab.",
        "Zuerst glaubt man nicht mehr die Dinge, die in dem Be­kenntnis gegeben werden.",
        "Wenn aber lange schon nicht mehr der lebendige Glaube da ist, der den Menschen mit absoluter Sicherheit auf die Formen hinblicken läßt, dann sind noch immer die Empfindungen und Gefühle da, die sich in diesem Glauben ausgebildet haben.",
        "Und wenn auch diese Gefühle nicht mehr da sind, wenn der Mensch nicht mehr die ererbte Freudigkeit haben kann, dann ist noch immer die Moral da.",
        "Heute stehen die, welche glauben, eine solche bodenlose Moral gründen zu können, nicht auf dem Boden einer bodenlosen Moral.",
        "In Wahrheit leben sie unter den Resten der Moral und der Weltanschauung, die ihnen aus dem Bekenntnis geblieben sind als ererbte Stücke der Kultur."
      ],
      [
        "Diejenigen, welche sagen, alles Übersinnliche sei unzu­gänglich für den Menschen, alles Übersinnliche sei phan­tastisch, die handeln so, wie sie es tun, weil in ihnen noch die Moral der Vorzeit lebt.",
        "Viele Menschen gibt es, die das Bekenntnis glauben überwunden zu haben, doch stehen sie alle noch unter der Moral, die ihnen das Bekenntnis ge­geben hat."
      ],
      [
        "Es gibt viele Sozialisten, die eine Moral begründen wol­len, eine Moral, die aus dem Nichts heraus geboren ist.",
        "Warum können sie aber überhaupt über Moral reden?",
        "Warum verschwindet denn nicht alle Moral in ein Chaos hinein?",
        "Weil sie die alte Moral, die sie bekämpfen, noch in ihren Gliedern haben, weil sie eben staatliche Anderungen auf der Grundlage der überkommenen staatlichen Moral herbeiführen wollen.",
        "Sie ist hervorgewachsen aus der Ver­gangenheit.",
        "Daher wird ein Fortschritt erst unter der Er­neuerung der Erkenntnis des Übersinnlichen möglich sein, der übersinnlichen Welt, wenn es möglich ist, dem Menschen etwas zu geben, was ihn hinaufweist in die übersinnliche Welt, was ihn bekannt macht mit den Kräften, die uns um­geben und die hineinspielen in die Welt, die um uns ist.",
        "Ist es möglich, ihm diese Weisheit des Übersinnlichen zu ver­mitteln, dann wird dies eine Gefühlswelt der Lebenssicher­heit und eine Moral begründen mit Impulsen für das Han­deln.",
        "Dann leben wir nicht mehr von ererbten Gütern, son­dern von dem, was aus der Zeit, in der wir leben, selbst entsprießen kann."
      ],
      [
        "Diese Erkenntnis des Übersinnlichen, welche die geistes­wissenschaftliche Weltanschauung geben will, verstößt gegen keine Logik.",
        "In welchem Sinne spricht sie von einem Über­sinnlichen?",
        "Spricht sie davon, daß in einem Jenseits oder an einem unbekannten Orte das Geistige ist?",
        "Merkwürdig, es werden Weltanschauungen gestiftet, die behaupten, daß ein"
      ],
      [
        "Jenseitsglaube alle Kultur vernichten müsse.",
        "Nun, alle solche Anschauungen wissen nicht, in welchem Sinne die wirkliche Geistesforschung von diesem Übersinnlichen spricht.",
        "Öfters ist das hier schon durch Vergleiche klargemacht worden, wie und in welchem Sinne die Geistesforschung von einem sol­chen Übersinnlichen spricht.",
        "Dieser Vergleich soll zum Schluß noch einmal vor unsere Seele hintreten."
      ],
      [
        "Für einen Menschen, der blind geboren ist, ist die Welt der Farben und des Lichtes ein Jenseits der für ihn wahr­nehmbaren Welt.",
        "Wodurch ist eine Welt für den Menschen da?",
        "Lediglich dadurch, daß er Organe hat für diese Welt.",
        "In dem Augenblicke, wo dem Blindgeborenen das Auge geöffnet wird, muß er sich nicht mehr bloß von anderen Menschen sagen lassen, es gibt Licht und Farbe, sondern da tritt eine neue Welt, die immer da war, vor sein Auge.",
        "Nichts anderes sagt die Geisteswissenschaft, und von nichts anderem handelt sie.",
        "Wenn sie von anderen Welten spricht, so spricht sie davon in genau demselben Sinne wie in dem Vergleich von der Welt der Farben und des Lichtes gegen­über dem Blindgeborenen.",
        "Der Geistesforscher sagt, daß eine Welt für ihn dann da ist, wenn ein Organ für sie da ist.",
        "Die übersinnliche Welt ist dem Menschen der Gegen­wart verschlossen, weil bei ihm keine Organe dafür vor­handen sind.",
        "Sie verhält sich nicht anders für ihn, als sich die Welt der Farben und des Lichtes für den Blindgebore­nen verhält."
      ],
      [
        "Hier sind nicht nur Gegenstände, die der Mensch mit dem Verstande und mit den Sinnen erfassen kann, hier sind noch ganz andere Wesenheiten.",
        "Indem Sie durch den Saal schreiten, schreiten Sie durch eine Welt des Geistigen, wie der Blinde, der die Stühle und Bänke nur tasten kann, durch eine Welt von Farben und Licht schreitet, ohne sie sehen zu können.",
        "Wie es von einem Blinden ein logisches Unding"
      ],
      [
        "wäre, nachdem er gehört hat, daß es Farbe und Licht gibt, zu sagen, das sei Phantasterei, ebenso ist es unlogisch, daß der, welcher nicht übersinnlich sieht, sagt, es sei Phan­tasterei.",
        "Es hat immer Leute gegeben, welche mehr sehen konnten als die Mitmenschen.",
        "Eingeweihte oder Initiierte hat man solche Menschen genannt.",
        "Es sind das Menschen, die eine Art geistiger Neugeburt erlebt haben und von denen in allen Religionen erzählt wird.",
        "Es gibt einen gei­stigen Augenblick im Leben eines solchen Menschen, der eine viele größere Bedeutung hat als die physische Geburt.",
        "Dieser geistige Augenblick besteht darin, daß der Mensch, der sein geistiges Auge und sein geistiges Ohr eröffnet hat, eine ganz neue Welt wahrnehmen kann, daß er sich bis zur übersinnlichen Welt hinaufentwickelt hat.",
        "Diejenigen, welche von der übersinnlichen Welt zu sprechen berechtigt sind - die Stifter der Religionen -, haben zu den Menschen in demselben Sinne gesprochen, wie der Sehende zu dem Blinden vom Licht spricht und ihm davon erzählt."
      ],
      [
        "Neuerdings dringt die Botschaft von der übersinnlichen Welt wieder an die Menschen heran durch die Geisteswissen­schaft.",
        "Dies geschieht in keinem anderen Sinn, als indem sie den Menschen zeigt, daß es immer Erleuchtete, Erfahrenere gegeben hat, die hineinschauen konnten in die übersinnliche Welt, und daß es heute noch Menschen gibt, die das geistige Auge offen haben, die die geistigen Eigenschaften der sinn­lichen Dinge sehen.",
        "Sie zeigt, daß es Menschen gibt, die hinter die Pforte des Todes schauen können, die sehen können, welches der unsterbliche Teil des Menschen ist, was übrigbleibt von dem Menschen, wenn er durch die Pforte des Todes schreitet.",
        "Über dieses alles in Einzelheiten aus der For­schung heraus Nachricht zu geben, ist unsere Aufgabe.",
        "Sie sind dazu berufen, einen neuen Mittelpunkt zu bilden, von dem aus die Menschen hören werden von der geistigen Welt."
      ],
      [
        "Es ist billig zu sagen: Gebt mir die Mittel, selbst hinein-zuschauen.",
        "Jeder kann die Mittel haben, wenn er sich an die richtige Quelle wendet.",
        "Durch die geisteswissenschaftliche Weltanschauung wird jedem die Möglichkeit geboten."
      ],
      [
        "Die erste Stufe ist aber, mit der heutigen Anschauungsweise sich zu erheben zu folgendem Gedanken, der sich in dem Men­schen ausbildet: Ich höre von einem Mitmenschen, daß er hineinschauen kann in die übersinnliche Welt, ich höre, daß er mir sehr viel zu sagen versteht über die übersinnliche Welt, er erzählt im einzelnen, wie es nach dem Tode aus­schaut, wie Kräfte und Wesenheiten die Welt durchpulsen, Kräfte und Wesenheiten, die dem gewöhnlichen Auge noch verschlossen sind.",
        "Ich kann zwar noch nicht hineinschauen in diese Welt, aber ich will meine Ahnung fragen, ob der Mann mir etwas Unwahrscheinliches sagt."
      ],
      [
        "Ich will meine Empfindung fragen, ob das nicht höchst wahrscheinlich klingt, wenn ich mich nicht durch materialistische Anschau­ungen abhalten lasse, ob das unbefangen klingt, was der Betreffende sagt.",
        "Dann will ich die Gedankenlogik zu Hilfe nehmen und sehen, ob er nicht etwas sagt, was das Leben erklärlich machen kann."
      ],
      [
        "Dann will ich noch weiter gehen.",
        "Ich will sagen, ich habe dich ruhig angehört, denn du hast etwas gesagt, was mit der Logik stimmt.",
        "Jetzt will ich das Schicksal des Menschen betrachten, will sehen, ob es mir erklärlich wird, wenn ich so die Welt betrachte."
      ],
      [
        "Indem ich mir also sage: nehmen wir einmal an, die Anschauung der Geisteswissenschaft wäre richtig, erklärt sie das Leben, wird das Leben verständlich? so prägen sich die Gedanken in meine Seele ein: ich will versuchen, im Leben zu erproben, ob sie Lebensfroheit, Lebenssicherheit, Lebenskraft gibt.",
        "So will ich Stück für Stück erproben, ob eine innere Möglich­keit besteht, das anzunehmen, was der Eingeweihte sagt."
      ],
      [
        "Ich will mich auf einen solchen Standpunkt stellen, wie sich"
      ],
      [
        "eine merkwürdige Persönlichkeit in bezug auf die gewöhn­liche Welt des Lichtes und der Farben gestellt hat."
      ],
      [
        "Öfters wurde schon das Leben der taubstummen und blin­den Helen Keller erwähnt.",
        "Das ist eine Persönlichkeit, die mit sieben Jahren noch wie ein kleines wildes Tier war, die aber eine geniale Erzieherin gefunden hat, so daß sie so weit gekommen ist, daß sie nicht nur eine Durchschnitts­bildung hatte, sondern sich messen konnte mit manchem gebildeten Menschen.",
        "Niemals ist sie imstande gewesen, Töne zu hören, Farben zu sehen, Licht wahrzunehmen.",
        "Fin­sternis und Stummheit lagerte um ihre Seele.",
        "Aber sie hat das, was andere Menschen von Farbe, Licht und Ton wahr­genommen haben, auf ihre Seele wirken lassen.",
        "Von ihr ist ein neues Büchelchen erschienen: «Optimismus».",
        "Sie zeigt darin, daß sie nicht nur unser Wissen aufgenommen hat, sondern auch von der Sprache und dem Wissen der Griechen und Römer.",
        "Sie spricht von den schönsten Schöpfungen des Hörens und Sehens, obgleich sie selbst nichts wahrgenom­men hat.",
        "In ihrer Seele hat sich nicht nur so etwas aus­gebildet wie Wortvorstellungen, sondern das Büchelchen über den Optimismus zeigt, daß sie Kraft und Sicherheit erhalten konnte aus den Mitteilungen der Sehenden um sie herum."
      ],
      [
        "So vermag der Mensch, wenn er sich nicht verschließt gegenüber den geistig Sehenden und Hörenden, Kraft und Sicherheit und Hoffnung für die Zukunft zu erhalten.",
        "Dis­harmonie macht schwach und kraftlos für das Leben.",
        "Sehend wird der Mensch für seine Umgebung, wenn er auf die Sehenden hört.",
        "Wissend wird er und frei handelnd, wenn er denen, die Kunde geben können, folgen kann.",
        "Das Leben vermag er in den Dienst des Übersinnlichen zu stellen.",
        "Eine neue Kultur aus dem Übersinnlichen heraus muß, wie das Lebensblut, den Staat und die gesellschaftlichen Formen"
      ],
      [
        "durchdringen.",
        "So hängt die Erkenntnis des Übersinnlichen in der Gegenwart mit großen Lebensfragen zusammen.",
        "Wenn die großen Lebensfragen in den verschiedensten For­men von allen Seiten uns entgegendrängen, dann muß man erkennen, daß man etwas braucht, was einen tiefer hinein-führt in das Verständnis des Lebens.",
        "Aus einer propheti-schen Voraussicht gegenüber dem, was kommen muß, ist die geisteswissenschaftliche Weltanschauung herausgegriffen, herausgeschaffen.",
        "Das soll uns die Serie von Vorträgen des Winters zeigen in bezug auf die Fragen der großen Kultur-strömungen und auch in bezug auf die einzelne Seele, die still und schlicht im häuslichen Heim schaffen muß vom Morgen bis zum Abend.",
        "Jede Seele findet in der Geistes-forschung etwas, wodurch sie Kraft und Sicherheit, innere Befriedigung, Lebensmut und Lebensfreude finden kann und auch das Notwendige zu einem wirklich gedeihlichen Menschheitsfortschritte."
      ],
      [
        "Wenn auch noch manche da sind, welche über die geistes-wissenschaftliche Erkenntnis des Übersinnlichen lächeln und als Praktiker, die sie sein wollen, sagen: was haben wir zu tun mit dem unpraktischen Zeug - die geisteswissenschaft­liche Bewegung wird arbeiten und eine Zeit wird kommen, wo auch solche, die heute noch zu den Zweiflern und Klein­mütigen und Ungläubigen gehören, hinsehen werden auf diejenigen, die als Samen gesät worden sind, weil sie ge­braucht werden zur Lösung der großen Fragen und Rätsel, die auf der Seele lasten werden.",
        "Immer mehr und mehr werden sie gebraucht werden für den Menschheits fortschritt schon in der nächsten Zukunft für die Fragen, die nicht menschlich willkürlich sind, sondern durch das Leben mit starker Kraft gestellt werden."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "BLUT IST EIN GANZ BESONDERER SAFT Berlin, 25. Oktober 1906",
    "paragraphs": [
      "Ein jeder von Ihnen hat zweifellos im Gedächtnis, daß der heutige Vortrag, seinem Titel nach, an ein Wort des Goetheschen Faust anknüpft. Sie wissen alle, daß in diesem Gedichte dargestellt wird, wie Faust, der Repräsentant des höchsten menschlichen Strebens, einen Bund eingeht mit den bösen Mächten, die ihrerseits wieder in dem Gedichte durch Mephistopheles, den Sendling der Hölle, repräsen­tiert werden. Sie wissen alle, daß Faust einen Vertrag schlie­ßen soll mit Mephistopheles, und daß das Schriftstück dann von Faust mit Blut unterschrieben werden soll. Faust hält das zunächst für eine Posse; Mephistopheles aber spricht den an dieser Stelle von Goethe zweifellos ernst gemeinten Satz: «Blut ist ein ganz besonderer Saft».",
      "Etwas Merkwürdiges ist bei dieser Stelle des Goetheschen Faust den sogenannten Goethe-Kommentatoren passiert. Sie wissen ja, daß über Goethes Faust eine so umfangreiche Literatur existiert, daß man ganze Bibliotheken damit fül­len könnte. Natürlich kann es nicht meine Aufgabe sein, mich weiter auszulassen über dasjenige, was diese verschie­denen Goethe-Erklärer gerade über diese Fauststelle sagen; aber sie bringen nicht viel anderes zutage als das, wovon der Faustkommentar, der einer der letzten ist, von dem Universitätsprofessor Minor, ein Beispiel gibt. Er sowie andere Kommentatoren behandeln diesen Satz als etwas, das von Mephistopheles wie eine Art ironischer Bemerkung hingesprochen sein soll, und Minor macht die merkwürdige,",
      "in der Tat höchst merkwürdige Bemerkung  hören Sie genau, was er sagt, um vielleicht auch staunen zu können, auf was alles ein Goethe-Erklärer kommen kann -, die Bemerkung: «Der Teufel ist der Feind des Blutes», und er verweist dabei darauf, daß das Blut dasjenige sei, was dem Menschen eigentlich das Leben erhöht und erhält, und daß daher der Teufel, der Feind des menschlichen Geschlechtes, auch nur der Feind des Blutes sein könne. Er macht nun mit Recht darauf aufmerksam, daß schon in der ältesten Be­arbeitung der Faustsage, wie auch in der Sage überhaupt, dieses Blut dieselbe Rolle spielt.",
      "In einem alten Faustbuche wird uns klar beschrieben, wie Faust sich mit einem kleinen Federmesser die linke Hand etwas aufzuritzen hat, wie er dann das herausflie­ßende Blut in die Feder nimmt und seinen Namen unter den Pakt schreibt, wie dann auf der linken Hand das Blut gerinnt und die Worte bildet: «0 Mensch entfliehe.» Dies alles ist richtig. Aber nun die Bemerkung, daß der Teufel ein Feind des Blutes sei und die Unterschrift deshalb mit Blut fordere, eben weil er ein Feind des Blutes sei. Ich möchte Sie fragen, ob jemand sich vorstellen kann, daß er just dasjenige begehre, was ihm unsympathisch ist. Ver­nünftigerweise kann man nur voraussetzen, daß an dieser Stelle Goethe gemeint hat - daß nicht nur Goethe, sondern auch die Hauptsage und die ältere Faustdichtung einzig und allein das gemeint haben können -, daß dem Teufel an dem Blute etwas Besonderes liegt und daß es ihm nicht einerlei ist, ob er mit gewöhnlicher, neutraler Tinte den Pakt unterschrieben erhält oder mit Blut. Man kann hier nichts anderes voraussetzen, als daß der Repräsentant der bösen Mächte glaubt, ja überzeugt ist, daß er den Faust ganz besonders dadurch in der Hand haben werde, daß er sich wenigstens eines Tropfens seines Blutes bemächtigt",
      "haben wird. Das ist ganz selbstverständlich und niemand kann diese Stelle anders verstehen, als daß Faust nicht des­halb mit Blut unterschreiben soll, weil der Teufel ein Feind des Blutes ist, sondern weil er sich des Blutes bemächtigen möchte.",
      "Dem liegt eine merkwürdige Empfindung zugrunde, die Empfindung, daß derjenige, der sich des Menschen Blutes bemächtigt, die Herrschaft über den Menschen habe, und daß das Blut deshalb ein ganz besonderer Saft ist, weil es sozusagen dasjenige ist, um das eigentlich gekämpft werden muß, wenn um den Menschen in bezug auf das Gute und auf das Böse gekämpft wird.",
      "Alle diejenigen Dinge, welche aus den Sagen und Mythen des Volkes uns überkommen sind und sich auf das Men­schenleben beziehen, werden in unserer Zeit in bezug auf die ganze Anschauung und Auffassung des Menschen einer besonderen Umwandlung unterliegen. Dasjenige Zeitalter liegt hinter uns, in dem man auf Sagen, Märchen und Mythen so geblickt hat, als ob in ihnen nur kindliche Volks­phantasie sich ausspräche. Ja, selbst die Zeit liegt hinter uns, in der man in einer kindlich gelehrtenhaften Weise davon gesprochen hat, daß in der Sage die dichtende Volksseele zum Ausdruck komme. Die dichtende Volksseele ist nichts an­deres als ein Erzeugnis des grünen Gelehrtentisches, denn es gibt ebenso einen grünen Gelehrtentisch, wie es einen grünen Bürokratentisch gibt. Wer einen Blick hineingetan hat in die Volksseele, der weiß sehr gut, daß es sich im Volke nicht um Erdichtungen und dergleichen Dinge han­delt, sondern um etwas viel Tieferes, das in seinen Sagen und Märchen von wunderbaren Mächten und wunderbaren Ereignissen zum Ausdruck kommt.",
      "Wenn wir uns von dem neuen Standpunkte der Geistes­forschung aus wieder in die Sagen und Mythen vertiefen,",
      "wenn wir jene großartigen und gewaltigen Bilder, die uns aus der Urzeit überkommen sind, auf uns wirken lassen, nachdem wir mit geisteswissenschaftlichen Forschungs­methoden ausgerüstet sind, so erscheinen uns diese Mythen und Sagen so, daß sie uns zum Ausdruck einer tiefsinnigen Urweisheit werden.",
      "Wahr ist es, daß der Mensch sich zunächst frägt, wie es komme, da wir es doch ursprünglich mit primitiven Volks-stufen, primitiven Volksanschauungen zu tun haben, daß der naive Mensch sich die Welträtsel bildlich veranschau­lichen konnte in diesen Sagen und Märchen und daß, wenn wir uns heute in diese Sagen und Märchen vertiefen, wir im Bilde dasjenige erblicken, was uns die Geistesforschung heute klar enthüllt. Zunächst muß das unsere Verwunderung er­regen. Wer sich aber tiefer und tiefer einläßt in die Art und Weise, wie diese Märchen und Mythen zustande gekommen sind, dem schwindet jedes Erstaunen, jeder Zweifel und er wird nicht nur das, was man naive Anschauung nennt, in diesen Sagen und Märchen finden, sondern den weisheits­vollen Ausdruck einer uralten, wahren Weisheits-Anschau­ung der Welt erkennen. Mehr, viel mehr noch kann man lernen, wenn man die Grundlage dieser Mythen und Sagen positiv durchforscht, als wenn man die heutige verstandes-und erfahrungsmäßige Wissenschaft in sich aufnimmt. Frei­lich muß man mit den Erforschungsmethoden der Geistes­wissenschaft ausgerüstet an diese Dinge herangehen. Alles, was man in den Sagen und alten Weltanschauungen über das Blut findet, pflegt von Bedeutung zu sein, weil man in diesen uralten Zeiten eine Weisheit hatte, die über das Blut, über jenen besonderen Saft, der das fließende Menschen-leben selbst ist, und über seine Bedeutung für die Welt Bescheid wußte.",
      "Es soll uns heute nicht beschäftigen, woher in Urzeiten",
      "jene Weisheit gekommen ist, obwohl der Schluß des Vor­trages auch darauf wird hindeuten müssen. Die eigentliche Betrachtung dieses Gegenstandes soll späteren Vorträgen vorbehalten bleiben. Aber das Blut selbst, in seiner Bedeu­tung für die Menschheit und den menschlichen Kultur­prozeß, wollen wir uns heute einmal anschauen. Nicht etwa eine physiologische oder rein naturwissenschaftliche Be­trachtung soll hier geboten werden, sondern eine Betrach­tung aus der geistigen Weltanschauung heraus. Und da dringen wir am besten in jedes Ding ein, wenn wir uns zu­nächst bewußt werden, welches die Bedeutung eines uralten Satzes ist, eines Satzes, der mit der Urkultur des alten Agyptens zusammenhängt, wo die Priesterweisheit des Her­mes gewaltet hat, eines Satzes, der als Grundsatz aller Gei­steswissenschaft gilt, der der hermetische Grundsatz genannt worden ist und der heißt: «Es ist oben alles wie unten.»",
      "Sie können manche dilettantische Erklärung dieses Satzes finden. Diejenige Erklärung aber, die uns zunächst heute hier beschäftigen soll, ist die folgende. Alle Geisteswissen­schaft ist sich darüber klar, daß die Welt, die dem Menschen zunächst durch seine fünf Sinne zugänglich ist, nicht die ganze Welt darstellt, sondern daß sie nur der Ausdruck ist für eine tiefere, hinter ihr verborgene Welt, die geistige Welt. Diese geistige Welt wird im Sinne dieses hermetischen Grundsatzes die obere Welt genannt, und die sinnliche Welt, die sich um uns herum ausbreitet, die wir mit unseren Sinnen wahrnehmen und mit unserem Verstande erforschen können, gilt als untere, als der Ausdruck der geistigen Welt. So daß der Geistesforscher in dieser sinnlichen Welt kein Letztes sieht, sondern eine Art Physiognomie, die ihm eine dahinterliegende seelische und geistige Welt ausdrückt, ge­nau so wie man, wenn man das menschliche Antlitz betrach­tet, nicht bei den Formen des Gesichtes und der Gesten",
      "stehenbleiben darf, sondern selbstverständlich von den Gesten und der Physiognomie auf dasjenige hingeführt wird, was sich seelisch und geistig in ihnen ausdrückt.",
      "Dasjenige, was jeder Mensch naiv tut, wenn er einem beseelten Wesen gegenübertritt, das macht der Okkultist oder der Geistesforscher der ganzen Welt gegenüber. «Es ist oben alles wie unten» würde, auf den Menschen angewandt, heißen: Es drücken sich diejenigen Impulse in seinem Ge­sichte aus, die in seiner Seele liegen: in einem harten, rohen Antlitz die Roheit der Seele, in einem Lächeln innerlicher Frohsinn, in den Tränenperlen die Leiden der Seele.",
      "Lassen Sie mich an der Frage, was eigentlich Weisheit ist, den hermetischen Grundsatz einmal darlegen. Es wurde in der Geisteswissenschaft immer davon gesprochen, daß die Weisheit des Menschen etwas zu tun habe mit der Erfah­rung, und zwar mit schmerzlicher Erfahrung. Derjenige, der unmittelbar in Schmerz und Leiden darinnensteckt, wird innerhalb dieses Schmerzes und Leidens vielleicht etwas zeigen, was innerliche Disharmonie ist. Derjenige aber, der die Schmerzen und Leiden überwunden hat und ihre Frucht in sich trägt, wird Ihnen immer wieder nur das sagen, daß er damit etwas von Weisheit aufgenommen hat. Die Freu­den und Lüste des Lebens, das, was mir das Leben geboten hat an Befriedigungen, das nehme ich dankbar hin; aber weniger als das alles möchte ich hingeben meine Schmerzen und Leiden, die hinter mir liegen: Meinen Schmerzen und Leiden verdanke ich die Weisheit. So hat von jeher die Geistesforschung in der Weisheit etwas gesehen wie kristal­lisierten Schmerz, der überwunden ist und sich in sein Ge­genteil verwandelt hat.",
      "Interessant ist es nun, daß die gegenwärtige mehr mate­rialistische Forschung in einer eigenartigen Weise gerade darauf zurückgekommen ist. In jüngster Zeit ist ein schönes",
      "Buch erschienen über die Mimik des Denkers, ein Buch, das lesenswert ist. Das Buch ist von keinem Theosophen, son­dern von einem Natur- und Seelenforscher. Er versucht zu zeigen, wie sich das innere Leben des Menschen, seine Art und Weise des Vorstellens, zum Ausdrucke bringt in der Physiognomie, und auch dieser Forscher macht darauf auf­merksam, daß der Denker immer etwas in seinem Gesichts­ausdruck hat, das an absorbierten Schmerz erinnert.",
      "So sehen Sie, als eine schöne Bestätigung eines uralten Grundsatzes der Geisteswissenschaft, diesen Grundsatz wie­der in der mehr materialistischen Anschauung unserer Zeit auftauchen. Das werden Sie noch tiefer und tiefer einsehen, und Sie werden finden, wie Zug um Zug dasjenige, was uralte Weisheit ist, der heutigen Wissenschaft wiederum zugänglich wird.",
      "Es macht das Wesen der Geistesforschung aus, daß alles, was uns in der Welt umgibt - das mineralische Gerüst, die Pflanzendecke, die Tierwelt unserer Erde -, als der physio­gnomische Ausdruck oder das Untere eines Oberen, eines dahinterliegenden geistigen Lebens angesehen wird. Vom okkulten oder geisteswissenschaftlichen Standpunkt aus wird dasjenige, was uns in der sinnlichen Welt gegeben wird, erst richtig verstanden, wenn man dazu das Obere, das geistige Vorbild, die geistigen Urwesen, aus denen das alles hervorgegangen ist, kennt. So soll uns heute beschäftigen, was hinter der Erscheinung des Blutes verborgen liegt, das­jenige, was sich in dem Blute einen physiognomischen Aus­druck hier in der Sinnenwelt schuf. Hat man dann diesen geistigen Hintergrund des Blutes, dann wird man auch ein­sehen, wie eine solche Erkenntnis zurückwirken muß auf unser ganzes geistiges Kulturleben.",
      "Große Fragen drängen sich in unserer Zeit an den Men­schen heran: Fragen der Erziehung nicht nur des jungen",
      "Menschen, sondern Fragen der Erziehung ganzer Völker, und auch die große Erziehungsfrage, die die Zukunft an die Menschheit stellen wird. Sie muß jeder erblicken, wenn er sein Auge auf die großen sozialen Umwälzungen unserer Zeit richtet, auf die sozialen Forderungen, die überall auf­treten, seien sie verkörpert in der Frauenfrage, in der sozialen Frage, in der Friedensfrage und so weiter. Alles das tritt vor unsere sorgende Seele. Alle diese Fragen wer­den hell und klar, wenn wir das, was als geistige Wesenheit hinter dem Blute liegt, kennen.",
      "Wer wollte leugnen, daß mit dieser Frage auch die Ras­senfrage zusammenhängt, die bezeichnenderweise auch in unserer Gegenwart wieder auftritt? Wir verstehen die Rassenfrage aber nur, wenn wir das geheimnisvolle Wirken des Blutes und der Blutmischung unter den Völkern ver­stehen. Endlich hängt auch noch eine Frage damit zusam­men, die immer aktueller und aktueller werden wird, je mehr man sich aus einem bloß ziellosen Vorgehen in dieser Sache herauswindet und durchringen wird zu einem ein­heitsvollen Vorgehen auf diesem Gebiete. Die Frage, auf die hier hingedeutet wird, ist die Kolonisationsfrage, jene Frage, die auftaucht, wenn Menschen kultivierter Völker mit unkultivierten Völkern zusammenkommen: Inwiefern können unkultivierteVölker neue Kulturen in sich aufneh­men? Wie kann ein Schwarzer, wie kann ein barbarischer Wilder kultiviert werden, wie hat man sich ihnen gegen­über zu benehmen? Da kommen nicht bloß die Gefühle einer schattenhaften Moral in Betracht, sondern große, ernste und bedeutsame Lebensfragen des Daseins. Derjenige, der nicht weiß, unter welchen Bedingungen ein Volk steht, ob in auf­oder absteigender Linie der Entwicklung, ob dies oder jenes durch sein Blut bedingt ist, der vermag nicht den richtigen Weg zu finden, um irgendeine Kultur bei einem anderen",
      "Volke einzuführen. Alles das taucht auf, wenn diese bedeu­tungsvolle Frage nach dem Blute aufgeworfen wird.",
      "Was das Blut als solches ist, das kennen Sie ja wohl alle aus der landläufigen Naturwissenschaft. Sie wissen, wenn Sie den Menschen und die höheren Tiere betrachten, daß dieses Blut wirklich das fließende Leben ist. Sie wissen, daß durch das Blut des Menschen Inneres nach außen geöffnet wird, und indem dies geschieht, nimmt der Mensch durch das Blut die Lebensluft, den Sauerstoff auf. Das Blut erfährt durch diese Sauerstoffaufnahme eine Erneuerung. Das­jenige Blut, welches das menschliche Innere gleichsam dem hereinströmenden Sauerstoff anbietet, ist eine Art von Gift-stoff für den Organismus, eine Art Vernichter und Zer­störer. Dieses blaurote Blut wird umgewandelt durch Auf­nahme von Sauerstoff, durch eine Art Verbrennungsprozeß, in rotes, lebenschaffendes Blut. Dieses Blut, das in alle Teile des Körpers dringt, in allen Teilen des Körpers die Ernäh­rungsstoffe ablagert, hat die Aufgabe, die Stoffe der Außen­welt unmittelbar in sich aufzunehmen und auf dem kür­zesten Wege zur Ernährung des Wesens zu verwenden. Der Mensch und die höheren Tiere haben nötig, erst diese Er­nährungsstoffe in das Blut überzuführen, das Blut zu bilden, den Sauerstoff der Luft in das Blut aufzunehmen und den Körper durch das Blut aufzubauen und zu erhalten.",
      "Nicht mit Unrecht hat ein geistvoller Seelenkenner ge­sagt: Das Blut mit seiner Bewegung ist wie ein zweiter Mensch, der sich zu dem anderen aus Knochen, Muskeln und Nervenmasse bestehenden Menschen wie eine Art von Außenwelt verhält. Und in der Tat nimmt der ganze Mensch fortwährend aus dem Blute seine Erhaltungskräfte auf und gibt andererseits dasjenige, was er nicht gebraucht hat, an das Blut ab. Im Blute ist also ein wirklicher Doppelgänger des Menschen vorhanden, der ihn fortwährend begleitet,",
      "aus dem er fortwährend seine neuen Kräfte schöpft und an den er dasjenige, was er nicht mehr braucht, abgibt. Mit vol­lem Recht hat man daher das Blut das fließende Menschen­leben genannt und ihm ähnliche Bedeutung beigemessen wie dem Zellstoff für die niederen Organismen. Was der Zellstoff für den niederen Orgnismus ist, das ist der so vielfach um-gewandelte «besondere Saft», das Blut, für den Menschen.",
      "Ein bedeutender Forscher, Ernst Haeckel, hat tief in die Werkstatt der Natur hineingeschaut und mit Recht in popu­lären Werken darauf aufmerksam gemacht, daß das Blut eigentlich am spätesten im Organismus entsteht. Wenn man die Entwicklung des Menschenkeims im Mutterleibe ver­folgt, so findet man, daß die Anlagen zum Knochen- und Muskelbau längst ausgebildet sind, bevor die Anlage zur Blutbildung entsteht. Erst sehr spät werden die Anlagen zur Blutbildung - mit ihr das Blutgefäß-System - im Men­schen sichtbar; erst sehr spät kommen sie heraus. Daraus schließt die Naturwissenschaft mit Recht, daß die Blut-bildung überhaupt erst spät in der Weltentwicklung auf­getreten ist, daß sozusagen andere Kräfte, die da waren, erst bis zur Höhe des Blutes heraufgehoben worden sind, um auf dieser Höhe dasjenige zu bewirken, was innerhalb des Menschen bewirkt werden soll. Wenn der Mensch als Men­schenkeim die früheren Stadien der Menschheits entwicklung durchmacht, sie noch einmal wiederholt, dann eignet er sich erst dasjenige an, was vor der Blutbildung in der Welt vor­handen war, um dann der Evolution in der Umwandlung, in der Heraufhebung alles Früheren zu diesem besonderen Saft, dem Blute, die Krone aufzusetzen.",
      "Wollen wir nun die hinter dem Blute waltenden geheim­nisvollen Gesetze des geistigen Universums studieren, dann müssen wir uns mit den elementarsten Begriffen der Gei­steswissenschaft ein wenig befassen. Schon oft sind diese",
      "elementaren Begriffe der Geisteswissenschaft hier ausein­andergesetzt worden. Sie werden sehen, daß diese elemen­taren Begriffe der Geisteswissenschaft das Obere sind, und daß sich uns dieses Obere, wenn wir es kennengelernt haben, in den bedeutungsvollen Gesetzen des Blutes, wie in denen des übrigen Lebens, zum Ausdruck bringt wie in einer Physiognomie.",
      "Diejenigen, welche diese elementaren Ge­setze der Geisteswissenschaft längst kennen, gestatten mir wohl, daß ich für die, welche zum ersten Male hier sind, kurz wiederhole. Dabei werden auch Ihnen solche Gesetze immer klarer und klarer werden, wenn Sie sie immer wie­der in besonderen neuen Fällen anwenden lernen.",
      "Freilich für diejenigen, die noch nichts wissen von Geisteswissen­schaft, die sich noch nicht eingelebt haben in die Lebens- und Weltanschauung, um die es sich hier handelt, ist, was ich jetzt sagen werde, mehr oder weniger nur eine Zusammen­stellung von Worten, unter denen sie sich nichts denken können. Aber es ist ja nicht immer der Mangel eines hinter dem Worte steckenden Begriffes daran schuld, wenn sich jemand bei einem Worte nichts denken kann.",
      "Es kann hier eine Bemerkung, die der geistvolle Licktenberg gemacht hat, etwas verändert angenommen werden: Wenn ein Kopf und ein Buch zusammenstoßen und es hohl klingt, so muß nicht immer das Buch daran schuld sein. So ist es auch bei der Beurteilung der geisteswissenschaftlichen Wahrheiten von seiten unserer Zeitgenossen.",
      "Wenn diese Wahrheiten den Menschen oftmals als bloße Worte an die Ohren klingen und sie sich nichts dabei denken können, so muß nicht im­mer die Geisteswissenschaft daran schuld sein. Derjenige aber, der sich einlebt in diese Dinge, der wird sehen, daß hinter den Bezeichnungen und Hinweisen auf höhere We­senheiten auch wirklich solche Wesenheiten stecken, die nicht in unserer sinnlichen Welt zu finden sind.",
      "In der geisteswissenschaftlichen Weltanschauung sehen wir, daß der Mensch, insofern er uns in der Außenwelt für unsere Sinne entgegentritt, insofern er Form und Gestalt ist, nur einen Teil der menschlichen Wesenheit ausmacht, und daß sogar hinter dem physischen Leibe viele andere Wesenheiten sind. Diesen physischen Leib hat der Mensch mit allen um ihn herumliegenden mineralischen, sogenann­ten leblosen Dingen gemeinschaftlich.",
      "Darüber hinaus hat aber der Mensch den sogenannten Ather- oder Lebensleib. Ather wird hier nicht in dem Sinne verstanden, wie die physische Wissenschaft es tut. Dieser Ather- oder Lebensleib ist ein Prinzip, das für den geisteswissenschaftlichen For­scher nicht bloß etwas Erdachtes, nicht bloß etwas Aus­spekuliertes ist, sondern etwas, das für seine geöffneten geistigen Sinne ebenso wirklich vorhanden ist wie die äuße­ren sinnlichen Farben für das sinnliche Auge.",
      "Zu sehen, wirklich zu sehen ist für den hellsehenden Menschen dieser Ather- oder Lebensleib. Er ist dasjenige, was die unorgani­schen Stoffe zu lebendigem Dasein aufruft, sie heraufholt aus der Leblosigkeit, um sie aufzufädeln an dem Faden des Lebens.",
      "Glauben Sie nicht, daß dieser Lebensleib für den okkulten Forscher nur etwas ist, was er zum Leblosen hin­zudenkt. Das versuchen die Naturforscher. Sie versuchen das, was sie mit dem Mikroskop und so weiter an den Dingen sehen können, zu vervollständigen, sich etwas zu erdenken, was sie dann das Lebensprinzip nennen.",
      "Auf diesem Standpunkt steht die geisteswissenschaftliche For­schung nicht, sie hat ein bestimmtes Prinzip. Sie sagt sich nicht: Hier stehe ich als Forscher so, wie ich nun einmal bin. Was es in der Welt gibt, muß sich meinem gegenwär­tigen Standpunkt fügen.",
      "Was ich nicht erkennen kann, das gibt es nicht. - Das ist ungefähr ebenso gescheit, wie wenn ein Blinder sagt, die Farben seien eine phantastische Sache.",
      "Es hat nicht derjenige über eine Sache zu entscheiden, der nichts darüber weiß, sondern derjenige, welcher etwas dar­über erlebt hat. Der Mensch ist in Entwicklung begriffen. Daher sagt die Geisteswissenschaft: Wenn du so bleibst, wie du bist, so kannst du nichts vom Atherleibe sehen, und kannst in der Tat von «Grenzen des Erkennens» und von «Ignorabismus» sprechen; wirst du aber ein anderer, eignest du dir die nötigen Fähigkeiten an, um die geistigen Dinge wahrzunehmen, so kann nicht von Grenzen der Erkenntnis gesprochen werden. Nur so lange gibt es diese, als der Mensch seine inneren Sinne nicht geöffnet hat. Daher ist auch der Agnostizismus nichts als eine drückende Last für unsere Kultur. Er sagt: Der Mensch ist so und so, und wenn er so und so ist, so kann er auch nur dies und das erkennen. Darauf ist zu antworten: Wenn er heute so und so ist, so muß er eben anders werden, und dann wird er auch anderes erkennen.",
      "Das zweite Glied des Menschen ist also der Atherleib, den der Mensch gemeinschaftlich mit der Pflanzenwelt hat.",
      "Das dritte Glied ist der sogenannte Astralleib, sehr schön und bedeutungsvoll so genannt, und es soll hier auch später noch einmal gezeigt werden, daß dieser Astralleib mit Recht so genannt wird. Theosophen, die für diesen Namen einen anderen wählen wollten, haben keine Ahnung davon, um was es sich hier handelt. Dem Astralleib obliegt es, im Men­schen und im Tiere, das Lebendige zur Empfindungssub­stanz aufzurufen, so daß sich innerhalb des Lebendigen nicht bloß Säfte bewegen, sondern daß sich darin dasjenige ausdrückt, was man Lust und Leid, Freude und Schmerz nennt. Damit haben Sie im wesentlichen auch den Unter­schied zwischen Pflanze und Tier angedeutet, obwohl es Übergänge gibt.",
      "Eine neue naturwissenschaftliche Forschergruppe hat geglaubt,",
      "auch den Pflanzen im direkten Sinne Empfindung zuschreiben zu sollen. Das ist aber nur ein Spiel mit Wor­ten. Es ist für gewisse Pflanzen selbstverständlich, daß sie Erregungszustände haben, wenn etwas in ihre Nähe kommt, wenn etwas auf sie einwirkt. Das ist aber keine Empfin­dung. Es muß im Innern des Geschöpfes ein Bild auftauchen als Reflex der Erregung. Wenn auch bei gewissen Pflanzen eine Gegenwirkung auf einen äußeren Eindruck geschieht, so ist das doch noch kein Beweis dafür, daß die Pflanze auch innerlich einen solchen Reiz zu einer Empfindung erhebt, daß sie ihn innerlich erlebt. Dasjenige, was man innerlich erlebt, hat seinen Sitz im Astralleibe. So sehen wir also, daß das, was bis zum Tier heraufkam, aus dem physischen Leib, dem Ather- oder Lebensleib und dem Astralleib besteht.",
      "Der Mensch ragt nun über das Tier durch etwas ganz Besonderes hinaus, und das, wodurch er über das Tier hin­ausragt, haben sinnige Menschen immer gefühlt. Es wird darauf hingewiesen durch das, was Jean Paul in seiner Lebensbeschreibung selbst von sich sagt: er erinnere sich ganz genau, wie ihm als kleines Kind im Hofe seines Eltern-hauses der Gedanke durch die Seele schoß: du bist ja ein «Ich», du bist ja eine Wesenheit, die innerlich zu sich Ich sagen kann. Das machte auf ihn einen bedeutenden Ein­druck.",
      "Alle sogenannte äußerliche Seelenkunde übersieht das Wichtigste, worauf es in diesem Punkte ankommt. Folgen Sie mir für einige Minuten in eine subtile Betrachtung hin­ein, die Ihnen aber zeigen wird, um was es sich handelt. Im ganzen Umkreis der deutschen Sprache gibt es ein einziges Wörtchen, das sich von allen anderen Wörtern prinzipiell unterscheidet. Von jedem Dinge, das hier in diesem Saale ist, kann jeder von Ihnen den Namen dieses Dinges nennen. Den Tisch kann jeder Tisch, den Stuhl kann jeder Stuhl",
      "nennen. Aber ein Wort, einen Namen gibt es, den Sie nicht aussprechen können außer für das, dem dieser Name zu­kommt: das ist das Wörtchen «Ich». Niemand kann zu einem anderen «Ich» sagen. Das «Ich» muß heraustönen aus der innersten Seele selbst, es ist der Name, den sich nur die Seele selbst beilegen kann. Jeder andere ist für mich ein «Du», und ich selbst bin für jeden anderen ein «Du».",
      "Alle Religionen empfanden dieses Ich als den Ausdruck für jenes Wesen in der Seele, durch das die Seele in sich selbst ihre Grundwesenheit, ihr Göttliches, sprechen zu las­sen vermag. Da beginnt dann dasjenige, was niemals durch die äußeren Sinne eindringen kann, was niemals in seiner Bedeutung von außen benannt werden kann, sondern aus dem Innersten heraus ertönen muß. Da beginnt jener Mono­log, jenes Selbstgespräch der Seele, wodurch das göttliche Selbst in der Seele sich ankündigt, wenn die Bahn frei wird für das Einziehen des Geistes in die Seele.",
      "In den älteren Kulturreligionen, noch im alten Hebrä­ischen, hat man diesen Namen «den unaussprechlichen Na­men Gottes» genannt, und was auch die heutige Philologie übersetzen mag, der alte jüdische Gottesname bedeutet nichts anderes als das, was heute durch das deutsche Wort «Ich» ausgedrückt wird. Bewegung ging durch die Reihen der Zuhörer, wenn der Name des «unbekannten Gottes» durch den Eingeweihten gesprochen wurde, wenn geahnt wurde, was durch dieses Wort ausgedrückt war, wenn das «Ich bin der Ich-Bin» im Tempel ertönte. In diesem Wort drückt sich das vierte Glied der menschlichen Wesenheit aus, das der Mensch im Umkreis seines irdischen Daseins für sich allein hat. Dieses Ich umschließt wiederum und bildet in sich aus die Keime zu höheren Stufen des Menschentums. Nur hingewiesen soll darauf werden, was in der mensch­lichen Entwicklung durch dieses vierte Glied in Zukunft",
      "zum Dasein gebracht werden wird, hingewiesen soll werden darauf, daß der Mensch aus dem physischen Leib, dem Atherleib, dem Astralleib und dem Ich oder dem eigent­lichen inneren Leben besteht, und daß in diesem inneren Leben die Keime zu drei weiteren Stufen der Entwicklung vorhanden sind, die aus dem Blute erstehen werden, näm­lich Manas, Buddhi und Atma, oder mit deutschen Worten:",
      "Manas = Geistselbst im Gegensatz zum Körperselbst, Buddhi = Lebensgeist, Atma = Geistmensch, der eigent­liche, wahre Geistmensch, der heute dem Menschen nur als Ideal vorschwebt, der als kleiner Keim im Innern veran­lagt ist und in ferner Zukunft seine Vollendung erreichen wird.",
      "So haben wir, wie im Regenbogen sieben Farben, wie in der Tonskala sieben Töne, im Reich der Atome sieben Stu­fen der Atomgewichte, die siebenstufige Skala des Men­schenwesens, die wieder in vier untere und in drei obere Stufen zerfällt.",
      "Nun versuchen wir, uns einmal klar zu werden darüber, wie sich dieses Obere, Geistige, einen physiognomischen Ausdruck verschafft in dem Unteren, wie es uns vor Augen tritt in der Sinneswelt. Nehmen Sie zunächst dasjenige, was sich im Menschen zu seinem physischen Leib kristalli­siert. Er hat es gemeinschaftlich mit der sogenannten leb­losen Natur. Wenn wir geisteswissenschaftlich sprechen von diesem physischen Leib, dann sprechen wir gar nicht ein­mal von dem, was das Auge sieht, sondern von dem Zu­sammenhang von Kräften, die den physischen Leib kon­struiert haben, von dem, was als Kraftnatur hinter dem physischen Leibe steht.",
      "Sehen wir uns die Pflanze an als das Wesen, das schon den Atherleib hat, welcher die physischen Stoffe heraufholt zum Leben, das heißt dasjenige, was sinnliche Materie ist,",
      "in Lebenssäfte verwandelt. Was ist es, das so die sogenann­ten leblosen Kräfte in die Lebenssäfte umgestaltet? Wir nennen es den Atherleib, und dieser Atherleib tut dasselbe im Tier und dasselbe auch im Menschen; er ruft dasjenige, was bloß sinnlich ist, zu lebendiger Konfiguration, zu leben­diger Gestaltung auf. Dieser Atherleib wird wieder durch­setzt von dem Astralleib. Und was macht dieser Astralleib? Er ruft die bewegte Substanz zum innerlichen Miterleben des Kreislaufs der stofflichen Säftebewegung auf, sodaß sich die äußere Bewegung in innerlichen Erlebnissen spiegelt.",
      "Wir sind damit so weit gekommen, daß wir den Men­schen begreifen, insofern er in das Tierreich hineingestellt ist. Alle Substanzen, aus denen der Mensch zusammen­gesetzt ist, finden Sie auch draußen in der leblosen Natur:",
      "Sauerstoff, Stickstoff, Wasserstoff, Schwefel, Phosphor und so weiter. Soll das, was umgewandelt ist durch den Ather­leib in lebendige Substanz, zu innerlichem Erfassen, zur Schaffung innerer Spiegelbilder von dem, was außen vor­geht, aufgerufen werden, so muß der Atherleib von dem, was wir Astralleib nennen, durchdrungen werden. Der Astralleib ruft die Empfindung hervor. Aber jetzt, auf dieser Stufe ruft der Astralkörper die Empfindung in ganz besonderer Weise hervor. Der Atherleib wandelt unorga­nische Substanz in Lebenssäfte um, der Astralleib wandelt diese lebendige Substanz in empfindende Substanz um. Aber",
      "- und das bitte ich besonders zu beachten - was empfindet eine Wesenheit, die nur mit diesen drei Leibern ausgestattet ist? Sie empfindet nur sich selbst, nur die eigenen Lebens­vorgänge, sie führt ein in sich abgeschlossenes Leben. Das ist eine höchst interessante Tatsache von außerordentlicher Wichtigkeit, wert, festgehalten zu werden. Sehen Sie sich einmal ein niederes Tier an. Was hat es ausgebildet? Um­gestaltet hat es leblose Substanz in lebendige Substanz,",
      "lebendige, bewegliche Substanz in empfindende Substanz. Und empfindende Substanz ist nur da, wo wenigstens die Anlage zu dem vorhanden ist, was später im ausgebildeten Nervensystem erscheint. So haben wir also leblose Sub­stanz, lebendige Substanz und von empfindungsbegabten Nerven durchsetzte Substanz. Wenn Sie sich einen Kristall ansehen, so haben Sie sich zunächst in dieser Kristallform einen Ausdruck gewisser Naturgesetze, die im sogenannten leblosen Reich draußen herrschen, vorzustellen. Kein Kri­stall könnte zustande kommen ohne die ganze ihn um­gebende Natur. Sie können kein Glied aus dem Kosmos herausreißen und für sich hinstellen, ebensowenig wie Sie den Menschen aus seiner ganzen Umgebung herausreißen können, der, wenn er nur ein paar Meilen über die Erde erhoben würde, sterben müßte. Wie er nur denkbar ist an dem Orte, an dem er ist, wo die entsprechenden Kräfte sich in ihm zusammenfügen, in ihm leben müssen, so ist es schon beim Kristall der Fall, und wer den Kristall richtig an­schaut, wird in ihm die ganze Natur, den ganzen Kosmos in einem Einzelabdruck sehen. Es ist ganz richtig, was Cuvier gesagt hat, daß ein vollkommener Anatom aus einem Kno­chen schließen kann, was für einem Tier derselbe angehört hat, weil jedes Tier seine ganz besonderen Knochenformen haben muß.",
      "So lebt auch in der Form des Kristalls der ganze Kosmos. Und ebenso drückt sich in der lebendigen Substanz eines Einzelwesens der ganze Kosmos aus. Die bewegten Säfte eines Wesens sind schon eine kleine Welt, ein Abdruck der großen Welt. Und wenn die Substanz zur Empfindung auf­gerufen wird, was lebt dann in den Empfindungen des ein­fachsten Wesens? In diesen Empfindungen sind die kos­mischen Gesetze gespiegelt, so daß das einzelne lebendige Wesen mikrokosmisch in sich den ganzen Makrokosmos",
      "empfindet. Das Empfindungsleben eines einfachen Wesens ist also ein Abdruck des Kosmos, wie der Kristall ein Ab­druck seiner Form ist. Mit einem dumpfen Bewußtsein hat man es in solch einfachem Lebewesen zu tun. Aber was dieses Bewußtsein an größerer Dumpfheit hat, das ist auf der anderen Seite ausgeglichen durch den größeren Umfang. Der ganze Kosmos leuchtet in dem dumpfen Bewußtsein, im Innern des Lebenswesens auf. Nun ist aber im Men­schen auch nichts anderes vorhanden als eine kompliziertere Ausbildung derjenigen drei Leiber, die in dem einfachsten empfindenden Lebewesen sich finden. Nehmen Sie den Menschen und sehen Sie ab von seinem Blute, nehmen Sie ihn als ein Wesen, das geformt ist von der Substanz der es umgebenden physischen Welt, das ebenso wie die Pflanze Säfte in sich enthält, die es zu lebendiger Substanz aufruft, und in die es sich ein Nervensystem eingliedert. Dieses erste Nervensystem ist das sogenannte sympathische. Das sym­pathische Nervensystem im Menschen dehnt sich zu beiden Seiten längs des Rückgrats aus, hat auf jeder Seite eine Reihe von Knoten, verzweigt und verästelt sich und schickt seine Fäden zu den verschiedenen Organen: Lunge, Ver­dauungswerkzeuge und so weiter. Es ist durch Seitenstränge mit dem Rückenmark verbunden.",
      "Zunächst bedeutet dieses sympathische Nervensystem das Empfindungsleben, das Ihnen eben geschildert worden ist. Der Mensch kann aber mit seinem Bewußtsein nicht hinunterreichen zu dem, was durch diese Nerven von den Weltvorgängen abgespiegelt wird. Diese Nerven sind Aus­drucksmittel. Und so, wie das Menschenleben aufgebaut ist aus der umliegenden kosmischen Welt, so spiegelt sich wider in dem sympathischen Nervensystem diese kosmische Welt. Diese Nerven leben ein dumpfes Innenleben. Könnte der Mensch untertauchen in dieses sympathische Nervensystem,",
      "so würde er, wenn er sein oberes Nervensystem einschlä­ferte, wie in einem Lichtleben die großen Gesetze des Kos­mos walten und wirken sehen. Es gab beim Menschen der Vorzeit ein heute überwundenes Hellsehen, welches man erkennen kann, wenn durch besondere Vorgänge die Tätig­keit des höheren Nervensystems ausgeschaltet und dadurch das untere Bewußtsein freigemacht wird. Dann lebt der Mensch in dem Nervensystem, das zum Spiegel für die Welt um ihn herum wird, in einer eigenartigen Weise. Ge­wisse niedere Tiere haben sich diese Stufe des Bewußtseins allerdings erhalten und bewahren sie noch heute. Es ist also ein dumpfes, dämmerhaftes Bewußtsein, aber es ist wesent­lich umfassender als das gegenwärtige Menschenbewußtsein. Es spiegelt als dumpfes Innenleben eine weiterreichende Welt, nicht bloß den kleinen Ausschnitt, den der heutige Mensch wahrnimmt.",
      "Für den Menschen tritt aber etwas anderes ein. Hat im Laufe der Entwicklung bis zum sympathischen Nerven­system der Kosmos ein Spiegelbild gefunden, so öffnet sich auf dieser Stufe der Entwicklung das Wesen wieder nach außen: dem sympathischen System gliedert sich das Rücken­mark ein. Das Rückenmark- und Gehirnsystem führt dann hin zu den Organen, die mit der Außenwelt die Verbindung herstellen. Wenn im Menschen die Bildung so weit ist, dann ist er nicht mehr berufen, bloß die ursprünglichen Bildungs-gesetze des Kosmos in sich spiegeln zu lassen, sondern es tritt das Spiegelbild selbst in ein Verhältnis zur Umgebung. Wenn das sympathische Nervensystem sich zusammen-gegliedert hat mit den höheren Teilen des Nervensystems, so ist dies ein Ausdruck der vor sich gegangenen Umwand­lung des Astralleibes. Dieser lebt dann nicht mehr bloß das kosmische Leben im dumpfen Bewußtsein mit, sondern er fügt sein besonderes Innenleben zu diesem hinzu. Durch",
      "das sympathische Nervensystem empfindet ein Wesen, was außer ihm vorgeht, durch das höhere Nervensystem das­jenige, was in ihm vorgeht. Und durch die höchste Form des Nervensystems, die gegenwärtig in der allgemeinen Mensch­heitsentwicklung zum Vorschein kommt, wird aus dem höher gegliederten Astralleib wieder das Material entnom­men, um Bilder der Außenwelt, Vorstellungen, zu schaffen. Der Mensch hat also die Fähigkeit verloren, die ursprüng­lichen dumpfen Bilder der Außenwelt zu erleben; er empfin­det sein Innenleben und baut sich aus diesem seinem Innen­leben auf höherer Stufe eine neue Bilderwelt auf, die ihm zwar ein kleineres Stück der Außenwelt spiegelt, aber in hellerer, vollkommenerer Art.",
      "Mit dieser Umwandlung geht, auf höherer Stufe der Entwicklung, eine andere Hand in Hand. Es dehnt sich die Umgestaltung des Astralleibes bis auf den Atherleib aus. Ebenso wie der Ä therleib in seiner Umgestaltung den Astral­leib hervorruft, wie zum sympathischen Nervensystem das Rückenmark- und Gehirnsystem hinzukommen, so bewirkt dasjenige, was von dem Atherleibe nach Aufnahme der niederen Säftezirkulation herausgewachsen und frei gewor­den ist, die Umsetzung der niederen Säfte in das, was wir Blut nennen. Das Blut ist ebenso ein Ausdruck des indi­vidualisierten Atherleibes wie das Gehirn und Rückenmark ein Ausdruck des individualisierten Astralleibes. Und durch diese Individualisierung kommt das zustande, was sich in dem «Ich» auslebt.",
      "Wenn wir von diesem Gesichtspunkte aus den Menschen in seiner Entwicklung so weit verfolgt haben, so sehen wir, daß wir zunächst eine fünfgliedrige Kette haben, die sich uns wie folgt zusammenschließt: erstens der physische Leib, zweitens der Atherleib, drittens der Astralleib, oder erstens die unorganischen, neutralen, physischen Kräfte, zweitens",
      "die Lebenssäfte, die sich auch in der Pflanze finden, drittens das niedere oder sympathische Nervensystem, viertens der von dem niederen astralen Leibe herausgehobene höhere Astralleib, der im Rückenmark und Gehirn seinen Aus­druck findet, fünftens dasjenige Prinzip, das den Atherleib individualisiert.",
      "So wie diese zwei Prinzipien individualisiert worden sind, so wird auch für den Menschen das erste Prinzip indi­vidualisiert, durch welches die leblosen Stoffe von außen eindringen und den menschlichen Körper aufbauen. Diese Umwandlung ist beim heutigen Menschen erst in der ersten Anlage vorhanden.",
      "Wir sehen, wie die äußeren formlosen Stoffe einfließen in den menschlichen Leib, wie der Atherleib diese Stoffe zu lebendigen Gebilden aufruft und wie dann durch den Astral-leib Bilder der Außenwelt geformt werden; wie weiter dieser Reflex der Außenwelt sich zu inneren Erlebnissen entfaltet und dann dieses Innenleben aus sich selbst wieder Bilder der Außenwelt erzeugt.",
      "Greift nun die Umwandlung auf den Atherleib über, so entsteht das Blut. Das Blutgefäß-System mit dem Herzen ist ein Ausdruck des umgewandelten Atherleibes, wie das Rückenmark- und Gehirnsystem ein solcher des umgewan­delten Astralleibes. Wie durch das Gehirn die Außenwelt verinnerlicht wird, so wird durch das Blut diese Innenwelt in dem Leib des Menschen zu einem äußeren Ausdrucke umgeschaffen. Ich muß im Gleichnisse sprechen, wenn ich die hier in Betracht kommenden komplizierten Vorgänge darstellen will. Das Blut nimmt die durch das Gehirn ver­innerlichten Bilder der Außenwelt auf, gestaltet sie zu lebendigen Bildungskräften um und bildet durch sie den jetzigen Menschenleib aus. Das Blut ist so der Stoff, der den menschlichen Leib auferbaut. Es stellt sich hier ein Vorgang",
      "uns vor Augen, durch den das Blut das Höchste aufnimmt, was es der Umwelt entnehmen kann, den Sauerstoff, näm­lich dasjenige, was das Blut stets wieder erneuert, mit neuem Leben versorgt. Dadurch wird das Blut veranlaßt, sich der Außenwelt zu öffnen.",
      "Damit haben wir den Weg verfolgt von der Außenwelt zur Innenwelt und wieder zurück vom Innern zum Außern. Nun ist ein Zweifaches möglich. Wir sehen, daß die Entstehung des Blutes da liegt, wo der Mensch als selbständiges Wesen der Außenwelt entgegen­tritt, wo er aus den Empfindungen, zu denen die Außenwelt geworden ist, selbständig wiederum Gestalten und Bilder schafft, wo er schöpferisch wird, wo also das Ich, der Eigen­wille aufleben kann.",
      "Kein Wesen, in dem dieser Vorgang noch nicht stattgefunden hat, könnte aus sich selbst heraus Ich sagen. Im Blute liegt das Prinzip für die Ich-Werdung. Ein Ich kann nur da zum Ausdrucke kommen, wo ein Wesen die Bilder, die es von der Außenwelt erzeugt, in sich selbst zu gestalten vermag.",
      "Ein Ich-Wesen muß fähig sein, die Außenwelt in sich aufzunehmen und innerhalb seiner selbst wieder zu erzeugen. Hätte der Mensch bloß Gehirn, so könnte er nur Bilder der Außenwelt in sich erzeugen und in sich erleben; er würde dann zu sich nur sagen können: Die Außenwelt ist in mir als Spiegelbild noch einmal wieder­holt; kann er aber diese Wiederholung der Außenwelt zu einer neuen Gestalt aufbauen, dann ist diese Gestalt nicht mehr bloß die Außenwelt: sie ist «Ich».",
      "Ein Wesen mit bloßem sympathischen Nervensystem spiegelt die Außen-welt, es empfindet also diese Außenwelt noch nicht als sich, noch nicht als Innenleben. Ein Wesen mit Rückenmark und Gehirn empfindet die Spiegelung als Innenleben.",
      "Ein Wesen aber mit Blut erlebt als seine eigene Gestalt sein Innenleben. Durch das Blut wird mit Hilfe des Sauerstoffes der Außen­welt nach den Bildern des Innenlebens der eigene Leib gestaltet.",
      "Diese Gestaltung kommt als Ich-Wahrnehmung zum Ausdruck. Nach zwei Seiten weist das Ich, und das Blut ist der äußere Ausdruck dieser Hinweisung. Nach innen ge­richtet ist der Blick des Ich, nach außen gerichtet ist der Wille des Ich.",
      "Nach innen sind die Kräfte des Blutes gerich­tet, sie bauen das Innere auf; nach außen sind sie gerichtet zum Sauerstoff der äußeren Welt hin. Daher geht der Mensch, wenn er in Schlaf fällt, im Unbewußtsein unter, er geht unter in dasjenige, was das Bewußtsein im Blute er­leben kann.",
      "Wenn der Mensch aber sein Auge der Außen­welt öffnet, dann nimmt das Blut die durch Gehirn und Sinne erzeugten Bilder in seine Gestaltungskräfte auf. Das Blut steht so in der Mitte zwischen der inneren Bilderwelt und der lebendigen Gestaltenwelt des Äußeren.",
      "Diese Rolle wird uns klar werden, wenn wir zwei Erscheinungen be­trachten. Die eine Erscheinung ist die Abstammung, die Verwandtschaft der bewußten Wesen, die andere Erschei­nung ist die Erfahrung der Welt der äußeren Erlebnisse.",
      "Die Abstammung stellt uns dahin, wo wir, wie man es gewöhn­lich nennt, durch das Blut stehen. Der Mensch wird heraus-geboren aus einem Zusammenhang, einer Rasse, einem Stamme, aus seiner Vorfahrenreihe, und dasjenige, was aus seinen Vorfahren sich auf ihn vererbt, findet seinen Ausdruck im Blute.",
      "Im Blut wird gleichsam zu­sammengefaßt, was sich aus der materiellen Vergangen­heit des Menschen herausgebildet hat. Es wird aber im Blute auch vorgebildet, was sich für die Zukunft des Menschen vorbereitet.",
      "Wenn der Mensch daher sein höheres Bewußtsein herab-dämpft, wenn er in der Hypnose, im Somnambulismus oder im atavistischen Hellsehen ist, dann taucht er unter in ein viel tieferes Bewußtsein und nimmt die großen Weltgesetze wahr, in einer traumartigen Form, nur viel klarer und heller",
      "als in den hellsten Träumen des gewöhnlichen Schlafes. Der Mensch hat dann die Tätigkeit des Gehirns, und bei tief­stem Somnambulismus auch diejenige des Rückenmarkes unterdrückt; er erlebt die Tätigkeit seines sympathischen Nervensystems, das heißt in einer dumpfen, dämmerhaften Form das Leben im ganzen Kosmos. In einem solchen Falle bringt dann das Blut nicht mehr die Bilder des Innenlebens zum Ausdruck, die durch das Gehirn vermittelt sind, son­dern dasjenige, was die Außenwelt in ihn hineingebaut hat. Nun aber haben an ihm gebaut die Kräfte seiner Vorfahren. Wie er die Form seiner Nase von einem Vorfahren hat, so die Form seines ganzen Leibes. Er empfindet so bei ge­dämpftem Bewußtsein seine Vorfahren in sich, wie er die durch die Sinne erzeugten Bilder der Außenwelt bei wachem Bewußtsein empfindet. Das heißt: seine Vorfahren rumoren in seinem Blute. Er lebt dann noch das Leben seiner Vor­fahren dumpf mit.",
      "Alles in der Welt ist in Entwicklung begriffen, auch das menschliche Bewußtsein. Die Bewußtseinsart, welche der Mensch jetzt hat, war ihm nicht immer eigen. Wenn wir in der Zeit zurückgehen zu unseren fernen Vorfahren, so fin­den wir eine andere Bewußtseinsart. Gegenwärtig nimmt der Mensch in seinem wachen Tagesleben durch seine Sinne die äußeren Dinge wahr und bildet sie zu Vorstellungen um. Diese Vorstellungen der Außenwelt wirken auf sein Blut. Es lebt daher und arbeitet in seinem Blute alles das, was er durch die äußeren Erlebnisse der Sinne empfangen hat. Das Gedächtnis ist nun mit diesen Erlebnissen, mit den Erfahrungen der Sinne erfüllt. Dagegen bleibt diesem heu­tigen Menschen unbewußt, was sich in seinem leiblichen Innenleben durch die Vererbung von seinen Vorfahren her vererbt hat. Er weiß nichts von den Formen seiner inneren Organe. So war es nicht in der Vorzeit. Da lebte im Blute",
      "nicht nur, was die Sinne von außen empfangen hatten, son­dern auch dasjenige, was in der Leibesgestalt vorhanden ist. Und weil diese Leibesgestalt ererbt ist von den Vor­fahren, so empfand der Mensch in sich das Leben der Vor­fahren.",
      "Denkt man sich ein solches Bewußtseinsleben gestei­gert, so erhält man eine Vorstellung davon, wie es sich auch in einem entsprechenden Gedächtnisse zum Ausdruck bringt. Ein Mensch, der nur erlebt, was er durch seine Sinne wahr­nimmt, der erinnert sich auch nur an das, was er durch die äußere Sinneserfahrung erlebt hat.",
      "Er kann nur ein Be­wußtsein von dem haben, was er seit seiner Kindheit auf diese Art erfahren hat. Anders war es beim Menschen der Vorzeit. Der erlebte, was in ihm war, und da dieses «Innere» ein Ergebnis der Vererbung ist, erlebte er in sei­nen Vorstellungen die Erlebnisse seiner Vorfahren mit.",
      "Er erinnerte sich nicht nur an seine Kindheit, sondern auch an die Erlebnisse seiner Vorfahren. Dieses Leben seiner Vor­fahren war in den Bildern, die sein Blut empfing, mit ge­genwärtig. So unglaublich es für die heutige materialistische Vorstellungsart auch ist: es ist doch wahr, daß es einmal ein Bewußtsein gegeben hat, durch das die Menschen nicht nur ihre Sinneswahrnehmungen als ihre eigenen Erlebnisse be­trachteten, sondern auch die Erlebnisse ihrer Vorfahren.",
      "Damals sagten sie: «Ich habe es erlebt» nicht nur zu dem, was ihre eigene Person erlebt hat, sondern auch zu dem, was die Vorfahren erfahren hatten; sie erinnerten sich des­sen. Zwar war diese frühere Bewußtseinsform des Menschen gegenüber dem gegenwärtigen wachen Tagesbewußtsein dämmerhaft, mehr wie ein lebhaft gesteigertes Träumen, aber sie war dafür umfassender.",
      "Sie dehnte sich über die Erfahrung der Vorfahren aus. Der Sohn fühlte sich mit Vater, Großvater in einem Ich verbunden, weil er deren Erlebnisse als seine eigenen miterlebte.",
      "Weil der Mensch dieses Bewußtsein hatte, weil er nicht bloß in seiner persönlichen Welt lebte, sondern weil in sei­nem Innern das Bewußtsein seiner vorhergehenden Gene­ration auflebte, deshalb bezeichnete er auch nicht bloß seine Person mit einem Namen, sondern eine ganze Generatio­nenreihe. Der Sohn, der Enkel und so weiter bezeichneten das Gemeinsame, das durch sie alle hindurchging, mit einem Namen.",
      "Der Mensch empfand sich als ein Glied der ganzen Generationsreihe. Das war eine wirkliche und wahre Emp-findung. Und wodurch wurde diese Bewußtseinsform in eine andere verwandelt? Sie wurde es durch ein Ereignis, das die geheimwissenschaftliche Geschichte gut kennt.",
      "Wenn Sie in der Geschichte zurückgehen, dann tritt für alle Völker des Erdkreises ein Moment auf, der Ihnen ganz genau bei jedem einzelnen Volke bezeichnet werden kann. Das ist der Moment, wo das Volk in einen neuen Kulturzustand ein­tritt, in dem es aufhört, alte Traditionen zu haben, wo es aufhört, Urweisheit zu besitzen, jene Weisheit, die durch das Blut der Generationen hindurchgerollt ist.",
      "Die Völker haben ein Bewußtsein davon, und dieses Bewußtsein finden wir ausgedrückt in den alten Sagen der Völker. Die Stämme blieben nämlich in früherer Zeit in sich abgeschlossen, die einzelnen Mitglieder der Familien heirateten untereinan­der.",
      "Das finden Sie ursprünglich bei allen Rassen und Völ­kern. Und ein wichtiger Moment für die Menschheit ist der, als dieses Prinzip durchbrochen wird, sich fremdes Blut mit fremdem Blute mischt, wo die Nah-Ehe in die Fern-Ehe übergeht.",
      "Die Nah-Ehe bewahrt das Blut der Generationen, sie läßt dasselbe Blut durch die einzelnen Glieder rinnen, das seit Generationen den Stamm, die Nation durchfloß. Die Fern-Ehe gießt neues Blut dem Menschen ein, und diese Durchbrechung des Stammesprinzipes, diese Mischung des Blutes, die bei allen Völkern sich findet und früher oder",
      "später auftritt, bedeutet die Geburt des äußeren Verstandes, die Geburt des Intellektes.",
      "Das ist eben das Wichtige, daß in alten Zeiten eine Art dämmerhaften Hellsehens vorhanden war und daß Mythen und Sagen aus diesem hellseherischen Vermögen heraus ent­standen sind, welches sich in dem verwandtschaftlichen Blute ausleben kann wie in dem vermischten Blute das ge­genwärtige Bewußtsein. Mit dem Eintritt der Fern-Ehe fällt auch die Geburt des logischen Denkens, die Geburt des Intellektes zusammen. So überraschend das ist, so wahr ist es. Es ist eine Erkenntnis, die immer mehr und mehr durch die äußere Forschung bestätigt werden wird. Die Anfänge sind schon gemacht. Die Blutmischung, die mit der Fern-Ehe eintritt, ist zu gleicher Zeit dasjenige, was das Hell-sehen von früher zunächst auslöscht, um die Menschheit zu einer höheren Entwicklungsstufe hinaufzuheben. Wie der, welcher eine okkulte Entwicklung durchmacht, dieses Hell-sehen wieder heraufhebt und es zu einer neuen Form um­wandelt, so hat sich umgekehrt das gegenwärtige wache Tagesbewußtsein aus einem alten dämmerhaften Hellsehen heraus entwickelt.",
      "Gegenwärtig drückt sich die ganze Umwelt, der der Mensch sich hingibt, im Blute aus, und diese Umwelt formt das Innere daher nach dem Äußeren. Beim Urmenschen drückte sich mehr das leibliche Innere im Blute aus. In den Urzeiten vererbten sich mit der Erinnerung an die Erleb­nisse der Vorfahren auch deren Neigungen zu diesem oder jenem Guten und Bösen. In dem Blute des Nachkommen waren die Wirkungen der Neigungen der Vorfahren zu spüren. Als dann das Blut durch die Fern-Ehe gemischt wurde, da wurde auch dieser Zusammenhang mit den Vor­fahren durchschnitten. Der Mensch ging über zum persön­lichen Eigenleben. Er lernte sich in seinen sittlichen Neigungen",
      "nach dem zu richten, was er im persönlichen Leben erfahren hat. So drückt sich in einem ungemischten Blute die Macht des Vorfahrenlebens aus, in dem gemischten die Macht der eigenen Erlebnisse. Davon erzählen die Sagen und Mythen der Völker. Sie sagen uns: Was Macht hat auf dein Blut, das hat Macht über dich. Die Macht der Völker-traditionen hörte auf, als sie nicht mehr wirken konnte auf das Blut, als dessen Aufnahmefähigkeit für solche Vor­fahrenmacht erlischt durch die Beimischung des fremden Blutes. Und dieser Satz gilt im weitesten Umfange. Welche Macht auch immer sich eines Menschen bemächtigen will, sie muß so auf ihn wirken, daß sich diese Wirkung im Blute ausdrückt. Will also eine böse Macht Einfluß gewinnen auf den Menschen, dann muß sie Herrschaft haben über sein Blut. Das ist der tiefe und geistvolle Zug des erwähnten Wortes aus Faust. Daher sagt der Repräsentant des bösen Prinzipes: Schreibe mir deinen Namen mit Blut unter den Pakt. Habe ich deinen Namen mit deinem Blute geschrie­ben, dann habe ich dich bei demjenigen erfaßt, wodurch der Mensch überhaupt erfaßt werden kann, ich habe dich zu mir herübergezogen. Wem das Blut gehört, dem gehört auch der Mensch oder des Menschen Ich.",
      "Wenn zwei Menschengruppen aufeinanderstoßen, wie dies bei der Kolonisation der Fall zu sein pflegt, dann wird derjenige, welcher die Evolution kennt, sagen können, ob eine fremde Kultur aufgenommen werden kann oder nicht. Nehmen Sie ein Volk, das herausgewachsen ist aus seiner Umgebung, in dessen Blut sich seine Umgebung hinein-gebildet hat, und versuchen Sie, ihm eine fremde Kultur aufzupfropfen. Es ist unmöglich. Das ist auch der Grund, warum gewisse Ureinwohner zugrunde gehen mußten, als die Kolonisten in bestimmte Gegenden kamen. Von diesem Gesichtspunkte aus wird man diese Frage beurteilen müssen,",
      "und dann wird man auch nicht mehr glauben, daß man jedes jedem aufpfropfen kann. Dem Blute darf nur das­jenige zugemutet werden, was es noch vertragen kann.",
      "Die Entdeckung der neueren Wissenschaft, daß, wenn man Blut eines Tieres mit dem eines ihm nicht verwandten vermischt, das eine Blut das andere tötet, ist eine alte okkulte Erkenntnis. Mischen Sie Menschenblut mit dem Blut niederer Affen, so tritt Vernichtung ein, weil sie zu weit voneinander abliegen. Mischen Sie Menschenblut und das Blut höherer Affen, so töten sie sich nicht. So wie die Mischung des Blutes von Tiergattungen, wenn sie zu ent­fernt sind, den wirklichen Tod hervorbringt, so tötete es das alte Hellsehen des niederen Menschen, als sein Blut mit dem Blute des nicht stammverwandten vermischt wurde. Das ganze heutige Geistesleben ist nichts anderes als das Er­gebnis der Blutmischung, und man wird in nicht zu ferner Zeit auch den Einfluß der Blutmischung studieren und im Menschenleben zurückverfolgen können, wenn man von diesem Gesichtspunkte aus wieder die Forschung betreibt. Also: Blut zu Blut von in der Entwicklung sich fernstehen-den Tiergattungen tötet; Blut zu Blut von verwandten Tier-gattungen tötet nicht. Der physische Organismus des Men­schen wird erhalten, auch wenn fremdes Blut zu fremdem Blute kommt, aber die hellseherische Kraft stirbt unter dem Einfluß der Blutmischung oder der Fern-Ehe.",
      "Der Mensch ist so gestaltet, daß, wenn sich Blut und Blut mischt und diese Blutmischung nicht von einer Seite her­kommt, die in der Entwicklung zu weit absteht, der In­tellekt geboren wird. Dadurch wird die ursprünglich aus dem Animalischen kommende Hellseherkraft vernichtet und ein neues Bewußtsein in der Entwicklung geboren.",
      "Es ist also bei der menschlichen Entwicklung auf höherer Stufe etwas Ähnliches vorhanden wie auf niederer Stufe in",
      "der Tierwelt. In der Tierwelt tötet fremdes Blut das fremde Blut. In der Menschenwelt tötet das fremde Blut dasjenige, was mit dem Verwandtenblut verbunden ist: das dumpfe, dämmerhafte Hellsehen. Das wache Tagesbewußtsein des Menschen der Gegenwart ist also ein Ergebnis eines Tötungs­prozesses. Es ist im Laufe der Entwicklung das Geistesleben der Nah-Ehe getötet worden, aber es ist auch dafür aus der Fern-Ehe das Neue, der Intellekt, das wache Tagesbewußt­sein geboren worden.",
      "Was also im Blute des Menschen leben kann, das lebt in seinem Ich. Wie der physische Leib der Ausdruck ist für das physische Prinzip, der Ätherleib für die Lebenssäfte und ihre Systeme, der Astralleib für das Nervensystem, so ist das Blut der Ausdruck für das Ich. Physisches Prinzip, Ätherleib, Astralleib sind das Obere, Blutzustand und Ich sind das Mittlere und physischer Leib, Lebenssystem, Ner­vensystem sind das Untere. Was sich deshalb eines Men­schen bemächtigen will, das muß sich seines Blutes be­mächtigen. Das muß berücksichtigt werden, wenn man im praktischen Leben vorwärtskommen will. Man kann zum Beispiel ein fremdes Volk in seiner Eigenart töten, wenn man kolonisierend seinem Blute zumutet, was dieses Blut nicht ertragen kann. Denn im Blute drückt sich das Ich aus. Erst dann haben Schönheit und Wahrheit den Menschen, wenn sie sein Blut haben. Mephistopheles bemächtigt sich des Blutes des Faust, weil er dessen Ich haben will. Der Satz, der das Leitmotiv dieses Vortrags bildet, ist daher aus der Tiefe der Erkenntnis heraus genommen. Ja, Blut ist ein ganz besonderer Saft."
    ],
    "sentences": [
      [
        "Ein jeder von Ihnen hat zweifellos im Gedächtnis, daß der heutige Vortrag, seinem Titel nach, an ein Wort des Goetheschen Faust anknüpft.",
        "Sie wissen alle, daß in diesem Gedichte dargestellt wird, wie Faust, der Repräsentant des höchsten menschlichen Strebens, einen Bund eingeht mit den bösen Mächten, die ihrerseits wieder in dem Gedichte durch Mephistopheles, den Sendling der Hölle, repräsen­tiert werden.",
        "Sie wissen alle, daß Faust einen Vertrag schlie­ßen soll mit Mephistopheles, und daß das Schriftstück dann von Faust mit Blut unterschrieben werden soll.",
        "Faust hält das zunächst für eine Posse; Mephistopheles aber spricht den an dieser Stelle von Goethe zweifellos ernst gemeinten Satz: «Blut ist ein ganz besonderer Saft»."
      ],
      [
        "Etwas Merkwürdiges ist bei dieser Stelle des Goetheschen Faust den sogenannten Goethe-Kommentatoren passiert.",
        "Sie wissen ja, daß über Goethes Faust eine so umfangreiche Literatur existiert, daß man ganze Bibliotheken damit fül­len könnte.",
        "Natürlich kann es nicht meine Aufgabe sein, mich weiter auszulassen über dasjenige, was diese verschie­denen Goethe-Erklärer gerade über diese Fauststelle sagen; aber sie bringen nicht viel anderes zutage als das, wovon der Faustkommentar, der einer der letzten ist, von dem Universitätsprofessor Minor, ein Beispiel gibt.",
        "Er sowie andere Kommentatoren behandeln diesen Satz als etwas, das von Mephistopheles wie eine Art ironischer Bemerkung hingesprochen sein soll, und Minor macht die merkwürdige,"
      ],
      [
        "in der Tat höchst merkwürdige Bemerkung hören Sie genau, was er sagt, um vielleicht auch staunen zu können, auf was alles ein Goethe-Erklärer kommen kann -, die Bemerkung: «Der Teufel ist der Feind des Blutes», und er verweist dabei darauf, daß das Blut dasjenige sei, was dem Menschen eigentlich das Leben erhöht und erhält, und daß daher der Teufel, der Feind des menschlichen Geschlechtes, auch nur der Feind des Blutes sein könne.",
        "Er macht nun mit Recht darauf aufmerksam, daß schon in der ältesten Be­arbeitung der Faustsage, wie auch in der Sage überhaupt, dieses Blut dieselbe Rolle spielt."
      ],
      [
        "In einem alten Faustbuche wird uns klar beschrieben, wie Faust sich mit einem kleinen Federmesser die linke Hand etwas aufzuritzen hat, wie er dann das herausflie­ßende Blut in die Feder nimmt und seinen Namen unter den Pakt schreibt, wie dann auf der linken Hand das Blut gerinnt und die Worte bildet: «0 Mensch entfliehe.» Dies alles ist richtig.",
        "Aber nun die Bemerkung, daß der Teufel ein Feind des Blutes sei und die Unterschrift deshalb mit Blut fordere, eben weil er ein Feind des Blutes sei.",
        "Ich möchte Sie fragen, ob jemand sich vorstellen kann, daß er just dasjenige begehre, was ihm unsympathisch ist.",
        "Ver­nünftigerweise kann man nur voraussetzen, daß an dieser Stelle Goethe gemeint hat - daß nicht nur Goethe, sondern auch die Hauptsage und die ältere Faustdichtung einzig und allein das gemeint haben können -, daß dem Teufel an dem Blute etwas Besonderes liegt und daß es ihm nicht einerlei ist, ob er mit gewöhnlicher, neutraler Tinte den Pakt unterschrieben erhält oder mit Blut.",
        "Man kann hier nichts anderes voraussetzen, als daß der Repräsentant der bösen Mächte glaubt, ja überzeugt ist, daß er den Faust ganz besonders dadurch in der Hand haben werde, daß er sich wenigstens eines Tropfens seines Blutes bemächtigt"
      ],
      [
        "haben wird.",
        "Das ist ganz selbstverständlich und niemand kann diese Stelle anders verstehen, als daß Faust nicht des­halb mit Blut unterschreiben soll, weil der Teufel ein Feind des Blutes ist, sondern weil er sich des Blutes bemächtigen möchte."
      ],
      [
        "Dem liegt eine merkwürdige Empfindung zugrunde, die Empfindung, daß derjenige, der sich des Menschen Blutes bemächtigt, die Herrschaft über den Menschen habe, und daß das Blut deshalb ein ganz besonderer Saft ist, weil es sozusagen dasjenige ist, um das eigentlich gekämpft werden muß, wenn um den Menschen in bezug auf das Gute und auf das Böse gekämpft wird."
      ],
      [
        "Alle diejenigen Dinge, welche aus den Sagen und Mythen des Volkes uns überkommen sind und sich auf das Men­schenleben beziehen, werden in unserer Zeit in bezug auf die ganze Anschauung und Auffassung des Menschen einer besonderen Umwandlung unterliegen.",
        "Dasjenige Zeitalter liegt hinter uns, in dem man auf Sagen, Märchen und Mythen so geblickt hat, als ob in ihnen nur kindliche Volks­phantasie sich ausspräche.",
        "Ja, selbst die Zeit liegt hinter uns, in der man in einer kindlich gelehrtenhaften Weise davon gesprochen hat, daß in der Sage die dichtende Volksseele zum Ausdruck komme.",
        "Die dichtende Volksseele ist nichts an­deres als ein Erzeugnis des grünen Gelehrtentisches, denn es gibt ebenso einen grünen Gelehrtentisch, wie es einen grünen Bürokratentisch gibt.",
        "Wer einen Blick hineingetan hat in die Volksseele, der weiß sehr gut, daß es sich im Volke nicht um Erdichtungen und dergleichen Dinge han­delt, sondern um etwas viel Tieferes, das in seinen Sagen und Märchen von wunderbaren Mächten und wunderbaren Ereignissen zum Ausdruck kommt."
      ],
      [
        "Wenn wir uns von dem neuen Standpunkte der Geistes­forschung aus wieder in die Sagen und Mythen vertiefen,"
      ],
      [
        "wenn wir jene großartigen und gewaltigen Bilder, die uns aus der Urzeit überkommen sind, auf uns wirken lassen, nachdem wir mit geisteswissenschaftlichen Forschungs­methoden ausgerüstet sind, so erscheinen uns diese Mythen und Sagen so, daß sie uns zum Ausdruck einer tiefsinnigen Urweisheit werden."
      ],
      [
        "Wahr ist es, daß der Mensch sich zunächst frägt, wie es komme, da wir es doch ursprünglich mit primitiven Volks-stufen, primitiven Volksanschauungen zu tun haben, daß der naive Mensch sich die Welträtsel bildlich veranschau­lichen konnte in diesen Sagen und Märchen und daß, wenn wir uns heute in diese Sagen und Märchen vertiefen, wir im Bilde dasjenige erblicken, was uns die Geistesforschung heute klar enthüllt.",
        "Zunächst muß das unsere Verwunderung er­regen.",
        "Wer sich aber tiefer und tiefer einläßt in die Art und Weise, wie diese Märchen und Mythen zustande gekommen sind, dem schwindet jedes Erstaunen, jeder Zweifel und er wird nicht nur das, was man naive Anschauung nennt, in diesen Sagen und Märchen finden, sondern den weisheits­vollen Ausdruck einer uralten, wahren Weisheits-Anschau­ung der Welt erkennen.",
        "Mehr, viel mehr noch kann man lernen, wenn man die Grundlage dieser Mythen und Sagen positiv durchforscht, als wenn man die heutige verstandes-und erfahrungsmäßige Wissenschaft in sich aufnimmt.",
        "Frei­lich muß man mit den Erforschungsmethoden der Geistes­wissenschaft ausgerüstet an diese Dinge herangehen.",
        "Alles, was man in den Sagen und alten Weltanschauungen über das Blut findet, pflegt von Bedeutung zu sein, weil man in diesen uralten Zeiten eine Weisheit hatte, die über das Blut, über jenen besonderen Saft, der das fließende Menschen-leben selbst ist, und über seine Bedeutung für die Welt Bescheid wußte."
      ],
      [
        "Es soll uns heute nicht beschäftigen, woher in Urzeiten"
      ],
      [
        "jene Weisheit gekommen ist, obwohl der Schluß des Vor­trages auch darauf wird hindeuten müssen.",
        "Die eigentliche Betrachtung dieses Gegenstandes soll späteren Vorträgen vorbehalten bleiben.",
        "Aber das Blut selbst, in seiner Bedeu­tung für die Menschheit und den menschlichen Kultur­prozeß, wollen wir uns heute einmal anschauen.",
        "Nicht etwa eine physiologische oder rein naturwissenschaftliche Be­trachtung soll hier geboten werden, sondern eine Betrach­tung aus der geistigen Weltanschauung heraus.",
        "Und da dringen wir am besten in jedes Ding ein, wenn wir uns zu­nächst bewußt werden, welches die Bedeutung eines uralten Satzes ist, eines Satzes, der mit der Urkultur des alten Agyptens zusammenhängt, wo die Priesterweisheit des Her­mes gewaltet hat, eines Satzes, der als Grundsatz aller Gei­steswissenschaft gilt, der der hermetische Grundsatz genannt worden ist und der heißt: «Es ist oben alles wie unten.»"
      ],
      [
        "Sie können manche dilettantische Erklärung dieses Satzes finden.",
        "Diejenige Erklärung aber, die uns zunächst heute hier beschäftigen soll, ist die folgende.",
        "Alle Geisteswissen­schaft ist sich darüber klar, daß die Welt, die dem Menschen zunächst durch seine fünf Sinne zugänglich ist, nicht die ganze Welt darstellt, sondern daß sie nur der Ausdruck ist für eine tiefere, hinter ihr verborgene Welt, die geistige Welt.",
        "Diese geistige Welt wird im Sinne dieses hermetischen Grundsatzes die obere Welt genannt, und die sinnliche Welt, die sich um uns herum ausbreitet, die wir mit unseren Sinnen wahrnehmen und mit unserem Verstande erforschen können, gilt als untere, als der Ausdruck der geistigen Welt.",
        "So daß der Geistesforscher in dieser sinnlichen Welt kein Letztes sieht, sondern eine Art Physiognomie, die ihm eine dahinterliegende seelische und geistige Welt ausdrückt, ge­nau so wie man, wenn man das menschliche Antlitz betrach­tet, nicht bei den Formen des Gesichtes und der Gesten"
      ],
      [
        "stehenbleiben darf, sondern selbstverständlich von den Gesten und der Physiognomie auf dasjenige hingeführt wird, was sich seelisch und geistig in ihnen ausdrückt."
      ],
      [
        "Dasjenige, was jeder Mensch naiv tut, wenn er einem beseelten Wesen gegenübertritt, das macht der Okkultist oder der Geistesforscher der ganzen Welt gegenüber.",
        "«Es ist oben alles wie unten» würde, auf den Menschen angewandt, heißen: Es drücken sich diejenigen Impulse in seinem Ge­sichte aus, die in seiner Seele liegen: in einem harten, rohen Antlitz die Roheit der Seele, in einem Lächeln innerlicher Frohsinn, in den Tränenperlen die Leiden der Seele."
      ],
      [
        "Lassen Sie mich an der Frage, was eigentlich Weisheit ist, den hermetischen Grundsatz einmal darlegen.",
        "Es wurde in der Geisteswissenschaft immer davon gesprochen, daß die Weisheit des Menschen etwas zu tun habe mit der Erfah­rung, und zwar mit schmerzlicher Erfahrung.",
        "Derjenige, der unmittelbar in Schmerz und Leiden darinnensteckt, wird innerhalb dieses Schmerzes und Leidens vielleicht etwas zeigen, was innerliche Disharmonie ist.",
        "Derjenige aber, der die Schmerzen und Leiden überwunden hat und ihre Frucht in sich trägt, wird Ihnen immer wieder nur das sagen, daß er damit etwas von Weisheit aufgenommen hat.",
        "Die Freu­den und Lüste des Lebens, das, was mir das Leben geboten hat an Befriedigungen, das nehme ich dankbar hin; aber weniger als das alles möchte ich hingeben meine Schmerzen und Leiden, die hinter mir liegen: Meinen Schmerzen und Leiden verdanke ich die Weisheit.",
        "So hat von jeher die Geistesforschung in der Weisheit etwas gesehen wie kristal­lisierten Schmerz, der überwunden ist und sich in sein Ge­genteil verwandelt hat."
      ],
      [
        "Interessant ist es nun, daß die gegenwärtige mehr mate­rialistische Forschung in einer eigenartigen Weise gerade darauf zurückgekommen ist.",
        "In jüngster Zeit ist ein schönes"
      ],
      [
        "Buch erschienen über die Mimik des Denkers, ein Buch, das lesenswert ist.",
        "Das Buch ist von keinem Theosophen, son­dern von einem Natur- und Seelenforscher.",
        "Er versucht zu zeigen, wie sich das innere Leben des Menschen, seine Art und Weise des Vorstellens, zum Ausdrucke bringt in der Physiognomie, und auch dieser Forscher macht darauf auf­merksam, daß der Denker immer etwas in seinem Gesichts­ausdruck hat, das an absorbierten Schmerz erinnert."
      ],
      [
        "So sehen Sie, als eine schöne Bestätigung eines uralten Grundsatzes der Geisteswissenschaft, diesen Grundsatz wie­der in der mehr materialistischen Anschauung unserer Zeit auftauchen.",
        "Das werden Sie noch tiefer und tiefer einsehen, und Sie werden finden, wie Zug um Zug dasjenige, was uralte Weisheit ist, der heutigen Wissenschaft wiederum zugänglich wird."
      ],
      [
        "Es macht das Wesen der Geistesforschung aus, daß alles, was uns in der Welt umgibt - das mineralische Gerüst, die Pflanzendecke, die Tierwelt unserer Erde -, als der physio­gnomische Ausdruck oder das Untere eines Oberen, eines dahinterliegenden geistigen Lebens angesehen wird.",
        "Vom okkulten oder geisteswissenschaftlichen Standpunkt aus wird dasjenige, was uns in der sinnlichen Welt gegeben wird, erst richtig verstanden, wenn man dazu das Obere, das geistige Vorbild, die geistigen Urwesen, aus denen das alles hervorgegangen ist, kennt.",
        "So soll uns heute beschäftigen, was hinter der Erscheinung des Blutes verborgen liegt, das­jenige, was sich in dem Blute einen physiognomischen Aus­druck hier in der Sinnenwelt schuf.",
        "Hat man dann diesen geistigen Hintergrund des Blutes, dann wird man auch ein­sehen, wie eine solche Erkenntnis zurückwirken muß auf unser ganzes geistiges Kulturleben."
      ],
      [
        "Große Fragen drängen sich in unserer Zeit an den Men­schen heran: Fragen der Erziehung nicht nur des jungen"
      ],
      [
        "Menschen, sondern Fragen der Erziehung ganzer Völker, und auch die große Erziehungsfrage, die die Zukunft an die Menschheit stellen wird.",
        "Sie muß jeder erblicken, wenn er sein Auge auf die großen sozialen Umwälzungen unserer Zeit richtet, auf die sozialen Forderungen, die überall auf­treten, seien sie verkörpert in der Frauenfrage, in der sozialen Frage, in der Friedensfrage und so weiter.",
        "Alles das tritt vor unsere sorgende Seele.",
        "Alle diese Fragen wer­den hell und klar, wenn wir das, was als geistige Wesenheit hinter dem Blute liegt, kennen."
      ],
      [
        "Wer wollte leugnen, daß mit dieser Frage auch die Ras­senfrage zusammenhängt, die bezeichnenderweise auch in unserer Gegenwart wieder auftritt?",
        "Wir verstehen die Rassenfrage aber nur, wenn wir das geheimnisvolle Wirken des Blutes und der Blutmischung unter den Völkern ver­stehen.",
        "Endlich hängt auch noch eine Frage damit zusam­men, die immer aktueller und aktueller werden wird, je mehr man sich aus einem bloß ziellosen Vorgehen in dieser Sache herauswindet und durchringen wird zu einem ein­heitsvollen Vorgehen auf diesem Gebiete.",
        "Die Frage, auf die hier hingedeutet wird, ist die Kolonisationsfrage, jene Frage, die auftaucht, wenn Menschen kultivierter Völker mit unkultivierten Völkern zusammenkommen: Inwiefern können unkultivierteVölker neue Kulturen in sich aufneh­men?",
        "Wie kann ein Schwarzer, wie kann ein barbarischer Wilder kultiviert werden, wie hat man sich ihnen gegen­über zu benehmen?",
        "Da kommen nicht bloß die Gefühle einer schattenhaften Moral in Betracht, sondern große, ernste und bedeutsame Lebensfragen des Daseins.",
        "Derjenige, der nicht weiß, unter welchen Bedingungen ein Volk steht, ob in auf­oder absteigender Linie der Entwicklung, ob dies oder jenes durch sein Blut bedingt ist, der vermag nicht den richtigen Weg zu finden, um irgendeine Kultur bei einem anderen"
      ],
      [
        "Volke einzuführen.",
        "Alles das taucht auf, wenn diese bedeu­tungsvolle Frage nach dem Blute aufgeworfen wird."
      ],
      [
        "Was das Blut als solches ist, das kennen Sie ja wohl alle aus der landläufigen Naturwissenschaft.",
        "Sie wissen, wenn Sie den Menschen und die höheren Tiere betrachten, daß dieses Blut wirklich das fließende Leben ist.",
        "Sie wissen, daß durch das Blut des Menschen Inneres nach außen geöffnet wird, und indem dies geschieht, nimmt der Mensch durch das Blut die Lebensluft, den Sauerstoff auf.",
        "Das Blut erfährt durch diese Sauerstoffaufnahme eine Erneuerung.",
        "Das­jenige Blut, welches das menschliche Innere gleichsam dem hereinströmenden Sauerstoff anbietet, ist eine Art von Gift-stoff für den Organismus, eine Art Vernichter und Zer­störer.",
        "Dieses blaurote Blut wird umgewandelt durch Auf­nahme von Sauerstoff, durch eine Art Verbrennungsprozeß, in rotes, lebenschaffendes Blut.",
        "Dieses Blut, das in alle Teile des Körpers dringt, in allen Teilen des Körpers die Ernäh­rungsstoffe ablagert, hat die Aufgabe, die Stoffe der Außen­welt unmittelbar in sich aufzunehmen und auf dem kür­zesten Wege zur Ernährung des Wesens zu verwenden.",
        "Der Mensch und die höheren Tiere haben nötig, erst diese Er­nährungsstoffe in das Blut überzuführen, das Blut zu bilden, den Sauerstoff der Luft in das Blut aufzunehmen und den Körper durch das Blut aufzubauen und zu erhalten."
      ],
      [
        "Nicht mit Unrecht hat ein geistvoller Seelenkenner ge­sagt: Das Blut mit seiner Bewegung ist wie ein zweiter Mensch, der sich zu dem anderen aus Knochen, Muskeln und Nervenmasse bestehenden Menschen wie eine Art von Außenwelt verhält.",
        "Und in der Tat nimmt der ganze Mensch fortwährend aus dem Blute seine Erhaltungskräfte auf und gibt andererseits dasjenige, was er nicht gebraucht hat, an das Blut ab.",
        "Im Blute ist also ein wirklicher Doppelgänger des Menschen vorhanden, der ihn fortwährend begleitet,"
      ],
      [
        "aus dem er fortwährend seine neuen Kräfte schöpft und an den er dasjenige, was er nicht mehr braucht, abgibt.",
        "Mit vol­lem Recht hat man daher das Blut das fließende Menschen­leben genannt und ihm ähnliche Bedeutung beigemessen wie dem Zellstoff für die niederen Organismen.",
        "Was der Zellstoff für den niederen Orgnismus ist, das ist der so vielfach um-gewandelte «besondere Saft», das Blut, für den Menschen."
      ],
      [
        "Ein bedeutender Forscher, Ernst Haeckel, hat tief in die Werkstatt der Natur hineingeschaut und mit Recht in popu­lären Werken darauf aufmerksam gemacht, daß das Blut eigentlich am spätesten im Organismus entsteht.",
        "Wenn man die Entwicklung des Menschenkeims im Mutterleibe ver­folgt, so findet man, daß die Anlagen zum Knochen- und Muskelbau längst ausgebildet sind, bevor die Anlage zur Blutbildung entsteht.",
        "Erst sehr spät werden die Anlagen zur Blutbildung - mit ihr das Blutgefäß-System - im Men­schen sichtbar; erst sehr spät kommen sie heraus.",
        "Daraus schließt die Naturwissenschaft mit Recht, daß die Blut-bildung überhaupt erst spät in der Weltentwicklung auf­getreten ist, daß sozusagen andere Kräfte, die da waren, erst bis zur Höhe des Blutes heraufgehoben worden sind, um auf dieser Höhe dasjenige zu bewirken, was innerhalb des Menschen bewirkt werden soll.",
        "Wenn der Mensch als Men­schenkeim die früheren Stadien der Menschheits entwicklung durchmacht, sie noch einmal wiederholt, dann eignet er sich erst dasjenige an, was vor der Blutbildung in der Welt vor­handen war, um dann der Evolution in der Umwandlung, in der Heraufhebung alles Früheren zu diesem besonderen Saft, dem Blute, die Krone aufzusetzen."
      ],
      [
        "Wollen wir nun die hinter dem Blute waltenden geheim­nisvollen Gesetze des geistigen Universums studieren, dann müssen wir uns mit den elementarsten Begriffen der Gei­steswissenschaft ein wenig befassen.",
        "Schon oft sind diese"
      ],
      [
        "elementaren Begriffe der Geisteswissenschaft hier ausein­andergesetzt worden.",
        "Sie werden sehen, daß diese elemen­taren Begriffe der Geisteswissenschaft das Obere sind, und daß sich uns dieses Obere, wenn wir es kennengelernt haben, in den bedeutungsvollen Gesetzen des Blutes, wie in denen des übrigen Lebens, zum Ausdruck bringt wie in einer Physiognomie."
      ],
      [
        "Diejenigen, welche diese elementaren Ge­setze der Geisteswissenschaft längst kennen, gestatten mir wohl, daß ich für die, welche zum ersten Male hier sind, kurz wiederhole.",
        "Dabei werden auch Ihnen solche Gesetze immer klarer und klarer werden, wenn Sie sie immer wie­der in besonderen neuen Fällen anwenden lernen."
      ],
      [
        "Freilich für diejenigen, die noch nichts wissen von Geisteswissen­schaft, die sich noch nicht eingelebt haben in die Lebens- und Weltanschauung, um die es sich hier handelt, ist, was ich jetzt sagen werde, mehr oder weniger nur eine Zusammen­stellung von Worten, unter denen sie sich nichts denken können.",
        "Aber es ist ja nicht immer der Mangel eines hinter dem Worte steckenden Begriffes daran schuld, wenn sich jemand bei einem Worte nichts denken kann."
      ],
      [
        "Es kann hier eine Bemerkung, die der geistvolle Licktenberg gemacht hat, etwas verändert angenommen werden: Wenn ein Kopf und ein Buch zusammenstoßen und es hohl klingt, so muß nicht immer das Buch daran schuld sein.",
        "So ist es auch bei der Beurteilung der geisteswissenschaftlichen Wahrheiten von seiten unserer Zeitgenossen."
      ],
      [
        "Wenn diese Wahrheiten den Menschen oftmals als bloße Worte an die Ohren klingen und sie sich nichts dabei denken können, so muß nicht im­mer die Geisteswissenschaft daran schuld sein.",
        "Derjenige aber, der sich einlebt in diese Dinge, der wird sehen, daß hinter den Bezeichnungen und Hinweisen auf höhere We­senheiten auch wirklich solche Wesenheiten stecken, die nicht in unserer sinnlichen Welt zu finden sind."
      ],
      [
        "In der geisteswissenschaftlichen Weltanschauung sehen wir, daß der Mensch, insofern er uns in der Außenwelt für unsere Sinne entgegentritt, insofern er Form und Gestalt ist, nur einen Teil der menschlichen Wesenheit ausmacht, und daß sogar hinter dem physischen Leibe viele andere Wesenheiten sind.",
        "Diesen physischen Leib hat der Mensch mit allen um ihn herumliegenden mineralischen, sogenann­ten leblosen Dingen gemeinschaftlich."
      ],
      [
        "Darüber hinaus hat aber der Mensch den sogenannten Ather- oder Lebensleib.",
        "Ather wird hier nicht in dem Sinne verstanden, wie die physische Wissenschaft es tut.",
        "Dieser Ather- oder Lebensleib ist ein Prinzip, das für den geisteswissenschaftlichen For­scher nicht bloß etwas Erdachtes, nicht bloß etwas Aus­spekuliertes ist, sondern etwas, das für seine geöffneten geistigen Sinne ebenso wirklich vorhanden ist wie die äuße­ren sinnlichen Farben für das sinnliche Auge."
      ],
      [
        "Zu sehen, wirklich zu sehen ist für den hellsehenden Menschen dieser Ather- oder Lebensleib.",
        "Er ist dasjenige, was die unorgani­schen Stoffe zu lebendigem Dasein aufruft, sie heraufholt aus der Leblosigkeit, um sie aufzufädeln an dem Faden des Lebens."
      ],
      [
        "Glauben Sie nicht, daß dieser Lebensleib für den okkulten Forscher nur etwas ist, was er zum Leblosen hin­zudenkt.",
        "Das versuchen die Naturforscher.",
        "Sie versuchen das, was sie mit dem Mikroskop und so weiter an den Dingen sehen können, zu vervollständigen, sich etwas zu erdenken, was sie dann das Lebensprinzip nennen."
      ],
      [
        "Auf diesem Standpunkt steht die geisteswissenschaftliche For­schung nicht, sie hat ein bestimmtes Prinzip.",
        "Sie sagt sich nicht: Hier stehe ich als Forscher so, wie ich nun einmal bin.",
        "Was es in der Welt gibt, muß sich meinem gegenwär­tigen Standpunkt fügen."
      ],
      [
        "Was ich nicht erkennen kann, das gibt es nicht. - Das ist ungefähr ebenso gescheit, wie wenn ein Blinder sagt, die Farben seien eine phantastische Sache."
      ],
      [
        "Es hat nicht derjenige über eine Sache zu entscheiden, der nichts darüber weiß, sondern derjenige, welcher etwas dar­über erlebt hat.",
        "Der Mensch ist in Entwicklung begriffen.",
        "Daher sagt die Geisteswissenschaft: Wenn du so bleibst, wie du bist, so kannst du nichts vom Atherleibe sehen, und kannst in der Tat von «Grenzen des Erkennens» und von «Ignorabismus» sprechen; wirst du aber ein anderer, eignest du dir die nötigen Fähigkeiten an, um die geistigen Dinge wahrzunehmen, so kann nicht von Grenzen der Erkenntnis gesprochen werden.",
        "Nur so lange gibt es diese, als der Mensch seine inneren Sinne nicht geöffnet hat.",
        "Daher ist auch der Agnostizismus nichts als eine drückende Last für unsere Kultur.",
        "Er sagt: Der Mensch ist so und so, und wenn er so und so ist, so kann er auch nur dies und das erkennen.",
        "Darauf ist zu antworten: Wenn er heute so und so ist, so muß er eben anders werden, und dann wird er auch anderes erkennen."
      ],
      [
        "Das zweite Glied des Menschen ist also der Atherleib, den der Mensch gemeinschaftlich mit der Pflanzenwelt hat."
      ],
      [
        "Das dritte Glied ist der sogenannte Astralleib, sehr schön und bedeutungsvoll so genannt, und es soll hier auch später noch einmal gezeigt werden, daß dieser Astralleib mit Recht so genannt wird.",
        "Theosophen, die für diesen Namen einen anderen wählen wollten, haben keine Ahnung davon, um was es sich hier handelt.",
        "Dem Astralleib obliegt es, im Men­schen und im Tiere, das Lebendige zur Empfindungssub­stanz aufzurufen, so daß sich innerhalb des Lebendigen nicht bloß Säfte bewegen, sondern daß sich darin dasjenige ausdrückt, was man Lust und Leid, Freude und Schmerz nennt.",
        "Damit haben Sie im wesentlichen auch den Unter­schied zwischen Pflanze und Tier angedeutet, obwohl es Übergänge gibt."
      ],
      [
        "Eine neue naturwissenschaftliche Forschergruppe hat geglaubt,"
      ],
      [
        "auch den Pflanzen im direkten Sinne Empfindung zuschreiben zu sollen.",
        "Das ist aber nur ein Spiel mit Wor­ten.",
        "Es ist für gewisse Pflanzen selbstverständlich, daß sie Erregungszustände haben, wenn etwas in ihre Nähe kommt, wenn etwas auf sie einwirkt.",
        "Das ist aber keine Empfin­dung.",
        "Es muß im Innern des Geschöpfes ein Bild auftauchen als Reflex der Erregung.",
        "Wenn auch bei gewissen Pflanzen eine Gegenwirkung auf einen äußeren Eindruck geschieht, so ist das doch noch kein Beweis dafür, daß die Pflanze auch innerlich einen solchen Reiz zu einer Empfindung erhebt, daß sie ihn innerlich erlebt.",
        "Dasjenige, was man innerlich erlebt, hat seinen Sitz im Astralleibe.",
        "So sehen wir also, daß das, was bis zum Tier heraufkam, aus dem physischen Leib, dem Ather- oder Lebensleib und dem Astralleib besteht."
      ],
      [
        "Der Mensch ragt nun über das Tier durch etwas ganz Besonderes hinaus, und das, wodurch er über das Tier hin­ausragt, haben sinnige Menschen immer gefühlt.",
        "Es wird darauf hingewiesen durch das, was Jean Paul in seiner Lebensbeschreibung selbst von sich sagt: er erinnere sich ganz genau, wie ihm als kleines Kind im Hofe seines Eltern-hauses der Gedanke durch die Seele schoß: du bist ja ein «Ich», du bist ja eine Wesenheit, die innerlich zu sich Ich sagen kann.",
        "Das machte auf ihn einen bedeutenden Ein­druck."
      ],
      [
        "Alle sogenannte äußerliche Seelenkunde übersieht das Wichtigste, worauf es in diesem Punkte ankommt.",
        "Folgen Sie mir für einige Minuten in eine subtile Betrachtung hin­ein, die Ihnen aber zeigen wird, um was es sich handelt.",
        "Im ganzen Umkreis der deutschen Sprache gibt es ein einziges Wörtchen, das sich von allen anderen Wörtern prinzipiell unterscheidet.",
        "Von jedem Dinge, das hier in diesem Saale ist, kann jeder von Ihnen den Namen dieses Dinges nennen.",
        "Den Tisch kann jeder Tisch, den Stuhl kann jeder Stuhl"
      ],
      [
        "nennen.",
        "Aber ein Wort, einen Namen gibt es, den Sie nicht aussprechen können außer für das, dem dieser Name zu­kommt: das ist das Wörtchen «Ich».",
        "Niemand kann zu einem anderen «Ich» sagen.",
        "Das «Ich» muß heraustönen aus der innersten Seele selbst, es ist der Name, den sich nur die Seele selbst beilegen kann.",
        "Jeder andere ist für mich ein «Du», und ich selbst bin für jeden anderen ein «Du»."
      ],
      [
        "Alle Religionen empfanden dieses Ich als den Ausdruck für jenes Wesen in der Seele, durch das die Seele in sich selbst ihre Grundwesenheit, ihr Göttliches, sprechen zu las­sen vermag.",
        "Da beginnt dann dasjenige, was niemals durch die äußeren Sinne eindringen kann, was niemals in seiner Bedeutung von außen benannt werden kann, sondern aus dem Innersten heraus ertönen muß.",
        "Da beginnt jener Mono­log, jenes Selbstgespräch der Seele, wodurch das göttliche Selbst in der Seele sich ankündigt, wenn die Bahn frei wird für das Einziehen des Geistes in die Seele."
      ],
      [
        "In den älteren Kulturreligionen, noch im alten Hebrä­ischen, hat man diesen Namen «den unaussprechlichen Na­men Gottes» genannt, und was auch die heutige Philologie übersetzen mag, der alte jüdische Gottesname bedeutet nichts anderes als das, was heute durch das deutsche Wort «Ich» ausgedrückt wird.",
        "Bewegung ging durch die Reihen der Zuhörer, wenn der Name des «unbekannten Gottes» durch den Eingeweihten gesprochen wurde, wenn geahnt wurde, was durch dieses Wort ausgedrückt war, wenn das «Ich bin der Ich-Bin» im Tempel ertönte.",
        "In diesem Wort drückt sich das vierte Glied der menschlichen Wesenheit aus, das der Mensch im Umkreis seines irdischen Daseins für sich allein hat.",
        "Dieses Ich umschließt wiederum und bildet in sich aus die Keime zu höheren Stufen des Menschentums.",
        "Nur hingewiesen soll darauf werden, was in der mensch­lichen Entwicklung durch dieses vierte Glied in Zukunft"
      ],
      [
        "zum Dasein gebracht werden wird, hingewiesen soll werden darauf, daß der Mensch aus dem physischen Leib, dem Atherleib, dem Astralleib und dem Ich oder dem eigent­lichen inneren Leben besteht, und daß in diesem inneren Leben die Keime zu drei weiteren Stufen der Entwicklung vorhanden sind, die aus dem Blute erstehen werden, näm­lich Manas, Buddhi und Atma, oder mit deutschen Worten:"
      ],
      [
        "Manas = Geistselbst im Gegensatz zum Körperselbst, Buddhi = Lebensgeist, Atma = Geistmensch, der eigent­liche, wahre Geistmensch, der heute dem Menschen nur als Ideal vorschwebt, der als kleiner Keim im Innern veran­lagt ist und in ferner Zukunft seine Vollendung erreichen wird."
      ],
      [
        "So haben wir, wie im Regenbogen sieben Farben, wie in der Tonskala sieben Töne, im Reich der Atome sieben Stu­fen der Atomgewichte, die siebenstufige Skala des Men­schenwesens, die wieder in vier untere und in drei obere Stufen zerfällt."
      ],
      [
        "Nun versuchen wir, uns einmal klar zu werden darüber, wie sich dieses Obere, Geistige, einen physiognomischen Ausdruck verschafft in dem Unteren, wie es uns vor Augen tritt in der Sinneswelt.",
        "Nehmen Sie zunächst dasjenige, was sich im Menschen zu seinem physischen Leib kristalli­siert.",
        "Er hat es gemeinschaftlich mit der sogenannten leb­losen Natur.",
        "Wenn wir geisteswissenschaftlich sprechen von diesem physischen Leib, dann sprechen wir gar nicht ein­mal von dem, was das Auge sieht, sondern von dem Zu­sammenhang von Kräften, die den physischen Leib kon­struiert haben, von dem, was als Kraftnatur hinter dem physischen Leibe steht."
      ],
      [
        "Sehen wir uns die Pflanze an als das Wesen, das schon den Atherleib hat, welcher die physischen Stoffe heraufholt zum Leben, das heißt dasjenige, was sinnliche Materie ist,"
      ],
      [
        "in Lebenssäfte verwandelt.",
        "Was ist es, das so die sogenann­ten leblosen Kräfte in die Lebenssäfte umgestaltet?",
        "Wir nennen es den Atherleib, und dieser Atherleib tut dasselbe im Tier und dasselbe auch im Menschen; er ruft dasjenige, was bloß sinnlich ist, zu lebendiger Konfiguration, zu leben­diger Gestaltung auf.",
        "Dieser Atherleib wird wieder durch­setzt von dem Astralleib.",
        "Und was macht dieser Astralleib?",
        "Er ruft die bewegte Substanz zum innerlichen Miterleben des Kreislaufs der stofflichen Säftebewegung auf, sodaß sich die äußere Bewegung in innerlichen Erlebnissen spiegelt."
      ],
      [
        "Wir sind damit so weit gekommen, daß wir den Men­schen begreifen, insofern er in das Tierreich hineingestellt ist.",
        "Alle Substanzen, aus denen der Mensch zusammen­gesetzt ist, finden Sie auch draußen in der leblosen Natur:"
      ],
      [
        "Sauerstoff, Stickstoff, Wasserstoff, Schwefel, Phosphor und so weiter.",
        "Soll das, was umgewandelt ist durch den Ather­leib in lebendige Substanz, zu innerlichem Erfassen, zur Schaffung innerer Spiegelbilder von dem, was außen vor­geht, aufgerufen werden, so muß der Atherleib von dem, was wir Astralleib nennen, durchdrungen werden.",
        "Der Astralleib ruft die Empfindung hervor.",
        "Aber jetzt, auf dieser Stufe ruft der Astralkörper die Empfindung in ganz besonderer Weise hervor.",
        "Der Atherleib wandelt unorga­nische Substanz in Lebenssäfte um, der Astralleib wandelt diese lebendige Substanz in empfindende Substanz um.",
        "Aber"
      ],
      [
        "- und das bitte ich besonders zu beachten - was empfindet eine Wesenheit, die nur mit diesen drei Leibern ausgestattet ist?",
        "Sie empfindet nur sich selbst, nur die eigenen Lebens­vorgänge, sie führt ein in sich abgeschlossenes Leben.",
        "Das ist eine höchst interessante Tatsache von außerordentlicher Wichtigkeit, wert, festgehalten zu werden.",
        "Sehen Sie sich einmal ein niederes Tier an.",
        "Was hat es ausgebildet?",
        "Um­gestaltet hat es leblose Substanz in lebendige Substanz,"
      ],
      [
        "lebendige, bewegliche Substanz in empfindende Substanz.",
        "Und empfindende Substanz ist nur da, wo wenigstens die Anlage zu dem vorhanden ist, was später im ausgebildeten Nervensystem erscheint.",
        "So haben wir also leblose Sub­stanz, lebendige Substanz und von empfindungsbegabten Nerven durchsetzte Substanz.",
        "Wenn Sie sich einen Kristall ansehen, so haben Sie sich zunächst in dieser Kristallform einen Ausdruck gewisser Naturgesetze, die im sogenannten leblosen Reich draußen herrschen, vorzustellen.",
        "Kein Kri­stall könnte zustande kommen ohne die ganze ihn um­gebende Natur.",
        "Sie können kein Glied aus dem Kosmos herausreißen und für sich hinstellen, ebensowenig wie Sie den Menschen aus seiner ganzen Umgebung herausreißen können, der, wenn er nur ein paar Meilen über die Erde erhoben würde, sterben müßte.",
        "Wie er nur denkbar ist an dem Orte, an dem er ist, wo die entsprechenden Kräfte sich in ihm zusammenfügen, in ihm leben müssen, so ist es schon beim Kristall der Fall, und wer den Kristall richtig an­schaut, wird in ihm die ganze Natur, den ganzen Kosmos in einem Einzelabdruck sehen.",
        "Es ist ganz richtig, was Cuvier gesagt hat, daß ein vollkommener Anatom aus einem Kno­chen schließen kann, was für einem Tier derselbe angehört hat, weil jedes Tier seine ganz besonderen Knochenformen haben muß."
      ],
      [
        "So lebt auch in der Form des Kristalls der ganze Kosmos.",
        "Und ebenso drückt sich in der lebendigen Substanz eines Einzelwesens der ganze Kosmos aus.",
        "Die bewegten Säfte eines Wesens sind schon eine kleine Welt, ein Abdruck der großen Welt.",
        "Und wenn die Substanz zur Empfindung auf­gerufen wird, was lebt dann in den Empfindungen des ein­fachsten Wesens?",
        "In diesen Empfindungen sind die kos­mischen Gesetze gespiegelt, so daß das einzelne lebendige Wesen mikrokosmisch in sich den ganzen Makrokosmos"
      ],
      [
        "empfindet.",
        "Das Empfindungsleben eines einfachen Wesens ist also ein Abdruck des Kosmos, wie der Kristall ein Ab­druck seiner Form ist.",
        "Mit einem dumpfen Bewußtsein hat man es in solch einfachem Lebewesen zu tun.",
        "Aber was dieses Bewußtsein an größerer Dumpfheit hat, das ist auf der anderen Seite ausgeglichen durch den größeren Umfang.",
        "Der ganze Kosmos leuchtet in dem dumpfen Bewußtsein, im Innern des Lebenswesens auf.",
        "Nun ist aber im Men­schen auch nichts anderes vorhanden als eine kompliziertere Ausbildung derjenigen drei Leiber, die in dem einfachsten empfindenden Lebewesen sich finden.",
        "Nehmen Sie den Menschen und sehen Sie ab von seinem Blute, nehmen Sie ihn als ein Wesen, das geformt ist von der Substanz der es umgebenden physischen Welt, das ebenso wie die Pflanze Säfte in sich enthält, die es zu lebendiger Substanz aufruft, und in die es sich ein Nervensystem eingliedert.",
        "Dieses erste Nervensystem ist das sogenannte sympathische.",
        "Das sym­pathische Nervensystem im Menschen dehnt sich zu beiden Seiten längs des Rückgrats aus, hat auf jeder Seite eine Reihe von Knoten, verzweigt und verästelt sich und schickt seine Fäden zu den verschiedenen Organen: Lunge, Ver­dauungswerkzeuge und so weiter.",
        "Es ist durch Seitenstränge mit dem Rückenmark verbunden."
      ],
      [
        "Zunächst bedeutet dieses sympathische Nervensystem das Empfindungsleben, das Ihnen eben geschildert worden ist.",
        "Der Mensch kann aber mit seinem Bewußtsein nicht hinunterreichen zu dem, was durch diese Nerven von den Weltvorgängen abgespiegelt wird.",
        "Diese Nerven sind Aus­drucksmittel.",
        "Und so, wie das Menschenleben aufgebaut ist aus der umliegenden kosmischen Welt, so spiegelt sich wider in dem sympathischen Nervensystem diese kosmische Welt.",
        "Diese Nerven leben ein dumpfes Innenleben.",
        "Könnte der Mensch untertauchen in dieses sympathische Nervensystem,"
      ],
      [
        "so würde er, wenn er sein oberes Nervensystem einschlä­ferte, wie in einem Lichtleben die großen Gesetze des Kos­mos walten und wirken sehen.",
        "Es gab beim Menschen der Vorzeit ein heute überwundenes Hellsehen, welches man erkennen kann, wenn durch besondere Vorgänge die Tätig­keit des höheren Nervensystems ausgeschaltet und dadurch das untere Bewußtsein freigemacht wird.",
        "Dann lebt der Mensch in dem Nervensystem, das zum Spiegel für die Welt um ihn herum wird, in einer eigenartigen Weise.",
        "Ge­wisse niedere Tiere haben sich diese Stufe des Bewußtseins allerdings erhalten und bewahren sie noch heute.",
        "Es ist also ein dumpfes, dämmerhaftes Bewußtsein, aber es ist wesent­lich umfassender als das gegenwärtige Menschenbewußtsein.",
        "Es spiegelt als dumpfes Innenleben eine weiterreichende Welt, nicht bloß den kleinen Ausschnitt, den der heutige Mensch wahrnimmt."
      ],
      [
        "Für den Menschen tritt aber etwas anderes ein.",
        "Hat im Laufe der Entwicklung bis zum sympathischen Nerven­system der Kosmos ein Spiegelbild gefunden, so öffnet sich auf dieser Stufe der Entwicklung das Wesen wieder nach außen: dem sympathischen System gliedert sich das Rücken­mark ein.",
        "Das Rückenmark- und Gehirnsystem führt dann hin zu den Organen, die mit der Außenwelt die Verbindung herstellen.",
        "Wenn im Menschen die Bildung so weit ist, dann ist er nicht mehr berufen, bloß die ursprünglichen Bildungs-gesetze des Kosmos in sich spiegeln zu lassen, sondern es tritt das Spiegelbild selbst in ein Verhältnis zur Umgebung.",
        "Wenn das sympathische Nervensystem sich zusammen-gegliedert hat mit den höheren Teilen des Nervensystems, so ist dies ein Ausdruck der vor sich gegangenen Umwand­lung des Astralleibes.",
        "Dieser lebt dann nicht mehr bloß das kosmische Leben im dumpfen Bewußtsein mit, sondern er fügt sein besonderes Innenleben zu diesem hinzu.",
        "Durch"
      ],
      [
        "das sympathische Nervensystem empfindet ein Wesen, was außer ihm vorgeht, durch das höhere Nervensystem das­jenige, was in ihm vorgeht.",
        "Und durch die höchste Form des Nervensystems, die gegenwärtig in der allgemeinen Mensch­heitsentwicklung zum Vorschein kommt, wird aus dem höher gegliederten Astralleib wieder das Material entnom­men, um Bilder der Außenwelt, Vorstellungen, zu schaffen.",
        "Der Mensch hat also die Fähigkeit verloren, die ursprüng­lichen dumpfen Bilder der Außenwelt zu erleben; er empfin­det sein Innenleben und baut sich aus diesem seinem Innen­leben auf höherer Stufe eine neue Bilderwelt auf, die ihm zwar ein kleineres Stück der Außenwelt spiegelt, aber in hellerer, vollkommenerer Art."
      ],
      [
        "Mit dieser Umwandlung geht, auf höherer Stufe der Entwicklung, eine andere Hand in Hand.",
        "Es dehnt sich die Umgestaltung des Astralleibes bis auf den Atherleib aus.",
        "Ebenso wie der Ä therleib in seiner Umgestaltung den Astral­leib hervorruft, wie zum sympathischen Nervensystem das Rückenmark- und Gehirnsystem hinzukommen, so bewirkt dasjenige, was von dem Atherleibe nach Aufnahme der niederen Säftezirkulation herausgewachsen und frei gewor­den ist, die Umsetzung der niederen Säfte in das, was wir Blut nennen.",
        "Das Blut ist ebenso ein Ausdruck des indi­vidualisierten Atherleibes wie das Gehirn und Rückenmark ein Ausdruck des individualisierten Astralleibes.",
        "Und durch diese Individualisierung kommt das zustande, was sich in dem «Ich» auslebt."
      ],
      [
        "Wenn wir von diesem Gesichtspunkte aus den Menschen in seiner Entwicklung so weit verfolgt haben, so sehen wir, daß wir zunächst eine fünfgliedrige Kette haben, die sich uns wie folgt zusammenschließt: erstens der physische Leib, zweitens der Atherleib, drittens der Astralleib, oder erstens die unorganischen, neutralen, physischen Kräfte, zweitens"
      ],
      [
        "die Lebenssäfte, die sich auch in der Pflanze finden, drittens das niedere oder sympathische Nervensystem, viertens der von dem niederen astralen Leibe herausgehobene höhere Astralleib, der im Rückenmark und Gehirn seinen Aus­druck findet, fünftens dasjenige Prinzip, das den Atherleib individualisiert."
      ],
      [
        "So wie diese zwei Prinzipien individualisiert worden sind, so wird auch für den Menschen das erste Prinzip indi­vidualisiert, durch welches die leblosen Stoffe von außen eindringen und den menschlichen Körper aufbauen.",
        "Diese Umwandlung ist beim heutigen Menschen erst in der ersten Anlage vorhanden."
      ],
      [
        "Wir sehen, wie die äußeren formlosen Stoffe einfließen in den menschlichen Leib, wie der Atherleib diese Stoffe zu lebendigen Gebilden aufruft und wie dann durch den Astral-leib Bilder der Außenwelt geformt werden; wie weiter dieser Reflex der Außenwelt sich zu inneren Erlebnissen entfaltet und dann dieses Innenleben aus sich selbst wieder Bilder der Außenwelt erzeugt."
      ],
      [
        "Greift nun die Umwandlung auf den Atherleib über, so entsteht das Blut.",
        "Das Blutgefäß-System mit dem Herzen ist ein Ausdruck des umgewandelten Atherleibes, wie das Rückenmark- und Gehirnsystem ein solcher des umgewan­delten Astralleibes.",
        "Wie durch das Gehirn die Außenwelt verinnerlicht wird, so wird durch das Blut diese Innenwelt in dem Leib des Menschen zu einem äußeren Ausdrucke umgeschaffen.",
        "Ich muß im Gleichnisse sprechen, wenn ich die hier in Betracht kommenden komplizierten Vorgänge darstellen will.",
        "Das Blut nimmt die durch das Gehirn ver­innerlichten Bilder der Außenwelt auf, gestaltet sie zu lebendigen Bildungskräften um und bildet durch sie den jetzigen Menschenleib aus.",
        "Das Blut ist so der Stoff, der den menschlichen Leib auferbaut.",
        "Es stellt sich hier ein Vorgang"
      ],
      [
        "uns vor Augen, durch den das Blut das Höchste aufnimmt, was es der Umwelt entnehmen kann, den Sauerstoff, näm­lich dasjenige, was das Blut stets wieder erneuert, mit neuem Leben versorgt.",
        "Dadurch wird das Blut veranlaßt, sich der Außenwelt zu öffnen."
      ],
      [
        "Damit haben wir den Weg verfolgt von der Außenwelt zur Innenwelt und wieder zurück vom Innern zum Außern.",
        "Nun ist ein Zweifaches möglich.",
        "Wir sehen, daß die Entstehung des Blutes da liegt, wo der Mensch als selbständiges Wesen der Außenwelt entgegen­tritt, wo er aus den Empfindungen, zu denen die Außenwelt geworden ist, selbständig wiederum Gestalten und Bilder schafft, wo er schöpferisch wird, wo also das Ich, der Eigen­wille aufleben kann."
      ],
      [
        "Kein Wesen, in dem dieser Vorgang noch nicht stattgefunden hat, könnte aus sich selbst heraus Ich sagen.",
        "Im Blute liegt das Prinzip für die Ich-Werdung.",
        "Ein Ich kann nur da zum Ausdrucke kommen, wo ein Wesen die Bilder, die es von der Außenwelt erzeugt, in sich selbst zu gestalten vermag."
      ],
      [
        "Ein Ich-Wesen muß fähig sein, die Außenwelt in sich aufzunehmen und innerhalb seiner selbst wieder zu erzeugen.",
        "Hätte der Mensch bloß Gehirn, so könnte er nur Bilder der Außenwelt in sich erzeugen und in sich erleben; er würde dann zu sich nur sagen können: Die Außenwelt ist in mir als Spiegelbild noch einmal wieder­holt; kann er aber diese Wiederholung der Außenwelt zu einer neuen Gestalt aufbauen, dann ist diese Gestalt nicht mehr bloß die Außenwelt: sie ist «Ich»."
      ],
      [
        "Ein Wesen mit bloßem sympathischen Nervensystem spiegelt die Außen-welt, es empfindet also diese Außenwelt noch nicht als sich, noch nicht als Innenleben.",
        "Ein Wesen mit Rückenmark und Gehirn empfindet die Spiegelung als Innenleben."
      ],
      [
        "Ein Wesen aber mit Blut erlebt als seine eigene Gestalt sein Innenleben.",
        "Durch das Blut wird mit Hilfe des Sauerstoffes der Außen­welt nach den Bildern des Innenlebens der eigene Leib gestaltet."
      ],
      [
        "Diese Gestaltung kommt als Ich-Wahrnehmung zum Ausdruck.",
        "Nach zwei Seiten weist das Ich, und das Blut ist der äußere Ausdruck dieser Hinweisung.",
        "Nach innen ge­richtet ist der Blick des Ich, nach außen gerichtet ist der Wille des Ich."
      ],
      [
        "Nach innen sind die Kräfte des Blutes gerich­tet, sie bauen das Innere auf; nach außen sind sie gerichtet zum Sauerstoff der äußeren Welt hin.",
        "Daher geht der Mensch, wenn er in Schlaf fällt, im Unbewußtsein unter, er geht unter in dasjenige, was das Bewußtsein im Blute er­leben kann."
      ],
      [
        "Wenn der Mensch aber sein Auge der Außen­welt öffnet, dann nimmt das Blut die durch Gehirn und Sinne erzeugten Bilder in seine Gestaltungskräfte auf.",
        "Das Blut steht so in der Mitte zwischen der inneren Bilderwelt und der lebendigen Gestaltenwelt des Äußeren."
      ],
      [
        "Diese Rolle wird uns klar werden, wenn wir zwei Erscheinungen be­trachten.",
        "Die eine Erscheinung ist die Abstammung, die Verwandtschaft der bewußten Wesen, die andere Erschei­nung ist die Erfahrung der Welt der äußeren Erlebnisse."
      ],
      [
        "Die Abstammung stellt uns dahin, wo wir, wie man es gewöhn­lich nennt, durch das Blut stehen.",
        "Der Mensch wird heraus-geboren aus einem Zusammenhang, einer Rasse, einem Stamme, aus seiner Vorfahrenreihe, und dasjenige, was aus seinen Vorfahren sich auf ihn vererbt, findet seinen Ausdruck im Blute."
      ],
      [
        "Im Blut wird gleichsam zu­sammengefaßt, was sich aus der materiellen Vergangen­heit des Menschen herausgebildet hat.",
        "Es wird aber im Blute auch vorgebildet, was sich für die Zukunft des Menschen vorbereitet."
      ],
      [
        "Wenn der Mensch daher sein höheres Bewußtsein herab-dämpft, wenn er in der Hypnose, im Somnambulismus oder im atavistischen Hellsehen ist, dann taucht er unter in ein viel tieferes Bewußtsein und nimmt die großen Weltgesetze wahr, in einer traumartigen Form, nur viel klarer und heller"
      ],
      [
        "als in den hellsten Träumen des gewöhnlichen Schlafes.",
        "Der Mensch hat dann die Tätigkeit des Gehirns, und bei tief­stem Somnambulismus auch diejenige des Rückenmarkes unterdrückt; er erlebt die Tätigkeit seines sympathischen Nervensystems, das heißt in einer dumpfen, dämmerhaften Form das Leben im ganzen Kosmos.",
        "In einem solchen Falle bringt dann das Blut nicht mehr die Bilder des Innenlebens zum Ausdruck, die durch das Gehirn vermittelt sind, son­dern dasjenige, was die Außenwelt in ihn hineingebaut hat.",
        "Nun aber haben an ihm gebaut die Kräfte seiner Vorfahren.",
        "Wie er die Form seiner Nase von einem Vorfahren hat, so die Form seines ganzen Leibes.",
        "Er empfindet so bei ge­dämpftem Bewußtsein seine Vorfahren in sich, wie er die durch die Sinne erzeugten Bilder der Außenwelt bei wachem Bewußtsein empfindet.",
        "Das heißt: seine Vorfahren rumoren in seinem Blute.",
        "Er lebt dann noch das Leben seiner Vor­fahren dumpf mit."
      ],
      [
        "Alles in der Welt ist in Entwicklung begriffen, auch das menschliche Bewußtsein.",
        "Die Bewußtseinsart, welche der Mensch jetzt hat, war ihm nicht immer eigen.",
        "Wenn wir in der Zeit zurückgehen zu unseren fernen Vorfahren, so fin­den wir eine andere Bewußtseinsart.",
        "Gegenwärtig nimmt der Mensch in seinem wachen Tagesleben durch seine Sinne die äußeren Dinge wahr und bildet sie zu Vorstellungen um.",
        "Diese Vorstellungen der Außenwelt wirken auf sein Blut.",
        "Es lebt daher und arbeitet in seinem Blute alles das, was er durch die äußeren Erlebnisse der Sinne empfangen hat.",
        "Das Gedächtnis ist nun mit diesen Erlebnissen, mit den Erfahrungen der Sinne erfüllt.",
        "Dagegen bleibt diesem heu­tigen Menschen unbewußt, was sich in seinem leiblichen Innenleben durch die Vererbung von seinen Vorfahren her vererbt hat.",
        "Er weiß nichts von den Formen seiner inneren Organe.",
        "So war es nicht in der Vorzeit.",
        "Da lebte im Blute"
      ],
      [
        "nicht nur, was die Sinne von außen empfangen hatten, son­dern auch dasjenige, was in der Leibesgestalt vorhanden ist.",
        "Und weil diese Leibesgestalt ererbt ist von den Vor­fahren, so empfand der Mensch in sich das Leben der Vor­fahren."
      ],
      [
        "Denkt man sich ein solches Bewußtseinsleben gestei­gert, so erhält man eine Vorstellung davon, wie es sich auch in einem entsprechenden Gedächtnisse zum Ausdruck bringt.",
        "Ein Mensch, der nur erlebt, was er durch seine Sinne wahr­nimmt, der erinnert sich auch nur an das, was er durch die äußere Sinneserfahrung erlebt hat."
      ],
      [
        "Er kann nur ein Be­wußtsein von dem haben, was er seit seiner Kindheit auf diese Art erfahren hat.",
        "Anders war es beim Menschen der Vorzeit.",
        "Der erlebte, was in ihm war, und da dieses «Innere» ein Ergebnis der Vererbung ist, erlebte er in sei­nen Vorstellungen die Erlebnisse seiner Vorfahren mit."
      ],
      [
        "Er erinnerte sich nicht nur an seine Kindheit, sondern auch an die Erlebnisse seiner Vorfahren.",
        "Dieses Leben seiner Vor­fahren war in den Bildern, die sein Blut empfing, mit ge­genwärtig.",
        "So unglaublich es für die heutige materialistische Vorstellungsart auch ist: es ist doch wahr, daß es einmal ein Bewußtsein gegeben hat, durch das die Menschen nicht nur ihre Sinneswahrnehmungen als ihre eigenen Erlebnisse be­trachteten, sondern auch die Erlebnisse ihrer Vorfahren."
      ],
      [
        "Damals sagten sie: «Ich habe es erlebt» nicht nur zu dem, was ihre eigene Person erlebt hat, sondern auch zu dem, was die Vorfahren erfahren hatten; sie erinnerten sich des­sen.",
        "Zwar war diese frühere Bewußtseinsform des Menschen gegenüber dem gegenwärtigen wachen Tagesbewußtsein dämmerhaft, mehr wie ein lebhaft gesteigertes Träumen, aber sie war dafür umfassender."
      ],
      [
        "Sie dehnte sich über die Erfahrung der Vorfahren aus.",
        "Der Sohn fühlte sich mit Vater, Großvater in einem Ich verbunden, weil er deren Erlebnisse als seine eigenen miterlebte."
      ],
      [
        "Weil der Mensch dieses Bewußtsein hatte, weil er nicht bloß in seiner persönlichen Welt lebte, sondern weil in sei­nem Innern das Bewußtsein seiner vorhergehenden Gene­ration auflebte, deshalb bezeichnete er auch nicht bloß seine Person mit einem Namen, sondern eine ganze Generatio­nenreihe.",
        "Der Sohn, der Enkel und so weiter bezeichneten das Gemeinsame, das durch sie alle hindurchging, mit einem Namen."
      ],
      [
        "Der Mensch empfand sich als ein Glied der ganzen Generationsreihe.",
        "Das war eine wirkliche und wahre Emp-findung.",
        "Und wodurch wurde diese Bewußtseinsform in eine andere verwandelt?",
        "Sie wurde es durch ein Ereignis, das die geheimwissenschaftliche Geschichte gut kennt."
      ],
      [
        "Wenn Sie in der Geschichte zurückgehen, dann tritt für alle Völker des Erdkreises ein Moment auf, der Ihnen ganz genau bei jedem einzelnen Volke bezeichnet werden kann.",
        "Das ist der Moment, wo das Volk in einen neuen Kulturzustand ein­tritt, in dem es aufhört, alte Traditionen zu haben, wo es aufhört, Urweisheit zu besitzen, jene Weisheit, die durch das Blut der Generationen hindurchgerollt ist."
      ],
      [
        "Die Völker haben ein Bewußtsein davon, und dieses Bewußtsein finden wir ausgedrückt in den alten Sagen der Völker.",
        "Die Stämme blieben nämlich in früherer Zeit in sich abgeschlossen, die einzelnen Mitglieder der Familien heirateten untereinan­der."
      ],
      [
        "Das finden Sie ursprünglich bei allen Rassen und Völ­kern.",
        "Und ein wichtiger Moment für die Menschheit ist der, als dieses Prinzip durchbrochen wird, sich fremdes Blut mit fremdem Blute mischt, wo die Nah-Ehe in die Fern-Ehe übergeht."
      ],
      [
        "Die Nah-Ehe bewahrt das Blut der Generationen, sie läßt dasselbe Blut durch die einzelnen Glieder rinnen, das seit Generationen den Stamm, die Nation durchfloß.",
        "Die Fern-Ehe gießt neues Blut dem Menschen ein, und diese Durchbrechung des Stammesprinzipes, diese Mischung des Blutes, die bei allen Völkern sich findet und früher oder"
      ],
      [
        "später auftritt, bedeutet die Geburt des äußeren Verstandes, die Geburt des Intellektes."
      ],
      [
        "Das ist eben das Wichtige, daß in alten Zeiten eine Art dämmerhaften Hellsehens vorhanden war und daß Mythen und Sagen aus diesem hellseherischen Vermögen heraus ent­standen sind, welches sich in dem verwandtschaftlichen Blute ausleben kann wie in dem vermischten Blute das ge­genwärtige Bewußtsein.",
        "Mit dem Eintritt der Fern-Ehe fällt auch die Geburt des logischen Denkens, die Geburt des Intellektes zusammen.",
        "So überraschend das ist, so wahr ist es.",
        "Es ist eine Erkenntnis, die immer mehr und mehr durch die äußere Forschung bestätigt werden wird.",
        "Die Anfänge sind schon gemacht.",
        "Die Blutmischung, die mit der Fern-Ehe eintritt, ist zu gleicher Zeit dasjenige, was das Hell-sehen von früher zunächst auslöscht, um die Menschheit zu einer höheren Entwicklungsstufe hinaufzuheben.",
        "Wie der, welcher eine okkulte Entwicklung durchmacht, dieses Hell-sehen wieder heraufhebt und es zu einer neuen Form um­wandelt, so hat sich umgekehrt das gegenwärtige wache Tagesbewußtsein aus einem alten dämmerhaften Hellsehen heraus entwickelt."
      ],
      [
        "Gegenwärtig drückt sich die ganze Umwelt, der der Mensch sich hingibt, im Blute aus, und diese Umwelt formt das Innere daher nach dem Äußeren.",
        "Beim Urmenschen drückte sich mehr das leibliche Innere im Blute aus.",
        "In den Urzeiten vererbten sich mit der Erinnerung an die Erleb­nisse der Vorfahren auch deren Neigungen zu diesem oder jenem Guten und Bösen.",
        "In dem Blute des Nachkommen waren die Wirkungen der Neigungen der Vorfahren zu spüren.",
        "Als dann das Blut durch die Fern-Ehe gemischt wurde, da wurde auch dieser Zusammenhang mit den Vor­fahren durchschnitten.",
        "Der Mensch ging über zum persön­lichen Eigenleben.",
        "Er lernte sich in seinen sittlichen Neigungen"
      ],
      [
        "nach dem zu richten, was er im persönlichen Leben erfahren hat.",
        "So drückt sich in einem ungemischten Blute die Macht des Vorfahrenlebens aus, in dem gemischten die Macht der eigenen Erlebnisse.",
        "Davon erzählen die Sagen und Mythen der Völker.",
        "Sie sagen uns: Was Macht hat auf dein Blut, das hat Macht über dich.",
        "Die Macht der Völker-traditionen hörte auf, als sie nicht mehr wirken konnte auf das Blut, als dessen Aufnahmefähigkeit für solche Vor­fahrenmacht erlischt durch die Beimischung des fremden Blutes.",
        "Und dieser Satz gilt im weitesten Umfange.",
        "Welche Macht auch immer sich eines Menschen bemächtigen will, sie muß so auf ihn wirken, daß sich diese Wirkung im Blute ausdrückt.",
        "Will also eine böse Macht Einfluß gewinnen auf den Menschen, dann muß sie Herrschaft haben über sein Blut.",
        "Das ist der tiefe und geistvolle Zug des erwähnten Wortes aus Faust.",
        "Daher sagt der Repräsentant des bösen Prinzipes: Schreibe mir deinen Namen mit Blut unter den Pakt.",
        "Habe ich deinen Namen mit deinem Blute geschrie­ben, dann habe ich dich bei demjenigen erfaßt, wodurch der Mensch überhaupt erfaßt werden kann, ich habe dich zu mir herübergezogen.",
        "Wem das Blut gehört, dem gehört auch der Mensch oder des Menschen Ich."
      ],
      [
        "Wenn zwei Menschengruppen aufeinanderstoßen, wie dies bei der Kolonisation der Fall zu sein pflegt, dann wird derjenige, welcher die Evolution kennt, sagen können, ob eine fremde Kultur aufgenommen werden kann oder nicht.",
        "Nehmen Sie ein Volk, das herausgewachsen ist aus seiner Umgebung, in dessen Blut sich seine Umgebung hinein-gebildet hat, und versuchen Sie, ihm eine fremde Kultur aufzupfropfen.",
        "Es ist unmöglich.",
        "Das ist auch der Grund, warum gewisse Ureinwohner zugrunde gehen mußten, als die Kolonisten in bestimmte Gegenden kamen.",
        "Von diesem Gesichtspunkte aus wird man diese Frage beurteilen müssen,"
      ],
      [
        "und dann wird man auch nicht mehr glauben, daß man jedes jedem aufpfropfen kann.",
        "Dem Blute darf nur das­jenige zugemutet werden, was es noch vertragen kann."
      ],
      [
        "Die Entdeckung der neueren Wissenschaft, daß, wenn man Blut eines Tieres mit dem eines ihm nicht verwandten vermischt, das eine Blut das andere tötet, ist eine alte okkulte Erkenntnis.",
        "Mischen Sie Menschenblut mit dem Blut niederer Affen, so tritt Vernichtung ein, weil sie zu weit voneinander abliegen.",
        "Mischen Sie Menschenblut und das Blut höherer Affen, so töten sie sich nicht.",
        "So wie die Mischung des Blutes von Tiergattungen, wenn sie zu ent­fernt sind, den wirklichen Tod hervorbringt, so tötete es das alte Hellsehen des niederen Menschen, als sein Blut mit dem Blute des nicht stammverwandten vermischt wurde.",
        "Das ganze heutige Geistesleben ist nichts anderes als das Er­gebnis der Blutmischung, und man wird in nicht zu ferner Zeit auch den Einfluß der Blutmischung studieren und im Menschenleben zurückverfolgen können, wenn man von diesem Gesichtspunkte aus wieder die Forschung betreibt.",
        "Also: Blut zu Blut von in der Entwicklung sich fernstehen-den Tiergattungen tötet; Blut zu Blut von verwandten Tier-gattungen tötet nicht.",
        "Der physische Organismus des Men­schen wird erhalten, auch wenn fremdes Blut zu fremdem Blute kommt, aber die hellseherische Kraft stirbt unter dem Einfluß der Blutmischung oder der Fern-Ehe."
      ],
      [
        "Der Mensch ist so gestaltet, daß, wenn sich Blut und Blut mischt und diese Blutmischung nicht von einer Seite her­kommt, die in der Entwicklung zu weit absteht, der In­tellekt geboren wird.",
        "Dadurch wird die ursprünglich aus dem Animalischen kommende Hellseherkraft vernichtet und ein neues Bewußtsein in der Entwicklung geboren."
      ],
      [
        "Es ist also bei der menschlichen Entwicklung auf höherer Stufe etwas Ähnliches vorhanden wie auf niederer Stufe in"
      ],
      [
        "der Tierwelt.",
        "In der Tierwelt tötet fremdes Blut das fremde Blut.",
        "In der Menschenwelt tötet das fremde Blut dasjenige, was mit dem Verwandtenblut verbunden ist: das dumpfe, dämmerhafte Hellsehen.",
        "Das wache Tagesbewußtsein des Menschen der Gegenwart ist also ein Ergebnis eines Tötungs­prozesses.",
        "Es ist im Laufe der Entwicklung das Geistesleben der Nah-Ehe getötet worden, aber es ist auch dafür aus der Fern-Ehe das Neue, der Intellekt, das wache Tagesbewußt­sein geboren worden."
      ],
      [
        "Was also im Blute des Menschen leben kann, das lebt in seinem Ich.",
        "Wie der physische Leib der Ausdruck ist für das physische Prinzip, der Ätherleib für die Lebenssäfte und ihre Systeme, der Astralleib für das Nervensystem, so ist das Blut der Ausdruck für das Ich.",
        "Physisches Prinzip, Ätherleib, Astralleib sind das Obere, Blutzustand und Ich sind das Mittlere und physischer Leib, Lebenssystem, Ner­vensystem sind das Untere.",
        "Was sich deshalb eines Men­schen bemächtigen will, das muß sich seines Blutes be­mächtigen.",
        "Das muß berücksichtigt werden, wenn man im praktischen Leben vorwärtskommen will.",
        "Man kann zum Beispiel ein fremdes Volk in seiner Eigenart töten, wenn man kolonisierend seinem Blute zumutet, was dieses Blut nicht ertragen kann.",
        "Denn im Blute drückt sich das Ich aus.",
        "Erst dann haben Schönheit und Wahrheit den Menschen, wenn sie sein Blut haben.",
        "Mephistopheles bemächtigt sich des Blutes des Faust, weil er dessen Ich haben will.",
        "Der Satz, der das Leitmotiv dieses Vortrags bildet, ist daher aus der Tiefe der Erkenntnis heraus genommen.",
        "Ja, Blut ist ein ganz besonderer Saft."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "DER URSPRUNG DES LEIDES Berlin, 8. November 1906",
    "paragraphs": [
      "Mehr noch als die anderen Vorträge des Winterzyklus hängen die drei nächsten zusammen: der heutige «Über den Ursprung des Leids», der nächste «Über den Ursprung des Bösen» und der folgende «Wie begreift man Krankheit und Tod?», doch wird jeder von diesen drei Vorträgen auch in sich selbst abgeschlossen und verständlich sein.",
      "Wenn der Mensch das Leben rings um sich her betrachtet, wenn er Selbstschau hält und den Sinn und die Bedeutung des Lebens bei sich selbst erforschen will, dann findet er einen eigentümlichen, zum Teil warnenden, zum Teil ganz rätselvollen Wächter vor dem Tore dieses Lebens stehen: das Leid.",
      "Das Leiden, das seinerseits wiederum eng verbunden ist mit dem, was wir in den nächsten Vorträgen betrachten wollen, mit dem Bösen, mit Krankheit und Tod, erscheint dem Menschen manchmal als etwas, was so tief ins Leben eingreift, daß es mit den allerhöchsten Fragen des Lebens zusammenzuhängen scheint. Daher ist die Frage nach dem Leide eine der wesentlichsten aller Weltanschauungen seit den ältesten Zeiten des Menschengeschlechts, und immer, wenn man versuchte, den Wert des Lebens abzuschätzen, den Sinn des Lebens zu erkennen, hat man vor allen Dingen erkennen wollen, welche Rolle das Leid, der Schmerz im menschlichen Leben spielt.",
      "Wie ein Störenfried erscheint das Leid mitten im fröh­lichen Leben, es erscheint als eine Herabminderung von Lebenlust und Lebenshoffnung. Gerade diejenigen, welche",
      "den Wert des Lebens in der Lebensfreudigkeit suchen, welche nur für die Lebensfreudigkeit da zu sein scheinen, haben diesen Störenfried, Leid und Schmerz, am meisten emp­funden. Wie wäre es sonst erklärbar, daß bei einem so lebensfrohen, so in Lebensfreudigkeit aufgehenden Volke, wie es die Griechen waren, ein Ausspruch wie ein dunkler Punkt am Sternenhimmel der Schönheit des Griechentums auftaucht, der Ausspruch des weisen Silen im Gefolge des Dionysos: Was ist für den Menschen das Beste? Das Beste für den Menschen ist, nicht geboren zu sein, und ist er einmal geboren, so ist das Zweitbeste, bald nach der Geburt zu sterben. - Vielleicht wissen Sie, daß Friedrich Nietzsche, als er die Geburt der Tragödie aus dem Geiste des alten Grie­chentums zu begreifen suchte, an diesen Spruch anknüpfte, um zu zeigen, wie auf dem Grunde griechischer Lebensweis­heit und griechischer Kunst das Leid und die Betrübnis des Menschen über das Leid und über das, was damit zusam­menhängt, eine bedeutungsvolle Rolle spielt.",
      "Nun aber finden wir auch einen anderen und kaum viel jüngeren Satz aus dem Griechentum, einen kurzen Aus­spruch, der uns zu gleicher Zeit zeigt, wie in einer gewissen Art wiederum aus diesem alten Griechentum heraus eine Erkenntnis aufdämmert, daß das Leiden und die Schmerzen der Welt doch nicht bloß eine verhängnisvolle Rolle spielen. Es ist der Ausspruch, den wir bei einem der ältesten grie­chischen Tragiker, bei Äschylos finden, daß aus Leiden Er­kenntnis erwächst. Da werden zwei Dinge zusammenge­bracht, von denen zweifellos ein großer Teil der Menschheit das eine aus dem Leben hinweggelöscht haben möchte, wäh­rend er das andere, die Erkenntnis, als eines der höchsten Güter des Lebens betrachtet.",
      "Daß das Leben und das Leid, wenigstens das Leben der heutigen Menschen und der höheren Wesen auf unserem",
      "Erdenrund, tief verflochten sind, hat man von jeher geglaubt einsehen zu müssen. So stehen nicht nur am Ausgangspunkt des biblischen Schöpfungsmythos Erkenntnis des Guten und Bösen und Leid innig miteinander verbunden, sondern wir sehen auch auf der anderen Seite, mitten aus der Anschauung des Alten Testaments heraus, wie aus einer schwarzen Anschauung des Leidens auch eine helle, licht-volle aufdämmert.",
      "Wenn wir uns im Alten Testament um-sehen, wenn wir den Schöpfungsmythos in bezug auf diese Frage verfolgen, so wird uns klar, daß man innerhalb dieser alten Weltansdiauung Leiden und Sünde zusammenbrachte, daß man Leid als die Folge der Sünde ansah. Heute, bei der Denkweise, die selbst da, wo man nicht recht will, sich der materialistischen Weltauffassung nähert, begreift man nicht mehr leicht, wie man in der Sünde die Ursache des Leidens suchen kann.",
      "Aber wenn wir Geistesforscher sind und uns in frühere Zeitalter hineindenken lernen, dann werden wir sehen, daß es nicht ganz so unsinnig ist, an einen solchen Zusammenhang zu glauben, und der nächste Vortrag wird uns zeigen, daß es eine Möglichkeit gibt, einen Zusammen­hang zwischen dem Bösen und dem Leid zu sehen. Das Leid aber aus seinen Ursachen zu erklären, stellte sich für die Anschauung des alten Judentums als eine Unmöglichkeit heraus.",
      "So sehen wir, daß mitten in dieser Anschauung, die Leid und Sünde in Zusammenhang bringt, die merkwür­dige Gestalt des Hiob steht, jene Gestalt, die uns zeigt oder zeigen will, wie Leiden und unsägliche Schmerzen mit einem vollkommen unschuldigen Leben zusammenhängen können, wie es unverdiente Leiden und Schmerzen geben kann. In dem Bewußtsein dieser eigenartig tragischen Persönlichkeit Hiob sehen wir noch einen anderen Zusammenhang von Leid und Schmerz aufdämmern, einen Zusammenhang mit der Veredlung des Menschen.",
      "Das Leid erscheint uns da als",
      "eine Prüfung, als Wurzel eines Aufwärtsklimmens, einer Höherentwicklung. So braucht dieses Leiden im Sinne dieser Hiob -Tragik keineswegs seinen Ursprung im Bösen zu haben, sondern kann selbst erster Ursprung sein, so daß das, was aus ihm hervorgeht, eine vollkommenere Phase menschlichen Daseins, menschlichen Lebens darstellt. Das alles liegt unserem heutigen, modernen Denken ziemlich fern, und die breitere Masse unseres heutigen gebildeten Publikums kann sich nicht mehr in eine solche Denkweise hineinfinden. Sie brauchen aber nur in Ihrem Leben etwas zurückzudenken und Sie werden sehen, daß Vollkommen­heit und Leid gar oft auch vor Ihren Augen zusammen­gestellt erschien, und daß es in der Menschheit immer ein Bewußtsein gegeben hat von dem Zusammenhang zwischen Leiden und Vollkommenheit. Dieses Bewußtsein wird uns hinüberheben zu dem, was wir heute im Sinne der Geistes-forschung zu betrachten haben werden, nämlich den Zu­sammenhang zwischen Leiden und Geistigkeit.",
      "Erinnern Sie sich, wie oft in diesem oder jenem Trauer-spiel der tragische Held vor Ihren Augen gestanden hat. Durch Leiden und leidensvolle Kämpfe hindurch führt der Dichter immer wieder und wiederum den Helden; und wenn er dann bis zu dem Punkte kommt, wo der Schmerz sich aufs höchste steigert und in dem Ende des physischen Körpers seinen Abschluß findet, dann lebt in der Seele des Zuschauers nicht bloß Mitleid mit dem tragischen Helden, nicht bloß die Betrübnis darüber, daß solche Leiden, wie sie sich eben abgespielt haben, möglich sind, sondern es stellt sich heraus, daß der Mensch vom Anblick des Leidens ge­hoben und erbaut wurde, daß er das Leid hat untergehen sehen im Tode und aus dem Tode heraus sich die Gewißheit ergeben hat, daß es einen Sieg gibt über Schmerzen und Leiden, ja selbst über den Tod. Durch nichts kann künstlerisch",
      "dieser höchste Sieg des Menschen, dieser Sieg seiner innersten Kräfte und Triebe, dieser Sieg des edelsten Trie­bes seiner Natur so erhaben vor Augen geführt werden als durch das Trauerspiel. Wenn dem Bewußtsein dieses Sieges das Erlebnis von Leiden und Schmerzen vorhergegangen ist und wir von solchen Tatsachen, die sich vor den Augen des Zuschauers im Theater immer wieder abspielen können, aufschauen zu dem, was ein großer Teil der heutigen Mensch­heit noch immer als das Höchste aller geschichtlichen Ent­wicklung empfindet, wenn wir aufschauen zu dem Ereignis, das unsere Zeitrechnung in zwei Teile teilt, zu dem Ereig­nisse der Erlösung durch den Christus Jesus, dann kann es uns auffallen, daß eine der größten Erhebungen, eine der größten Erbauungen und Siegeshoffnungen, die jemals im Herzen der Menschen Platz gegriffen haben, aus dem welt-geschichtlichen Anblick des Leides entsprossen ist. Die gro­ßen, bedeutsamen und tief in das Menschenherz einschnei­denden Empfindungen der christlichen Weltanschauung, jene Empfindungen, die für so viele Menschen Lebenshoff­nung und Lebenskraft sind, die Gewißheit geben, daß es ein Ewiges, daß es einen Sieg über den Tod gibt, alle diese erbauenden und erhebenden Empfindungen entspringen aus der Anschauung eines universellen Leidens, eines Leidens, das die Unschuld trifft, eines Leidens, das durch keine Sünde der eigenen Persönlichkeit herbeigeführt worden ist.",
      "So sehen wir auch hier ein Höchstes im Bewußtsein der Menschheit sich an das Leid anknüpfen. Und wenn wir so sehen, wie diese Dinge im kleineren und im größeren immer wieder in der Menschheit auftauchen, wie sie geradezu den elementaren Teil der ganzen menschlichen Natur und des ganzen menschlichen Bewußtseins bilden, dann muß es uns doch scheinen, als ob das Leiden irgendwie mit dem Höch­sten im Menschen zusammenhänge.",
      "Nur ein Hinweis sollte das sein auf eine Grundempfin­dung der menschlichen Seele, die sich immer und immer wieder losringt, und die gleichsam wie ein großer Trost dasteht dafür, daß es Leiden gibt. Wenn wir uns nun noch feiner und intimer in das Menschenleben einleben, so kön­nen sich uns auch Erscheinungen vor die Seele stellen, die uns auf die Bedeutung des Leidens hinweisen. Wir werden hier symptomatisch auf eine solcheErscheinung hinweisen müssen, die vielleicht kaum damit zusammenzuhängen scheint, wenn wir uns jedoch intimer auf die menschliche Natur einlassen, werden wir sehen, daß auch diese Erscheinung auf die Bedeutung gewisser Seiten des Leides hinweisen wird.",
      "Denken Sie noch einmal an das tragische Kunstwerk, das Trauerspiel, das nur entstehen kann, wenn sich des Dichters Seele weit, weit öffnet, aus sich herausgeht und lernt, frem­des Leid mitzuempfinden, fremdes Leid auf die eigene Seele abzulagern. Und nun vergleichen Sie diese Empfindung nicht etwa bloß mit dem Lustspiele - da werden wir keinen guten Vergleich herausbekommen -, sondern mit etwas, was in gewisser Weise auch zur. Kunst gehört: mit der Stimmung, aus der die Karikatur fließt, die vielleicht mit Spott und Hohn dasjenige im Zerrbilde zeigt, was in der Seele des anderen vorgeht und in die äußere Wirksamkeit tritt. Versuchen wir es, uns zwei Menschen vor die Seele hinzustellen, von denen der eine ein Ereignis oder einen Menschen tragisch ergreift, der andere als Karikatur er­faßt. Nicht ein bloßer Vergleich, nicht ein bloßes Bild ist es, wenn wir sagen, die Seele des tragischen Dichters und Künstlers erscheint uns, wie wenn sie aus sich herausginge und weiter und weiter würde. Was aber eröffnet sich ihr durch dieses Weiterwerden? Das Verständnis des anderen Menschen. Durch nichts versteht man das Leben des an­deren mehr, als wenn man seinen Schmerz auf die eigene",
      "Seele ablagern läßt. Was muß man aber tun, wenn man karikieren will? Man darf nicht eingehen auf das, was die andere Seele fühlt, man muß sich über sie stellen, sie von sich weisen, und dieses Vonsichweisen ist die Grundlage des Zerrbildes. Niemand wird leugnen, daß, ebenso wie uns durch das tragische Mitleid die andere Persönlichkeit tief verständlich wird, durch die Karikatur dasjenige vor uns auftritt, was in der Seele der eigenen Persönlichkeit des Karikierenden lebt. Viel mehr lernen wir die Überlegen­heit, den Witz, das Anschauungsvermögen, die Phantasie des Karikierenden kennen als den, der karikiert wird.",
      "Haben wir so aus gewissen Symptomen heraus anschau­lich gemacht, daß das Leid doch mit etwas Tiefem in der Menschennatur zusammenhängt, so dürfen wir hoffen, daß durch ein Begreifen des eigentlichen Wesens der Menschen-natur uns auch Schmerz und Leid in ihrem Ursprung klar werden können.",
      "Die Geisteswissenschaft, die wir hier zu vertreten haben, geht davon aus, daß alles Dasein um uns herum seinen Ursprung aus dem Geiste genommen hat. Eine mehr mate­rialistische Anschauung sieht den Geist nur da, wo er wie eine Krone der sinnlichen Schöpfung erscheint, wie eine Blüte, die sich aus der Wurzel des materiellen Daseins her­aushebt. Diese letztere Anschauung sieht rings um sich das materielle Dasein, die physische Körperwelt sich herauf-organisieren innerhalb der lebenden Wesen, sie sieht das Bewußtsein, die Empfindung entspringen, sieht Lust und Leid innerhalb des Lebens hervorgehen und den Geist aus der Körperlichkeit heraus sich erheben.",
      "Wenn wir so das Leben rings um uns betrachten, so ist auch für die wahre Geistesforschung der Geist, wie er uns in der sinnlichen Welt entgegentritt, zunächst ein Ergebnis der physischen Natur, aus welcher er heraussprießt.",
      "In den zwei letzten Vorträgen wurde dargestellt, wie wir uns im Sinne der Geistesforschung den ganzen Menschen, den physischen oder leiblichen, den seelischen und den geistigen Menschen vorzustellen haben. Das, was wir mit Augen sehen, mit den Sinnen äußerlich wahrnehmen kön­nen, das, was der Materialismus als das einzige Wesen der Natur betrachtet, ist der Geistesforschung nichts an­deres als das erste Glied der menschlichen Wesenheit: der physische Leib.",
      "Wir wissen, daß dieser in bezug auf seine Stoffe und Gesetze dem Menschen mit der ganzen übrigen leblosen Welt gemeinsam ist. Wir wissen aber auch, daß dieser physische Körper aufgerufen wird zum Leben durch das, was wir den sogenannten Äther- oder Lebensleib nennen; und wir wissen dies, weil für die geistige Forschung dieser Lebensleib nicht eine Spekulation, sondern eine Wirk­lichkeit ist, die erschaut werden kann, wenn der Mensch die höheren Sinne, die in ihm schlummern, in sich eröffnet hat.",
      "Wir betrachten den zweiten Teil der menschlichen Wesen­heit, den Atherleib, als etwas, was der Mensch gemein­schaftlich hat mit der übrigen Pflanzenwelt. Als das dritte Glied der menschlichen Wesenheit betrachten wir den Astral­leib, den Träger von Lust und Unlust, von Begierde und Leidenschaft, den der Mensch mit der Tierheit gemeinsam hat.",
      "Und dann sehen wir, daß des Menschen Selbstbewußt­sein, die Möglichkeit, zu sich « Ich» zu sagen, die Krone der Menschennatur ist, die er mit keinem anderen Wesen ge­meinsam hat; daß dieses Ich als die Blüte der drei Leiber, des physischen, Ather- und Astralleibes hervorgeht. So sehen wir einen Zusammenhang dieser vier Glieder, auf welchen die Geistesforschung immer hingewiesen hat.",
      "Die pythagoräische Vierheit ist nichts anderes als diese Vierheit:",
      "physischer Leib, Atherleib, Astralleib und Ich. Diejenigen, die sich tiefer mit Theosophie beschäftigt haben, wissen, daß",
      "dieses Ich aus sich selber herausarbeitet, was wir das Geist­selbst oder Manas, den Lebensgeist oder Buddhi und den eigentlichen Geistmenschen oder Atma nennen.",
      "Das sei noch einmal vor Sie hingestellt, damit wir uns in richtiger Weise orientieren können. Dem Geistesforscher erscheint also der Mensch als ein viergliedriges Wesen. Nun kommt der Punkt, wo sich die wahre Geistesforschung, die mit den Augen des Geistes hinter die Wesenheiten sieht, die eindringt in die tiefen Gründe des Daseins, tief unter­scheidet von einer rein äußerlichen Betrachtungsweise der Dinge. Zwar sagen wir auch, so wie der Mensch jetzt vor uns steht, müssen chemische und physikalische Gesetze die Grundlage des Leibes, des Lebens, die Grundlage der Emp­findung, des Bewußtseins, die Grundlage des Selbstbewußt­seins werden. Wenn wir aber geisteswissenschaftlich auf das Wesen eingehen, stellt sich uns die Sache gerade umgekehrt dar. Was sich uns im Sinne der Erscheinung als das Letzte darstellt, das Bewußtsein, das sich heraushebt aus dem physischen Leib, das erscheint uns als das ursprünglich Schöpferische. Auf dem Grunde von allem erblicken wir den bewußten Geist, und deshalb erkennt der Geistesfor­scher, wie unsinnig die Frage ist: woher kommt der Geist? Das kann nie die Frage sein; es kann lediglich gefragt wer­den: woher kommt die Materie? Die Materie aber ist für die Geistesforschung aus dem Geiste entsprungen, ist nichts als verdichteter Geist.",
      "Ein Gleichnis: Denken Sie sich ein Gefäß mit Wasser. Dieses Wasser denken Sie sich in einem seiner Teile ab­gekühlt, bis es zu Eis erstarrt. Was ist nun das Eis? Eis ist Wasser, Wasser in anderer Form, in festem Zustande. So sieht der Geistesforscher auch die Materie an. Wie das Was­ser sich zum Eis verhält, so verhält sich der Geist zur Ma­terie. Wie das Eis nichts anderes ist als ein Ergebnis des",
      "Wassers, so ist die Materie nichts anderes als ein Ergebnis des Geistes, und wie Eis wieder zu Wasser werden kann, so kann der Geist wieder seinen Ursprung nehmen aus der Materie, kann wieder aus der Materie hervorgehen oder umgekehrt, die Materie kann sich wieder in Geist auflösen.",
      "So sehen wir einen ewigen Kreislauf des Geistes. Wir sehen den Geist, der das ganze Universum durchflutet, wir sehen aus ihm heraus die materiellen Wesenheiten ent­stehen, die sich verdichten, und wir sehen wieder auf der anderen Seite Wesenheiten, die das Feste wieder verflüch­tigen. In allem, was uns heute als Materielles umgibt, ist etwas, in das der Geist hineingeflossen und darin erstarrt ist. So sehen wir in jeglichem materiellen Wesen erstarrten Geist. So wie wir dem Eise nur die nötige Wärme zuzu­führen brauchen, um wieder Wasser entstehen zu lassen, so brauchen wir den Wesen um uns herum nur den nötigen Geist zuzuführen, um in ihnen den Geist erstehen zu lassen. Wir sprechen von einer Wiedergeburt des Geistes, der in die Materie hineingeflossen und darin erstarrt ist. So erscheint uns auch der astralische Leib - der Träger. von Lust und Unlust, Begierde und Leidenschaft - nicht als etwas, was aus dem physischen Dasein hervorgehen konnte, sondern als dasselbe Element, das in uns auflebt als bewußter Geist, wie das, was uns erscheint als das die ganze Welt durch­flutende Element, welches - durch einen Prozeß des mensch­lichen Lebens - wieder aus der Materie erlöst wird. Das, was als Letztes erscheint, ist zu gleicher Zeit das Erste. Es hat den physischen Leib und ebenso den Ätherleib hervor­gebracht und erscheint, wenn beide in ihrer Entwicklung auf einer gewissen Höhe angelangt sind, aus ihnen heraus aufs neue geboren.",
      "So sieht die Geistesforschung die Dinge an. Nun erschei­nen uns diese drei Glieder - Worte sollen uns nur zur Klärung",
      "dienen - unter drei bestimmten Namen am allerbesten. Die Materie nehmen wir wahr in gewisser Form, sie er­scheint uns in der Außenwelt in bestimmter Weise. Wir sprechen von der Form, von der Gestalt der Materie und von dem Leben, das in der Gestalt erscheint, und endlich von dem Bewußtsein, das innerhalb des Lebens erscheint. So sprechen wir, wie von den drei Stufen: physischer Leib, Ätherleib und Astralleib, auch von den drei Stufen: Form, Leben und Bewußtsein. In dem Bewußtsein entspringt erst das Selbstbewußtsein. Das soll uns indessen heute nicht beschäftigen, mehr das nächste Mal.",
      "Seit jeher und auch besonders in unserer Zeit hat man viel darüber nachgedacht, was das Leben eigentlich bedeutet, was der Ursprung und der Sinn des Lebens sei. Wenige Anhalts­punkte hat die heutige Naturwissenschaft über die Bedeu­tung des Lebens und über sein Wesen erkunden können. Aber eines hat sich diese neue Naturwissenschaft schon seit län­gerer Zeit zu eigen gemacht, was auch die Geistesforschung immer wieder als ihre Überzeugung und ihre Erkenntnis ausgesprochen hat, nämlich: Leben innerhalb der physi­schen Welt unterscheidet sich stofflich von dem sogenannten Nichtleben, dem Leblosen, im Grunde nur durch die Mannig­faltigkeit und Kompliziertheit der Gestaltung. Nur da kann das Leben wohnen, wo eine viel kompliziertere Gestaltung der Stoffe eintritt, als sie im Gebiete des Leblosen vorhan­den ist. Sie wissen vielleicht, daß das Leben zu seiner Grund-substanz etwas hat, was man als eiweißartige Substanz be­zeichnen könnte, für die der Ausdruck «lebendiges Eiweiß» nicht unangebracht wäre. Dieses lebendige Eiweiß unter­scheidet sich vom toten leblosen Eiweiß ganz beträchtlich durch eine Eigenschaft. Lebendiges Eiweiß zerfällt nämlich sogleich, wenn es vom Leben verlassen ist. Totes Eiweiß, zum Beispiel das vom toten Hühnerei, können Sie nicht längere",
      "Zeit in dem Zustande erhalten, in dem es ist. Das ist über­haupt die Eigenart der lebendigen Substanz, daß in dem Augenblick, wo das Leben von ihr gewichen ist, sie ihre Teile nicht mehr zusammenhalten kann. Wenn wir uns auch heute nicht weiter auf das Wesen des Lebens einlassen kön­nen, so kann uns doch schon eine Erscheinung hinweisen auf etwas, was tief mit dem Leben zusammenhängt und es charakterisiert. Und was ist nun dieses Charakteristische? Es ist eben diese Eigenschaft der lebendigen Substanz, daß sie zerfällt, wenn das Leben aus ihr gewichen ist. Denken Sie sich eine Substanz vom Leben entblößt: sie zerfällt; denken Sie sich eine stoffliche Mannigfaltigkeit, die nicht von Leben durchdrungen ist: sie hat die Eigenschaft, zu zerfallen. Was tut nun das Leben? Es stellt sich immer und immer wieder dem Zerfall entgegen; also das Leben erhält. Das ist das Verjüngende des Lebens, daß es sich dem, was in seiner Materie vorgehen würde, immer wieder widersetzt. Leben in der Substanz heißt: Widerstand gegen den Zerfall. Vergleichen Sie den äußeren Vorgang des Todes mit dem Leben, und es wird Ihnen klar sein, daß das Leben alles das nicht zeigt, was den Vorgang des Todes, das In-sich-selbst-Zerfallen, charakterisiert, sondern daß es vielmehr die Substanz immer wieder vor dem Zerfall errettet, sich ihrem Zerfall entgegenstellt. So ist das Leben, indem es die in sich selbst zerfallende Substanz wieder erneuert, die Grundlage des physischen Daseins und des Bewußtseins.",
      "Nicht eine bloße Worterklärung haben wir damit ge­geben. Eine Worterklärung wäre es, wenn sich das, was sie bedeutet, nicht fortwährend zutragen würde. Sie brauchen aber nur eine lebendige Substanz zu betrachten, so werden Sie finden, daß sie fortwährend von außen Stoff aufnimmt, sich ihn einverleibt, indes Teile von ihr vernichtet werden:",
      "ein Prozeß, durch den das Leben fortwährend der Vernichtung",
      "entgegenarbeitet. Wir haben es also mit einer Wirklichkeit zu tun.",
      "Alte Materie absondern und neue wieder bilden, das ist Leben. Leben ist aber noch nicht Empfindung und noch nicht Bewußtsein. Es ist eine kindliche Vorstellungsart man­cher Wissenschaftler, die sie den Begriff der Empfindung so wenig richtig fassen läßt, daß sie der Pflanze, der wir Leben zuschreiben müssen, auch Empfindung beimessen.",
      "Wenn man das sagt, weil manche Pflanzen Blätter und Blüten auf einen äußeren Reiz hin schließen, wie wenn sie diesen Reiz empfinden würden, so könnte man auch sagen, das blaue Lackmuspapier, das durch äußeren Reiz gerötet wird, habe Empfindung. Auch chemischen Substanzen könnten wir dann Empfindung zuschreiben, weil sie auf gewisse Ein­flüsse reagieren.",
      "Das genügt aber nicht. Soll Empfindung konstatiert werden, so muß sich der Reiz im Innern spie­geln. Erst dann können wir von dem ersten Element des Bewußtseins, von der Empfindung sprechen. Und was ist dieses erste Element des Bewußtseins?",
      "Wenn wir uns in der Welterforschung auf die nächsthöhere Stufe erheben und das Wesen des Bewußtseins zu erfassen suchen, so werden wir es zwar nicht gleich erkennen, aber es doch ein wenig in der Seele leuchten spüren, ebenso wie wir auch das Wesen des Lebens ein wenig erklären konnten. Wo Leben ist, kann allein Bewußtsein entstehen, nur aus dem Leben heraus kann Bewußtsein entspringen.",
      "Entspringt das Leben aus der scheinbar leblosen Materie, indem die Zusammenset­zung der Materie so kompliziert wird, daß sie sich selbst nicht erhalten kann und vom Leben ergriffen werden muß, um ihren Zerfall fortwährend zu verhindern, so erscheint uns das Bewußtsein innerhalb des Lebens als etwas Höhe­res. Da, wo das Leben fortwährend als Leben vernichtet wird, wo fortwährend ein Wesen hart an der Grenze",
      "zwischen Leben und Tod steht, wo fortwährend das Leben wieder aus der lebendigen Substanz zu verschwinden droht, da entsteht das Bewußtsein. Und wie zuerst die Substanz zerfallen ist, wenn das Leben sie nicht bewohnte, so scheint uns jetzt das Leben zu zerfallen, wenn nicht als neues Prin­zip das Bewußtsein hinzuträte. Das Bewußtsein kann nicht anders begriffen werden als indem wir sagen: so wie das Leben dazu da ist, gewisse Vorgänge zu erneuern, deren Fehlen den Zerfall der Materie herbeiführen würde, so ist das Bewußtsein dazu da, das Leben, das sich sonst auflösen würde, immer wieder zu erneuern.",
      "Nicht jedes Leben kann sich auf diese Weise innerlich immerfort erneuern. Es muß auf einer höheren Stufe an­gekommen sein, wenn es sich aus sich selbst erneuern soll. Nur dasjenige Leben kann zum Bewußtsein erwachen, wel­ches in sich selbst so stark ist, daß es fortwährend den Tod in sich verträgt. Oder gibt es ein solches Leben nicht, das in jedem Augenblick den Tod in sich selbst hat? Sie brauchen nur das Menschenleben anzusehen und sich zu erinnern an das, was im letzten Vortrage unter dem Titel «Blut ist ein ganz besonderer Saft» gesagt worden ist. Aus dem Blute erneuert sich fortwährend das menschliche Leben, und ein geistvoller deutscher Seelenkundiger hat gesagt, im Blute hat der Mensch einen Doppelgänger, aus dem er fortwäh­rend Kraft zieht. Aber auch eine andere Kraft hat das Blut noch: es erzeugt fortwährend aus sich selbst den Tod. Wenn das Blut die lebenerweckenden Stoffe an die Körperorgane abgesetzt hat, dann führt es die lebenzerstörenden Kräfte wieder herauf zum Herzen und in die Lungen. Was in die Lungen zurückfließt, ist für das Leben Gift, ist das, was das Leben fortwährend ersterben macht.",
      "Wenn ein Wesen dem Zerfall entgegenarbeitet, dann ist es ein lebendiges Wesen. Ist es imstande, in sich selbst den",
      "Tod erstehen zu lassen und diesen Tod fortwährend zum Leben umzuwandeln, dann entsteht Bewußtsein. Das Be­wußtsein ist die stärkste von allen Kräften, die uns ent­gegentreten. Bewußtsein oder bewußter Geist ist diejenige Kraft, welche ewig aus dem Tode, der inmitten des Lebens erzeugt werden muß, das Leben wieder erstehen läßt. Leben ist ein Prozeß, der es zu tun hat mit einer Außenwelt und einer Innenwelt; Bewußtsein aber ist ein Prozeß, der es nur mit einer Innenwelt zu tun hat. Eine Substanz, die nach außen hin sterben kann, kann nicht bewußt werden. Bewußt kann nur eine solche Substanz sein, die in ihrem eigenen Mittelpunkt den Tod erzeugt und überwindet. So ist der Tod - wie ein deutscher geistvoller Theosoph gesagt hat - nicht nur die Wurzel des Lebens, sondern auch die Wurzel des Bewußtseins.",
      "Wenn wir diesen Zusammenhang begriffen haben, dann brauchen wir nur mit offenen Augen die Erscheinungen anzusehen, und der Schmerz wird uns begreiflich erschei­nen. Alles das, womit das Bewußtsein beginnt, ist ursprüng­lich Schmerz. Wenn das Leben sich nach außen öffnet, wenn einer lebendigen Wesenheit Licht, Luft, Hitze, Kälte ent­gegentreten, dann wirken diese äußeren Elemente zunächst auf das lebendige Wesen. Solange diese Elemente aber nur auf dieses lebendige Wesen wirken, solange sie von diesem lebendigen Wesen aufgenommen werden, wie sie von der Pflanze als Träger von inneren Lebensvorgängen aufge­nommen werden, solange entsteht kein Bewußtsein. Be­wußtsein entsteht erst dann, wenn diese äußeren Elemente in Widerspruch treten mit dem inneren Leben, wenn eine Zerstörung stattfindet. Aus der Zerstörung des Lebens muß das Bewußtsein erfließen. Ohne teilweisen Tod wird ein Lichtstrahl in ein lebendiges Wesen nicht eindringen kön­nen, wird in dem lebendigen Wesen nie der Vorgang angeregt",
      "werden können, aus dem das Bewußtsein entspringt. Wenn aber das Licht in die Oberfläche des Lebens eindringt, dann eine teilweise Verwüstung anrichtet, die inneren Stoffe und Kräfte niederreißt, dann entsteht jener geheimnisvolle Vorgang, der sich überall in der Außenwelt in ganz be­stimmter Weise abspielt.",
      "Stellen Sie sich vor: Die intelli­genten Kräfte der Welt wären zu einer Höhe emporgestie­gen, daß das äußere Licht und die äußere Luft ihnen fremd geworden wären. Nur eine Zeitlang blieben sie mit ihnen in Einklang, dann vervollkommneten sie sich selbst, wo­durch ein Widerspruch entstand.",
      "Könnten Sie mit den Augen des Geistes diesen Vorgang verfolgen, so könnten Sie sehen, wie da, wo sich in einfache Wesen ein Lichtstrahl eindrängt, die Haut etwas umgestaltet wird und ein win­ziges Auge entsteht. Was ist es nun, was da in der Materie zuerst aufdämmert?",
      "In was drückt sich diese feine Zer­störung aus, denn eine Zerstörung ist es, was dabei vor sich geht? Es ist der Schmerz, der nichts als ein Ausdruck für diese Zerstörung ist. Überall, wo das Leben der äußeren Natur entgegentritt, findet Zerstörung statt, die, wenn sie größer wird, selbst den Tod hervorbringt.",
      "Aus dem Schmerz wird das Bewußtsein geboren. Derselbe Prozeß, der Ihr Auge geschaffen hat, wäre ein Zerstörungsprozeß gewor­den, wenn er an dem Wesen, das sich in dem menschlichen Wesen heraufentwickelt hat, überhand genommen hätte.",
      "So hat er aber nur einen kleinen Teil ergriffen, wodurch er aus der Zerstörung, aus dem partiellen Tod heraus jene Spiege­lung der Außenwelt schaffen konnte, die man das Bewußt­sein nennt. Das Bewußtsein innerhalb der Materie wird also aus dem Leide, aus dem Schmerz geboren.",
      "Wenn wir diesen Zusammenhang zwischen Leid und Schmerz und dem bewußten Geist, der uns umgibt, einsehen, dann verstehen wir wohl auch ein Wort eines christlichen",
      "Eingeweihten, der solche Dinge gründlich intuitiv wußte und auf dem Grunde von allem bewußten Leben den Schmerz sah, das Wort: «In aller Natur seufzet jede Krea­tur in Schmerzen, erwartungsvoll, die Gotteskindschaft zu erlangen.» Das finden Sie im 8. Kapitel des Paulus, als eine wunderbare Ausprägung dieser Grundlage des Bewußtseins im Schmerz.",
      "So kann man es auch verstehen, wie bedeu­tende, sinnige Menschen dem Schmerze eine so große, um­fassende Rolle zugeschrieben haben. Nur ein Beispiel möchte ich hier anführen. Ein großer deutscher Philosoph sagt, wenn man die ganze Natur um sich herum ansieht, so er­scheint einem überall auf ihrem Antlitz der Schmerz, das Leid ausgedrückt, ja, wenn man die höheren Tiere ansieht, so zeigen sie dem tiefer Blickenden einen leidensvollen Ausdruck.",
      "Und wer wollte nicht zugeben, daß manche Tier­physiognomie aussieht wie der Ausdruck eines tief verhal­tenen Schmerzes? Wenn wir die Sache so ansehen, wie wir das eben angedeutet haben, dann sehen wir die Entstehung des Bewußtseins aus dem Schmerze, so daß das Wesen, das aus der Zerstörung heraus Bewußtsein bildet, aus dem Ver­fall des Lebens heraus ein Höheres erstehen läßt, aus dem Tode heraus fortwährend sich selbst erschafft.",
      "Wenn das Lebendige nicht leiden könnte, niemals könnte das Bewußt­sein entstehen. Wenn der Tod nicht in der Welt wäre, nie­mals könnte in der sichtbaren Welt der Geist existieren. Das ist die Stärke des Geistes, daß er die Zerstörung in etwas noch Höheres, als das Leben ist, umschafft und so mitten im Leben ein Höheres, ein Bewußtsein bildet.",
      "Im­mer weiter und weiter sehen wir dann die verschiedenen Schmerzerlehnisse zu den Organen des Bewußtseins sich entwickeln. Man sieht es schon bei den Tieren, die zur Ab­wehr nach außen nur ein Reflexbewußtsein haben, ähnlich wie der Mensch, wenn Gefahr für das Auge besteht, dasselbe",
      "schließt. Wenn die Reflexbewegung nicht mehr genügt, das innere Leben zu schonen, wenn der Reiz zu stark wird, so erhebt sich die innere Widerstandskraft und gebiert die Sinne, die Empfindung, Auge und Ohr. Sie wissen vielleicht aus mancher unliebsamen Erfahrung heraus, vielleicht auch instinktiv, daß die Sache so ist. Ja, Sie wissen aus einer höheren Stufe Ihres Bewußtseins ganz genau, daß das, was jetzt gesagt worden ist, eine Wahrheit ist. Ein Beispiel wird die Sache noch verdeutlichen. Wann fühlen Sie gewisse innere Organe Ihres Organismus? Sie gehen durchs Leben und fühlen weder Ihren Magen, noch Ihre Leber, noch Ihre Lunge, Sie fühlen keines Ihrer Organe, solange sie gesund sind. Sie fühlen sie nur dann, wenn sie Sie schmer­zen, und Sie wissen eigentlich erst, daß Sie dieses oder jenes Organ haben, wenn es Sie schmerzt, wenn Sie empfinden, daß da etwas nicht in Ordnung ist, daß ein Zerstörungs­prozeß beginnt.",
      "Wenn wir dieses Beispiel, diese Erklärung nehmen, dann sehen wir, daß aus dem Schmerz fortwährend bewußtes Leben geboren wird. Tritt der Schmerz zum Leben, so ge­biert er die Empfindung und das Bewußtsein. Dieses Ge­bären, dieses Hervorbringen eines Höheren, spiegelt sich wiederum im Bewußtsein als die Lust, und es gab nie eine Lust, ohne daß es vorher einen Schmerz gegeben hätte. Unten in dem Leben, das sich eben aus der physischen Ma­terie heraus erhebt, gibt es noch keine Lust. Wenn aber der Schmerz Bewußtsein hat erstehen lassen und als Bewußt­sein schöpferisch weiterwirkt, dann ist diese Schöpfung auf einer höheren Stufe und drückt sich im Gefühle der Lust aus. Dem Schaffen liegt die Lust zugrunde. Lust kann nur da sein, wo innerliches oder äußerliches Schaffen möglich ist. Irgendwie liegt einer jeden Lust das Schaffen zugrunde, wie jeder Unlust die Notwendigkeit des Schaffens zugrunde",
      "liegt. Nehmen Sie etwas, was auf niederer Stufe das Leid charakterisieren kann, zum Beispiel das Gefühl des Hun­gers, der das Leben zerstören kann. Dem treten Sie mit der Nahrung entgegen. Die Nahrungsaufnahme wird zum Ge­nuß, weil die Nahrung in der Lage ist, in eine Lebenssteige­rung, in eine Lebensproduktion überzugehen. So sehen Sie, daß auf Grundlage des Schmerzes höheres Schaffen, Lust entsteht. Eher als die Lust ist also das Leid. Daher kann auch die Philosophie Schopenhauers und die Eduard von Hartmanns mit Recht sagen, daß das Leid eine allgemeine Lebensempfindung sei. Sie gehen aber nicht tief genug auf den Ursprung des Leides zurück, kommen nicht auf den Punkt, wo sich das Leid zu etwas Höherem entwickeln soll. Der Ursprung des Leides wird da gefunden, wo aus dem Leben Bewußtsein entsteht, wo Geist aus dem Leben herausgeboren wird.",
      "So können wir jetzt auch begreifen, was dem Menschen in der Seele dämmert von dem Zusammenhang zwischen Leid und Schmerz und Erkenntnis und Bewußtsein, so konnten wir noch nachweisen, wie aus Schmerz und Leid ein Edleres, Vollkommeneres herausgeboren wird.",
      "Diejenigen, welche meine Vorträge öfter gehört haben, werden sich auf die Hinweise entsinnen, daß es etwas gibt wie eine Einweihung, wobei ein höheres Bewußtsein vor­handen ist und wobei der Mensch sich von den sinnlichen Dingen zu der Anschauung einer geistigen Welt erhebt, daß Kräfte und Fähigkeiten in der menschlichen Seele schlum­mern, die aus der Seele herausgeholt werden können wie die Sehkraft aus dem Blindgeborenen durch die Operation, daß dann gleichsam ein neuer Mensch ersteht, dem die ganze Welt auf höherer Stufe wie verwandelt erscheint. Wie dem Blindgeborenen nach der Operation, so erscheinen dem gei­stig Geborenen die Dinge in neuem Licht. Aber auch dies",
      "kann nur geschehen, indem derselbe Prozeß, der eben ge­nannt worden ist, sich auf einer höheren Stufe wiederholt. Wenn das, was Sie beim Durchschnittsmenschen vereint finden, getrennt wird, wenn eine Art Zerstörungsprozeß in der niederen Menschennatur auftritt, dann kann dieses höhere Bewußtsein, dieses Schauen in der geistigen Welt, eintreten.",
      "Drei Kräfte gibt es in der menschlichen Natur: Denken, Fühlen und Wollen. Diese drei Kräfte hängen an der physi­schen Menschenorganisation. Gewisse Willensakte treten auf, nachdem gewisse Denk- und Gefühlsvorgänge statt-gefunden haben. Der Organismus des Menschen muß in richtiger Weise funktionieren, wenn diese drei Kräfte zu­sammenstimmen sollen. Sind gewisse Leitungen unterbro­chen, gewisse Teile erkrankt, dann herrscht keine richtige Harmonie zwischen Denken, Fühlen und Wollen. Der Mensch ist dadurch, daß die Organe des Wollens gelähmt sind, nicht imstande, seine Gedanken in Willensimpulse umzusetzen. Er ist schwach als Tatmensch, er kann zwar gut denken, aber sich nicht entschließen, einen Gedanken in Wirklichkeit umzusetzen. Eine andere Art ist die, wo der Mensch nicht imstande ist, seine Gefühle durch die Ge­danken richtig lenken zu lassen, die Gefühle in Einklang mit den dahinterstehenden Gedanken zu bringen. Der Tob­süchtige ist im Grunde nichts anderes.",
      "Im Menschen der Gegenwart besteht eine Harmonie zwi­schen Denken, Fühlen und Wollen, in der befindet sich heute ein normal gebildeter Mensch, der einem Leidenden gegenüber in den richtigen Gefühls- und Willenszustand kommt. Dies ist alles richtig für gewisse Stufen der Ent­wicklung. Es ist aber zu beachten, daß sich diese Harmonie im Gegenwartsmenschen unbewußt herstellt. Soll der Mensch aber eingeweiht werden, soll er hineinsehen in die höheren",
      "Welten, dann müssen diese drei Glieder: Denken, Fühlen und Wollen, auseinandergerissen werden. Die Willens- und Gefühlsorgane müssen eine Scheidung erleiden. Der physi­sche Organismus eines Eingeweihten ist daher auch anders als der eines Nichteingeweihten, wenn das die Anatomie auch noch nicht hat nachweisen können. Der Kontakt zwi­schen Denken, Fühlen und Wollen ist unterbrochen. Der Eingeweihte wäre imstande, irgend jemand tief leiden zu sehen, ohne daß sich ein Gefühl in ihm regte, kalt würde er stehenbleiben und es ansehen können. Und warum ist dies so? Es darf sich beim Eingeweihten nichts unbewußt inein­andergliedern, er ist aus Freiheit ein mitleidsvoller Mensch und nicht, weil ihn etwas Äußeres dazu zwingt. Das ist der Unterschied zwischen einem Eingeweihten und einem Nicht-eingeweihten. Ein solches höheres Bewußtsein schafft gleich­sam eine höhere Substanz, und der Mensch zerfällt in einen Gefühls-, einen Willens- und einen Denkmenschen. Über diesen dreien ihront dann erst der höhere, neugeborene Mensch, und von dieser Stufe eines höheren Bewußtseins aus werden dann jene drei in Einklang gebracht. Hier muß dann auch wieder der Tod, die Zerstörung eingreifen. Träte diese Zerstörung so ein, daß nicht zugleich auch ein neues Bewußtsein entsproßte, dann würde Wahnsinn entstehen. Wahnsinn würde also nichts anderes sein als der Zustand, in dem das menschliche Wesen zerschellt ist, ohne daß die höhere, bewußte Instanz geschaffen worden ist.",
      "So tritt auch hier wieder ein Doppeltes ein: eine Art Zerstörungsprozeß des Niederen neben einem Entstehungs-prozeß des Höheren. Wie im Blute das Gift in den Venen und wie zwischen dem roten und blauen Blut das Bewußt­sein im gewöhnlichen Menschen erzeugt wird, so wird in dem initiierten Menschen wieder in dem Zusammenwirken von Leben und Tod das höhere Bewußtsein im Inneren erzeugt,",
      "und die Seligkeit entspringt wiederum einer höheren Lust, dem Schaffen, das aus dem Tode hervorgeht.",
      "Das ist es, was der Mensch ahnt, wenn er den geheimnis­vollen Zusammenhang spürt zwischen Schmerz und Leid und dem Höchsten, das der Mensch erreichen kann. Deshalb läßt der tragische Dichter aus dem im Leide untergehenden Helden den Sieg des Lebens, das Bewußtsein von dem Siege des Ewigen über das Zeitliche hervorgehen. Deshalb sieht das Christentum mit Recht in dem Untergehen des Christus Jesus - seiner irdischen Natur nach - in Schmerz und Leid, in Qual und Elend den Sieg des ewigen Lebens über die zeitliche Vergänglichkeit. Deshalb auch wird unser Leben rei­cher, inhaltsvoller, wenn wir es erweitern können über das­jenige, was außerhalb unseres Selbstes liegt, wenn wir in dem Leben, das außerhalb unseres Selbstes ist, aufgehen können.",
      "So wie wir aus dem Schmerz, der durch einen äußeren Lichtstrahl angeregt ist und durch uns als lebendige Wesen überwunden wird, ein höheres Bewußtsein schaffen, so wird, wenn wir die Leiden der anderen in unsere eigene, größere Bewußtseinswelt umwandeln, aus der Empfäng­lichkeit für das Leid der anderen ein Schaffen im Mitleid geboren. Und so entsteht endlich aus dem Leide auch die Liebe. Denn was ist die Liebe anderes, als sein Bewußtsein ausdehnen über andere Wesen? Wenn wir selbst soviel ent­behren wollen, soviel ausgeben wollen, uns selbst soviel ärmer machen wollen, als wir dem anderen Wesen geben, und wenn wir imstande sind, geradeso wie die Haut, die den Lichtstrahl empfängt und aus ihrem Schmerz ein höhe­res Wesen, ein Auge zu bilden vermag, wenn wir imstande sind, aus der Verbreitung unseres Lebens über die anderen Leben ein höheres Leben zu saugen, dann wird in uns selbst, aus dem, was wir weggeben an das andere Wesen, die Liebe, das Mitfühlen mit allen Kreaturen geboren.",
      "Das liegt auch dem Ausspruche des griechischen Dichters zugrunde: Aus Leben ward Lehre, aus Lehre Erkennt­nis. Hier berührt sich wiederum, wie im vorigen Vortrage schon gesagt, eine auf neuesten naturwissenschaftlichen For­schungen beruhende Erkenntnis mit den Resultaten der alten Geistesforschung. Immer hat die alte Geistesforschung gesagt, daß höchste Erkenntnis, höchste Lehre nur aus dem Leid hervorgehen kann. Wenn wir ein krankes Glied be­sitzen und Schmerz daran gelitten haben, so kennen wir dieses Glied am allerbesten; ebenso kennen wir das am besten, was wir in der eigenen Seele abgelagert haben. Es quillt aus dem eigenen Leid als dessen Frucht die Er­kenntnis.",
      "Dasselbe liegt auch dem Kreuzestod des Christus Jesus zugrunde, dem, wie aus der christlichen Anschauung her­vorgeht, bald der sich in der Welt ausbreitende Heilige Geist folgte. Wir verstehen also jetzt das Hervorgehen des Heiligen Geistes aus dem Kreuzestod des Christus Jesus als einen Prozeß, auf den durch das Gleichnis vom Weizen-korn hingewiesen wird. Aus der Zerstörung muß die neue Frucht hervorgehen, und so wird auch aus der Zerstörung, aus den Schmerzen, die am Kreuze ertragen worden sind, der Geist, der sich am Pfingstfeste über die Apostel ergießt, geboren. Das wird im Johannes-Evangelium klar aus­gesprochen, wenn gesagt ist: der Geist war noch nicht da, denn der Christus war noch nicht verklärt. Wer das Johannes-Evangelium tiefer. liest, der wird Bedeutungs­volles für sich daraus hervorgehen sehen.",
      "Manchen wird man sagen hören können, daß er die Schmerzen nicht missen möchte, da sie ihm die Erkenntnis gebracht haben. Jeder Gestorbene kann Sie lehren, daß das wahr ist, was ich gesagt habe. Würde der Mensch den Kampf gegen die Zerstörung in sich bis zum wirklichen",
      "Tode führen, wenn nicht der Schmerz, wie ein Wächter des Lebens, fortwährend neben ihm stände? Der Schmerz macht uns aufmerksam darauf, daß wir gegen die Zerstörung des Lebens Vorkehrungen zu treffen haben. Aus dem Schmerze heraus schaffen wir neues Leben. In den Aufzeichnungen eines modernen Naturforschers über die Mimik des Den­kers lesen wir, daß auf dem Antlitz des Denkers etwas liegt wie ein verhaltener Schmerz.",
      "Wenn es sich mit der Erhebung, die aus der durch Schmerz erlangten Erkenntnis fließt, so verhält, wenn es also wahr ist, daß aus Leid Lehre entsteht, dann ist nicht mit Un­recht - wie wir das nächste Mal sehen werden - in der bib­lischen Schöpfungsurkunde die Erkenntnis des Guten und des Bösen mit den Leiden und Schmerzen in Zusammen­hang gebracht. Deshalb ist auch von tiefer Blickenden mit Recht immer wieder betont worden, wie der Ursprung der Läuterung, die Erhöhung der menschlichen Natur, im Schmerz liegt, und wenn die theosophische Weltanschau­ung in dem großen Schicksalsgesetze, Karma, von den Lei­den aus, die ein Mensch im gegenwärtigen Leben erleidet, hindeutet auf das, was er in früheren Leben gesündigt, ver­brochen hat, dann verstehen wir einen solchen Zusammen­hang auch nur aus der tieferen Menschennatur heraus. Das­jenige, was im früheren Leben von uns in der Außenwelt vollführt wurde, verwandelt sich aus wilden in erhabene Kräfte. Die Sünde ist gleichsam wie ein Gift, das aber, wenn es in Substanz des Lebens verwandelt wird, sich zum Heilmittel gestaltet. So kann die Sünde wieder zur Kräf­tigung und Erhöhung des Menschen beitragen, und so stellen sich uns auch in der Erzählung von Hiob die Schmerzen und Leiden als eine Erhöhung der Erkenntnis und des Geistes dar.",
      "Das sollte nur eine Skizze sein, die auf den Zusammenhang",
      "von irdischem Dasein und Leiden und Schmerzen hin­weisen sollte. Sie sollte zeigen, wie wir den Sinn von Leiden und Schmerzen einsehen können, wenn wir sehen, wie sie erstarren, sich kristallisieren in physischen Dingen und Or­ganismen bis zum Menschen, und wie durch ein Verflüssigen des Erstarrten der Geist bei uns wiedergeboren werden kann, wenn wir sehen, daß im Geist der Ursprung des Schmerzes, des Leides ist. Das, was uns der Geist gibt, ist Schönheit, Kraft und Weisheit, das verwandelte Bild der ursprünglichen Stätte des Schmerzes. Deshalb hat nicht mit Unrecht ein geistvoller Mann, Fabre d'Olivet, den Ver­gleich gebraucht, um das Höchste, Edelste, Geläutertste in der Menschennatur in seinem Hervorgehen aus dem Schmerz zu zeigen, daß das Hervorgehen von Weisheit und Schön­heit aus dem Leid vergleichbar ist einem Vorgang draußen in der Natur, dem Geborenwerden der wertvollen, schönen Perle. Denn aus was wird sie geboren? Aus der Krankheit des Muscheltieres, aus der Zerstörung innerhalb der Perl­muschel. Wie die Schönheit der Perle geboren wird aus Krankheit und damit aus Leiden, so wird Erkenntnis, edle Menschennatur und geläuterter Menschensinn aus dem Lei­den, aus dem Schmerz geboren.",
      "So dürfen wir wohl im Einklang mit dem alten griechi­schen Dichter Äschylos sagen: Aus dem Leid entsteht Lehre, aus der Lehre Erkenntnis. Und ebenso wie in bezug auf vieles andere dürfen wir in bezug auf den Schmerz sagen, daß wir ihn erst dann erfaßt haben, wenn wir ihn er­kennen nicht nur an sich selbst, sondern an dem, was aus ihm hervorgeht. Wie so manches andere wird auch der Schmerz nur an seinen Früchten erkannt."
    ],
    "sentences": [
      [
        "Mehr noch als die anderen Vorträge des Winterzyklus hängen die drei nächsten zusammen: der heutige «Über den Ursprung des Leids», der nächste «Über den Ursprung des Bösen» und der folgende «Wie begreift man Krankheit und Tod?», doch wird jeder von diesen drei Vorträgen auch in sich selbst abgeschlossen und verständlich sein."
      ],
      [
        "Wenn der Mensch das Leben rings um sich her betrachtet, wenn er Selbstschau hält und den Sinn und die Bedeutung des Lebens bei sich selbst erforschen will, dann findet er einen eigentümlichen, zum Teil warnenden, zum Teil ganz rätselvollen Wächter vor dem Tore dieses Lebens stehen: das Leid."
      ],
      [
        "Das Leiden, das seinerseits wiederum eng verbunden ist mit dem, was wir in den nächsten Vorträgen betrachten wollen, mit dem Bösen, mit Krankheit und Tod, erscheint dem Menschen manchmal als etwas, was so tief ins Leben eingreift, daß es mit den allerhöchsten Fragen des Lebens zusammenzuhängen scheint.",
        "Daher ist die Frage nach dem Leide eine der wesentlichsten aller Weltanschauungen seit den ältesten Zeiten des Menschengeschlechts, und immer, wenn man versuchte, den Wert des Lebens abzuschätzen, den Sinn des Lebens zu erkennen, hat man vor allen Dingen erkennen wollen, welche Rolle das Leid, der Schmerz im menschlichen Leben spielt."
      ],
      [
        "Wie ein Störenfried erscheint das Leid mitten im fröh­lichen Leben, es erscheint als eine Herabminderung von Lebenlust und Lebenshoffnung.",
        "Gerade diejenigen, welche"
      ],
      [
        "den Wert des Lebens in der Lebensfreudigkeit suchen, welche nur für die Lebensfreudigkeit da zu sein scheinen, haben diesen Störenfried, Leid und Schmerz, am meisten emp­funden.",
        "Wie wäre es sonst erklärbar, daß bei einem so lebensfrohen, so in Lebensfreudigkeit aufgehenden Volke, wie es die Griechen waren, ein Ausspruch wie ein dunkler Punkt am Sternenhimmel der Schönheit des Griechentums auftaucht, der Ausspruch des weisen Silen im Gefolge des Dionysos: Was ist für den Menschen das Beste?",
        "Das Beste für den Menschen ist, nicht geboren zu sein, und ist er einmal geboren, so ist das Zweitbeste, bald nach der Geburt zu sterben. - Vielleicht wissen Sie, daß Friedrich Nietzsche, als er die Geburt der Tragödie aus dem Geiste des alten Grie­chentums zu begreifen suchte, an diesen Spruch anknüpfte, um zu zeigen, wie auf dem Grunde griechischer Lebensweis­heit und griechischer Kunst das Leid und die Betrübnis des Menschen über das Leid und über das, was damit zusam­menhängt, eine bedeutungsvolle Rolle spielt."
      ],
      [
        "Nun aber finden wir auch einen anderen und kaum viel jüngeren Satz aus dem Griechentum, einen kurzen Aus­spruch, der uns zu gleicher Zeit zeigt, wie in einer gewissen Art wiederum aus diesem alten Griechentum heraus eine Erkenntnis aufdämmert, daß das Leiden und die Schmerzen der Welt doch nicht bloß eine verhängnisvolle Rolle spielen.",
        "Es ist der Ausspruch, den wir bei einem der ältesten grie­chischen Tragiker, bei Äschylos finden, daß aus Leiden Er­kenntnis erwächst.",
        "Da werden zwei Dinge zusammenge­bracht, von denen zweifellos ein großer Teil der Menschheit das eine aus dem Leben hinweggelöscht haben möchte, wäh­rend er das andere, die Erkenntnis, als eines der höchsten Güter des Lebens betrachtet."
      ],
      [
        "Daß das Leben und das Leid, wenigstens das Leben der heutigen Menschen und der höheren Wesen auf unserem"
      ],
      [
        "Erdenrund, tief verflochten sind, hat man von jeher geglaubt einsehen zu müssen.",
        "So stehen nicht nur am Ausgangspunkt des biblischen Schöpfungsmythos Erkenntnis des Guten und Bösen und Leid innig miteinander verbunden, sondern wir sehen auch auf der anderen Seite, mitten aus der Anschauung des Alten Testaments heraus, wie aus einer schwarzen Anschauung des Leidens auch eine helle, licht-volle aufdämmert."
      ],
      [
        "Wenn wir uns im Alten Testament um-sehen, wenn wir den Schöpfungsmythos in bezug auf diese Frage verfolgen, so wird uns klar, daß man innerhalb dieser alten Weltansdiauung Leiden und Sünde zusammenbrachte, daß man Leid als die Folge der Sünde ansah.",
        "Heute, bei der Denkweise, die selbst da, wo man nicht recht will, sich der materialistischen Weltauffassung nähert, begreift man nicht mehr leicht, wie man in der Sünde die Ursache des Leidens suchen kann."
      ],
      [
        "Aber wenn wir Geistesforscher sind und uns in frühere Zeitalter hineindenken lernen, dann werden wir sehen, daß es nicht ganz so unsinnig ist, an einen solchen Zusammenhang zu glauben, und der nächste Vortrag wird uns zeigen, daß es eine Möglichkeit gibt, einen Zusammen­hang zwischen dem Bösen und dem Leid zu sehen.",
        "Das Leid aber aus seinen Ursachen zu erklären, stellte sich für die Anschauung des alten Judentums als eine Unmöglichkeit heraus."
      ],
      [
        "So sehen wir, daß mitten in dieser Anschauung, die Leid und Sünde in Zusammenhang bringt, die merkwür­dige Gestalt des Hiob steht, jene Gestalt, die uns zeigt oder zeigen will, wie Leiden und unsägliche Schmerzen mit einem vollkommen unschuldigen Leben zusammenhängen können, wie es unverdiente Leiden und Schmerzen geben kann.",
        "In dem Bewußtsein dieser eigenartig tragischen Persönlichkeit Hiob sehen wir noch einen anderen Zusammenhang von Leid und Schmerz aufdämmern, einen Zusammenhang mit der Veredlung des Menschen."
      ],
      [
        "Das Leid erscheint uns da als"
      ],
      [
        "eine Prüfung, als Wurzel eines Aufwärtsklimmens, einer Höherentwicklung.",
        "So braucht dieses Leiden im Sinne dieser Hiob -Tragik keineswegs seinen Ursprung im Bösen zu haben, sondern kann selbst erster Ursprung sein, so daß das, was aus ihm hervorgeht, eine vollkommenere Phase menschlichen Daseins, menschlichen Lebens darstellt.",
        "Das alles liegt unserem heutigen, modernen Denken ziemlich fern, und die breitere Masse unseres heutigen gebildeten Publikums kann sich nicht mehr in eine solche Denkweise hineinfinden.",
        "Sie brauchen aber nur in Ihrem Leben etwas zurückzudenken und Sie werden sehen, daß Vollkommen­heit und Leid gar oft auch vor Ihren Augen zusammen­gestellt erschien, und daß es in der Menschheit immer ein Bewußtsein gegeben hat von dem Zusammenhang zwischen Leiden und Vollkommenheit.",
        "Dieses Bewußtsein wird uns hinüberheben zu dem, was wir heute im Sinne der Geistes-forschung zu betrachten haben werden, nämlich den Zu­sammenhang zwischen Leiden und Geistigkeit."
      ],
      [
        "Erinnern Sie sich, wie oft in diesem oder jenem Trauer-spiel der tragische Held vor Ihren Augen gestanden hat.",
        "Durch Leiden und leidensvolle Kämpfe hindurch führt der Dichter immer wieder und wiederum den Helden; und wenn er dann bis zu dem Punkte kommt, wo der Schmerz sich aufs höchste steigert und in dem Ende des physischen Körpers seinen Abschluß findet, dann lebt in der Seele des Zuschauers nicht bloß Mitleid mit dem tragischen Helden, nicht bloß die Betrübnis darüber, daß solche Leiden, wie sie sich eben abgespielt haben, möglich sind, sondern es stellt sich heraus, daß der Mensch vom Anblick des Leidens ge­hoben und erbaut wurde, daß er das Leid hat untergehen sehen im Tode und aus dem Tode heraus sich die Gewißheit ergeben hat, daß es einen Sieg gibt über Schmerzen und Leiden, ja selbst über den Tod.",
        "Durch nichts kann künstlerisch"
      ],
      [
        "dieser höchste Sieg des Menschen, dieser Sieg seiner innersten Kräfte und Triebe, dieser Sieg des edelsten Trie­bes seiner Natur so erhaben vor Augen geführt werden als durch das Trauerspiel.",
        "Wenn dem Bewußtsein dieses Sieges das Erlebnis von Leiden und Schmerzen vorhergegangen ist und wir von solchen Tatsachen, die sich vor den Augen des Zuschauers im Theater immer wieder abspielen können, aufschauen zu dem, was ein großer Teil der heutigen Mensch­heit noch immer als das Höchste aller geschichtlichen Ent­wicklung empfindet, wenn wir aufschauen zu dem Ereignis, das unsere Zeitrechnung in zwei Teile teilt, zu dem Ereig­nisse der Erlösung durch den Christus Jesus, dann kann es uns auffallen, daß eine der größten Erhebungen, eine der größten Erbauungen und Siegeshoffnungen, die jemals im Herzen der Menschen Platz gegriffen haben, aus dem welt-geschichtlichen Anblick des Leides entsprossen ist.",
        "Die gro­ßen, bedeutsamen und tief in das Menschenherz einschnei­denden Empfindungen der christlichen Weltanschauung, jene Empfindungen, die für so viele Menschen Lebenshoff­nung und Lebenskraft sind, die Gewißheit geben, daß es ein Ewiges, daß es einen Sieg über den Tod gibt, alle diese erbauenden und erhebenden Empfindungen entspringen aus der Anschauung eines universellen Leidens, eines Leidens, das die Unschuld trifft, eines Leidens, das durch keine Sünde der eigenen Persönlichkeit herbeigeführt worden ist."
      ],
      [
        "So sehen wir auch hier ein Höchstes im Bewußtsein der Menschheit sich an das Leid anknüpfen.",
        "Und wenn wir so sehen, wie diese Dinge im kleineren und im größeren immer wieder in der Menschheit auftauchen, wie sie geradezu den elementaren Teil der ganzen menschlichen Natur und des ganzen menschlichen Bewußtseins bilden, dann muß es uns doch scheinen, als ob das Leiden irgendwie mit dem Höch­sten im Menschen zusammenhänge."
      ],
      [
        "Nur ein Hinweis sollte das sein auf eine Grundempfin­dung der menschlichen Seele, die sich immer und immer wieder losringt, und die gleichsam wie ein großer Trost dasteht dafür, daß es Leiden gibt.",
        "Wenn wir uns nun noch feiner und intimer in das Menschenleben einleben, so kön­nen sich uns auch Erscheinungen vor die Seele stellen, die uns auf die Bedeutung des Leidens hinweisen.",
        "Wir werden hier symptomatisch auf eine solcheErscheinung hinweisen müssen, die vielleicht kaum damit zusammenzuhängen scheint, wenn wir uns jedoch intimer auf die menschliche Natur einlassen, werden wir sehen, daß auch diese Erscheinung auf die Bedeutung gewisser Seiten des Leides hinweisen wird."
      ],
      [
        "Denken Sie noch einmal an das tragische Kunstwerk, das Trauerspiel, das nur entstehen kann, wenn sich des Dichters Seele weit, weit öffnet, aus sich herausgeht und lernt, frem­des Leid mitzuempfinden, fremdes Leid auf die eigene Seele abzulagern.",
        "Und nun vergleichen Sie diese Empfindung nicht etwa bloß mit dem Lustspiele - da werden wir keinen guten Vergleich herausbekommen -, sondern mit etwas, was in gewisser Weise auch zur.",
        "Kunst gehört: mit der Stimmung, aus der die Karikatur fließt, die vielleicht mit Spott und Hohn dasjenige im Zerrbilde zeigt, was in der Seele des anderen vorgeht und in die äußere Wirksamkeit tritt.",
        "Versuchen wir es, uns zwei Menschen vor die Seele hinzustellen, von denen der eine ein Ereignis oder einen Menschen tragisch ergreift, der andere als Karikatur er­faßt.",
        "Nicht ein bloßer Vergleich, nicht ein bloßes Bild ist es, wenn wir sagen, die Seele des tragischen Dichters und Künstlers erscheint uns, wie wenn sie aus sich herausginge und weiter und weiter würde.",
        "Was aber eröffnet sich ihr durch dieses Weiterwerden?",
        "Das Verständnis des anderen Menschen.",
        "Durch nichts versteht man das Leben des an­deren mehr, als wenn man seinen Schmerz auf die eigene"
      ],
      [
        "Seele ablagern läßt.",
        "Was muß man aber tun, wenn man karikieren will?",
        "Man darf nicht eingehen auf das, was die andere Seele fühlt, man muß sich über sie stellen, sie von sich weisen, und dieses Vonsichweisen ist die Grundlage des Zerrbildes.",
        "Niemand wird leugnen, daß, ebenso wie uns durch das tragische Mitleid die andere Persönlichkeit tief verständlich wird, durch die Karikatur dasjenige vor uns auftritt, was in der Seele der eigenen Persönlichkeit des Karikierenden lebt.",
        "Viel mehr lernen wir die Überlegen­heit, den Witz, das Anschauungsvermögen, die Phantasie des Karikierenden kennen als den, der karikiert wird."
      ],
      [
        "Haben wir so aus gewissen Symptomen heraus anschau­lich gemacht, daß das Leid doch mit etwas Tiefem in der Menschennatur zusammenhängt, so dürfen wir hoffen, daß durch ein Begreifen des eigentlichen Wesens der Menschen-natur uns auch Schmerz und Leid in ihrem Ursprung klar werden können."
      ],
      [
        "Die Geisteswissenschaft, die wir hier zu vertreten haben, geht davon aus, daß alles Dasein um uns herum seinen Ursprung aus dem Geiste genommen hat.",
        "Eine mehr mate­rialistische Anschauung sieht den Geist nur da, wo er wie eine Krone der sinnlichen Schöpfung erscheint, wie eine Blüte, die sich aus der Wurzel des materiellen Daseins her­aushebt.",
        "Diese letztere Anschauung sieht rings um sich das materielle Dasein, die physische Körperwelt sich herauf-organisieren innerhalb der lebenden Wesen, sie sieht das Bewußtsein, die Empfindung entspringen, sieht Lust und Leid innerhalb des Lebens hervorgehen und den Geist aus der Körperlichkeit heraus sich erheben."
      ],
      [
        "Wenn wir so das Leben rings um uns betrachten, so ist auch für die wahre Geistesforschung der Geist, wie er uns in der sinnlichen Welt entgegentritt, zunächst ein Ergebnis der physischen Natur, aus welcher er heraussprießt."
      ],
      [
        "In den zwei letzten Vorträgen wurde dargestellt, wie wir uns im Sinne der Geistesforschung den ganzen Menschen, den physischen oder leiblichen, den seelischen und den geistigen Menschen vorzustellen haben.",
        "Das, was wir mit Augen sehen, mit den Sinnen äußerlich wahrnehmen kön­nen, das, was der Materialismus als das einzige Wesen der Natur betrachtet, ist der Geistesforschung nichts an­deres als das erste Glied der menschlichen Wesenheit: der physische Leib."
      ],
      [
        "Wir wissen, daß dieser in bezug auf seine Stoffe und Gesetze dem Menschen mit der ganzen übrigen leblosen Welt gemeinsam ist.",
        "Wir wissen aber auch, daß dieser physische Körper aufgerufen wird zum Leben durch das, was wir den sogenannten Äther- oder Lebensleib nennen; und wir wissen dies, weil für die geistige Forschung dieser Lebensleib nicht eine Spekulation, sondern eine Wirk­lichkeit ist, die erschaut werden kann, wenn der Mensch die höheren Sinne, die in ihm schlummern, in sich eröffnet hat."
      ],
      [
        "Wir betrachten den zweiten Teil der menschlichen Wesen­heit, den Atherleib, als etwas, was der Mensch gemein­schaftlich hat mit der übrigen Pflanzenwelt.",
        "Als das dritte Glied der menschlichen Wesenheit betrachten wir den Astral­leib, den Träger von Lust und Unlust, von Begierde und Leidenschaft, den der Mensch mit der Tierheit gemeinsam hat."
      ],
      [
        "Und dann sehen wir, daß des Menschen Selbstbewußt­sein, die Möglichkeit, zu sich « Ich» zu sagen, die Krone der Menschennatur ist, die er mit keinem anderen Wesen ge­meinsam hat; daß dieses Ich als die Blüte der drei Leiber, des physischen, Ather- und Astralleibes hervorgeht.",
        "So sehen wir einen Zusammenhang dieser vier Glieder, auf welchen die Geistesforschung immer hingewiesen hat."
      ],
      [
        "Die pythagoräische Vierheit ist nichts anderes als diese Vierheit:"
      ],
      [
        "physischer Leib, Atherleib, Astralleib und Ich.",
        "Diejenigen, die sich tiefer mit Theosophie beschäftigt haben, wissen, daß"
      ],
      [
        "dieses Ich aus sich selber herausarbeitet, was wir das Geist­selbst oder Manas, den Lebensgeist oder Buddhi und den eigentlichen Geistmenschen oder Atma nennen."
      ],
      [
        "Das sei noch einmal vor Sie hingestellt, damit wir uns in richtiger Weise orientieren können.",
        "Dem Geistesforscher erscheint also der Mensch als ein viergliedriges Wesen.",
        "Nun kommt der Punkt, wo sich die wahre Geistesforschung, die mit den Augen des Geistes hinter die Wesenheiten sieht, die eindringt in die tiefen Gründe des Daseins, tief unter­scheidet von einer rein äußerlichen Betrachtungsweise der Dinge.",
        "Zwar sagen wir auch, so wie der Mensch jetzt vor uns steht, müssen chemische und physikalische Gesetze die Grundlage des Leibes, des Lebens, die Grundlage der Emp­findung, des Bewußtseins, die Grundlage des Selbstbewußt­seins werden.",
        "Wenn wir aber geisteswissenschaftlich auf das Wesen eingehen, stellt sich uns die Sache gerade umgekehrt dar.",
        "Was sich uns im Sinne der Erscheinung als das Letzte darstellt, das Bewußtsein, das sich heraushebt aus dem physischen Leib, das erscheint uns als das ursprünglich Schöpferische.",
        "Auf dem Grunde von allem erblicken wir den bewußten Geist, und deshalb erkennt der Geistesfor­scher, wie unsinnig die Frage ist: woher kommt der Geist?",
        "Das kann nie die Frage sein; es kann lediglich gefragt wer­den: woher kommt die Materie?",
        "Die Materie aber ist für die Geistesforschung aus dem Geiste entsprungen, ist nichts als verdichteter Geist."
      ],
      [
        "Ein Gleichnis: Denken Sie sich ein Gefäß mit Wasser.",
        "Dieses Wasser denken Sie sich in einem seiner Teile ab­gekühlt, bis es zu Eis erstarrt.",
        "Was ist nun das Eis?",
        "Eis ist Wasser, Wasser in anderer Form, in festem Zustande.",
        "So sieht der Geistesforscher auch die Materie an.",
        "Wie das Was­ser sich zum Eis verhält, so verhält sich der Geist zur Ma­terie.",
        "Wie das Eis nichts anderes ist als ein Ergebnis des"
      ],
      [
        "Wassers, so ist die Materie nichts anderes als ein Ergebnis des Geistes, und wie Eis wieder zu Wasser werden kann, so kann der Geist wieder seinen Ursprung nehmen aus der Materie, kann wieder aus der Materie hervorgehen oder umgekehrt, die Materie kann sich wieder in Geist auflösen."
      ],
      [
        "So sehen wir einen ewigen Kreislauf des Geistes.",
        "Wir sehen den Geist, der das ganze Universum durchflutet, wir sehen aus ihm heraus die materiellen Wesenheiten ent­stehen, die sich verdichten, und wir sehen wieder auf der anderen Seite Wesenheiten, die das Feste wieder verflüch­tigen.",
        "In allem, was uns heute als Materielles umgibt, ist etwas, in das der Geist hineingeflossen und darin erstarrt ist.",
        "So sehen wir in jeglichem materiellen Wesen erstarrten Geist.",
        "So wie wir dem Eise nur die nötige Wärme zuzu­führen brauchen, um wieder Wasser entstehen zu lassen, so brauchen wir den Wesen um uns herum nur den nötigen Geist zuzuführen, um in ihnen den Geist erstehen zu lassen.",
        "Wir sprechen von einer Wiedergeburt des Geistes, der in die Materie hineingeflossen und darin erstarrt ist.",
        "So erscheint uns auch der astralische Leib - der Träger. von Lust und Unlust, Begierde und Leidenschaft - nicht als etwas, was aus dem physischen Dasein hervorgehen konnte, sondern als dasselbe Element, das in uns auflebt als bewußter Geist, wie das, was uns erscheint als das die ganze Welt durch­flutende Element, welches - durch einen Prozeß des mensch­lichen Lebens - wieder aus der Materie erlöst wird.",
        "Das, was als Letztes erscheint, ist zu gleicher Zeit das Erste.",
        "Es hat den physischen Leib und ebenso den Ätherleib hervor­gebracht und erscheint, wenn beide in ihrer Entwicklung auf einer gewissen Höhe angelangt sind, aus ihnen heraus aufs neue geboren."
      ],
      [
        "So sieht die Geistesforschung die Dinge an.",
        "Nun erschei­nen uns diese drei Glieder - Worte sollen uns nur zur Klärung"
      ],
      [
        "dienen - unter drei bestimmten Namen am allerbesten.",
        "Die Materie nehmen wir wahr in gewisser Form, sie er­scheint uns in der Außenwelt in bestimmter Weise.",
        "Wir sprechen von der Form, von der Gestalt der Materie und von dem Leben, das in der Gestalt erscheint, und endlich von dem Bewußtsein, das innerhalb des Lebens erscheint.",
        "So sprechen wir, wie von den drei Stufen: physischer Leib, Ätherleib und Astralleib, auch von den drei Stufen: Form, Leben und Bewußtsein.",
        "In dem Bewußtsein entspringt erst das Selbstbewußtsein.",
        "Das soll uns indessen heute nicht beschäftigen, mehr das nächste Mal."
      ],
      [
        "Seit jeher und auch besonders in unserer Zeit hat man viel darüber nachgedacht, was das Leben eigentlich bedeutet, was der Ursprung und der Sinn des Lebens sei.",
        "Wenige Anhalts­punkte hat die heutige Naturwissenschaft über die Bedeu­tung des Lebens und über sein Wesen erkunden können.",
        "Aber eines hat sich diese neue Naturwissenschaft schon seit län­gerer Zeit zu eigen gemacht, was auch die Geistesforschung immer wieder als ihre Überzeugung und ihre Erkenntnis ausgesprochen hat, nämlich: Leben innerhalb der physi­schen Welt unterscheidet sich stofflich von dem sogenannten Nichtleben, dem Leblosen, im Grunde nur durch die Mannig­faltigkeit und Kompliziertheit der Gestaltung.",
        "Nur da kann das Leben wohnen, wo eine viel kompliziertere Gestaltung der Stoffe eintritt, als sie im Gebiete des Leblosen vorhan­den ist.",
        "Sie wissen vielleicht, daß das Leben zu seiner Grund-substanz etwas hat, was man als eiweißartige Substanz be­zeichnen könnte, für die der Ausdruck «lebendiges Eiweiß» nicht unangebracht wäre.",
        "Dieses lebendige Eiweiß unter­scheidet sich vom toten leblosen Eiweiß ganz beträchtlich durch eine Eigenschaft.",
        "Lebendiges Eiweiß zerfällt nämlich sogleich, wenn es vom Leben verlassen ist.",
        "Totes Eiweiß, zum Beispiel das vom toten Hühnerei, können Sie nicht längere"
      ],
      [
        "Zeit in dem Zustande erhalten, in dem es ist.",
        "Das ist über­haupt die Eigenart der lebendigen Substanz, daß in dem Augenblick, wo das Leben von ihr gewichen ist, sie ihre Teile nicht mehr zusammenhalten kann.",
        "Wenn wir uns auch heute nicht weiter auf das Wesen des Lebens einlassen kön­nen, so kann uns doch schon eine Erscheinung hinweisen auf etwas, was tief mit dem Leben zusammenhängt und es charakterisiert.",
        "Und was ist nun dieses Charakteristische?",
        "Es ist eben diese Eigenschaft der lebendigen Substanz, daß sie zerfällt, wenn das Leben aus ihr gewichen ist.",
        "Denken Sie sich eine Substanz vom Leben entblößt: sie zerfällt; denken Sie sich eine stoffliche Mannigfaltigkeit, die nicht von Leben durchdrungen ist: sie hat die Eigenschaft, zu zerfallen.",
        "Was tut nun das Leben?",
        "Es stellt sich immer und immer wieder dem Zerfall entgegen; also das Leben erhält.",
        "Das ist das Verjüngende des Lebens, daß es sich dem, was in seiner Materie vorgehen würde, immer wieder widersetzt.",
        "Leben in der Substanz heißt: Widerstand gegen den Zerfall.",
        "Vergleichen Sie den äußeren Vorgang des Todes mit dem Leben, und es wird Ihnen klar sein, daß das Leben alles das nicht zeigt, was den Vorgang des Todes, das In-sich-selbst-Zerfallen, charakterisiert, sondern daß es vielmehr die Substanz immer wieder vor dem Zerfall errettet, sich ihrem Zerfall entgegenstellt.",
        "So ist das Leben, indem es die in sich selbst zerfallende Substanz wieder erneuert, die Grundlage des physischen Daseins und des Bewußtseins."
      ],
      [
        "Nicht eine bloße Worterklärung haben wir damit ge­geben.",
        "Eine Worterklärung wäre es, wenn sich das, was sie bedeutet, nicht fortwährend zutragen würde.",
        "Sie brauchen aber nur eine lebendige Substanz zu betrachten, so werden Sie finden, daß sie fortwährend von außen Stoff aufnimmt, sich ihn einverleibt, indes Teile von ihr vernichtet werden:"
      ],
      [
        "ein Prozeß, durch den das Leben fortwährend der Vernichtung"
      ],
      [
        "entgegenarbeitet.",
        "Wir haben es also mit einer Wirklichkeit zu tun."
      ],
      [
        "Alte Materie absondern und neue wieder bilden, das ist Leben.",
        "Leben ist aber noch nicht Empfindung und noch nicht Bewußtsein.",
        "Es ist eine kindliche Vorstellungsart man­cher Wissenschaftler, die sie den Begriff der Empfindung so wenig richtig fassen läßt, daß sie der Pflanze, der wir Leben zuschreiben müssen, auch Empfindung beimessen."
      ],
      [
        "Wenn man das sagt, weil manche Pflanzen Blätter und Blüten auf einen äußeren Reiz hin schließen, wie wenn sie diesen Reiz empfinden würden, so könnte man auch sagen, das blaue Lackmuspapier, das durch äußeren Reiz gerötet wird, habe Empfindung.",
        "Auch chemischen Substanzen könnten wir dann Empfindung zuschreiben, weil sie auf gewisse Ein­flüsse reagieren."
      ],
      [
        "Das genügt aber nicht.",
        "Soll Empfindung konstatiert werden, so muß sich der Reiz im Innern spie­geln.",
        "Erst dann können wir von dem ersten Element des Bewußtseins, von der Empfindung sprechen.",
        "Und was ist dieses erste Element des Bewußtseins?"
      ],
      [
        "Wenn wir uns in der Welterforschung auf die nächsthöhere Stufe erheben und das Wesen des Bewußtseins zu erfassen suchen, so werden wir es zwar nicht gleich erkennen, aber es doch ein wenig in der Seele leuchten spüren, ebenso wie wir auch das Wesen des Lebens ein wenig erklären konnten.",
        "Wo Leben ist, kann allein Bewußtsein entstehen, nur aus dem Leben heraus kann Bewußtsein entspringen."
      ],
      [
        "Entspringt das Leben aus der scheinbar leblosen Materie, indem die Zusammenset­zung der Materie so kompliziert wird, daß sie sich selbst nicht erhalten kann und vom Leben ergriffen werden muß, um ihren Zerfall fortwährend zu verhindern, so erscheint uns das Bewußtsein innerhalb des Lebens als etwas Höhe­res.",
        "Da, wo das Leben fortwährend als Leben vernichtet wird, wo fortwährend ein Wesen hart an der Grenze"
      ],
      [
        "zwischen Leben und Tod steht, wo fortwährend das Leben wieder aus der lebendigen Substanz zu verschwinden droht, da entsteht das Bewußtsein.",
        "Und wie zuerst die Substanz zerfallen ist, wenn das Leben sie nicht bewohnte, so scheint uns jetzt das Leben zu zerfallen, wenn nicht als neues Prin­zip das Bewußtsein hinzuträte.",
        "Das Bewußtsein kann nicht anders begriffen werden als indem wir sagen: so wie das Leben dazu da ist, gewisse Vorgänge zu erneuern, deren Fehlen den Zerfall der Materie herbeiführen würde, so ist das Bewußtsein dazu da, das Leben, das sich sonst auflösen würde, immer wieder zu erneuern."
      ],
      [
        "Nicht jedes Leben kann sich auf diese Weise innerlich immerfort erneuern.",
        "Es muß auf einer höheren Stufe an­gekommen sein, wenn es sich aus sich selbst erneuern soll.",
        "Nur dasjenige Leben kann zum Bewußtsein erwachen, wel­ches in sich selbst so stark ist, daß es fortwährend den Tod in sich verträgt.",
        "Oder gibt es ein solches Leben nicht, das in jedem Augenblick den Tod in sich selbst hat?",
        "Sie brauchen nur das Menschenleben anzusehen und sich zu erinnern an das, was im letzten Vortrage unter dem Titel «Blut ist ein ganz besonderer Saft» gesagt worden ist.",
        "Aus dem Blute erneuert sich fortwährend das menschliche Leben, und ein geistvoller deutscher Seelenkundiger hat gesagt, im Blute hat der Mensch einen Doppelgänger, aus dem er fortwäh­rend Kraft zieht.",
        "Aber auch eine andere Kraft hat das Blut noch: es erzeugt fortwährend aus sich selbst den Tod.",
        "Wenn das Blut die lebenerweckenden Stoffe an die Körperorgane abgesetzt hat, dann führt es die lebenzerstörenden Kräfte wieder herauf zum Herzen und in die Lungen.",
        "Was in die Lungen zurückfließt, ist für das Leben Gift, ist das, was das Leben fortwährend ersterben macht."
      ],
      [
        "Wenn ein Wesen dem Zerfall entgegenarbeitet, dann ist es ein lebendiges Wesen.",
        "Ist es imstande, in sich selbst den"
      ],
      [
        "Tod erstehen zu lassen und diesen Tod fortwährend zum Leben umzuwandeln, dann entsteht Bewußtsein.",
        "Das Be­wußtsein ist die stärkste von allen Kräften, die uns ent­gegentreten.",
        "Bewußtsein oder bewußter Geist ist diejenige Kraft, welche ewig aus dem Tode, der inmitten des Lebens erzeugt werden muß, das Leben wieder erstehen läßt.",
        "Leben ist ein Prozeß, der es zu tun hat mit einer Außenwelt und einer Innenwelt; Bewußtsein aber ist ein Prozeß, der es nur mit einer Innenwelt zu tun hat.",
        "Eine Substanz, die nach außen hin sterben kann, kann nicht bewußt werden.",
        "Bewußt kann nur eine solche Substanz sein, die in ihrem eigenen Mittelpunkt den Tod erzeugt und überwindet.",
        "So ist der Tod - wie ein deutscher geistvoller Theosoph gesagt hat - nicht nur die Wurzel des Lebens, sondern auch die Wurzel des Bewußtseins."
      ],
      [
        "Wenn wir diesen Zusammenhang begriffen haben, dann brauchen wir nur mit offenen Augen die Erscheinungen anzusehen, und der Schmerz wird uns begreiflich erschei­nen.",
        "Alles das, womit das Bewußtsein beginnt, ist ursprüng­lich Schmerz.",
        "Wenn das Leben sich nach außen öffnet, wenn einer lebendigen Wesenheit Licht, Luft, Hitze, Kälte ent­gegentreten, dann wirken diese äußeren Elemente zunächst auf das lebendige Wesen.",
        "Solange diese Elemente aber nur auf dieses lebendige Wesen wirken, solange sie von diesem lebendigen Wesen aufgenommen werden, wie sie von der Pflanze als Träger von inneren Lebensvorgängen aufge­nommen werden, solange entsteht kein Bewußtsein.",
        "Be­wußtsein entsteht erst dann, wenn diese äußeren Elemente in Widerspruch treten mit dem inneren Leben, wenn eine Zerstörung stattfindet.",
        "Aus der Zerstörung des Lebens muß das Bewußtsein erfließen.",
        "Ohne teilweisen Tod wird ein Lichtstrahl in ein lebendiges Wesen nicht eindringen kön­nen, wird in dem lebendigen Wesen nie der Vorgang angeregt"
      ],
      [
        "werden können, aus dem das Bewußtsein entspringt.",
        "Wenn aber das Licht in die Oberfläche des Lebens eindringt, dann eine teilweise Verwüstung anrichtet, die inneren Stoffe und Kräfte niederreißt, dann entsteht jener geheimnisvolle Vorgang, der sich überall in der Außenwelt in ganz be­stimmter Weise abspielt."
      ],
      [
        "Stellen Sie sich vor: Die intelli­genten Kräfte der Welt wären zu einer Höhe emporgestie­gen, daß das äußere Licht und die äußere Luft ihnen fremd geworden wären.",
        "Nur eine Zeitlang blieben sie mit ihnen in Einklang, dann vervollkommneten sie sich selbst, wo­durch ein Widerspruch entstand."
      ],
      [
        "Könnten Sie mit den Augen des Geistes diesen Vorgang verfolgen, so könnten Sie sehen, wie da, wo sich in einfache Wesen ein Lichtstrahl eindrängt, die Haut etwas umgestaltet wird und ein win­ziges Auge entsteht.",
        "Was ist es nun, was da in der Materie zuerst aufdämmert?"
      ],
      [
        "In was drückt sich diese feine Zer­störung aus, denn eine Zerstörung ist es, was dabei vor sich geht?",
        "Es ist der Schmerz, der nichts als ein Ausdruck für diese Zerstörung ist.",
        "Überall, wo das Leben der äußeren Natur entgegentritt, findet Zerstörung statt, die, wenn sie größer wird, selbst den Tod hervorbringt."
      ],
      [
        "Aus dem Schmerz wird das Bewußtsein geboren.",
        "Derselbe Prozeß, der Ihr Auge geschaffen hat, wäre ein Zerstörungsprozeß gewor­den, wenn er an dem Wesen, das sich in dem menschlichen Wesen heraufentwickelt hat, überhand genommen hätte."
      ],
      [
        "So hat er aber nur einen kleinen Teil ergriffen, wodurch er aus der Zerstörung, aus dem partiellen Tod heraus jene Spiege­lung der Außenwelt schaffen konnte, die man das Bewußt­sein nennt.",
        "Das Bewußtsein innerhalb der Materie wird also aus dem Leide, aus dem Schmerz geboren."
      ],
      [
        "Wenn wir diesen Zusammenhang zwischen Leid und Schmerz und dem bewußten Geist, der uns umgibt, einsehen, dann verstehen wir wohl auch ein Wort eines christlichen"
      ],
      [
        "Eingeweihten, der solche Dinge gründlich intuitiv wußte und auf dem Grunde von allem bewußten Leben den Schmerz sah, das Wort: «In aller Natur seufzet jede Krea­tur in Schmerzen, erwartungsvoll, die Gotteskindschaft zu erlangen.» Das finden Sie im 8.",
        "Kapitel des Paulus, als eine wunderbare Ausprägung dieser Grundlage des Bewußtseins im Schmerz."
      ],
      [
        "So kann man es auch verstehen, wie bedeu­tende, sinnige Menschen dem Schmerze eine so große, um­fassende Rolle zugeschrieben haben.",
        "Nur ein Beispiel möchte ich hier anführen.",
        "Ein großer deutscher Philosoph sagt, wenn man die ganze Natur um sich herum ansieht, so er­scheint einem überall auf ihrem Antlitz der Schmerz, das Leid ausgedrückt, ja, wenn man die höheren Tiere ansieht, so zeigen sie dem tiefer Blickenden einen leidensvollen Ausdruck."
      ],
      [
        "Und wer wollte nicht zugeben, daß manche Tier­physiognomie aussieht wie der Ausdruck eines tief verhal­tenen Schmerzes?",
        "Wenn wir die Sache so ansehen, wie wir das eben angedeutet haben, dann sehen wir die Entstehung des Bewußtseins aus dem Schmerze, so daß das Wesen, das aus der Zerstörung heraus Bewußtsein bildet, aus dem Ver­fall des Lebens heraus ein Höheres erstehen läßt, aus dem Tode heraus fortwährend sich selbst erschafft."
      ],
      [
        "Wenn das Lebendige nicht leiden könnte, niemals könnte das Bewußt­sein entstehen.",
        "Wenn der Tod nicht in der Welt wäre, nie­mals könnte in der sichtbaren Welt der Geist existieren.",
        "Das ist die Stärke des Geistes, daß er die Zerstörung in etwas noch Höheres, als das Leben ist, umschafft und so mitten im Leben ein Höheres, ein Bewußtsein bildet."
      ],
      [
        "Im­mer weiter und weiter sehen wir dann die verschiedenen Schmerzerlehnisse zu den Organen des Bewußtseins sich entwickeln.",
        "Man sieht es schon bei den Tieren, die zur Ab­wehr nach außen nur ein Reflexbewußtsein haben, ähnlich wie der Mensch, wenn Gefahr für das Auge besteht, dasselbe"
      ],
      [
        "schließt.",
        "Wenn die Reflexbewegung nicht mehr genügt, das innere Leben zu schonen, wenn der Reiz zu stark wird, so erhebt sich die innere Widerstandskraft und gebiert die Sinne, die Empfindung, Auge und Ohr.",
        "Sie wissen vielleicht aus mancher unliebsamen Erfahrung heraus, vielleicht auch instinktiv, daß die Sache so ist.",
        "Ja, Sie wissen aus einer höheren Stufe Ihres Bewußtseins ganz genau, daß das, was jetzt gesagt worden ist, eine Wahrheit ist.",
        "Ein Beispiel wird die Sache noch verdeutlichen.",
        "Wann fühlen Sie gewisse innere Organe Ihres Organismus?",
        "Sie gehen durchs Leben und fühlen weder Ihren Magen, noch Ihre Leber, noch Ihre Lunge, Sie fühlen keines Ihrer Organe, solange sie gesund sind.",
        "Sie fühlen sie nur dann, wenn sie Sie schmer­zen, und Sie wissen eigentlich erst, daß Sie dieses oder jenes Organ haben, wenn es Sie schmerzt, wenn Sie empfinden, daß da etwas nicht in Ordnung ist, daß ein Zerstörungs­prozeß beginnt."
      ],
      [
        "Wenn wir dieses Beispiel, diese Erklärung nehmen, dann sehen wir, daß aus dem Schmerz fortwährend bewußtes Leben geboren wird.",
        "Tritt der Schmerz zum Leben, so ge­biert er die Empfindung und das Bewußtsein.",
        "Dieses Ge­bären, dieses Hervorbringen eines Höheren, spiegelt sich wiederum im Bewußtsein als die Lust, und es gab nie eine Lust, ohne daß es vorher einen Schmerz gegeben hätte.",
        "Unten in dem Leben, das sich eben aus der physischen Ma­terie heraus erhebt, gibt es noch keine Lust.",
        "Wenn aber der Schmerz Bewußtsein hat erstehen lassen und als Bewußt­sein schöpferisch weiterwirkt, dann ist diese Schöpfung auf einer höheren Stufe und drückt sich im Gefühle der Lust aus.",
        "Dem Schaffen liegt die Lust zugrunde.",
        "Lust kann nur da sein, wo innerliches oder äußerliches Schaffen möglich ist.",
        "Irgendwie liegt einer jeden Lust das Schaffen zugrunde, wie jeder Unlust die Notwendigkeit des Schaffens zugrunde"
      ],
      [
        "liegt.",
        "Nehmen Sie etwas, was auf niederer Stufe das Leid charakterisieren kann, zum Beispiel das Gefühl des Hun­gers, der das Leben zerstören kann.",
        "Dem treten Sie mit der Nahrung entgegen.",
        "Die Nahrungsaufnahme wird zum Ge­nuß, weil die Nahrung in der Lage ist, in eine Lebenssteige­rung, in eine Lebensproduktion überzugehen.",
        "So sehen Sie, daß auf Grundlage des Schmerzes höheres Schaffen, Lust entsteht.",
        "Eher als die Lust ist also das Leid.",
        "Daher kann auch die Philosophie Schopenhauers und die Eduard von Hartmanns mit Recht sagen, daß das Leid eine allgemeine Lebensempfindung sei.",
        "Sie gehen aber nicht tief genug auf den Ursprung des Leides zurück, kommen nicht auf den Punkt, wo sich das Leid zu etwas Höherem entwickeln soll.",
        "Der Ursprung des Leides wird da gefunden, wo aus dem Leben Bewußtsein entsteht, wo Geist aus dem Leben herausgeboren wird."
      ],
      [
        "So können wir jetzt auch begreifen, was dem Menschen in der Seele dämmert von dem Zusammenhang zwischen Leid und Schmerz und Erkenntnis und Bewußtsein, so konnten wir noch nachweisen, wie aus Schmerz und Leid ein Edleres, Vollkommeneres herausgeboren wird."
      ],
      [
        "Diejenigen, welche meine Vorträge öfter gehört haben, werden sich auf die Hinweise entsinnen, daß es etwas gibt wie eine Einweihung, wobei ein höheres Bewußtsein vor­handen ist und wobei der Mensch sich von den sinnlichen Dingen zu der Anschauung einer geistigen Welt erhebt, daß Kräfte und Fähigkeiten in der menschlichen Seele schlum­mern, die aus der Seele herausgeholt werden können wie die Sehkraft aus dem Blindgeborenen durch die Operation, daß dann gleichsam ein neuer Mensch ersteht, dem die ganze Welt auf höherer Stufe wie verwandelt erscheint.",
        "Wie dem Blindgeborenen nach der Operation, so erscheinen dem gei­stig Geborenen die Dinge in neuem Licht.",
        "Aber auch dies"
      ],
      [
        "kann nur geschehen, indem derselbe Prozeß, der eben ge­nannt worden ist, sich auf einer höheren Stufe wiederholt.",
        "Wenn das, was Sie beim Durchschnittsmenschen vereint finden, getrennt wird, wenn eine Art Zerstörungsprozeß in der niederen Menschennatur auftritt, dann kann dieses höhere Bewußtsein, dieses Schauen in der geistigen Welt, eintreten."
      ],
      [
        "Drei Kräfte gibt es in der menschlichen Natur: Denken, Fühlen und Wollen.",
        "Diese drei Kräfte hängen an der physi­schen Menschenorganisation.",
        "Gewisse Willensakte treten auf, nachdem gewisse Denk- und Gefühlsvorgänge statt-gefunden haben.",
        "Der Organismus des Menschen muß in richtiger Weise funktionieren, wenn diese drei Kräfte zu­sammenstimmen sollen.",
        "Sind gewisse Leitungen unterbro­chen, gewisse Teile erkrankt, dann herrscht keine richtige Harmonie zwischen Denken, Fühlen und Wollen.",
        "Der Mensch ist dadurch, daß die Organe des Wollens gelähmt sind, nicht imstande, seine Gedanken in Willensimpulse umzusetzen.",
        "Er ist schwach als Tatmensch, er kann zwar gut denken, aber sich nicht entschließen, einen Gedanken in Wirklichkeit umzusetzen.",
        "Eine andere Art ist die, wo der Mensch nicht imstande ist, seine Gefühle durch die Ge­danken richtig lenken zu lassen, die Gefühle in Einklang mit den dahinterstehenden Gedanken zu bringen.",
        "Der Tob­süchtige ist im Grunde nichts anderes."
      ],
      [
        "Im Menschen der Gegenwart besteht eine Harmonie zwi­schen Denken, Fühlen und Wollen, in der befindet sich heute ein normal gebildeter Mensch, der einem Leidenden gegenüber in den richtigen Gefühls- und Willenszustand kommt.",
        "Dies ist alles richtig für gewisse Stufen der Ent­wicklung.",
        "Es ist aber zu beachten, daß sich diese Harmonie im Gegenwartsmenschen unbewußt herstellt.",
        "Soll der Mensch aber eingeweiht werden, soll er hineinsehen in die höheren"
      ],
      [
        "Welten, dann müssen diese drei Glieder: Denken, Fühlen und Wollen, auseinandergerissen werden.",
        "Die Willens- und Gefühlsorgane müssen eine Scheidung erleiden.",
        "Der physi­sche Organismus eines Eingeweihten ist daher auch anders als der eines Nichteingeweihten, wenn das die Anatomie auch noch nicht hat nachweisen können.",
        "Der Kontakt zwi­schen Denken, Fühlen und Wollen ist unterbrochen.",
        "Der Eingeweihte wäre imstande, irgend jemand tief leiden zu sehen, ohne daß sich ein Gefühl in ihm regte, kalt würde er stehenbleiben und es ansehen können.",
        "Und warum ist dies so?",
        "Es darf sich beim Eingeweihten nichts unbewußt inein­andergliedern, er ist aus Freiheit ein mitleidsvoller Mensch und nicht, weil ihn etwas Äußeres dazu zwingt.",
        "Das ist der Unterschied zwischen einem Eingeweihten und einem Nicht-eingeweihten.",
        "Ein solches höheres Bewußtsein schafft gleich­sam eine höhere Substanz, und der Mensch zerfällt in einen Gefühls-, einen Willens- und einen Denkmenschen.",
        "Über diesen dreien ihront dann erst der höhere, neugeborene Mensch, und von dieser Stufe eines höheren Bewußtseins aus werden dann jene drei in Einklang gebracht.",
        "Hier muß dann auch wieder der Tod, die Zerstörung eingreifen.",
        "Träte diese Zerstörung so ein, daß nicht zugleich auch ein neues Bewußtsein entsproßte, dann würde Wahnsinn entstehen.",
        "Wahnsinn würde also nichts anderes sein als der Zustand, in dem das menschliche Wesen zerschellt ist, ohne daß die höhere, bewußte Instanz geschaffen worden ist."
      ],
      [
        "So tritt auch hier wieder ein Doppeltes ein: eine Art Zerstörungsprozeß des Niederen neben einem Entstehungs-prozeß des Höheren.",
        "Wie im Blute das Gift in den Venen und wie zwischen dem roten und blauen Blut das Bewußt­sein im gewöhnlichen Menschen erzeugt wird, so wird in dem initiierten Menschen wieder in dem Zusammenwirken von Leben und Tod das höhere Bewußtsein im Inneren erzeugt,"
      ],
      [
        "und die Seligkeit entspringt wiederum einer höheren Lust, dem Schaffen, das aus dem Tode hervorgeht."
      ],
      [
        "Das ist es, was der Mensch ahnt, wenn er den geheimnis­vollen Zusammenhang spürt zwischen Schmerz und Leid und dem Höchsten, das der Mensch erreichen kann.",
        "Deshalb läßt der tragische Dichter aus dem im Leide untergehenden Helden den Sieg des Lebens, das Bewußtsein von dem Siege des Ewigen über das Zeitliche hervorgehen.",
        "Deshalb sieht das Christentum mit Recht in dem Untergehen des Christus Jesus - seiner irdischen Natur nach - in Schmerz und Leid, in Qual und Elend den Sieg des ewigen Lebens über die zeitliche Vergänglichkeit.",
        "Deshalb auch wird unser Leben rei­cher, inhaltsvoller, wenn wir es erweitern können über das­jenige, was außerhalb unseres Selbstes liegt, wenn wir in dem Leben, das außerhalb unseres Selbstes ist, aufgehen können."
      ],
      [
        "So wie wir aus dem Schmerz, der durch einen äußeren Lichtstrahl angeregt ist und durch uns als lebendige Wesen überwunden wird, ein höheres Bewußtsein schaffen, so wird, wenn wir die Leiden der anderen in unsere eigene, größere Bewußtseinswelt umwandeln, aus der Empfäng­lichkeit für das Leid der anderen ein Schaffen im Mitleid geboren.",
        "Und so entsteht endlich aus dem Leide auch die Liebe.",
        "Denn was ist die Liebe anderes, als sein Bewußtsein ausdehnen über andere Wesen?",
        "Wenn wir selbst soviel ent­behren wollen, soviel ausgeben wollen, uns selbst soviel ärmer machen wollen, als wir dem anderen Wesen geben, und wenn wir imstande sind, geradeso wie die Haut, die den Lichtstrahl empfängt und aus ihrem Schmerz ein höhe­res Wesen, ein Auge zu bilden vermag, wenn wir imstande sind, aus der Verbreitung unseres Lebens über die anderen Leben ein höheres Leben zu saugen, dann wird in uns selbst, aus dem, was wir weggeben an das andere Wesen, die Liebe, das Mitfühlen mit allen Kreaturen geboren."
      ],
      [
        "Das liegt auch dem Ausspruche des griechischen Dichters zugrunde: Aus Leben ward Lehre, aus Lehre Erkennt­nis.",
        "Hier berührt sich wiederum, wie im vorigen Vortrage schon gesagt, eine auf neuesten naturwissenschaftlichen For­schungen beruhende Erkenntnis mit den Resultaten der alten Geistesforschung.",
        "Immer hat die alte Geistesforschung gesagt, daß höchste Erkenntnis, höchste Lehre nur aus dem Leid hervorgehen kann.",
        "Wenn wir ein krankes Glied be­sitzen und Schmerz daran gelitten haben, so kennen wir dieses Glied am allerbesten; ebenso kennen wir das am besten, was wir in der eigenen Seele abgelagert haben.",
        "Es quillt aus dem eigenen Leid als dessen Frucht die Er­kenntnis."
      ],
      [
        "Dasselbe liegt auch dem Kreuzestod des Christus Jesus zugrunde, dem, wie aus der christlichen Anschauung her­vorgeht, bald der sich in der Welt ausbreitende Heilige Geist folgte.",
        "Wir verstehen also jetzt das Hervorgehen des Heiligen Geistes aus dem Kreuzestod des Christus Jesus als einen Prozeß, auf den durch das Gleichnis vom Weizen-korn hingewiesen wird.",
        "Aus der Zerstörung muß die neue Frucht hervorgehen, und so wird auch aus der Zerstörung, aus den Schmerzen, die am Kreuze ertragen worden sind, der Geist, der sich am Pfingstfeste über die Apostel ergießt, geboren.",
        "Das wird im Johannes-Evangelium klar aus­gesprochen, wenn gesagt ist: der Geist war noch nicht da, denn der Christus war noch nicht verklärt.",
        "Wer das Johannes-Evangelium tiefer. liest, der wird Bedeutungs­volles für sich daraus hervorgehen sehen."
      ],
      [
        "Manchen wird man sagen hören können, daß er die Schmerzen nicht missen möchte, da sie ihm die Erkenntnis gebracht haben.",
        "Jeder Gestorbene kann Sie lehren, daß das wahr ist, was ich gesagt habe.",
        "Würde der Mensch den Kampf gegen die Zerstörung in sich bis zum wirklichen"
      ],
      [
        "Tode führen, wenn nicht der Schmerz, wie ein Wächter des Lebens, fortwährend neben ihm stände?",
        "Der Schmerz macht uns aufmerksam darauf, daß wir gegen die Zerstörung des Lebens Vorkehrungen zu treffen haben.",
        "Aus dem Schmerze heraus schaffen wir neues Leben.",
        "In den Aufzeichnungen eines modernen Naturforschers über die Mimik des Den­kers lesen wir, daß auf dem Antlitz des Denkers etwas liegt wie ein verhaltener Schmerz."
      ],
      [
        "Wenn es sich mit der Erhebung, die aus der durch Schmerz erlangten Erkenntnis fließt, so verhält, wenn es also wahr ist, daß aus Leid Lehre entsteht, dann ist nicht mit Un­recht - wie wir das nächste Mal sehen werden - in der bib­lischen Schöpfungsurkunde die Erkenntnis des Guten und des Bösen mit den Leiden und Schmerzen in Zusammen­hang gebracht.",
        "Deshalb ist auch von tiefer Blickenden mit Recht immer wieder betont worden, wie der Ursprung der Läuterung, die Erhöhung der menschlichen Natur, im Schmerz liegt, und wenn die theosophische Weltanschau­ung in dem großen Schicksalsgesetze, Karma, von den Lei­den aus, die ein Mensch im gegenwärtigen Leben erleidet, hindeutet auf das, was er in früheren Leben gesündigt, ver­brochen hat, dann verstehen wir einen solchen Zusammen­hang auch nur aus der tieferen Menschennatur heraus.",
        "Das­jenige, was im früheren Leben von uns in der Außenwelt vollführt wurde, verwandelt sich aus wilden in erhabene Kräfte.",
        "Die Sünde ist gleichsam wie ein Gift, das aber, wenn es in Substanz des Lebens verwandelt wird, sich zum Heilmittel gestaltet.",
        "So kann die Sünde wieder zur Kräf­tigung und Erhöhung des Menschen beitragen, und so stellen sich uns auch in der Erzählung von Hiob die Schmerzen und Leiden als eine Erhöhung der Erkenntnis und des Geistes dar."
      ],
      [
        "Das sollte nur eine Skizze sein, die auf den Zusammenhang"
      ],
      [
        "von irdischem Dasein und Leiden und Schmerzen hin­weisen sollte.",
        "Sie sollte zeigen, wie wir den Sinn von Leiden und Schmerzen einsehen können, wenn wir sehen, wie sie erstarren, sich kristallisieren in physischen Dingen und Or­ganismen bis zum Menschen, und wie durch ein Verflüssigen des Erstarrten der Geist bei uns wiedergeboren werden kann, wenn wir sehen, daß im Geist der Ursprung des Schmerzes, des Leides ist.",
        "Das, was uns der Geist gibt, ist Schönheit, Kraft und Weisheit, das verwandelte Bild der ursprünglichen Stätte des Schmerzes.",
        "Deshalb hat nicht mit Unrecht ein geistvoller Mann, Fabre d'Olivet, den Ver­gleich gebraucht, um das Höchste, Edelste, Geläutertste in der Menschennatur in seinem Hervorgehen aus dem Schmerz zu zeigen, daß das Hervorgehen von Weisheit und Schön­heit aus dem Leid vergleichbar ist einem Vorgang draußen in der Natur, dem Geborenwerden der wertvollen, schönen Perle.",
        "Denn aus was wird sie geboren?",
        "Aus der Krankheit des Muscheltieres, aus der Zerstörung innerhalb der Perl­muschel.",
        "Wie die Schönheit der Perle geboren wird aus Krankheit und damit aus Leiden, so wird Erkenntnis, edle Menschennatur und geläuterter Menschensinn aus dem Lei­den, aus dem Schmerz geboren."
      ],
      [
        "So dürfen wir wohl im Einklang mit dem alten griechi­schen Dichter Äschylos sagen: Aus dem Leid entsteht Lehre, aus der Lehre Erkenntnis.",
        "Und ebenso wie in bezug auf vieles andere dürfen wir in bezug auf den Schmerz sagen, daß wir ihn erst dann erfaßt haben, wenn wir ihn er­kennen nicht nur an sich selbst, sondern an dem, was aus ihm hervorgeht.",
        "Wie so manches andere wird auch der Schmerz nur an seinen Früchten erkannt."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "DER URSPRUNG DES BÖSEN Berlin, 22. November 1906",
    "paragraphs": [
      "Es ist charakteristisch für die ganze heutige Literatur, daß sie so wenig vom Bösen sprieht. Der Materialismus befaßt sidi eben nidit mit dem Bösen. Leid, Krankheit und Tod können anscheinend eine materielle Erklärung finden, aber das Böse nicht. Beim Tier spricht man von Grausamkeit, Schädlichkeit, aber böse kann man das Tier nidit nennen. Das Böse erschöpft sich innerhalb des Menschenreiches. Die heutige Naturwissenschaft sudit den Mensdien aus dem Tier heraus zu begreifen und verwischt alle Unterschiede zwischen Mensch und Tier. Darum muß sie audi das Böse leugnen. Man muß, um das Böse zu finden, ganz eingehen auf die mensdilidien Eigenschaften. Man muß erkennen, daß der Mensdi ein eigenes Reich in Anspruch nimmt. Wir wollen diese Frage jetzt vom geisteswissenschaftlichen Stand­punkt aus betrachten.",
      "Es gibt eine menschliche Urweisheit, die hinter dem rein äußerlichen Sinnenschein der Dinge zum eigentlichen Wesen der Dinge vordringt. Früher wurde diese Weisheit in engen Kreisen bewahrt und nur nach strengen Proben wurde der Zu­gang zu diesen Kreisen gewährt. Ehe ein Mensch Zutritt er­langte, mußte er den Hütern dieser Weisheit bewiesen haben, daß er sein Wissen nur in selbstlosester Weise verwenden werde. Seit den letzten Jahrzehnten ist das Elementare dieser Weisheits-Wissenschaft aus gewissen Gründen popularisiert worden. Immer mehr wird davon ins tägliche Leben einflie­ßen. Wir stehen erst am Anfang dieser Entwicklung.",
      "Wie hängt nun das Böse mit der eigentlichen Menschen-natur zusammen? Oft hat man sich das Böse auf die ver­schiedenste Art zu erklären versucht. Da hat man gesagt:",
      "Es gibt kein Böses im eigentlichen Sinne des Wortes. Es ist ein herabgemindertes Gutes, es ist das schlechteste Gute. Denn wie es bei allem verschiedene Grade des Daseins gibt, so auch beim Guten. Oder man sagte: Wie das Gute eine Urmacht ist, so ist es auch das Böse. Diese Ansicht prägte sieh namentlich in der persischen Mythe von Ormuzd und Ahriman aus. Die Geheimwissenschaft erst zeigt aus der Tiefe der menschlichen und der ganzen kosmischen Natur heraus, wie das Böse zu begreifen ist. Leugnet man es, kann man es gar nicht begreifen. Man muß verstehen, wel­che Aufgabe, welche Mission das Böse in der Welt hat. Aus der Entwicklung des Menschen in die Zukunft hinein sehen wir, wie die Menschen aus der Vergangenheit geworden sind und was das Böse in ihrem Entwicklungsgang bedeu­ten soll.",
      "Die Geheimwissenschaft lehrt das Dasein gewisser hoch-entwickelter Menschen, der Eingeweihten oder Initiierten. In den Geheimschulen aller Zeiten wird gelehrt, wie sich der Mensch auf eine solche Entwicklungsstufe bringen kann. Bestimmte Übungen werden da vorgeschrieben, die auf ganz natürliche Weise den Menschen fortentwickeln. Medi­tations- und Konzentrationsübungen sind es, die dem Men­schen eine andere Anschauung geben sollen, eine Anschau­ung, die er nicht mit dem Verstande und den fünf Sinnen erwerben kann. Die Meditation führt zunächst weg von der sinnlichen Auffassung. Durch innere seelische Arbeit wird da der Mensch frei von den Sinnen. Etwas Ahnliches geht da im Menschen vor sieh wie bei der Operation eines Blindgeborenen. Eine Art Operation findet statt, die geistige Augen und Ohren öffnet. Diese Entwicklung wird in längerer",
      "Zeit die ganze Menschheit erreichen. Das Weltliche darf man darum aber nicht verleugnen, wenn man sieh höher entwickeln will. Weltflüchtige Askese taugt nicht fürs Hellsehen. Hellsehen ist die Frucht dessen, was die Seele in der Sinnenwelt sammelt. Schön verglich die griechische Philosophie die Mensehenseele mit einer Biene. Die Welt von Farben und Licht bietet der Seele den Honig, den sie mitbringt in die höhere Welt. Sinnenerfahrung muß die Seele vergeistigen und hinauftragen in höhere Welten.",
      "Welche Aufgabe hat nun die Seele, die frei ist vom Leibe? Wir treffen hier auf einen wichtigen Grundsatz. Jedes Wesen wird, wenn es sich herausentwickelt hat, auf einer höheren Stufe Leiter und Führer derjenigen Wesen und Formen, durch die es durchgegangen ist. Wir sehen da ein Zukunftsbild. Wenn der Mensch sieh so vergeistigt haben wird, daß er den physischen Leib nicht mehr braucht, wirkt der Mensch als geistiger Leiter von außen auf die Welt ein. Dann ist die Aufgabe dieses Planeten erfüllt. Er geht dann zu einer anderen Verkörperung über. Die Erde wird dann ein neues planetarisches Dasein erhalten. Die Menschen werden dann die Götter des neuen Planeten sein. Der Mensdiheitsleib, der verlassen ist vom Geist, wird nie­deres Reich sein. Wir tragen jetzt eine doppelte Natur in uns: das, was herrschen wird auf dem nächsten Planeten, und das, was das niedere Reich sein wird. So wie die Erde sich neu verkörpern wird, so hat sie sich auch herausgebildet aus früheren Entwicklungsvorgängen, und so wie die Men­schen die Götter des nächsten Planeten sein werden, so waren die uns jetzt leitenden Wesenheiten Menschen auf dem vor­hergehenden Planeten, und sie hatten als Niederes das, was wir Menschen auf der Erde sind. Damit finden wir den Zu­sammenhang der Erde mit Vorgängen, die in der Vergan­genheit und in der Zukunft liegen. Die Stufe, die der Mensch",
      "heute auf der Erde hat, hatten einstmals die Wesen, die die Schöpfer und Führer der Menschen heute sind, die Elohim­Geister, die sich offenbaren als Führer der Entwicklung des Menschen. Und die Menschen werden auf dem zukünftigen Planeten so weit sein, daß sie selbst Lenker und Leiter sind.",
      "Aber man muß nicht denken, es müsse sich nun genau so wiederholen; dasselbe wiederholt sieh nie. Nichts geschieht zweimal in der Welt. Nie war das Dasein so wie jetzt auf der Erde. Das Erdendasein bedeutet den Kosmos der Liebe, das Dasein auf dem früheren Planeten bedeutet den Kos­mos der Weisheit.",
      "Die Liebe vom Elementarsten bis zum Höchsten sollen wir entwickeln. Die Weisheit ruht ver­borgen auf dem Grunde des Erdendaseins. Darum soll man nicht von der «niederen» physischen Menschennatur spre­chen, denn sie ist gewissermaßen die vollkommenste Form des Menschen.",
      "Man betrachte den weisheitsvollen Bau eines Knochens, zum Beispiel des Oberschenkelknochens. Da ist das Problem: mit dem geringsten Aufwand von Material und Kraft die größtmöglichste Gewiehtsmasse zu tragen, in vollkommenster Art gelöst.",
      "Man schaue sich den Wunder-bau des Herzens, des Gehirns an! Der Astralleib steht nicht etwa höher. Er ist der Genießer, der fortwährende Attacken auf das weisheitsvoll gebaute Herz macht. Er wird noch lange brauchen, um so vollkommen und weise zu sein wie der physische Leib.",
      "Aber er muß es werden. Darin besteht die Entwicklung. Auch der physische Leib mußte sich so entwickeln. Was weise an ihm ist, mußte aus Unweisheit und Irrtum hervorgehen. Die Weisheitsentwicklung ging der Liebesentwicklung voraus.",
      "Die Liebe ist noch nicht voll­kommen. Aber in der ganzen Natur ist sie zu finden. Bei der Pflanze, beim Tier, beim Menschen, von der niedersten Geschlechtsliebe an bis zur höchsten, vergeistigtesten Liebe.",
      "Ungeheure Mengen von Wesen, die der Liebestrieb hervorgebracht,",
      "gehen im Kampf ums Dasein zugrunde. Kampf wirkt überall da, wo Liebe ist. Das Auftreten der Liebe bringt Kampf, notwendigen Kampf mit sieh. Aber sie wird ihn auch überwinden, wird den Krieg in Harmonie ver­wandeln.",
      "Weisheit ist das Charakteristikum der physischen Natur. Da, wo diese Weisheit von Liebe durchsetzt ist, da erst ist der Anfang der Erdentwicklung. Wie heute Kampf auf der Erde ist, war auf dem früheren Planeten Irrtum zu finden. Merkwürdige Fabelwesen wandelten da umher, Irrtümer der Natur, die nicht entwicklungsfähig waren. Wie Liebe aus Lieblosem hervorgeht, so die Weisheit aus Unweisheit. Die, welche die Erdentwicklung erreichen, werden die Liebe als eine Naturkraft in den nächsten Planeten hinein­bringen. So ward auch einst die Weisheit auf die Erde ge­tragen. Die Menschen der Erde schauen auf zu den Göttern als zu den Bringern der Weisheit. Die Menschen des folgen­den Planeten werden zu den Göttern als zu den Bringern der Liebe aufschauen. Die Weisheit wird den Menschen als göttliche Offenbarung von den Menschen des früheren Planeten zuteil. Alle Reiche der Welt hängen unter sich zusammen. Wenn es keine Pflanzen gäbe, so würde in kur­zer Zeit die Lebensluft verpestet sein; denn Mensch und Tier atmen Sauerstoff ein und lebenvernichtende Kohlen­säure wieder aus. Doch die Pflanzen atmen Kohlensäure ein und geben Sauerstoff von sich. So hängt hier hinsichtlich der Lebensluft das Höhere vom Niederen ab.",
      "So ist es nun in allen Reichen. Wie das Tier und der Mensch von der Pflanze, so sind wieder die Götter von den Menschen abhängig. Das hat die griechische Mythe so schön ausgedrückt: Die Götter erhalten von den Sterblichen Nek­tar und Ambrosia. Beide bedeuten die Liebe. Die Liebe wird innerhalb des Menschengeschleehtes erzeugt. Und Liebe",
      "atmet das Göttergeschlecht ein, sie ist die Götternahrung. Die Liebe, die von den Menschen erzeugt wird, wird den Göttern Speise. Das ist viel wirklicher als etwa die Elek­trizität, so seltsam es zuerst erscheint. Die Liebe tritt zu­erst als Geschleehtsliebe auf und entwickelt sich hinauf bis zur höchsten geistigen Liebe. Aber alle Liebe, niedere und hohe, ist Götteratem. Nun kann man sagen: Wenn das alles so ist, kann es kein Böses geben. Aber Weisheit liegt der Welt zugrunde, Liebe entwickelt sich. Weisheit wird die Lenkerin der Liebe. So wie alle Weisheit aus Irrtum ge­boren wird, ringt sieh alle Liebe nur aus Kämpfen zur Höhe empor.",
      "Nicht alle Wesen des früheren Planeten stiegen zur Höhe der Weisheit hinan. Es sind Wesen zurückgeblieben, sie stehen ungefähr zwischen Göttern und Menschen. Sie brau­chen noch etwas vom Menschen. Aber in einen physischen Körper können sie sich nicht mehr kleiden. Luziferische Wesenheiten nennt man sie, oder man faßt sie zusammen unter dem Namen Luzifer als ihrem Anführer. Wie wirkt nun Luzifer auf die Menschen? Nicht so wie die Götter. Das Göttliche tritt an das Edelste im Menschen heran, aber an das Niedere kann und soll es nicht kommen. Weisheit und Liebe werden erst am Ende der Entwicklung ihre Ver­mählung feiern. Aber die luziferischen Wesenheiten treten an das niedere, unentwickelte Element der Liebe heran. Sie bilden die Brücke zwischen Weisheit und Liebe. So erst mischt sich die Weisheit mit der Liebe. Das, was sieh nur ans Unpersönliche wendet, verstrickt sich so mit der Per­sönlichkeit. Auf dem früheren Planeten war die Weisheit ein Instinkt, wie es heute die Liebe ist. Ein schöpferischer Weisheitsinstinkt war herrschend, wie heute ein schöpfe­rischer Liebesinstinkt. Früher hatte also die Weisheit den Menschen instinktmäßig geführt. Dadurch aber, daß die",
      "Weisheit heraustrat und nicht mehr führte, ward der Mensch selbstbewußt, er wußte sieh als ein selbständiges Wesen. Im Tier ist die Weisheit noch instinktmäßig, daruni ist es noch nicht selbstbewußt. Aber die Weisheit wollte den Men­schen nun von außen lenken und leiten, ohne daß die Liebe einen Zusammenhang damit hatte.",
      "Da Luzifer kam, pflanzte er die menschliche Weisheit in die Liebe. Und die mensch­liche Weisheit schaut auf zur göttlichen Weisheit. Im Men­schen ward die Weisheit zum Enthusiasmus, zur Liebe selbst. Hätte nur die Weisheit ihren Einfluß ausgeübt, so wäre der Mensch nur gut geworden, er hätte die Liebe nur zum Aufbau des Erdenbewußtseins gebraucht.",
      "Aber Luzifer brachte die Liebe mit dem Selbst in Verbindung, zum Selbst­bewußtsein trat die Selbstliebe. Das wird schön im Para­diesesmythus ausgedrückt: «... und sie sahen, daß sie nackend waren», das heißt, damals sahen die Menschen zum ersten Male sich selbst, vorher hatten sie nur die Um­welt gesehen.",
      "Da hatten sie nur ein Erdenbewußtsein, aber kein Selbstbewußtsein. Nun konnten die Menschen die Weisheit in den Dienst des Selbst stellen. Selbstlose Liebe zur Umwelt und Liebe zum Selbst gab es von nun an.",
      "Und die Selbstliebe war böse und die Selbstlosigkeit war gut. Nie hätte der Mensch ein warmes Selbstbewußtsein bekom­men ohne Luzifer. Denken und Weisheit traten nun in den Dienst des Selbst. Nun gab es eine Wahl zwischen gut und böse.",
      "Nur um das Selbst in den Dienst der Welt zu stellen, darf Liebe zum Selbst hinzutreten. Nur wenn die Rose den Garten zieren will, darf sie sich selbst schmücken. Das muß man sich bei einer höheren, okkulten Entwicklung tief in die Seele schreiben.",
      "Um das Gute fühlen zu können, mußte der Mensch auch das Böse fühlen können. Enthusiasmus für das Höhere gaben ihm die Götter. Aber ohne das Böse konnte es kein Selbstgefühl, keine freie Wahl des Guten,",
      "keine Freiheit geben. Das Gute konnte ohne Luzifer ver­wirklicht werden, die Freiheit nicht. Um das Gute wählen zu können, muß der Mensch auch das Böse vor sich haben, es muß ihm innewohnen als Kraft der Selbstliebe. Aber die Selbstliebe muß zur All-Liebe werden. Dann wird das Böse überwunden sein. Freiheit und das Böse entspringen aus demselben Punkt. Luzifer enthusiasmiert den Menschen menschlich für das Göttliche. Luzifer ist der Träger des Lichts. Elohim ist das Licht selbst. Hat das Lieht der Weis­heit die Weisheit im Menschen entzündet, so hat Luzifer das Licht in den Menschen hineingetragen. Aber der schwarze Schatten des Bösen mußte sich hineinmischen. Luzifer bringt eine eingeschränkte, fleckenerfüllte Weisheit, aber diese kann in den Menschen eindringen. Luzifer ist der Träger der äußeren, menschlichen Wissenschaft, die ja im Dienste des Egoismus steht. Darum wird vom okkulten Schüler Selbstlosigkeit gegenüber dem Wissen verlangt. Dies ist der Ursprung des Bösen in der menschlichen Entwicklung. Was der Sauerteig des alten Brotteiges für das neue Brot ist, das ist vom früheren Planeten Luzifer für uns. Das Böse wird gut an seinem Ort. Bei uns ist es nicht mehr gut. Das Böse ist ein versetztes Gutes. Das absolut Gute eines Planeten bringt in einem seiner Teile zum neuen Planeten immer auch das Böse mit. Das Böse ist ein notwendiger Entwick­lungsgang.",
      "Man darf nicht sagen, die Welt sei unvollkommen, weil das Böse in ihr ist. Vielmehr ist sie gerade darum vollkom­men. Wenn in einem Gemälde herrliche Lichtgestalten und böse Teufelsfratzen zugleich dargestellt sind, so würde man das Bild doch vernichten, wenn man die Teufelsfratzen herausschneiden wollte. Die Weltenschöpfer brauchten das Böse, um das Gute zur Entfaltung zu bringen. Was sich erst am Felsen des Bösen brechen muß, ist ein Gutes. Durch",
      "Selbstliebe nur kann es die All-Liebe zu ihrer höchsten Blüte bringen. Darum hat Goethe so recht, wenn er im Faust den Mephisto sagen läßt:",
      "«Ich bin ein Teil von jener Kraft,",
      "die stets das Böse will und stets das Gute schafft.»"
    ],
    "sentences": [
      [
        "Es ist charakteristisch für die ganze heutige Literatur, daß sie so wenig vom Bösen sprieht.",
        "Der Materialismus befaßt sidi eben nidit mit dem Bösen.",
        "Leid, Krankheit und Tod können anscheinend eine materielle Erklärung finden, aber das Böse nicht.",
        "Beim Tier spricht man von Grausamkeit, Schädlichkeit, aber böse kann man das Tier nidit nennen.",
        "Das Böse erschöpft sich innerhalb des Menschenreiches.",
        "Die heutige Naturwissenschaft sudit den Mensdien aus dem Tier heraus zu begreifen und verwischt alle Unterschiede zwischen Mensch und Tier.",
        "Darum muß sie audi das Böse leugnen.",
        "Man muß, um das Böse zu finden, ganz eingehen auf die mensdilidien Eigenschaften.",
        "Man muß erkennen, daß der Mensdi ein eigenes Reich in Anspruch nimmt.",
        "Wir wollen diese Frage jetzt vom geisteswissenschaftlichen Stand­punkt aus betrachten."
      ],
      [
        "Es gibt eine menschliche Urweisheit, die hinter dem rein äußerlichen Sinnenschein der Dinge zum eigentlichen Wesen der Dinge vordringt.",
        "Früher wurde diese Weisheit in engen Kreisen bewahrt und nur nach strengen Proben wurde der Zu­gang zu diesen Kreisen gewährt.",
        "Ehe ein Mensch Zutritt er­langte, mußte er den Hütern dieser Weisheit bewiesen haben, daß er sein Wissen nur in selbstlosester Weise verwenden werde.",
        "Seit den letzten Jahrzehnten ist das Elementare dieser Weisheits-Wissenschaft aus gewissen Gründen popularisiert worden.",
        "Immer mehr wird davon ins tägliche Leben einflie­ßen.",
        "Wir stehen erst am Anfang dieser Entwicklung."
      ],
      [
        "Wie hängt nun das Böse mit der eigentlichen Menschen-natur zusammen?",
        "Oft hat man sich das Böse auf die ver­schiedenste Art zu erklären versucht.",
        "Da hat man gesagt:"
      ],
      [
        "Es gibt kein Böses im eigentlichen Sinne des Wortes.",
        "Es ist ein herabgemindertes Gutes, es ist das schlechteste Gute.",
        "Denn wie es bei allem verschiedene Grade des Daseins gibt, so auch beim Guten.",
        "Oder man sagte: Wie das Gute eine Urmacht ist, so ist es auch das Böse.",
        "Diese Ansicht prägte sieh namentlich in der persischen Mythe von Ormuzd und Ahriman aus.",
        "Die Geheimwissenschaft erst zeigt aus der Tiefe der menschlichen und der ganzen kosmischen Natur heraus, wie das Böse zu begreifen ist.",
        "Leugnet man es, kann man es gar nicht begreifen.",
        "Man muß verstehen, wel­che Aufgabe, welche Mission das Böse in der Welt hat.",
        "Aus der Entwicklung des Menschen in die Zukunft hinein sehen wir, wie die Menschen aus der Vergangenheit geworden sind und was das Böse in ihrem Entwicklungsgang bedeu­ten soll."
      ],
      [
        "Die Geheimwissenschaft lehrt das Dasein gewisser hoch-entwickelter Menschen, der Eingeweihten oder Initiierten.",
        "In den Geheimschulen aller Zeiten wird gelehrt, wie sich der Mensch auf eine solche Entwicklungsstufe bringen kann.",
        "Bestimmte Übungen werden da vorgeschrieben, die auf ganz natürliche Weise den Menschen fortentwickeln.",
        "Medi­tations- und Konzentrationsübungen sind es, die dem Men­schen eine andere Anschauung geben sollen, eine Anschau­ung, die er nicht mit dem Verstande und den fünf Sinnen erwerben kann.",
        "Die Meditation führt zunächst weg von der sinnlichen Auffassung.",
        "Durch innere seelische Arbeit wird da der Mensch frei von den Sinnen.",
        "Etwas Ahnliches geht da im Menschen vor sieh wie bei der Operation eines Blindgeborenen.",
        "Eine Art Operation findet statt, die geistige Augen und Ohren öffnet.",
        "Diese Entwicklung wird in längerer"
      ],
      [
        "Zeit die ganze Menschheit erreichen.",
        "Das Weltliche darf man darum aber nicht verleugnen, wenn man sieh höher entwickeln will.",
        "Weltflüchtige Askese taugt nicht fürs Hellsehen.",
        "Hellsehen ist die Frucht dessen, was die Seele in der Sinnenwelt sammelt.",
        "Schön verglich die griechische Philosophie die Mensehenseele mit einer Biene.",
        "Die Welt von Farben und Licht bietet der Seele den Honig, den sie mitbringt in die höhere Welt.",
        "Sinnenerfahrung muß die Seele vergeistigen und hinauftragen in höhere Welten."
      ],
      [
        "Welche Aufgabe hat nun die Seele, die frei ist vom Leibe?",
        "Wir treffen hier auf einen wichtigen Grundsatz.",
        "Jedes Wesen wird, wenn es sich herausentwickelt hat, auf einer höheren Stufe Leiter und Führer derjenigen Wesen und Formen, durch die es durchgegangen ist.",
        "Wir sehen da ein Zukunftsbild.",
        "Wenn der Mensch sieh so vergeistigt haben wird, daß er den physischen Leib nicht mehr braucht, wirkt der Mensch als geistiger Leiter von außen auf die Welt ein.",
        "Dann ist die Aufgabe dieses Planeten erfüllt.",
        "Er geht dann zu einer anderen Verkörperung über.",
        "Die Erde wird dann ein neues planetarisches Dasein erhalten.",
        "Die Menschen werden dann die Götter des neuen Planeten sein.",
        "Der Mensdiheitsleib, der verlassen ist vom Geist, wird nie­deres Reich sein.",
        "Wir tragen jetzt eine doppelte Natur in uns: das, was herrschen wird auf dem nächsten Planeten, und das, was das niedere Reich sein wird.",
        "So wie die Erde sich neu verkörpern wird, so hat sie sich auch herausgebildet aus früheren Entwicklungsvorgängen, und so wie die Men­schen die Götter des nächsten Planeten sein werden, so waren die uns jetzt leitenden Wesenheiten Menschen auf dem vor­hergehenden Planeten, und sie hatten als Niederes das, was wir Menschen auf der Erde sind.",
        "Damit finden wir den Zu­sammenhang der Erde mit Vorgängen, die in der Vergan­genheit und in der Zukunft liegen.",
        "Die Stufe, die der Mensch"
      ],
      [
        "heute auf der Erde hat, hatten einstmals die Wesen, die die Schöpfer und Führer der Menschen heute sind, die Elohim­Geister, die sich offenbaren als Führer der Entwicklung des Menschen.",
        "Und die Menschen werden auf dem zukünftigen Planeten so weit sein, daß sie selbst Lenker und Leiter sind."
      ],
      [
        "Aber man muß nicht denken, es müsse sich nun genau so wiederholen; dasselbe wiederholt sieh nie.",
        "Nichts geschieht zweimal in der Welt.",
        "Nie war das Dasein so wie jetzt auf der Erde.",
        "Das Erdendasein bedeutet den Kosmos der Liebe, das Dasein auf dem früheren Planeten bedeutet den Kos­mos der Weisheit."
      ],
      [
        "Die Liebe vom Elementarsten bis zum Höchsten sollen wir entwickeln.",
        "Die Weisheit ruht ver­borgen auf dem Grunde des Erdendaseins.",
        "Darum soll man nicht von der «niederen» physischen Menschennatur spre­chen, denn sie ist gewissermaßen die vollkommenste Form des Menschen."
      ],
      [
        "Man betrachte den weisheitsvollen Bau eines Knochens, zum Beispiel des Oberschenkelknochens.",
        "Da ist das Problem: mit dem geringsten Aufwand von Material und Kraft die größtmöglichste Gewiehtsmasse zu tragen, in vollkommenster Art gelöst."
      ],
      [
        "Man schaue sich den Wunder-bau des Herzens, des Gehirns an!",
        "Der Astralleib steht nicht etwa höher.",
        "Er ist der Genießer, der fortwährende Attacken auf das weisheitsvoll gebaute Herz macht.",
        "Er wird noch lange brauchen, um so vollkommen und weise zu sein wie der physische Leib."
      ],
      [
        "Aber er muß es werden.",
        "Darin besteht die Entwicklung.",
        "Auch der physische Leib mußte sich so entwickeln.",
        "Was weise an ihm ist, mußte aus Unweisheit und Irrtum hervorgehen.",
        "Die Weisheitsentwicklung ging der Liebesentwicklung voraus."
      ],
      [
        "Die Liebe ist noch nicht voll­kommen.",
        "Aber in der ganzen Natur ist sie zu finden.",
        "Bei der Pflanze, beim Tier, beim Menschen, von der niedersten Geschlechtsliebe an bis zur höchsten, vergeistigtesten Liebe."
      ],
      [
        "Ungeheure Mengen von Wesen, die der Liebestrieb hervorgebracht,"
      ],
      [
        "gehen im Kampf ums Dasein zugrunde.",
        "Kampf wirkt überall da, wo Liebe ist.",
        "Das Auftreten der Liebe bringt Kampf, notwendigen Kampf mit sieh.",
        "Aber sie wird ihn auch überwinden, wird den Krieg in Harmonie ver­wandeln."
      ],
      [
        "Weisheit ist das Charakteristikum der physischen Natur.",
        "Da, wo diese Weisheit von Liebe durchsetzt ist, da erst ist der Anfang der Erdentwicklung.",
        "Wie heute Kampf auf der Erde ist, war auf dem früheren Planeten Irrtum zu finden.",
        "Merkwürdige Fabelwesen wandelten da umher, Irrtümer der Natur, die nicht entwicklungsfähig waren.",
        "Wie Liebe aus Lieblosem hervorgeht, so die Weisheit aus Unweisheit.",
        "Die, welche die Erdentwicklung erreichen, werden die Liebe als eine Naturkraft in den nächsten Planeten hinein­bringen.",
        "So ward auch einst die Weisheit auf die Erde ge­tragen.",
        "Die Menschen der Erde schauen auf zu den Göttern als zu den Bringern der Weisheit.",
        "Die Menschen des folgen­den Planeten werden zu den Göttern als zu den Bringern der Liebe aufschauen.",
        "Die Weisheit wird den Menschen als göttliche Offenbarung von den Menschen des früheren Planeten zuteil.",
        "Alle Reiche der Welt hängen unter sich zusammen.",
        "Wenn es keine Pflanzen gäbe, so würde in kur­zer Zeit die Lebensluft verpestet sein; denn Mensch und Tier atmen Sauerstoff ein und lebenvernichtende Kohlen­säure wieder aus.",
        "Doch die Pflanzen atmen Kohlensäure ein und geben Sauerstoff von sich.",
        "So hängt hier hinsichtlich der Lebensluft das Höhere vom Niederen ab."
      ],
      [
        "So ist es nun in allen Reichen.",
        "Wie das Tier und der Mensch von der Pflanze, so sind wieder die Götter von den Menschen abhängig.",
        "Das hat die griechische Mythe so schön ausgedrückt: Die Götter erhalten von den Sterblichen Nek­tar und Ambrosia.",
        "Beide bedeuten die Liebe.",
        "Die Liebe wird innerhalb des Menschengeschleehtes erzeugt.",
        "Und Liebe"
      ],
      [
        "atmet das Göttergeschlecht ein, sie ist die Götternahrung.",
        "Die Liebe, die von den Menschen erzeugt wird, wird den Göttern Speise.",
        "Das ist viel wirklicher als etwa die Elek­trizität, so seltsam es zuerst erscheint.",
        "Die Liebe tritt zu­erst als Geschleehtsliebe auf und entwickelt sich hinauf bis zur höchsten geistigen Liebe.",
        "Aber alle Liebe, niedere und hohe, ist Götteratem.",
        "Nun kann man sagen: Wenn das alles so ist, kann es kein Böses geben.",
        "Aber Weisheit liegt der Welt zugrunde, Liebe entwickelt sich.",
        "Weisheit wird die Lenkerin der Liebe.",
        "So wie alle Weisheit aus Irrtum ge­boren wird, ringt sieh alle Liebe nur aus Kämpfen zur Höhe empor."
      ],
      [
        "Nicht alle Wesen des früheren Planeten stiegen zur Höhe der Weisheit hinan.",
        "Es sind Wesen zurückgeblieben, sie stehen ungefähr zwischen Göttern und Menschen.",
        "Sie brau­chen noch etwas vom Menschen.",
        "Aber in einen physischen Körper können sie sich nicht mehr kleiden.",
        "Luziferische Wesenheiten nennt man sie, oder man faßt sie zusammen unter dem Namen Luzifer als ihrem Anführer.",
        "Wie wirkt nun Luzifer auf die Menschen?",
        "Nicht so wie die Götter.",
        "Das Göttliche tritt an das Edelste im Menschen heran, aber an das Niedere kann und soll es nicht kommen.",
        "Weisheit und Liebe werden erst am Ende der Entwicklung ihre Ver­mählung feiern.",
        "Aber die luziferischen Wesenheiten treten an das niedere, unentwickelte Element der Liebe heran.",
        "Sie bilden die Brücke zwischen Weisheit und Liebe.",
        "So erst mischt sich die Weisheit mit der Liebe.",
        "Das, was sieh nur ans Unpersönliche wendet, verstrickt sich so mit der Per­sönlichkeit.",
        "Auf dem früheren Planeten war die Weisheit ein Instinkt, wie es heute die Liebe ist.",
        "Ein schöpferischer Weisheitsinstinkt war herrschend, wie heute ein schöpfe­rischer Liebesinstinkt.",
        "Früher hatte also die Weisheit den Menschen instinktmäßig geführt.",
        "Dadurch aber, daß die"
      ],
      [
        "Weisheit heraustrat und nicht mehr führte, ward der Mensch selbstbewußt, er wußte sieh als ein selbständiges Wesen.",
        "Im Tier ist die Weisheit noch instinktmäßig, daruni ist es noch nicht selbstbewußt.",
        "Aber die Weisheit wollte den Men­schen nun von außen lenken und leiten, ohne daß die Liebe einen Zusammenhang damit hatte."
      ],
      [
        "Da Luzifer kam, pflanzte er die menschliche Weisheit in die Liebe.",
        "Und die mensch­liche Weisheit schaut auf zur göttlichen Weisheit.",
        "Im Men­schen ward die Weisheit zum Enthusiasmus, zur Liebe selbst.",
        "Hätte nur die Weisheit ihren Einfluß ausgeübt, so wäre der Mensch nur gut geworden, er hätte die Liebe nur zum Aufbau des Erdenbewußtseins gebraucht."
      ],
      [
        "Aber Luzifer brachte die Liebe mit dem Selbst in Verbindung, zum Selbst­bewußtsein trat die Selbstliebe.",
        "Das wird schön im Para­diesesmythus ausgedrückt: «... und sie sahen, daß sie nackend waren», das heißt, damals sahen die Menschen zum ersten Male sich selbst, vorher hatten sie nur die Um­welt gesehen."
      ],
      [
        "Da hatten sie nur ein Erdenbewußtsein, aber kein Selbstbewußtsein.",
        "Nun konnten die Menschen die Weisheit in den Dienst des Selbst stellen.",
        "Selbstlose Liebe zur Umwelt und Liebe zum Selbst gab es von nun an."
      ],
      [
        "Und die Selbstliebe war böse und die Selbstlosigkeit war gut.",
        "Nie hätte der Mensch ein warmes Selbstbewußtsein bekom­men ohne Luzifer.",
        "Denken und Weisheit traten nun in den Dienst des Selbst.",
        "Nun gab es eine Wahl zwischen gut und böse."
      ],
      [
        "Nur um das Selbst in den Dienst der Welt zu stellen, darf Liebe zum Selbst hinzutreten.",
        "Nur wenn die Rose den Garten zieren will, darf sie sich selbst schmücken.",
        "Das muß man sich bei einer höheren, okkulten Entwicklung tief in die Seele schreiben."
      ],
      [
        "Um das Gute fühlen zu können, mußte der Mensch auch das Böse fühlen können.",
        "Enthusiasmus für das Höhere gaben ihm die Götter.",
        "Aber ohne das Böse konnte es kein Selbstgefühl, keine freie Wahl des Guten,"
      ],
      [
        "keine Freiheit geben.",
        "Das Gute konnte ohne Luzifer ver­wirklicht werden, die Freiheit nicht.",
        "Um das Gute wählen zu können, muß der Mensch auch das Böse vor sich haben, es muß ihm innewohnen als Kraft der Selbstliebe.",
        "Aber die Selbstliebe muß zur All-Liebe werden.",
        "Dann wird das Böse überwunden sein.",
        "Freiheit und das Böse entspringen aus demselben Punkt.",
        "Luzifer enthusiasmiert den Menschen menschlich für das Göttliche.",
        "Luzifer ist der Träger des Lichts.",
        "Elohim ist das Licht selbst.",
        "Hat das Lieht der Weis­heit die Weisheit im Menschen entzündet, so hat Luzifer das Licht in den Menschen hineingetragen.",
        "Aber der schwarze Schatten des Bösen mußte sich hineinmischen.",
        "Luzifer bringt eine eingeschränkte, fleckenerfüllte Weisheit, aber diese kann in den Menschen eindringen.",
        "Luzifer ist der Träger der äußeren, menschlichen Wissenschaft, die ja im Dienste des Egoismus steht.",
        "Darum wird vom okkulten Schüler Selbstlosigkeit gegenüber dem Wissen verlangt.",
        "Dies ist der Ursprung des Bösen in der menschlichen Entwicklung.",
        "Was der Sauerteig des alten Brotteiges für das neue Brot ist, das ist vom früheren Planeten Luzifer für uns.",
        "Das Böse wird gut an seinem Ort.",
        "Bei uns ist es nicht mehr gut.",
        "Das Böse ist ein versetztes Gutes.",
        "Das absolut Gute eines Planeten bringt in einem seiner Teile zum neuen Planeten immer auch das Böse mit.",
        "Das Böse ist ein notwendiger Entwick­lungsgang."
      ],
      [
        "Man darf nicht sagen, die Welt sei unvollkommen, weil das Böse in ihr ist.",
        "Vielmehr ist sie gerade darum vollkom­men.",
        "Wenn in einem Gemälde herrliche Lichtgestalten und böse Teufelsfratzen zugleich dargestellt sind, so würde man das Bild doch vernichten, wenn man die Teufelsfratzen herausschneiden wollte.",
        "Die Weltenschöpfer brauchten das Böse, um das Gute zur Entfaltung zu bringen.",
        "Was sich erst am Felsen des Bösen brechen muß, ist ein Gutes.",
        "Durch"
      ],
      [
        "Selbstliebe nur kann es die All-Liebe zu ihrer höchsten Blüte bringen.",
        "Darum hat Goethe so recht, wenn er im Faust den Mephisto sagen läßt:"
      ],
      [
        "«Ich bin ein Teil von jener Kraft,"
      ],
      [
        "die stets das Böse will und stets das Gute schafft.»"
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "WIE BEGREIFT MAN KRANKHEIT UND TOD? Berlin, 13. Dezember 1906",
    "paragraphs": [
      "Heute haben wir es mit einem Thema zu tun, das zwei­fellos jedem Menschen nahegeht, denn die beiden Worte «Krankheit und Tod» drücken etwas aus, was sich in jedes Leben hineinstellt, oftmals wie ein unerbetener Gast, oft aber auch als etwas Quälendes, Beengendes, Furchtmachen­des. Ja, der Tod stellt sieh als die größte Rätselfrage ins Dasein hinein, so daß, wenn jemand die Frage nach dem Wesen des Todes gelöst hat, für ihn dann wohl auch die Frage nach dem Wesen des Lebens gelöst ist. Oft hört man sagen: Der Tod bildet ein Rätsel, noch keiner hat es gelöst, und auch keiner wird es je lösen. - Die Menschen, die der­gleichen aussprechen, ahnen gar nicht, welche Unbescheiden­heit in diesen Worten liegt, sie ahnen gar nicht, daß es eine Lösung solcher Rätselfragen gibt und daß sie es nur nicht verstehen. Heute, wo wir es mit einem so umfassend wich­tigen Ding zu tun haben, bitte ich Sie, ganz besonders dar­auf zu achten, daß es sich um nichts anderes handeln kann, als um eine Beantwortung der gestellten Frage: Wie begreift man Krankheit und Tod? Wir können uns daher nicht auf spezielle Fragen über Krankheiten und Gesundheit einlas­sen, sondern müssen uns im wesentlichen an die Frage hal­ten: Wie erlangt man ein Verständnis für diese zwei wich­tigen Fragen unseres Daseins?",
      "Die bekannteste Antwort auf die Frage nach dem Wesen des Todes, die Jahrhunderte hindurch geltend war, heute aber für den weitaus größten Teil der Gebildeten der Menschheit",
      "ihren Wert eingebüßt hat, liegt vor in den Worten des Paulus: «Denn der Tod ist der Sünde Sold.» Wie gesagt, viele Jahrhunderte hindurch war dieses Wort eine Art Lö­sung des Rätsels des Todes. Heute wird derjenige, der im modernen Sinne denkt, mit einer solchen Antwort überhaupt nichts anfangen können, denn daß die Sünde etwas völlig Moralisches, etwas rein im Wesen des menschlichen Verhal­tens Liegendes, die Ursache einer physischen Tatsache, wie der Tod es ist, sein könnte oder irgendwie mit dem Wesen der Krankheit zusammenhängen sollte, das ist für einen heutigen Denker ganz unerfindlich.",
      "Es wird uns vielleicht noch nützlich sein, wenn wir auch darauf hinweisen, daß unsere Gegenwart nicht einmal mehr den Wortlaut des Satzes: «Denn der Tod ist der Sünde Sold» versteht. Denn unter «Sünde» verstanden Paulus und die, welche zu seiner Zeit lebten, ganz und gar nicht das, was man heute im philiströsen Sinne darunter versteht. Nicht eine Verfehlung im gewöhnlichen Sinne ist hier mit Sünde gemeint, auch nicht eine Verfehlung radikaler Art, sondern unter Sünde wird da verstanden, was aus Selbst­sucht und Egoismus hervorgeht. Alles, was Selbstsucht und Egoismus zum Antriebe des Handelns hat - im Gegensatz zu dem, was sachlichen, objektiven Impulsen entspringt -, ist Sünde. Der Egoismus, das selbstische Handeln, aber setzt voraus, daß der Mensch selbständig, ich-bewußt geworden ist. Das muß man erkennen, wenn man sich ganz und gar auf die Denkweise eines solchen Geistes wie Paulus einläßt.",
      "Wer nicht an der Oberfläche des Verständnisses der alt-und neutestamentlichen Urkunden bleibt, sondern wirklich in ihren Geist eindringt, der weiß, daß eine ganz bestimmte, man möchte sagen naturphilosophische Denkweise die Un­terströmung dieser alt- und neutestamentlichen Denkweise bildet. Diese Unterströmung ist etwa die folgende: Alles,",
      "was an Lebensschöpfung in der Welt vorhanden ist, richtet sich nach einem ganz bestimmten Ziel hin. Die niederen Wesen sind noch neutral gegen Lust und Leid, Freude und Schmerz. Wir finden dann, wie sich das Leben steigert und etwas damit verbunden wird. Derjenige, dem schaudert, wenn man von Zielstrebigkeit spricht, der möge bedenken, daß hier nicht eine Theorie gedacht ist, sondern daß es sich hier um eine reine Tatsache handelt: das ganze Reich der Lebewesen bis zum Menschen hinauf nähert sieh einer be­stimmten Tatsache, die sich darin zeigt, daß an der Spitze der Lebewesen ein persönliches Bewußtsein möglich ist.",
      "Es schaute der Eingeweihte des Alten und Neuen Testa­mentes hinunter ins Reich der Tiere und sah, wie alles dahin strebt, daß einmal eine freie Persönlichkeit zustande kom­men kann, die aus sieh selbst heraus die Antriebe und Im­pulse zum Handeln haben kann, und wie mit dem Wesen einer solchen Persönlichkeit das verbunden ist, was man die Möglichkeit einer egoistischen, selbstsüchtigen Handlung nennt. Nun aber würde ein Denker wie Paulus sagen: Wenn in einem Leibe eine solche Persönlichkeit wohnt, die ego­istisch zu handeln imstande ist, so muß dieser Leib sterblich sein. In einem unsterblichen Leibe würde niemals eine Seele mit Selbständigkeit, Selbstbewußtsein und folglich auch mit Egoismus wohnen können. Daher gehören zusammen: ein sterblicher Leib und eine Seele mit Persönlichkeitsbewußt­sein und die einseitige Ausbildung der Persönlichkeit zu Handlungsimpulsen. Das heißt die Bibel «Sünde», und so definiert Paulus: «Der Tod ist der Sünde Sold». Da sehen Sie allerdings, daß wir diesen, wie jeden anderen Ausspruch der Bibel modifizieren müssen, weil sie im Laufe der Jahr­hunderte ganz in ihr Gegenteil umgekehrt worden sind. Modifiziert man sie, nicht indem man sie umdeutet, sondern indem man sich klarmacht, daß man den gegenwärtigen",
      "Sinn, den die Theologie gibt, in den ursprünglichen verwan­delt, so sieht man daraus, daß man es oftmals mit einer sehr tiefen Auffassung der Sache zu tun hatte, die dem gar nicht so fernsteht, was man heute wieder begreifen kann. Dies zur notwendigen Richtigstellung.",
      "Aber es haben sich ja die Denker, die Weltanschauungs­forscher aller Zeiten mit der Frage nach dem Rätsel des Todes beschäftigt, und wir finden diese Frage seit Jahrtau­senden scheinbar in der mannigfaltigsten Weise beantwor­tet. Wir können uns hier nicht mit einer geschichtlichen Be­trachtung einer solchen Lösung befassen, daher sei nur auf zwei Denker hingewiesen, damit Sie sehen, wie selbst der Gegenwart recht nahestehende Denker nichts Erhebliches zu dieser Frage beizubringen wissen.",
      "Der eine ist Schopenhauer. Sie kennen ja alle seine pessi­mistische Art zu denken, und wer einmal den Satz durch­gegangen ist: «Das Leben ist eine mißliche Sache, und ich habe mir vorgenommen, das meinige damit hinzubringen, über dasselbe nachzudenken» - der wird begreifen, daß Schopenhauer kaum zu einer anderen Lösung gekommen ist als zu der: Eigentlich tröstet der Tod über das Leben und das Leben über den Tod; das Leben ist eine fatale Sache, und man könnte es nicht ertragen, wenn man nicht wüßte, daß der Tod es schließen würde; und wenn man die Furcht vor dem Tode hat, dann braucht man sich nur einmal klarzu-machen, daß das Leben nicht besser sei und daß durch den Tod nichts weiter beschlossen ist. Das ist seine pessimistische Art zu denken, die nur einmal darüber hinausführt, wo er den Erdgeist sagen läßt: Ihr wollt, daß immer neues Leben entsteht, da muß ich Platz haben. Also sieht Schopenhauer in einer gewissen Beziehung in der Tatsache, daß das Leben sich fortpflanzt, immer neues Leben gebiert, die Notwen­digkeit, daß das Alte sterben müsse, damit für das Neue",
      "Raum sei. Sonst weiß auch Schopenhauer gar nichts Erheb­liches vorzubringen; denn alles, was er sonst sagt, atmet in diesen zwei Worten.",
      "Der andere ist Eduard von Hartmann. Er hat sich noch in seinem letzten Buche mit dem Rätsel des Todes beschäf­tigt. Er sagt da: Wenn wir uns das zunächst höchste Lebe­wesen betrachten, so finden wir, daß der Mensch, nachdem wieder ein oder zwei neue Generationen heraufgezogen sind, die Welt nicht mehr versteht. Wenn der Mensch alt geworden ist, kann er die Jugend nicht mehr fassen, daher ist es not­wendig, daß das Alte absterbe und Neues wieder hervor­komme. - Sie sehen jedenfalls auf diese Fragen auch keine Antwort, die uns mit wirklichem Verständnis dem Rätsel des Todes näherbringen könnte.",
      "So wollen wir einmal in die heutigen, gegenwärtigen Welt­anschauungen hineinstellen, was die sogenannte Geisteswis­senschaft, dieman heute auch Anthroposophie nennt, über die Ursachen von Tod und Krankheit zu sagen hat. Wir wollen uns aber dabei eines klarmachen: der Geisteswissenschaft geht es nicht so gut wie den anderen Wissenschaften, daß sie in einer bestimmten Weise über alles sprechen kann. Der heutige Naturforscher würde es nicht begreifen, daß man, wenn man über Krankheit und Tod spricht, trennen muß zwischen Tier und Mensch, daß man aber gerade, wenn man die Frage des heutigen Vortrages begreifen will, sich wird auf die Erscheinungen beim Menschen beschränken müssen. Da die Wesen nicht nur das abstrakte «Gleiche» miteinander haben, sondern auch jedes sein Wesentliches und seine Eigen­art hat, so wird nur einiges von dem, was heute gesagt wird, auch auf die Tierwelt anzuwenden sein, vielleicht auch auf die Pflanzen; im wesentlichen aber wird über den Menschen gesprochen werden, und die anderen Dinge werden nur herangezogen werden, wenn sie etwas erklären sollen.",
      "Wenn wir Tod und Krankheit beim Menschen erfassen wollen, müssen wir vor allen Dingen darauf sehen, daß der Mensch im Sinne der Geisteswissenschaft ein höchst kom­pliziertes Wesen ist und daß wir den Menschen seinem Wesen nach aus den folgenden vier Gliedern heraus begreifen müssen: erstens haben wir den äußerlich sichtbaren physi­schen Körper, als zweites den Ather- oder Lebensleib, so­dann den Astralleib, und als viertes das Ich des Menschen oder den Mittelpunkt seines Wesens. Dann müssen wir uns klar sein, daß im physischen Leibe dieselben Kräfte und Stoffe vorhanden sind wie in der physischen Welt draußen und daß in dem Atherleib das liegt, was diese Stoffe zum Leben aufruft, und daß der Mensch seinen Atherleib mit der ganzen Pflanzenwelt gemeinschaftlich hat. Der Astral­leib, den der Mensch mit den Tieren gemein hat, ist der Trä­ger des ganzen Gefühlslebens, von Begierden, Lust und Un­lust, Freude und Schmerz. Das Ich hat der Mensch ganz für sich allein, das macht ihn zur Krone der Erdenschöpfung.",
      "Wenn wir den Menschen als physischen Organismus vor uns haben, dann müssen wir uns klarmachen, daß innerhalb dieses physischen Organismus die drei anderen Glieder als Bildner und Architekten arbeiten. Das physische Prinzip arbeitet nur teilweise am physischen Organismus des Men­schen, in einem anderen Teil ist im wesentlichen der Äther-leib tätig, wieder in einem anderen der Astralleib, und wie­derum in einem anderen Teil des Menschen ist das Ich tätig. Der Mensch besteht für die Geisteswissenschaft physisch erst einmal aus Knochen, Muskeln, denjenigen Organen, die den Menschen stützen, ihn zu einem festen, auf der Erde gehen­den Gebilde machen; diese allein rechnet man im strengsten Sinn der Geisteswissenschaft zu dem durch das physische Prinzip zustande gekommenen Teil der Organe. Dazu kom­men noch die eigentlichen Sinnesorgane; dabei haben wir es",
      "mit physikalischen Apparaten zu tun; beim Auge mit einer Art camera obscura, beim Ohr mit einem sehr komplizier­ten Musikinstrument. Es kommt nun darauf an, woraus diese Organe gebaut sind. Sie sind von dem ersten Prinzip gebaut. Dagegen sind alle Organe, die mit Wachstum, Fort­pflanzung, Verdauung und anderem zusammenhängen, nicht bloß im Sinne des physischen Prinzips gebaut, sondern im Sinne des Äther- oder Lebensleibes, der ja auch die physi­schen Organe durchdringt. Nur der gesetzmäßige Aufbau wird vom physischen Prinzip besorgt, der Vorgang von Verdauung, Fortpflanzung und Wachstum dagegen wird vom Ätherprinzip besorgt. Der Astralleib ist der Schöpfer des ganzen Nervensystems, bis hinauf zum Gehirn und zu den Strängen, die in Form von Sinnesnervensträngen zum Gehirn gehen. Das Ich endlich ist der Architekt des Blut­kreislaufes. Wenn wir also in echt geisteswissenschaftlichem Sinne einen menschlichen Organismus vor uns haben, so sind wir uns klar, daß diese vier Glieder - auch im äußerlich wahrnehmbaren Organismus - eigentlich wie vier ganz voneinander verschiedene Wesenheiten im Menschen ver­schmelzen und miteinander wirksam gemacht worden sind. Diese Glieder, die den menschlichen Organismus zusammen­setzen, sind von ganz verschiedenem Werte, und wir wer­den ihre Bedeutung für den Menschen begreifen, wenn wir erforschen, wie die Entwicklung des Menschen mit diesen einzelnen Gliedern zusammenhängt.",
      "Heute sei mehr vom physiologischen Gesichtspunkt aus besprochen, was man die Arbeit des physischen Prinzips im menschlichen Organismus nennt. Das wird geleistet in der Epoche von der Geburt bis zum Zahnwechsel. Da arbeitet das physische Prinzip am physischen Leibe so, wie die Kräfte und Stoffe des mütterlichen Organismus am Kindeskeim arbeiten, bevor das Kind geboren ist. Vom siebenten Jahre",
      "bis zur Geschlechtsreife arbeitet am physischen Leibe haupt­sächlich das Ätherprinzip, und von der Geschlechtsreife an arbeiten die Kräfte, die innerhalb des Astralleibes verankert sind. So daß wir uns die Entwicklung des Menschen recht vorstellen, wenn wir uns denken, daß der Mensch bis zur Geburt vom Leibe der Mutter umschlossen ist.",
      "Mit der Ge­burt drängt er gleichsam den mütterlichen Leib zurück, seine Sinne werden frei, und nun ist es möglich, daß die äußere Welt anfängt, auf den menschlichen Organismus einzuwir­ken. Da stößt der Mensch auch eine Hülle von sich, und derjenige erst begreift richtig die Entwicklung des Menschen, der begreift, daß zwar nicht im physischen, aber im geisti­gen Leben etwas Ähnliches in der Zeit des Zahnwechsels vor sich geht.",
      "Um das siebente Jahr herum wird der Mensch richtig ein zweites Mal geboren. Da wird nämlich sein Äther-leib zur freien Tätigkeit geboren, wie sein physischer Leib zur Zeit der Geburt. So wie physisch der Mutterleib an dem Menschenkeim in der Zeit vor der Geburt arbeitet, so arbeiten geistige Kräfte des Weltenäthers bis zum Zahn-wechsel an dem Ätherleib des Menschen, und sie werden um das siebente Jahr herum ebenso zurückgedrängt wie der Mutterleib bei der physischen Geburt.",
      "Bis zum siebenten Jahre liegt der Ätherleib wie latent im physischen Leibe. Wie bei einem in Brand gesetzten Zündholz ist es mit dem Ätherleib um die Zeit des Zahnwechsels herum. Er ist im physischen Leibe darinnen gebunden und kommt nun her­aus zur eigenen, freien, selbständigen Tätigkeit.",
      "Und das Zeichen, wodurch sich diese freie Tätigkeit des Ätherleibes ankündigt, ist gerade der Zahnwechsel. Der Zahnwechsel hat für den, der tiefer in die Natur des Menschen hinein-schaut, eine ganz bedeutsame Stellung.",
      "Haben wir einen Menschen bis zum siebenten Jahr vor uns, so arbeitet das physische Prinzip frei im physischen Leib; aber gebunden",
      "und aus den geistigen Hüllen noch nicht herausgeboren ist das Äther- und das astrale Prinzip.",
      "Wenn wir den Menschen bis zum siebenten Jahr betrach­ten, so enthält er eine ganze Summe von Vererbungstat­sachen, die er nicht mit seinem eigenen Prinzip erbaut hat, sondern die er von den Vorfahren ererbt erhalten hat. Dazu gehört das, was man die Milchzähne nennt. Erst die Zähne, die nach dem Zahnwechsel kommen, sind im Kinde die eigene Schöpfung des Prinzips, das als physisches dazu veranlagt ist, die feste Stütze zu bilden. Was in den Zähnen zum Ausdruck kommt, schafft bis zum Zahnwechsel im In­nern, und es bildet am Ende seiner Wirksamkeit gleichsam den Schlußpunkt und bringt den härtesten Teil des Stütz­organes in den Zähnen hervor, weil es noch den Äther- oder Lebensleib als Wachstumsträger in sich gebunden hält.",
      "Nachdem dieses Prinzip abgestoßen ist, wird der Äther-leib frei und schafft jetzt an den physischen Organen bis zur Geschlechtsreife, und dann wird ebenso eine Hülle, die äußere astrale Hülle, weggedrängt wie bei der Geburt die Mutterhülle. Astralisch wird der Mensch bei der Geschlechts-reife zum dritten Male geboren. Und die wirkenden Kräfte, die im Ätherleib gebunden waren, machen jetzt für ihre Schöpfungsart im Menschen den Schlußpunkt, indem sie die Fähigkeit der Geschleditsreife, der Fortpflanzung, und ihre Organe erzeugen. So wie das physische Prinzip im sieben­ten Jahre durch die Zähne den Schlußpunkt macht, indem es die letzten harten Organe schafft, und wodurch der Äther-leib, das Wachstumsprinzip, frei wird, so schafft das astrale Prinzip in dem Moment, wo es frei wird, die stärkste Kon­zentration der Triebe und Begierden, der Lebensäußerung, insofern wir es mit der physischen Natur zu tun haben. Wie Sie das physische Prinzip wie konzentriert in den Zähnen haben, so das Wachstumsprinzip in der Geschlechtsreife. Da",
      "ist der Astralleib, die Umhüllung des Ich frei, und das Ich arbeitet nun am Astralleib.",
      "Der europäische Kulturmenseh folgt nicht bloß seinen Trieben und Begierden; er hat sie geläutert und umge­wandelt in moralische Empfindungen und ethische Ideale. Vergleichen wir nun einen Wilden mit einem europäischen Durchschnittsmenschen oder gar mit einem Schiller oder Franz von Assisi, so können wir sagen, daß diese ihre Triebe vom Ich aus umgestaltet, geläutert haben. So können wir uns sagen, daß dieser Astralleib stets zwei Teile enthält:",
      "einen, der aus der ursprünglichen Anlage herrührt, und einen, den das Ich selbst geboren hat. Nun verstehen wir die Arbeit des Ich nur dann, wenn wir uns klarmachen, daß der Mensch einer Wiederverkörperung - wiederholten Er­denleben - unterliegt; daß der Mensch, wenn er geboren wird, gleichsam in vier voneinander geteilten Leibern sich die Früchte und Ergebnisse früherer Erdenleben mitbringt, die als ein Maß für die Energie und Kraft seines Lebens da sind. Der eine Mensch wird geboren, weil er es früher dazu gebracht hat, mit viel Lebensenergie, mit starken Kräften seinen Astralleib umzugestalten. Der andere wird darin bald erlahmen. Wenn man hellsehend untersuchen kann, wie das Ich beginnt, an dem Astralleibe frei zu arbeiten, die Begierden, Triebe und Leidenschaften vom Ich aus zu be­herrschen, dann könnte man, wenn man das Maß von Ener­gie, das das Ich sich mitgebracht hat, anzugeben vermag, sagen: dieses Maß ist so groß, daß das Ich so und so lange an seiner Umgestaltung an sich arbeiten wird und nicht mehr. Und nach der Zeit der Gesehlechtsreife gibt es für jeden Menschen ein solches Maß, durch das man messen kann und angeben könnte, bis wann er alles aus seinem Astralkörper herausgearbeitet hat nach den ihm in diesem Leben zugeteilten Pfunden. Was der Mensch so in seinem",
      "Gemüt an Lebenskräften umzugestalten und zu läutern ver­mag, erhält sich selbst. Solange dieses Maß ausreicht, lebt er auf Kosten des sich selbst erhaltenden Astralleibes. Ist er erschöpft, findet er keinen Mut mehr, neue Triebe umzu­gestalten, kurz, keine Energie, an sieh zu arbeiten, dann reißt der Lebensfaden ab, - und er muß nach einem Maße, das jedem Menschen zuerteilt ist, einmal abreißen. Dann ist die Zeit gekommen, wo der Astralleib seine Kräfte von dem Prinzip des menschlichen Lebens nehmen muß, das ihm zunächst liegt, vom Ätherleib. Und jetzt kommt die Zeit, wo der Astralleib auf Kosten der im Ätherleib aufgespei­cherten Kraft lebt; der Ausdruck dafür ist für den Menschen da, wenn sein Gedächtnis, seine produktive Einbildungs-kraft allmählich schwindet.",
      "Wir haben öfter hier gehört, daß der Ätherleib der Trä­ger der produktiven Phantasie und des Gedächtnisses ist, dessen, was man Lebenshoffnung und Lebensmut nennt. Diese Gefühle, wenn sie zu seinem bleibenden Element wer­den, haften an dem Ätherleib. Sie werden jetzt von dem Astralleib herausgesogen; und nachdem der Astralleib so auf Kosten des Ätherleibes gelebt und alles, was dieser her­zugeben hatte, ausgesogen hat, beginnt die Zeit, wo die schöpferischen Kräfte des physischen Leibes vom Astralleib aufgezehrt werden. Und sind diese herausgezehrt, dann schwindet die Lebenskraft des physischen Leibes, der Kör­per verhärtet sich, der Puls wird langsamer. Da zehrt der Astrall eib zuletzt auch noch am physischen Leibe und nimmt ihm die Kraft weg. Und hat er die aufgezehrt, dann ist keine Möglichkeit mehr, daß aus dem physischen Prinzip heraus der physische Leib erhalten werden kann.",
      "Soll der Astralleib es dahin bringen, daß er frei werden und zu dem Leben und der Arbeit des Ich geboren werden soll, dann ist es notwendig, daß in der zweiten Hälfte des",
      "Lebens der freigewordene Astralleib, wenn das Maß der Arbeit ersehöpft ist, seine Hüllen geradeso wie sie gebildet worden sind, selber wieder aufzehrt. So ist das individu­eIle Leben vom Ich heraus geschaffen.",
      "Zum Gleichnis diene Folgendes: Denken Sie sich ein Stück Holz, das Sie anzünden. Wäre es nicht so, wie es ist, so würden Sie es nicht anzünden können. Die Flamme quillt aus dem Holz hervor, aber sie zehrt es zu gleicher Zeit auf. Das ist das Wesen der Flamme, daß sie aus dem Holz her­aus frei wird und den eigenen Mutterboden aufzehrt. So wird der Astralleib dreifach herausgeboren, so zehrt er, wie die Flamme das Holz, seine eigene Grundlage auf; und darin besteht die Möglichkeit, daß das individuelle Leben da sein kann, weil es seine Grundlage wieder aufzehrt. Der Tod ist ihm die Wurzel des Lebens, und es könnte gar kein bewußt individuelles Leben geben, wenn es nicht den Tod gäbe. Wir verstehen und begreifen den Tod allein, indem wir seinen Ursprung zu erkennen suchen, und daher begrei­fen wir das Leben, indem wir sein Verhältnis zum Tod er­kennen. In ähnlicher Weise lernen wir das Wesen der Krankheit begreifen, und dies wird uns noch mehr das Wesen des Todes klarmachen. Jede Krankheit stellt sich wie eine Zerstörerin des Lebens dar. Was ist Krankheit?",
      "Um ihr Wesen zu verstehen, müssen wir den Menschen im Zusammenhang mit der Natur betrachten. Machen wir uns klar, was denn geschieht, wenn der Mensch als leben­diges Wesen der übrigen Natur gegenübersteht. Mit jedem Luftzug, mit jedem Ton, mit der Nahrung, mit dem Licht, die er in sich aufnimmt, tritt der Mensch in ein Wediselver­hältnis mit der ihn umgebenden Natur. Wenn Sie die Sache genau betrachten, so werden Sie auch ohne Okkultismus darauf kommen, daß die Dinge draußen die eigentlichen Bildner und Öffner der physischen Organe sind. Wenn gewisse",
      "Tiere in finstere Höhlen einwandern, dann werden ihre Augen mit der Zeit rückgebildet. Wo kein Licht mehr ist, können nicht mehr lichtempfängliche Augen sein; um-gekehrt, nur wo Licht ist, können lichtempfindliche Augen sich bilden.",
      "Deshalb sagt Goethe, das Auge wird vom Licht für das Licht gebildet. Natürlich wird im Sinne dessen, was die eigentlichen inneren Architekten genannt werden, der physische Leib aufgebaut. Der Mensch ist ein physisches Wesen, und die äußeren Dinge sind dasjenige, woraus im Einklang mit den inneren Bildnern der ganze Mensch auf­gebaut wird.",
      "Dann wird das Verhältnis einzelner Kräfte und Stoffe zum Menschen ein ganz anderes Bild ergeben. Diejenigen, die hier den tiefen Blick des wahren Mystikers gehabt haben, werden uns hier besonders viel sagen kön­nen.",
      "Für Paracelsus ist die ganze äußere Welt ein fächer-artig auseinandergelegter menschlicher Organismus, und der Mensch ist wie ein Extrakt der ganzen äußeren Welt. Wenn wir eine Pflanze sehen, können wir im Sinne des Paracelsus sagen: In dieser Pflanze ist ein gesetzmäßiger Zusammen­hang, und es gibt etwas im Menschen, was im gesunden oder kranken Organismus dieser Pflanze entspricht.",
      "Daher nennt Paracelsus zum Beispiel einen Cholerakranken einen «Arsenikus», und das Arsenik ist ihm ein Heilmittel für Cholera. So besteht eine Beziehung zwischen jedem Organ des Menschen und dem, was in der Natur um ihn herum ist.",
      "Man bräuchte nur eine Essenz der Natur zu nehmen und sie menschenähnlich formen, dann hätte man den Men­schen. In der ganzen Natur sind die einzelnen Buchstaben ausgebreitet, nimmt man sie zusammen, dann hat man den Menschen.",
      "Da bekommen Sie eine Ahnung, wie die ganze übrige Natur auf den Menschen wirkt, und daß der Mensch berufen ist, aus der ganzen übrigen Natur seine Wesenheit zusammenzusetzen. Alles, was in uns ist, ist im Grunde",
      "genommen in uns hineingezogen aus der äußeren Natur, aufgenommen worden in den Lebensprozeß. Wenn wir dieses Geheimnis von der Verlebendigung äußerer Kräfte und Stoffe verstehen, dann werden wir das Wesen einer Krankheit begreifen können.",
      "Wir kommen da auf ein Kapitel, wo es einem heutigen Gebildeten schwer wird zu verstehen, wie viele Begriffe in der Medizin wie eine Art Nebelgebilde wirken. Wie wirkt es heute in den Versammlungen suggestiv, wenn jemand als Naturheilkundiger das Wort «Gift» ausspricht. Was ist ein Gift, und was ist eine unnatürliche Wirkung im mensch­liehen Organismus? Was Sie auch immer in den mensch­liehen Organismus einführen, wirkt nach Naturgesetzen. Es ist unerfindlich, wie man davon sprechen kann, daß irgend etwas nicht nach Naturgesetzen im Körper wirken könnte. Und was ist ein Gift? Wasser ist ein starkes Gift, wenn Sie zehn Eimer davon auf einmal vertilgen; und was heute Gift ist, könnte von den wohltätigsten Wirkungen sein, wenn man es in der richtigen Weise dem Körper zuführt. Es kommt immer darauf an, in welcher Quantität und unter welchen Umständen man einen Stoff zu sich nimmt. Es gibt kein Gift an sich.",
      "In Afrika gibt es einen Stamm, der eine bestimmte Hunde­art zur Jagd verwendet. Nun gibt es aber dort eine Art von Fliegen, die ein bestimmtes Gift in sich tragen, das die Hunde tötet, wenn sie von den Fliegen gestochen werden. Da haben die Wilden des Sambesiflusses ein Mittel gegen diesen Stich gefunden. Sie führen nämlich die trächtigen Hündinnen gerade in solche Gegenden, wo sehr viele von diesen Tsetsefliegen sind, und lassen die Hündinnen von den Tsetsefliegen stechen. Die Wilden wissen es dann so ein­zurichten, daß die Hündinnen erst dann sterben, wenn sie geworfen haben. Und nun stellt sich die Tatsache heraus,",
      "daß die jungen Hunde jetzt immun sind und zur Jagd ver­wendet werden können.",
      "Da ist etwas geschehen, was für das Verständnis des Le­bens so wichtig ist: Ein Gift ist in einen Lebensprozeß auf­genommen worden im Moment, wo eine absteigende Linie in eine aufsteigende Linie übergeht, so daß das Gift ein zum Organismus gehöriger Stoff wird. Was wir so von der äuße­ren Natur aufgenommen haben, das macht uns stark und schützt uns gerade.",
      "Die Geisteswissenschaft zeigt uns, daß der ganze mensch­liche Organismus auf diese Weise auferbaut ist; wenn wir so sagen wollen, aus lauter Dingen, die ursprünglich Gifte waren. Für die Nahrungsmittel, die Sie heute genießen, hat man sich die Möglichkeit geholt, sie zu essen, nachdem man sich durch einen ähnlichen Vorgang in der rückläufigen Linie gegen ihre Schädlichkeit immun gemacht hat. Und wir sind um so stärker, je mehr solcher Stoffe wir auf diese Weise uns einverleibt haben. Schwach machen wir uns ge­gen die äußere Natur, indem wir ihre Stoffe zurückweisen.",
      "In den Gegenden, wo die Arzneikunde noch auf den Ok­kultismus aufgebaut ist, wirft der Arzt seine ganze Persön­lichkeit in die Schranken. Es gibt Kuren, innerhalb welcher der Arzt sich zum Beispiel Schlangengift einverleibt, dann wird sein Speichel zum Heilmittel gegen solche Schlangen­bisse. Er verleibt dem eigenen Organismus das Gift ein, macht sich dadurch zum Träger der heilenden Kräfte, wird stark und macht damit die anderen stark gegen das betref­fende Gift.",
      "Das Harmloseste, was der Organismus hat, ist auf diese Weise entstanden. Die Einverleibung der äußeren Welten und der Natur braucht der Organismus; aber dabei muß auch die Möglichkeit gegeben werden, daß die Sache wie ein Pendel hinüberschlägt nach der anderen Seite. Immer",
      "ist die Möglichkeit gegeben, wenn der Mensch sich solchen Stoffen aussetzt - und dem ist er in jedem Augenblick aus­gesetzt -, daß das Mittel in seiner Wirkung sich überschlägt und schädigt, je nachdem, ob der Lebensleib geeignet ist, es aufzunehmen oder nicht. Dadurch wird der Organismus stark gegen das Mittel, wenn er im Augenblick stark genug ist, den Stoff in sich aufzunehmen. Es gibt keine Möglich­keit, der Krankheit zu entkommen, wenn man die Gesund­heit haben will. Jede Möglichkeit, sich gegen die äußeren Einflüsse stark zu machen, beruht auf der Möglichkeit, Krankheit zu haben, krank zu sein. So ist die Krankheit die Bedingung der Gesundheit. Das ist ein ganz realer Werdegang. Das ist geradezu die Folgerung und Gabe der Krankheit, daß das Starke vom Menschen erworben wer­den muß. Was beim Ausschlagen des Pendels überlebt, das hat die Frucht der Immunität aus der Krankheit, - und sogar über den Tod hinaus.",
      "Wer etwas weitergeht, wird gerade daraus eine Art von Verständnis für das Wesen der Krankheit und das Wesen des Todes gewinnen. Wollen wir die Stärke, die Gesund­heit, dann müssen wir ihre Vorbedingung, die Krankheit, mit in den Kauf nehmen. Wollen wir stark sein, dann müs-sen wir uns gegen die Schwäche schützen, indem wir die Schwäche in uns selber aufnehmen und in Stärke verwan­deln. Wenn man dies lebendig auffaßt, wird es uns Krank­heit und Tod begreiflich machen. Diese Begriffe wird die geisteswissenschaftliche Bewegung der Menschheit bringen. Heute mag das für viele noch etwas sein, was nur zum Ver­stande spricht. Wenn aber der Verstand die Sache völlig aufgenommen haben wird, dann wird das eine tiefe har­monische Gemütslage im Menschen bewirken, dann wird das Lebensweisheit werden.",
      "Haben Sie denn noch nicht gehört, daß die anthroposophischen",
      "Wahrheiten, die aus dem Okkultismus heraus ge­schöpft sind, sogar gefährlich werden können? Haben wir nicht zahlreiche Gegner, die behaupten, die Anthroposophie sei ein Gift und schädige den Menschen? Ja, das wissen die Anthroposophen und der Okkultist selber, daß die An­throposophie auch schädlich wirken kann; sie wissen aber auch, daß sie aufgenommen und einverleibt werden muß, um den Menschen stark zu machen, und daß sie nicht nur etwas ist, worüber man diskutieren kann, sondern etwas, was sich dann imLeben bewährt als ein geistiges Heilmittel.",
      "Und das weiß die Geisteswissenschaft auch, daß das Physische aus dem Geistigen heraus aufgebaut wird. Wir­ken die geistigen Kräfte auf den Ätherleib, dann wirken sie auch als gesund im Zusammenhang des physischen Leibes. Sind unsere Vorstellungen von der Welt und vom Leben gesund, dann sind diese gesunden Gedanken die kräftigsten Heilmittel, und nur auf schwache Naturen, die durch Mate­rialismus und Naturalismus schwache Naturen geworden sind, wirkt das, was die Anthroposophie als Wahrheit ver­kündigt, krankmachend. Das müssen sie sich einverleiben, um sich stark zu machen. Erst dann hat die Anthroposophie ihre Aufgabe erfüllt, wenn sie starke Menschen im Leben erzeugt.",
      "Unsere Frage nach Leben und Tod hat Goethe so schön gelöst: Alles in der Natur ist Leben; sie hat den Tod nur erfunden, um viel Leben zu haben. Und so könnte man sagen: Sie hat auch neben dem Tod die Krankheit erfun­den, um die starke Gesundheit zu erzeugen, und sie hat not­wendigerweise der Weisheit scheinbar schädigende Wirkung zugeben müssen, damit diese Weisheit kräftigend und hei­lend auf die Menschheit wirkt.",
      "Gerade dadurch unterscheidet sich die geisteswissenschaft­liche Weltbewegung von den anderen Bewegungen, daß",
      "man über sie streiten und diskutieren kann, wenn man von ihr verlangt, sie solle sich logisch beweisen. Nicht etwas, was sieh bloß mit logischen Gründen erhärten läßt, soll die Anthroposophie sein, sondern etwas, was die Menschen gei­stig und auch körperlich gesund macht. Je mehr sie ihre Wirkungen draußen im Leben zeigt, indem sie das Leben so erhöht, daß der Lebensschmerz in Lebensglück verwan­delt wird, desto mehr werden lebendige Beweise für sie da sein. Mögen die Leute heute noch so sehr glauben, sie könn­ten etwas logisch dagegen einwenden: die Geisteswissen­schaft ist etwas, das wie ein scheinbares Gift umgewandelt wird in ein Heilmittel und dann befruehtend wirkt im Le­ben. Und nicht in der Logik wird sie sich zeigen - sie kann nicht bloß bewiesen werden - sie wird sich bewähren im Leben."
    ],
    "sentences": [
      [
        "Heute haben wir es mit einem Thema zu tun, das zwei­fellos jedem Menschen nahegeht, denn die beiden Worte «Krankheit und Tod» drücken etwas aus, was sich in jedes Leben hineinstellt, oftmals wie ein unerbetener Gast, oft aber auch als etwas Quälendes, Beengendes, Furchtmachen­des.",
        "Ja, der Tod stellt sieh als die größte Rätselfrage ins Dasein hinein, so daß, wenn jemand die Frage nach dem Wesen des Todes gelöst hat, für ihn dann wohl auch die Frage nach dem Wesen des Lebens gelöst ist.",
        "Oft hört man sagen: Der Tod bildet ein Rätsel, noch keiner hat es gelöst, und auch keiner wird es je lösen. - Die Menschen, die der­gleichen aussprechen, ahnen gar nicht, welche Unbescheiden­heit in diesen Worten liegt, sie ahnen gar nicht, daß es eine Lösung solcher Rätselfragen gibt und daß sie es nur nicht verstehen.",
        "Heute, wo wir es mit einem so umfassend wich­tigen Ding zu tun haben, bitte ich Sie, ganz besonders dar­auf zu achten, daß es sich um nichts anderes handeln kann, als um eine Beantwortung der gestellten Frage: Wie begreift man Krankheit und Tod?",
        "Wir können uns daher nicht auf spezielle Fragen über Krankheiten und Gesundheit einlas­sen, sondern müssen uns im wesentlichen an die Frage hal­ten: Wie erlangt man ein Verständnis für diese zwei wich­tigen Fragen unseres Daseins?"
      ],
      [
        "Die bekannteste Antwort auf die Frage nach dem Wesen des Todes, die Jahrhunderte hindurch geltend war, heute aber für den weitaus größten Teil der Gebildeten der Menschheit"
      ],
      [
        "ihren Wert eingebüßt hat, liegt vor in den Worten des Paulus: «Denn der Tod ist der Sünde Sold.» Wie gesagt, viele Jahrhunderte hindurch war dieses Wort eine Art Lö­sung des Rätsels des Todes.",
        "Heute wird derjenige, der im modernen Sinne denkt, mit einer solchen Antwort überhaupt nichts anfangen können, denn daß die Sünde etwas völlig Moralisches, etwas rein im Wesen des menschlichen Verhal­tens Liegendes, die Ursache einer physischen Tatsache, wie der Tod es ist, sein könnte oder irgendwie mit dem Wesen der Krankheit zusammenhängen sollte, das ist für einen heutigen Denker ganz unerfindlich."
      ],
      [
        "Es wird uns vielleicht noch nützlich sein, wenn wir auch darauf hinweisen, daß unsere Gegenwart nicht einmal mehr den Wortlaut des Satzes: «Denn der Tod ist der Sünde Sold» versteht.",
        "Denn unter «Sünde» verstanden Paulus und die, welche zu seiner Zeit lebten, ganz und gar nicht das, was man heute im philiströsen Sinne darunter versteht.",
        "Nicht eine Verfehlung im gewöhnlichen Sinne ist hier mit Sünde gemeint, auch nicht eine Verfehlung radikaler Art, sondern unter Sünde wird da verstanden, was aus Selbst­sucht und Egoismus hervorgeht.",
        "Alles, was Selbstsucht und Egoismus zum Antriebe des Handelns hat - im Gegensatz zu dem, was sachlichen, objektiven Impulsen entspringt -, ist Sünde.",
        "Der Egoismus, das selbstische Handeln, aber setzt voraus, daß der Mensch selbständig, ich-bewußt geworden ist.",
        "Das muß man erkennen, wenn man sich ganz und gar auf die Denkweise eines solchen Geistes wie Paulus einläßt."
      ],
      [
        "Wer nicht an der Oberfläche des Verständnisses der alt-und neutestamentlichen Urkunden bleibt, sondern wirklich in ihren Geist eindringt, der weiß, daß eine ganz bestimmte, man möchte sagen naturphilosophische Denkweise die Un­terströmung dieser alt- und neutestamentlichen Denkweise bildet.",
        "Diese Unterströmung ist etwa die folgende: Alles,"
      ],
      [
        "was an Lebensschöpfung in der Welt vorhanden ist, richtet sich nach einem ganz bestimmten Ziel hin.",
        "Die niederen Wesen sind noch neutral gegen Lust und Leid, Freude und Schmerz.",
        "Wir finden dann, wie sich das Leben steigert und etwas damit verbunden wird.",
        "Derjenige, dem schaudert, wenn man von Zielstrebigkeit spricht, der möge bedenken, daß hier nicht eine Theorie gedacht ist, sondern daß es sich hier um eine reine Tatsache handelt: das ganze Reich der Lebewesen bis zum Menschen hinauf nähert sieh einer be­stimmten Tatsache, die sich darin zeigt, daß an der Spitze der Lebewesen ein persönliches Bewußtsein möglich ist."
      ],
      [
        "Es schaute der Eingeweihte des Alten und Neuen Testa­mentes hinunter ins Reich der Tiere und sah, wie alles dahin strebt, daß einmal eine freie Persönlichkeit zustande kom­men kann, die aus sieh selbst heraus die Antriebe und Im­pulse zum Handeln haben kann, und wie mit dem Wesen einer solchen Persönlichkeit das verbunden ist, was man die Möglichkeit einer egoistischen, selbstsüchtigen Handlung nennt.",
        "Nun aber würde ein Denker wie Paulus sagen: Wenn in einem Leibe eine solche Persönlichkeit wohnt, die ego­istisch zu handeln imstande ist, so muß dieser Leib sterblich sein.",
        "In einem unsterblichen Leibe würde niemals eine Seele mit Selbständigkeit, Selbstbewußtsein und folglich auch mit Egoismus wohnen können.",
        "Daher gehören zusammen: ein sterblicher Leib und eine Seele mit Persönlichkeitsbewußt­sein und die einseitige Ausbildung der Persönlichkeit zu Handlungsimpulsen.",
        "Das heißt die Bibel «Sünde», und so definiert Paulus: «Der Tod ist der Sünde Sold».",
        "Da sehen Sie allerdings, daß wir diesen, wie jeden anderen Ausspruch der Bibel modifizieren müssen, weil sie im Laufe der Jahr­hunderte ganz in ihr Gegenteil umgekehrt worden sind.",
        "Modifiziert man sie, nicht indem man sie umdeutet, sondern indem man sich klarmacht, daß man den gegenwärtigen"
      ],
      [
        "Sinn, den die Theologie gibt, in den ursprünglichen verwan­delt, so sieht man daraus, daß man es oftmals mit einer sehr tiefen Auffassung der Sache zu tun hatte, die dem gar nicht so fernsteht, was man heute wieder begreifen kann.",
        "Dies zur notwendigen Richtigstellung."
      ],
      [
        "Aber es haben sich ja die Denker, die Weltanschauungs­forscher aller Zeiten mit der Frage nach dem Rätsel des Todes beschäftigt, und wir finden diese Frage seit Jahrtau­senden scheinbar in der mannigfaltigsten Weise beantwor­tet.",
        "Wir können uns hier nicht mit einer geschichtlichen Be­trachtung einer solchen Lösung befassen, daher sei nur auf zwei Denker hingewiesen, damit Sie sehen, wie selbst der Gegenwart recht nahestehende Denker nichts Erhebliches zu dieser Frage beizubringen wissen."
      ],
      [
        "Der eine ist Schopenhauer.",
        "Sie kennen ja alle seine pessi­mistische Art zu denken, und wer einmal den Satz durch­gegangen ist: «Das Leben ist eine mißliche Sache, und ich habe mir vorgenommen, das meinige damit hinzubringen, über dasselbe nachzudenken» - der wird begreifen, daß Schopenhauer kaum zu einer anderen Lösung gekommen ist als zu der: Eigentlich tröstet der Tod über das Leben und das Leben über den Tod; das Leben ist eine fatale Sache, und man könnte es nicht ertragen, wenn man nicht wüßte, daß der Tod es schließen würde; und wenn man die Furcht vor dem Tode hat, dann braucht man sich nur einmal klarzu-machen, daß das Leben nicht besser sei und daß durch den Tod nichts weiter beschlossen ist.",
        "Das ist seine pessimistische Art zu denken, die nur einmal darüber hinausführt, wo er den Erdgeist sagen läßt: Ihr wollt, daß immer neues Leben entsteht, da muß ich Platz haben.",
        "Also sieht Schopenhauer in einer gewissen Beziehung in der Tatsache, daß das Leben sich fortpflanzt, immer neues Leben gebiert, die Notwen­digkeit, daß das Alte sterben müsse, damit für das Neue"
      ],
      [
        "Raum sei.",
        "Sonst weiß auch Schopenhauer gar nichts Erheb­liches vorzubringen; denn alles, was er sonst sagt, atmet in diesen zwei Worten."
      ],
      [
        "Der andere ist Eduard von Hartmann.",
        "Er hat sich noch in seinem letzten Buche mit dem Rätsel des Todes beschäf­tigt.",
        "Er sagt da: Wenn wir uns das zunächst höchste Lebe­wesen betrachten, so finden wir, daß der Mensch, nachdem wieder ein oder zwei neue Generationen heraufgezogen sind, die Welt nicht mehr versteht.",
        "Wenn der Mensch alt geworden ist, kann er die Jugend nicht mehr fassen, daher ist es not­wendig, daß das Alte absterbe und Neues wieder hervor­komme. - Sie sehen jedenfalls auf diese Fragen auch keine Antwort, die uns mit wirklichem Verständnis dem Rätsel des Todes näherbringen könnte."
      ],
      [
        "So wollen wir einmal in die heutigen, gegenwärtigen Welt­anschauungen hineinstellen, was die sogenannte Geisteswis­senschaft, dieman heute auch Anthroposophie nennt, über die Ursachen von Tod und Krankheit zu sagen hat.",
        "Wir wollen uns aber dabei eines klarmachen: der Geisteswissenschaft geht es nicht so gut wie den anderen Wissenschaften, daß sie in einer bestimmten Weise über alles sprechen kann.",
        "Der heutige Naturforscher würde es nicht begreifen, daß man, wenn man über Krankheit und Tod spricht, trennen muß zwischen Tier und Mensch, daß man aber gerade, wenn man die Frage des heutigen Vortrages begreifen will, sich wird auf die Erscheinungen beim Menschen beschränken müssen.",
        "Da die Wesen nicht nur das abstrakte «Gleiche» miteinander haben, sondern auch jedes sein Wesentliches und seine Eigen­art hat, so wird nur einiges von dem, was heute gesagt wird, auch auf die Tierwelt anzuwenden sein, vielleicht auch auf die Pflanzen; im wesentlichen aber wird über den Menschen gesprochen werden, und die anderen Dinge werden nur herangezogen werden, wenn sie etwas erklären sollen."
      ],
      [
        "Wenn wir Tod und Krankheit beim Menschen erfassen wollen, müssen wir vor allen Dingen darauf sehen, daß der Mensch im Sinne der Geisteswissenschaft ein höchst kom­pliziertes Wesen ist und daß wir den Menschen seinem Wesen nach aus den folgenden vier Gliedern heraus begreifen müssen: erstens haben wir den äußerlich sichtbaren physi­schen Körper, als zweites den Ather- oder Lebensleib, so­dann den Astralleib, und als viertes das Ich des Menschen oder den Mittelpunkt seines Wesens.",
        "Dann müssen wir uns klar sein, daß im physischen Leibe dieselben Kräfte und Stoffe vorhanden sind wie in der physischen Welt draußen und daß in dem Atherleib das liegt, was diese Stoffe zum Leben aufruft, und daß der Mensch seinen Atherleib mit der ganzen Pflanzenwelt gemeinschaftlich hat.",
        "Der Astral­leib, den der Mensch mit den Tieren gemein hat, ist der Trä­ger des ganzen Gefühlslebens, von Begierden, Lust und Un­lust, Freude und Schmerz.",
        "Das Ich hat der Mensch ganz für sich allein, das macht ihn zur Krone der Erdenschöpfung."
      ],
      [
        "Wenn wir den Menschen als physischen Organismus vor uns haben, dann müssen wir uns klarmachen, daß innerhalb dieses physischen Organismus die drei anderen Glieder als Bildner und Architekten arbeiten.",
        "Das physische Prinzip arbeitet nur teilweise am physischen Organismus des Men­schen, in einem anderen Teil ist im wesentlichen der Äther-leib tätig, wieder in einem anderen der Astralleib, und wie­derum in einem anderen Teil des Menschen ist das Ich tätig.",
        "Der Mensch besteht für die Geisteswissenschaft physisch erst einmal aus Knochen, Muskeln, denjenigen Organen, die den Menschen stützen, ihn zu einem festen, auf der Erde gehen­den Gebilde machen; diese allein rechnet man im strengsten Sinn der Geisteswissenschaft zu dem durch das physische Prinzip zustande gekommenen Teil der Organe.",
        "Dazu kom­men noch die eigentlichen Sinnesorgane; dabei haben wir es"
      ],
      [
        "mit physikalischen Apparaten zu tun; beim Auge mit einer Art camera obscura, beim Ohr mit einem sehr komplizier­ten Musikinstrument.",
        "Es kommt nun darauf an, woraus diese Organe gebaut sind.",
        "Sie sind von dem ersten Prinzip gebaut.",
        "Dagegen sind alle Organe, die mit Wachstum, Fort­pflanzung, Verdauung und anderem zusammenhängen, nicht bloß im Sinne des physischen Prinzips gebaut, sondern im Sinne des Äther- oder Lebensleibes, der ja auch die physi­schen Organe durchdringt.",
        "Nur der gesetzmäßige Aufbau wird vom physischen Prinzip besorgt, der Vorgang von Verdauung, Fortpflanzung und Wachstum dagegen wird vom Ätherprinzip besorgt.",
        "Der Astralleib ist der Schöpfer des ganzen Nervensystems, bis hinauf zum Gehirn und zu den Strängen, die in Form von Sinnesnervensträngen zum Gehirn gehen.",
        "Das Ich endlich ist der Architekt des Blut­kreislaufes.",
        "Wenn wir also in echt geisteswissenschaftlichem Sinne einen menschlichen Organismus vor uns haben, so sind wir uns klar, daß diese vier Glieder - auch im äußerlich wahrnehmbaren Organismus - eigentlich wie vier ganz voneinander verschiedene Wesenheiten im Menschen ver­schmelzen und miteinander wirksam gemacht worden sind.",
        "Diese Glieder, die den menschlichen Organismus zusammen­setzen, sind von ganz verschiedenem Werte, und wir wer­den ihre Bedeutung für den Menschen begreifen, wenn wir erforschen, wie die Entwicklung des Menschen mit diesen einzelnen Gliedern zusammenhängt."
      ],
      [
        "Heute sei mehr vom physiologischen Gesichtspunkt aus besprochen, was man die Arbeit des physischen Prinzips im menschlichen Organismus nennt.",
        "Das wird geleistet in der Epoche von der Geburt bis zum Zahnwechsel.",
        "Da arbeitet das physische Prinzip am physischen Leibe so, wie die Kräfte und Stoffe des mütterlichen Organismus am Kindeskeim arbeiten, bevor das Kind geboren ist.",
        "Vom siebenten Jahre"
      ],
      [
        "bis zur Geschlechtsreife arbeitet am physischen Leibe haupt­sächlich das Ätherprinzip, und von der Geschlechtsreife an arbeiten die Kräfte, die innerhalb des Astralleibes verankert sind.",
        "So daß wir uns die Entwicklung des Menschen recht vorstellen, wenn wir uns denken, daß der Mensch bis zur Geburt vom Leibe der Mutter umschlossen ist."
      ],
      [
        "Mit der Ge­burt drängt er gleichsam den mütterlichen Leib zurück, seine Sinne werden frei, und nun ist es möglich, daß die äußere Welt anfängt, auf den menschlichen Organismus einzuwir­ken.",
        "Da stößt der Mensch auch eine Hülle von sich, und derjenige erst begreift richtig die Entwicklung des Menschen, der begreift, daß zwar nicht im physischen, aber im geisti­gen Leben etwas Ähnliches in der Zeit des Zahnwechsels vor sich geht."
      ],
      [
        "Um das siebente Jahr herum wird der Mensch richtig ein zweites Mal geboren.",
        "Da wird nämlich sein Äther-leib zur freien Tätigkeit geboren, wie sein physischer Leib zur Zeit der Geburt.",
        "So wie physisch der Mutterleib an dem Menschenkeim in der Zeit vor der Geburt arbeitet, so arbeiten geistige Kräfte des Weltenäthers bis zum Zahn-wechsel an dem Ätherleib des Menschen, und sie werden um das siebente Jahr herum ebenso zurückgedrängt wie der Mutterleib bei der physischen Geburt."
      ],
      [
        "Bis zum siebenten Jahre liegt der Ätherleib wie latent im physischen Leibe.",
        "Wie bei einem in Brand gesetzten Zündholz ist es mit dem Ätherleib um die Zeit des Zahnwechsels herum.",
        "Er ist im physischen Leibe darinnen gebunden und kommt nun her­aus zur eigenen, freien, selbständigen Tätigkeit."
      ],
      [
        "Und das Zeichen, wodurch sich diese freie Tätigkeit des Ätherleibes ankündigt, ist gerade der Zahnwechsel.",
        "Der Zahnwechsel hat für den, der tiefer in die Natur des Menschen hinein-schaut, eine ganz bedeutsame Stellung."
      ],
      [
        "Haben wir einen Menschen bis zum siebenten Jahr vor uns, so arbeitet das physische Prinzip frei im physischen Leib; aber gebunden"
      ],
      [
        "und aus den geistigen Hüllen noch nicht herausgeboren ist das Äther- und das astrale Prinzip."
      ],
      [
        "Wenn wir den Menschen bis zum siebenten Jahr betrach­ten, so enthält er eine ganze Summe von Vererbungstat­sachen, die er nicht mit seinem eigenen Prinzip erbaut hat, sondern die er von den Vorfahren ererbt erhalten hat.",
        "Dazu gehört das, was man die Milchzähne nennt.",
        "Erst die Zähne, die nach dem Zahnwechsel kommen, sind im Kinde die eigene Schöpfung des Prinzips, das als physisches dazu veranlagt ist, die feste Stütze zu bilden.",
        "Was in den Zähnen zum Ausdruck kommt, schafft bis zum Zahnwechsel im In­nern, und es bildet am Ende seiner Wirksamkeit gleichsam den Schlußpunkt und bringt den härtesten Teil des Stütz­organes in den Zähnen hervor, weil es noch den Äther- oder Lebensleib als Wachstumsträger in sich gebunden hält."
      ],
      [
        "Nachdem dieses Prinzip abgestoßen ist, wird der Äther-leib frei und schafft jetzt an den physischen Organen bis zur Geschlechtsreife, und dann wird ebenso eine Hülle, die äußere astrale Hülle, weggedrängt wie bei der Geburt die Mutterhülle.",
        "Astralisch wird der Mensch bei der Geschlechts-reife zum dritten Male geboren.",
        "Und die wirkenden Kräfte, die im Ätherleib gebunden waren, machen jetzt für ihre Schöpfungsart im Menschen den Schlußpunkt, indem sie die Fähigkeit der Geschleditsreife, der Fortpflanzung, und ihre Organe erzeugen.",
        "So wie das physische Prinzip im sieben­ten Jahre durch die Zähne den Schlußpunkt macht, indem es die letzten harten Organe schafft, und wodurch der Äther-leib, das Wachstumsprinzip, frei wird, so schafft das astrale Prinzip in dem Moment, wo es frei wird, die stärkste Kon­zentration der Triebe und Begierden, der Lebensäußerung, insofern wir es mit der physischen Natur zu tun haben.",
        "Wie Sie das physische Prinzip wie konzentriert in den Zähnen haben, so das Wachstumsprinzip in der Geschlechtsreife."
      ],
      [
        "ist der Astralleib, die Umhüllung des Ich frei, und das Ich arbeitet nun am Astralleib."
      ],
      [
        "Der europäische Kulturmenseh folgt nicht bloß seinen Trieben und Begierden; er hat sie geläutert und umge­wandelt in moralische Empfindungen und ethische Ideale.",
        "Vergleichen wir nun einen Wilden mit einem europäischen Durchschnittsmenschen oder gar mit einem Schiller oder Franz von Assisi, so können wir sagen, daß diese ihre Triebe vom Ich aus umgestaltet, geläutert haben.",
        "So können wir uns sagen, daß dieser Astralleib stets zwei Teile enthält:"
      ],
      [
        "einen, der aus der ursprünglichen Anlage herrührt, und einen, den das Ich selbst geboren hat.",
        "Nun verstehen wir die Arbeit des Ich nur dann, wenn wir uns klarmachen, daß der Mensch einer Wiederverkörperung - wiederholten Er­denleben - unterliegt; daß der Mensch, wenn er geboren wird, gleichsam in vier voneinander geteilten Leibern sich die Früchte und Ergebnisse früherer Erdenleben mitbringt, die als ein Maß für die Energie und Kraft seines Lebens da sind.",
        "Der eine Mensch wird geboren, weil er es früher dazu gebracht hat, mit viel Lebensenergie, mit starken Kräften seinen Astralleib umzugestalten.",
        "Der andere wird darin bald erlahmen.",
        "Wenn man hellsehend untersuchen kann, wie das Ich beginnt, an dem Astralleibe frei zu arbeiten, die Begierden, Triebe und Leidenschaften vom Ich aus zu be­herrschen, dann könnte man, wenn man das Maß von Ener­gie, das das Ich sich mitgebracht hat, anzugeben vermag, sagen: dieses Maß ist so groß, daß das Ich so und so lange an seiner Umgestaltung an sich arbeiten wird und nicht mehr.",
        "Und nach der Zeit der Gesehlechtsreife gibt es für jeden Menschen ein solches Maß, durch das man messen kann und angeben könnte, bis wann er alles aus seinem Astralkörper herausgearbeitet hat nach den ihm in diesem Leben zugeteilten Pfunden.",
        "Was der Mensch so in seinem"
      ],
      [
        "Gemüt an Lebenskräften umzugestalten und zu läutern ver­mag, erhält sich selbst.",
        "Solange dieses Maß ausreicht, lebt er auf Kosten des sich selbst erhaltenden Astralleibes.",
        "Ist er erschöpft, findet er keinen Mut mehr, neue Triebe umzu­gestalten, kurz, keine Energie, an sieh zu arbeiten, dann reißt der Lebensfaden ab, - und er muß nach einem Maße, das jedem Menschen zuerteilt ist, einmal abreißen.",
        "Dann ist die Zeit gekommen, wo der Astralleib seine Kräfte von dem Prinzip des menschlichen Lebens nehmen muß, das ihm zunächst liegt, vom Ätherleib.",
        "Und jetzt kommt die Zeit, wo der Astralleib auf Kosten der im Ätherleib aufgespei­cherten Kraft lebt; der Ausdruck dafür ist für den Menschen da, wenn sein Gedächtnis, seine produktive Einbildungs-kraft allmählich schwindet."
      ],
      [
        "Wir haben öfter hier gehört, daß der Ätherleib der Trä­ger der produktiven Phantasie und des Gedächtnisses ist, dessen, was man Lebenshoffnung und Lebensmut nennt.",
        "Diese Gefühle, wenn sie zu seinem bleibenden Element wer­den, haften an dem Ätherleib.",
        "Sie werden jetzt von dem Astralleib herausgesogen; und nachdem der Astralleib so auf Kosten des Ätherleibes gelebt und alles, was dieser her­zugeben hatte, ausgesogen hat, beginnt die Zeit, wo die schöpferischen Kräfte des physischen Leibes vom Astralleib aufgezehrt werden.",
        "Und sind diese herausgezehrt, dann schwindet die Lebenskraft des physischen Leibes, der Kör­per verhärtet sich, der Puls wird langsamer.",
        "Da zehrt der Astrall eib zuletzt auch noch am physischen Leibe und nimmt ihm die Kraft weg.",
        "Und hat er die aufgezehrt, dann ist keine Möglichkeit mehr, daß aus dem physischen Prinzip heraus der physische Leib erhalten werden kann."
      ],
      [
        "Soll der Astralleib es dahin bringen, daß er frei werden und zu dem Leben und der Arbeit des Ich geboren werden soll, dann ist es notwendig, daß in der zweiten Hälfte des"
      ],
      [
        "Lebens der freigewordene Astralleib, wenn das Maß der Arbeit ersehöpft ist, seine Hüllen geradeso wie sie gebildet worden sind, selber wieder aufzehrt.",
        "So ist das individu­eIle Leben vom Ich heraus geschaffen."
      ],
      [
        "Zum Gleichnis diene Folgendes: Denken Sie sich ein Stück Holz, das Sie anzünden.",
        "Wäre es nicht so, wie es ist, so würden Sie es nicht anzünden können.",
        "Die Flamme quillt aus dem Holz hervor, aber sie zehrt es zu gleicher Zeit auf.",
        "Das ist das Wesen der Flamme, daß sie aus dem Holz her­aus frei wird und den eigenen Mutterboden aufzehrt.",
        "So wird der Astralleib dreifach herausgeboren, so zehrt er, wie die Flamme das Holz, seine eigene Grundlage auf; und darin besteht die Möglichkeit, daß das individuelle Leben da sein kann, weil es seine Grundlage wieder aufzehrt.",
        "Der Tod ist ihm die Wurzel des Lebens, und es könnte gar kein bewußt individuelles Leben geben, wenn es nicht den Tod gäbe.",
        "Wir verstehen und begreifen den Tod allein, indem wir seinen Ursprung zu erkennen suchen, und daher begrei­fen wir das Leben, indem wir sein Verhältnis zum Tod er­kennen.",
        "In ähnlicher Weise lernen wir das Wesen der Krankheit begreifen, und dies wird uns noch mehr das Wesen des Todes klarmachen.",
        "Jede Krankheit stellt sich wie eine Zerstörerin des Lebens dar.",
        "Was ist Krankheit?"
      ],
      [
        "Um ihr Wesen zu verstehen, müssen wir den Menschen im Zusammenhang mit der Natur betrachten.",
        "Machen wir uns klar, was denn geschieht, wenn der Mensch als leben­diges Wesen der übrigen Natur gegenübersteht.",
        "Mit jedem Luftzug, mit jedem Ton, mit der Nahrung, mit dem Licht, die er in sich aufnimmt, tritt der Mensch in ein Wediselver­hältnis mit der ihn umgebenden Natur.",
        "Wenn Sie die Sache genau betrachten, so werden Sie auch ohne Okkultismus darauf kommen, daß die Dinge draußen die eigentlichen Bildner und Öffner der physischen Organe sind.",
        "Wenn gewisse"
      ],
      [
        "Tiere in finstere Höhlen einwandern, dann werden ihre Augen mit der Zeit rückgebildet.",
        "Wo kein Licht mehr ist, können nicht mehr lichtempfängliche Augen sein; um-gekehrt, nur wo Licht ist, können lichtempfindliche Augen sich bilden."
      ],
      [
        "Deshalb sagt Goethe, das Auge wird vom Licht für das Licht gebildet.",
        "Natürlich wird im Sinne dessen, was die eigentlichen inneren Architekten genannt werden, der physische Leib aufgebaut.",
        "Der Mensch ist ein physisches Wesen, und die äußeren Dinge sind dasjenige, woraus im Einklang mit den inneren Bildnern der ganze Mensch auf­gebaut wird."
      ],
      [
        "Dann wird das Verhältnis einzelner Kräfte und Stoffe zum Menschen ein ganz anderes Bild ergeben.",
        "Diejenigen, die hier den tiefen Blick des wahren Mystikers gehabt haben, werden uns hier besonders viel sagen kön­nen."
      ],
      [
        "Für Paracelsus ist die ganze äußere Welt ein fächer-artig auseinandergelegter menschlicher Organismus, und der Mensch ist wie ein Extrakt der ganzen äußeren Welt.",
        "Wenn wir eine Pflanze sehen, können wir im Sinne des Paracelsus sagen: In dieser Pflanze ist ein gesetzmäßiger Zusammen­hang, und es gibt etwas im Menschen, was im gesunden oder kranken Organismus dieser Pflanze entspricht."
      ],
      [
        "Daher nennt Paracelsus zum Beispiel einen Cholerakranken einen «Arsenikus», und das Arsenik ist ihm ein Heilmittel für Cholera.",
        "So besteht eine Beziehung zwischen jedem Organ des Menschen und dem, was in der Natur um ihn herum ist."
      ],
      [
        "Man bräuchte nur eine Essenz der Natur zu nehmen und sie menschenähnlich formen, dann hätte man den Men­schen.",
        "In der ganzen Natur sind die einzelnen Buchstaben ausgebreitet, nimmt man sie zusammen, dann hat man den Menschen."
      ],
      [
        "Da bekommen Sie eine Ahnung, wie die ganze übrige Natur auf den Menschen wirkt, und daß der Mensch berufen ist, aus der ganzen übrigen Natur seine Wesenheit zusammenzusetzen.",
        "Alles, was in uns ist, ist im Grunde"
      ],
      [
        "genommen in uns hineingezogen aus der äußeren Natur, aufgenommen worden in den Lebensprozeß.",
        "Wenn wir dieses Geheimnis von der Verlebendigung äußerer Kräfte und Stoffe verstehen, dann werden wir das Wesen einer Krankheit begreifen können."
      ],
      [
        "Wir kommen da auf ein Kapitel, wo es einem heutigen Gebildeten schwer wird zu verstehen, wie viele Begriffe in der Medizin wie eine Art Nebelgebilde wirken.",
        "Wie wirkt es heute in den Versammlungen suggestiv, wenn jemand als Naturheilkundiger das Wort «Gift» ausspricht.",
        "Was ist ein Gift, und was ist eine unnatürliche Wirkung im mensch­liehen Organismus?",
        "Was Sie auch immer in den mensch­liehen Organismus einführen, wirkt nach Naturgesetzen.",
        "Es ist unerfindlich, wie man davon sprechen kann, daß irgend etwas nicht nach Naturgesetzen im Körper wirken könnte.",
        "Und was ist ein Gift?",
        "Wasser ist ein starkes Gift, wenn Sie zehn Eimer davon auf einmal vertilgen; und was heute Gift ist, könnte von den wohltätigsten Wirkungen sein, wenn man es in der richtigen Weise dem Körper zuführt.",
        "Es kommt immer darauf an, in welcher Quantität und unter welchen Umständen man einen Stoff zu sich nimmt.",
        "Es gibt kein Gift an sich."
      ],
      [
        "In Afrika gibt es einen Stamm, der eine bestimmte Hunde­art zur Jagd verwendet.",
        "Nun gibt es aber dort eine Art von Fliegen, die ein bestimmtes Gift in sich tragen, das die Hunde tötet, wenn sie von den Fliegen gestochen werden.",
        "Da haben die Wilden des Sambesiflusses ein Mittel gegen diesen Stich gefunden.",
        "Sie führen nämlich die trächtigen Hündinnen gerade in solche Gegenden, wo sehr viele von diesen Tsetsefliegen sind, und lassen die Hündinnen von den Tsetsefliegen stechen.",
        "Die Wilden wissen es dann so ein­zurichten, daß die Hündinnen erst dann sterben, wenn sie geworfen haben.",
        "Und nun stellt sich die Tatsache heraus,"
      ],
      [
        "daß die jungen Hunde jetzt immun sind und zur Jagd ver­wendet werden können."
      ],
      [
        "Da ist etwas geschehen, was für das Verständnis des Le­bens so wichtig ist: Ein Gift ist in einen Lebensprozeß auf­genommen worden im Moment, wo eine absteigende Linie in eine aufsteigende Linie übergeht, so daß das Gift ein zum Organismus gehöriger Stoff wird.",
        "Was wir so von der äuße­ren Natur aufgenommen haben, das macht uns stark und schützt uns gerade."
      ],
      [
        "Die Geisteswissenschaft zeigt uns, daß der ganze mensch­liche Organismus auf diese Weise auferbaut ist; wenn wir so sagen wollen, aus lauter Dingen, die ursprünglich Gifte waren.",
        "Für die Nahrungsmittel, die Sie heute genießen, hat man sich die Möglichkeit geholt, sie zu essen, nachdem man sich durch einen ähnlichen Vorgang in der rückläufigen Linie gegen ihre Schädlichkeit immun gemacht hat.",
        "Und wir sind um so stärker, je mehr solcher Stoffe wir auf diese Weise uns einverleibt haben.",
        "Schwach machen wir uns ge­gen die äußere Natur, indem wir ihre Stoffe zurückweisen."
      ],
      [
        "In den Gegenden, wo die Arzneikunde noch auf den Ok­kultismus aufgebaut ist, wirft der Arzt seine ganze Persön­lichkeit in die Schranken.",
        "Es gibt Kuren, innerhalb welcher der Arzt sich zum Beispiel Schlangengift einverleibt, dann wird sein Speichel zum Heilmittel gegen solche Schlangen­bisse.",
        "Er verleibt dem eigenen Organismus das Gift ein, macht sich dadurch zum Träger der heilenden Kräfte, wird stark und macht damit die anderen stark gegen das betref­fende Gift."
      ],
      [
        "Das Harmloseste, was der Organismus hat, ist auf diese Weise entstanden.",
        "Die Einverleibung der äußeren Welten und der Natur braucht der Organismus; aber dabei muß auch die Möglichkeit gegeben werden, daß die Sache wie ein Pendel hinüberschlägt nach der anderen Seite.",
        "Immer"
      ],
      [
        "ist die Möglichkeit gegeben, wenn der Mensch sich solchen Stoffen aussetzt - und dem ist er in jedem Augenblick aus­gesetzt -, daß das Mittel in seiner Wirkung sich überschlägt und schädigt, je nachdem, ob der Lebensleib geeignet ist, es aufzunehmen oder nicht.",
        "Dadurch wird der Organismus stark gegen das Mittel, wenn er im Augenblick stark genug ist, den Stoff in sich aufzunehmen.",
        "Es gibt keine Möglich­keit, der Krankheit zu entkommen, wenn man die Gesund­heit haben will.",
        "Jede Möglichkeit, sich gegen die äußeren Einflüsse stark zu machen, beruht auf der Möglichkeit, Krankheit zu haben, krank zu sein.",
        "So ist die Krankheit die Bedingung der Gesundheit.",
        "Das ist ein ganz realer Werdegang.",
        "Das ist geradezu die Folgerung und Gabe der Krankheit, daß das Starke vom Menschen erworben wer­den muß.",
        "Was beim Ausschlagen des Pendels überlebt, das hat die Frucht der Immunität aus der Krankheit, - und sogar über den Tod hinaus."
      ],
      [
        "Wer etwas weitergeht, wird gerade daraus eine Art von Verständnis für das Wesen der Krankheit und das Wesen des Todes gewinnen.",
        "Wollen wir die Stärke, die Gesund­heit, dann müssen wir ihre Vorbedingung, die Krankheit, mit in den Kauf nehmen.",
        "Wollen wir stark sein, dann müs-sen wir uns gegen die Schwäche schützen, indem wir die Schwäche in uns selber aufnehmen und in Stärke verwan­deln.",
        "Wenn man dies lebendig auffaßt, wird es uns Krank­heit und Tod begreiflich machen.",
        "Diese Begriffe wird die geisteswissenschaftliche Bewegung der Menschheit bringen.",
        "Heute mag das für viele noch etwas sein, was nur zum Ver­stande spricht.",
        "Wenn aber der Verstand die Sache völlig aufgenommen haben wird, dann wird das eine tiefe har­monische Gemütslage im Menschen bewirken, dann wird das Lebensweisheit werden."
      ],
      [
        "Haben Sie denn noch nicht gehört, daß die anthroposophischen"
      ],
      [
        "Wahrheiten, die aus dem Okkultismus heraus ge­schöpft sind, sogar gefährlich werden können?",
        "Haben wir nicht zahlreiche Gegner, die behaupten, die Anthroposophie sei ein Gift und schädige den Menschen?",
        "Ja, das wissen die Anthroposophen und der Okkultist selber, daß die An­throposophie auch schädlich wirken kann; sie wissen aber auch, daß sie aufgenommen und einverleibt werden muß, um den Menschen stark zu machen, und daß sie nicht nur etwas ist, worüber man diskutieren kann, sondern etwas, was sich dann imLeben bewährt als ein geistiges Heilmittel."
      ],
      [
        "Und das weiß die Geisteswissenschaft auch, daß das Physische aus dem Geistigen heraus aufgebaut wird.",
        "Wir­ken die geistigen Kräfte auf den Ätherleib, dann wirken sie auch als gesund im Zusammenhang des physischen Leibes.",
        "Sind unsere Vorstellungen von der Welt und vom Leben gesund, dann sind diese gesunden Gedanken die kräftigsten Heilmittel, und nur auf schwache Naturen, die durch Mate­rialismus und Naturalismus schwache Naturen geworden sind, wirkt das, was die Anthroposophie als Wahrheit ver­kündigt, krankmachend.",
        "Das müssen sie sich einverleiben, um sich stark zu machen.",
        "Erst dann hat die Anthroposophie ihre Aufgabe erfüllt, wenn sie starke Menschen im Leben erzeugt."
      ],
      [
        "Unsere Frage nach Leben und Tod hat Goethe so schön gelöst: Alles in der Natur ist Leben; sie hat den Tod nur erfunden, um viel Leben zu haben.",
        "Und so könnte man sagen: Sie hat auch neben dem Tod die Krankheit erfun­den, um die starke Gesundheit zu erzeugen, und sie hat not­wendigerweise der Weisheit scheinbar schädigende Wirkung zugeben müssen, damit diese Weisheit kräftigend und hei­lend auf die Menschheit wirkt."
      ],
      [
        "Gerade dadurch unterscheidet sich die geisteswissenschaft­liche Weltbewegung von den anderen Bewegungen, daß"
      ],
      [
        "man über sie streiten und diskutieren kann, wenn man von ihr verlangt, sie solle sich logisch beweisen.",
        "Nicht etwas, was sieh bloß mit logischen Gründen erhärten läßt, soll die Anthroposophie sein, sondern etwas, was die Menschen gei­stig und auch körperlich gesund macht.",
        "Je mehr sie ihre Wirkungen draußen im Leben zeigt, indem sie das Leben so erhöht, daß der Lebensschmerz in Lebensglück verwan­delt wird, desto mehr werden lebendige Beweise für sie da sein.",
        "Mögen die Leute heute noch so sehr glauben, sie könn­ten etwas logisch dagegen einwenden: die Geisteswissen­schaft ist etwas, das wie ein scheinbares Gift umgewandelt wird in ein Heilmittel und dann befruehtend wirkt im Le­ben.",
        "Und nicht in der Logik wird sie sich zeigen - sie kann nicht bloß bewiesen werden - sie wird sich bewähren im Leben."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "DIE ERZIEHUNG DES KINDES VOM STANDPUNKT DER GEISTESWISSENSCHAFT Köln, 1. Dezember 1906",
    "paragraphs": [
      "Als vor drei Jahrzehnten die geisteswissenschaftliche Be­wegung ihren Anfang nahm, handelte es sich bei den eigent-lich führenden Persönlichkeiten nicht darum, eine neue Idee in die Welt zu bringen, nach welcher eine Begierde nach übersinnlichen Welten Befriedigung finden sollte, sondern darum, eine geistige Einsicht weiteren Kreisen zugänglich zu machen, durch welche man die geistigen und auch die praktischen Lebensfragen lösen könne. - Eine von diesen Fragen ist die des heutigen Themas, eine Frage, die uns ins alltägliche Leben hineinführt und darum jeden Menschen interessieren muß. Die Erziehungsfrage kann nur im Zu­sammenhang mit intimer Kenntnis vom Wesen des Men­schen gehandhabt werden. Für keine Strömung ist das Wesen der Geistesforschung günstiger als für die Erziehungsfrage, durch welche sich durch eine Erkenntnis, die eindringt ins übersinnliche Leben, leitende Grundgedanken ergeben.",
      "Wir müssen auch hier wieder ausgehen von der Betrach­tung des Wesens des Menschen. Was der Verstand erfassen kann, das ist ja für die Geistesforschung nur ein Teil des menschlichen Wesens. Das, was wir am Menschen greifen und sehen, diese physische Leibeswesenheit hat er mit der ganzen übrigen Natur gemeinsam. Nicht durch Spekula­tion, nicht durch Gedankenphilosophie, sondern durch das­jenige, was mit hellseherischem Blick der höhere Sinn schauen kann, forscht der Geisteswissenschafter. Ihm zeigt sich als",
      "zweites Glied im Menschen der Atherleib, ein geistiger Or­ganismus, der wesentlich feiner ist als der physische. Er hat nichts mit dem physikalischen Begriff von Ather zu tun und wird besser nicht als ein Stoff, sondern als eine Summe von Kräften, als eine Summe von Strömungen, von Kraifwir­kungen beschrieben. Er ist aber der Architekt des aus ihm heraus kristallisierten physischen Leibes, welcher sich aus ihm herausentwickelt wie etwa das Eis aus dem Wasser. So müssen wir uns vorstellen, daß alles, was am Menschen physischer Leib, physischer Organismus ist, herausgebildet ist aus dem Ätherleib. Diesen haben wir gemeinsam mit allen lebenden Wesen, mit der Pflanzen- und Tierwelt. Er hat eine ähnliche Form wie der physische Leib, seine Form und Größe schließen sich der Form und Größe desselben an. An den unteren Teilen aber ist er verschieden, bei den Tieren ragt er weit heraus. Man beschreibt hiermit, was man als Atherkörper kennt, etwa so, wie man einem Blinden sagt, eine Farbe ist blau oder rot. Ebensowenig wie dem Sehenden dies phantastisch erscheint, ist für den, welcher die in jedem Menschen schlummernden Fähigkeiten entwik­kelt, Phantasie in dem Beschriebenen.",
      "Als drittes Glied des menschlichen Wesens erkennen wir den Astralleib, den Träger von all dem, was wir Leiden­schaften, niedere und zum Teil auch höhere nennen, alles, was der Mensch an Lust und Leid, Freude und Schmerz, Begierde und Trieb in sich trägt. Der Astralkörper ist Trä-ger auch der gewöhnlichen Gedankenwelt, der Willensim­pulse. Er wird wiederum durch die Entwicklung höherer Sinne geschaut.Er umgibt den Menschen wie eine Art Wolke, die den physischen und Ätherleib durchsetzt. Ihn haben wir mit der ganzen Tierwelt gemein. Alles in ihm ist Bewegung, alles spiegelt sich in ihm ab, was an Gemütsbewegungen sich vollzieht. Warum hat er den Namen «Astral»? Wie",
      "der physische Körper durch seine physischen Stoffe mit dem ganzen Erdenkörper zusammenhängt, so steht der Astral­leib mit der ganzen die Erde umgebenden Welt der Sterne in Verbindung. Alle die Kräfte, die den Astralleib durch­dringen und des Menschen Schicksal und Charakter bedin­gen, sind deshalb so benannt worden von solchen, die tief hineingeschaut haben in den geheimnisvollen Zusammen­hang mit der ganzen die Erde umgebenden Astralwelt. In einem orphischen Gesange an den orphischen Urgott drückt Goethe, der tief hineingeschaut hat in die Zusammenhänge zwischen der Natur, dem Menschen und dem Kosmos, in schöner Strophe dasjenige aus, was sich im Astralleib ab­spielt:",
      "Wie an dem Tag, der dich der Welt verliehen,",
      "Die Sonne stand zum Gruße der Planeten,",
      "Bist alsobald und fort und fort gediehen",
      "Nach dem Gesetz, wonach du angetreten.",
      "So mußt du sein, dir kannst du nicht entfliehen!",
      "So sagten schon Sibyllen, so Propheten,",
      "Und keine Zeit und keine Macht zerstückelt",
      "Geprägte Form, die lebend sich entwickelt.",
      "Durch das vierte Glied ist der Mensch die Krone der Schöpfung. Es umfaßt das, als Kraft begriffen, was ihm die Fähigkeit gibt, zu sich «Ich» zu sagen, was ein jeder nur zu sich selbst sagen kann. Es ist der Ausdruck dafür, daß die Seele ihren göttlichen Urfunken in sich sprechen läßt. Alles, was sie mit den anderen Menschen gemeinsam hat, kann als Bezeichnung an ihr Ohr klingen, aber was jeder als inneren Gott in sich hat, kann nicht von außen an ihn herantreten. Deshalb wurde es in den jüdischen Geheimschulen der un­aussprechliche Name Gottes genannt, das Jahve, das «Ich bin der Ich-Bin» der Hebräer, das der Priester selbst nur",
      "mit Schauern nannte. Dieses «Ich bin der Ich-bin» schreibt sich die Seele zu. - Wir sprachen von der Gemeinschaft des physischen Körpers mit der materiellen, des Ätherkörpers mit der Pflanzen-, des Astralkörpers mit der Tierwelt; sein Ich hat der Mensch mit niemand und mit nichts gemeinsam; daher wird er durch dieses zur Krone der Schöpfung. Diese viergliedrige Wesenheit hat man in allen okkulten Schulen als Vierheit der menschlichen Natur angesprochen. Von der Kindheit an bis zum reifen Alter bilden sich diese vier Kör­per heraus, indem jeder dieser Teile sich besonders entwik­kelt. Daher müssen wir jeden am werdenden Menschen gesondert betrachten, wenn wir ihn verstehen wollen. Ver­anlagt finden wir sie alle nicht nur im Kinde, sondern schon im Embryo. Die Entwicklung aber der vier Glieder ist ganz voneinander verschieden. Der Mensch entwickelt sich nicht ohne Umgebung, er ist kein Wesen für sich. Er kann nur gedeihen und sich entwickeln, wenn er von andern Wesen­heiten des Kosmos umgeben ist. Als Embryo muß ihn der mütterliche Organismus umschließen, und erst, wenn er eine gewisse Reife erlangt hat, kann er aus ihm frei werden. Bis zu einer gewissen Stufe muß er umschlossen sein vom müt­terlichen Organismus.",
      "Ähnliche Vorgänge gehen noch öfter mit dem Menschen vor sich während seiner Entwicklung. Geradeso wie der physische Leib als Keim bis zur Geburt vom mütterlichen Organismus umgeben ist, so bleibt der Mensch nachher von geistigen Organen umgeben, die der geistigen Welt ange­hören, von einer Äther- und einer Astralhülle. Er ruht in denselben wie bis zu seiner Geburt im Mutterschoß.",
      "Wenn ein gewisser Zeitpunkt in der Altersentwicklung erreicht ist, die Zeit des Zahnwechsels, dann löst sich um den Ätherleib herum ebenso eine Ätherhülle los wie bei der physischen Geburt die physische Hülle. Da wird dann der",
      "Ätherleib nach allen Richtungen frei, da wird er erst ge­boren. Vorher hatte sich an ihn eine Wesenheit derselben Art angeschlossen, so daß Strömungen hinaus- und hinein­gingen wie die Gefäße der physischen Mutter in den physi­schen Leib des Kindes. So wird nach und nach das Kind zum zweiten Mal, ätherisch, geboren. Dann ist noch immer der Astralleib von einer schützenden Hülle umgeben, von einer den Leib bewegenden und durchkraftenden Hülle bis zur Zeit der Geschlechtsreife. Dann zieht auch die sich zu­rück, und der Mensch wird zum dritten Mal geboren; die astralische Geburt findet statt.",
      "Diese dreifache Geburt zeigt, daß wir jede einzelne die­ser Wesenheiten getrennt betrachten müssen. So wie es un­möglich ist, daß man das äußere Licht an das Auge des Kindes heranbringen kann, solange es im Mutterleibe ist, so ist es für den Seelenzustand, wenn nicht unmöglich, so doch im höchsten Grade schädlich, äußere Einflüsse an den Ätherleib heranzubringen, ehe derselbe nach allen Seiten hin frei geworden ist. Ebensowenig darf an den Astralleib vor der Geschlechtsreife etwas herangebracht werden, was ihn unmittelbar beeinflußt. Vom geisteswissenschaftlichen Standpunkt aus darf auf den Menschen bis zum siebten Jahre erzieherisch nur so gewirkt werden, daß wir bewußt nur seinen physischen Körper beeinflussen. Wir dürfen sei­nen Ätherleib vorher so wenig beeinflussen wie den physi­schen vor der Geburt. Wie aber die Pflege der Mutter von Einfluß ist auf die Entwicklung des Embryo, so muß auch hier die Unantastbarkeit des Ätherleibes geschützt werden, wenn sich das Kind gedeihlich entwickeln soll.",
      "Was heißt das fürs physische Leben? Bis zum Zahnwech­sel ist nur der physische Leib den Wirkungen von außen übergeben; daher dürfen wir bis dahin nur diesen erziehen. Und wenn in dieser Zeit etwas von außen an den Ätherleib",
      "herangebracht wird, so ist das eine Versündigung gegen die Gesetze der Menschenerziehung.",
      "Was am Ätherleib des Menschen haftet, ist nicht nur das, was dem Ätherleib der Pflanze eignet; für den Menschen wird er zum Träger dessen, was von seelischer Dauer ist; Gewohnheiten und Charakter, Gewissen und Gedächtnis, seine bleibende Temperamentsanlage haftet am Ätherleib.",
      "Am Astralleib haftet außer den genannten Gefühlsanlagen die Urteilsfähigkeit. Danach wissen wir, wann wir einzu­greifen haben in die betreffenden Anlagen. So wie bis zum siebenten Jahre die äußeren Sinne des Kindes freigegeben werden, so werden bis zum vierzehnten Jahre die Gewohn­heiten, das Gedächtnis, das Temperament und so weiter frei, und dann bis zum zwanzigsten, zweiundzwanzigsten Jahre der kritische Verstand, das selbständige Verhältnis zur Umwelt. Hieraus ergeben sich ganz bestirninte Erzie­hungsprinzipien für die einzelnen Lebensepochen, nämlich bis zum siebten Jahre die Pflege alles dessen, was Zusam­menhang hat mit dem physischen Leibe. Dies ist nicht nur in äußerer mechanischer Weise aufzufassen, sondern es kommt noch vieles hinzu. Die Organe bilden sich nach und nach aus; wichtige physische Organe kommen zur Entfal­tung in dieser Zeit. Es ist daher wichtig, wie wir auf die Sinne wirken, was das Kind sieht und wahrnimmt. Eine Fähigkeit des Menschen ist hierbei maßgebend, der Nach­ahmungstrieb. Der griechische Philosoph Aristoteles sagt bezeichnend: Der Mensch ist das nachahmendste der Tiere. Bis zum Zahnwechsel ist das für das Kind besonders zu­treffend; da steht es unter dem Zeichen der Nachahmung. Daher muß man in die Umgebung des Kindes alles das bringen, was durch die Sinnesorgane bildend auf dasselbe wirken kann. Dasjenige, was als Lichtstrahl durchs Auge, als Ton durchs Ohr dringt, hat die Bedeutung, daß es für",
      "die physischen Organe bildend wirkt. Durch Ermahnung hingegen wird nichts erlangt in diesen Jahren. Gebot und Verbot haben gar keine Wirkung. Die größte Bedeutung aber hat das Vorbild. Was das Kind sehen kann, das, was geschieht, betrachtet es als etwas, was es tun und nachahmen darf. So überraschte einmal ein gutgeartetes Kind seine Eltern damit, daß es Geld aus einer Kassette genommen hatte. Die Eltern waren entsetzt und glaubten, das Kind hätte einen Hang zum Stehlen. Auf Befragen stellte sich aber heraus, daß das Kind einfach nur nachgeahmt hatte, was es Vater und Mutter täglich hatte tun sehen. Es muß deshalb das Vorbild so sein, daß durch Nachahmung des­selben im Kinde innere Kräfte erweckt werden können. Darum kann man durch Predigen nichts nützen, nur da­durch, wie man in der Umgebung des Kindes ist. Daher soll man mit dem, was man tut, auf die Gegenwart des Kindes Rücksicht nehmen, sich nicht gestatten etwas zu tun, was es nicht nachahmen darf. Es ist dies viel wichtiger, als etwas selbst zu tun und dann dem Kinde zu verbieten.",
      "Es ist also wichtig, daß der Erzieher in diesen Jahren ein Vorbild ist, daß er nur Dinge tut, die das Kind nachahmen darf. Auf Vorbild und Nachahmung beruht die Erziehung in diesen Jahren. Das erkennt der, welcher hineinsieht in die Wesenheit des Menschen, und der Erfolg gibt ihm recht. Darnach ist es auch nicht richtig, dem Kind vor dem Zahn-wechsel den Sinn der Buchstaben einprägen zu wollen; es kann zunächst nur die Form derselben nachahmen, indem es sie nachmalt. Denn die Kraft zum Begreifen des Sinnes haftet erst am Ätherleib.",
      "Alle diese Feinheiten lassen sich begreifen vermöge der Geistesforschung; bis ins einzelne kann diese Wissenschaft hineinleuchten in das, was zu geschehen hat. Organbildend, für die physischen Organe von Bedeutung ist alles das, was",
      "in der Umgebung des Kindes vor sich geht, auch in mora­lischer Beziehung, und von dem Kinde wahrgenommen wird. So ist es nicht gleichgültig, ob das kleine Kind Schmerz und Leid oder Freude und Lust um sich her sieht. Denn Freude und Lust begründen gesunde Anlagen, sind gesunde Organbildner; was anderes einfließt, kann zum Begründer von Krankheit werden. Alles um das Kind her­um sollte Freude und Lust atmen, und beides hervorzu­rufen sollte der Erzieher bedacht sein, bis auf die Farbe der Kleider, der Tapeten und der Gegenstände. Dabei ist sorg­fältig die individuelle Anlage des Kindes zu berücksichtigen.",
      "Ein Kind, das zu Ernst und Stille neigt, sollte dunklere, bläuliche, grünliche Farben in seiner Umgebung sehen, ein lebhaftes, lebendiges Kind gelbliche, rötliche Farben. Dies scheint ein Widerspruch zu sein. Allein es verhält sich so, daß durch die Fähigkeit der Sinne die Erweckung der Ge­genfarbe wachgerufen wird. Das Bläuliche wirkt belebend, während für lebhafte Kinder die ins gelblich-rötliche spie­lenden Töne die Gegenfärbung aufrufen.",
      "Sie sehen, ganz ins Praktische hinein leuchtet da die Gei­stesforschung. Die Organe, welche in der Entwicklung sind, muß man so behandeln, daß sie sich entsprechend entfalten können, daß sie veranlaßt werden, die inneren Kräfte her-auszubilden. Darum sollte man dem Kinde auch keine fer­tigen Spielsachen geben wie Baukasten, Puppen und so weiter. Man gebe ihm lieber eine aus einer alten Serviette hergestellte Puppe mit Tintenaugen, Nase und Mund. Jedes Kind zieht eine selbstgemachte Puppe, aus einem Stiefel-knecht oder einer alten Serviette, den schön ausgeputzten Wachsdamen vor. Warum? Weil dadurch die Imagination geweckt wird, weil die Phantasie in Tätigkeit gesetzt wird und die inneren Organe anfangen zu arbeiten zur Freude und Lust des Kindes. Wie lebendig und interessiert ist solch",
      "ein Kind bei einem Spiel, wie geht es mit Leib und Seele auf in dem, was seine Imaginationen ihm vorspielen. Wie lässig und unvergnügt sitzt das andere da; denn bei einer fertigen Puppe ist keine Möglichkeit mehr, etwas hinzu zu ergänzen, und seine inneren Organe werden zur Untätig­keit verdammt, wenn es solche fertigen Dinge bekommt. Solange der physische Leib in seiner Entwicklung begriffen ist, hat das Kind einen außerordentlich gesunden Instinkt für das, was ihm gut ist, wenn er ihm nicht verdorben wird. Solange der physische Leib der einzige ist, der frei zur Außenwelt in Beziehung steht, zeigt er selbst, was ihm frommt. Wenn frühzeitig viel weiter eingegriffen wird, so wird dieser Instinkt ausgetrieben, der sonst zeigt, was dem Kind gedeihlich ist. Auf Freude, Lust und Begierde muß sich hier die Erziehung aufbauen. In dieser Zeit wäre jeg­licher Anflug von Askese gleichbedeutend mit Ausrottung der natürlichen Gesundheit und Entwicklungsmöglichkeit.",
      "Wenn das Kind gegen sein siebentes Jahr hinlebt, bei dem allmählichen Zahnwechsel, lösen sich die äußeren Hüllen des Ätherleibes ab und dieser wird ebenso frei, wie vorher der physische Leib. Jetzt muß der Erzieher alles heran­bringen, was den Ätherleib ausbildet. Aber er muß sich hüten, zu großen Wert darauf zu legen, daß die Vernunft und der Verstand ausgebildet werden. In dieser Zeit, zwi­schen dem siebenten und zwölften Jahre des Kindes handelt es sich vorzugsweise um Autorität, Glauben, Vertrauen und Ehrfurcht. Gewohnheit und Charakter sind die speziellen Äußerungen des Ätherleibes, während auf die Urteilskraft in dieser Zeit nicht gewirkt werden soll, da dies vor der Geschlechtsreife ohne Schaden nicht geschehen kann.",
      "Die Ausbildung des Ätherleibes fällt in die Zeit vom siebenten bis zum sechzehnten Jahre, beim Mädchen bis zum vierzehnten Jahr. Fürs ganze spätere Leben bleibt von",
      "Wichtigkeit, daß in dem Kinde das Gefühl von Ehrfurcht geweckt und genährt wird. Das kann etwa folgendermaßen geschehen: Es wird ihm von bedeutenden Menschen nicht nur der Geschichte, sondern auch aus den umgebenden Le­benskreisen ein Bild gegeben durch Mitteilungen und Er­zählungen, etwa von einem Verwandten, vor dem man Achtung und Ehrfurcht haben kann.",
      "Es wird dem Kinde Ehrfurcht und Scheu eingeflößt, die ihm verbietet, irgend­einen Gedanken von Kritik oder Opposition der verehrten Person gegenüber aufkommen zu lassen. Dann darf es die­sen Menschen einmal sehen; es lebt in heiliger Erwartung des Augenblicks, und eines Tages steht es vor der Türe dieser Person und empfindet eine heilige Scheu, auf die Klinke zu drücken und das Zimmer zu betreten, das ihm ein Heiligtum ist.",
      "Diese Momente der Ehrfurcht sind Kräfte für das spätere Leben. Von ungeheurer Bedeutung ist, daß der Erzieher, der Lehrer selbst, in dieser Zeit dem Kinde Autorität sei. Nicht an Grundsätze muß das Kind glauben, sondern an Menschen.",
      "Die Menschen, die das Kind um­geben, die es sieht und hört, die müssen seine Ideale sein, und aus der Geschichte oder Literatur muß es sie wählen. Hier gilt der Spruch: «Ein Jeder muß sich seinen Helden wählen, dem er die Wege zum Olymp hinauf sich nach­arbeitet.» Ganz falsch ist es, wenn die materialistischeWelt­anschauung gegen die Autorität sich ausspricht, das Kind schon zur Selbständigkeit anhält und das Gefühl der Hin­gebung und Verehrung mißachtet.",
      "Die gesunde Entwicklung leidet Schaden, wenn es schon vor der Geburt des Astral­leibes auf sein eigenes Urteil gestellt wird. Wichtig ist, daß in dieser Zeit das Gedächtnis herausgebildet wird, und zwar geschieht das am besten auf ganz mechanische Weise.",
      "Nicht die Rechenmaschine sollte benützt werden, sondern ganz mechanisch gedächtnismäßig sollte das Einmaleins, sollten",
      "Gedichte und so weiter eingeprägt werden. Nur ein mate­rialistisches Vorurteil kann für diese Zeit behaupten, daß man sich diese Dinge erst merken soll, wenn man sie ver­steht. In alten Zeiten hat man in dieser Hinsicht richtiger erzogen.",
      "Vom ersten bis siebenten Jahre sang man vor, allerlei Verse, die guten alten Ammen- und Kinderlieder. Es kommt dabei nicht auf den Sinn an, und so finden wir in alten Liedern zwischen bedeutungsvollen Zeilen etwas, was nur wegen des Klanges da ist.",
      "Es kam beim Vorsingen nur auf den Zusammenklang und die Harmonie für das kindliche Ohr an, daher die oft sinnlosen Reime. Zum Bei­spiel: «Flieg, Käfer flieg, dein Vater ist im Krieg, deine Mutter ist im Pommerland, Pommerland ist abgebrannt; flieg, Käfer, flieg.» Pommerland bedeutet, nebenbei gesagt, in der Mundart des Kindes Mutterland.",
      "Der Ausdruck stammt noch aus jener Zeit, in der man an den geistigen Menschen geglaubt hat, der aus der geistigen in die physi­sche Welt kommt. Pommerland war das Land der geistigen Herkunft. Nicht auf den Sinn aber kommt es hier an, son­dern auf den Klang.",
      "Daher haben wir soviele, viele Kinder­lieder, die eigentlichen Sinn nicht aufweisen. - Gedächtnis, Gewohnheit und Charakter müssen in ihren Grundfesten in dieser Periode angelegt werden. Der Weg dazu ist die Autorität.",
      "Ein Mensch, bei dem dies nicht geschieht, weist eine mangelhafte Erziehung auf. Wo richtig erzogen wird, muß das Hinaufschauen zur Autorität in dieser Zeit zur Geltung kommen, während Grundsätze erst nach der astra­lischen Geburt am Platze sind.",
      "Dasjenige, was vom Kind als innerste Natur eines Menschen geahnt wird, was in der Autorität verehrt wird, was überhaupt zu ihm strömt vom Erzieher, das bildet des Kindes Gewissen, den Charakter und sogar sein Temperament aus und wird zur dauernden Anlage bei ihm. Dann müssen wir uns klar sein, daß in",
      "diesen Jahren bildend auf den Ätherleib wirkt, was durch Gleichnisse und Sinnbilder den Geist der Welt kennen­lernen läßt. Daher der Segen der Märchenbilder in dieser Zeit und das Vorführen großer Persönlichkeiten und Hel­den in Sage und Geschichte.",
      "Man muß in dieser Zeit auf die Pflege des Ätherleibes ebenso bedacht sein wie vorher auf diejenige des physischen Leibes. Wie in den ersten Jahren durch Lust und Freude organbildend gewirkt wurde, so muß vom siebenten bis zum vierzehnten - für die Jungen bis zum sechzehnten - Lebens­jahre alles ausgebildet werden, was das Gefühl erhöhter Gesundheit und Lebensfreudigkeit hervorruft; daher der Wert des Turnunterrichtes. Mangelhaft ist derselbe aber, wenn der Turnlehrer mit dem Blick des Anatomen die Tur­ner betrachtet, wenn er nur nach dem äußeren Zweck einer Gliedbewegung zielt. Es kommt vielmehr darauf an, daß der Lehrer sich intuitiv so hineindenkt in die fühlende Seele des Kindes, daß er weiß, durch welche Bewegung des Leibes die Seele den Eindruck von Kraftgefühl, von Gesundheits­gefühl bekommt, was dem Menschen Wohlgefühl, Lust sei­ner eigenen Leiblichkeit bereitet. So erst bekommt die Turn­übung einen innerlichen Wert und Einfluß auf das Gefühl der wachsenden Kraft. Eine rechte Turnübung ist nicht nur für das äußerlich anschauende Auge, sondern auch für den fühlenden Menschen.",
      "Einen großen Einfluß bis in den Äther- und Astralleib hinein übt jedes Künstlerische. Daher muß echtes, wahres Künstlerisches den Ätherleib durchdringen. Gute Vokal-und Instrumentalmusik zum Beispiel ist von hoher Be­deutung, und das Kinderauge sollte viel Schönes um sich her erblicken.",
      "Aber durch nichts ist der Religionsunterricht zu ersetzen. Die Bilder des Übersinnlichen prägen sich tief in den Ätherleib",
      "ein. Es kommt hier nicht darauf an, daß der Schüler kritisieren kann, daß er sein Urteil fällt über irgendein Glaubensbekenntnis, sondern darauf, daß er eine Anschau­ung empfängt von dem, was übersinnlich ist, was über das Vergängliche hinausgeht. Daher sind alle religiösen Vor­stellungen in bildliche Darstellungen zu bringen.",
      "Die größte Sorgfalt muß gelegt werden auf die Erzie­hung aus dem Lebendigen heraus. Dadurch, daß das Kind zu viel mit totem Stoff zu tun bekommt, wird viel an ihm verdorben, während alles, woran es das Lebendige ahnen kann, wichtig ist für den Ätherleib. Alles sollte Handlung, Tat, Leben sein; das belebt den Geist. Selbst im Spielzeug ist dies Moment von Bedeutung. So sind die alten Bilder­bücher zum Ziehen, zwei Klötze, die es hämmernd ver­binden kann, anregend, indem sie die Ahnung von innerer Bewegung des Lebens geben. Nichts Schlimmeres für den Geist, als aus fertigen geometrischen Gegenständen Formen zusammenstellen und -setzen zu lassen. Darum soll das Kind nicht mit dem Baukasten bauen, sondern von Grund auf alles selbst aufbauen. Das Kind muß lernen, das Lebendige aus dem Unlebendigen zu machen. Durch das Fertige, Un­lebendige wird die materielle Zeit das Lebendige auslöschen. Vieles erstirbt an dem sich entwickelnden Gehirn, wenn das Kind Dinge machen soll, die keinen Sinn haben, wie Flecht­arbeiten und so weiter. Ganze Anlagen bleiben dadurch unentwickelt. Vieles, was Unheil in unserem sozialen Zu­sammenleben bedeutet, ist auf die Kinderstube zurückzu­führen. Das Spielzeug des Unlebendigen bildet auch nicht den Glauben an das Lebendige heran, und daher besteht der tiefere Zusammenhang zwischen der Kindererziehung und der Glaubenslosigkeit unseres Zeitalters. So haben die Dinge einen tiefen Zusammenhang",
      "Wenn die Geschlechtsreife erlangt wird, fallen die astralen",
      "Hüllen, von denen der Leib umgeben ist, ebenfalls ab. Mit dem Gefühl für das andere Geschlecht tritt die persön­liche Urteilskraft hervor. Jetzt erst kommt die Zeit, in der man an die Urteilskraft appellieren kann, an das Ja und Nein, an den kritischen Verstand. Kaum dann, wenn der Mensch diesen Jahren entwachsen ist, vermag er ein eigenes Urteil abzugeben, geschweige denn früher. Es ist ein Un­ding, wenn solche jungen Menschen schon urteilen und auf die Kultur, auch nur im kleinsten Umfang, Einfluß ausüben wollen. So wenig ein Kind im Mutterleibe hören und sehen kann, vermag der noch nicht astral entwickelte Mensch vor dem zwanzigsten Jahr ein gesundes Urteil zu bilden. Für jedes Lebensalter ist der entsprechende Einfluß nötig, für das erste Vorbild, Nachahmung, für das zweite Autorität und Nacheiferung, für das dritte Grundsätze. - Äußerst wichtig ist, wer den jungen Menschen in diesem Lebensalter als Lehrer entgegentritt, um ihnen ihre Lernbegierde und ihren Freiheitsdrang in die rechten Bahnen zu lenken.",
      "Die geistige Weltanschauung erfüllt den Erzieher mit einer Fülle von Grundsätzen. Diese Grundsätze helfen dem Lehrer bei der Entwicklung des Menschengeschlechtes. Gei­steswissenschaft kann dadurch praktisch eingreifen in die wichtigsten Vorgänge des Menschenlebens und wir sehen sie im richtigen Verhältnis zum täglichen Leben. Dadurch, daß wir den Menschen in allen seinen Gliedern kennen, wissen wir, auf welche Glieder wir zu wirken haben und was wir tun müssen, damit unter solchen Verhältnissen, wie sie wirklich sind, der Mensch gedeiht. Wenn eine Mutter sich selbst nicht ordentlich ernähren kann, so wirkt das durch den Mutterleib auf den Embryo; wie dessen Mutter gepflegt werden muß, so auch die spätere Umgebung des Kindes; dadurch wird das Kind mitgepflegt. Das ist etwas, was auch ins Geistige zu übertragen ist. Weil nun das Kind",
      "in der Äther-Mutterhülle schlummert, in der Astral-Um­gebung wurzelt, so kommt es darauf an, wie in seiner Um­gebung die Dinge sich vollziehen. Jeder. Gedanke, jedes Gefühl, alles Unausgesprochene, was diejenigen bewegt, die in seiner Umgebung sind, wirkt mit; da gilt nicht: Fühlen und denken darfst du dies und jenes wohl, wenn du es nur nicht sagst. - Mit reinen Gedanken und Gefühlen muß man das Kind umgeben und darum bis ins innerste Herz Rein­heit bewahren, keine unlauteren Gedanken sich gestatten. Durch Worte wirken wir nur auf das Sinnesvermögen, Ge­fühle und Gedanken impfen wir der schützenden Mutter-hülle des Äther- und Astralleibes ein und sie gehen auf das Kind über. Solange es von Hüllen umgeben ist, müssen wir diese pflegen. Pfropft man unreine Gedanken und Leiden­schaften in diese hinein, so verdirbt man ebensoviel, als wenn man in die physische Hülle des Mutterleibes Schäd­liches bringt. Bis in diese Feinheiten hinein vermag somit die geistige Weltanschauung zu leuchten. Aus der Erkennt­nis der Menschennatur heraus erfüllt sie den Erzieher mit der nötigen Einsicht.",
      "Geisteswissenschaft soll nicht eine Theorie sein und Über­zeugungen lehren; sie soll handeln, eingreifen ins praktische Leben. Indem sie gesundes Leben bewirkt, indem sie ge­sunde Menschen in leiblicher und geistiger Beziehung macht, erweist sie sich nicht nur als richtige, sondern als gesunde Wahrheit, die ausfließen muß in das ganze Leben des Men­schen. Am besten können wir durch Geisteswissenschaft der Menschheit dienen und ihr soziale und andere Kräfte zu­führen, wenn wir diese herausholen aus dem werdenden Menschen. Der werdende, der sich entwickelnde Mensch ist eines der größten Rätsel des Lebens. Derjenige, der es prak­tisch löst, erweist sich als der rechte Erzieher, als der wahre Rätsellöser in der Bildung des Menschen."
    ],
    "sentences": [
      [
        "Als vor drei Jahrzehnten die geisteswissenschaftliche Be­wegung ihren Anfang nahm, handelte es sich bei den eigent-lich führenden Persönlichkeiten nicht darum, eine neue Idee in die Welt zu bringen, nach welcher eine Begierde nach übersinnlichen Welten Befriedigung finden sollte, sondern darum, eine geistige Einsicht weiteren Kreisen zugänglich zu machen, durch welche man die geistigen und auch die praktischen Lebensfragen lösen könne. - Eine von diesen Fragen ist die des heutigen Themas, eine Frage, die uns ins alltägliche Leben hineinführt und darum jeden Menschen interessieren muß.",
        "Die Erziehungsfrage kann nur im Zu­sammenhang mit intimer Kenntnis vom Wesen des Men­schen gehandhabt werden.",
        "Für keine Strömung ist das Wesen der Geistesforschung günstiger als für die Erziehungsfrage, durch welche sich durch eine Erkenntnis, die eindringt ins übersinnliche Leben, leitende Grundgedanken ergeben."
      ],
      [
        "Wir müssen auch hier wieder ausgehen von der Betrach­tung des Wesens des Menschen.",
        "Was der Verstand erfassen kann, das ist ja für die Geistesforschung nur ein Teil des menschlichen Wesens.",
        "Das, was wir am Menschen greifen und sehen, diese physische Leibeswesenheit hat er mit der ganzen übrigen Natur gemeinsam.",
        "Nicht durch Spekula­tion, nicht durch Gedankenphilosophie, sondern durch das­jenige, was mit hellseherischem Blick der höhere Sinn schauen kann, forscht der Geisteswissenschafter.",
        "Ihm zeigt sich als"
      ],
      [
        "zweites Glied im Menschen der Atherleib, ein geistiger Or­ganismus, der wesentlich feiner ist als der physische.",
        "Er hat nichts mit dem physikalischen Begriff von Ather zu tun und wird besser nicht als ein Stoff, sondern als eine Summe von Kräften, als eine Summe von Strömungen, von Kraifwir­kungen beschrieben.",
        "Er ist aber der Architekt des aus ihm heraus kristallisierten physischen Leibes, welcher sich aus ihm herausentwickelt wie etwa das Eis aus dem Wasser.",
        "So müssen wir uns vorstellen, daß alles, was am Menschen physischer Leib, physischer Organismus ist, herausgebildet ist aus dem Ätherleib.",
        "Diesen haben wir gemeinsam mit allen lebenden Wesen, mit der Pflanzen- und Tierwelt.",
        "Er hat eine ähnliche Form wie der physische Leib, seine Form und Größe schließen sich der Form und Größe desselben an.",
        "An den unteren Teilen aber ist er verschieden, bei den Tieren ragt er weit heraus.",
        "Man beschreibt hiermit, was man als Atherkörper kennt, etwa so, wie man einem Blinden sagt, eine Farbe ist blau oder rot.",
        "Ebensowenig wie dem Sehenden dies phantastisch erscheint, ist für den, welcher die in jedem Menschen schlummernden Fähigkeiten entwik­kelt, Phantasie in dem Beschriebenen."
      ],
      [
        "Als drittes Glied des menschlichen Wesens erkennen wir den Astralleib, den Träger von all dem, was wir Leiden­schaften, niedere und zum Teil auch höhere nennen, alles, was der Mensch an Lust und Leid, Freude und Schmerz, Begierde und Trieb in sich trägt.",
        "Der Astralkörper ist Trä-ger auch der gewöhnlichen Gedankenwelt, der Willensim­pulse.",
        "Er wird wiederum durch die Entwicklung höherer Sinne geschaut.Er umgibt den Menschen wie eine Art Wolke, die den physischen und Ätherleib durchsetzt.",
        "Ihn haben wir mit der ganzen Tierwelt gemein.",
        "Alles in ihm ist Bewegung, alles spiegelt sich in ihm ab, was an Gemütsbewegungen sich vollzieht.",
        "Warum hat er den Namen «Astral»?"
      ],
      [
        "der physische Körper durch seine physischen Stoffe mit dem ganzen Erdenkörper zusammenhängt, so steht der Astral­leib mit der ganzen die Erde umgebenden Welt der Sterne in Verbindung.",
        "Alle die Kräfte, die den Astralleib durch­dringen und des Menschen Schicksal und Charakter bedin­gen, sind deshalb so benannt worden von solchen, die tief hineingeschaut haben in den geheimnisvollen Zusammen­hang mit der ganzen die Erde umgebenden Astralwelt.",
        "In einem orphischen Gesange an den orphischen Urgott drückt Goethe, der tief hineingeschaut hat in die Zusammenhänge zwischen der Natur, dem Menschen und dem Kosmos, in schöner Strophe dasjenige aus, was sich im Astralleib ab­spielt:"
      ],
      [
        "Wie an dem Tag, der dich der Welt verliehen,"
      ],
      [
        "Die Sonne stand zum Gruße der Planeten,"
      ],
      [
        "Bist alsobald und fort und fort gediehen"
      ],
      [
        "Nach dem Gesetz, wonach du angetreten."
      ],
      [
        "So mußt du sein, dir kannst du nicht entfliehen!"
      ],
      [
        "So sagten schon Sibyllen, so Propheten,"
      ],
      [
        "Und keine Zeit und keine Macht zerstückelt"
      ],
      [
        "Geprägte Form, die lebend sich entwickelt."
      ],
      [
        "Durch das vierte Glied ist der Mensch die Krone der Schöpfung.",
        "Es umfaßt das, als Kraft begriffen, was ihm die Fähigkeit gibt, zu sich «Ich» zu sagen, was ein jeder nur zu sich selbst sagen kann.",
        "Es ist der Ausdruck dafür, daß die Seele ihren göttlichen Urfunken in sich sprechen läßt.",
        "Alles, was sie mit den anderen Menschen gemeinsam hat, kann als Bezeichnung an ihr Ohr klingen, aber was jeder als inneren Gott in sich hat, kann nicht von außen an ihn herantreten.",
        "Deshalb wurde es in den jüdischen Geheimschulen der un­aussprechliche Name Gottes genannt, das Jahve, das «Ich bin der Ich-Bin» der Hebräer, das der Priester selbst nur"
      ],
      [
        "mit Schauern nannte.",
        "Dieses «Ich bin der Ich-bin» schreibt sich die Seele zu. - Wir sprachen von der Gemeinschaft des physischen Körpers mit der materiellen, des Ätherkörpers mit der Pflanzen-, des Astralkörpers mit der Tierwelt; sein Ich hat der Mensch mit niemand und mit nichts gemeinsam; daher wird er durch dieses zur Krone der Schöpfung.",
        "Diese viergliedrige Wesenheit hat man in allen okkulten Schulen als Vierheit der menschlichen Natur angesprochen.",
        "Von der Kindheit an bis zum reifen Alter bilden sich diese vier Kör­per heraus, indem jeder dieser Teile sich besonders entwik­kelt.",
        "Daher müssen wir jeden am werdenden Menschen gesondert betrachten, wenn wir ihn verstehen wollen.",
        "Ver­anlagt finden wir sie alle nicht nur im Kinde, sondern schon im Embryo.",
        "Die Entwicklung aber der vier Glieder ist ganz voneinander verschieden.",
        "Der Mensch entwickelt sich nicht ohne Umgebung, er ist kein Wesen für sich.",
        "Er kann nur gedeihen und sich entwickeln, wenn er von andern Wesen­heiten des Kosmos umgeben ist.",
        "Als Embryo muß ihn der mütterliche Organismus umschließen, und erst, wenn er eine gewisse Reife erlangt hat, kann er aus ihm frei werden.",
        "Bis zu einer gewissen Stufe muß er umschlossen sein vom müt­terlichen Organismus."
      ],
      [
        "Ähnliche Vorgänge gehen noch öfter mit dem Menschen vor sich während seiner Entwicklung.",
        "Geradeso wie der physische Leib als Keim bis zur Geburt vom mütterlichen Organismus umgeben ist, so bleibt der Mensch nachher von geistigen Organen umgeben, die der geistigen Welt ange­hören, von einer Äther- und einer Astralhülle.",
        "Er ruht in denselben wie bis zu seiner Geburt im Mutterschoß."
      ],
      [
        "Wenn ein gewisser Zeitpunkt in der Altersentwicklung erreicht ist, die Zeit des Zahnwechsels, dann löst sich um den Ätherleib herum ebenso eine Ätherhülle los wie bei der physischen Geburt die physische Hülle.",
        "Da wird dann der"
      ],
      [
        "Ätherleib nach allen Richtungen frei, da wird er erst ge­boren.",
        "Vorher hatte sich an ihn eine Wesenheit derselben Art angeschlossen, so daß Strömungen hinaus- und hinein­gingen wie die Gefäße der physischen Mutter in den physi­schen Leib des Kindes.",
        "So wird nach und nach das Kind zum zweiten Mal, ätherisch, geboren.",
        "Dann ist noch immer der Astralleib von einer schützenden Hülle umgeben, von einer den Leib bewegenden und durchkraftenden Hülle bis zur Zeit der Geschlechtsreife.",
        "Dann zieht auch die sich zu­rück, und der Mensch wird zum dritten Mal geboren; die astralische Geburt findet statt."
      ],
      [
        "Diese dreifache Geburt zeigt, daß wir jede einzelne die­ser Wesenheiten getrennt betrachten müssen.",
        "So wie es un­möglich ist, daß man das äußere Licht an das Auge des Kindes heranbringen kann, solange es im Mutterleibe ist, so ist es für den Seelenzustand, wenn nicht unmöglich, so doch im höchsten Grade schädlich, äußere Einflüsse an den Ätherleib heranzubringen, ehe derselbe nach allen Seiten hin frei geworden ist.",
        "Ebensowenig darf an den Astralleib vor der Geschlechtsreife etwas herangebracht werden, was ihn unmittelbar beeinflußt.",
        "Vom geisteswissenschaftlichen Standpunkt aus darf auf den Menschen bis zum siebten Jahre erzieherisch nur so gewirkt werden, daß wir bewußt nur seinen physischen Körper beeinflussen.",
        "Wir dürfen sei­nen Ätherleib vorher so wenig beeinflussen wie den physi­schen vor der Geburt.",
        "Wie aber die Pflege der Mutter von Einfluß ist auf die Entwicklung des Embryo, so muß auch hier die Unantastbarkeit des Ätherleibes geschützt werden, wenn sich das Kind gedeihlich entwickeln soll."
      ],
      [
        "Was heißt das fürs physische Leben?",
        "Bis zum Zahnwech­sel ist nur der physische Leib den Wirkungen von außen übergeben; daher dürfen wir bis dahin nur diesen erziehen.",
        "Und wenn in dieser Zeit etwas von außen an den Ätherleib"
      ],
      [
        "herangebracht wird, so ist das eine Versündigung gegen die Gesetze der Menschenerziehung."
      ],
      [
        "Was am Ätherleib des Menschen haftet, ist nicht nur das, was dem Ätherleib der Pflanze eignet; für den Menschen wird er zum Träger dessen, was von seelischer Dauer ist; Gewohnheiten und Charakter, Gewissen und Gedächtnis, seine bleibende Temperamentsanlage haftet am Ätherleib."
      ],
      [
        "Am Astralleib haftet außer den genannten Gefühlsanlagen die Urteilsfähigkeit.",
        "Danach wissen wir, wann wir einzu­greifen haben in die betreffenden Anlagen.",
        "So wie bis zum siebenten Jahre die äußeren Sinne des Kindes freigegeben werden, so werden bis zum vierzehnten Jahre die Gewohn­heiten, das Gedächtnis, das Temperament und so weiter frei, und dann bis zum zwanzigsten, zweiundzwanzigsten Jahre der kritische Verstand, das selbständige Verhältnis zur Umwelt.",
        "Hieraus ergeben sich ganz bestirninte Erzie­hungsprinzipien für die einzelnen Lebensepochen, nämlich bis zum siebten Jahre die Pflege alles dessen, was Zusam­menhang hat mit dem physischen Leibe.",
        "Dies ist nicht nur in äußerer mechanischer Weise aufzufassen, sondern es kommt noch vieles hinzu.",
        "Die Organe bilden sich nach und nach aus; wichtige physische Organe kommen zur Entfal­tung in dieser Zeit.",
        "Es ist daher wichtig, wie wir auf die Sinne wirken, was das Kind sieht und wahrnimmt.",
        "Eine Fähigkeit des Menschen ist hierbei maßgebend, der Nach­ahmungstrieb.",
        "Der griechische Philosoph Aristoteles sagt bezeichnend: Der Mensch ist das nachahmendste der Tiere.",
        "Bis zum Zahnwechsel ist das für das Kind besonders zu­treffend; da steht es unter dem Zeichen der Nachahmung.",
        "Daher muß man in die Umgebung des Kindes alles das bringen, was durch die Sinnesorgane bildend auf dasselbe wirken kann.",
        "Dasjenige, was als Lichtstrahl durchs Auge, als Ton durchs Ohr dringt, hat die Bedeutung, daß es für"
      ],
      [
        "die physischen Organe bildend wirkt.",
        "Durch Ermahnung hingegen wird nichts erlangt in diesen Jahren.",
        "Gebot und Verbot haben gar keine Wirkung.",
        "Die größte Bedeutung aber hat das Vorbild.",
        "Was das Kind sehen kann, das, was geschieht, betrachtet es als etwas, was es tun und nachahmen darf.",
        "So überraschte einmal ein gutgeartetes Kind seine Eltern damit, daß es Geld aus einer Kassette genommen hatte.",
        "Die Eltern waren entsetzt und glaubten, das Kind hätte einen Hang zum Stehlen.",
        "Auf Befragen stellte sich aber heraus, daß das Kind einfach nur nachgeahmt hatte, was es Vater und Mutter täglich hatte tun sehen.",
        "Es muß deshalb das Vorbild so sein, daß durch Nachahmung des­selben im Kinde innere Kräfte erweckt werden können.",
        "Darum kann man durch Predigen nichts nützen, nur da­durch, wie man in der Umgebung des Kindes ist.",
        "Daher soll man mit dem, was man tut, auf die Gegenwart des Kindes Rücksicht nehmen, sich nicht gestatten etwas zu tun, was es nicht nachahmen darf.",
        "Es ist dies viel wichtiger, als etwas selbst zu tun und dann dem Kinde zu verbieten."
      ],
      [
        "Es ist also wichtig, daß der Erzieher in diesen Jahren ein Vorbild ist, daß er nur Dinge tut, die das Kind nachahmen darf.",
        "Auf Vorbild und Nachahmung beruht die Erziehung in diesen Jahren.",
        "Das erkennt der, welcher hineinsieht in die Wesenheit des Menschen, und der Erfolg gibt ihm recht.",
        "Darnach ist es auch nicht richtig, dem Kind vor dem Zahn-wechsel den Sinn der Buchstaben einprägen zu wollen; es kann zunächst nur die Form derselben nachahmen, indem es sie nachmalt.",
        "Denn die Kraft zum Begreifen des Sinnes haftet erst am Ätherleib."
      ],
      [
        "Alle diese Feinheiten lassen sich begreifen vermöge der Geistesforschung; bis ins einzelne kann diese Wissenschaft hineinleuchten in das, was zu geschehen hat.",
        "Organbildend, für die physischen Organe von Bedeutung ist alles das, was"
      ],
      [
        "in der Umgebung des Kindes vor sich geht, auch in mora­lischer Beziehung, und von dem Kinde wahrgenommen wird.",
        "So ist es nicht gleichgültig, ob das kleine Kind Schmerz und Leid oder Freude und Lust um sich her sieht.",
        "Denn Freude und Lust begründen gesunde Anlagen, sind gesunde Organbildner; was anderes einfließt, kann zum Begründer von Krankheit werden.",
        "Alles um das Kind her­um sollte Freude und Lust atmen, und beides hervorzu­rufen sollte der Erzieher bedacht sein, bis auf die Farbe der Kleider, der Tapeten und der Gegenstände.",
        "Dabei ist sorg­fältig die individuelle Anlage des Kindes zu berücksichtigen."
      ],
      [
        "Ein Kind, das zu Ernst und Stille neigt, sollte dunklere, bläuliche, grünliche Farben in seiner Umgebung sehen, ein lebhaftes, lebendiges Kind gelbliche, rötliche Farben.",
        "Dies scheint ein Widerspruch zu sein.",
        "Allein es verhält sich so, daß durch die Fähigkeit der Sinne die Erweckung der Ge­genfarbe wachgerufen wird.",
        "Das Bläuliche wirkt belebend, während für lebhafte Kinder die ins gelblich-rötliche spie­lenden Töne die Gegenfärbung aufrufen."
      ],
      [
        "Sie sehen, ganz ins Praktische hinein leuchtet da die Gei­stesforschung.",
        "Die Organe, welche in der Entwicklung sind, muß man so behandeln, daß sie sich entsprechend entfalten können, daß sie veranlaßt werden, die inneren Kräfte her-auszubilden.",
        "Darum sollte man dem Kinde auch keine fer­tigen Spielsachen geben wie Baukasten, Puppen und so weiter.",
        "Man gebe ihm lieber eine aus einer alten Serviette hergestellte Puppe mit Tintenaugen, Nase und Mund.",
        "Jedes Kind zieht eine selbstgemachte Puppe, aus einem Stiefel-knecht oder einer alten Serviette, den schön ausgeputzten Wachsdamen vor.",
        "Warum?",
        "Weil dadurch die Imagination geweckt wird, weil die Phantasie in Tätigkeit gesetzt wird und die inneren Organe anfangen zu arbeiten zur Freude und Lust des Kindes.",
        "Wie lebendig und interessiert ist solch"
      ],
      [
        "ein Kind bei einem Spiel, wie geht es mit Leib und Seele auf in dem, was seine Imaginationen ihm vorspielen.",
        "Wie lässig und unvergnügt sitzt das andere da; denn bei einer fertigen Puppe ist keine Möglichkeit mehr, etwas hinzu zu ergänzen, und seine inneren Organe werden zur Untätig­keit verdammt, wenn es solche fertigen Dinge bekommt.",
        "Solange der physische Leib in seiner Entwicklung begriffen ist, hat das Kind einen außerordentlich gesunden Instinkt für das, was ihm gut ist, wenn er ihm nicht verdorben wird.",
        "Solange der physische Leib der einzige ist, der frei zur Außenwelt in Beziehung steht, zeigt er selbst, was ihm frommt.",
        "Wenn frühzeitig viel weiter eingegriffen wird, so wird dieser Instinkt ausgetrieben, der sonst zeigt, was dem Kind gedeihlich ist.",
        "Auf Freude, Lust und Begierde muß sich hier die Erziehung aufbauen.",
        "In dieser Zeit wäre jeg­licher Anflug von Askese gleichbedeutend mit Ausrottung der natürlichen Gesundheit und Entwicklungsmöglichkeit."
      ],
      [
        "Wenn das Kind gegen sein siebentes Jahr hinlebt, bei dem allmählichen Zahnwechsel, lösen sich die äußeren Hüllen des Ätherleibes ab und dieser wird ebenso frei, wie vorher der physische Leib.",
        "Jetzt muß der Erzieher alles heran­bringen, was den Ätherleib ausbildet.",
        "Aber er muß sich hüten, zu großen Wert darauf zu legen, daß die Vernunft und der Verstand ausgebildet werden.",
        "In dieser Zeit, zwi­schen dem siebenten und zwölften Jahre des Kindes handelt es sich vorzugsweise um Autorität, Glauben, Vertrauen und Ehrfurcht.",
        "Gewohnheit und Charakter sind die speziellen Äußerungen des Ätherleibes, während auf die Urteilskraft in dieser Zeit nicht gewirkt werden soll, da dies vor der Geschlechtsreife ohne Schaden nicht geschehen kann."
      ],
      [
        "Die Ausbildung des Ätherleibes fällt in die Zeit vom siebenten bis zum sechzehnten Jahre, beim Mädchen bis zum vierzehnten Jahr.",
        "Fürs ganze spätere Leben bleibt von"
      ],
      [
        "Wichtigkeit, daß in dem Kinde das Gefühl von Ehrfurcht geweckt und genährt wird.",
        "Das kann etwa folgendermaßen geschehen: Es wird ihm von bedeutenden Menschen nicht nur der Geschichte, sondern auch aus den umgebenden Le­benskreisen ein Bild gegeben durch Mitteilungen und Er­zählungen, etwa von einem Verwandten, vor dem man Achtung und Ehrfurcht haben kann."
      ],
      [
        "Es wird dem Kinde Ehrfurcht und Scheu eingeflößt, die ihm verbietet, irgend­einen Gedanken von Kritik oder Opposition der verehrten Person gegenüber aufkommen zu lassen.",
        "Dann darf es die­sen Menschen einmal sehen; es lebt in heiliger Erwartung des Augenblicks, und eines Tages steht es vor der Türe dieser Person und empfindet eine heilige Scheu, auf die Klinke zu drücken und das Zimmer zu betreten, das ihm ein Heiligtum ist."
      ],
      [
        "Diese Momente der Ehrfurcht sind Kräfte für das spätere Leben.",
        "Von ungeheurer Bedeutung ist, daß der Erzieher, der Lehrer selbst, in dieser Zeit dem Kinde Autorität sei.",
        "Nicht an Grundsätze muß das Kind glauben, sondern an Menschen."
      ],
      [
        "Die Menschen, die das Kind um­geben, die es sieht und hört, die müssen seine Ideale sein, und aus der Geschichte oder Literatur muß es sie wählen.",
        "Hier gilt der Spruch: «Ein Jeder muß sich seinen Helden wählen, dem er die Wege zum Olymp hinauf sich nach­arbeitet.» Ganz falsch ist es, wenn die materialistischeWelt­anschauung gegen die Autorität sich ausspricht, das Kind schon zur Selbständigkeit anhält und das Gefühl der Hin­gebung und Verehrung mißachtet."
      ],
      [
        "Die gesunde Entwicklung leidet Schaden, wenn es schon vor der Geburt des Astral­leibes auf sein eigenes Urteil gestellt wird.",
        "Wichtig ist, daß in dieser Zeit das Gedächtnis herausgebildet wird, und zwar geschieht das am besten auf ganz mechanische Weise."
      ],
      [
        "Nicht die Rechenmaschine sollte benützt werden, sondern ganz mechanisch gedächtnismäßig sollte das Einmaleins, sollten"
      ],
      [
        "Gedichte und so weiter eingeprägt werden.",
        "Nur ein mate­rialistisches Vorurteil kann für diese Zeit behaupten, daß man sich diese Dinge erst merken soll, wenn man sie ver­steht.",
        "In alten Zeiten hat man in dieser Hinsicht richtiger erzogen."
      ],
      [
        "Vom ersten bis siebenten Jahre sang man vor, allerlei Verse, die guten alten Ammen- und Kinderlieder.",
        "Es kommt dabei nicht auf den Sinn an, und so finden wir in alten Liedern zwischen bedeutungsvollen Zeilen etwas, was nur wegen des Klanges da ist."
      ],
      [
        "Es kam beim Vorsingen nur auf den Zusammenklang und die Harmonie für das kindliche Ohr an, daher die oft sinnlosen Reime.",
        "Zum Bei­spiel: «Flieg, Käfer flieg, dein Vater ist im Krieg, deine Mutter ist im Pommerland, Pommerland ist abgebrannt; flieg, Käfer, flieg.» Pommerland bedeutet, nebenbei gesagt, in der Mundart des Kindes Mutterland."
      ],
      [
        "Der Ausdruck stammt noch aus jener Zeit, in der man an den geistigen Menschen geglaubt hat, der aus der geistigen in die physi­sche Welt kommt.",
        "Pommerland war das Land der geistigen Herkunft.",
        "Nicht auf den Sinn aber kommt es hier an, son­dern auf den Klang."
      ],
      [
        "Daher haben wir soviele, viele Kinder­lieder, die eigentlichen Sinn nicht aufweisen. - Gedächtnis, Gewohnheit und Charakter müssen in ihren Grundfesten in dieser Periode angelegt werden.",
        "Der Weg dazu ist die Autorität."
      ],
      [
        "Ein Mensch, bei dem dies nicht geschieht, weist eine mangelhafte Erziehung auf.",
        "Wo richtig erzogen wird, muß das Hinaufschauen zur Autorität in dieser Zeit zur Geltung kommen, während Grundsätze erst nach der astra­lischen Geburt am Platze sind."
      ],
      [
        "Dasjenige, was vom Kind als innerste Natur eines Menschen geahnt wird, was in der Autorität verehrt wird, was überhaupt zu ihm strömt vom Erzieher, das bildet des Kindes Gewissen, den Charakter und sogar sein Temperament aus und wird zur dauernden Anlage bei ihm.",
        "Dann müssen wir uns klar sein, daß in"
      ],
      [
        "diesen Jahren bildend auf den Ätherleib wirkt, was durch Gleichnisse und Sinnbilder den Geist der Welt kennen­lernen läßt.",
        "Daher der Segen der Märchenbilder in dieser Zeit und das Vorführen großer Persönlichkeiten und Hel­den in Sage und Geschichte."
      ],
      [
        "Man muß in dieser Zeit auf die Pflege des Ätherleibes ebenso bedacht sein wie vorher auf diejenige des physischen Leibes.",
        "Wie in den ersten Jahren durch Lust und Freude organbildend gewirkt wurde, so muß vom siebenten bis zum vierzehnten - für die Jungen bis zum sechzehnten - Lebens­jahre alles ausgebildet werden, was das Gefühl erhöhter Gesundheit und Lebensfreudigkeit hervorruft; daher der Wert des Turnunterrichtes.",
        "Mangelhaft ist derselbe aber, wenn der Turnlehrer mit dem Blick des Anatomen die Tur­ner betrachtet, wenn er nur nach dem äußeren Zweck einer Gliedbewegung zielt.",
        "Es kommt vielmehr darauf an, daß der Lehrer sich intuitiv so hineindenkt in die fühlende Seele des Kindes, daß er weiß, durch welche Bewegung des Leibes die Seele den Eindruck von Kraftgefühl, von Gesundheits­gefühl bekommt, was dem Menschen Wohlgefühl, Lust sei­ner eigenen Leiblichkeit bereitet.",
        "So erst bekommt die Turn­übung einen innerlichen Wert und Einfluß auf das Gefühl der wachsenden Kraft.",
        "Eine rechte Turnübung ist nicht nur für das äußerlich anschauende Auge, sondern auch für den fühlenden Menschen."
      ],
      [
        "Einen großen Einfluß bis in den Äther- und Astralleib hinein übt jedes Künstlerische.",
        "Daher muß echtes, wahres Künstlerisches den Ätherleib durchdringen.",
        "Gute Vokal-und Instrumentalmusik zum Beispiel ist von hoher Be­deutung, und das Kinderauge sollte viel Schönes um sich her erblicken."
      ],
      [
        "Aber durch nichts ist der Religionsunterricht zu ersetzen.",
        "Die Bilder des Übersinnlichen prägen sich tief in den Ätherleib"
      ],
      [
        "ein.",
        "Es kommt hier nicht darauf an, daß der Schüler kritisieren kann, daß er sein Urteil fällt über irgendein Glaubensbekenntnis, sondern darauf, daß er eine Anschau­ung empfängt von dem, was übersinnlich ist, was über das Vergängliche hinausgeht.",
        "Daher sind alle religiösen Vor­stellungen in bildliche Darstellungen zu bringen."
      ],
      [
        "Die größte Sorgfalt muß gelegt werden auf die Erzie­hung aus dem Lebendigen heraus.",
        "Dadurch, daß das Kind zu viel mit totem Stoff zu tun bekommt, wird viel an ihm verdorben, während alles, woran es das Lebendige ahnen kann, wichtig ist für den Ätherleib.",
        "Alles sollte Handlung, Tat, Leben sein; das belebt den Geist.",
        "Selbst im Spielzeug ist dies Moment von Bedeutung.",
        "So sind die alten Bilder­bücher zum Ziehen, zwei Klötze, die es hämmernd ver­binden kann, anregend, indem sie die Ahnung von innerer Bewegung des Lebens geben.",
        "Nichts Schlimmeres für den Geist, als aus fertigen geometrischen Gegenständen Formen zusammenstellen und -setzen zu lassen.",
        "Darum soll das Kind nicht mit dem Baukasten bauen, sondern von Grund auf alles selbst aufbauen.",
        "Das Kind muß lernen, das Lebendige aus dem Unlebendigen zu machen.",
        "Durch das Fertige, Un­lebendige wird die materielle Zeit das Lebendige auslöschen.",
        "Vieles erstirbt an dem sich entwickelnden Gehirn, wenn das Kind Dinge machen soll, die keinen Sinn haben, wie Flecht­arbeiten und so weiter.",
        "Ganze Anlagen bleiben dadurch unentwickelt.",
        "Vieles, was Unheil in unserem sozialen Zu­sammenleben bedeutet, ist auf die Kinderstube zurückzu­führen.",
        "Das Spielzeug des Unlebendigen bildet auch nicht den Glauben an das Lebendige heran, und daher besteht der tiefere Zusammenhang zwischen der Kindererziehung und der Glaubenslosigkeit unseres Zeitalters.",
        "So haben die Dinge einen tiefen Zusammenhang"
      ],
      [
        "Wenn die Geschlechtsreife erlangt wird, fallen die astralen"
      ],
      [
        "Hüllen, von denen der Leib umgeben ist, ebenfalls ab.",
        "Mit dem Gefühl für das andere Geschlecht tritt die persön­liche Urteilskraft hervor.",
        "Jetzt erst kommt die Zeit, in der man an die Urteilskraft appellieren kann, an das Ja und Nein, an den kritischen Verstand.",
        "Kaum dann, wenn der Mensch diesen Jahren entwachsen ist, vermag er ein eigenes Urteil abzugeben, geschweige denn früher.",
        "Es ist ein Un­ding, wenn solche jungen Menschen schon urteilen und auf die Kultur, auch nur im kleinsten Umfang, Einfluß ausüben wollen.",
        "So wenig ein Kind im Mutterleibe hören und sehen kann, vermag der noch nicht astral entwickelte Mensch vor dem zwanzigsten Jahr ein gesundes Urteil zu bilden.",
        "Für jedes Lebensalter ist der entsprechende Einfluß nötig, für das erste Vorbild, Nachahmung, für das zweite Autorität und Nacheiferung, für das dritte Grundsätze. - Äußerst wichtig ist, wer den jungen Menschen in diesem Lebensalter als Lehrer entgegentritt, um ihnen ihre Lernbegierde und ihren Freiheitsdrang in die rechten Bahnen zu lenken."
      ],
      [
        "Die geistige Weltanschauung erfüllt den Erzieher mit einer Fülle von Grundsätzen.",
        "Diese Grundsätze helfen dem Lehrer bei der Entwicklung des Menschengeschlechtes.",
        "Gei­steswissenschaft kann dadurch praktisch eingreifen in die wichtigsten Vorgänge des Menschenlebens und wir sehen sie im richtigen Verhältnis zum täglichen Leben.",
        "Dadurch, daß wir den Menschen in allen seinen Gliedern kennen, wissen wir, auf welche Glieder wir zu wirken haben und was wir tun müssen, damit unter solchen Verhältnissen, wie sie wirklich sind, der Mensch gedeiht.",
        "Wenn eine Mutter sich selbst nicht ordentlich ernähren kann, so wirkt das durch den Mutterleib auf den Embryo; wie dessen Mutter gepflegt werden muß, so auch die spätere Umgebung des Kindes; dadurch wird das Kind mitgepflegt.",
        "Das ist etwas, was auch ins Geistige zu übertragen ist.",
        "Weil nun das Kind"
      ],
      [
        "in der Äther-Mutterhülle schlummert, in der Astral-Um­gebung wurzelt, so kommt es darauf an, wie in seiner Um­gebung die Dinge sich vollziehen.",
        "Jeder.",
        "Gedanke, jedes Gefühl, alles Unausgesprochene, was diejenigen bewegt, die in seiner Umgebung sind, wirkt mit; da gilt nicht: Fühlen und denken darfst du dies und jenes wohl, wenn du es nur nicht sagst. - Mit reinen Gedanken und Gefühlen muß man das Kind umgeben und darum bis ins innerste Herz Rein­heit bewahren, keine unlauteren Gedanken sich gestatten.",
        "Durch Worte wirken wir nur auf das Sinnesvermögen, Ge­fühle und Gedanken impfen wir der schützenden Mutter-hülle des Äther- und Astralleibes ein und sie gehen auf das Kind über.",
        "Solange es von Hüllen umgeben ist, müssen wir diese pflegen.",
        "Pfropft man unreine Gedanken und Leiden­schaften in diese hinein, so verdirbt man ebensoviel, als wenn man in die physische Hülle des Mutterleibes Schäd­liches bringt.",
        "Bis in diese Feinheiten hinein vermag somit die geistige Weltanschauung zu leuchten.",
        "Aus der Erkennt­nis der Menschennatur heraus erfüllt sie den Erzieher mit der nötigen Einsicht."
      ],
      [
        "Geisteswissenschaft soll nicht eine Theorie sein und Über­zeugungen lehren; sie soll handeln, eingreifen ins praktische Leben.",
        "Indem sie gesundes Leben bewirkt, indem sie ge­sunde Menschen in leiblicher und geistiger Beziehung macht, erweist sie sich nicht nur als richtige, sondern als gesunde Wahrheit, die ausfließen muß in das ganze Leben des Men­schen.",
        "Am besten können wir durch Geisteswissenschaft der Menschheit dienen und ihr soziale und andere Kräfte zu­führen, wenn wir diese herausholen aus dem werdenden Menschen.",
        "Der werdende, der sich entwickelnde Mensch ist eines der größten Rätsel des Lebens.",
        "Derjenige, der es prak­tisch löst, erweist sich als der rechte Erzieher, als der wahre Rätsellöser in der Bildung des Menschen."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "SCHULFRAGEN VOM STANDPUNKT DER GEISTESWISSENSCHAFT Berlin, 24. Januar 1907",
    "paragraphs": [
      "Es handelt sich im heutigen Vortrag um Dinge, die un­mittelbar verwirklicht werden können. Aber wir wollen bei dieser Betrachtung stets die ganze Menschheitsentwick­lung vor Augen haben, dann werden wir auch die Einzel-entwicklung des jungen Menschen verstehen und sie leiten können. Mitten hinein in die Erziehung stellt sich die Schule mit ihren Anforderungen. Aus dem Wesen des Menschen und aus der Menschheitsentwicklung heraus wollen wir sie zu fassen suchen. Vier Leibesglieder unterscheiden wir zu­nächst am Menschen: physischer Leib, Äther- oder Lebens-leib, astralischer Leib und das Ich, der Mittelpunkt des Men­schen. Aber mit der physischen Geburt werden noch nicht alle vier Glieder für äußere Einwirkungen frei. Mit der physischen Geburt wird nur der physische Leib frei; zur Zeit des Zahnwechsels wird der Ätherleib geboren, zur Zeit der Geschlechtsreife der Astralleib. Wie Augen und Ohren vor der physischen Geburt unter der schützenden Mutter-hülle, so werden Gedächtnis, Temperament und so weiter, die am Ätherleib haften, vor dem Zahnwechsel unter der schützenden Hülle des Äthers entwickelt. Jean Paul sagt:",
      "Ein Weltreisender, der alle Länder durchquert, lernt auf allen seinen Reisen nicht soviel, wie das Kind bis zum sie­benten Jahre von seiner Amme. - Der Erzieher muß Frei­heit geben dem, was sich durch die Naturkräfte selbst ent­wickelt.",
      "Wozu brauchen wir denn überhaupt bei der Erziehung des Kindes eine Schule? Was nach der physischen Geburt heranwächst, bedarf einer schützenden Hülle, ähnlich wie der Keim im Mutterleibe. Denn erst an einem bestimmten Punkte tritt der Mensch in ein neues Leben. Bevor er an diesen Punkt kommt, ist sein Leben eine Wiederholung frü­herer Lebensepochen. Auch der Keim macht ja eine Wieder­holung aller Stadien der Entwicklung von Urzeiten her durch. So wiederholt das Kind nach der Geburt frühere Menschheitsepochen. Friedrich August Wolf charakterisierte die Stufen des Menschen von der Kindheit an folgender­maßen. Erste Epoche: das goldene mildharmonische Alter vom ersten bis zum dritten Jahre. Es entspricht dem Leben der heutigen Indianer und Südseeinsulaner. Zweite Epoche:",
      "sie spiegelt wider die Kämpfe in Asien, deren Widerschläge und Wirkungen in Europa, die Heroenzeit der Griechen; weiter hinaus die Zeit der nordamerikanischen Wilden, und im einzelnen Kinde die Lebensepoche bis zum sechsten Jahre. Dritte Epoche: sie entspricht der Griechenzeit von Homer an bis zu Alexander dem Großen, reicht im einzelnen Kinde bis zum neunten Jahre. Vierte Epoche: Römerzeit, reicht bis zum zwölften Jahre. Fünfte Epoche: Mittelalter, reicht bis zum fünfzehnten Jahre; die Religion soll hier die Kraft-natur adeln. Sechste Epoche: Renaissance, bis zum acht­zehnten Jahre. Siebente Epoche: Reformationszeit, bis zum einundzwanzigsten Jahre. Achte Epoche: reicht bis zum vierundzwanzigsten Jahre, in ihr erhebt sich der Mensch zur Gegenwart. Dieses Schema entspricht einer guten, gei­stig wertvollen Grundlage, nur dürfen wir es nicht so eng auffassen. Wir müssen die ganze Abstammung des Men­schen mit in Betracht ziehen. Der Mensch stammt nicht vom niederen Tiere. Zwar stammt er von Wesen, die physisch weit hinter den heute lebenden Menschen zurückstanden,",
      "aber doch dem Affen ganz und gar nicht ähnlich waren. Die Geisteswissenschaft weist hin auf die Zeiten, wo der Mensch die Atlantis bewohnte.",
      "Der Geist und die Seele der Atlantier waren anders ge­artet als bei den heutigen Menschen. Sie hatten nicht ein sogenanntes Verstandesbewußtsein. Sie konnten nicht schrei­ben und rechnen. Ihr Bewußtsein war gewissermaßen som­nambul. Viele Dinge der geistigen Welten konnten sie durch­schauen. Ihr Bewußtsein war ähnlich dem eines schlafenden Menschen mit lebhaften Träumen. Aber die Bilder, die in ihrem Bewußtsein aufstiegen, waren nicht chaotisch, son­dern geregelt und lebendig. Damals war auch der Wille noch mächtig, auf die Glieder einzuwirken. Degenerierte Nach­kommen von ihnen sind die heutigen höheren Säugetiere, namentlich die Affen. Das gewöhnliche atlantische Bewußt­sein war ein Bilderbewußtsein. Unser Traumbewußtsein ist ein Rest davon. Die kühnste Phantasie von heute ist in ihren Bildern nur ein schwacher Abglanz dieser Bilderwelt der Atlantier. Und der Atlantier beherrschte die Bilder. Logik, Vernunftgesetze gab es damals nicht. Im willkürlichen Spiel der Kinder haben wir einen Abglanz davon, im kindlichen Spiel klingt die bildliche Anschauung weiter. Leben quQll dem Atlantier aus allen Dingen wie heute dem Kind aus dem Spielzeug.",
      "In der lemurischen Zeit stieg der Mensch zum ersten Mal in den physischen Leib hinab. Das wird heute bei der phy­sischen Geburt wiederholt. Damals stieg der Mensch in den Leib hinab und entwickelte ihn seelisch-geistig immer hö­her. Die lemurische und atlantische Epoche wiederholt der Mensch bis zum siebenten Jahre.",
      "Vom Zahnwechsel bis zur Geschlechtsreife wird die Ent­wicklungsepoche wiederholt, in der große geistige Lehrer in der Menschheit auftraten. Die letzten von diesen waren",
      "Buddha, Plato, Pythagoras, Hermes, Moses, Zarathustr und so weiter. Damals wirkte die geistige Welt noch meh in die Menschheit hinein. In den Heroensagen wird uns die bewahrt. Jener Geist der alten Kulturepochen muß dahe dem Schulunterricht in diesen Jahren zugrunde liegen.",
      "Bis zum zwölften Jahrhundert, dem Zeitalter der Städte gründung, haben wir die Epoche, die dem siebenten bi vierzehnten Jahre des Kindes entspricht. Da konnte nu vom Prinzip der Gemeinsamkeit und Autorität die Red sein. Etwas von der Macht und dem Glanz der großen Füh rer muß vorhanden sein in diesen Jahren für die Kinde Die Lehrerfrage ist deshalb in der ganzen Schulangelege heit die wichtigste. Eine selbstverständliche Autorität mu der Lehrer den Kindern sein; so wie die Gewalt dessen, w die großen Lehrer zu sagen hatten, von selbst einfloß in d Menschenseelen. Schlimm ist es, wenn das Kind zweifelt seinem Lehrer. Das schadet sehr. Die Verehrung, die d Kind dem Lehrer zollt, muß die denkbar größte sein. Di muß so weit gehen, daß das Wohlwollen, das der Lehr gibt - und es ist selbstverständlich, daß er es gibt -, de Kinde wie ein Geschenk erscheint. Auf die methodisch-pä agogischen Grundsätze kommt es nicht an, sondern dara daß der Lehrer Psychologie im höchsten Sinne kennt. Seelen stud ium ist das wichtigste Element der Lehrerbildung. Ni wie die Seele entwickelt werden soll, soll man wissen, so dem man muß sehen, wie der Mensch sich wirklich entwi kelt.",
      "Und jedes Zeitalter stellt andere Forderungen an den Menschen, so daß allgemein gültige Schemen wertlos sind. Zum Lehrer gehört nicht Wissen und Beherrschen der   -thoden der Pädagogik, sondern ein bestimmter Charakter, eine Gesinnung, die schon wirkt, ehe der Lehrer gespro en hat. Er muß, bis zu einem gewissen Grade, eine innere Entwicklung",
      "durchgemacht haben, er muß nicht nur gelernt, er muß sich innerlich verwandelt haben. Man wird einst beim Examen nicht das Wissen, ja nicht einmal die pädagogischen Grundsätze, sondern das Sein prüfen. Leben muß die Schule für das Kind sein. Sie soll nicht nur das Leben abbilden, sie soll das Leben sein, denn sie soll eine frühere Lebens-epoche lebendig machen. Die Schule soll ein eigenes Leben erzeugen; nicht soll das äußere Leben hineinfließen. Was der Mensch später nicht mehr hat, soll er hier in der Schule haben. Bildliche, gleichnisartige Vorstellungen sollen in rei­cher Weise erweckt werden. «Alles Vergängliche ist nur ein Gleichnis»: von diesem Satz muß der Lehrer voll über­zeugt sein. Er darf nicht denken, wenn er bildlich redet:",
      "das ist nur ein Gleichnis. Wenn er voll mitlebt mit dem Kinde, dann geht aus seiner Seele Kraft in die des Kindes über. Ins Bild, in den Reichtum der Imagination, muß man die Naturvorgänge kleiden. Erschaffen muß man, was hin­ter dem Sinnlichen ist. Unser heutiger Anschauungsunter­richt ist darum ganz verfehlt, da er nur aufs Äußere hin­weist. Das Samenkorn hat nicht nur die Pflanze in sich, sondern auch die Sonnenkraft, ja den ganzen Kosmos. Auf-erwecken muß man die gleichnisartigen Kräfte, damit das Kind sich in die Natur einlebt. Nicht an der Rechenmaschine, sondern an den lebendigen Fingern muß man mit dem Kinde rechnen. Die lebendige Geisteskraft muß angeregt werden. Man muß dem Kinde nicht nur die Pflanze zeigen und beschreiben, sondern sie vom Kinde malen lassen. Dann werden frohe Menschen aus der Schule hervorgehen, die dem Leben einen Sinn abgewinnen. Rechnen und Natur­kunde schult die Denkkraft, das Gedächtnis und die Erinne­rung. Geschichte schult die Gefühlskräfte. Fühlen mit allem Großen und Schönen entwickelt Liebe zu dem, was geliebt sein muß. Der Wille aber wird nur ausgebildet durch die",
      "religiöse Anschauung. Die muß alles durchdringen. Jean Paul sagt: Horchet wie richtig ein Kind spricht und fraget dann seinen Vater, er soll es erklären. - Das Kind kann nicht alles verstehen, was es tatsächlich kann. Und so ist es auch bei allen Menschen. Nur unsere materielle Zeit will dem Gedächtnis so wenig zumuten. Zuerst lernt das Kind, später versteht es das Gelernte, und noch später lernt es die Gesetze kennen.",
      "Zwischen dem siebenten und vierzehnten Jahre muß auch der Schönheitssinn entwickelt werden. Er ist es, der uns auch die symbolische Auffassung der Dinge vermittelt. Vor allem soll aber Leben dem Kinde werden und möglichst wenig abstrakte Ideen. Die sollen erst nach der Geschlechtsreife kommen. Dann soll es erst die Theorien lernen, wenn es schon sinnvoll in die Dinge eingedrungen ist. Der Geist der Natur soll zuvor gesprochen haben, die Tatsachen selbst, die ja hinter dem Sinnlichen liegen. Man muß nicht fürch­ten, daß nach der Schulzeit alles vergessen werde. Es kommt nur darauf an, daß es Früchte trägt, daß der Geist geformt wird. Nur das bleibt, was der Mensch gefühlt und empfun­den hat. Das Einzelne geht, das Allgemeine bleibt und wächst. Nie aber kann ein Unterricht ohne religiöse Grund­lage geführt werden. Eine religionslose Schule ist einfach eine Illusion. Auch in Haeckels Welträtsel steht ja eine Religion. Wer Religion bekämpft, tut es entweder von einem hohen Standpunkt aus, wie Schiller sagt «aus Religion», oder von einem sehr tiefen Standpunkt aus. Aber nie kann eine Theorie eine Religion ersetzen.Religionsgeschichte kann das nie ersetzen. Wer in einer tief religiösen Grundstimmung ist, der kann auch Religion geben. Der Geist, der in der Welt lebt, lebt auch im Menschen. Man muß fühlen, daß man in einer geistigen Weltordnung steht, von der man seine Mission empfängt. Es gibt ein Wort: «Ein Blick ins Buch,",
      "und zwei ins Leben, das muß die Form dem Geiste geben.» Aber die Schule muß unmittelbares Leben sein; das Buch selbst muß Leben sein, muß erfreuen wie das Leben selbst. So können wir den Spruch so formen:",
      "Ein Blick ins Buch, der wie ein Blick ins Leben,",
      "Der kann die rechte Form dem Geiste geben."
    ],
    "sentences": [
      [
        "Es handelt sich im heutigen Vortrag um Dinge, die un­mittelbar verwirklicht werden können.",
        "Aber wir wollen bei dieser Betrachtung stets die ganze Menschheitsentwick­lung vor Augen haben, dann werden wir auch die Einzel-entwicklung des jungen Menschen verstehen und sie leiten können.",
        "Mitten hinein in die Erziehung stellt sich die Schule mit ihren Anforderungen.",
        "Aus dem Wesen des Menschen und aus der Menschheitsentwicklung heraus wollen wir sie zu fassen suchen.",
        "Vier Leibesglieder unterscheiden wir zu­nächst am Menschen: physischer Leib, Äther- oder Lebens-leib, astralischer Leib und das Ich, der Mittelpunkt des Men­schen.",
        "Aber mit der physischen Geburt werden noch nicht alle vier Glieder für äußere Einwirkungen frei.",
        "Mit der physischen Geburt wird nur der physische Leib frei; zur Zeit des Zahnwechsels wird der Ätherleib geboren, zur Zeit der Geschlechtsreife der Astralleib.",
        "Wie Augen und Ohren vor der physischen Geburt unter der schützenden Mutter-hülle, so werden Gedächtnis, Temperament und so weiter, die am Ätherleib haften, vor dem Zahnwechsel unter der schützenden Hülle des Äthers entwickelt.",
        "Jean Paul sagt:"
      ],
      [
        "Ein Weltreisender, der alle Länder durchquert, lernt auf allen seinen Reisen nicht soviel, wie das Kind bis zum sie­benten Jahre von seiner Amme. - Der Erzieher muß Frei­heit geben dem, was sich durch die Naturkräfte selbst ent­wickelt."
      ],
      [
        "Wozu brauchen wir denn überhaupt bei der Erziehung des Kindes eine Schule?",
        "Was nach der physischen Geburt heranwächst, bedarf einer schützenden Hülle, ähnlich wie der Keim im Mutterleibe.",
        "Denn erst an einem bestimmten Punkte tritt der Mensch in ein neues Leben.",
        "Bevor er an diesen Punkt kommt, ist sein Leben eine Wiederholung frü­herer Lebensepochen.",
        "Auch der Keim macht ja eine Wieder­holung aller Stadien der Entwicklung von Urzeiten her durch.",
        "So wiederholt das Kind nach der Geburt frühere Menschheitsepochen.",
        "Friedrich August Wolf charakterisierte die Stufen des Menschen von der Kindheit an folgender­maßen.",
        "Erste Epoche: das goldene mildharmonische Alter vom ersten bis zum dritten Jahre.",
        "Es entspricht dem Leben der heutigen Indianer und Südseeinsulaner.",
        "Zweite Epoche:"
      ],
      [
        "sie spiegelt wider die Kämpfe in Asien, deren Widerschläge und Wirkungen in Europa, die Heroenzeit der Griechen; weiter hinaus die Zeit der nordamerikanischen Wilden, und im einzelnen Kinde die Lebensepoche bis zum sechsten Jahre.",
        "Dritte Epoche: sie entspricht der Griechenzeit von Homer an bis zu Alexander dem Großen, reicht im einzelnen Kinde bis zum neunten Jahre.",
        "Vierte Epoche: Römerzeit, reicht bis zum zwölften Jahre.",
        "Fünfte Epoche: Mittelalter, reicht bis zum fünfzehnten Jahre; die Religion soll hier die Kraft-natur adeln.",
        "Sechste Epoche: Renaissance, bis zum acht­zehnten Jahre.",
        "Siebente Epoche: Reformationszeit, bis zum einundzwanzigsten Jahre.",
        "Achte Epoche: reicht bis zum vierundzwanzigsten Jahre, in ihr erhebt sich der Mensch zur Gegenwart.",
        "Dieses Schema entspricht einer guten, gei­stig wertvollen Grundlage, nur dürfen wir es nicht so eng auffassen.",
        "Wir müssen die ganze Abstammung des Men­schen mit in Betracht ziehen.",
        "Der Mensch stammt nicht vom niederen Tiere.",
        "Zwar stammt er von Wesen, die physisch weit hinter den heute lebenden Menschen zurückstanden,"
      ],
      [
        "aber doch dem Affen ganz und gar nicht ähnlich waren.",
        "Die Geisteswissenschaft weist hin auf die Zeiten, wo der Mensch die Atlantis bewohnte."
      ],
      [
        "Der Geist und die Seele der Atlantier waren anders ge­artet als bei den heutigen Menschen.",
        "Sie hatten nicht ein sogenanntes Verstandesbewußtsein.",
        "Sie konnten nicht schrei­ben und rechnen.",
        "Ihr Bewußtsein war gewissermaßen som­nambul.",
        "Viele Dinge der geistigen Welten konnten sie durch­schauen.",
        "Ihr Bewußtsein war ähnlich dem eines schlafenden Menschen mit lebhaften Träumen.",
        "Aber die Bilder, die in ihrem Bewußtsein aufstiegen, waren nicht chaotisch, son­dern geregelt und lebendig.",
        "Damals war auch der Wille noch mächtig, auf die Glieder einzuwirken.",
        "Degenerierte Nach­kommen von ihnen sind die heutigen höheren Säugetiere, namentlich die Affen.",
        "Das gewöhnliche atlantische Bewußt­sein war ein Bilderbewußtsein.",
        "Unser Traumbewußtsein ist ein Rest davon.",
        "Die kühnste Phantasie von heute ist in ihren Bildern nur ein schwacher Abglanz dieser Bilderwelt der Atlantier.",
        "Und der Atlantier beherrschte die Bilder.",
        "Logik, Vernunftgesetze gab es damals nicht.",
        "Im willkürlichen Spiel der Kinder haben wir einen Abglanz davon, im kindlichen Spiel klingt die bildliche Anschauung weiter.",
        "Leben quQll dem Atlantier aus allen Dingen wie heute dem Kind aus dem Spielzeug."
      ],
      [
        "In der lemurischen Zeit stieg der Mensch zum ersten Mal in den physischen Leib hinab.",
        "Das wird heute bei der phy­sischen Geburt wiederholt.",
        "Damals stieg der Mensch in den Leib hinab und entwickelte ihn seelisch-geistig immer hö­her.",
        "Die lemurische und atlantische Epoche wiederholt der Mensch bis zum siebenten Jahre."
      ],
      [
        "Vom Zahnwechsel bis zur Geschlechtsreife wird die Ent­wicklungsepoche wiederholt, in der große geistige Lehrer in der Menschheit auftraten.",
        "Die letzten von diesen waren"
      ],
      [
        "Buddha, Plato, Pythagoras, Hermes, Moses, Zarathustr und so weiter.",
        "Damals wirkte die geistige Welt noch meh in die Menschheit hinein.",
        "In den Heroensagen wird uns die bewahrt.",
        "Jener Geist der alten Kulturepochen muß dahe dem Schulunterricht in diesen Jahren zugrunde liegen."
      ],
      [
        "Bis zum zwölften Jahrhundert, dem Zeitalter der Städte gründung, haben wir die Epoche, die dem siebenten bi vierzehnten Jahre des Kindes entspricht.",
        "Da konnte nu vom Prinzip der Gemeinsamkeit und Autorität die Red sein.",
        "Etwas von der Macht und dem Glanz der großen Füh rer muß vorhanden sein in diesen Jahren für die Kinde Die Lehrerfrage ist deshalb in der ganzen Schulangelege heit die wichtigste.",
        "Eine selbstverständliche Autorität mu der Lehrer den Kindern sein; so wie die Gewalt dessen, w die großen Lehrer zu sagen hatten, von selbst einfloß in d Menschenseelen.",
        "Schlimm ist es, wenn das Kind zweifelt seinem Lehrer.",
        "Das schadet sehr.",
        "Die Verehrung, die d Kind dem Lehrer zollt, muß die denkbar größte sein.",
        "Di muß so weit gehen, daß das Wohlwollen, das der Lehr gibt - und es ist selbstverständlich, daß er es gibt -, de Kinde wie ein Geschenk erscheint.",
        "Auf die methodisch-pä agogischen Grundsätze kommt es nicht an, sondern dara daß der Lehrer Psychologie im höchsten Sinne kennt.",
        "Seelen stud ium ist das wichtigste Element der Lehrerbildung.",
        "Ni wie die Seele entwickelt werden soll, soll man wissen, so dem man muß sehen, wie der Mensch sich wirklich entwi kelt."
      ],
      [
        "Und jedes Zeitalter stellt andere Forderungen an den Menschen, so daß allgemein gültige Schemen wertlos sind.",
        "Zum Lehrer gehört nicht Wissen und Beherrschen der -thoden der Pädagogik, sondern ein bestimmter Charakter, eine Gesinnung, die schon wirkt, ehe der Lehrer gespro en hat.",
        "Er muß, bis zu einem gewissen Grade, eine innere Entwicklung"
      ],
      [
        "durchgemacht haben, er muß nicht nur gelernt, er muß sich innerlich verwandelt haben.",
        "Man wird einst beim Examen nicht das Wissen, ja nicht einmal die pädagogischen Grundsätze, sondern das Sein prüfen.",
        "Leben muß die Schule für das Kind sein.",
        "Sie soll nicht nur das Leben abbilden, sie soll das Leben sein, denn sie soll eine frühere Lebens-epoche lebendig machen.",
        "Die Schule soll ein eigenes Leben erzeugen; nicht soll das äußere Leben hineinfließen.",
        "Was der Mensch später nicht mehr hat, soll er hier in der Schule haben.",
        "Bildliche, gleichnisartige Vorstellungen sollen in rei­cher Weise erweckt werden.",
        "«Alles Vergängliche ist nur ein Gleichnis»: von diesem Satz muß der Lehrer voll über­zeugt sein.",
        "Er darf nicht denken, wenn er bildlich redet:"
      ],
      [
        "das ist nur ein Gleichnis.",
        "Wenn er voll mitlebt mit dem Kinde, dann geht aus seiner Seele Kraft in die des Kindes über.",
        "Ins Bild, in den Reichtum der Imagination, muß man die Naturvorgänge kleiden.",
        "Erschaffen muß man, was hin­ter dem Sinnlichen ist.",
        "Unser heutiger Anschauungsunter­richt ist darum ganz verfehlt, da er nur aufs Äußere hin­weist.",
        "Das Samenkorn hat nicht nur die Pflanze in sich, sondern auch die Sonnenkraft, ja den ganzen Kosmos.",
        "Auf-erwecken muß man die gleichnisartigen Kräfte, damit das Kind sich in die Natur einlebt.",
        "Nicht an der Rechenmaschine, sondern an den lebendigen Fingern muß man mit dem Kinde rechnen.",
        "Die lebendige Geisteskraft muß angeregt werden.",
        "Man muß dem Kinde nicht nur die Pflanze zeigen und beschreiben, sondern sie vom Kinde malen lassen.",
        "Dann werden frohe Menschen aus der Schule hervorgehen, die dem Leben einen Sinn abgewinnen.",
        "Rechnen und Natur­kunde schult die Denkkraft, das Gedächtnis und die Erinne­rung.",
        "Geschichte schult die Gefühlskräfte.",
        "Fühlen mit allem Großen und Schönen entwickelt Liebe zu dem, was geliebt sein muß.",
        "Der Wille aber wird nur ausgebildet durch die"
      ],
      [
        "religiöse Anschauung.",
        "Die muß alles durchdringen.",
        "Jean Paul sagt: Horchet wie richtig ein Kind spricht und fraget dann seinen Vater, er soll es erklären. - Das Kind kann nicht alles verstehen, was es tatsächlich kann.",
        "Und so ist es auch bei allen Menschen.",
        "Nur unsere materielle Zeit will dem Gedächtnis so wenig zumuten.",
        "Zuerst lernt das Kind, später versteht es das Gelernte, und noch später lernt es die Gesetze kennen."
      ],
      [
        "Zwischen dem siebenten und vierzehnten Jahre muß auch der Schönheitssinn entwickelt werden.",
        "Er ist es, der uns auch die symbolische Auffassung der Dinge vermittelt.",
        "Vor allem soll aber Leben dem Kinde werden und möglichst wenig abstrakte Ideen.",
        "Die sollen erst nach der Geschlechtsreife kommen.",
        "Dann soll es erst die Theorien lernen, wenn es schon sinnvoll in die Dinge eingedrungen ist.",
        "Der Geist der Natur soll zuvor gesprochen haben, die Tatsachen selbst, die ja hinter dem Sinnlichen liegen.",
        "Man muß nicht fürch­ten, daß nach der Schulzeit alles vergessen werde.",
        "Es kommt nur darauf an, daß es Früchte trägt, daß der Geist geformt wird.",
        "Nur das bleibt, was der Mensch gefühlt und empfun­den hat.",
        "Das Einzelne geht, das Allgemeine bleibt und wächst.",
        "Nie aber kann ein Unterricht ohne religiöse Grund­lage geführt werden.",
        "Eine religionslose Schule ist einfach eine Illusion.",
        "Auch in Haeckels Welträtsel steht ja eine Religion.",
        "Wer Religion bekämpft, tut es entweder von einem hohen Standpunkt aus, wie Schiller sagt «aus Religion», oder von einem sehr tiefen Standpunkt aus.",
        "Aber nie kann eine Theorie eine Religion ersetzen.Religionsgeschichte kann das nie ersetzen.",
        "Wer in einer tief religiösen Grundstimmung ist, der kann auch Religion geben.",
        "Der Geist, der in der Welt lebt, lebt auch im Menschen.",
        "Man muß fühlen, daß man in einer geistigen Weltordnung steht, von der man seine Mission empfängt.",
        "Es gibt ein Wort: «Ein Blick ins Buch,"
      ],
      [
        "und zwei ins Leben, das muß die Form dem Geiste geben.» Aber die Schule muß unmittelbares Leben sein; das Buch selbst muß Leben sein, muß erfreuen wie das Leben selbst.",
        "So können wir den Spruch so formen:"
      ],
      [
        "Ein Blick ins Buch, der wie ein Blick ins Leben,"
      ],
      [
        "Der kann die rechte Form dem Geiste geben."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "DER IRRSINN VOM STANDPUNKTE DER GEISTESWISSENSCHAFT Berlin, 31. Januar 1907",
    "paragraphs": [
      "Gerade die Geisteswissenschaft muß über die sogenannten Geisteskrankheiten etwas zusagen haben. Zunächst ist schon der Name nicht richtig gewählt. Man sollte nicht von Geistes­krankheiten reden. Ferner sind gerade auf diesem Gebiete in der Laienwelt die größten Irrtümer verbreitet, sowohl in gelehrten wie in den ungelehrten Kreisen und ihrer Lite­ratur. Die Erscheinungsformen werden für die Sache selbst angesehen. Man spricht von Größenwahn, Verfolgungs­wahn, religiösem Wahn. Diese Ausdrücke bezeichnen alle nur Symptome. Niemand kann durch eine religiöse Idee wahnsinnig werden. So kann man zum Beispiel den merk­würdigen Satz lesen, Hölderlin sei an der Disharmonie zwischen moderner und antiker Weltanschauung erkrankt. Wäre Hölderlin kein Dichter gewesen, so wäre doch die­selbe Art Wahnsinn über ihn gekommen, nur hätte sie sich anders, in anderen Ideen zum Ausdruck gebracht. Wenn je­mand in religiösen Ideen lebt und erkrankt dann, so werden sich seine religiösen Ideen verzerren. Hat er in materiali­stischen Ideen gelebt, so verzerren sich diese. Die Gründe für die Geisteskrankheit liegen tief in der menschlichen Natur. Die heutige Medizin schafft auf diesem Gebiete nichts Positives zutage; sie hat nur Hypothesen, Zweifel, Mutmaßungen. Allerdings ist es schwer, ja unmöglich für den Materialisten, sich in diesen Fragen Klarheit zu schaffen. Gar vieles, was der Arzt nicht mehr zu den Geisteskrankheiten",
      "rechnet, gehört schon dazu: zum Beispiel Queru­lantenwahnsinn, ebenso religiöse Sektierer und Fanatiker. Letztere leben unter einer Idee wie unter einer Zwangsvor­stellung und üben auf Schwache eine große suggestive Kraft aus, so daß Zeitkrankheiten, Gedankenepidemien entstehen.",
      "Wie kann sich eigentlich so etwas wie Irrsinn im Wesen des Menschen festsetzen? Zur Beantwortung dieser Frage müssen wir die vier niederen Glieder des Menschen: physi­scher Leib, Lebensleib, Astralleib und das Ich vor Augen haben. Das Ich arbeitet an den drei übrigen Gliedern der menschlichen Wesenheit. Vor allem veredelt und läutert es den Astralleib, indem es ihn zwingt, nicht blind seinen Trie­ben zu folgen. Aber das Ich arbeitet auch in den Lebensleib hinein, und zwar durch die großen Impulse des Lebens, namentlich durch die künstlerischen Impulse. Wie im Astral­leib durch die Arbeit des Ich zwei Teile entstehen, ein ge­läuterterer und ungeläuterterer, so wird nun auch der Le­bensleib zweigeteilt. Und allmählich wird der Teil, der vom Ich bearbeitet wird, immer größer. Auch ins Physische wirkt das Ich, aber unbewußt. Bewußt vermag es das nur bei einem höheren Schüler der Eingeweihten.",
      "Nun müssen wir, um unsere Frage beantworten zu können, uns an die Wiederverkörperung erinnern. Beim Schlafen geht etwas ganz Ahnliches mit uns vor wie beim Tode. Im Schlafe trennen sich der Astralleib und das Ich vom physischen Körper. Alle Triebe und Empfindungen sinken damit hinab in ein unbewußtes Dunkel. Im Bette blei­ben nur der physische Leib und der Atherleib zurück. Beim Tode trennt sich auch der Ather- oder Lebensleib vom phy­sischen Körper los. In den nächsten Stunden, während des Menschen Wesenheit im Atherleibe ruht, zieht das ganze bisherige Leben in großen Bildern an seiner Seele vorüber, so lange, bis auch der Atherleib sich von ihm ablöst und im",
      "allgemeinen Weltenäther aufgeht. Aber nur das Stoffliche des Atherleibes löst sich auf. Das Erinnerungsbild bleibt, wie eine Essenz, durch alle folgenden Zeiten mit dem Astral­leibe und dem Ich verbunden.",
      "Zunächst geht es mit in den Kamaloka-Zustand über. Kamaloka, Ort der Begierden, nennen wir den Zustand, in dem alles das aus dem Astral­leib ausgeschieden wird, was noch am Erdenleben hängt. Alles, was noch nicht veredelt war, löst sich auf, das andere wird in alle Zukunft mitgenommen.",
      "In ganz geringem Maße gehen auch Teile des physischen Leibes mit, aber nur bei sehr veredelten Menschen. Bei der neuen Verkörperung nimmt der Mensch die unveredelten Teile wieder an sich, um weiter an ihrer Läuterung zu arbeiten.",
      "Je öfter der Mensch auf Erden erscheint, desto fester wird sein Charak­ter, ein desto feineres Gewissen bekommt er, desto größer und zahlreicher sind seine Talente und Kräfte. Den her­metischen Grundsatz brauchen wir vor allem bei der Erklä­rung der Geisteskrankheiten: Es ist oben alles wie unten und unten alles wie oben.",
      "Im lächelnden Antlitz drückt sich uns ohne weiteres die Heiterkeit des Menschen aus. Die Tränenperle kündet innere Trauer der Seele an. Heiterkeit und Trauer werden wir in diesem Falle das Obere nennen, Lächeln und Tränen, die das materielle Bild von Heiterkeit und Trauer darstellen, das Untere.",
      "Ein richtig geschulter Mensch sieht die ganze Welt anders an. Eine Blume ist ihm der Ausdruck der Trauer oder der Heiterkeit des Erd­geistes. Und das ist ihm so wenig ein bloß poetischer Ge­danke, wie die Seele nur ein poetischer Gedanke ist.",
      "Der Erde liegt der Erdengeist als Oberes zugrunde. Alles Mate­rielle ist verdichteter Geist, geradeso wie das Eis nur ver­dichtetes Wasser ist. Wie man das Eis schmelzen kann, so daß es Wasser wird, so kann man auch die Materie wandeln, so daß sie Geist wird.",
      "Wir unterscheiden folgende physische",
      "Teile am Menschen, die seinen oberen Gliedern entsprechen:",
      "erstens rein Physisches, was nach rein physischen Gesetzen gebaut ist, vor allem die Sinnesorgane, zweitens alles das, was mit Verdauung, Wachstum, Fortpflanzung zusammen­hängt. Das, was die Kristalle aufbaut, könnte auch den menschlichen Leib aufbauen, aber er wäre dann ein toter Organismus. Der Atherleib ist der Bildner, der die Ver­dauungsorgane und so weiter aufbaut. Drittens Nerven­system (Gehirn und Rückenmark): sein Bildner ist der Astralleib, viertens das Blut. In ihm wohnt das Ich, das zugleich der Architekt des Blutsystems ist.",
      "Blutzirkulation:    Ich",
      "Nervensystem:    Astralleib",
      "Fortpflanzung:    Ätherleib",
      "Physisches:    Physischer Leib",
      "Alles Physische ist den Gesetzen der physischen Ver­erbung unterworfen, aber ebenso die Fortpflanzungsorgane, Nervensystem und Blutzirkulation. Mit diesem physischen Leib muß sich die Individualität vereinigen. Das Ich mit seinem veredelten Astral- und Atherleib, ja sogar Teile des physischen Leibes, müssen mit dem Ererbten zusammen­stimmen, eine Harmonie muß das zusammen bilden. Fast immer findet auch wirklich ein Zusammenstimmen statt, denn dem Geistigen paßt sich das Physische an, es wandelt sich um. Wie, wenn aber eine solche Anpassung nicht mög­lich ist, wie, wenn der Astralleib ein Nervensystem be­kommt, das er nicht ohne weiteres benutzen kann?",
      "Sinnestäuschungen rechnen wir nicht zu den Geistes­krankheiten. Dazu kann uns ein Buch des Wiener Kriminal­anthropologen Moritz Benedikt viel Interessantes bieten, obwohl es nicht in geisteswissenschaftlichem Sinne geschrie­ben ist. Benedikt erzählt darin seine eigenen Erlebnisse und",
      "Erfahrungen. Er hat im linken Auge einen partiellen Star, so daß er etwas unregelmäßig sieht. Wenn er nun im Dun­kel in einer ganz bestimmten Richtung schaut, so sieht er Gespenster ganz besonderer Art. Einmal ward er davon so erschreckt, daß er zur Waffe griff. Das ist so zu erklären:",
      "Ein gesunder Mensch ist sich der inneren Bestandteile seines Auges nicht bewußt. Wer aber Unregelmäßigkeiten im Auge hat, der wird sich deren in der Weise bewußt, daß sie ihm außen im Spiegelbilde erst entgegentreten.",
      "Das wollen wir nun auf die ganze menschliche Wesenheit ausdehnen. Wir werden uns ja unseres Innern überhaupt nicht bewußt, son­dern nur dessen, was uns von außen übermittelt wird. Wenn Harmonie herrscht zwischen oben und unten, so ist man sich der innern Vorgänge überhaupt nicht bewußt.",
      "Hat einer zum Beispiel ein schwerfälliges Gehirn, das der Astral­leib nicht gebrauchen kann, so drückt sich diese Störung, die der Astralleib erleidet, ebenso nach außenhin aus, wie die Störung im Auge es tat. Da wird der Astralleib sich seiner selbst bewußt, weil er gestört ist; da sieht er sich nach außen projiziert, Hoffnungen, Wünsche, Begierden treten ihm in Gestalten von außen entgegen.",
      "Wahnsinn, Querulanten­wahnsinn, Hysterie gehören hierher, alles das, wo der Mensch seine Gefühle nicht in Einklang bringen kann mit der Außenwelt. Aber auch der Atherleib kann an inneren Abnormitäten leiden.",
      "Er ist der Träger der bildlichen Vor­stellungen. Wenn der Atherleib sich seiner selbst unbewußt Ist, so treten die Bilder der Außenwelt ihm wahr entgegen. Spiegeln sich aber bei Störungen des Atherleibes die Bilder nach außen, so werden es Wahnideen, Paranoia.",
      "Wenn der physische Leib, der den Einklang mit der physischen Um­gebung bringen soll, selbst erkrankt, wenn der physische Leib sich seiner selbst bewußt wird, so tritt Idiotie auf. Wenn der physische Leib zu schwer ist, so daß der Astralleib",
      "ihn nicht beherrschen kann, daß er nicht heraus kann, so tritt das ein, was man Dementia nennt. Wenn die phy­sischen Organe aber zu beweglich sind, so daß sie die seeli­sche Tätigkeit nicht deutlich ausdrücken, so entsteht Paralyse. Doch es gibt hier eine unendliche Fülle von solchen Fällen, die ganz verschiedenen Ursprung haben können, namentlich die Wahnvorstellungen. Sie können entspringen einmal aus der Projektion des Astralleibes oder aus der Erkrankung des Astralleibes. Dann werden die Affekte so stark, daß es zu Tobsuchtsanfällen kommt. Diese drücken sich im Äther-leib ab und daraus entstehen Wahnideen. Diese Wahnvor­stellungen sind wie die Narbe zu der Wunde im Astralleib. Sie sind viel schwerer heilbar als die Tobsucht. Pupillen-starre ist manchmal eine Vorbereitung zum Wahnsinn.",
      "Wir wollen uns nun daran erinnern, daß der Mensch mehr als einmal geboren wird. Zuerst physisch. Dann zur Zeit des Zahnwechsels wird der Ätherleib geboren und zur Zeit der Geschlechtsreife der Astralleib. Es kann nun vor­kommen, daß erst bei der Geburt des Astralleibes der Miß­klang zwischen oben und unten bemerkbar wird. Vorher bewahrte die umschließende Astralhülle den Einklang. Nach der astralen Geburt ist dann der Astralleib sich selbst über-lassen, und nun tritt der Mißklang zwischen ihm und dem physischen Leibe hervor. Diese Art von Irrsinn äußert sich in der Weise, daß das junge Wesen oft auf ganz verschiedene Fragen ein und dieselbe Antwort gibt; auch leidet es unter Zwangsvorstellungen. Man nennt diese Erkrankungen Ju­gendblödsinn. Doch tritt dies nicht plötzlich auf, sondern bereitet sich langsam vor, vom elften, zwölften Jahre an. De­pressionszustände, Ermüdbarkeit, Nicht-Auskommen mit der Umgebung, Kopfschmerzen, Verdauungs- und Schlaf­störungen sind Vorboten. Es ist traurig, wenn man bedenkt, daß die meisten Eltern ihre Kinder für solche Erkrankungen",
      "noch bestrafen, da sie diese Zustände für Unarten hal­ten. Gerade der Jugendblödsinn ist am schwersten zu heilen. Aber der Geist als solcher kann nicht krank sein; er ist immer gesund. Er wird nur gestört, wenn das Untere nicht dazu stimmt.",
      "Wenn man sich in einem Gartenkugelspiegel betrachtet, so sieht man ein Zerrbild seiner selbst. Niemand schließt aber aus dem Zerrbild, daß das wahre Gesicht auch verzerrt sein müsse. So ist es auch mit den Geisteskrank­heiten.",
      "Zerrbilder des Geistes im Physischen sind die Wahn­sinnsformen. Darum ist auf dem Wege der Logik, des ab­strakten Begriffes nie eine Heilung möglich. Solche Versuche sind völlig wertlos. Auch unsere körperlichen Organe sind verdichteter Geist, wenn auch nicht unser Geist.",
      "Und am fernsten stehen dem zum Physischen verdichteten Geiste schattenhafte, logische Gebilde; am nächsten aber bildliche, von Leidenschaften durchzogene, imaginative Vorstellun­gen. Diese können die krankmachende Kraft anderer Bilder aus dem Felde schlagen.",
      "Gegenvorstellungen muß man geben durch die Macht und Gewalt einer anderen Persönlichkeit. Das Unlogische kann man den Kranken nicht durch Klar­machen beweisen, aber durch lebendige Vorstellungen kann man wirken.",
      "Die Macht der Persönlichkeit muß dem Kran­ken beweisen, daß er zum Beispiel das, was er nicht zu können glaubt, doch kann. Das muß der Kranke sehen. Auf dem Gebiete der sogenannten Geisteskrankheiten wird sich die gewöhnliche Wissenschaft einst mit der Geisteswissen­schaft verbinden müssen.",
      "Ein ausführliches Studium ist nötig, um immer die richtigen Gegenvorstellungen bereit zu haben. Diese dürfen auch nicht «normal» sein, sondern müssen nach der anderen Seite ausschlagen.",
      "Die Geisteswissenschaft ist nichts Tatenloses, sie ver­kriecht sich nicht in Weltenfernheit; sie will praktisch mit­arbeiten. Weil geistige Kräfte der Welt zugrunde liegen,",
      "müssen wir sie kennenlernen, wenn wir in der Welt wirken wollen. Unsere materielle Welt ist ein Abdruck der geistigen Welt. Die müssen wir kennenlernen, um das Physische zu verstehen. Freilich sagt Hellenbach: Was geht uns all das Geistergesindel an. Wir aber wollen sagen: Doch, das Men­schengesindel geht uns an, und da die Menschen mit der geistigen Welt verbunden sind, so wollen wir die Brücke zwischen beiden finden."
    ],
    "sentences": [
      [
        "Gerade die Geisteswissenschaft muß über die sogenannten Geisteskrankheiten etwas zusagen haben.",
        "Zunächst ist schon der Name nicht richtig gewählt.",
        "Man sollte nicht von Geistes­krankheiten reden.",
        "Ferner sind gerade auf diesem Gebiete in der Laienwelt die größten Irrtümer verbreitet, sowohl in gelehrten wie in den ungelehrten Kreisen und ihrer Lite­ratur.",
        "Die Erscheinungsformen werden für die Sache selbst angesehen.",
        "Man spricht von Größenwahn, Verfolgungs­wahn, religiösem Wahn.",
        "Diese Ausdrücke bezeichnen alle nur Symptome.",
        "Niemand kann durch eine religiöse Idee wahnsinnig werden.",
        "So kann man zum Beispiel den merk­würdigen Satz lesen, Hölderlin sei an der Disharmonie zwischen moderner und antiker Weltanschauung erkrankt.",
        "Wäre Hölderlin kein Dichter gewesen, so wäre doch die­selbe Art Wahnsinn über ihn gekommen, nur hätte sie sich anders, in anderen Ideen zum Ausdruck gebracht.",
        "Wenn je­mand in religiösen Ideen lebt und erkrankt dann, so werden sich seine religiösen Ideen verzerren.",
        "Hat er in materiali­stischen Ideen gelebt, so verzerren sich diese.",
        "Die Gründe für die Geisteskrankheit liegen tief in der menschlichen Natur.",
        "Die heutige Medizin schafft auf diesem Gebiete nichts Positives zutage; sie hat nur Hypothesen, Zweifel, Mutmaßungen.",
        "Allerdings ist es schwer, ja unmöglich für den Materialisten, sich in diesen Fragen Klarheit zu schaffen.",
        "Gar vieles, was der Arzt nicht mehr zu den Geisteskrankheiten"
      ],
      [
        "rechnet, gehört schon dazu: zum Beispiel Queru­lantenwahnsinn, ebenso religiöse Sektierer und Fanatiker.",
        "Letztere leben unter einer Idee wie unter einer Zwangsvor­stellung und üben auf Schwache eine große suggestive Kraft aus, so daß Zeitkrankheiten, Gedankenepidemien entstehen."
      ],
      [
        "Wie kann sich eigentlich so etwas wie Irrsinn im Wesen des Menschen festsetzen?",
        "Zur Beantwortung dieser Frage müssen wir die vier niederen Glieder des Menschen: physi­scher Leib, Lebensleib, Astralleib und das Ich vor Augen haben.",
        "Das Ich arbeitet an den drei übrigen Gliedern der menschlichen Wesenheit.",
        "Vor allem veredelt und läutert es den Astralleib, indem es ihn zwingt, nicht blind seinen Trie­ben zu folgen.",
        "Aber das Ich arbeitet auch in den Lebensleib hinein, und zwar durch die großen Impulse des Lebens, namentlich durch die künstlerischen Impulse.",
        "Wie im Astral­leib durch die Arbeit des Ich zwei Teile entstehen, ein ge­läuterterer und ungeläuterterer, so wird nun auch der Le­bensleib zweigeteilt.",
        "Und allmählich wird der Teil, der vom Ich bearbeitet wird, immer größer.",
        "Auch ins Physische wirkt das Ich, aber unbewußt.",
        "Bewußt vermag es das nur bei einem höheren Schüler der Eingeweihten."
      ],
      [
        "Nun müssen wir, um unsere Frage beantworten zu können, uns an die Wiederverkörperung erinnern.",
        "Beim Schlafen geht etwas ganz Ahnliches mit uns vor wie beim Tode.",
        "Im Schlafe trennen sich der Astralleib und das Ich vom physischen Körper.",
        "Alle Triebe und Empfindungen sinken damit hinab in ein unbewußtes Dunkel.",
        "Im Bette blei­ben nur der physische Leib und der Atherleib zurück.",
        "Beim Tode trennt sich auch der Ather- oder Lebensleib vom phy­sischen Körper los.",
        "In den nächsten Stunden, während des Menschen Wesenheit im Atherleibe ruht, zieht das ganze bisherige Leben in großen Bildern an seiner Seele vorüber, so lange, bis auch der Atherleib sich von ihm ablöst und im"
      ],
      [
        "allgemeinen Weltenäther aufgeht.",
        "Aber nur das Stoffliche des Atherleibes löst sich auf.",
        "Das Erinnerungsbild bleibt, wie eine Essenz, durch alle folgenden Zeiten mit dem Astral­leibe und dem Ich verbunden."
      ],
      [
        "Zunächst geht es mit in den Kamaloka-Zustand über.",
        "Kamaloka, Ort der Begierden, nennen wir den Zustand, in dem alles das aus dem Astral­leib ausgeschieden wird, was noch am Erdenleben hängt.",
        "Alles, was noch nicht veredelt war, löst sich auf, das andere wird in alle Zukunft mitgenommen."
      ],
      [
        "In ganz geringem Maße gehen auch Teile des physischen Leibes mit, aber nur bei sehr veredelten Menschen.",
        "Bei der neuen Verkörperung nimmt der Mensch die unveredelten Teile wieder an sich, um weiter an ihrer Läuterung zu arbeiten."
      ],
      [
        "Je öfter der Mensch auf Erden erscheint, desto fester wird sein Charak­ter, ein desto feineres Gewissen bekommt er, desto größer und zahlreicher sind seine Talente und Kräfte.",
        "Den her­metischen Grundsatz brauchen wir vor allem bei der Erklä­rung der Geisteskrankheiten: Es ist oben alles wie unten und unten alles wie oben."
      ],
      [
        "Im lächelnden Antlitz drückt sich uns ohne weiteres die Heiterkeit des Menschen aus.",
        "Die Tränenperle kündet innere Trauer der Seele an.",
        "Heiterkeit und Trauer werden wir in diesem Falle das Obere nennen, Lächeln und Tränen, die das materielle Bild von Heiterkeit und Trauer darstellen, das Untere."
      ],
      [
        "Ein richtig geschulter Mensch sieht die ganze Welt anders an.",
        "Eine Blume ist ihm der Ausdruck der Trauer oder der Heiterkeit des Erd­geistes.",
        "Und das ist ihm so wenig ein bloß poetischer Ge­danke, wie die Seele nur ein poetischer Gedanke ist."
      ],
      [
        "Der Erde liegt der Erdengeist als Oberes zugrunde.",
        "Alles Mate­rielle ist verdichteter Geist, geradeso wie das Eis nur ver­dichtetes Wasser ist.",
        "Wie man das Eis schmelzen kann, so daß es Wasser wird, so kann man auch die Materie wandeln, so daß sie Geist wird."
      ],
      [
        "Wir unterscheiden folgende physische"
      ],
      [
        "Teile am Menschen, die seinen oberen Gliedern entsprechen:"
      ],
      [
        "erstens rein Physisches, was nach rein physischen Gesetzen gebaut ist, vor allem die Sinnesorgane, zweitens alles das, was mit Verdauung, Wachstum, Fortpflanzung zusammen­hängt.",
        "Das, was die Kristalle aufbaut, könnte auch den menschlichen Leib aufbauen, aber er wäre dann ein toter Organismus.",
        "Der Atherleib ist der Bildner, der die Ver­dauungsorgane und so weiter aufbaut.",
        "Drittens Nerven­system (Gehirn und Rückenmark): sein Bildner ist der Astralleib, viertens das Blut.",
        "In ihm wohnt das Ich, das zugleich der Architekt des Blutsystems ist."
      ],
      [
        "Blutzirkulation: Ich"
      ],
      [
        "Nervensystem: Astralleib"
      ],
      [
        "Fortpflanzung: Ätherleib"
      ],
      [
        "Physisches: Physischer Leib"
      ],
      [
        "Alles Physische ist den Gesetzen der physischen Ver­erbung unterworfen, aber ebenso die Fortpflanzungsorgane, Nervensystem und Blutzirkulation.",
        "Mit diesem physischen Leib muß sich die Individualität vereinigen.",
        "Das Ich mit seinem veredelten Astral- und Atherleib, ja sogar Teile des physischen Leibes, müssen mit dem Ererbten zusammen­stimmen, eine Harmonie muß das zusammen bilden.",
        "Fast immer findet auch wirklich ein Zusammenstimmen statt, denn dem Geistigen paßt sich das Physische an, es wandelt sich um.",
        "Wie, wenn aber eine solche Anpassung nicht mög­lich ist, wie, wenn der Astralleib ein Nervensystem be­kommt, das er nicht ohne weiteres benutzen kann?"
      ],
      [
        "Sinnestäuschungen rechnen wir nicht zu den Geistes­krankheiten.",
        "Dazu kann uns ein Buch des Wiener Kriminal­anthropologen Moritz Benedikt viel Interessantes bieten, obwohl es nicht in geisteswissenschaftlichem Sinne geschrie­ben ist.",
        "Benedikt erzählt darin seine eigenen Erlebnisse und"
      ],
      [
        "Erfahrungen.",
        "Er hat im linken Auge einen partiellen Star, so daß er etwas unregelmäßig sieht.",
        "Wenn er nun im Dun­kel in einer ganz bestimmten Richtung schaut, so sieht er Gespenster ganz besonderer Art.",
        "Einmal ward er davon so erschreckt, daß er zur Waffe griff.",
        "Das ist so zu erklären:"
      ],
      [
        "Ein gesunder Mensch ist sich der inneren Bestandteile seines Auges nicht bewußt.",
        "Wer aber Unregelmäßigkeiten im Auge hat, der wird sich deren in der Weise bewußt, daß sie ihm außen im Spiegelbilde erst entgegentreten."
      ],
      [
        "Das wollen wir nun auf die ganze menschliche Wesenheit ausdehnen.",
        "Wir werden uns ja unseres Innern überhaupt nicht bewußt, son­dern nur dessen, was uns von außen übermittelt wird.",
        "Wenn Harmonie herrscht zwischen oben und unten, so ist man sich der innern Vorgänge überhaupt nicht bewußt."
      ],
      [
        "Hat einer zum Beispiel ein schwerfälliges Gehirn, das der Astral­leib nicht gebrauchen kann, so drückt sich diese Störung, die der Astralleib erleidet, ebenso nach außenhin aus, wie die Störung im Auge es tat.",
        "Da wird der Astralleib sich seiner selbst bewußt, weil er gestört ist; da sieht er sich nach außen projiziert, Hoffnungen, Wünsche, Begierden treten ihm in Gestalten von außen entgegen."
      ],
      [
        "Wahnsinn, Querulanten­wahnsinn, Hysterie gehören hierher, alles das, wo der Mensch seine Gefühle nicht in Einklang bringen kann mit der Außenwelt.",
        "Aber auch der Atherleib kann an inneren Abnormitäten leiden."
      ],
      [
        "Er ist der Träger der bildlichen Vor­stellungen.",
        "Wenn der Atherleib sich seiner selbst unbewußt Ist, so treten die Bilder der Außenwelt ihm wahr entgegen.",
        "Spiegeln sich aber bei Störungen des Atherleibes die Bilder nach außen, so werden es Wahnideen, Paranoia."
      ],
      [
        "Wenn der physische Leib, der den Einklang mit der physischen Um­gebung bringen soll, selbst erkrankt, wenn der physische Leib sich seiner selbst bewußt wird, so tritt Idiotie auf.",
        "Wenn der physische Leib zu schwer ist, so daß der Astralleib"
      ],
      [
        "ihn nicht beherrschen kann, daß er nicht heraus kann, so tritt das ein, was man Dementia nennt.",
        "Wenn die phy­sischen Organe aber zu beweglich sind, so daß sie die seeli­sche Tätigkeit nicht deutlich ausdrücken, so entsteht Paralyse.",
        "Doch es gibt hier eine unendliche Fülle von solchen Fällen, die ganz verschiedenen Ursprung haben können, namentlich die Wahnvorstellungen.",
        "Sie können entspringen einmal aus der Projektion des Astralleibes oder aus der Erkrankung des Astralleibes.",
        "Dann werden die Affekte so stark, daß es zu Tobsuchtsanfällen kommt.",
        "Diese drücken sich im Äther-leib ab und daraus entstehen Wahnideen.",
        "Diese Wahnvor­stellungen sind wie die Narbe zu der Wunde im Astralleib.",
        "Sie sind viel schwerer heilbar als die Tobsucht.",
        "Pupillen-starre ist manchmal eine Vorbereitung zum Wahnsinn."
      ],
      [
        "Wir wollen uns nun daran erinnern, daß der Mensch mehr als einmal geboren wird.",
        "Zuerst physisch.",
        "Dann zur Zeit des Zahnwechsels wird der Ätherleib geboren und zur Zeit der Geschlechtsreife der Astralleib.",
        "Es kann nun vor­kommen, daß erst bei der Geburt des Astralleibes der Miß­klang zwischen oben und unten bemerkbar wird.",
        "Vorher bewahrte die umschließende Astralhülle den Einklang.",
        "Nach der astralen Geburt ist dann der Astralleib sich selbst über-lassen, und nun tritt der Mißklang zwischen ihm und dem physischen Leibe hervor.",
        "Diese Art von Irrsinn äußert sich in der Weise, daß das junge Wesen oft auf ganz verschiedene Fragen ein und dieselbe Antwort gibt; auch leidet es unter Zwangsvorstellungen.",
        "Man nennt diese Erkrankungen Ju­gendblödsinn.",
        "Doch tritt dies nicht plötzlich auf, sondern bereitet sich langsam vor, vom elften, zwölften Jahre an.",
        "De­pressionszustände, Ermüdbarkeit, Nicht-Auskommen mit der Umgebung, Kopfschmerzen, Verdauungs- und Schlaf­störungen sind Vorboten.",
        "Es ist traurig, wenn man bedenkt, daß die meisten Eltern ihre Kinder für solche Erkrankungen"
      ],
      [
        "noch bestrafen, da sie diese Zustände für Unarten hal­ten.",
        "Gerade der Jugendblödsinn ist am schwersten zu heilen.",
        "Aber der Geist als solcher kann nicht krank sein; er ist immer gesund.",
        "Er wird nur gestört, wenn das Untere nicht dazu stimmt."
      ],
      [
        "Wenn man sich in einem Gartenkugelspiegel betrachtet, so sieht man ein Zerrbild seiner selbst.",
        "Niemand schließt aber aus dem Zerrbild, daß das wahre Gesicht auch verzerrt sein müsse.",
        "So ist es auch mit den Geisteskrank­heiten."
      ],
      [
        "Zerrbilder des Geistes im Physischen sind die Wahn­sinnsformen.",
        "Darum ist auf dem Wege der Logik, des ab­strakten Begriffes nie eine Heilung möglich.",
        "Solche Versuche sind völlig wertlos.",
        "Auch unsere körperlichen Organe sind verdichteter Geist, wenn auch nicht unser Geist."
      ],
      [
        "Und am fernsten stehen dem zum Physischen verdichteten Geiste schattenhafte, logische Gebilde; am nächsten aber bildliche, von Leidenschaften durchzogene, imaginative Vorstellun­gen.",
        "Diese können die krankmachende Kraft anderer Bilder aus dem Felde schlagen."
      ],
      [
        "Gegenvorstellungen muß man geben durch die Macht und Gewalt einer anderen Persönlichkeit.",
        "Das Unlogische kann man den Kranken nicht durch Klar­machen beweisen, aber durch lebendige Vorstellungen kann man wirken."
      ],
      [
        "Die Macht der Persönlichkeit muß dem Kran­ken beweisen, daß er zum Beispiel das, was er nicht zu können glaubt, doch kann.",
        "Das muß der Kranke sehen.",
        "Auf dem Gebiete der sogenannten Geisteskrankheiten wird sich die gewöhnliche Wissenschaft einst mit der Geisteswissen­schaft verbinden müssen."
      ],
      [
        "Ein ausführliches Studium ist nötig, um immer die richtigen Gegenvorstellungen bereit zu haben.",
        "Diese dürfen auch nicht «normal» sein, sondern müssen nach der anderen Seite ausschlagen."
      ],
      [
        "Die Geisteswissenschaft ist nichts Tatenloses, sie ver­kriecht sich nicht in Weltenfernheit; sie will praktisch mit­arbeiten.",
        "Weil geistige Kräfte der Welt zugrunde liegen,"
      ],
      [
        "müssen wir sie kennenlernen, wenn wir in der Welt wirken wollen.",
        "Unsere materielle Welt ist ein Abdruck der geistigen Welt.",
        "Die müssen wir kennenlernen, um das Physische zu verstehen.",
        "Freilich sagt Hellenbach: Was geht uns all das Geistergesindel an.",
        "Wir aber wollen sagen: Doch, das Men­schengesindel geht uns an, und da die Menschen mit der geistigen Welt verbunden sind, so wollen wir die Brücke zwischen beiden finden."
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "WEISHEIT UND GESUNDHEIT Berlin, 14. Februar 1907",
    "paragraphs": [
      "Die Geisteswissenschaft will im praktischen Leben wirken, sie will den Menschen Kraft und Sicherheit geben. Sie ist nichts für Neugierige, sondern nur für solche, die tätig sein wollen, die kräftig mitarbeiten wollen im Leben. Gei­steswissenschaft hat es zu allen Zeiten gegeben. In den Kreisen, in denen man sie pflegte, hieß es immer, daß der Mensch über die reine Verstandeskraft hinaus sich zu höhe­ren Geisteskräften entwickeln könne, als die des gewöhn­lichen Lebens sind. Den Zusammenhang von heilig, heil und heilsam fühlte man dort immer. Der heilige Geist ist der absolut gesunde Geist, der sich in die menschliche Seele senkt, um Heil zu verbreiten in der Welt. Aber gerade von diesem Gesichtspunkte aus wird die Geisteswissenschaft oft mißverstanden. Sie führt den Menschen von endlichen, egoistischen Zielen des Wissens und Strebens zu großen, universellen Gesichtspunkten, zur Verbindung des Einzel­nen mit dem Universum. Aber die höheren Kräfte, die die Geisteswissenschaft dadurch verleiht, ziehen so viele Men­schen an und reizen sie zu egoistischem Streben. Trotzdem die Geisteswissenschaft in Wahrheit den Menschen am wei­testen abführt vom Persönlichen, so wird sie doch gar oft als Dienerin des Egoismus gebraucht. Von heute auf mor­gen wollen die Menschen ihre egoistischen Wünsche von ihr erfüllt haben.",
      "Es gab Geisteswissenschaft bei einer Brüderschaft in Afrika, den Therapeuten. Dieselbe Sekte hieß in dem Teil der Erde,",
      "in dem das Christentum entstand, Essener oder Essäer. Schon der Name «Therapeuten» zeigt ihre Beziehung zum Geiste und zur Gesundheit. Durch Mittel des Geistes, in Verbin­dung mit materieller Wissenschaft, heilten die Therapeuten oder Essäer. Wer die Geisteswissenschaft aufnimmt, nimmt wirkliche Heilmittel auf: ein Lebenselixier ist die Geistes­wissenschaft. Nicht durch Diskussion und logische Gründe soll sie bewiesen werden, sondern ins Leben eingeführt, soll sie diejenigen Menschen, in die sie einfließt, heil und gesund machen. Nur wissen, daß es Reinkarnation und Karma gibt, und in schönen Redensarten davon sprechen können, ist so gut wie Nicht-Geisteswissenschaft. Täglich, stündlich muß man in ihr leben, die Seele ganz damit durchdringen und ruhig abwarten, was geschieht, dann wird man ihre Wir­kung sehen. Wer die geisteswissenschaftlichen Gedanken in sich trägt wie Nahrung- und Samengedanken, in Stunden von Leid und Freude, in Stunden der Devotion und Erhe­bung, in Stunden, wo das Leben zu zerreißen droht, wer fühlt, wie sie Lust zur Arbeit, Kraft und Hoffnung bringen, der hat sie recht erfaßt. Hier gilt das Goethesche Wort:",
      "«Das Was bedenke, mehr bedenke Wie!»",
      "Eine ganz individuelle Angelegenheit des einzelnen Men­schen muß die Geisteswissenschaft werden. Zu den Sternen schaut der geisteswissenschaftlich strebende Mensch auf und begreift sie nach den Gesetzen des Lebens, die den ganzen Weltenraum durchpulsen. Wenn des Morgens die Sonne in ihrer Herrlichkeit heraufsteigt und am Abend der Mond in seiner stillen Pracht, wenn die Wolken am Himmelsraum dahinziehen, da schaut er hinauf und da werden ihm die Vorgänge am Himmelszelt zum Ausdruck des seelisch-gei­stigen universellen Lebens, wie wir die Bewegungen eines Gesichtes oder einer Hand als Ausdruck seelisch-geistigen Lebens im Menschen anschauen. Und dann schauen wir in",
      "die Vergangenheit, sehen das Wirken der geistigen Welt in der physischen und erheben unseren Sinn zum Geiste. Sauget den Geist ein, und ihr sauget gesundes Leben mit ihm ein! Aber fern sei jegliche Bequemlichkeit.",
      "«Erhebung zum Un­endlichen begründet die Gesundheit» sagen viele, vertiefen sich aber nur in abstrakte, allgemeine Gedanken. Das ist nicht wahre Geisteswissenschaft. Die wahre Geisteswissen­schaft geht aufs einzelne ein, sie fordert, daß wir uns in Geduld und Liebe mit jeder Pflanze, jedem Stein befassen.",
      "Nicht durch Zauberei wollen wir die Geisteswelt suchen. Sie ist da. Aber wir sollen sie nicht abseits von der Sinnlichkeit suchen, sondern da, wo wir hingestellt sind zur tüchtigen Arbeit des Tages. So wird die Geisteswissenschaft eine indi­viduelle Angelegenheit.",
      "Wie ein Mensch kein Verständnis haben kann für ein Ton- oder Bildwerk, so hat mancher auch kein Verständnis für den Geist. Was manche Menschen sich von Geistererscheinungen für Vorstellungen machen, kann folgendes Beispiel erläutern: In einer kleinen Stadt beobachtete man eines Abends einen merkwürdigen Licht­schein, der sich an der Kirchhofmauer hinzog.",
      "Die ganze Stadt sprach bald davon, und da man keine natürliche Er­klärung fand, so mußte es eine Geistererscheinung gewesen sein. Mehrere Personen hatten den Lichtschein gesehen, und das gerade machte die Sache zweifelhaft.",
      "Um einen wirk­lichen Geist zu sehen, muß der Mensch gewisse geistige Or­gane und Fähigkeiten entwickelt haben. In der heutigen Zeit kann das nur ganz vereinzelt vorkommen. Daß meh­rere beliebige Personen den Lichtschein sahen, ist der beste Beweis dafür, daß es kein Geist war.",
      "Die Sache klärte sich auch bald auf. Eine alte Dame pflegte allabendlich ihr Hündchen beim Scheine der Laterne herauszuführen. An diesem Abend ward zufällig der Lichtschein bemerkt. Wir sollen nicht derartigen vermeintlichen Geistererscheinungen",
      "nachspüren. Die alltäglichen Erscheinungen sind die wich­tigsten Manifestationen des Geistes für uns.",
      "Weisheit ist nicht bloß Wissenschaft, doch muß sie die Wissenschaft in sich haben: sie ist ins Leben übergetretene Wissenschaft, die in jedem Augenblick zu Entschluß und Tat werden kann. Wer bloß die Gesetze kennt, ist Wissen­schafter.",
      "Wer in jedem Augenblick das Wissen so anzuwen­den versteht, daß etwas daraus werden kann, ist weise. Weisheit ist fruchtbar gewordene Wissenschaft. Wir müs­sen vergessen, woher wir die Gesetze gewannen, und uns mit ihnen durchdringen, daß sie in uns eine Kraft werden.",
      "Goethe kam von der genauen Betrachtung der einzelnen Pflanze zur Idee der Urpflanze. Das ist ein Gebilde der geistigen Intuition, ein Bild einer Pflanze, das in uns leben kann, nach deren Bild man unzählige Pflanzen erfinden könnte, die noch nicht da sind, die aber lebensfähig sein könnten.",
      "Im Weisen werden die Gesetze so, daß sie sich loslösen vom Einzelnen, daß sie leben in Ewigkeit. Dazu gehört aber das, was man Imagination, bildliche Vorstellung nennt. Abstrakte Gedanken und Begriffe können Wissen­schaft sein, aber nicht Weisheit.",
      "Wäre Goethe bei Begriffen stehengeblieben, so hätte er nicht die Urpflanze gefunden. Die Urpflanze muß man so lebendig vor sich sehen, daß man sie zeichnen kann mit Wurzeln, Stengeln, Blättern und Früchten, ohne daß sie einer anderen Pflanze ähnlich wäre.",
      "Das ist kein Spiel der Phantasie. Die Phantasie ist nur ein Schattenbild der Imagination, aber sie kann sich zur Ima­gination erheben. Noch ist uns die Welt der Imagination nicht zugänglich, aber sie kann es werden.",
      "Dunkel wäre es um uns, wenn das Auge das einfallende Licht nicht in Bilder und Farbenvorstellungen umsetzen könnte. So müssen wir, wie im Auge, auch in der Seele Kräfte entwickeln, die gegen­ständlich sind.",
      "Wer glaubt, er müsse warten, bis eine nebelhafte",
      "Manifestation eines Geistes ihm erscheint, der hat diese Arbeit nicht erfaßt. Arbeiten muß die Seele, wie das Auge arbeitet, wenn das Licht einfällt. Ohne die Arbeit der Seele kann nie die geistige Welt einströmen. Es müssen Bil­der geschaffen werden in der Seele. Die Objektivität bleibt erhalten, wenn man nicht sich Bilder egoistischer Wünsche und so weiter schafft. Wenn der Mensch so seine Seele der geistigen Welt entgegenstreckt, dann strömt die geistige Welt in ihn hinein und wirkt gesundend. Gesundend wir­ken die Imaginationen, wirken die Bilder. Wenn man die Begriffe der Geisteswissenschaft zu Bildern machen kann, die nicht nur Linien, sondern Leben, Farben und Ton haben, wenn die ganze Welt solch ein Bild wird, dann wird diese Weisheit auf jedem Gebiete des Lebens solch Heilmittel werden, nicht nur für uns selbst, sondern auch für andere, für die ganze Welt. Wenn auch die Bilder zuerst falsch sind, so schadet das nicht. Sie werden berichtigt werden durch die, die uns leiten.",
      "Ein solcher Weiser war Paracelsus, er hat sich durch­drungen mit der ganzen Welt und sie umgewandelt in lebendige Kraft, so daß jede Pflanze ihm etwas zu sagen wußte. Was sagte sie ihm? Sie offenbarte ihm, was Weisheit ist. Das Tier ist in gewissem Sinne weise: im Instinkt des Tieres liegt Weisheit. Aber das Tier hat keine individuelle Seele, sondern eine Gruppenseele, die von außen wirkt, wie eine geistige Wesenheit. Alle Tiere, deren Blut man unbe­schadet mischen kann, haben eine gemeinsame Seele, die Gruppenseele. Diese Weisheit der von außen wirkenden Seele ward im Menschen individualisiert. Jeder Mensch hat seine eigene, von innen wirkende, individuelle Seele, aber die Sicherheit des Daseins mußte er dafür einbüßen. Un­sicherheit ist das Charakteristische der Wissenschaft. Men­schenleben ist Probieren, Wählen, Suchen, Tasten. Aber es",
      "gibt eine höhere Entwicklung. Das Wissen, das der Mensch sich mühsam auf dem Probierwege erringt, kann wieder Weisheit werden. Wenn man das Lebendige umschmilzt in ein von Farbe, Ton und Licht Erfülltes, in Imagination, so wird man weise. Das tat Paracelsus. So ging er an jede Pflanze, an jede chemische Substanz heran. Wie das Tier unmittelbar weiß, was ihm heilsam ist, so erkannte auch Paracelsus unmittelbar die Heilkräfte der Pflanzen: aber nicht unbewußt instinktiv, sondern von bewußter Weisheit erfüllt erfaßte er, welchen Kranken das gut sein werde. In diesem Sinne waren auch die Therapeuten und Essäer weise. Das kann man nicht durch Probieren erkennen, sondern nur dann, wenn die Weisheit zur Imagination wird. Die Pflanze spricht dann zu dem Bilde, das von ihr in der Seele lebt und sagt: Ja, dazu bin ich gut. Die Pflanze erkennt ihr Bild in der Seele des Menschen, der sie anschaut, sie verwandelt ihr Bild, und dann weiß und fühlt der Mensch unmittelbar, wozu sie gut ist. Die Geisteswissenschaft hat nichts gegen wirkliche Wissenschaft einzuwenden, und kein wahrhaft geisteswissenschaftlich strebender Mensch wird versäumen, sich mit den Errungenschaften der Wissenschaft bekannt zu machen. Aber er bleibt nicht stehen dabei, und so erhebt er das Wissen zu schöpferischem, weisheitsvollem Erkennen.",
      "Wir wissen, daß die menschliche Wesenheit zunächst zu­sammengesetzt ist aus physischem Leib, Äther- oder Lebens-leib, Astralleib und dem Ich. Das gewöhnliche Wissen nun dringt nur vor bis zum Astralleib und wird ein Glied von ihm. Die Imagination aber dringt bis in den Ätherleib hin­ein, erfüllt mit Lebensgeist den Lebensleib und macht, daß der Mensch ein lebendiger Heiler wird. Wie groß die Wir­kung der Imagination ist gegenüber rein abstrakten Be­griffen, können wir zunächst am besten erkennen an den schlimmen Wirkungen, die sie haben kann. Ein Mensch war",
      "anwesend, als seinem Bruder das Bein amputiert wurde. Bei der Bearbeitung des Knochens gab es einen merkwür­digen Ton. In demselben Moment fühlte er einen heftigen Schmerz an derselben Stelle des Beines, an der bei seinem Bruder die Operation vorgenommen wurde. Lange Zeit konnte er den Schmerz nicht loswerden, während sein Bru­der nichts mehr spürte. Da hatte der Klang des Knochens sich imaginativ in des Menschen Ätherleib eingegraben und die Schmerzen hervorgerufen.",
      "Sehr interessante Versuche machte auch ein Berner Arzt auf diesem Gebiete. Er nahm ein gewöhnliches Hufeisen und befestigte zwei Drähte derartig daran, als seien es die Leitungsdrähte einer Elektrisiermaschine. Jeder, der hinzu­kam, glaubte, es mit einer solchen zu tun zu haben, und fühlte wirklich, wenn er die Drähte berührte, einen elek­trischen Strom. Manche behaupteten sogar, die gräßlichsten Schmerzen zu fühlen. Die ganze Veranstaltung wirkte eben bildlich. Einreden hätte man das den Menschen nicht kön­nen. Es gibt gewisse Leute, die reich werden durch die Her­stellung von Pillen aus gewöhnlichem Brot. Diese Pillen «heilen» alle möglichen Krankheiten und finden nament­lich als Schlafmittel Anwendung. In einem Sanatorium pflegte eine Dame regelmäßig des Abends solche Pillen zu nehmen. Sie schlief stets vortreiflich danach. Da beschloß sie eines Abends, sich das Leben zu nehmen und nahm so viele Pillen, als sie erwischen konnte. Die Sache wurde in­des bemerkt und die Ärzte der Anstalt gerieten in die größte Aufregung, denn die Dame zeigte alle Symptome des her­annahenden Todes. Nur ein Arzt blieb ruhig, und das war der, der die Pillen gemacht hatte.",
      "Der Mensch muß Kraft haben, das bloß Gewußte zum lebendigen Bilde zu machen. Darauf beruht auch die Wir­kung der Hypnose. Ausgeschaltet ist in der Hypnose der",
      "astralische Leib, und der Hypnotiseur wirkt direkt auf den Ätherleib ein durch Bilder. Aber das ist ein krankhafter Prozeß. Die Bilder, die wir schaffen, drücken sich dem Ätherleib ein. Und sind die Bilder aus der geistigen Welt genommen, so können sie alles Krankhafte aus der geistigen Weltenkraft heraus austilgen, das heißt mit den Welten­strömungen ausgleichen, harmonisieren.",
      "Alles Krankhafte stammt aus dem Egoismus. Bei einem solchen Vorgang wer­den wir über unser gewöhnliches Vorstellungsleben hinaus-gehoben: Gleichsam ein Herabdämmern der gewöhnlichen Vorstellungen findet dann statt.",
      "Und das muß bisweilen eintreten, zum Beispiel im Schlaf. Da trennt sich der Astral­leib mit dem Ich ab von dem physischen Leib und Lebens-leib und vereint sich mit dem Geiste der Erde. Und von da aus wirkt er gesundend auf den Ätherleib ein, prägt ihm Gesundung bringende Bilder ein.",
      "Aber das geschieht un­bewußt. Nur der höher Entwickelte tut dies bewußt. Ur­ewige Ideen stehen hinter allem, sagt Plato. Ein Seher sieht das geistige Wesen in jeder Pflanze, die Gestalt der Pflanze ist ja selbst aus solchen geistigen Bildern aufgebaut.",
      "Der Mensch kann diese Bilder aufnehmen und dadurch schöp­ferisch werden. Nur Tiere und Menschen, eigentlich nur Menschen, können erkranken. Die Bilder als Geistiges wir­ken in der ganzen Natur, wir Menschen aber nehmen den Geist in uns hinein und müssen ihn nun wieder zum Leben erheben.",
      "Imaginative Weisheit wird Gesundheit bringen. Was befruchtend wirkt bis zum Bilde, das ist Weisheit. Der Geist schafft die Imagination. Die Geisteswissenschaft, die uns solche Weisheit gibt, kann uns am besten Heilung von Krankheiten bringen, und zwar vor allem - vorbeugend -von solchen, die man noch nicht hat.",
      "Aber das ist freilich schwer zu kontrollieren. Die Geisteswissenschaft hat auch die Kraft, die den Menschen verjüngt, kraftvoll und jung",
      "erhält. Die Weisheit gießt Lebenskraft in den Menschen, und die Jugendkraft ist etwas, was stark und frisch macht. Solche Weisheit öffnet die Seele. Und Weisheit ist der Same der Liebe. Liebe kann man nicht predigen. Am mitleid- und liebevollsten waren die Therapeuten und Essäer. Weisheit durchwärmt die menschliche Seele, läßt die Liebe ausströ­men; darum ist es nicht wunderbar, wenn solche Weise durch Handauflegen heilen konnten. Die Weisheit strömt Liebeskraft in die Glieder. Weil Christus der Weiseste war, war er auch der beste Heiler, strömte die Liebe und das Mitleid von ihm aus, was allein helfen kann. Wenn ein Mensch mit gebrochenem Bein auf der Straße liegt, und es stehen die liebevollsten Menschen um ihn herum, so werden sie ihm doch nicht helfen können. Wenn aber ein Arzt kommt, der ein Bein einzurichten versteht, dem seine Weis­heit ermöglicht, sein Mitleid zur Tat werden zu lassen, dann wird geholfen werden. Können, erkennen, weise sein ist die Grundlage alles Menschenhelfens. Weisheit ist immer um uns in der Welt, weil weise Wesen sie ausgossen. Wenn die Weisheit auf ihrem Gipfel angekommen ist, wird sie sein die allumfassende Liebe. Liebe wird die zukünftige Welt uns entgegenstrahlen. Weisheit ist die Mutter der Liebe. Der weisheitsvolle Geist ist der große Heiler. Dar­um ist der Christus, die Liebe, aus dem heiligen, das heißt heilenden Geist geboren."
    ],
    "sentences": [
      [
        "Die Geisteswissenschaft will im praktischen Leben wirken, sie will den Menschen Kraft und Sicherheit geben.",
        "Sie ist nichts für Neugierige, sondern nur für solche, die tätig sein wollen, die kräftig mitarbeiten wollen im Leben.",
        "Gei­steswissenschaft hat es zu allen Zeiten gegeben.",
        "In den Kreisen, in denen man sie pflegte, hieß es immer, daß der Mensch über die reine Verstandeskraft hinaus sich zu höhe­ren Geisteskräften entwickeln könne, als die des gewöhn­lichen Lebens sind.",
        "Den Zusammenhang von heilig, heil und heilsam fühlte man dort immer.",
        "Der heilige Geist ist der absolut gesunde Geist, der sich in die menschliche Seele senkt, um Heil zu verbreiten in der Welt.",
        "Aber gerade von diesem Gesichtspunkte aus wird die Geisteswissenschaft oft mißverstanden.",
        "Sie führt den Menschen von endlichen, egoistischen Zielen des Wissens und Strebens zu großen, universellen Gesichtspunkten, zur Verbindung des Einzel­nen mit dem Universum.",
        "Aber die höheren Kräfte, die die Geisteswissenschaft dadurch verleiht, ziehen so viele Men­schen an und reizen sie zu egoistischem Streben.",
        "Trotzdem die Geisteswissenschaft in Wahrheit den Menschen am wei­testen abführt vom Persönlichen, so wird sie doch gar oft als Dienerin des Egoismus gebraucht.",
        "Von heute auf mor­gen wollen die Menschen ihre egoistischen Wünsche von ihr erfüllt haben."
      ],
      [
        "Es gab Geisteswissenschaft bei einer Brüderschaft in Afrika, den Therapeuten.",
        "Dieselbe Sekte hieß in dem Teil der Erde,"
      ],
      [
        "in dem das Christentum entstand, Essener oder Essäer.",
        "Schon der Name «Therapeuten» zeigt ihre Beziehung zum Geiste und zur Gesundheit.",
        "Durch Mittel des Geistes, in Verbin­dung mit materieller Wissenschaft, heilten die Therapeuten oder Essäer.",
        "Wer die Geisteswissenschaft aufnimmt, nimmt wirkliche Heilmittel auf: ein Lebenselixier ist die Geistes­wissenschaft.",
        "Nicht durch Diskussion und logische Gründe soll sie bewiesen werden, sondern ins Leben eingeführt, soll sie diejenigen Menschen, in die sie einfließt, heil und gesund machen.",
        "Nur wissen, daß es Reinkarnation und Karma gibt, und in schönen Redensarten davon sprechen können, ist so gut wie Nicht-Geisteswissenschaft.",
        "Täglich, stündlich muß man in ihr leben, die Seele ganz damit durchdringen und ruhig abwarten, was geschieht, dann wird man ihre Wir­kung sehen.",
        "Wer die geisteswissenschaftlichen Gedanken in sich trägt wie Nahrung- und Samengedanken, in Stunden von Leid und Freude, in Stunden der Devotion und Erhe­bung, in Stunden, wo das Leben zu zerreißen droht, wer fühlt, wie sie Lust zur Arbeit, Kraft und Hoffnung bringen, der hat sie recht erfaßt.",
        "Hier gilt das Goethesche Wort:"
      ],
      [
        "«Das Was bedenke, mehr bedenke Wie!»"
      ],
      [
        "Eine ganz individuelle Angelegenheit des einzelnen Men­schen muß die Geisteswissenschaft werden.",
        "Zu den Sternen schaut der geisteswissenschaftlich strebende Mensch auf und begreift sie nach den Gesetzen des Lebens, die den ganzen Weltenraum durchpulsen.",
        "Wenn des Morgens die Sonne in ihrer Herrlichkeit heraufsteigt und am Abend der Mond in seiner stillen Pracht, wenn die Wolken am Himmelsraum dahinziehen, da schaut er hinauf und da werden ihm die Vorgänge am Himmelszelt zum Ausdruck des seelisch-gei­stigen universellen Lebens, wie wir die Bewegungen eines Gesichtes oder einer Hand als Ausdruck seelisch-geistigen Lebens im Menschen anschauen.",
        "Und dann schauen wir in"
      ],
      [
        "die Vergangenheit, sehen das Wirken der geistigen Welt in der physischen und erheben unseren Sinn zum Geiste.",
        "Sauget den Geist ein, und ihr sauget gesundes Leben mit ihm ein!",
        "Aber fern sei jegliche Bequemlichkeit."
      ],
      [
        "«Erhebung zum Un­endlichen begründet die Gesundheit» sagen viele, vertiefen sich aber nur in abstrakte, allgemeine Gedanken.",
        "Das ist nicht wahre Geisteswissenschaft.",
        "Die wahre Geisteswissen­schaft geht aufs einzelne ein, sie fordert, daß wir uns in Geduld und Liebe mit jeder Pflanze, jedem Stein befassen."
      ],
      [
        "Nicht durch Zauberei wollen wir die Geisteswelt suchen.",
        "Sie ist da.",
        "Aber wir sollen sie nicht abseits von der Sinnlichkeit suchen, sondern da, wo wir hingestellt sind zur tüchtigen Arbeit des Tages.",
        "So wird die Geisteswissenschaft eine indi­viduelle Angelegenheit."
      ],
      [
        "Wie ein Mensch kein Verständnis haben kann für ein Ton- oder Bildwerk, so hat mancher auch kein Verständnis für den Geist.",
        "Was manche Menschen sich von Geistererscheinungen für Vorstellungen machen, kann folgendes Beispiel erläutern: In einer kleinen Stadt beobachtete man eines Abends einen merkwürdigen Licht­schein, der sich an der Kirchhofmauer hinzog."
      ],
      [
        "Die ganze Stadt sprach bald davon, und da man keine natürliche Er­klärung fand, so mußte es eine Geistererscheinung gewesen sein.",
        "Mehrere Personen hatten den Lichtschein gesehen, und das gerade machte die Sache zweifelhaft."
      ],
      [
        "Um einen wirk­lichen Geist zu sehen, muß der Mensch gewisse geistige Or­gane und Fähigkeiten entwickelt haben.",
        "In der heutigen Zeit kann das nur ganz vereinzelt vorkommen.",
        "Daß meh­rere beliebige Personen den Lichtschein sahen, ist der beste Beweis dafür, daß es kein Geist war."
      ],
      [
        "Die Sache klärte sich auch bald auf.",
        "Eine alte Dame pflegte allabendlich ihr Hündchen beim Scheine der Laterne herauszuführen.",
        "An diesem Abend ward zufällig der Lichtschein bemerkt.",
        "Wir sollen nicht derartigen vermeintlichen Geistererscheinungen"
      ],
      [
        "nachspüren.",
        "Die alltäglichen Erscheinungen sind die wich­tigsten Manifestationen des Geistes für uns."
      ],
      [
        "Weisheit ist nicht bloß Wissenschaft, doch muß sie die Wissenschaft in sich haben: sie ist ins Leben übergetretene Wissenschaft, die in jedem Augenblick zu Entschluß und Tat werden kann.",
        "Wer bloß die Gesetze kennt, ist Wissen­schafter."
      ],
      [
        "Wer in jedem Augenblick das Wissen so anzuwen­den versteht, daß etwas daraus werden kann, ist weise.",
        "Weisheit ist fruchtbar gewordene Wissenschaft.",
        "Wir müs­sen vergessen, woher wir die Gesetze gewannen, und uns mit ihnen durchdringen, daß sie in uns eine Kraft werden."
      ],
      [
        "Goethe kam von der genauen Betrachtung der einzelnen Pflanze zur Idee der Urpflanze.",
        "Das ist ein Gebilde der geistigen Intuition, ein Bild einer Pflanze, das in uns leben kann, nach deren Bild man unzählige Pflanzen erfinden könnte, die noch nicht da sind, die aber lebensfähig sein könnten."
      ],
      [
        "Im Weisen werden die Gesetze so, daß sie sich loslösen vom Einzelnen, daß sie leben in Ewigkeit.",
        "Dazu gehört aber das, was man Imagination, bildliche Vorstellung nennt.",
        "Abstrakte Gedanken und Begriffe können Wissen­schaft sein, aber nicht Weisheit."
      ],
      [
        "Wäre Goethe bei Begriffen stehengeblieben, so hätte er nicht die Urpflanze gefunden.",
        "Die Urpflanze muß man so lebendig vor sich sehen, daß man sie zeichnen kann mit Wurzeln, Stengeln, Blättern und Früchten, ohne daß sie einer anderen Pflanze ähnlich wäre."
      ],
      [
        "Das ist kein Spiel der Phantasie.",
        "Die Phantasie ist nur ein Schattenbild der Imagination, aber sie kann sich zur Ima­gination erheben.",
        "Noch ist uns die Welt der Imagination nicht zugänglich, aber sie kann es werden."
      ],
      [
        "Dunkel wäre es um uns, wenn das Auge das einfallende Licht nicht in Bilder und Farbenvorstellungen umsetzen könnte.",
        "So müssen wir, wie im Auge, auch in der Seele Kräfte entwickeln, die gegen­ständlich sind."
      ],
      [
        "Wer glaubt, er müsse warten, bis eine nebelhafte"
      ],
      [
        "Manifestation eines Geistes ihm erscheint, der hat diese Arbeit nicht erfaßt.",
        "Arbeiten muß die Seele, wie das Auge arbeitet, wenn das Licht einfällt.",
        "Ohne die Arbeit der Seele kann nie die geistige Welt einströmen.",
        "Es müssen Bil­der geschaffen werden in der Seele.",
        "Die Objektivität bleibt erhalten, wenn man nicht sich Bilder egoistischer Wünsche und so weiter schafft.",
        "Wenn der Mensch so seine Seele der geistigen Welt entgegenstreckt, dann strömt die geistige Welt in ihn hinein und wirkt gesundend.",
        "Gesundend wir­ken die Imaginationen, wirken die Bilder.",
        "Wenn man die Begriffe der Geisteswissenschaft zu Bildern machen kann, die nicht nur Linien, sondern Leben, Farben und Ton haben, wenn die ganze Welt solch ein Bild wird, dann wird diese Weisheit auf jedem Gebiete des Lebens solch Heilmittel werden, nicht nur für uns selbst, sondern auch für andere, für die ganze Welt.",
        "Wenn auch die Bilder zuerst falsch sind, so schadet das nicht.",
        "Sie werden berichtigt werden durch die, die uns leiten."
      ],
      [
        "Ein solcher Weiser war Paracelsus, er hat sich durch­drungen mit der ganzen Welt und sie umgewandelt in lebendige Kraft, so daß jede Pflanze ihm etwas zu sagen wußte.",
        "Was sagte sie ihm?",
        "Sie offenbarte ihm, was Weisheit ist.",
        "Das Tier ist in gewissem Sinne weise: im Instinkt des Tieres liegt Weisheit.",
        "Aber das Tier hat keine individuelle Seele, sondern eine Gruppenseele, die von außen wirkt, wie eine geistige Wesenheit.",
        "Alle Tiere, deren Blut man unbe­schadet mischen kann, haben eine gemeinsame Seele, die Gruppenseele.",
        "Diese Weisheit der von außen wirkenden Seele ward im Menschen individualisiert.",
        "Jeder Mensch hat seine eigene, von innen wirkende, individuelle Seele, aber die Sicherheit des Daseins mußte er dafür einbüßen.",
        "Un­sicherheit ist das Charakteristische der Wissenschaft.",
        "Men­schenleben ist Probieren, Wählen, Suchen, Tasten.",
        "Aber es"
      ],
      [
        "gibt eine höhere Entwicklung.",
        "Das Wissen, das der Mensch sich mühsam auf dem Probierwege erringt, kann wieder Weisheit werden.",
        "Wenn man das Lebendige umschmilzt in ein von Farbe, Ton und Licht Erfülltes, in Imagination, so wird man weise.",
        "Das tat Paracelsus.",
        "So ging er an jede Pflanze, an jede chemische Substanz heran.",
        "Wie das Tier unmittelbar weiß, was ihm heilsam ist, so erkannte auch Paracelsus unmittelbar die Heilkräfte der Pflanzen: aber nicht unbewußt instinktiv, sondern von bewußter Weisheit erfüllt erfaßte er, welchen Kranken das gut sein werde.",
        "In diesem Sinne waren auch die Therapeuten und Essäer weise.",
        "Das kann man nicht durch Probieren erkennen, sondern nur dann, wenn die Weisheit zur Imagination wird.",
        "Die Pflanze spricht dann zu dem Bilde, das von ihr in der Seele lebt und sagt: Ja, dazu bin ich gut.",
        "Die Pflanze erkennt ihr Bild in der Seele des Menschen, der sie anschaut, sie verwandelt ihr Bild, und dann weiß und fühlt der Mensch unmittelbar, wozu sie gut ist.",
        "Die Geisteswissenschaft hat nichts gegen wirkliche Wissenschaft einzuwenden, und kein wahrhaft geisteswissenschaftlich strebender Mensch wird versäumen, sich mit den Errungenschaften der Wissenschaft bekannt zu machen.",
        "Aber er bleibt nicht stehen dabei, und so erhebt er das Wissen zu schöpferischem, weisheitsvollem Erkennen."
      ],
      [
        "Wir wissen, daß die menschliche Wesenheit zunächst zu­sammengesetzt ist aus physischem Leib, Äther- oder Lebens-leib, Astralleib und dem Ich.",
        "Das gewöhnliche Wissen nun dringt nur vor bis zum Astralleib und wird ein Glied von ihm.",
        "Die Imagination aber dringt bis in den Ätherleib hin­ein, erfüllt mit Lebensgeist den Lebensleib und macht, daß der Mensch ein lebendiger Heiler wird.",
        "Wie groß die Wir­kung der Imagination ist gegenüber rein abstrakten Be­griffen, können wir zunächst am besten erkennen an den schlimmen Wirkungen, die sie haben kann.",
        "Ein Mensch war"
      ],
      [
        "anwesend, als seinem Bruder das Bein amputiert wurde.",
        "Bei der Bearbeitung des Knochens gab es einen merkwür­digen Ton.",
        "In demselben Moment fühlte er einen heftigen Schmerz an derselben Stelle des Beines, an der bei seinem Bruder die Operation vorgenommen wurde.",
        "Lange Zeit konnte er den Schmerz nicht loswerden, während sein Bru­der nichts mehr spürte.",
        "Da hatte der Klang des Knochens sich imaginativ in des Menschen Ätherleib eingegraben und die Schmerzen hervorgerufen."
      ],
      [
        "Sehr interessante Versuche machte auch ein Berner Arzt auf diesem Gebiete.",
        "Er nahm ein gewöhnliches Hufeisen und befestigte zwei Drähte derartig daran, als seien es die Leitungsdrähte einer Elektrisiermaschine.",
        "Jeder, der hinzu­kam, glaubte, es mit einer solchen zu tun zu haben, und fühlte wirklich, wenn er die Drähte berührte, einen elek­trischen Strom.",
        "Manche behaupteten sogar, die gräßlichsten Schmerzen zu fühlen.",
        "Die ganze Veranstaltung wirkte eben bildlich.",
        "Einreden hätte man das den Menschen nicht kön­nen.",
        "Es gibt gewisse Leute, die reich werden durch die Her­stellung von Pillen aus gewöhnlichem Brot.",
        "Diese Pillen «heilen» alle möglichen Krankheiten und finden nament­lich als Schlafmittel Anwendung.",
        "In einem Sanatorium pflegte eine Dame regelmäßig des Abends solche Pillen zu nehmen.",
        "Sie schlief stets vortreiflich danach.",
        "Da beschloß sie eines Abends, sich das Leben zu nehmen und nahm so viele Pillen, als sie erwischen konnte.",
        "Die Sache wurde in­des bemerkt und die Ärzte der Anstalt gerieten in die größte Aufregung, denn die Dame zeigte alle Symptome des her­annahenden Todes.",
        "Nur ein Arzt blieb ruhig, und das war der, der die Pillen gemacht hatte."
      ],
      [
        "Der Mensch muß Kraft haben, das bloß Gewußte zum lebendigen Bilde zu machen.",
        "Darauf beruht auch die Wir­kung der Hypnose.",
        "Ausgeschaltet ist in der Hypnose der"
      ],
      [
        "astralische Leib, und der Hypnotiseur wirkt direkt auf den Ätherleib ein durch Bilder.",
        "Aber das ist ein krankhafter Prozeß.",
        "Die Bilder, die wir schaffen, drücken sich dem Ätherleib ein.",
        "Und sind die Bilder aus der geistigen Welt genommen, so können sie alles Krankhafte aus der geistigen Weltenkraft heraus austilgen, das heißt mit den Welten­strömungen ausgleichen, harmonisieren."
      ],
      [
        "Alles Krankhafte stammt aus dem Egoismus.",
        "Bei einem solchen Vorgang wer­den wir über unser gewöhnliches Vorstellungsleben hinaus-gehoben: Gleichsam ein Herabdämmern der gewöhnlichen Vorstellungen findet dann statt."
      ],
      [
        "Und das muß bisweilen eintreten, zum Beispiel im Schlaf.",
        "Da trennt sich der Astral­leib mit dem Ich ab von dem physischen Leib und Lebens-leib und vereint sich mit dem Geiste der Erde.",
        "Und von da aus wirkt er gesundend auf den Ätherleib ein, prägt ihm Gesundung bringende Bilder ein."
      ],
      [
        "Aber das geschieht un­bewußt.",
        "Nur der höher Entwickelte tut dies bewußt.",
        "Ur­ewige Ideen stehen hinter allem, sagt Plato.",
        "Ein Seher sieht das geistige Wesen in jeder Pflanze, die Gestalt der Pflanze ist ja selbst aus solchen geistigen Bildern aufgebaut."
      ],
      [
        "Der Mensch kann diese Bilder aufnehmen und dadurch schöp­ferisch werden.",
        "Nur Tiere und Menschen, eigentlich nur Menschen, können erkranken.",
        "Die Bilder als Geistiges wir­ken in der ganzen Natur, wir Menschen aber nehmen den Geist in uns hinein und müssen ihn nun wieder zum Leben erheben."
      ],
      [
        "Imaginative Weisheit wird Gesundheit bringen.",
        "Was befruchtend wirkt bis zum Bilde, das ist Weisheit.",
        "Der Geist schafft die Imagination.",
        "Die Geisteswissenschaft, die uns solche Weisheit gibt, kann uns am besten Heilung von Krankheiten bringen, und zwar vor allem - vorbeugend -von solchen, die man noch nicht hat."
      ],
      [
        "Aber das ist freilich schwer zu kontrollieren.",
        "Die Geisteswissenschaft hat auch die Kraft, die den Menschen verjüngt, kraftvoll und jung"
      ],
      [
        "erhält.",
        "Die Weisheit gießt Lebenskraft in den Menschen, und die Jugendkraft ist etwas, was stark und frisch macht.",
        "Solche Weisheit öffnet die Seele.",
        "Und Weisheit ist der Same der Liebe.",
        "Liebe kann man nicht predigen.",
        "Am mitleid- und liebevollsten waren die Therapeuten und Essäer.",
        "Weisheit durchwärmt die menschliche Seele, läßt die Liebe ausströ­men; darum ist es nicht wunderbar, wenn solche Weise durch Handauflegen heilen konnten.",
        "Die Weisheit strömt Liebeskraft in die Glieder.",
        "Weil Christus der Weiseste war, war er auch der beste Heiler, strömte die Liebe und das Mitleid von ihm aus, was allein helfen kann.",
        "Wenn ein Mensch mit gebrochenem Bein auf der Straße liegt, und es stehen die liebevollsten Menschen um ihn herum, so werden sie ihm doch nicht helfen können.",
        "Wenn aber ein Arzt kommt, der ein Bein einzurichten versteht, dem seine Weis­heit ermöglicht, sein Mitleid zur Tat werden zu lassen, dann wird geholfen werden.",
        "Können, erkennen, weise sein ist die Grundlage alles Menschenhelfens.",
        "Weisheit ist immer um uns in der Welt, weil weise Wesen sie ausgossen.",
        "Wenn die Weisheit auf ihrem Gipfel angekommen ist, wird sie sein die allumfassende Liebe.",
        "Liebe wird die zukünftige Welt uns entgegenstrahlen.",
        "Weisheit ist die Mutter der Liebe.",
        "Der weisheitsvolle Geist ist der große Heiler.",
        "Dar­um ist der Christus, die Liebe, aus dem heiligen, das heißt heilenden Geist geboren."
      ]
    ]
  },
  {
    "order": 11,
    "title_de": "DER LEBENSLAUF DES MENSCHEN VOM GEISTESWISSENSCHAFTLICHEN STANDPUNKTE Berlin, 28. Februar 1907",
    "paragraphs": [
      "Der alte Wahrspruch eines griechischen Mysterientempels:   «Erkenne dich selbst» geht durch die Menschheit als eine Aufforderung zu der tiefsten menschlichen Betrachtungs­weise. Er stellt eine der größten Wahrheiten dar, aber es geht mit diesem Ausspruch wie mit allen eigentlichen gro­ßen Wahrheiten: Richtig verstanden, bedeuten sie etwas Universelles, etwas Gewaltiges. Aber nur allzu leicht kön­nen sie mißverstanden werden - und dieser insbesondere. Er ist niemals im ursprünglichen Sinne so gemeint gewesen, daß der Mensch sein alltägliches Selbst betrachten soll, auch niemals so, daß der Mensch die Summe alles Wissens in sich selber finden könne. Wenn wir ihn richtig verstehen, so bedeutet er eine Aufforderung, das Selbst. das höhere Selbst des Menschen zu erkennen.",
      "Wo ist das höhere Selbst des Menschen?",
      "Wir können uns durch einen Vergleich klarmachen, wo dieses höhere Selbst ist und was dieser Spruch bedeutet. Gewiß, hätten wir nicht Augen, wir könnten unmöglich das Licht um uns herum wahrnehmen. Aber niemals - und das gilt als ebenso sicher - niemals könnten wir Augen haben, wenn nicht das den Raum durchflutende Sonnenlicht erst diese Augen geschaffen hätte. Aus ursprünglich niederen Organisationen, aus einem Lebewesen, das keine Augen hatte, das um sich nur Dunkles hatte, lockte geradezu das",
      "Licht erst die Augen heraus. Darum ist es so tief begründet, was Goethe sagt: «Die Augen sind am Licht und für das Licht gebildet.» Aber die Augen sind nicht da, um sich selbst zu betrachten. Wollten wir vom Standpunkt der Augen sprechen, so müßten wir sagen: Die Augen erfüllen ihren Zweck um so besser, je mehr sie sich selbst vergessen und ihren Schöpfer - das Licht - erkennen. Der Mensch würde immer mehr die Mission der Augen erfüllen, wenn er hereinblicken könnte in dieses Augeninnere selbst. Dieses sogenannte Innere vergessen und gerade das, was das Innere geschaffen hat, das höhere Selbst des Auges, das Licht, er­kennen, das ist die Aufgabe, die Mission des Auges! Ähn­lich verhält es sich mit dem, was der Mensch das gewöhn­liche Selbst nennt. Auch das ist nichts anderes als Organ, Werkzeug, und die Selbsterkenntnis steigt um so höher, je mehr dieses Selbst des Menschen sich selbst vergessen kann, je mehr es gewahr wird, daß in der Außenwelt ebenso das Geisteslicht ist, das unsere geistigen Augen geschaffen hat und noch fortwährend schafft. Daher ist mit Selbsterkennt­nis, wenn sie richtig verstanden wird, Selbstentwicklung gemeint. Dies müssen wir im Hintergrunde sehen, wenn wir heute ein Thema - wichtig für den Menschen wie wenige - betrachten wollen: das Thema der Selbsterkennt­nis im höchsten Sinne des Wortes.",
      "Wir wollen den Menschen betrachten von der Geburt bis zum Tode, und wollen die ganze Wesenheit des Menschen dabei berücksichtigen. Dann müssen wir allerdings nicht vergessen, daß der Mensch bei Beginn seines physischen Daseins bereits etwas mitbringt, daß er uns nicht wie etwas Neugebildetes entgegentritt, sondern wie ein Wesen, das schon wiederholte Erdenleben hinter sich hat und in diesen Erdenleben sich den Grundcharakter seiner Individualität bereits geholt hat. Wollen wir verstehen, was der Mensch",
      "bei seiner Geburt sich mitbringt, so müssen wir den Men­schen betrachten nach dem Tode. Denn daraus wird sich uns ergeben, was sich der Mensch durch den Zeitraum vom Tode bis zur neuen Geburt aufbewahrte, um es bei der neuen Geburt mitzubringen.",
      "Erinnern wir uns, was geschieht, wenn der Mensch stirbt:",
      "er hinterläßt den physischen Leichnam. Der wesentliche Unterschied zwischen Tod und Schlaf ist der, daß der Mensch im Schlafe im Bette liegen hat den physischen und den Ätherleib, und daß nur herausgeholt ist der Astralleib und das, was wir das Ich nennen.",
      "Ebenso wie die Ziegel­steine nicht von selbst zum Palast zusammenlaufen, so brauchen die physischen Kräfte den Ätherleib als inneren Architekten. Er ist mit dem Menschen verbunden und er­hält von der Geburt bis zum Tode den Zusammenhang der physischen Stoffe und Kräfte; er rettet jeden Augenblick die chemische Mischung vor dem Verfall.",
      "Im Tode hebt er sich jetzt wirklich heraus, und daher bleibt der physische Teil als der verfallende Leichnam zurück. Im Schlafe also geht nur der Astralleib, als der Träger von Lust und Leid, Begierden und Affekten, und dazu das Ich aus dem physi­schen Leib heraus; im Tode trennt sich nun noch der Ä ther­leib heraus und ist eine Weile mit dem Astralleib und dem Ich zusammen.",
      "Dies ist ein wichtiger Augenblick im Dasein des Menschen. In diesem Augenblick geht an der mensch­lichen Seele blitzschnell die Erinnerung an das ganze bis­herige Erdenleben vorüber, von der Geburt bis zum Tode, wie ein großes Tableau.",
      "Dieses Tableau stellt sich wie ein Gemälde dar. Alles, was uns mit Lust und Leid verknüpft hat, das empfinden wir in diesem Augenblicke nicht. Wie wir bei einem Gemälde nicht den Dolchstich fühlen, so füh­len wir auch dabei nicht all den Schmerz und all das Leid, die Lust oder Freude, die da an uns vorübergleiten.",
      "objektive Betrachter stehen wir da dem verflossenen Leben gegenüber.",
      "Dann kommt der Zeitpunkt, wo sich auch der Äther-leib herauszieht und auflöst im allgemeinen die Welt durch­flutenden Weltenäther. Aber etwas bleibt da von dem Äther-leib zurück: das ist eine Art Auszug aus dem ganzen bisherigen Leben. Das Tableau verliert sich und löst sich auf; aber wie wenn wir in einemBuche einen kurzen Auszug machen, so bleibt hier durch die ganzen folgenden Wege mit dem Menschen etwas wie eine Art Essenz vereinigt. Zu gleicher Zeit müssen wir uns eines klarmachen: Neben dieser Essenz vom Ätherleib bleibt, wenn auch wenig, nur gleich­sam ein Kraftpunkt, auch eine Essenz von dem physischen Leibe des Menschen zurück; selbstverständlich nicht so, daß ihn ein physisches Auge sehen kann, sondern wie ein Kraft-zentrum. Das ist mit dem Lebensleib ebenfalls verbunden, und das gibt dem physischen Leibe gerade die menschliche Form. Dann geht der Mensch durch einen Zustand durch, in dem er sich allmählich den Zusammenhang mit der phy­sischen Welt abgewöhnt.",
      "Jetzt ist nach dem Tode noch der Astralleib des Men­schen da. Um uns klarzumachen, welches Leben jetzt der Astralleib führt, stellen wir uns vor: alles, was der Mensch auch an den niedrigsten Genüssen erlebt, bleibt an seinem Astralleib haften. Der physische Leib fühlt nicht die Freude und hat keine Begierden; er ist das Werkzeug des Astral­leibes, und der hat daran seine Freude und seinen Genuß. Wenn wir zum Beispiel einen Feinschmecker vor uns haben, so hat nicht sein physischer Leib Genuß an den Genuß-mitteln, sondern der Astralleib empfindet ihn, indem er sich des physischen Werkzeuges zum Genuß bedient. Die Sucht zu genießen bleibt auch, wenn er den physischen Leib ab­gelegt hat; nur die Werkzeuge fehlen jetzt. Daraus ersehen",
      "Sie die Natur des Astralleibes, wie der jetzt nach dem Tode lebt. Es ist so, wie wenn Sie durch eine Gegend gehen, lech­zend vor Durst, aber diesen Durst nicht befriedigen können, weil weit und breit keine Quelle ist. In ähnlicher Weise empfindet der Astralleib aus einem guten Grunde Begier­den, Genußsucht, Affekte, die er früher gehabt hat, als einen brennenden Durst - nicht weil die Dinge nicht da sind, sondern weil ihm die Organe fehlen, um den Genuß zu befriedigen. Gerade deshalb haben die Religionen die Feuer­qualen, die der Mensch nach dem Tode zu bestehen hat, als Beispiel dafür hingestellt.",
      "Bis sich der Astralleib seinen Zusammenhang mit dem physischen Leibe abgewöhnt hat, bleibt er im Kamaloka, wo sich der Astralleib nach und nach freimachen muß von dem, was ihm zugeströmt ist, während er den physischen Leib hatte. Ein Mensch, der schon in diesem Leben seine Affekte geläutert hat, der nicht mehr an den rohen Genüs­sen der Nahrungsmittel, sondern an dem Schönen, der Kunst oder an der Geistigkeit seinen Gefallen findet, wird sich sein Kamaloka abkürzen; ein Mensch, der sich aber nur befriedigen kann durch die Anwendung dessen, was ihm die physischen Werkzeuge geben können, wird lange in der Sphäre des brennenden Durstes leben, und dieser Zustand endet damit, daß alles, was der Mensch in seinem Astralleib noch nicht vergeistigt hat, wie eine Art von Leichnam vom Astralleib abfällt, so wie der Ätherleib und der physische Leib abgefallen sind, und um so mehr abfallen muß, je weniger er seinen Astralleib geläutert und gereinigt hat. Daher wird später eine geläuterte Natur viel mitnehmen von ihrem Astralleib und zu dem hinzufügen, was wir die Essenz des physischen und Ätherleibes nannten.",
      "Mit diesen drei Essenzen geht das Ich nun ein in die eigentliche geistige Welt, und in dieser geistigen Welt hat",
      "das Ich auszubilden alles, was es hier während dieses Lebens erlebt und erworben hat. Sie brauchen nur daran zu denken, daß der eine schon mit großen Anlagen in das Leben hin­einkommt, als ganz junges Kind Anlagen hat, die wir nur herauszuholen brauchen. Die hat er, weil er während des Aufenthaltes im Geistesland seine Erfahrungen ausgebildet hat, die zu Fähigkeiten und Anlagen während dieser Zeit umgewandelt worden sind.",
      "Im Laufe eines jeden Erdenlebens bringt der Mensch etwas Neues hinzu zu den drei Essenzen seiner Leiber. Ein Mensch, der als ein besonders begabter Mensch geboren wird, hat seine früheren Leben gut angewendet, hat in sei­nem verflossenen Leben viele Blätter wie zu einem Buche zusammengelegt, und darin stehen die Erfahrungen und Errungenschaften seiner früheren Erdenleben. Damit tritt der Mensch in ein neues Leben ein und erhält einen physi­schen Leib von seinen physischen Vorfahren. Dieser Wesens-kern, der sich aus den früheren Erlebnissen die Früchte mitbringt, wird zu der Familie hingezogen, die ihm die phy­sischen Merkmale geben kann, die ihn befähigen, seine indi­viduellen Anlagen, die er sich früher erworben hat, zu gebrauchen. Nicht sind es die Vererbungsmerkmale, die des Menschen Handeln und Fähigkeiten ausmachen, die liefern nur die Werkzeuge; aber die Werkzeuge müssen da sein. Wie der Klaviervirtuose ein Instrument, so muß die Indi­vidualität, wenn sie von einem neuen physischen Leib um­hüllt wird, in diesem die richtigen Werkzeuge finden, um sich in der physischen Welt in der richtigen Weise zum Ausdruck bringen zu können. Daher die Täuschung, als ob nur physische Vererbung vorliegt. Gewiß liegt sie vor, aber nur weil die Individualität sich zu den Eltern hingezogen fühlt, die ihr die geeigneten Werkzeuge geben können. Alles, von dem wir gesagt haben, daß es im Laufe der Zeit",
      "abgeworfen worden ist, muß sich in derselben Weise wieder um den Menschen herum kristallisieren; alles das erhält der Mensch wiederum neu, damit er im weiteren Leben von neuem zur Läuterung seiner Wesenheit beitragen kann.",
      "Für die erste Hälfte des menschlichen Lebens haben wir schon die Bausteine zusammengetragen. Wir werden nun etwas zu wiederholen haben aus dem Bereich der Erzie­hungs- und Schulfragen, werden das für den zweiten Teil des menschlichen Lebenslaufes weiter auszubauen haben, um zu sehen, wie der physische, ätherische und astralische Leib im ersten Teil des menschlichen Lebenslaufes sich ent­wickeln, und wie Glück und Inhalt des Menschenlebens da­von abhängen. Dies ist ein wichtiges Kapitel, das wir aller­dings so auffassen müssen, daß es große Gesetze hinstellt, die vielfach Abänderung erfahren, aber in großen Umrissen gilt es. Und nur wer die Gesetze kennt und sie immer zu beachten versteht, wird sich in der richtigen Weise in den Lebenslauf einfügen, wird seiner Bestimmung immer klarer und klarer entgegengehen können.",
      "Beginnen wir bei des Menschen Geburt. Wir haben schon davon gesprochen, daß bei der physischen Geburt eigentlich erst sein physischer Leib völlig geboren wird, der bis dahin von der physischen Mutterhülle umgeben wurde. Da haben sich alle Organe nur dadurch entwickelt, daß der Mensch bis zur physischen Geburt gegen alle Seiten hin geschützt ist. Und nun ist es, wie wenn der Mensch die physische Mut­terhülle zurückstößt und sein physischer Leib jetzt allein erst den Wirkungen der physischen Elemente ausgesetzt ist. Nach dieser Geburt ist der Ätherleib noch nicht und noch weniger der Astralleib geboren; diese sind noch eingehüllt von einer Äther- und von einer astralen Hülle. Wie eine Schale, die nur für das geistige Auge des Sehers sichtbar ist, umgibt eine astrale und eine ätherische Hülle den Menschen,",
      "die nicht seiner eigenen Natur angehören, die ihn schützen und einhüllen. Die Ätherhülle umgibt den Menschen bis zum siebenten Jahre, der Zeit des Zahnwechsels. Da erst wird der Ätherleib geboren; da erst wird die Ätherhülle zurückgedrängt, wie die physische Hülle bei der physischen Geburt; und mit der Geschlechtsreife wird erst der Astral­leib der äußeren Welt vollständig ausgesetzt.",
      "Wir müssen uns klarmachen, daß in den ersten sieben Jahren des Lebens nur jene Essenz, die wir die Essenz des physischen Leibes nannten, vollständig frei wirkt, daß sie die physische Form gibt; sie leitet die physische Struktur ein. Die Organe wachsen in der Außenwelt heran, so daß sie ihre Form, ihre Anlage haben und nur noch weiterwach­sen brauchen. Wir müssen daher alles in seine Umgebung bringen, was die Struktur des physischen Leibes in der allerbesten Weise entfalten kann. Dafür konnten wir zwei Zauberworte anführen: Nachahmung und Beispiel oder Vor­bild. Alles, was um das Kind herum ist, wird von ihm nach­geahmt, und diese Nachahmung lockt die inneren Organe zu ihrer Form. Wenn auch das Gehirn mit dem siebenten Jahre noch sehr unvollkommen ist, die Richtung hat es doch erhalten, und was ihm bis dahin vorenthalten ist, kann es später nicht mehr nachholen. In den Zähnen macht das phy­sische Prinzip gleichsam Schlußpunkt, denn es ist das Prin­zip des Gestaltens, des Formens. So wie die Zähne am anschaulichsten zeigen, daß die Glieder sich konsolidiert haben, so sind auch die anderen weicheren Organe bestimmt. Das Licht wirkt und lockt die Kraft des Auges an die Ober­fläche. Wir haben erwähnt, daß es gut ist, dem Kinde mög­lichst nicht fertige Puppen und derartiges zu geben, wir haben erwähnt, daß ein gesundes Kind nur für eine kurze Zeit Freude daran findet. Dagegen hat es seine Freude daran, wenn Sie eine Serviette zusammenbinden und mit",
      "Tintenklecksen Augen und Ohren machen und ihm als Spielzeug geben. Wie ein Muskel nur stark wird, wenn er angewendet wird, so ist es auch hier: jetzt muß das Kind arbeiten und das in der Phantasie aufbauen, was die Puppe nicht hat. Da wird der innere organische Aufbau bewirkt. Es ist daher von besonderer Bedeutung, daß man das Kind innerlich arbeiten läßt, in seine Umgebung das bringt, was die Organe durchströmt mit Freude und Lust und Genuß an der Umgebung. Das schafft Kraft für die Bildung der Or­gane. Durch nichts kann man die Organe mehr ruinieren, als wenn man dem Kinde nicht das Richtige zuführt. Die Phan­tasie, die in ihm tätig ist, arbeitet an den Formen seiner Organe, und nichts wäre verfehlter, als durch eine falsche Askese das Kind an ein lustloses Dasein gewöhnen zu wol­len. Freude ist der Praktiker in den ersten Lebensjahren, und die gesunden Lebensinstinkte sind die Bildner, die man nur nicht verderben soll. Die richtige Nahrung, dem Kinde ge­reicht, wird bewirken, daß das Kind Lust an der Ernährung bekommt, die ihm frommt; falsche Nahrung wird das Kind krank machen. Für jede Stufe, für alles weiß die Geistes­wissenschaft da die nötigen Dinge. So müssen wir uns dar­über klar sein, daß in den ersten sieben Jahren das Gattungs­gemäße vorzugsweise herauskommt, denn das physische Prinzip arbeitet an dem Menschen, und ungestört müssen wir das Kind arbeiten lassen.",
      "Bei der Ernährungsfrage tritt ein innerlicher Zusammen­hang hervor zwischen der Muttermilch und dem Kinde, der sich dadurch ausdrückt, daß in den ersten Lebensjahren geradezu ein geistiges Verhältnis zwischen der Mutter und dem Kinde besteht; und eine Mutter, die ihr Kind selbst nährt, beachtet das. In der Muttermilch ist nicht bloß das, was physisch und chemisch ist, es ist etwas, was geistig ver­wandt ist mit dem Kinde. Der Geisteswissenschafter sieht",
      "da etwas, was aus dem Ätherleib der Mutter herausgeboren ist, und weil der Ätherleib des Kindes noch ungeboren ist, so verträgt er in der ersten Zeit insbesondere nur das, was schon durch einen anderen Ätherleib zubereitet ist. Es be­steht ein inniger Kontakt zwischen dem, was das Kind braucht, und dem, was ihm die Mutter selbst reicht. Pro­zentual betrachtet: Etwa 16 bis 20 Prozent derjenigen Kin­der, die im Säuglingsalter sterben, sind solche, die von der eigenen Mutter genährt werden; dagegen 26 bis 30 Prozent solche, die von Fremden genährt werden. Darin sehen Sie den Zusammenhang zwischen den Lebensleibern. Es ist eine Art Charakter, der sich in den ersten Lebensjahren physisch zum Ausdruck bringt; das mehr Gattungsmäßige bildet sich heraus, konsolidiert sich, wird fest, gibt ihm den Charakter, durch den es einem bestimmten Geschlecht angehört. Die Familienzüge prägen sich erst von dieser Zeit an auf seinem Antlitz aus.",
      "Die Zeit vom siebenten bis zum vierzehnten Jahre ist die, für welche wir schon die beiden Zauberworte «Nach­eiferung» und «Autorität» angeführt haben. Der Mensch braucht in dieser Zeit einen andern Menschen, der für ihn die Verkörperung alles Guten, Schönen und Weisen ist; er braucht einen Menschen überhaupt, in dem er die Grund­sätze und Lehren verleiblicht sieht. Mit Moralpredigen ist in dieser Zeit viel weniger getan, als wenn Sie dem Kinde Vorbilder anführen, die dem Kinde den Weg hinauf zum Olymp zeigen. Für die ganze spätere Zeit ist es für den Menschen von Bedeutung, wenn er jetzt einen Menschen über sich sieht, vor dem er eine tiefe Achtung hat. Selbst­verständliche Nachfolge ist es, um die es sich da handelt. Daher müssen wir den Geschichtsunterricht so einrichten, daß wir die Weisheit und verkörperte Charakterstärke dem Kinde im Bilde vor Augen führen; und vom Art-Charakter",
      "geht er über mehr zu einem Spezial-Charakter, was nicht mehr mit der Vorfahrenreihe zusammenhängt. Aus der Nachahmung der Eltern wird die Nachahmung der fremden Art. Der Gesichtskreis erweitert sich über das Familienhafte hinaus; wir müssen Menschen in die Nähe des Kindes brin­gen, damit der Ätherleib sich weiter ausbreiten kann über das Artgemäße hinaus.",
      "Während bis zum Zahnwechsel das sich ausprägt, was den Menschen in die Familie hineinstellt, bekommen die Gesten jetzt ihren Charakter; das, was den Menschen zu einem besonderen Menschen macht, prägt sich aus, wenn der Mensch heraustritt aus dem Kreise der Fa­milie. Denn jetzt ist die Ätherhülle zerschlagen, nun kann auf den Ätherleib gewirkt werden, wenn in des Kindes Umgebung solche Menschen sind, die durch das, was sie in sich selber tragen, solche Eigenschaften ausbilden können, die im Ätherleib des Kindes aufgespeichert liegen.",
      "Und jene Grundanlagen, die der Mensch als Früchte seiner früheren Inkarnation in seinem Ätherleib mitgenommen hatte, ent­wickeln sich jetzt, wo nach dem siebenten Jahre der Äther-leib nach allen Seiten frei ist. Daher muß der Erzieher wo­möglich etwas zurücktreten und nicht darauf pochen: dies sind die richtigen Erziehungsgrundsätze, sondern auf das sehen, was das Kind mitgebracht hat; denn jetzt müssen durch den freigewordenen Ätherleib nach allen Seiten die Organe erstarken und sich vergrößern.",
      "Während bis zum siebenten Jahre die physischen Organe durch physische Kräfte ausgearbeitet und plastisch gestaltet wurden, haben wir jetzt diese sich vergrößernden Organe, um Gewissen, Moral, Tatkraft, all die ätherischen Eigenschaften da hin­einzuarbeiten. Alles, was bildhaft ist, was mit der reineren geistigen Freude an der Natur zusammenhängt, müssen wir hineinprägen, denn das muß so fest im Menschen sitzen, daß es im Ätherleib haftet: Einen festen Charakter kann",
      "der Mensch nur haben, wenn er so seinen Ätherleib frei ent­wickeln kann. Und ein Erzieher muß sich in dieser Zeit sagen: Du hast es nicht zu tun mit etwas, das du formen kannst, so wie du willst; sondern du kannst da etwas für das ganze Leben verderben, wenn du nicht erlauschest, was aus dem früheren Ätherleib herübergekommen ist. Daher müssen auch die physischen Ubungen so ausgedacht sein, daß in dem Kinde das Gefühl des Erstarkens, des Vermehrt­werdens lebt. «Ich werde größer», «ich wachse», muß eine moralische, nicht bloß physische Empfindung im Kinde sein. Das arbeitet ebenso plastisch am Ätherleib wie das physische Prinzip am physischen Leibe.",
      "Und in derselben Weise wie, während die physische Mut­terhülle den physischen Leib umgibt, die physischen Organe sich ausbilden, so umgibt die Astralhülle noch die astralen Eigenschaften, die der Mensch sich mitbringt; die bilden sich zunächst in der astralischen Hülle, und erst mit der Ge­schlechtsreife tritt der Mensch der Welt mit einem freien Astralleib entgegen. Jetzt erst kann Urteil, Kritik und Be­griffsbildung hineingreifen. In einem früheren Lebensalter würde ihm das viel zu früh gegeben werden. Der Mensch sollte in einem früheren Lebensjahre noch kein Bekenntnis haben, denn das kann er sich erst bilden, wenn sein Astral­leib geboren ist. Vorher soll er aufschauen zu den Bekennern und von ihnen entgegennehmen, was er glauben soll; denn in diesem Zeitalter sich das selbst bestimmen, gibt eine astrale Karikatur. Vom okkulten Standpunkt ist es unmög­lich, wenn der junge Mensch veranlaßt wird, schon irgend­ein Bekenntnis zu haben. Es ist sinnlos und ist entwick­lungswidrig, wenn ein Kind in diesem Lebensalter es für möglich hält zu sagen: Ich habe ein eigenes Glaubensbe­kenntnis. Das wäre ein Zeichen, daß etwas in der Erziehung des betreffenden Menschen versäumt worden ist; daß er",
      "nicht jene große Kraft in sich hat ausbilden können, die gerade unter dem Eindruck der berechtigten Autorität her­anreift. Der Astralleib wird in dieser Zeit geboren, und langsam und allmählich hat in dieser Zeit vom vierzehnten Jahre ab das Urteil heranzureifen, das zum Bekenntnis führt. Das ist die Zeit, wo religiöse, moralische Empfindun­gen, wo künstlerische Errungenschaften in seinem Antlitz sich ausprägen. Dadurch kann er frei und als einzelnes Indi­viduum der Welt gegenübertreten. Das dauert bis zum ein­undzwanzigsten oder dreiundzwanzigsten Jahre.",
      "Es ist ein wichtiger Moment, wo mit der Geschlechtsreife der Mensch dem Menschen entgegentritt. Wie alles Ver­gängliche ein Gleichnis ist, so ist auch das Gegenübertreten des Männlichen und Weiblichen ein Symbolum. So wie die Liebe zum Einzelnen nach und nach erwacht, so erwachen jetzt überhaupt erst die persönlichen Verhältnisse zur Um­gebung; vorher sind es allgemein menschliche Verhältnisse. Eigenes Urteil und eigene Verhältnisse zur Umwelt treten erst jetzt auf. Da kommt im Astralen der Fond heraus, den der Mensch sich mitgebracht hat und der sich jetzt erst frei entwickeln kann. Alle hohen Ideale, alle schönen Lebens-hoffnungen und Lebenserwartungen, die nichts anderes sind als das, was im Astralleib als astraler Fond mitgebracht wird, sind Kräfte, die da sein müssen. Der Mensch ent­wickelt sich recht, der seine Lehrzeit so durchmacht, daß er das, was in ihm veranlagt ist, nach und nach herausbringt, nicht das, was in der Welt ist, sondern was er sich mitbringt. Ideale sind nicht da, sondern wir haben sie, weil die Kraft in uns rege ist, die in dieser Zeit jenes Hinausstreben des Jünglings macht; und nichts ist schlimmer für das spätere Leben, als wenn diese Kräfte bis zum zwanzigsten Jahre nicht da waren, die Lebenshoffnung und Lebenssehnsucht sind, denn das sind reale Kräfte. Je mehr wir von dem heutigen",
      "Fond des Inneren herauszubringen imstande sind, desto besser fördern wir den sich entwickelnden Menschen. Erst mit dem dreiundzwanzigsten Jahre ist das alles heraus­gebracht, und dann kann der Mensch seine Wanderjahre antreten. Da erst ist sein Ich geboren, da tritt er als eine freie Persönlichkeit frei der Welt gegenüber.",
      "Jetzt ist das, was sein Ich, seine vier Glieder sich zusam­mengearbeitet haben, in unmittelbarem Umgang mit der Welt. Jetzt wirkt ganz frei, ohne daß er ein Inneres erst noch ausgebildet braucht, die innere Lebenserfahrung des Menschen; jetzt erst ist er reif, der unmittelbaren Wirklich­keit gegenüberzutreten. Hat er das schon früher getan, so sind die schönsten Anlagen in ihm verdorben; er hat da die Kräfte ertötet, die er als Fond mitgebracht hat. Es ist eine Versündigung an der Jugend, wenn wir die Prosa des Le­bens früher wirken lassen. Jetzt reift der Mensch heran, und es kommt nun die Zeit, wo er so recht vom Leben ler­nen kann. Er entwickelt sich jetzt nach den sogenannten Meisterjahren hin, die in die Zeit vom achtundzwanzigsten bis zum fünfunddreißigsten Jahre fallen. Nehmen Sie aber den Zeitraum nicht zu pedantisch.",
      "Um das fünfunddreißigste Jahr herum, da liegt des Men­schen Lebensmitte, was alle Zeiten, die etwas gewußt haben von der Geisteswissenschaft, als etwas ungeheuer Wichtiges angesehen haben. Denn während bis zum einundzwanzig­sten Jahre der Mensch aus seinen drei Leibern herausgeholt hat, was in ihm veranlagt ist, und bis zum achtundzwan­zigsten Jahre aus der Umgebung herausgeholt hat, was sie ihm frei bieten konnte, beginnt er jetzt frei an seinen Lei­bern zu arbeiten, zuerst seinen astralen Teil zu festigen. Vorher hat er zu lernen gehabt aus der Umgebung und von der Umgebung; jetzt wird sein Urteil so, daß es eine gewisse Tragkraft bekommt für die Umgebung, und der Mensch",
      "tut wohl, wenn er vorher mit seinem Urteil über die Welt nicht zu stark abschließt. Erst gegen das fünfunddreißigste Jahr zu sollten wir unser Urteil verfestigen. Dann wird der Astralleib immer dichter und dichter. Haben wir bis dahin geübt, so dürfen wir jetzt ausübend werden. Jetzt fängt unser Urteil an, für die Umgebung etwas zu bedeuten. Jetzt, wo es heißt, mittun für die Welt, beginnt der Mensch sein Urteil in die Waagschale zu legen. Nun wird aus dem Wandernden ein Ratender, und nun können sich die andern nach ihm richten.",
      "Mit dem fünfunddreißigsten Jahre beginnt es, daß die Erfahrungen zu einer Art von Weisheit werden können. Mit dem fünfunddreißigsten Jahre ist der Zeitpunkt ein­getreten, der sich auch im physischen Leben dadurch kenn­zeichnet, daß der Astralleib und Ätherleib sich von der Welt zurückziehen. Bis zum einundzwangzigsten Jahre und dar­über hinaus wirkt der Astralleib im Ich, im Blut und Ner­vensystem. Da wirkt er wachsend, verfestigend, konsoli­dierend, der Mensch bekommt in dieser Beziehung eine gewisse Festigkeit. Was sich in seiner Gefühls- und Gedan­kenwelt richtig kristallisiert, das wird er in Einklang und zum Ausdruck bringen in Mut und Geistestätigkeit. Daher können wir diese Zeit auch die Zeit der Ausbildung des Blut- und Nervensystems nennen. Diese Zeit ist physisch abgeschlossen etwa gegen das fünfunddreißigste Jahr zu, wo sich der Ätherleib mehr zurückzieht von dem Wirken im äußeren physischen Leibe. Daher die Eigenart, daß von dieser Mitte an der Mensch allmählich aufhört, sich zu ver­größern; er konsolidiert sich, das Fett fängt an sich abzu­lagern, und die Muskeln gewinnen an Stärke. Das rührt aber nur davon her, daß der Ätherleib beginnt, sich zu­rückzuziehen. Daher werden auch die Kräfte des Äther-leibes frei, weil sie nicht mehr an dem physischen Leib zu",
      "arbeiten haben, und es gliedert sich zusammen mit dem, was der Mensch innerlich ausgebildet hat. Da wird der Mensch weise. Daher haben die Alten wohl gewußt, daß der Rat eines Menschen im öffentlichen Leben erst dann eine Bedeu­tung haben kann, wenn der Ätherleib sich zurückzieht vom physischen Leibe: dann kann er eintreten ins öffentliche Leben, und seine Anlagen haben für Staat und öffentliches Leben eine Bedeutung.",
      "Vom fünfunddreißigsten Jahre ab zieht sich der Mensch immer mehr und mehr ins Innere zurück. Wenn wir auf einen solchen Menschen hinsehen, wird er nicht mehr jene Jugenderwartung und jene Jugendsehnsucht haben; dafür aber hat er seine Urteile, etwas, von dem wir fühlen, daß es eine Kraft ist im öffentlichen Leben. Nun sehen wir auch, wie diejenigen Kräfte und Fähigkeiten, die an dem Äther-leib hängen, wie das Gedächtnis, abzunehmen beginnen. Und nun kommen wir in die Jahre hinein, etwa gegen fünf­zig, wo auch das physische Prinzip sich zurückzieht von dem Menschen, immer mehr und mehr Knochenerde ab­setzt, wo die Gewebe locker werden. Das physische Prinzip verbindet sich immer mehr mit dem Ätherprinzip, und das, was in Knochen, Muskeln, Blut und Nerven gegangen ist, fängt an, ein eigenes Leben zu entwickeln. Geistiger und Immer geistiger wird der Mensch. Allerdings muß das da­durch gefördert werden, daß die frühere Erziehung in rich­tiger Weise gelenkt worden ist. Da muß der Astralleib auch etwas gehabt haben. Hat der Astralleib keine Jugendfreu-den gehabt, dann ist das nicht in ihm, was sich jetzt in den dichteren Ätherleib einprägen soll. Und ist das nicht drin­nen, dann kann jenes mächtige Innenleben sich nicht ent­wickeln, und es muß das eintreten, was man das Kindisch-werden im Alter nennt. Jene, die in der Jugend nicht die frische Kraft bekommen haben, fangen an auszudorren.",
      "Es ist geradezu auch in geisteswissenschaftlicher Beziehung außerordentlich wichtig, das zu beobachten.",
      "Die günstigste Zeit für die Entfaltung spiritueller An­lagen ist die Zeit, wenn das fünfunddreißigste Jahr gekom­men ist. Da werden die Kräfte, die sonst in den Körper hineingehen, frei, man hat sie zur Verfügung und kann mit ihnen arbeiten. Es ist daher ein besonders günstiges kar­misches Geschick, wenn der Mensch nicht zu spät zur ok­kulten Entwicklung kommt. Solange der Mensch noch damit zu tun hat, seine Kräfte nach außen zu richten, solange kann er sie nicht nach innen richten. Daher muß der Zeitpunkt um das fünfunddreißigste Jahr herum als ein Kulminations-punkt angesehen werden. In der ersten Hälfte des Lebens hat sich alles schon zu einem rhythmischen Gang entwickelt, aber in der zweiten Hälfte sind die Grenzen nicht mehr so bestimmt, obwohl in der Geisteswissenschaft Grenzen im­mer angegeben worden sind, aber diese sind ungenau.",
      "Wir arbeiten da der Zukunft erst entgegen. Was der Mensch in der höheren Altersstufe in seinem Innern aus­bildet, wird in der Zukunft Organ- und Körper-schaffend sein; das wird auch im Welten-Kosmos später mitwirken. Es wird in der Zukunft etwas da sein, was wir an der ersten Hälfte jetzt schon beobachten können. Diese Einteilung hat vielleicht, namentlich für die Jugend, etwas Bedrückendes, aber wer die Lehren der Geisteswissenschaft wirklich in sich aufnimmt, kann das nicht mehr empfinden. Wenn Sie das Menschenleben von einem hohen Standpunkt aus über­schauen, werden Sie sehen, daß gerade durch eine solche Betrachtung des Lebenslaufes der Mensch zum richtigen Ge­brauch und zu der Praxis hingeführt wird. Der Mensch wird die Resignation üben müssen, zu warten, bis er die Organe hat, um in der ihnen entsprechenden Sphäre richtig zu wirken."
    ],
    "sentences": [
      [
        "Der alte Wahrspruch eines griechischen Mysterientempels: «Erkenne dich selbst» geht durch die Menschheit als eine Aufforderung zu der tiefsten menschlichen Betrachtungs­weise.",
        "Er stellt eine der größten Wahrheiten dar, aber es geht mit diesem Ausspruch wie mit allen eigentlichen gro­ßen Wahrheiten: Richtig verstanden, bedeuten sie etwas Universelles, etwas Gewaltiges.",
        "Aber nur allzu leicht kön­nen sie mißverstanden werden - und dieser insbesondere.",
        "Er ist niemals im ursprünglichen Sinne so gemeint gewesen, daß der Mensch sein alltägliches Selbst betrachten soll, auch niemals so, daß der Mensch die Summe alles Wissens in sich selber finden könne.",
        "Wenn wir ihn richtig verstehen, so bedeutet er eine Aufforderung, das Selbst. das höhere Selbst des Menschen zu erkennen."
      ],
      [
        "Wo ist das höhere Selbst des Menschen?"
      ],
      [
        "Wir können uns durch einen Vergleich klarmachen, wo dieses höhere Selbst ist und was dieser Spruch bedeutet.",
        "Gewiß, hätten wir nicht Augen, wir könnten unmöglich das Licht um uns herum wahrnehmen.",
        "Aber niemals - und das gilt als ebenso sicher - niemals könnten wir Augen haben, wenn nicht das den Raum durchflutende Sonnenlicht erst diese Augen geschaffen hätte.",
        "Aus ursprünglich niederen Organisationen, aus einem Lebewesen, das keine Augen hatte, das um sich nur Dunkles hatte, lockte geradezu das"
      ],
      [
        "Licht erst die Augen heraus.",
        "Darum ist es so tief begründet, was Goethe sagt: «Die Augen sind am Licht und für das Licht gebildet.» Aber die Augen sind nicht da, um sich selbst zu betrachten.",
        "Wollten wir vom Standpunkt der Augen sprechen, so müßten wir sagen: Die Augen erfüllen ihren Zweck um so besser, je mehr sie sich selbst vergessen und ihren Schöpfer - das Licht - erkennen.",
        "Der Mensch würde immer mehr die Mission der Augen erfüllen, wenn er hereinblicken könnte in dieses Augeninnere selbst.",
        "Dieses sogenannte Innere vergessen und gerade das, was das Innere geschaffen hat, das höhere Selbst des Auges, das Licht, er­kennen, das ist die Aufgabe, die Mission des Auges!",
        "Ähn­lich verhält es sich mit dem, was der Mensch das gewöhn­liche Selbst nennt.",
        "Auch das ist nichts anderes als Organ, Werkzeug, und die Selbsterkenntnis steigt um so höher, je mehr dieses Selbst des Menschen sich selbst vergessen kann, je mehr es gewahr wird, daß in der Außenwelt ebenso das Geisteslicht ist, das unsere geistigen Augen geschaffen hat und noch fortwährend schafft.",
        "Daher ist mit Selbsterkennt­nis, wenn sie richtig verstanden wird, Selbstentwicklung gemeint.",
        "Dies müssen wir im Hintergrunde sehen, wenn wir heute ein Thema - wichtig für den Menschen wie wenige - betrachten wollen: das Thema der Selbsterkennt­nis im höchsten Sinne des Wortes."
      ],
      [
        "Wir wollen den Menschen betrachten von der Geburt bis zum Tode, und wollen die ganze Wesenheit des Menschen dabei berücksichtigen.",
        "Dann müssen wir allerdings nicht vergessen, daß der Mensch bei Beginn seines physischen Daseins bereits etwas mitbringt, daß er uns nicht wie etwas Neugebildetes entgegentritt, sondern wie ein Wesen, das schon wiederholte Erdenleben hinter sich hat und in diesen Erdenleben sich den Grundcharakter seiner Individualität bereits geholt hat.",
        "Wollen wir verstehen, was der Mensch"
      ],
      [
        "bei seiner Geburt sich mitbringt, so müssen wir den Men­schen betrachten nach dem Tode.",
        "Denn daraus wird sich uns ergeben, was sich der Mensch durch den Zeitraum vom Tode bis zur neuen Geburt aufbewahrte, um es bei der neuen Geburt mitzubringen."
      ],
      [
        "Erinnern wir uns, was geschieht, wenn der Mensch stirbt:"
      ],
      [
        "er hinterläßt den physischen Leichnam.",
        "Der wesentliche Unterschied zwischen Tod und Schlaf ist der, daß der Mensch im Schlafe im Bette liegen hat den physischen und den Ätherleib, und daß nur herausgeholt ist der Astralleib und das, was wir das Ich nennen."
      ],
      [
        "Ebenso wie die Ziegel­steine nicht von selbst zum Palast zusammenlaufen, so brauchen die physischen Kräfte den Ätherleib als inneren Architekten.",
        "Er ist mit dem Menschen verbunden und er­hält von der Geburt bis zum Tode den Zusammenhang der physischen Stoffe und Kräfte; er rettet jeden Augenblick die chemische Mischung vor dem Verfall."
      ],
      [
        "Im Tode hebt er sich jetzt wirklich heraus, und daher bleibt der physische Teil als der verfallende Leichnam zurück.",
        "Im Schlafe also geht nur der Astralleib, als der Träger von Lust und Leid, Begierden und Affekten, und dazu das Ich aus dem physi­schen Leib heraus; im Tode trennt sich nun noch der Ä ther­leib heraus und ist eine Weile mit dem Astralleib und dem Ich zusammen."
      ],
      [
        "Dies ist ein wichtiger Augenblick im Dasein des Menschen.",
        "In diesem Augenblick geht an der mensch­lichen Seele blitzschnell die Erinnerung an das ganze bis­herige Erdenleben vorüber, von der Geburt bis zum Tode, wie ein großes Tableau."
      ],
      [
        "Dieses Tableau stellt sich wie ein Gemälde dar.",
        "Alles, was uns mit Lust und Leid verknüpft hat, das empfinden wir in diesem Augenblicke nicht.",
        "Wie wir bei einem Gemälde nicht den Dolchstich fühlen, so füh­len wir auch dabei nicht all den Schmerz und all das Leid, die Lust oder Freude, die da an uns vorübergleiten."
      ],
      [
        "objektive Betrachter stehen wir da dem verflossenen Leben gegenüber."
      ],
      [
        "Dann kommt der Zeitpunkt, wo sich auch der Äther-leib herauszieht und auflöst im allgemeinen die Welt durch­flutenden Weltenäther.",
        "Aber etwas bleibt da von dem Äther-leib zurück: das ist eine Art Auszug aus dem ganzen bisherigen Leben.",
        "Das Tableau verliert sich und löst sich auf; aber wie wenn wir in einemBuche einen kurzen Auszug machen, so bleibt hier durch die ganzen folgenden Wege mit dem Menschen etwas wie eine Art Essenz vereinigt.",
        "Zu gleicher Zeit müssen wir uns eines klarmachen: Neben dieser Essenz vom Ätherleib bleibt, wenn auch wenig, nur gleich­sam ein Kraftpunkt, auch eine Essenz von dem physischen Leibe des Menschen zurück; selbstverständlich nicht so, daß ihn ein physisches Auge sehen kann, sondern wie ein Kraft-zentrum.",
        "Das ist mit dem Lebensleib ebenfalls verbunden, und das gibt dem physischen Leibe gerade die menschliche Form.",
        "Dann geht der Mensch durch einen Zustand durch, in dem er sich allmählich den Zusammenhang mit der phy­sischen Welt abgewöhnt."
      ],
      [
        "Jetzt ist nach dem Tode noch der Astralleib des Men­schen da.",
        "Um uns klarzumachen, welches Leben jetzt der Astralleib führt, stellen wir uns vor: alles, was der Mensch auch an den niedrigsten Genüssen erlebt, bleibt an seinem Astralleib haften.",
        "Der physische Leib fühlt nicht die Freude und hat keine Begierden; er ist das Werkzeug des Astral­leibes, und der hat daran seine Freude und seinen Genuß.",
        "Wenn wir zum Beispiel einen Feinschmecker vor uns haben, so hat nicht sein physischer Leib Genuß an den Genuß-mitteln, sondern der Astralleib empfindet ihn, indem er sich des physischen Werkzeuges zum Genuß bedient.",
        "Die Sucht zu genießen bleibt auch, wenn er den physischen Leib ab­gelegt hat; nur die Werkzeuge fehlen jetzt.",
        "Daraus ersehen"
      ],
      [
        "Sie die Natur des Astralleibes, wie der jetzt nach dem Tode lebt.",
        "Es ist so, wie wenn Sie durch eine Gegend gehen, lech­zend vor Durst, aber diesen Durst nicht befriedigen können, weil weit und breit keine Quelle ist.",
        "In ähnlicher Weise empfindet der Astralleib aus einem guten Grunde Begier­den, Genußsucht, Affekte, die er früher gehabt hat, als einen brennenden Durst - nicht weil die Dinge nicht da sind, sondern weil ihm die Organe fehlen, um den Genuß zu befriedigen.",
        "Gerade deshalb haben die Religionen die Feuer­qualen, die der Mensch nach dem Tode zu bestehen hat, als Beispiel dafür hingestellt."
      ],
      [
        "Bis sich der Astralleib seinen Zusammenhang mit dem physischen Leibe abgewöhnt hat, bleibt er im Kamaloka, wo sich der Astralleib nach und nach freimachen muß von dem, was ihm zugeströmt ist, während er den physischen Leib hatte.",
        "Ein Mensch, der schon in diesem Leben seine Affekte geläutert hat, der nicht mehr an den rohen Genüs­sen der Nahrungsmittel, sondern an dem Schönen, der Kunst oder an der Geistigkeit seinen Gefallen findet, wird sich sein Kamaloka abkürzen; ein Mensch, der sich aber nur befriedigen kann durch die Anwendung dessen, was ihm die physischen Werkzeuge geben können, wird lange in der Sphäre des brennenden Durstes leben, und dieser Zustand endet damit, daß alles, was der Mensch in seinem Astralleib noch nicht vergeistigt hat, wie eine Art von Leichnam vom Astralleib abfällt, so wie der Ätherleib und der physische Leib abgefallen sind, und um so mehr abfallen muß, je weniger er seinen Astralleib geläutert und gereinigt hat.",
        "Daher wird später eine geläuterte Natur viel mitnehmen von ihrem Astralleib und zu dem hinzufügen, was wir die Essenz des physischen und Ätherleibes nannten."
      ],
      [
        "Mit diesen drei Essenzen geht das Ich nun ein in die eigentliche geistige Welt, und in dieser geistigen Welt hat"
      ],
      [
        "das Ich auszubilden alles, was es hier während dieses Lebens erlebt und erworben hat.",
        "Sie brauchen nur daran zu denken, daß der eine schon mit großen Anlagen in das Leben hin­einkommt, als ganz junges Kind Anlagen hat, die wir nur herauszuholen brauchen.",
        "Die hat er, weil er während des Aufenthaltes im Geistesland seine Erfahrungen ausgebildet hat, die zu Fähigkeiten und Anlagen während dieser Zeit umgewandelt worden sind."
      ],
      [
        "Im Laufe eines jeden Erdenlebens bringt der Mensch etwas Neues hinzu zu den drei Essenzen seiner Leiber.",
        "Ein Mensch, der als ein besonders begabter Mensch geboren wird, hat seine früheren Leben gut angewendet, hat in sei­nem verflossenen Leben viele Blätter wie zu einem Buche zusammengelegt, und darin stehen die Erfahrungen und Errungenschaften seiner früheren Erdenleben.",
        "Damit tritt der Mensch in ein neues Leben ein und erhält einen physi­schen Leib von seinen physischen Vorfahren.",
        "Dieser Wesens-kern, der sich aus den früheren Erlebnissen die Früchte mitbringt, wird zu der Familie hingezogen, die ihm die phy­sischen Merkmale geben kann, die ihn befähigen, seine indi­viduellen Anlagen, die er sich früher erworben hat, zu gebrauchen.",
        "Nicht sind es die Vererbungsmerkmale, die des Menschen Handeln und Fähigkeiten ausmachen, die liefern nur die Werkzeuge; aber die Werkzeuge müssen da sein.",
        "Wie der Klaviervirtuose ein Instrument, so muß die Indi­vidualität, wenn sie von einem neuen physischen Leib um­hüllt wird, in diesem die richtigen Werkzeuge finden, um sich in der physischen Welt in der richtigen Weise zum Ausdruck bringen zu können.",
        "Daher die Täuschung, als ob nur physische Vererbung vorliegt.",
        "Gewiß liegt sie vor, aber nur weil die Individualität sich zu den Eltern hingezogen fühlt, die ihr die geeigneten Werkzeuge geben können.",
        "Alles, von dem wir gesagt haben, daß es im Laufe der Zeit"
      ],
      [
        "abgeworfen worden ist, muß sich in derselben Weise wieder um den Menschen herum kristallisieren; alles das erhält der Mensch wiederum neu, damit er im weiteren Leben von neuem zur Läuterung seiner Wesenheit beitragen kann."
      ],
      [
        "Für die erste Hälfte des menschlichen Lebens haben wir schon die Bausteine zusammengetragen.",
        "Wir werden nun etwas zu wiederholen haben aus dem Bereich der Erzie­hungs- und Schulfragen, werden das für den zweiten Teil des menschlichen Lebenslaufes weiter auszubauen haben, um zu sehen, wie der physische, ätherische und astralische Leib im ersten Teil des menschlichen Lebenslaufes sich ent­wickeln, und wie Glück und Inhalt des Menschenlebens da­von abhängen.",
        "Dies ist ein wichtiges Kapitel, das wir aller­dings so auffassen müssen, daß es große Gesetze hinstellt, die vielfach Abänderung erfahren, aber in großen Umrissen gilt es.",
        "Und nur wer die Gesetze kennt und sie immer zu beachten versteht, wird sich in der richtigen Weise in den Lebenslauf einfügen, wird seiner Bestimmung immer klarer und klarer entgegengehen können."
      ],
      [
        "Beginnen wir bei des Menschen Geburt.",
        "Wir haben schon davon gesprochen, daß bei der physischen Geburt eigentlich erst sein physischer Leib völlig geboren wird, der bis dahin von der physischen Mutterhülle umgeben wurde.",
        "Da haben sich alle Organe nur dadurch entwickelt, daß der Mensch bis zur physischen Geburt gegen alle Seiten hin geschützt ist.",
        "Und nun ist es, wie wenn der Mensch die physische Mut­terhülle zurückstößt und sein physischer Leib jetzt allein erst den Wirkungen der physischen Elemente ausgesetzt ist.",
        "Nach dieser Geburt ist der Ätherleib noch nicht und noch weniger der Astralleib geboren; diese sind noch eingehüllt von einer Äther- und von einer astralen Hülle.",
        "Wie eine Schale, die nur für das geistige Auge des Sehers sichtbar ist, umgibt eine astrale und eine ätherische Hülle den Menschen,"
      ],
      [
        "die nicht seiner eigenen Natur angehören, die ihn schützen und einhüllen.",
        "Die Ätherhülle umgibt den Menschen bis zum siebenten Jahre, der Zeit des Zahnwechsels.",
        "Da erst wird der Ätherleib geboren; da erst wird die Ätherhülle zurückgedrängt, wie die physische Hülle bei der physischen Geburt; und mit der Geschlechtsreife wird erst der Astral­leib der äußeren Welt vollständig ausgesetzt."
      ],
      [
        "Wir müssen uns klarmachen, daß in den ersten sieben Jahren des Lebens nur jene Essenz, die wir die Essenz des physischen Leibes nannten, vollständig frei wirkt, daß sie die physische Form gibt; sie leitet die physische Struktur ein.",
        "Die Organe wachsen in der Außenwelt heran, so daß sie ihre Form, ihre Anlage haben und nur noch weiterwach­sen brauchen.",
        "Wir müssen daher alles in seine Umgebung bringen, was die Struktur des physischen Leibes in der allerbesten Weise entfalten kann.",
        "Dafür konnten wir zwei Zauberworte anführen: Nachahmung und Beispiel oder Vor­bild.",
        "Alles, was um das Kind herum ist, wird von ihm nach­geahmt, und diese Nachahmung lockt die inneren Organe zu ihrer Form.",
        "Wenn auch das Gehirn mit dem siebenten Jahre noch sehr unvollkommen ist, die Richtung hat es doch erhalten, und was ihm bis dahin vorenthalten ist, kann es später nicht mehr nachholen.",
        "In den Zähnen macht das phy­sische Prinzip gleichsam Schlußpunkt, denn es ist das Prin­zip des Gestaltens, des Formens.",
        "So wie die Zähne am anschaulichsten zeigen, daß die Glieder sich konsolidiert haben, so sind auch die anderen weicheren Organe bestimmt.",
        "Das Licht wirkt und lockt die Kraft des Auges an die Ober­fläche.",
        "Wir haben erwähnt, daß es gut ist, dem Kinde mög­lichst nicht fertige Puppen und derartiges zu geben, wir haben erwähnt, daß ein gesundes Kind nur für eine kurze Zeit Freude daran findet.",
        "Dagegen hat es seine Freude daran, wenn Sie eine Serviette zusammenbinden und mit"
      ],
      [
        "Tintenklecksen Augen und Ohren machen und ihm als Spielzeug geben.",
        "Wie ein Muskel nur stark wird, wenn er angewendet wird, so ist es auch hier: jetzt muß das Kind arbeiten und das in der Phantasie aufbauen, was die Puppe nicht hat.",
        "Da wird der innere organische Aufbau bewirkt.",
        "Es ist daher von besonderer Bedeutung, daß man das Kind innerlich arbeiten läßt, in seine Umgebung das bringt, was die Organe durchströmt mit Freude und Lust und Genuß an der Umgebung.",
        "Das schafft Kraft für die Bildung der Or­gane.",
        "Durch nichts kann man die Organe mehr ruinieren, als wenn man dem Kinde nicht das Richtige zuführt.",
        "Die Phan­tasie, die in ihm tätig ist, arbeitet an den Formen seiner Organe, und nichts wäre verfehlter, als durch eine falsche Askese das Kind an ein lustloses Dasein gewöhnen zu wol­len.",
        "Freude ist der Praktiker in den ersten Lebensjahren, und die gesunden Lebensinstinkte sind die Bildner, die man nur nicht verderben soll.",
        "Die richtige Nahrung, dem Kinde ge­reicht, wird bewirken, daß das Kind Lust an der Ernährung bekommt, die ihm frommt; falsche Nahrung wird das Kind krank machen.",
        "Für jede Stufe, für alles weiß die Geistes­wissenschaft da die nötigen Dinge.",
        "So müssen wir uns dar­über klar sein, daß in den ersten sieben Jahren das Gattungs­gemäße vorzugsweise herauskommt, denn das physische Prinzip arbeitet an dem Menschen, und ungestört müssen wir das Kind arbeiten lassen."
      ],
      [
        "Bei der Ernährungsfrage tritt ein innerlicher Zusammen­hang hervor zwischen der Muttermilch und dem Kinde, der sich dadurch ausdrückt, daß in den ersten Lebensjahren geradezu ein geistiges Verhältnis zwischen der Mutter und dem Kinde besteht; und eine Mutter, die ihr Kind selbst nährt, beachtet das.",
        "In der Muttermilch ist nicht bloß das, was physisch und chemisch ist, es ist etwas, was geistig ver­wandt ist mit dem Kinde.",
        "Der Geisteswissenschafter sieht"
      ],
      [
        "da etwas, was aus dem Ätherleib der Mutter herausgeboren ist, und weil der Ätherleib des Kindes noch ungeboren ist, so verträgt er in der ersten Zeit insbesondere nur das, was schon durch einen anderen Ätherleib zubereitet ist.",
        "Es be­steht ein inniger Kontakt zwischen dem, was das Kind braucht, und dem, was ihm die Mutter selbst reicht.",
        "Pro­zentual betrachtet: Etwa 16 bis 20 Prozent derjenigen Kin­der, die im Säuglingsalter sterben, sind solche, die von der eigenen Mutter genährt werden; dagegen 26 bis 30 Prozent solche, die von Fremden genährt werden.",
        "Darin sehen Sie den Zusammenhang zwischen den Lebensleibern.",
        "Es ist eine Art Charakter, der sich in den ersten Lebensjahren physisch zum Ausdruck bringt; das mehr Gattungsmäßige bildet sich heraus, konsolidiert sich, wird fest, gibt ihm den Charakter, durch den es einem bestimmten Geschlecht angehört.",
        "Die Familienzüge prägen sich erst von dieser Zeit an auf seinem Antlitz aus."
      ],
      [
        "Die Zeit vom siebenten bis zum vierzehnten Jahre ist die, für welche wir schon die beiden Zauberworte «Nach­eiferung» und «Autorität» angeführt haben.",
        "Der Mensch braucht in dieser Zeit einen andern Menschen, der für ihn die Verkörperung alles Guten, Schönen und Weisen ist; er braucht einen Menschen überhaupt, in dem er die Grund­sätze und Lehren verleiblicht sieht.",
        "Mit Moralpredigen ist in dieser Zeit viel weniger getan, als wenn Sie dem Kinde Vorbilder anführen, die dem Kinde den Weg hinauf zum Olymp zeigen.",
        "Für die ganze spätere Zeit ist es für den Menschen von Bedeutung, wenn er jetzt einen Menschen über sich sieht, vor dem er eine tiefe Achtung hat.",
        "Selbst­verständliche Nachfolge ist es, um die es sich da handelt.",
        "Daher müssen wir den Geschichtsunterricht so einrichten, daß wir die Weisheit und verkörperte Charakterstärke dem Kinde im Bilde vor Augen führen; und vom Art-Charakter"
      ],
      [
        "geht er über mehr zu einem Spezial-Charakter, was nicht mehr mit der Vorfahrenreihe zusammenhängt.",
        "Aus der Nachahmung der Eltern wird die Nachahmung der fremden Art.",
        "Der Gesichtskreis erweitert sich über das Familienhafte hinaus; wir müssen Menschen in die Nähe des Kindes brin­gen, damit der Ätherleib sich weiter ausbreiten kann über das Artgemäße hinaus."
      ],
      [
        "Während bis zum Zahnwechsel das sich ausprägt, was den Menschen in die Familie hineinstellt, bekommen die Gesten jetzt ihren Charakter; das, was den Menschen zu einem besonderen Menschen macht, prägt sich aus, wenn der Mensch heraustritt aus dem Kreise der Fa­milie.",
        "Denn jetzt ist die Ätherhülle zerschlagen, nun kann auf den Ätherleib gewirkt werden, wenn in des Kindes Umgebung solche Menschen sind, die durch das, was sie in sich selber tragen, solche Eigenschaften ausbilden können, die im Ätherleib des Kindes aufgespeichert liegen."
      ],
      [
        "Und jene Grundanlagen, die der Mensch als Früchte seiner früheren Inkarnation in seinem Ätherleib mitgenommen hatte, ent­wickeln sich jetzt, wo nach dem siebenten Jahre der Äther-leib nach allen Seiten frei ist.",
        "Daher muß der Erzieher wo­möglich etwas zurücktreten und nicht darauf pochen: dies sind die richtigen Erziehungsgrundsätze, sondern auf das sehen, was das Kind mitgebracht hat; denn jetzt müssen durch den freigewordenen Ätherleib nach allen Seiten die Organe erstarken und sich vergrößern."
      ],
      [
        "Während bis zum siebenten Jahre die physischen Organe durch physische Kräfte ausgearbeitet und plastisch gestaltet wurden, haben wir jetzt diese sich vergrößernden Organe, um Gewissen, Moral, Tatkraft, all die ätherischen Eigenschaften da hin­einzuarbeiten.",
        "Alles, was bildhaft ist, was mit der reineren geistigen Freude an der Natur zusammenhängt, müssen wir hineinprägen, denn das muß so fest im Menschen sitzen, daß es im Ätherleib haftet: Einen festen Charakter kann"
      ],
      [
        "der Mensch nur haben, wenn er so seinen Ätherleib frei ent­wickeln kann.",
        "Und ein Erzieher muß sich in dieser Zeit sagen: Du hast es nicht zu tun mit etwas, das du formen kannst, so wie du willst; sondern du kannst da etwas für das ganze Leben verderben, wenn du nicht erlauschest, was aus dem früheren Ätherleib herübergekommen ist.",
        "Daher müssen auch die physischen Ubungen so ausgedacht sein, daß in dem Kinde das Gefühl des Erstarkens, des Vermehrt­werdens lebt.",
        "«Ich werde größer», «ich wachse», muß eine moralische, nicht bloß physische Empfindung im Kinde sein.",
        "Das arbeitet ebenso plastisch am Ätherleib wie das physische Prinzip am physischen Leibe."
      ],
      [
        "Und in derselben Weise wie, während die physische Mut­terhülle den physischen Leib umgibt, die physischen Organe sich ausbilden, so umgibt die Astralhülle noch die astralen Eigenschaften, die der Mensch sich mitbringt; die bilden sich zunächst in der astralischen Hülle, und erst mit der Ge­schlechtsreife tritt der Mensch der Welt mit einem freien Astralleib entgegen.",
        "Jetzt erst kann Urteil, Kritik und Be­griffsbildung hineingreifen.",
        "In einem früheren Lebensalter würde ihm das viel zu früh gegeben werden.",
        "Der Mensch sollte in einem früheren Lebensjahre noch kein Bekenntnis haben, denn das kann er sich erst bilden, wenn sein Astral­leib geboren ist.",
        "Vorher soll er aufschauen zu den Bekennern und von ihnen entgegennehmen, was er glauben soll; denn in diesem Zeitalter sich das selbst bestimmen, gibt eine astrale Karikatur.",
        "Vom okkulten Standpunkt ist es unmög­lich, wenn der junge Mensch veranlaßt wird, schon irgend­ein Bekenntnis zu haben.",
        "Es ist sinnlos und ist entwick­lungswidrig, wenn ein Kind in diesem Lebensalter es für möglich hält zu sagen: Ich habe ein eigenes Glaubensbe­kenntnis.",
        "Das wäre ein Zeichen, daß etwas in der Erziehung des betreffenden Menschen versäumt worden ist; daß er"
      ],
      [
        "nicht jene große Kraft in sich hat ausbilden können, die gerade unter dem Eindruck der berechtigten Autorität her­anreift.",
        "Der Astralleib wird in dieser Zeit geboren, und langsam und allmählich hat in dieser Zeit vom vierzehnten Jahre ab das Urteil heranzureifen, das zum Bekenntnis führt.",
        "Das ist die Zeit, wo religiöse, moralische Empfindun­gen, wo künstlerische Errungenschaften in seinem Antlitz sich ausprägen.",
        "Dadurch kann er frei und als einzelnes Indi­viduum der Welt gegenübertreten.",
        "Das dauert bis zum ein­undzwanzigsten oder dreiundzwanzigsten Jahre."
      ],
      [
        "Es ist ein wichtiger Moment, wo mit der Geschlechtsreife der Mensch dem Menschen entgegentritt.",
        "Wie alles Ver­gängliche ein Gleichnis ist, so ist auch das Gegenübertreten des Männlichen und Weiblichen ein Symbolum.",
        "So wie die Liebe zum Einzelnen nach und nach erwacht, so erwachen jetzt überhaupt erst die persönlichen Verhältnisse zur Um­gebung; vorher sind es allgemein menschliche Verhältnisse.",
        "Eigenes Urteil und eigene Verhältnisse zur Umwelt treten erst jetzt auf.",
        "Da kommt im Astralen der Fond heraus, den der Mensch sich mitgebracht hat und der sich jetzt erst frei entwickeln kann.",
        "Alle hohen Ideale, alle schönen Lebens-hoffnungen und Lebenserwartungen, die nichts anderes sind als das, was im Astralleib als astraler Fond mitgebracht wird, sind Kräfte, die da sein müssen.",
        "Der Mensch ent­wickelt sich recht, der seine Lehrzeit so durchmacht, daß er das, was in ihm veranlagt ist, nach und nach herausbringt, nicht das, was in der Welt ist, sondern was er sich mitbringt.",
        "Ideale sind nicht da, sondern wir haben sie, weil die Kraft in uns rege ist, die in dieser Zeit jenes Hinausstreben des Jünglings macht; und nichts ist schlimmer für das spätere Leben, als wenn diese Kräfte bis zum zwanzigsten Jahre nicht da waren, die Lebenshoffnung und Lebenssehnsucht sind, denn das sind reale Kräfte.",
        "Je mehr wir von dem heutigen"
      ],
      [
        "Fond des Inneren herauszubringen imstande sind, desto besser fördern wir den sich entwickelnden Menschen.",
        "Erst mit dem dreiundzwanzigsten Jahre ist das alles heraus­gebracht, und dann kann der Mensch seine Wanderjahre antreten.",
        "Da erst ist sein Ich geboren, da tritt er als eine freie Persönlichkeit frei der Welt gegenüber."
      ],
      [
        "Jetzt ist das, was sein Ich, seine vier Glieder sich zusam­mengearbeitet haben, in unmittelbarem Umgang mit der Welt.",
        "Jetzt wirkt ganz frei, ohne daß er ein Inneres erst noch ausgebildet braucht, die innere Lebenserfahrung des Menschen; jetzt erst ist er reif, der unmittelbaren Wirklich­keit gegenüberzutreten.",
        "Hat er das schon früher getan, so sind die schönsten Anlagen in ihm verdorben; er hat da die Kräfte ertötet, die er als Fond mitgebracht hat.",
        "Es ist eine Versündigung an der Jugend, wenn wir die Prosa des Le­bens früher wirken lassen.",
        "Jetzt reift der Mensch heran, und es kommt nun die Zeit, wo er so recht vom Leben ler­nen kann.",
        "Er entwickelt sich jetzt nach den sogenannten Meisterjahren hin, die in die Zeit vom achtundzwanzigsten bis zum fünfunddreißigsten Jahre fallen.",
        "Nehmen Sie aber den Zeitraum nicht zu pedantisch."
      ],
      [
        "Um das fünfunddreißigste Jahr herum, da liegt des Men­schen Lebensmitte, was alle Zeiten, die etwas gewußt haben von der Geisteswissenschaft, als etwas ungeheuer Wichtiges angesehen haben.",
        "Denn während bis zum einundzwanzig­sten Jahre der Mensch aus seinen drei Leibern herausgeholt hat, was in ihm veranlagt ist, und bis zum achtundzwan­zigsten Jahre aus der Umgebung herausgeholt hat, was sie ihm frei bieten konnte, beginnt er jetzt frei an seinen Lei­bern zu arbeiten, zuerst seinen astralen Teil zu festigen.",
        "Vorher hat er zu lernen gehabt aus der Umgebung und von der Umgebung; jetzt wird sein Urteil so, daß es eine gewisse Tragkraft bekommt für die Umgebung, und der Mensch"
      ],
      [
        "tut wohl, wenn er vorher mit seinem Urteil über die Welt nicht zu stark abschließt.",
        "Erst gegen das fünfunddreißigste Jahr zu sollten wir unser Urteil verfestigen.",
        "Dann wird der Astralleib immer dichter und dichter.",
        "Haben wir bis dahin geübt, so dürfen wir jetzt ausübend werden.",
        "Jetzt fängt unser Urteil an, für die Umgebung etwas zu bedeuten.",
        "Jetzt, wo es heißt, mittun für die Welt, beginnt der Mensch sein Urteil in die Waagschale zu legen.",
        "Nun wird aus dem Wandernden ein Ratender, und nun können sich die andern nach ihm richten."
      ],
      [
        "Mit dem fünfunddreißigsten Jahre beginnt es, daß die Erfahrungen zu einer Art von Weisheit werden können.",
        "Mit dem fünfunddreißigsten Jahre ist der Zeitpunkt ein­getreten, der sich auch im physischen Leben dadurch kenn­zeichnet, daß der Astralleib und Ätherleib sich von der Welt zurückziehen.",
        "Bis zum einundzwangzigsten Jahre und dar­über hinaus wirkt der Astralleib im Ich, im Blut und Ner­vensystem.",
        "Da wirkt er wachsend, verfestigend, konsoli­dierend, der Mensch bekommt in dieser Beziehung eine gewisse Festigkeit.",
        "Was sich in seiner Gefühls- und Gedan­kenwelt richtig kristallisiert, das wird er in Einklang und zum Ausdruck bringen in Mut und Geistestätigkeit.",
        "Daher können wir diese Zeit auch die Zeit der Ausbildung des Blut- und Nervensystems nennen.",
        "Diese Zeit ist physisch abgeschlossen etwa gegen das fünfunddreißigste Jahr zu, wo sich der Ätherleib mehr zurückzieht von dem Wirken im äußeren physischen Leibe.",
        "Daher die Eigenart, daß von dieser Mitte an der Mensch allmählich aufhört, sich zu ver­größern; er konsolidiert sich, das Fett fängt an sich abzu­lagern, und die Muskeln gewinnen an Stärke.",
        "Das rührt aber nur davon her, daß der Ätherleib beginnt, sich zu­rückzuziehen.",
        "Daher werden auch die Kräfte des Äther-leibes frei, weil sie nicht mehr an dem physischen Leib zu"
      ],
      [
        "arbeiten haben, und es gliedert sich zusammen mit dem, was der Mensch innerlich ausgebildet hat.",
        "Da wird der Mensch weise.",
        "Daher haben die Alten wohl gewußt, daß der Rat eines Menschen im öffentlichen Leben erst dann eine Bedeu­tung haben kann, wenn der Ätherleib sich zurückzieht vom physischen Leibe: dann kann er eintreten ins öffentliche Leben, und seine Anlagen haben für Staat und öffentliches Leben eine Bedeutung."
      ],
      [
        "Vom fünfunddreißigsten Jahre ab zieht sich der Mensch immer mehr und mehr ins Innere zurück.",
        "Wenn wir auf einen solchen Menschen hinsehen, wird er nicht mehr jene Jugenderwartung und jene Jugendsehnsucht haben; dafür aber hat er seine Urteile, etwas, von dem wir fühlen, daß es eine Kraft ist im öffentlichen Leben.",
        "Nun sehen wir auch, wie diejenigen Kräfte und Fähigkeiten, die an dem Äther-leib hängen, wie das Gedächtnis, abzunehmen beginnen.",
        "Und nun kommen wir in die Jahre hinein, etwa gegen fünf­zig, wo auch das physische Prinzip sich zurückzieht von dem Menschen, immer mehr und mehr Knochenerde ab­setzt, wo die Gewebe locker werden.",
        "Das physische Prinzip verbindet sich immer mehr mit dem Ätherprinzip, und das, was in Knochen, Muskeln, Blut und Nerven gegangen ist, fängt an, ein eigenes Leben zu entwickeln.",
        "Geistiger und Immer geistiger wird der Mensch.",
        "Allerdings muß das da­durch gefördert werden, daß die frühere Erziehung in rich­tiger Weise gelenkt worden ist.",
        "Da muß der Astralleib auch etwas gehabt haben.",
        "Hat der Astralleib keine Jugendfreu-den gehabt, dann ist das nicht in ihm, was sich jetzt in den dichteren Ätherleib einprägen soll.",
        "Und ist das nicht drin­nen, dann kann jenes mächtige Innenleben sich nicht ent­wickeln, und es muß das eintreten, was man das Kindisch-werden im Alter nennt.",
        "Jene, die in der Jugend nicht die frische Kraft bekommen haben, fangen an auszudorren."
      ],
      [
        "Es ist geradezu auch in geisteswissenschaftlicher Beziehung außerordentlich wichtig, das zu beobachten."
      ],
      [
        "Die günstigste Zeit für die Entfaltung spiritueller An­lagen ist die Zeit, wenn das fünfunddreißigste Jahr gekom­men ist.",
        "Da werden die Kräfte, die sonst in den Körper hineingehen, frei, man hat sie zur Verfügung und kann mit ihnen arbeiten.",
        "Es ist daher ein besonders günstiges kar­misches Geschick, wenn der Mensch nicht zu spät zur ok­kulten Entwicklung kommt.",
        "Solange der Mensch noch damit zu tun hat, seine Kräfte nach außen zu richten, solange kann er sie nicht nach innen richten.",
        "Daher muß der Zeitpunkt um das fünfunddreißigste Jahr herum als ein Kulminations-punkt angesehen werden.",
        "In der ersten Hälfte des Lebens hat sich alles schon zu einem rhythmischen Gang entwickelt, aber in der zweiten Hälfte sind die Grenzen nicht mehr so bestimmt, obwohl in der Geisteswissenschaft Grenzen im­mer angegeben worden sind, aber diese sind ungenau."
      ],
      [
        "Wir arbeiten da der Zukunft erst entgegen.",
        "Was der Mensch in der höheren Altersstufe in seinem Innern aus­bildet, wird in der Zukunft Organ- und Körper-schaffend sein; das wird auch im Welten-Kosmos später mitwirken.",
        "Es wird in der Zukunft etwas da sein, was wir an der ersten Hälfte jetzt schon beobachten können.",
        "Diese Einteilung hat vielleicht, namentlich für die Jugend, etwas Bedrückendes, aber wer die Lehren der Geisteswissenschaft wirklich in sich aufnimmt, kann das nicht mehr empfinden.",
        "Wenn Sie das Menschenleben von einem hohen Standpunkt aus über­schauen, werden Sie sehen, daß gerade durch eine solche Betrachtung des Lebenslaufes der Mensch zum richtigen Ge­brauch und zu der Praxis hingeführt wird.",
        "Der Mensch wird die Resignation üben müssen, zu warten, bis er die Organe hat, um in der ihnen entsprechenden Sphäre richtig zu wirken."
      ]
    ]
  },
  {
    "order": 12,
    "title_de": "WER SIND DIE ROSENKREUZER? Berlin, 14. März 1907",
    "paragraphs": [
      "Mit den Rosenkreuzern, die uns heute beschäftigen sollen, können in unserer Zeit die wenigsten Menschen einen Be­griff verbinden, welcher der Sache auch nur einigermaßen entspricht. Es ist allerdings nicht so leicht, mit dem Namen Rosenkreuzer irgendeinen besonderen Begriff zu verbinden. Etwas Unbestimmtes scheint für viele Menschen hinter die­sem Namen zu liegen. Wenn dann der eine oder der andere in kulturhistorischen oder sonstigen Büchern nachsieht, in denen man gewohnt ist, sich über solche Sachen Rat zu holen, so findet er allerdings einige Dinge darüber gesagt, zum Bei­spiel, daß die Rosenkreuzer eine Sekte oder dergleichen in den früheren Jahrhunderten deutscher Geistesentwicklung waren. Er findet auf der einen Seite von einigen hervor­gehoben, daß man nicht richtig dahinterkommen könne, ob hinter dem vielen Schwindel und der Charlatanerie, welche sich einmal unter dem Namen des Rosenkreuzertums breit­gemacht haben, auch irgend einmal etwas Vernünftiges und Klares gesteckt haben mag. Und auf der anderen Seite fin­det er dann auch allerlei Mitteilungen in gelehrten Büchern.",
      "Man muß in der Tat sagen, wenn das stimmen würde, was in der einschlägigen Literatur über die Rosenkreuzer geschrieben ist, dann könnte man so ziemlich damit einver­standen sein, daß das, was sich hinter diesem Namen ver­birgt, für eitle Windbeutelei, reinen Schwindel und viel­leicht noch viel Schlimmeres zu halten ist. Und auch jene, die noch versuchen, das Rosenkreuzertum zu verteidigen,",
      "entweder von oben herab oder vielleicht auch, indem sie be­merklich machen, daß sie über ein besonderes Wissen ver­fügen oder Aufschlüsse zu geben in der Lage sind, erwecken bei unseren Zeitgenossen und unseren Anschauungen kein besonderes Vertrauen. Allzuviel kommt auch bei der Ver­teidigung der Rosenkreuzer nicht heraus; insbesondere dann nicht, wenn gesagt wird: Gewiß, das Rosenkreuzertum wird in Zusammenhang gebracht mit Alchemie, mit der Bereitung des Steines der Weisen und allerlei sonstigen alchemistischen Kunststücken. Aber diese Kunststücke bedeuten dem echten, wahren Rosenkreuzer nichts als ein Sinnbild für die innere, moralische Läuterung der Seele, die Heranbildung der be­sonderen menschlichen Tugenden. Und wenn man sagt, es werde in der Rosenkreuzerei davon gesprochen, daß man unedle Metalle in Gold verwandeln könne, so sei damit nichts anderes gemeint, als daß man die unedlen Metalle der verschiedenen Menschenuntugenden in das Gold der mensch­lichen Tugenden verwandeln könne, und daß dieser Ver­wandlungsprozeß nur eine symbolische Darstellung dessen sei, wie man sich innerlich moralisch entwickeln solle.",
      "Wenn es so wäre, so würde die ganze Geschichte nichts weiter als eine Trivialität oder noch etwas viel Nichtigeres sein, denn es ist schlechterdings kaum einzusehen, warum man allerlei alchemistische Dinge wie Metallverwandlung und so weiter erfinden sollte, um ein so auf der Hand liegen­des Ding zu demonstrieren, daß der Mensch sich läutern und seine Untugenden verwandeln solle. Dieser Einwand kann immer gegen diejenigen gemacht werden, die das große Werk des Rosenkreuzertums wie etwas bloß Symbolisches auffassen. Aber in der Tat steckt etwas viel Tieferes da­hinter.",
      "Nicht länger möchte ich mich bei dem Geschichtlichen aufhalten. Das Geschichtliche soll uns heute, wo ich eine",
      "sachliche Auseinandersetzung über das Rosenkreuzertum zu geben beabsichtige, wenig angehen. Das Geschichtliche braucht uns nicht weiter zu berühren, als nur insofern wir dadurch erfahren, daß das Rosenkreuzertum eine Grün­dung, eine Stiftung ist, die seit dem vierzehnten Jahrhun­dert tatsächlich im Abendlande besteht, daß sie zurückgeht auf eine Persönlichkeit, welche fast sagenumwoben ist, wie man bemerken könnte, von der aber die Geschichte nicht viel zu melden weiß: Christian Rosenkreuz.",
      "Was nun aus den verschiedenen Mitteilungen als ein ge­wisser Grundklang hervorgeht, ist dahin zusammenzufas­sen, daß Christian Rosenkreuz - so ist zwar nicht sein wah­rer, wohl aber derjenige Name, unter dem er bekannt geworden ist - am Ende des fünfzehnten und im Beginne des sechzehnten Jahrhunderts auch Reisen gemacht habe, und daß er auf seinen Reisen durch das Morgenland das sogenannte Buch ... kennengelernt habe, jenes Buch, von dem uns sehr geheimnisvoll gesagt wird, daß Paracelsus, der große mittelalterliche Arzt und Mystiker, sein Wissen daraus geschöpft habe. Dies ist wirklich eine wahre Tatsache, doch nur die Eingeweihten wissen: erstens, was das Buch M... ist, und zweitens, was das Studium im Buche ... . bedeutet.",
      "Die äußere Welt ist immer wieder hingewiesen worden auf das Rosenkreuzertum durch die beiden Schriften, die vom Anfange des siebzehnten Jahrhunderts stammen. Im Jahre 1614 erschien die sogenannte «Fama Fraternitatis» und ein Jahr später die sogenannte «Confessio» - zwei Bü­cher, über die von gelehrter Seite viel gestritten worden ist. Und zwar nicht nur darüber, worüber bei so vielen Büchern sonst gestritten wird, ob jener Valentin Andreae, der in seinen späteren Lebensjahren ein ganz normaler Super­intendent war, auch wirklich das Buch verfaßt hat -, sondern",
      "bei diesen Büchern ist auch darüber gestritten worden, ob sie von den Verfassern ernst genommen worden sind, oder ob sie nur ein Spott darüber sein sollten, daß es eine gewisse geheimnisvolle Brüderschaft des Rosenkreuzes gäbe, welche diese und jene Tendenzen und Ziele habe. Dann gibt es im Gefolge dieser Schriften eine ganze Reihe anderer, die allerlei aus dem Bereiche des Rosenkreuzertums mitteilen. Wenn Sie die Schriften von Valentin Andreae und auch an­dere rosenkreuzerische Schriften in die Hand nehmen, dann werden Sie, wenn Sie die eigentliche Grundlage des Rosen­kreuzertums nicht kennen, in diesen Schriften nichts beson­deres finden. Denn es ist überhaupt bis in unsere Zeit hinein nicht möglich gewesen, auch nur das Elementarste aus dem Bereiche dieser Geistesströmung, die seit dem vierzehnten Jahrhundert wirklich existiert hat und auch heute noch existiert, kennenzulernen. Alles, was in die Literatur über­gegangen ist, was geschrieben und gedruckt worden ist, sind einzelne Bruchstücke, einzelne verlorene, durch Verrat an die Öffentlichkeit gekommene Dinge, die ungenau und in vielfacher Weise durch Charlatanerie, Schwindel, Unver­stand und Dummheit verkehrt worden sind. Die wahre, echte Rosenkreuzerei ist, seitdem sie besteht, stets nur Ge­genstand mündlicher Mitteilung an solche gewesen, welche sich eidlich zur Geheimhaltung verpflichten mußten. Daher ist auch nichts Erhebliches in die öffentliche Literatur über­gegangen. Erst dann, wenn man dasjenige kennt, was heute",
      "- aus gewissen Gründen, die zu erläutern jetzt zu weit füh­ren würde - in der elementaren Rosenkreuzerei öffentlich mitgeteilt werden kann und wovon wir heute werden spre­chen können, kann man in den oftmals grotesken, oft bloß komischen, oft aber auch schwindelhaften und selten stim­menden Mitteilungen der Literatur einigen Sinn finden.",
      "Die Rosenkreuzerei ist eine der Methoden, wie man die",
      "sogenannte Einweihung erreichen kann. Was Einweihung heißt, davon ist des öfteren an dieser Stelle schon die Rede gewesen. Einweihen heißt, die in jeder Menschenseele schlum­mernden Fähigkeiten erwecken, durch die man hineinsehen kann in die geistigen Welten, die hinter unserer sinnlichen Welt liegen, und von denen unsere sinnliche Welt nur ein äußerer Ausdruck, eine Wirkung ist. Ein Eingeweihter ist derjenige, welcher die genau bestimmten, wissenschaftlich durchgearbeiteten Methoden der Einweihung angewendet hat, Methoden, die ebenso wissenschaftlich durchgearbeitet sind wie diejenigen der Chemie, der Physik oder anderer wissenschaftlicher Gebiete. Dasjenige, was in solchen Metho­den durchgemacht wird, ist allerdings nicht etwas, was der Mensch auf etwas Äußeres anzuwenden hat, sondern was sich zunächst nur auf ihn selbst bezieht, auf das Instrument, das Werkzeug, durch das man in die geistige Welt hinein-sieht. Der wirkliche Geisteskenner weiß, wie tief und wahr Goethes Ausspruch ist:",
      "Geheimnisvoll am lichten Tag",
      "Läßt sich Natur des Schleiers nicht berauben,",
      "Und was sie deinem Geist nicht offenbaren mag,",
      "Das zwingst du ihr nicht ab mit Hebeln und mit Schrauben.",
      "Tief, tief sind die Geheimnisse der Natur, aber nicht un­ergründlich tief, wie manche sagen möchten, die im höheren Sinne nur zu bequem sind, in die Geheimnisse der Natur einzudringen. Nicht unergründlich tief sind sie, sondern zu ergründen durch den Menschengeist, zwar nicht durch den Alltagsgeist, aber den Menschengeist, der verborgene Kräfte der Seele durch gewisse, streng umschriebene Methoden aus sich herausholt. Wenn der Mensch sich nach und nach vorbe­reitet, dann gelangt er allmählich dazu, dasjenige geoffen-bart zu erhalten, was als ein Wissen nur denen zukommt,",
      "die wirklich eingeweiht sind: jenes große Geheimnis, von dem, was, um mit Goethes Ausspruch zu sprechen, «die Welt im Innersten zusammenhält». Die Enthüllung die­ses Geheimnisses ist eigentlich die Frucht der wirklichen Einweihung.",
      "Es ist hier des öfteren auseinandergesetzt worden, daß die ersten Stufen der Einweihung durchaus gefahrlos für jeden zu durchwandern sind, daß aber die höheren Stufen die größtmöglichste menschliche Hingabe an die unbeding­teste Wahrheitserforschung verlangen. Wenn der Mensch sich jenen Pforten nähert, durch die er einen Einblick ge­winnen kann in ganz andere Welten, dann weiß er aller­dings, daß etwas von Wirklichkeit steckt hinter der oftmals gebrauchten Redensart, daß es gefährlich ist, großen Men­schenmengen die heiligen Geheimnisse des Daseins mitzu­teilen.",
      "Soweit es heute möglich ist und soweit es geschehen kann, die Menschen dazu vorzubereiten, allmählich den Weg finden zu können, zu den höchsten Geheimnissen der Natur und der geistigen Welt, soweit ist es auch möglich, die höheren Geheimnisse zu enthüllen. Was man die geistes-wissenschaftliche Bewegung nennt, ist ein Pfad, der er­schlossen ist, die Menschen dahin zu führen, daß sie den Weg zu den höheren Geheimnissen finden können.",
      "Solcher Wege zu den höheren Geheimnissen gibt es eine ganze An­zahl. Nicht als ob die letzte Weisheit, die der Mensch er-ringen kann, viele Gestalten annehmen könnte; das ist nicht der Fall. Die höchste Weisheit ist eine einheitliche.",
      "Wo und wann auch immer Menschen leben oder gelebt haben, wenn sie einmal zur höchsten Weisheit gekommen sind, dann ist diese höchste Weisheit für alle Menschen eine einheitliche, wie der Ausblick vom Gipfel eines Berges, wenn man ganz oben sich befindet, ein einheitlicher ist. Aber es gibt ver­schiedene Wege, um zum Gipfel des Berges hinaufzugelangen,",
      "und man wird denjenigen Weg wählen, welcher von dem Ausgangspunkte aus, an dem man sich befindet, der geeignetste ist. Wenn man an einem gewissen Punkte des Berges steht und einen Weg vom eigenen Standpunkte haben kann, so wird man nicht erst um den Berg herumgehen.",
      "So ist es auch mit dem Weg, der zu der höchsten Erkenntnis hin aufführt. Hier handelt es sich darum, daß die Ausgangs­punkte, die man zu wählen hat, von der Menschennatur aus zu nehmen sind. Das, was hier in Betracht kommt, beachten die Menschen heutzutage viel zu wenig: Es ist die große Verschiedenheit der menschlichen Natur zu berücksichtigen.",
      "Anders organisiert als heute waren, wenn auch vielleicht nicht für die grobe Anatomie und Physiologie, aber für die feinere Geistesforschung, jene höheren Glieder des alten indischen Volkes, so daß es möglich war, bis heute eine wunderbare Geheim- oder Geisteswissenschaft zu bewahren und auch die dazugehörige Methode der Einweihung: die sogenannte Yoga-Schulung. Diese orientalische Yoga-Schu­lung ist der Weg, welcher zu dem Gipfel der Erkenntnis hinaufführt bei einer so organisierten Natur, wie die An­gehörigen des alten indischen Volkes sie hatten.",
      "Für den heutigen Europäer würde derselbe Weg so unsinnig sein, wie wenn jemand, der an einem bestimmten Fußpunkte eines Berges steht, erst um den Berg herumgehen wollte, um einen Weg zu suchen und zu benützen. Die Natur des heutigen Europäers ist ganz anders als die orientalische Natur.",
      "An­ders als heute war auch die menschliche Natur organisiert um die Zeit der Entstehung des Christentums herum, einige Jahrhunderte vorher und einige nachher.",
      "Wenn wir daran festhalten, was eben gesagt worden ist, daß Einweihung soviel bedeutet wie innere Kräfte heraus­zuholen, innere Kräfte zu erwecken durch bestimmte Metho­den, so daß der Mensch das Instrument wird, durch das er",
      "in die geistige Welt hineinschauen und sie erforschen kann, dann müssen wir zugeben, daß auf diese Menschennatur Rücksicht genommen werden muß. So wie die alten heiligen Rishis, jene großen Lehrer des alten indischen Volkes, die wunderbare Methode ausgearbeitet haben, die heute noch immer für die Angehörigen des indischen Volkstums ihre Gültigkeit hat, so wie im Anfange des Christentums die christlich-gnostische Methode hinaufführen mußte in die geistigen Gebiete, so muß für den modernen Menschen, für den Menschen, der in unserer heutigen Umwelt lebt, wenn er ganz und gar dieser heutigen Welt angehört und aus die­ser die Bedingungen seines Daseins schöpft, eine andere Methode die taugliche sei. Deshalb erneuern die großen Meister der Weisheit, welche die Menschengeschicke leiten, im Laufe der Jahrhunderte und Jahrtausende immer wie­der und wieder die Methoden, durch die der Gipfel der Weisheit erreicht werden kann. Für die heutige Menschheit, für den Menschen, der aus den modernen Bedingungen des Daseins herausgewachsen ist, sind gerade von der rosen­kreuzerischen Strömung die rosenkreuzerischen Methoden begründet worden. Sie sind also Einweihungsmethoden, die geradeso zum Gipfel der Weisheit hinaufführen wie andere Methoden, nur daß sie auf besondere, augenblicklich vor­handene Bedingungen des modernen Menschen eingehen.",
      "Nicht sind etwa die rosenkreuzerischen Methoden un­christlich oder antichristlich. Davon kann keine Rede sein. Dasjenige, was das Christentum dem Menschen an Schulung bieten kann, das wird auch in der rosenkreuzerischen Me­thode geboten. Aber zu gleicher Zeit erwirbt sich derjenige, der eine Rosenkreuzerschulung durchmacht, die Fähigkeit, die geheim- und geisteswissenschaftlichen Errungenschaften in vollem Einklang zu sehen mit der ganzen modernen Bil­dung, mit alledem, was modernes Fühlen und moderne Anschauung",
      "von der Natur des Geistes notwendig macht. Für lange Jahrhunderte in die Zukunft hinein werden die rosen­kreuzerischen Methoden die richtigen Methoden der Ein­weihung in das geistige Leben sein. Als sie begründet wor­den sind, galten für ihre Anhänger gewisse Regeln. Diese Regeln gelten im Grunde genommen auch heute noch. Weil diese Regeln streng eingehalten werden von allen denen, die wirklich Rosenkreuzer sind, deshalb ist es für Außen­stehende unmöglich, den Rosenkreuzer zu erkennen. Nie erkenne einer den anderen, das ist die erste Regel, die nur in letzter Zeit eine kleine Änderung erfahren hat. Ihr sollt die Weisheit im engsten Kreise pflegen, Ihr sollt aber die Resultate, die Früchte der Weisheit allen Menschen zugäng­lich machen. Deshalb trug der Rosenkreuzer bis vor kurzem dasjenige, wodurch er in die Tiefe der Natur hineinschaut, niemals vor das Publikum. Keine Theorie, kein Begriff, keine Idee, nichts von irgendwelchen Vorstellungen und Erkennt­nissen wurde da gegeben, sondern Arbeiten wurden geleistet, welche die Kultur vorwärtsbringen und wodurch die Weis­heit dem Volke in einer Weise eingeimpft wurde, daß die Außenstehenden nicht viel davon merken konnten.",
      "Das ist der erste Grundsatz, den weiter auszuführen zu weit führen würde, und in bezug auf dessen Kern ich nur bemerken wollte, daß er heutzutage zum Teil durch­brochen wird, daß aber die höhere rosenkreuzerische Weis­heit nicht verkündet werden darf. Der zweite Grundsatz bezieht sich auf die Art des Auftretens und heißt: Gehe auf in derjenigen Volksmasse und derjenigen Kulturströmung, in die du hineingestellt worden bist. Sei ein Mitglied des Volkes und Standes der Bildungs- und der Kulturstufe, in die du hineingestellt worden bist. Trage kein besonderes Kleid, wie es gewöhnlich ausgedrückt wird, trage das all­gemeine Kleid, welches die anderen tragen. - Daher werden",
      "Sie als eine Art und Weise finden, daß der Rosenkreuzer da, wo er wirkt, möglichst wenig aus der Ehrsucht und aus der Selbstsucht heraus zu wirken sucht. Er wird versuchen, da und dort an Kulturströmungen anzuknüpfen, bestrebt sein, sie zu vertiefen und das Vorhandene zu gebrauchen, aber er wird immer im Auge haben etwas, was noch viel tiefer ist, was ihn verbindet mit der Zentralweisheit des Rosenkreuzertums selbst. Die anderen Grundsätze brau­chen uns jetzt nicht zu beschäftigen, denn wir wollen uns jetzt mit der Rosenkreuzerschulung befassen, wie sie seit Jahrhunderten bestanden hat und noch besteht. Die Dinge, die mitgeteilt werden können, sind in gewisser Beziehung elementar, sind nur der Anfang des ganzen Systems der Rosenkreuzerschulung. Es muß aber gesagt werden, daß von dieser Schulung dasselbe gilt, was von jeder geisteswissenschaftlichen Schulung gesagt werden kann: daß die Menschen nicht literarisch suchen sollen, sondern nur dann sich praktisch mit der Sache beschäftigen möchten, wenn sie die persönliche Anleitung eines Wissenden haben. Alles, was man in dieser Beziehung sagen kann, finden Sie in der Zeit­schrift «Luzifer-Gnosis» von Nr. 13 an unter dem Titel:",
      "«Wie erlangt man Erkenntnisse der höheren Welten?»",
      "Was bei der Rosenkreuzerschulung zwecks Eintretens in die geistige Welt der Schüler zu absolvieren hat, sind fol­gende sieben Stufen. Diese brauchen nicht etwa in der Rei­henfolge, wie ich sie aufzählen werde, von dem Schüler durchgemacht zu werden. Der Lehrer wird, je nach der In­dividualität des Schülers, aus dem einen oder dem anderen Punkte dasjenige herausheben, was gerade für den Schüler notwendig ist, und wird so eine Art von Lehrgang, eine Art von innerem Entwicklungsgang dem betreffenden Schüler persönlich zu geben haben. Hier muß man aber die Stufen der Rosenkreuzerschulung aufzählen. Es sind sieben:",
      "1.    Was man im rosenkreuzerischen Sinne «Studium» nennt.",
      "2.    Was man als Aneignung der sogenannten imagina­tiven Erkenntnis bezeichnet.",
      "3.    Was man die Aneignung der okkulten Schrift nennt.",
      "4.    Was man entweder mit dem anspruchslosen Wort be­zeichnet: Rhythmisierung des Lebens, oder auch, und zwar im wahrhaftigen Sinne: die Bereitung des Steins der Weisen. Das ist etwas, was es gibt, was nur nicht jenes törichte Ding ist, von dem Sie in Büchern lesen können.",
      "5.    Was man die Erkenntnis des Mikrokosmos, das heißt der eigenen menschlichen Natur nennt.",
      "6.    Was man nennt: das Aufgehen in den Makrokosmos oder in die große Welt draußen.",
      "7.    Was man nennt: die Erreichung der Gottseligkeit.",
      "In welcher Aufeinanderfolge der Schüler diese Stufen durchmacht, das hängt ganz von seiner Individualität ab. Durchmachen aber muß er sie in der elementaren Rosen­kreuzerschulung. Betrachten Sie das, was ich Ihnen bezüg­lich der Rosenkreuzerschulung gesagt habe und was ich jetzt noch charakterisieren werde, als eine Art Ideal. Glau­ben Sie nicht, daß man es von heute auf morgen ausführen kann, aber man muß das, was einem heute noch fernsteht, seinem tieferen Inhalte nach, wenigstens dem Wortlaute nach kennenlernen. Beginnen kann der Mensch zu jeder Zeit, wenn er sich bewußt ist, daß er Geduld, Energie und Ausdauer haben muß.",
      "Der erste Punkt, das Studium, schließt ein Wort ein, das für viele pendantisch klingt. Es wird aber keine Gelehrsam­keit darunter verstanden. Um Eingeweihter zu sein, braucht man nicht gelehrt zu sein. Gelehrsamkeit hat mit geistiger",
      "Erkenntnis nicht allzuviel zu tun. Unter dem Studium, um das es sich hier handelt, ist etwas anderes zu verstehen. Die­ses Studium ist aber unerläßlich, und niemand darf durch einen wirklich kundigen Lehrer der Rosenkreuzerei in höhere Stufen eingeführt werden, wenn er nicht Neigung hat, die Stufe des Studiums wirklich durchzumachen. Durch das Studium soll sich der Schüler ein völlig vernünftiges, ganz und gar logisches Denken aneignen, ein Denken, wel­ches ihn davor bewahrt, beim Durchgang durch die folgen­den Stufen - wie das leicht sein könnte - den Boden unter den Füßen zu verlieren. Es muß durchaus festgehalten wer­den, daß derjenige, der eintreten soll in die geistige Welt, sie vorher kennenlernen soll, da sie in manche Irrpfade hin­einführen kann, welcher Gefahr er nur dann entgeht, wenn er alles Phantastische, alles Unlogische, alles, was irgend­wie unvernünftig sein könnte, vor allen Dingen abgelegt hat. Ein Phantast, der sich Vorstellungen über allerlei Un-wirkliches macht, ist nicht zu gebrauchen für die geistige Welt.",
      "Das ist der eine Grund. Der andere Grund ist der, daß man, wenn man in die höheren Welten kommt, das Mannigfaltigste an Wahrnehmungen erfährt, was durch und durch verschieden ist von dem, was uns hier in der Sinnenwelt umgibt. Derjenige, welcher hineinschauen kann",
      "- wenn ihm die inneren Sinne der Seele geöffnet werden -in die uns am nächsten befindlichen geistigen Welten, die wir gewohnt sind, die astrale und geistige Welt zu nennen, in die Welten, aus denen der Mensch ebenso herausgeboren ist wie aus der physischen Welt, lernt Dinge kennen, die grundverschieden sind von den Wahrnehmungen in unserer Sinnenwelt. Wer die astrale oder geistige Welt betritt, weiß, wie grundverschieden diese Welten sind von dem, was er hier mit Augen zu sehen, mit Ohren zu hören gewohnt ist.",
      "Aber eines ist gleich durch alle drei Welten, durch die phy­sische, astrale, geistige oder devachanische Welt, und das ist das logische Denken. Weil das logische Denken in allen drei Welten dasselbe ist, deshalb kann es hier in dieser physi­schen Welt schon gelernt werden, so daß wir durch dasselbe eine feste Stütze in den anderen Welten haben werden. Lernt man aber so denken, daß der Gedanke irrlichteliert, so daß man nicht unterscheiden kann Phantasiegebilde von Wirklichkeit, so daß man zum Beispiel, wie unsere Physiker heute es tun, Atome, die niemand in unserer physischen Welt gesehen hat, wie etwas Wirkliches behandelt, gibt man sich solchen Phantasien schon in der physischen Welt hin, dann ist man nicht fähig, sich hinaufzuheben in die höheren Welten. Denken Sie sich einmal, was ein Mensch, der nicht an strenge und unerbittliche Logik gewohnt ist, von den höheren Welten für Zeug erzählen könnte.",
      "Nun handelt es sich allerdings nicht um das, was man im gewöhnlichen Sinne Denken nennt. Das gewöhnliche Den­ken ist nur ein Kombinieren sinnlicher Wirklichkeiten. Hier handelt es sich aber um ein Denken, das sinnlichkeitsfrei geworden ist. Gelehrte und Philosophen leugnen heutzu­tage ein solches Denken überhaupt. Sie können bei vielen Philosophen, die heute einen großen Namen haben, nach­lesen, daß der Mensch nicht in bloßen Gedanken denken könne, sondern immer nur in solchen Gedanken denken müsse, die einen Rest von sinnlichen Bildern enthalten. Wenn ein Philosoph das sagt, dann beweist das nichts wei­ter, als daß er nicht in reinen Gedanken denken kann, und es ist eine unbeschreibliche Unbescheidenheit, wenn man das, was man selber nicht kann, als eine allgemeine Un­fähigkeit hinstellt. Der Mensch muß imstande sein, sich Gedanken zu bilden, die nicht mehr von Wahrnehmungen der Augen und Ohren abhängig sind, so daß er in einer",
      "reinen Gedankenwelt schweben kann, in der Welt, die er in sich selber findet, wenn er die Aufmerksamkeit von den äußeren, sinnlichen Wirklichkeiten ablenkt. Dieses Denken nennt man in der Geisteswissenschaft und auch im Rosen­kreuzertum das sich selbst erzeugende Denken. Derjenige, der nichts anderes tun will, um ein solches Studium zu ab­solvieren, mag die Lehrbücher der heutigen Geisteswissen­schaft vornehmen. Das, was Sie da finden, sind nicht bloß sinnnliche Kombinationen, sondern Gedanken, die aus höhe­ren Welten stammen, Gedanken, die ein geschlossenes Den­ken darstellen, das jeder verstehen kann, so daß er nicht bei der gewöhnlichen, trivialen Art des Denkens stehenzublei­ben braucht.",
      "Um die erste Stufe der Rosenkreuzerschulung möglich zu machen, ist es nötig, daß das, was seit Jahrhunderten im engsten Kreise behütet worden ist, durch Literatur und Vorträge der Menschheit zugänglich gemacht wird. Was zu­gänglich gemacht wird, ist aber nichts anderes als das Ein­maleins, der Anfang des großen und unermeßlichen Weltenwissens. Mit der Zeit wird immer mehr davon in die Mensch­heit einfließen. Seit einigen Dezennien ist der elementare Teil desselben der Menschheit enthüllt worden. Daran kön­nen Sie Ihr Denken schulen. Für diejenigen, die das gründ­licher machen wollen, die also in eine solche strenge Schu­lung des Denkens eintreten wollen, sind meine beiden Bücher «Wahrheit und Wissenschaft» und «Die Philosophie der Freiheit» bestimmt. Diese Bücher sind nicht so geschrieben wie andere Bücher, daß sie einen Satz einer bestimmten Stelle auch an eine andere Stelle des betreffenden Buches setzen könnten. Diese Bücher sind keine Gedanken-Aggre­gate, sondern Gedanken-Organismen. Ein Gedanke wächst wie ein Organismus, er wächst organisch aus dem anderen heraus. Diese Bücher sind also nicht so geschrieben, daß einfach",
      "ein Gedanke zum anderen hinzugefügt wird, sondern so, daß die späteren Gedanken aus den vorhergehenden her-ausgewachsen sind wie bei einem Organismus. So müssen in dem Leser auch die Gedanken herauswachsen, er muß spü­ren, wie er hingetrieben wird zu dem Denken; und dann macht er sich jene eigentümliche Art des Denkens, das sich selbst erzeugende Denken, zu eigen, ohne welches man die höheren Stufen der rosenkreuzerischen Schulung nicht er­langen kann, obgleich diese gründlichere Art nicht absolut notwendig ist und man sehr gut bei der geisteswissenschaft­lichen, elementaren Literatur bleiben kann, da diese den Stoff für das Studium auch abzugeben vermag.",
      "Das zweite ist die Aneignung des imaginativen Denkens. Dasjenige, was ich imaginatives Denken nenne, sollte man sich erst aneignen, wenn man auf diese Weise strenge innere Gedankennotwendigkeit in sich aufgenommen hat, so daß man einen strengen Wissenskern besitzt. Man kann sonst leicht den Boden unter den Füßen verlieren. Was ist nun imaginatives Denken? Goethe, der in seinem rosenkreuzeri­schen Gedicht «Die Geheimnisse» gezeigt hat, wie tief er in die rosenkreuzerischen Geheimnisse eingeweiht war, gibt einen Hinweis in einem schönen Spruch des Chorus Mysti­cus im zweiten Teil des Faust, wo er das Geleitwort ge­geben hat: «Alles Vergängliche ist nur ein Gleichnis.» Dies wurde überall, wo eine innere rosenkreuzerische Schulung vorhanden war, in systematischer Weise entwickelt. Der Rosenkreuzer mußte fähig werden, durch die ganze Welt zu gehen und neben der logischen Erkenntnis sich die ima­ginative Erkenntnis derselben anzueignen, diejenige Er­kenntnis, die in allem, was um uns herum ist, ein Geistiges, ein Unvergängliches sieht. Wenn Sie einem Menschen gegen-übertreten und Sie sehen auf seinem Antlitz ein heiteres Lächeln, dann werden Sie nicht dabei stehenbleiben, nur",
      "jene eigentümlichen Windungen im Gesicht, die Physio­gnomie, die sich Ihrem Auge darbietet, zu beschreiben. Es wird vielmehr Ihre Seele sich klar sein darüber, daß in jenem eigentümlichen Ausdruck der Heiterkeit sich das innere Leben der Seele verrät, ebensowenig wie Sie bei per­lenden Tränen dabei stehenbleiben werden, sie zu unter­suchen.",
      "Sie werden sich klar darüber sein, daß die Tränen der Ausdruck inneren Schmerzes, inneren Leides sind. Das Äußere ist Ausdruck des Inneren. Sie sehen in der Physio­gnomie bis auf den Grund der Seele. Der ganzen übrigen Natur gegenüber muß das der Rosenkreuzerschüler lernen.",
      "So wie das menschliche Antlitz und die Bewegung der Hände Ausdrucksmittel sind für das menschliche Seelenleben, so ist alles, was in der Natur vorgeht, Ausdruck eines seelisch-geistigen Lebens. Wie die Geste Ausdruck für unsere Seele ist, so wird für den Rosenkreuzer alles - nicht bloß als poetisches Bild, sondern als tiefe Wirklichkeit -, die ganze Erde um uns herum der Ausdruck seelisch-gei­stigen Lebens: die Steine, Pflanzen und Tiere, die Sterne, jeder Luftzug.",
      "Alles, was um uns herum ist, wird so der Ausdruck von Seelisch-Geistigem, nicht etwa in poetischer Beziehung, sondern in Wirklichkeit, wie das leuchtende Auge, die sich runzelnde Stirne, die perlende Träne physio­gnomische Ausdrücke innerer Seelenzustände sind. Dann erst wissen Sie, was imaginative Erkenntnis heißt, wenn Ihnen das, was Goethe in seinem Faust vom Erdgeiste sagt, nicht mehr ein poetisches Bild, sondern Wirklichkeit ist, wenn Sie bei dem heutigen materialistischen Sinn unserer Bevölkerung nicht stehenbleiben, sondern bei dem Worte des Erdgeistes Wirklichkeit zu erkennen vermögen, wäh­rend man heute froh ist, wenn man ein poetisches Bild darin genießen kann:",
      "In Lebensfluten, im Tatensturm",
      "Wall' ich auf und ab,",
      "Webe hin und her!",
      "Geburt und Grab,",
      "Ein ewiges Meer,",
      "Ein wechselnd Weben,",
      "Ein glühend Leben,",
      "So schaff' ich am sausenden Webstuhl der Zeit",
      "Und wirke der Gottheit lebendiges Kleid.",
      "Wenn Ihnen diese Worte des Erdgeistes Wirklichkeit geworden sind und Sie es ruhig aushalten können, daß Sie von Materialisten für einen Narren gehalten werden, da Sie wissen, daß Sie eine tiefere Logik haben, da Sie wissen, daß jene phantastischer sind und nur zu wissen glauben, daß Sie aber wissen, daß Sie einer freien Wirklichkeit des Gei­stes gegenüberstehen, und ebenso wahr und wirklich, wie eine menschliche Seele in den Physiognomien lebt, auch in der Erdphysiognomie ein Erdgeist lebt. Wenn Sie in einer Pflanze die Heiterkeit des Erdgeistes erblicken, wenn die Erde Ihnen der Ausdruck des leiderfüllten Erdgeistes wird, wenn Ihnen die Natur so erscheint, als wenn sie zu Ihnen spräche, wie wenn sie Ihnen ihr Geheimnis wirklich mit­teilte, wenn Sie das erleben, dann fangen Sie an, ihre Ge­heimnisse zu buchstabieren und zu verstehen, was es heißt:",
      "imaginative Erkenntnis zu erwerben. Dann kommen Sie dahin, zu verstehen, wie dies im Rosenkreuzertum und auch bei den Vorfahren des Rosenkreuzertums in dem großen okkulten Ideal des heiligen Grals hingestellt worden ist als dem reinsten und schönsten Ausdruck für das Streben nach Imaginativer Erkenntnis.",
      "Lassen Sie uns einmal einen Blick werfen auf die wahre Natur dieses Ideals vom heiligen Gral. Es tritt Ihnen in",
      "jeder Rosenkreuzerschule in der Weise vor Augen, wie ich es jetzt charakterisieren will. Ich benutze hierzu die Form eines Dialogs, der aber niemals in wirklichen Rosenkreuzer­schulen gehalten worden ist. Da wurde durch lange Ent­wicklungsmethoden im Leben das erreicht, was ich jetzt im Dialog zusammenfassen will. Er gibt das, was das Ideal des heiligen Grals wirklich enthält.",
      "Sieh Dir an die Pflanze, wie sie herauswächst aus der Erde. Ihre Wurzel ist in den Boden hineingesenkt, sie ist nach dem Mittelpunkt der Erde hin gerichtet, der Stengel strebt nach oben, die Blüte nach oben öffnend, darinnen die befruchtenden Organe, die den Samen zeugen werden, wodurch die Pflanze über sich selbst hinauslebt. Nicht erst Darwin, der große Naturforscher, hat davon gesprochen, daß, wenn man die Pflanze mit dem Menschen vergleicht, nicht die Blüte, sondern die Wurzel mit dem Kopfe ver­glichen werden müsse. Die Wurzel der Pflanze entspricht dem Kopfe des Menschen - so sagte schon der Rosenkreuzer-Okkultismus-, und dasjenige, was von der Pflanze als Blütenkelch der Sonne keusch entgegenstrebt, das ist das, was der Mensch als Befruchtungsorgane nach unten wendet. Der Mensch ist eine umgekehrte Pflanze. Er wen­det die Organe, welche die Pflanze keusch nach oben dem Lichte zuwendet, schamvoll nach unten und verhüllt sie. Der Mensch ist die umgekehrte Pflanze: das ist ein Grund­satz des Rosenkreuzer-Okkultismus und des Okkultismus aller Zeiten. Die Pflanze ist mit den Befruchtungsorganen keusch der Sonne zugewendet. Der Mensch hat die Befruch­tungsorgane nach dem Mittelpunkte der Erde gerichtet, den Kopf frei nach dem Sonnenraum hinaus. Zwischen beiden, mitten drinnen, steht das Tier. Die drei Richtungen, die sich durch die Pflanze, das Tier und den Menschen ergeben, bezeichnet man als das Kreuz. Die Pflanze ist der Balken,",
      "der nach unten geht, das Tier ist der Querbalken, der Mensch ist der Balken nach oben. Wenn Plato, der große eingeweihte Philosoph des Altertums, sagt, daß die Weltseele an dem Kreuze des Weltenleibes gekreuzigt ist, so bedeutet das nichts anderes, als daß der Mensch die höchste Ausgestal­tung der Weltenseele darstellt, und daß die Weltenseele hindurchgegangen ist durch die drei Reiche: Pflanzenreich, Tierreich und Menschenreich. Die Weltenseele ist an dem Kreuze: Pflanzenreich, Tierreich und Menschenreich, den drei Naturreichen, gekreuzigt. - Ein wunderbar tiefes Bild von Plato, ganz aus der Geisteswissenschaft herausge­sprochen.",
      "Unzählige Male wurde dieses Bild in den Rosenkreuzer­schulen wiederholt: Schaut Euch die Pflanze an mit dem Kopf nach unten, mit den Befruchtungsorganen nach oben, die sich dem Sonnenstrahl entgegenstrecken. - Diesen Son­nenstrahl nannte man die heilige Liebeslanze, welche die Pflanze zu durchdringen hat, damit der Same zum Wachsen und Reifen kommen kann. Nun sagte man dem Schüler:",
      "Richte den Blick hinauf bis zum Menschen, sieh dir die Pflanze und dann den Menschen an, vergleiche des Menschen Materie und Stoff mit denen der Pflanze. Der Mensch ist die umgekehrte Pflanze, er ist es geworden, weil er seinen Stoff, sein Fleisch durchdrungen hat mit physischer Begierde, mit Leidenschaft und Sinnlichkeit. Keusch und rein darf die Pflanze die Befruchtungsorgane der Befruchtungslanze, der hehren Liebeslanze, entgegenstrecken. Der Mensch kommt auf einen ähnlichen Standpunkt in der Zeit, wo er die Be­gierde vollkommen geläutert haben wird, so daß er in eine Zukunft hineinblickt, die ihm die Erfüllung des Ideals brin­gen wird: Du bist so keusch und rein wie der Blütenkelch der Pflanze. Dann wirst du auf der Höhe der irdischen Ent­wicklung angelangt sein, dann wird nicht mehr unreine Begierde",
      "deine niederen Organe durchziehen, dann wirst du die geistige Liebeslanze, deine produktive Kraft, die dann ganz geistig sein wird, entgegenstrecken dem Blütenkelch, wie der Pflanzenkelch sich öffnet der heiligen Liebeslanze im Sonnenstrahl. So geht der Mensch durch die Reiche der Natur hindurch und läutert sich hinauf bis zur Entwicklung derjenigen Organe, die heute erst in der Anlage begriffen sind. Wenn der Mensch in dem, was heilig und edel ist, etwas hervorbringt, so ist er am Anfang einer zukünftigen, produktiven Kraft, die er haben wird, wenn seine niedere Natur ihre vollständige Läuterung durchgemacht hat. Dann wird er ein neues Organ haben. Der Blütenkelch der Pflanze wird auf höherer Stufe neuerdings erstehen und wird der Lanze des Amfortas entgegengestreckt werden, wie der Blütenkelch der geistigen Liebeslanze der Sonne.",
      "So stelle dir auf niederer Stufe dasjenige dar, was, als hohes Ideal gegeben, in Zukunft des Menschen Geschlecht sein wird, wenn alles Niedere geläutert sein wird und alles keusch und rein sich entgegenhalten wird der vergeistigten Sonne der Zukunft, wenn dieser Pflanzenkelch hindurch­gegangen sein wird durch die Menschennatur, die in gewis­ser Beziehung höher, in gewisser Beziehung niederer stehen wird als die Pflanze, wenn er hinaufgeläutert sein wird bis zur höchsten Geistigkeit, und vorgehalten wird der ver­geistigten Sonne als der heilige Kelch, der erhöhte Pflanzenkelch, der durch die Menschheit hindurchgegangen ist.",
      "Dies wurde geistig erfaßt von dem Rosenkreuzerschüler, es ist das Geheimnis des heiligen Gral, das höchste Ideal, das vor den Menschen hingestellt werden kann. So erscheint die ganze Natur mit einem geistigen Sinn durchglüht und durch­strömt. Wenn man so alles erfaßt, alles als ein Gleichnis des Geistigen sieht, dann ist man auf dem Wege, die imagina­tive Erkenntnis zu erwerben. Dann dringen aus den Dingen",
      "die Farben und werden selbständig, es dringen aus ihnen die Töne und werden selbständig, der Raum erfüllt sich mit einer selbständigen Farben- und Tonwelt, und in diesen kündigen sich geistige Wesenheiten an. Wir steigen von der imaginativen Erkenntnis zu der wirklichen Erkenntnis des geistigen Raumes auf. Das ist der Weg, den der Rosenkreuzer auf der zweiten Stufe seiner Schulung nimmt.",
      "Das dritte ist die Kenntnis der okkulten Schrift. Die okkulte Schrift ist keine gewöhnliche Schrift, sondern eine solche, die mit den Naturgeheimnissen zusammenhängt. Ich möchte Ihnen gleich klarmachen, was Sie sich unter der okkulten Schrift vorzustellen haben. Ein verbreitetes Zei­chen dieser Schrift ist der sogenannte Wirbel. Sie können sich denselben so vorstellen, daß Sie sich zwei Sechser ineinander verschlungen denken. Dieses Zeichen gebraucht man, um gewisse Erscheinungen, die in der ganzen natür­lichen und geistigen Welt vorhanden sind, zu kennzeichnen und ihre innere Natur zu charakterisieren. Wenn Sie eine Pflanze nehmen und betrachten, so werden Sie finden, daß sie sich bis zum Samenkorn entwickelt. Wenn Sie dieses Samenkorn in die Erde legen, so entwickelt sich eine ähn­liche Pflanze, die der alten gleich ist. Daß da etwas Stoff­liches von der alten Pflanze in die neue übergeht, ist ein materielles Vorurteil, das durch nichts gerechtfertigt ist und von der Zukunft widerlegt werden wird. In die neue Pflanze geht lediglich die bildsame Kraft über. Die alte Pflanze erstirbt stofflich ganz und gar, und die neue Pflanze ist stofflich etwas ganz Neues. Nicht das allergeringste Stoffliche geht aus der alten Pflanze in die neue über. Diesen neuen Ansatz einer Entstehung und eines Vergehens einer Pflanze bezeichnet man dadurch, daß man zwei sich inein­ander schlingende Spiralen, also einen Wirbel zeichnet, und zwar ohne eine Verbindung der beiden Linien zu bewirken.",
      "# Bild s. 195",
      "Nun finden sich solche Wirbel sowohl in der äußeren als auch in der geistigen Natur. So sagt uns zum Beispiel die Geistesforschung, daß in der Entwicklung der Menschheit einst ein solcher Wirbel vorhanden war, als die alte atlan­tische Kultur in die neue nachatlantische Kultur überging. Die Geisteswissenschaft zeigt Ihnen hier etwas, was die heutige Naturwissenschaft nur in der ersten elementarsten Stufe kennt. Sie zeigt Ihnen, daß das, was heute Meer ist zwischen Europa und Amerika, ausgefüllt war mit einem Kontinente, daß sich eine uralte Kultur da entwickelt hatte, daß durch die «Sündflut» jener Kontinent überflutet wurde und verschwand. Dies zeigt uns, daß das, was uns Plato von dem Untergang der Insel Poseidonis mitteilt, auf Rich­tigkeit beruht, und daß sie ein Rest des uralten, atlan­nschen Kontinentes war. Jene Kultur verschwand in bezug auf ihre geistige Eigenschaft, und eine neue Kultur trat auf, so daß man diesen Vorgang kennzeichnen kann mit den zwei ineinander sich schlingenden Spiralen, dem Wirbel. Das Alte wird bezeichnet durch die sich hineinschlingende Spirale, das Neue durch die sich herausschlingende.",
      "Als der Übergang von der atlantischen Kultur in die nachatlantische vor sich ging, da erschien im Frühlinge die Sonne im Sternbilde des Krebses. Sie wissen, daß die Sonne im Laufe des Jahres vorwärtsrückt. In jener alten Zeit ging sie, wie gesagt, bei Frühlingsanfang im Sternbilde des Krebses auf, dann eine Zeitlang im Sternbilde der Zwil­linge, dann im Sternbilde des Stieres und dann des Widders. Die Völker haben immer dasjenige als etwas besonders",
      "Wohltätiges empfunden, was ihnen vorn Himmeisgewölbe die ersten Sonnenstrahlen zusendet. Daher sehen Sie, daß man, als die Sonne anfing im Sternbilde des Widders aufzugehen, angefangen hat, den Widder zu verehren. Daher rühren die ganzen Lammsagen, die Sage vom goldenen Vließ und so weiter. Früher, bevor die Sonne im Sternbilde des Widders aufgegangen war, ging sie im Sternbilde des Stieres auf. Daher haben die Kulturen, welche den Widder-Kulturen vorangegangen sind, den Stier als heiliges Tier verehrt. Sie finden daher in jener Zeit zum Beispiel die Verehrung des ägyptischen Stieres Apis. In der Zeit des Überganges von der atlantischen in die nachatlantische Zeit haben Sie die Herrschaft des Sternbildes des Krebses gehabt. Und daher haben Sie die zwei ineinandergeschlungenen Wirbel als Zeichen des Krebses im Kalender.",
      "Es gibt hunderte, tausende dieser Zeichen, die man nach und nach lernt. Das sind nicht willkürliche Zeichen. Wenn man sie kennt, zeigen sie einem die Wege, um hineinzu­kriechen in die Dinge und in den Dingen zu leben. Wie das Studium den Verstand, die imaginative Erkenntnis das Gemüt ergreift, so ergreift die Erkenntnis der okkulten Schrift den Willen. Sie zeigt uns die Wege beim Schaffen und Produzieren. Wenn daher das Studium uns Erkenntnis, die Imagination Anschauung bringt, so bringt uns die Er­kenntnis der okkulten Schrift Magie, die Erkenntnis der in den Dingen schlummernden Naturgesetze, die Erkenntnis, die uns tiefer in das Wesen der Dinge hineinführt. Sie können bei vielen - meinetwegen auch bei Eliphas Levi - viele okkulte Zeichen finden. Derjenige aber, der nichts weiß von diesen Dingen, wird wenig dabei lernen können. Sie können indessen eine Andeutung darin finden, wie sie aussehen. In den Werken, die Sie darüber gedruckt finden, steht gewöhnlich Unzutreffendes. Heilig gehalten wurden",
      "von allen Völkern, von den Eingeweihten wenigstens, diese okkulten Schriftzeichen. Und wenn wir weiter zurückgehen, finden wir strenge Bestimmungen über deren Geheimhal­tung, damit diejenigen, welche solche Zeichen gebrauchen dürfen, sie nie unwürdig gebrauchen mögen. Die strengsten Strafen sind auf die Übertretung dieser Bestimmungen gesetzt.",
      "Das vierte ist das, was man die Bereitung des Steines der Weisen nennt. Was Sie darüber in der Literatur finden, ist ziemlich unzutreffend, ja sogar meistens törichtes Zeug. Wäre der Stein der Weisen das, was da geschildert wird, so hätte jeder ein Recht, darüber zu spotten. Sie werden ein Stück davon erkennen, wenn Sie meiner Betrachtung fol­gen: sie wird Ihnen einen großen Einblick geben. Am Ende des achtzehnten Jahrhunderts stand in einer ernstzuneh­menden mitteldeutschen Zeitschrift eine Notiz über den Stein der Weisen. Wer diese Notiz liest und etwas von der Sache versteht, der findet, daß der Schreiber irgendwo ein­mal etwas darüber vernommen hat. Seine Worte sind ganz richtig, aber man sieht auch, daß er seine Worte selbst nicht richtig versteht. Der Verfasser der Notiz schreibt da: Der Stein der Weisen ist etwas, was alle Menschen kennen, etwas, was die meisten Menschen oft und oft in der Hand haben, was man an vielen Orten der Erde findet und von dem nur der Mensch nicht weiß, daß es der Stein der Weisen ist. - Eine sonderbare Beschreibung ist das, wie der Stein der Weisen sein soll, und dennoch wörtlich wahr. Man muß die Sache nur richtig verstehen.",
      "Betrachten Sie einmal den menschlichen Atmungsprozeß, denn mit einer Regulierung des Atmens hängt das zusam­men, was man die Auffindung oder Bereitung des Steines der Weisen nennt. Der Mensch atmet heute Sauerstoff ein und Kohlensäure aus, also die Verbindung des Sauerstoffs",
      "mit Kohlenstoff wird ausgeatmet. Der Mensch atmet Sauer­stoff, die Lebensluft, ein und Kohlensäure, ein wirkliches Gift, aus. Mit dieser Kohlensäure kann der Mensch und das Tier nicht leben. Würden die Tiere, die geradeso atmen wie der Mensch, allein auf der Erde sein und hätten sie immer so geatmet wie heute, so würden sie die Luft um sich herum verpestet haben, und weder Tier noch Mensch könnte heute noch atmen. Woher kommt es nun, daß sie aber noch atmen können? Daher, daß die Pflanze die Kohlensäure aufnimmt, den Kohlenstoff in sich behält und den Sauerstoff wieder zurückgibt, so daß Menschen und Tiere den Sauerstoff wie­der zur Atmung benützen können. Es ist also ein schöner Wechselprozeß zwischen der Atmung der Tier- und Men­schenwelt und der Atmung oder dem Assimilationsprozeß der Pflanzenwelt - Assimilationsprozeß, damit kein pedan­tischer Gelehrter etwas dagegen einwenden kann. Der­jenige, der jeden Tag fünf Mark einnimmt und jeden Tag zwei Mark ausgibt, schafft einen Überschuß, bei ihm steht die Sache anders als bei demjenigen, der fünf Mark ausgibt und nur zwei Mark einnimmt. Ähnlich kann es auch bei der Atmung sein. Das Wesentliche aber hierbei ist, daß dieser Tauschprozeß zwischen Mensch und Pflanzenwelt besteht.",
      "Dieser Tauschprozeß ist höchst merkwürdig. Betrachten wir ihn deshalb noch einmal etwas näher. In den Menschenleib geht Sauerstoff ein, aus dem Menschenleib kommt Koh­lensäure heraus. Kohlensäure besteht aus Sauerstoff und Kohlenstoff. Die Pflanze behält den Kohlenstoff und gibt den Sauerstoff dem Menschen wieder zurück. Sie können in der Steinkohle, die Sie Jahrmillionen nach Entstehung der betreffenden Pflanze aus der Erde herausgraben, den Koh­lenstoff, welchen die Pflanze eingeatmet hat, wieder er­blicken. Der gewöhnliche Atmungsprozeß, der so verläuft, wie er eben geschildert wurde, zeigt an, wie notwendig der",
      "Mensch zu seinem Leben heute die Pflanze hat, und wie in ihm beim Atmungsprozeß etwas vorgeht, was nur ein hal­ber Prozeß ist. Er braucht die Pflanze als etwas, was nicht in ihm ist, damit sie ihm den Kohlenstoff in Sauerstoff um­wandelt.",
      "Nun gibt es eine Rhythmisierung des Atmungsprozesses in rosenkreuzerischem Sinn, über die indessen Näheres nur von Mensch zu Mensch mitgeteilt werden kann. Es kann zwar hier darauf hingedeutet werden, aber nur so, daß von einem Eingehen in Einzelheiten Abstand genommen wird. Aber der Rosenkreuzerschüler bekam und bekommt seine bestimmte Anweisung, er mußte in einer bestimmten Weise atmen, in einem bestimmten Rhythmus und mit ganz be­stimmten Gedankenformen. Dadurch wird sein Atmungs­prozeß umgewandelt. Diese Umwandlung können Sie sich nur vorstellen, wenn Sie den Ausspruch berücksichtigen:",
      "Steter Tropfen höhlt den Stein. Auch bei den höchststehen­den Menschen wird nicht von heute auf morgen der ganze innere Lebensprozeß umgestaltet, wenn in rosenkreuze­rischer Form geatmet wird. Aber dasjenige, was bei solcher Atmung im Leibe des Menschen umgestaltet wird, geht nach einer bestimmten Richtung hin, nämlich dahin, daß der Mensch in Zukunft imstande ist, in sich selbst die Koh­lensäure wieder in brauchbaren Sauerstoff umzuwandeln, so daß das, was heute draußen in der Pflanze vor sich geht:",
      "die Umwandlung der Kohlensäure in den Kohlenstoff, das, was heute die Pflanze dem Menschen abnimmt, von dem Menschen, wenn der Atmungsprozeß immer weiter und weiter wirken wird in dem Einzuweihenden, in einem eige­nen Organ bewirkt werden wird, von dem Physiologie und Anatomie noch nichts wissen, das aber gleichwohl in der Entwicklung begriffen ist. Der Mensch wird also dann selbst die Umwandlung bewirken. Statt den Kohlenstoff",
      "hinauszuatmen und an die Pflanze abzugeben, wird er ihn in sich selbst verwenden und seinen eigenen Leib mit Hilfe des Kohlenstoffes, den er vorher an die Pflanze abgeben mußte, auferbauen.",
      "Halten Sie das, was ich eben gesagt habe, zusammen mit dem, was ich von dem Ideal des heiligen Grals mitgeteilt habe: nämlich daß die reine keusche Pflanzennatur durch­gegangen sein wird durch die Menschennatur, und daß diese Menschennatur in ihrer höchsten Geistigkeit wieder bei der Pflanze von heute angekommen sein wird. Den Pflanzenprozeß in sich selbst durchzumachen, wird der Mensch einst imstande sein. Seine jetzigen Stoffe, die er in sich hat, wird er immer mehr zu jenem Ideal hinbilden, daß der Körper ein Pflanzenleib und der Träger eines viel höhe­ren und geistigeren Bewußtseins sein wird. So lernt der Schüler die Alchemie, durch die er in den Stand gesetzt wird, die Säfte und Stoffe des Menschen in Kohlenstoff um­zuwandeln. Was heute die Pflanze tut, indem sie ihren Leib aus Kohlenstoff auferbaut, das wird der Mensch einst selbst tun. Er wird sich aus Kohlenstoff eine Struktur des Leibes bilden, die die Struktur des künftigen Menschenleibes sein wird.",
      "Ein großes Geheimnis verbirgt sich hinter dem, was man die Rhythrnisierung des Atmungsprozesses nennt. Jetzt ver­stehen Sie wohl jene Andeutung über den Stein der Weisen, die in der vorhin zitierten Notiz enthalten ist. Was lernt der Mensch also bezüglich des Aufbaues seiner späteren Leibesform? Er lernt die gewöhnliche Kohle erzeugen, die auch die Substanz des Diamanten ist, um damit seinen Leib aufzubauen. Diesen Kohlenstoff wird der Mensch bei einem erhöhten und erweiterten Bewußtsein aus sich selbst ent­nehmen und in sich selbst verwenden können. Er wird seine eigene Substanz, die auf der Kohlenstoffstruktur aufgebaute",
      "Pflanzensubstanz bilden können. Das ist die Alchemie, welche zur Bildung des Steines der Weisen hinführt. Der Menschenleib selbst ist jene Retorte, die in dem Sinne ver­wandelt wird, wie es eben hier angedeutet worden ist.",
      "So verbirgt sich hinter der Regulierung des Atmungs-prozesses, hinter dem, was man oft bezüglich des Steines der Weisen, aber meist in ganz unsinniger Weise, angedeutet findet, das, was man die Auffindung oder Bereitung des Steines der Weisen nennt. Das sind die Andeutungen, wie sie erst seit kurzem aus den Rosenkreuzerschulen in die Öffentlichkeit gedrungen sind. Vergeblich werden Sie sie in Büchern suchen. Das ist ein kleiner Teil der vierten Stufe:",
      "die Aufsuchung des Steines der Weisen.",
      "Das fünfte besteht in dem, was man die Erkenntnis des Mikrokosmos, der kleinen Welt, nennt. Das führt uns auf das zurück, was Paracelsus gesagt hat und worauf ich schon oft hingewiesen habe: Alle Dinge, die um uns herum sind, würden, wenn wir aus ihnen einen Auszug nehmen könn­ten, als Extrakt den Menschen ergeben. Der Mensch hat in sich diejenigen Stoffe und Kräfte, welche als kurze Rekapi­tulation der ganzen übrigen Natur erscheinen, so daß, wenn wir die Natur um uns sehen, wir sagen können, was drau­ßen in der Natur ist, ist im großen das Urbild von dem, was in uns allen als Nachbild erscheint. Nehmen wir zum Beispiel das Licht. Was hat nun dieses Licht im Menschen bewirkt? Wenn es kein menschliches Auge gäbe, so könnte es nicht das Licht gewahr werden. Die Welt wäre finster und dunkel für uns. Aber ebenso wie Tiere, wenn sie in finstere Höhlen einwandem, wie zum Beispiel in die Höh­len von Kentucky, das Sehvermögen verlieren, so wird auf der anderen Seite das Auge vorn Lichte selbst geschaffen. Wir hätten kein Auge, wenn es kein Licht gäbe. Das Licht hat erst unsere Sehorgane aus der Haut, aus dem Organismus",
      "herausgelockt. Das Auge, hat Goethe gesagt, ist vom Licht und für das Licht, das Ohr vom Ton und für den Ton geschaffen. Alle Dinge sind aus der großen Welt, dem Makrokosmos, herausgeboren. Darin beruht das Geheim­nis, daß man unter gewissen Anleitungen und Anweisungen, durch eine Vertiefung in den Körper hinein, nicht bloß die leibliche, sondem auch die geistige Welt ergründen und die uns umgebende Natur erkennen lernen kann. Wer unter gewissen Bedingungen lernt, mit gewissen Gedankenformen sich meditativ ganz in das Innere des Auges zu versenken, der lernt die innere, wesentliche Natur des Lichtes er­kennen. Zwischen den Augenbrauen, an der Nasenwurzel, ist ein Punkt, der in dieser Beziehung auch von hoher Be­deutung ist. Wenn man sich in ihn vertieft, dann lernt man bedeutsame, wichtige Vorgänge in der geistigen Welt kennen, die sich abgespielt haben, als diese Partie des Kopfes sich aus der umliegenden Welt herausgebildet hat. So lernt man die geistige Zusammenfügung des Menschen kennen. Aus geistigen Wesenheiten und Kräften heraus ist der Mensch ganz und gar gebildet. Wenn er sich daher in seine Form vertieft, lernt er die Wesenheiten und geistigen Kräfte er­kennen, die seinen Organismus, die seine Form aufgebaut haben.",
      "Eine Bemerkung muß hier noch gemacht werden. Dieses Versenken ins Innere des Menschen, ebenso wie die anderen Übungen, die hinunterarbeiten in das Leibliche, durch die vom Ich aus in den physischen Leib hineingearbeitet wird -Atman kommt von Atmen -, sollten nicht ohne Vorberei­tung vorgenommen werden. Wenn man damit zu arbeiten anfängt, muß man eigentlich geistig schon vorgearbeitet haben. Deshalb wird in der Rosenkreuzerschulung auch streng auf Gedankenschulung gehalten. Es ist auch bei die­ser Schulung für den Schüler die große Moral, ein fester",
      "innerer Wesenskern nötig. Wenn er diese nicht hat, so kann er straucheln. In jedes Glied kann er sich meditativ versen­ken, und Welten gehen ihm in seinem Inneren auf. Niemand kann die wahre Natur des Alten Testamentes kennen­lernen ohne eine solche Versenkung in das eigentlich mensch­liche Innere, allerdings nach bestimmten Vorschriften, die ihm in der geisteswissenschaftlichen Schulung gegeben wer­den können.",
      "Alle diese Dinge sind aus der Geisteswissen­schaft, aus Einblicken in die geistige Welt heraus geschrie­ben. Daher kann man sie auch nur verstehen, wenn man imstande ist, sie wieder in sich aufzusuchen.",
      "Der Mensch ist aus dem Makrokosmos herausgeboren, und er muß als Mikrokosmos die darin wirkenden Kräfte und Gesetze wieder in sich finden. Nicht als Anatorn kann man den Menschen in sich kennenlernen. Nur dann kann man das, wenn man lernt, in sein eigenes Inneres zu blicken, das dann in einzelnen Gebieten leuchtend und tönend wird.",
      "Jedes Organ hat seine bestimmte Farbe und seinen bestimmten Ton, wenn das Ganze bloßgelegt wird vor der nach innen schauenden Seele. Wenn der Mensch durch die Rosenkreu­zerschulung in seinem Innern kennengelernt hat, was aus dem Makrokosmos heraus geschaffen worden ist, dann kann er in sich die Dinge kennenlernen, die im Makrokosmos sind.",
      "Hat der Mensch, durch Versenkung in sein Auge oder in den Punkt über der Nasenwurzel, sein Inneres erkannt, dann kann er herausgehen und die großen Gesetze im gro­ßen Kosmos geistig erkennen. Und er lernt dann aus eigener Anschauung geistig dasjenige erkennen, was ein inspirierter Genius im Alten Testament beschrieben hat, er sieht es in der Akasha- Chronik und kann die Menschheitsentwicklung durch Jahrmillionen hindurch verfolgen.",
      "Das kann man alles durch eine solche Schulung wirklich erkennen. Das ist aber eine andere Schulung als die gewöhnliche.",
      "Man darf nicht glauben, daß Selbsterkenntnis durch planloses Hineinbrüten in sich errungen wird oder daß, wenn man hineinschaut in sich, der Gott im Inneren zu sprechen anfängt, wie das heute häufig gelehrt wird. Nein, man muß in seine Organe sich vertiefen, um dann das große Selbst der Welt erkennen zu können. Wahr ist es:",
      "durch alle Zeiten geht der Spruch «Erkenne dich selbst», aber ebenso wahr ist es, daß das höhere Selbst nicht durch das eigene Innere zu erkennen ist, sondern, wie schon Goethe, der große Seher, sagt, indem man seinen Geist zum Universum erweitert. Das geschieht auf der sechsten Stufe der rosenkreuzerischen Schulung, wenn man auf diese Weise geduldig seinen Weg geht. Nicht bequem ist der Weg. Man muß in sein Wesen untertauchen. Man kann nicht zufrieden sein mit Phrasen und Allgemeinheiten. Man muß in jedes Wesen eintauchen, es liebevoll in sich aufnehmen. Jede Bequemlichkeit muß einem fremd wer­den. Untertauchen muß man in die Wesen, im Konkreten, im Besonderen die Wesen kennenlernen, nicht herumreden über, was man so nennt: Harmonie mit der Welt, Eins-werden mit der Weltenseele, Zusammenschmelzen mit der Welt. Solche Phrasen sind nichts wert gegenüber der Rosen­kreuzerschulung, die nicht von Harmonie mit dem Unend­lichen schwätzt oder sich in ähnlichen Phrasen ergeht, son­dern die Kräfte in der Menschenseele lebendig werden läßt.",
      "Wenn der Mensch sein Selbst so zu erweitern versucht hat, dann wird die siebente Stufe der Seele nicht mehr fern liegen. Dann verwandelt sich Erkenntnis in Gefühl, dann geht das, was in seiner Seele lebendig ist, in Empfindung über, und er hört auf, sich nur in sich selbst zu fühlen. Er fängt an, sich in jedem Wesen zu fühlen. Wenn er unter­getaucht ist in jeden Stein, in jede Pflanze, in jedes Tier, dann fühlt er mit Pflanze, Stein und Tier, und es sagt, es",
      "offenbart ihm jedes einzelne Ding seine Wesenheit, nicht in Worten, nicht in Begriffen, sondern im innersten Gefühl. Dann beginnt jene Zeit, wo ihn ein allgemeines Netz von Sympathie mit den Wesen verbindet, wo er sich in alle Wesen hineinlebt. Dies Hineinleben in alle Wesen nennt man die siebente Stufe, die Gottseligkeit, das selige Ruhen in allen Wesen. Wenn der Mensch sein Selbst verbunden fühlt mit allen übrigen Wesenheiten, nicht mehr in seiner Haut lebt, sondern eingegangen ist in alle Wesen, mitfühlt mit allen Wesen, wenn er ausgebreitet ist in dem ganzen Weltenraum, so daß er zu allem sagen kann: «Das bist du», wenn er ganz Gefühl, ganz Seligkeit geworden ist, dann darf das gesagt werden, was Goethe aus der Rosenkreuzer­schulung heraus in seinem Gedichte «Die Geheimnisse» ausspricht:",
      "«Wer hat dem Kreuze Rosen zugesellt?»",
      "Das darf aber nicht nur gesagt werden von dem höchsten Standpunkte, sondern von den ersten Schritten an, wo man dasjenige zu seinem Losungswort macht, was sich ausdrückt in dem von Rosen urnschlungenen Kreuz. Das Kreuz ist der Ausdruck dafür, daß der Mensch jenes Selbst, in das man hineinbrütet und das nur das niedere Selbst ist, welches niemals das höhere Selbst gewahren kann, überwindet, daß er herausgeht aus dem niederen Selbst, aufgeht in dem Höheren, das ihn selig hinein führt in das Leben und Weben von allen Wesenheiten, wenn er einsieht, was da steht in einem Gedichte des «West-Östlichen Divan» von Goethe:",
      "«Und solang du das nicht hast,",
      "Dieses:    Stirb und Werde,",
      "Bist du nur ein trüber Gast",
      "Auf der dunklen Erde.»",
      "Ja, wer es nicht verstehen kann, dieses Überwinden des eng begrenzten Selbst und dieses Aufgehen im höheren Selbst, wer es nicht begreifen kann, jenes Symbolum des Sterbens und des Werdens, das Verdorren des niederen Selbst und das Aufblühen der Rosen des höheren Selbst, der kann nicht jene Devise begreifen, die Goethe aus­gesprochen hat und mit der wir das Sachliche des Rosen­kreuzertums beschließen wollen, das Losungswort, das Zeichen der sieben Glieder, das über dem mit Rosen um­wundenen Kreuz stehen muß:",
      "«Von der Gewalt, die alle Wesen bindet,",
      "Befreit der Mensch sich, der sich überwindet.»"
    ],
    "sentences": [
      [
        "Mit den Rosenkreuzern, die uns heute beschäftigen sollen, können in unserer Zeit die wenigsten Menschen einen Be­griff verbinden, welcher der Sache auch nur einigermaßen entspricht.",
        "Es ist allerdings nicht so leicht, mit dem Namen Rosenkreuzer irgendeinen besonderen Begriff zu verbinden.",
        "Etwas Unbestimmtes scheint für viele Menschen hinter die­sem Namen zu liegen.",
        "Wenn dann der eine oder der andere in kulturhistorischen oder sonstigen Büchern nachsieht, in denen man gewohnt ist, sich über solche Sachen Rat zu holen, so findet er allerdings einige Dinge darüber gesagt, zum Bei­spiel, daß die Rosenkreuzer eine Sekte oder dergleichen in den früheren Jahrhunderten deutscher Geistesentwicklung waren.",
        "Er findet auf der einen Seite von einigen hervor­gehoben, daß man nicht richtig dahinterkommen könne, ob hinter dem vielen Schwindel und der Charlatanerie, welche sich einmal unter dem Namen des Rosenkreuzertums breit­gemacht haben, auch irgend einmal etwas Vernünftiges und Klares gesteckt haben mag.",
        "Und auf der anderen Seite fin­det er dann auch allerlei Mitteilungen in gelehrten Büchern."
      ],
      [
        "Man muß in der Tat sagen, wenn das stimmen würde, was in der einschlägigen Literatur über die Rosenkreuzer geschrieben ist, dann könnte man so ziemlich damit einver­standen sein, daß das, was sich hinter diesem Namen ver­birgt, für eitle Windbeutelei, reinen Schwindel und viel­leicht noch viel Schlimmeres zu halten ist.",
        "Und auch jene, die noch versuchen, das Rosenkreuzertum zu verteidigen,"
      ],
      [
        "entweder von oben herab oder vielleicht auch, indem sie be­merklich machen, daß sie über ein besonderes Wissen ver­fügen oder Aufschlüsse zu geben in der Lage sind, erwecken bei unseren Zeitgenossen und unseren Anschauungen kein besonderes Vertrauen.",
        "Allzuviel kommt auch bei der Ver­teidigung der Rosenkreuzer nicht heraus; insbesondere dann nicht, wenn gesagt wird: Gewiß, das Rosenkreuzertum wird in Zusammenhang gebracht mit Alchemie, mit der Bereitung des Steines der Weisen und allerlei sonstigen alchemistischen Kunststücken.",
        "Aber diese Kunststücke bedeuten dem echten, wahren Rosenkreuzer nichts als ein Sinnbild für die innere, moralische Läuterung der Seele, die Heranbildung der be­sonderen menschlichen Tugenden.",
        "Und wenn man sagt, es werde in der Rosenkreuzerei davon gesprochen, daß man unedle Metalle in Gold verwandeln könne, so sei damit nichts anderes gemeint, als daß man die unedlen Metalle der verschiedenen Menschenuntugenden in das Gold der mensch­lichen Tugenden verwandeln könne, und daß dieser Ver­wandlungsprozeß nur eine symbolische Darstellung dessen sei, wie man sich innerlich moralisch entwickeln solle."
      ],
      [
        "Wenn es so wäre, so würde die ganze Geschichte nichts weiter als eine Trivialität oder noch etwas viel Nichtigeres sein, denn es ist schlechterdings kaum einzusehen, warum man allerlei alchemistische Dinge wie Metallverwandlung und so weiter erfinden sollte, um ein so auf der Hand liegen­des Ding zu demonstrieren, daß der Mensch sich läutern und seine Untugenden verwandeln solle.",
        "Dieser Einwand kann immer gegen diejenigen gemacht werden, die das große Werk des Rosenkreuzertums wie etwas bloß Symbolisches auffassen.",
        "Aber in der Tat steckt etwas viel Tieferes da­hinter."
      ],
      [
        "Nicht länger möchte ich mich bei dem Geschichtlichen aufhalten.",
        "Das Geschichtliche soll uns heute, wo ich eine"
      ],
      [
        "sachliche Auseinandersetzung über das Rosenkreuzertum zu geben beabsichtige, wenig angehen.",
        "Das Geschichtliche braucht uns nicht weiter zu berühren, als nur insofern wir dadurch erfahren, daß das Rosenkreuzertum eine Grün­dung, eine Stiftung ist, die seit dem vierzehnten Jahrhun­dert tatsächlich im Abendlande besteht, daß sie zurückgeht auf eine Persönlichkeit, welche fast sagenumwoben ist, wie man bemerken könnte, von der aber die Geschichte nicht viel zu melden weiß: Christian Rosenkreuz."
      ],
      [
        "Was nun aus den verschiedenen Mitteilungen als ein ge­wisser Grundklang hervorgeht, ist dahin zusammenzufas­sen, daß Christian Rosenkreuz - so ist zwar nicht sein wah­rer, wohl aber derjenige Name, unter dem er bekannt geworden ist - am Ende des fünfzehnten und im Beginne des sechzehnten Jahrhunderts auch Reisen gemacht habe, und daß er auf seinen Reisen durch das Morgenland das sogenannte Buch ... kennengelernt habe, jenes Buch, von dem uns sehr geheimnisvoll gesagt wird, daß Paracelsus, der große mittelalterliche Arzt und Mystiker, sein Wissen daraus geschöpft habe.",
        "Dies ist wirklich eine wahre Tatsache, doch nur die Eingeweihten wissen: erstens, was das Buch M... ist, und zweitens, was das Studium im Buche ... . bedeutet."
      ],
      [
        "Die äußere Welt ist immer wieder hingewiesen worden auf das Rosenkreuzertum durch die beiden Schriften, die vom Anfange des siebzehnten Jahrhunderts stammen.",
        "Im Jahre 1614 erschien die sogenannte «Fama Fraternitatis» und ein Jahr später die sogenannte «Confessio» - zwei Bü­cher, über die von gelehrter Seite viel gestritten worden ist.",
        "Und zwar nicht nur darüber, worüber bei so vielen Büchern sonst gestritten wird, ob jener Valentin Andreae, der in seinen späteren Lebensjahren ein ganz normaler Super­intendent war, auch wirklich das Buch verfaßt hat -, sondern"
      ],
      [
        "bei diesen Büchern ist auch darüber gestritten worden, ob sie von den Verfassern ernst genommen worden sind, oder ob sie nur ein Spott darüber sein sollten, daß es eine gewisse geheimnisvolle Brüderschaft des Rosenkreuzes gäbe, welche diese und jene Tendenzen und Ziele habe.",
        "Dann gibt es im Gefolge dieser Schriften eine ganze Reihe anderer, die allerlei aus dem Bereiche des Rosenkreuzertums mitteilen.",
        "Wenn Sie die Schriften von Valentin Andreae und auch an­dere rosenkreuzerische Schriften in die Hand nehmen, dann werden Sie, wenn Sie die eigentliche Grundlage des Rosen­kreuzertums nicht kennen, in diesen Schriften nichts beson­deres finden.",
        "Denn es ist überhaupt bis in unsere Zeit hinein nicht möglich gewesen, auch nur das Elementarste aus dem Bereiche dieser Geistesströmung, die seit dem vierzehnten Jahrhundert wirklich existiert hat und auch heute noch existiert, kennenzulernen.",
        "Alles, was in die Literatur über­gegangen ist, was geschrieben und gedruckt worden ist, sind einzelne Bruchstücke, einzelne verlorene, durch Verrat an die Öffentlichkeit gekommene Dinge, die ungenau und in vielfacher Weise durch Charlatanerie, Schwindel, Unver­stand und Dummheit verkehrt worden sind.",
        "Die wahre, echte Rosenkreuzerei ist, seitdem sie besteht, stets nur Ge­genstand mündlicher Mitteilung an solche gewesen, welche sich eidlich zur Geheimhaltung verpflichten mußten.",
        "Daher ist auch nichts Erhebliches in die öffentliche Literatur über­gegangen.",
        "Erst dann, wenn man dasjenige kennt, was heute"
      ],
      [
        "- aus gewissen Gründen, die zu erläutern jetzt zu weit füh­ren würde - in der elementaren Rosenkreuzerei öffentlich mitgeteilt werden kann und wovon wir heute werden spre­chen können, kann man in den oftmals grotesken, oft bloß komischen, oft aber auch schwindelhaften und selten stim­menden Mitteilungen der Literatur einigen Sinn finden."
      ],
      [
        "Die Rosenkreuzerei ist eine der Methoden, wie man die"
      ],
      [
        "sogenannte Einweihung erreichen kann.",
        "Was Einweihung heißt, davon ist des öfteren an dieser Stelle schon die Rede gewesen.",
        "Einweihen heißt, die in jeder Menschenseele schlum­mernden Fähigkeiten erwecken, durch die man hineinsehen kann in die geistigen Welten, die hinter unserer sinnlichen Welt liegen, und von denen unsere sinnliche Welt nur ein äußerer Ausdruck, eine Wirkung ist.",
        "Ein Eingeweihter ist derjenige, welcher die genau bestimmten, wissenschaftlich durchgearbeiteten Methoden der Einweihung angewendet hat, Methoden, die ebenso wissenschaftlich durchgearbeitet sind wie diejenigen der Chemie, der Physik oder anderer wissenschaftlicher Gebiete.",
        "Dasjenige, was in solchen Metho­den durchgemacht wird, ist allerdings nicht etwas, was der Mensch auf etwas Äußeres anzuwenden hat, sondern was sich zunächst nur auf ihn selbst bezieht, auf das Instrument, das Werkzeug, durch das man in die geistige Welt hinein-sieht.",
        "Der wirkliche Geisteskenner weiß, wie tief und wahr Goethes Ausspruch ist:"
      ],
      [
        "Geheimnisvoll am lichten Tag"
      ],
      [
        "Läßt sich Natur des Schleiers nicht berauben,"
      ],
      [
        "Und was sie deinem Geist nicht offenbaren mag,"
      ],
      [
        "Das zwingst du ihr nicht ab mit Hebeln und mit Schrauben."
      ],
      [
        "Tief, tief sind die Geheimnisse der Natur, aber nicht un­ergründlich tief, wie manche sagen möchten, die im höheren Sinne nur zu bequem sind, in die Geheimnisse der Natur einzudringen.",
        "Nicht unergründlich tief sind sie, sondern zu ergründen durch den Menschengeist, zwar nicht durch den Alltagsgeist, aber den Menschengeist, der verborgene Kräfte der Seele durch gewisse, streng umschriebene Methoden aus sich herausholt.",
        "Wenn der Mensch sich nach und nach vorbe­reitet, dann gelangt er allmählich dazu, dasjenige geoffen-bart zu erhalten, was als ein Wissen nur denen zukommt,"
      ],
      [
        "die wirklich eingeweiht sind: jenes große Geheimnis, von dem, was, um mit Goethes Ausspruch zu sprechen, «die Welt im Innersten zusammenhält».",
        "Die Enthüllung die­ses Geheimnisses ist eigentlich die Frucht der wirklichen Einweihung."
      ],
      [
        "Es ist hier des öfteren auseinandergesetzt worden, daß die ersten Stufen der Einweihung durchaus gefahrlos für jeden zu durchwandern sind, daß aber die höheren Stufen die größtmöglichste menschliche Hingabe an die unbeding­teste Wahrheitserforschung verlangen.",
        "Wenn der Mensch sich jenen Pforten nähert, durch die er einen Einblick ge­winnen kann in ganz andere Welten, dann weiß er aller­dings, daß etwas von Wirklichkeit steckt hinter der oftmals gebrauchten Redensart, daß es gefährlich ist, großen Men­schenmengen die heiligen Geheimnisse des Daseins mitzu­teilen."
      ],
      [
        "Soweit es heute möglich ist und soweit es geschehen kann, die Menschen dazu vorzubereiten, allmählich den Weg finden zu können, zu den höchsten Geheimnissen der Natur und der geistigen Welt, soweit ist es auch möglich, die höheren Geheimnisse zu enthüllen.",
        "Was man die geistes-wissenschaftliche Bewegung nennt, ist ein Pfad, der er­schlossen ist, die Menschen dahin zu führen, daß sie den Weg zu den höheren Geheimnissen finden können."
      ],
      [
        "Solcher Wege zu den höheren Geheimnissen gibt es eine ganze An­zahl.",
        "Nicht als ob die letzte Weisheit, die der Mensch er-ringen kann, viele Gestalten annehmen könnte; das ist nicht der Fall.",
        "Die höchste Weisheit ist eine einheitliche."
      ],
      [
        "Wo und wann auch immer Menschen leben oder gelebt haben, wenn sie einmal zur höchsten Weisheit gekommen sind, dann ist diese höchste Weisheit für alle Menschen eine einheitliche, wie der Ausblick vom Gipfel eines Berges, wenn man ganz oben sich befindet, ein einheitlicher ist.",
        "Aber es gibt ver­schiedene Wege, um zum Gipfel des Berges hinaufzugelangen,"
      ],
      [
        "und man wird denjenigen Weg wählen, welcher von dem Ausgangspunkte aus, an dem man sich befindet, der geeignetste ist.",
        "Wenn man an einem gewissen Punkte des Berges steht und einen Weg vom eigenen Standpunkte haben kann, so wird man nicht erst um den Berg herumgehen."
      ],
      [
        "So ist es auch mit dem Weg, der zu der höchsten Erkenntnis hin aufführt.",
        "Hier handelt es sich darum, daß die Ausgangs­punkte, die man zu wählen hat, von der Menschennatur aus zu nehmen sind.",
        "Das, was hier in Betracht kommt, beachten die Menschen heutzutage viel zu wenig: Es ist die große Verschiedenheit der menschlichen Natur zu berücksichtigen."
      ],
      [
        "Anders organisiert als heute waren, wenn auch vielleicht nicht für die grobe Anatomie und Physiologie, aber für die feinere Geistesforschung, jene höheren Glieder des alten indischen Volkes, so daß es möglich war, bis heute eine wunderbare Geheim- oder Geisteswissenschaft zu bewahren und auch die dazugehörige Methode der Einweihung: die sogenannte Yoga-Schulung.",
        "Diese orientalische Yoga-Schu­lung ist der Weg, welcher zu dem Gipfel der Erkenntnis hinaufführt bei einer so organisierten Natur, wie die An­gehörigen des alten indischen Volkes sie hatten."
      ],
      [
        "Für den heutigen Europäer würde derselbe Weg so unsinnig sein, wie wenn jemand, der an einem bestimmten Fußpunkte eines Berges steht, erst um den Berg herumgehen wollte, um einen Weg zu suchen und zu benützen.",
        "Die Natur des heutigen Europäers ist ganz anders als die orientalische Natur."
      ],
      [
        "An­ders als heute war auch die menschliche Natur organisiert um die Zeit der Entstehung des Christentums herum, einige Jahrhunderte vorher und einige nachher."
      ],
      [
        "Wenn wir daran festhalten, was eben gesagt worden ist, daß Einweihung soviel bedeutet wie innere Kräfte heraus­zuholen, innere Kräfte zu erwecken durch bestimmte Metho­den, so daß der Mensch das Instrument wird, durch das er"
      ],
      [
        "in die geistige Welt hineinschauen und sie erforschen kann, dann müssen wir zugeben, daß auf diese Menschennatur Rücksicht genommen werden muß.",
        "So wie die alten heiligen Rishis, jene großen Lehrer des alten indischen Volkes, die wunderbare Methode ausgearbeitet haben, die heute noch immer für die Angehörigen des indischen Volkstums ihre Gültigkeit hat, so wie im Anfange des Christentums die christlich-gnostische Methode hinaufführen mußte in die geistigen Gebiete, so muß für den modernen Menschen, für den Menschen, der in unserer heutigen Umwelt lebt, wenn er ganz und gar dieser heutigen Welt angehört und aus die­ser die Bedingungen seines Daseins schöpft, eine andere Methode die taugliche sei.",
        "Deshalb erneuern die großen Meister der Weisheit, welche die Menschengeschicke leiten, im Laufe der Jahrhunderte und Jahrtausende immer wie­der und wieder die Methoden, durch die der Gipfel der Weisheit erreicht werden kann.",
        "Für die heutige Menschheit, für den Menschen, der aus den modernen Bedingungen des Daseins herausgewachsen ist, sind gerade von der rosen­kreuzerischen Strömung die rosenkreuzerischen Methoden begründet worden.",
        "Sie sind also Einweihungsmethoden, die geradeso zum Gipfel der Weisheit hinaufführen wie andere Methoden, nur daß sie auf besondere, augenblicklich vor­handene Bedingungen des modernen Menschen eingehen."
      ],
      [
        "Nicht sind etwa die rosenkreuzerischen Methoden un­christlich oder antichristlich.",
        "Davon kann keine Rede sein.",
        "Dasjenige, was das Christentum dem Menschen an Schulung bieten kann, das wird auch in der rosenkreuzerischen Me­thode geboten.",
        "Aber zu gleicher Zeit erwirbt sich derjenige, der eine Rosenkreuzerschulung durchmacht, die Fähigkeit, die geheim- und geisteswissenschaftlichen Errungenschaften in vollem Einklang zu sehen mit der ganzen modernen Bil­dung, mit alledem, was modernes Fühlen und moderne Anschauung"
      ],
      [
        "von der Natur des Geistes notwendig macht.",
        "Für lange Jahrhunderte in die Zukunft hinein werden die rosen­kreuzerischen Methoden die richtigen Methoden der Ein­weihung in das geistige Leben sein.",
        "Als sie begründet wor­den sind, galten für ihre Anhänger gewisse Regeln.",
        "Diese Regeln gelten im Grunde genommen auch heute noch.",
        "Weil diese Regeln streng eingehalten werden von allen denen, die wirklich Rosenkreuzer sind, deshalb ist es für Außen­stehende unmöglich, den Rosenkreuzer zu erkennen.",
        "Nie erkenne einer den anderen, das ist die erste Regel, die nur in letzter Zeit eine kleine Änderung erfahren hat.",
        "Ihr sollt die Weisheit im engsten Kreise pflegen, Ihr sollt aber die Resultate, die Früchte der Weisheit allen Menschen zugäng­lich machen.",
        "Deshalb trug der Rosenkreuzer bis vor kurzem dasjenige, wodurch er in die Tiefe der Natur hineinschaut, niemals vor das Publikum.",
        "Keine Theorie, kein Begriff, keine Idee, nichts von irgendwelchen Vorstellungen und Erkennt­nissen wurde da gegeben, sondern Arbeiten wurden geleistet, welche die Kultur vorwärtsbringen und wodurch die Weis­heit dem Volke in einer Weise eingeimpft wurde, daß die Außenstehenden nicht viel davon merken konnten."
      ],
      [
        "Das ist der erste Grundsatz, den weiter auszuführen zu weit führen würde, und in bezug auf dessen Kern ich nur bemerken wollte, daß er heutzutage zum Teil durch­brochen wird, daß aber die höhere rosenkreuzerische Weis­heit nicht verkündet werden darf.",
        "Der zweite Grundsatz bezieht sich auf die Art des Auftretens und heißt: Gehe auf in derjenigen Volksmasse und derjenigen Kulturströmung, in die du hineingestellt worden bist.",
        "Sei ein Mitglied des Volkes und Standes der Bildungs- und der Kulturstufe, in die du hineingestellt worden bist.",
        "Trage kein besonderes Kleid, wie es gewöhnlich ausgedrückt wird, trage das all­gemeine Kleid, welches die anderen tragen. - Daher werden"
      ],
      [
        "Sie als eine Art und Weise finden, daß der Rosenkreuzer da, wo er wirkt, möglichst wenig aus der Ehrsucht und aus der Selbstsucht heraus zu wirken sucht.",
        "Er wird versuchen, da und dort an Kulturströmungen anzuknüpfen, bestrebt sein, sie zu vertiefen und das Vorhandene zu gebrauchen, aber er wird immer im Auge haben etwas, was noch viel tiefer ist, was ihn verbindet mit der Zentralweisheit des Rosenkreuzertums selbst.",
        "Die anderen Grundsätze brau­chen uns jetzt nicht zu beschäftigen, denn wir wollen uns jetzt mit der Rosenkreuzerschulung befassen, wie sie seit Jahrhunderten bestanden hat und noch besteht.",
        "Die Dinge, die mitgeteilt werden können, sind in gewisser Beziehung elementar, sind nur der Anfang des ganzen Systems der Rosenkreuzerschulung.",
        "Es muß aber gesagt werden, daß von dieser Schulung dasselbe gilt, was von jeder geisteswissenschaftlichen Schulung gesagt werden kann: daß die Menschen nicht literarisch suchen sollen, sondern nur dann sich praktisch mit der Sache beschäftigen möchten, wenn sie die persönliche Anleitung eines Wissenden haben.",
        "Alles, was man in dieser Beziehung sagen kann, finden Sie in der Zeit­schrift «Luzifer-Gnosis» von Nr. 13 an unter dem Titel:"
      ],
      [
        "«Wie erlangt man Erkenntnisse der höheren Welten?»"
      ],
      [
        "Was bei der Rosenkreuzerschulung zwecks Eintretens in die geistige Welt der Schüler zu absolvieren hat, sind fol­gende sieben Stufen.",
        "Diese brauchen nicht etwa in der Rei­henfolge, wie ich sie aufzählen werde, von dem Schüler durchgemacht zu werden.",
        "Der Lehrer wird, je nach der In­dividualität des Schülers, aus dem einen oder dem anderen Punkte dasjenige herausheben, was gerade für den Schüler notwendig ist, und wird so eine Art von Lehrgang, eine Art von innerem Entwicklungsgang dem betreffenden Schüler persönlich zu geben haben.",
        "Hier muß man aber die Stufen der Rosenkreuzerschulung aufzählen.",
        "Es sind sieben:"
      ],
      [
        "Was man im rosenkreuzerischen Sinne «Studium» nennt."
      ],
      [
        "Was man als Aneignung der sogenannten imagina­tiven Erkenntnis bezeichnet."
      ],
      [
        "Was man die Aneignung der okkulten Schrift nennt."
      ],
      [
        "Was man entweder mit dem anspruchslosen Wort be­zeichnet: Rhythmisierung des Lebens, oder auch, und zwar im wahrhaftigen Sinne: die Bereitung des Steins der Weisen.",
        "Das ist etwas, was es gibt, was nur nicht jenes törichte Ding ist, von dem Sie in Büchern lesen können."
      ],
      [
        "Was man die Erkenntnis des Mikrokosmos, das heißt der eigenen menschlichen Natur nennt."
      ],
      [
        "Was man nennt: das Aufgehen in den Makrokosmos oder in die große Welt draußen."
      ],
      [
        "Was man nennt: die Erreichung der Gottseligkeit."
      ],
      [
        "In welcher Aufeinanderfolge der Schüler diese Stufen durchmacht, das hängt ganz von seiner Individualität ab.",
        "Durchmachen aber muß er sie in der elementaren Rosen­kreuzerschulung.",
        "Betrachten Sie das, was ich Ihnen bezüg­lich der Rosenkreuzerschulung gesagt habe und was ich jetzt noch charakterisieren werde, als eine Art Ideal.",
        "Glau­ben Sie nicht, daß man es von heute auf morgen ausführen kann, aber man muß das, was einem heute noch fernsteht, seinem tieferen Inhalte nach, wenigstens dem Wortlaute nach kennenlernen.",
        "Beginnen kann der Mensch zu jeder Zeit, wenn er sich bewußt ist, daß er Geduld, Energie und Ausdauer haben muß."
      ],
      [
        "Der erste Punkt, das Studium, schließt ein Wort ein, das für viele pendantisch klingt.",
        "Es wird aber keine Gelehrsam­keit darunter verstanden.",
        "Um Eingeweihter zu sein, braucht man nicht gelehrt zu sein.",
        "Gelehrsamkeit hat mit geistiger"
      ],
      [
        "Erkenntnis nicht allzuviel zu tun.",
        "Unter dem Studium, um das es sich hier handelt, ist etwas anderes zu verstehen.",
        "Die­ses Studium ist aber unerläßlich, und niemand darf durch einen wirklich kundigen Lehrer der Rosenkreuzerei in höhere Stufen eingeführt werden, wenn er nicht Neigung hat, die Stufe des Studiums wirklich durchzumachen.",
        "Durch das Studium soll sich der Schüler ein völlig vernünftiges, ganz und gar logisches Denken aneignen, ein Denken, wel­ches ihn davor bewahrt, beim Durchgang durch die folgen­den Stufen - wie das leicht sein könnte - den Boden unter den Füßen zu verlieren.",
        "Es muß durchaus festgehalten wer­den, daß derjenige, der eintreten soll in die geistige Welt, sie vorher kennenlernen soll, da sie in manche Irrpfade hin­einführen kann, welcher Gefahr er nur dann entgeht, wenn er alles Phantastische, alles Unlogische, alles, was irgend­wie unvernünftig sein könnte, vor allen Dingen abgelegt hat.",
        "Ein Phantast, der sich Vorstellungen über allerlei Un-wirkliches macht, ist nicht zu gebrauchen für die geistige Welt."
      ],
      [
        "Das ist der eine Grund.",
        "Der andere Grund ist der, daß man, wenn man in die höheren Welten kommt, das Mannigfaltigste an Wahrnehmungen erfährt, was durch und durch verschieden ist von dem, was uns hier in der Sinnenwelt umgibt.",
        "Derjenige, welcher hineinschauen kann"
      ],
      [
        "- wenn ihm die inneren Sinne der Seele geöffnet werden -in die uns am nächsten befindlichen geistigen Welten, die wir gewohnt sind, die astrale und geistige Welt zu nennen, in die Welten, aus denen der Mensch ebenso herausgeboren ist wie aus der physischen Welt, lernt Dinge kennen, die grundverschieden sind von den Wahrnehmungen in unserer Sinnenwelt.",
        "Wer die astrale oder geistige Welt betritt, weiß, wie grundverschieden diese Welten sind von dem, was er hier mit Augen zu sehen, mit Ohren zu hören gewohnt ist."
      ],
      [
        "Aber eines ist gleich durch alle drei Welten, durch die phy­sische, astrale, geistige oder devachanische Welt, und das ist das logische Denken.",
        "Weil das logische Denken in allen drei Welten dasselbe ist, deshalb kann es hier in dieser physi­schen Welt schon gelernt werden, so daß wir durch dasselbe eine feste Stütze in den anderen Welten haben werden.",
        "Lernt man aber so denken, daß der Gedanke irrlichteliert, so daß man nicht unterscheiden kann Phantasiegebilde von Wirklichkeit, so daß man zum Beispiel, wie unsere Physiker heute es tun, Atome, die niemand in unserer physischen Welt gesehen hat, wie etwas Wirkliches behandelt, gibt man sich solchen Phantasien schon in der physischen Welt hin, dann ist man nicht fähig, sich hinaufzuheben in die höheren Welten.",
        "Denken Sie sich einmal, was ein Mensch, der nicht an strenge und unerbittliche Logik gewohnt ist, von den höheren Welten für Zeug erzählen könnte."
      ],
      [
        "Nun handelt es sich allerdings nicht um das, was man im gewöhnlichen Sinne Denken nennt.",
        "Das gewöhnliche Den­ken ist nur ein Kombinieren sinnlicher Wirklichkeiten.",
        "Hier handelt es sich aber um ein Denken, das sinnlichkeitsfrei geworden ist.",
        "Gelehrte und Philosophen leugnen heutzu­tage ein solches Denken überhaupt.",
        "Sie können bei vielen Philosophen, die heute einen großen Namen haben, nach­lesen, daß der Mensch nicht in bloßen Gedanken denken könne, sondern immer nur in solchen Gedanken denken müsse, die einen Rest von sinnlichen Bildern enthalten.",
        "Wenn ein Philosoph das sagt, dann beweist das nichts wei­ter, als daß er nicht in reinen Gedanken denken kann, und es ist eine unbeschreibliche Unbescheidenheit, wenn man das, was man selber nicht kann, als eine allgemeine Un­fähigkeit hinstellt.",
        "Der Mensch muß imstande sein, sich Gedanken zu bilden, die nicht mehr von Wahrnehmungen der Augen und Ohren abhängig sind, so daß er in einer"
      ],
      [
        "reinen Gedankenwelt schweben kann, in der Welt, die er in sich selber findet, wenn er die Aufmerksamkeit von den äußeren, sinnlichen Wirklichkeiten ablenkt.",
        "Dieses Denken nennt man in der Geisteswissenschaft und auch im Rosen­kreuzertum das sich selbst erzeugende Denken.",
        "Derjenige, der nichts anderes tun will, um ein solches Studium zu ab­solvieren, mag die Lehrbücher der heutigen Geisteswissen­schaft vornehmen.",
        "Das, was Sie da finden, sind nicht bloß sinnnliche Kombinationen, sondern Gedanken, die aus höhe­ren Welten stammen, Gedanken, die ein geschlossenes Den­ken darstellen, das jeder verstehen kann, so daß er nicht bei der gewöhnlichen, trivialen Art des Denkens stehenzublei­ben braucht."
      ],
      [
        "Um die erste Stufe der Rosenkreuzerschulung möglich zu machen, ist es nötig, daß das, was seit Jahrhunderten im engsten Kreise behütet worden ist, durch Literatur und Vorträge der Menschheit zugänglich gemacht wird.",
        "Was zu­gänglich gemacht wird, ist aber nichts anderes als das Ein­maleins, der Anfang des großen und unermeßlichen Weltenwissens.",
        "Mit der Zeit wird immer mehr davon in die Mensch­heit einfließen.",
        "Seit einigen Dezennien ist der elementare Teil desselben der Menschheit enthüllt worden.",
        "Daran kön­nen Sie Ihr Denken schulen.",
        "Für diejenigen, die das gründ­licher machen wollen, die also in eine solche strenge Schu­lung des Denkens eintreten wollen, sind meine beiden Bücher «Wahrheit und Wissenschaft» und «Die Philosophie der Freiheit» bestimmt.",
        "Diese Bücher sind nicht so geschrieben wie andere Bücher, daß sie einen Satz einer bestimmten Stelle auch an eine andere Stelle des betreffenden Buches setzen könnten.",
        "Diese Bücher sind keine Gedanken-Aggre­gate, sondern Gedanken-Organismen.",
        "Ein Gedanke wächst wie ein Organismus, er wächst organisch aus dem anderen heraus.",
        "Diese Bücher sind also nicht so geschrieben, daß einfach"
      ],
      [
        "ein Gedanke zum anderen hinzugefügt wird, sondern so, daß die späteren Gedanken aus den vorhergehenden her-ausgewachsen sind wie bei einem Organismus.",
        "So müssen in dem Leser auch die Gedanken herauswachsen, er muß spü­ren, wie er hingetrieben wird zu dem Denken; und dann macht er sich jene eigentümliche Art des Denkens, das sich selbst erzeugende Denken, zu eigen, ohne welches man die höheren Stufen der rosenkreuzerischen Schulung nicht er­langen kann, obgleich diese gründlichere Art nicht absolut notwendig ist und man sehr gut bei der geisteswissenschaft­lichen, elementaren Literatur bleiben kann, da diese den Stoff für das Studium auch abzugeben vermag."
      ],
      [
        "Das zweite ist die Aneignung des imaginativen Denkens.",
        "Dasjenige, was ich imaginatives Denken nenne, sollte man sich erst aneignen, wenn man auf diese Weise strenge innere Gedankennotwendigkeit in sich aufgenommen hat, so daß man einen strengen Wissenskern besitzt.",
        "Man kann sonst leicht den Boden unter den Füßen verlieren.",
        "Was ist nun imaginatives Denken?",
        "Goethe, der in seinem rosenkreuzeri­schen Gedicht «Die Geheimnisse» gezeigt hat, wie tief er in die rosenkreuzerischen Geheimnisse eingeweiht war, gibt einen Hinweis in einem schönen Spruch des Chorus Mysti­cus im zweiten Teil des Faust, wo er das Geleitwort ge­geben hat: «Alles Vergängliche ist nur ein Gleichnis.» Dies wurde überall, wo eine innere rosenkreuzerische Schulung vorhanden war, in systematischer Weise entwickelt.",
        "Der Rosenkreuzer mußte fähig werden, durch die ganze Welt zu gehen und neben der logischen Erkenntnis sich die ima­ginative Erkenntnis derselben anzueignen, diejenige Er­kenntnis, die in allem, was um uns herum ist, ein Geistiges, ein Unvergängliches sieht.",
        "Wenn Sie einem Menschen gegen-übertreten und Sie sehen auf seinem Antlitz ein heiteres Lächeln, dann werden Sie nicht dabei stehenbleiben, nur"
      ],
      [
        "jene eigentümlichen Windungen im Gesicht, die Physio­gnomie, die sich Ihrem Auge darbietet, zu beschreiben.",
        "Es wird vielmehr Ihre Seele sich klar sein darüber, daß in jenem eigentümlichen Ausdruck der Heiterkeit sich das innere Leben der Seele verrät, ebensowenig wie Sie bei per­lenden Tränen dabei stehenbleiben werden, sie zu unter­suchen."
      ],
      [
        "Sie werden sich klar darüber sein, daß die Tränen der Ausdruck inneren Schmerzes, inneren Leides sind.",
        "Das Äußere ist Ausdruck des Inneren.",
        "Sie sehen in der Physio­gnomie bis auf den Grund der Seele.",
        "Der ganzen übrigen Natur gegenüber muß das der Rosenkreuzerschüler lernen."
      ],
      [
        "So wie das menschliche Antlitz und die Bewegung der Hände Ausdrucksmittel sind für das menschliche Seelenleben, so ist alles, was in der Natur vorgeht, Ausdruck eines seelisch-geistigen Lebens.",
        "Wie die Geste Ausdruck für unsere Seele ist, so wird für den Rosenkreuzer alles - nicht bloß als poetisches Bild, sondern als tiefe Wirklichkeit -, die ganze Erde um uns herum der Ausdruck seelisch-gei­stigen Lebens: die Steine, Pflanzen und Tiere, die Sterne, jeder Luftzug."
      ],
      [
        "Alles, was um uns herum ist, wird so der Ausdruck von Seelisch-Geistigem, nicht etwa in poetischer Beziehung, sondern in Wirklichkeit, wie das leuchtende Auge, die sich runzelnde Stirne, die perlende Träne physio­gnomische Ausdrücke innerer Seelenzustände sind.",
        "Dann erst wissen Sie, was imaginative Erkenntnis heißt, wenn Ihnen das, was Goethe in seinem Faust vom Erdgeiste sagt, nicht mehr ein poetisches Bild, sondern Wirklichkeit ist, wenn Sie bei dem heutigen materialistischen Sinn unserer Bevölkerung nicht stehenbleiben, sondern bei dem Worte des Erdgeistes Wirklichkeit zu erkennen vermögen, wäh­rend man heute froh ist, wenn man ein poetisches Bild darin genießen kann:"
      ],
      [
        "In Lebensfluten, im Tatensturm"
      ],
      [
        "Wall' ich auf und ab,"
      ],
      [
        "Webe hin und her!"
      ],
      [
        "Geburt und Grab,"
      ],
      [
        "Ein ewiges Meer,"
      ],
      [
        "Ein wechselnd Weben,"
      ],
      [
        "Ein glühend Leben,"
      ],
      [
        "So schaff' ich am sausenden Webstuhl der Zeit"
      ],
      [
        "Und wirke der Gottheit lebendiges Kleid."
      ],
      [
        "Wenn Ihnen diese Worte des Erdgeistes Wirklichkeit geworden sind und Sie es ruhig aushalten können, daß Sie von Materialisten für einen Narren gehalten werden, da Sie wissen, daß Sie eine tiefere Logik haben, da Sie wissen, daß jene phantastischer sind und nur zu wissen glauben, daß Sie aber wissen, daß Sie einer freien Wirklichkeit des Gei­stes gegenüberstehen, und ebenso wahr und wirklich, wie eine menschliche Seele in den Physiognomien lebt, auch in der Erdphysiognomie ein Erdgeist lebt.",
        "Wenn Sie in einer Pflanze die Heiterkeit des Erdgeistes erblicken, wenn die Erde Ihnen der Ausdruck des leiderfüllten Erdgeistes wird, wenn Ihnen die Natur so erscheint, als wenn sie zu Ihnen spräche, wie wenn sie Ihnen ihr Geheimnis wirklich mit­teilte, wenn Sie das erleben, dann fangen Sie an, ihre Ge­heimnisse zu buchstabieren und zu verstehen, was es heißt:"
      ],
      [
        "imaginative Erkenntnis zu erwerben.",
        "Dann kommen Sie dahin, zu verstehen, wie dies im Rosenkreuzertum und auch bei den Vorfahren des Rosenkreuzertums in dem großen okkulten Ideal des heiligen Grals hingestellt worden ist als dem reinsten und schönsten Ausdruck für das Streben nach Imaginativer Erkenntnis."
      ],
      [
        "Lassen Sie uns einmal einen Blick werfen auf die wahre Natur dieses Ideals vom heiligen Gral.",
        "Es tritt Ihnen in"
      ],
      [
        "jeder Rosenkreuzerschule in der Weise vor Augen, wie ich es jetzt charakterisieren will.",
        "Ich benutze hierzu die Form eines Dialogs, der aber niemals in wirklichen Rosenkreuzer­schulen gehalten worden ist.",
        "Da wurde durch lange Ent­wicklungsmethoden im Leben das erreicht, was ich jetzt im Dialog zusammenfassen will.",
        "Er gibt das, was das Ideal des heiligen Grals wirklich enthält."
      ],
      [
        "Sieh Dir an die Pflanze, wie sie herauswächst aus der Erde.",
        "Ihre Wurzel ist in den Boden hineingesenkt, sie ist nach dem Mittelpunkt der Erde hin gerichtet, der Stengel strebt nach oben, die Blüte nach oben öffnend, darinnen die befruchtenden Organe, die den Samen zeugen werden, wodurch die Pflanze über sich selbst hinauslebt.",
        "Nicht erst Darwin, der große Naturforscher, hat davon gesprochen, daß, wenn man die Pflanze mit dem Menschen vergleicht, nicht die Blüte, sondern die Wurzel mit dem Kopfe ver­glichen werden müsse.",
        "Die Wurzel der Pflanze entspricht dem Kopfe des Menschen - so sagte schon der Rosenkreuzer-Okkultismus-, und dasjenige, was von der Pflanze als Blütenkelch der Sonne keusch entgegenstrebt, das ist das, was der Mensch als Befruchtungsorgane nach unten wendet.",
        "Der Mensch ist eine umgekehrte Pflanze.",
        "Er wen­det die Organe, welche die Pflanze keusch nach oben dem Lichte zuwendet, schamvoll nach unten und verhüllt sie.",
        "Der Mensch ist die umgekehrte Pflanze: das ist ein Grund­satz des Rosenkreuzer-Okkultismus und des Okkultismus aller Zeiten.",
        "Die Pflanze ist mit den Befruchtungsorganen keusch der Sonne zugewendet.",
        "Der Mensch hat die Befruch­tungsorgane nach dem Mittelpunkte der Erde gerichtet, den Kopf frei nach dem Sonnenraum hinaus.",
        "Zwischen beiden, mitten drinnen, steht das Tier.",
        "Die drei Richtungen, die sich durch die Pflanze, das Tier und den Menschen ergeben, bezeichnet man als das Kreuz.",
        "Die Pflanze ist der Balken,"
      ],
      [
        "der nach unten geht, das Tier ist der Querbalken, der Mensch ist der Balken nach oben.",
        "Wenn Plato, der große eingeweihte Philosoph des Altertums, sagt, daß die Weltseele an dem Kreuze des Weltenleibes gekreuzigt ist, so bedeutet das nichts anderes, als daß der Mensch die höchste Ausgestal­tung der Weltenseele darstellt, und daß die Weltenseele hindurchgegangen ist durch die drei Reiche: Pflanzenreich, Tierreich und Menschenreich.",
        "Die Weltenseele ist an dem Kreuze: Pflanzenreich, Tierreich und Menschenreich, den drei Naturreichen, gekreuzigt. - Ein wunderbar tiefes Bild von Plato, ganz aus der Geisteswissenschaft herausge­sprochen."
      ],
      [
        "Unzählige Male wurde dieses Bild in den Rosenkreuzer­schulen wiederholt: Schaut Euch die Pflanze an mit dem Kopf nach unten, mit den Befruchtungsorganen nach oben, die sich dem Sonnenstrahl entgegenstrecken. - Diesen Son­nenstrahl nannte man die heilige Liebeslanze, welche die Pflanze zu durchdringen hat, damit der Same zum Wachsen und Reifen kommen kann.",
        "Nun sagte man dem Schüler:"
      ],
      [
        "Richte den Blick hinauf bis zum Menschen, sieh dir die Pflanze und dann den Menschen an, vergleiche des Menschen Materie und Stoff mit denen der Pflanze.",
        "Der Mensch ist die umgekehrte Pflanze, er ist es geworden, weil er seinen Stoff, sein Fleisch durchdrungen hat mit physischer Begierde, mit Leidenschaft und Sinnlichkeit.",
        "Keusch und rein darf die Pflanze die Befruchtungsorgane der Befruchtungslanze, der hehren Liebeslanze, entgegenstrecken.",
        "Der Mensch kommt auf einen ähnlichen Standpunkt in der Zeit, wo er die Be­gierde vollkommen geläutert haben wird, so daß er in eine Zukunft hineinblickt, die ihm die Erfüllung des Ideals brin­gen wird: Du bist so keusch und rein wie der Blütenkelch der Pflanze.",
        "Dann wirst du auf der Höhe der irdischen Ent­wicklung angelangt sein, dann wird nicht mehr unreine Begierde"
      ],
      [
        "deine niederen Organe durchziehen, dann wirst du die geistige Liebeslanze, deine produktive Kraft, die dann ganz geistig sein wird, entgegenstrecken dem Blütenkelch, wie der Pflanzenkelch sich öffnet der heiligen Liebeslanze im Sonnenstrahl.",
        "So geht der Mensch durch die Reiche der Natur hindurch und läutert sich hinauf bis zur Entwicklung derjenigen Organe, die heute erst in der Anlage begriffen sind.",
        "Wenn der Mensch in dem, was heilig und edel ist, etwas hervorbringt, so ist er am Anfang einer zukünftigen, produktiven Kraft, die er haben wird, wenn seine niedere Natur ihre vollständige Läuterung durchgemacht hat.",
        "Dann wird er ein neues Organ haben.",
        "Der Blütenkelch der Pflanze wird auf höherer Stufe neuerdings erstehen und wird der Lanze des Amfortas entgegengestreckt werden, wie der Blütenkelch der geistigen Liebeslanze der Sonne."
      ],
      [
        "So stelle dir auf niederer Stufe dasjenige dar, was, als hohes Ideal gegeben, in Zukunft des Menschen Geschlecht sein wird, wenn alles Niedere geläutert sein wird und alles keusch und rein sich entgegenhalten wird der vergeistigten Sonne der Zukunft, wenn dieser Pflanzenkelch hindurch­gegangen sein wird durch die Menschennatur, die in gewis­ser Beziehung höher, in gewisser Beziehung niederer stehen wird als die Pflanze, wenn er hinaufgeläutert sein wird bis zur höchsten Geistigkeit, und vorgehalten wird der ver­geistigten Sonne als der heilige Kelch, der erhöhte Pflanzenkelch, der durch die Menschheit hindurchgegangen ist."
      ],
      [
        "Dies wurde geistig erfaßt von dem Rosenkreuzerschüler, es ist das Geheimnis des heiligen Gral, das höchste Ideal, das vor den Menschen hingestellt werden kann.",
        "So erscheint die ganze Natur mit einem geistigen Sinn durchglüht und durch­strömt.",
        "Wenn man so alles erfaßt, alles als ein Gleichnis des Geistigen sieht, dann ist man auf dem Wege, die imagina­tive Erkenntnis zu erwerben.",
        "Dann dringen aus den Dingen"
      ],
      [
        "die Farben und werden selbständig, es dringen aus ihnen die Töne und werden selbständig, der Raum erfüllt sich mit einer selbständigen Farben- und Tonwelt, und in diesen kündigen sich geistige Wesenheiten an.",
        "Wir steigen von der imaginativen Erkenntnis zu der wirklichen Erkenntnis des geistigen Raumes auf.",
        "Das ist der Weg, den der Rosenkreuzer auf der zweiten Stufe seiner Schulung nimmt."
      ],
      [
        "Das dritte ist die Kenntnis der okkulten Schrift.",
        "Die okkulte Schrift ist keine gewöhnliche Schrift, sondern eine solche, die mit den Naturgeheimnissen zusammenhängt.",
        "Ich möchte Ihnen gleich klarmachen, was Sie sich unter der okkulten Schrift vorzustellen haben.",
        "Ein verbreitetes Zei­chen dieser Schrift ist der sogenannte Wirbel.",
        "Sie können sich denselben so vorstellen, daß Sie sich zwei Sechser ineinander verschlungen denken.",
        "Dieses Zeichen gebraucht man, um gewisse Erscheinungen, die in der ganzen natür­lichen und geistigen Welt vorhanden sind, zu kennzeichnen und ihre innere Natur zu charakterisieren.",
        "Wenn Sie eine Pflanze nehmen und betrachten, so werden Sie finden, daß sie sich bis zum Samenkorn entwickelt.",
        "Wenn Sie dieses Samenkorn in die Erde legen, so entwickelt sich eine ähn­liche Pflanze, die der alten gleich ist.",
        "Daß da etwas Stoff­liches von der alten Pflanze in die neue übergeht, ist ein materielles Vorurteil, das durch nichts gerechtfertigt ist und von der Zukunft widerlegt werden wird.",
        "In die neue Pflanze geht lediglich die bildsame Kraft über.",
        "Die alte Pflanze erstirbt stofflich ganz und gar, und die neue Pflanze ist stofflich etwas ganz Neues.",
        "Nicht das allergeringste Stoffliche geht aus der alten Pflanze in die neue über.",
        "Diesen neuen Ansatz einer Entstehung und eines Vergehens einer Pflanze bezeichnet man dadurch, daß man zwei sich inein­ander schlingende Spiralen, also einen Wirbel zeichnet, und zwar ohne eine Verbindung der beiden Linien zu bewirken."
      ],
      [
        "# Bild s. 195"
      ],
      [
        "Nun finden sich solche Wirbel sowohl in der äußeren als auch in der geistigen Natur.",
        "So sagt uns zum Beispiel die Geistesforschung, daß in der Entwicklung der Menschheit einst ein solcher Wirbel vorhanden war, als die alte atlan­tische Kultur in die neue nachatlantische Kultur überging.",
        "Die Geisteswissenschaft zeigt Ihnen hier etwas, was die heutige Naturwissenschaft nur in der ersten elementarsten Stufe kennt.",
        "Sie zeigt Ihnen, daß das, was heute Meer ist zwischen Europa und Amerika, ausgefüllt war mit einem Kontinente, daß sich eine uralte Kultur da entwickelt hatte, daß durch die «Sündflut» jener Kontinent überflutet wurde und verschwand.",
        "Dies zeigt uns, daß das, was uns Plato von dem Untergang der Insel Poseidonis mitteilt, auf Rich­tigkeit beruht, und daß sie ein Rest des uralten, atlan­nschen Kontinentes war.",
        "Jene Kultur verschwand in bezug auf ihre geistige Eigenschaft, und eine neue Kultur trat auf, so daß man diesen Vorgang kennzeichnen kann mit den zwei ineinander sich schlingenden Spiralen, dem Wirbel.",
        "Das Alte wird bezeichnet durch die sich hineinschlingende Spirale, das Neue durch die sich herausschlingende."
      ],
      [
        "Als der Übergang von der atlantischen Kultur in die nachatlantische vor sich ging, da erschien im Frühlinge die Sonne im Sternbilde des Krebses.",
        "Sie wissen, daß die Sonne im Laufe des Jahres vorwärtsrückt.",
        "In jener alten Zeit ging sie, wie gesagt, bei Frühlingsanfang im Sternbilde des Krebses auf, dann eine Zeitlang im Sternbilde der Zwil­linge, dann im Sternbilde des Stieres und dann des Widders.",
        "Die Völker haben immer dasjenige als etwas besonders"
      ],
      [
        "Wohltätiges empfunden, was ihnen vorn Himmeisgewölbe die ersten Sonnenstrahlen zusendet.",
        "Daher sehen Sie, daß man, als die Sonne anfing im Sternbilde des Widders aufzugehen, angefangen hat, den Widder zu verehren.",
        "Daher rühren die ganzen Lammsagen, die Sage vom goldenen Vließ und so weiter.",
        "Früher, bevor die Sonne im Sternbilde des Widders aufgegangen war, ging sie im Sternbilde des Stieres auf.",
        "Daher haben die Kulturen, welche den Widder-Kulturen vorangegangen sind, den Stier als heiliges Tier verehrt.",
        "Sie finden daher in jener Zeit zum Beispiel die Verehrung des ägyptischen Stieres Apis.",
        "In der Zeit des Überganges von der atlantischen in die nachatlantische Zeit haben Sie die Herrschaft des Sternbildes des Krebses gehabt.",
        "Und daher haben Sie die zwei ineinandergeschlungenen Wirbel als Zeichen des Krebses im Kalender."
      ],
      [
        "Es gibt hunderte, tausende dieser Zeichen, die man nach und nach lernt.",
        "Das sind nicht willkürliche Zeichen.",
        "Wenn man sie kennt, zeigen sie einem die Wege, um hineinzu­kriechen in die Dinge und in den Dingen zu leben.",
        "Wie das Studium den Verstand, die imaginative Erkenntnis das Gemüt ergreift, so ergreift die Erkenntnis der okkulten Schrift den Willen.",
        "Sie zeigt uns die Wege beim Schaffen und Produzieren.",
        "Wenn daher das Studium uns Erkenntnis, die Imagination Anschauung bringt, so bringt uns die Er­kenntnis der okkulten Schrift Magie, die Erkenntnis der in den Dingen schlummernden Naturgesetze, die Erkenntnis, die uns tiefer in das Wesen der Dinge hineinführt.",
        "Sie können bei vielen - meinetwegen auch bei Eliphas Levi - viele okkulte Zeichen finden.",
        "Derjenige aber, der nichts weiß von diesen Dingen, wird wenig dabei lernen können.",
        "Sie können indessen eine Andeutung darin finden, wie sie aussehen.",
        "In den Werken, die Sie darüber gedruckt finden, steht gewöhnlich Unzutreffendes.",
        "Heilig gehalten wurden"
      ],
      [
        "von allen Völkern, von den Eingeweihten wenigstens, diese okkulten Schriftzeichen.",
        "Und wenn wir weiter zurückgehen, finden wir strenge Bestimmungen über deren Geheimhal­tung, damit diejenigen, welche solche Zeichen gebrauchen dürfen, sie nie unwürdig gebrauchen mögen.",
        "Die strengsten Strafen sind auf die Übertretung dieser Bestimmungen gesetzt."
      ],
      [
        "Das vierte ist das, was man die Bereitung des Steines der Weisen nennt.",
        "Was Sie darüber in der Literatur finden, ist ziemlich unzutreffend, ja sogar meistens törichtes Zeug.",
        "Wäre der Stein der Weisen das, was da geschildert wird, so hätte jeder ein Recht, darüber zu spotten.",
        "Sie werden ein Stück davon erkennen, wenn Sie meiner Betrachtung fol­gen: sie wird Ihnen einen großen Einblick geben.",
        "Am Ende des achtzehnten Jahrhunderts stand in einer ernstzuneh­menden mitteldeutschen Zeitschrift eine Notiz über den Stein der Weisen.",
        "Wer diese Notiz liest und etwas von der Sache versteht, der findet, daß der Schreiber irgendwo ein­mal etwas darüber vernommen hat.",
        "Seine Worte sind ganz richtig, aber man sieht auch, daß er seine Worte selbst nicht richtig versteht.",
        "Der Verfasser der Notiz schreibt da: Der Stein der Weisen ist etwas, was alle Menschen kennen, etwas, was die meisten Menschen oft und oft in der Hand haben, was man an vielen Orten der Erde findet und von dem nur der Mensch nicht weiß, daß es der Stein der Weisen ist. - Eine sonderbare Beschreibung ist das, wie der Stein der Weisen sein soll, und dennoch wörtlich wahr.",
        "Man muß die Sache nur richtig verstehen."
      ],
      [
        "Betrachten Sie einmal den menschlichen Atmungsprozeß, denn mit einer Regulierung des Atmens hängt das zusam­men, was man die Auffindung oder Bereitung des Steines der Weisen nennt.",
        "Der Mensch atmet heute Sauerstoff ein und Kohlensäure aus, also die Verbindung des Sauerstoffs"
      ],
      [
        "mit Kohlenstoff wird ausgeatmet.",
        "Der Mensch atmet Sauer­stoff, die Lebensluft, ein und Kohlensäure, ein wirkliches Gift, aus.",
        "Mit dieser Kohlensäure kann der Mensch und das Tier nicht leben.",
        "Würden die Tiere, die geradeso atmen wie der Mensch, allein auf der Erde sein und hätten sie immer so geatmet wie heute, so würden sie die Luft um sich herum verpestet haben, und weder Tier noch Mensch könnte heute noch atmen.",
        "Woher kommt es nun, daß sie aber noch atmen können?",
        "Daher, daß die Pflanze die Kohlensäure aufnimmt, den Kohlenstoff in sich behält und den Sauerstoff wieder zurückgibt, so daß Menschen und Tiere den Sauerstoff wie­der zur Atmung benützen können.",
        "Es ist also ein schöner Wechselprozeß zwischen der Atmung der Tier- und Men­schenwelt und der Atmung oder dem Assimilationsprozeß der Pflanzenwelt - Assimilationsprozeß, damit kein pedan­tischer Gelehrter etwas dagegen einwenden kann.",
        "Der­jenige, der jeden Tag fünf Mark einnimmt und jeden Tag zwei Mark ausgibt, schafft einen Überschuß, bei ihm steht die Sache anders als bei demjenigen, der fünf Mark ausgibt und nur zwei Mark einnimmt.",
        "Ähnlich kann es auch bei der Atmung sein.",
        "Das Wesentliche aber hierbei ist, daß dieser Tauschprozeß zwischen Mensch und Pflanzenwelt besteht."
      ],
      [
        "Dieser Tauschprozeß ist höchst merkwürdig.",
        "Betrachten wir ihn deshalb noch einmal etwas näher.",
        "In den Menschenleib geht Sauerstoff ein, aus dem Menschenleib kommt Koh­lensäure heraus.",
        "Kohlensäure besteht aus Sauerstoff und Kohlenstoff.",
        "Die Pflanze behält den Kohlenstoff und gibt den Sauerstoff dem Menschen wieder zurück.",
        "Sie können in der Steinkohle, die Sie Jahrmillionen nach Entstehung der betreffenden Pflanze aus der Erde herausgraben, den Koh­lenstoff, welchen die Pflanze eingeatmet hat, wieder er­blicken.",
        "Der gewöhnliche Atmungsprozeß, der so verläuft, wie er eben geschildert wurde, zeigt an, wie notwendig der"
      ],
      [
        "Mensch zu seinem Leben heute die Pflanze hat, und wie in ihm beim Atmungsprozeß etwas vorgeht, was nur ein hal­ber Prozeß ist.",
        "Er braucht die Pflanze als etwas, was nicht in ihm ist, damit sie ihm den Kohlenstoff in Sauerstoff um­wandelt."
      ],
      [
        "Nun gibt es eine Rhythmisierung des Atmungsprozesses in rosenkreuzerischem Sinn, über die indessen Näheres nur von Mensch zu Mensch mitgeteilt werden kann.",
        "Es kann zwar hier darauf hingedeutet werden, aber nur so, daß von einem Eingehen in Einzelheiten Abstand genommen wird.",
        "Aber der Rosenkreuzerschüler bekam und bekommt seine bestimmte Anweisung, er mußte in einer bestimmten Weise atmen, in einem bestimmten Rhythmus und mit ganz be­stimmten Gedankenformen.",
        "Dadurch wird sein Atmungs­prozeß umgewandelt.",
        "Diese Umwandlung können Sie sich nur vorstellen, wenn Sie den Ausspruch berücksichtigen:"
      ],
      [
        "Steter Tropfen höhlt den Stein.",
        "Auch bei den höchststehen­den Menschen wird nicht von heute auf morgen der ganze innere Lebensprozeß umgestaltet, wenn in rosenkreuze­rischer Form geatmet wird.",
        "Aber dasjenige, was bei solcher Atmung im Leibe des Menschen umgestaltet wird, geht nach einer bestimmten Richtung hin, nämlich dahin, daß der Mensch in Zukunft imstande ist, in sich selbst die Koh­lensäure wieder in brauchbaren Sauerstoff umzuwandeln, so daß das, was heute draußen in der Pflanze vor sich geht:"
      ],
      [
        "die Umwandlung der Kohlensäure in den Kohlenstoff, das, was heute die Pflanze dem Menschen abnimmt, von dem Menschen, wenn der Atmungsprozeß immer weiter und weiter wirken wird in dem Einzuweihenden, in einem eige­nen Organ bewirkt werden wird, von dem Physiologie und Anatomie noch nichts wissen, das aber gleichwohl in der Entwicklung begriffen ist.",
        "Der Mensch wird also dann selbst die Umwandlung bewirken.",
        "Statt den Kohlenstoff"
      ],
      [
        "hinauszuatmen und an die Pflanze abzugeben, wird er ihn in sich selbst verwenden und seinen eigenen Leib mit Hilfe des Kohlenstoffes, den er vorher an die Pflanze abgeben mußte, auferbauen."
      ],
      [
        "Halten Sie das, was ich eben gesagt habe, zusammen mit dem, was ich von dem Ideal des heiligen Grals mitgeteilt habe: nämlich daß die reine keusche Pflanzennatur durch­gegangen sein wird durch die Menschennatur, und daß diese Menschennatur in ihrer höchsten Geistigkeit wieder bei der Pflanze von heute angekommen sein wird.",
        "Den Pflanzenprozeß in sich selbst durchzumachen, wird der Mensch einst imstande sein.",
        "Seine jetzigen Stoffe, die er in sich hat, wird er immer mehr zu jenem Ideal hinbilden, daß der Körper ein Pflanzenleib und der Träger eines viel höhe­ren und geistigeren Bewußtseins sein wird.",
        "So lernt der Schüler die Alchemie, durch die er in den Stand gesetzt wird, die Säfte und Stoffe des Menschen in Kohlenstoff um­zuwandeln.",
        "Was heute die Pflanze tut, indem sie ihren Leib aus Kohlenstoff auferbaut, das wird der Mensch einst selbst tun.",
        "Er wird sich aus Kohlenstoff eine Struktur des Leibes bilden, die die Struktur des künftigen Menschenleibes sein wird."
      ],
      [
        "Ein großes Geheimnis verbirgt sich hinter dem, was man die Rhythrnisierung des Atmungsprozesses nennt.",
        "Jetzt ver­stehen Sie wohl jene Andeutung über den Stein der Weisen, die in der vorhin zitierten Notiz enthalten ist.",
        "Was lernt der Mensch also bezüglich des Aufbaues seiner späteren Leibesform?",
        "Er lernt die gewöhnliche Kohle erzeugen, die auch die Substanz des Diamanten ist, um damit seinen Leib aufzubauen.",
        "Diesen Kohlenstoff wird der Mensch bei einem erhöhten und erweiterten Bewußtsein aus sich selbst ent­nehmen und in sich selbst verwenden können.",
        "Er wird seine eigene Substanz, die auf der Kohlenstoffstruktur aufgebaute"
      ],
      [
        "Pflanzensubstanz bilden können.",
        "Das ist die Alchemie, welche zur Bildung des Steines der Weisen hinführt.",
        "Der Menschenleib selbst ist jene Retorte, die in dem Sinne ver­wandelt wird, wie es eben hier angedeutet worden ist."
      ],
      [
        "So verbirgt sich hinter der Regulierung des Atmungs-prozesses, hinter dem, was man oft bezüglich des Steines der Weisen, aber meist in ganz unsinniger Weise, angedeutet findet, das, was man die Auffindung oder Bereitung des Steines der Weisen nennt.",
        "Das sind die Andeutungen, wie sie erst seit kurzem aus den Rosenkreuzerschulen in die Öffentlichkeit gedrungen sind.",
        "Vergeblich werden Sie sie in Büchern suchen.",
        "Das ist ein kleiner Teil der vierten Stufe:"
      ],
      [
        "die Aufsuchung des Steines der Weisen."
      ],
      [
        "Das fünfte besteht in dem, was man die Erkenntnis des Mikrokosmos, der kleinen Welt, nennt.",
        "Das führt uns auf das zurück, was Paracelsus gesagt hat und worauf ich schon oft hingewiesen habe: Alle Dinge, die um uns herum sind, würden, wenn wir aus ihnen einen Auszug nehmen könn­ten, als Extrakt den Menschen ergeben.",
        "Der Mensch hat in sich diejenigen Stoffe und Kräfte, welche als kurze Rekapi­tulation der ganzen übrigen Natur erscheinen, so daß, wenn wir die Natur um uns sehen, wir sagen können, was drau­ßen in der Natur ist, ist im großen das Urbild von dem, was in uns allen als Nachbild erscheint.",
        "Nehmen wir zum Beispiel das Licht.",
        "Was hat nun dieses Licht im Menschen bewirkt?",
        "Wenn es kein menschliches Auge gäbe, so könnte es nicht das Licht gewahr werden.",
        "Die Welt wäre finster und dunkel für uns.",
        "Aber ebenso wie Tiere, wenn sie in finstere Höhlen einwandem, wie zum Beispiel in die Höh­len von Kentucky, das Sehvermögen verlieren, so wird auf der anderen Seite das Auge vorn Lichte selbst geschaffen.",
        "Wir hätten kein Auge, wenn es kein Licht gäbe.",
        "Das Licht hat erst unsere Sehorgane aus der Haut, aus dem Organismus"
      ],
      [
        "herausgelockt.",
        "Das Auge, hat Goethe gesagt, ist vom Licht und für das Licht, das Ohr vom Ton und für den Ton geschaffen.",
        "Alle Dinge sind aus der großen Welt, dem Makrokosmos, herausgeboren.",
        "Darin beruht das Geheim­nis, daß man unter gewissen Anleitungen und Anweisungen, durch eine Vertiefung in den Körper hinein, nicht bloß die leibliche, sondem auch die geistige Welt ergründen und die uns umgebende Natur erkennen lernen kann.",
        "Wer unter gewissen Bedingungen lernt, mit gewissen Gedankenformen sich meditativ ganz in das Innere des Auges zu versenken, der lernt die innere, wesentliche Natur des Lichtes er­kennen.",
        "Zwischen den Augenbrauen, an der Nasenwurzel, ist ein Punkt, der in dieser Beziehung auch von hoher Be­deutung ist.",
        "Wenn man sich in ihn vertieft, dann lernt man bedeutsame, wichtige Vorgänge in der geistigen Welt kennen, die sich abgespielt haben, als diese Partie des Kopfes sich aus der umliegenden Welt herausgebildet hat.",
        "So lernt man die geistige Zusammenfügung des Menschen kennen.",
        "Aus geistigen Wesenheiten und Kräften heraus ist der Mensch ganz und gar gebildet.",
        "Wenn er sich daher in seine Form vertieft, lernt er die Wesenheiten und geistigen Kräfte er­kennen, die seinen Organismus, die seine Form aufgebaut haben."
      ],
      [
        "Eine Bemerkung muß hier noch gemacht werden.",
        "Dieses Versenken ins Innere des Menschen, ebenso wie die anderen Übungen, die hinunterarbeiten in das Leibliche, durch die vom Ich aus in den physischen Leib hineingearbeitet wird -Atman kommt von Atmen -, sollten nicht ohne Vorberei­tung vorgenommen werden.",
        "Wenn man damit zu arbeiten anfängt, muß man eigentlich geistig schon vorgearbeitet haben.",
        "Deshalb wird in der Rosenkreuzerschulung auch streng auf Gedankenschulung gehalten.",
        "Es ist auch bei die­ser Schulung für den Schüler die große Moral, ein fester"
      ],
      [
        "innerer Wesenskern nötig.",
        "Wenn er diese nicht hat, so kann er straucheln.",
        "In jedes Glied kann er sich meditativ versen­ken, und Welten gehen ihm in seinem Inneren auf.",
        "Niemand kann die wahre Natur des Alten Testamentes kennen­lernen ohne eine solche Versenkung in das eigentlich mensch­liche Innere, allerdings nach bestimmten Vorschriften, die ihm in der geisteswissenschaftlichen Schulung gegeben wer­den können."
      ],
      [
        "Alle diese Dinge sind aus der Geisteswissen­schaft, aus Einblicken in die geistige Welt heraus geschrie­ben.",
        "Daher kann man sie auch nur verstehen, wenn man imstande ist, sie wieder in sich aufzusuchen."
      ],
      [
        "Der Mensch ist aus dem Makrokosmos herausgeboren, und er muß als Mikrokosmos die darin wirkenden Kräfte und Gesetze wieder in sich finden.",
        "Nicht als Anatorn kann man den Menschen in sich kennenlernen.",
        "Nur dann kann man das, wenn man lernt, in sein eigenes Inneres zu blicken, das dann in einzelnen Gebieten leuchtend und tönend wird."
      ],
      [
        "Jedes Organ hat seine bestimmte Farbe und seinen bestimmten Ton, wenn das Ganze bloßgelegt wird vor der nach innen schauenden Seele.",
        "Wenn der Mensch durch die Rosenkreu­zerschulung in seinem Innern kennengelernt hat, was aus dem Makrokosmos heraus geschaffen worden ist, dann kann er in sich die Dinge kennenlernen, die im Makrokosmos sind."
      ],
      [
        "Hat der Mensch, durch Versenkung in sein Auge oder in den Punkt über der Nasenwurzel, sein Inneres erkannt, dann kann er herausgehen und die großen Gesetze im gro­ßen Kosmos geistig erkennen.",
        "Und er lernt dann aus eigener Anschauung geistig dasjenige erkennen, was ein inspirierter Genius im Alten Testament beschrieben hat, er sieht es in der Akasha- Chronik und kann die Menschheitsentwicklung durch Jahrmillionen hindurch verfolgen."
      ],
      [
        "Das kann man alles durch eine solche Schulung wirklich erkennen.",
        "Das ist aber eine andere Schulung als die gewöhnliche."
      ],
      [
        "Man darf nicht glauben, daß Selbsterkenntnis durch planloses Hineinbrüten in sich errungen wird oder daß, wenn man hineinschaut in sich, der Gott im Inneren zu sprechen anfängt, wie das heute häufig gelehrt wird.",
        "Nein, man muß in seine Organe sich vertiefen, um dann das große Selbst der Welt erkennen zu können.",
        "Wahr ist es:"
      ],
      [
        "durch alle Zeiten geht der Spruch «Erkenne dich selbst», aber ebenso wahr ist es, daß das höhere Selbst nicht durch das eigene Innere zu erkennen ist, sondern, wie schon Goethe, der große Seher, sagt, indem man seinen Geist zum Universum erweitert.",
        "Das geschieht auf der sechsten Stufe der rosenkreuzerischen Schulung, wenn man auf diese Weise geduldig seinen Weg geht.",
        "Nicht bequem ist der Weg.",
        "Man muß in sein Wesen untertauchen.",
        "Man kann nicht zufrieden sein mit Phrasen und Allgemeinheiten.",
        "Man muß in jedes Wesen eintauchen, es liebevoll in sich aufnehmen.",
        "Jede Bequemlichkeit muß einem fremd wer­den.",
        "Untertauchen muß man in die Wesen, im Konkreten, im Besonderen die Wesen kennenlernen, nicht herumreden über, was man so nennt: Harmonie mit der Welt, Eins-werden mit der Weltenseele, Zusammenschmelzen mit der Welt.",
        "Solche Phrasen sind nichts wert gegenüber der Rosen­kreuzerschulung, die nicht von Harmonie mit dem Unend­lichen schwätzt oder sich in ähnlichen Phrasen ergeht, son­dern die Kräfte in der Menschenseele lebendig werden läßt."
      ],
      [
        "Wenn der Mensch sein Selbst so zu erweitern versucht hat, dann wird die siebente Stufe der Seele nicht mehr fern liegen.",
        "Dann verwandelt sich Erkenntnis in Gefühl, dann geht das, was in seiner Seele lebendig ist, in Empfindung über, und er hört auf, sich nur in sich selbst zu fühlen.",
        "Er fängt an, sich in jedem Wesen zu fühlen.",
        "Wenn er unter­getaucht ist in jeden Stein, in jede Pflanze, in jedes Tier, dann fühlt er mit Pflanze, Stein und Tier, und es sagt, es"
      ],
      [
        "offenbart ihm jedes einzelne Ding seine Wesenheit, nicht in Worten, nicht in Begriffen, sondern im innersten Gefühl.",
        "Dann beginnt jene Zeit, wo ihn ein allgemeines Netz von Sympathie mit den Wesen verbindet, wo er sich in alle Wesen hineinlebt.",
        "Dies Hineinleben in alle Wesen nennt man die siebente Stufe, die Gottseligkeit, das selige Ruhen in allen Wesen.",
        "Wenn der Mensch sein Selbst verbunden fühlt mit allen übrigen Wesenheiten, nicht mehr in seiner Haut lebt, sondern eingegangen ist in alle Wesen, mitfühlt mit allen Wesen, wenn er ausgebreitet ist in dem ganzen Weltenraum, so daß er zu allem sagen kann: «Das bist du», wenn er ganz Gefühl, ganz Seligkeit geworden ist, dann darf das gesagt werden, was Goethe aus der Rosenkreuzer­schulung heraus in seinem Gedichte «Die Geheimnisse» ausspricht:"
      ],
      [
        "«Wer hat dem Kreuze Rosen zugesellt?»"
      ],
      [
        "Das darf aber nicht nur gesagt werden von dem höchsten Standpunkte, sondern von den ersten Schritten an, wo man dasjenige zu seinem Losungswort macht, was sich ausdrückt in dem von Rosen urnschlungenen Kreuz.",
        "Das Kreuz ist der Ausdruck dafür, daß der Mensch jenes Selbst, in das man hineinbrütet und das nur das niedere Selbst ist, welches niemals das höhere Selbst gewahren kann, überwindet, daß er herausgeht aus dem niederen Selbst, aufgeht in dem Höheren, das ihn selig hinein führt in das Leben und Weben von allen Wesenheiten, wenn er einsieht, was da steht in einem Gedichte des «West-Östlichen Divan» von Goethe:"
      ],
      [
        "«Und solang du das nicht hast,"
      ],
      [
        "Dieses: Stirb und Werde,"
      ],
      [
        "Bist du nur ein trüber Gast"
      ],
      [
        "Auf der dunklen Erde.»"
      ],
      [
        "Ja, wer es nicht verstehen kann, dieses Überwinden des eng begrenzten Selbst und dieses Aufgehen im höheren Selbst, wer es nicht begreifen kann, jenes Symbolum des Sterbens und des Werdens, das Verdorren des niederen Selbst und das Aufblühen der Rosen des höheren Selbst, der kann nicht jene Devise begreifen, die Goethe aus­gesprochen hat und mit der wir das Sachliche des Rosen­kreuzertums beschließen wollen, das Losungswort, das Zeichen der sieben Glieder, das über dem mit Rosen um­wundenen Kreuz stehen muß:"
      ],
      [
        "«Von der Gewalt, die alle Wesen bindet,"
      ],
      [
        "Befreit der Mensch sich, der sich überwindet.»"
      ]
    ]
  },
  {
    "order": 13,
    "title_de": "RICHARD WAGNER UND DIE MYSTIK Berlin, 28. März 1907",
    "paragraphs": [
      "Gegen eine Betrachtung, wie die heutige eine ist, die Richard Wagner und die Mystik in einen Zusammenhang bringen wird, erheben sich wohl leicht von vorneherein gewisse Vorurteile, welche aus Mißverständnissen gewonnen sein können, die einer solchen Betrachtung eines Künstlers von einem gewissen geisteswissenschaftlichen Standpunkte aus überhaupt entgegengebracht werden können. Und eine zweite Art von Vorurteilen sind diejenigen, die der Mystik als solcher entgegengebracht werden.",
      "Alles dasjenige, was heute zu sagen sein wird über Richard Wagners Stellung in der Kunst auf der einen Seite und in der Mystik auf der anderen Seite, kann den Wider­spruch hervorrufen: Ja, da wird eine ganze Menge in Richard Wagner hineingetragen, wovon er selbst nie etwas ausgesprochen hat, worüber er selbst nichts irgendwie hat verlauten lassen. - Gegen ein solches Vorurteil muß gesagt werden, daß derjenige, der eine solche Betrachtung anstellt, wie die heutige sein wird, sich selbstverständlich einen sol­chen Einwand von vornherein machen würde. Aber es ist gar nicht die Absicht, wenn wir eine geistige Erscheinung in der Welt betrachten, nur dasjenige zu sagen, was die ent­sprechende Persönlichkeit selbst gesagt hat. Das würde, wenn es nur konsequent durchgedacht wird, überhaupt un­möglich machen, wahrhaft höhere Betrachtungen gegenüber den Erscheinungen der Welt anzustellen.",
      "Denken Sie einmal, wenn der Botaniker - wir könnten",
      "auch sagen der Lyriker - über eine Pflanze, über eine Natur­erscheinung dasjenige ausspricht, was er, also der Botani­ker, über diese Naturerscheinung zu denken vermag, oder wenn der Lyriker ausspricht, was er zu fühlen vermag gegenüber einer Pflanze oder einer Naturerscheinung, würde da irgend jemand verlangen, daß die Pflanze oder die Na­turerscheinung selbst das zu sagen vermöchte, was dem Botaniker oder dem Lyriker aus der Seele herausströmt? Nicht darum kann es sich handeln, daß dasjenige, was wir über eine geistige oder eine andere Erscheinung der Welt zu sagen haben, von dieser Erscheinung selbst gesagt wird. Da müßten Sie auch verlangen, daß die Pflanze selbst dem Botaniker die Gesetze ihres Wachstums auszudrücken ver­mag, da müßten Sie es als ein Unrecht ansehen, daß der Lyriker einer Naturerscheinung gegenüber von Gefühlen spricht, die diese Naturerscheinung nicht selbst auszudrücken vermag. Vielmehr müssen wir sagen, daß gerade in der menschlichen Seele sich dasjenige ankündigen muß, was die Außenwelt nicht über sich selbst zu sagen vermag.",
      "In solcher Art, bitte, nehmen Sie alles dasjenige, was Ihnen heute über eine solche geistige Erscheinung wie Richard Wagner gesagt werden soll. So wahr es ist, daß die Pflanze die Gesetze ihres Wachstums nicht selbst weiß, aber danach wächst, sich danach gestaltet, so wahr ist es, daß ein Künstler nicht selber zu sagen braucht, was ein geisteswissenschaftlicher Betrachter als die Gesetze seines Werdens und die Gesetze seiner ganzen Wesenheit aussagen muß. Aber ebenso wahr ist es, daß der Künstler diese Gesetze darlebt, danach schafft, wie die Pflanze nach den Gesetzen schafft, die man hinterher findet, wie sie die Gesetze, die ihr eingeprägt sind, darlebt. Daher darf es kein Einwand sein, daß Richard Wagner diese Dinge nicht selbst gesagt hat, die heute vorgebracht werden. Das andere bezieht sich",
      "auf das, was man als die Mystik kennt. Gelehrte und Un­gelehrte sprechen von der Mystik so, als wäre sie eine dunkle, nebulose Betrachtung der Welt, gegenüber dem, was man die eigentliche wissenschaftliche, begriffliche Be­trachtung der Welt nennt. Die Gnostiker, die großen Mysti­ker der ersten christlichen Jahrhunderte, haben anders über die Mystik gedacht. Und diejenigen, welche überhaupt etwas von der Mystik verstehen, denken zu allen Zeiten anders über die Mystik. Die Gnostiker haben die Mystik «mathesis» genannt, Mathematik, nicht weil die Mystik Mathematik wäre, sondern aus dem Grunde, weil der wahre Mystiker in bezug auf seine Ideen und Vorstel­lungen von den höheren geistigen Welten dieselbe kristall­klare, durchsichtige Helligkeit anstrebt, welche auf gewis­sen anderen Gebieten die mathematischen Vorstellungen und Begriffe haben. Die Mystik ist, wenn sie in Wahrheit erfaßt wird, nicht ein dunkles, gefühlsmäßiges Erfassen der Welt, sondern das Klarste, Kristallklarste, was es überhaupt geben kann. Von diesen zwei Gesichtspunkten, die durch die Zurückweisung zweier Vorurteile hier dargelegt worden sind, wollen wir ausgehen.",
      "Man kann Richard Wagner wirklich vom höchsten gei­steswissenschaftlichen Standpunkt aus betrachten. Denn wenn es bei irgendeinem der Geistsucher im letzten Jahr­hundert der Fall war, daß er sich sein ganzes Leben hin­durch in der ehrlichsten, redlichsten Weise bemüht hat, die Quellen und Grundlagen der Weltenrätsel zu finden, bei ihm war es der Fall. Er nennt sein Haus in Bayreuth «Wahnfried», indem er damit selbst angibt den Grund da­für, daß dort «sein Wähnen Ruhe fand». Mit diesem Wort, daß da sein Wähnen Ruhe fand, ist viel, recht viel gesagt.",
      "Derjenige, der ehrlich und redlich den Pfad der Erkennt­nis zu gehen versucht, und der, gleichgültig ob in dieser",
      "oder jener Form, in künstlerischer oder in anderer Form die Gebiete des geistigen Lebens, die er auf dem Erkennt­nispfade gefunden zu haben glaubt, ausprägt, derjenige, der so redlich den Erkenntnispfad geht, der weiß, was das Wort Wähnen heißt, wieviel Wahngebilde auf dem Er­kenntnispfad sich ihm in den Weg stellen, und er weiß, daß das Erkennen nicht etwas ist, was sich in einer nüchternen, trockenen Weise abspielt. Er weiß, daß das Erkennen in Wahrheit etwas ist, was sich unter Katastrophen des inneren seelischen Lebens, unter Aufsteigen und Abfallen in bezug auf das menschliche Innere abspielt, er weiß, daß es da furchtbare Gefahren auf der einen Seite und Seligkeiten, wunderbare Seligkeiten auf der anderen Seite gibt. Und er weiß, daß eines demjenigen in Aussicht steht, der diesen Erkenntnispfad geht: die Ruhe, die göttliche Ruhe, die aus einem intimen Sich-Einleben in die göttlichen Weltengeheimnisse hervorgeht. Etwas von solcher Gesinnung, etwas von solcher Stimmung drückt sich bei Richard Wag­ner in dem Wort aus: «Weil hier mein Wähnen Ruhe fand, Wahnfried sei dieses Haus genannt.»",
      "Er war nicht ein Künstler wie so viele andere, die aus einer wesenlosen Phantasie heraus schaffen wollen. Er war ein Künstler, der von allem Anfang an seinen Beruf als große weltgeschichtliche Mission auffaßte, dem im künst­lerischen Schaffen Schönheit zu gleicher Zeit Wahrheit, Ausleben der Erkenntnis sein sollte. Religiöses Fühlen und Empfinden war ihm zugleich die Seele des künstlerischen Schaffens, und die Kunst war ihm etwas Heiliges. Für ihn hatte der Künstler eine Art priesterlichen Beruf, und das, was Richard Wagner als Künstler der Menschheit schenkte, sollte in seinem Sinne eine religiöse Weihe haben, eine reli­giöse Aufgabe und Mission im Entwicklungsgang der Menschheit erfüllen. So empfand er sich selbst als einen",
      "derjenigen, die ihrem Zeitalter aus der Tiefe und Fülle der Wahrheit heraus etwas geben wollen.",
      "Wenn die Geisteswissenschaft nicht eine abgezogene graue Theorie, nicht ein Schweben in einem weltfremden Wolken­kuckucksheim sein soll, dann muß sie den Weg finden, um eine so bedeutsame geistige Erscheinung wie Richard Wag­ner von ihrem Gesichtspunkte aus zu verstehen und zu würdigen. Das kann sie, wenn sie in der richtigen Art ver­standen wird.",
      "Richard Wagner hat in sich das Gefühl, die Empfindung gehabt, die ihn hinleiteten zu denselben Wahrheiten von den Ursprüngen der Menschheitsentwicklung, zu denen uns auch die Geisteswissenschaft weist. Etwas verbindet Richard Wagner tief mit dem geisteswissenschaftlichen Füh­len und Empfinden, mit aller wahren Mystik: das, was er bei sich den Zusammenklang der verschiedenen Künste, die Einheit der Künste, das liebevolle, harmonische Zusam­menklingen der Künste nennt. Das, was er als einen Mangel unseres künstlerischen Wirkens der Gegenwart empfand, war dasjenige, was er die Selbstsucht, den Egoismus der einzelnen Künste nannte. Er empfand ein Ideal über ihm schwebend, welches sich ihm so darstellte, daß nicht die eine Kunst den einen Weg und die andere ihren anderen Weg geht, sondern daß eine Harmonie der Künste sich herausgestaltet, zu der alle zusammenwirken können in selbstloser Weise und liebevoller Hingabe. Er sagt, eine solche Kunst oder ein solches künstlerisches Ideal hat es im Laufe der Weltenentwicklung einmal gegeben. Namentlich suchte er ein solches Ideal im alten Griechentum, das voran­gegangen war der künstlerischen Epoche des Sophokles, Euripides und anderen. Er sagt, bevor die Künste sich ge­spalten haben, bevor das dramatische Kunstwerk für sich, der Tanz für sich war, haben sie zusammengewirkt, sind in",
      "selbstlosem Streben vereinigt gewesen in dem Gesamtkunst­werk. Dieses Gesamtkunstwerk ahnt er in einer Art hell­sichtiger Schau. Die Historie erwähnt nichts davon, aber sie muß ihm recht geben, denn sie geht zu dem Urstand der verschiedenen Völker zurück, wo nicht nur die Künste zu­sammengewirkt haben zu einer einheitlichen großen Har­monie, sondern wo zusammengewirkt haben die verschie­denen Geistes- und Kulturströmungen überhaupt.",
      "Das, was wir heute Kunst und Wissenschaft nennen, sieht die Geisteswissenschaft als verschiedene Zweige an, die aus einer einzigen Wurzel herausgewachsen sind. Ob wir in die alte Griechenzeit zurückgehen, ob in die alte ägyptische Zeit, ob zu den indischen und persischen Völkern, ob wir in unsere germanische Heimat selbst zurückgehen: überall treffen wir auf eine Urkultur, die unsere materialistische Forschung nicht, aber die hellseherische Schau erreichen kann. Wir treffen auf eine Kultur, wo es eine gesonderte Wissenschaft und Kunst nicht gab, wo alles vereinigt war, wo alles so war, daß man geneigt war, es Mysterium zu nennen. Bevor es Kunststätten, bevor es wissenschaftliche Stätten gab, gab es Mysterienstätten. Was waren sie? Sie waren eine Vereinigung von Weisheit, Schönheit und reli­giöser Frömmigkeit.",
      "Wir können uns eine Vorstellung machen, was in jenen Tempelstätten, die zu gleicher Zeit Schulen und zu gleicher Zeit die wahren künstlerischen Stätten waren, vorging, wenn wir uns vor die Seele malen das große Weltendrama, von dem, wie gesagt, die materialistische Geschichte nichts zu melden hat, das sich aber abgespielt hat vor den zu den alten Weihestätten, den Mysterien Zugelassenen. Der, wel­cher da zugelassen wurde, sah in dramatischer Darstellung alles, was man aufbringen konnte an dramatischer Re­präsentation, an musikalischer Leistung, durchtränkt von",
      "dem, was man glaubte, an Weisheit ergriffen zu haben, und durchtränkt von dem, zu dem die Seele in wahrhaft reli­giöser Frömmigkeit aufschaute. In wenigen Worten können wir vor die Seele hinmalen, wie es ausgeschaut hat in jener Zeit, aus der uns keine Urkunden als die der Geisteswissen­schaft etwas melden. Da wurden die, welche zugelassen wurden, vereinigt, um eine Art Weltschöpfungsdrama an­zuschauen. Solche Weltschöpfungsdramen hat es überall gegeben. Da wurde gezeigt, wie göttliche Urwesenheiten aus geistigen Höhen sich herunterbewegten, wie sie ihr Wesen einströmen ließen in den Weltenstoff und wie sich der Weltenstoff formte zu den verschiedenen Naturwesen, zu den verschiedenen Naturreichen, das mineralische Reich, das Pflanzenreich, das tierische Reich und das Menschenreich, wie also das Göttliche hineinströmte in dasjenige, was draußen in den verschiedenen Naturwesen uns entgegenleuchtet und entgegenblickt, wie dann dieses Göttliche eine Art von Auferstehung in den menschlichen Seelen feiert.",
      "Dasjenige, was tiefere Persönlichkeiten immer empfun­den haben, daß die Welt von einem Göttlichen ausgeströmt ist, daß dieses Göttliche in den Menschenseelen zu einem Bewußtsein kommt, gleichsam aus den menschlichen Augen und Sinnen herausschaut und sich selbst in seinem Schaffen betrachtet, dieser Abstieg und diese Auferstehung des Gött­lichen wurde in Ägypten in dem Osiris-Drama und in den verschiedensten Weihestätten Griechenlands begangen. Der­jenige, der da zuschauen durfte und sah, wie alles, was an Kunst und Weisheit da war, dazu diente, um dieses Welten­schöpfungsdrama darzustellen, der empfand gegenüber die­sem Drama, das man Urdrama nennen könnte, zunächst eine religiöse Stimmung. Verehrungs- und ehrfurchtsvoll sah er den Gott, der herunterstieg in die Materie, in allen Wesen schlummern und in der Menschenseele auferstehen.",
      "Ehrfurchtsvoll genoß er jene Stimmung, die Goethe einmal schön und bedeutungsvoll ausgedrückt hat in den Worten:",
      "«Wenn die gesunde Natur des Menschen als ein Ganzes wirkt, wenn er sich in der Welt als in einem großen, schö­nen, würdigen und werten Ganzen fühlt, wenn das har­monische Behagen ihm ein reines, freies Entzücken gewährt, dann würde das Weltall, wenn es sich selbst empfinden könnte, als an sein Ziel gelangt, aufjauchzen und den Gipfel des eigenen Wesens und Werdens bewundern.» Und eine wunderbare religiöse Stimmung ergoß sich in die Herzen der Zuschauer dieses Weltendramas.",
      "Aber nicht bloß religiöse Stimmung war es, die vorhanden war, auch Weisheit war es, dasjenige, was später der Mensch in Form von wissenschaftlichen Begriffen, in Form von Ideen und Vorstellungen sich klarmachte über die Weltentstehung und ihre Wesenheiten. Das sah man hier vor Augen: Weis­heit, die geschaut wurde im äußeren Bilde, und Wissen­schaft, die zugleich Religion war. Da man alles das, was man an Schönheit aufbringen konnte, äußerlich in Bildern ausdrücken konnte, und da die Weisheit zur Frömmigkeit stimmte, so war dieses Weltendrama Wissenschaft und Kunst zu gleicher Zeit.",
      "Daß es so eine ursprüngliche Harmonie gegeben hat, lebte als dunkle Ahnung in der Seele Richard Wagners. Er sah freilich zunächst auf jene Urkultur im alten Griechen­land, die noch religiösen Charakter hatte, und er sagte sich, da wirkte noch nicht Musik, noch nicht Drama, noch nicht Tanz und Architektur für sich, sondern im grauesten Alter­tum wirkten alle zusammen: Religion, Kunst und Weisheit überhaupt. Und dann, so sagte sich Richard Wagner, sind die Künste herausgetreten aus ihrer Selbstlosigkeit, da wur­den sie selbstsüchtig und egoistisch. Nun hatte Richard Wagner eine große ahnungsvolle Intuition. Er schaute",
      "zurück in die Zeiten urferner Vergangenheit, wo die Men­schen noch nicht so individuell waren wie heute, noch nicht so persönlich wie später, als sich die einzelnen Menschen noch als Glieder ihres Stammes, ihres ganzen Volkes fühl­ten, wo man noch dasjenige als Realität ansah, was man Volksgeist, Stammesgeist nannte. In jene alten Zeiten einer natürlichen Selbstlosigkeit sah Richard Wagner zurück, und ihm ging die Idee auf: Um ein Selbst zu sein, mußten die Menschen jene alten Stammesgemeinschaften verlassen, das persönliche Element mußte hervortreten. Nur auf Grund des persönlichen Elementes konnten die Menschen ihre Frei­heit gewinnen. Diese ist aber nicht zu gewinnen ohne eine Art von Egoismus. So sah Richard Wagner zurück in alles das, was die Menschen zusammengehalten hat. Die Men­schen mußten diese Selbstlosigkeit verlassen, bewußter und bewußter mußten sie werden. So stellte sich ihm die urferne Vergangenheit dar. Und dann sagte er sich: Nachdem sie die Freiheit errungen haben, müssen sie den Weg wieder zurückfinden zu Bruderbünden, zu liebevollen Verbänden, und aus der Bewußtheit heraus muß der selbstsüchtige Mensch wieder selbstlos werden. Die Liebe muß wieder alle durchdringen.",
      "Das erscheint ihm als Ideal einer fernen Kunst, und so verbindet sich bei ihm die Gegenwart mit der Zukunft, und die Kunst ist es, der er eine wichtige Stellung in bezug auf die Entwicklung anweist. Die Kunst scheint ihm parallel­gehend mit der Menschheitsentwicklung zu sein. Wie die Menschheit, so haben sich die Künste entwickelt. Aus einer Gesamtheit der Künste hervorgehend, wurden die Künste egoistisch. Das Drama, die Architektur und der Tanz wur­den etwas für sich. So ist es geworden in der Gegenwart. Parallel der egoistisch gewordenen Welt haben wir die egoistisch gewordene Kunst. Er blickt hin auf eine Zeit, wo",
      "auch die Kunst wieder eine Kunstgemeinschaft haben wird. Daher nennt man Richard Wagner den «Kommunisten» der Künstler, weil er einen «Kommunismus» der Künstler so vor Augen hatte. So sieht er im Zusammenklang der Künste, zu dem er sein Scherflein beitragen will, einen mächtigen Hebel, um aus der Selbstlosigkeit der Kunst heraus etwas in die Seelen der Menschen zu gießen von jener Selbstlosigkeit, die einen zukünftigen menschlichen Bruderbund begründen muß. So war er künstlerisch ein Missionar menschlicher sozialer Selbstlosigkeit, indem er in jede Menschenseele jenen Impuls gießen wollte, der die Seele hinleitet zur inneren Selbstlosigkeit, die die Menschen in Harmonie verbindet. Wahrhaftig, ein großer Missions­gedanke, der vor Richard Wagners Seele auftauchte, ein Missionsgedanke, den nur eine Persönlichkeit haben konnte, ganz durchdringen konnte, die in sich selber etwas von dem wirklichen geistigen Impuls, die einen tiefen Glauben an die Wahrheit des geistigen Lebens hatte. Diesen tiefen Glau­ben aber hatte Richard Wagner.",
      "Wir können uns an einem seiner Werke, zunächst vor­bereitend, diesen Glauben Richard Wagners an die geistige Welt hinter der sinnlichen vor die Seele halten, an seinem «Fliegenden Holländer». Schon da tritt uns Richard Wag­ners richtiger und wahrhaft redlicher Glaube an die geistige Welt hinter der sinnlichen entgegen. Halten Sie sich vor Augen, daß ich nicht im entferntesten behaupte, daß die Gedanken, die hier ausgesprochen werden, bewußt vor der Seele Richard Wagners standen, ebensowenig wie die Ge­danken der Botaniker oder Lyriker bewußt in der Pflanze leben. Aber wie der Botaniker oder Lyriker an ihr emp­findet, so lebte Richard Wagner im Sinne dieser Vorstel­lung und im Sinne dieser geistigen Gesetze.",
      "Der materialistische Mensch sieht die Menschen um sich",
      "herum an und er sieht sie in sinnlicher Abgeschlossenheit im materiellen Dasein nebeneinanderstehen. Die Seele ist ein­geschlossen in sinnliche Leiber, und so glaubt der Materia­list, daß es keine andere Art von Gemeinschaft gäbe zwischen Mensch und Mensch als diejenige, die äußerlich, sinnlich vermittelt wird.",
      "Was der einzelne Mensch dem anderen sagen kann, was der einzelne dem anderen tun kann, ist rein äußerlich, materiell wirklich; daran glaubt der materia­listische Denker. Daß es eine verborgene Gemeinschaft der Menschen gibt, daß es etwas gibt, was von Seele zu Seele wirkt, auch wenn kein äußerliches Wirken durch sprach­liche oder materielle Mittel da ist, davon ist derjenige überzeugt, der etwas weiß von der geistigen Welt hinter der sinnlichen Welt.",
      "Geheime geistige Wirkungen gehen und strömen von Seele zu Seele. Dasjenige, was einer denkt und fühlt, auch wenn es innerhalb der Seele beschlossen bleibt, ist nicht bedeutungs- und wertlos für den anderen Menschen, auf den sich die Gedanken und Gefühle be­ziehen.",
      "Der materialistische Denker weiß bloß davon, daß der andere Mensch mit der Hand berührt werden kann, daß man ihm mit materiellen Mitteln beistehen kann. Er glaubt nicht, daß das Gefühl, das in ihm lebt, eine reale Bedeutung für die anderen Menschen hat, daß Seele und Seele durch Bande verknüpft ist, die man nicht mit sinn­lichen Augen sehen kann.",
      "Der Mystiker weiß, daß ein sol­ches Band von Seele zu Seele sich schlingt. Richard Wagner war tief durchdrungen davon, daß das der Fall ist.",
      "Wenn wir uns klarmachen wollen, was damit angedeutet ist, dann blicken wir zurück auf eine schöne mittelalterliche Sage, die der heutige Mensch nur als Sage empfindet, die aber für denjenigen, der sie geschrieben hat, und für den, der sie mystisch zu verstehen weiß, etwas anderes ist als eine Sage, nämlich der Ausdruck einer geistigen Wirklichkeit.",
      "Da erinnert uns eine Sage, die uns ein mittelalterliches Epos überliefert hat, an den armen Heinrich, der eine furcht­bare Krankheit hatte. Da hören wir, daß nur eines den armen Heinrich von seiner furchtbaren Krankheit heilen kann, nämlich wenn sich ein reines weibliches Wesen für ihn opfert.",
      "Die Liebe der reinen weiblichen Seele ist im­stande, etwas zu bedeuten, etwas Reales zu sein für das andere Menschenleben. Daß Seele für Seele im rein geistigen Reiche etwas füreinander sein können, wovon sich das mate­rialistische Denken keine Vorstellung macht, das liegt hinter einer solchen Sage.",
      "Die Opferung des reinen weiblichen Wesens für den armen Heinrich, ist sie denn schließlich etwas anderes als ein sinnlicher Ausdruck für dasjenige, was ein großer Teil der Menschheit überhaupt als die mysti­sche Wirkung des Opfers ansieht? Ist denn das Opfer dieser Jungfrau für den armen Heinrich nicht dasjenige, was der Erlöser am Kreuze für die Menschheit dargebracht hat, ist es nicht jene mystische geistige Wirkung von Seele zu Seele?",
      "Daß hinter dem Äußeren etwas leben kann, das sehen wir da, da glaubt das Bewußtsein ahnungsvoll, daß es eine solche Geistigkeit gibt. Deshalb kam Wagner zu der Sage vom Fliegenden Holländer, jenem Mann, der sich mit dem Materiellen verbunden hatte und keine Erlösung finden kann von dem Stoff, mit dem er verstrickt ist.",
      "Nicht mit Unrecht hat man den Fliegenden Holländer den Ahasver des Meeres, den Ewigen Juden des Meeres genannt. Wie in der Idee des Ewigen Juden etwas Tiefes liegt, so in der Idee vom Ewigen Juden des Meeres, vom Fliegenden Holländer.",
      "Betrachten wir uns den Ahasver von diesem Gesichts­punkte aus. Er ist der Mensch, der nicht glauben kann an den Erlöser, an eine Persönlichkeit, die die Menschheit vor­wärtsführt zu größeren Höhen, zu immer vollkommeneren und vollkommeneren Stufen der Entwicklung. Der Ahasver",
      "ist verstrickt in das bleibende Dasein; während der Mensch in Wahrheit, wenn er weiterkommen will, aufwärtssteigen muß von Stufe zu Stufe, kann sich der, welcher nicht stre­ben will, mit der Materie verbinden. Er kann demjenigen Hohn sprechen, der Führer der Menschheit zu höheren und höheren Stufen ist.",
      "Dann muß er in die Materie verstrickt werden. Was heißt es: In die Materie verstrickt werden? Wer in die Materie verstrickt wird, für den wiederholt sich das äußere Leben im ewigen Einerlei. Denn dadurch unter­scheidet sich das materielle vom geistigen Auffassen, daß das Materielle sich immer wiederholt, während der Geist aufsteigt.",
      "In dem Augenblicke, wo der Geist der Materie verfällt, verfällt er der Wiederholung des immer Gleichen. Und so ist es mit dem Fliegenden Holländer. In jenen alten Zeiten hatten die verschiedenen Völker das Bekanntwerden mit fremden Ländern benützen können, um die Ideen im­mer höher und höher zu heben.",
      "Wer dieses erreichen konnte, der betrachtete das Fahren über das Meer, das Hinausstür­men zu fremden Küsten als ein bloßes Mittel der Vervoll­kommnung der Menschheit. Derjenige, der die Vollkom­menheitsidee, das Fließen der Geistesströmung nicht spürte, verstrickte sich in das Einerlei des bloß zur Materie, zum Stofflichen Gehörigen.",
      "Der Fliegende Holländer, der seinen Hang nur zum Stofflichen hat, wird verlassen von den Kräften der Entwicklung, von der Liebe, die das Mittel ist zur Vervollkommnung, das Mittel zum Aufstieg, zur Ent­wicklung, so daß er sich in die Materie, in die Stoffe hinein­spinnt und sich für ihn dasselbe dann in ewiger Wieder­holung wiederholen muß. Solche Wesen, die nicht ergriffen, nicht erfaßt werden können zu einem höheren Aufstieg, müssen berührt werden von jungfräulichem Wesen.",
      "Jung­fräulich und von reiner Liebe erfüllt muß das Wesen sein, das den Fliegenden Holländer erlösen kann.",
      "Die Seele, die noch nicht in den Stoff verstrickt ist, hat eine Beziehung zu der Seele, die in den Stoff verstrickt ist. Das ahnt Richard Wagner und das drückt er in seinem Drama in so bedeutungsvoller Weise aus.",
      "Das war ein mystisches Empfinden der Wahrheit, das war die Empfin­dung der Gemeinschaft der Geister, die hinter der Gemein­schaft des Stoffes ist. Wahrhaftig, ein solcher, der so fühlte, durfte sich eine so hohe geistige Mission zuschreiben, wie Richard Wagner sie sich zuschrieb, der durfte seine Ge­dankenflüge hinlenken in Gebiete, wo er über Musik und Drama ganz anders dachte, als man vor ihm gedacht hat.",
      "Er sah in seiner Art zurück in jene griechische Urzeit, wo es einheitliche Kunstwerke gab, wo die Musik nur zum Aus­druck brachte, was das übrige Dramatische nicht in seiner Vollständigkeit zum Ausdruck bringen konnte, wo die ewigen Weltgesetze in dem Rhythmus des Tanzes zum Ausdruck kamen. Er sah etwas in dem alten Kunstwerk, wo noch zusammenwirkten Tanz, Rhythmus und Harmo­nie im dramatisch-musikalischen Kunstwerk des urfernen Altertums.",
      "Es erstand vor ihm eine eigentümliche Anschau­ung über das Wesen des Musikalischen. Das eigentliche Wesen des Musikalischen sah Richard Wagner in der Har­monie der Töne. Aber er sagte sich, nur dann, wenn die Schwesterkünste dasjenige, was sie hineinzugeben haben, hergeben für die Harmonie, dann strömt von solchen Schwe­sterkünsten in die Harmonie der Musik etwas ein.",
      "Die eine der Künste ist der Tanz. Nicht der Tanz, der später die Menschheit ergriff, sondern der, welcher in den Formen des Tanzes Bewegungen in der Natur und Bewegungen der Sterne ausdrückt. So war der alte Tanz.",
      "Der alte Tanz war herausgeboren aus einem Erfühlen der Naturgesetze, durch eigene Bewegung ein Nachbild dessen, was in der Natur sich bewegte. Dieses Wesen des Tanzrhythmus strahlte",
      "hinein in die musikalische Harmonie und gab der Harmonie der Musik den Rhythmus. Dann trat die andere Schwester­kunst hinzu, die Dichtung. Sie konnte nur einiges in Worten ausdrücken. Aber dasjenige, was Worte nicht ausdrücken konnten, das mußten die Schwesterkünste zum Ausdruck bringen. So wirkten Tanz, Musik, Dichtung in Harmonie und es entstand das Musikalische als Dreiklang von Har­monie, Rhythmus und Melodie. Es entstand, weil die Schwesterkünste zusammenwirkten.",
      "Das stand vor dem Mystiker als der Geist des alten Kunstwerks, wo noch nicht Melodie, Rhythmus und Har­monie in der späteren Vollkommenheit da waren. Das weiß Richard Wagner und das weiß auch der Mystiker. Nun sagte er sich: in späterer Zeit trennten sich die Künste, die hier schwesterlich zusammenwirkten. Der Tanz wurde etwas für sich, die Dichtung wurde etwas für sich. Dadurch wurde das rhythmische Erleben als etwas für sich hin-gestellt und ebenso auch die Musik, die nichts mehr wissen wollte von der Schwester, ebenso wie die Dichtung sich trennte von dem Musikalischen und nichts mehr hinein­strömen konnte in das Musikalische.",
      "Richard Wagner sah, wie mit der Zunahme der Egoismen der Menschen die Künste egoistischer wurden, und er ver­folgte so die Künste bis in die neueste Zeit hinein. Wir können ihm jetzt nicht folgen, wie er seine Künste verfolgt, wie sie selbständiger und egoistischer werden. Sehen wir, wie er selbst versuchen will, aus den Einseitigkeiten, die ihm vorliegen, etwas Harmonisches zu schaffen. Da wollen wir ihm folgen, da zeigt sich seine ganze Größe, die hinter das Wesen der Dinge auf diesem Gebiete zu kommen sucht.",
      "Zwei Geister standen vor Richard Wagners Seele, die die Einseitigkeit der Künste pflegten, die er zusammenbringen wollte. Die Einseitigkeit des Musikalischen und die Einseitigkeit",
      "des Dramatischen zeigten Beethoven und Shake­speare. Shakespeare war für Richard Wagner der einseitige Dramatiker, weil es für Richard Wagner klar war, daß, wenn er sein tiefes Inneres betrachtete, die ganze Stufen­leiter der Empfindungen und Gefühle, die man von außen nicht sehen kann, die nicht in Gesten, nicht einmal in Worte übergehen kann, wenn es sich um Wesenhaftes handelt, daß diese Stufenleiter der Empfindungen nicht im Wortdrama zum Ausdruck kommen kann.",
      "Das Wortdrama stellt die Handlung dar, wenn sie schon hinausgetreten ist aus den inneren Impulsen in Raum und Zeit. Wenn das Drama sich abspielt, so müssen wir schließen, daß die Person die Im­pulse schon erlebt hat.",
      "Wir sehen das schon alles übergehen in das, was das Auge sehen und das Ohr hören kann und nicht mehr als das, was sich abspielt als Dramatik im Innern der Person selbst. So muß der Dramatiker sich ausschwei­gen über dasjenige, was als die tieferen Gefühle und Emp­findungen die Untergründe für dasjenige darstellen, was sich äußerlich auf der Bühne zeigt.",
      "Auf der anderen Seite sind ihm die einseitigen Künstler die Symphoniker, die reinen Instrumental-Musiker, diejenigen, die wirklich in ihrem wunderbaren Tongefüge dasjenige darzustellen ver­mögen, was im Inneren der Seele vorgeht, die innere Dra­matik, die aber gestenlos bleibt, die nicht nach außen in Raum und Zeit überströmt. So hat er auf der einen Seite die musikalische Kunst, den Ausdruck des menschlichen Innern, die, wenn sie nach außen will, ihr Unvermögen fühlt, und auf der anderen Seite hat er die dramatische Kunst, die mit der musikalischen Kunst sich nicht ver­schwistert, die erst darzustellen vermag, wenn die Impulse in Raum und Zeit hinausgeflossen sind.",
      "Shakespeare - Mo­zart, Haydn, Beethoven stellen ihm zwei Seiten dar, künst­lerisch ausgeprägt. In Beethovens Neunter Symphonie sieht",
      "er etwas, was die eine einseitige Kunstform aus sich heraus durchbrechen will. Er sieht, wie in der Neunten Symphonie gleichsam die Hüllen zerspringen, wie sie gleichsam sich auslebt im Wort, weil sie in Liebe die ganze Menschheit umfassen will, weil sie hinausdrängt in die ganze Welt. Da sieht er etwas, was hinaus will in Raum und Zeit; und es noch weiter hinauszuführen in Raum und Zeit, das betrach­tet er als seine Mission. Nicht nur so, wie es in der Neunten Symphonie ist, den Ausdruck der Empfindungen, die innere Dramatik der Seele ausströmen zu lassen, nicht nur so, wie es da ist, wünscht er es, sondern er wünscht es einfließen zu lassen in Wort und Handlung, so daß man beide vor sich auf der Bühne hat, die innere Skala der Empfindungen in der Musik und in der Dramatik das - weil sie herausgeht in Raum und Zeit -, was die innere Skala der Empfin­dungen zu äußeren Handlungen bildet. Shakespeare und Beethoven in einer höheren Einheit - das will er sein. Den ganzen Menschen will er darstellen.",
      "Sehen wir eine Handlung auf der Bühne, dann sollen wir nicht bloß sehen, was sich vor Augen und Ohren abspielt, sondern wir wollen auch hören, was die innersten Impulse des menschlichen Wesens sind. Deshalb genügt Richard Wagner auch die alte Oper nicht. Denn da waren Dichter und Musiker jeder für sich. Der Dichter drückte aus, was er auszudrücken hatte, der Musiker kam hinzu, um die Dich­tung auszudrücken. Die Musik aber soll dazu da sein, um auszudrücken, was die Dichtung nicht ausdrücken kann. Das menschliche Wesen besteht aus dem Inneren, das im Äußeren nicht zum Ausdruck kommen kann, und aus dem Äußeren, das zwar im Wortdrama zum Ausdruck kommen kann, aber sich ausschweigen muß über die inneren Impulse. Deshalb muß das Musikalische nicht so sein, daß es die Dichtung illustriert, sondern so, daß es die Dichtung vervollständigt.",
      "Die Musik muß ausdrücken, was die Dichtung nicht ausdrücken kann.",
      "Das ist der große Gedanke Richard Wagners. So will er schaffen, so schreibt er sich seine Mission zu für ein selbst­loses Zusammenwirken von Musik und Dichtung in einem Gesamtkunstwerk. Und so sehen wir im Grunde genommen diesen seinen Grundgedanken auf eine mystische Grund­lage zurückgehen, auf jene Grundlage, die den ganzen Menschen erfassen will, nicht den äußeren Menschen bloß, sondern den ganzen Menschen, der durchdrungen ist von dem inneren.",
      "Der Mensch ist mehr als das, was sich äußer­lich auslebt. Richard Wagner weiß, daß in des Menschen Inneren ein höheres Selbst ruht, ein höheres Selbst vor­handen ist. Aber nur teilweise kommt in dem, was in Raum und Zeit erscheint, das höhere Selbst zum Ausdruck.",
      "Aber das innere Höhere, was über das Gewöhnliche hinausgeht, will Richard Wagner erfassen. Daher genügt ihm das eine Mittel nicht, sondern er sucht, was den Menschen in ver­schiedener Weise erfassen kann.",
      "Er muß daher auch seine Zuflucht nehmen zu dem, was hinausgeht über die unmittel­bare Persönlichkeit, was sich erhebt zum Übermenschlichen. Das geschieht im Mythos. In der mythischen Individuali­tät tritt uns nicht der einzelne Mensch entgegen, sondern gleichsam ein Übermenschliches.",
      "Was der Übermensch im Menschen bedeutet, das drückt uns der Mythos aus. Was nicht in einem, sondern in vielen Menschen lebt, das drücken uns mythologische Figuren wie Siegfried und Lohengrin aus. Weil Wagner in das Tiefste der Menschen gehen wollte, brauchte er die übermenschlichen Persönlichkeiten der Mythen.",
      "Wie tief er hineingreift in den ganzen Werde- und Ent­wicklungsprozeß, können wir verstehen, wenn wir ihm nur ein bißchen folgen. Zu den höchsten menschlichen Rätselfragen,",
      "wie sie sich aussprechen in so großartiger Weise in dem Nibelungendrama und im Parsifaldrama, erhebt er sich und sucht sie herauszugestalten aus der Anschauung, der Empfindung und dem Gefühl für die ganze Menschheit.",
      "Wir können nun einzelne Streiflichter auf dasjenige werfen, in dem Richard Wagners künstlerische Seele lebt. Wir werden sehen, wenn wir auch nur weniges heraus-greifen, wie tief er verbunden ist mit dem, was man die mythischen Zusammenhänge der Menschheit nennt.",
      "Warum greift Wagner gerade zum Siegfrieddrama? Was wollte er damit darstellen? Wir gelangen am leichtesten dazu, wenn wir anknüpfen an Richard Wagners Idee von der ganzen Menschheitsentwicklung. Er sah zurück in die Urzeiten, wo der Mensch durch enge Stammesbande der Menschheit in einer ursprünglichen, selbstlosen Liebe verknüpft war.",
      "Er sah zurück in jene Zeiten, wo die Menschen sich so fühlten, daß der einzelne seine Selbständigkeit in seinem dumpfen Bewußtsein noch nicht empfand, sondern sich als ein Glied in einem Stamme fühlte, zu dem er gehörte, daß er gleich­sam in der Stammesseele etwas Wirkliches, etwas Reales fühlte. Vor allen Dingen spürte Richard Wagner, wie das­jenige, was in Europa lebte, zurückführt in uralte Zeiten, wo eine ursprüngliche Liebe die Menschen noch zu brüder­lichen Gruppen und Verbänden vereinigte.",
      "Er blickte auch zurück in jene Zeiten, von denen die geisteswissenschaftliche Weltanschauung spricht, die sagt, daß alles in Entwicklung ist. Die geisteswissenschaftliche Anschauung sagt uns, daß auch das Bewußtsein sich nach und nach entwickelt hat.",
      "Das heutige klare Bewußtsein hat sich aus Zuständen entwickelt, von denen spärliche Nachklänge noch vorhanden sind. Im Traumbewußtsein, im Bildertraum sah Richard Wagner Nachklänge eines Bilderbewußtseins, das früher der ganzen Menschheit eigen war.",
      "Das heutige Tagesbewußtsein, das",
      "vom Morgen bis zum Abend, bis zum Einschlafen dauert, hat ein viel dumpferes Bewußtsein verdrängt. In diesem alten, dumpfen Bewußtseinszustand hingen die Menschen viel tiefer zusammen. Da kam die menschliche Individuali­tät noch nicht so heraus wie später und damit auch nicht der menschliche Egoismus, der eine notwendige Stufe in der menschlichen Entwicklung bedeutet. Richard Wagner sah, daß es eine natürliche Liebe gab, die schon im Blute lag und die einzelnen Blutsverwandten zusammenknüpfte.",
      "Nun will ich aus der rationalen Mystik heraus eine An­schauung darlegen, die für diejenigen, welche die anderen Vorträge nicht gehört haben, etwas Groteskes haben, aber für die anderen etwas Mathematisch-Sicheres bekommen wird. Dasjenige, was heute in Europa lebt als heutiges klares Tagesbewußtsein, hat sich aus einer uralten Mensch­heit entwickelt, der atlantischen Menschheit, die der uns­rigen vorangegangen ist und da gelebt hat, wo heute die Fluten des atlantischen Ozeans sind. Diejenigen, welche achtgeben auf das, was in der Welt vorgeht, werden wissen, daß selbst die Naturwissenschaft schon von einem atlan­tischen Kontinent spricht. Auch in der naturwissenschaft­lichen Zeitschrift «Kosmos» erschien ein Artikel darüber. Da lebten die Vorfahren der Menschen, die heute Europa bewohnen, unter anderen physikalischen Bedingungen. Sie lebten noch in Luft und Wasser. Der Boden war weithin bedeckt mit großen, mächtigen Nebelmassen. Damals sah man nicht die Sonne, wie man sie heute sieht. Sie war um­geben von mächtigen Farbenhöfen, weil alles bedeckt war mit mächtigen Nebelmassen. Die germanische Sagenwelt hat das Gedächtnis an jene alten Lande in dem Ausdruck Niflheim, Nibelungenheim bewahrt. Das sind die Erinne­rungen an jenes alte Nebelland, und es ist eine feine, intime Wendung in dem, was sich aus jener Urzeit als Sage erhalten",
      "hat, daß, als die Flut allmählich die atlantischen Lande überspülte, dieselbe Flut auch die Flüsse der deutschen Tief­ebene gebildet hat, so daß das Wesen des Rheins angesehen wird wie ein Überbleibsel jenes Wesens, das als das atlan­tische Nebelwesen einstmals weithin die Lande bedeckt hat. Es ist so, wie wenn das Rheinwasser abgeflossen wäre aus den Nebelmassen der alten Atlantis, des Nebelheims, des Nibelungenheims. So stellt die Sage das in dumpfem, ahnungsvollem Bewußtsein dar. Und indem die Völker ostwärts zogen, weil die physischen Verhältnisse so wurden, daß sie die Gegenden verlassen mußten, verließ sie das dumpfe Bewußtsein. Dieses wurde heller und heller, der Egoismus wurde aber auch größer.",
      "Das alte dumpfe Bewußtsein hatte eine gewisse Selbst-losigkeit zur Folge. Mit dem Reinigen der Luft zog der Egoismus herauf. Der Nebeldunst der alten Atlantis bildete rings um den Menschen eine Atmosphäre von Weisheit, die erfüllt war von Selbstlosigkeit, von Liebe. Das strömte in die Wasser des Rheins und ruhte da unten als Weisheit, als Gold. Wenn das aber vom Egoismus erfaßt wird, dann gibt es zu gleicher Zeit die egoistische Macht. So sahen die Re­präsentanten der alten Bewohner von Nibelungenheim, als sie ostwärts zogen, den Rhein den Hort in sich schließen, der aus dem Gold der Weisheit bestand, die einstmals in selbstloser Art gewirkt hat. Das alles ruhte - nicht so aus-gesprochen - in der Sagenwelt, deren sich Richard Wagners Seele bemächtigte. Und diese Seele war dem großen gei­stigen Wesen, das darinnen wirkte und das Gedächtnis der alten Tatsachen bewahrte, so kongenial, daß sie aus dieser Sagenwelt dasjenige herausholte, was der Extrakt seiner ganzen Weltanschauung war. So hören wir nachklingen in der Musik Richard Wagners und sehen im Drama über die Bühne schreiten das Werden und Weben des menschlichen",
      "Egoismus. Das Zusammenschließen des Rings, wir sehen es in dem, daß Alberich dem Rhein, den Wellenmädchen das Gold abnimmt. In Alberich sehen wir den egoistisch gewor­denen Repräsentanten der Nibelungen. Wir sehen den Menschen, welcher der Liebe, die den Menschen in ein Gan­zes hineingestellt hat, abschwört. Die Macht des Besitzes verknüpft Richard Wagner mit der Idee, die in jener Sagen-welt webt. So sieht er jene alte Welt. Es tritt ihr entgegen diejenige Welt, die Walhalla begründet hat, es tritt entgegen die Welt des Wotan der Welt der alten Götter. Sie haben dasjenige, was alle Menschen gemeinsam hatten. Sie stellen eine Art von Gruppenseele dar, so auch Wotan. Aber da, wo die Einzelpersönlichkeit ergriffen wird von dem Ring, der sich um das Ich des Menschen spannt, wird auch er er­faßt von der Gier nach Gold. So sehen wir das, was als Volksseele in Wotan lebte, dasjenige, was der Mensch in egoistischer Art an dem Rheingold in sich erlebt, in einer feinen Art in Richard Wagners ganzer Kunst, in seinem ganzen Schaffen. Wir hören es aus den Klängen seiner Musik heraus. Wer sollte es nicht spüren können? Niemand sollte sagen, daß da in sein Werk etwas hineingelegt wird. Dagegen habe ich mich verwahrt. Aber wer sollte nicht spüren in der Es-Dur-Stelle des «Rheingold» das Ein­schlagen des Ich? Wie sollte das menschliche Ohr nicht spüren können das Auftreten des Ich in diesem langen Ton der Es-Dur-Stelle des «Rheingold»?",
      "So könnten wir bis in die musikalische Kunst hinein Richard Wagners mystisches Fühlen verfolgen.",
      "Wir sehen dann, wie sich Wotan auseinanderzusetzen hat nicht mit dem Bewußtsein, das sich von Seele zu Seele ge­sponnen hat, sondern mit dem, was sich noch nicht heraus­gesponnen hat da, wo das Volksbewußtsein noch lebendig gespürt worden ist. Dieses Bewußtsein tritt da auf, wo",
      "Wotan den Riesen den Ring entreißen will. Da tritt das alte Bewußtsein vor ihm auf in der Gestalt der Erda. Be­deutsam ist die Art, wie da gesprochen wird. Oder ist die Gestalt nicht so geschildert, daß sie die Repräsentantin des alten Bewußtseins ist, die nicht bloß weiß, was der Verstand verbindet, sondern auch weiß aus hellseherischem Bewußt­sein heraus, was in der Umwelt vorgeht?",
      "Bekannt ist dir,",
      "Was die Tiefe birgt,",
      "Was Berg und Tal,",
      "Luft und Wasser durchwebt.",
      "Wo Wesen sind,",
      "Wehet dein Atem;",
      "Wo Hirne sinnen,",
      "Haftet dein Sinn:",
      "Alles, sagt man,",
      "Sei dir bekannt.",
      "Man kann nicht klarer das Bewußtsein darstellen, das in Nebelheim war, man kann das alte Bewußtsein nicht klarer kennzeichnen, als es in den Worten ausgeprägt ist:",
      "Mein Schlaf ist Träumen,",
      "Mein Träumen Sinnen,",
      "Mein Sinnen Walten des Wissens.",
      "So war es: wie ein Träumen, aber ein Träumen, das wußte von der ganzen Umwelt, das wirkte von Mensch zu Mensch, das wirkte in die tiefste Tiefe der Natur hinein. Das war sein Sinnen, das war sein Wollen, sein Handeln, denn der Mensch handelte aus diesem Bewußtsein heraus. Dieses Be­wußtsein trat vor Wotan in der Erda hin. Es entstand da­durch ein neues Bewußtsein.",
      "In allem Mystischen wird das Höhere durch eine weib­liche Persönlichkeit dargestellt. Das ist es auch, was sich in Goethes schönen Worten im Chorus mysticus verbirgt:",
      "«Das Ewig-Weibliche zieht uns hinan.» Die verschiedenen Völker haben dieses Streben der Seele zu einem höheren Bewußtsein dargestellt als eine Vereinigung mit irgend­einem Weiblichen, in dem das Höhere in der menschlichen Seele dargestellt wird. Die Seele ist dasjenige, was von den Weltgesetzen durchstrahlt wird, und diese Weltgesetze sind es, mit denen sie sich wie in einer Ehe vereinigt. So sehen Sie, wie im alten Ägypten die Isis und wie überall sonst ein höherer Bewußtseinszustand der Seele als Weibliches hin-gestellt wird, und zwar in der Weise, wie es dem Charak­ter eines Volkes entspricht. Was das Volk als sein eigent­liches Wesen empfindet, das wird ihm dargestellt in der Verbindung des Menschen mit der betreffenden weiblichen Persönlichkeit entweder im Tod oder schon während des Lebens.",
      "Auf zwei Arten - das haben uns die Vorträge bisher gezeigt - kann der Mensch über die Sinnlichkeit hinaus­wachsen. Einmal kann er das Sinnliche abstreifen und sich verbinden mit dem Geiste im Tode oder schon hier im Leben, wenn sein geistiges Auge geöffnet wird. Dement­sprechend sehen wir, wie dieses Höhere, das der Mensch erleben kann, auch in der deutschen Mythe als eine weib­liche Persönlichkeit dargestellt wird. Für die Vorfahren der Mitteleuropäer ist es der Kriegsmann, der tapfer kämpft und auf dem Schlachtfelde fällt, der nach dem Tode in die geistige Welt geht, um mit dem Höheren vereinigt zu wer­den, daher kommt dem Kriegsmann die Walküre entgegen, die ihn hinaufträgt in die Welt des Geistigen. Die weibliche Figur der Walküre stellt die Verbindung mit dem höheren Bewußtsein dar. Wotan zeugt mit Erda die Brünnhilde, mit",
      "der sich Siegfried vereinigen soll, wenn er hingeführt wer­den soll zu dem geistigen Leben. Die Töchter der Erda stellen das höhere Bewußtsein des Eingeweihten dar. In Siegfried wächst der neue Mensch heran, der durch eine besondere Ausprägung und Vollkommenheit des Inneren schon während des Lebens die Vereinigung mit der Walküre vollziehen kann.",
      "Was die deutsche Sagenwelt birgt, was in ihr lebt, hat Richard Wagner zum Ausdruck gebracht. Auch das hat er zum Ausdruck gebracht, daß die alte Gruppenseele ab­sterben muß in einer Götterdämmerung, ebenso wie das individuelle Bewußtsein des Menschen in Siegfried sich ausleben muß. Das alles wirkte und lebte und webte in seiner Seele. Die höchsten Menschheitsprobleme lebten und wirk­ten in ihm, und er hat sie, insofern sie des Menschen Inneres darstellen, im Musikalischen, und insofern sie menschliche Taten darstellen, im Dramatischen dargestellt.",
      "So sehen wir, wie Richard Wagner als Künstler den höheren Werdegang des Menschen aus dem Mystischen her­aus schöpft. Das hat ihn auch dazu geführt, eine tief be­deutsame Gestalt zum Mittelpunkt einer solchen Dramen­schöpfung zu machen, die Gestalt des Lohengrin. Was ist der Lohengrin? Diesen Lohengrin verstehen wir nur, wenn wir sehen, wie sich die Sage im Volk einlebt während einer Zeit, wo in ganz Europa bedeutsame soziale Umwälzungen vor sich gingen. Wir verstehen, was in der Seele desjenigen lebte, der das Bild des Lohengrin in seiner Vereinigung mit dem Weibe, die bei Richard Wagner Elsa von Brabant ist, darstellt. Wir sehen, wie durch ganz Europa hindurch ein neues Zeitalter sich bildet, das Zeitalter, in dem das Ringen der menschlichen Individualität zum Ausdruck kommt. Mit etwas scheinbar ganz Prosaischem, hinter dem aber etwas ganz Tiefes steckt, können wir es ausdrücken. In Frankreich,",
      "Schottland, England, hinten in Rußland, überall sehen wir ein neues soziales Gebilde entstehen: die freie Stadt. Während draußen auf dem Lande die Menschen in den Nachklängen alter Stammesgemeinschaften lebten, strömten diejenigen Menschen, welche sich der Stammes-zusammengehörigkeit entreißen wollten, aus derselben her­aus in die Stadt. Da, in der Stadt, entstand das individuelle Freiheitsbewußtsein. Da lebten die Menschen, die sich den Zusammengehörigkeitsbanden entreißen wollten, die ihr Leben da einzig und allein leben wollten. Es war ein mäch­tiger Umschwung, der sich damals vollzog. Bisher war es der Name, der angab, wozu der Mensch gehörte und was er wert war. In der Stadt war der Name nichts wert. Was bekümmerte man sich da darum, aus welcher Familie der Mensch herausgewachsen war? Da war er so viel wert als er Können hatte. Da entwickelte sich der individuelle Mensch. Die Entwicklung von der Selbstlosigkeit zur Individualität wurde zur Entwicklung von der Individualität zum Bruder-bund. Das stellte in der Mitte des Mittelalters die Sage dar, indem das Alte ersetzt wurde durch das, was der Mensch aus seinem Inneren heraus sich selbst zu geben in der Lage war.",
      "Sehen wir zurück auf die alten führenden Priester-geschlechter, auf diejenigen, die früher Führer waren, auf diejenigen, die die Adelsgeschlechter, die Weisen abgegeben haben: sie stammten aus Familienverbänden. Daß sie einem solchen Verbande angehörten, daß sie das richtige Blut hatten, darauf kam es an. In der Zukunft wird es darauf nicht mehr ankommen. Der, welcher ein Führer der Mensch­heit sein wird, der kann unbekannt sein durch das, was ihn mit der Menschheit verbindet, da profaniert man ihn, wenn man ihm einen Namen gibt. Daher das Ideal der großen Individualitäten, das Ideal des namenlosen Weisen, das sich",
      "immer mehr herausbildet. Der namenlose Weise ist nicht durch das Herkommen etwas, sondern durch das, was er ist. Er ist die freie Individualität, die von den anderen aner­kannt wird, weil sie alles aus sich selbst ist, weil sie nichts anderes sein will, als was sie für die anderen ist. So steht Lohengrin als Repräsentant, als Führer der Menschheit zur Freiheit da. Das mittelalterliche Städtebewußtsein sehen wir repräsentiert in dem Weibe, das sich mit Lohengrin ver­bindet. Mit einer der großen Individualitäten der Mensch­heit verbunden wurde derjenige, der zwischen der Mensch­heit und den großen Wesen steht, der den Verkehr zwischen den großen Führern der Menschheit und den Menschen vermittelt. Ein solcher hat immer einen bestimmten Namen gehabt. Den nennt man in aller Geheim- und Geisteswissen­schaff mit dem technischen Namen des «Schwan». Der Schwan ist eine ganz bestimmte Stufe der höheren Geistes-entwicklung. Der Schwan vereinigt den gewöhnlichen Men­schen mit dem höheren Führer der Menschheit. Einen Ab­glanz von diesem sehen wir in der Lohengrinsage.",
      "Wir brauchen solche Dinge nicht in Begriffe zu fassen, die einer pedantischen Lebensauffassung entnommen sind. Ja, wir tun Unrecht, wenn wir es tun. Wir kommen nur zur Klarheit, wenn unsere Begriffe weitherzig werden, so daß uns die Dinge, die uns Richard Wagner verständlich macht, nicht pedantische Worthülsen sind, sondern Vorstellungen entzünden, die weit, weit sich ausspinnen. Gestatten Sie mir, daß ich nicht Begriffe mit pedantischen Konturen vor Sie hinstelle, sondern solche, die weite Perspektiven eröff­nen. Daher muß man eine Gestalt wie Lohengrin in ihrer welthistorischen Bedeutung hinstellen und zeigen, wie in Richard Wagners Seele sich ein Verständnis dafür angespon­nen hat und wie dieses Verständnis künstlerische Gestalt gewonnen hat.",
      "So ist es Richard Wagner auch gegangen mit der Idee vom heiligen Gral. Im letzten Vortrage: «Wer sind die Rosenkreuzer?» trat diese Idee vom heiligen Gral vor unsere Seele. Es ist höchst merkwürdig, daß in Richard Wag­ners Seele in einem bestimmten Zeitpunkte etwas aufleuch­tet, was wie ein Ahnen von jener großen Lehre des Mittel­alters, vom heiligen Gral war. Diese Lehre leuchtete ihm erst auf, als eine andere vorangegangen war. Im Jahre 1856 war es, als in Richard Wagners Seele die Idee auf­tauchte, die in dem Drama «Die Sieger» dargestellt werden sollte. Das Drama ist nicht ausgeführt worden. Das, was er aber hineingeheimnissen wollte, kam im «Parsifal» zum Ausdruck. Aber wohin die Idee ging, das stellt uns die Kon­zeption des Dramas «Die Sieger» dar:",
      "Ananda wird geliebt von einem Tschandalamädchen. Ananda aber ist durch das Kastenvorurteil weit getrennt von der Liebe des Tschandalamädchens. Er darf der Liebe des Tschandalamädchens nicht nachgehen. Er wird Sieger über die eigene Natur dadurch, daß er ein Zögling des Buddha wird. In der Anhängerschaft des Buddha findet er den Sieg, da findet er sich zurück, da überwindet er die menschliche Neigung, und dem Tschandalamädchen wird eröffnet, daß es in einem früheren Leben ein Brahmanen­mädchen war und die Liebe eines Tschandalajünglings aus­geschlagen hat. Sie wird dann auch Siegerin und ist ver­einigt im Geiste mit dem Ananda, dem Brahmanenjüngling.",
      "In schöner Weise drückt Richard Wagner die Idee aus, sie geht bis zu den anthroposophisch-christlichen Grundlagen von Reinkarnation und Karma. Wir werden geführt bis zu dem Punkt, wo das Mädchen in ihrem früheren Leben sich selbst das zugefügt hat, was es jetzt erlebt. Im Jahre 1856 hat er das schon ausgearbeitet.",
      "Im Jahre 1857, am Karfreitag war es, wo er in der Einsiedlerhütte,",
      "dem «Asyl auf dem grünen Hügel», saß und hinausschaute auf das Feld und sah, wie die Pflanzenwelt aus dem Erdboden herauskam. Da hatte er eine Ahnung von jenen Triebkräften, die durch die Strahlen der Sonne herauskamen aus der Erde und die durch die ganze Welt gehen, eine Ahnung von jener Triebkraft, die in jedem Wesen lebt, aber nicht so einfach bleiben kann. Wenn sie zu höheren und höheren Stufen hinaufsteigen will, muß sie durch den Tod hindurchgehen. So empfand er gerade an der sprießenden und sprossenden Pflanzenwelt, die er er­blickte, indem er hinauswendete den Blick über den Züricher See und die Villa Wesendonck, die polarische Idee, die an­dere Idee, die Idee des Todes, das, was Goethe so schön ausgedrückt hat in dem Satze, der das Gedicht «Selige Sehn­sucht» beschließt:",
      "Und so lang du das nicht hast,",
      "Dieses:    Stirb und Werde,",
      "Bist du nur ein trüber Gast",
      "Auf der dunkeln Erde.",
      "Und was er in dem Hymnus an die Natur so umschrieb:",
      "Die Natur hat den Tod erfunden, weil sie mehr Leben haben wollte, weil sie ein höheres, geistiges Leben nur aus dem Tode heraus schaffen kann.",
      "So empfand Richard Wagner am Karfreitag, wo das Symbolum des Todes vor die Menschheit und das Mensch­heitsgedächtnis hintritt. Da empfand er den Zusammen­hang zwischen Tod, Leben und Unsterblichkeit. Er lenkt sein Gefühl von dem Leben, das aus der Erde heraussprießt, zu dem Tod am Kreuze, zu dem Tode, der aber zu gleicher Zeit der Urquell ist für den Glauben der Christenheit, daß das Leben den Sieg erringen wird über den Tod, daß es das ewige Leben erringen wird. Das Leben der Ewigkeit sprießt",
      "aus diesem Tod. Die tiefe Verwandtschaft der Karfreitags-idee, der Erlösungsidee, mit der sprießenden, sprossenden Natur, das lebte in Richard Wagner, und diese Idee ist identisch mit dem, was wir als die Gralsidee schildern konn­ten, wo die keusche Pflanze mit ihrer Blüte der Sonne ent­gegenstrebt im Gegensatz zum begierdevollen Menschen. Er sah den Menschen, wie er von der Begierde durchzogen ist, und betrachtete das Ideal der Zukunft, wo der Mensch durch die Überwindung der Begierde das höhere Bewußt­sein, jene höhere befruchtende Kraft erlangt haben wird, die der Geist erzeugen wird. Und er schaute hin auf das Kreuz, wie das Blut des Erlösers geflossen ist, das auf­gefangen wurde in der Gralsschale, und die das Symbolum gebildet hat für diese Idee von der Erlösung, und sie ver­band sich ihm mit dem Werden der Natur. Diese Idee zog im Jahre 1857 durch Richard Wagners Seele, und er schrieb damals mit einigen Strichen auf, was er dann in seinem Karfreitagszauber zum Ausdruck brachte. Er schrieb hin:",
      "Aus dem Tod die werdende Pflanzenwelt und im Tod dem Christen das unsterbliche Leben. Da empfand er den Geist hinter allen Dingen und den Geist als Sieger über den Tod.",
      "Es mußte zwar zunächst hinter den anderen künstleri­schen Ideen seiner Seele diese Idee des Parsifal zurücktreten, aber sie kam doch noch heraus am Ende seines Lebens, wo sie ihm immer klarer wurde als Bild des Erkenntnispfades des Menschen. Das hat ihn veranlaßt, den Weg zum heiligen Gral darzustellen, um zu zeigen, wie bewirkt werden kann, daß des Menschen Begierdennatur geläutert wird. Dieses Idealist dargestellt in der heiligen reinen Schale, die dar­stellt den Pflanzenkelch, der vom Sonnenstrahl, der heiligen Liebeslanze, zu reinem und keuschem neuen Schaffen be­fruchtet wird. Es sticht der Sonnenstrahl hinein in das Stoff­liche wie die Lanze des Amfortas in das sündige Blut. Da",
      "aber bewirkt sie Leid und den Tod. Reinigt sich dieses sün­dige Blut, so daß es so rein ist wie der Pflanzenblütenkelch auf einer höheren Stufe, ohne Begierde, keusch wie der Pflanzenkelch dem Sonnenstrahl gegenüber, so erscheint das wie der Weg zum heiligen Gral. Der Weg dahin kann nur gefunden werden von dem, der mit reinem Herzen, ohne berührt zu sein von dem, was die Welt gibt, ohne weltliches Wissen, als reiner Tor dahin geht und in dem die Frage nach dem Weltgeheimnis lebt.",
      "So sehen wir, wie in Richard Wagner aus mystischer Grundlage heraus die Parsifalidee aus der heiligen Grals­idee geboren wird. Er hat sie einmal darstellen wollen, in­dem er die ganze mittelalterliche Geschichte in einer Art geschichtlichen Betrachtung in seinem Werk «Die Wibe-lungen » darzustellen beabsichtigte. Es sollte sich die mittel­alterliche Kaiseridee vergeistigen dadurch, daß er Barba­rossa nach dem Orient ziehen lassen wollte, und mit dem äußeren Reich wollte er dann alles Indische, wo der Held das ursprünglich Geistige des Christentums aufsuchen wollte, hineinströmen lassen. So ergießt sich dann für ihn die Idee der mittelalterlichen Kaisergeschichten in der Par­sifalsage, und so konnte er dann in der Parsifalidee die Karfreitagstradition der Christenheit in solch wunderbarer Weise künstlerisch zum Ausdruck bringen, daß ich sagen darf, Richard Wagner hat vollbracht, was ihm als Ideal vorschwebte: die Kunst religiös zu machen. In dieser künstlerischen Neugestaltung der Karfreitagstradition hat Richard Wagner jene schöne geniale Idee zum Ausdruck gebracht von dem Zusammenwirken des Glaubens- und Gralsmotives, jene Idee, daß die Menschheit erlöst werden wird, daß sie, sich vervollkommnend, hinstreben wird zur Erlösung, daß in dem, was die Menschheit als Geist durch­strömt, von dem jede Seele einen Tropfen hat als höheres",
      "Selbst, daß das in dem Christus Jesus als Erlösung der Menschheit voranleuchtet.",
      "Das stand an jenem Karfreitag 1857 schon vor der Seele Richard Wagners und hat ihm eingegeben die Verbindung der Parsifalidee mit der Erlösung durch den Christus Jesus, der die geistige Atmosphäre, in der die Menschheit lebt, durchströmt, und den wir fühlen können, wenn wir ver­ständnisvoll erfühlen die Erzählung vom heiligen Gral. Das kann wieder zu einem konkreten geistig-seelischen Leben erwachen, wenn man in der Karfreitagsidee wieder herausfühlt den Übergang von der Mitternacht von Grün-donnerstag, von der weichenden Gründonnerstagwelt, zum Karfreitag, dem Symbolum des Sieges der auferstehenden Natur.",
      "Daß die Feste wieder lebendig werden, das war auch etwas, was in Richard Wagner lebte, als er aus einer un­mittelbaren Festesidee sein Kunstwerk herausgeboren hat. Die Feste sind herausgeboren aus einem lebendigen Ver­ständnis der Natur. Das Osterfest ist festgesetzt worden in einer Zeit, in der man wußte, daß die Konstellationen von Sonne und Mond hereinwirken aus der Natur in den Men­schensinn. In dem Osterfest kommt es konkret zum Aus­druck. Die heutigen Menschen wollen es abstrakt festsetzen, so daß man es nicht mehr so erlebt, wie wenn man familiär vertraut ist mit der Natur. Wenn man geistig empfindet, so empfindet man alles, was um uns ist, geistig. Wenn wir noch spüren, was die Tradition uns überliefert hat an Festen, dann werden wir da auch spüren etwas, wie es uns der Kar­freitag geben soll. Das spürte Richard Wagner und er fühlte auch, was das Erlöserwort «Ich bin bei euch bis ans Ende der Welt» bedeuten soll: Folgt den Spuren, die euch führen können zu dem hohen Ideal des heiligen Grals. Dann wer­den die Menschen, die in der Wahrheit leben, selbst Erlöser.",
      "Ein Erlöser hat die Menschheit erlöst. Richard Wagner fügt aber noch das andere Wort hinzu: Wann ist der Erlöser erlöst? Er ist erlöst, wenn er in jedem Menschenherzen wohnt. So wie er in jedes Menschenherz heruntergestiegen ist, so muß jedes Menschenherz hinaufsteigen. Und auch davon fühlte Richard Wagner etwas, als er aus dem Glau­bensmotiv heraus das mystische Fühlen der Menschheit in das schöne Wort im Parsifal ausklingen ließ:",
      "«Höchsten Heiles Wunder:",
      "Erlösung dem Erlöser!»,",
      "dieses Wort, das ihn so recht verschwistert und vermählt zeigt mit dem höchsten Ideale, das sich der Mensch setzen kann: sich zu nähern derjenigen Macht, die in der Welt lebt und zu uns herunter will. Wenn wir ihrer würdig werden wollen, dann bringen wir, was aus Richard Wagners Parsi­fal am Schlusse heraustönt: Erlösung dem Erlöser."
    ],
    "sentences": [
      [
        "Gegen eine Betrachtung, wie die heutige eine ist, die Richard Wagner und die Mystik in einen Zusammenhang bringen wird, erheben sich wohl leicht von vorneherein gewisse Vorurteile, welche aus Mißverständnissen gewonnen sein können, die einer solchen Betrachtung eines Künstlers von einem gewissen geisteswissenschaftlichen Standpunkte aus überhaupt entgegengebracht werden können.",
        "Und eine zweite Art von Vorurteilen sind diejenigen, die der Mystik als solcher entgegengebracht werden."
      ],
      [
        "Alles dasjenige, was heute zu sagen sein wird über Richard Wagners Stellung in der Kunst auf der einen Seite und in der Mystik auf der anderen Seite, kann den Wider­spruch hervorrufen: Ja, da wird eine ganze Menge in Richard Wagner hineingetragen, wovon er selbst nie etwas ausgesprochen hat, worüber er selbst nichts irgendwie hat verlauten lassen. - Gegen ein solches Vorurteil muß gesagt werden, daß derjenige, der eine solche Betrachtung anstellt, wie die heutige sein wird, sich selbstverständlich einen sol­chen Einwand von vornherein machen würde.",
        "Aber es ist gar nicht die Absicht, wenn wir eine geistige Erscheinung in der Welt betrachten, nur dasjenige zu sagen, was die ent­sprechende Persönlichkeit selbst gesagt hat.",
        "Das würde, wenn es nur konsequent durchgedacht wird, überhaupt un­möglich machen, wahrhaft höhere Betrachtungen gegenüber den Erscheinungen der Welt anzustellen."
      ],
      [
        "Denken Sie einmal, wenn der Botaniker - wir könnten"
      ],
      [
        "auch sagen der Lyriker - über eine Pflanze, über eine Natur­erscheinung dasjenige ausspricht, was er, also der Botani­ker, über diese Naturerscheinung zu denken vermag, oder wenn der Lyriker ausspricht, was er zu fühlen vermag gegenüber einer Pflanze oder einer Naturerscheinung, würde da irgend jemand verlangen, daß die Pflanze oder die Na­turerscheinung selbst das zu sagen vermöchte, was dem Botaniker oder dem Lyriker aus der Seele herausströmt?",
        "Nicht darum kann es sich handeln, daß dasjenige, was wir über eine geistige oder eine andere Erscheinung der Welt zu sagen haben, von dieser Erscheinung selbst gesagt wird.",
        "Da müßten Sie auch verlangen, daß die Pflanze selbst dem Botaniker die Gesetze ihres Wachstums auszudrücken ver­mag, da müßten Sie es als ein Unrecht ansehen, daß der Lyriker einer Naturerscheinung gegenüber von Gefühlen spricht, die diese Naturerscheinung nicht selbst auszudrücken vermag.",
        "Vielmehr müssen wir sagen, daß gerade in der menschlichen Seele sich dasjenige ankündigen muß, was die Außenwelt nicht über sich selbst zu sagen vermag."
      ],
      [
        "In solcher Art, bitte, nehmen Sie alles dasjenige, was Ihnen heute über eine solche geistige Erscheinung wie Richard Wagner gesagt werden soll.",
        "So wahr es ist, daß die Pflanze die Gesetze ihres Wachstums nicht selbst weiß, aber danach wächst, sich danach gestaltet, so wahr ist es, daß ein Künstler nicht selber zu sagen braucht, was ein geisteswissenschaftlicher Betrachter als die Gesetze seines Werdens und die Gesetze seiner ganzen Wesenheit aussagen muß.",
        "Aber ebenso wahr ist es, daß der Künstler diese Gesetze darlebt, danach schafft, wie die Pflanze nach den Gesetzen schafft, die man hinterher findet, wie sie die Gesetze, die ihr eingeprägt sind, darlebt.",
        "Daher darf es kein Einwand sein, daß Richard Wagner diese Dinge nicht selbst gesagt hat, die heute vorgebracht werden.",
        "Das andere bezieht sich"
      ],
      [
        "auf das, was man als die Mystik kennt.",
        "Gelehrte und Un­gelehrte sprechen von der Mystik so, als wäre sie eine dunkle, nebulose Betrachtung der Welt, gegenüber dem, was man die eigentliche wissenschaftliche, begriffliche Be­trachtung der Welt nennt.",
        "Die Gnostiker, die großen Mysti­ker der ersten christlichen Jahrhunderte, haben anders über die Mystik gedacht.",
        "Und diejenigen, welche überhaupt etwas von der Mystik verstehen, denken zu allen Zeiten anders über die Mystik.",
        "Die Gnostiker haben die Mystik «mathesis» genannt, Mathematik, nicht weil die Mystik Mathematik wäre, sondern aus dem Grunde, weil der wahre Mystiker in bezug auf seine Ideen und Vorstel­lungen von den höheren geistigen Welten dieselbe kristall­klare, durchsichtige Helligkeit anstrebt, welche auf gewis­sen anderen Gebieten die mathematischen Vorstellungen und Begriffe haben.",
        "Die Mystik ist, wenn sie in Wahrheit erfaßt wird, nicht ein dunkles, gefühlsmäßiges Erfassen der Welt, sondern das Klarste, Kristallklarste, was es überhaupt geben kann.",
        "Von diesen zwei Gesichtspunkten, die durch die Zurückweisung zweier Vorurteile hier dargelegt worden sind, wollen wir ausgehen."
      ],
      [
        "Man kann Richard Wagner wirklich vom höchsten gei­steswissenschaftlichen Standpunkt aus betrachten.",
        "Denn wenn es bei irgendeinem der Geistsucher im letzten Jahr­hundert der Fall war, daß er sich sein ganzes Leben hin­durch in der ehrlichsten, redlichsten Weise bemüht hat, die Quellen und Grundlagen der Weltenrätsel zu finden, bei ihm war es der Fall.",
        "Er nennt sein Haus in Bayreuth «Wahnfried», indem er damit selbst angibt den Grund da­für, daß dort «sein Wähnen Ruhe fand».",
        "Mit diesem Wort, daß da sein Wähnen Ruhe fand, ist viel, recht viel gesagt."
      ],
      [
        "Derjenige, der ehrlich und redlich den Pfad der Erkennt­nis zu gehen versucht, und der, gleichgültig ob in dieser"
      ],
      [
        "oder jener Form, in künstlerischer oder in anderer Form die Gebiete des geistigen Lebens, die er auf dem Erkennt­nispfade gefunden zu haben glaubt, ausprägt, derjenige, der so redlich den Erkenntnispfad geht, der weiß, was das Wort Wähnen heißt, wieviel Wahngebilde auf dem Er­kenntnispfad sich ihm in den Weg stellen, und er weiß, daß das Erkennen nicht etwas ist, was sich in einer nüchternen, trockenen Weise abspielt.",
        "Er weiß, daß das Erkennen in Wahrheit etwas ist, was sich unter Katastrophen des inneren seelischen Lebens, unter Aufsteigen und Abfallen in bezug auf das menschliche Innere abspielt, er weiß, daß es da furchtbare Gefahren auf der einen Seite und Seligkeiten, wunderbare Seligkeiten auf der anderen Seite gibt.",
        "Und er weiß, daß eines demjenigen in Aussicht steht, der diesen Erkenntnispfad geht: die Ruhe, die göttliche Ruhe, die aus einem intimen Sich-Einleben in die göttlichen Weltengeheimnisse hervorgeht.",
        "Etwas von solcher Gesinnung, etwas von solcher Stimmung drückt sich bei Richard Wag­ner in dem Wort aus: «Weil hier mein Wähnen Ruhe fand, Wahnfried sei dieses Haus genannt.»"
      ],
      [
        "Er war nicht ein Künstler wie so viele andere, die aus einer wesenlosen Phantasie heraus schaffen wollen.",
        "Er war ein Künstler, der von allem Anfang an seinen Beruf als große weltgeschichtliche Mission auffaßte, dem im künst­lerischen Schaffen Schönheit zu gleicher Zeit Wahrheit, Ausleben der Erkenntnis sein sollte.",
        "Religiöses Fühlen und Empfinden war ihm zugleich die Seele des künstlerischen Schaffens, und die Kunst war ihm etwas Heiliges.",
        "Für ihn hatte der Künstler eine Art priesterlichen Beruf, und das, was Richard Wagner als Künstler der Menschheit schenkte, sollte in seinem Sinne eine religiöse Weihe haben, eine reli­giöse Aufgabe und Mission im Entwicklungsgang der Menschheit erfüllen.",
        "So empfand er sich selbst als einen"
      ],
      [
        "derjenigen, die ihrem Zeitalter aus der Tiefe und Fülle der Wahrheit heraus etwas geben wollen."
      ],
      [
        "Wenn die Geisteswissenschaft nicht eine abgezogene graue Theorie, nicht ein Schweben in einem weltfremden Wolken­kuckucksheim sein soll, dann muß sie den Weg finden, um eine so bedeutsame geistige Erscheinung wie Richard Wag­ner von ihrem Gesichtspunkte aus zu verstehen und zu würdigen.",
        "Das kann sie, wenn sie in der richtigen Art ver­standen wird."
      ],
      [
        "Richard Wagner hat in sich das Gefühl, die Empfindung gehabt, die ihn hinleiteten zu denselben Wahrheiten von den Ursprüngen der Menschheitsentwicklung, zu denen uns auch die Geisteswissenschaft weist.",
        "Etwas verbindet Richard Wagner tief mit dem geisteswissenschaftlichen Füh­len und Empfinden, mit aller wahren Mystik: das, was er bei sich den Zusammenklang der verschiedenen Künste, die Einheit der Künste, das liebevolle, harmonische Zusam­menklingen der Künste nennt.",
        "Das, was er als einen Mangel unseres künstlerischen Wirkens der Gegenwart empfand, war dasjenige, was er die Selbstsucht, den Egoismus der einzelnen Künste nannte.",
        "Er empfand ein Ideal über ihm schwebend, welches sich ihm so darstellte, daß nicht die eine Kunst den einen Weg und die andere ihren anderen Weg geht, sondern daß eine Harmonie der Künste sich herausgestaltet, zu der alle zusammenwirken können in selbstloser Weise und liebevoller Hingabe.",
        "Er sagt, eine solche Kunst oder ein solches künstlerisches Ideal hat es im Laufe der Weltenentwicklung einmal gegeben.",
        "Namentlich suchte er ein solches Ideal im alten Griechentum, das voran­gegangen war der künstlerischen Epoche des Sophokles, Euripides und anderen.",
        "Er sagt, bevor die Künste sich ge­spalten haben, bevor das dramatische Kunstwerk für sich, der Tanz für sich war, haben sie zusammengewirkt, sind in"
      ],
      [
        "selbstlosem Streben vereinigt gewesen in dem Gesamtkunst­werk.",
        "Dieses Gesamtkunstwerk ahnt er in einer Art hell­sichtiger Schau.",
        "Die Historie erwähnt nichts davon, aber sie muß ihm recht geben, denn sie geht zu dem Urstand der verschiedenen Völker zurück, wo nicht nur die Künste zu­sammengewirkt haben zu einer einheitlichen großen Har­monie, sondern wo zusammengewirkt haben die verschie­denen Geistes- und Kulturströmungen überhaupt."
      ],
      [
        "Das, was wir heute Kunst und Wissenschaft nennen, sieht die Geisteswissenschaft als verschiedene Zweige an, die aus einer einzigen Wurzel herausgewachsen sind.",
        "Ob wir in die alte Griechenzeit zurückgehen, ob in die alte ägyptische Zeit, ob zu den indischen und persischen Völkern, ob wir in unsere germanische Heimat selbst zurückgehen: überall treffen wir auf eine Urkultur, die unsere materialistische Forschung nicht, aber die hellseherische Schau erreichen kann.",
        "Wir treffen auf eine Kultur, wo es eine gesonderte Wissenschaft und Kunst nicht gab, wo alles vereinigt war, wo alles so war, daß man geneigt war, es Mysterium zu nennen.",
        "Bevor es Kunststätten, bevor es wissenschaftliche Stätten gab, gab es Mysterienstätten.",
        "Was waren sie?",
        "Sie waren eine Vereinigung von Weisheit, Schönheit und reli­giöser Frömmigkeit."
      ],
      [
        "Wir können uns eine Vorstellung machen, was in jenen Tempelstätten, die zu gleicher Zeit Schulen und zu gleicher Zeit die wahren künstlerischen Stätten waren, vorging, wenn wir uns vor die Seele malen das große Weltendrama, von dem, wie gesagt, die materialistische Geschichte nichts zu melden hat, das sich aber abgespielt hat vor den zu den alten Weihestätten, den Mysterien Zugelassenen.",
        "Der, wel­cher da zugelassen wurde, sah in dramatischer Darstellung alles, was man aufbringen konnte an dramatischer Re­präsentation, an musikalischer Leistung, durchtränkt von"
      ],
      [
        "dem, was man glaubte, an Weisheit ergriffen zu haben, und durchtränkt von dem, zu dem die Seele in wahrhaft reli­giöser Frömmigkeit aufschaute.",
        "In wenigen Worten können wir vor die Seele hinmalen, wie es ausgeschaut hat in jener Zeit, aus der uns keine Urkunden als die der Geisteswissen­schaft etwas melden.",
        "Da wurden die, welche zugelassen wurden, vereinigt, um eine Art Weltschöpfungsdrama an­zuschauen.",
        "Solche Weltschöpfungsdramen hat es überall gegeben.",
        "Da wurde gezeigt, wie göttliche Urwesenheiten aus geistigen Höhen sich herunterbewegten, wie sie ihr Wesen einströmen ließen in den Weltenstoff und wie sich der Weltenstoff formte zu den verschiedenen Naturwesen, zu den verschiedenen Naturreichen, das mineralische Reich, das Pflanzenreich, das tierische Reich und das Menschenreich, wie also das Göttliche hineinströmte in dasjenige, was draußen in den verschiedenen Naturwesen uns entgegenleuchtet und entgegenblickt, wie dann dieses Göttliche eine Art von Auferstehung in den menschlichen Seelen feiert."
      ],
      [
        "Dasjenige, was tiefere Persönlichkeiten immer empfun­den haben, daß die Welt von einem Göttlichen ausgeströmt ist, daß dieses Göttliche in den Menschenseelen zu einem Bewußtsein kommt, gleichsam aus den menschlichen Augen und Sinnen herausschaut und sich selbst in seinem Schaffen betrachtet, dieser Abstieg und diese Auferstehung des Gött­lichen wurde in Ägypten in dem Osiris-Drama und in den verschiedensten Weihestätten Griechenlands begangen.",
        "Der­jenige, der da zuschauen durfte und sah, wie alles, was an Kunst und Weisheit da war, dazu diente, um dieses Welten­schöpfungsdrama darzustellen, der empfand gegenüber die­sem Drama, das man Urdrama nennen könnte, zunächst eine religiöse Stimmung.",
        "Verehrungs- und ehrfurchtsvoll sah er den Gott, der herunterstieg in die Materie, in allen Wesen schlummern und in der Menschenseele auferstehen."
      ],
      [
        "Ehrfurchtsvoll genoß er jene Stimmung, die Goethe einmal schön und bedeutungsvoll ausgedrückt hat in den Worten:"
      ],
      [
        "«Wenn die gesunde Natur des Menschen als ein Ganzes wirkt, wenn er sich in der Welt als in einem großen, schö­nen, würdigen und werten Ganzen fühlt, wenn das har­monische Behagen ihm ein reines, freies Entzücken gewährt, dann würde das Weltall, wenn es sich selbst empfinden könnte, als an sein Ziel gelangt, aufjauchzen und den Gipfel des eigenen Wesens und Werdens bewundern.» Und eine wunderbare religiöse Stimmung ergoß sich in die Herzen der Zuschauer dieses Weltendramas."
      ],
      [
        "Aber nicht bloß religiöse Stimmung war es, die vorhanden war, auch Weisheit war es, dasjenige, was später der Mensch in Form von wissenschaftlichen Begriffen, in Form von Ideen und Vorstellungen sich klarmachte über die Weltentstehung und ihre Wesenheiten.",
        "Das sah man hier vor Augen: Weis­heit, die geschaut wurde im äußeren Bilde, und Wissen­schaft, die zugleich Religion war.",
        "Da man alles das, was man an Schönheit aufbringen konnte, äußerlich in Bildern ausdrücken konnte, und da die Weisheit zur Frömmigkeit stimmte, so war dieses Weltendrama Wissenschaft und Kunst zu gleicher Zeit."
      ],
      [
        "Daß es so eine ursprüngliche Harmonie gegeben hat, lebte als dunkle Ahnung in der Seele Richard Wagners.",
        "Er sah freilich zunächst auf jene Urkultur im alten Griechen­land, die noch religiösen Charakter hatte, und er sagte sich, da wirkte noch nicht Musik, noch nicht Drama, noch nicht Tanz und Architektur für sich, sondern im grauesten Alter­tum wirkten alle zusammen: Religion, Kunst und Weisheit überhaupt.",
        "Und dann, so sagte sich Richard Wagner, sind die Künste herausgetreten aus ihrer Selbstlosigkeit, da wur­den sie selbstsüchtig und egoistisch.",
        "Nun hatte Richard Wagner eine große ahnungsvolle Intuition.",
        "Er schaute"
      ],
      [
        "zurück in die Zeiten urferner Vergangenheit, wo die Men­schen noch nicht so individuell waren wie heute, noch nicht so persönlich wie später, als sich die einzelnen Menschen noch als Glieder ihres Stammes, ihres ganzen Volkes fühl­ten, wo man noch dasjenige als Realität ansah, was man Volksgeist, Stammesgeist nannte.",
        "In jene alten Zeiten einer natürlichen Selbstlosigkeit sah Richard Wagner zurück, und ihm ging die Idee auf: Um ein Selbst zu sein, mußten die Menschen jene alten Stammesgemeinschaften verlassen, das persönliche Element mußte hervortreten.",
        "Nur auf Grund des persönlichen Elementes konnten die Menschen ihre Frei­heit gewinnen.",
        "Diese ist aber nicht zu gewinnen ohne eine Art von Egoismus.",
        "So sah Richard Wagner zurück in alles das, was die Menschen zusammengehalten hat.",
        "Die Men­schen mußten diese Selbstlosigkeit verlassen, bewußter und bewußter mußten sie werden.",
        "So stellte sich ihm die urferne Vergangenheit dar.",
        "Und dann sagte er sich: Nachdem sie die Freiheit errungen haben, müssen sie den Weg wieder zurückfinden zu Bruderbünden, zu liebevollen Verbänden, und aus der Bewußtheit heraus muß der selbstsüchtige Mensch wieder selbstlos werden.",
        "Die Liebe muß wieder alle durchdringen."
      ],
      [
        "Das erscheint ihm als Ideal einer fernen Kunst, und so verbindet sich bei ihm die Gegenwart mit der Zukunft, und die Kunst ist es, der er eine wichtige Stellung in bezug auf die Entwicklung anweist.",
        "Die Kunst scheint ihm parallel­gehend mit der Menschheitsentwicklung zu sein.",
        "Wie die Menschheit, so haben sich die Künste entwickelt.",
        "Aus einer Gesamtheit der Künste hervorgehend, wurden die Künste egoistisch.",
        "Das Drama, die Architektur und der Tanz wur­den etwas für sich.",
        "So ist es geworden in der Gegenwart.",
        "Parallel der egoistisch gewordenen Welt haben wir die egoistisch gewordene Kunst.",
        "Er blickt hin auf eine Zeit, wo"
      ],
      [
        "auch die Kunst wieder eine Kunstgemeinschaft haben wird.",
        "Daher nennt man Richard Wagner den «Kommunisten» der Künstler, weil er einen «Kommunismus» der Künstler so vor Augen hatte.",
        "So sieht er im Zusammenklang der Künste, zu dem er sein Scherflein beitragen will, einen mächtigen Hebel, um aus der Selbstlosigkeit der Kunst heraus etwas in die Seelen der Menschen zu gießen von jener Selbstlosigkeit, die einen zukünftigen menschlichen Bruderbund begründen muß.",
        "So war er künstlerisch ein Missionar menschlicher sozialer Selbstlosigkeit, indem er in jede Menschenseele jenen Impuls gießen wollte, der die Seele hinleitet zur inneren Selbstlosigkeit, die die Menschen in Harmonie verbindet.",
        "Wahrhaftig, ein großer Missions­gedanke, der vor Richard Wagners Seele auftauchte, ein Missionsgedanke, den nur eine Persönlichkeit haben konnte, ganz durchdringen konnte, die in sich selber etwas von dem wirklichen geistigen Impuls, die einen tiefen Glauben an die Wahrheit des geistigen Lebens hatte.",
        "Diesen tiefen Glau­ben aber hatte Richard Wagner."
      ],
      [
        "Wir können uns an einem seiner Werke, zunächst vor­bereitend, diesen Glauben Richard Wagners an die geistige Welt hinter der sinnlichen vor die Seele halten, an seinem «Fliegenden Holländer».",
        "Schon da tritt uns Richard Wag­ners richtiger und wahrhaft redlicher Glaube an die geistige Welt hinter der sinnlichen entgegen.",
        "Halten Sie sich vor Augen, daß ich nicht im entferntesten behaupte, daß die Gedanken, die hier ausgesprochen werden, bewußt vor der Seele Richard Wagners standen, ebensowenig wie die Ge­danken der Botaniker oder Lyriker bewußt in der Pflanze leben.",
        "Aber wie der Botaniker oder Lyriker an ihr emp­findet, so lebte Richard Wagner im Sinne dieser Vorstel­lung und im Sinne dieser geistigen Gesetze."
      ],
      [
        "Der materialistische Mensch sieht die Menschen um sich"
      ],
      [
        "herum an und er sieht sie in sinnlicher Abgeschlossenheit im materiellen Dasein nebeneinanderstehen.",
        "Die Seele ist ein­geschlossen in sinnliche Leiber, und so glaubt der Materia­list, daß es keine andere Art von Gemeinschaft gäbe zwischen Mensch und Mensch als diejenige, die äußerlich, sinnlich vermittelt wird."
      ],
      [
        "Was der einzelne Mensch dem anderen sagen kann, was der einzelne dem anderen tun kann, ist rein äußerlich, materiell wirklich; daran glaubt der materia­listische Denker.",
        "Daß es eine verborgene Gemeinschaft der Menschen gibt, daß es etwas gibt, was von Seele zu Seele wirkt, auch wenn kein äußerliches Wirken durch sprach­liche oder materielle Mittel da ist, davon ist derjenige überzeugt, der etwas weiß von der geistigen Welt hinter der sinnlichen Welt."
      ],
      [
        "Geheime geistige Wirkungen gehen und strömen von Seele zu Seele.",
        "Dasjenige, was einer denkt und fühlt, auch wenn es innerhalb der Seele beschlossen bleibt, ist nicht bedeutungs- und wertlos für den anderen Menschen, auf den sich die Gedanken und Gefühle be­ziehen."
      ],
      [
        "Der materialistische Denker weiß bloß davon, daß der andere Mensch mit der Hand berührt werden kann, daß man ihm mit materiellen Mitteln beistehen kann.",
        "Er glaubt nicht, daß das Gefühl, das in ihm lebt, eine reale Bedeutung für die anderen Menschen hat, daß Seele und Seele durch Bande verknüpft ist, die man nicht mit sinn­lichen Augen sehen kann."
      ],
      [
        "Der Mystiker weiß, daß ein sol­ches Band von Seele zu Seele sich schlingt.",
        "Richard Wagner war tief durchdrungen davon, daß das der Fall ist."
      ],
      [
        "Wenn wir uns klarmachen wollen, was damit angedeutet ist, dann blicken wir zurück auf eine schöne mittelalterliche Sage, die der heutige Mensch nur als Sage empfindet, die aber für denjenigen, der sie geschrieben hat, und für den, der sie mystisch zu verstehen weiß, etwas anderes ist als eine Sage, nämlich der Ausdruck einer geistigen Wirklichkeit."
      ],
      [
        "Da erinnert uns eine Sage, die uns ein mittelalterliches Epos überliefert hat, an den armen Heinrich, der eine furcht­bare Krankheit hatte.",
        "Da hören wir, daß nur eines den armen Heinrich von seiner furchtbaren Krankheit heilen kann, nämlich wenn sich ein reines weibliches Wesen für ihn opfert."
      ],
      [
        "Die Liebe der reinen weiblichen Seele ist im­stande, etwas zu bedeuten, etwas Reales zu sein für das andere Menschenleben.",
        "Daß Seele für Seele im rein geistigen Reiche etwas füreinander sein können, wovon sich das mate­rialistische Denken keine Vorstellung macht, das liegt hinter einer solchen Sage."
      ],
      [
        "Die Opferung des reinen weiblichen Wesens für den armen Heinrich, ist sie denn schließlich etwas anderes als ein sinnlicher Ausdruck für dasjenige, was ein großer Teil der Menschheit überhaupt als die mysti­sche Wirkung des Opfers ansieht?",
        "Ist denn das Opfer dieser Jungfrau für den armen Heinrich nicht dasjenige, was der Erlöser am Kreuze für die Menschheit dargebracht hat, ist es nicht jene mystische geistige Wirkung von Seele zu Seele?"
      ],
      [
        "Daß hinter dem Äußeren etwas leben kann, das sehen wir da, da glaubt das Bewußtsein ahnungsvoll, daß es eine solche Geistigkeit gibt.",
        "Deshalb kam Wagner zu der Sage vom Fliegenden Holländer, jenem Mann, der sich mit dem Materiellen verbunden hatte und keine Erlösung finden kann von dem Stoff, mit dem er verstrickt ist."
      ],
      [
        "Nicht mit Unrecht hat man den Fliegenden Holländer den Ahasver des Meeres, den Ewigen Juden des Meeres genannt.",
        "Wie in der Idee des Ewigen Juden etwas Tiefes liegt, so in der Idee vom Ewigen Juden des Meeres, vom Fliegenden Holländer."
      ],
      [
        "Betrachten wir uns den Ahasver von diesem Gesichts­punkte aus.",
        "Er ist der Mensch, der nicht glauben kann an den Erlöser, an eine Persönlichkeit, die die Menschheit vor­wärtsführt zu größeren Höhen, zu immer vollkommeneren und vollkommeneren Stufen der Entwicklung.",
        "Der Ahasver"
      ],
      [
        "ist verstrickt in das bleibende Dasein; während der Mensch in Wahrheit, wenn er weiterkommen will, aufwärtssteigen muß von Stufe zu Stufe, kann sich der, welcher nicht stre­ben will, mit der Materie verbinden.",
        "Er kann demjenigen Hohn sprechen, der Führer der Menschheit zu höheren und höheren Stufen ist."
      ],
      [
        "Dann muß er in die Materie verstrickt werden.",
        "Was heißt es: In die Materie verstrickt werden?",
        "Wer in die Materie verstrickt wird, für den wiederholt sich das äußere Leben im ewigen Einerlei.",
        "Denn dadurch unter­scheidet sich das materielle vom geistigen Auffassen, daß das Materielle sich immer wiederholt, während der Geist aufsteigt."
      ],
      [
        "In dem Augenblicke, wo der Geist der Materie verfällt, verfällt er der Wiederholung des immer Gleichen.",
        "Und so ist es mit dem Fliegenden Holländer.",
        "In jenen alten Zeiten hatten die verschiedenen Völker das Bekanntwerden mit fremden Ländern benützen können, um die Ideen im­mer höher und höher zu heben."
      ],
      [
        "Wer dieses erreichen konnte, der betrachtete das Fahren über das Meer, das Hinausstür­men zu fremden Küsten als ein bloßes Mittel der Vervoll­kommnung der Menschheit.",
        "Derjenige, der die Vollkom­menheitsidee, das Fließen der Geistesströmung nicht spürte, verstrickte sich in das Einerlei des bloß zur Materie, zum Stofflichen Gehörigen."
      ],
      [
        "Der Fliegende Holländer, der seinen Hang nur zum Stofflichen hat, wird verlassen von den Kräften der Entwicklung, von der Liebe, die das Mittel ist zur Vervollkommnung, das Mittel zum Aufstieg, zur Ent­wicklung, so daß er sich in die Materie, in die Stoffe hinein­spinnt und sich für ihn dasselbe dann in ewiger Wieder­holung wiederholen muß.",
        "Solche Wesen, die nicht ergriffen, nicht erfaßt werden können zu einem höheren Aufstieg, müssen berührt werden von jungfräulichem Wesen."
      ],
      [
        "Jung­fräulich und von reiner Liebe erfüllt muß das Wesen sein, das den Fliegenden Holländer erlösen kann."
      ],
      [
        "Die Seele, die noch nicht in den Stoff verstrickt ist, hat eine Beziehung zu der Seele, die in den Stoff verstrickt ist.",
        "Das ahnt Richard Wagner und das drückt er in seinem Drama in so bedeutungsvoller Weise aus."
      ],
      [
        "Das war ein mystisches Empfinden der Wahrheit, das war die Empfin­dung der Gemeinschaft der Geister, die hinter der Gemein­schaft des Stoffes ist.",
        "Wahrhaftig, ein solcher, der so fühlte, durfte sich eine so hohe geistige Mission zuschreiben, wie Richard Wagner sie sich zuschrieb, der durfte seine Ge­dankenflüge hinlenken in Gebiete, wo er über Musik und Drama ganz anders dachte, als man vor ihm gedacht hat."
      ],
      [
        "Er sah in seiner Art zurück in jene griechische Urzeit, wo es einheitliche Kunstwerke gab, wo die Musik nur zum Aus­druck brachte, was das übrige Dramatische nicht in seiner Vollständigkeit zum Ausdruck bringen konnte, wo die ewigen Weltgesetze in dem Rhythmus des Tanzes zum Ausdruck kamen.",
        "Er sah etwas in dem alten Kunstwerk, wo noch zusammenwirkten Tanz, Rhythmus und Harmo­nie im dramatisch-musikalischen Kunstwerk des urfernen Altertums."
      ],
      [
        "Es erstand vor ihm eine eigentümliche Anschau­ung über das Wesen des Musikalischen.",
        "Das eigentliche Wesen des Musikalischen sah Richard Wagner in der Har­monie der Töne.",
        "Aber er sagte sich, nur dann, wenn die Schwesterkünste dasjenige, was sie hineinzugeben haben, hergeben für die Harmonie, dann strömt von solchen Schwe­sterkünsten in die Harmonie der Musik etwas ein."
      ],
      [
        "Die eine der Künste ist der Tanz.",
        "Nicht der Tanz, der später die Menschheit ergriff, sondern der, welcher in den Formen des Tanzes Bewegungen in der Natur und Bewegungen der Sterne ausdrückt.",
        "So war der alte Tanz."
      ],
      [
        "Der alte Tanz war herausgeboren aus einem Erfühlen der Naturgesetze, durch eigene Bewegung ein Nachbild dessen, was in der Natur sich bewegte.",
        "Dieses Wesen des Tanzrhythmus strahlte"
      ],
      [
        "hinein in die musikalische Harmonie und gab der Harmonie der Musik den Rhythmus.",
        "Dann trat die andere Schwester­kunst hinzu, die Dichtung.",
        "Sie konnte nur einiges in Worten ausdrücken.",
        "Aber dasjenige, was Worte nicht ausdrücken konnten, das mußten die Schwesterkünste zum Ausdruck bringen.",
        "So wirkten Tanz, Musik, Dichtung in Harmonie und es entstand das Musikalische als Dreiklang von Har­monie, Rhythmus und Melodie.",
        "Es entstand, weil die Schwesterkünste zusammenwirkten."
      ],
      [
        "Das stand vor dem Mystiker als der Geist des alten Kunstwerks, wo noch nicht Melodie, Rhythmus und Har­monie in der späteren Vollkommenheit da waren.",
        "Das weiß Richard Wagner und das weiß auch der Mystiker.",
        "Nun sagte er sich: in späterer Zeit trennten sich die Künste, die hier schwesterlich zusammenwirkten.",
        "Der Tanz wurde etwas für sich, die Dichtung wurde etwas für sich.",
        "Dadurch wurde das rhythmische Erleben als etwas für sich hin-gestellt und ebenso auch die Musik, die nichts mehr wissen wollte von der Schwester, ebenso wie die Dichtung sich trennte von dem Musikalischen und nichts mehr hinein­strömen konnte in das Musikalische."
      ],
      [
        "Richard Wagner sah, wie mit der Zunahme der Egoismen der Menschen die Künste egoistischer wurden, und er ver­folgte so die Künste bis in die neueste Zeit hinein.",
        "Wir können ihm jetzt nicht folgen, wie er seine Künste verfolgt, wie sie selbständiger und egoistischer werden.",
        "Sehen wir, wie er selbst versuchen will, aus den Einseitigkeiten, die ihm vorliegen, etwas Harmonisches zu schaffen.",
        "Da wollen wir ihm folgen, da zeigt sich seine ganze Größe, die hinter das Wesen der Dinge auf diesem Gebiete zu kommen sucht."
      ],
      [
        "Zwei Geister standen vor Richard Wagners Seele, die die Einseitigkeit der Künste pflegten, die er zusammenbringen wollte.",
        "Die Einseitigkeit des Musikalischen und die Einseitigkeit"
      ],
      [
        "des Dramatischen zeigten Beethoven und Shake­speare.",
        "Shakespeare war für Richard Wagner der einseitige Dramatiker, weil es für Richard Wagner klar war, daß, wenn er sein tiefes Inneres betrachtete, die ganze Stufen­leiter der Empfindungen und Gefühle, die man von außen nicht sehen kann, die nicht in Gesten, nicht einmal in Worte übergehen kann, wenn es sich um Wesenhaftes handelt, daß diese Stufenleiter der Empfindungen nicht im Wortdrama zum Ausdruck kommen kann."
      ],
      [
        "Das Wortdrama stellt die Handlung dar, wenn sie schon hinausgetreten ist aus den inneren Impulsen in Raum und Zeit.",
        "Wenn das Drama sich abspielt, so müssen wir schließen, daß die Person die Im­pulse schon erlebt hat."
      ],
      [
        "Wir sehen das schon alles übergehen in das, was das Auge sehen und das Ohr hören kann und nicht mehr als das, was sich abspielt als Dramatik im Innern der Person selbst.",
        "So muß der Dramatiker sich ausschwei­gen über dasjenige, was als die tieferen Gefühle und Emp­findungen die Untergründe für dasjenige darstellen, was sich äußerlich auf der Bühne zeigt."
      ],
      [
        "Auf der anderen Seite sind ihm die einseitigen Künstler die Symphoniker, die reinen Instrumental-Musiker, diejenigen, die wirklich in ihrem wunderbaren Tongefüge dasjenige darzustellen ver­mögen, was im Inneren der Seele vorgeht, die innere Dra­matik, die aber gestenlos bleibt, die nicht nach außen in Raum und Zeit überströmt.",
        "So hat er auf der einen Seite die musikalische Kunst, den Ausdruck des menschlichen Innern, die, wenn sie nach außen will, ihr Unvermögen fühlt, und auf der anderen Seite hat er die dramatische Kunst, die mit der musikalischen Kunst sich nicht ver­schwistert, die erst darzustellen vermag, wenn die Impulse in Raum und Zeit hinausgeflossen sind."
      ],
      [
        "Shakespeare - Mo­zart, Haydn, Beethoven stellen ihm zwei Seiten dar, künst­lerisch ausgeprägt.",
        "In Beethovens Neunter Symphonie sieht"
      ],
      [
        "er etwas, was die eine einseitige Kunstform aus sich heraus durchbrechen will.",
        "Er sieht, wie in der Neunten Symphonie gleichsam die Hüllen zerspringen, wie sie gleichsam sich auslebt im Wort, weil sie in Liebe die ganze Menschheit umfassen will, weil sie hinausdrängt in die ganze Welt.",
        "Da sieht er etwas, was hinaus will in Raum und Zeit; und es noch weiter hinauszuführen in Raum und Zeit, das betrach­tet er als seine Mission.",
        "Nicht nur so, wie es in der Neunten Symphonie ist, den Ausdruck der Empfindungen, die innere Dramatik der Seele ausströmen zu lassen, nicht nur so, wie es da ist, wünscht er es, sondern er wünscht es einfließen zu lassen in Wort und Handlung, so daß man beide vor sich auf der Bühne hat, die innere Skala der Empfindungen in der Musik und in der Dramatik das - weil sie herausgeht in Raum und Zeit -, was die innere Skala der Empfin­dungen zu äußeren Handlungen bildet.",
        "Shakespeare und Beethoven in einer höheren Einheit - das will er sein.",
        "Den ganzen Menschen will er darstellen."
      ],
      [
        "Sehen wir eine Handlung auf der Bühne, dann sollen wir nicht bloß sehen, was sich vor Augen und Ohren abspielt, sondern wir wollen auch hören, was die innersten Impulse des menschlichen Wesens sind.",
        "Deshalb genügt Richard Wagner auch die alte Oper nicht.",
        "Denn da waren Dichter und Musiker jeder für sich.",
        "Der Dichter drückte aus, was er auszudrücken hatte, der Musiker kam hinzu, um die Dich­tung auszudrücken.",
        "Die Musik aber soll dazu da sein, um auszudrücken, was die Dichtung nicht ausdrücken kann.",
        "Das menschliche Wesen besteht aus dem Inneren, das im Äußeren nicht zum Ausdruck kommen kann, und aus dem Äußeren, das zwar im Wortdrama zum Ausdruck kommen kann, aber sich ausschweigen muß über die inneren Impulse.",
        "Deshalb muß das Musikalische nicht so sein, daß es die Dichtung illustriert, sondern so, daß es die Dichtung vervollständigt."
      ],
      [
        "Die Musik muß ausdrücken, was die Dichtung nicht ausdrücken kann."
      ],
      [
        "Das ist der große Gedanke Richard Wagners.",
        "So will er schaffen, so schreibt er sich seine Mission zu für ein selbst­loses Zusammenwirken von Musik und Dichtung in einem Gesamtkunstwerk.",
        "Und so sehen wir im Grunde genommen diesen seinen Grundgedanken auf eine mystische Grund­lage zurückgehen, auf jene Grundlage, die den ganzen Menschen erfassen will, nicht den äußeren Menschen bloß, sondern den ganzen Menschen, der durchdrungen ist von dem inneren."
      ],
      [
        "Der Mensch ist mehr als das, was sich äußer­lich auslebt.",
        "Richard Wagner weiß, daß in des Menschen Inneren ein höheres Selbst ruht, ein höheres Selbst vor­handen ist.",
        "Aber nur teilweise kommt in dem, was in Raum und Zeit erscheint, das höhere Selbst zum Ausdruck."
      ],
      [
        "Aber das innere Höhere, was über das Gewöhnliche hinausgeht, will Richard Wagner erfassen.",
        "Daher genügt ihm das eine Mittel nicht, sondern er sucht, was den Menschen in ver­schiedener Weise erfassen kann."
      ],
      [
        "Er muß daher auch seine Zuflucht nehmen zu dem, was hinausgeht über die unmittel­bare Persönlichkeit, was sich erhebt zum Übermenschlichen.",
        "Das geschieht im Mythos.",
        "In der mythischen Individuali­tät tritt uns nicht der einzelne Mensch entgegen, sondern gleichsam ein Übermenschliches."
      ],
      [
        "Was der Übermensch im Menschen bedeutet, das drückt uns der Mythos aus.",
        "Was nicht in einem, sondern in vielen Menschen lebt, das drücken uns mythologische Figuren wie Siegfried und Lohengrin aus.",
        "Weil Wagner in das Tiefste der Menschen gehen wollte, brauchte er die übermenschlichen Persönlichkeiten der Mythen."
      ],
      [
        "Wie tief er hineingreift in den ganzen Werde- und Ent­wicklungsprozeß, können wir verstehen, wenn wir ihm nur ein bißchen folgen.",
        "Zu den höchsten menschlichen Rätselfragen,"
      ],
      [
        "wie sie sich aussprechen in so großartiger Weise in dem Nibelungendrama und im Parsifaldrama, erhebt er sich und sucht sie herauszugestalten aus der Anschauung, der Empfindung und dem Gefühl für die ganze Menschheit."
      ],
      [
        "Wir können nun einzelne Streiflichter auf dasjenige werfen, in dem Richard Wagners künstlerische Seele lebt.",
        "Wir werden sehen, wenn wir auch nur weniges heraus-greifen, wie tief er verbunden ist mit dem, was man die mythischen Zusammenhänge der Menschheit nennt."
      ],
      [
        "Warum greift Wagner gerade zum Siegfrieddrama?",
        "Was wollte er damit darstellen?",
        "Wir gelangen am leichtesten dazu, wenn wir anknüpfen an Richard Wagners Idee von der ganzen Menschheitsentwicklung.",
        "Er sah zurück in die Urzeiten, wo der Mensch durch enge Stammesbande der Menschheit in einer ursprünglichen, selbstlosen Liebe verknüpft war."
      ],
      [
        "Er sah zurück in jene Zeiten, wo die Menschen sich so fühlten, daß der einzelne seine Selbständigkeit in seinem dumpfen Bewußtsein noch nicht empfand, sondern sich als ein Glied in einem Stamme fühlte, zu dem er gehörte, daß er gleich­sam in der Stammesseele etwas Wirkliches, etwas Reales fühlte.",
        "Vor allen Dingen spürte Richard Wagner, wie das­jenige, was in Europa lebte, zurückführt in uralte Zeiten, wo eine ursprüngliche Liebe die Menschen noch zu brüder­lichen Gruppen und Verbänden vereinigte."
      ],
      [
        "Er blickte auch zurück in jene Zeiten, von denen die geisteswissenschaftliche Weltanschauung spricht, die sagt, daß alles in Entwicklung ist.",
        "Die geisteswissenschaftliche Anschauung sagt uns, daß auch das Bewußtsein sich nach und nach entwickelt hat."
      ],
      [
        "Das heutige klare Bewußtsein hat sich aus Zuständen entwickelt, von denen spärliche Nachklänge noch vorhanden sind.",
        "Im Traumbewußtsein, im Bildertraum sah Richard Wagner Nachklänge eines Bilderbewußtseins, das früher der ganzen Menschheit eigen war."
      ],
      [
        "Das heutige Tagesbewußtsein, das"
      ],
      [
        "vom Morgen bis zum Abend, bis zum Einschlafen dauert, hat ein viel dumpferes Bewußtsein verdrängt.",
        "In diesem alten, dumpfen Bewußtseinszustand hingen die Menschen viel tiefer zusammen.",
        "Da kam die menschliche Individuali­tät noch nicht so heraus wie später und damit auch nicht der menschliche Egoismus, der eine notwendige Stufe in der menschlichen Entwicklung bedeutet.",
        "Richard Wagner sah, daß es eine natürliche Liebe gab, die schon im Blute lag und die einzelnen Blutsverwandten zusammenknüpfte."
      ],
      [
        "Nun will ich aus der rationalen Mystik heraus eine An­schauung darlegen, die für diejenigen, welche die anderen Vorträge nicht gehört haben, etwas Groteskes haben, aber für die anderen etwas Mathematisch-Sicheres bekommen wird.",
        "Dasjenige, was heute in Europa lebt als heutiges klares Tagesbewußtsein, hat sich aus einer uralten Mensch­heit entwickelt, der atlantischen Menschheit, die der uns­rigen vorangegangen ist und da gelebt hat, wo heute die Fluten des atlantischen Ozeans sind.",
        "Diejenigen, welche achtgeben auf das, was in der Welt vorgeht, werden wissen, daß selbst die Naturwissenschaft schon von einem atlan­tischen Kontinent spricht.",
        "Auch in der naturwissenschaft­lichen Zeitschrift «Kosmos» erschien ein Artikel darüber.",
        "Da lebten die Vorfahren der Menschen, die heute Europa bewohnen, unter anderen physikalischen Bedingungen.",
        "Sie lebten noch in Luft und Wasser.",
        "Der Boden war weithin bedeckt mit großen, mächtigen Nebelmassen.",
        "Damals sah man nicht die Sonne, wie man sie heute sieht.",
        "Sie war um­geben von mächtigen Farbenhöfen, weil alles bedeckt war mit mächtigen Nebelmassen.",
        "Die germanische Sagenwelt hat das Gedächtnis an jene alten Lande in dem Ausdruck Niflheim, Nibelungenheim bewahrt.",
        "Das sind die Erinne­rungen an jenes alte Nebelland, und es ist eine feine, intime Wendung in dem, was sich aus jener Urzeit als Sage erhalten"
      ],
      [
        "hat, daß, als die Flut allmählich die atlantischen Lande überspülte, dieselbe Flut auch die Flüsse der deutschen Tief­ebene gebildet hat, so daß das Wesen des Rheins angesehen wird wie ein Überbleibsel jenes Wesens, das als das atlan­tische Nebelwesen einstmals weithin die Lande bedeckt hat.",
        "Es ist so, wie wenn das Rheinwasser abgeflossen wäre aus den Nebelmassen der alten Atlantis, des Nebelheims, des Nibelungenheims.",
        "So stellt die Sage das in dumpfem, ahnungsvollem Bewußtsein dar.",
        "Und indem die Völker ostwärts zogen, weil die physischen Verhältnisse so wurden, daß sie die Gegenden verlassen mußten, verließ sie das dumpfe Bewußtsein.",
        "Dieses wurde heller und heller, der Egoismus wurde aber auch größer."
      ],
      [
        "Das alte dumpfe Bewußtsein hatte eine gewisse Selbst-losigkeit zur Folge.",
        "Mit dem Reinigen der Luft zog der Egoismus herauf.",
        "Der Nebeldunst der alten Atlantis bildete rings um den Menschen eine Atmosphäre von Weisheit, die erfüllt war von Selbstlosigkeit, von Liebe.",
        "Das strömte in die Wasser des Rheins und ruhte da unten als Weisheit, als Gold.",
        "Wenn das aber vom Egoismus erfaßt wird, dann gibt es zu gleicher Zeit die egoistische Macht.",
        "So sahen die Re­präsentanten der alten Bewohner von Nibelungenheim, als sie ostwärts zogen, den Rhein den Hort in sich schließen, der aus dem Gold der Weisheit bestand, die einstmals in selbstloser Art gewirkt hat.",
        "Das alles ruhte - nicht so aus-gesprochen - in der Sagenwelt, deren sich Richard Wagners Seele bemächtigte.",
        "Und diese Seele war dem großen gei­stigen Wesen, das darinnen wirkte und das Gedächtnis der alten Tatsachen bewahrte, so kongenial, daß sie aus dieser Sagenwelt dasjenige herausholte, was der Extrakt seiner ganzen Weltanschauung war.",
        "So hören wir nachklingen in der Musik Richard Wagners und sehen im Drama über die Bühne schreiten das Werden und Weben des menschlichen"
      ],
      [
        "Egoismus.",
        "Das Zusammenschließen des Rings, wir sehen es in dem, daß Alberich dem Rhein, den Wellenmädchen das Gold abnimmt.",
        "In Alberich sehen wir den egoistisch gewor­denen Repräsentanten der Nibelungen.",
        "Wir sehen den Menschen, welcher der Liebe, die den Menschen in ein Gan­zes hineingestellt hat, abschwört.",
        "Die Macht des Besitzes verknüpft Richard Wagner mit der Idee, die in jener Sagen-welt webt.",
        "So sieht er jene alte Welt.",
        "Es tritt ihr entgegen diejenige Welt, die Walhalla begründet hat, es tritt entgegen die Welt des Wotan der Welt der alten Götter.",
        "Sie haben dasjenige, was alle Menschen gemeinsam hatten.",
        "Sie stellen eine Art von Gruppenseele dar, so auch Wotan.",
        "Aber da, wo die Einzelpersönlichkeit ergriffen wird von dem Ring, der sich um das Ich des Menschen spannt, wird auch er er­faßt von der Gier nach Gold.",
        "So sehen wir das, was als Volksseele in Wotan lebte, dasjenige, was der Mensch in egoistischer Art an dem Rheingold in sich erlebt, in einer feinen Art in Richard Wagners ganzer Kunst, in seinem ganzen Schaffen.",
        "Wir hören es aus den Klängen seiner Musik heraus.",
        "Wer sollte es nicht spüren können?",
        "Niemand sollte sagen, daß da in sein Werk etwas hineingelegt wird.",
        "Dagegen habe ich mich verwahrt.",
        "Aber wer sollte nicht spüren in der Es-Dur-Stelle des «Rheingold» das Ein­schlagen des Ich?",
        "Wie sollte das menschliche Ohr nicht spüren können das Auftreten des Ich in diesem langen Ton der Es-Dur-Stelle des «Rheingold»?"
      ],
      [
        "So könnten wir bis in die musikalische Kunst hinein Richard Wagners mystisches Fühlen verfolgen."
      ],
      [
        "Wir sehen dann, wie sich Wotan auseinanderzusetzen hat nicht mit dem Bewußtsein, das sich von Seele zu Seele ge­sponnen hat, sondern mit dem, was sich noch nicht heraus­gesponnen hat da, wo das Volksbewußtsein noch lebendig gespürt worden ist.",
        "Dieses Bewußtsein tritt da auf, wo"
      ],
      [
        "Wotan den Riesen den Ring entreißen will.",
        "Da tritt das alte Bewußtsein vor ihm auf in der Gestalt der Erda.",
        "Be­deutsam ist die Art, wie da gesprochen wird.",
        "Oder ist die Gestalt nicht so geschildert, daß sie die Repräsentantin des alten Bewußtseins ist, die nicht bloß weiß, was der Verstand verbindet, sondern auch weiß aus hellseherischem Bewußt­sein heraus, was in der Umwelt vorgeht?"
      ],
      [
        "Bekannt ist dir,"
      ],
      [
        "Was die Tiefe birgt,"
      ],
      [
        "Was Berg und Tal,"
      ],
      [
        "Luft und Wasser durchwebt."
      ],
      [
        "Wo Wesen sind,"
      ],
      [
        "Wehet dein Atem;"
      ],
      [
        "Wo Hirne sinnen,"
      ],
      [
        "Haftet dein Sinn:"
      ],
      [
        "Alles, sagt man,"
      ],
      [
        "Sei dir bekannt."
      ],
      [
        "Man kann nicht klarer das Bewußtsein darstellen, das in Nebelheim war, man kann das alte Bewußtsein nicht klarer kennzeichnen, als es in den Worten ausgeprägt ist:"
      ],
      [
        "Mein Schlaf ist Träumen,"
      ],
      [
        "Mein Träumen Sinnen,"
      ],
      [
        "Mein Sinnen Walten des Wissens."
      ],
      [
        "So war es: wie ein Träumen, aber ein Träumen, das wußte von der ganzen Umwelt, das wirkte von Mensch zu Mensch, das wirkte in die tiefste Tiefe der Natur hinein.",
        "Das war sein Sinnen, das war sein Wollen, sein Handeln, denn der Mensch handelte aus diesem Bewußtsein heraus.",
        "Dieses Be­wußtsein trat vor Wotan in der Erda hin.",
        "Es entstand da­durch ein neues Bewußtsein."
      ],
      [
        "In allem Mystischen wird das Höhere durch eine weib­liche Persönlichkeit dargestellt.",
        "Das ist es auch, was sich in Goethes schönen Worten im Chorus mysticus verbirgt:"
      ],
      [
        "«Das Ewig-Weibliche zieht uns hinan.» Die verschiedenen Völker haben dieses Streben der Seele zu einem höheren Bewußtsein dargestellt als eine Vereinigung mit irgend­einem Weiblichen, in dem das Höhere in der menschlichen Seele dargestellt wird.",
        "Die Seele ist dasjenige, was von den Weltgesetzen durchstrahlt wird, und diese Weltgesetze sind es, mit denen sie sich wie in einer Ehe vereinigt.",
        "So sehen Sie, wie im alten Ägypten die Isis und wie überall sonst ein höherer Bewußtseinszustand der Seele als Weibliches hin-gestellt wird, und zwar in der Weise, wie es dem Charak­ter eines Volkes entspricht.",
        "Was das Volk als sein eigent­liches Wesen empfindet, das wird ihm dargestellt in der Verbindung des Menschen mit der betreffenden weiblichen Persönlichkeit entweder im Tod oder schon während des Lebens."
      ],
      [
        "Auf zwei Arten - das haben uns die Vorträge bisher gezeigt - kann der Mensch über die Sinnlichkeit hinaus­wachsen.",
        "Einmal kann er das Sinnliche abstreifen und sich verbinden mit dem Geiste im Tode oder schon hier im Leben, wenn sein geistiges Auge geöffnet wird.",
        "Dement­sprechend sehen wir, wie dieses Höhere, das der Mensch erleben kann, auch in der deutschen Mythe als eine weib­liche Persönlichkeit dargestellt wird.",
        "Für die Vorfahren der Mitteleuropäer ist es der Kriegsmann, der tapfer kämpft und auf dem Schlachtfelde fällt, der nach dem Tode in die geistige Welt geht, um mit dem Höheren vereinigt zu wer­den, daher kommt dem Kriegsmann die Walküre entgegen, die ihn hinaufträgt in die Welt des Geistigen.",
        "Die weibliche Figur der Walküre stellt die Verbindung mit dem höheren Bewußtsein dar.",
        "Wotan zeugt mit Erda die Brünnhilde, mit"
      ],
      [
        "der sich Siegfried vereinigen soll, wenn er hingeführt wer­den soll zu dem geistigen Leben.",
        "Die Töchter der Erda stellen das höhere Bewußtsein des Eingeweihten dar.",
        "In Siegfried wächst der neue Mensch heran, der durch eine besondere Ausprägung und Vollkommenheit des Inneren schon während des Lebens die Vereinigung mit der Walküre vollziehen kann."
      ],
      [
        "Was die deutsche Sagenwelt birgt, was in ihr lebt, hat Richard Wagner zum Ausdruck gebracht.",
        "Auch das hat er zum Ausdruck gebracht, daß die alte Gruppenseele ab­sterben muß in einer Götterdämmerung, ebenso wie das individuelle Bewußtsein des Menschen in Siegfried sich ausleben muß.",
        "Das alles wirkte und lebte und webte in seiner Seele.",
        "Die höchsten Menschheitsprobleme lebten und wirk­ten in ihm, und er hat sie, insofern sie des Menschen Inneres darstellen, im Musikalischen, und insofern sie menschliche Taten darstellen, im Dramatischen dargestellt."
      ],
      [
        "So sehen wir, wie Richard Wagner als Künstler den höheren Werdegang des Menschen aus dem Mystischen her­aus schöpft.",
        "Das hat ihn auch dazu geführt, eine tief be­deutsame Gestalt zum Mittelpunkt einer solchen Dramen­schöpfung zu machen, die Gestalt des Lohengrin.",
        "Was ist der Lohengrin?",
        "Diesen Lohengrin verstehen wir nur, wenn wir sehen, wie sich die Sage im Volk einlebt während einer Zeit, wo in ganz Europa bedeutsame soziale Umwälzungen vor sich gingen.",
        "Wir verstehen, was in der Seele desjenigen lebte, der das Bild des Lohengrin in seiner Vereinigung mit dem Weibe, die bei Richard Wagner Elsa von Brabant ist, darstellt.",
        "Wir sehen, wie durch ganz Europa hindurch ein neues Zeitalter sich bildet, das Zeitalter, in dem das Ringen der menschlichen Individualität zum Ausdruck kommt.",
        "Mit etwas scheinbar ganz Prosaischem, hinter dem aber etwas ganz Tiefes steckt, können wir es ausdrücken.",
        "In Frankreich,"
      ],
      [
        "Schottland, England, hinten in Rußland, überall sehen wir ein neues soziales Gebilde entstehen: die freie Stadt.",
        "Während draußen auf dem Lande die Menschen in den Nachklängen alter Stammesgemeinschaften lebten, strömten diejenigen Menschen, welche sich der Stammes-zusammengehörigkeit entreißen wollten, aus derselben her­aus in die Stadt.",
        "Da, in der Stadt, entstand das individuelle Freiheitsbewußtsein.",
        "Da lebten die Menschen, die sich den Zusammengehörigkeitsbanden entreißen wollten, die ihr Leben da einzig und allein leben wollten.",
        "Es war ein mäch­tiger Umschwung, der sich damals vollzog.",
        "Bisher war es der Name, der angab, wozu der Mensch gehörte und was er wert war.",
        "In der Stadt war der Name nichts wert.",
        "Was bekümmerte man sich da darum, aus welcher Familie der Mensch herausgewachsen war?",
        "Da war er so viel wert als er Können hatte.",
        "Da entwickelte sich der individuelle Mensch.",
        "Die Entwicklung von der Selbstlosigkeit zur Individualität wurde zur Entwicklung von der Individualität zum Bruder-bund.",
        "Das stellte in der Mitte des Mittelalters die Sage dar, indem das Alte ersetzt wurde durch das, was der Mensch aus seinem Inneren heraus sich selbst zu geben in der Lage war."
      ],
      [
        "Sehen wir zurück auf die alten führenden Priester-geschlechter, auf diejenigen, die früher Führer waren, auf diejenigen, die die Adelsgeschlechter, die Weisen abgegeben haben: sie stammten aus Familienverbänden.",
        "Daß sie einem solchen Verbande angehörten, daß sie das richtige Blut hatten, darauf kam es an.",
        "In der Zukunft wird es darauf nicht mehr ankommen.",
        "Der, welcher ein Führer der Mensch­heit sein wird, der kann unbekannt sein durch das, was ihn mit der Menschheit verbindet, da profaniert man ihn, wenn man ihm einen Namen gibt.",
        "Daher das Ideal der großen Individualitäten, das Ideal des namenlosen Weisen, das sich"
      ],
      [
        "immer mehr herausbildet.",
        "Der namenlose Weise ist nicht durch das Herkommen etwas, sondern durch das, was er ist.",
        "Er ist die freie Individualität, die von den anderen aner­kannt wird, weil sie alles aus sich selbst ist, weil sie nichts anderes sein will, als was sie für die anderen ist.",
        "So steht Lohengrin als Repräsentant, als Führer der Menschheit zur Freiheit da.",
        "Das mittelalterliche Städtebewußtsein sehen wir repräsentiert in dem Weibe, das sich mit Lohengrin ver­bindet.",
        "Mit einer der großen Individualitäten der Mensch­heit verbunden wurde derjenige, der zwischen der Mensch­heit und den großen Wesen steht, der den Verkehr zwischen den großen Führern der Menschheit und den Menschen vermittelt.",
        "Ein solcher hat immer einen bestimmten Namen gehabt.",
        "Den nennt man in aller Geheim- und Geisteswissen­schaff mit dem technischen Namen des «Schwan».",
        "Der Schwan ist eine ganz bestimmte Stufe der höheren Geistes-entwicklung.",
        "Der Schwan vereinigt den gewöhnlichen Men­schen mit dem höheren Führer der Menschheit.",
        "Einen Ab­glanz von diesem sehen wir in der Lohengrinsage."
      ],
      [
        "Wir brauchen solche Dinge nicht in Begriffe zu fassen, die einer pedantischen Lebensauffassung entnommen sind.",
        "Ja, wir tun Unrecht, wenn wir es tun.",
        "Wir kommen nur zur Klarheit, wenn unsere Begriffe weitherzig werden, so daß uns die Dinge, die uns Richard Wagner verständlich macht, nicht pedantische Worthülsen sind, sondern Vorstellungen entzünden, die weit, weit sich ausspinnen.",
        "Gestatten Sie mir, daß ich nicht Begriffe mit pedantischen Konturen vor Sie hinstelle, sondern solche, die weite Perspektiven eröff­nen.",
        "Daher muß man eine Gestalt wie Lohengrin in ihrer welthistorischen Bedeutung hinstellen und zeigen, wie in Richard Wagners Seele sich ein Verständnis dafür angespon­nen hat und wie dieses Verständnis künstlerische Gestalt gewonnen hat."
      ],
      [
        "So ist es Richard Wagner auch gegangen mit der Idee vom heiligen Gral.",
        "Im letzten Vortrage: «Wer sind die Rosenkreuzer?» trat diese Idee vom heiligen Gral vor unsere Seele.",
        "Es ist höchst merkwürdig, daß in Richard Wag­ners Seele in einem bestimmten Zeitpunkte etwas aufleuch­tet, was wie ein Ahnen von jener großen Lehre des Mittel­alters, vom heiligen Gral war.",
        "Diese Lehre leuchtete ihm erst auf, als eine andere vorangegangen war.",
        "Im Jahre 1856 war es, als in Richard Wagners Seele die Idee auf­tauchte, die in dem Drama «Die Sieger» dargestellt werden sollte.",
        "Das Drama ist nicht ausgeführt worden.",
        "Das, was er aber hineingeheimnissen wollte, kam im «Parsifal» zum Ausdruck.",
        "Aber wohin die Idee ging, das stellt uns die Kon­zeption des Dramas «Die Sieger» dar:"
      ],
      [
        "Ananda wird geliebt von einem Tschandalamädchen.",
        "Ananda aber ist durch das Kastenvorurteil weit getrennt von der Liebe des Tschandalamädchens.",
        "Er darf der Liebe des Tschandalamädchens nicht nachgehen.",
        "Er wird Sieger über die eigene Natur dadurch, daß er ein Zögling des Buddha wird.",
        "In der Anhängerschaft des Buddha findet er den Sieg, da findet er sich zurück, da überwindet er die menschliche Neigung, und dem Tschandalamädchen wird eröffnet, daß es in einem früheren Leben ein Brahmanen­mädchen war und die Liebe eines Tschandalajünglings aus­geschlagen hat.",
        "Sie wird dann auch Siegerin und ist ver­einigt im Geiste mit dem Ananda, dem Brahmanenjüngling."
      ],
      [
        "In schöner Weise drückt Richard Wagner die Idee aus, sie geht bis zu den anthroposophisch-christlichen Grundlagen von Reinkarnation und Karma.",
        "Wir werden geführt bis zu dem Punkt, wo das Mädchen in ihrem früheren Leben sich selbst das zugefügt hat, was es jetzt erlebt.",
        "Im Jahre 1856 hat er das schon ausgearbeitet."
      ],
      [
        "Im Jahre 1857, am Karfreitag war es, wo er in der Einsiedlerhütte,"
      ],
      [
        "dem «Asyl auf dem grünen Hügel», saß und hinausschaute auf das Feld und sah, wie die Pflanzenwelt aus dem Erdboden herauskam.",
        "Da hatte er eine Ahnung von jenen Triebkräften, die durch die Strahlen der Sonne herauskamen aus der Erde und die durch die ganze Welt gehen, eine Ahnung von jener Triebkraft, die in jedem Wesen lebt, aber nicht so einfach bleiben kann.",
        "Wenn sie zu höheren und höheren Stufen hinaufsteigen will, muß sie durch den Tod hindurchgehen.",
        "So empfand er gerade an der sprießenden und sprossenden Pflanzenwelt, die er er­blickte, indem er hinauswendete den Blick über den Züricher See und die Villa Wesendonck, die polarische Idee, die an­dere Idee, die Idee des Todes, das, was Goethe so schön ausgedrückt hat in dem Satze, der das Gedicht «Selige Sehn­sucht» beschließt:"
      ],
      [
        "Und so lang du das nicht hast,"
      ],
      [
        "Dieses: Stirb und Werde,"
      ],
      [
        "Bist du nur ein trüber Gast"
      ],
      [
        "Auf der dunkeln Erde."
      ],
      [
        "Und was er in dem Hymnus an die Natur so umschrieb:"
      ],
      [
        "Die Natur hat den Tod erfunden, weil sie mehr Leben haben wollte, weil sie ein höheres, geistiges Leben nur aus dem Tode heraus schaffen kann."
      ],
      [
        "So empfand Richard Wagner am Karfreitag, wo das Symbolum des Todes vor die Menschheit und das Mensch­heitsgedächtnis hintritt.",
        "Da empfand er den Zusammen­hang zwischen Tod, Leben und Unsterblichkeit.",
        "Er lenkt sein Gefühl von dem Leben, das aus der Erde heraussprießt, zu dem Tod am Kreuze, zu dem Tode, der aber zu gleicher Zeit der Urquell ist für den Glauben der Christenheit, daß das Leben den Sieg erringen wird über den Tod, daß es das ewige Leben erringen wird.",
        "Das Leben der Ewigkeit sprießt"
      ],
      [
        "aus diesem Tod.",
        "Die tiefe Verwandtschaft der Karfreitags-idee, der Erlösungsidee, mit der sprießenden, sprossenden Natur, das lebte in Richard Wagner, und diese Idee ist identisch mit dem, was wir als die Gralsidee schildern konn­ten, wo die keusche Pflanze mit ihrer Blüte der Sonne ent­gegenstrebt im Gegensatz zum begierdevollen Menschen.",
        "Er sah den Menschen, wie er von der Begierde durchzogen ist, und betrachtete das Ideal der Zukunft, wo der Mensch durch die Überwindung der Begierde das höhere Bewußt­sein, jene höhere befruchtende Kraft erlangt haben wird, die der Geist erzeugen wird.",
        "Und er schaute hin auf das Kreuz, wie das Blut des Erlösers geflossen ist, das auf­gefangen wurde in der Gralsschale, und die das Symbolum gebildet hat für diese Idee von der Erlösung, und sie ver­band sich ihm mit dem Werden der Natur.",
        "Diese Idee zog im Jahre 1857 durch Richard Wagners Seele, und er schrieb damals mit einigen Strichen auf, was er dann in seinem Karfreitagszauber zum Ausdruck brachte.",
        "Er schrieb hin:"
      ],
      [
        "Aus dem Tod die werdende Pflanzenwelt und im Tod dem Christen das unsterbliche Leben.",
        "Da empfand er den Geist hinter allen Dingen und den Geist als Sieger über den Tod."
      ],
      [
        "Es mußte zwar zunächst hinter den anderen künstleri­schen Ideen seiner Seele diese Idee des Parsifal zurücktreten, aber sie kam doch noch heraus am Ende seines Lebens, wo sie ihm immer klarer wurde als Bild des Erkenntnispfades des Menschen.",
        "Das hat ihn veranlaßt, den Weg zum heiligen Gral darzustellen, um zu zeigen, wie bewirkt werden kann, daß des Menschen Begierdennatur geläutert wird.",
        "Dieses Idealist dargestellt in der heiligen reinen Schale, die dar­stellt den Pflanzenkelch, der vom Sonnenstrahl, der heiligen Liebeslanze, zu reinem und keuschem neuen Schaffen be­fruchtet wird.",
        "Es sticht der Sonnenstrahl hinein in das Stoff­liche wie die Lanze des Amfortas in das sündige Blut."
      ],
      [
        "aber bewirkt sie Leid und den Tod.",
        "Reinigt sich dieses sün­dige Blut, so daß es so rein ist wie der Pflanzenblütenkelch auf einer höheren Stufe, ohne Begierde, keusch wie der Pflanzenkelch dem Sonnenstrahl gegenüber, so erscheint das wie der Weg zum heiligen Gral.",
        "Der Weg dahin kann nur gefunden werden von dem, der mit reinem Herzen, ohne berührt zu sein von dem, was die Welt gibt, ohne weltliches Wissen, als reiner Tor dahin geht und in dem die Frage nach dem Weltgeheimnis lebt."
      ],
      [
        "So sehen wir, wie in Richard Wagner aus mystischer Grundlage heraus die Parsifalidee aus der heiligen Grals­idee geboren wird.",
        "Er hat sie einmal darstellen wollen, in­dem er die ganze mittelalterliche Geschichte in einer Art geschichtlichen Betrachtung in seinem Werk «Die Wibe-lungen » darzustellen beabsichtigte.",
        "Es sollte sich die mittel­alterliche Kaiseridee vergeistigen dadurch, daß er Barba­rossa nach dem Orient ziehen lassen wollte, und mit dem äußeren Reich wollte er dann alles Indische, wo der Held das ursprünglich Geistige des Christentums aufsuchen wollte, hineinströmen lassen.",
        "So ergießt sich dann für ihn die Idee der mittelalterlichen Kaisergeschichten in der Par­sifalsage, und so konnte er dann in der Parsifalidee die Karfreitagstradition der Christenheit in solch wunderbarer Weise künstlerisch zum Ausdruck bringen, daß ich sagen darf, Richard Wagner hat vollbracht, was ihm als Ideal vorschwebte: die Kunst religiös zu machen.",
        "In dieser künstlerischen Neugestaltung der Karfreitagstradition hat Richard Wagner jene schöne geniale Idee zum Ausdruck gebracht von dem Zusammenwirken des Glaubens- und Gralsmotives, jene Idee, daß die Menschheit erlöst werden wird, daß sie, sich vervollkommnend, hinstreben wird zur Erlösung, daß in dem, was die Menschheit als Geist durch­strömt, von dem jede Seele einen Tropfen hat als höheres"
      ],
      [
        "Selbst, daß das in dem Christus Jesus als Erlösung der Menschheit voranleuchtet."
      ],
      [
        "Das stand an jenem Karfreitag 1857 schon vor der Seele Richard Wagners und hat ihm eingegeben die Verbindung der Parsifalidee mit der Erlösung durch den Christus Jesus, der die geistige Atmosphäre, in der die Menschheit lebt, durchströmt, und den wir fühlen können, wenn wir ver­ständnisvoll erfühlen die Erzählung vom heiligen Gral.",
        "Das kann wieder zu einem konkreten geistig-seelischen Leben erwachen, wenn man in der Karfreitagsidee wieder herausfühlt den Übergang von der Mitternacht von Grün-donnerstag, von der weichenden Gründonnerstagwelt, zum Karfreitag, dem Symbolum des Sieges der auferstehenden Natur."
      ],
      [
        "Daß die Feste wieder lebendig werden, das war auch etwas, was in Richard Wagner lebte, als er aus einer un­mittelbaren Festesidee sein Kunstwerk herausgeboren hat.",
        "Die Feste sind herausgeboren aus einem lebendigen Ver­ständnis der Natur.",
        "Das Osterfest ist festgesetzt worden in einer Zeit, in der man wußte, daß die Konstellationen von Sonne und Mond hereinwirken aus der Natur in den Men­schensinn.",
        "In dem Osterfest kommt es konkret zum Aus­druck.",
        "Die heutigen Menschen wollen es abstrakt festsetzen, so daß man es nicht mehr so erlebt, wie wenn man familiär vertraut ist mit der Natur.",
        "Wenn man geistig empfindet, so empfindet man alles, was um uns ist, geistig.",
        "Wenn wir noch spüren, was die Tradition uns überliefert hat an Festen, dann werden wir da auch spüren etwas, wie es uns der Kar­freitag geben soll.",
        "Das spürte Richard Wagner und er fühlte auch, was das Erlöserwort «Ich bin bei euch bis ans Ende der Welt» bedeuten soll: Folgt den Spuren, die euch führen können zu dem hohen Ideal des heiligen Grals.",
        "Dann wer­den die Menschen, die in der Wahrheit leben, selbst Erlöser."
      ],
      [
        "Ein Erlöser hat die Menschheit erlöst.",
        "Richard Wagner fügt aber noch das andere Wort hinzu: Wann ist der Erlöser erlöst?",
        "Er ist erlöst, wenn er in jedem Menschenherzen wohnt.",
        "So wie er in jedes Menschenherz heruntergestiegen ist, so muß jedes Menschenherz hinaufsteigen.",
        "Und auch davon fühlte Richard Wagner etwas, als er aus dem Glau­bensmotiv heraus das mystische Fühlen der Menschheit in das schöne Wort im Parsifal ausklingen ließ:"
      ],
      [
        "«Höchsten Heiles Wunder:"
      ],
      [
        "Erlösung dem Erlöser!»,"
      ],
      [
        "dieses Wort, das ihn so recht verschwistert und vermählt zeigt mit dem höchsten Ideale, das sich der Mensch setzen kann: sich zu nähern derjenigen Macht, die in der Welt lebt und zu uns herunter will.",
        "Wenn wir ihrer würdig werden wollen, dann bringen wir, was aus Richard Wagners Parsi­fal am Schlusse heraustönt: Erlösung dem Erlöser."
      ]
    ]
  },
  {
    "order": 14,
    "title_de": "BIBEL UND WEISHEIT Berlin, 26. April 1907",
    "paragraphs": [
      "Wir haben gestern versucht, uns den Sinn vor die Seele hinzurücken, durch den dasjenige, was wir Geisteswissenschaft nennen, sich den religiösen Urkunden annähern will. Wir wollen heute versuchen, wenigstens in einigen Bei­spielen tiefer in diejenige religiöse Urkunde, die der gegen­wärtigen Kulturmenschheit doch wohl noch am nächsten liegt, in die Bibel, einzudringen. Vom Standpunkte der Geisteswissenschaft kommt man am leichtesten in die Bibel hinein, wenn man zunächst versucht, von dem Neuen Testa­ment, von den Evangelien auszugehen. Nachdem wir ge­stern auseinandergesetzt haben, wie wir die sogenannte Kritik, den kritischen Geist auffassen sollen, wie wir uns zu der Niederschrift der verschiedenen einzelnen Teile des Neuen Testamentes und zu der Schriftensammlung des Alten Testamentes vom Standpunkte der Geisteswissen­schaft stellen können, wollen wir heute mehr das Positive ins Auge fassen, voraussetzen, was gestern gesagt worden ist und ohne jede Befangenheit vom geisteswissenschaft­lichen Standpunkt in diese Sache hineinleuchten.",
      "Sie wissen, daß dem Menschen, wenn er aus dem Bedürf­nisse des christlich-gläubigen Herzens heraus an die vier Evangelien herangeht, zunächst eigentümliche Widersprüche begegnen können, welche sich aus den vier Evangelien, die man nach Matthäus, nach Markus, nach Lukas, nach Jo­hannes nennt, ergeben. Derjenige, der sich heute wenn auch noch so gläubig zu diesen Büchern verhält, hat doch keine",
      "richtige Vorstellung davon, in welchem Verhältnisse in alten, viel religiöseren Zeiten der Gläubige der Bibel gegen­überstand, was das Wort «Bibel», respektive der Aus­druck «das Wort Gottes» eigentlich für die alten Gläubigen bedeutete. Wir brauchen uns nur an das Wort« Inspiration» zu erinnern und daß durch Jahrhunderte hindurch die gläubigen Gemüter festgehalten haben daran, daß jene, welche die religiösen Urkunden niedergeschrieben haben, inspiriert waren, daß sie unter dem unmittelbaren Einflusse des göttlichen Geistes selbst geschrieben haben. Und so wahr sie den Glauben hatten, daß von diesem göttlichen Geiste nur die Wahrheit ausgehen konnte, so wahr erschien ihnen jedes Wort, das in der Bibel stand, als heilig. Die Bibel war ihnen der Ausdruck für die gewaltigen Welt­rätsel, die sich vor die Seele des Menschen hindrängten. Wie hätte ein Mensch, der sich vorstellte, daß die alten Gottesmänner Persönlichkeiten waren, die unmittelbar un­ter der Inspiration des göttlichen Geistes standen, glauben können, daß diese etwas geschrieben hätten, ja etwas hätten schreiben können, an das man Kritik anlegen muß. Dann hätte in den Herzen dieser Gläubigen nicht ein unmittel­bares Hängen an jeglichem Wort sein dürfen.",
      "Für den heutigen Menschen ist es schwer, sich in diese Gemütsstimmung hineinzuversetzen. Er liest das erste und er liest das dritte Evangelium. Es werden ihm zwei Ab­stammungstafeln des Jesus von Nazareth vorgeführt, die eine in dem Evangelium nach Matthäus die andere in dem Evangelium nach Lukas. Er verfolgt die Namen und findet, daß dieselben nicht übereinstimmen, daß schon beim drit­ten Glied von Joseph aufwärts ein anderer Name auftritt, daß, wo bei Matthäus Salomon steht, bei Lukas Nathan sich findet und so weiter, daß eine ganze Reihe von Namen in den Tafeln verschieden sind, und er frägt sich: Wie ist es",
      "möglich, daß dasjenige, was durch Jahrhunderte hindurch den Menschen als ein Quell der Wahrheit gedient hat, solche Widersprüche aufweisen kann? - Im Grunde genom­men sehen wir in einer einzigen solchen Erwägung den Keimpunkt zu all den Zweifeln, die, hinsichtlich der Ein­heitlichkeit der Schrift und zuletzt bezüglich ihrer Inspira­tion, den Menschen, den Kritikern gekommen sind. Aus solchen Erwägungen heraus, die in komplizierter Weise bis ins feinste Detail durchgeführt worden sind, hat man die Bücher des Neuen Testamentes zerlegt, hat man gefunden, was mehr oder weniger echt ist, hat man gefunden, daß das erste Evangelium von dem vierten abweicht, woraus sich notwendig ergeben mußte, daß man es im vierten Evangelium mit etwas ganz anderem als mit einer histo­rischen Urkunde zu tun hat. Wie könnte man auch un­befangenen Geistes diese Widersprüche hinwegdekretieren? Es ist nur zu natürlich, daß der moderne Mensch, wenn er so etwas sieht, Kritik anlegen muß.",
      "Nun fragen wir uns aber, wie ist es möglich, daß durch Jahrhunderte, Jahrtausende hindurch wahrlich auch nicht gerade dumme Köpfe diese Bücher in der Hand gehabt haben und nicht auch zu einer Kritik, zu einem Sehen dieser Widersprüche gekommen sind? In bezug auf die große Menge der Gläubigen könnte man sich vielleicht darauf berufen und sagen, die Bibel ist bis in die neueste Zeit nur in den Händen einiger weniger gewesen; die Gläubigen haben sie vor der Erfindung der Buchdruckerkunst fast gar nicht in die Hand bekommen. Man kann sagen, die große Menge konnte gar nicht irre werden an etwas, was ihr von den leitenden Persönlichkeiten gar nicht vorgelegt wurde. Aber sollen wir uns vorstellen, daß diejenigen, welche die Bibel in die Hand bekommen haben, nicht gesehen hätten, was die heutige Kritik sagt?",
      "Es wird von einzelnen Historikern eingewendet: lang­sam, durch die Gewalt der Kirche, habe sich das Ansehen dieser Bücher erst befestigt, nach und nach erst habe sich das herausgebildet, was man das Ehrfurchtsgebietende die­ser biblischen Geschichte nennt. Vor einer richtigen ge­schichtlichen Betrachtung kann der Inhalt der Bibel auch gar nicht bestehen. Wenn wir zurückgehen in die ersten christlichen Jahrhunderte und die Tatsachen prüfen, dann kommen wir zu dem Urteil, daß bei dem Konzil zu Nikäa festgestellt worden ist, welches die richtigen Evangelien sind, und daß durch Machtspruch dekretiert worden ist:",
      "Das sind die heiligen Schriften.",
      "Vor einer unbefangenen geschichtlichen Betrachtung kann das nicht bestehen. Wir werden zu Persönlichkeiten ge­führt, die in den alten Zeiten des Christentums gelebt haben. Wir finden dann in ihren Mitteilungen, daß zum Beispiel im Jahre 160 n. Chr. eine sogenannte Evangelienharmonie gemacht wurde, das heißt eine Zusammenstellung der verschiedenen Evangelien, so daß sie ein einheitliches Bild geben sollten. Später ist dies noch öfters gemacht wor­den, und wir können finden, wenn wir die Evangelien vom zweiten Jahrhundert sorgfältig prüfen, daß auch dasjenige hineingearbeitet worden ist, was wir jetzt als Inhalt des Neuen Testamentes kennen. Wir können noch weiter zu­rückgehen, bis zu den ersten Kirchenvätern. Wenn wir ge­rade diese kritisch prüfen, so zeigt sich uns, wie sie mit ungeheurer Ehrfurcht von der Bibel sprechen, mit einer Ehrfurcht, die die Annahme zuläßt, daß sie geglaubt haben, die Bibel sei von höherer Geistigkeit inspiriert. Wir können bis zu Origines zurückgehen und bemerken dann, wie er in derselben Art und mit derselben Ehrfurcht von den bib­lischen Büchern spricht. Und wenn wir einzelne Worte neh­men, die sogar nur derjenige mitteilt, von dem nicht mit",
      "Unrecht gesagt wird, daß er noch ein Hörer des Apostels Johannes gewesen sei, Matthäus, dann finden wir, daß aus seiner Seele etwas herausspricht, was wir in demselben Sinne zusammenfügen können mit dem, was später die Stimmung der Gläubigen, auch der gelehrtesten Gläubigen, gegenüber den Evangelien war.",
      "Freilich muß sich der Mensch, der so etwas betrachtet, etwas, ja sogar gründlich, frei machen können von gewissen Vorurteilen. So wie spätere Zeiten sich zu dem, was man Christentum nennt, gestellt haben, so haben sich diejenigen, die in den ersten Jahrhunderten als Gelehrte gelebt haben, nicht dazu gestellt. Und wenn heute jemand von irgend­einem orthodoxen Standpunkte aus zu einem kommt, der die Bibel nicht gerade so auffaßt, wie er, und zu ihm sagt, er sei ein Ungläubiger, er dürfe sich nicht Christ nennen, er verstoße gegen das rechte Wort der Bibel - so dürfen wir wohl an solche alten Gläubigen erinnern, an denen zu zweifeln auch die nicht wagen, welche sich die Bibel in willkürlicher Weise zurechtlegen. An ein Wort des Kirchenvaters Augu­stinus will ich mich anlehnen. Das Wort heißt: Dasjenige, was man heute christliche Religion nennt, ist uralt. Es ist die uralte wahre Religion, und das, was die uralte wahre Religion ist, das nennt man jetzt die christliche Religion.",
      "Man denke an ein solches Wort und stelle dann daneben, was insbesondere ein geisteswissenschaftlidier Erklärer der Bibel sehr häufig erfahren kann. Ist es nicht oftmals ge­radezu tragisch, wie gegnerische Stimmungen hervorgeru­fen werden, wie der Geisteswissenschafter bei Bekannten, Freunden und Verwandten herben Widerspruch findet, in­dem sie ihm sagen: da kommst du wieder mit deinen geistes-wissenschaftlichen Phrasen, wo bleibt denn da die Bibel? Einem solchen Ausspruche liegt eine tiefe Unkenntnis der wirklichen Bibel zugrunde und außerdem liegt darin eine",
      "große Prätention, der Anspruch, mit seiner Auffassung der Bibel unfehlbar zu sein. Wenn sich nur solche Gläubige ganz klar darüber werden wollten, was es heißt, der geistes­wissenschaftlichen Auffassung der Bibel so gegenüberzutre­ten. Es heißt nichts anderes als: was ich in der Bibel finde, ist das unbedingt Richtige.",
      "Es ist ja nicht so, daß der geisteswissenschaftliche Stand­punkt sich etwa weniger positiv zur Bibel verhält, sondern so, daß er gerade die wirkliche Bedeutung, den wirklichen Sachverhalt aus dieser Bibel wiederum herausentwickeln will. Richtiges Verstehen ist es, um was es sich gegenüber den religiösen Urkunden für die geisteswissenschaftliche Weltanschauung handelt. Daher darf derjenige, welcher aus Bequemlichkeit bei irgendeiner anderen Ansicht steht, die gerade zufällig da ist, an die er sich gewöhnt hat, der geisteswissenschaftlichen Anschauung eigentlich nicht ent­gegentreten. Denn vielfach lebt in der Seele derjenigen, die einer wirklichen Erklärung der Bibel entgegentreten, etwas Gegnerisches, so daß sie sagen: Ihr verleugnet die Bibel, ihr macht euch und eure Familie unglücklich. - Vielfach steckt auch nichts anderes dahinter als der Gedanke: Ich will nicht lernen; ich weiß, was ich weiß.",
      "Lesen wir einem solchen Ausspruch gegenüber die Bergpredigt und verstehen wir sie richtig, dann werden wir uns nicht mehr, auch wenn wir uns Christen nennen, auf einen solchen Standpunkt stellen dürfen. Nur der erste Satz der Bergpredigt sei hier zitiert. Es ist, wie die, welche häufiger hierher kommen, wissen, öfter schon gesehen. Richtig deutsch wiedergegeben heißt er: «Selig sind, welche da sind Bettler im Geiste, denn sie werden in sich selbst finden die Reiche der Himmel.» Man kann das, was man geistes-wissenschaftliche Gesinnung nennt, nicht schöner ausdrük­ken, als es mit diesen Worten die Bergpredigt tut.",
      "Was heißt geisteswissenschaftliche Gesinnung? Es heißt nichts anderes als dasjenige, was in uns liegt, den tiefsten Kern unserer eigenen Wesenheit, die in uns lebendige, gei­stige Natur zur Entfaltung zu bringen.",
      "Ebenso wie das­jenige, was unseren Körper bildet, den Stoffen der um­liegenden Welt entnommen ist, so ist dasjenige, was in uns vorhanden ist, dem Geiste, der um uns lebt und zu allen Zeiten gelebt hat, entnommen. Und so wahr es ist, daß unser Körper nur ein Tropfen ist in dem Meere der mate­riellen Wirklichkeit, so wahr ist es, daß unsere Seele, unser Geist nur ein Tropfen ist in dem Meere des allumfassenden Weltengeistes.",
      "Aber so wie der Tropfen, der aus dem Meere genommen wird, seiner Substanz nach dasselbe ist wie das Wasser des ganzen Meeres, so ist dasjenige, was in des Menschen tiefster Seele lebt, substantiell gleich mit dem Wesen des Göttlichen. Weil der Gott im Menschen lebt, kann der Mensch Gott erkennen; weil der Mensch geistig ist, kann der Mensch, wenn er nur will, eindringen in die geistige Welt um ihn herum.",
      "Ein zweites gehört aber dazu, wenn der Mensch wirklich eindringen will in diese geistigen Welten, und dieses zweite, das dazu gehört, ist mit dem einfachen Wort gegeben: Niemals stehenbleiben! Man darf eine Entwicklung nicht bloß glauben, sondern man muß die Entwicklung leben.",
      "Was heißt es, eine Entwicklung leben? Nichts anderes, als das Bewußtsein in sich tragen, daß der Mensch sich aus einem unvollkommenen Zustande zu seinem jetzigen entwickelt hat, und daß er sich in die Zukunft hinein jederzeit weiter entwickeln kann.",
      "Zunächst denken wir nicht daran, daß des Menschen äußere Gestalt sich in dieser Entwicklung umändert, sondern daran, daß die Menschenseele von Stufe zu Stufe hinaufklimmen kann; daß es ein Aufwärtsschreiten dieser Seele gibt, daß es mög­lich ist, von Tag zu Tag vollkommener zu werden. Heute",
      "lernen wir etwas, unsere Seelenkräfte sind imstande, dies oder jenes einzusehen, unser Wille ist imstande, dies oder jenes zu tun. Bleiben wir stehen bei dem, was wir heute einsehen, bei dem, was unser Wille heute zu tun imstande ist, dann entwickeln wir uns nicht. Tragen wir aber das Bewußtsein in uns, daß außer den Kräften, die sich in uns schon entwickelt haben, auch noch andere Kräfte in uns schlummern - so schlummern, wie der Pflanzenkeim, der sich zur Pflanze entwickelt hat, andere Pflanzenkeime in sich schlummernd trägt -, dann werden wir jeden Tag mehr erkennen, daß wir durch eine höhere Entfaltung des Willens aus unserer Seele die geistigen Augen und Ohren herausholen können, und sehen, daß es mit jedem Tag besser werden kann. Dies dürfen wir nicht im trivialen Sinne verstehen, sondern so, daß diese Entwicklung in geistig-seelischer Richtung eine universelle Bedeutung hat.",
      "Wenn wir in der materiellen Welt tierische Gestalten sich körperlich zu einer edlen Menschenform entwickeln sehen, so berechtigt das nicht zu der Annahme, daß der Mensch sich aus den Tieren herausentwickelt habe, auch wenn die Naturwissenschaft festgestellt hat, daß in bezug auf die physische Gestalt des Menschen eine größere Ähn­lichkeit zwischen den niedrigstentwickelten Menschen und den höchstentwickelten Affen, als zwischen den niederen Affen und den höchsten Affenarten bestehe. Von diesem Verhältnis leitet ja die Naturwissenschaft die Verwandt­schaft des Menschen mit dem Affen ab. Dies hat im Jahre 1859 wie eine große Ketzerei der große Naturforscher Huxley ausgesprochen. Ein großer Teil dessen, was Sie in Haeckels Schriften lesen, ist unter dem unmittelbaren Ge­mütseindruck dieses Satzes geschrieben. Derjenige, der an die geistige Entwicklung glaubt, sagt sich: Wohlan, zu­gegeben, daß der Mensch in bezug auf seine äußere Form,",
      "seine Körperlichkeit dem höchstentwickelten Affen näher steht als dieser dem niedrigsten seiner eigenen Gattung, aber ebenso wahr ist es auch, daß derjenige, der eine be­stimmte Stufe der Geistigkeit erreicht hat, dem auf niede­ren Stufen der Menschheit Stehenden ferner steht als der niedrigste Mensch dem höchstentwickelten Tiere.",
      "Verfolgen wir den Faden der Entwicklung in die höhe­ren Gebiete, so sehen wir ihn sich in geistige Gebiete hinein fortsetzen, und in dem Geistigen sehen wir die von der Geisteswissenschaft geschilderte Entwicklung als etwas ebenso Wirkliches, wie es für die sinnlichen Augen die materielle Entwicklung ist. Theosophie hat es zu allen Zeiten gegeben. Schon . . . sagt, daß das alte indische Atma Vidya dasselbe ist, daß es aber zu den verschiedenen Zei­ten mit den verschiedensten Namen benannt wurde. Die heutige Naturforschung anerkennt eine Entwicklung von den niederen tierischen Formen bis zum Menschen. Dagegen sagte die Theosophie zu allen Zeiten: wir erkennen auch eine solche Entwicklung an, wir stehen durchaus auf dem Boden solcher Entwicklung, wir erkennen an, daß es einen gewaltigen Unterschied gibt zwischen der vollkommenen Gestalt des Menschen und einem niederen Tiere, das im Meerschlamme lebt und kaum dem mit dem Mikroskop bewaffneten Auge sichtbar ist. Durch wie viele Zwischen­stufen muß der Mensch hindurdischreiten, wenn er vom Unvollkommenen zum Vollkommenen vorrückt! Als ebenso wirklich und real sieht der Geisteswissenschafler die Ent­wicklung der Seele und des Geistes an. Er sieht ebenso große Unterschiede zwischen solchen Individualitäten, die Eingeweihte geworden sind, die in einem höheren Grade die in der Seele eines jeden Menschen liegenden Eigenschaf­ten zu göttlichem Schauen gebrauchen, und demjenigen Menschen, der kaum die ersten Keime der Seelentätigkeit",
      "entwickelt hat. Der Unterschied in der Entwicklung vom Unvollkommensten der niedrigsten Seelenstufe bis zu dem vollkommenen Eingeweihten ist größer als der zwischen dem kleinsten Lebewesen und dem vollkommensten Kör­per des Menschen. Wer weiß, daß es Eingeweihte gibt, die tief hineinschauen können in die Entwicklung der materiel­len Dinge, der weiß, daß es auch geistige Entwicklung gibt.",
      "Wer das weiß, der weiß auch, daß die Stimmung keine andere sein kann, als daß er sich sagt: ich sehe hinauf zu den göttlichen Idealen, zu denen ich den Keim in der Seele trage; ich weiß, daß in der Zukunft sich etwas herausentwickelt haben wird, was heute noch in mir schlummert, nur schwach veranlagt ist. Ich weiß aber auch, daß ich alle Kräfte anwenden muß, um zu diesen Höhen hinaufzukom­men. Als ein Bettler im Geiste kommt sich dann der vor, welcher so die geistige Welt ansieht. Und der ist «beseligt», das heißt selig fühlt er sich dann. Und wir haben in der Bergpredigt im geisteswissenschaftlichen Sinne ein so wun­derbares Wort das da heißt: «Selig sind die, die da Bettler sind im Geiste, denn sie werden in sich selbst finden die Reiche der Himmel.» - Keiner, der den Sprachgebrauch der alten Zeiten kennt, wird wähnen, daß diejenigen, welche vom Himmel sprechen, einen Himmel im unbekannten Jenseits meinten. Man stellte sich vor, daß überall da, wo man ist, auch der Himmel ist. Wo wir jetzt sind, da ist der Himmel, da ist die geistige Welt. Ebenso wie der Blinde, wenn er operiert wird, den Raum, den er vorher nur tasten konnte, mit Farben erfüllt sieht, so sieht der, dessen gei­stiger Sinn geöffnet ist, eine neue Welt um sich. Er sieht, was immer um ihn herum ist, in neuer Gestalt, in der Ge­stalt, in der er sehen muß, wenn er sich zu höherer Mensch­lichkeit hinaufentwickeln will. Er braucht nicht zu glauben, daß anderswo, an einem anderen Orte oder zu anderer",
      "Zeit der Himmel sei. Ihm gilt das Wort des Christus: Das Himmelreich ist mitten unter euch.",
      "Das Himmelreich ist da, wo wir sind, es durchdringt alle körperlichen Dinge. Wie das Wasser das Eis durch­dringt, so schwimmt gleichsam im Meere des göttlichen Geistes dasjenige, was sich aus diesem Geist als körperlich materielle Welt verdichtet hat. Alles Körperliche ist ver­dichtetes, verwandeltes Geistiges. Hinter allem Körper­lichen steht das Geistige. Hier werden wir schon zu dem­jenigen geführt, was in bezug auf geisteswissenschaftliche Auffassung das Verhältnis des Menschen zur Entwicklung ist. Ebenso wie draußen in der tierischen Welt Vollkomme­nes und Unvollkommenes lebt, so leben in bezug auf das Geistige die verschiedensten Individualitäten: die einen fortgeschritten, die anderen zurückgeblieben, die einen hin-einsehend in Gebiete, wohin die moderne Wissenschaft noch leuchtet, die anderen hineinsehend in die tiefsten Unter­gründe der menschlichen Erkenntnis, vom Wilden bis zu dem zur Göttlichkeit entwickelten Menschen, der befähigt ist, draußen in der Welt das Geistige um sich zu schauen. Alle diese Zwischenstufen glaubten nicht nur, sondern kannten diejenigen, welche Eingeweihte waren. Und wenn man von Eingeweihten sprach, so sprach man von ihnen als von solchen, die mehr wissen als die sie umgebende Menschheit. Immer hat man von solchen Eingeweihten ge­sprochen, und nun wollen wir uns einmal klarmachen, in welchem Sinne man von den in die geistigen Welten Ein­geweihten gesprochen hat.",
      "Wie schon oft hier auseinandergesetzt worden ist, finden wir, wenn wir in uralte Zeiten zurückgehen, daß auch das Alltagsbewußtsein anders war als heute, daß ein mehr hellseherisches Bewußtsein vorhanden war. Hellseherisch wird es nicht genannt, weil es etwa klarer wäre als das",
      "Tagesbewußtsein, sondern weil es gleichsam durch die Ge­genstände hindurch bis in die Seele hinein sieht, aber es ist ein dumpfes, dämmerhaftes Bewußtsein, dessen Überreste sich im nächtlichen Traumbewußtsein des Menschen er­halten haben. Aus ihm hat sich das heutige taghelle Be­wußtsein der Menschheit entwickelt.",
      "Wenn wir zurück­blicken in jene alten Zeiten, wo die große Masse der Menschen in diesem heilseherischen Bewußtsein lebte, so finden wir, daß es auch da schon Eingeweihte gab. Wodurch unterscheiden sich nun jene alten Eingeweihten von den­jenigen, die noch in einem mehr dämmerhaften Bewußtsein um sie herum waren?",
      "Sie unterscheiden sich dadurch, daß sie schon etwas wußten von dem Bewußtsein, das die Menschheit bekommen sollte und heute hat, dadurch, daß sie imstande waren, von der Zukunft etwas vorauszuneh­men, in der Art in die Welt hineinzuschauen, wie die ganze Menschheit in späterer Zeit es erlangt hat. Es war diejenige Art, welche mit den Augen und Ohren des Leibes wahr­nimmt, mit denjenigen Organen, mit denen der Mensch sinnlich untersucht und verstandesmäßig begreift.",
      "Wie das heute bei den Menschen im allgemeinen wohl der Fall ist, so war es auch schon bei einzelnen eingeweihten Menschen der Vorzeit. Sie waren eben deshalb Eingeweihte. Der Ein­geweihte nimmt etwas von der Zukunft voraus.",
      "Ebenso trägt der Eingeweihte unserer Tage etwas von dem erhöh­ten Hellsehen, von dem erhöhten Schauen, das die Mensch­heit in Zukunft haben wird, in sich. Er weiß etwas zu sagen von dem, was die jetzige Menschheit in Zukunft haben wird.",
      "So blickten die Alten, die etwas von diesen Dingen ver­standen haben, hinauf zu dem Eingeweihten. Sie sagten sich: Wie er die Dinge ansieht, so werden in Zukunft die Menschen die Dinge auch ansehen. Sehen wir uns ihn an, er",
      "ist das lebendige Ideal, er ist derjenige, der uns durch seine Gestalt erkennbar macht, was wir sein werden. - In diesem Sinne war er ihnen ein Prophet, und wenn er noch höher stand, ein Messias. Und so sagten sie sich, der Verlauf der Geschichte wird so sein, daß er die große Zahl der Menschen zu dem, was er erreicht hat hinführen wird.",
      "Einen «Erst­geborenen» nannten sie einen solchen. Derjenige aber, wel­cher in solcher Weise eingeweiht werden sollte, hatte durch verschiedene Stufen hindurchzugehen. Es gibt durch die verschiedenen Stufen bis zu den höchsten Einweihungsstufen hinauf die mannigfaltigsten Erkenntnis- und Wil­lensgrade.",
      "Durch viele Stufen kann man durchschreiten. Wie die Pflanze bei ihrer Entwicklung die verschiedenen Stufen durchmacht, von der Wurzel zu Blatt, Blüte und Frucht, so schreitet der Mensch hinauf von Einsicht zu Ein­sicht, bis er vom Schüler zum Eingeweihten selber wird.",
      "Dieser Fortschritt geschieht durch Schulung, und diese Schulung kann man sich aneignen. Derjenige, welcher leugnet, daß es eine solche Schulung gibt, durch die er zu einer höheren Art des Anschauens, zu der Eröffnung von Augen und Ohren des Geistes gelangen kann, der weiß es eben nicht, der hat noch keine Kunde erhalten von solcher Schulung.",
      "Das ist die Aufgabe der Geisteswissenschaft: der Menschheit zu sagen, daß es eine solche Schulung der Auf­wärtsentwicklung gibt. In meiner Zeitschrift «Luzifer-Gnosis» können Sie lesen, daß jetzt in viel tieferer Weise von dem Prinzip der Einweihung und der geistigen Kultur gesprochen werden kann.",
      "Die mannigfaltigsten Gründe sprechen dafür. Einen Grund möchte ich aber anführen.",
      "Gerade das ist das Tragische, das so Bedrückende, die Seele Zermarternde für den modernen Menschen, daß er an die alten Urkunden nicht mehr glauben kann, daß ihm dieselben nicht mehr Verkörperungen des Wortes Gottes",
      "sein können, weil die Entwicklung von Verstand und Ver­nunft zu weit vorgerückt ist, so daß er die alte Botschaft nicht mehr brauchen kann. Er braucht aber eine neue Bot­schaft, und diese will ihm die Geisteswissenschaft bringen. Wir haben gleichsam im Bilde in die Zukunft hin eingesehen, und heute noch sieht derjenige, welcher sich zum Ein­geweihten entwickelt, die Entwicklung der Menschheit in der Zukunft. Er muß sich aber nach bestimmten Methoden entwickeln. Ebenso wie die Methoden, durch die man astro­nomische Wahrheiten erfährt, ganz bestimmte sind, so sind die Methoden, durch die man in die höhere Geistigkeit hinaufrückt, auch ganz bestimmte. Niemand darf sich sagen, daß er auf eigene Faust in die höheren Gebiete hinauf­steigen soll. Das ist so, wie wenn man auf eigene Faust Mathematik studieren und nichts auf Autorität hin an­nehmen wollte. Man braucht aber einen Leiter und Führer, der einem die Wege zeigt. Keine andere Autorität gibt es mehr auf diesem Gebiete. Daher ist es nur Rederei, wenn das Prinzip des gläubigen Hinneigens und Bekennens auf die Geisteswissenschaft angewendet wird. Es ist ein Miß­verständnis, wenn in der Geisteswissenschaft von Autorität und Gläubigkeit gesprochen wird.",
      "Nun gab es in den verschiedenen Jahrtausenden immer Bücher - eigentlich nicht Bücher, sondern mehr eine münd­liche Tradition, wenn wir in die alten Zeiten zurückgehen, und diese mündliche Tradition umfaßte die Regeln, wie man eingeweiht wird. Wollen wir uns einen Begriff von dem machen, wie solche Tradition war, wie solche Vor­schriften waren, die zeigten, was der Mensch zu tun hat, wenn er anfängt sich zu vergeistigen, bis zu den höchsten Einweihungsstufen, so brauchen wir nur daran zu denken, daß bei denen, die als Führer und Leiter wirkten, nichts niedergeschrieben werden durfte. Diese Regeln dürfen auch",
      "heute noch nicht niedergeschrieben, sondern nur mündlich denjenigen übertragen werden, die dazu würdig sind. Es gab einen Einweihungskanon. Er enthielt die Regeln der Geburt des Geistesmenschen; er zeigte die Regeln, die der Mensch erfüllen muß, um zu den hohen Zielen zu kommen. Wer sich dem geistigen Streben widmete, der mußte von einer Stufe der Übungs- und Lebensweise zur anderen, höheren geführt werden. Bist du auf der höheren Stufe, dann kommt der Eingeweihte und zeigt dir die höheren Geheimnisse.",
      "Nur noch ein Wort über die Art und Weise, wie ein solcher Einweihungskodex gehandhabt worden ist. Das ist heute nicht mehr so üblich wie in alten Zeiten. Die Einweihungsprozesse schreiten auch vorwärts. Der Schüler wurde in alten Zeiten in eine Art Ekstase gebracht. Das Wort hatte damals eine andere Bedeutung als heute, es bedeutete nicht Außer-sich-Sein, sondern ein Bewußtwerden in höheren Be­wußtseinszuständen und dahin hatte der geistige Führer den Schüler geführt. Es war vorgeschrieben, wie lange man in solchem Bewußtseinszustande gehalten werden mußte; es waren dreieinhalb Tage. Heute ist es nicht mehr so, daß das Bewußtsein herabgedämpft wird. Damals aber war der Betreffende in Ekstase und Entrückung, da wußte er nicht, was um ihn herum in der Sinnenwelt vorging, da war der Einzuweihende auf dem Gebiete der sinnlichen Welt wie einer, der schläft. Er wurde also hingeführt zu einem Be­wußtseinszustand, in dem die äußere Sinnenwelt schwand. Aber was er erlebte, unterschied sich beträchtlich von dem, was der heutige Mensch erlebt, wenn beim Einschlafen die äußeren sinnlichen Gegenstände um ihn herum verschwin­den. Die äußeren sinnlichen Dinge verschwanden, aber der Mensch lebte in einer Welt des Geistes; licht wurde es um ihn herum. Das, was man Astrallidit nennt, ging ihm auf:",
      "ein Licht, das ein anderes Licht ist als das physische, das uns erscheint wie ein Meer von geistiger Substanz, in dem geistige Wesenheiten eingebettet sind und aus dem sie sich herausentwickeln. Und wenn er noch höher stieg, hörte er aus dieser Welt erklingen, was in den alten pythagoräischen Schulen die Sphärenharmonie genannt wird. Dasjenige, was der Verstand als Weltgesetz in Begriffen erkennt, das nimmt der, welcher auf solcher Stufe sich befindet, wie eine Art Klang, wie geistige Musik wahr. Die geistigen Kräfte äußern sich in Harmonie und Rhythmus. Es ist aber dabei nicht an die äußere Musik zu denken. Die geistige Welt, die Welt der Himmel klingt und tönt für das astrale Licht. In diese Welt wurde der Einzuweihende eingeführt. Da lernte er die Stufen der menschlichen Göttlichkeit kennen, die die Menschheit erst in fernen Zeiten erklimmen wird. Das alles wurde für ihn Wahrheit, das durchlebte er in dreieinhalb Tagen.",
      "Unzählige Menschen haben in der Welt gelebt und leben noch, die wissen, daß das, was dem Menschen heute grotesk erscheint, ebenso eine Welt der Wirklichkeit ist, wie die, welche das äußere Ohr und das äußere Auge wahrnehmen kann. Wenn dann der Betreffende nach dreieinhalb Tagen wieder in die Sinnenwelt zurückgeführt war, wenn er be­reichert mit dem Wissen vom geistigen Leben wieder ein­ging in diese Welt, wenn er vorbereitet war dafür, ein Zeuge der geistigen Welt zu sein, dann war es immer nur ein einziges, ein gleiches Wort, das alle Eingeweihten beim Wiederbetreten der sinnlichen Welt sagten: 0 du mein Gott, wie herrlich hast du mich gemacht! Dies war die Empfindung, in die die Seele sich aushauchte nach der Ein­weihung, beim Wiederbetreten der gewöhnlichen sinnlichen Welt. Dies alles lebte in den Köpfen derjenigen, die die Einweihung zu leiten hatten. Später wurde, als das Schreiben",
      "nach und nach mehr Sitte wurde, auch manches auf­geschrieben. Es gab aber eine typische Beschreibung des Lebens eines Eingeweihten. Man sagte ungefähr: Derjenige, welcher eingeweiht, aufgenommen werden soll in die Kult­stätten der Einweihung, hat sein Leben so und so einzurich­ten, und er hat die Erfahrung zu machen, die schließlich mit den Worten: 0 du mein Gott, wie herrlich hast du mich gemacht, ihren Abschluß fand.",
      "Wenn Sie sich das Leben, wie es ein Eingeweihter durch­machen muß vor die Seele hinstellen können, so wie Sie sich das Leben eines Menschen vorstellen können, der in einem chemischen Laboratorium experimentieren will, dann wür­den Sie ein typisches Bild von dem Menschen, der sich höher entwickelt, bekommen. Dann würden Sie ein typisches Bild bekommen dessen, der auferweckt werden soll. Solche Ein­weihungsbücher hat es gegeben, oder sie haben wenigstens in den Köpfen derjenigen gelebt, die die Einweihung ge­leitet haben. Wenn wir verstehen, daß es solche Bücher gegeben hat, dann werden wir uns nicht mehr wundern, wenn wir die verschiedensten Eingeweihten der verschie­denen Völker in ähnlicher Weise beschrieben finden. Darin liegt ein großes Geheimnis, darin ruht ein wunderbares Mysterium. Zu ihren Eingeweihten haben die Völker immer aufgesehen, soweit sie von ihnen gewußt haben. Was sie von ihnen erzählt haben, war nicht das, was der heutige Biograph von den großen Männern erzählt. Was sie er­zählten, war der geistige Lebensgang, den der Eingeweihte erlebte. So werden wir verstehen, warum - wenn wir den Lebensgang von Hermes, Buddha, Zarathustra, Moses und Christus verfolgen - wir bei diesen Gestalten zu einem ähnlichen Lebensbilde kommen. Und warum? Weil sie die­ses Leben leben mußten, wenn sie zum Eingeweihten werden wollten. Einfach das Lebensbild des Eingeweihten steht",
      "vor uns in dem Leben des Hermes, Zarathustra, und so weiter.",
      "In dem, was die äußere Struktur der Lebensbeschreibung ist, können wir überall das Bild des Eingeweihten sehen, und von hier aus können wir uns die Frage beantworten: Wer waren diejenigen, welche die Evangelien geschrieben haben? Sie finden auf diese Frage eine geisteswissenschaft­liche Antwort in meinem Buche «Das Christentum als my­stische Tatsache».",
      "Was ich hier nur mit kurzen Worten an­deuten kann, finden Sie dort ausführlich dargelegt, und damit auch hingewiesen auf die geistige Glaubwürdigkeit der Evangelien. Es ist dargelegt, daß das, was in den Evan­gelien steht, alten Einweihungsbüchern entnommen ist.",
      "Na­türlich unterschieden sich die Bücher, welche Eingeweihte über diese Dinge schrieben, durch Nebensächliches. In der Hauptsache aber kam der Inhalt immer auf dasselbe hin­aus. Nur müssen wir uns klarmachen, daß die, welche die Evangelien geschrieben haben, nichts anderes hatten als solche alten Einweihungsbücher.",
      "Wenn wir dann das wirk­lich Darinstehende ansehen, dann können wir in den ver­schiedenen Evangelien verschiedene Formen der Initiation oder Einweihung erblicken. Und warum unterscheiden sie sich? Weil ihre Schreiber die Einweihung von verschiedenen Orten her kannten.",
      "Verstehen werden wir dies, wenn wir das Verhältnis der Männer, die die Evangelien verfaßt haben, zum Christus Jesus ansehen. Wir erlangen die beste Vorstellung, wenn wir uns an die schönen Worte erinnern, mit denen die Apokalypse beginnt.",
      "Der, welcher die Schrift des Johannes diktierte, wird genannt: das Erste und das Letzte, das Alpha und das Omega. Nichts anderes ist damit gemeint, als dasjenige, was - trotzdem die Zeiten und For­men der Welt sich wandeln von Menschengeschlecht zu Men­schengeschlecht, von Menschenrasse zu Menschenrasse, von",
      "Planet zu Planet - als eine einheitliche, geistige Wesenheit immer vorhanden bleibt. Wenn wir dies immer vorhandenbleibende Wesen als das Göttliche bezeichnen und sehen, daß wir einen Funken davon in uns haben, so fühlen wir uns mit diesem Alpha und Omega verwandt, ja wir fühlen dieses als das letzte Ideal, zu dem sich das sich Entwickelnde immer mehr hinaufhebt. So wurde uns dieses Ewige in allen Zeiten, dieses Dauernde in allem Wechsel vorgeführt.",
      "Nun müssen wir uns an den Sprachgebrauch erinnern, der ganz aus unserem Bewußtsein verschwunden ist. Ich möchte Ihnen das, worum es sich handelt, mit ein paar Worten vorführen. Heute ist der Name, den wir dem Men­schen geben, mehr oder weniger gleichgültig. Wir fühlen keinen rechten Zusammenhang zwischen dem Menschen und seinem Namen. Je weiter zurück man geht, desto be­deutungsvoller und wesentlicher wird der Name, man legte Wert auf gewisse Gesetze, durch die der Mensch einen Na­men bekommt. Ich brauche nur zu erinnern, daß es nicht sehr lange her ist, als noch die Gepflogenheit bestand, daß man in den Kalender schaute und dem neugeborenen Kinde den Namen gegeben hat, der am Tage seiner Geburt im Kalender stand. Man nahm an, daß das Kind sich hingedrängt fühlte zur Geburt an dem Tage, der diesen Namen trug. Derjenige, welcher die Einweihung durchgemacht hat, die ich beschrieben habe, hat einen neuen Namen erhalten, den Einweihungsnamen, und dieser bezeichnete seine innere Wesenheit, bezeichnete das, was er bedeutet in der Welt, das als was ihn der Führer erkannte. Dieser Name war mit seinem Wesen verknüpft und drückte das aus, was nur die innere Wesenheit angeht.",
      "Nun erinnern Sie sich, daß in der Bibel, im Neuen Testa­mente, die mannigfaltigsten Aussprüche Jesu angeführt werden. Derjenige nur dringt tiefer in diese Schriften ein,",
      "der vom Gesichtspunkte des Eingeweihten an dieselben herangeht und der von der Namengebung auch etwas ver­steht. Man bezeichnete zum Beispiel jemanden, wenn man ihn geistig bezeichnen und ausdrücken wollte, daß er noch auf niederer Stufe steht, mit einem Ausdrucke, der hergenommen war von den Eigenschaften des Astralleibes; wenn er höher stand, mit Ausdrücken, die hergenommen waren von Eigenschaften des Ätherleibes. Wollte man das Typische ausdrücken, dann nahm man Ausdrücke, die von Eigenschaften des physischen Leibes hergenommen sind. So hatten die alten Namen eine Beziehung zu den Men­schen und drückten so recht eigentlich das Wesen aus. Er­innern wir uns jetzt, wie oft in den Evangelien Worte des Jesus vorkommen, wo er sich als etwas Bestimmtes be­zeichnet - namentlich im Johannes-Evangelium können Sie solches finden. Wir können sie vielfach zurückführen auf ein Wort, auf das Wörtchen Ich. Erinnern Sie sich an das, was ich schon öfter in diesen Vorträgen ausgeführt habe:",
      "Man unterscheidet vier Glieder der menschlichen Wesen­heit: physischer Leib, Ätherleib, Astralleib und Ich. Dieses Ich wird immer größer und größer, dieses Ich ist so, daß es sich zur Einweihung hinaufentwickelt, dieses Ich ist un­vollkommen beim wenig entwickelten Menschen, gewaltig und vollkommen beim Eingeweihten. Wenn nun Christus im Johannes-Evangelium oftmals hindeutet darauf, daß er identisch sei mit dem «Ich-bin», wenn er sich bezeichnet als denjenigen, der da eins ist mit der tiefsten Wesenheit des Menschen in dem Satze «Ich und der Vater sind eins», wenn Sie das nehmen, so werden Sie es nun verstehen können von dieser Namengebung aus, weil er das Ewige in sich schließt, nicht weil er ein gewöhnlicher Mensch war und er mit die­sem Ich den gewöhnlichen Menschen bezeichnete, sondern weil er etwas war, das über den gewöhnlichen Menschen",
      "hinausging, weil er Christus, das Alpha und Omega war. So sahen die, welche in jener Zeit lebten, in ihm ein gött­liches Wesen, das den physischen Leib trug, ein Wesen, für das ebenso gleichgültig ist der physische Leib und ebenso wichtig das Geistige, wie für den physischen Menschen der physische Leib höchst bedeutsam und unwichtig das Gei­stige ist.",
      "Das Hervorstechende beim Menschen wurde sein Name, und wenn wir dieses noch weiter bedenken, dann verstehen wir noch etwas anderes - Sie werden von da den Weg finden in manches Mysterium der Bibel -, wir ver­stehen, was es zu bedeuten hat, als Moses dem Jehova ge­genüberstand und Jehova ihn zum Gesandten für das Volk machen will und Moses erwiderte: Was soll ich ihnen sagen, wer mich gesandt hat? - Und wir hören die bedeutungsvol­len Worte: Sage, der «Ich-bin» hat dich gesandt. - Auf welche Wesenheit deutet hier Jehova selbst hin? Auf das, was im wesentlichen im tiefsten Inneren jeder Menschen­wesenheit liegt.",
      "Gelangen wir an das vierte Glied der menschlichen Wesenheit, so sehen wir, daß das Ich ein Name ist, den wir uns selbst geben müssen. Das Göttliche muß selbst sprechen, das Göttliche, das an einem Punkte zu sprechen be­ginnt, das als kleiner, unbedeutender Keim im Menschen lebt und zu unendlicher Größe entwickelt werden kann.",
      "Das ist es, was gemeint ist, was dem Moses den Auftrag gab und sagte: Sage ihnen, «Der Ich-bin» hat dich gesandt. Das, was wie ein göttlicher Keim in jeder menschlichen Seele liegt, das, was im physischen, Äther- und Astralleib eingehüllt ist wie ein Punkt, zu dem wir «Ich-bin» sagen, das, was noch un­bedeutend über sie emporwädist und was noch unbedeu­tend in uns emporlebt, werden wir nicht als das Geringe in unserer Wesenheit bezeichnen, sondern als das Wich­tigste.",
      "Das Wesentliche ist es, das im Menschen lebt und das den Moses schicken will, indem es sagt: «Ich bin der Ich-bin.»",
      "So sehen Sie, welch tiefer Sinn in solcher Namengebung steckt, und wenn hingedeutet wurde auf dieses «Ich bin», dann wurde zu gleicher Zeit auch immer hingedeutet auf denjenigen Punkt in der Menschheitsentwicklung, den ich auch schon in diesen Vorträgen erwähnt habe und der auch in der Bibel angedeutet wird, nämlich den Punkt, wo der physische Mensch beseelt wird. Öfter habe ich schon aus­einandergesetzt, wie das, was heute der physische Mensch ist, sich von niederen Stufen heraufentwickelt hat, wie er sich dadurch, daß er mit einer Seele, die von der Gottheit herunterstieg, begabt wurde, sich weiterentwickeln konnte.",
      "Was aus dem Schoße der Gottheit herunterstieg, hat sich hineingesenkt in den physischen Leib und hat den physi­schen Leib weiterentwickelt. Dieser Moment ist auch in der Bibel angedeutet. Sie lehrt ihn mit ein paar Worten.",
      "Vor jenem Momente, der sich in Wirklichkeit über lange Zeit räume erstreckt hat hatte jener menschliche Korper nicht das, was man brauchte, um das Ich zur Entfaltung zu brin­gen, nicht das, was man als physischer Mensch auch heute notwendig gebraucht. In jener Zeit atmeten die Menschenvorfahren noch nicht durch Lungen, in jener Zeit entwickelte der Mensch aus einem schwimmblasenartigen Organ heraus seine Lunge.",
      "Er lernte da erst die Lungenluftatmung, und von diesem Vorgange ab gab es erst die Beseelung des menschlichen Körpers. Denken Sie sich diesen Vorgang zusammengedrängt in einen Satz, so haben Sie das biblische Wort: Und Gott blies dem Menschen den Odem ein und er ward eine lebendige Seele.",
      "Dadurch, daß der Mensch als physisches Wesen atmen lernte, war er be­fähigt, die Seele aufzunehmen. Gehen wir auf die Bedeu­tung des Jehovah-Namens zurück, dann finden wir, daß Jehovah soviel heißt wie «Wehen», daß die Luft dahinweht.",
      "Es ist im Worte Jahve nichts anderes ausgedrückt als",
      "der wehende Atem, mit dem der Ichgeist in den Menschen einzieht. So wird in diesem Namen dargestellt, wie der wehende Atem seine Wesenheit in dem Satze ausdrückt:",
      "«Ich bin der Ich-bin», der einen Teil seiner Wesenheit hineingießt in den Menschen. Es wird uns ein wahrer Weltenvorgang da vorgeführt. So wird uns zur wahren Tatsache jenes Ewige, das in der Menschennatur lebt. Ob wir den Menschen von heute oder den Menschen vor tau­senden von Jahren nehmen, das Ichwesen war da vor allen Zeiten. Denken Sie sich das Ichwesen in seiner höchsten Offenbarung, wo alles Äußere unwesentlich ist, denken Sie sich, daß ein Mensch das Innerste so groß und gewaltig er­kennt, dann haben Sie die Vorstellung, die sich die alten Christus-Anhänger von dem Christus machten. Was da in den ältesten Zeiten nur als Funke lebte, in höchster Glorie lebte es in Jesus von Nazareth. Er war, weil er der höchste Göttliche war, der höchste Eingeweihte, daher das Wort:",
      "«Ehe denn Abraham ward, bin Ich.» Er ist in körperlicher Gestalt dasjenige, was da ist, ehe Abraham war, was da ist, ehe Abraham, Isaak und Jakob waren, er ist das, was als das größte Mensdiheitsideal vor dem steht, der sich ent­wickeln will, vor dem, der die Worte der Bergpredigt be­folgt: «Selig sind diejenigen, die da sind Bettler im Geist, denn sie werden in sich finden die Reiche der Himmel.» Nehmen wir dieses Wort so, dann haben Sie die Vor­stellung, die sich die Christus-Anhänger damals machten. Was konnten sie von diesem höchsten inkarnierten Gott für eine Lebensbeschreibung geben? Wo war eine Lebens­beschreibung, die seiner würdig war? Das war die Lebens­beschreibung, die man im Einweihungskanon gab, demjeni­gen Kanon, der die Regeln enthielt, nach denen der Ein­zuweihende initiiert werden sollte. Wie man sieht, war es so: Willst du eingeweiht werden, dann hast du von Lebensstufe",
      "zu Lebensstufe das und das durchzumachen bis zur höchsten Stufe, die angedeutet ist mit den Worten: Mein Gott, mein Gott, wie hast du mich verherrlicht! . . . (Hier bricht die Nachschrift ab.)"
    ],
    "sentences": [
      [
        "Wir haben gestern versucht, uns den Sinn vor die Seele hinzurücken, durch den dasjenige, was wir Geisteswissenschaft nennen, sich den religiösen Urkunden annähern will.",
        "Wir wollen heute versuchen, wenigstens in einigen Bei­spielen tiefer in diejenige religiöse Urkunde, die der gegen­wärtigen Kulturmenschheit doch wohl noch am nächsten liegt, in die Bibel, einzudringen.",
        "Vom Standpunkte der Geisteswissenschaft kommt man am leichtesten in die Bibel hinein, wenn man zunächst versucht, von dem Neuen Testa­ment, von den Evangelien auszugehen.",
        "Nachdem wir ge­stern auseinandergesetzt haben, wie wir die sogenannte Kritik, den kritischen Geist auffassen sollen, wie wir uns zu der Niederschrift der verschiedenen einzelnen Teile des Neuen Testamentes und zu der Schriftensammlung des Alten Testamentes vom Standpunkte der Geisteswissen­schaft stellen können, wollen wir heute mehr das Positive ins Auge fassen, voraussetzen, was gestern gesagt worden ist und ohne jede Befangenheit vom geisteswissenschaft­lichen Standpunkt in diese Sache hineinleuchten."
      ],
      [
        "Sie wissen, daß dem Menschen, wenn er aus dem Bedürf­nisse des christlich-gläubigen Herzens heraus an die vier Evangelien herangeht, zunächst eigentümliche Widersprüche begegnen können, welche sich aus den vier Evangelien, die man nach Matthäus, nach Markus, nach Lukas, nach Jo­hannes nennt, ergeben.",
        "Derjenige, der sich heute wenn auch noch so gläubig zu diesen Büchern verhält, hat doch keine"
      ],
      [
        "richtige Vorstellung davon, in welchem Verhältnisse in alten, viel religiöseren Zeiten der Gläubige der Bibel gegen­überstand, was das Wort «Bibel», respektive der Aus­druck «das Wort Gottes» eigentlich für die alten Gläubigen bedeutete.",
        "Wir brauchen uns nur an das Wort« Inspiration» zu erinnern und daß durch Jahrhunderte hindurch die gläubigen Gemüter festgehalten haben daran, daß jene, welche die religiösen Urkunden niedergeschrieben haben, inspiriert waren, daß sie unter dem unmittelbaren Einflusse des göttlichen Geistes selbst geschrieben haben.",
        "Und so wahr sie den Glauben hatten, daß von diesem göttlichen Geiste nur die Wahrheit ausgehen konnte, so wahr erschien ihnen jedes Wort, das in der Bibel stand, als heilig.",
        "Die Bibel war ihnen der Ausdruck für die gewaltigen Welt­rätsel, die sich vor die Seele des Menschen hindrängten.",
        "Wie hätte ein Mensch, der sich vorstellte, daß die alten Gottesmänner Persönlichkeiten waren, die unmittelbar un­ter der Inspiration des göttlichen Geistes standen, glauben können, daß diese etwas geschrieben hätten, ja etwas hätten schreiben können, an das man Kritik anlegen muß.",
        "Dann hätte in den Herzen dieser Gläubigen nicht ein unmittel­bares Hängen an jeglichem Wort sein dürfen."
      ],
      [
        "Für den heutigen Menschen ist es schwer, sich in diese Gemütsstimmung hineinzuversetzen.",
        "Er liest das erste und er liest das dritte Evangelium.",
        "Es werden ihm zwei Ab­stammungstafeln des Jesus von Nazareth vorgeführt, die eine in dem Evangelium nach Matthäus die andere in dem Evangelium nach Lukas.",
        "Er verfolgt die Namen und findet, daß dieselben nicht übereinstimmen, daß schon beim drit­ten Glied von Joseph aufwärts ein anderer Name auftritt, daß, wo bei Matthäus Salomon steht, bei Lukas Nathan sich findet und so weiter, daß eine ganze Reihe von Namen in den Tafeln verschieden sind, und er frägt sich: Wie ist es"
      ],
      [
        "möglich, daß dasjenige, was durch Jahrhunderte hindurch den Menschen als ein Quell der Wahrheit gedient hat, solche Widersprüche aufweisen kann? - Im Grunde genom­men sehen wir in einer einzigen solchen Erwägung den Keimpunkt zu all den Zweifeln, die, hinsichtlich der Ein­heitlichkeit der Schrift und zuletzt bezüglich ihrer Inspira­tion, den Menschen, den Kritikern gekommen sind.",
        "Aus solchen Erwägungen heraus, die in komplizierter Weise bis ins feinste Detail durchgeführt worden sind, hat man die Bücher des Neuen Testamentes zerlegt, hat man gefunden, was mehr oder weniger echt ist, hat man gefunden, daß das erste Evangelium von dem vierten abweicht, woraus sich notwendig ergeben mußte, daß man es im vierten Evangelium mit etwas ganz anderem als mit einer histo­rischen Urkunde zu tun hat.",
        "Wie könnte man auch un­befangenen Geistes diese Widersprüche hinwegdekretieren?",
        "Es ist nur zu natürlich, daß der moderne Mensch, wenn er so etwas sieht, Kritik anlegen muß."
      ],
      [
        "Nun fragen wir uns aber, wie ist es möglich, daß durch Jahrhunderte, Jahrtausende hindurch wahrlich auch nicht gerade dumme Köpfe diese Bücher in der Hand gehabt haben und nicht auch zu einer Kritik, zu einem Sehen dieser Widersprüche gekommen sind?",
        "In bezug auf die große Menge der Gläubigen könnte man sich vielleicht darauf berufen und sagen, die Bibel ist bis in die neueste Zeit nur in den Händen einiger weniger gewesen; die Gläubigen haben sie vor der Erfindung der Buchdruckerkunst fast gar nicht in die Hand bekommen.",
        "Man kann sagen, die große Menge konnte gar nicht irre werden an etwas, was ihr von den leitenden Persönlichkeiten gar nicht vorgelegt wurde.",
        "Aber sollen wir uns vorstellen, daß diejenigen, welche die Bibel in die Hand bekommen haben, nicht gesehen hätten, was die heutige Kritik sagt?"
      ],
      [
        "Es wird von einzelnen Historikern eingewendet: lang­sam, durch die Gewalt der Kirche, habe sich das Ansehen dieser Bücher erst befestigt, nach und nach erst habe sich das herausgebildet, was man das Ehrfurchtsgebietende die­ser biblischen Geschichte nennt.",
        "Vor einer richtigen ge­schichtlichen Betrachtung kann der Inhalt der Bibel auch gar nicht bestehen.",
        "Wenn wir zurückgehen in die ersten christlichen Jahrhunderte und die Tatsachen prüfen, dann kommen wir zu dem Urteil, daß bei dem Konzil zu Nikäa festgestellt worden ist, welches die richtigen Evangelien sind, und daß durch Machtspruch dekretiert worden ist:"
      ],
      [
        "Das sind die heiligen Schriften."
      ],
      [
        "Vor einer unbefangenen geschichtlichen Betrachtung kann das nicht bestehen.",
        "Wir werden zu Persönlichkeiten ge­führt, die in den alten Zeiten des Christentums gelebt haben.",
        "Wir finden dann in ihren Mitteilungen, daß zum Beispiel im Jahre 160 n.",
        "Chr. eine sogenannte Evangelienharmonie gemacht wurde, das heißt eine Zusammenstellung der verschiedenen Evangelien, so daß sie ein einheitliches Bild geben sollten.",
        "Später ist dies noch öfters gemacht wor­den, und wir können finden, wenn wir die Evangelien vom zweiten Jahrhundert sorgfältig prüfen, daß auch dasjenige hineingearbeitet worden ist, was wir jetzt als Inhalt des Neuen Testamentes kennen.",
        "Wir können noch weiter zu­rückgehen, bis zu den ersten Kirchenvätern.",
        "Wenn wir ge­rade diese kritisch prüfen, so zeigt sich uns, wie sie mit ungeheurer Ehrfurcht von der Bibel sprechen, mit einer Ehrfurcht, die die Annahme zuläßt, daß sie geglaubt haben, die Bibel sei von höherer Geistigkeit inspiriert.",
        "Wir können bis zu Origines zurückgehen und bemerken dann, wie er in derselben Art und mit derselben Ehrfurcht von den bib­lischen Büchern spricht.",
        "Und wenn wir einzelne Worte neh­men, die sogar nur derjenige mitteilt, von dem nicht mit"
      ],
      [
        "Unrecht gesagt wird, daß er noch ein Hörer des Apostels Johannes gewesen sei, Matthäus, dann finden wir, daß aus seiner Seele etwas herausspricht, was wir in demselben Sinne zusammenfügen können mit dem, was später die Stimmung der Gläubigen, auch der gelehrtesten Gläubigen, gegenüber den Evangelien war."
      ],
      [
        "Freilich muß sich der Mensch, der so etwas betrachtet, etwas, ja sogar gründlich, frei machen können von gewissen Vorurteilen.",
        "So wie spätere Zeiten sich zu dem, was man Christentum nennt, gestellt haben, so haben sich diejenigen, die in den ersten Jahrhunderten als Gelehrte gelebt haben, nicht dazu gestellt.",
        "Und wenn heute jemand von irgend­einem orthodoxen Standpunkte aus zu einem kommt, der die Bibel nicht gerade so auffaßt, wie er, und zu ihm sagt, er sei ein Ungläubiger, er dürfe sich nicht Christ nennen, er verstoße gegen das rechte Wort der Bibel - so dürfen wir wohl an solche alten Gläubigen erinnern, an denen zu zweifeln auch die nicht wagen, welche sich die Bibel in willkürlicher Weise zurechtlegen.",
        "An ein Wort des Kirchenvaters Augu­stinus will ich mich anlehnen.",
        "Das Wort heißt: Dasjenige, was man heute christliche Religion nennt, ist uralt.",
        "Es ist die uralte wahre Religion, und das, was die uralte wahre Religion ist, das nennt man jetzt die christliche Religion."
      ],
      [
        "Man denke an ein solches Wort und stelle dann daneben, was insbesondere ein geisteswissenschaftlidier Erklärer der Bibel sehr häufig erfahren kann.",
        "Ist es nicht oftmals ge­radezu tragisch, wie gegnerische Stimmungen hervorgeru­fen werden, wie der Geisteswissenschafter bei Bekannten, Freunden und Verwandten herben Widerspruch findet, in­dem sie ihm sagen: da kommst du wieder mit deinen geistes-wissenschaftlichen Phrasen, wo bleibt denn da die Bibel?",
        "Einem solchen Ausspruche liegt eine tiefe Unkenntnis der wirklichen Bibel zugrunde und außerdem liegt darin eine"
      ],
      [
        "große Prätention, der Anspruch, mit seiner Auffassung der Bibel unfehlbar zu sein.",
        "Wenn sich nur solche Gläubige ganz klar darüber werden wollten, was es heißt, der geistes­wissenschaftlichen Auffassung der Bibel so gegenüberzutre­ten.",
        "Es heißt nichts anderes als: was ich in der Bibel finde, ist das unbedingt Richtige."
      ],
      [
        "Es ist ja nicht so, daß der geisteswissenschaftliche Stand­punkt sich etwa weniger positiv zur Bibel verhält, sondern so, daß er gerade die wirkliche Bedeutung, den wirklichen Sachverhalt aus dieser Bibel wiederum herausentwickeln will.",
        "Richtiges Verstehen ist es, um was es sich gegenüber den religiösen Urkunden für die geisteswissenschaftliche Weltanschauung handelt.",
        "Daher darf derjenige, welcher aus Bequemlichkeit bei irgendeiner anderen Ansicht steht, die gerade zufällig da ist, an die er sich gewöhnt hat, der geisteswissenschaftlichen Anschauung eigentlich nicht ent­gegentreten.",
        "Denn vielfach lebt in der Seele derjenigen, die einer wirklichen Erklärung der Bibel entgegentreten, etwas Gegnerisches, so daß sie sagen: Ihr verleugnet die Bibel, ihr macht euch und eure Familie unglücklich. - Vielfach steckt auch nichts anderes dahinter als der Gedanke: Ich will nicht lernen; ich weiß, was ich weiß."
      ],
      [
        "Lesen wir einem solchen Ausspruch gegenüber die Bergpredigt und verstehen wir sie richtig, dann werden wir uns nicht mehr, auch wenn wir uns Christen nennen, auf einen solchen Standpunkt stellen dürfen.",
        "Nur der erste Satz der Bergpredigt sei hier zitiert.",
        "Es ist, wie die, welche häufiger hierher kommen, wissen, öfter schon gesehen.",
        "Richtig deutsch wiedergegeben heißt er: «Selig sind, welche da sind Bettler im Geiste, denn sie werden in sich selbst finden die Reiche der Himmel.» Man kann das, was man geistes-wissenschaftliche Gesinnung nennt, nicht schöner ausdrük­ken, als es mit diesen Worten die Bergpredigt tut."
      ],
      [
        "Was heißt geisteswissenschaftliche Gesinnung?",
        "Es heißt nichts anderes als dasjenige, was in uns liegt, den tiefsten Kern unserer eigenen Wesenheit, die in uns lebendige, gei­stige Natur zur Entfaltung zu bringen."
      ],
      [
        "Ebenso wie das­jenige, was unseren Körper bildet, den Stoffen der um­liegenden Welt entnommen ist, so ist dasjenige, was in uns vorhanden ist, dem Geiste, der um uns lebt und zu allen Zeiten gelebt hat, entnommen.",
        "Und so wahr es ist, daß unser Körper nur ein Tropfen ist in dem Meere der mate­riellen Wirklichkeit, so wahr ist es, daß unsere Seele, unser Geist nur ein Tropfen ist in dem Meere des allumfassenden Weltengeistes."
      ],
      [
        "Aber so wie der Tropfen, der aus dem Meere genommen wird, seiner Substanz nach dasselbe ist wie das Wasser des ganzen Meeres, so ist dasjenige, was in des Menschen tiefster Seele lebt, substantiell gleich mit dem Wesen des Göttlichen.",
        "Weil der Gott im Menschen lebt, kann der Mensch Gott erkennen; weil der Mensch geistig ist, kann der Mensch, wenn er nur will, eindringen in die geistige Welt um ihn herum."
      ],
      [
        "Ein zweites gehört aber dazu, wenn der Mensch wirklich eindringen will in diese geistigen Welten, und dieses zweite, das dazu gehört, ist mit dem einfachen Wort gegeben: Niemals stehenbleiben!",
        "Man darf eine Entwicklung nicht bloß glauben, sondern man muß die Entwicklung leben."
      ],
      [
        "Was heißt es, eine Entwicklung leben?",
        "Nichts anderes, als das Bewußtsein in sich tragen, daß der Mensch sich aus einem unvollkommenen Zustande zu seinem jetzigen entwickelt hat, und daß er sich in die Zukunft hinein jederzeit weiter entwickeln kann."
      ],
      [
        "Zunächst denken wir nicht daran, daß des Menschen äußere Gestalt sich in dieser Entwicklung umändert, sondern daran, daß die Menschenseele von Stufe zu Stufe hinaufklimmen kann; daß es ein Aufwärtsschreiten dieser Seele gibt, daß es mög­lich ist, von Tag zu Tag vollkommener zu werden.",
        "Heute"
      ],
      [
        "lernen wir etwas, unsere Seelenkräfte sind imstande, dies oder jenes einzusehen, unser Wille ist imstande, dies oder jenes zu tun.",
        "Bleiben wir stehen bei dem, was wir heute einsehen, bei dem, was unser Wille heute zu tun imstande ist, dann entwickeln wir uns nicht.",
        "Tragen wir aber das Bewußtsein in uns, daß außer den Kräften, die sich in uns schon entwickelt haben, auch noch andere Kräfte in uns schlummern - so schlummern, wie der Pflanzenkeim, der sich zur Pflanze entwickelt hat, andere Pflanzenkeime in sich schlummernd trägt -, dann werden wir jeden Tag mehr erkennen, daß wir durch eine höhere Entfaltung des Willens aus unserer Seele die geistigen Augen und Ohren herausholen können, und sehen, daß es mit jedem Tag besser werden kann.",
        "Dies dürfen wir nicht im trivialen Sinne verstehen, sondern so, daß diese Entwicklung in geistig-seelischer Richtung eine universelle Bedeutung hat."
      ],
      [
        "Wenn wir in der materiellen Welt tierische Gestalten sich körperlich zu einer edlen Menschenform entwickeln sehen, so berechtigt das nicht zu der Annahme, daß der Mensch sich aus den Tieren herausentwickelt habe, auch wenn die Naturwissenschaft festgestellt hat, daß in bezug auf die physische Gestalt des Menschen eine größere Ähn­lichkeit zwischen den niedrigstentwickelten Menschen und den höchstentwickelten Affen, als zwischen den niederen Affen und den höchsten Affenarten bestehe.",
        "Von diesem Verhältnis leitet ja die Naturwissenschaft die Verwandt­schaft des Menschen mit dem Affen ab.",
        "Dies hat im Jahre 1859 wie eine große Ketzerei der große Naturforscher Huxley ausgesprochen.",
        "Ein großer Teil dessen, was Sie in Haeckels Schriften lesen, ist unter dem unmittelbaren Ge­mütseindruck dieses Satzes geschrieben.",
        "Derjenige, der an die geistige Entwicklung glaubt, sagt sich: Wohlan, zu­gegeben, daß der Mensch in bezug auf seine äußere Form,"
      ],
      [
        "seine Körperlichkeit dem höchstentwickelten Affen näher steht als dieser dem niedrigsten seiner eigenen Gattung, aber ebenso wahr ist es auch, daß derjenige, der eine be­stimmte Stufe der Geistigkeit erreicht hat, dem auf niede­ren Stufen der Menschheit Stehenden ferner steht als der niedrigste Mensch dem höchstentwickelten Tiere."
      ],
      [
        "Verfolgen wir den Faden der Entwicklung in die höhe­ren Gebiete, so sehen wir ihn sich in geistige Gebiete hinein fortsetzen, und in dem Geistigen sehen wir die von der Geisteswissenschaft geschilderte Entwicklung als etwas ebenso Wirkliches, wie es für die sinnlichen Augen die materielle Entwicklung ist.",
        "Theosophie hat es zu allen Zeiten gegeben.",
        "Schon . . . sagt, daß das alte indische Atma Vidya dasselbe ist, daß es aber zu den verschiedenen Zei­ten mit den verschiedensten Namen benannt wurde.",
        "Die heutige Naturforschung anerkennt eine Entwicklung von den niederen tierischen Formen bis zum Menschen.",
        "Dagegen sagte die Theosophie zu allen Zeiten: wir erkennen auch eine solche Entwicklung an, wir stehen durchaus auf dem Boden solcher Entwicklung, wir erkennen an, daß es einen gewaltigen Unterschied gibt zwischen der vollkommenen Gestalt des Menschen und einem niederen Tiere, das im Meerschlamme lebt und kaum dem mit dem Mikroskop bewaffneten Auge sichtbar ist.",
        "Durch wie viele Zwischen­stufen muß der Mensch hindurdischreiten, wenn er vom Unvollkommenen zum Vollkommenen vorrückt!",
        "Als ebenso wirklich und real sieht der Geisteswissenschafler die Ent­wicklung der Seele und des Geistes an.",
        "Er sieht ebenso große Unterschiede zwischen solchen Individualitäten, die Eingeweihte geworden sind, die in einem höheren Grade die in der Seele eines jeden Menschen liegenden Eigenschaf­ten zu göttlichem Schauen gebrauchen, und demjenigen Menschen, der kaum die ersten Keime der Seelentätigkeit"
      ],
      [
        "entwickelt hat.",
        "Der Unterschied in der Entwicklung vom Unvollkommensten der niedrigsten Seelenstufe bis zu dem vollkommenen Eingeweihten ist größer als der zwischen dem kleinsten Lebewesen und dem vollkommensten Kör­per des Menschen.",
        "Wer weiß, daß es Eingeweihte gibt, die tief hineinschauen können in die Entwicklung der materiel­len Dinge, der weiß, daß es auch geistige Entwicklung gibt."
      ],
      [
        "Wer das weiß, der weiß auch, daß die Stimmung keine andere sein kann, als daß er sich sagt: ich sehe hinauf zu den göttlichen Idealen, zu denen ich den Keim in der Seele trage; ich weiß, daß in der Zukunft sich etwas herausentwickelt haben wird, was heute noch in mir schlummert, nur schwach veranlagt ist.",
        "Ich weiß aber auch, daß ich alle Kräfte anwenden muß, um zu diesen Höhen hinaufzukom­men.",
        "Als ein Bettler im Geiste kommt sich dann der vor, welcher so die geistige Welt ansieht.",
        "Und der ist «beseligt», das heißt selig fühlt er sich dann.",
        "Und wir haben in der Bergpredigt im geisteswissenschaftlichen Sinne ein so wun­derbares Wort das da heißt: «Selig sind die, die da Bettler sind im Geiste, denn sie werden in sich selbst finden die Reiche der Himmel.» - Keiner, der den Sprachgebrauch der alten Zeiten kennt, wird wähnen, daß diejenigen, welche vom Himmel sprechen, einen Himmel im unbekannten Jenseits meinten.",
        "Man stellte sich vor, daß überall da, wo man ist, auch der Himmel ist.",
        "Wo wir jetzt sind, da ist der Himmel, da ist die geistige Welt.",
        "Ebenso wie der Blinde, wenn er operiert wird, den Raum, den er vorher nur tasten konnte, mit Farben erfüllt sieht, so sieht der, dessen gei­stiger Sinn geöffnet ist, eine neue Welt um sich.",
        "Er sieht, was immer um ihn herum ist, in neuer Gestalt, in der Ge­stalt, in der er sehen muß, wenn er sich zu höherer Mensch­lichkeit hinaufentwickeln will.",
        "Er braucht nicht zu glauben, daß anderswo, an einem anderen Orte oder zu anderer"
      ],
      [
        "Zeit der Himmel sei.",
        "Ihm gilt das Wort des Christus: Das Himmelreich ist mitten unter euch."
      ],
      [
        "Das Himmelreich ist da, wo wir sind, es durchdringt alle körperlichen Dinge.",
        "Wie das Wasser das Eis durch­dringt, so schwimmt gleichsam im Meere des göttlichen Geistes dasjenige, was sich aus diesem Geist als körperlich materielle Welt verdichtet hat.",
        "Alles Körperliche ist ver­dichtetes, verwandeltes Geistiges.",
        "Hinter allem Körper­lichen steht das Geistige.",
        "Hier werden wir schon zu dem­jenigen geführt, was in bezug auf geisteswissenschaftliche Auffassung das Verhältnis des Menschen zur Entwicklung ist.",
        "Ebenso wie draußen in der tierischen Welt Vollkomme­nes und Unvollkommenes lebt, so leben in bezug auf das Geistige die verschiedensten Individualitäten: die einen fortgeschritten, die anderen zurückgeblieben, die einen hin-einsehend in Gebiete, wohin die moderne Wissenschaft noch leuchtet, die anderen hineinsehend in die tiefsten Unter­gründe der menschlichen Erkenntnis, vom Wilden bis zu dem zur Göttlichkeit entwickelten Menschen, der befähigt ist, draußen in der Welt das Geistige um sich zu schauen.",
        "Alle diese Zwischenstufen glaubten nicht nur, sondern kannten diejenigen, welche Eingeweihte waren.",
        "Und wenn man von Eingeweihten sprach, so sprach man von ihnen als von solchen, die mehr wissen als die sie umgebende Menschheit.",
        "Immer hat man von solchen Eingeweihten ge­sprochen, und nun wollen wir uns einmal klarmachen, in welchem Sinne man von den in die geistigen Welten Ein­geweihten gesprochen hat."
      ],
      [
        "Wie schon oft hier auseinandergesetzt worden ist, finden wir, wenn wir in uralte Zeiten zurückgehen, daß auch das Alltagsbewußtsein anders war als heute, daß ein mehr hellseherisches Bewußtsein vorhanden war.",
        "Hellseherisch wird es nicht genannt, weil es etwa klarer wäre als das"
      ],
      [
        "Tagesbewußtsein, sondern weil es gleichsam durch die Ge­genstände hindurch bis in die Seele hinein sieht, aber es ist ein dumpfes, dämmerhaftes Bewußtsein, dessen Überreste sich im nächtlichen Traumbewußtsein des Menschen er­halten haben.",
        "Aus ihm hat sich das heutige taghelle Be­wußtsein der Menschheit entwickelt."
      ],
      [
        "Wenn wir zurück­blicken in jene alten Zeiten, wo die große Masse der Menschen in diesem heilseherischen Bewußtsein lebte, so finden wir, daß es auch da schon Eingeweihte gab.",
        "Wodurch unterscheiden sich nun jene alten Eingeweihten von den­jenigen, die noch in einem mehr dämmerhaften Bewußtsein um sie herum waren?"
      ],
      [
        "Sie unterscheiden sich dadurch, daß sie schon etwas wußten von dem Bewußtsein, das die Menschheit bekommen sollte und heute hat, dadurch, daß sie imstande waren, von der Zukunft etwas vorauszuneh­men, in der Art in die Welt hineinzuschauen, wie die ganze Menschheit in späterer Zeit es erlangt hat.",
        "Es war diejenige Art, welche mit den Augen und Ohren des Leibes wahr­nimmt, mit denjenigen Organen, mit denen der Mensch sinnlich untersucht und verstandesmäßig begreift."
      ],
      [
        "Wie das heute bei den Menschen im allgemeinen wohl der Fall ist, so war es auch schon bei einzelnen eingeweihten Menschen der Vorzeit.",
        "Sie waren eben deshalb Eingeweihte.",
        "Der Ein­geweihte nimmt etwas von der Zukunft voraus."
      ],
      [
        "Ebenso trägt der Eingeweihte unserer Tage etwas von dem erhöh­ten Hellsehen, von dem erhöhten Schauen, das die Mensch­heit in Zukunft haben wird, in sich.",
        "Er weiß etwas zu sagen von dem, was die jetzige Menschheit in Zukunft haben wird."
      ],
      [
        "So blickten die Alten, die etwas von diesen Dingen ver­standen haben, hinauf zu dem Eingeweihten.",
        "Sie sagten sich: Wie er die Dinge ansieht, so werden in Zukunft die Menschen die Dinge auch ansehen.",
        "Sehen wir uns ihn an, er"
      ],
      [
        "ist das lebendige Ideal, er ist derjenige, der uns durch seine Gestalt erkennbar macht, was wir sein werden. - In diesem Sinne war er ihnen ein Prophet, und wenn er noch höher stand, ein Messias.",
        "Und so sagten sie sich, der Verlauf der Geschichte wird so sein, daß er die große Zahl der Menschen zu dem, was er erreicht hat hinführen wird."
      ],
      [
        "Einen «Erst­geborenen» nannten sie einen solchen.",
        "Derjenige aber, wel­cher in solcher Weise eingeweiht werden sollte, hatte durch verschiedene Stufen hindurchzugehen.",
        "Es gibt durch die verschiedenen Stufen bis zu den höchsten Einweihungsstufen hinauf die mannigfaltigsten Erkenntnis- und Wil­lensgrade."
      ],
      [
        "Durch viele Stufen kann man durchschreiten.",
        "Wie die Pflanze bei ihrer Entwicklung die verschiedenen Stufen durchmacht, von der Wurzel zu Blatt, Blüte und Frucht, so schreitet der Mensch hinauf von Einsicht zu Ein­sicht, bis er vom Schüler zum Eingeweihten selber wird."
      ],
      [
        "Dieser Fortschritt geschieht durch Schulung, und diese Schulung kann man sich aneignen.",
        "Derjenige, welcher leugnet, daß es eine solche Schulung gibt, durch die er zu einer höheren Art des Anschauens, zu der Eröffnung von Augen und Ohren des Geistes gelangen kann, der weiß es eben nicht, der hat noch keine Kunde erhalten von solcher Schulung."
      ],
      [
        "Das ist die Aufgabe der Geisteswissenschaft: der Menschheit zu sagen, daß es eine solche Schulung der Auf­wärtsentwicklung gibt.",
        "In meiner Zeitschrift «Luzifer-Gnosis» können Sie lesen, daß jetzt in viel tieferer Weise von dem Prinzip der Einweihung und der geistigen Kultur gesprochen werden kann."
      ],
      [
        "Die mannigfaltigsten Gründe sprechen dafür.",
        "Einen Grund möchte ich aber anführen."
      ],
      [
        "Gerade das ist das Tragische, das so Bedrückende, die Seele Zermarternde für den modernen Menschen, daß er an die alten Urkunden nicht mehr glauben kann, daß ihm dieselben nicht mehr Verkörperungen des Wortes Gottes"
      ],
      [
        "sein können, weil die Entwicklung von Verstand und Ver­nunft zu weit vorgerückt ist, so daß er die alte Botschaft nicht mehr brauchen kann.",
        "Er braucht aber eine neue Bot­schaft, und diese will ihm die Geisteswissenschaft bringen.",
        "Wir haben gleichsam im Bilde in die Zukunft hin eingesehen, und heute noch sieht derjenige, welcher sich zum Ein­geweihten entwickelt, die Entwicklung der Menschheit in der Zukunft.",
        "Er muß sich aber nach bestimmten Methoden entwickeln.",
        "Ebenso wie die Methoden, durch die man astro­nomische Wahrheiten erfährt, ganz bestimmte sind, so sind die Methoden, durch die man in die höhere Geistigkeit hinaufrückt, auch ganz bestimmte.",
        "Niemand darf sich sagen, daß er auf eigene Faust in die höheren Gebiete hinauf­steigen soll.",
        "Das ist so, wie wenn man auf eigene Faust Mathematik studieren und nichts auf Autorität hin an­nehmen wollte.",
        "Man braucht aber einen Leiter und Führer, der einem die Wege zeigt.",
        "Keine andere Autorität gibt es mehr auf diesem Gebiete.",
        "Daher ist es nur Rederei, wenn das Prinzip des gläubigen Hinneigens und Bekennens auf die Geisteswissenschaft angewendet wird.",
        "Es ist ein Miß­verständnis, wenn in der Geisteswissenschaft von Autorität und Gläubigkeit gesprochen wird."
      ],
      [
        "Nun gab es in den verschiedenen Jahrtausenden immer Bücher - eigentlich nicht Bücher, sondern mehr eine münd­liche Tradition, wenn wir in die alten Zeiten zurückgehen, und diese mündliche Tradition umfaßte die Regeln, wie man eingeweiht wird.",
        "Wollen wir uns einen Begriff von dem machen, wie solche Tradition war, wie solche Vor­schriften waren, die zeigten, was der Mensch zu tun hat, wenn er anfängt sich zu vergeistigen, bis zu den höchsten Einweihungsstufen, so brauchen wir nur daran zu denken, daß bei denen, die als Führer und Leiter wirkten, nichts niedergeschrieben werden durfte.",
        "Diese Regeln dürfen auch"
      ],
      [
        "heute noch nicht niedergeschrieben, sondern nur mündlich denjenigen übertragen werden, die dazu würdig sind.",
        "Es gab einen Einweihungskanon.",
        "Er enthielt die Regeln der Geburt des Geistesmenschen; er zeigte die Regeln, die der Mensch erfüllen muß, um zu den hohen Zielen zu kommen.",
        "Wer sich dem geistigen Streben widmete, der mußte von einer Stufe der Übungs- und Lebensweise zur anderen, höheren geführt werden.",
        "Bist du auf der höheren Stufe, dann kommt der Eingeweihte und zeigt dir die höheren Geheimnisse."
      ],
      [
        "Nur noch ein Wort über die Art und Weise, wie ein solcher Einweihungskodex gehandhabt worden ist.",
        "Das ist heute nicht mehr so üblich wie in alten Zeiten.",
        "Die Einweihungsprozesse schreiten auch vorwärts.",
        "Der Schüler wurde in alten Zeiten in eine Art Ekstase gebracht.",
        "Das Wort hatte damals eine andere Bedeutung als heute, es bedeutete nicht Außer-sich-Sein, sondern ein Bewußtwerden in höheren Be­wußtseinszuständen und dahin hatte der geistige Führer den Schüler geführt.",
        "Es war vorgeschrieben, wie lange man in solchem Bewußtseinszustande gehalten werden mußte; es waren dreieinhalb Tage.",
        "Heute ist es nicht mehr so, daß das Bewußtsein herabgedämpft wird.",
        "Damals aber war der Betreffende in Ekstase und Entrückung, da wußte er nicht, was um ihn herum in der Sinnenwelt vorging, da war der Einzuweihende auf dem Gebiete der sinnlichen Welt wie einer, der schläft.",
        "Er wurde also hingeführt zu einem Be­wußtseinszustand, in dem die äußere Sinnenwelt schwand.",
        "Aber was er erlebte, unterschied sich beträchtlich von dem, was der heutige Mensch erlebt, wenn beim Einschlafen die äußeren sinnlichen Gegenstände um ihn herum verschwin­den.",
        "Die äußeren sinnlichen Dinge verschwanden, aber der Mensch lebte in einer Welt des Geistes; licht wurde es um ihn herum.",
        "Das, was man Astrallidit nennt, ging ihm auf:"
      ],
      [
        "ein Licht, das ein anderes Licht ist als das physische, das uns erscheint wie ein Meer von geistiger Substanz, in dem geistige Wesenheiten eingebettet sind und aus dem sie sich herausentwickeln.",
        "Und wenn er noch höher stieg, hörte er aus dieser Welt erklingen, was in den alten pythagoräischen Schulen die Sphärenharmonie genannt wird.",
        "Dasjenige, was der Verstand als Weltgesetz in Begriffen erkennt, das nimmt der, welcher auf solcher Stufe sich befindet, wie eine Art Klang, wie geistige Musik wahr.",
        "Die geistigen Kräfte äußern sich in Harmonie und Rhythmus.",
        "Es ist aber dabei nicht an die äußere Musik zu denken.",
        "Die geistige Welt, die Welt der Himmel klingt und tönt für das astrale Licht.",
        "In diese Welt wurde der Einzuweihende eingeführt.",
        "Da lernte er die Stufen der menschlichen Göttlichkeit kennen, die die Menschheit erst in fernen Zeiten erklimmen wird.",
        "Das alles wurde für ihn Wahrheit, das durchlebte er in dreieinhalb Tagen."
      ],
      [
        "Unzählige Menschen haben in der Welt gelebt und leben noch, die wissen, daß das, was dem Menschen heute grotesk erscheint, ebenso eine Welt der Wirklichkeit ist, wie die, welche das äußere Ohr und das äußere Auge wahrnehmen kann.",
        "Wenn dann der Betreffende nach dreieinhalb Tagen wieder in die Sinnenwelt zurückgeführt war, wenn er be­reichert mit dem Wissen vom geistigen Leben wieder ein­ging in diese Welt, wenn er vorbereitet war dafür, ein Zeuge der geistigen Welt zu sein, dann war es immer nur ein einziges, ein gleiches Wort, das alle Eingeweihten beim Wiederbetreten der sinnlichen Welt sagten: 0 du mein Gott, wie herrlich hast du mich gemacht!",
        "Dies war die Empfindung, in die die Seele sich aushauchte nach der Ein­weihung, beim Wiederbetreten der gewöhnlichen sinnlichen Welt.",
        "Dies alles lebte in den Köpfen derjenigen, die die Einweihung zu leiten hatten.",
        "Später wurde, als das Schreiben"
      ],
      [
        "nach und nach mehr Sitte wurde, auch manches auf­geschrieben.",
        "Es gab aber eine typische Beschreibung des Lebens eines Eingeweihten.",
        "Man sagte ungefähr: Derjenige, welcher eingeweiht, aufgenommen werden soll in die Kult­stätten der Einweihung, hat sein Leben so und so einzurich­ten, und er hat die Erfahrung zu machen, die schließlich mit den Worten: 0 du mein Gott, wie herrlich hast du mich gemacht, ihren Abschluß fand."
      ],
      [
        "Wenn Sie sich das Leben, wie es ein Eingeweihter durch­machen muß vor die Seele hinstellen können, so wie Sie sich das Leben eines Menschen vorstellen können, der in einem chemischen Laboratorium experimentieren will, dann wür­den Sie ein typisches Bild von dem Menschen, der sich höher entwickelt, bekommen.",
        "Dann würden Sie ein typisches Bild bekommen dessen, der auferweckt werden soll.",
        "Solche Ein­weihungsbücher hat es gegeben, oder sie haben wenigstens in den Köpfen derjenigen gelebt, die die Einweihung ge­leitet haben.",
        "Wenn wir verstehen, daß es solche Bücher gegeben hat, dann werden wir uns nicht mehr wundern, wenn wir die verschiedensten Eingeweihten der verschie­denen Völker in ähnlicher Weise beschrieben finden.",
        "Darin liegt ein großes Geheimnis, darin ruht ein wunderbares Mysterium.",
        "Zu ihren Eingeweihten haben die Völker immer aufgesehen, soweit sie von ihnen gewußt haben.",
        "Was sie von ihnen erzählt haben, war nicht das, was der heutige Biograph von den großen Männern erzählt.",
        "Was sie er­zählten, war der geistige Lebensgang, den der Eingeweihte erlebte.",
        "So werden wir verstehen, warum - wenn wir den Lebensgang von Hermes, Buddha, Zarathustra, Moses und Christus verfolgen - wir bei diesen Gestalten zu einem ähnlichen Lebensbilde kommen.",
        "Und warum?",
        "Weil sie die­ses Leben leben mußten, wenn sie zum Eingeweihten werden wollten.",
        "Einfach das Lebensbild des Eingeweihten steht"
      ],
      [
        "vor uns in dem Leben des Hermes, Zarathustra, und so weiter."
      ],
      [
        "In dem, was die äußere Struktur der Lebensbeschreibung ist, können wir überall das Bild des Eingeweihten sehen, und von hier aus können wir uns die Frage beantworten: Wer waren diejenigen, welche die Evangelien geschrieben haben?",
        "Sie finden auf diese Frage eine geisteswissenschaft­liche Antwort in meinem Buche «Das Christentum als my­stische Tatsache»."
      ],
      [
        "Was ich hier nur mit kurzen Worten an­deuten kann, finden Sie dort ausführlich dargelegt, und damit auch hingewiesen auf die geistige Glaubwürdigkeit der Evangelien.",
        "Es ist dargelegt, daß das, was in den Evan­gelien steht, alten Einweihungsbüchern entnommen ist."
      ],
      [
        "Na­türlich unterschieden sich die Bücher, welche Eingeweihte über diese Dinge schrieben, durch Nebensächliches.",
        "In der Hauptsache aber kam der Inhalt immer auf dasselbe hin­aus.",
        "Nur müssen wir uns klarmachen, daß die, welche die Evangelien geschrieben haben, nichts anderes hatten als solche alten Einweihungsbücher."
      ],
      [
        "Wenn wir dann das wirk­lich Darinstehende ansehen, dann können wir in den ver­schiedenen Evangelien verschiedene Formen der Initiation oder Einweihung erblicken.",
        "Und warum unterscheiden sie sich?",
        "Weil ihre Schreiber die Einweihung von verschiedenen Orten her kannten."
      ],
      [
        "Verstehen werden wir dies, wenn wir das Verhältnis der Männer, die die Evangelien verfaßt haben, zum Christus Jesus ansehen.",
        "Wir erlangen die beste Vorstellung, wenn wir uns an die schönen Worte erinnern, mit denen die Apokalypse beginnt."
      ],
      [
        "Der, welcher die Schrift des Johannes diktierte, wird genannt: das Erste und das Letzte, das Alpha und das Omega.",
        "Nichts anderes ist damit gemeint, als dasjenige, was - trotzdem die Zeiten und For­men der Welt sich wandeln von Menschengeschlecht zu Men­schengeschlecht, von Menschenrasse zu Menschenrasse, von"
      ],
      [
        "Planet zu Planet - als eine einheitliche, geistige Wesenheit immer vorhanden bleibt.",
        "Wenn wir dies immer vorhandenbleibende Wesen als das Göttliche bezeichnen und sehen, daß wir einen Funken davon in uns haben, so fühlen wir uns mit diesem Alpha und Omega verwandt, ja wir fühlen dieses als das letzte Ideal, zu dem sich das sich Entwickelnde immer mehr hinaufhebt.",
        "So wurde uns dieses Ewige in allen Zeiten, dieses Dauernde in allem Wechsel vorgeführt."
      ],
      [
        "Nun müssen wir uns an den Sprachgebrauch erinnern, der ganz aus unserem Bewußtsein verschwunden ist.",
        "Ich möchte Ihnen das, worum es sich handelt, mit ein paar Worten vorführen.",
        "Heute ist der Name, den wir dem Men­schen geben, mehr oder weniger gleichgültig.",
        "Wir fühlen keinen rechten Zusammenhang zwischen dem Menschen und seinem Namen.",
        "Je weiter zurück man geht, desto be­deutungsvoller und wesentlicher wird der Name, man legte Wert auf gewisse Gesetze, durch die der Mensch einen Na­men bekommt.",
        "Ich brauche nur zu erinnern, daß es nicht sehr lange her ist, als noch die Gepflogenheit bestand, daß man in den Kalender schaute und dem neugeborenen Kinde den Namen gegeben hat, der am Tage seiner Geburt im Kalender stand.",
        "Man nahm an, daß das Kind sich hingedrängt fühlte zur Geburt an dem Tage, der diesen Namen trug.",
        "Derjenige, welcher die Einweihung durchgemacht hat, die ich beschrieben habe, hat einen neuen Namen erhalten, den Einweihungsnamen, und dieser bezeichnete seine innere Wesenheit, bezeichnete das, was er bedeutet in der Welt, das als was ihn der Führer erkannte.",
        "Dieser Name war mit seinem Wesen verknüpft und drückte das aus, was nur die innere Wesenheit angeht."
      ],
      [
        "Nun erinnern Sie sich, daß in der Bibel, im Neuen Testa­mente, die mannigfaltigsten Aussprüche Jesu angeführt werden.",
        "Derjenige nur dringt tiefer in diese Schriften ein,"
      ],
      [
        "der vom Gesichtspunkte des Eingeweihten an dieselben herangeht und der von der Namengebung auch etwas ver­steht.",
        "Man bezeichnete zum Beispiel jemanden, wenn man ihn geistig bezeichnen und ausdrücken wollte, daß er noch auf niederer Stufe steht, mit einem Ausdrucke, der hergenommen war von den Eigenschaften des Astralleibes; wenn er höher stand, mit Ausdrücken, die hergenommen waren von Eigenschaften des Ätherleibes.",
        "Wollte man das Typische ausdrücken, dann nahm man Ausdrücke, die von Eigenschaften des physischen Leibes hergenommen sind.",
        "So hatten die alten Namen eine Beziehung zu den Men­schen und drückten so recht eigentlich das Wesen aus.",
        "Er­innern wir uns jetzt, wie oft in den Evangelien Worte des Jesus vorkommen, wo er sich als etwas Bestimmtes be­zeichnet - namentlich im Johannes-Evangelium können Sie solches finden.",
        "Wir können sie vielfach zurückführen auf ein Wort, auf das Wörtchen Ich.",
        "Erinnern Sie sich an das, was ich schon öfter in diesen Vorträgen ausgeführt habe:"
      ],
      [
        "Man unterscheidet vier Glieder der menschlichen Wesen­heit: physischer Leib, Ätherleib, Astralleib und Ich.",
        "Dieses Ich wird immer größer und größer, dieses Ich ist so, daß es sich zur Einweihung hinaufentwickelt, dieses Ich ist un­vollkommen beim wenig entwickelten Menschen, gewaltig und vollkommen beim Eingeweihten.",
        "Wenn nun Christus im Johannes-Evangelium oftmals hindeutet darauf, daß er identisch sei mit dem «Ich-bin», wenn er sich bezeichnet als denjenigen, der da eins ist mit der tiefsten Wesenheit des Menschen in dem Satze «Ich und der Vater sind eins», wenn Sie das nehmen, so werden Sie es nun verstehen können von dieser Namengebung aus, weil er das Ewige in sich schließt, nicht weil er ein gewöhnlicher Mensch war und er mit die­sem Ich den gewöhnlichen Menschen bezeichnete, sondern weil er etwas war, das über den gewöhnlichen Menschen"
      ],
      [
        "hinausging, weil er Christus, das Alpha und Omega war.",
        "So sahen die, welche in jener Zeit lebten, in ihm ein gött­liches Wesen, das den physischen Leib trug, ein Wesen, für das ebenso gleichgültig ist der physische Leib und ebenso wichtig das Geistige, wie für den physischen Menschen der physische Leib höchst bedeutsam und unwichtig das Gei­stige ist."
      ],
      [
        "Das Hervorstechende beim Menschen wurde sein Name, und wenn wir dieses noch weiter bedenken, dann verstehen wir noch etwas anderes - Sie werden von da den Weg finden in manches Mysterium der Bibel -, wir ver­stehen, was es zu bedeuten hat, als Moses dem Jehova ge­genüberstand und Jehova ihn zum Gesandten für das Volk machen will und Moses erwiderte: Was soll ich ihnen sagen, wer mich gesandt hat? - Und wir hören die bedeutungsvol­len Worte: Sage, der «Ich-bin» hat dich gesandt. - Auf welche Wesenheit deutet hier Jehova selbst hin?",
        "Auf das, was im wesentlichen im tiefsten Inneren jeder Menschen­wesenheit liegt."
      ],
      [
        "Gelangen wir an das vierte Glied der menschlichen Wesenheit, so sehen wir, daß das Ich ein Name ist, den wir uns selbst geben müssen.",
        "Das Göttliche muß selbst sprechen, das Göttliche, das an einem Punkte zu sprechen be­ginnt, das als kleiner, unbedeutender Keim im Menschen lebt und zu unendlicher Größe entwickelt werden kann."
      ],
      [
        "Das ist es, was gemeint ist, was dem Moses den Auftrag gab und sagte: Sage ihnen, «Der Ich-bin» hat dich gesandt.",
        "Das, was wie ein göttlicher Keim in jeder menschlichen Seele liegt, das, was im physischen, Äther- und Astralleib eingehüllt ist wie ein Punkt, zu dem wir «Ich-bin» sagen, das, was noch un­bedeutend über sie emporwädist und was noch unbedeu­tend in uns emporlebt, werden wir nicht als das Geringe in unserer Wesenheit bezeichnen, sondern als das Wich­tigste."
      ],
      [
        "Das Wesentliche ist es, das im Menschen lebt und das den Moses schicken will, indem es sagt: «Ich bin der Ich-bin.»"
      ],
      [
        "So sehen Sie, welch tiefer Sinn in solcher Namengebung steckt, und wenn hingedeutet wurde auf dieses «Ich bin», dann wurde zu gleicher Zeit auch immer hingedeutet auf denjenigen Punkt in der Menschheitsentwicklung, den ich auch schon in diesen Vorträgen erwähnt habe und der auch in der Bibel angedeutet wird, nämlich den Punkt, wo der physische Mensch beseelt wird.",
        "Öfter habe ich schon aus­einandergesetzt, wie das, was heute der physische Mensch ist, sich von niederen Stufen heraufentwickelt hat, wie er sich dadurch, daß er mit einer Seele, die von der Gottheit herunterstieg, begabt wurde, sich weiterentwickeln konnte."
      ],
      [
        "Was aus dem Schoße der Gottheit herunterstieg, hat sich hineingesenkt in den physischen Leib und hat den physi­schen Leib weiterentwickelt.",
        "Dieser Moment ist auch in der Bibel angedeutet.",
        "Sie lehrt ihn mit ein paar Worten."
      ],
      [
        "Vor jenem Momente, der sich in Wirklichkeit über lange Zeit räume erstreckt hat hatte jener menschliche Korper nicht das, was man brauchte, um das Ich zur Entfaltung zu brin­gen, nicht das, was man als physischer Mensch auch heute notwendig gebraucht.",
        "In jener Zeit atmeten die Menschenvorfahren noch nicht durch Lungen, in jener Zeit entwickelte der Mensch aus einem schwimmblasenartigen Organ heraus seine Lunge."
      ],
      [
        "Er lernte da erst die Lungenluftatmung, und von diesem Vorgange ab gab es erst die Beseelung des menschlichen Körpers.",
        "Denken Sie sich diesen Vorgang zusammengedrängt in einen Satz, so haben Sie das biblische Wort: Und Gott blies dem Menschen den Odem ein und er ward eine lebendige Seele."
      ],
      [
        "Dadurch, daß der Mensch als physisches Wesen atmen lernte, war er be­fähigt, die Seele aufzunehmen.",
        "Gehen wir auf die Bedeu­tung des Jehovah-Namens zurück, dann finden wir, daß Jehovah soviel heißt wie «Wehen», daß die Luft dahinweht."
      ],
      [
        "Es ist im Worte Jahve nichts anderes ausgedrückt als"
      ],
      [
        "der wehende Atem, mit dem der Ichgeist in den Menschen einzieht.",
        "So wird in diesem Namen dargestellt, wie der wehende Atem seine Wesenheit in dem Satze ausdrückt:"
      ],
      [
        "«Ich bin der Ich-bin», der einen Teil seiner Wesenheit hineingießt in den Menschen.",
        "Es wird uns ein wahrer Weltenvorgang da vorgeführt.",
        "So wird uns zur wahren Tatsache jenes Ewige, das in der Menschennatur lebt.",
        "Ob wir den Menschen von heute oder den Menschen vor tau­senden von Jahren nehmen, das Ichwesen war da vor allen Zeiten.",
        "Denken Sie sich das Ichwesen in seiner höchsten Offenbarung, wo alles Äußere unwesentlich ist, denken Sie sich, daß ein Mensch das Innerste so groß und gewaltig er­kennt, dann haben Sie die Vorstellung, die sich die alten Christus-Anhänger von dem Christus machten.",
        "Was da in den ältesten Zeiten nur als Funke lebte, in höchster Glorie lebte es in Jesus von Nazareth.",
        "Er war, weil er der höchste Göttliche war, der höchste Eingeweihte, daher das Wort:"
      ],
      [
        "«Ehe denn Abraham ward, bin Ich.» Er ist in körperlicher Gestalt dasjenige, was da ist, ehe Abraham war, was da ist, ehe Abraham, Isaak und Jakob waren, er ist das, was als das größte Mensdiheitsideal vor dem steht, der sich ent­wickeln will, vor dem, der die Worte der Bergpredigt be­folgt: «Selig sind diejenigen, die da sind Bettler im Geist, denn sie werden in sich finden die Reiche der Himmel.» Nehmen wir dieses Wort so, dann haben Sie die Vor­stellung, die sich die Christus-Anhänger damals machten.",
        "Was konnten sie von diesem höchsten inkarnierten Gott für eine Lebensbeschreibung geben?",
        "Wo war eine Lebens­beschreibung, die seiner würdig war?",
        "Das war die Lebens­beschreibung, die man im Einweihungskanon gab, demjeni­gen Kanon, der die Regeln enthielt, nach denen der Ein­zuweihende initiiert werden sollte.",
        "Wie man sieht, war es so: Willst du eingeweiht werden, dann hast du von Lebensstufe"
      ],
      [
        "zu Lebensstufe das und das durchzumachen bis zur höchsten Stufe, die angedeutet ist mit den Worten: Mein Gott, mein Gott, wie hast du mich verherrlicht! . . . (Hier bricht die Nachschrift ab.)"
      ]
    ]
  },
  {
    "order": 15,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Die in vorliegendem Bande enthaltenen Vorträge des Winterhalhjahres 1906/07 sind die vierte der öffentlithen Vortragsreihen, weithe Rudolf Steiner in Berlin seit 1903 regelmäßig durchführte. In seiner Selbst-biographie «Mein Lehensgang» (Kapitel XXXI) weist er in folgender Art auf diesen Teil seiner Vortragstätigkeit hin: «So war es nicht etwa die in der Theosophischen Gesellschaft vereinigte Mitgliedschaft, auf die Marie von Sivers (Marie Steiner) und ich zählten, sondern die­jenigen Menschen überhaupt, die sich mit Herz und Sinn einfanden, wenn ernst zu nehmende Geist-Erkenntnis gepflegt wurde.",
      "Das Wirken innerhalb der damals bestehenden Zweige der Theo­sophischen Gesellschaft, das notwendig als Ausgangspunkt war, bil­dete daher nur einen Teil unserer Tätigkeit. Die Hauptsache war die Einrichtung von öffentlichen Vorträgen, in denen ich zu einem Publi­kum sprach, das außerhalb der Theosophischen Gesellschaft stand und das zu meinen Vorträgen nur wegen deren Inhalt kam.» (Vergleiche hierzu auch die Vorrede von Marie Steiner in dem Band «Aus schick­saltragender Zeit», Dornach 1959.)",
      "Das Winterhalbjahr 1906/07 umfaßte eigentlich 15 Vorträge, jedoch von zweien (11. April 1907): «Was wissen unsere Gelehrten von Theosophie?» und (25. April 1907): «Bibel und Weisheit» haben sich keine Nachschriften erhalten. Der Vortrag «Bibel und Weisheit» vom 26. April 1907 (Fortsetzung vom 25. April 1907) wurde, weil in sich geschlossen, aufgenommen, obwohl leider der Schluß fehlt. Vom sech­sten Vortrag «Die Erziehung des Kindes vom Gesichtspunkt der Gei­steswissenschaft» (10. Januar 1907) hat sich ebenfalls keine Nachschrift erhalten. An seiner Stelle wurde der Vortrag, der am 1. Dezember1906 in Köln gehalten wurde, der seinerseits wiederum durch Notizen aus dem Vortrag vom 12. Januar 1907 in Leipzig ergänzt wurde, auf­genommen. Rudolf Steiner hat über dieses Thema in verschiedenen deutschen Städten gesprochen und seine Ausführungen zu einem Auf­satz umgearbeitet, der erstmals in der Zeitschrift «Luzifer-Gnosis» (1907) abgedruckt wurde. Dieser Aufsatz befindet sich innerhalb der Gesamtausgabe im Band «Luzifer-Gnosis - Grundlegende Aufsätze zur Anthroposophie aus den Jahren 1903 bis 1908», Dornach 1959.",
      "Schon einmal publiziert waren Vortrag II, V, VIII und IX in Einzel-ausgaben (siehe Seite 5), VI, VII und X in der Zeitschrift «Die Men­schenschule» 23. Jg., 1949, Nr.1, und 30. Jg., 1956, Nr.4.",
      "Die meisten Nachschriften der in vorliegendem Bande enthaltenen Vorträge weisen Mängel auf, sind lückenhaft und können zum Teil nur als Inhaltsangaben bewertet werden. Die Nachschriften waren nicht zum Druck bestimmt und sind auch von Rudolf Steiner selbst nicht durchgesehen worden.",
      "Die in diesen Vorträgen gebrauchten Worte «Theosophie» und «theosophisch», deren sich Rudolf Steiner immer im Sinne seiner anthroposophisch orientierten Geisteswissenschaft (Anthroposophie) be­dient hat, sind, um Verwechslungen vorzubeugen, meist durch «Geistes-wissenschaft» oder «Anthroposophie» ersetzt worden. Diese Maß­nahme wurde in vielen Publikationen von Vorträgen von Frau Marie Steiner schon durchgeführt.",
      "11    es ist erst dreißig Jahre her, seit eine theosophische Bewegung",
      "duroh die Welt geht: Helena Petrowna Blavatsky (1831-1891) gründete mit H. S. Olcott im Jahre 1875 die Theosophische Gesellschaft. Vergleiche Rudolf Steiner, Geschichte und Be­dingungen der anthroposophischen Bewegung im Verhältnis zur Anthroposophischen Gesellschaft. 8 Vorträge, gehalten in Dornach vom 10. bis 17. Juni 1923. 2. Auflage Dornach 1959:",
      "ferner «Mein Lebensgang», letzte Auflage Dornach 1949.",
      "12    die lheosophie würde sich an ihrem ersten Grundsatz versün­digen: «Die Zwecke der Theosophischen Gesellschaft sind: a) den Kern einer allgemeinen Brüderschaft der Menschheit zu bilden, ohne Unterschied der Rasse, des Glaubens, des Geschlechts, der Kaste oder Farbe.» § 1 der Verfassung.",
      "22    in der Zeitschrift «Luzifer» habe ich den scheinbar grotesken",
      "Satz aus gesprochen: Siehe: «Luzifer-Gnosis - Grundlegende",
      "Aufsätze zur Anthroposophie aus den Jahren 1903 bis 1908»,",
      "Dornach 1959 in dem Aufsatz «Theosophie und soziale Frage».",
      "Als Einzelbroschüre erschienen unter dem Titel: Geisteswissen­schaft und soziale Frage - Drei Aufsätze, Dornach 1957.",
      "23    hat eine Natur forscherversammlung in Stuttgart stattgefunden.",
      "78. Versammlung deutscher Naturforscher und Ärzte in Stutt­gart 1906.",
      "24    Theodor Lipps durfte Jetzt über Naturwissenschaft und Philo­sophie sprechen: Theodor Lipps, Naturwissenschaft und Welt­anschauung, Vortrag, gehalten auf der 78. Versammlung deut­scher Naturforscher und Ärzte in Stuttgart; Heidelberg 1906.",
      "33    Helen Keller . . . Von ihr ist ein neues Büchelchen erschienen:",
      "Optimismus, ein Glaubensbekenntnis von Helen Keller, deutsche Ausgabe Stuttgart 1906.",
      "35    der Faust-Kommentar . . . von dem Professor Minor: Minor, Goethes Faust, Entstehungsgeschichte und Erklärung (2 Bände), Stuttgart 1901.",
      "52    es ist ganz richtig, was Guvier gesagt hat: Siehe Goethes Aufsatz:",
      "Principes de Philosophie zoologique. In Goethes Naturwissen­schaftliche Schriften, herausgegeben und mit Kommentaren ver­sehen von Rudolf Steiner. 1. Band: Schriften über die Bildung und Umbildung organischer Naturen, 2. Auflage Bern 1949.",
      "67    Der Ausspruch des weisen Silen: Aristoteles im Dialog Eude­mos: «Man erzählt: Als Midas auf den Silen Jagd machte und es ihm gelungen war, ihn zu fangen, da habe dieser auf die dringende Frage des Königs, was für den Menschen das Beste und das Wünschenswerteste von allem sei, in unverbrüchlichem Schweigen verharrt. Als ihn aber der König durch Anwendung aller möglichen Mittel mit Mühe dazu brachte, ihm etwas zu erwidern, da habe er hohnlachend gesagt:",
      "101    Paulus-Zitat: «Denn der Tod ist der Sünde Sold»: Epistel an die Römer, 6, 23.",
      "103    Schopenhauer-Zitat: Arthur Schopenhauers sämtliche Werke in zwölf Bänden herausgegeben und mit einer Einleitung von Rudolf Steiner, Cotta Stuttgart 1894, Band 1, Seite 12.",
      "104    Eduard von Hartmann in seinem letzten Buche: Das Problem des Lebens, 1906.",
      "116    Goethe-Zitat: Wörtlich: «Leben ist ihre schönste Erfindung, der Tod ihr Kunstgriff, viel Leben zu haben.» Die Natur, aphori­stisch von Goethe (1780) mit Anmerkungen von Rudolf Steiner, in: Veröffentlichungen aus dem literarischen Frühwerk, Band I, Dornach 1939.",
      "120    Goethe-Zitat: Urworte, orphisch.",
      "134    Friedrich August Wolf charakterisierte die Stufen von der Kind­heit an folgendermaßen: Wolf, Ideen über Erziehung, Schule und Universität, Quedlinburg 1835: Entwicklungsstufen des männlichen Individuums.",
      "143    ein Buch des Wiener Kriminalanthropolo gen: Moritz Benedikt, Aus meinem Leben. Erinnerungen und Erörterungen, Wien 1906.",
      "147    Hellenbach: Freiherr Lazar von Hellenbach (1827-1887), Philo­soph, Okkultist und bekannter Spiritist.",
      "151    Goethe . . . die Urpftanze: Goethe, Die Metamorphose der Pflan­zen. Siehe Hinweis zu Seite 52.",
      "158    Goethe-Zitat: Wörtlich: «Das Auge hat sein Dasein dem Licht zu danken. Aus gleichgültigen Hilfsorganen ruft sich das Licht ein Organ hervor, das seinesgleichen werde, und so bildet sich das Auge am Lichte fürs Licht, damit das innere Licht dem äußeren entgegentrete.» Goethe, Entwurf einer Farbenlehre (1810), in: Goethes Naturwissenschaftliche Schriften, heraus­gegeben und mit Kommentaren von Rudolf Steiner, 3. Band:",
      "Die Farbenlehre, 2. Auflage Bern 1947.",
      "176    im Jahre 1615 erschien die so genannte «Fama Fraternitatis»",
      "und die sogenannte «Gonfessio»: Siehe hierzu: Die chymische",
      "Hochzeit des Christian Rosenkreuz - Fama Fraternitatis. Ins",
      "Neuhochdeutsche übertragen von Walter Weber, mit einem",
      "Aufsatz von Rudolf Steiner, Stuttgart 1957.",
      "178    Goethe-Zitat: Faust I, Nacht.",
      "183    Wie erlangt man Erkenntnisse der höheren Welten?, Berlin 1904,",
      "187    meine beiden Bücher: Wahrheit und Wissenschaft, Vorspiel einer «Philosophie der Freiheit», Weimar 1892, 4. Auflage Dornach 1958. «Die Philosophie der Freiheit - Grundzüge einer moder­nen Weltanschauung», Berlin 1884, ii. Auflage Stuttgart 1955.",
      "190    in dem großen okkulten Ideal des beiligen Grals: Siehe Rudolf Steiner, Von der Suche nach dem heiligen Gral, (6 Vorträge ge­halten in Leipzig vom 28. Dezember 1913 bis 2.Januar 1914), Dornach 1934 (Neuauflage in Vorbereitung); Bilder okkulter Siegel und Säulen - Der Münchner Kongreß Pfingsten 1907 (Aufsätze und Vorträge aus dem Jahre 1907 mit 36 Abbildun­gen), Dornach 1957.",
      "214    Goethe-Zitat: Aus: Winckelmann.",
      "244    Augustinus-Zitat: Aug. Retractationes,L.I., Cap. XIII, 3. «Was man gegenwärtig die christliche Religion nennt, bestand schon bei den Alten und fehlte nicht in den Anfängen des Menschen­geschlechts und als Christus im Fleische erschien, erhielt die wahre Religion, die schon vorher vorhanden war, den Namen der christlichen.»",
      "248  Schon . . . sagt, daß das alte indische Atma Vidya dasselbe ist:",
      "In der Nachschrift steht hier «Paulus», was aber offensichtlich auf einem Hörfehler oder einer größeren Lücke in der Nach­schriif beruhen muß, da sich bei Paulus keine derartige Äuße­rung findet.",
      "252    in meiner Zeitschrift «Luzifer-Gnosis» können Sie Lesen: Luzi­fer-Gnosis - Grundlegende Aufsätze zur Anthroposophie aus den Jahren 1903-1908, Dornach 1959.",
      "257  in meinem Buche «Das Christentum als mystische Tatsache»:",
      "Das Christentum als mystische Tatsache und die Mysterien des Altertums, Berlin 1902, 7. Auflage Dornach 1959."
    ],
    "sentences": [
      [
        "Die in vorliegendem Bande enthaltenen Vorträge des Winterhalhjahres 1906/07 sind die vierte der öffentlithen Vortragsreihen, weithe Rudolf Steiner in Berlin seit 1903 regelmäßig durchführte.",
        "In seiner Selbst-biographie «Mein Lehensgang» (Kapitel XXXI) weist er in folgender Art auf diesen Teil seiner Vortragstätigkeit hin: «So war es nicht etwa die in der Theosophischen Gesellschaft vereinigte Mitgliedschaft, auf die Marie von Sivers (Marie Steiner) und ich zählten, sondern die­jenigen Menschen überhaupt, die sich mit Herz und Sinn einfanden, wenn ernst zu nehmende Geist-Erkenntnis gepflegt wurde."
      ],
      [
        "Das Wirken innerhalb der damals bestehenden Zweige der Theo­sophischen Gesellschaft, das notwendig als Ausgangspunkt war, bil­dete daher nur einen Teil unserer Tätigkeit.",
        "Die Hauptsache war die Einrichtung von öffentlichen Vorträgen, in denen ich zu einem Publi­kum sprach, das außerhalb der Theosophischen Gesellschaft stand und das zu meinen Vorträgen nur wegen deren Inhalt kam.» (Vergleiche hierzu auch die Vorrede von Marie Steiner in dem Band «Aus schick­saltragender Zeit», Dornach 1959.)"
      ],
      [
        "Das Winterhalbjahr 1906/07 umfaßte eigentlich 15 Vorträge, jedoch von zweien (11.",
        "April 1907): «Was wissen unsere Gelehrten von Theosophie?» und (25.",
        "April 1907): «Bibel und Weisheit» haben sich keine Nachschriften erhalten.",
        "Der Vortrag «Bibel und Weisheit» vom 26.",
        "April 1907 (Fortsetzung vom 25.",
        "April 1907) wurde, weil in sich geschlossen, aufgenommen, obwohl leider der Schluß fehlt.",
        "Vom sech­sten Vortrag «Die Erziehung des Kindes vom Gesichtspunkt der Gei­steswissenschaft» (10.",
        "Januar 1907) hat sich ebenfalls keine Nachschrift erhalten.",
        "An seiner Stelle wurde der Vortrag, der am 1.",
        "Dezember1906 in Köln gehalten wurde, der seinerseits wiederum durch Notizen aus dem Vortrag vom 12.",
        "Januar 1907 in Leipzig ergänzt wurde, auf­genommen.",
        "Rudolf Steiner hat über dieses Thema in verschiedenen deutschen Städten gesprochen und seine Ausführungen zu einem Auf­satz umgearbeitet, der erstmals in der Zeitschrift «Luzifer-Gnosis» (1907) abgedruckt wurde.",
        "Dieser Aufsatz befindet sich innerhalb der Gesamtausgabe im Band «Luzifer-Gnosis - Grundlegende Aufsätze zur Anthroposophie aus den Jahren 1903 bis 1908», Dornach 1959."
      ],
      [
        "Schon einmal publiziert waren Vortrag II, V, VIII und IX in Einzel-ausgaben (siehe Seite 5), VI, VII und X in der Zeitschrift «Die Men­schenschule» 23.",
        "Jg., 1949, Nr.1, und 30.",
        "Jg., 1956, Nr.4."
      ],
      [
        "Die meisten Nachschriften der in vorliegendem Bande enthaltenen Vorträge weisen Mängel auf, sind lückenhaft und können zum Teil nur als Inhaltsangaben bewertet werden.",
        "Die Nachschriften waren nicht zum Druck bestimmt und sind auch von Rudolf Steiner selbst nicht durchgesehen worden."
      ],
      [
        "Die in diesen Vorträgen gebrauchten Worte «Theosophie» und «theosophisch», deren sich Rudolf Steiner immer im Sinne seiner anthroposophisch orientierten Geisteswissenschaft (Anthroposophie) be­dient hat, sind, um Verwechslungen vorzubeugen, meist durch «Geistes-wissenschaft» oder «Anthroposophie» ersetzt worden.",
        "Diese Maß­nahme wurde in vielen Publikationen von Vorträgen von Frau Marie Steiner schon durchgeführt."
      ],
      [
        "11 es ist erst dreißig Jahre her, seit eine theosophische Bewegung"
      ],
      [
        "duroh die Welt geht: Helena Petrowna Blavatsky (1831-1891) gründete mit H.",
        "Olcott im Jahre 1875 die Theosophische Gesellschaft.",
        "Vergleiche Rudolf Steiner, Geschichte und Be­dingungen der anthroposophischen Bewegung im Verhältnis zur Anthroposophischen Gesellschaft. 8 Vorträge, gehalten in Dornach vom 10. bis 17.",
        "Juni 1923. 2.",
        "Auflage Dornach 1959:"
      ],
      [
        "ferner «Mein Lebensgang», letzte Auflage Dornach 1949."
      ],
      [
        "12 die lheosophie würde sich an ihrem ersten Grundsatz versün­digen: «Die Zwecke der Theosophischen Gesellschaft sind: a) den Kern einer allgemeinen Brüderschaft der Menschheit zu bilden, ohne Unterschied der Rasse, des Glaubens, des Geschlechts, der Kaste oder Farbe.» § 1 der Verfassung."
      ],
      [
        "22 in der Zeitschrift «Luzifer» habe ich den scheinbar grotesken"
      ],
      [
        "Satz aus gesprochen: Siehe: «Luzifer-Gnosis - Grundlegende"
      ],
      [
        "Aufsätze zur Anthroposophie aus den Jahren 1903 bis 1908»,"
      ],
      [
        "Dornach 1959 in dem Aufsatz «Theosophie und soziale Frage»."
      ],
      [
        "Als Einzelbroschüre erschienen unter dem Titel: Geisteswissen­schaft und soziale Frage - Drei Aufsätze, Dornach 1957."
      ],
      [
        "23 hat eine Natur forscherversammlung in Stuttgart stattgefunden."
      ],
      [
        "Versammlung deutscher Naturforscher und Ärzte in Stutt­gart 1906."
      ],
      [
        "24 Theodor Lipps durfte Jetzt über Naturwissenschaft und Philo­sophie sprechen: Theodor Lipps, Naturwissenschaft und Welt­anschauung, Vortrag, gehalten auf der 78.",
        "Versammlung deut­scher Naturforscher und Ärzte in Stuttgart; Heidelberg 1906."
      ],
      [
        "33 Helen Keller . . .",
        "Von ihr ist ein neues Büchelchen erschienen:"
      ],
      [
        "Optimismus, ein Glaubensbekenntnis von Helen Keller, deutsche Ausgabe Stuttgart 1906."
      ],
      [
        "35 der Faust-Kommentar . . . von dem Professor Minor: Minor, Goethes Faust, Entstehungsgeschichte und Erklärung (2 Bände), Stuttgart 1901."
      ],
      [
        "52 es ist ganz richtig, was Guvier gesagt hat: Siehe Goethes Aufsatz:"
      ],
      [
        "Principes de Philosophie zoologique.",
        "In Goethes Naturwissen­schaftliche Schriften, herausgegeben und mit Kommentaren ver­sehen von Rudolf Steiner. 1.",
        "Band: Schriften über die Bildung und Umbildung organischer Naturen, 2.",
        "Auflage Bern 1949."
      ],
      [
        "67 Der Ausspruch des weisen Silen: Aristoteles im Dialog Eude­mos: «Man erzählt: Als Midas auf den Silen Jagd machte und es ihm gelungen war, ihn zu fangen, da habe dieser auf die dringende Frage des Königs, was für den Menschen das Beste und das Wünschenswerteste von allem sei, in unverbrüchlichem Schweigen verharrt.",
        "Als ihn aber der König durch Anwendung aller möglichen Mittel mit Mühe dazu brachte, ihm etwas zu erwidern, da habe er hohnlachend gesagt:"
      ],
      [
        "101 Paulus-Zitat: «Denn der Tod ist der Sünde Sold»: Epistel an die Römer, 6, 23."
      ],
      [
        "103 Schopenhauer-Zitat: Arthur Schopenhauers sämtliche Werke in zwölf Bänden herausgegeben und mit einer Einleitung von Rudolf Steiner, Cotta Stuttgart 1894, Band 1, Seite 12."
      ],
      [
        "104 Eduard von Hartmann in seinem letzten Buche: Das Problem des Lebens, 1906."
      ],
      [
        "116 Goethe-Zitat: Wörtlich: «Leben ist ihre schönste Erfindung, der Tod ihr Kunstgriff, viel Leben zu haben.» Die Natur, aphori­stisch von Goethe (1780) mit Anmerkungen von Rudolf Steiner, in: Veröffentlichungen aus dem literarischen Frühwerk, Band I, Dornach 1939."
      ],
      [
        "120 Goethe-Zitat: Urworte, orphisch."
      ],
      [
        "134 Friedrich August Wolf charakterisierte die Stufen von der Kind­heit an folgendermaßen: Wolf, Ideen über Erziehung, Schule und Universität, Quedlinburg 1835: Entwicklungsstufen des männlichen Individuums."
      ],
      [
        "143 ein Buch des Wiener Kriminalanthropolo gen: Moritz Benedikt, Aus meinem Leben.",
        "Erinnerungen und Erörterungen, Wien 1906."
      ],
      [
        "147 Hellenbach: Freiherr Lazar von Hellenbach (1827-1887), Philo­soph, Okkultist und bekannter Spiritist."
      ],
      [
        "151 Goethe . . . die Urpftanze: Goethe, Die Metamorphose der Pflan­zen.",
        "Siehe Hinweis zu Seite 52."
      ],
      [
        "158 Goethe-Zitat: Wörtlich: «Das Auge hat sein Dasein dem Licht zu danken.",
        "Aus gleichgültigen Hilfsorganen ruft sich das Licht ein Organ hervor, das seinesgleichen werde, und so bildet sich das Auge am Lichte fürs Licht, damit das innere Licht dem äußeren entgegentrete.» Goethe, Entwurf einer Farbenlehre (1810), in: Goethes Naturwissenschaftliche Schriften, heraus­gegeben und mit Kommentaren von Rudolf Steiner, 3.",
        "Band:"
      ],
      [
        "Die Farbenlehre, 2.",
        "Auflage Bern 1947."
      ],
      [
        "176 im Jahre 1615 erschien die so genannte «Fama Fraternitatis»"
      ],
      [
        "und die sogenannte «Gonfessio»: Siehe hierzu: Die chymische"
      ],
      [
        "Hochzeit des Christian Rosenkreuz - Fama Fraternitatis."
      ],
      [
        "Neuhochdeutsche übertragen von Walter Weber, mit einem"
      ],
      [
        "Aufsatz von Rudolf Steiner, Stuttgart 1957."
      ],
      [
        "178 Goethe-Zitat: Faust I, Nacht."
      ],
      [
        "183 Wie erlangt man Erkenntnisse der höheren Welten?, Berlin 1904,"
      ],
      [
        "187 meine beiden Bücher: Wahrheit und Wissenschaft, Vorspiel einer «Philosophie der Freiheit», Weimar 1892, 4.",
        "Auflage Dornach 1958.",
        "«Die Philosophie der Freiheit - Grundzüge einer moder­nen Weltanschauung», Berlin 1884, ii.",
        "Auflage Stuttgart 1955."
      ],
      [
        "190 in dem großen okkulten Ideal des beiligen Grals: Siehe Rudolf Steiner, Von der Suche nach dem heiligen Gral, (6 Vorträge ge­halten in Leipzig vom 28.",
        "Dezember 1913 bis 2.Januar 1914), Dornach 1934 (Neuauflage in Vorbereitung); Bilder okkulter Siegel und Säulen - Der Münchner Kongreß Pfingsten 1907 (Aufsätze und Vorträge aus dem Jahre 1907 mit 36 Abbildun­gen), Dornach 1957."
      ],
      [
        "214 Goethe-Zitat: Aus: Winckelmann."
      ],
      [
        "244 Augustinus-Zitat: Aug.",
        "Retractationes,L.I., Cap.",
        "XIII, 3.",
        "«Was man gegenwärtig die christliche Religion nennt, bestand schon bei den Alten und fehlte nicht in den Anfängen des Menschen­geschlechts und als Christus im Fleische erschien, erhielt die wahre Religion, die schon vorher vorhanden war, den Namen der christlichen.»"
      ],
      [
        "248 Schon . . . sagt, daß das alte indische Atma Vidya dasselbe ist:"
      ],
      [
        "In der Nachschrift steht hier «Paulus», was aber offensichtlich auf einem Hörfehler oder einer größeren Lücke in der Nach­schriif beruhen muß, da sich bei Paulus keine derartige Äuße­rung findet."
      ],
      [
        "252 in meiner Zeitschrift «Luzifer-Gnosis» können Sie Lesen: Luzi­fer-Gnosis - Grundlegende Aufsätze zur Anthroposophie aus den Jahren 1903-1908, Dornach 1959."
      ],
      [
        "257 in meinem Buche «Das Christentum als mystische Tatsache»:"
      ],
      [
        "Das Christentum als mystische Tatsache und die Mysterien des Altertums, Berlin 1902, 7.",
        "Auflage Dornach 1959."
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
