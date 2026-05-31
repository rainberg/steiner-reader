#!/usr/bin/env python3
"""Standalone import script for GA121 — GA121 - Die Mission einzelner Volksseelen im Zusammenhang mit der germanisch-nordischen Mythologie"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA121 - Die Mission einzelner Volksseelen im Zusammenhang mit der germanisch-nordischen Mythologie"""
GA_NUMBER = "GA121"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "EINE VORREDE Nachträglich geschrieben zu diesen vor mehr als sieben lahren gehaltenen Vorträgen",
    "paragraphs": [
      "In diesen Vorträgen, die im Juni1910 in Christiania gehalten worden sind, habe ich den Versuch gewagt, die Psychologie der Völkerentwik­kelung zu zeichnen. Als Grundlage der Betrachtung hat gedient, was ich über anthroposophisch orientierte Geisteswissenschaft (in meinen Büchern «Theosophie», «Geheimwissenschaft», «Vom Menschenrätsel», «Von Seelenrätseln» und anderen) dargestellt habe.",
      "Ich durfte auf dieser Grundlage aufbauen, weil meine Zuhörer bekannt waren mit der wissenschaftlichen Anschauung, die in meinen Büchern gekennzeichnet wird. Es kommt aber zu diesem äußeren Grund für die Wahl des Gesichtspunktes noch ein innerer.",
      "Für eine wirkliche Psychologie der Völkercharaktere kann die anthropologische, ethnographische, selbst die historische Betrachtung der gewöhnlichen Wissenschaft keine aus­reichende Grundlegung geben. Man kommt mit dem von dieser Wis­senschaft Gebotenen nicht weiter als man mit der Anatomie und Physiologie kommt für eine Erkenntnis des Seelenlebens des Menschen.",
      "Wie man bei dem einzelnen Menschen vom Leibe zur Seele fortschreiten muß, wenn man sein inneres Leben kennen lernen will, so muß man für die Völkercharaktere zu dem ihnen zugrunde liegenden Seelisch-Gei­stigen vordringen, wenn man eine wirkliche Erkenntnis derselben anstrebt. Dieses Seelisch-Geistige ist aber nicht ein bloßes Zusammenwirken der Einzel-Seelen der Menschen, sondern es ist ein diesen über­geordnetes Seelisch-Geistiges.",
      "Ein solches zu betrachten, ist der gegen­wärtigen Wissenschaft ganz ungewohnt. Vor ihrem Forum ist es paradox von Volksseelen als von wirklichen Wesenheiten zu sprechen, wie man vom wirklichen Denken, Fühlen und Wollen des einzelnen Menschen spricht.",
      "Und ebenso paradox ist es vor diesem Forum, die Völker-Entwickelung auf der Erde in Zusammenhang zu bringen mit den Kräften der Himmelskörper des Weltraumes. Man braucht aber, um die Sache nicht mehr paradox zu finden, sich nur zu erinnern, daß niemand die Kräfte, welche eine Magnetnadel in der Nord-Süd-Richtung",
      "einstellen, innerhalb der Magnetnadel selbst suchen wird. Er schreibt sie der Wirkung des Erdmagnetismus zu. Er sucht die Gründe für die Richtung der Nadel im Kosmos. Wird man also nicht die Gründe für die Entwickelung von Volkscharakteren, Volkswanderungen usw. außerhalb der Volkszusammenhänge im Kosmos suchen dürfen? Von der anthroposophischen Anschauung ganz abgesehen, für die höhere geistige Wesenheiten eine Wirklichkeit sind, kommt für den Inhalt dieser Vorträge noch ein ganz anderes in Betracht. Dieser Inhalt legt aller­dings eine höhere geistige Wirklichkeit der Völker-Entwickelung zu­grunde, und er sucht die Kräfte, welche dieser Entwickelung die Rich­tungen geben, in einer solchen Wirklichkeit. Allein die Betrachtung steigt dann herab zu den Tatsachen, die im Leben der Völker zutage treten. Und da zeigt es sich, daß diese Tatsachen durch diese Grund­legung verständlich werden. Man kann dadurch die Lebensverhältnisse der einzelnen Völker sowohl, wie auch ihre gegenseitigen Beziehungen durchschauen, während es ohne eine solche Grundlegung ein wahres Erkennen auf diesem Gebiete nicht gibt. Man muß entweder auf eine Völkerpsychologie verzichten, oder man muß für sie eine Grundlegung in einer geistigen Wirklichkeit suchen.",
      "Ich habe mich nicht gescheut, für die höheren geistigen Wesenheiten die Namen anzuwenden, welche in den ersten christlichen Jahrhunder­ten üblich waren. Der Orientale würde andere Namen wählen. Doch wenn man auch heute das Anwenden solcher Namen wenig «wissen­schaftlich» finden kann, so scheint es mir doch richtig, vor solcher Anwendung nicht zurückzuschrecken; erstens wird dadurch dem christ­lichen Grundcharakter unserer abendländischen Kultur Rechnung getragen, zweitens ist dadurch doch noch eher eine Verständigung mög­lich, als wenn völlig neue Namen gewählt würden, oder wenn orienta­lische Bezeichnungen übernommen würden, deren wahrer Inhalt doch nur demjenigen gegenwärtig sein kann, der in dem entsprechenden Kulturzusammenhang seelisch darinnen steht. Mir schwebt doch die Möglichkeit vor, daß derjenige, welcher in diese geistigen Zusammen-hänge eindringen will, sich, wenn er die Sache als solche nicht ablehnt, an Namen wie Engel, Erzengel, Throne usw. ebensowenig stoßen wird, wie er dies in der physischen Wissenschaft gegenüber Benennungen wie",
      "positive und negative Elektrizität, Magnetismus, polarisiertes Licht usw. tut.",
      "Wer den Inhalt dieser Vorträge zusammenhält mit den schmerzlichen Prüfungen der Kulturmenschheit in diesen Tagen, der wird finden kön­nen, daß das damals Gesagte manches Licht verbreitet über jetzt Ge­schehendes. Hielte ich diese Vorträge jetzt, so könnte man glauben, daß der augenblickliche Stand der Weltereignisse solche Betrachtungen herausforderte. So steht zum Beispiel auf Seite 3 des ersten Vortrages:",
      "«Es ist... von einer ganz besonderen Wichtigkeit..., daß gerade in unserer Zeit in unbefangenster Weise auch gesprochen wird über das­jenige, was wir die Mission der einzelnen Volksseelen der Menschheit nennen ..., weil die nächsten Schicksale der Menschheit in einem viel höheren Grade als das bisher der Fall war, die Menschen zu einer ge­meinsamen Menschheitsmission zusammenführen werden. Zu dieser gemeinsamen Mission werden aber die einzelnen Volksangehörigen nur dann ihren entsprechenden freien, konkreten Beitrag liefern können, wenn sie vor allen Dingen ein Verständnis haben für ihr Volkstum, ein Verständnis für dasjenige, was man nennen kann .» Die Zeiten sind wohl nun da, in denen die Schicksale der Menschheit selber lehren, daß in einer solchen Anschauung Wahrheit ist.",
      "Vielleicht ist gerade das Thema von den «Volksseelen» ein solches, das zeigt, wie geistige Betrachtung, die auf die wirkliche übersinnliche Wesenheit des Daseins geht, zugleich die wahrhaft praktische Lebens­anschauung gibt, die Licht wirft auch auf die einzelnsten Fragen des Lebens. Eine Lebensbetrachtung, die für die Entwickelung und das Wesen der Völker nur solche Vorstellungen gebraucht, die für die Naturwissenschaft mit Recht geltend gemacht werden, kann das nicht. Diese mechanistisch-physische Wissenschaft hat ihr Großes geleistet in der Hervorbringung mechanisch-physikalisch-chemischer Kultur-mittel; für die Kulturmittel des geistigen Lebens der Menschheit bedarf es einer auf das Geistige hingeordneten Wissenschaft. Unsere Zeit bedarf einer solchen Wissenschaft.",
      "Berlin, 8. Februar 1918.    Rudolf Steiner"
    ],
    "sentences": [
      [
        "In diesen Vorträgen, die im Juni1910 in Christiania gehalten worden sind, habe ich den Versuch gewagt, die Psychologie der Völkerentwik­kelung zu zeichnen.",
        "Als Grundlage der Betrachtung hat gedient, was ich über anthroposophisch orientierte Geisteswissenschaft (in meinen Büchern «Theosophie», «Geheimwissenschaft», «Vom Menschenrätsel», «Von Seelenrätseln» und anderen) dargestellt habe."
      ],
      [
        "Ich durfte auf dieser Grundlage aufbauen, weil meine Zuhörer bekannt waren mit der wissenschaftlichen Anschauung, die in meinen Büchern gekennzeichnet wird.",
        "Es kommt aber zu diesem äußeren Grund für die Wahl des Gesichtspunktes noch ein innerer."
      ],
      [
        "Für eine wirkliche Psychologie der Völkercharaktere kann die anthropologische, ethnographische, selbst die historische Betrachtung der gewöhnlichen Wissenschaft keine aus­reichende Grundlegung geben.",
        "Man kommt mit dem von dieser Wis­senschaft Gebotenen nicht weiter als man mit der Anatomie und Physiologie kommt für eine Erkenntnis des Seelenlebens des Menschen."
      ],
      [
        "Wie man bei dem einzelnen Menschen vom Leibe zur Seele fortschreiten muß, wenn man sein inneres Leben kennen lernen will, so muß man für die Völkercharaktere zu dem ihnen zugrunde liegenden Seelisch-Gei­stigen vordringen, wenn man eine wirkliche Erkenntnis derselben anstrebt.",
        "Dieses Seelisch-Geistige ist aber nicht ein bloßes Zusammenwirken der Einzel-Seelen der Menschen, sondern es ist ein diesen über­geordnetes Seelisch-Geistiges."
      ],
      [
        "Ein solches zu betrachten, ist der gegen­wärtigen Wissenschaft ganz ungewohnt.",
        "Vor ihrem Forum ist es paradox von Volksseelen als von wirklichen Wesenheiten zu sprechen, wie man vom wirklichen Denken, Fühlen und Wollen des einzelnen Menschen spricht."
      ],
      [
        "Und ebenso paradox ist es vor diesem Forum, die Völker-Entwickelung auf der Erde in Zusammenhang zu bringen mit den Kräften der Himmelskörper des Weltraumes.",
        "Man braucht aber, um die Sache nicht mehr paradox zu finden, sich nur zu erinnern, daß niemand die Kräfte, welche eine Magnetnadel in der Nord-Süd-Richtung"
      ],
      [
        "einstellen, innerhalb der Magnetnadel selbst suchen wird.",
        "Er schreibt sie der Wirkung des Erdmagnetismus zu.",
        "Er sucht die Gründe für die Richtung der Nadel im Kosmos.",
        "Wird man also nicht die Gründe für die Entwickelung von Volkscharakteren, Volkswanderungen usw. außerhalb der Volkszusammenhänge im Kosmos suchen dürfen?",
        "Von der anthroposophischen Anschauung ganz abgesehen, für die höhere geistige Wesenheiten eine Wirklichkeit sind, kommt für den Inhalt dieser Vorträge noch ein ganz anderes in Betracht.",
        "Dieser Inhalt legt aller­dings eine höhere geistige Wirklichkeit der Völker-Entwickelung zu­grunde, und er sucht die Kräfte, welche dieser Entwickelung die Rich­tungen geben, in einer solchen Wirklichkeit.",
        "Allein die Betrachtung steigt dann herab zu den Tatsachen, die im Leben der Völker zutage treten.",
        "Und da zeigt es sich, daß diese Tatsachen durch diese Grund­legung verständlich werden.",
        "Man kann dadurch die Lebensverhältnisse der einzelnen Völker sowohl, wie auch ihre gegenseitigen Beziehungen durchschauen, während es ohne eine solche Grundlegung ein wahres Erkennen auf diesem Gebiete nicht gibt.",
        "Man muß entweder auf eine Völkerpsychologie verzichten, oder man muß für sie eine Grundlegung in einer geistigen Wirklichkeit suchen."
      ],
      [
        "Ich habe mich nicht gescheut, für die höheren geistigen Wesenheiten die Namen anzuwenden, welche in den ersten christlichen Jahrhunder­ten üblich waren.",
        "Der Orientale würde andere Namen wählen.",
        "Doch wenn man auch heute das Anwenden solcher Namen wenig «wissen­schaftlich» finden kann, so scheint es mir doch richtig, vor solcher Anwendung nicht zurückzuschrecken; erstens wird dadurch dem christ­lichen Grundcharakter unserer abendländischen Kultur Rechnung getragen, zweitens ist dadurch doch noch eher eine Verständigung mög­lich, als wenn völlig neue Namen gewählt würden, oder wenn orienta­lische Bezeichnungen übernommen würden, deren wahrer Inhalt doch nur demjenigen gegenwärtig sein kann, der in dem entsprechenden Kulturzusammenhang seelisch darinnen steht.",
        "Mir schwebt doch die Möglichkeit vor, daß derjenige, welcher in diese geistigen Zusammen-hänge eindringen will, sich, wenn er die Sache als solche nicht ablehnt, an Namen wie Engel, Erzengel, Throne usw. ebensowenig stoßen wird, wie er dies in der physischen Wissenschaft gegenüber Benennungen wie"
      ],
      [
        "positive und negative Elektrizität, Magnetismus, polarisiertes Licht usw. tut."
      ],
      [
        "Wer den Inhalt dieser Vorträge zusammenhält mit den schmerzlichen Prüfungen der Kulturmenschheit in diesen Tagen, der wird finden kön­nen, daß das damals Gesagte manches Licht verbreitet über jetzt Ge­schehendes.",
        "Hielte ich diese Vorträge jetzt, so könnte man glauben, daß der augenblickliche Stand der Weltereignisse solche Betrachtungen herausforderte.",
        "So steht zum Beispiel auf Seite 3 des ersten Vortrages:"
      ],
      [
        "«Es ist... von einer ganz besonderen Wichtigkeit..., daß gerade in unserer Zeit in unbefangenster Weise auch gesprochen wird über das­jenige, was wir die Mission der einzelnen Volksseelen der Menschheit nennen ..., weil die nächsten Schicksale der Menschheit in einem viel höheren Grade als das bisher der Fall war, die Menschen zu einer ge­meinsamen Menschheitsmission zusammenführen werden.",
        "Zu dieser gemeinsamen Mission werden aber die einzelnen Volksangehörigen nur dann ihren entsprechenden freien, konkreten Beitrag liefern können, wenn sie vor allen Dingen ein Verständnis haben für ihr Volkstum, ein Verständnis für dasjenige, was man nennen kann .» Die Zeiten sind wohl nun da, in denen die Schicksale der Menschheit selber lehren, daß in einer solchen Anschauung Wahrheit ist."
      ],
      [
        "Vielleicht ist gerade das Thema von den «Volksseelen» ein solches, das zeigt, wie geistige Betrachtung, die auf die wirkliche übersinnliche Wesenheit des Daseins geht, zugleich die wahrhaft praktische Lebens­anschauung gibt, die Licht wirft auch auf die einzelnsten Fragen des Lebens.",
        "Eine Lebensbetrachtung, die für die Entwickelung und das Wesen der Völker nur solche Vorstellungen gebraucht, die für die Naturwissenschaft mit Recht geltend gemacht werden, kann das nicht.",
        "Diese mechanistisch-physische Wissenschaft hat ihr Großes geleistet in der Hervorbringung mechanisch-physikalisch-chemischer Kultur-mittel; für die Kulturmittel des geistigen Lebens der Menschheit bedarf es einer auf das Geistige hingeordneten Wissenschaft.",
        "Unsere Zeit bedarf einer solchen Wissenschaft."
      ],
      [
        "Berlin, 8.",
        "Februar 1918.",
        "Rudolf Steiner"
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ERSTER VORTRAG Kristiania, 7.Juni 1910",
    "paragraphs": [
      "Es gereicht mir zu großer Befriedigung, nun schon das dritte Mal in etwas längeren Ausführungen zu unsern Freunden hier in Norwegen sprechen zu können, und ich möchte auf die lieben Worte unseres lieben Freundes Eriksen nur ganz kurz sagen, daß die Worte herzlicher Begrü­ßung, die er soeben ausgesprochen hat, ebenso herzlich und aus ebenso tiefen Gründen der Seele heraus, wie sie gesprochen worden sind, von mir erwidert werden.",
      "Ich hoffe, daß auch dieser Vortragszyklus, den ich nunmehr vor Ihnen beginnen möchte, einiges beitragen kann zu der Erkenntnis von dem, was wir das Gesamtbild unserer Weltanschauung nennen. Ich möchte gerade bei diesem Vortragszyklus darauf aufmerksam machen, daß er ja in seinem Verlaufe mancherlei enthalten muß, was sozusagen zu den einschneidendsten Wahrheiten unserer Weltanschauung gehört, daß er einiges von dem wird enthalten müssen, was eigentlich dem gegenwärtigen menschlichen Denken noch ziemlich fern liegt. Daher bitte ich vor allen Dingen diejenigen der verehrten Freunde, welche sich mit den weitergehenden Fragen der geisteswissenschaftlichen Weltan­schauung weniger befaßt haben, darauf Rücksicht zu nehmen, daß wir ja nicht vorwärts kommen würden auf unserm Felde, wenn wir nicht von Zeit zu Zeit immer wieder einen kräftigen Ruck, einen kräftigen Sprung in diejenigen Partien geistiger Erkenntnis tun würden, welche gerade dem gegenwärtigen menschlichen Denken, Fühlen und Empfin­den eigentlich ziemlich fern liegen.",
      "Von diesem Gesichtspunkte aus wird manchmal den Ausführungen gegenüber ein gewisser guter Wille notwendig sein; denn um alles das herbeizutragen, was herbeigetragen werden müßte an Belegen und Be­weisen für dasjenige, was in den nächsten Tagen von dieser Stelle aus gesprochen werden wird, dazu gehört eine viel längere Zeit. Wir wür­den nicht vorwärts kommen, wenn nicht gerade diesen Ausführungen gegenüber sozusagen etwas appelliert würde an den guten Willen, an das Entgegenkommen spirituellen Verständnisses. Es ist in der Tat das",
      "Gebiet, welches wir hiermit berühren, ein solches, das so ziemlich bis in unsere Zeiten hinein gerade von Okkultisten, gerade von Mystikern und Theosophen gemieden worden ist, und zwar gemieden worden ist aus dem Grunde, weil ein höherer Grad von Vorurteilslosigkeit not­wendig ist, um die Dinge, die zu sagen sind, gewissermaßen ohne Widerstreben, das manchmal auftauchen könnte, entgegenzunehmen.",
      "Wie das gemeint ist, wird Ihnen vielleicht am verständlichsten wer­den, wenn Sie sich erinnern, daß man in einem gewissen Grad mysti­scher oder okkulter Entwickelung ein heimatloser Mensch genannt wird. Es ist dies geradezu ein technischer Ausdruck, «heimatloser Mensch», und wenn wir ohne Umschweife - da wir nicht über den Pfad der Erkenntnis sprechen - charakterisieren wollen, was mit dem Worte «heimatloser Mensch» gemeint ist, so können wir kurz sagen, daß derjenige ein heimatloser Mensch genannt wird, der in seiner Er­kenntnis, seiner Auffassung der großen Menschheitsgesetze in Wahrheit unbeeinflußbar ist von alledem, was sonst im Menschen aufsteigt aus dem Ort, an dem er in Gemäßheit seines Volkstums lebt. Ein heimat­loser Mensch, können wir auch sagen, ist derjenige, welcher die große Mission der Gesamtmenschheit in sich aufzunehmen vermag, ohne daß sich die Nuancen der besondern Gefühle und Empfindungen einmi­schen, die aus diesem oder jenem Heimatboden herauswachsen. Sie sehen daraus, daß zu einem gewissen Reifegrad mystischer oder okkul­ter Entwickelung ein freier Gesichtspunkt gerade gegenüber demjeni­gen gehört, was wir mit Recht sonst als etwas Großes betrachten, was wir anderseits dem einzelnen Menschenleben gegenüber als die Mission der einzelnen Volksgeister, als dasjenige bezeichnen, was aus dem Untergrunde eines Volksbodens, aus dem Geiste der Völker heraus die einzelnen konkreten Beiträge zu der gesamten Mission der Menschheit liefert.",
      "Schildern wollen wir also sozusagen das Große dessen, wovon der heimatlose Mensch in gewisser Beziehung frei werden muß. Nun haben die heimatlosen Menschen aller Zeiten, von den Urzeiten angefangen bis in unsere Tage hinein, immer gewußt, daß, wenn sie sozusagen in vollem Umfange charakterisieren würden dasjenige, was man als den Charakter der Heimatlosigkeit bezeichnet, sie dann wenig, sehr wenig",
      "Verständnis finden würden. Es würde zunächst einmal das Vorurteil diesen heimatlosen Menschen entgegengebracht werden, das sich in dem Vorwurfe ausdrücken würde: Ihr habt ja allen Zusammenhang mit dem Mutterboden des Volkstums verloren; Ihr habt ja kein Verständnis für das, was den Menschen sonst das Teuerste ist. - Nun ist es aber nicht so.",
      "Heimatlosigkeit ist in gewisser Beziehung doch im Grunde genom­men - oder kann es wenigstens sein - ein Umweg, um, nachdem diese heilige Stätte, diese Heimatlosigkeit erreicht ist, wieder den Rückweg zu finden zu den Volkssubstanzen, den Einklang zu finden mit dem Bodenständigen in der Menschheitsentwickelung. Wenn darauf von vornherein aufmerksam gemacht werden muß, so ist es auf der andern Seite doch nicht unbegründet, daß gerade in unserer Zeit in unbefan­genster Weise auch einmal über dasjenige gesprochen wird, was wir die Mission der einzelnen Volksseelen der Menschheit nennen.",
      "Ebenso, wie es begründet ist, daß bisher sozusagen bis zu einem gewissen Grade von dieser Mission ganz geschwiegen wurde, ebenso begründet ist es, in unserer Gegenwart damit zu beginnen, von dieser Mission zu reden. Es ist aus dem Grunde von einer ganz besonderen Wichtigkeit, weil die nächsten Schicksale der Menschheit in einem viel höheren Grade als das bisher der Fall war, die Menschen zu einer gemeinsamen Menschheits­mission zusammenführen werden.",
      "Zu dieser gemeinsamen Mission wer­den aber die einzelnen Volksangehörigen nur dann ihren entsprechen­den freien, konkreten Beitrag liefern können, wenn sie vor allen Dingen ein Verständnis haben für ihr Volkstum, ein Verständnis für dasjenige, was man nennen könnte «Selbsterkenntnis des Volkstums». Wenn im alten Griechenland in den apollinischen Mysterien der Satz: «Erkenne dich selbst» eine große Rolle gespielt hat, so wird in einer nicht zu fernen Zukunft der Ausspruch an die Volksseelen gerichtet werden:",
      "«Erkennet euch selbst als Volksseelen.» Dieser Spruch wird eine gewisse Bedeutung haben für das Zukunftswirken der Menschheit.",
      "Nun wird es unserer Zeit schon ganz besonders schwer, Wesenheiten anzuerkennen, welche für die äußere sinnliche Wahrnehmung, für die äußere materielle Erkenntnis sozusagen gar nicht da sind. Es wird ja vielleicht nicht so schwierig sein für unsere Gegenwart, anzuerkennen, daß der Mensch, so wie er in der Welt vor uns steht, gewisse Glieder,",
      "gewisse Teile seiner Wesenheit hat, die übersinnlich, unsichtbar sind. Es wird sich vielleicht der gegenwärtige materialistische Sinn der Menschheit noch leichter zu dieser Anschauung führen lassen, daß We­senheiten, die man wenigstens nach ihrer Außenseite hin physisch sehen kann, wie die Menschen, auch einen übersinnlichen, unsichtbaren Teil haben.",
      "Aber eine starke Zumutung ist es für unsere Gegenwart, wenn man zu ihr sprechen soll von Wesenheiten, die eigentlich nach gewöhn­licher Anschauung gar nicht da sind. Denn was ist es eigentlich, was man heute da oder dort Volksseele, Volksgeist nennt?",
      "Es ist höchstens das, was man gelten läßt als eine Eigenschaft, als eine gemeinschaftliche Eigenschaft von so und so vielen hundert Menschen oder Millionen von Menschen, die auf einem gewissen Boden zusammengedrängt sind. Daß irgend etwas, was da lebt außer den vielen Millionen Menschen, die auf dem Boden zusammengedrängt sind, daß irgend etwas Reales, das sich decken würde mit dem Begriff Volksgeist, diesem Begriffe zugrunde liegt, das ist schwer für ein Bewußtsein unserer gegenwärtigen Zeit klar zu machen.",
      "Wenn man fragen würde - sagen wir jetzt, um etwas ganz Neutrales zu haben-: Was versteht der gegenwärtige Mensch unter dem schweizerischen Volksgeist? - da würde er in abstrakten Ausdrücken einige Eigenschaften beschreiben, welche diejenigen Menschen haben, welche das schweizerische Gebiet der Alpen und des Jura bewohnen, und wird sich klar darüber sein, daß dem nicht etwas entspricht, was man mit äußeren Erkenntniskräften, mit Augen oder sonstigen Wahr­nehmungsorganen erkennen könnte. Das muß das erste sein, daß man in offener und ehrlicher Weise sich den Gedanken bilden kann, daß es Wesenheiten gibt, die sich ohne weiteres eigentlich nicht sinnlich äu­ßern, dem gewöhnlichen materiellen Wahrnehmungsvermögen sich nicht darbieten, daß es sozusagen zwischen den Wesen, die sinnlich wahrnehmbar sind, andere unsichtbar wirkende Wesenheiten gibt, die hereinwirken in sichtbare Wesenheiten, wie die menschliche Wesenheit in die menschlichen Hände oder menschlichen Finger, daß man also sprechen kann von dem schweizerischen Volksgeist wie von dem Geiste eines Menschen, und daß man diesen Geist des Menschen ebenso genau von dem unterscheiden kann, was man in den zehn Fingern vor sich hat, wie man den schweizerischen Volksgeist unterscheiden kann von",
      "den Millionen von Menschen, die in den Bergen der Schweiz leben. Er ist noch etwas anderes, nämlich eine Wesenheit, wie der Mensch selber eine Wesenheit ist. Nur unterscheiden sich die Menschen davon da­durch, daß sie dem Wahrnehmungsvermögen des Menschen eine sinn­liche Außenseite darbieten. In demselben Maße, wie sich der Mensch dem sinnlichen Wahrnehmungsvermögen darbietet, bietet eine äußere Erscheinung, etwas, was man mit Empfindungsorganen oder äußeren Sinnen sehen oder wahrnehmen kann, ein Volksgeist nicht dar, aber er ist dennoch eine durchaus reale Wesenheit.",
      "Heute wird es sich darum handeln, uns gewissermaßen eine Vorstel­lung zu bilden von einer solchen realen Wesenheit. Wie machen wir das überhaupt in der Geisteswissenschaft, wenn wir uns von einer realen Wesenheit eine Vorstellung bilden wollen?",
      "Ein charakteristisches Bei­spiel, wie wir uns eine Vorstellung bilden von einer realen Wesenheit, gewinnen wir, wenn wir zuerst einmal den Blick auf das Wesen des Menschen werfen. Wenn wir geisteswissenschaftlich den Menschen be­schreiben, unterscheiden wir an ihm den physischen Leib, den Äther-oder Lebensleib, den Astralleib oder Empfindungsleib und das, was wir als das höchste Glied der menschlichen Wesenheit betrachten, das Ich.",
      "Wir wissen also, daß wir in dem, was wir physischen Leib, Atherleib, Astralleib und Ich nennen, sozusagen den gegenwärtigen Menschen vor uns haben. Sie wissen aber auch, daß wir auf eine Entwickelung der Menschheit in der Zukunft hinblicken, und daß das Ich an den drei nie­deren Gliedern der menschlichen Wesenheit arbeitet, sodaß es dieseGlie­der vergeistigt, umarbeitet von der gegenwärtigen niederen in die zu­künftige höhere Form.",
      "Das Ich wird das Astrale umarbeiten, umformen, so daß es etwas anderes werden wird, als was es heute schon ist. Der Astralleib wird dann darstellen das, was Sie unter dem Namen Geist-selbst oder Manas kennen.",
      "Ebenso wird eine noch höhere Arbeit des Ich an dem Atherleibe oder Lebensleibe geleistet werden dadurch, daß es ihn umarbeitet und umprägt in das, was wir Lebensgeist oder Budhi nennen. Und endlich ist die höchste Arbeit des Menschen, die wir uns vorläufig denken können, die, daß der Mensch das widerstrebendste Glied seiner Wesenheit, den physischen Leib vergeistigen, umwandeln und metamorphosieren wird in das Geistige.",
      "Es wird das höchste Glied",
      "der menschlichen Wesenheit sein, wenn das Ich umgestaltet haben wird das, was heute physischer Leib ist, das, was heute uns am gröbsten und materiellsten entgegentritt, wenn das Ich es umgestaltet haben wird in den Geistesmenschen oder Atma. So blicken wir auf drei Glieder der menschlichen Natur, die sich in der Vergangenheit entwickelt haben, auf eines, in dem wir jetzt darinnen stehen, und auf drei andere, aus denen das Ich etwas Neues in der Zukunft machen wird.",
      "Wir wissen auch, daß zwischen der Arbeit, die verflossen ist, und zwischen der Arbeit, die in der Zukunft verfließen wird, um die drei höheren Glieder zu bilden, etwas dazwischen liegt. Wir wissen, daß wir das Ich selber gegliedert uns denken müssen. Es arbeitet an einer Art von Zwischenwesenheit. Wir sprechen daher davon, daß zwischen dem Astralleibe, wie er aus der Vergangenheit dem Menschen geworden ist, und dem Geistselbst oder Manas, das aus diesem Astralleib in ferner Zukunft dem Menschen werden wird, in der Mitte darinnen liegen die drei vorbereitenden Glieder; das sind: die Empfindungsseele, das nie­derste Glied, in dem das Ich gearbeitet hat, die Verstandes- oder Gemütsseele und die Bewußtseinsseele. So daß wir sagen können:",
      "Von dem, was wir herausarbeiten als Geistselbst oder Manas, von dem ist außerordentlich wenig heute beim Menschen vorhanden, höchstens der Anfang. Dagegen hat sich der Mensch dadurch zu dieser künftigen Arbeit vorbereitet, daß er seine drei niederen Glieder in einer gewissen Weise, in gewissem Maße hat beherrschen gelernt. Er hat sich vorberei­tet dadurch, daß er den Empfindungs leib oder den astralischen Leib hat beherrschen gelernt, indem er mit seinem Ich in denselben eingedrungen ist und innerhalb des Empfindungsleibes die Empfindungsseele heraus­gebildet hat. Ebenso wie die Empfindungsseele in einem gewissen Ver­hältnis zum Empfindungsleibe steht, so steht die Verstandes- oder Gemütsseele in einem gewissen Verhältnis zum Äther- oder Lebensleibe, so daß die Verstandes- oder Gemütsseele ein schwaches Vorbild dessen ist, was der Lebensgeist oder Buddhi sein wird, zwar ein schwaches Vor­bild, aber doch ein Vorbild. Und das, was in der Bewußtseinsseele sich befindet, ist in gewisser Weise von dem Ich hineingearbeitet in den physischen Leib. Daher ist sie ein schwaches Vorbild dessen, was einst Geistesmensch oder Atma sein wird. Wir können auch sagen: Gegenwärtig",
      "erkennen wir am Menschen, wenn wir absehen von geringfügigen Teilen, die er schon aus dem astralischen Leibe herausgearbeitet hat als Anfang des Geistselbstes oder Manas, vier verschiedene Glieder. Wir können heute unterscheiden:",
      "1.    den physischen Leib,",
      "2.    den Ätherleib,",
      "3.    den Astralleib,",
      "4.    das in demselben arbeitende Ich,",
      "und ferner, wie ein Vorglanz zu den höheren Gliedern:",
      "die Empfindungsseele,",
      "die Verstandesseele,",
      "die Bewußtseinsseele.",
      "Da haben wir den Menschen als eine Wesenheit vor uns, wie er sich uns heute darbietet, und da erfassen wir sozusagen diesen Menschen in dem gegenwärtigen Augenblicke seines Werdens. Wir sehen förmlich das Ich herausarbeiten, nachdem als Vorbereitung ihm geworden ist die Empfindungs-, Verstandes- und Bewußtseinsseele, die höheren Glieder. Wir sehen dieses Ich arbeiten mit den Kräften der Empfindungs-, Ver­standes- und Bewußtseinsseele an dem astralischen Leibe, an den An­fängen des Geistselbstes. Wir sehen den Menschen gegenwärtig in diesem Momente seines Arbeitens.",
      "Diejenigen - und es werden die meisten von Ihnen sein -, die sich mit dem befaßt haben, was wir die Erforschung der Akashachronik nennen, mit der Entwickelung des Menschen in urferner Vergangenheit und mit dem Ausblick in die ferne Zukunft, die werden wissen, daß die Menschen, wie ich sie Ihnen skizzenhaft charakterisieren konnte, sich entwickelt haben, daß wir zurückschauen können in ferne Vergangen­heit, daß die Menschen lange Entwickelungsepochen gebraucht haben, um die erste Anlage ihres physischen Leibes, dann die erste Anlage des Ätherleibes und endlich des Astralleibes zu bilden und diese drei Glie­der dann weiter zu entwickeln. Der Mensch hat dazu lange Zeiträume gebraucht, und Sie wissen vielleicht auch, daß der Mensch die frühere Entwickelung seines Wesens, zum Beispiel die Entwickelung seines astralischen Leibes, nicht in demselben Zustande der Erde durchge­macht hat, in dem die Erde heute ist, sondern daß er seinen astralischen",
      "Leib entwickelt hat in einem früheren Zustande des Erdendaseins, dem Monden dasein. Wie wir das heutige Leben als die Folge früherer Erden-leben, früherer Verkörperungen erkennen, so blicken wir auch auf frühere Verkörperungen unserer Erde zurück. Das, was wir Empfin­dungsseele, Verstandes- oder Gemütsseele nennen, wurde erst in dem heutigen Erdendasein gebildet. In dem Mondendasein wurde der astra­lische Leib eingepflanzt, und in einem noch früheren Dasein unserer Erde, dem Sonnenzustande, wurde der Ätherleib eingepflanzt und endlich während des Saturnzustandes der physische Leib. So daß wir auf drei Verkörperungen der Erde zurückblicken, und auf jeder dieser Verkörperungen sehen wir eines der Glieder, die der Mensch heute in sich trägt, zuerst veranlagt und dann weiter ausgebildet.",
      "Noch etwas anderes ist zu betonen, wenn wir von dem Saturn-, Sonnen-, Monden-Zustande reden. Genau so, wie wir als Menschen auf der Erde den Zustand durchmachen, den wir den selbstbewußten Menschheitszustand nennen können. so haben während früherer Zu­stände unserer Erdenentwickelung, während des alten Monden-, Son­nen- und Saturnzustandes andere Wesen die Stufe durchgemacht, die wir heute auf der Erde durchmachen.",
      "Es ist dabei ziemlich gleichgültig, ob man mit der Terminologie, die man im Orient gebraucht, oder mit derjenigen, die mehr im Okzident üblich ist, die Wesenheiten benennt. Diejenigen Wesenheiten, die während des Mondenzustandes unserer Er­de auf der Stufe standen, auf der der Mensch heute steht, und die die nächsthöheren Wesenheiten sind, die über uns stehen, nennen wir in der Terminologie der christlichen Esoterik Angeloi oder Engel.",
      "Sie stehen eine Stufe höher als der Mensch, weil sie um eine Epoche früher ihre Menschheitsstufe absolviert haben, so daß diese Wesenheiten dasjenige, was wir heute sind, dazumal während des alten Mondenzustandes waren. Sie waren es aber nicht so, daß sie damals auf dem Monde herumgegangen wären wie die Menschen heute auf der Erde.",
      "Sie waren Wesenheiten auf der Menschheitsstufe, aber sie lebten nicht im Fleische wie der Mensch heute. So entsprach nur ihre Stufe der Entwickelung dem Menschsein, das der Mensch heute durchmacht. Ebenso finden wir Wesenheiten noch höherer Art, welche während des alten Sonnenzu­standes die Menschheitsentwickelung durchgemacht haben.",
      "Es sind die",
      "Archangeloi oder Erzengel. Das sind Wesenheiten, die zwei Stufen höher stehen als der Mensch, die zwei Epochen früher ihre Menschheits­stufe durchgemacht haben. Wenn wir noch weiter zurückgehen bis zur ersten Verkörperung unseres Erdendaseins, bis zum Saturnzustand, da finden wir, daß da diejenigen Wesenheiten ihre Menschheitsstufe durchgemacht haben, die wir als Geister der Persönlichkeit, Archai, Urbeginne bezeichnen, so daß wir, wenn wir bei diesen Wesenheiten beginnen - die also in urferner Vergangenheit, während des alten Sa­turnzustandes Menschen waren - und dann die Verkörperungen der Erde verfolgen bis auf unseren Zeitpunkt, vor uns haben die Entwik­kelungsstufen der Wesen bis herunter zu unserer Wesenheit. Wir können also sagen: Urbeginne, Archai waren Menschen auf dem alten Saturn; Erzengel, Archangeloi waren Menschen auf der alten Sonne; Engel oder Angeloi waren Menschen auf dem alten Mond; Menschen sind Menschen auf unserer Erde.",
      "Da wir nun wissen, daß wir in der Zukunft unsere Entwickelung weiterführen, dasjenige, was unsere niederen Glieder sind, weiter ent­falten, also dasjenige, was heute unser astralischer Leib, unser Äther-oder Lebensleib und unser physischer Leib ist, so müssen wir doch fragen: Ist es nicht ebenso natürlich, daß die Wesenheiten, die früher die Menschheitsstufe durchgemacht haben, jetzt schon auf der Stufe sind, wo sie umarbeiten ihren astralischen Leib in das Geistselbst oder Manas? Wie wir während der nächsten Verkörperung unserer Erde -während des Jupiter-Daseins - fertig werden mit der Umgestaltung unseres Astralleibes in Geistselbst oder Manas, so sind fertig geworden diejenigen Wesenheiten, die während der Mondepoche Menschen wa­ren, die Angeloi, mit der Umgestaltung ihrer Astralleiber in Geistselbst oder Manas, oder sie werden damit während unseres Erdendaseins fertig werden. Sie machen das durch während unserer Erdenverkörpe­rung, was wir erst während der nächsten Verkörperung der Erde werden durchzumachen haben. Blicken wir noch weiter zurück auf die Wesen, die während des alten Sonnendaseins Menschen waren, so kön­nen wir sagen: Sie haben schon während des Mondenzustandes das durchmachen müssen, was wir erst in der nächsten Erdenverkörperung werden durchmachen müssen. Sie stehen bei der Arbeit, die der Mensch",
      "ausführen wird, wenn er mit seinem Ich umarbeitet seinen Äther- oder Lebensleib in Lebensgeist oder Buddhi. Wir haben also in diesen Archan­geloi, in diesen Erzengeln Wesenheiten, die zwei Stufen über uns stehen, die auf der Stufe stehen, die wir einst erreichen werden, wenn wir von unserem Ich aus umarbeiten werden den Lebensleib in Lebensgeist oder Buddhi. Wir blicken, wenn wir zu diesen Wesenheiten aufschauen, so zu ihnen auf, daß wir sagen: Wir sehen in ihnen Wesenheiten, die zwei Stufen über uns stehen, Wesenheiten, in denen wir gleichsam voraus-genommen sehen, was wir selber in Zukunft erleben werden; wir blicken zu ihnen auf als zu solchen Wesen, die heute arbeiten an ihrem Äther- oder Lebensleib und ihn umformen zu Lebensgeist oder Buddhi. Ebenso blicken wir auf zu noch höheren Wesenheiten, zu den Geistern der Persönlichkeit. Sie stehen auf einer noch höheren Stufe als die Erz­engel, auf einer Stufe, die der Mensch erreichen wird in noch fernerer Zukunft, wenn er wird umarbeiten können den physischen Leib in Atma oder Geistesmensch.",
      "So wahr der Mensch auf der jetzigen Stufe seines Daseins ist, so wahr sind diese entsprechenden Wesenheiten auf den eben charakterisierten Stufen ihres Daseins, so wahr stehen sie über uns, so wahr sind sie Realitäten. Nun steht ihre Realität nicht etwa fern dem Erdendasein, sondern greift vielmehr in dasselbe ein, wirkt hinein in unser Menschen-dasein. Wir müssen uns jetzt nur fragen: Wie wirken diese über dem Menschen stehenden Wesenheiten in unser Menschheitsdasein hinein? Wenn wir uns dieses Hineinwirken begreiflich machen wollen, dann mussen wir darauf Rücksicht nehmen, daß solche Wesenheiten sozu­sagen in ihrer Arbeit einen anderen geistigen Anblick darbieten werden als diejenigen Wesenheiten, die wir heute Menschen nennen. Es ist in der Tat ein beträchtlicher Unterschied zwischen diesen Wesenheiten, die über dem Menschen stehen, und denjenigen Wesenheiten, die heute erst auf der Menschheitsstufe sich befinden. So sonderbar das jetzt auch klingen mag, es wird Ihnen im Laufe der nächsten Tage noch vollstän­dig klar werden. Es ist doch durchaus aus wirklicher Geistesforschung heraus gesprochen: Der Mensch, wie er heute ist, ist gewissermaßen in einem Mittelzustand seines Daseins. So wie heute sein Ich an seinen niederen Gliedern arbeitet, wird es nicht immer bleiben. Es ist gleichsam",
      "das ganze menschliche Wesen heute wie in sich zusammenhängend, und es bildet gleichsam eine durch nichts unterbrochene Wesenheit. Das kann in der Zukunft der Menschheitsentwickelung anders werden, und es wird wesentlich anders werden. Wenn der Mensch einmal so weit sein wird, daß er mit vollem Bewußtsein an seinem Astralleib arbeiten und mit seinem Ich diesen Astralleib in Geistselbst oder Manas umar­beiten wird, dann wird ein ähnlicher Zustand bei vollem Bewußtsein vorhanden sein, wie er jetzt beim Unbewußtsein oder Unterbewußtsein des Menschen im Schlafe vorhanden ist.",
      "Stellen Sie sich einmal den Schlafzustand des Menschen vor. Der Mensch rückt beim Schlafzustand in bezug auf seinen Astralleib und sein Ich aus seinem physischen Leib und seinem Ätherleib heraus, er läßt sie im Bette liegen und schwebt dann gleichsam außerhalb des physischen und Ätherleibes Denken Sie sich jetzt in diesem Zustande den Menschen so, daß das Bewußtsein erwacht: Ich bin ein Ich, - daß es so erwacht in diesem Geistesleib, wie es im tagwachen Bewußtseins­zustande da ist.",
      "Was würde der Mensch schon gegenwärtig für einen merkwürdigen Anblick für sich selber darbieten! Er würde an einer Stelle fühlen: «Da bin ich», und vielleicht da unten, weit weg von dieser ersteren Stelle: «Da ist mein physischer Leib und mein Ätherleib; sie sind an jenem Orte und sie gehören zu mir, aber ich mit meinen anderen Gliedern, ich schwebe außerhalb, da oben».",
      "Wenn der Mensch heute bewußt wird in seinem Astralleibe, außerhalb seines physischen und Ätherleibes, dann kann er allerdings - und wenn er heute auf der Erde sozusagen noch so hoch entwickelt ist - nichts anderes tun, als frei in seinem Astralleibe sich da- oder dorthin bewegen und kann unabhängig von seinem physischen Leibe da oder dort in der Welt tätig sein, aber das kann er dann noch nicht mit seinem physischen und Ätherleibe. Man wird sie aber in ferner Zukunft auch von einer Stätte des Nordens von Europa zum Beispiel von außen hingeleiten können nach einer anderen Stätte, ihnen befehlen: Geht weiter! und sie dann in ihrer Be­wegung von außen lenken.",
      "Das geht heute noch nicht. Das wird aber der Mensch können, wenn er sich über die Stufe der Erdenentwickelung zu der Jupiterstufe entwickelt haben wird, zu der folgenden Entwik­kelungsstufe unseres Erdenplaneten.",
      "Das wird auch der folgende Entwickelungszustand",
      "des Menschen sein. Wir werden dann fühlen, daß wir gewissermaßen für uns selbst der Dirigent von außen sein werden. Das ist das Wesentliche. Und das führt zu einer Spaltung von dem, was wir heute die menschliche Wesenheit genannt haben.",
      "Das materialistische Bewußtsein kann damit allerdings nicht viel anfangen. Es kann nicht verfolgen dasjenige, was heute schon in gewis­ser Beziehung real in der Außenwelt wirkt in ähnlicher Weise, wie es eininal in der Zukunft beim Menschenwesen vorhanden sein wird.",
      "Solche Erscheinungen sind schon heute da. Die Menschen könnten sie wahrnehmen, wenn sie acht geben würden. Sie würden dann sehen, daß es gewisse Wesenheiten gibt, die zum Beispiel zu früh sich so entwickelt haben.",
      "Wie der Mensch, wenn er den richtigen Zeitpunkt abwartet, im richtigen Zeitpunkt den Jupiterzustand erreichen wird, so daß er leiten kann seinen physischen und ätherischen Leib, so gibt es auch Wesen, welche in gewisser Beziehung sich vorschnell entwickelt haben, ohne den richtigen Zeitpunkt abgewartet zu haben. Solche vorzeitig entwik­kelte Wesenheiten haben wir in unserer Vogelwelt, und zwar in solchen Wesenheiten der Vogelwelt, welche jedes Jahr die großen Wanderzüge über die Erde vollführen.",
      "Da ist es die sogenannte Gruppenseele, welche mit dem ätherischen Leibe eines jeden Vogels zusammenhängt. So wie die Gruppenseele die regelmäßigen Wanderzüge der Vögel über die Erde hin dirigiert, so wird der Mensch, nachdem er sein Geistselbst oder Manas entwickelt hat, das, was wir physischen und ätherischen Leib nennen, befehligen, ihnen gebieten, sie in Bewegung setzen.",
      "In einem noch höheren Sinne wird der Mensch diese dirigieren, von außen in Bewegung setzen können, wenn er einmal so weit entwickelt sein wird, daß er auch noch umarbeitend in bezug auf den Äther- oder Lebensleib wirkt. Solche Wesenheiten, die das schon können, gibt es schon heute.",
      "Das sind die Archangeloi oder Erzengel. Das sind Wesenheiten, die das bereits können, was der Mensch einmal können wird, Wesenheiten, die dasjenige vollbringen können, was man nennen kann «seinen ätheri­schen und seinen physischen Leib von außen dirigieren», die aber außerdem auch noch arbeiten können an ihrem eigenen Ätherleibe.",
      "Bilden Sie sich als Idee den Begriff von Wesenheiten, die sozusagen im Umkreis unserer Erde wirken, die in der geistigen Atmosphäre",
      "unserer Erde enthalten sind mit ihrem Ich, die von diesem ihrem Ich aus schon umgewandelt haben ihren astralischen Leib, so daß sie ein vollentwickeltes Geistselbst oder Manas besitzen, die aber jetzt mit diesem vollentwickelten Geistselbst oder Manas weiterwirken auf unserer Erde und hereinarbeiten in die Menschen, indem sie unseren Äther- oder Lebensleib umgestalten; Wesenheiten, die auf der Stufe stehen, auf welcher sie den Äther- oder Lebensleib zu Buddhi oder Lebensgeist umgestalten. Wenn Sie sich solche Wesenheiten denken, die also auf der Stufe der geistigen Hierarchien stehen, die wir Erzengel nennen, haben Sie einen Begriff von dem, was man «Volksgeister» nennt, was man die dirigierenden Volksgeister der Erde nennt. Die Volksgeister gehören in die Stufe der Archangeloi oder Erzengel. Wir werden sehen, wie sie ihrerseits den Äther- oder Lebensleib dirigieren, und wie sie dadurch wieder hineinwirken in die Menschheit und diese in ihre eigene Tätigkeit einbeziehen. Wenn wir die verschiedenen Völ­ker unserer Erde betrachten und einzelne herausheben, dann werden wir in dem eigentümlichen Weben und Leben dieser Völker, in dem, was wir die besonderen, charakteristischen Eigenschaften dieser Völker nennen, ein Abbild von dem haben, was wir als die Mission der Volks-geister betrachten können.",
      "Wenn wir die Mission dieser Wesenheiten erkennen - Inspiratoren der Völker sind diese Wesenheiten -, dann können wir sagen, was ein Volk ist. Ein Volk ist eine zusammengehörige Gruppe von Menschen, welche von einem der Archangeloi, einem der Erzengel geleitet wird. Die einzelnen Glieder eines Volkes bekommen das, was sie als Glieder des Volkes tun, was sie als Glieder des Volkes vollführen, von einer solchen Seite her inspiriert. Dadurch, daß wir uns vorstellen, daß diese Volksgeister individuell verschieden sind, wie die Menschen auf unserer Erde, werden wir es begreiflich finden, daß die einzelnen verschiedenen Gruppen der Völker die individuelle Mission dieser Archangeloi sind. Wenn wir uns einmal geistig veranschaulichen, wie in der Weltge­schichte Volk nach Volk und auch Volk neben Volk wirkt, so können wir jetzt, wenigstens in abstrakter Form - die Form wird immer kon­kreter und konkreter werden in den nächsten Vorträgen - uns vorstel­len, daß alles, was da vor sich geht, inspiriert ist von diesen geistigen",
      "Wesenheiten. Aber eines wird uns wohl leicht vor die Seele treten können: daß neben diesem Wirken von Volk nach Volk noch etwas anderes stattfindet in der Menschheitsentwickelung. Sie können, wenn Sie jenen Zeitraum überblicken, den wir von der großen atlantischen Katastrophe aus rechnen, die das Antlitz der Erde so weit verändert hat, daß jener Kontinent, der bestanden hat zwischen dem heutigen Afrika, Amerika und Europa, in jener Zeit untergegangen ist, die Zeit­räume unterscheiden, in welchen die großen Völker gewirkt haben, bei denen die nachatlantischen Kulturen herauskamen: die alte indische, die persische, die ägyptisch-chaldäische, die griechisch-lateinische und unsere gegenwärtige Kultur, die nach einiger Zeit in die sechste Kultur-epoche übergehen wird.",
      "Wir bemerken auch, daß nacheinander darin gewirkt haben verschiedene Völkerinspiratoren. Wir wissen, daß noch lange die ägyptisch-chaldäische Kultur gewirkt hat, als die griechische Kultur schon ihren Anfang nahm, und daß die griechische Kultur noch weiter waltete, als die römische schon ihren Anfang genommen hatte.",
      "So können wir die Völker nebeneinander und nacheinander betrachten. Aber in allem, was sich in und mit den Völkern entwickelt, entwickelt sich noch etwas anderes. Es ist ein Fortschritt in der menschlichen Ent­wickelung.",
      "Es kommt dabei nicht in Betracht, ob wir das eine höher oder niedriger stellen. Es kann zum Beispiel einer sagen: Mir gefällt die indische Kultur am besten. Das mag ein persönliches Urteil sein. Wer aber nicht auf persönliche Urteile schwört, der wird sagen: Es ist gleichgültig, wie wir die Dinge bewerten; der notwendige Gang führt die Menschheit vorwärts, mag man das später auch Niedergang nennen.",
      "Die Notwendigkeit führt die Menschheit vorwärts. Wenn wir die ver­schiedenen Zeiträume vergleichen, 5000 Jahre vor Christus, 3000 Jahre vor Christus und 1000 Jahre nach Christus, dann ist etwas noch da, was über die Volksgeister hinübergreift, etwas, woran die verschiedenen Volksgeister teilnehmen.",
      "Sie brauchen das nur in unserer Zeit ins Auge zu fassen. Woher kommt es, daß in diesem Saale so viele Menschen zusammensitzen können, die aus den verschiedensten Volksgebieten herkommen und sich verstehen und sich zu verstehen versuchen in bezug auf das Allerwichtigste, was sie hier zusammengeführt hat?",
      "Die verschiedenen Menschen kommen aus dem Bereich der verschiedensten",
      "Volksgeister heraus, und dennoch gibt es etwas, worin sie sich verste­hen. In ähnlicher Weise verstanden sich und konnten sich verstehen in damaliger Zeit die verschiedenen Völker untereinander, weil es in jeder Zeit etwas gibt, was die Volksseele übergreift, die verschiedenen Volks­seelen zusammenführen kann, etwas, was man überall mehr oder weni­ger versteht. Das ist dasjenige, was man mit dem recht schlechten, aber gebräuchlichen deutschen Wort «Zeitgeist» benennt oder auch «Geist der Epoche». Der Geist der Epoche, der Zeitgeist, ist ein anderer in der griechischen Zeit, ein anderer in der unsrigen. Diejenigen, welche den Geist in unserer Zeit erfassen, werden zur Theosophie hingetrieben. Das ist das aüs dem Geiste der Epoche über die einzelnen Volksgeister Über­greifende. In derjenigen Zeit, in der Christus Jesus auf der Erde erschien, bezeichnete sein Vorläufer, Johannes der Täufer, den Geist, den man als Zeitgeist bezeichnen könnte, mit den Worten: «Ändert die Verfassung der Seele, denn die Reiche der Himmel sind nahe herbei-gekommen. »",
      "So kann man für jede Epoche den Zeitgeist finden, und das ist etwas, was sich hineinwebt in das Weben der Volksgeister, das wir damit zu gleicher Zeit als das Weben der Archangeloi charakterisiert haben. Für den heutigen materialistischen Menschen ist der Zeitgeist etwas ganz Abstraktes ohne Realität, und noch weniger darf man ihm damit kom­men, in dem Zeitgeist ein wahres Wesen zu sehen. Dennoch verbirgt sich hinter dem Worte «Zeitgeist» eine wirkliche Wesenheit, keine andere Wesenheit als eine solche, die drei Stufen über der Menschheits­stufe steht. Jene Wesenheiten verbergen sich dahinter, die schon auf dem alten Saturn, der am weitesten zurückliegenden Entwickelungs­epoche der Erde, ihre Menschheitsstufe durchmachten, und die heute aus dem geistigen Umkreis der Erde an der Umgestaltung der Erde arbeiten und dabei die letzte Phase sozusagen an der Umgestaltung ihres physischen Leibes in Geistesmensch oder Atma durchmachen. Mit hohen Wesenheiten haben wir es hier zu tun, mit Wesenheiten, gegen­über deren Eigenschaften den Menschen ein Schwindel überkommen möchte. Es sind diejenigen Wesenheiten, die wir wieder bezeichnen könnten als die eigentlichen Inspiratoren - oder wir müssen auf diesem Gebiete sagen, wenn wir mit technischen Ausdrücken des Okkultismus",
      "sprechen wollen -, die Intuitoren des Zeitgeistes oder der Zeitgeister. Sie wirken so, daß sie sich abwechseln und gleichsam einer dem andern die Hand reicht. Von Epoche zu Epoche reichen sie sich ihre Aufgabe zu. Der Geist der Epoche, der während der griechischen Zeit wirkte, reicht weiter die Mission an den, der später wirkt und so weiter. Sie wechseln sich also ab. Es sind, wie wir sahen, eine Anzahl solcher Zeit-geister, solcher Geister der Persönlichkeit, die als Zeitgeist wirken. Sie sind eine höhere Rangordnung gegenüber den Volksgeistern, diese Geister der Persönlichkeit, diese Intuitoren des Zeitgeistes. In jedem Zeitalter wirkt vorzugsweise einer und gibt diesem Zeitalter seine Ge­samtsignatur, gibt seine Aufträge an die Volk sgeister, so daß dasjenige, was der Gesamtgeist der Epoche ist, sich spezialisiert, individualisiert nach den Volksgeistern. Dann wird er abgelöst in der kommenden Epoche von einem andern Zeitgeiste, einem andern Geiste der Persön­lichkeit, einem andern Archë.",
      "Wenn eine gewisse Anzahl von Epochen vorübergegangen ist, dann ist ein Zeitgeist durch die Weiterentwickelung hindurchgegangen. Das mussen wir uns so vorstellen: Wenn wir in unserer Zeit sterben und unsere Entwickelung hier durchgemacht haben, so gibt unsere Persön­lichkeit das Ergebnis dieses Erdenlebens an das nächste Erdenleben weiter. So ist es auch mit den Geistern der Epoche der Fall. In jeder Epoche haben wir einen solchen Geist der Epoche; der gibt am Ende der Epoche sein Amt an seinen Nachfolger ab, dieser wieder an seinen weiteren Nachfolger und so weiter. Die vorangegangenen machen in­zwischen ihre eigene Entwickelung durch, dann kommt derjenige, der am längsten nicht daran gewesen ist, wieder an die Reihe, so daß der­selbe in einer spätern Epoche, während die andern dann ihre eigene Entwickelung durchmachen, als Geist der Epoche wiederkommt und für die fortgeschrittene Menschheit das, was er selber für seine höhere Mission erworben hat, intuierend der Menschheit einflößt. Wir blicken zu diesen Geistern der Persönlichkeit hinauf, zu diesen Wesen, die mit dem sonst so nichtssagenden Worte «Zeitgeist» benannt werden kön­nen, so, daß wir sagen können: Wir Menschen gehen von Inkarnation zu Inkarnation; wir wissen aber ganz genau, daß, indem wir selber von Epoche zu Epoche schreiten, indem wir in die Zukunft sehen, immer",
      "andere Zeitgeister die Geschehnisse unserer Erde regieren. Aber auch unser heutiger Zeitgeist wird wiederkommen, wir werden ihm wieder begegnen. Wegen dieser Eigenschaft dieser Geister der Persönlichkeit, daß sie gleichsam Kreise beschreiben und wieder zu ihrem Ausgangs­punkte zurückkommen, daß sie Zyklen beschreiben, wegen dieser Eigenschaft werden sie auch «Geister der Umlaufszeiten» genannt. -Wir werden diesen Ausdruck noch genauer zu rechtfertigen haben.",
      "Also diese höheren geistigen Wesenheiten, die ihre Befehle ausgeben an die Volksgeister, werden auch Geister der Umlaufszeiten genannt. Es sind damit gemeint jene Umlaufszeiten, die der Mensch selber durch­zumachen hat, indem er von Epoche zu Epoche in gewisser Weise zurückkehrt zu früheren Zuständen und sie in höherer Form wieder­holt. Nun sehen Sie, dieses Wiederholen der Eigentümlichkeiten frühe­rer Formen, das kann Ihnen auffallen. Wenn Sie in geisteswissenschaft­lichem Sinne genau die Entwickelung der Menschheitsstufen auf der Erde durchnehmen, so finden Sie diese wiederholten Geschehnisse in der verschiedensten Weise. So ist eine Wiederholung darin, daß sozu­sagen sieben Epochen sich folgen nach der atlantischen Katastrophe, die wir nennen die nachatlantischen Kulturstufen. Die griechisch-latei­nische Stufe oder Kulturepoche bildet sozusagen den Wendepunkt in unserm Zyklus und erleidet daher keine Wiederholung. Auf diese folgt die Wiederholung der ägyptisch-chaldäischen Epoche, und zwar in unserer eigenen Zeit. Auf diese wird folgen eine andere Epoche, die eine Wiederholung der persischen Zeit sein wird, allerdings in etwas anderer Art, und dann wird die siebente Epoche kommen, die eine Wiederholung der uralt-indischen Kultur, der Epoche der heiligen Rishis sein wird, so daß in dieser Epoche gewisse Dinge in anderer Form heraus kommen werden, die damals veranlagt worden sind. Die Len­kung dieser Geschehnisse obliegt den Zeitgeistern.",
      "Daß nun auf die Erde verteilt in verschiedenen Völkern das ausge­lebt wird, was von Epoche zu Epoche weiterschreitet, daß die verschie­densten Gestalten aus diesem oder jenem Boden gebildet werden, aus dieser oder jener Sprachgemeinschaft herauswachsen, aus dieser oder jener Formensprache, aus Architektur, Kunst und Wissenschaft entste­hen können und alle die Metamorphosen annehmen können und alles",
      "das aufzunehmen vermögen, was der Geist der Epoche der Menschheit einflößen kann, dazu brauchen wir die Volksgeister, die in der Hierar­chie höherer Wesenheiten zu den Erzengeln gehören.",
      "Nun brauchen wir noch eine Vermittlung zwischen der höheren Mission der Volksgeister und denjenigen Wesenheiten, die hier auf der Erde von ihnen inspiriert werden sollen. Sie werden unschwer erkennen können, zunächst in abstrakter Form, daß die Vermittler dieser beiden Geisterarten die Hierarchie der Engel sind. Sie bilden das vermittelnde Glied zwischen Volksgeist und Einzelmensch. Damit der Mensch in sich hineinbekommen kann, was der Volksgeist dem ganzen Volke einzuflößen hat, damit der einzelne Mensch ein Werkzeug werde in der Mission des Volkes, dazu bedarf es dieser Vermittlung zwischen Ein­zelmensch und Erzengel des Volkes.",
      "So haben wir hinaufgeschaut zu den Wesen, welche Mensch gewor­den sind, drei Stufen bevor der Erdenmensch seine Menschheitsstufe erreichte, und haben gesehen, wie sie sich hineinstellen in ihrem Bewußtsein in die Menschheit und eingreifen in unsere Erdenentwicke­lung. Wir werden nun morgen zu zeigen haben, inwiefern das Arbeiten der Erzengel von oben herunter, von ihrem Ich aus, das schon Manas oder Geistselbst ausgebildet hat und am Ätherleib oder Lebensleib des Menschen arbeitet, gerade in den Produktionen, in den Eigenschaften und in dem Charakter eines Volkes sich darlebt. Der Mensch steht darin in dieser Arbeit der höheren Wesenheiten, unmittelbar umgibt sie den Menschen, indem er als Angehöriger eines Volkes in dieselbe hin­eingestellt ist. Der Mensch ist zwar zunächst eine menschliche Indivi­dualität, eine Ausgestaltung einer Ichheit, dann aber ist er nicht nur Individualität, sondern auch Angehöriger eines Volkes und damit etwas, wofür er zunächst als menschliche Individualität nichts kann. Was kann der Mensch, indem er einem bestimmten Volke angehört, dafür, daß er gerade die Sprache dieses Volkes spricht? Das ist nicht eine individuelle Errungenschaft, das gehört auch nicht zu dem, was wir ein individuelles Fortschreiten nennen, das ist das Strombett, in das er aufgenommen wird. Das, was wir menschliches Fortschreiten nen­nen, ist etwas ganz anderes. Indem wir die Volksseele weben und leben sehen, werden wir uns erinnern, worin das Fortschreiten des Menschen",
      "besteht und was der Mensch braucht, um sich durch dasselbe durch­zubewegen. Wir werden sehen, was sozusagen nicht nur zu seiner Ent­wickelung, sondern zur Entwickelung noch ganz anderer Wesenheiten gehört.",
      "So sehen wir, wie der Mensch eingegliedert ist in die Reihe der Hier­archien, wie in seiner Entwickelung von Zeit zu Zeit, von Epoche zu Epoche Wesenheiten, die wir von der anderen Seite her kennen, mit­wirken. Und wir haben gesehen, wie dafür gesorgt wird, daß sich diese Wesenheiten in der mannigfaltigsten individuellen Weise ausleben kön­nen, haben gesehen, daß das, was sie zu liefern haben, sich hineinleben kann in die Menschen.",
      "Die großen Richtlinien der einzelnen Epochen geben die Zeitgeister. Die Ausbreitung des Zeitgeistes über die ganze Erde hin wird durch die einzelnen Völkerindividualitäten möglich. Während die Zeitgeister die Volksgeister befähigen, wird durch die Engel bewirkt, daß diese einfließen können in die einzelnen Menschen, so daß die einzelnen Menschen ihre Mission erfüllen können. Daß die einzelnen Menschen Werkzeuge werden in dieser Mission der Volksgeister, das wird bewirkt durch die Wesen, welche zwischen den Menschen und den Volksgei-stern stehen, durch die Engel oder Angeloi.",
      "Wie dieses wunderbare Netz uns erkennen lassen wird das Wirken der mannigfaltigen Volksindividualitäten der Vorzeit und der Gegen­wart, das wird einen Gegenstand dieser Vorträge bilden. Wir werden im nächsten Vortrag damit beginnen, in das Konkrete hineinzuleuch­ten, wie dieses Gewebe, auf das wir heute nur skizzenhaft hingedeutet haben, gesponnen wird, das Geistesgewebe, das unser nächstes Welten-dasein ist."
    ],
    "sentences": [
      [
        "Es gereicht mir zu großer Befriedigung, nun schon das dritte Mal in etwas längeren Ausführungen zu unsern Freunden hier in Norwegen sprechen zu können, und ich möchte auf die lieben Worte unseres lieben Freundes Eriksen nur ganz kurz sagen, daß die Worte herzlicher Begrü­ßung, die er soeben ausgesprochen hat, ebenso herzlich und aus ebenso tiefen Gründen der Seele heraus, wie sie gesprochen worden sind, von mir erwidert werden."
      ],
      [
        "Ich hoffe, daß auch dieser Vortragszyklus, den ich nunmehr vor Ihnen beginnen möchte, einiges beitragen kann zu der Erkenntnis von dem, was wir das Gesamtbild unserer Weltanschauung nennen.",
        "Ich möchte gerade bei diesem Vortragszyklus darauf aufmerksam machen, daß er ja in seinem Verlaufe mancherlei enthalten muß, was sozusagen zu den einschneidendsten Wahrheiten unserer Weltanschauung gehört, daß er einiges von dem wird enthalten müssen, was eigentlich dem gegenwärtigen menschlichen Denken noch ziemlich fern liegt.",
        "Daher bitte ich vor allen Dingen diejenigen der verehrten Freunde, welche sich mit den weitergehenden Fragen der geisteswissenschaftlichen Weltan­schauung weniger befaßt haben, darauf Rücksicht zu nehmen, daß wir ja nicht vorwärts kommen würden auf unserm Felde, wenn wir nicht von Zeit zu Zeit immer wieder einen kräftigen Ruck, einen kräftigen Sprung in diejenigen Partien geistiger Erkenntnis tun würden, welche gerade dem gegenwärtigen menschlichen Denken, Fühlen und Empfin­den eigentlich ziemlich fern liegen."
      ],
      [
        "Von diesem Gesichtspunkte aus wird manchmal den Ausführungen gegenüber ein gewisser guter Wille notwendig sein; denn um alles das herbeizutragen, was herbeigetragen werden müßte an Belegen und Be­weisen für dasjenige, was in den nächsten Tagen von dieser Stelle aus gesprochen werden wird, dazu gehört eine viel längere Zeit.",
        "Wir wür­den nicht vorwärts kommen, wenn nicht gerade diesen Ausführungen gegenüber sozusagen etwas appelliert würde an den guten Willen, an das Entgegenkommen spirituellen Verständnisses.",
        "Es ist in der Tat das"
      ],
      [
        "Gebiet, welches wir hiermit berühren, ein solches, das so ziemlich bis in unsere Zeiten hinein gerade von Okkultisten, gerade von Mystikern und Theosophen gemieden worden ist, und zwar gemieden worden ist aus dem Grunde, weil ein höherer Grad von Vorurteilslosigkeit not­wendig ist, um die Dinge, die zu sagen sind, gewissermaßen ohne Widerstreben, das manchmal auftauchen könnte, entgegenzunehmen."
      ],
      [
        "Wie das gemeint ist, wird Ihnen vielleicht am verständlichsten wer­den, wenn Sie sich erinnern, daß man in einem gewissen Grad mysti­scher oder okkulter Entwickelung ein heimatloser Mensch genannt wird.",
        "Es ist dies geradezu ein technischer Ausdruck, «heimatloser Mensch», und wenn wir ohne Umschweife - da wir nicht über den Pfad der Erkenntnis sprechen - charakterisieren wollen, was mit dem Worte «heimatloser Mensch» gemeint ist, so können wir kurz sagen, daß derjenige ein heimatloser Mensch genannt wird, der in seiner Er­kenntnis, seiner Auffassung der großen Menschheitsgesetze in Wahrheit unbeeinflußbar ist von alledem, was sonst im Menschen aufsteigt aus dem Ort, an dem er in Gemäßheit seines Volkstums lebt.",
        "Ein heimat­loser Mensch, können wir auch sagen, ist derjenige, welcher die große Mission der Gesamtmenschheit in sich aufzunehmen vermag, ohne daß sich die Nuancen der besondern Gefühle und Empfindungen einmi­schen, die aus diesem oder jenem Heimatboden herauswachsen.",
        "Sie sehen daraus, daß zu einem gewissen Reifegrad mystischer oder okkul­ter Entwickelung ein freier Gesichtspunkt gerade gegenüber demjeni­gen gehört, was wir mit Recht sonst als etwas Großes betrachten, was wir anderseits dem einzelnen Menschenleben gegenüber als die Mission der einzelnen Volksgeister, als dasjenige bezeichnen, was aus dem Untergrunde eines Volksbodens, aus dem Geiste der Völker heraus die einzelnen konkreten Beiträge zu der gesamten Mission der Menschheit liefert."
      ],
      [
        "Schildern wollen wir also sozusagen das Große dessen, wovon der heimatlose Mensch in gewisser Beziehung frei werden muß.",
        "Nun haben die heimatlosen Menschen aller Zeiten, von den Urzeiten angefangen bis in unsere Tage hinein, immer gewußt, daß, wenn sie sozusagen in vollem Umfange charakterisieren würden dasjenige, was man als den Charakter der Heimatlosigkeit bezeichnet, sie dann wenig, sehr wenig"
      ],
      [
        "Verständnis finden würden.",
        "Es würde zunächst einmal das Vorurteil diesen heimatlosen Menschen entgegengebracht werden, das sich in dem Vorwurfe ausdrücken würde: Ihr habt ja allen Zusammenhang mit dem Mutterboden des Volkstums verloren; Ihr habt ja kein Verständnis für das, was den Menschen sonst das Teuerste ist. - Nun ist es aber nicht so."
      ],
      [
        "Heimatlosigkeit ist in gewisser Beziehung doch im Grunde genom­men - oder kann es wenigstens sein - ein Umweg, um, nachdem diese heilige Stätte, diese Heimatlosigkeit erreicht ist, wieder den Rückweg zu finden zu den Volkssubstanzen, den Einklang zu finden mit dem Bodenständigen in der Menschheitsentwickelung.",
        "Wenn darauf von vornherein aufmerksam gemacht werden muß, so ist es auf der andern Seite doch nicht unbegründet, daß gerade in unserer Zeit in unbefan­genster Weise auch einmal über dasjenige gesprochen wird, was wir die Mission der einzelnen Volksseelen der Menschheit nennen."
      ],
      [
        "Ebenso, wie es begründet ist, daß bisher sozusagen bis zu einem gewissen Grade von dieser Mission ganz geschwiegen wurde, ebenso begründet ist es, in unserer Gegenwart damit zu beginnen, von dieser Mission zu reden.",
        "Es ist aus dem Grunde von einer ganz besonderen Wichtigkeit, weil die nächsten Schicksale der Menschheit in einem viel höheren Grade als das bisher der Fall war, die Menschen zu einer gemeinsamen Menschheits­mission zusammenführen werden."
      ],
      [
        "Zu dieser gemeinsamen Mission wer­den aber die einzelnen Volksangehörigen nur dann ihren entsprechen­den freien, konkreten Beitrag liefern können, wenn sie vor allen Dingen ein Verständnis haben für ihr Volkstum, ein Verständnis für dasjenige, was man nennen könnte «Selbsterkenntnis des Volkstums».",
        "Wenn im alten Griechenland in den apollinischen Mysterien der Satz: «Erkenne dich selbst» eine große Rolle gespielt hat, so wird in einer nicht zu fernen Zukunft der Ausspruch an die Volksseelen gerichtet werden:"
      ],
      [
        "«Erkennet euch selbst als Volksseelen.» Dieser Spruch wird eine gewisse Bedeutung haben für das Zukunftswirken der Menschheit."
      ],
      [
        "Nun wird es unserer Zeit schon ganz besonders schwer, Wesenheiten anzuerkennen, welche für die äußere sinnliche Wahrnehmung, für die äußere materielle Erkenntnis sozusagen gar nicht da sind.",
        "Es wird ja vielleicht nicht so schwierig sein für unsere Gegenwart, anzuerkennen, daß der Mensch, so wie er in der Welt vor uns steht, gewisse Glieder,"
      ],
      [
        "gewisse Teile seiner Wesenheit hat, die übersinnlich, unsichtbar sind.",
        "Es wird sich vielleicht der gegenwärtige materialistische Sinn der Menschheit noch leichter zu dieser Anschauung führen lassen, daß We­senheiten, die man wenigstens nach ihrer Außenseite hin physisch sehen kann, wie die Menschen, auch einen übersinnlichen, unsichtbaren Teil haben."
      ],
      [
        "Aber eine starke Zumutung ist es für unsere Gegenwart, wenn man zu ihr sprechen soll von Wesenheiten, die eigentlich nach gewöhn­licher Anschauung gar nicht da sind.",
        "Denn was ist es eigentlich, was man heute da oder dort Volksseele, Volksgeist nennt?"
      ],
      [
        "Es ist höchstens das, was man gelten läßt als eine Eigenschaft, als eine gemeinschaftliche Eigenschaft von so und so vielen hundert Menschen oder Millionen von Menschen, die auf einem gewissen Boden zusammengedrängt sind.",
        "Daß irgend etwas, was da lebt außer den vielen Millionen Menschen, die auf dem Boden zusammengedrängt sind, daß irgend etwas Reales, das sich decken würde mit dem Begriff Volksgeist, diesem Begriffe zugrunde liegt, das ist schwer für ein Bewußtsein unserer gegenwärtigen Zeit klar zu machen."
      ],
      [
        "Wenn man fragen würde - sagen wir jetzt, um etwas ganz Neutrales zu haben-: Was versteht der gegenwärtige Mensch unter dem schweizerischen Volksgeist? - da würde er in abstrakten Ausdrücken einige Eigenschaften beschreiben, welche diejenigen Menschen haben, welche das schweizerische Gebiet der Alpen und des Jura bewohnen, und wird sich klar darüber sein, daß dem nicht etwas entspricht, was man mit äußeren Erkenntniskräften, mit Augen oder sonstigen Wahr­nehmungsorganen erkennen könnte.",
        "Das muß das erste sein, daß man in offener und ehrlicher Weise sich den Gedanken bilden kann, daß es Wesenheiten gibt, die sich ohne weiteres eigentlich nicht sinnlich äu­ßern, dem gewöhnlichen materiellen Wahrnehmungsvermögen sich nicht darbieten, daß es sozusagen zwischen den Wesen, die sinnlich wahrnehmbar sind, andere unsichtbar wirkende Wesenheiten gibt, die hereinwirken in sichtbare Wesenheiten, wie die menschliche Wesenheit in die menschlichen Hände oder menschlichen Finger, daß man also sprechen kann von dem schweizerischen Volksgeist wie von dem Geiste eines Menschen, und daß man diesen Geist des Menschen ebenso genau von dem unterscheiden kann, was man in den zehn Fingern vor sich hat, wie man den schweizerischen Volksgeist unterscheiden kann von"
      ],
      [
        "den Millionen von Menschen, die in den Bergen der Schweiz leben.",
        "Er ist noch etwas anderes, nämlich eine Wesenheit, wie der Mensch selber eine Wesenheit ist.",
        "Nur unterscheiden sich die Menschen davon da­durch, daß sie dem Wahrnehmungsvermögen des Menschen eine sinn­liche Außenseite darbieten.",
        "In demselben Maße, wie sich der Mensch dem sinnlichen Wahrnehmungsvermögen darbietet, bietet eine äußere Erscheinung, etwas, was man mit Empfindungsorganen oder äußeren Sinnen sehen oder wahrnehmen kann, ein Volksgeist nicht dar, aber er ist dennoch eine durchaus reale Wesenheit."
      ],
      [
        "Heute wird es sich darum handeln, uns gewissermaßen eine Vorstel­lung zu bilden von einer solchen realen Wesenheit.",
        "Wie machen wir das überhaupt in der Geisteswissenschaft, wenn wir uns von einer realen Wesenheit eine Vorstellung bilden wollen?"
      ],
      [
        "Ein charakteristisches Bei­spiel, wie wir uns eine Vorstellung bilden von einer realen Wesenheit, gewinnen wir, wenn wir zuerst einmal den Blick auf das Wesen des Menschen werfen.",
        "Wenn wir geisteswissenschaftlich den Menschen be­schreiben, unterscheiden wir an ihm den physischen Leib, den Äther-oder Lebensleib, den Astralleib oder Empfindungsleib und das, was wir als das höchste Glied der menschlichen Wesenheit betrachten, das Ich."
      ],
      [
        "Wir wissen also, daß wir in dem, was wir physischen Leib, Atherleib, Astralleib und Ich nennen, sozusagen den gegenwärtigen Menschen vor uns haben.",
        "Sie wissen aber auch, daß wir auf eine Entwickelung der Menschheit in der Zukunft hinblicken, und daß das Ich an den drei nie­deren Gliedern der menschlichen Wesenheit arbeitet, sodaß es dieseGlie­der vergeistigt, umarbeitet von der gegenwärtigen niederen in die zu­künftige höhere Form."
      ],
      [
        "Das Ich wird das Astrale umarbeiten, umformen, so daß es etwas anderes werden wird, als was es heute schon ist.",
        "Der Astralleib wird dann darstellen das, was Sie unter dem Namen Geist-selbst oder Manas kennen."
      ],
      [
        "Ebenso wird eine noch höhere Arbeit des Ich an dem Atherleibe oder Lebensleibe geleistet werden dadurch, daß es ihn umarbeitet und umprägt in das, was wir Lebensgeist oder Budhi nennen.",
        "Und endlich ist die höchste Arbeit des Menschen, die wir uns vorläufig denken können, die, daß der Mensch das widerstrebendste Glied seiner Wesenheit, den physischen Leib vergeistigen, umwandeln und metamorphosieren wird in das Geistige."
      ],
      [
        "Es wird das höchste Glied"
      ],
      [
        "der menschlichen Wesenheit sein, wenn das Ich umgestaltet haben wird das, was heute physischer Leib ist, das, was heute uns am gröbsten und materiellsten entgegentritt, wenn das Ich es umgestaltet haben wird in den Geistesmenschen oder Atma.",
        "So blicken wir auf drei Glieder der menschlichen Natur, die sich in der Vergangenheit entwickelt haben, auf eines, in dem wir jetzt darinnen stehen, und auf drei andere, aus denen das Ich etwas Neues in der Zukunft machen wird."
      ],
      [
        "Wir wissen auch, daß zwischen der Arbeit, die verflossen ist, und zwischen der Arbeit, die in der Zukunft verfließen wird, um die drei höheren Glieder zu bilden, etwas dazwischen liegt.",
        "Wir wissen, daß wir das Ich selber gegliedert uns denken müssen.",
        "Es arbeitet an einer Art von Zwischenwesenheit.",
        "Wir sprechen daher davon, daß zwischen dem Astralleibe, wie er aus der Vergangenheit dem Menschen geworden ist, und dem Geistselbst oder Manas, das aus diesem Astralleib in ferner Zukunft dem Menschen werden wird, in der Mitte darinnen liegen die drei vorbereitenden Glieder; das sind: die Empfindungsseele, das nie­derste Glied, in dem das Ich gearbeitet hat, die Verstandes- oder Gemütsseele und die Bewußtseinsseele.",
        "So daß wir sagen können:"
      ],
      [
        "Von dem, was wir herausarbeiten als Geistselbst oder Manas, von dem ist außerordentlich wenig heute beim Menschen vorhanden, höchstens der Anfang.",
        "Dagegen hat sich der Mensch dadurch zu dieser künftigen Arbeit vorbereitet, daß er seine drei niederen Glieder in einer gewissen Weise, in gewissem Maße hat beherrschen gelernt.",
        "Er hat sich vorberei­tet dadurch, daß er den Empfindungs leib oder den astralischen Leib hat beherrschen gelernt, indem er mit seinem Ich in denselben eingedrungen ist und innerhalb des Empfindungsleibes die Empfindungsseele heraus­gebildet hat.",
        "Ebenso wie die Empfindungsseele in einem gewissen Ver­hältnis zum Empfindungsleibe steht, so steht die Verstandes- oder Gemütsseele in einem gewissen Verhältnis zum Äther- oder Lebensleibe, so daß die Verstandes- oder Gemütsseele ein schwaches Vorbild dessen ist, was der Lebensgeist oder Buddhi sein wird, zwar ein schwaches Vor­bild, aber doch ein Vorbild.",
        "Und das, was in der Bewußtseinsseele sich befindet, ist in gewisser Weise von dem Ich hineingearbeitet in den physischen Leib.",
        "Daher ist sie ein schwaches Vorbild dessen, was einst Geistesmensch oder Atma sein wird.",
        "Wir können auch sagen: Gegenwärtig"
      ],
      [
        "erkennen wir am Menschen, wenn wir absehen von geringfügigen Teilen, die er schon aus dem astralischen Leibe herausgearbeitet hat als Anfang des Geistselbstes oder Manas, vier verschiedene Glieder.",
        "Wir können heute unterscheiden:"
      ],
      [
        "1. den physischen Leib,"
      ],
      [
        "2. den Ätherleib,"
      ],
      [
        "3. den Astralleib,"
      ],
      [
        "4. das in demselben arbeitende Ich,"
      ],
      [
        "und ferner, wie ein Vorglanz zu den höheren Gliedern:"
      ],
      [
        "die Empfindungsseele,"
      ],
      [
        "die Verstandesseele,"
      ],
      [
        "die Bewußtseinsseele."
      ],
      [
        "Da haben wir den Menschen als eine Wesenheit vor uns, wie er sich uns heute darbietet, und da erfassen wir sozusagen diesen Menschen in dem gegenwärtigen Augenblicke seines Werdens.",
        "Wir sehen förmlich das Ich herausarbeiten, nachdem als Vorbereitung ihm geworden ist die Empfindungs-, Verstandes- und Bewußtseinsseele, die höheren Glieder.",
        "Wir sehen dieses Ich arbeiten mit den Kräften der Empfindungs-, Ver­standes- und Bewußtseinsseele an dem astralischen Leibe, an den An­fängen des Geistselbstes.",
        "Wir sehen den Menschen gegenwärtig in diesem Momente seines Arbeitens."
      ],
      [
        "Diejenigen - und es werden die meisten von Ihnen sein -, die sich mit dem befaßt haben, was wir die Erforschung der Akashachronik nennen, mit der Entwickelung des Menschen in urferner Vergangenheit und mit dem Ausblick in die ferne Zukunft, die werden wissen, daß die Menschen, wie ich sie Ihnen skizzenhaft charakterisieren konnte, sich entwickelt haben, daß wir zurückschauen können in ferne Vergangen­heit, daß die Menschen lange Entwickelungsepochen gebraucht haben, um die erste Anlage ihres physischen Leibes, dann die erste Anlage des Ätherleibes und endlich des Astralleibes zu bilden und diese drei Glie­der dann weiter zu entwickeln.",
        "Der Mensch hat dazu lange Zeiträume gebraucht, und Sie wissen vielleicht auch, daß der Mensch die frühere Entwickelung seines Wesens, zum Beispiel die Entwickelung seines astralischen Leibes, nicht in demselben Zustande der Erde durchge­macht hat, in dem die Erde heute ist, sondern daß er seinen astralischen"
      ],
      [
        "Leib entwickelt hat in einem früheren Zustande des Erdendaseins, dem Monden dasein.",
        "Wie wir das heutige Leben als die Folge früherer Erden-leben, früherer Verkörperungen erkennen, so blicken wir auch auf frühere Verkörperungen unserer Erde zurück.",
        "Das, was wir Empfin­dungsseele, Verstandes- oder Gemütsseele nennen, wurde erst in dem heutigen Erdendasein gebildet.",
        "In dem Mondendasein wurde der astra­lische Leib eingepflanzt, und in einem noch früheren Dasein unserer Erde, dem Sonnenzustande, wurde der Ätherleib eingepflanzt und endlich während des Saturnzustandes der physische Leib.",
        "So daß wir auf drei Verkörperungen der Erde zurückblicken, und auf jeder dieser Verkörperungen sehen wir eines der Glieder, die der Mensch heute in sich trägt, zuerst veranlagt und dann weiter ausgebildet."
      ],
      [
        "Noch etwas anderes ist zu betonen, wenn wir von dem Saturn-, Sonnen-, Monden-Zustande reden.",
        "Genau so, wie wir als Menschen auf der Erde den Zustand durchmachen, den wir den selbstbewußten Menschheitszustand nennen können. so haben während früherer Zu­stände unserer Erdenentwickelung, während des alten Monden-, Son­nen- und Saturnzustandes andere Wesen die Stufe durchgemacht, die wir heute auf der Erde durchmachen."
      ],
      [
        "Es ist dabei ziemlich gleichgültig, ob man mit der Terminologie, die man im Orient gebraucht, oder mit derjenigen, die mehr im Okzident üblich ist, die Wesenheiten benennt.",
        "Diejenigen Wesenheiten, die während des Mondenzustandes unserer Er­de auf der Stufe standen, auf der der Mensch heute steht, und die die nächsthöheren Wesenheiten sind, die über uns stehen, nennen wir in der Terminologie der christlichen Esoterik Angeloi oder Engel."
      ],
      [
        "Sie stehen eine Stufe höher als der Mensch, weil sie um eine Epoche früher ihre Menschheitsstufe absolviert haben, so daß diese Wesenheiten dasjenige, was wir heute sind, dazumal während des alten Mondenzustandes waren.",
        "Sie waren es aber nicht so, daß sie damals auf dem Monde herumgegangen wären wie die Menschen heute auf der Erde."
      ],
      [
        "Sie waren Wesenheiten auf der Menschheitsstufe, aber sie lebten nicht im Fleische wie der Mensch heute.",
        "So entsprach nur ihre Stufe der Entwickelung dem Menschsein, das der Mensch heute durchmacht.",
        "Ebenso finden wir Wesenheiten noch höherer Art, welche während des alten Sonnenzu­standes die Menschheitsentwickelung durchgemacht haben."
      ],
      [
        "Es sind die"
      ],
      [
        "Archangeloi oder Erzengel.",
        "Das sind Wesenheiten, die zwei Stufen höher stehen als der Mensch, die zwei Epochen früher ihre Menschheits­stufe durchgemacht haben.",
        "Wenn wir noch weiter zurückgehen bis zur ersten Verkörperung unseres Erdendaseins, bis zum Saturnzustand, da finden wir, daß da diejenigen Wesenheiten ihre Menschheitsstufe durchgemacht haben, die wir als Geister der Persönlichkeit, Archai, Urbeginne bezeichnen, so daß wir, wenn wir bei diesen Wesenheiten beginnen - die also in urferner Vergangenheit, während des alten Sa­turnzustandes Menschen waren - und dann die Verkörperungen der Erde verfolgen bis auf unseren Zeitpunkt, vor uns haben die Entwik­kelungsstufen der Wesen bis herunter zu unserer Wesenheit.",
        "Wir können also sagen: Urbeginne, Archai waren Menschen auf dem alten Saturn; Erzengel, Archangeloi waren Menschen auf der alten Sonne; Engel oder Angeloi waren Menschen auf dem alten Mond; Menschen sind Menschen auf unserer Erde."
      ],
      [
        "Da wir nun wissen, daß wir in der Zukunft unsere Entwickelung weiterführen, dasjenige, was unsere niederen Glieder sind, weiter ent­falten, also dasjenige, was heute unser astralischer Leib, unser Äther-oder Lebensleib und unser physischer Leib ist, so müssen wir doch fragen: Ist es nicht ebenso natürlich, daß die Wesenheiten, die früher die Menschheitsstufe durchgemacht haben, jetzt schon auf der Stufe sind, wo sie umarbeiten ihren astralischen Leib in das Geistselbst oder Manas?",
        "Wie wir während der nächsten Verkörperung unserer Erde -während des Jupiter-Daseins - fertig werden mit der Umgestaltung unseres Astralleibes in Geistselbst oder Manas, so sind fertig geworden diejenigen Wesenheiten, die während der Mondepoche Menschen wa­ren, die Angeloi, mit der Umgestaltung ihrer Astralleiber in Geistselbst oder Manas, oder sie werden damit während unseres Erdendaseins fertig werden.",
        "Sie machen das durch während unserer Erdenverkörpe­rung, was wir erst während der nächsten Verkörperung der Erde werden durchzumachen haben.",
        "Blicken wir noch weiter zurück auf die Wesen, die während des alten Sonnendaseins Menschen waren, so kön­nen wir sagen: Sie haben schon während des Mondenzustandes das durchmachen müssen, was wir erst in der nächsten Erdenverkörperung werden durchmachen müssen.",
        "Sie stehen bei der Arbeit, die der Mensch"
      ],
      [
        "ausführen wird, wenn er mit seinem Ich umarbeitet seinen Äther- oder Lebensleib in Lebensgeist oder Buddhi.",
        "Wir haben also in diesen Archan­geloi, in diesen Erzengeln Wesenheiten, die zwei Stufen über uns stehen, die auf der Stufe stehen, die wir einst erreichen werden, wenn wir von unserem Ich aus umarbeiten werden den Lebensleib in Lebensgeist oder Buddhi.",
        "Wir blicken, wenn wir zu diesen Wesenheiten aufschauen, so zu ihnen auf, daß wir sagen: Wir sehen in ihnen Wesenheiten, die zwei Stufen über uns stehen, Wesenheiten, in denen wir gleichsam voraus-genommen sehen, was wir selber in Zukunft erleben werden; wir blicken zu ihnen auf als zu solchen Wesen, die heute arbeiten an ihrem Äther- oder Lebensleib und ihn umformen zu Lebensgeist oder Buddhi.",
        "Ebenso blicken wir auf zu noch höheren Wesenheiten, zu den Geistern der Persönlichkeit.",
        "Sie stehen auf einer noch höheren Stufe als die Erz­engel, auf einer Stufe, die der Mensch erreichen wird in noch fernerer Zukunft, wenn er wird umarbeiten können den physischen Leib in Atma oder Geistesmensch."
      ],
      [
        "So wahr der Mensch auf der jetzigen Stufe seines Daseins ist, so wahr sind diese entsprechenden Wesenheiten auf den eben charakterisierten Stufen ihres Daseins, so wahr stehen sie über uns, so wahr sind sie Realitäten.",
        "Nun steht ihre Realität nicht etwa fern dem Erdendasein, sondern greift vielmehr in dasselbe ein, wirkt hinein in unser Menschen-dasein.",
        "Wir müssen uns jetzt nur fragen: Wie wirken diese über dem Menschen stehenden Wesenheiten in unser Menschheitsdasein hinein?",
        "Wenn wir uns dieses Hineinwirken begreiflich machen wollen, dann mussen wir darauf Rücksicht nehmen, daß solche Wesenheiten sozu­sagen in ihrer Arbeit einen anderen geistigen Anblick darbieten werden als diejenigen Wesenheiten, die wir heute Menschen nennen.",
        "Es ist in der Tat ein beträchtlicher Unterschied zwischen diesen Wesenheiten, die über dem Menschen stehen, und denjenigen Wesenheiten, die heute erst auf der Menschheitsstufe sich befinden.",
        "So sonderbar das jetzt auch klingen mag, es wird Ihnen im Laufe der nächsten Tage noch vollstän­dig klar werden.",
        "Es ist doch durchaus aus wirklicher Geistesforschung heraus gesprochen: Der Mensch, wie er heute ist, ist gewissermaßen in einem Mittelzustand seines Daseins.",
        "So wie heute sein Ich an seinen niederen Gliedern arbeitet, wird es nicht immer bleiben.",
        "Es ist gleichsam"
      ],
      [
        "das ganze menschliche Wesen heute wie in sich zusammenhängend, und es bildet gleichsam eine durch nichts unterbrochene Wesenheit.",
        "Das kann in der Zukunft der Menschheitsentwickelung anders werden, und es wird wesentlich anders werden.",
        "Wenn der Mensch einmal so weit sein wird, daß er mit vollem Bewußtsein an seinem Astralleib arbeiten und mit seinem Ich diesen Astralleib in Geistselbst oder Manas umar­beiten wird, dann wird ein ähnlicher Zustand bei vollem Bewußtsein vorhanden sein, wie er jetzt beim Unbewußtsein oder Unterbewußtsein des Menschen im Schlafe vorhanden ist."
      ],
      [
        "Stellen Sie sich einmal den Schlafzustand des Menschen vor.",
        "Der Mensch rückt beim Schlafzustand in bezug auf seinen Astralleib und sein Ich aus seinem physischen Leib und seinem Ätherleib heraus, er läßt sie im Bette liegen und schwebt dann gleichsam außerhalb des physischen und Ätherleibes Denken Sie sich jetzt in diesem Zustande den Menschen so, daß das Bewußtsein erwacht: Ich bin ein Ich, - daß es so erwacht in diesem Geistesleib, wie es im tagwachen Bewußtseins­zustande da ist."
      ],
      [
        "Was würde der Mensch schon gegenwärtig für einen merkwürdigen Anblick für sich selber darbieten!",
        "Er würde an einer Stelle fühlen: «Da bin ich», und vielleicht da unten, weit weg von dieser ersteren Stelle: «Da ist mein physischer Leib und mein Ätherleib; sie sind an jenem Orte und sie gehören zu mir, aber ich mit meinen anderen Gliedern, ich schwebe außerhalb, da oben»."
      ],
      [
        "Wenn der Mensch heute bewußt wird in seinem Astralleibe, außerhalb seines physischen und Ätherleibes, dann kann er allerdings - und wenn er heute auf der Erde sozusagen noch so hoch entwickelt ist - nichts anderes tun, als frei in seinem Astralleibe sich da- oder dorthin bewegen und kann unabhängig von seinem physischen Leibe da oder dort in der Welt tätig sein, aber das kann er dann noch nicht mit seinem physischen und Ätherleibe.",
        "Man wird sie aber in ferner Zukunft auch von einer Stätte des Nordens von Europa zum Beispiel von außen hingeleiten können nach einer anderen Stätte, ihnen befehlen: Geht weiter! und sie dann in ihrer Be­wegung von außen lenken."
      ],
      [
        "Das geht heute noch nicht.",
        "Das wird aber der Mensch können, wenn er sich über die Stufe der Erdenentwickelung zu der Jupiterstufe entwickelt haben wird, zu der folgenden Entwik­kelungsstufe unseres Erdenplaneten."
      ],
      [
        "Das wird auch der folgende Entwickelungszustand"
      ],
      [
        "des Menschen sein.",
        "Wir werden dann fühlen, daß wir gewissermaßen für uns selbst der Dirigent von außen sein werden.",
        "Das ist das Wesentliche.",
        "Und das führt zu einer Spaltung von dem, was wir heute die menschliche Wesenheit genannt haben."
      ],
      [
        "Das materialistische Bewußtsein kann damit allerdings nicht viel anfangen.",
        "Es kann nicht verfolgen dasjenige, was heute schon in gewis­ser Beziehung real in der Außenwelt wirkt in ähnlicher Weise, wie es eininal in der Zukunft beim Menschenwesen vorhanden sein wird."
      ],
      [
        "Solche Erscheinungen sind schon heute da.",
        "Die Menschen könnten sie wahrnehmen, wenn sie acht geben würden.",
        "Sie würden dann sehen, daß es gewisse Wesenheiten gibt, die zum Beispiel zu früh sich so entwickelt haben."
      ],
      [
        "Wie der Mensch, wenn er den richtigen Zeitpunkt abwartet, im richtigen Zeitpunkt den Jupiterzustand erreichen wird, so daß er leiten kann seinen physischen und ätherischen Leib, so gibt es auch Wesen, welche in gewisser Beziehung sich vorschnell entwickelt haben, ohne den richtigen Zeitpunkt abgewartet zu haben.",
        "Solche vorzeitig entwik­kelte Wesenheiten haben wir in unserer Vogelwelt, und zwar in solchen Wesenheiten der Vogelwelt, welche jedes Jahr die großen Wanderzüge über die Erde vollführen."
      ],
      [
        "Da ist es die sogenannte Gruppenseele, welche mit dem ätherischen Leibe eines jeden Vogels zusammenhängt.",
        "So wie die Gruppenseele die regelmäßigen Wanderzüge der Vögel über die Erde hin dirigiert, so wird der Mensch, nachdem er sein Geistselbst oder Manas entwickelt hat, das, was wir physischen und ätherischen Leib nennen, befehligen, ihnen gebieten, sie in Bewegung setzen."
      ],
      [
        "In einem noch höheren Sinne wird der Mensch diese dirigieren, von außen in Bewegung setzen können, wenn er einmal so weit entwickelt sein wird, daß er auch noch umarbeitend in bezug auf den Äther- oder Lebensleib wirkt.",
        "Solche Wesenheiten, die das schon können, gibt es schon heute."
      ],
      [
        "Das sind die Archangeloi oder Erzengel.",
        "Das sind Wesenheiten, die das bereits können, was der Mensch einmal können wird, Wesenheiten, die dasjenige vollbringen können, was man nennen kann «seinen ätheri­schen und seinen physischen Leib von außen dirigieren», die aber außerdem auch noch arbeiten können an ihrem eigenen Ätherleibe."
      ],
      [
        "Bilden Sie sich als Idee den Begriff von Wesenheiten, die sozusagen im Umkreis unserer Erde wirken, die in der geistigen Atmosphäre"
      ],
      [
        "unserer Erde enthalten sind mit ihrem Ich, die von diesem ihrem Ich aus schon umgewandelt haben ihren astralischen Leib, so daß sie ein vollentwickeltes Geistselbst oder Manas besitzen, die aber jetzt mit diesem vollentwickelten Geistselbst oder Manas weiterwirken auf unserer Erde und hereinarbeiten in die Menschen, indem sie unseren Äther- oder Lebensleib umgestalten; Wesenheiten, die auf der Stufe stehen, auf welcher sie den Äther- oder Lebensleib zu Buddhi oder Lebensgeist umgestalten.",
        "Wenn Sie sich solche Wesenheiten denken, die also auf der Stufe der geistigen Hierarchien stehen, die wir Erzengel nennen, haben Sie einen Begriff von dem, was man «Volksgeister» nennt, was man die dirigierenden Volksgeister der Erde nennt.",
        "Die Volksgeister gehören in die Stufe der Archangeloi oder Erzengel.",
        "Wir werden sehen, wie sie ihrerseits den Äther- oder Lebensleib dirigieren, und wie sie dadurch wieder hineinwirken in die Menschheit und diese in ihre eigene Tätigkeit einbeziehen.",
        "Wenn wir die verschiedenen Völ­ker unserer Erde betrachten und einzelne herausheben, dann werden wir in dem eigentümlichen Weben und Leben dieser Völker, in dem, was wir die besonderen, charakteristischen Eigenschaften dieser Völker nennen, ein Abbild von dem haben, was wir als die Mission der Volks-geister betrachten können."
      ],
      [
        "Wenn wir die Mission dieser Wesenheiten erkennen - Inspiratoren der Völker sind diese Wesenheiten -, dann können wir sagen, was ein Volk ist.",
        "Ein Volk ist eine zusammengehörige Gruppe von Menschen, welche von einem der Archangeloi, einem der Erzengel geleitet wird.",
        "Die einzelnen Glieder eines Volkes bekommen das, was sie als Glieder des Volkes tun, was sie als Glieder des Volkes vollführen, von einer solchen Seite her inspiriert.",
        "Dadurch, daß wir uns vorstellen, daß diese Volksgeister individuell verschieden sind, wie die Menschen auf unserer Erde, werden wir es begreiflich finden, daß die einzelnen verschiedenen Gruppen der Völker die individuelle Mission dieser Archangeloi sind.",
        "Wenn wir uns einmal geistig veranschaulichen, wie in der Weltge­schichte Volk nach Volk und auch Volk neben Volk wirkt, so können wir jetzt, wenigstens in abstrakter Form - die Form wird immer kon­kreter und konkreter werden in den nächsten Vorträgen - uns vorstel­len, daß alles, was da vor sich geht, inspiriert ist von diesen geistigen"
      ],
      [
        "Wesenheiten.",
        "Aber eines wird uns wohl leicht vor die Seele treten können: daß neben diesem Wirken von Volk nach Volk noch etwas anderes stattfindet in der Menschheitsentwickelung.",
        "Sie können, wenn Sie jenen Zeitraum überblicken, den wir von der großen atlantischen Katastrophe aus rechnen, die das Antlitz der Erde so weit verändert hat, daß jener Kontinent, der bestanden hat zwischen dem heutigen Afrika, Amerika und Europa, in jener Zeit untergegangen ist, die Zeit­räume unterscheiden, in welchen die großen Völker gewirkt haben, bei denen die nachatlantischen Kulturen herauskamen: die alte indische, die persische, die ägyptisch-chaldäische, die griechisch-lateinische und unsere gegenwärtige Kultur, die nach einiger Zeit in die sechste Kultur-epoche übergehen wird."
      ],
      [
        "Wir bemerken auch, daß nacheinander darin gewirkt haben verschiedene Völkerinspiratoren.",
        "Wir wissen, daß noch lange die ägyptisch-chaldäische Kultur gewirkt hat, als die griechische Kultur schon ihren Anfang nahm, und daß die griechische Kultur noch weiter waltete, als die römische schon ihren Anfang genommen hatte."
      ],
      [
        "So können wir die Völker nebeneinander und nacheinander betrachten.",
        "Aber in allem, was sich in und mit den Völkern entwickelt, entwickelt sich noch etwas anderes.",
        "Es ist ein Fortschritt in der menschlichen Ent­wickelung."
      ],
      [
        "Es kommt dabei nicht in Betracht, ob wir das eine höher oder niedriger stellen.",
        "Es kann zum Beispiel einer sagen: Mir gefällt die indische Kultur am besten.",
        "Das mag ein persönliches Urteil sein.",
        "Wer aber nicht auf persönliche Urteile schwört, der wird sagen: Es ist gleichgültig, wie wir die Dinge bewerten; der notwendige Gang führt die Menschheit vorwärts, mag man das später auch Niedergang nennen."
      ],
      [
        "Die Notwendigkeit führt die Menschheit vorwärts.",
        "Wenn wir die ver­schiedenen Zeiträume vergleichen, 5000 Jahre vor Christus, 3000 Jahre vor Christus und 1000 Jahre nach Christus, dann ist etwas noch da, was über die Volksgeister hinübergreift, etwas, woran die verschiedenen Volksgeister teilnehmen."
      ],
      [
        "Sie brauchen das nur in unserer Zeit ins Auge zu fassen.",
        "Woher kommt es, daß in diesem Saale so viele Menschen zusammensitzen können, die aus den verschiedensten Volksgebieten herkommen und sich verstehen und sich zu verstehen versuchen in bezug auf das Allerwichtigste, was sie hier zusammengeführt hat?"
      ],
      [
        "Die verschiedenen Menschen kommen aus dem Bereich der verschiedensten"
      ],
      [
        "Volksgeister heraus, und dennoch gibt es etwas, worin sie sich verste­hen.",
        "In ähnlicher Weise verstanden sich und konnten sich verstehen in damaliger Zeit die verschiedenen Völker untereinander, weil es in jeder Zeit etwas gibt, was die Volksseele übergreift, die verschiedenen Volks­seelen zusammenführen kann, etwas, was man überall mehr oder weni­ger versteht.",
        "Das ist dasjenige, was man mit dem recht schlechten, aber gebräuchlichen deutschen Wort «Zeitgeist» benennt oder auch «Geist der Epoche».",
        "Der Geist der Epoche, der Zeitgeist, ist ein anderer in der griechischen Zeit, ein anderer in der unsrigen.",
        "Diejenigen, welche den Geist in unserer Zeit erfassen, werden zur Theosophie hingetrieben.",
        "Das ist das aüs dem Geiste der Epoche über die einzelnen Volksgeister Über­greifende.",
        "In derjenigen Zeit, in der Christus Jesus auf der Erde erschien, bezeichnete sein Vorläufer, Johannes der Täufer, den Geist, den man als Zeitgeist bezeichnen könnte, mit den Worten: «Ändert die Verfassung der Seele, denn die Reiche der Himmel sind nahe herbei-gekommen. »"
      ],
      [
        "So kann man für jede Epoche den Zeitgeist finden, und das ist etwas, was sich hineinwebt in das Weben der Volksgeister, das wir damit zu gleicher Zeit als das Weben der Archangeloi charakterisiert haben.",
        "Für den heutigen materialistischen Menschen ist der Zeitgeist etwas ganz Abstraktes ohne Realität, und noch weniger darf man ihm damit kom­men, in dem Zeitgeist ein wahres Wesen zu sehen.",
        "Dennoch verbirgt sich hinter dem Worte «Zeitgeist» eine wirkliche Wesenheit, keine andere Wesenheit als eine solche, die drei Stufen über der Menschheits­stufe steht.",
        "Jene Wesenheiten verbergen sich dahinter, die schon auf dem alten Saturn, der am weitesten zurückliegenden Entwickelungs­epoche der Erde, ihre Menschheitsstufe durchmachten, und die heute aus dem geistigen Umkreis der Erde an der Umgestaltung der Erde arbeiten und dabei die letzte Phase sozusagen an der Umgestaltung ihres physischen Leibes in Geistesmensch oder Atma durchmachen.",
        "Mit hohen Wesenheiten haben wir es hier zu tun, mit Wesenheiten, gegen­über deren Eigenschaften den Menschen ein Schwindel überkommen möchte.",
        "Es sind diejenigen Wesenheiten, die wir wieder bezeichnen könnten als die eigentlichen Inspiratoren - oder wir müssen auf diesem Gebiete sagen, wenn wir mit technischen Ausdrücken des Okkultismus"
      ],
      [
        "sprechen wollen -, die Intuitoren des Zeitgeistes oder der Zeitgeister.",
        "Sie wirken so, daß sie sich abwechseln und gleichsam einer dem andern die Hand reicht.",
        "Von Epoche zu Epoche reichen sie sich ihre Aufgabe zu.",
        "Der Geist der Epoche, der während der griechischen Zeit wirkte, reicht weiter die Mission an den, der später wirkt und so weiter.",
        "Sie wechseln sich also ab.",
        "Es sind, wie wir sahen, eine Anzahl solcher Zeit-geister, solcher Geister der Persönlichkeit, die als Zeitgeist wirken.",
        "Sie sind eine höhere Rangordnung gegenüber den Volksgeistern, diese Geister der Persönlichkeit, diese Intuitoren des Zeitgeistes.",
        "In jedem Zeitalter wirkt vorzugsweise einer und gibt diesem Zeitalter seine Ge­samtsignatur, gibt seine Aufträge an die Volk sgeister, so daß dasjenige, was der Gesamtgeist der Epoche ist, sich spezialisiert, individualisiert nach den Volksgeistern.",
        "Dann wird er abgelöst in der kommenden Epoche von einem andern Zeitgeiste, einem andern Geiste der Persön­lichkeit, einem andern Archë."
      ],
      [
        "Wenn eine gewisse Anzahl von Epochen vorübergegangen ist, dann ist ein Zeitgeist durch die Weiterentwickelung hindurchgegangen.",
        "Das mussen wir uns so vorstellen: Wenn wir in unserer Zeit sterben und unsere Entwickelung hier durchgemacht haben, so gibt unsere Persön­lichkeit das Ergebnis dieses Erdenlebens an das nächste Erdenleben weiter.",
        "So ist es auch mit den Geistern der Epoche der Fall.",
        "In jeder Epoche haben wir einen solchen Geist der Epoche; der gibt am Ende der Epoche sein Amt an seinen Nachfolger ab, dieser wieder an seinen weiteren Nachfolger und so weiter.",
        "Die vorangegangenen machen in­zwischen ihre eigene Entwickelung durch, dann kommt derjenige, der am längsten nicht daran gewesen ist, wieder an die Reihe, so daß der­selbe in einer spätern Epoche, während die andern dann ihre eigene Entwickelung durchmachen, als Geist der Epoche wiederkommt und für die fortgeschrittene Menschheit das, was er selber für seine höhere Mission erworben hat, intuierend der Menschheit einflößt.",
        "Wir blicken zu diesen Geistern der Persönlichkeit hinauf, zu diesen Wesen, die mit dem sonst so nichtssagenden Worte «Zeitgeist» benannt werden kön­nen, so, daß wir sagen können: Wir Menschen gehen von Inkarnation zu Inkarnation; wir wissen aber ganz genau, daß, indem wir selber von Epoche zu Epoche schreiten, indem wir in die Zukunft sehen, immer"
      ],
      [
        "andere Zeitgeister die Geschehnisse unserer Erde regieren.",
        "Aber auch unser heutiger Zeitgeist wird wiederkommen, wir werden ihm wieder begegnen.",
        "Wegen dieser Eigenschaft dieser Geister der Persönlichkeit, daß sie gleichsam Kreise beschreiben und wieder zu ihrem Ausgangs­punkte zurückkommen, daß sie Zyklen beschreiben, wegen dieser Eigenschaft werden sie auch «Geister der Umlaufszeiten» genannt. -Wir werden diesen Ausdruck noch genauer zu rechtfertigen haben."
      ],
      [
        "Also diese höheren geistigen Wesenheiten, die ihre Befehle ausgeben an die Volksgeister, werden auch Geister der Umlaufszeiten genannt.",
        "Es sind damit gemeint jene Umlaufszeiten, die der Mensch selber durch­zumachen hat, indem er von Epoche zu Epoche in gewisser Weise zurückkehrt zu früheren Zuständen und sie in höherer Form wieder­holt.",
        "Nun sehen Sie, dieses Wiederholen der Eigentümlichkeiten frühe­rer Formen, das kann Ihnen auffallen.",
        "Wenn Sie in geisteswissenschaft­lichem Sinne genau die Entwickelung der Menschheitsstufen auf der Erde durchnehmen, so finden Sie diese wiederholten Geschehnisse in der verschiedensten Weise.",
        "So ist eine Wiederholung darin, daß sozu­sagen sieben Epochen sich folgen nach der atlantischen Katastrophe, die wir nennen die nachatlantischen Kulturstufen.",
        "Die griechisch-latei­nische Stufe oder Kulturepoche bildet sozusagen den Wendepunkt in unserm Zyklus und erleidet daher keine Wiederholung.",
        "Auf diese folgt die Wiederholung der ägyptisch-chaldäischen Epoche, und zwar in unserer eigenen Zeit.",
        "Auf diese wird folgen eine andere Epoche, die eine Wiederholung der persischen Zeit sein wird, allerdings in etwas anderer Art, und dann wird die siebente Epoche kommen, die eine Wiederholung der uralt-indischen Kultur, der Epoche der heiligen Rishis sein wird, so daß in dieser Epoche gewisse Dinge in anderer Form heraus kommen werden, die damals veranlagt worden sind.",
        "Die Len­kung dieser Geschehnisse obliegt den Zeitgeistern."
      ],
      [
        "Daß nun auf die Erde verteilt in verschiedenen Völkern das ausge­lebt wird, was von Epoche zu Epoche weiterschreitet, daß die verschie­densten Gestalten aus diesem oder jenem Boden gebildet werden, aus dieser oder jener Sprachgemeinschaft herauswachsen, aus dieser oder jener Formensprache, aus Architektur, Kunst und Wissenschaft entste­hen können und alle die Metamorphosen annehmen können und alles"
      ],
      [
        "das aufzunehmen vermögen, was der Geist der Epoche der Menschheit einflößen kann, dazu brauchen wir die Volksgeister, die in der Hierar­chie höherer Wesenheiten zu den Erzengeln gehören."
      ],
      [
        "Nun brauchen wir noch eine Vermittlung zwischen der höheren Mission der Volksgeister und denjenigen Wesenheiten, die hier auf der Erde von ihnen inspiriert werden sollen.",
        "Sie werden unschwer erkennen können, zunächst in abstrakter Form, daß die Vermittler dieser beiden Geisterarten die Hierarchie der Engel sind.",
        "Sie bilden das vermittelnde Glied zwischen Volksgeist und Einzelmensch.",
        "Damit der Mensch in sich hineinbekommen kann, was der Volksgeist dem ganzen Volke einzuflößen hat, damit der einzelne Mensch ein Werkzeug werde in der Mission des Volkes, dazu bedarf es dieser Vermittlung zwischen Ein­zelmensch und Erzengel des Volkes."
      ],
      [
        "So haben wir hinaufgeschaut zu den Wesen, welche Mensch gewor­den sind, drei Stufen bevor der Erdenmensch seine Menschheitsstufe erreichte, und haben gesehen, wie sie sich hineinstellen in ihrem Bewußtsein in die Menschheit und eingreifen in unsere Erdenentwicke­lung.",
        "Wir werden nun morgen zu zeigen haben, inwiefern das Arbeiten der Erzengel von oben herunter, von ihrem Ich aus, das schon Manas oder Geistselbst ausgebildet hat und am Ätherleib oder Lebensleib des Menschen arbeitet, gerade in den Produktionen, in den Eigenschaften und in dem Charakter eines Volkes sich darlebt.",
        "Der Mensch steht darin in dieser Arbeit der höheren Wesenheiten, unmittelbar umgibt sie den Menschen, indem er als Angehöriger eines Volkes in dieselbe hin­eingestellt ist.",
        "Der Mensch ist zwar zunächst eine menschliche Indivi­dualität, eine Ausgestaltung einer Ichheit, dann aber ist er nicht nur Individualität, sondern auch Angehöriger eines Volkes und damit etwas, wofür er zunächst als menschliche Individualität nichts kann.",
        "Was kann der Mensch, indem er einem bestimmten Volke angehört, dafür, daß er gerade die Sprache dieses Volkes spricht?",
        "Das ist nicht eine individuelle Errungenschaft, das gehört auch nicht zu dem, was wir ein individuelles Fortschreiten nennen, das ist das Strombett, in das er aufgenommen wird.",
        "Das, was wir menschliches Fortschreiten nen­nen, ist etwas ganz anderes.",
        "Indem wir die Volksseele weben und leben sehen, werden wir uns erinnern, worin das Fortschreiten des Menschen"
      ],
      [
        "besteht und was der Mensch braucht, um sich durch dasselbe durch­zubewegen.",
        "Wir werden sehen, was sozusagen nicht nur zu seiner Ent­wickelung, sondern zur Entwickelung noch ganz anderer Wesenheiten gehört."
      ],
      [
        "So sehen wir, wie der Mensch eingegliedert ist in die Reihe der Hier­archien, wie in seiner Entwickelung von Zeit zu Zeit, von Epoche zu Epoche Wesenheiten, die wir von der anderen Seite her kennen, mit­wirken.",
        "Und wir haben gesehen, wie dafür gesorgt wird, daß sich diese Wesenheiten in der mannigfaltigsten individuellen Weise ausleben kön­nen, haben gesehen, daß das, was sie zu liefern haben, sich hineinleben kann in die Menschen."
      ],
      [
        "Die großen Richtlinien der einzelnen Epochen geben die Zeitgeister.",
        "Die Ausbreitung des Zeitgeistes über die ganze Erde hin wird durch die einzelnen Völkerindividualitäten möglich.",
        "Während die Zeitgeister die Volksgeister befähigen, wird durch die Engel bewirkt, daß diese einfließen können in die einzelnen Menschen, so daß die einzelnen Menschen ihre Mission erfüllen können.",
        "Daß die einzelnen Menschen Werkzeuge werden in dieser Mission der Volksgeister, das wird bewirkt durch die Wesen, welche zwischen den Menschen und den Volksgei-stern stehen, durch die Engel oder Angeloi."
      ],
      [
        "Wie dieses wunderbare Netz uns erkennen lassen wird das Wirken der mannigfaltigen Volksindividualitäten der Vorzeit und der Gegen­wart, das wird einen Gegenstand dieser Vorträge bilden.",
        "Wir werden im nächsten Vortrag damit beginnen, in das Konkrete hineinzuleuch­ten, wie dieses Gewebe, auf das wir heute nur skizzenhaft hingedeutet haben, gesponnen wird, das Geistesgewebe, das unser nächstes Welten-dasein ist."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "ZWEITER VORTRAG Kristiania, 8. Juni 1910",
    "paragraphs": [
      "Es ist gestern gesagt worden, daß diejenigen Wesenheiten, welche als Volksgeister zu betrachten sind, auf einer solchen Stufe stehen, daß sie in ihrem gegenwärtigen Dasein von ihrer Ichheit aus an ihrem Äther-oder Lebensleib arbeiten, daß sie also diesen Äther- oder Lebensleib von dem innersten Wesen ihres Seelischen heraus bearbeiten.",
      "Nun wird ja natürlich jeder von Ihnen sich sagen können: Gewiß muß es zugegeben werden, daß die Arbeit an diesem Äther- oder Le­bensleib nicht unmittelbar mit äußeren Wahrnehmungsorganen, mit physischen Augen gesehen werden kann, sondern daß dies sozusagen eine Angelegenheit des hellseherischen Bewußtseins ist. Wenn aber die Tätigkeit dieser Wesenheiten, also dieser Volksgeister, in das Men­schenleben hineinragt, so muß doch auf der anderen Seite irgend etwas aufzuzeigen sein, irgend etwas anzuführen sein, was in einer gewissen Weise im Äußerlichen sichtbar, eine Art Abdruck, eine Art Abglanz dieser Arbeit jener Volksgeister oder Erzengelwesen ist. Außerdem müssen ja diese Wesenheiten gewissermaßen auch einen physischen Leib haben. Es muß sich ihre Leiblichkeit in irgend einer Form zum Aus­druck bringen. Und diese physische Form, in der sie sich zum Ausdruck bringen, die Arbeit, die Wirksamkeit dieser Wesenheiten, die müßten sich auch in irgend einer Weise in der Welt andeuten, in der der Mensch ist, denn schließlich muß ja der Menschenleib etwas mit der Arbeit dieser geistigen Wesenheiten zu tun haben.",
      "Wir werden ausgehen von dem Äther- oder Lebensleib dieser Wesen­heiten und von der Arbeit, welche sie in diesem Äther- oder Lebensleib verrichten. Da also werden wir uns zunächst an die Forschungen des hellseherischen Bewußtseins wenden müssen. Wo findet nun die hell­seherische Forschung etwas, was bezeichnet werden kann als ein solcher Ätherleib dieser Erzengelwesen, dieser Archangeloi, und wie haben wir diese Arbeit aufzufassen? - Sie alle wissen, daß das Antlitz, die Ober­fläche unserer Erde an den verschiedenen Stellen verschieden ist, und daß an den verschiedenen Stellen unserer Erde in der allerverschiedensten",
      "Art die Bedingungen gegeben sind zur Entfaltung von Volkseigen­tümlichkeiten, von Volkseigenschaften. Das äußere materialistische Bewußtsein wird davon sprechen, daß Klima, Pflanzenwuchs, viel-leicht das Wasser irgend eines Landes oder einer Gegend unserer Erde maßgebend seien neben mancherlei anderem für das, was sich an Volks-eigentümlichkeiten, Volkseigenschaften kundgibt.",
      "Daß das materielle Bewußtsein, das Bewußtsein des physischen Planes so spricht, ist weiter nicht verwunderlich, denn dieses Bewußtsein des physischen Planes kennt eben nur das, was mit Augen gesehen werden kann. Für das hell­seherische Bewußtsein ist aber die Sache noch ganz anders.",
      "Wer mit hellseherischem Bewußtsein die verschiedenen Gebiete unserer Erde durchwandert, wer mit diesem Bewußtsein den einen oder anderen Boden unserer Erde betritt, der weiß, daß in dem eigentümlichen phy­sischen Pflanzenbild, in der eigentümlichen Konfiguration der Gesteine sich nicht alles dasjenige erschöpft, was er von diesem Boden, von die­sem Bilde irgend eines Erdengebietes weiß. Wenn aber für das materia­listische Bewußtsein nur von einem Abstraktum gesprochen wird, wenn wir von einem eigentümlichen Aroma, ja, von einer Aura eines bestimm­ten Gebietes unserer Erde sprechen, ist das wiederum begreiflich.",
      "Für das hellseherische Bewußtsein erhebt sich in der Tat über jedem Fleck unserer Erde dieses eigentümliche geistige Wolkengebilde, das man bezeichnen muß als die Äther-Aura eines besonderen Erdengebietes. Diese Äther-Aura ist anders, ganz anders über den Gefilden der Schweiz als über den Gefilden Italiens und wieder anders über den Gefilden Norwegens, Dänemarks oder Deutschlands.",
      "So wahr jeder Mensch seinen eigenen Ätherleib hat, so wahr ist über jedem Gebiete unserer Erdoberfläche eine Art Äther-Aura aufgetürmt.",
      "Diese Äther-Aura nun unterscheidet sich sehr wesentlich von anderen ätherischen Auren, sagen wir von den ätherischen Auren der Menschen. Wenn wir einen Menschen betrachten, der im Leben steht, dann finden wir, daß die Äther-Aura des Menschen an diesen Menschen gebunden ist, so lange er lebt, das heißt von der Geburt bis zum Tode. Sie war also sozusagen verbunden mit seinem physischen Leibe und ändert sich eigentlich nur insoweit, als der Mensch im Leben eine Entwickelung durchmacht, wenn er in bezug auf Intelligenz, Moral und so weiter",
      "höher steigt. Dann aber sehen wir immer, daß diese Äther-Aura des Menschen sozusagen von innen heraus sich ändert, gewisse Einschlüsse bekommt, die von innen aufglänzen, aufleuchten. Anders ist das bei jenen Äther-Auren, welche über den verschiedenen Ländergebieten wahrzunehmen sind. Gewiß, sie haben durch lange Zeiten hindurch einen gewissen Grundton, und sie haben etwas, was durch lange Zeiten hindurch bleibt. Aber es gibt in diesen Äther-Auren auch rasch sich vollziehende Änderungen, und diese rasch sich vollziehenden Änderun­gen sind das, was diese Auren von den menschlichen Auren unterschei­det, die sich langsam und allmählich ändern und, wenn sie sich ändern, diese Änderung nur von innen heraus vollziehen. Diese Auren über den verschiedenen Ländergebieten ändern sich nämlich im Laufe der Ent­wickelung der Erdenmenschheit dann, wenn ein Volk seinen Wohnsitz verläßt und von einem anderen Erdengebiete Besitz ergreift. Das ist das Eigentümliche, daß in der Tat die Äther-Aura, die über einem bestimmten Erdengebiete ist, nicht allein abhängt von dem, was sozu­sagen aus dem Boden aufsteigt, sondern daß sie davon abhängt, welches Volk zuletzt seinen Wohnsitz auf diesem Erdengebiete aufgeschlagen hatte.",
      "So suchen diejenigen, welche die Geschicke unseres Menschenge­schlechtes in ihrer wahren Gestaltung auf der Erde verfolgen wollen, das Ineinandergreifen gerade dieses Teiles der Äther-Auren unserer Erdengebiete zu verfolgen. Sehr, sehr änderten sich die verschiedenen Äther-Auren Europas in der Zeit, die man als die Zeit der Völkerwan­derung bezeichnet. Daraus sehen Sie schon, daß in dieser Äther-Aura über einem Erdengebiete etwas veränderlich ist, das in der Tat plötzlich sich umändern kann, und diese Umänderung kann in gewisser Bezie­hung sogar von außen gebracht werden. So ist eine jede solche Äther-Aura in gewisser Beziehung ein Zusammenfluß von dem, was aus dem Boden stammt und von dem, was sozusagen durch die Wanderungen der Völker hineingetragen wird.",
      "Wenn wir diese Aura betrachten, dann müssen wir uns klar sein dar­über, daß in gewisser Beziehung der Satz, der so leicht in der Geisteswis­senschaft angeführt wird, aber eigentlich im Grunde genommen niemals so recht verstanden wird oder wenigstens niemals so recht in seiner",
      "tiefen Tragweite betrachtet wird, die denkbar weiteste Gültigkeit hat, der Satz: daß alles, was das physische Bewußtsein draußen in der Welt sieht, doch nur Maja oder Illusion ist. Der Satz wird oftmals auf dem Gebiete der theosophischen Weltanschauung ausgesprochen, aber be­achtet im einzelnen, so daß man ihn wirklich ins Leben einführt, wird er doch im Grunde genommen recht wenig.",
      "Man spricht ihn mehr als abstrakte Wahrheit aus. Will man aber die konkreten Verhältnisse be­trachten, dann vergißt man ihn und bleibt beim materiellen Bewußtsein stehen. In Wahrheit ist dasjenige, was in geheimnisvoller Weise uns entgegentritt von dem Stück Erde, das von einem Volke bewohnt ist, die Äther-Aura des betreffenden Erdengebietes.",
      "Das, was den physi­schen Augen entgegentritt in der grünen Pflanzendecke der Erde, der eigentümlichen Konfiguration des Bodens und so weiter, das ist im Grunde genommen nur Maja oder äußerliche Illusion, das ist gleichsam eine Verdichtung dessen, was in der Äther-Aura wirkt. Allerdings ist nur dasjenige von dem Äußerlichen von dieser Äther-Aura abhängig, worauf die Äther-Aura, das heißt ein sich lebendig organisierendes Prin­zip Einfluß haben kann.",
      "Die Erzengel, die die geistigen Gesetze inne haben, können nicht in die physischen Gesetze eingreifen. Da hinein, wo also bloß die physischen Gesetze wirken und in Betracht kommen, wie bei den Gebirgsverhältnissen, der Wölbung des Bodens und so wei­ter, wo das, was die großen Änderungen des Volkes bedingt, abhängig ist von den physischen Verhältnissen, da hinein reicht der Einfluß der Erzengel nicht; so weit sind die Erzengel in ihrer Entwickelung noch nicht, daß sie in die physischen Verhältnisse eingreifen könnten.",
      "Weil sie das nicht können, weil sie da abhängig sind, deshalb müssen sie zu gewissen Zeiten über die Erde wandern, deshalb verkörpern sie sich in dem, was die Konfiguration des Bodens bedeutet, gleichsam als in dem physischen Leib, also in dem, was von den physischen Gesetzen be­herrscht ist. Da kann der Ätherleib des Volkes noch nicht hinein, da kann er sich noch nicht organisierend hinein erstrecken.",
      "Deshalb wird der Boden aufgesucht, wenn er sich als geeignet erweisen soll, und aus dieser Ehe zwischen dem Ätherleibe, der aber jetzt von geistig-seeli­schen Kräften durcharbeitet wird, und dem physischen Stück Erde entsteht dasjenige, was uns als der Zauberhauch im Äußern eines Volkstums",
      "entgegentritt, das, was der Mensch, der nicht Hellseher ist, in einem Lande bloß fühlen kann, was der Mensch aber, der mit hellsehe­rischem Bewußtsein Land und Volk durchschaut, erschauen kann.",
      "Wie aber wirkt jetzt dasjenige herein, was sozusagen die Arbeit des Erzengels, des Volksgeistes in dem Ätherleib, der über den Boden sich erhebt, ist? Was ist die Arbeit des Erzengels, wie wirkt er herein in das Menschliche, das auf diesem Boden sich bewegt, das in dieser Wolke des Volksgeistes darinnen lebt?",
      "Er wirkt so hinein, daß diese Kraft in drei Arten beim Menschen sich zum Ausdruck bringt. Die Äther-Aura des Volkes ist es, die in den Menschen hineinwirkt, den Menschen durch­setzt, durchwebt, und zwar wirkt diese Äther-Aura so in die mensch­liche Wesenheit hinein, daß ein Dreifaches in der menschlichen Wesen­heit davon ergriffen wird.",
      "Durch die Mischung dieses Dreifachen ent­steht dann der eigentümliche Charakter, den ein Mensch trägt, der in dieser Äther-Aura des Volkes darinnen lebt. Diese Äther-Aura, worauf wirkt sie beim Menschen?",
      "Sie wirkt auf ein Dreifaches in den Tempe­ramenten. Sie wirkt auf die Temperamente, die selber in das Emotions­leben des Menschen versenkt sind, die im Ätherleibe des Menschen darinnen wirken, nur nicht auf das sogenannte melancholische Tempe­rament.",
      "Die Äther-Aura des Volkes wirkt auf das cholerische, phleg­matische und sanguinische Temperament. Im allgemeinen also fließt das, was die Kraft der Äther-Aura des Volkes ist, in diese drei Tempe­ramente hinein.",
      "Nun können diese drei Temperamente in der einzelnen menschlichen Individualität in der verschiedensten Weise gemischt sein und zusammenwirken. Unendliche Mannigfaltigkeit können Sie sich da denken, wenn die drei Kräfte zusammenwirken, wenn die eine die andere beeinflußt, besiegt und so weiter.",
      "Dadurch entsteht die mannig­faltigste Konfiguration, die uns zum Beispiel in Rußland, Norwegen, Deutschland verschiedenartig entgegentritt. Das macht den Volks­charakter des Menschen aus, was in die Temperamente hineinwirkt.",
      "Der Unterschied, der hier bei den einzelnen Individuen besteht, wird nur durch den Grad der Mischung bewirkt. Die Volkstemperamente sind also nach den Einwirkungen der Volksaura gemischt.",
      "So also haben wir über die Erde hin wirksam die Volksgeister. Die haben aber auch ihre eigenen Wege; denn das ist für ihre eigenen Angelegenheiten",
      "nicht das Wesentliche, daß sie in die Temperamente hinein-wirken. Das tun sie nur deshalb, weil die Kräfte in der Welt in Wechsel­wirkung miteinander treten. Das tun sie zunächst als ihre gewollten Taten, als das, was ihre Mission ist.",
      "Daneben kommen aber auch die eigenen Angelegenheiten ihres Ichs in Betracht. Die bestehen darin, daß sie selber weiterkommen in ihrer Entwickelung, daß sie selber über die Erde schreiten und sich auf diesem oder jenem Gebiet der Erde verkör­pern.",
      "Das sind aber ihre eigenen Angelegenheiten. Das andere, was sie in den Temperamenten der Menschen tun, das ist etwas, was sie neben­bei arbeiten, was ihr Beruf ist. Natürlich kommt der Mensch auch wieder durch ihre Arbeit vorwärts, sie wirkt auf ihn zurück.",
      "Daher wirkt auch die menschliche Arbeit auf den Volksgeist zurück. Welche Bedeutung die einzelnen Menschen für den Volksgeist haben, das wer­den wir noch sehen. Das ist wichtig. Das Wesentliche ist aber, daß wir einen solchen Volksgeist verfolgen können, wie er sich in der Welt verkörpert, dann wieder eine Zeitlang in der geistigen Welt lebt und sich sodann wieder wo anders verkörpert und so weiter.",
      "Wenn wir diese Vorgänge betrachten, so haben wir immer nur Ich-Angelegenheiten dieser Wesen vor uns. Denken Sie sich also nun - damit Sie sich das recht konkret vorstellen - den menschlichen Ätherleib in den Volks­ätherleib eingebettet; denken Sie sich dann das Ineinanderwirken vom menschlichen Ätherleib und Volksätherleib, und denken Sie sich dar­auf, daß sich der Volksätherleib in den Volkstemperamenten spiegelt, spiegelt in der Mischung der Temperamente der einzelnen Menschen, dann haben Sie das Geheimnis, wie uns der Volksgeist in seiner Art innerhalb eines Volkes entgegentritt.",
      "Nun haben wir, nachdem wir dieses gesagt haben, im Grunde genom­men die wichtigste Arbeit der eigentlichen Erzengel oder Volksgeister erschöpft. Wir würden aber noch lange nicht die Eigentümlichkeiten eines Volkes erschöpft haben, wenn wir nur die Art des Charakters, wie ein Mensch ihn innerhalb dieses Volkes besitzt, in Betracht ziehen wollten. Aber die Erzengelwesenheiten, die die eigentlichen Geister der Volksstämme sind, die haben diese Aufgabe.",
      "Nun eignet aber einem Volke, wie Sie leicht ahnen können, noch manches andere. Woher kommt das? Wenn der Erzengel, der leitende",
      "Volksgeist sich nicht mit anderen Wesenheiten auf demselben Grund und Boden begegnen und nicht mit ihnen zusammenarbeiten würde in diesem Ätherleib des Menschen, dann würde manches von den Eigen­schaften eines Volkes gar nicht entstehen können. Der Mensch ist ein Schauplatz für die Begegnung der Erzengel mit noch anderen Wesen­heiten, die mit den Erzengeln zusammenwirken und sozusagen mit ihnen zusammenarbeiten. Aus diesem Zusammenarbeiten entsteht aber noch etwas ganz anderes. Das hellseherische Bewußtsein findet, wenn es die Völker studiert, merkwürdigerweise geheimnisvolle Wesenheiten außer den bereits charakterisierten Erzengelwesen, die in gewisser Be­ziehung den Erzengeln verwandt, aber doch wieder in anderer Bezie­hung vollständig von ihnen verschieden sind, vor allen Dingen dadurch, daß sie viel größere Kräfte anzuwenden vermögen als die Volksgeister selber. Der Volksgeist wirkt in einer außerordentlich feinen und inti­men Weise auf die einzelne menschliche Seele in diesem Hineinweben in die Temperamente. Aber in einer viel stärkeren, kraftvolleren Weise wirken da noch andere Wesenheiten hinein. Diese anderen Wesenheiten müssen wir uns einmal aus unserer allgemeinen Kenntnis der Hierar­chien klar machen. Da werden wir sozusagen den Namen finden für diese anderen Wesenheiten, die das hellseherische Bewußtsein beob­achtet. Stellen Sie sich einmal vor die Hierarchien der Geister in fol­gender Weise:",
      "1.    Menschen,",
      "2.    Engel,",
      "3.    Erzengel,",
      "4.    Urbeginne oder Geister der Persönlichkeit,",
      "5.    Gewalten oder Geister der Form.",
      "Sodann würden wir weiter zu anderen kommen, die wir aber heute nicht weiter in Betracht ziehen wollen. Wenn Sie sich nun an dasjenige erinnern, wovon wir gestern gesprochen haben - und was Sie auch genau auseinandergesetzt finden in den Mitteilungen aus der «Akasha­Chronik» und in meiner Schrift «Die Geheimwissenschaft» -, so wer­den Sie sich sagen: Von diesen Wesenheiten sind es die Erzengel, welche während der alten Sonnenzeit ihre Menschheitsstufe durchgemacht haben. Da waren diejenigen Wesenheiten, die wir Geister der Form",
      "oder Gewalten nennen, die jetzt zwei Stufen höher sind als die Erz­engel, auf der Erzengelstufe; sie waren Archangeloi, solche Wesenhei­ten, wie es die heute charakterisierten Volksgeister sind. Das war da­mals ihre normale Entwickelungsstufe.",
      "Nun gibt es aber ein eigentümliches Geheimnis in der Entwickelung, das ist das Gesetz von dem Zurückbleiben gewisser Wesenheiten, das Gesetz, welches bewirkt, daß auf jeder Stufe gewisse Wesenheiten zu­rückbleiben, die dann auf der folgenden Stufe nicht auf der normalen Höhe stehen, sondern eigentlich den Charakter haben, den sie auf den früheren Stufen haben sollten. Nun sind während unserer Menschheits­evolution immer Wesenheiten zurückgeblieben.",
      "Unter diesen Zurück­gebliebenen sind auch solche Geister der Form, solche Gewalten, und sie sind in einer ganz eigenartigen Weise zurückgeblieben, nämlich so, daß sie zwar in bezug auf gewisse Eigenschaften Geister der Form, Gewalten sind, daß sie durch gewisse Eigenschaften das können, was heute nur die Geister der Form können, die den Menschen auf der Erdenstufe das Ich verliehen haben, daß sie das aber nicht vollständig können, weil sie nicht alle dazu notwendigen Eigenschaften besitzen. Sie sind so stehen geblieben, daß sie nicht auf der Sonne, sondern jetzt während ihrer Erdenzeit ihre Erzengelstufe durchmachen, so daß sie Wesenheiten sind, die jetzt auf der Stufe der Volksgeister stehen, aber ganz andere Eigenschaften haben.",
      "Während die Volksgeister intim hineinwirken in das Menschenleben, weil sie zwei Stufen höher stehen als der Mensch, also mit den Menschen immer noch verwandt sind, sind diese Gewalten, diese Geister der Form vier Stufen über die Menschheitsstufe erhaben. Sie haben daher ungeheuer viele und große Kräfte, die nicht dazu taugen würden, so intim in die Menschen hinein­zuwirken.",
      "Sie würden robuster wirken, aber kein anderes Gebiet haben für ihre Wirksamkeit als dasjenige, auf dem die normalen Volksgeister, die Erzengel, stehen.",
      "Das ist das Schwierige, daß man erst unterscheiden lernen muß in der höheren Welt. Die, welche glauben, mit ein paar Begriffen in den höheren Welten auskommen zu können, irren sich sehr. Der Mensch, der mit oberflächlichen Begriffen in die höheren Welten hinaufsteigt, der findet da wohl die Erzengel. Aber man muß unterscheiden, ob es",
      "Wesen sind, die jetzt normalerweise auf die Erzengelstufe gekommen sind oder solche, die während des Sonnenzustandes der Erde auf dieser Stufe hätten stehen sollen. So also wirken auf dem gleichen Gebiete mit den Geistern der Volksstämme oder Erzengeln zusammen andere We­senheiten, die sozusagen in der Rangordnung der Erzengel stehen, die aber mit ganz anderen, robusteren Eigenschaften begabt sind, mit sol­chen Eigenschaften, wie sie die sonstigen Geister der Form haben, und die dadurch tief eingreifen können in die menschliche Natur. Denn was haben diese Geister der Form während des Erdendaseins aus dem Men­schen gemacht? Denken Sie sich, daß die Menschen zu sich nicht Ich sagen könnten, wenn die Geister der Form nicht das Gehirn geformt hätten zu dem, was der Mensch heute als solches besitzt. Also bis in die physische Gestaltung hinein können solche Wesenheiten wirken, trotz­dem sie nur auf der Stufe der Erzengel stehen. Sie treten in eine Art von Wettkampf mit den Volksgeistern auf dem Terrain, wo die Volks-geister wirken.",
      "Das erste, was sie hauptsächlich bewirken, indem diese Geister von der einen Seite und die anderen von der anderen Seite zusammenstoßen, ist die Sprache, das, was nicht entstehen könnte ohne den ganzen Bau und die Form des menschlichen Leibes. In dem Bau des Menschen haben Sie die Wirksamkeit dieser anderen Volksgeister, die mit den Natur­gewalten und mit den Menschen verbunden werden. Also die Sprache dürfen wir nicht einfach denselben Wesenheiten zuschreiben, die in intimer Weise in das Volkstemperament hineinwirken und dem Volke als um zwei Stufen über dem Menschen stehende Wesen ihre Konfigu­ration aufprägen. Die Wesen, welche die Sprache geben, haben große Kraft, sie sind eigentlich Gewalten; sie wirken auf die Erde, weil sie auf der Erde geblieben sind, während ihre anderen Genossen im Ich wirken von der Sonne aus in den Weltenraum hinein. Von den Men­schen wurde vor dem Erscheinen des Christus Jesus das Jahve- oder Jehova-Wesen verehrt, und sie verehrten nachher als vom Weltenraum hereinwirkend das Christuswesen. In bezug auf die Sprachgeister müs­sen wir sagen, daß in der Sprache gerade das vom Menschen geliebt wird, was bei der Erde verblieben ist. Wir müssen uns ganz andere Anschauungen angewöhnen. Der Mensch ist gewohnt, seine eigenen",
      "Begriffe auf das ganze Weltall anzuwenden. Er tut natürlich sehr Un­recht, wenn er die Tatsache, daß diese hohen Wesenheiten zurückblei­ben in der Entwickelung, ungefähr so betrachtet, wie wenn ein Schul­mädchen in einer Klasse sitzen bleibt. Sie bleiben nicht sitzen, weil sie nicht gelernt haben, sondern aus Gründen großer Weisheit, die in der Welt waltet. Würden nicht gewisse Wesenheiten auf ihre normale Weiterentwickelung verzichten und, statt mit der Sonne weiterzugehen, ihre Weiterentwickelung auf der Erde durchmachen, so würde das nicht auf der Erde haben entstehen können, was wir Sprache nennen. In gewisser Beziehung hat der Mensch seine Sprache innig zu lieben, und zwar aus dem Grunde, weil sozusagen aus Liebe bei ihm geblieben sind hohe Wesenheiten, die verzichtet haben auf gewisse Eigenschaften, damit der Mensch sich so entwickeln kann, wie das der Weisheit ent­spricht. Gerade so wie wir das Vorauseilen als eine Art von Opfer ansehen müssen, so müssen wir auch das Zurückbleiben in früheren Entwickelungsepochen als eine Art von Opfer ansehen, und wir müssen uns durchaus klar sein, daß die Menschen zu gewissen Eigenschaften gar nicht hätten kommen können, wenn nicht solche Opfer gebracht worden wären.",
      "So also sehen wir, wie in dem Ätherleibe des Menschen und in dem Ä therleibe des Volksgeistes, der in Betracht kommt, zweierlei Wesen­heiten ihre Arbeit austauschen: die normal entwickelten Erzengel und die auf der Erzengelstufe stehengebliebenen Geister der Form, die ver­zichtet haben auf ihre eigene Entwickelung, um den Menschen während ihres Erdendaseins die Volkssprache einzuverleiben. Sie mußten die Kraft haben, den Kehlkopf, die ganzen Sprachwerkzeuge so umzubil-den, daß das Ergebnis dieser Sprachwerkzeuge eine physische Manife­station, nämlich gerade die Sprache ist. Wir müssen also als Ergebnis dieses Zusammenwirkens gerade dasjenige ansehen, was als Volksge­müt, als Volkstemperament mit der Sprache im Bunde uns entgegen­tritt. Was der Mensch auszusprechen vermag, wodurch er sich als Angehöriger seines Volkes kundgibt, was er hinaustönen läßt in die Luft, das ist dasjenige, was die mit den Volksgeistern verbündeten Geister der Form nur deshalb bewirken können, weil sie mit ihren großen Kräften und Gewalten auf der Stufe der Volksgeister stehen",
      "geblieben sind. So findet also ein solches Zusammenwirken statt inner­halb derjenigen Terrains, derjenigen Gebiete, wo die Volksgeister wir­ken. Ein ähnliches Zusammenwirken findet aber auch noch auf einem anderen Gebiete statt.",
      "Ich habe gestern angeführt, daß noch andere Kräfte, die Urbeginne oder die Geister der Persönlichkeit, die während des Erdendaseins das darstellen, was man Zeitgeist nennt, wirksam sind. Diese wirken so, daß sie von ihrem eigentlichen Ich aus, von ihrer seelischen Organisa­tion aus, in den physischen Leib hineinarbeiten, daß sie also die Kräfte des physischen Leibes in Bewegung bringen.",
      "Wir müssen also voraus­setzen, daß, wenn in einer bestimmten Zeit als Ergebnis der Wirkung des Zeitgeistes irgend etwas eintritt, irgend etwas sich innerhalb eines Zeitgeistes offenbart, wodurch die Menschheit einen Fortschritt macht, daß das einer Arbeit mit physischen Kräften innerhalb unseres Erden-daseins entspricht. Sie können das sehr leicht einsehen, Sie brauchen es sich nur zu überlegen, um zu begreifen, wie wirklich physische Voraus­setzungen notwendig sind, damit dieses oder jenes im Zeitgeiste entsteht.",
      "Oder können Sie sich vorstellen, daß unter anderen Voraussetzungen Kepler oder Kopernikus oder Perikles in einer anderen Zeit gelebt haben könnten? Die Persönlichkeiten wachsen aus ganz bestimmten Zeitverhältnissen heraus, aus denjenigen Verhältnissen, die in einem bestimmten Zeitpunkte durch die physische Arbeit von höheren Wesen­heiten konfiguriert und organisiert werden.",
      "Da sind es in der Tat die physischen Verhältnisse, freilich physische Verhältnisse, die wir uns nicht als materielle Klötze vorzustellen haben, sondern als gewisse Konfigurationen in der physischen Gemeinsamkeit unserer Erde. Manchmal tritt diese Konfiguration ganz gewaltig hervor; manchmal muß dabei, wenn der Zeitgeist in irgendeiner Weise seinen Einfluß übt, eine ganz bestimmte physische Konstellation zustande kommen.",
      "Den­ken Sie nur daran, daß, als man einmal erst ganz bestimmt geschliffene Gläser hatte, diese durch Kinderspiel in einer Glasschleiferwerkstätte so zusammengefügt wurden, daß man daran bemerken konnte die opti­sche Wirkung als Fernglas, so daß der Erfinder des Fernrohres nur die Beobachtung dieses Gesetzes des Fernrohres zu realisieren brauchte.",
      "Diese Sache ist ein historisches Faktum. Denken Sie sich aber, welche",
      "physischen Vorgänge notwendig waren, damit das alles hat stattfinden können! Die Linsen mußten erst erfunden, geschliffen und in der ent­sprechenden Weise zusammengesetzt werden. Sie können da wohl das Wort «Zufall» gebrauchen, aber Sie können es nur anwenden, wenn Sie darauf verzichten, die Gesetzmäßigkeit auch in solchen Gescheh­nissen zu begreifen. Diese physischen Verhältnisse führen zusammen die Archai, die Urkräfte. Das Spiegelbild ihrer Arbeit ist das, was an einem Punkte der Erde zusammenführend wirkt, was sonst als Zeitgeist in mannigfaltiger Weise wirkt. Denken Sie sich, was in neuerer Zeit mit vielen physischen Dingen nicht geworden wäre, wenn diese Arbeit der Archai in Ihren physischen Leibern nicht stattgefunden hätte. So ist es in der Tat die Arbeit der Archai, welche in dieser Beziehung, in dieser Richtung wirkt.",
      "Wenn nun diese Archai in dieser Weise wirken und den Zeitgeist dirigieren, so können wir uns wieder fragen: Wie intuieren eigentlich diese Zeitgeister den Menschheitsfortschritt? Sie intuieren ihn dadurch, daß einen Menschen das, was im Physischen geschieht, wie zufällig an­regt. Es sind nicht bloß Legenden, wenn auch das manchmal zutrifft. Ich erinnere nur an die schwingende Kirchenlampe im Dome zu Pisa, wo Galilei das Pendelgesetz entdeckt hat an den regelmäßigen Schwin­gungen der Lampe im Dom, und wie dann Kepler und Newton zu ihren Entdeckungen angeregt wurden. Hunderte und Tausende von Fällen könnte man erzählen, wo physisches Geschehen zusammengeführt wird mit menschlichem Denken, woraus man ersehen könnte, wie da intuiert wird von den Archai oder Urkräften das, was als Ideen, als Zeitideen in die Welt hinausgeht, was die Menschen dann in ihrer Entwickelung beeinflußt, was ihren Fortschritt regelt und gesetzmäßig durchdringt. Aber auch auf diesem Gebiet wirken zusammen die Wesenheiten, die normalerweise während unseres Erdendaseins Geister der Persönlich­keit geworden sind, mit anderen, die dadurch, daß sie auf dem Mond zurückgeblieben sind, jetzt nicht Geister der Form oder Gewalten sind, wie sie auf der Erde sein sollten, sondern auch jetzt erst wirken als Gei­ster der Persönlichkeit.",
      "So sind diejenigen Wesenheiten, die nicht schon von der Sonnenstufe, sondern erst von der Mondenstufe aus verzichtet haben, jetzt Geister",
      "der Persönlichkeit, aber nicht mit den Eigenschaften, die sie normaler­weise haben sollten, das heißt, sie intuieren nicht in der Weise wie die normalen Geister der Persönlichkeit, sondern als zurückgebliebene Gei­ster der Form. Sie regen nicht von außen an und überlassen es intim dem Menschen selber, das zu beobachten, was im Physischen bewirkt wird, sondern sie regen im Innern an, sie konfigurieren im Innern des Gehirns und geben dem Denken eine gewisse Richtung.",
      "Daher ist das Denken des Menschen in den verschiedenen Zeiträumen von innen angeregt, so daß jedes Zeitalter eine bestimmte Art des Denkens hat. Das hängt mit den feinen Konfigurationen des Denkens zusammen, mit inneren Konstellationen.",
      "Da arbeiten die zurückgebliebenen Geister der Form, die den Charakter der Geister der Persönlichkeit haben, im Innern der Menschen und bringen eine gewisse Denkart, eine ganz bestimmte Form der Begriffe hervor. Das macht es, daß die Menschen von Epoche zu Epoche nicht nur geführt werden im Sinne der intuie­renden Geister der Persönlichkeit, wo sie sich selber anregen lassen, das oder jenes zu tun, sondern daß sie fortgetrieben werden wie durch innere Kräfte, so daß das Denken von innen heraus sich physisch kund-gibt, wie sich in der Sprache kundgibt das, was auf der anderen Seite als Geister der Form zurückgeblieben ist.",
      "So drückt die Denkart sich aus als eine Manifestation der Geister der Form, die in unserer Zeit als Geister der Persönlichkeit auftreten. Es sind also nicht so intim wir­kende Geister der Persönlichkeit, die es dem Menschen überlassen, zu machen, was er will, sondern ihn ergreifen und mit vorwärtsstürmender Gewalt drängen.",
      "Daher können Sie immer diese zwei Typen in denjeni­gen Menschen sehen, welche von dem Zeitgeist angeregt sind. In den­jenigen, welche von den wahren Zeitgeistern, von den auf normaler Stufe stehenden, angeregt sind, können Sie sozusagen sehen die wahren Vertreter ihrer Zeit.",
      "Wir können sie betrachten als Menschen, die kom­men mußten, und ihre Tätigkeit als etwas, was nicht anders hat gesche­hen können. Es kommen aber auch andere Menschen, in denen wirken diejenigen Geister der Persönlichkeit, die eigentlich Geister der Form sind.",
      "Das sind die anderen Geister, die wir bezeichnet haben als die Denkgeister, die während des Mondenzyklus auf ihren jetzigen Stand­punkt vorrückten. Der Mensch ist nun der Schauplatz, auf dem alles",
      "dies zusammenwirkt. Dieses Zusammenwirken macht sich dadurch geltend, daß Sprache und Denken in ein Wechselverhältnis treten, da­durch, daß nicht bloß die Geister, die auf der gleichen Stufe stehen, in ein Wechselverhältnis kommen, sondern daß auch die normalen Erz­engel, die Volksgemüt und Volkstemperament regeln, in Wechselver­hältnisse treten mit dem, was eben charakterisiert worden ist, also nicht nur mit den auf der Erzengelstufe stehenden Geistern der Form, son­dern auch mit denjenigen Geistern der Persönlichkeit, die eigentlich zurückgebliebene Geister der Form sind.",
      "Diese zwei Arten treten in der menschlichen Natur und menschlichen Wesenheit auf. Dieses Verhältnis ist im höchsten Grade interessant zu studieren, wenn man mit okkulten Kenntnissen, mit okkultem Sehver­mögen von Volk zu Volk geht.",
      "Da kann man sehen, wie die normalen Volksgeister wirken, und wie dann diese normalen Volksgeister ihre Befehle von den Zeitgeistern bekommen; wie aber diese Volksgeister zusammenwirken im Innern des Menschen mit den Sprachgeistern und auch mit den Denkgeistern, die in die Gedanken der Menschen hinein-wirken. Da finden sich im Innern des Menschen nicht nur normale Erzengel und abnorme Erzengel, sondern auch die Erzengel im Gegen­satz mit den abnormen Geistern der Persönlichkeit, die von innen heraus die Gedankenarbeit einer bestimmten Zeit regeln.",
      "Da ist es nun im höchsten Grade interessant - ich habe gesagt, es werden Zustände angedeutet werden, denen Sie entgegenkommen müssen mit Ihrem spirituellen Verständnis, die eingekleidet werden müssen in gewöhn­liche Worte, weil im Leben noch keine Sprache geschaffen ist, die alles das glaubhaft und verständlich machen würde; man muß alles aus­drücken in Worten, die den Tatbestand etwas bildhaft geben, was aber einer bedeutungsvollen Tatsache der Menschheitsentwickelung ent­spricht -, da ist es nun im höchsten Grade interessant und wichtig, der Menschheitsentwickelung in neuerer Zeit zu folgen, wichtig zu wissen, daß einmal geradezu ein gegenseitiger Vertrag geschlossen worden ist von einem der leitenden Geister der Völker, der ein normaler Erzengel ist, mit einem solchen Geist, der als Geist der Denkkräfte im Innern wirkt, also mit einem abnormen Geist der Persönlichkeit, und es zeigt sich in einer gewissen geschichtlichen Epoche das ernste, bedeutsame",
      "Ergebnis dieses Vertrages. Um diesen Vertrag noch besonders voll zu machen, wurde ein harmonisches Verhältnis hergestellt mit dem ent­sprechenden abnormen Erzengel, der der leitende Geist der Sprache in jener Zeit war, so daß es einen Punkt in der Menschheitsentwickelung gibt, wo sozusagen zusammenwirkt normales und abnormes Erzengel­tum, und wo außerdem noch als Einschlag hineinwirkt die Denkungs­art, die von innen heraus durch einen abnormen Geist der Persönlich­keit bewirkt wird.",
      "Dieser Vertrag zwischen diesen drei Parteien spiegelt sich in einem bestimmten Volke wider. Das ist das indische Volk, das Volk, das in der ersten nachatlantischen Zeit die nachatlantische Kultur einleitete.",
      "Während dieser indischen Kultur trat jene Konstellation ein, wo jene drei Wesenheiten am harmonischsten zusammenwirkten. Die Folge davon ist alles dasjenige, was wir als die historische Rolle dieses indischen Volkes bezeichnen können.",
      "Auch in den Zeiten, von denen es schon geschichtliche Überlieferungen gibt, wirkt das nach, was da­mals in dem Vertrag abgeschlossen wurde. Dies war der Grund, warum mit einer solchen Gewalt die alte heilige Sprache der Inder wirkte und jene gewaltigen historischen Kulturwirkungen hatte, warum sie noch so gewaltig in der Folgezeit wirken konnte.",
      "Diese Kraft brachten die abnormen Erzengel, die in der Sprache wirkten. Diese Gewalt der Sans­kritsprache beruht gerade auf dem Vertrage, von dem ich eben gespro­chen habe. Und wiederum beruht darauf die eigenartige indische Phi­losophie, die als Philosophie, als vom Innern des Menschen heraus schaffendes Denken noch nicht erreicht ist von irgendeinem andern Volke der Welt; darauf beruht die innere Geschlossenheit des Denkens der indischen Kultur.",
      "Bei allen andern Gebieten haben wir andere Ver­hältnisse zu beobachten. In ihr allein trat dazumal das zutage, was jetzt charakterisiert worden ist. Daher ist es so unendlich reizvoll, diesen Gedankengängen zu folgen, die dadurch eine besondere Konfi­guration haben, weil sie hervorgegangen sind nicht aus dem Überge­wichte des normalen Erzengels über den abnormen, sondern als etwas, was in Harmonie mit jener Geschlossenheit steht, weil tatsächlich jeder Gedanke vom Volkstemperament absorbiert und mit Liebe ins einzelne hinein fortgesponnen worden ist - damals, als das indische Volk als erste Kulturblüte der nachatlantischen Zeit vorhanden war.",
      "Sprache wirkte so fort aus dem Grunde, weil da nicht ein Kampf ent­standen war, der sonst überall entstanden wäre, sondern weil ein Zu­sammenwirken zwischen dem Erzengel der normalen Entwickelung und dem Erzengel der abnormen Entwickelung stattfand, so daß man sagen kann, daß die Sprache, ausgegossen von dem reinsten Tempera­ment, selber ein Produkt des Temperamentes ist. Das ist das Geheimnis dieses ersten Kulturvolkes der nachatlantischen Zeit.",
      "Das aber ist es, was betrachtet werden muß bei allen andern Völkern, daß nämlich bei ihnen eine eigenartige Zusammenwirkung entsteht zwischen diesen drei Kräften, zwischen dem normalen Volksgeist oder Erzengel, dem abnormen Erzengel und zwischen dem, was innerlich wirkt in dem abnormen Geist der Zeit, der nicht als Zeitgeist, sondern von innen heraus wirkt, und endlich dem, was der wahre Zeitgeist dem Volke innerlich übertragen hat. Darauf beruht die wahre Erkenntnis eines Volkes, daß man diese Kräfte im Innern belauscht, daß man den Anteil prüft, den ein jeder Faktor an der Konstitution des Volkes hat.",
      "Daher ist es schwierig geworden für die Menschen, welche nicht die okkulten Kräfte der Menschheitsentwickelung in Frage ziehen, eigent­lich das Wort «Volk» zu definieren. Versuchen Sie einmal die einzelnen Bücher herzunehmen, worin der Begriff des Volkes irgendwo in der Welt definiert worden ist, und Sie werden sehen, was da alles als Defi­nition des Begriffes Volk existiert und wie sehr sie voneinander abwei­chen.",
      "Sie müssen ja voneinander abweichen, weil der eine mehr fühlt, was von der einen Seite, von den normalen Erzengeln herkommt, der andere mehr fühlt, was von dem abnormen Erzengel herrührt und der Dritte wieder das, was von den einzelnen Persönlichkeiten des Volkes kommt. Ein jeder fühlt etwas anderes und verwertet es in seiner Defini­tion.",
      "Das ist es gerade, was uns klar geworden ist durch die Geisteswis­senschaft, daß diese Definitionen nicht immer falsch zu sein brauchen; sie sind nur immer in Maja, in Illusion getaucht. An dem, was einer sagt, kann man sehen, ob er nur die Maja betrachtet, und ob er die verschiedenen wirkenden Kräfte unberücksichtigt läßt.",
      "Daher wird man selbstverständlich immer einen ganz anderen Begriff bekommen, wenn vom geisteswissenschaftlichen Standpunkte aus ein Volk wie das schweizerische, das auf demselben Grund und Boden lebt und drei",
      "Sprachen spricht, und dagegen Völker mit einheitlicher Sprache be­trachtet werden.",
      "Warum Völker mehr aus dem Geiste der Persönlichkeit heraus wir­ken, also durch das Zusammenwirken der einzelnen Persönlichkeiten namentlich ihr Dasein haben, darüber werden wir noch zu sprechen haben. Solche Völker, die mehr ihr Dasein haben durch den abnormen Geist der Persönlichkeit, werden wir auch auf der Erde finden. Diese Geister der Persönlichkeit wirken nicht auf Weiterentwickelung hin. Sie brauchen sich nur den Charakter des nordamerikanischen Volkes klar zu legen, so haben Sie ein Volk, das vorderhand auf diesem Prinzip beruht. So werden Sie sehen, daß wir die Weltgeschichte, insofern sie Völkergeschichte ist, erst verstehen werden, wenn wir normale und ab­norme Erzengel, normale und abnorme Geister der Persönlichkeit in ihrem gegenseitigen Rang und ihrem Zusammenwirken und gleichzeitig in der Aufeinanderfolge der Völker im Verlaufe der Weltgeschichte verfolgen werden."
    ],
    "sentences": [
      [
        "Es ist gestern gesagt worden, daß diejenigen Wesenheiten, welche als Volksgeister zu betrachten sind, auf einer solchen Stufe stehen, daß sie in ihrem gegenwärtigen Dasein von ihrer Ichheit aus an ihrem Äther-oder Lebensleib arbeiten, daß sie also diesen Äther- oder Lebensleib von dem innersten Wesen ihres Seelischen heraus bearbeiten."
      ],
      [
        "Nun wird ja natürlich jeder von Ihnen sich sagen können: Gewiß muß es zugegeben werden, daß die Arbeit an diesem Äther- oder Le­bensleib nicht unmittelbar mit äußeren Wahrnehmungsorganen, mit physischen Augen gesehen werden kann, sondern daß dies sozusagen eine Angelegenheit des hellseherischen Bewußtseins ist.",
        "Wenn aber die Tätigkeit dieser Wesenheiten, also dieser Volksgeister, in das Men­schenleben hineinragt, so muß doch auf der anderen Seite irgend etwas aufzuzeigen sein, irgend etwas anzuführen sein, was in einer gewissen Weise im Äußerlichen sichtbar, eine Art Abdruck, eine Art Abglanz dieser Arbeit jener Volksgeister oder Erzengelwesen ist.",
        "Außerdem müssen ja diese Wesenheiten gewissermaßen auch einen physischen Leib haben.",
        "Es muß sich ihre Leiblichkeit in irgend einer Form zum Aus­druck bringen.",
        "Und diese physische Form, in der sie sich zum Ausdruck bringen, die Arbeit, die Wirksamkeit dieser Wesenheiten, die müßten sich auch in irgend einer Weise in der Welt andeuten, in der der Mensch ist, denn schließlich muß ja der Menschenleib etwas mit der Arbeit dieser geistigen Wesenheiten zu tun haben."
      ],
      [
        "Wir werden ausgehen von dem Äther- oder Lebensleib dieser Wesen­heiten und von der Arbeit, welche sie in diesem Äther- oder Lebensleib verrichten.",
        "Da also werden wir uns zunächst an die Forschungen des hellseherischen Bewußtseins wenden müssen.",
        "Wo findet nun die hell­seherische Forschung etwas, was bezeichnet werden kann als ein solcher Ätherleib dieser Erzengelwesen, dieser Archangeloi, und wie haben wir diese Arbeit aufzufassen? - Sie alle wissen, daß das Antlitz, die Ober­fläche unserer Erde an den verschiedenen Stellen verschieden ist, und daß an den verschiedenen Stellen unserer Erde in der allerverschiedensten"
      ],
      [
        "Art die Bedingungen gegeben sind zur Entfaltung von Volkseigen­tümlichkeiten, von Volkseigenschaften.",
        "Das äußere materialistische Bewußtsein wird davon sprechen, daß Klima, Pflanzenwuchs, viel-leicht das Wasser irgend eines Landes oder einer Gegend unserer Erde maßgebend seien neben mancherlei anderem für das, was sich an Volks-eigentümlichkeiten, Volkseigenschaften kundgibt."
      ],
      [
        "Daß das materielle Bewußtsein, das Bewußtsein des physischen Planes so spricht, ist weiter nicht verwunderlich, denn dieses Bewußtsein des physischen Planes kennt eben nur das, was mit Augen gesehen werden kann.",
        "Für das hell­seherische Bewußtsein ist aber die Sache noch ganz anders."
      ],
      [
        "Wer mit hellseherischem Bewußtsein die verschiedenen Gebiete unserer Erde durchwandert, wer mit diesem Bewußtsein den einen oder anderen Boden unserer Erde betritt, der weiß, daß in dem eigentümlichen phy­sischen Pflanzenbild, in der eigentümlichen Konfiguration der Gesteine sich nicht alles dasjenige erschöpft, was er von diesem Boden, von die­sem Bilde irgend eines Erdengebietes weiß.",
        "Wenn aber für das materia­listische Bewußtsein nur von einem Abstraktum gesprochen wird, wenn wir von einem eigentümlichen Aroma, ja, von einer Aura eines bestimm­ten Gebietes unserer Erde sprechen, ist das wiederum begreiflich."
      ],
      [
        "Für das hellseherische Bewußtsein erhebt sich in der Tat über jedem Fleck unserer Erde dieses eigentümliche geistige Wolkengebilde, das man bezeichnen muß als die Äther-Aura eines besonderen Erdengebietes.",
        "Diese Äther-Aura ist anders, ganz anders über den Gefilden der Schweiz als über den Gefilden Italiens und wieder anders über den Gefilden Norwegens, Dänemarks oder Deutschlands."
      ],
      [
        "So wahr jeder Mensch seinen eigenen Ätherleib hat, so wahr ist über jedem Gebiete unserer Erdoberfläche eine Art Äther-Aura aufgetürmt."
      ],
      [
        "Diese Äther-Aura nun unterscheidet sich sehr wesentlich von anderen ätherischen Auren, sagen wir von den ätherischen Auren der Menschen.",
        "Wenn wir einen Menschen betrachten, der im Leben steht, dann finden wir, daß die Äther-Aura des Menschen an diesen Menschen gebunden ist, so lange er lebt, das heißt von der Geburt bis zum Tode.",
        "Sie war also sozusagen verbunden mit seinem physischen Leibe und ändert sich eigentlich nur insoweit, als der Mensch im Leben eine Entwickelung durchmacht, wenn er in bezug auf Intelligenz, Moral und so weiter"
      ],
      [
        "höher steigt.",
        "Dann aber sehen wir immer, daß diese Äther-Aura des Menschen sozusagen von innen heraus sich ändert, gewisse Einschlüsse bekommt, die von innen aufglänzen, aufleuchten.",
        "Anders ist das bei jenen Äther-Auren, welche über den verschiedenen Ländergebieten wahrzunehmen sind.",
        "Gewiß, sie haben durch lange Zeiten hindurch einen gewissen Grundton, und sie haben etwas, was durch lange Zeiten hindurch bleibt.",
        "Aber es gibt in diesen Äther-Auren auch rasch sich vollziehende Änderungen, und diese rasch sich vollziehenden Änderun­gen sind das, was diese Auren von den menschlichen Auren unterschei­det, die sich langsam und allmählich ändern und, wenn sie sich ändern, diese Änderung nur von innen heraus vollziehen.",
        "Diese Auren über den verschiedenen Ländergebieten ändern sich nämlich im Laufe der Ent­wickelung der Erdenmenschheit dann, wenn ein Volk seinen Wohnsitz verläßt und von einem anderen Erdengebiete Besitz ergreift.",
        "Das ist das Eigentümliche, daß in der Tat die Äther-Aura, die über einem bestimmten Erdengebiete ist, nicht allein abhängt von dem, was sozu­sagen aus dem Boden aufsteigt, sondern daß sie davon abhängt, welches Volk zuletzt seinen Wohnsitz auf diesem Erdengebiete aufgeschlagen hatte."
      ],
      [
        "So suchen diejenigen, welche die Geschicke unseres Menschenge­schlechtes in ihrer wahren Gestaltung auf der Erde verfolgen wollen, das Ineinandergreifen gerade dieses Teiles der Äther-Auren unserer Erdengebiete zu verfolgen.",
        "Sehr, sehr änderten sich die verschiedenen Äther-Auren Europas in der Zeit, die man als die Zeit der Völkerwan­derung bezeichnet.",
        "Daraus sehen Sie schon, daß in dieser Äther-Aura über einem Erdengebiete etwas veränderlich ist, das in der Tat plötzlich sich umändern kann, und diese Umänderung kann in gewisser Bezie­hung sogar von außen gebracht werden.",
        "So ist eine jede solche Äther-Aura in gewisser Beziehung ein Zusammenfluß von dem, was aus dem Boden stammt und von dem, was sozusagen durch die Wanderungen der Völker hineingetragen wird."
      ],
      [
        "Wenn wir diese Aura betrachten, dann müssen wir uns klar sein dar­über, daß in gewisser Beziehung der Satz, der so leicht in der Geisteswis­senschaft angeführt wird, aber eigentlich im Grunde genommen niemals so recht verstanden wird oder wenigstens niemals so recht in seiner"
      ],
      [
        "tiefen Tragweite betrachtet wird, die denkbar weiteste Gültigkeit hat, der Satz: daß alles, was das physische Bewußtsein draußen in der Welt sieht, doch nur Maja oder Illusion ist.",
        "Der Satz wird oftmals auf dem Gebiete der theosophischen Weltanschauung ausgesprochen, aber be­achtet im einzelnen, so daß man ihn wirklich ins Leben einführt, wird er doch im Grunde genommen recht wenig."
      ],
      [
        "Man spricht ihn mehr als abstrakte Wahrheit aus.",
        "Will man aber die konkreten Verhältnisse be­trachten, dann vergißt man ihn und bleibt beim materiellen Bewußtsein stehen.",
        "In Wahrheit ist dasjenige, was in geheimnisvoller Weise uns entgegentritt von dem Stück Erde, das von einem Volke bewohnt ist, die Äther-Aura des betreffenden Erdengebietes."
      ],
      [
        "Das, was den physi­schen Augen entgegentritt in der grünen Pflanzendecke der Erde, der eigentümlichen Konfiguration des Bodens und so weiter, das ist im Grunde genommen nur Maja oder äußerliche Illusion, das ist gleichsam eine Verdichtung dessen, was in der Äther-Aura wirkt.",
        "Allerdings ist nur dasjenige von dem Äußerlichen von dieser Äther-Aura abhängig, worauf die Äther-Aura, das heißt ein sich lebendig organisierendes Prin­zip Einfluß haben kann."
      ],
      [
        "Die Erzengel, die die geistigen Gesetze inne haben, können nicht in die physischen Gesetze eingreifen.",
        "Da hinein, wo also bloß die physischen Gesetze wirken und in Betracht kommen, wie bei den Gebirgsverhältnissen, der Wölbung des Bodens und so wei­ter, wo das, was die großen Änderungen des Volkes bedingt, abhängig ist von den physischen Verhältnissen, da hinein reicht der Einfluß der Erzengel nicht; so weit sind die Erzengel in ihrer Entwickelung noch nicht, daß sie in die physischen Verhältnisse eingreifen könnten."
      ],
      [
        "Weil sie das nicht können, weil sie da abhängig sind, deshalb müssen sie zu gewissen Zeiten über die Erde wandern, deshalb verkörpern sie sich in dem, was die Konfiguration des Bodens bedeutet, gleichsam als in dem physischen Leib, also in dem, was von den physischen Gesetzen be­herrscht ist.",
        "Da kann der Ätherleib des Volkes noch nicht hinein, da kann er sich noch nicht organisierend hinein erstrecken."
      ],
      [
        "Deshalb wird der Boden aufgesucht, wenn er sich als geeignet erweisen soll, und aus dieser Ehe zwischen dem Ätherleibe, der aber jetzt von geistig-seeli­schen Kräften durcharbeitet wird, und dem physischen Stück Erde entsteht dasjenige, was uns als der Zauberhauch im Äußern eines Volkstums"
      ],
      [
        "entgegentritt, das, was der Mensch, der nicht Hellseher ist, in einem Lande bloß fühlen kann, was der Mensch aber, der mit hellsehe­rischem Bewußtsein Land und Volk durchschaut, erschauen kann."
      ],
      [
        "Wie aber wirkt jetzt dasjenige herein, was sozusagen die Arbeit des Erzengels, des Volksgeistes in dem Ätherleib, der über den Boden sich erhebt, ist?",
        "Was ist die Arbeit des Erzengels, wie wirkt er herein in das Menschliche, das auf diesem Boden sich bewegt, das in dieser Wolke des Volksgeistes darinnen lebt?"
      ],
      [
        "Er wirkt so hinein, daß diese Kraft in drei Arten beim Menschen sich zum Ausdruck bringt.",
        "Die Äther-Aura des Volkes ist es, die in den Menschen hineinwirkt, den Menschen durch­setzt, durchwebt, und zwar wirkt diese Äther-Aura so in die mensch­liche Wesenheit hinein, daß ein Dreifaches in der menschlichen Wesen­heit davon ergriffen wird."
      ],
      [
        "Durch die Mischung dieses Dreifachen ent­steht dann der eigentümliche Charakter, den ein Mensch trägt, der in dieser Äther-Aura des Volkes darinnen lebt.",
        "Diese Äther-Aura, worauf wirkt sie beim Menschen?"
      ],
      [
        "Sie wirkt auf ein Dreifaches in den Tempe­ramenten.",
        "Sie wirkt auf die Temperamente, die selber in das Emotions­leben des Menschen versenkt sind, die im Ätherleibe des Menschen darinnen wirken, nur nicht auf das sogenannte melancholische Tempe­rament."
      ],
      [
        "Die Äther-Aura des Volkes wirkt auf das cholerische, phleg­matische und sanguinische Temperament.",
        "Im allgemeinen also fließt das, was die Kraft der Äther-Aura des Volkes ist, in diese drei Tempe­ramente hinein."
      ],
      [
        "Nun können diese drei Temperamente in der einzelnen menschlichen Individualität in der verschiedensten Weise gemischt sein und zusammenwirken.",
        "Unendliche Mannigfaltigkeit können Sie sich da denken, wenn die drei Kräfte zusammenwirken, wenn die eine die andere beeinflußt, besiegt und so weiter."
      ],
      [
        "Dadurch entsteht die mannig­faltigste Konfiguration, die uns zum Beispiel in Rußland, Norwegen, Deutschland verschiedenartig entgegentritt.",
        "Das macht den Volks­charakter des Menschen aus, was in die Temperamente hineinwirkt."
      ],
      [
        "Der Unterschied, der hier bei den einzelnen Individuen besteht, wird nur durch den Grad der Mischung bewirkt.",
        "Die Volkstemperamente sind also nach den Einwirkungen der Volksaura gemischt."
      ],
      [
        "So also haben wir über die Erde hin wirksam die Volksgeister.",
        "Die haben aber auch ihre eigenen Wege; denn das ist für ihre eigenen Angelegenheiten"
      ],
      [
        "nicht das Wesentliche, daß sie in die Temperamente hinein-wirken.",
        "Das tun sie nur deshalb, weil die Kräfte in der Welt in Wechsel­wirkung miteinander treten.",
        "Das tun sie zunächst als ihre gewollten Taten, als das, was ihre Mission ist."
      ],
      [
        "Daneben kommen aber auch die eigenen Angelegenheiten ihres Ichs in Betracht.",
        "Die bestehen darin, daß sie selber weiterkommen in ihrer Entwickelung, daß sie selber über die Erde schreiten und sich auf diesem oder jenem Gebiet der Erde verkör­pern."
      ],
      [
        "Das sind aber ihre eigenen Angelegenheiten.",
        "Das andere, was sie in den Temperamenten der Menschen tun, das ist etwas, was sie neben­bei arbeiten, was ihr Beruf ist.",
        "Natürlich kommt der Mensch auch wieder durch ihre Arbeit vorwärts, sie wirkt auf ihn zurück."
      ],
      [
        "Daher wirkt auch die menschliche Arbeit auf den Volksgeist zurück.",
        "Welche Bedeutung die einzelnen Menschen für den Volksgeist haben, das wer­den wir noch sehen.",
        "Das ist wichtig.",
        "Das Wesentliche ist aber, daß wir einen solchen Volksgeist verfolgen können, wie er sich in der Welt verkörpert, dann wieder eine Zeitlang in der geistigen Welt lebt und sich sodann wieder wo anders verkörpert und so weiter."
      ],
      [
        "Wenn wir diese Vorgänge betrachten, so haben wir immer nur Ich-Angelegenheiten dieser Wesen vor uns.",
        "Denken Sie sich also nun - damit Sie sich das recht konkret vorstellen - den menschlichen Ätherleib in den Volks­ätherleib eingebettet; denken Sie sich dann das Ineinanderwirken vom menschlichen Ätherleib und Volksätherleib, und denken Sie sich dar­auf, daß sich der Volksätherleib in den Volkstemperamenten spiegelt, spiegelt in der Mischung der Temperamente der einzelnen Menschen, dann haben Sie das Geheimnis, wie uns der Volksgeist in seiner Art innerhalb eines Volkes entgegentritt."
      ],
      [
        "Nun haben wir, nachdem wir dieses gesagt haben, im Grunde genom­men die wichtigste Arbeit der eigentlichen Erzengel oder Volksgeister erschöpft.",
        "Wir würden aber noch lange nicht die Eigentümlichkeiten eines Volkes erschöpft haben, wenn wir nur die Art des Charakters, wie ein Mensch ihn innerhalb dieses Volkes besitzt, in Betracht ziehen wollten.",
        "Aber die Erzengelwesenheiten, die die eigentlichen Geister der Volksstämme sind, die haben diese Aufgabe."
      ],
      [
        "Nun eignet aber einem Volke, wie Sie leicht ahnen können, noch manches andere.",
        "Woher kommt das?",
        "Wenn der Erzengel, der leitende"
      ],
      [
        "Volksgeist sich nicht mit anderen Wesenheiten auf demselben Grund und Boden begegnen und nicht mit ihnen zusammenarbeiten würde in diesem Ätherleib des Menschen, dann würde manches von den Eigen­schaften eines Volkes gar nicht entstehen können.",
        "Der Mensch ist ein Schauplatz für die Begegnung der Erzengel mit noch anderen Wesen­heiten, die mit den Erzengeln zusammenwirken und sozusagen mit ihnen zusammenarbeiten.",
        "Aus diesem Zusammenarbeiten entsteht aber noch etwas ganz anderes.",
        "Das hellseherische Bewußtsein findet, wenn es die Völker studiert, merkwürdigerweise geheimnisvolle Wesenheiten außer den bereits charakterisierten Erzengelwesen, die in gewisser Be­ziehung den Erzengeln verwandt, aber doch wieder in anderer Bezie­hung vollständig von ihnen verschieden sind, vor allen Dingen dadurch, daß sie viel größere Kräfte anzuwenden vermögen als die Volksgeister selber.",
        "Der Volksgeist wirkt in einer außerordentlich feinen und inti­men Weise auf die einzelne menschliche Seele in diesem Hineinweben in die Temperamente.",
        "Aber in einer viel stärkeren, kraftvolleren Weise wirken da noch andere Wesenheiten hinein.",
        "Diese anderen Wesenheiten müssen wir uns einmal aus unserer allgemeinen Kenntnis der Hierar­chien klar machen.",
        "Da werden wir sozusagen den Namen finden für diese anderen Wesenheiten, die das hellseherische Bewußtsein beob­achtet.",
        "Stellen Sie sich einmal vor die Hierarchien der Geister in fol­gender Weise:"
      ],
      [
        "Menschen,"
      ],
      [
        "Engel,"
      ],
      [
        "Erzengel,"
      ],
      [
        "Urbeginne oder Geister der Persönlichkeit,"
      ],
      [
        "Gewalten oder Geister der Form."
      ],
      [
        "Sodann würden wir weiter zu anderen kommen, die wir aber heute nicht weiter in Betracht ziehen wollen.",
        "Wenn Sie sich nun an dasjenige erinnern, wovon wir gestern gesprochen haben - und was Sie auch genau auseinandergesetzt finden in den Mitteilungen aus der «Akasha­Chronik» und in meiner Schrift «Die Geheimwissenschaft» -, so wer­den Sie sich sagen: Von diesen Wesenheiten sind es die Erzengel, welche während der alten Sonnenzeit ihre Menschheitsstufe durchgemacht haben.",
        "Da waren diejenigen Wesenheiten, die wir Geister der Form"
      ],
      [
        "oder Gewalten nennen, die jetzt zwei Stufen höher sind als die Erz­engel, auf der Erzengelstufe; sie waren Archangeloi, solche Wesenhei­ten, wie es die heute charakterisierten Volksgeister sind.",
        "Das war da­mals ihre normale Entwickelungsstufe."
      ],
      [
        "Nun gibt es aber ein eigentümliches Geheimnis in der Entwickelung, das ist das Gesetz von dem Zurückbleiben gewisser Wesenheiten, das Gesetz, welches bewirkt, daß auf jeder Stufe gewisse Wesenheiten zu­rückbleiben, die dann auf der folgenden Stufe nicht auf der normalen Höhe stehen, sondern eigentlich den Charakter haben, den sie auf den früheren Stufen haben sollten.",
        "Nun sind während unserer Menschheits­evolution immer Wesenheiten zurückgeblieben."
      ],
      [
        "Unter diesen Zurück­gebliebenen sind auch solche Geister der Form, solche Gewalten, und sie sind in einer ganz eigenartigen Weise zurückgeblieben, nämlich so, daß sie zwar in bezug auf gewisse Eigenschaften Geister der Form, Gewalten sind, daß sie durch gewisse Eigenschaften das können, was heute nur die Geister der Form können, die den Menschen auf der Erdenstufe das Ich verliehen haben, daß sie das aber nicht vollständig können, weil sie nicht alle dazu notwendigen Eigenschaften besitzen.",
        "Sie sind so stehen geblieben, daß sie nicht auf der Sonne, sondern jetzt während ihrer Erdenzeit ihre Erzengelstufe durchmachen, so daß sie Wesenheiten sind, die jetzt auf der Stufe der Volksgeister stehen, aber ganz andere Eigenschaften haben."
      ],
      [
        "Während die Volksgeister intim hineinwirken in das Menschenleben, weil sie zwei Stufen höher stehen als der Mensch, also mit den Menschen immer noch verwandt sind, sind diese Gewalten, diese Geister der Form vier Stufen über die Menschheitsstufe erhaben.",
        "Sie haben daher ungeheuer viele und große Kräfte, die nicht dazu taugen würden, so intim in die Menschen hinein­zuwirken."
      ],
      [
        "Sie würden robuster wirken, aber kein anderes Gebiet haben für ihre Wirksamkeit als dasjenige, auf dem die normalen Volksgeister, die Erzengel, stehen."
      ],
      [
        "Das ist das Schwierige, daß man erst unterscheiden lernen muß in der höheren Welt.",
        "Die, welche glauben, mit ein paar Begriffen in den höheren Welten auskommen zu können, irren sich sehr.",
        "Der Mensch, der mit oberflächlichen Begriffen in die höheren Welten hinaufsteigt, der findet da wohl die Erzengel.",
        "Aber man muß unterscheiden, ob es"
      ],
      [
        "Wesen sind, die jetzt normalerweise auf die Erzengelstufe gekommen sind oder solche, die während des Sonnenzustandes der Erde auf dieser Stufe hätten stehen sollen.",
        "So also wirken auf dem gleichen Gebiete mit den Geistern der Volksstämme oder Erzengeln zusammen andere We­senheiten, die sozusagen in der Rangordnung der Erzengel stehen, die aber mit ganz anderen, robusteren Eigenschaften begabt sind, mit sol­chen Eigenschaften, wie sie die sonstigen Geister der Form haben, und die dadurch tief eingreifen können in die menschliche Natur.",
        "Denn was haben diese Geister der Form während des Erdendaseins aus dem Men­schen gemacht?",
        "Denken Sie sich, daß die Menschen zu sich nicht Ich sagen könnten, wenn die Geister der Form nicht das Gehirn geformt hätten zu dem, was der Mensch heute als solches besitzt.",
        "Also bis in die physische Gestaltung hinein können solche Wesenheiten wirken, trotz­dem sie nur auf der Stufe der Erzengel stehen.",
        "Sie treten in eine Art von Wettkampf mit den Volksgeistern auf dem Terrain, wo die Volks-geister wirken."
      ],
      [
        "Das erste, was sie hauptsächlich bewirken, indem diese Geister von der einen Seite und die anderen von der anderen Seite zusammenstoßen, ist die Sprache, das, was nicht entstehen könnte ohne den ganzen Bau und die Form des menschlichen Leibes.",
        "In dem Bau des Menschen haben Sie die Wirksamkeit dieser anderen Volksgeister, die mit den Natur­gewalten und mit den Menschen verbunden werden.",
        "Also die Sprache dürfen wir nicht einfach denselben Wesenheiten zuschreiben, die in intimer Weise in das Volkstemperament hineinwirken und dem Volke als um zwei Stufen über dem Menschen stehende Wesen ihre Konfigu­ration aufprägen.",
        "Die Wesen, welche die Sprache geben, haben große Kraft, sie sind eigentlich Gewalten; sie wirken auf die Erde, weil sie auf der Erde geblieben sind, während ihre anderen Genossen im Ich wirken von der Sonne aus in den Weltenraum hinein.",
        "Von den Men­schen wurde vor dem Erscheinen des Christus Jesus das Jahve- oder Jehova-Wesen verehrt, und sie verehrten nachher als vom Weltenraum hereinwirkend das Christuswesen.",
        "In bezug auf die Sprachgeister müs­sen wir sagen, daß in der Sprache gerade das vom Menschen geliebt wird, was bei der Erde verblieben ist.",
        "Wir müssen uns ganz andere Anschauungen angewöhnen.",
        "Der Mensch ist gewohnt, seine eigenen"
      ],
      [
        "Begriffe auf das ganze Weltall anzuwenden.",
        "Er tut natürlich sehr Un­recht, wenn er die Tatsache, daß diese hohen Wesenheiten zurückblei­ben in der Entwickelung, ungefähr so betrachtet, wie wenn ein Schul­mädchen in einer Klasse sitzen bleibt.",
        "Sie bleiben nicht sitzen, weil sie nicht gelernt haben, sondern aus Gründen großer Weisheit, die in der Welt waltet.",
        "Würden nicht gewisse Wesenheiten auf ihre normale Weiterentwickelung verzichten und, statt mit der Sonne weiterzugehen, ihre Weiterentwickelung auf der Erde durchmachen, so würde das nicht auf der Erde haben entstehen können, was wir Sprache nennen.",
        "In gewisser Beziehung hat der Mensch seine Sprache innig zu lieben, und zwar aus dem Grunde, weil sozusagen aus Liebe bei ihm geblieben sind hohe Wesenheiten, die verzichtet haben auf gewisse Eigenschaften, damit der Mensch sich so entwickeln kann, wie das der Weisheit ent­spricht.",
        "Gerade so wie wir das Vorauseilen als eine Art von Opfer ansehen müssen, so müssen wir auch das Zurückbleiben in früheren Entwickelungsepochen als eine Art von Opfer ansehen, und wir müssen uns durchaus klar sein, daß die Menschen zu gewissen Eigenschaften gar nicht hätten kommen können, wenn nicht solche Opfer gebracht worden wären."
      ],
      [
        "So also sehen wir, wie in dem Ätherleibe des Menschen und in dem Ä therleibe des Volksgeistes, der in Betracht kommt, zweierlei Wesen­heiten ihre Arbeit austauschen: die normal entwickelten Erzengel und die auf der Erzengelstufe stehengebliebenen Geister der Form, die ver­zichtet haben auf ihre eigene Entwickelung, um den Menschen während ihres Erdendaseins die Volkssprache einzuverleiben.",
        "Sie mußten die Kraft haben, den Kehlkopf, die ganzen Sprachwerkzeuge so umzubil-den, daß das Ergebnis dieser Sprachwerkzeuge eine physische Manife­station, nämlich gerade die Sprache ist.",
        "Wir müssen also als Ergebnis dieses Zusammenwirkens gerade dasjenige ansehen, was als Volksge­müt, als Volkstemperament mit der Sprache im Bunde uns entgegen­tritt.",
        "Was der Mensch auszusprechen vermag, wodurch er sich als Angehöriger seines Volkes kundgibt, was er hinaustönen läßt in die Luft, das ist dasjenige, was die mit den Volksgeistern verbündeten Geister der Form nur deshalb bewirken können, weil sie mit ihren großen Kräften und Gewalten auf der Stufe der Volksgeister stehen"
      ],
      [
        "geblieben sind.",
        "So findet also ein solches Zusammenwirken statt inner­halb derjenigen Terrains, derjenigen Gebiete, wo die Volksgeister wir­ken.",
        "Ein ähnliches Zusammenwirken findet aber auch noch auf einem anderen Gebiete statt."
      ],
      [
        "Ich habe gestern angeführt, daß noch andere Kräfte, die Urbeginne oder die Geister der Persönlichkeit, die während des Erdendaseins das darstellen, was man Zeitgeist nennt, wirksam sind.",
        "Diese wirken so, daß sie von ihrem eigentlichen Ich aus, von ihrer seelischen Organisa­tion aus, in den physischen Leib hineinarbeiten, daß sie also die Kräfte des physischen Leibes in Bewegung bringen."
      ],
      [
        "Wir müssen also voraus­setzen, daß, wenn in einer bestimmten Zeit als Ergebnis der Wirkung des Zeitgeistes irgend etwas eintritt, irgend etwas sich innerhalb eines Zeitgeistes offenbart, wodurch die Menschheit einen Fortschritt macht, daß das einer Arbeit mit physischen Kräften innerhalb unseres Erden-daseins entspricht.",
        "Sie können das sehr leicht einsehen, Sie brauchen es sich nur zu überlegen, um zu begreifen, wie wirklich physische Voraus­setzungen notwendig sind, damit dieses oder jenes im Zeitgeiste entsteht."
      ],
      [
        "Oder können Sie sich vorstellen, daß unter anderen Voraussetzungen Kepler oder Kopernikus oder Perikles in einer anderen Zeit gelebt haben könnten?",
        "Die Persönlichkeiten wachsen aus ganz bestimmten Zeitverhältnissen heraus, aus denjenigen Verhältnissen, die in einem bestimmten Zeitpunkte durch die physische Arbeit von höheren Wesen­heiten konfiguriert und organisiert werden."
      ],
      [
        "Da sind es in der Tat die physischen Verhältnisse, freilich physische Verhältnisse, die wir uns nicht als materielle Klötze vorzustellen haben, sondern als gewisse Konfigurationen in der physischen Gemeinsamkeit unserer Erde.",
        "Manchmal tritt diese Konfiguration ganz gewaltig hervor; manchmal muß dabei, wenn der Zeitgeist in irgendeiner Weise seinen Einfluß übt, eine ganz bestimmte physische Konstellation zustande kommen."
      ],
      [
        "Den­ken Sie nur daran, daß, als man einmal erst ganz bestimmt geschliffene Gläser hatte, diese durch Kinderspiel in einer Glasschleiferwerkstätte so zusammengefügt wurden, daß man daran bemerken konnte die opti­sche Wirkung als Fernglas, so daß der Erfinder des Fernrohres nur die Beobachtung dieses Gesetzes des Fernrohres zu realisieren brauchte."
      ],
      [
        "Diese Sache ist ein historisches Faktum.",
        "Denken Sie sich aber, welche"
      ],
      [
        "physischen Vorgänge notwendig waren, damit das alles hat stattfinden können!",
        "Die Linsen mußten erst erfunden, geschliffen und in der ent­sprechenden Weise zusammengesetzt werden.",
        "Sie können da wohl das Wort «Zufall» gebrauchen, aber Sie können es nur anwenden, wenn Sie darauf verzichten, die Gesetzmäßigkeit auch in solchen Gescheh­nissen zu begreifen.",
        "Diese physischen Verhältnisse führen zusammen die Archai, die Urkräfte.",
        "Das Spiegelbild ihrer Arbeit ist das, was an einem Punkte der Erde zusammenführend wirkt, was sonst als Zeitgeist in mannigfaltiger Weise wirkt.",
        "Denken Sie sich, was in neuerer Zeit mit vielen physischen Dingen nicht geworden wäre, wenn diese Arbeit der Archai in Ihren physischen Leibern nicht stattgefunden hätte.",
        "So ist es in der Tat die Arbeit der Archai, welche in dieser Beziehung, in dieser Richtung wirkt."
      ],
      [
        "Wenn nun diese Archai in dieser Weise wirken und den Zeitgeist dirigieren, so können wir uns wieder fragen: Wie intuieren eigentlich diese Zeitgeister den Menschheitsfortschritt?",
        "Sie intuieren ihn dadurch, daß einen Menschen das, was im Physischen geschieht, wie zufällig an­regt.",
        "Es sind nicht bloß Legenden, wenn auch das manchmal zutrifft.",
        "Ich erinnere nur an die schwingende Kirchenlampe im Dome zu Pisa, wo Galilei das Pendelgesetz entdeckt hat an den regelmäßigen Schwin­gungen der Lampe im Dom, und wie dann Kepler und Newton zu ihren Entdeckungen angeregt wurden.",
        "Hunderte und Tausende von Fällen könnte man erzählen, wo physisches Geschehen zusammengeführt wird mit menschlichem Denken, woraus man ersehen könnte, wie da intuiert wird von den Archai oder Urkräften das, was als Ideen, als Zeitideen in die Welt hinausgeht, was die Menschen dann in ihrer Entwickelung beeinflußt, was ihren Fortschritt regelt und gesetzmäßig durchdringt.",
        "Aber auch auf diesem Gebiet wirken zusammen die Wesenheiten, die normalerweise während unseres Erdendaseins Geister der Persönlich­keit geworden sind, mit anderen, die dadurch, daß sie auf dem Mond zurückgeblieben sind, jetzt nicht Geister der Form oder Gewalten sind, wie sie auf der Erde sein sollten, sondern auch jetzt erst wirken als Gei­ster der Persönlichkeit."
      ],
      [
        "So sind diejenigen Wesenheiten, die nicht schon von der Sonnenstufe, sondern erst von der Mondenstufe aus verzichtet haben, jetzt Geister"
      ],
      [
        "der Persönlichkeit, aber nicht mit den Eigenschaften, die sie normaler­weise haben sollten, das heißt, sie intuieren nicht in der Weise wie die normalen Geister der Persönlichkeit, sondern als zurückgebliebene Gei­ster der Form.",
        "Sie regen nicht von außen an und überlassen es intim dem Menschen selber, das zu beobachten, was im Physischen bewirkt wird, sondern sie regen im Innern an, sie konfigurieren im Innern des Gehirns und geben dem Denken eine gewisse Richtung."
      ],
      [
        "Daher ist das Denken des Menschen in den verschiedenen Zeiträumen von innen angeregt, so daß jedes Zeitalter eine bestimmte Art des Denkens hat.",
        "Das hängt mit den feinen Konfigurationen des Denkens zusammen, mit inneren Konstellationen."
      ],
      [
        "Da arbeiten die zurückgebliebenen Geister der Form, die den Charakter der Geister der Persönlichkeit haben, im Innern der Menschen und bringen eine gewisse Denkart, eine ganz bestimmte Form der Begriffe hervor.",
        "Das macht es, daß die Menschen von Epoche zu Epoche nicht nur geführt werden im Sinne der intuie­renden Geister der Persönlichkeit, wo sie sich selber anregen lassen, das oder jenes zu tun, sondern daß sie fortgetrieben werden wie durch innere Kräfte, so daß das Denken von innen heraus sich physisch kund-gibt, wie sich in der Sprache kundgibt das, was auf der anderen Seite als Geister der Form zurückgeblieben ist."
      ],
      [
        "So drückt die Denkart sich aus als eine Manifestation der Geister der Form, die in unserer Zeit als Geister der Persönlichkeit auftreten.",
        "Es sind also nicht so intim wir­kende Geister der Persönlichkeit, die es dem Menschen überlassen, zu machen, was er will, sondern ihn ergreifen und mit vorwärtsstürmender Gewalt drängen."
      ],
      [
        "Daher können Sie immer diese zwei Typen in denjeni­gen Menschen sehen, welche von dem Zeitgeist angeregt sind.",
        "In den­jenigen, welche von den wahren Zeitgeistern, von den auf normaler Stufe stehenden, angeregt sind, können Sie sozusagen sehen die wahren Vertreter ihrer Zeit."
      ],
      [
        "Wir können sie betrachten als Menschen, die kom­men mußten, und ihre Tätigkeit als etwas, was nicht anders hat gesche­hen können.",
        "Es kommen aber auch andere Menschen, in denen wirken diejenigen Geister der Persönlichkeit, die eigentlich Geister der Form sind."
      ],
      [
        "Das sind die anderen Geister, die wir bezeichnet haben als die Denkgeister, die während des Mondenzyklus auf ihren jetzigen Stand­punkt vorrückten.",
        "Der Mensch ist nun der Schauplatz, auf dem alles"
      ],
      [
        "dies zusammenwirkt.",
        "Dieses Zusammenwirken macht sich dadurch geltend, daß Sprache und Denken in ein Wechselverhältnis treten, da­durch, daß nicht bloß die Geister, die auf der gleichen Stufe stehen, in ein Wechselverhältnis kommen, sondern daß auch die normalen Erz­engel, die Volksgemüt und Volkstemperament regeln, in Wechselver­hältnisse treten mit dem, was eben charakterisiert worden ist, also nicht nur mit den auf der Erzengelstufe stehenden Geistern der Form, son­dern auch mit denjenigen Geistern der Persönlichkeit, die eigentlich zurückgebliebene Geister der Form sind."
      ],
      [
        "Diese zwei Arten treten in der menschlichen Natur und menschlichen Wesenheit auf.",
        "Dieses Verhältnis ist im höchsten Grade interessant zu studieren, wenn man mit okkulten Kenntnissen, mit okkultem Sehver­mögen von Volk zu Volk geht."
      ],
      [
        "Da kann man sehen, wie die normalen Volksgeister wirken, und wie dann diese normalen Volksgeister ihre Befehle von den Zeitgeistern bekommen; wie aber diese Volksgeister zusammenwirken im Innern des Menschen mit den Sprachgeistern und auch mit den Denkgeistern, die in die Gedanken der Menschen hinein-wirken.",
        "Da finden sich im Innern des Menschen nicht nur normale Erzengel und abnorme Erzengel, sondern auch die Erzengel im Gegen­satz mit den abnormen Geistern der Persönlichkeit, die von innen heraus die Gedankenarbeit einer bestimmten Zeit regeln."
      ],
      [
        "Da ist es nun im höchsten Grade interessant - ich habe gesagt, es werden Zustände angedeutet werden, denen Sie entgegenkommen müssen mit Ihrem spirituellen Verständnis, die eingekleidet werden müssen in gewöhn­liche Worte, weil im Leben noch keine Sprache geschaffen ist, die alles das glaubhaft und verständlich machen würde; man muß alles aus­drücken in Worten, die den Tatbestand etwas bildhaft geben, was aber einer bedeutungsvollen Tatsache der Menschheitsentwickelung ent­spricht -, da ist es nun im höchsten Grade interessant und wichtig, der Menschheitsentwickelung in neuerer Zeit zu folgen, wichtig zu wissen, daß einmal geradezu ein gegenseitiger Vertrag geschlossen worden ist von einem der leitenden Geister der Völker, der ein normaler Erzengel ist, mit einem solchen Geist, der als Geist der Denkkräfte im Innern wirkt, also mit einem abnormen Geist der Persönlichkeit, und es zeigt sich in einer gewissen geschichtlichen Epoche das ernste, bedeutsame"
      ],
      [
        "Ergebnis dieses Vertrages.",
        "Um diesen Vertrag noch besonders voll zu machen, wurde ein harmonisches Verhältnis hergestellt mit dem ent­sprechenden abnormen Erzengel, der der leitende Geist der Sprache in jener Zeit war, so daß es einen Punkt in der Menschheitsentwickelung gibt, wo sozusagen zusammenwirkt normales und abnormes Erzengel­tum, und wo außerdem noch als Einschlag hineinwirkt die Denkungs­art, die von innen heraus durch einen abnormen Geist der Persönlich­keit bewirkt wird."
      ],
      [
        "Dieser Vertrag zwischen diesen drei Parteien spiegelt sich in einem bestimmten Volke wider.",
        "Das ist das indische Volk, das Volk, das in der ersten nachatlantischen Zeit die nachatlantische Kultur einleitete."
      ],
      [
        "Während dieser indischen Kultur trat jene Konstellation ein, wo jene drei Wesenheiten am harmonischsten zusammenwirkten.",
        "Die Folge davon ist alles dasjenige, was wir als die historische Rolle dieses indischen Volkes bezeichnen können."
      ],
      [
        "Auch in den Zeiten, von denen es schon geschichtliche Überlieferungen gibt, wirkt das nach, was da­mals in dem Vertrag abgeschlossen wurde.",
        "Dies war der Grund, warum mit einer solchen Gewalt die alte heilige Sprache der Inder wirkte und jene gewaltigen historischen Kulturwirkungen hatte, warum sie noch so gewaltig in der Folgezeit wirken konnte."
      ],
      [
        "Diese Kraft brachten die abnormen Erzengel, die in der Sprache wirkten.",
        "Diese Gewalt der Sans­kritsprache beruht gerade auf dem Vertrage, von dem ich eben gespro­chen habe.",
        "Und wiederum beruht darauf die eigenartige indische Phi­losophie, die als Philosophie, als vom Innern des Menschen heraus schaffendes Denken noch nicht erreicht ist von irgendeinem andern Volke der Welt; darauf beruht die innere Geschlossenheit des Denkens der indischen Kultur."
      ],
      [
        "Bei allen andern Gebieten haben wir andere Ver­hältnisse zu beobachten.",
        "In ihr allein trat dazumal das zutage, was jetzt charakterisiert worden ist.",
        "Daher ist es so unendlich reizvoll, diesen Gedankengängen zu folgen, die dadurch eine besondere Konfi­guration haben, weil sie hervorgegangen sind nicht aus dem Überge­wichte des normalen Erzengels über den abnormen, sondern als etwas, was in Harmonie mit jener Geschlossenheit steht, weil tatsächlich jeder Gedanke vom Volkstemperament absorbiert und mit Liebe ins einzelne hinein fortgesponnen worden ist - damals, als das indische Volk als erste Kulturblüte der nachatlantischen Zeit vorhanden war."
      ],
      [
        "Sprache wirkte so fort aus dem Grunde, weil da nicht ein Kampf ent­standen war, der sonst überall entstanden wäre, sondern weil ein Zu­sammenwirken zwischen dem Erzengel der normalen Entwickelung und dem Erzengel der abnormen Entwickelung stattfand, so daß man sagen kann, daß die Sprache, ausgegossen von dem reinsten Tempera­ment, selber ein Produkt des Temperamentes ist.",
        "Das ist das Geheimnis dieses ersten Kulturvolkes der nachatlantischen Zeit."
      ],
      [
        "Das aber ist es, was betrachtet werden muß bei allen andern Völkern, daß nämlich bei ihnen eine eigenartige Zusammenwirkung entsteht zwischen diesen drei Kräften, zwischen dem normalen Volksgeist oder Erzengel, dem abnormen Erzengel und zwischen dem, was innerlich wirkt in dem abnormen Geist der Zeit, der nicht als Zeitgeist, sondern von innen heraus wirkt, und endlich dem, was der wahre Zeitgeist dem Volke innerlich übertragen hat.",
        "Darauf beruht die wahre Erkenntnis eines Volkes, daß man diese Kräfte im Innern belauscht, daß man den Anteil prüft, den ein jeder Faktor an der Konstitution des Volkes hat."
      ],
      [
        "Daher ist es schwierig geworden für die Menschen, welche nicht die okkulten Kräfte der Menschheitsentwickelung in Frage ziehen, eigent­lich das Wort «Volk» zu definieren.",
        "Versuchen Sie einmal die einzelnen Bücher herzunehmen, worin der Begriff des Volkes irgendwo in der Welt definiert worden ist, und Sie werden sehen, was da alles als Defi­nition des Begriffes Volk existiert und wie sehr sie voneinander abwei­chen."
      ],
      [
        "Sie müssen ja voneinander abweichen, weil der eine mehr fühlt, was von der einen Seite, von den normalen Erzengeln herkommt, der andere mehr fühlt, was von dem abnormen Erzengel herrührt und der Dritte wieder das, was von den einzelnen Persönlichkeiten des Volkes kommt.",
        "Ein jeder fühlt etwas anderes und verwertet es in seiner Defini­tion."
      ],
      [
        "Das ist es gerade, was uns klar geworden ist durch die Geisteswis­senschaft, daß diese Definitionen nicht immer falsch zu sein brauchen; sie sind nur immer in Maja, in Illusion getaucht.",
        "An dem, was einer sagt, kann man sehen, ob er nur die Maja betrachtet, und ob er die verschiedenen wirkenden Kräfte unberücksichtigt läßt."
      ],
      [
        "Daher wird man selbstverständlich immer einen ganz anderen Begriff bekommen, wenn vom geisteswissenschaftlichen Standpunkte aus ein Volk wie das schweizerische, das auf demselben Grund und Boden lebt und drei"
      ],
      [
        "Sprachen spricht, und dagegen Völker mit einheitlicher Sprache be­trachtet werden."
      ],
      [
        "Warum Völker mehr aus dem Geiste der Persönlichkeit heraus wir­ken, also durch das Zusammenwirken der einzelnen Persönlichkeiten namentlich ihr Dasein haben, darüber werden wir noch zu sprechen haben.",
        "Solche Völker, die mehr ihr Dasein haben durch den abnormen Geist der Persönlichkeit, werden wir auch auf der Erde finden.",
        "Diese Geister der Persönlichkeit wirken nicht auf Weiterentwickelung hin.",
        "Sie brauchen sich nur den Charakter des nordamerikanischen Volkes klar zu legen, so haben Sie ein Volk, das vorderhand auf diesem Prinzip beruht.",
        "So werden Sie sehen, daß wir die Weltgeschichte, insofern sie Völkergeschichte ist, erst verstehen werden, wenn wir normale und ab­norme Erzengel, normale und abnorme Geister der Persönlichkeit in ihrem gegenseitigen Rang und ihrem Zusammenwirken und gleichzeitig in der Aufeinanderfolge der Völker im Verlaufe der Weltgeschichte verfolgen werden."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "DRITTER VORTRAG Kristiania, 9. Juni 1910",
    "paragraphs": [
      "Wir werden innerhalb des Zyklus dieser Vorträge Betrachtungen an­stellen, welche sozusagen jedem leicht in die Seele gehen werden, weil er sich in intensivster Weise unmittelbar für sie wird interessieren kön­nen. Aber, weil sonst das Ganze nicht verständlich werden würde, müssen wir auch solche Betrachtungen anstellen, welche um der Voll­ständigkeit und des Verständnisses willen notwendig sind, und die etwas schwieriger sein werden als dasjenige, was sozusagen der Haupt­stock unserer Vorträge ist. Wir werden zum Beispiel heute in die Not­wendigkeit versetzt sein, einen Blick in das Innere jener Wesenheiten zu tun, von denen wir in den beiden vorhergehenden Betrachtungen gesprochen haben, in das Innere der normalen Volksgeister.",
      "Wir haben bereits gesagt, was zu ihrer äußeren Charakteristik not­wendig war, daß sie Wesenheiten sind, die zwei Stufen höher stehen als der Mensch, Wesenheiten, welche an der Umgestaltung ihres Ätherleibes arbeiten, also eben jetzt daran sind, ihre Ätherleiber umzuarbeiten in dasjenige, was man Lebensgeist oder Buddhi nennt. Der Mensch ist in diese Arbeit eingesponnen. Insofern, als die Entwickelung dieser Wesenheiten so fortschreitet, daß der Mensch in diese Entwickelung hineingesponnen ist, äußert sich die Spiegelung dieses Volksgeistes in der menschlichen Individualität selber als der Volkscharakter des ein­zelnen menschlichen Individuums.",
      "Nun werden wir etwas hineinzusehen haben in das Innere einer solchen Volksseele. Wenn wir in das heutige Innere des Menschen hineinleuchten wollen, haben wir dazu nötig, uns dieses Innere dreigliedrig vorzustellen, es uns so vorzustellen, daß wir es uns teilen in:",
      "die Empfindungsseele, gleichsam das unterste Glied der menschlichen inneren Wesenheit,",
      "die Verstandes- oder Gemütsseele, das mittlere Glied, und",
      "die Bewußtseinsseele, das höchste Glied des menschlichen Innern, wo eigentlich erst so recht das menschliche Ich zum Bewußtsein gebracht wird.",
      "In der Bewußtseinsseele ist eigentlich so recht erst das vorhanden, was man das menschliche Selbstbewußtsein nennt. Trotzdem ist das Ich des Menschen in allen drei Teilen seines inneren Lebens - sowohl in der Empfindungsseele als auch in der Verstandes- oder Gemütsseele und in der Bewußtseinsseele - tätig.",
      "In der Empfindungsseele ist dieses Ich so tätig, daß der Mensch dieses sein Ich kaum erst ahnt. Er ist insofern in der Empfindungsseele allen Trieben und Leidenschaften hingegeben. Das Ich brütet dumpf in dem, was wir Empfindungsseele nennen. Das Ich arbeitet sich dann erst heraus, kommt erst zum Vorschein in der Verstandes- oder Gemütsseele und wird ganz klar erst in der Bewußtseinsseele. Wenn wir diese drei Glieder des menschlichen Innern abgesondert für sich untersuchen wol­len, so müssen wir sie als drei Modifikationen, als drei Teile innerhalb des Astralleibes ansehen. Allerdings gilt ja das, daß diese drei Modifi­kationen, diese drei Glieder des Astralleibes, vorbereitend umarbeiten den Astralleib selber, den Ätherleib und den physischen Leib. Aber diese Umarbeitungen sind doch nicht dasjenige, was uns als das eigent­liche menschliche Innere, als das Seelische entgegentritt. Das Seelische, das Innere des Menschen, sind drei Modifikationen des astralischen Leibes. Die drei Modifikationen müssen sich gewisser Werkzeuge bedie­nen, und diese prägen sich so aus, daß im Astralleibe die Empfindungsseele eine Art von Werkzeug hat, im Ätherleibe die Verstandes- oder Gemütsseele, und im physischen Leibe die Bewußtseinsseele. So also können wir das menschliche Innere von dem, was menschliche Hüllennatur ist, unterscheiden. Es ist also des Menschen innere Natur aus drei Modifikationen des astralischen Leibes bestehend.",
      "So wie beim Menschen das Innere, das, worin das Ich arbeitet und sich ausprägt, sich in diesen drei Modifikationen des Astralleibes dar­stellt, so stellt bei denjenigen geistigen Wesenheiten, die wir als Volksgeister bezeichnen, das eigentliche Innere oder das, was wir mit dem menschlichen Inneren vergleichen können, dar drei Glieder, drei Modi­fikationen im Ätherleibe. So wie wir beim Menschen unterscheiden Empfindungsseele, Verstandesseele, Bewußtseinsseele, so müssen wir bei den Erzengelwesenheiten, den normalen Volksgeistern, drei Modi­fikationen im Ätherleibe unterscheiden. Aber weil diese drei Modifikationen",
      "nicht im Astralleibe sind, sondern im Ätherleibe, deshalb sind sie ganz, ganz anders, wesentlich anders, als die drei Modifikationen im Seelenleben des Menschen. Daher müssen Sie sich auch die Bewußt­seinsform, das ganze Seelenleben dieser Volksgeister anders vorstellen als das Seelenleben des Menschen. Wir dringen also gleichsam von einer äußeren Charakteristik jetzt in das Innere der Seele dieser Volksgeister ein. Das wird nicht ganz leicht sein, aber wir müssen schon versuchen, diesen Rubikon zu überschreiten. Da wird es sich nun darum handeln, daß wir von irgendeinem Begriffe ausgehen, der Ihnen geläufig sein kann, einem Begriffe, der sozusagen etwas Ähnliches bietet wie das innere Leben der Volksgeister. Solche Dinge hat der Mensch nicht viele in seinem normalen Leben, er hat im Gegenteil außerordentlich wenig von dem in seinem eigenen Bewußtsein, was in dem Bewußtsein der Volksgeister lebt. Aber Sie können sich doch eine Vorstellung davon machen, wenn Sie geduldig einmal die folgende Betrachtung mit mir anstellen.",
      "Sie haben alle in der Schule gelernt, daß die drei Winkel des Dreiecks 1800 sind, und Sie wissen, daß Sie das niemals durch irgend eine äußere Erfahrung lernen könnten. Denken Sie sich meinetwegen eiserne, höl­zerne Dreiecke. Wenn Sie nun mit einem Winkelmaße messen, wie viel die drei Winkel ausmachen, dann wird Sie diese äußere Erfahrung nie­mals belehren können, daß diese drei Winkel 1800 sind. Aber Sie werden sofort belehrt sein - gleichgültig ob Sie diese drei Winkel auf­zeichnen oder sie sich nur vorstellen -, wenn Sie von innen heraus erfahren, daß die drei Winkel 180 sind. Sie müssen das durch die Kraft Ihrer eigenen Seele von innen heraus erfahren. Sie brauchen dazu nur das Folgende in Gedanken auszuführen. Das, was ich jetzt aufzeichne, zeichnet man nur zur Versinnbildlichung des Gedankens.",
      "In dieser Figur haben Sie den strikten Beweis, daß die drei Winkel zusammen 1800 sind. Wenn Sie sich diese Figur einmal so recht vor die Seele treten lassen, so wird sie Ihnen für alle Fälle diese Gewißheit bringen. Diese Figur können Sie in Gedanken ausführen, ohne daß Sie sie äußerlich aufzeichnen. Sie vollziehen dann eine reine Gedankenope­ration durch die Kraft Ihres eigenen Inneren, Sie brauchen gar nicht aus sich herauszutreten. Sie können sich einen Augenblick vorstellen, daß es das, was man Empfindungswelt nennt, und das, was durch die äußeren Sinne in den Menschen hineingeht, gar nicht gibt. Denken Sie sich also die äußere Welt vollständig weg, den Raum in Gedanken konstruiert, dann würden in diesem Raume alle Dreiecke in ihrer Win­kelsumme 1800 zeigen. Um zu einer geometrisch-mathematischen Er­kenntnis zu kommen, braucht nicht ein äußerer Gegenstand an Ihre Sinne heranzutreten, es bedarf nur dessen, was inneres Erlebnis ist, was im Bewußtsein selber verläuft.",
      "Ich mußte dieses Beispiel gebrauchen, denn es ist das einfachste und praktischste, weil die Menschen das schon wissen, da sie es in der Schule gelernt haben. Ich könnte Ihnen auch das Beispiel der Hegelschen Logik geben, dann würden Sie auch eine Summe von innerlichen Begriffen ha­ben, aber da würden wir viel Unbekanntes darin finden, da die Hegel­sche Logik in den weitesten Kreisen unbekannt ist. Daraus können Sie also ersehen, wie der Mensch bloß von innen heraus zu Erkenntnissen kommen kann, ohne daß er durch etwas Äußerliches dazu angeregt wird.",
      "Wenn Sie sich das vorstellen, was äußerlich nur erreichbar ist in der Welt in mathematisch konstruktiver Weise, dann haben Sie einen Teil begriffen von dem, wie das Bewußtsein der Erzengel wirkt. Sie nehmen nämlich eine solche Welt, wie sie an den äußeren Menschen herantritt, eine Welt von äußeren Farben und Tönen, gar nicht wahr. Diese Empfindungen hat niemals ein solches Wesen; es hat niemals die Mög­lichkeit, daß es mit seinem Tastsinn an irgend etwas herantritt und dadurch Wahrnehmungen empfängt. Diese Erlebnisse hat ein solches Wesen niemals. Aber das Erlebnis hat es, das man mit den Worten aus­drücken kann: Jetzt kommt mir aus einer Welt, die mich inspiriert, etwas zu; diese Welt ist durch mein Bewußtsein hindurchgegangen, füllt mein Bewußtsein aus.",
      "Nun sind die Erzengel nicht etwa Wesen, die bloß mathematisch vorstellen, vielmehr ist der Mensch so unvollkommen, daß er nur in solchen Abstraktionen, wie die mathematischen Wahrheiten sind, sich die Tätigkeit der Erzengel vorzustellen vermag. Sie sind das, was für den Menschen sowohl als für die Volksgeister als normal erscheint.",
      "Daraus können Sie aber entnehmen, daß die äußere physische Welt, die für die Menschen durch die Sinne da ist, die Erzengel gar nichts angeht. In der Gestalt also, wie die physische Welt für den Menschen da ist, wie der Mensch durch seine Sinne die Kundgebungen der physischen Welt erhält, in dieser Weise ist die Welt für die Erzengel nicht vorhanden.",
      "Schalten Sie also das, was nur als physische Empfindung da ist, aus Ihrem Weltbilde aus, denken Sie alles weg, was Sie durch äußere Wahr­nehmungen in sich aufgenommen haben, dann schalten Sie aus Ihrem Weltbilde eben das aus, was die Erzengel nichts angeht. Also werden wir uns sagen: Ja, was ist denn von dem, was auch menschliches Bewußtsein werden kann, noch für die Erzengel da?",
      "Was ist von dem­selben für die Volksgeister vorhanden? Alles, was Sie in der Empfin­dungsseele erleben, was Sie als gewöhnliche, durch die Außenwelt bewirkte Lust, als gewöhnliches, durch die Außenwelt bewirktes Leid erleben, alles, was Farben, Töne, überhaupt sinnliche Wahrnehmungen der Außenwelt sind, das geht diese Wesenheiten nichts an.",
      "Schalten Sie also den ganzen Inhalt der menschlichen Empfindungsseele aus, und sagen Sie sich, was im Weltbilde vorhanden ist dadurch, daß für den Menschen die Empfindungsseele da ist, das ist für die Erzengel nicht von Bedeutung, da wirken sie nicht hinein. Sogar ein Teil der Verstandesseele ist noch kein Element, das für die Erzengel von Bedeu­tung ist, insoweit dieselbe angeregt wird durch die äußeren Empfin­dungen.",
      "Was äußerlich angeregt wurde, was der Mensch mit dem Ver­stande verarbeitet und dem Gemüte durchlebt, auch das geht die Erz­engel nichts an. Aber in die Verstandesseele des Menschen spielen doch schon gewisse Dinge hinein, welche der Mensch sozusagen auf dem­selben Terrain mit den Erzengeln erlebt.",
      "Wir können ganz genau wahr­nehmen, daß solche Dinge in die menschliche Verstandes- oder Gemütsseele hineinspielen, wenn wir sehen, wie zum Beispiel in unserem Leben dasjenige, was wir unsere moralischen Ideale nennen, an uns herantritt.",
      "Es gäbe keine moralischen Ideale, wenn wir angewiesen wären, uns nur über dasjenige Empfindungen zu machen, über das Lust und Leid zu empfinden und uns darüber Gedanken zu machen, was uns von der Außenwelt als die Sinneswahrnehmung entgegentritt. Da würden wir uns zwar über die Blumen des Feldes, auch über eine schöne Land­schaftskonfiguration freuen können, aber wir würden niemals in unse­rem Gemüte für ein Ideal entbrennen können, das uns nicht aus der Außenwelt entgegenleuchten kann, das wir uns in die Seele einschreiben können, und wofür wir dann erglühen. Aber wir müssen nicht nur erglühen und in der Empfindungsseele fühlen, sondern wir müssen auch darüber denken. Der Mensch, der nur empfindet, der nicht denkt, der kann zwar ein Schwärmer, aber niemals ein praktischer Mensch sein. Wir müssen die Ideale nicht von außen in die Empfindungsseele auf­nehmen, sondern sie einströmen lassen aus der geistigen Welt und sie in der Verstandes- oder Gemütsseele verarbeiten. Die künstlerischen, die architektonischen Ideale und so weiter sind in der Verstandes- oder Gemütsseele und in der Bewußtseinsseele anwesend. Sie hängen zusam­men mit dem, was der Mensch von außen nicht wahrnehmen kann, was aber doch innerlich sein Wesen durchglüht und durchsetzt, so daß es einen Teil seines Lebens ausmacht.",
      "Schauen Sie sich das Leben der Völker von Epoche zu Epoche an, wie es verlaufen ist, wie immer neue Vorstellungen und Weltgeheimnisse darin aufgekommen sind. Wo hätten die Griechen ihre Vorstellungen über Zeus und Athene hernehmen können, wenn sie sich nur auf die äußere Wahrnehmung verlassen hätten! Das lebte sich von innen hinein, was in den Weistümern, in den Mythologien, Religionen und in den Wissenschaften der Völker enthalten ist. So also müssen wir sehen, daß die Hälfte unseres inneren Wesens, die Hälfte unserer Verstandes- oder Gemütsseele und unserer Bewußtseinsseele von innen heraus angefüllt sind, und zwar gerade so weit, als der Mensch sich mit dem, was eben charakterisiert worden ist, innerlich durchdringt, so weit können die Erzengel in das menschliche Innere vordringen, und so weit geht auch das eigentliche Leben der Erzengel. Das müssen Sie also vom inneren Leben ausschalten, was von außen durch die Empfindungsseele aufge­nommen und durch die Verstandes- oder Gemütsseele verarbeitet wird.",
      "Dann haben Sie aber auch noch das, was wir unser Ich nennen. Für uns ist das Ich das höchste Glied unserer Wesenheit. Was wir da hineintragen in das moralische Bewußtsein, das sind Ideale, moralische, ästhetische, ideelle Gedanken. So wie der Ausblick dem Menschen gleichsam nach innen verschlossen ist, sich aber nach außen durch seine Sinne der Außenwelt öffnen kann, so kann er sagen: Ich nehme Farben, Töne, Kälte und Wärme wahr. Aber er hat auch das Bewußtsein, daß hinter diesen Wahrnehmungen von Farben, Tönen, Wärme und Kälte noch etwas Wesenhaftes ist. Das sind die Wesen des tierischen, pflanzlichen und mineralischen Reiches. Das ist dahinter; so daß der Mensch sich in der angedeuteten Weise die Welt darüber hinaus fortgesetzt denken kann. Darüber hinaus ist aber die Aussicht für den gewöhnlichen Men­schen verschlossen. Wäre das nicht der Fall, so könnte es gar keinen Materialismus geben. Würde der Mensch die Aussicht frei haben auf das Gebiet, das sich von der Verstandesseele und der Bewußtseinsseele nach oben hin erstreckt, dann wäre es ebenso töricht, die geistige Welt zu bezweifeln, wie es heute töricht wäre, die Existenz der Tier-, Pflan­zen- und Mineralwelt in Zweifel zu ziehen.",
      "Denken Sie nun, wie das Ich beim Menschen, das höchste Glied des­selben, in sich einschließt die Empfindungs-, Verstandes- und Bewußt­seinsseele. Beim Erzengel ist es nun so, daß sein Seelenleben anfängt bei seinem Erleben in der Verstandes- oder Gemütsseele, dann hinaufgeht in das Ich, das sich aber ausbreitet in eine Welt höherer Reiche, in ein Reich geistiger Tatsachen, in dem es lebt, wie der Mensch im Reiche der Tiere, Pflanzen und Mineralien lebt. So daß wir sagen können: Wir müssen zwar einsehen, daß dieses Erzengelwesen in seinem Seelenleben dasjenige, was wir menschliches Ich nennen, haben kann, jedoch kön­nen wir nicht sagen, daß das Ich des Erzengels mit diesem Ich gleicher Art ist. Mit dem Ich des Menschen ist also das Erzengel-Ich nicht einer­lei. Das Erzengel-Ich liegt eben um zwei Stufen höher, so daß der Erz­engel mit seinem Ich in einer höheren Welt wurzelt. So wie nun der Mensch durch seine Sinnesempfindung auf Farben schaut, Töne hört, so schaut der Erzengel herunter auf die Welt, die das Ich als objektive Wahrheit umschließt, nur daß sich um dieses Ich noch etwas herumgruppiert von jenem Teile des Astralischen, das wir Menschen in uns",
      "als Verstandes- oder Gemütsseele kennen. Denken Sie sich diese Wesen­heiten in eine Welt schauend, die nicht das Mineralische, Pflanzliche und Tierische erreicht. Denken Sie, daß dafür der Blick, der ein geisti­ger ist, auf ihr Weltbild hingerichtet ist und daß sie da Mittelpunkte wahrnehmen. Diese Mittelpunkte sind die menschlichen Iche, um die sich wieder etwas gruppiert, das wie eine Art Aura aussieht. Da haben Sie das Bild, wie das Erzengelwesen auf die Völkerpersönlichkeiten, die zu dem Erzengel gehören, die das Volk ausmachen, heruntersieht. Seine Welt besteht aus einem astralischen Wahrnehmungsfelde, in dem ge­wisse Zentren darin sind. Diese Zentren, diese Mittelpunkte sind die einzelnen menschlichen Persönlichkeiten, sind die einzelnen mensch­lichen Iche. Also gerade so, wie für uns Farben und Töne, Wärme und Kälte im Wahrnehmungsfelde liegen und für uns die bedeutsame Welt sind, so sind für die Erzengelwesen, für die Volksgeister wir selbst mit einem Teil unseres Innenlebens das Wahrnehmungsfeld, und wie wir in die Außenwelt hineingehen und diese bearbeiten und umgestalten zu Instrumenten, so sind wir diejenigen Objekte - insofern wir zu diesem oder jenem Volksgeist gehören -, welche zu dem Arbeitsfelde der Erz­engel oder Volksgeister gehören.",
      "Da sehen wir hinein, so sonderbar das auch klingen mag, in eine höhere Erkenntnistheorie der Erzengel. Die ist nämlich eine ganz an­dere als die Erkenntnistheorie der Menschen, denn es ist schon dasjenige, was für die Erzengel das Gegebene ist, ganz anders. Für den Menschen ist das Gegebene das im Raume Ausgebreitete, das uns durch die Sinne als Farbe, Ton, Wärme, Kälte, Härte und Weichheit entgegentritt. Für die Erzengel ist das Gegebene, was innen im menschlichen Bewußtseinsfelde auftritt. Das ist für sie eine Summe von Zentren, von Mittelpunk­ten, um welche die inneren Erlebnisse der Menschen gesponnen sind, insofern als sich diese Erlebnisse in der Verstandes- oder Gemütsseele abspielen; ihre Tätigkeit ist in dem entsprechenden Falle aber eine höhere.",
      "Wie spezialisiert sich nun das Weltbild der Erzengel oder Volksgei­ster? Für den Menschen spezialisiert sich das Weltbild dadurch, daß, wenn er irgendeinen Gegenstand mit der Hand ergreift, er ihn warm oder kalt empfindet. Der Erzengel erlebt etwas Ähnliches, indem er die",
      "menschlichen Individualitäten trifft. Da trifft er Menschen, welche mehr von der inneren Aktivität beseelt sind, reicheren Seeleninhalt haben, die machen auf ihn einen intensiveren Eindruck. Andere findet er lässig, lethargisch, mit armem Seeleninhalt, das sind die Wesen, die für ihn so dastehen, wie Wärme und Kälte für das Weltbild der mensch­lichen Seele. So spezialisiert sich das Weltbild des Erzengels, und je nachdem kann er die einzelnen Menschen gebrauchen, für sie arbeiten, indem er dasjenige webt, was aus seiner Wesenheit heraus das gesamte Volk zu leiten hat.",
      "Aber auch sonst steht mit dem Leben dieses Erzengels das Leben des betreffenden Volkes, dem er vorsteht, in gewissem Zusammenhang. Gerade so, wie der Mensch aufsteigende und absteigende Perioden im Leben hat, eine aufsteigende Jugendzeit und die absteigende Zeit des Alters, so erlebt der Erzengel in der aufsteigenden und absteigenden Kultur eines Volkes seine Jugend und sein Alter.",
      "Nun müssen wir wieder in das innere Leben eines solchen Erzengels hineinsehen. Sie haben aus dem, was ich erzählt habe, wohl schon gemerkt, daß dasjenige, was der Mensch von außen bekommt, der Erz­engel von innen erhält; dafür bekommt der Erzengel die Empfindung, wenn die Volksindividualitäten als Zentren in ihm auftreten, daß das, was da an ihn herantritt, zwar von innen in seinem Bewußtsein auftritt, aber ihm doch sozusagen etwas Fremdes ist. Es ist etwas, was bei ihm so auftritt, wie die Einfälle in unserm Bewußtsein. In umgekehrter Weise tritt das auch an ihn heran, wie beim Menschen Jugend und Alter herantritt. Beim Menschen wird die Jugend so erlebt, daß er sich in seinen Gliedern frisch fühlt, daß sie im Aufstreben begriffen sind, sich entwickeln. Im Alter werden diese Glieder sozusagen schlaff und ver­sagen ihren Dienst. Das ist etwas, was der Mensch aus seinem Inneren herauskommen fühlt. Der Erzengel fühlt nun zwar alles als aus seinem Inneren herauskommend, aber es erscheint ihm das Auf- und Absteigen des Volkes doch als etwas Fremdes, als etwas, wovon er das Gefühl hat, daß es von ihm unabhängig ist, womit er also nicht direkt etwas zu tun hat, was ihm aber Veranlassung gibt, sich in irgendeinem Volke zu bestimmter Zeit zu verkörpern. Wenn die Möglichkeit da ist, sich zu verkörpern, wenn ein in der aufstrebenden Periode seines Lebens, in der",
      "aufstrebenden Vollkraft lebendes Volk vorhanden ist, dann geht der Erzengel hinunter, ebenso wie der Mensch hinuntersteigt, wenn er das Leben durchlebt hat zwischen dem Tod und einer neuen Geburt. So also geht der Erzengel ebenso hinunter in ein Volk und verkörpert sich darin. Ebenso fühlt der Erzengel seinen Tod, die Notwendigkeit, sich von dem betreffenden Volke zurückzuziehen, wenn die einzelnen Wahrnehmungen, die Zentren, die er wahrnimmt, anfangen weniger produktiv, weniger aktiv zu sein, wenn sie anfangen, weniger Inhalt zu haben. Dann kommt die Zeit, wo er eine solche Volksgemeinschaft ver­läßt; er kommt dann in sein Devachan, in sein Leben zwischen Tod und neuer Geburt, um bei späterer Gelegenheit in anderer Weise eine Volks­gemeinschaft aufzusuchen. So bedeutet das jugendlich aufsteigende Leben eines Volkes die Jugend des Volksgeistes, und er nimmt sie wahr als ein frisches strömendes Element, in dem er lebt. Die absteigende Periode des Volkslebens nimmt er wahr als ein Dürrwerden der Zen­tren, die in seinem Wahrnehmungsgebiete sind. - Das sollte also eine Art Einblick in das Innere einer solchen Volksseele sein.",
      "Wenn wir uns das vor Augen führen, was eben gesagt worden ist, dann dürfen wir sagen: In gewisser Beziehung steht doch eine solche Volksseele dem einzelnen Menschenleben ziemlich fern, denn in dem einzelnen Menschen ist dasjenige, was er in seiner Empfindungsseele und in dem niederen Teil seiner Verstandesseele hat, ein Gebiet, in welches der Volksgeist, der Erzengel nicht hineinreicht. Für den Men­schen ist es aber etwas sehr Reales. Da fühlt der Mensch recht sehr, daß das mit dem Innersten, dem Intimsten seines eigenen Lebens zusammen­hängt. Es ist in gewisser Beziehung die Erzengel-Natur, die führende Volksnatur, etwas, was über dem einzelnen Menschen schwebt. Den persönlichen Dingen, die der Mensch dadurch erlebt, daß er Wahrneh­mungen durch seine Sinne hat, steht der Erzengel, der das Volk leitet, fremd gegenüber. - Aber da gibt es Vermittler, und es ist wichtig, daß wir verstehen, daß es solche Vermittler gibt. Das sind die Wesen, die wir Engel nennen, und die zwischen Erzengel und Mensch stehen. Fassen Sie es im strengsten Sinne des Wortes auf: Volksgeister sind Erzengel, sind solche Geister, welche mit der Umgestaltung ihres astra­lischen Leibes zu Geistselbst oder Manas fertig sind, und jetzt umgestalten",
      "ihren Lebensleib zu Buddhi. Zwischen diesen Wesen und den Menschen stehen mitten drinnen die Engelwesen. Das sind solche We­sen, die mit der Umarbeitung ihres Astralleibes in Manas oder Geistselbst beschäftigt, aber noch nicht mit dieser Arbeit zu Ende gekommen sind. Der Mensch steht am Anfange dieser Arbeit im gegenwärtigen Zeitalter, die Engel stehen dem Ende derselben nahe, sind aber keines­wegs fertig damit. Daher berühren sich die Terrains dieser Wesenheiten viel intimer mit denen, in welchen der Mensch steht und lebt. Wir können sagen, daß die Engelwesen mit ihrer ganzen Seelenhaftigkeit dem zugeneigt sind, was wir astralischen Leib nennen. Deshalb haben sie volles Verständnis für alles das, was die menschliche Persönlichkeit durch Leid und Freude erleben kann. Aber weil sie auf der andern Seite viel höher über das menschliche Ich hinaufragen, weil sie ein höheres Ich haben, weil sie einen Teil der höheren Welt aufnehmen können, deshalb ragt ihre Bewußtseinswelt in diejenigen Terrains hinein, auf denen sich die Bewußtseinswelt der Erzengel befindet. Sie sind also so recht die Vermittler zwischen Erzengel und einzelner Menschen-Indi­vidualität. Sie empfangen ihrerseits die Befehle der Volksgeister und tragen sie in die einzelnen Seelen hinein, und durch diese Vermittelung ergibt sich dann dasjenige, was der einzelne wirken kann, nicht bloß für seinen eigenen Fortschritt, seine eigene Entwickelung, sondern für sein ganzes Volk.",
      "Der Mensch hat diese zwei Strömungen in seinem Erleben nebenein­ander. Die eine Strömung ist die, die ihn von Inkarnation zu Inkarnation vorwärts bringt, die seine eigenen Angelegenheiten angeht, welche er vor allen Dingen zu besorgen hat, um diejenige Pflicht zu erfüllen, die doch im Grunde genommen die allerstrengste ist, denn es ist seine eigenste Pflicht. Er darf nicht stehen bleiben, weil er sonst die Keime, die in ihm veranlagt sind, brach liegen lassen würde, wenn er sich um sie nicht kümmerte. Das ist aber seine eigenste Angelegenheit, durch die er vorwärts schreitet von Verkörperung zu Verkörperung. Was er aber zu seiner Volksgemeinschaft beiträgt, was zu den Angelegenheiten sei­ner unmittelbaren Volksgemeinschaft gehört, das bildet die Inspiration des Engels, der die Befehle des Erzengels zu den einzelnen Menschen heranträgt. Wir können uns also ganz gut vorstellen, daß wir auf einem",
      "Gebiete der Erde ein Volk haben, und über dieses Volk ist ausgebreitet die Volks-Aura, die Äther-Aura, und da spielen wieder die Kräfte des Volksgeistes hinein und modifizieren nach den drei Arten von Kräften den Ätherleib des Menschen. Das, was in diese Volks-Aura hineinspielt, das ist der Erzengel. Ihn denken wir uns als ein höheres Wesen, als ein Wesen, das in der Entwickelung zwei Stufen höher steht als der Mensch, das über dem ganzen Volke schwebt und die Anordnungen gibt in bezug auf das, was dieses Volk im großen zu erfüllen hat. Der Erzengel weiß, was getan werden muß während des Aufstrebens, während der Jugendfrische des Volkes; er weiß, zu welchen Verrichtungen des Vol­kes der Übergang von der Jugend zum Alter benutzt werden muß, damit seine Impulse richtig wirken können.",
      "Diese großen Züge bildet der Erzengel. Hier auf diesem physischen Plan aber muß der einzelne Mensch arbeiten, hier muß der Mensch dafür sorgen, daß diese großen Ziele verwirklicht werden. Da stehen dann zwischen dem einzelnen Menschen und dem Erzengel die Engel als Mittelwesen, die den Menschen dann hindrängen zu dem Platze, an den er hingedrängt werden muß, damit im Volksgefühle dasjenige geschieht, was den großen Anordnungen des Erzengels entspricht. Wir stellen uns ein richtiges Bild der Sache vor, wenn wir uns das, was ich beschrieben habe, keineswegs bloß als Allegorie, sondern möglichst als Wirklichkeit vorstellen.",
      "Nun wirkt hinein in das ganze Gewebe, das der Erzengel spinnt, dasjenige, was wir die abnormen Erzengel genannt haben, die Geister der Sprache, in dem Sinne genommen, wie ich es gestern charakterisiert habe. Wir haben aber auch charakterisiert, wie die abnormen Geister der Persönlichkeit, die Archai, hereinwirken. Da können wir nun hinblicken auf das Feld, wo der Erzengel seine Befehle erteilt, wo er die Missionen ausgibt, die von den Engeln weiter in die einzelnen Menschen hineingetragen werden. Aber der Erzengel kann auch in das Feld der abnormen Geister der Persönlichkeit hineinwirken, und es können in dem gegenseitigen Zusammenwirken des Erzengels mit den abnormen Geistern der Persönlichkeit - weil sie ganz andere Ziele verfolgen als die Erzengel - in gewisser Beziehung die Maßnahmen des Erzengels durchkreuzt werden. Wenn das geschieht, wenn diese abnormen Geister",
      "der Persönlichkeit die Maßnahmen des Erzengels durchkreuzen, dann können wir die Wahrnehmung machen, daß sich innerhalb eines Volkes selber Gruppen bilden mit speziellen Aufgaben. Dadurch, daß sich innerhalb eines Volkes solche Gruppen mit speziellen Aufgaben bilden, wird das Wirken der Geister der Persönlichkeit äußerlich sichtbar. Das kann durch viele Jahrhunderte hindurch dauern. Sie haben zum Bei­spiel gerade in dem Gebiete, in dem wir insbesondere jetzt geisteswis­senschaftlich zu wirken haben, in Deutschland, durch Jahrhunderte hindurch dieses Spiel des Erzengels der Deutschen im Zusammenwirken mit den manchmal widerstrebenden einzelnen Geistern der Persönlich­keit gesehen. In der Zersplitterung der gemeinsamen deutschen Nation in die kleineren Volkspartien haben Sie ein Zusammenspiel der abnor­men Geister der Persönlichkeit mit dem Erzengel.",
      "Solche Völker haben etwas wenig Zentralisiertes, sie sehen mehr auf die Ausbildung der Individualitäten. Das hat in gewisser Beziehung sein Gutes, weil dadurch eine große Mannigfaltigkeit, viele Nuancen des Volkstums zum Ausdruck kommen können.",
      "Aber Sie können auch den anderen Fall ins Auge fassen, daß nicht der abnorme Geist der Persönlichkeit, sondern der normale Geist der Persönlichkeit, der im Zeitgeist sich äußert, für irgend einen Zeitpunkt sozusagen wichtiger wird, als er es sonst im gewöhnlichen Verlaufe ist.",
      "Wenn wir also auf ein Volk blicken, so blicken wir, als auf seine erste Macht, auf den Erzengel hin. Da wirkt dann der Zeitgeist hinein, gibt seine Befehle an den Erzengel, und dieser gibt seine Befehle weiter an die Engel, und diese vermitteln sie dem einzelnen Menschen. Weil man nun gewöhnlich nur das sieht, was einem am nächsten steht, so sieht man bei diesem zusammengesetzten Wirken als das Wichtigste das Wirken der Erzengel. Es kann aber auch eintreten, daß der Zeitgeist schwerwiegendere, gewichtigere Befehle ausgeben muß, daß er sozu­sagen genötigt ist, dem Erzengel etwas wegzunehmen, weil er einen Teil des Volkes herausgliedern muß, damit das, was Aufgabe der Zeit, Mis­sion des Zeitgeistes ist, erfüllt werden kann. In einem solchen Falle splittern sich dann Volksgemeinschaften von anderen ab. Da gewinnt der Zeitgeist sichtbarlich die Oberhand über das Wirken des Erzengels. Ein solcher Fall trat ein, als das holländische Volk von der Grundlage,",
      "die es mit dem deutschen Volke gemeinsam hatte, absplitterte. Holland und Deutschland hatten ursprünglich einen gemeinsamen Erzengel, und die Absplitterung geschah dadurch, daß der Zeitgeist in einem bestimmten Augenblicke einen Teil heraussonderte und diesem Teil dann dasjenige übertrug, was die wichtigen Angelegenheiten des mo­dernen Zeitgeistes geworden sind. Alles, was Sie in der holländischen Geschichte lesen können - Geschichte ist zwar nur ein äußerer Aus­druck, eine Maja für dasjenige, was innerer Vorgang ist -, ist nur eine Widerspiegelung dieses inneren Vorgangs. So sehen wir in diesem Fall äußerlich sich vollziehen die Absplitterung des holländischen Volkes von dem gemeinsamen deutschen Volkstum. Der innere Kern ist aber der, daß der Zeitgeist ein Werkzeug brauchte, um dasjenige auszufüh­ren, was die überseeische Mission des Zeitgeistes war. Die ganze Mission des holländischen Volkes ist eine Mission des Zeitgeistes gewesen. Und zu dem Zwecke wurde es abgespalten, um dem Zeitgeiste zu ermögli­chen, in einer bestimmten Zeit etwas Wichtiges mit diesem Teile auszu­führen. Das, was die Historiker beschreiben, ist nur äußere Maja, was die wahren Tatsachen mehr verhüllt als enthüllt.",
      "Noch anderswo kann Ihnen entgegentreten das, was sich in dieser Beziehung in auffälliger Weise zugetragen hat, nämlich daß sich ein Teil eines Volkes von dem gemeinsamen Volke abspalten mußte. Das ist bei dem portugiesischen Volke der Fall. Sie werden vergeblich an­dere Gründe dafür in diesem Falle suchen und finden, als daß es sich hier lediglich um einen Sieg des Zeitgeistes über den Erzengel handelt. Wenn Sie die einzelnen Ereignisse durchgehen, werden Sie finden, daß hier die Gelegenheit benutzt wurde, ein besonderes Volkstum zu bil­den - viele Gelegenheiten waren nicht da. Das spanische Volk bildete mit dem portugiesischen ein Muttervolk. Die äußeren Gründe sind vielleicht die, daß die Flüsse nur bis zur portugiesischen Grenze gut befahrbar sind. Andere äußere Gründe gibt es nicht. Dagegen gibt es den inneren Grund, daß die Aufgaben erfüllt werden mußten, die gerade die Aufgaben der Portugiesen waren und die andere waren, als die Aufgaben des gemeinsamen spanischen Volkes. Da sehen wir die Zeitgeister eine Zeitlang eine intensivere Tätigkeit entwickeln, als sie sonst ausführen. Wir sehen die bisherige Harmonie durch eine andere",
      "ersetzt. Wir sehen den Zeitgeist, statt daß er seine Befehle an den Erz­engel erteilt, direkt in die Geschichte des Volkes eingreifen und sehen, wie die anderen Geister diese Gelegenheit benutzen, um sich zu ver­körpern. Wenn ein solches Volkstum abgespalten wird, dann versieht der Zeitgeist eine Zeitlang in dem ersten Enthusiasmus, der die einzel­nen Menschen durchdrungen hat, so sehr die Funktionen des Erzengels, daß die Abspaltung kaum als etwas anderes vorhanden ist denn als ein Hasten und Drängen innerhalb dieses Volkes. Man sieht die Hast und das Drängen, die Regsamkeit, die aus der Mission des Zeitgeistes kommt. Dann aber stellt sich die Möglichkeit ein, daß ein normaler und ein abnormer Erzengel sich in dem abgespaltenen Volksteil verkörpert. So sehen wir das Heranwachsen des holländischen und des portugiesi­schen Volkes, die sodann ihre eigenen normalen und eigenen abnormen Erzengel bekommen. In dem, was sich darin verkörpert, in der Ver­schiedenheit des Temperamentes des Volkes, das in den einzelnen Per­sönlichkeiten zum Ausdrucke kommt, sehen wir das Hineinspielen desjenigen, was wir als diese geistigen Wesenheiten genannt haben. In ganz merkwürdiger Art sehen wir das Hineinspielen dieser geistigen Wesenheiten, und wir erkennen dann, daß die sich äußerlich abspie­lende Geschichte nur ein Ergebnis des Wirkens derselben ist.",
      "Nach und nach gewinnt der Satz, daß die Außenwelt Maja oder Illusion ist, immer konkretere Bedeutung. Das, was in der äußerlichen Geschichte geschieht, ist nur der äußere Abglanz der geistigen, der übersinnlichen Wesenheiten, gerade so wie der äußere Mensch nur der äußere Abglanz des inneren Menschen ist. Deshalb mußte ich sagen, und das muß immer wieder betont werden: Der Satz «Die Welt ist Maja» ist von allergrößter Wichtigkeit. Es genügt aber nicht, daß man ihn abstrakt betont, man muß vielmehr in der Lage sein, ihn in den Einzelheiten durchzuführen.",
      "Nun haben wir aber gesehen, daß auch andere Geister und Hierar­chien in dem, was wir die Welt nennen, tätig sind. Wir haben von den normalen und abnormen Erzengeln gesprochen. Die abnormen Erz­engel haben sich uns nun entpuppt als eigentliche Geister der Form oder Gewalten, die nur auf einen gewissen Teil der Eigenschaften ihrer Ent­wickelung verzichtet haben. Wir können dann fragen: Wie ist es aber",
      "mit den normalen Geistern der Form? Die normalen Geister der Form erblicken wir um vier Grade höher stehend als den Menschen. - Wir werden in unserer nächsten Betrachtung noch einiges über diese nor­malen Geister der Form zu sprechen haben. - Das sind also Wesenheiten, welche vier Grade höher sind als der Mensch. Dasjenige aber, was wir gestern als Hierarchien angeführt haben, erschöpft sich nicht mit dem, was wir nach oben abschließend als Geister der Form genannt haben. Höher als diese stehen die Geister der Bewegung, die Dynameis, die Mächte; noch höher die Wesenheiten, die wir Kyriotetes, Herrschaf­ten oder Geister der Weisheit nennen. Sie finden diese verschiedenen geistigen Wesenheiten sowohl in meiner «Geheimwissenschaft» als auch in meiner Schrift über die «Akasha-Chronik» aufgeführt.",
      "Nun werden Sie begreifen können, daß das Gesetz des Verzichtens, des Zurückbleibens auch für die höheren Geister gilt, daß also auch die Geister der Bewegung mit gewissen Eigenschaften zurückbleiben kön­nen - Geister der Bewegung, die fünf Stufen höher sind als der Mensch -, daß gewisse Geister der Bewegung heute in der Menschheits­entwickelung enthalten sind so, als ob sie erst Geister der Form, Gewal­ten wären. Das sind in bezug auf gewisse Eigenschaften eigentlich Geister der Bewegung und in bezug auf andere Eigenschaften, hinsicht­lich welcher sie verzichtet haben, Geister der Form. So daß wir haben normale Geister der Form, die vier Stufen höher stehen als der Mensch, und andere Geister, die auf demselben Terrain, wo die Geister der Form sind, wirken, die aber eigentlich Geister der Bewegung sind. Das ist also ein Gebiet, auf dem - so wie wir ein Gebiet gefunden haben, auf dem normale und abnorme Erzengel zusammenwirken - die normalen und abnormen Geister der Form, die zurückgebliebenen Geister der Bewegung, zusammenwirken. Durch dieses Zusammenwirken geschieht aber etwas, was die Menschen sehr wohl angeht; dadurch geschieht die Ausgestaltung dessen, was wir die menschlichen Rassen nennen, die wir unterscheiden müssen von den Völkern.",
      "Wir bekommen keinen verwirrenden Begriff, wenn wir die Sache so betrachten, sondern einen flüssigen Begriff; wir dürfen das nicht alles zusammenwerfen. Ein Volk ist keine Rasse. Der Volksbegriff hat nichts zu tun mit dem Rassenbegriff. Es kann sich eine Rasse in die",
      "verschiedensten Völker spalten. Rassen sind andere Gemeinschaften als Volksgemeinschaften. Wir sprechen gewiß mit Recht von einem deutschen, einem holländischen, einem norwegischen Volke; wir spre­chen aber von einer germanischen Rasse. Was wirkt da nun in dem Rassenbegriff? Da wirken zusammen diejenigen Wesenheiten, die wir als die normalen Geister der Form oder Gewalten bezeichnen, und die Wesenheiten, die wir als die abnormen Geister der Form, die eigentlich Geister der Bewegung sind mit Missionen der Geister der Form, kennen gelernt haben. Deshalb sind die Menschen in Rassen gespalten. Das, was die Menschen über das ganze Erdenrund hin gleich macht, was jeden Menschen, gleichgültig welcher Rasse er angehört, zum Menschen, zum Angehörigen des ganzen Menschentums macht, das bewirken die normalen Geister der Form. Dasjenige aber, was über die ganze Erde dahinspielt, was das gesamte Menschentum in Rassen gliedert, das bewirken die abnormen Geister der Form, die verzichtet haben zugun­sten der Tatsache, daß nicht eine einzige Menschheit auf der Erde erscheint, sondern eine Mannigfaltigkeit von Menschen.",
      "Da gewinnen wir sozusagen den Untergrund, den Boden für das, woraus sich erst die einzelnen Völkerindividualitäten erheben. Wir gewinnen dadurch die Umschau über den ganzen Erdenplaneten, finden den Erdenplaneten dazu bestimmt, eine Menschheit zu tragen durch die normalen Geister der Form, finden, daß sich die zurückgebliebenen Geister der Bewegung in dieses Terrain der Geister der Form hineinbegeben und als abnorme Geister der Form das Menschentum auf dem ganzen Erdenrund in die einzelnen Rassen gliedern. Wenn wir hineinblicken in das, was diese Geister eigentlich wollen, wenn wir uns ver­tiefen in die Ziele und Aufgaben dieser normalen und abnormen Geister der Form, dann werden wir verstehen, was sie mit den Menschenrassen wollen, wie durch dieselben eine Grundlage geschaffen wird für das, was sich aus ihnen heraushebt. Wenn wir dann noch ein Volk selbst betrachten, dann werden wir das Volk begriffen und verstanden haben."
    ],
    "sentences": [
      [
        "Wir werden innerhalb des Zyklus dieser Vorträge Betrachtungen an­stellen, welche sozusagen jedem leicht in die Seele gehen werden, weil er sich in intensivster Weise unmittelbar für sie wird interessieren kön­nen.",
        "Aber, weil sonst das Ganze nicht verständlich werden würde, müssen wir auch solche Betrachtungen anstellen, welche um der Voll­ständigkeit und des Verständnisses willen notwendig sind, und die etwas schwieriger sein werden als dasjenige, was sozusagen der Haupt­stock unserer Vorträge ist.",
        "Wir werden zum Beispiel heute in die Not­wendigkeit versetzt sein, einen Blick in das Innere jener Wesenheiten zu tun, von denen wir in den beiden vorhergehenden Betrachtungen gesprochen haben, in das Innere der normalen Volksgeister."
      ],
      [
        "Wir haben bereits gesagt, was zu ihrer äußeren Charakteristik not­wendig war, daß sie Wesenheiten sind, die zwei Stufen höher stehen als der Mensch, Wesenheiten, welche an der Umgestaltung ihres Ätherleibes arbeiten, also eben jetzt daran sind, ihre Ätherleiber umzuarbeiten in dasjenige, was man Lebensgeist oder Buddhi nennt.",
        "Der Mensch ist in diese Arbeit eingesponnen.",
        "Insofern, als die Entwickelung dieser Wesenheiten so fortschreitet, daß der Mensch in diese Entwickelung hineingesponnen ist, äußert sich die Spiegelung dieses Volksgeistes in der menschlichen Individualität selber als der Volkscharakter des ein­zelnen menschlichen Individuums."
      ],
      [
        "Nun werden wir etwas hineinzusehen haben in das Innere einer solchen Volksseele.",
        "Wenn wir in das heutige Innere des Menschen hineinleuchten wollen, haben wir dazu nötig, uns dieses Innere dreigliedrig vorzustellen, es uns so vorzustellen, daß wir es uns teilen in:"
      ],
      [
        "die Empfindungsseele, gleichsam das unterste Glied der menschlichen inneren Wesenheit,"
      ],
      [
        "die Verstandes- oder Gemütsseele, das mittlere Glied, und"
      ],
      [
        "die Bewußtseinsseele, das höchste Glied des menschlichen Innern, wo eigentlich erst so recht das menschliche Ich zum Bewußtsein gebracht wird."
      ],
      [
        "In der Bewußtseinsseele ist eigentlich so recht erst das vorhanden, was man das menschliche Selbstbewußtsein nennt.",
        "Trotzdem ist das Ich des Menschen in allen drei Teilen seines inneren Lebens - sowohl in der Empfindungsseele als auch in der Verstandes- oder Gemütsseele und in der Bewußtseinsseele - tätig."
      ],
      [
        "In der Empfindungsseele ist dieses Ich so tätig, daß der Mensch dieses sein Ich kaum erst ahnt.",
        "Er ist insofern in der Empfindungsseele allen Trieben und Leidenschaften hingegeben.",
        "Das Ich brütet dumpf in dem, was wir Empfindungsseele nennen.",
        "Das Ich arbeitet sich dann erst heraus, kommt erst zum Vorschein in der Verstandes- oder Gemütsseele und wird ganz klar erst in der Bewußtseinsseele.",
        "Wenn wir diese drei Glieder des menschlichen Innern abgesondert für sich untersuchen wol­len, so müssen wir sie als drei Modifikationen, als drei Teile innerhalb des Astralleibes ansehen.",
        "Allerdings gilt ja das, daß diese drei Modifi­kationen, diese drei Glieder des Astralleibes, vorbereitend umarbeiten den Astralleib selber, den Ätherleib und den physischen Leib.",
        "Aber diese Umarbeitungen sind doch nicht dasjenige, was uns als das eigent­liche menschliche Innere, als das Seelische entgegentritt.",
        "Das Seelische, das Innere des Menschen, sind drei Modifikationen des astralischen Leibes.",
        "Die drei Modifikationen müssen sich gewisser Werkzeuge bedie­nen, und diese prägen sich so aus, daß im Astralleibe die Empfindungsseele eine Art von Werkzeug hat, im Ätherleibe die Verstandes- oder Gemütsseele, und im physischen Leibe die Bewußtseinsseele.",
        "So also können wir das menschliche Innere von dem, was menschliche Hüllennatur ist, unterscheiden.",
        "Es ist also des Menschen innere Natur aus drei Modifikationen des astralischen Leibes bestehend."
      ],
      [
        "So wie beim Menschen das Innere, das, worin das Ich arbeitet und sich ausprägt, sich in diesen drei Modifikationen des Astralleibes dar­stellt, so stellt bei denjenigen geistigen Wesenheiten, die wir als Volksgeister bezeichnen, das eigentliche Innere oder das, was wir mit dem menschlichen Inneren vergleichen können, dar drei Glieder, drei Modi­fikationen im Ätherleibe.",
        "So wie wir beim Menschen unterscheiden Empfindungsseele, Verstandesseele, Bewußtseinsseele, so müssen wir bei den Erzengelwesenheiten, den normalen Volksgeistern, drei Modi­fikationen im Ätherleibe unterscheiden.",
        "Aber weil diese drei Modifikationen"
      ],
      [
        "nicht im Astralleibe sind, sondern im Ätherleibe, deshalb sind sie ganz, ganz anders, wesentlich anders, als die drei Modifikationen im Seelenleben des Menschen.",
        "Daher müssen Sie sich auch die Bewußt­seinsform, das ganze Seelenleben dieser Volksgeister anders vorstellen als das Seelenleben des Menschen.",
        "Wir dringen also gleichsam von einer äußeren Charakteristik jetzt in das Innere der Seele dieser Volksgeister ein.",
        "Das wird nicht ganz leicht sein, aber wir müssen schon versuchen, diesen Rubikon zu überschreiten.",
        "Da wird es sich nun darum handeln, daß wir von irgendeinem Begriffe ausgehen, der Ihnen geläufig sein kann, einem Begriffe, der sozusagen etwas Ähnliches bietet wie das innere Leben der Volksgeister.",
        "Solche Dinge hat der Mensch nicht viele in seinem normalen Leben, er hat im Gegenteil außerordentlich wenig von dem in seinem eigenen Bewußtsein, was in dem Bewußtsein der Volksgeister lebt.",
        "Aber Sie können sich doch eine Vorstellung davon machen, wenn Sie geduldig einmal die folgende Betrachtung mit mir anstellen."
      ],
      [
        "Sie haben alle in der Schule gelernt, daß die drei Winkel des Dreiecks 1800 sind, und Sie wissen, daß Sie das niemals durch irgend eine äußere Erfahrung lernen könnten.",
        "Denken Sie sich meinetwegen eiserne, höl­zerne Dreiecke.",
        "Wenn Sie nun mit einem Winkelmaße messen, wie viel die drei Winkel ausmachen, dann wird Sie diese äußere Erfahrung nie­mals belehren können, daß diese drei Winkel 1800 sind.",
        "Aber Sie werden sofort belehrt sein - gleichgültig ob Sie diese drei Winkel auf­zeichnen oder sie sich nur vorstellen -, wenn Sie von innen heraus erfahren, daß die drei Winkel 180 sind.",
        "Sie müssen das durch die Kraft Ihrer eigenen Seele von innen heraus erfahren.",
        "Sie brauchen dazu nur das Folgende in Gedanken auszuführen.",
        "Das, was ich jetzt aufzeichne, zeichnet man nur zur Versinnbildlichung des Gedankens."
      ],
      [
        "In dieser Figur haben Sie den strikten Beweis, daß die drei Winkel zusammen 1800 sind.",
        "Wenn Sie sich diese Figur einmal so recht vor die Seele treten lassen, so wird sie Ihnen für alle Fälle diese Gewißheit bringen.",
        "Diese Figur können Sie in Gedanken ausführen, ohne daß Sie sie äußerlich aufzeichnen.",
        "Sie vollziehen dann eine reine Gedankenope­ration durch die Kraft Ihres eigenen Inneren, Sie brauchen gar nicht aus sich herauszutreten.",
        "Sie können sich einen Augenblick vorstellen, daß es das, was man Empfindungswelt nennt, und das, was durch die äußeren Sinne in den Menschen hineingeht, gar nicht gibt.",
        "Denken Sie sich also die äußere Welt vollständig weg, den Raum in Gedanken konstruiert, dann würden in diesem Raume alle Dreiecke in ihrer Win­kelsumme 1800 zeigen.",
        "Um zu einer geometrisch-mathematischen Er­kenntnis zu kommen, braucht nicht ein äußerer Gegenstand an Ihre Sinne heranzutreten, es bedarf nur dessen, was inneres Erlebnis ist, was im Bewußtsein selber verläuft."
      ],
      [
        "Ich mußte dieses Beispiel gebrauchen, denn es ist das einfachste und praktischste, weil die Menschen das schon wissen, da sie es in der Schule gelernt haben.",
        "Ich könnte Ihnen auch das Beispiel der Hegelschen Logik geben, dann würden Sie auch eine Summe von innerlichen Begriffen ha­ben, aber da würden wir viel Unbekanntes darin finden, da die Hegel­sche Logik in den weitesten Kreisen unbekannt ist.",
        "Daraus können Sie also ersehen, wie der Mensch bloß von innen heraus zu Erkenntnissen kommen kann, ohne daß er durch etwas Äußerliches dazu angeregt wird."
      ],
      [
        "Wenn Sie sich das vorstellen, was äußerlich nur erreichbar ist in der Welt in mathematisch konstruktiver Weise, dann haben Sie einen Teil begriffen von dem, wie das Bewußtsein der Erzengel wirkt.",
        "Sie nehmen nämlich eine solche Welt, wie sie an den äußeren Menschen herantritt, eine Welt von äußeren Farben und Tönen, gar nicht wahr.",
        "Diese Empfindungen hat niemals ein solches Wesen; es hat niemals die Mög­lichkeit, daß es mit seinem Tastsinn an irgend etwas herantritt und dadurch Wahrnehmungen empfängt.",
        "Diese Erlebnisse hat ein solches Wesen niemals.",
        "Aber das Erlebnis hat es, das man mit den Worten aus­drücken kann: Jetzt kommt mir aus einer Welt, die mich inspiriert, etwas zu; diese Welt ist durch mein Bewußtsein hindurchgegangen, füllt mein Bewußtsein aus."
      ],
      [
        "Nun sind die Erzengel nicht etwa Wesen, die bloß mathematisch vorstellen, vielmehr ist der Mensch so unvollkommen, daß er nur in solchen Abstraktionen, wie die mathematischen Wahrheiten sind, sich die Tätigkeit der Erzengel vorzustellen vermag.",
        "Sie sind das, was für den Menschen sowohl als für die Volksgeister als normal erscheint."
      ],
      [
        "Daraus können Sie aber entnehmen, daß die äußere physische Welt, die für die Menschen durch die Sinne da ist, die Erzengel gar nichts angeht.",
        "In der Gestalt also, wie die physische Welt für den Menschen da ist, wie der Mensch durch seine Sinne die Kundgebungen der physischen Welt erhält, in dieser Weise ist die Welt für die Erzengel nicht vorhanden."
      ],
      [
        "Schalten Sie also das, was nur als physische Empfindung da ist, aus Ihrem Weltbilde aus, denken Sie alles weg, was Sie durch äußere Wahr­nehmungen in sich aufgenommen haben, dann schalten Sie aus Ihrem Weltbilde eben das aus, was die Erzengel nichts angeht.",
        "Also werden wir uns sagen: Ja, was ist denn von dem, was auch menschliches Bewußtsein werden kann, noch für die Erzengel da?"
      ],
      [
        "Was ist von dem­selben für die Volksgeister vorhanden?",
        "Alles, was Sie in der Empfin­dungsseele erleben, was Sie als gewöhnliche, durch die Außenwelt bewirkte Lust, als gewöhnliches, durch die Außenwelt bewirktes Leid erleben, alles, was Farben, Töne, überhaupt sinnliche Wahrnehmungen der Außenwelt sind, das geht diese Wesenheiten nichts an."
      ],
      [
        "Schalten Sie also den ganzen Inhalt der menschlichen Empfindungsseele aus, und sagen Sie sich, was im Weltbilde vorhanden ist dadurch, daß für den Menschen die Empfindungsseele da ist, das ist für die Erzengel nicht von Bedeutung, da wirken sie nicht hinein.",
        "Sogar ein Teil der Verstandesseele ist noch kein Element, das für die Erzengel von Bedeu­tung ist, insoweit dieselbe angeregt wird durch die äußeren Empfin­dungen."
      ],
      [
        "Was äußerlich angeregt wurde, was der Mensch mit dem Ver­stande verarbeitet und dem Gemüte durchlebt, auch das geht die Erz­engel nichts an.",
        "Aber in die Verstandesseele des Menschen spielen doch schon gewisse Dinge hinein, welche der Mensch sozusagen auf dem­selben Terrain mit den Erzengeln erlebt."
      ],
      [
        "Wir können ganz genau wahr­nehmen, daß solche Dinge in die menschliche Verstandes- oder Gemütsseele hineinspielen, wenn wir sehen, wie zum Beispiel in unserem Leben dasjenige, was wir unsere moralischen Ideale nennen, an uns herantritt."
      ],
      [
        "Es gäbe keine moralischen Ideale, wenn wir angewiesen wären, uns nur über dasjenige Empfindungen zu machen, über das Lust und Leid zu empfinden und uns darüber Gedanken zu machen, was uns von der Außenwelt als die Sinneswahrnehmung entgegentritt.",
        "Da würden wir uns zwar über die Blumen des Feldes, auch über eine schöne Land­schaftskonfiguration freuen können, aber wir würden niemals in unse­rem Gemüte für ein Ideal entbrennen können, das uns nicht aus der Außenwelt entgegenleuchten kann, das wir uns in die Seele einschreiben können, und wofür wir dann erglühen.",
        "Aber wir müssen nicht nur erglühen und in der Empfindungsseele fühlen, sondern wir müssen auch darüber denken.",
        "Der Mensch, der nur empfindet, der nicht denkt, der kann zwar ein Schwärmer, aber niemals ein praktischer Mensch sein.",
        "Wir müssen die Ideale nicht von außen in die Empfindungsseele auf­nehmen, sondern sie einströmen lassen aus der geistigen Welt und sie in der Verstandes- oder Gemütsseele verarbeiten.",
        "Die künstlerischen, die architektonischen Ideale und so weiter sind in der Verstandes- oder Gemütsseele und in der Bewußtseinsseele anwesend.",
        "Sie hängen zusam­men mit dem, was der Mensch von außen nicht wahrnehmen kann, was aber doch innerlich sein Wesen durchglüht und durchsetzt, so daß es einen Teil seines Lebens ausmacht."
      ],
      [
        "Schauen Sie sich das Leben der Völker von Epoche zu Epoche an, wie es verlaufen ist, wie immer neue Vorstellungen und Weltgeheimnisse darin aufgekommen sind.",
        "Wo hätten die Griechen ihre Vorstellungen über Zeus und Athene hernehmen können, wenn sie sich nur auf die äußere Wahrnehmung verlassen hätten!",
        "Das lebte sich von innen hinein, was in den Weistümern, in den Mythologien, Religionen und in den Wissenschaften der Völker enthalten ist.",
        "So also müssen wir sehen, daß die Hälfte unseres inneren Wesens, die Hälfte unserer Verstandes- oder Gemütsseele und unserer Bewußtseinsseele von innen heraus angefüllt sind, und zwar gerade so weit, als der Mensch sich mit dem, was eben charakterisiert worden ist, innerlich durchdringt, so weit können die Erzengel in das menschliche Innere vordringen, und so weit geht auch das eigentliche Leben der Erzengel.",
        "Das müssen Sie also vom inneren Leben ausschalten, was von außen durch die Empfindungsseele aufge­nommen und durch die Verstandes- oder Gemütsseele verarbeitet wird."
      ],
      [
        "Dann haben Sie aber auch noch das, was wir unser Ich nennen.",
        "Für uns ist das Ich das höchste Glied unserer Wesenheit.",
        "Was wir da hineintragen in das moralische Bewußtsein, das sind Ideale, moralische, ästhetische, ideelle Gedanken.",
        "So wie der Ausblick dem Menschen gleichsam nach innen verschlossen ist, sich aber nach außen durch seine Sinne der Außenwelt öffnen kann, so kann er sagen: Ich nehme Farben, Töne, Kälte und Wärme wahr.",
        "Aber er hat auch das Bewußtsein, daß hinter diesen Wahrnehmungen von Farben, Tönen, Wärme und Kälte noch etwas Wesenhaftes ist.",
        "Das sind die Wesen des tierischen, pflanzlichen und mineralischen Reiches.",
        "Das ist dahinter; so daß der Mensch sich in der angedeuteten Weise die Welt darüber hinaus fortgesetzt denken kann.",
        "Darüber hinaus ist aber die Aussicht für den gewöhnlichen Men­schen verschlossen.",
        "Wäre das nicht der Fall, so könnte es gar keinen Materialismus geben.",
        "Würde der Mensch die Aussicht frei haben auf das Gebiet, das sich von der Verstandesseele und der Bewußtseinsseele nach oben hin erstreckt, dann wäre es ebenso töricht, die geistige Welt zu bezweifeln, wie es heute töricht wäre, die Existenz der Tier-, Pflan­zen- und Mineralwelt in Zweifel zu ziehen."
      ],
      [
        "Denken Sie nun, wie das Ich beim Menschen, das höchste Glied des­selben, in sich einschließt die Empfindungs-, Verstandes- und Bewußt­seinsseele.",
        "Beim Erzengel ist es nun so, daß sein Seelenleben anfängt bei seinem Erleben in der Verstandes- oder Gemütsseele, dann hinaufgeht in das Ich, das sich aber ausbreitet in eine Welt höherer Reiche, in ein Reich geistiger Tatsachen, in dem es lebt, wie der Mensch im Reiche der Tiere, Pflanzen und Mineralien lebt.",
        "So daß wir sagen können: Wir müssen zwar einsehen, daß dieses Erzengelwesen in seinem Seelenleben dasjenige, was wir menschliches Ich nennen, haben kann, jedoch kön­nen wir nicht sagen, daß das Ich des Erzengels mit diesem Ich gleicher Art ist.",
        "Mit dem Ich des Menschen ist also das Erzengel-Ich nicht einer­lei.",
        "Das Erzengel-Ich liegt eben um zwei Stufen höher, so daß der Erz­engel mit seinem Ich in einer höheren Welt wurzelt.",
        "So wie nun der Mensch durch seine Sinnesempfindung auf Farben schaut, Töne hört, so schaut der Erzengel herunter auf die Welt, die das Ich als objektive Wahrheit umschließt, nur daß sich um dieses Ich noch etwas herumgruppiert von jenem Teile des Astralischen, das wir Menschen in uns"
      ],
      [
        "als Verstandes- oder Gemütsseele kennen.",
        "Denken Sie sich diese Wesen­heiten in eine Welt schauend, die nicht das Mineralische, Pflanzliche und Tierische erreicht.",
        "Denken Sie, daß dafür der Blick, der ein geisti­ger ist, auf ihr Weltbild hingerichtet ist und daß sie da Mittelpunkte wahrnehmen.",
        "Diese Mittelpunkte sind die menschlichen Iche, um die sich wieder etwas gruppiert, das wie eine Art Aura aussieht.",
        "Da haben Sie das Bild, wie das Erzengelwesen auf die Völkerpersönlichkeiten, die zu dem Erzengel gehören, die das Volk ausmachen, heruntersieht.",
        "Seine Welt besteht aus einem astralischen Wahrnehmungsfelde, in dem ge­wisse Zentren darin sind.",
        "Diese Zentren, diese Mittelpunkte sind die einzelnen menschlichen Persönlichkeiten, sind die einzelnen mensch­lichen Iche.",
        "Also gerade so, wie für uns Farben und Töne, Wärme und Kälte im Wahrnehmungsfelde liegen und für uns die bedeutsame Welt sind, so sind für die Erzengelwesen, für die Volksgeister wir selbst mit einem Teil unseres Innenlebens das Wahrnehmungsfeld, und wie wir in die Außenwelt hineingehen und diese bearbeiten und umgestalten zu Instrumenten, so sind wir diejenigen Objekte - insofern wir zu diesem oder jenem Volksgeist gehören -, welche zu dem Arbeitsfelde der Erz­engel oder Volksgeister gehören."
      ],
      [
        "Da sehen wir hinein, so sonderbar das auch klingen mag, in eine höhere Erkenntnistheorie der Erzengel.",
        "Die ist nämlich eine ganz an­dere als die Erkenntnistheorie der Menschen, denn es ist schon dasjenige, was für die Erzengel das Gegebene ist, ganz anders.",
        "Für den Menschen ist das Gegebene das im Raume Ausgebreitete, das uns durch die Sinne als Farbe, Ton, Wärme, Kälte, Härte und Weichheit entgegentritt.",
        "Für die Erzengel ist das Gegebene, was innen im menschlichen Bewußtseinsfelde auftritt.",
        "Das ist für sie eine Summe von Zentren, von Mittelpunk­ten, um welche die inneren Erlebnisse der Menschen gesponnen sind, insofern als sich diese Erlebnisse in der Verstandes- oder Gemütsseele abspielen; ihre Tätigkeit ist in dem entsprechenden Falle aber eine höhere."
      ],
      [
        "Wie spezialisiert sich nun das Weltbild der Erzengel oder Volksgei­ster?",
        "Für den Menschen spezialisiert sich das Weltbild dadurch, daß, wenn er irgendeinen Gegenstand mit der Hand ergreift, er ihn warm oder kalt empfindet.",
        "Der Erzengel erlebt etwas Ähnliches, indem er die"
      ],
      [
        "menschlichen Individualitäten trifft.",
        "Da trifft er Menschen, welche mehr von der inneren Aktivität beseelt sind, reicheren Seeleninhalt haben, die machen auf ihn einen intensiveren Eindruck.",
        "Andere findet er lässig, lethargisch, mit armem Seeleninhalt, das sind die Wesen, die für ihn so dastehen, wie Wärme und Kälte für das Weltbild der mensch­lichen Seele.",
        "So spezialisiert sich das Weltbild des Erzengels, und je nachdem kann er die einzelnen Menschen gebrauchen, für sie arbeiten, indem er dasjenige webt, was aus seiner Wesenheit heraus das gesamte Volk zu leiten hat."
      ],
      [
        "Aber auch sonst steht mit dem Leben dieses Erzengels das Leben des betreffenden Volkes, dem er vorsteht, in gewissem Zusammenhang.",
        "Gerade so, wie der Mensch aufsteigende und absteigende Perioden im Leben hat, eine aufsteigende Jugendzeit und die absteigende Zeit des Alters, so erlebt der Erzengel in der aufsteigenden und absteigenden Kultur eines Volkes seine Jugend und sein Alter."
      ],
      [
        "Nun müssen wir wieder in das innere Leben eines solchen Erzengels hineinsehen.",
        "Sie haben aus dem, was ich erzählt habe, wohl schon gemerkt, daß dasjenige, was der Mensch von außen bekommt, der Erz­engel von innen erhält; dafür bekommt der Erzengel die Empfindung, wenn die Volksindividualitäten als Zentren in ihm auftreten, daß das, was da an ihn herantritt, zwar von innen in seinem Bewußtsein auftritt, aber ihm doch sozusagen etwas Fremdes ist.",
        "Es ist etwas, was bei ihm so auftritt, wie die Einfälle in unserm Bewußtsein.",
        "In umgekehrter Weise tritt das auch an ihn heran, wie beim Menschen Jugend und Alter herantritt.",
        "Beim Menschen wird die Jugend so erlebt, daß er sich in seinen Gliedern frisch fühlt, daß sie im Aufstreben begriffen sind, sich entwickeln.",
        "Im Alter werden diese Glieder sozusagen schlaff und ver­sagen ihren Dienst.",
        "Das ist etwas, was der Mensch aus seinem Inneren herauskommen fühlt.",
        "Der Erzengel fühlt nun zwar alles als aus seinem Inneren herauskommend, aber es erscheint ihm das Auf- und Absteigen des Volkes doch als etwas Fremdes, als etwas, wovon er das Gefühl hat, daß es von ihm unabhängig ist, womit er also nicht direkt etwas zu tun hat, was ihm aber Veranlassung gibt, sich in irgendeinem Volke zu bestimmter Zeit zu verkörpern.",
        "Wenn die Möglichkeit da ist, sich zu verkörpern, wenn ein in der aufstrebenden Periode seines Lebens, in der"
      ],
      [
        "aufstrebenden Vollkraft lebendes Volk vorhanden ist, dann geht der Erzengel hinunter, ebenso wie der Mensch hinuntersteigt, wenn er das Leben durchlebt hat zwischen dem Tod und einer neuen Geburt.",
        "So also geht der Erzengel ebenso hinunter in ein Volk und verkörpert sich darin.",
        "Ebenso fühlt der Erzengel seinen Tod, die Notwendigkeit, sich von dem betreffenden Volke zurückzuziehen, wenn die einzelnen Wahrnehmungen, die Zentren, die er wahrnimmt, anfangen weniger produktiv, weniger aktiv zu sein, wenn sie anfangen, weniger Inhalt zu haben.",
        "Dann kommt die Zeit, wo er eine solche Volksgemeinschaft ver­läßt; er kommt dann in sein Devachan, in sein Leben zwischen Tod und neuer Geburt, um bei späterer Gelegenheit in anderer Weise eine Volks­gemeinschaft aufzusuchen.",
        "So bedeutet das jugendlich aufsteigende Leben eines Volkes die Jugend des Volksgeistes, und er nimmt sie wahr als ein frisches strömendes Element, in dem er lebt.",
        "Die absteigende Periode des Volkslebens nimmt er wahr als ein Dürrwerden der Zen­tren, die in seinem Wahrnehmungsgebiete sind. - Das sollte also eine Art Einblick in das Innere einer solchen Volksseele sein."
      ],
      [
        "Wenn wir uns das vor Augen führen, was eben gesagt worden ist, dann dürfen wir sagen: In gewisser Beziehung steht doch eine solche Volksseele dem einzelnen Menschenleben ziemlich fern, denn in dem einzelnen Menschen ist dasjenige, was er in seiner Empfindungsseele und in dem niederen Teil seiner Verstandesseele hat, ein Gebiet, in welches der Volksgeist, der Erzengel nicht hineinreicht.",
        "Für den Men­schen ist es aber etwas sehr Reales.",
        "Da fühlt der Mensch recht sehr, daß das mit dem Innersten, dem Intimsten seines eigenen Lebens zusammen­hängt.",
        "Es ist in gewisser Beziehung die Erzengel-Natur, die führende Volksnatur, etwas, was über dem einzelnen Menschen schwebt.",
        "Den persönlichen Dingen, die der Mensch dadurch erlebt, daß er Wahrneh­mungen durch seine Sinne hat, steht der Erzengel, der das Volk leitet, fremd gegenüber. - Aber da gibt es Vermittler, und es ist wichtig, daß wir verstehen, daß es solche Vermittler gibt.",
        "Das sind die Wesen, die wir Engel nennen, und die zwischen Erzengel und Mensch stehen.",
        "Fassen Sie es im strengsten Sinne des Wortes auf: Volksgeister sind Erzengel, sind solche Geister, welche mit der Umgestaltung ihres astra­lischen Leibes zu Geistselbst oder Manas fertig sind, und jetzt umgestalten"
      ],
      [
        "ihren Lebensleib zu Buddhi.",
        "Zwischen diesen Wesen und den Menschen stehen mitten drinnen die Engelwesen.",
        "Das sind solche We­sen, die mit der Umarbeitung ihres Astralleibes in Manas oder Geistselbst beschäftigt, aber noch nicht mit dieser Arbeit zu Ende gekommen sind.",
        "Der Mensch steht am Anfange dieser Arbeit im gegenwärtigen Zeitalter, die Engel stehen dem Ende derselben nahe, sind aber keines­wegs fertig damit.",
        "Daher berühren sich die Terrains dieser Wesenheiten viel intimer mit denen, in welchen der Mensch steht und lebt.",
        "Wir können sagen, daß die Engelwesen mit ihrer ganzen Seelenhaftigkeit dem zugeneigt sind, was wir astralischen Leib nennen.",
        "Deshalb haben sie volles Verständnis für alles das, was die menschliche Persönlichkeit durch Leid und Freude erleben kann.",
        "Aber weil sie auf der andern Seite viel höher über das menschliche Ich hinaufragen, weil sie ein höheres Ich haben, weil sie einen Teil der höheren Welt aufnehmen können, deshalb ragt ihre Bewußtseinswelt in diejenigen Terrains hinein, auf denen sich die Bewußtseinswelt der Erzengel befindet.",
        "Sie sind also so recht die Vermittler zwischen Erzengel und einzelner Menschen-Indi­vidualität.",
        "Sie empfangen ihrerseits die Befehle der Volksgeister und tragen sie in die einzelnen Seelen hinein, und durch diese Vermittelung ergibt sich dann dasjenige, was der einzelne wirken kann, nicht bloß für seinen eigenen Fortschritt, seine eigene Entwickelung, sondern für sein ganzes Volk."
      ],
      [
        "Der Mensch hat diese zwei Strömungen in seinem Erleben nebenein­ander.",
        "Die eine Strömung ist die, die ihn von Inkarnation zu Inkarnation vorwärts bringt, die seine eigenen Angelegenheiten angeht, welche er vor allen Dingen zu besorgen hat, um diejenige Pflicht zu erfüllen, die doch im Grunde genommen die allerstrengste ist, denn es ist seine eigenste Pflicht.",
        "Er darf nicht stehen bleiben, weil er sonst die Keime, die in ihm veranlagt sind, brach liegen lassen würde, wenn er sich um sie nicht kümmerte.",
        "Das ist aber seine eigenste Angelegenheit, durch die er vorwärts schreitet von Verkörperung zu Verkörperung.",
        "Was er aber zu seiner Volksgemeinschaft beiträgt, was zu den Angelegenheiten sei­ner unmittelbaren Volksgemeinschaft gehört, das bildet die Inspiration des Engels, der die Befehle des Erzengels zu den einzelnen Menschen heranträgt.",
        "Wir können uns also ganz gut vorstellen, daß wir auf einem"
      ],
      [
        "Gebiete der Erde ein Volk haben, und über dieses Volk ist ausgebreitet die Volks-Aura, die Äther-Aura, und da spielen wieder die Kräfte des Volksgeistes hinein und modifizieren nach den drei Arten von Kräften den Ätherleib des Menschen.",
        "Das, was in diese Volks-Aura hineinspielt, das ist der Erzengel.",
        "Ihn denken wir uns als ein höheres Wesen, als ein Wesen, das in der Entwickelung zwei Stufen höher steht als der Mensch, das über dem ganzen Volke schwebt und die Anordnungen gibt in bezug auf das, was dieses Volk im großen zu erfüllen hat.",
        "Der Erzengel weiß, was getan werden muß während des Aufstrebens, während der Jugendfrische des Volkes; er weiß, zu welchen Verrichtungen des Vol­kes der Übergang von der Jugend zum Alter benutzt werden muß, damit seine Impulse richtig wirken können."
      ],
      [
        "Diese großen Züge bildet der Erzengel.",
        "Hier auf diesem physischen Plan aber muß der einzelne Mensch arbeiten, hier muß der Mensch dafür sorgen, daß diese großen Ziele verwirklicht werden.",
        "Da stehen dann zwischen dem einzelnen Menschen und dem Erzengel die Engel als Mittelwesen, die den Menschen dann hindrängen zu dem Platze, an den er hingedrängt werden muß, damit im Volksgefühle dasjenige geschieht, was den großen Anordnungen des Erzengels entspricht.",
        "Wir stellen uns ein richtiges Bild der Sache vor, wenn wir uns das, was ich beschrieben habe, keineswegs bloß als Allegorie, sondern möglichst als Wirklichkeit vorstellen."
      ],
      [
        "Nun wirkt hinein in das ganze Gewebe, das der Erzengel spinnt, dasjenige, was wir die abnormen Erzengel genannt haben, die Geister der Sprache, in dem Sinne genommen, wie ich es gestern charakterisiert habe.",
        "Wir haben aber auch charakterisiert, wie die abnormen Geister der Persönlichkeit, die Archai, hereinwirken.",
        "Da können wir nun hinblicken auf das Feld, wo der Erzengel seine Befehle erteilt, wo er die Missionen ausgibt, die von den Engeln weiter in die einzelnen Menschen hineingetragen werden.",
        "Aber der Erzengel kann auch in das Feld der abnormen Geister der Persönlichkeit hineinwirken, und es können in dem gegenseitigen Zusammenwirken des Erzengels mit den abnormen Geistern der Persönlichkeit - weil sie ganz andere Ziele verfolgen als die Erzengel - in gewisser Beziehung die Maßnahmen des Erzengels durchkreuzt werden.",
        "Wenn das geschieht, wenn diese abnormen Geister"
      ],
      [
        "der Persönlichkeit die Maßnahmen des Erzengels durchkreuzen, dann können wir die Wahrnehmung machen, daß sich innerhalb eines Volkes selber Gruppen bilden mit speziellen Aufgaben.",
        "Dadurch, daß sich innerhalb eines Volkes solche Gruppen mit speziellen Aufgaben bilden, wird das Wirken der Geister der Persönlichkeit äußerlich sichtbar.",
        "Das kann durch viele Jahrhunderte hindurch dauern.",
        "Sie haben zum Bei­spiel gerade in dem Gebiete, in dem wir insbesondere jetzt geisteswis­senschaftlich zu wirken haben, in Deutschland, durch Jahrhunderte hindurch dieses Spiel des Erzengels der Deutschen im Zusammenwirken mit den manchmal widerstrebenden einzelnen Geistern der Persönlich­keit gesehen.",
        "In der Zersplitterung der gemeinsamen deutschen Nation in die kleineren Volkspartien haben Sie ein Zusammenspiel der abnor­men Geister der Persönlichkeit mit dem Erzengel."
      ],
      [
        "Solche Völker haben etwas wenig Zentralisiertes, sie sehen mehr auf die Ausbildung der Individualitäten.",
        "Das hat in gewisser Beziehung sein Gutes, weil dadurch eine große Mannigfaltigkeit, viele Nuancen des Volkstums zum Ausdruck kommen können."
      ],
      [
        "Aber Sie können auch den anderen Fall ins Auge fassen, daß nicht der abnorme Geist der Persönlichkeit, sondern der normale Geist der Persönlichkeit, der im Zeitgeist sich äußert, für irgend einen Zeitpunkt sozusagen wichtiger wird, als er es sonst im gewöhnlichen Verlaufe ist."
      ],
      [
        "Wenn wir also auf ein Volk blicken, so blicken wir, als auf seine erste Macht, auf den Erzengel hin.",
        "Da wirkt dann der Zeitgeist hinein, gibt seine Befehle an den Erzengel, und dieser gibt seine Befehle weiter an die Engel, und diese vermitteln sie dem einzelnen Menschen.",
        "Weil man nun gewöhnlich nur das sieht, was einem am nächsten steht, so sieht man bei diesem zusammengesetzten Wirken als das Wichtigste das Wirken der Erzengel.",
        "Es kann aber auch eintreten, daß der Zeitgeist schwerwiegendere, gewichtigere Befehle ausgeben muß, daß er sozu­sagen genötigt ist, dem Erzengel etwas wegzunehmen, weil er einen Teil des Volkes herausgliedern muß, damit das, was Aufgabe der Zeit, Mis­sion des Zeitgeistes ist, erfüllt werden kann.",
        "In einem solchen Falle splittern sich dann Volksgemeinschaften von anderen ab.",
        "Da gewinnt der Zeitgeist sichtbarlich die Oberhand über das Wirken des Erzengels.",
        "Ein solcher Fall trat ein, als das holländische Volk von der Grundlage,"
      ],
      [
        "die es mit dem deutschen Volke gemeinsam hatte, absplitterte.",
        "Holland und Deutschland hatten ursprünglich einen gemeinsamen Erzengel, und die Absplitterung geschah dadurch, daß der Zeitgeist in einem bestimmten Augenblicke einen Teil heraussonderte und diesem Teil dann dasjenige übertrug, was die wichtigen Angelegenheiten des mo­dernen Zeitgeistes geworden sind.",
        "Alles, was Sie in der holländischen Geschichte lesen können - Geschichte ist zwar nur ein äußerer Aus­druck, eine Maja für dasjenige, was innerer Vorgang ist -, ist nur eine Widerspiegelung dieses inneren Vorgangs.",
        "So sehen wir in diesem Fall äußerlich sich vollziehen die Absplitterung des holländischen Volkes von dem gemeinsamen deutschen Volkstum.",
        "Der innere Kern ist aber der, daß der Zeitgeist ein Werkzeug brauchte, um dasjenige auszufüh­ren, was die überseeische Mission des Zeitgeistes war.",
        "Die ganze Mission des holländischen Volkes ist eine Mission des Zeitgeistes gewesen.",
        "Und zu dem Zwecke wurde es abgespalten, um dem Zeitgeiste zu ermögli­chen, in einer bestimmten Zeit etwas Wichtiges mit diesem Teile auszu­führen.",
        "Das, was die Historiker beschreiben, ist nur äußere Maja, was die wahren Tatsachen mehr verhüllt als enthüllt."
      ],
      [
        "Noch anderswo kann Ihnen entgegentreten das, was sich in dieser Beziehung in auffälliger Weise zugetragen hat, nämlich daß sich ein Teil eines Volkes von dem gemeinsamen Volke abspalten mußte.",
        "Das ist bei dem portugiesischen Volke der Fall.",
        "Sie werden vergeblich an­dere Gründe dafür in diesem Falle suchen und finden, als daß es sich hier lediglich um einen Sieg des Zeitgeistes über den Erzengel handelt.",
        "Wenn Sie die einzelnen Ereignisse durchgehen, werden Sie finden, daß hier die Gelegenheit benutzt wurde, ein besonderes Volkstum zu bil­den - viele Gelegenheiten waren nicht da.",
        "Das spanische Volk bildete mit dem portugiesischen ein Muttervolk.",
        "Die äußeren Gründe sind vielleicht die, daß die Flüsse nur bis zur portugiesischen Grenze gut befahrbar sind.",
        "Andere äußere Gründe gibt es nicht.",
        "Dagegen gibt es den inneren Grund, daß die Aufgaben erfüllt werden mußten, die gerade die Aufgaben der Portugiesen waren und die andere waren, als die Aufgaben des gemeinsamen spanischen Volkes.",
        "Da sehen wir die Zeitgeister eine Zeitlang eine intensivere Tätigkeit entwickeln, als sie sonst ausführen.",
        "Wir sehen die bisherige Harmonie durch eine andere"
      ],
      [
        "ersetzt.",
        "Wir sehen den Zeitgeist, statt daß er seine Befehle an den Erz­engel erteilt, direkt in die Geschichte des Volkes eingreifen und sehen, wie die anderen Geister diese Gelegenheit benutzen, um sich zu ver­körpern.",
        "Wenn ein solches Volkstum abgespalten wird, dann versieht der Zeitgeist eine Zeitlang in dem ersten Enthusiasmus, der die einzel­nen Menschen durchdrungen hat, so sehr die Funktionen des Erzengels, daß die Abspaltung kaum als etwas anderes vorhanden ist denn als ein Hasten und Drängen innerhalb dieses Volkes.",
        "Man sieht die Hast und das Drängen, die Regsamkeit, die aus der Mission des Zeitgeistes kommt.",
        "Dann aber stellt sich die Möglichkeit ein, daß ein normaler und ein abnormer Erzengel sich in dem abgespaltenen Volksteil verkörpert.",
        "So sehen wir das Heranwachsen des holländischen und des portugiesi­schen Volkes, die sodann ihre eigenen normalen und eigenen abnormen Erzengel bekommen.",
        "In dem, was sich darin verkörpert, in der Ver­schiedenheit des Temperamentes des Volkes, das in den einzelnen Per­sönlichkeiten zum Ausdrucke kommt, sehen wir das Hineinspielen desjenigen, was wir als diese geistigen Wesenheiten genannt haben.",
        "In ganz merkwürdiger Art sehen wir das Hineinspielen dieser geistigen Wesenheiten, und wir erkennen dann, daß die sich äußerlich abspie­lende Geschichte nur ein Ergebnis des Wirkens derselben ist."
      ],
      [
        "Nach und nach gewinnt der Satz, daß die Außenwelt Maja oder Illusion ist, immer konkretere Bedeutung.",
        "Das, was in der äußerlichen Geschichte geschieht, ist nur der äußere Abglanz der geistigen, der übersinnlichen Wesenheiten, gerade so wie der äußere Mensch nur der äußere Abglanz des inneren Menschen ist.",
        "Deshalb mußte ich sagen, und das muß immer wieder betont werden: Der Satz «Die Welt ist Maja» ist von allergrößter Wichtigkeit.",
        "Es genügt aber nicht, daß man ihn abstrakt betont, man muß vielmehr in der Lage sein, ihn in den Einzelheiten durchzuführen."
      ],
      [
        "Nun haben wir aber gesehen, daß auch andere Geister und Hierar­chien in dem, was wir die Welt nennen, tätig sind.",
        "Wir haben von den normalen und abnormen Erzengeln gesprochen.",
        "Die abnormen Erz­engel haben sich uns nun entpuppt als eigentliche Geister der Form oder Gewalten, die nur auf einen gewissen Teil der Eigenschaften ihrer Ent­wickelung verzichtet haben.",
        "Wir können dann fragen: Wie ist es aber"
      ],
      [
        "mit den normalen Geistern der Form?",
        "Die normalen Geister der Form erblicken wir um vier Grade höher stehend als den Menschen. - Wir werden in unserer nächsten Betrachtung noch einiges über diese nor­malen Geister der Form zu sprechen haben. - Das sind also Wesenheiten, welche vier Grade höher sind als der Mensch.",
        "Dasjenige aber, was wir gestern als Hierarchien angeführt haben, erschöpft sich nicht mit dem, was wir nach oben abschließend als Geister der Form genannt haben.",
        "Höher als diese stehen die Geister der Bewegung, die Dynameis, die Mächte; noch höher die Wesenheiten, die wir Kyriotetes, Herrschaf­ten oder Geister der Weisheit nennen.",
        "Sie finden diese verschiedenen geistigen Wesenheiten sowohl in meiner «Geheimwissenschaft» als auch in meiner Schrift über die «Akasha-Chronik» aufgeführt."
      ],
      [
        "Nun werden Sie begreifen können, daß das Gesetz des Verzichtens, des Zurückbleibens auch für die höheren Geister gilt, daß also auch die Geister der Bewegung mit gewissen Eigenschaften zurückbleiben kön­nen - Geister der Bewegung, die fünf Stufen höher sind als der Mensch -, daß gewisse Geister der Bewegung heute in der Menschheits­entwickelung enthalten sind so, als ob sie erst Geister der Form, Gewal­ten wären.",
        "Das sind in bezug auf gewisse Eigenschaften eigentlich Geister der Bewegung und in bezug auf andere Eigenschaften, hinsicht­lich welcher sie verzichtet haben, Geister der Form.",
        "So daß wir haben normale Geister der Form, die vier Stufen höher stehen als der Mensch, und andere Geister, die auf demselben Terrain, wo die Geister der Form sind, wirken, die aber eigentlich Geister der Bewegung sind.",
        "Das ist also ein Gebiet, auf dem - so wie wir ein Gebiet gefunden haben, auf dem normale und abnorme Erzengel zusammenwirken - die normalen und abnormen Geister der Form, die zurückgebliebenen Geister der Bewegung, zusammenwirken.",
        "Durch dieses Zusammenwirken geschieht aber etwas, was die Menschen sehr wohl angeht; dadurch geschieht die Ausgestaltung dessen, was wir die menschlichen Rassen nennen, die wir unterscheiden müssen von den Völkern."
      ],
      [
        "Wir bekommen keinen verwirrenden Begriff, wenn wir die Sache so betrachten, sondern einen flüssigen Begriff; wir dürfen das nicht alles zusammenwerfen.",
        "Ein Volk ist keine Rasse.",
        "Der Volksbegriff hat nichts zu tun mit dem Rassenbegriff.",
        "Es kann sich eine Rasse in die"
      ],
      [
        "verschiedensten Völker spalten.",
        "Rassen sind andere Gemeinschaften als Volksgemeinschaften.",
        "Wir sprechen gewiß mit Recht von einem deutschen, einem holländischen, einem norwegischen Volke; wir spre­chen aber von einer germanischen Rasse.",
        "Was wirkt da nun in dem Rassenbegriff?",
        "Da wirken zusammen diejenigen Wesenheiten, die wir als die normalen Geister der Form oder Gewalten bezeichnen, und die Wesenheiten, die wir als die abnormen Geister der Form, die eigentlich Geister der Bewegung sind mit Missionen der Geister der Form, kennen gelernt haben.",
        "Deshalb sind die Menschen in Rassen gespalten.",
        "Das, was die Menschen über das ganze Erdenrund hin gleich macht, was jeden Menschen, gleichgültig welcher Rasse er angehört, zum Menschen, zum Angehörigen des ganzen Menschentums macht, das bewirken die normalen Geister der Form.",
        "Dasjenige aber, was über die ganze Erde dahinspielt, was das gesamte Menschentum in Rassen gliedert, das bewirken die abnormen Geister der Form, die verzichtet haben zugun­sten der Tatsache, daß nicht eine einzige Menschheit auf der Erde erscheint, sondern eine Mannigfaltigkeit von Menschen."
      ],
      [
        "Da gewinnen wir sozusagen den Untergrund, den Boden für das, woraus sich erst die einzelnen Völkerindividualitäten erheben.",
        "Wir gewinnen dadurch die Umschau über den ganzen Erdenplaneten, finden den Erdenplaneten dazu bestimmt, eine Menschheit zu tragen durch die normalen Geister der Form, finden, daß sich die zurückgebliebenen Geister der Bewegung in dieses Terrain der Geister der Form hineinbegeben und als abnorme Geister der Form das Menschentum auf dem ganzen Erdenrund in die einzelnen Rassen gliedern.",
        "Wenn wir hineinblicken in das, was diese Geister eigentlich wollen, wenn wir uns ver­tiefen in die Ziele und Aufgaben dieser normalen und abnormen Geister der Form, dann werden wir verstehen, was sie mit den Menschenrassen wollen, wie durch dieselben eine Grundlage geschaffen wird für das, was sich aus ihnen heraushebt.",
        "Wenn wir dann noch ein Volk selbst betrachten, dann werden wir das Volk begriffen und verstanden haben."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "VIERTER VORTRAG Kristiania, 10. Juni 1910",
    "paragraphs": [
      "Will man zu dem Verhältnis der Menschenrassen zu einander vordrin­gen, welche ja die Grundlage sind, aus welcher sich die einzelnen Volksgemeinschaften herausheben, dann muß man berücksichtigen, daß der Mensch, den wir vor uns haben, der wir selber sind, eigentlich ein recht kompliziertes Wesen ist und nur durch das Zusammenwirken vieler, vieler Wesenheiten des Weltalls in seiner heutigen Form und Wesenheit hat entstehen können. Wir wissen ja aus der Betrachtung der «Akasha-Chronik» und aus anderen Betrachtungen, die über die Entwickelung des Menschen gepflogen worden sind, daß unsere Erde selbst früher - bevor sie den jetzigen Zustand erreicht hat - drei Zustände hat durch­machen müssen.",
      "Im Verlaufe dieser drei Zustände sind nach und nach veranlagt und bis zu ihrem heutigen Grade ausgebildet worden die drei sogenannten Glieder des Menschen: der physische Leib, der Äther- oder Lebensleib und der Astralleib. Während der jetzigen Erdenverkörpe­rung ist erst der Mensch fähig geworden, ein viertes Glied, ein Ich in sich aufzunehmen.",
      "Diese vier Glieder seiner Wesenheit zeigen uns alles das, was durch die drei oder vier Verkörperungen unserer Erde hin­durch geschehen ist, durch die Verkörperung als Saturn, Sonne, Mond und durch die Erdenzeit selbst, soweit sie bis jetzt verlaufen ist. Wenn Sie vorüberziehen lassen vor Ihrem Blick alle die Wesenheiten, die da zusammengewirkt haben, diese Geister des Willens oder Throne' die Geister der Weisheit, Geister der Bewegung, Geister der Form, Geister der Persönlichkeit, Erzengel, bis herunter zu den Engeln, und über den Geistern des Willens oder Thronen die Cherubime und Seraphime, so werden Sie sich sagen können, daß aus einem ganz komplizierten Zu­sammenwirken erst hervorgehen konnte, was des Menschen heutige Organisation möglich macht.",
      "Wir haben gesehen, daß nicht nur not­wendig war, daß so viele Wesenheiten und Naturkräfte zusammenwirkten im Kosmos, sondern daß zum Zustandekommen des Menschen auch noch nötig war, daß zu gewissen Epochen gewisse Wesenheiten auf den normalen Gang ihrer Entwickelung verzichteten, zurückgeblieben",
      "sind, so daß sie in anderer Weise, als es bei ihrem normalen Entwickelungsgange möglich gewesen wäre, in die menschliche Orga­nisation eingreifen konnten.",
      "Also wir sehen in ein wunderbar vielgestaltiges und mannigfaltiges Gewebe hinein, wenn wir den Menschen, so wie er uns heute vor Augen tritt, eigentlich verstehen wollen. Wir müssen uns auch klar sein darüber, daß wir nur dann, wenn wir gewissermaßen dieses Gewebe aus­einanderhalten und die einzelnen Wesen in ihrer Tätigkeit belauschen, verstehen lernen, wie durch das Zusammenwirken dieser Wesenheiten der Mensch erst zustande gekommen ist.",
      "Da können wir nun sagen: Die hauptsächlichste Wesenheit, welche für den heutigen Menschen in Betracht kommt, ist diejenige, welche ihm die Möglichkeit gegeben hat, zu sich «Ich» zu sagen, nach und nach zu dem Bewußtsein des Ich zu kommen. Und wir wissen, daß diese Möglichkeit zuerst von den Gei­stern der Form, von denjenigen Wesenheiten gegeben worden ist, die wir Gewalten, Exusiai nennen.",
      "Wenn wir gerade diese Wesenheiten bei ihrer Tätigkeit, welche sie dem Menschen zuwenden, belauschen und uns gewissermaßen fragen: Wie würde es mit dem Menschen werden, wenn bloß diese Wesenheiten, und zwar nur diejenige Art dieser Wesen­heiten, die in normaler Entwickelung sich befindet, in der Hauptsache im Menschen tätig wäre? - so werden wir finden: Sie sind die Verleiher der Ich-Organisation. Damit ist aber schon gesagt, daß sie eigentlich, wenn wir sie ihrer eigenen Natur nach betrachten, ihr Hauptinteresse daran haben, den Menschen zu seinem Ich zu bringen.",
      "Nun aber ist das, was diese Wesenheiten eigentlich im Menschen zu verrichten haben, im heutigen Menschenleben erst in einem bestimmten Lebensalter aktuell, tritt erst in einem bestimmten Lebensalter zutage.",
      "Wenn Sie sich an das erinnern, was über die Erziehung des Kindes vom Standpunkte der Geisteswissenschaft gesagt worden ist, so werden Sie sich sagen: Der Mensch entwickelt hauptsächlich zwischen seiner physischen Geburt und dem Zahnwechsel, also bis zum siebenten Jahre hin, den physischen Leib. An der Entwickelung dieses physischen Leibes haben diese Geister der Form gar kein besonderes Interesse, denn diese ist im Grunde genommen eine Wiederholung dessen, was auf dem alten Saturn mit dem Menschen geschah, was sich schon oftmals wiederholt",
      "hat, und was sich nach der letzten physischen Geburt bis zum siebenten Lebensjahre vorläufig zum letzten Male in einer besonderen Art wie­derholt hat. Dann kommt die Zeit vom siebenten bis zum vierzehnten Jahre, also bis zur Geschlechtsreife.",
      "Auch das ist eine Zeit, an der die Geister der Form kein besonderes Interesse haben; es ist eine Wieder­holung der alten Sonnenzeit, und die Geister der Form wollten eigent­lich mit ihrer Haupttätigkeit, mit der Verleihung des Ich, erst im Zustande des Erdenlebens eingreifen. Wir kommen dann zu dem dritten Lebensalter, das zwischen dem fünfzehnten und dem ein- oder zwei­undzwanzigsten Lebensjahre abläuft.",
      "In dieser Zeit wird der Astralleib, der in normaler Weise der Mondentwickelung zugehört, wiederholent­lich entwickelt im Menschen. Da haben die Geister der Form, die sich normal entwickeln, noch immer kein Interesse am Menschen, so daß wir sagen müssen: Die drei Lebensalter des Menschen, die der eigent­lichen Geburt des Ich vorangehen, die erst um das zwanzigste Jahr herum eintritt, bieten kein unmittelbares Interesse für die Geister der Form.",
      "Sie greifen - man möchte sagen, aus ihrer eigenen Natur heraus - erst um das zwanzigste Lebensjahr herum ein, so daß, wenn Sie das bedenken, Sie es nicht mehr so ganz sonderbar finden werden, wenn gesagt wird: Nach der eigentlichen Intention der Geister der Form würde der Mensch erst in dem Zustande, in welchem er sich um das zwanzigste Lebensjahr herum befindet, da zu sein brauchen. Das, was sich im Menschen bis dahin entwickelt, ist im Grunde genommen für diese Geister der Form eine Art Embryonal-, eine Art Keimzustand.",
      "Und wenn ich etwas bildlich sprechen darf, so möchte ich sagen: Den Geistern der Form, welche sich normal entwickelt haben, wäre es am liebsten, wenn alles mit einer gewissen Regelmäßigkeit herginge, wenn ihnen bis dahin niemand ins Handwerk pfuschte. Wenn niemand diesen Geistern der Form bis zum zwanzigsten Jahre dazwischen käme, so würde der Mensch während der ersten sieben Jahre der Entwickelung das Bewußtsein haben, das dem physischen Leibe zukommt; das ist nämlich ein sehr dumpfes Bewußtsein, wie es die Mineralwelt hat.",
      "Im zweiten Stadium - in der Zeit vom siebenten bis zum vierzehnten Jahre - würde er ein Schlafbewußtsein haben. Vom vierzehnten bis zwanzigsten Jahre würde er in intensiver Weise im Inneren wirksam",
      "sein, aber eine Art von Traumdasein führen. Nach diesem Bewußtsein als Mondenwesenheit, etwa im einundzwanzigsten Jahre, würde der Mensch erst eigentlich erwachen. Da würde er erst zu dem Ichbewußt­sein kommen. Wenn es nach der normalen Entwickelung ginge, dann würde er da erst aus sich herausgehen und die Außenwelt in dem Weltbilde überblicken, das heute unser bekanntes Weltbild ist.",
      "So also sehen Sie, daß im Grunde genommen, wenn wir nur die Tätigkeit der Geister der Form in Betracht ziehen, der Mensch sehr verfrüht zu seinem Bewußtsein kommt, wie er es heute hat, denn Sie wissen, daß dieses Bewußtsein beim heutigen Menschen in gewissem Grade bald nach der physischen Geburt erwacht. Es würde nicht in der Form erwachen, daß es klar und deutlich die physische Außenwelt sieht, wenn nicht andere Geister, die eigentlich Geister der Bewegung sind, zurückgeblieben wären und verzichtet hätten auf die Entwicke­lung gewisser Fähigkeiten, die sie bis zur Erdenentwickelung hätten erlangen können, wenn sie nicht stehengeblieben wären in ihrer Ent­wickelung, so daß sie jetzt während der Erdenentwickelung in die Entwickelung des Menschen in besonderer Weise eingreifen können.",
      "Weil sie ihre Entwickelung in einer anderen Weise durchgemacht haben, sind sie in der Lage, dem Menschen schon früher das beizubringen, was er erst um das zwanzigste Jahr herum erringen sollte. So also sind das geistige Wesenheiten, welche verzichtet haben auf die Möglichkeit, ihre Entwickelung bis zur Erdenentwickelung in normaler Weise weiter­zutreiben, geistige Wesenheiten, die während der Erdenentwickelung Geister der Bewegung hätten sein können, die aber stehen geblieben sind auf der Stufe der Geister der Form und die nun in der Erdenentwickelung als Geister der Form wirken.",
      "So können sie während der Erdenentwickelung dem Menschen, der eigentlich noch gar nicht reif ist dazu und der manches aus der früheren Zeit noch nachzuholen hat, das verleihen, was die normale Entwickelungsform erst um das zwan­zigste Jahr herum verleihen würde. So tritt der Mensch in das Dasein und erhält von den abnormen Geistern der Form Fähigkeiten, die er sonst erst um das zwanzigste Jahr herum erhalten würde.",
      "Das alles hat ganz bedeutsame Folgen. Denken Sie sich einmal, es wäre nicht so. Wenn es nicht so wäre, wenn diese Geister mit abnormer",
      "Entwickelung nicht eingreifen würden, dann würde der Mensch über­haupt erst für die physische Welt in Betracht kommen in dem Zustande, den er um das zwanzigste Jahr herum hat, das heißt, er müßte in diesem Zustande als physisches Wesen geboren werden, er müßte ganz andere Keimzustände durchmachen. In der Tat wird durch diese abnormen Gei­ster der Form die menschliche Entwickelung schon von der Geburt an bis zum zwanzigsten Jahre in die physische Welt hinausgestellt; das ist ungefähr das erste Drittel unseres Erdenlebens. Wir müssen also sagen:",
      "Das erste Drittel unseres Erdenlebens wird nicht durch die den Erdenzustand beherrschenden geistigen Wesenheiten, sondern durch andere, abnorme geistige Wesenheiten regiert, und weil diese teilnehmen an der Entwickelung, so haben wir Menschen auch nicht die Gestalt, die wir hätten, wenn wir in dem Zustande geboren würden, den wir um das zwanzigste Jahr herum haben. Das muß der Mensch damit bezahlen, daß er ein Drittel seines Lebens - die Zeit bis zu seinem zwanzigsten Jahre hin - so zubringt, daß er dem großen Einfluß dieser abnormen Wesenheiten hingegeben ist. Sein ganzes Wachstum macht der Mensch eigentlich unter den Einflüssen der abnormen Wesenheiten durch. Er muß es dadurch bezahlen, daß, nachdem das mittlere Drittel abgelaufen ist - das im Grunde nur den normalen Geistern der Form gehört -, die absteigende Bahn, ein Zurückgehen beginnt, und seine Äther- und Astralorganisation zerfallen, so daß das Leben in drei Glieder oder Abteilungen zerfällt: in ein aufsteigendes, ein mittleres und ein abstei­gendes Drittel. In dem mittleren Teil wird der Mensch während seines Erdenlebens eigentlich erst Mensch, und im letzten Drittel muß er das zurückgeben, was er während des ersten, aufsteigenden Drittels em­pfangen hat, muß er die entsprechende Abschlagszahlung leisten.",
      "Wäre der Mensch in der Tat ausschließlich den Einflüssen der nor­malen Geister der Form hingegeben gewesen, dann würde alles das, was heute bis ins zwanzigste Jahr hinein geschieht, ein ganz anderes Antlitz, eine ganz andere Gestalt haben. Es wäre alles ganz anders verlaufen, so daß alles das, was mit des Menschen heutiger Entwickelung zusam­menhängt in der ersten der drei Lebensepochen, im Grunde genommen ein Dasein ist, das vieles von den späteren Lebensepochen vorausnimmt. Dadurch ist der Mensch bis zu der zweiten Epoche seines Lebens ein",
      "materielleres Wesen geworden, als er sonst geworden wäre. Der Mensch hätte sonst bis zu diesem Momente seines Lebens nur geistige Zustände durchgemacht und würde bis zur jetzigen materiellen Verdichtung erst herabgestiegen sein in dem Zeitpunkte der Entwickelung, den er erst im zwanzigsten oder einundzwanzigsten Lebensjahre durchmacht, wo er sich selber an die Erde gebunden vorfände. Es sagt uns also die Geisteswissenschaft, daß, wenn diese Entwickelung so vorwärts gegan­gen wäre, der Mensch erst in dem Zustande so recht eigentlich auf die Erde herabgestiegen wäre, den er heute im zwanzigsten oder einund­zwanzigsten Lebensjahre erreicht; er würde die vorangehenden Zu­stände nicht auf der Erde haben durchmachen können. Er hätte sie erhöht über der Erde, im Umkreis der Erde durchmachen müssen. Und jetzt begreifen Sie den ganzen Gang der menschlichen Kindheit und Jugendentwickelung. Wir können sehen, wenn wir diese gerade Linie",
      "B-C als Erdenweg bezeichnen, so wären es die Geister der Form, die den Menschen dazu bestimmt hätten, herunterzusteigen erst in diesem Punkte, (20/21 der Zeichnung). Hier würde der Mensch also erst die Erde erreicht haben, und er würde wieder hinaufsteigen nach dem vierzigsten Jahre und das letzte Drittel seines Lebens in einem vergeistigten Zustande durchmachen. Durch die abnormen Wesenheiten wurde der Mensch gedrängt, schon hier (bei A der Zeichnung) herabzusteigen und das Leben auf der Erde aufzunehmen. Das ist das Ge­heimnis unseres Daseins. So sehen wir, daß wir durch die uns eigentlich dirigierenden normalen Wesenheiten nur in dem mittleren Drittel unse­res Lebens ganz beherrscht sind, während unsere Wachstums- und unsere Niedergangsperiode unter dem Einfluß ganz anderer Wesen­heiten stehen, die in irgendeiner Weise auf ihre normale Entwickelung verzichtet haben.",
      "Wenn das alles so geworden wäre, wie es nicht geworden ist, wenn der Mensch erhöht im Umkreis der Erde das erste und dritte Drittel seines Lebens durchgemacht und nur im mittleren Teile die Erde be­rührt hätte, also im Grunde genommen ein ganz anderes Wesen gewor­den wäre, dann würde der Mensch nicht in dem Grade an die Erde gebunden sein, in dem er tatsächlich heute an dieselbe gebunden ist. Wenn das eingetreten wäre, dann würden alle Menschen, welche die Erde betreten, von gleicher Gestalt und Wesenheit sein; dann würden alle Menschen, die über die Erde hingegangen sind, gleichgestaltet gewesen sein.",
      "Eine Menschheit gäbe es nur. Dasjenige, was uns zu einem solchen Wesen macht, daß sich daraus die spezifischen Eigenschaften der Rassen ergeben, die im Menschentum zum Ausdruck kommen, das ist nicht im mittleren Drittel des Lebens enthalten.",
      "Durch alles das, was in der Zeit vorher liegt, was im ersten Drittel des Lebens sich vollzieht, sind wir mehr mit allen unseren Kräften an die Erde gebunden, als es die normalen Geister der Form für uns bestimmt haben. Dadurch aber ist der Mensch mehr von der Erde, auf der er lebt, abhängig geworden, als er es sonst geworden wäre.",
      "Er ist abhängig geworden von dem Orte der Erde, auf dem er lebt. Dadurch, daß der Mensch - sozusagen gegen die Intentionen der Geister der Form - früher auf die Erde herunter­steigt, wird er abhängig von dem Orte, weil er sich in einem Zustande mit der Erde verbindet, der ihm gar nicht vorgezeichnet ist.",
      "Unab­hängig wäre der Mensch geworden davon, ob er im Norden oder Süden, im Osten oder Westen die Erde betreten hätte, wenn er sie nur im mittleren Drittel seines Lebens betreten hätte. Dadurch aber, daß er abhängig wird von der Erde, dadurch, daß er eine Jugend durchmacht in der Weise, wie wir es charakterisiert haben, wird er erdgebunden, wird er ein mit dem Gebiete, auf dem er geboren ist, zusammenhängen­des, zu ihm gehörendes Wesen.",
      "Dadurch wird er abhängig von all den Verhältnissen der Erde, die diesem Orte zugehören, von dem Einfallen der Sonnenstrahlen, von dem Umstand, ob die Gegend nahe dem Äqua­tor in der heißen Zone oder in einem mehr gemäßigten Gebiete sich befindet, ob er auf einem niedrig gelegenen Gebiet oder auf einem Hochplateau geboren ist. Man atmet ja ganz verschiedenartig in der Ebene oder im Gebirge.",
      "Der Mensch wird also ganz abhängig von den",
      "irdischen Verhältnissen, von dem Ort, an dem er geboren ist. So sehen wir, daß der Mensch förmlich mit seiner Erdenmutter zusammenge­wachsen ist dadurch, daß er so eng zusammenhängt mit dem Orte, mit dem Gebiete der Erde, auf dem er jeweils geboren wird, und daß er bestimmt wird durch diejenigen Eigenschaften, die er dadurch erhält, daß diese Kräfte der Erde, die durch den betreffenden Ort bestimmt sind, in ihm wirken. Das alles bestimmt seinen Rassencharakter, und auf diesem Umwege sind die abnormen Geister der Form - diejenigen Gei­ster der Form oder Gewalten, die zu einer anderen Zeit als zwischen dem einundzwanzigsten bis dreiundzwanzigsten Jahre dem Menschen das geben, was wir heutiges Erdenbewußtsein nennen - die Verursacher der Rassenverschiedenheit des Menschen über die ganze Erde hin, die also von dem Orte auf der Erde abhängt, auf dem der Mensch geboren wird.",
      "Nun erlangt der Mensch während dieser Zeit - die also im Grunde genommen unter der Herrschaft der abnormen Geister der Form steht - auch die Möglichkeit, die Fähigkeit, seinesgleichen hervorzubringen. Auch diese Fähigkeit wird während der Zeit erworben, in welcher der Mensch gar nicht rein von den normalen Geistern der Form dirigiert wird. Dadurch ist die Möglichkeit gegeben, daß der Mensch nicht nur in der geschilderten Weise abhängig wird von dem Orte, auf dem er geboren ist, sondern daß die Eigenschaften, die er dadurch erhält, auch auf seine Nachkommen vererbt werden können, daß also die Rassenzusammengehörigkeit nicht nur sich ausspricht in den Einflüssen des Wohnplatzes, sondern auch in dem, was durch die Rasse vererbt ist. Darin haben Sie die Erklärung dafür, warum die Rasse dasjenige ist, was vererbbar ist, und wir werden verstehen, was die Geisteswissen­schaft zeigt: daß nur in der Vergangenheit die Rassenmerkmale durch den Ort hervorgebracht sind, an dem die Menschen geboren wurden. Das war in der letzten lemurischen und in der ersten atlantischen Zeit der Fall, als der Mensch direkt von der irdischen Umgebung abhängig war. In späterer Zeit beginnt die Rasse den Charakter zu haben, daß sie an die Vererbung gebunden ist und nicht mehr an den Ort. So sehen wir in der Rasse etwas, was ursprünglich an einen bestimmten Ort der Erde gebunden war und das sich dann in der Menschheit durch die Verer­bung fortpflanzte, aber vom Orte immer unabhängiger wurde.",
      "Aus dem, was ich jetzt gesagt habe, werden Sie erkennen, in welchem Zeitraume der Evolution es erst einen Sinn hat, von dem Rassenbegriff zu sprechen. Es hat keinen Sinn - im eigentlichen Sinne des Wortes -, vor der lemurischen Zeit von einem Rassenbegriff zu sprechen, denn in dieser Zeit steigt der Mensch erst auf die Erde herab.",
      "Vorher war er im Umkreis der Erde; dann kam er auf die Erde, und es vererbten sich die Rassenmerkmale in der atlantischen Zeit und bis herein in unsere nachatlantische Epoche. Wir werden sehen, wie in unserer Zeit die Volksmerkmale das sind, was die Rassencharaktere wieder auseinander bringt, was sie wieder auszulöschen beginnt.",
      "Das alles werden wir noch später sehen. Wir müssen uns jetzt nur hüten, die Welt so zu betrachten, als ob die Evolution nur wie ein Rad wäre, das anfangs- und endlos um sich herumrollte; die Vorstellung von dem rollenden Rad, die in man­cher mystischen Weltanschauung so breit ausgeführt wird, bringt eine furchtbare Verwirrung in den Begriff der eigentlichen Menschheits­evolution.",
      "Wenn man sich den Vorgang so vorstellt, daß sich alles sozusagen wie um ein bleibendes Zentrum herum bewegt, wobei es in so- und soviele Rassen gegliedert ist, dann hat man eigentlich keinen Begriff davon, daß alles sich in Entwickelung befindet, und daß auch die Rassen sich entwickeln. Die Rassen sind entstanden und werden einmal vergehen, werden einmal nicht mehr da sein.",
      "Sie wiederholen sich nicht etwa immer in der gleichen Art, wie es bei Sinnett falsch im «Esoterischen Buddhismus» dargestellt wird. In der alten lemurischen Zeit müssen wir das Aufgehen der Rassenmerkmale, der Rasseneigen­tümlichkeiten suchen; wir müssen dann deren Sich-Fortpflanzen bis in unsere Zeit verfolgen, müssen uns dabei aber klar sein, daß, wenn unsere gegenwärtige fünfte Entwickelungsepoche von der sechsten und siebenten abgelöst wird, keine Rede mehr sein kann von einem Zu­stande, den wir als Rasse werden bezeichnen können.",
      "Wenn wir uns diese Entwickelung aber so vorstellen, als ob sie immer nur gleichmäßig so fortrollte, dann haben wir nur eine Art Mühlrad im Kopfe, sind aber weit entfernt von dem Verständnisse dessen, was in der Welt wirklich vor sich geht.",
      "Wir sehen also, wie die Rassenentwickelung erst beginnt in der lemu­rischen Zeit durch das Hineinwirken der abnormen Geister der Form.",
      "Da lassen diese Geister die Kräfte unseres Erdenplaneten eingreifen an dem Orte, wo der Mensch seine erste Lebenszeit zu verbringen hat, und das überträgt sich in gewisser Weise auch wieder auf das spätere Leben, weil der Mensch ein Gedächtnis hat, durch das er sich erinnert an die eigentlich abnormerweise vor dem einundzwanzigsten Jahre auf der Erde zugebrachte Zeit auch in dem späteren Leben. Der Mensch würde ein ganz anderes Wesen sein, wenn nur die normalen Geister der Form wirkten. Durch die abnormen Geister der Form ist der Mensch abhän­gig von dem Punkte der Erde, auf dem er lebt. Die Abweichung von den Gesetzen der normalen Geister der Form ist auf die eben geschil­derte Weise entstanden, so daß bedeutsam wurde für den Menschen der Punkt der Erde, auf dem er in einer bestimmten Verkörperung lebt.",
      "Wir werden diese Verhältnisse noch genauer begreifen durch die folgende Betrachtung. Da können wir in gewisser Weise angeben, wie der Untergrund, der Bodengrund, sein Wesen nach oben strahlt und die menschliche Organisation durchdringt, so daß der Mensch abhängig wird von diesem Erdenuntergrund. In dieser Beziehung können wir also bestimmte Punkte der Erde angeben, die mit der menschlichen Wesenheit entwickelungsgeschichtlich zusammenhängen. Wir werden auf diese Verhältnisse noch genauer eingehen. Ich will sie jetzt in ab­stracto charakterisieren.",
      "Da haben Sie zum Beispiel (siehe Figur Seite 74) einen Punkt, der im Innern von Afrika liegt. An diesem Punkte wirken gleichsam von der Erde ausstrahlend alle diejenigen Kräfte, welche den Menschen namentlich während seiner ersten Kindheitszeit ergreifen können. Spä­ter wird der Einfluß solcher Kräfte auf den Menschen geringer; er ist dann diesen Kräften weniger ausgesetzt, aber sie prägen sich ihm mit dem, was aus ihnen kommt, doch in der stärksten Weise auf. So also wirkt jener Punkt auf der Erde, auf dem der Mensch lebt, am allerstärksten in der ersten Kindheitszeit und bestimmt dadurch diejenigen Menschen, die ganz abhängig sind von diesen Kräften, ihr ganzes Leben hindurch so, daß jener Punkt ihnen die ersten Kindheitsmerkmale blei­bend aufprägt. Das ist ungefähr eine Charakteristik aller derjenigen Menschen - in bezug auf ihren Rassencharakter -, die sozusagen um diesen Erdenpunkt herum die bestimmenden Kräfte aus der Erde heraus",
      "erhalten. Das, was wir schwarze Rasse nennen, ist im wesentlichen durch diese Eigenschaften bedingt.",
      "Wenn Sie nun weiter nach Asien hinübergehen, da haben Sie einen Punkt auf der Erdoberfläche, wo die späteren Jugendmerkmale dem Menschen aus den Erdenkräften heraus bleibend aufgedrückt werden, wo das, was die besonderen Eigenschaften des späteren Jugendzeitalters sind, aus der Erdenwesenheit heraus auf den Menschen übertragen wird und ihm den Rassencharakter gibt. Die hier in Betracht kommenden Rassen sind die gelben und bräunlichen Rassen unserer Zeit.",
      "Wenn wir dann weiter von Osten nach Westen gehen, so finden wir einen Punkt, der von Asien her gegen Europa zu liegt und der die spä­testen Merkmale, diejenigen Merkmale, die gerade in dem späteren, auf die erste Jugendzeit folgenden Lebensalter dem Menschen zukommen, dem Menschen bleibend aufdrückt' den Punkt, wo der Mensch nicht schon in der Kindheit von den Erdenkräften ergriffen wird, sondern dann, wenn die Jugend in das spätere Lebensalter übergeht.",
      "In dieser Art wird der Mensch von den Kräften ergriffen, die von der Erde aus bestimmend für ihn sind, so daß wir, wenn wir diese ein­zelnen Punkte ins Auge fassen, eine merkwürdig verlaufende Linie erhalten. Diese Linie besteht auch für unsere Zeit. Der afrikanische",
      "Punkt entspricht denjenigen Kräften der Erde, welche dem Menschen die ersten Kindheitsmerkmale aufdrücken, der asiatische Punkt den­jenigen, welche dem Menschen die Jugendmerkmale geben, und die reifsten Merkmale drückt dem Menschen der entsprechende Punkt im europäischen Gebiete auf. Das ist einfach eine Gesetzmäßigkeit. Da alle Menschen in verschiedenen Reinkarnationen durch die verschiedenen Rassen durchgehen, so besteht, obgleich man uns entgegenhalten kann, daß der Europäer gegen die schwarze und die gelbe Rasse einen Vorsprung",
      "hat, doch keine eigentliche Benachteiligung. Hier ist die Wahr­heit zwar manchmal verschleiert, aber Sie sehen, man kommt mit Hilfe der Geheimwissenschaft doch auf merkwürdige Erkenntnisse.",
      "Wenn wir dann diese Linie weiterziehen, so kommen wir weiter nach Westen nach den amerikanischen Gebieten hinüber, in jene Gebiete, wo diejenigen Kräfte wirksam sind, die jenseits des mittleren Lebensdrittels liegen. Und da kommen wir - ich bitte das nicht mißzuverstehen, was eben gesagt wird; es bezieht sich nur auf den Menschen, insofern er von den physisch-organisatorischen Kräften abhängig ist, von den Kräften, die nicht sein Wesen als Menschen ausmachen, sondern in denen er lebt -, da kommen wir zu den Kräften, die sehr viel zu tun haben mit dem Absterben des Menschen, mit demjenigen im Menschen, was dem letzten Lebensdrittel angehört. Diese gesetzmäßig verlaufende Linie gibt es durchaus; sie ist eine Wahrheit, eine reale Kurve, und drückt die Gesetzmäßigkeit im Wirken unserer Erde auf den Menschen aus. Diesen Gang nehmen die Kräfte, die auf den Menschen rassebestim­mend wirken. Nicht etwa deshalb, weil es den Europäern gefallen hat, ist die indianische Bevölkerung ausgestorben, sondern weil die india­nische Bevölkerung die Kräfte erwerben mußte, die sie zum Aussterben führten. Von der Eigentümlichkeit dieser Linie hängt das ab, was auf der Oberfläche unserer Erde mit den Rassen sich abspielt, was von den Kräften, die nicht unter dem Einfluß der normalen Geister der Form stehen, bewirkt wird. Wo Rassencharaktere in Betracht kommen, da wirken sie in dieser Weise. In unserer Zeit wird der Rassencharakter aber allmählich überwunden.",
      "So recht vorgebildet hat sich das schon in der allerfrühesten Erdenzeit. Wenn wir bis in die alte lemurische Zeit zurückgehen würden, so könnten wir die allerersten Ausgangspunkte der Rassenentwickelung in der Gegend des heutigen Afrika und Asien finden. Dann sehen wir später eine Herüberbewegung des Menschen nach der westlichen Rich­tung, und in der Verfolgung der rassebestimmenden Kräfte nach We­sten können wir dann das Absterben in den Indianern beobachten. Nach Westen mußte die Menschheit gehen, um als Rasse zu sterben. Um aufzufrischen die Menschheit mit neuer Jugendkraft, findet der Zug nach Osten statt, der Zug, der von Atlantis herüber über Europa nach",
      "Asien sich bewegt. Dann geschieht eine Wiederholung des Zuges nach dem Westen. Es wiederholt sich aber jetzt nicht die Bewegung der Rassen, sondern gleichsam eine höhere Stufe der Rassenentwickelung, die Entwickelung der Kulturen.",
      "In gewisser Weise kann man sehen, daß die Entwickelung der Kulturen durchaus den Charakter annimmt, der im Sinne einer Fortsetzung der Rassenlinie liegt. So haben wir zum Beispiel diejenige Kultur, welche wir auch schon in dieser Betrachtung mit genügender Bewunderung charakterisiert haben, die uralt-indische Kultur, die als erste nachatlantische Kultur erschien, zu bezeichnen als die dem ersten Kindesalter entsprechende Epoche, wo der Mensch in Beziehung auf die Wertschätzung der physischen Natur noch schläft, und in seine Seele wirken hinein die Offenbarungen einer geistigen Welt.",
      "In der Tat ist die erste, indische Kultur eine Offenbarung von oben, eine Offenbarung aus spirituellen Höhen, und sie konnte nur aus dem Grunde in die Menschen hineinwirken, weil der Mensch unter den Einfluß der indischen Erde kam, unter dem er in weit zurückliegender Zeit schon gestanden hatte. Damals in urferner Vergangenheit wurde der physische Rassecharakter aus der Erde heraus bestimmt; jetzt bei wiederholter Anwesenheit an demselben Erden-Orte wurde mehr eine Seelenbeschaffenheit, die des altindischen Menschen bestimmt.",
      "Durch den Zug von Westen nach Osten ist eine solche Jugendfrische aufge­treten, daß durch diesen Vorgang die eigentümliche Geisteskonfigura­tion hervorgehen konnte, welche die ursprüngliche indische Kultur charakterisiert. Sie werden sehen, daß eine sehr alte indische Kultur, die noch nicht erforscht worden ist, und von der nur ein Abkömmling ist, was heute die Wissenschaft indische Kultur nennt, in dieser Weise ihre Erklärung findet, nämlich dadurch, daß die atlantische Kultur sich in gewisser Beziehung in der uralt-indischen wiederholt.",
      "Wenn wir nunmehr die Kulturen, die sich in der nachatlantischen Zeit gefolgt sind, betrachten, so können wir sehen, daß sie die aufein­anderfolgende Wiederholung früherer im physischen Leibe durchge­machter, aber wieder durch Verjüngung ganz anders gewordener Ver­hältnisse darstellen. So sehen wir in der persischen Kultur eine solche, welche in gewisser Weise mit dem zusammenhängt, was wir nennen können ein Sich-Durchringen desjenigen Menschen, der vorzugsweise",
      "in der ersten menschlichen Lebenskraft lebt, wo er noch den Einflüssen der abnormen Geister der Form hingegeben ist, mit den Kräften, die von den normalen Geistern der Form stammen. Dieser Gegensatz ist in der persischen Kultur in dem Bewußtsein und in der Gestalt von Licht und Finsternis, von Ormuzd und Ahriman enthalten.",
      "Je weiter wir herüber kommen nach Westen, desto mehr sehen wir, wie die Eigenschaften eines reiferen Alters der Kultur aufgedrückt werden. Wenn wir auch zugeben müssen, daß bis zur heutigen Gegen­wart die Schöpfungen der Menschen in höherem Grade noch abhängig sind von den abnormen Kräften und Wesenheiten des Weltalls, so werden wir es doch begreiflich finden, wenn gesagt wird, daß nicht mehr ausschließlich mit Eigenschaften der Rasse die Menschen nach Westen gehen. Auch können wir verstehen, daß in gewisser Weise der Zug der Kultur ein solcher ist, daß die volle Jugendfrische der Kultur, das produktive Element derselben immer mehr erstirbt, je weiter sie nach Westen kommt.",
      "Wer objektiv betrachtet, kann aus vielen Verhältnissen ersehen, daß auch unsere Zeitkultur in dieser Weise gesetzmäßig bestimmt ist. Man ist aber nicht geneigt, objektiv zu sehen. Wenn Sie aber das, was sich ergibt, betrachten, das betrachten, daß in der Tat alle Kultur im Flusse ist, da sehen Sie, daß, je weiter wir nach Westen kommen, die Kultur immer unproduktiver wird. Sie nähert sich also als Kultur dem Abster­ben. Je weiter nach Westen, desto mehr werden nur die äußeren Teile der Kultur blühen, die, welche nicht Auffrischung durch Jugendkraft erleben, sondern sich in gewisser Weise in das Greisenhafte hinein ausleben. Daher wird der Mensch im Westen für die Menschheit noch Großes und Gewaltiges leisten können in bezug auf physikalische, chemische und astronomische Entdeckungen, für alles, was unabhängig ist von der erfrischenden Jugendkraft. Das aber, was produktive Kraft benötigt, das braucht in der Tat eine andere Konfiguration der auf den Menschen wirkenden Kräfte.",
      "Nehmen wir an, der Mensch wächst von der Kindheit bis zu einer gewissen Stufe; dann erblüht eigentlich erst sein Geistiges. Zuerst ist der Mensch ein physisch wachsendes Wesen. Es muß sich das, was bei einem kleinen Knirps in einem engen Raume zusammengedrängt ist,",
      "erst physisch ausdehnen. Dann wird die Menschenbildung in das Innere zusammengedrängt. - So ist es aber auch mit der Menschheit im großen. Wir sehen ein eigentümliches Gesetz, wenn wir die charakterisierte Kurve verfolgen. Wir finden es sogar in den Kontinenten ausgedrückt. Wir sehen, daß zunächst eine Art ursprünglicher Anfangspunkt der physischen Menschenentwickelung in Afrika vorliegt, daß dann der Raum, auf dem sich die Menschheit ausbildet, sich ins Weite ausdehnt. Das finden wir dann in den weiten Flächen der asiatischen Bildung. Große, mächtige Flächen bewohnt der Mensch da.",
      "Schauen wir nun auf die Wiederholung der Rassenbildung in den nachatlantischen Kulturen. Wie der Mensch in der Jugend gleichsam neugierig mit den Augen hinschaut in die Umgebung, so blickt der Mensch der alten indischen Kultur in die Welt. Das hängt durchaus mit den jugendfrischen Kräften zusammen, die den Menschen ausdehnen und in seinem Wachstum in die Weite organisieren. Dann muß das Geistige beginnen und muß sich das Physische zusammendrängen; da sehen wir, daß, indem die Kultur in Europa fortschreitet, in merkwür­diger Weise der Raum, auf dem diese Menschheit ausgebreitet ist, zu­sammengedrängt wird in kleinere Dimensionen. Wir sehen, daß Europa der kleinste Erdteil ist, und je weiter der Mensch nach Westen fort­schreitet, desto mehr strebt er nach einem Zusammendrängen. Er strebt in Halbinseln hinaus ins Meer und schnürt sich immer mehr zusammen nach dem Westen hin.",
      "Dies hängt alles mit dem geistigen Gang der Entwickelung zusam­men. Sie sehen hier in eigenartiger Weise in die Mysterien der geistigen Entwickelung hinein. Aber mit dem Zusammendrängen nach Westen hin ist eine Krisis gegeben. Da ist eine Krisis, durch welche ein mehr unproduktives Element zu wirken beginnt. Die Produktivität stirbt in den Halbinselgebieten nach dem Westen hin in einer gewissen Weise ab. Diese Unproduktivität zeigt sich in dem, was vorhin charakterisiert worden ist, daß nämlich sozusagen selbst die Kultur, je weiter sie nach Westen geht, ein starres, greisenhaftes, nach dem Absterben hin gehen­des Element annimmt. Das ist etwas, was in den Geheimschulen immer bekannt war. Sie werden nun begreifen, daß ich sagte, das, was ich mitteilen werde, könnte etwas gefährlich werden, weil die Menschen",
      "entrüstet werden könnten. Und es darf noch lange nicht alles gesagt werden, was dazu diente, den Menschen in bezug auf die höheren Ge­biete seines Wesens unabhängig zu machen, damit er wahrnimmt, was aus der Erde rassebestimmend aufsteigt, was später den Kulturcharak­ter bestimmt, und was in noch späterer Zeit wieder unbedeutend wer­den wird, wenn der Mensch zum Geistigen wieder zurückkehrt.",
      "Sie werden daher begreifen, daß mit diesem ganzen Gang der Menschheits­entwickelung der Gang der geistigen Entwickelung, den diejenigen immer gekannt haben, die tiefer in die Geheimnisse des Daseins einge­weiht waren, zusammenhängt. Die Richtigkeit des Gesagten hängt nicht davon ab, ob man für das eine mehr, für das andere weniger begeistert ist; die hängt von der Notwendigkeit in der Entwickelung ab.",
      "Wer gegen die Notwendigkeit sprechen würde, der könnte nichts erreichen. Gegen sie sprechen, heißt ihr Hindernisse in den Weg schie­ben. Daher ist es nur natürlich, daß in gewisser Weise die Menschen, die in das Gebiet ziehen, das mehr nach Westen liegt, sich eine Auffrischung wieder vom Osten holen müssen, einen Einschlag vom Osten erhalten müssen, daß aber das mitteleuropäische Gebiet sich auf die eigene Pro­duktivität, wie sie vor der Halbinselbildung bestanden hat, besinnen muß.",
      "Das ist der Grund, warum in Europa gerade - ich meine in dem Strich, der unser gemeinsames Gebiet umfaßt: Skandinavien und Deutschland - die Menschen sich auf ihr eigenes Seelisches besinnen müssen, und warum dagegen gerade im Westen aufgesucht werden muß der Teil der Menschheit, der etwas von Osten übertragen erhalten soll. Das ist tief durch den Gesamtcharakter der Erdenmenschheit bedingt.",
      "Sie sehen, daß selbst in der geisteswissenschaftlichen Entwickelung das sich noch wiederholt. Auch tritt uns das entgegen in der vierten nachatlantischen Kultur bei dem Römer- und Griechentum. Es ist Tatsache, daß die Römer in gewisser Beziehung weiter sind als die Griechen, daß sie aber von dem von ihnen eroberten Volke, welches weiter östlich wohnt, das Geistesleben nehmen.",
      "Das hier zutage tretende Gesetz wird immer mehr und mehr sich bewahrheiten, je weiter die Gebiete nach Westen gelegen sind. Diese großen Wahrheiten kann man im Grunde genommen nur andeutungs­weise sagen. Sie geben uns dasjenige, was dem inneren Charakter",
      "unserer Mission für jedes Stück der Erdoberfläche entspricht. Sie sehen, daß wir begreifen müssen dasjenige, was wir zu tun haben, um uns zu dem Gemeinsamkeitscharakter der Menschheit zu erheben. Da liegt die große Verantwortlichkeit, die man hat, wenn man eingreifen will in die große Bewegung der Menschheit. Wo die große Bewegung der Mensch­heit in Betracht kommt, da darf keine persönliche Sympathie und kein persönlicher Enthusiasmus mitspielen. Denn nicht darauf kommt es an, sondern darauf, was in den großen Gesetzen des Menschentums bedingt ist. Das muß man aus den großen Gesetzen heraus erkennen und sich nicht beeinflussen lassen durch Voreingenommenheit für dieses oder jenes. So ist im Grunde genommen der Charakter des ganzen Rosen­kreuzertums. Rosenkreuzertum ist, zu wirken im Sinne der ganzen Menschheitsentwickelung. Wenn man den Boden, auf dem man steht, erkennt bis zur Insel- und Halbinselbildung, dann wird man fühlen, welche Empfindung einen überkommen muß, wenn man im Sinne der Menschheitsentwickelung wirken will.",
      "Einstmals wurde der Mensch durch die abnormen Geister der Form heruntergeführt auf die Erde, gebunden an die verschiedenen Punkte der Erdoberfläche; dadurch wurde die Grundlage der Rassenentwickelung geschaffen. Dann aber sehen wir immer mehr die Rassen sich vermischen. Wir sehen eingreifen in die Rassenentwickelung, das heißt sich aus ihr erheben die Volksentwickelung. Wir sehen sie hineingreifen bis in die Entwickelung des einzelnen Menschen. Es ist ein großes My­sterium damit ausgesprochen, wenn man etwa sagt: Wer war Plato in bezug auf seine äußere Wesenheit, in bezug auf das Hineingeborensein in die Menschheit? Das war ein Mensch, der hineingewachsen war in das Geschlecht der Soloniden, angehörte dem Stamme der Ionier, dem Volke der Griechen, der ganzen kaukasischen Rasse. - Das Verstehen, daß Plato ein Solonide, ein Ionier, ein Grieche, ein Kaukasier war, das spricht, wenn man es in seiner Gesetzmäßigkeit durchschaut, ein tiefes Mysterium aus. Es spricht das Mysterium aus, das uns zeigt, wie auf der weiten Basis des ganzen Erdenplaneten zusammenwirken die normalen und abnormen Geister der Form, die eigentlich das größte Interesse daran haben, den Menschen zum Erdenmenschen zu machen. Es spricht sich darin aus, wie sich durch dieses Zusammenwirken das Menschentum",
      "spezifiziert, wie dann die anderen Wesenheiten eingreifen, von denen wir bei der Charakteristik der einzelnen Völkerschaften schon gesprochen haben. Jeder Mensch ist mit seiner Wesenheit an den Vor­gängen beteiligt, durch die alle die höheren Wesenheiten, diese höheren Geister zusammenwirkend die Weltentwickelung gestalten.",
      "Man versteht den einzelnen Menschen nicht, wenn man nicht sieht, wie er in seiner Gesamtentwickelung dadurch, daß diese Wesenheiten zusammenwirken, geworden ist. Dadurch, daß auf unserem Erdenpla­neten durch das geheimnisvolle Zusammenwirken der Geister der Form, die die normale Entwickelung durchgemacht haben, und der Geister der Form, die die abnorme Entwickelung durchgemacht haben, einmal eine kaukasische Rasse geschaffen wurde, dadurch wurde der Grund und Boden dafür geschaffen, daß ein Plato überhaupt werden konnte. Dadurch, daß wir die abnormen und normalen Erzengel bis zu den Engeln eingreifen sehen, sehen wir den Weg, der notwendig war, um einen Plato hervorzubringen, der uns als menschliche Wesenheit, mit menschlichem Antlitz, mit ganz bestimmten Verstandes-, Gefühls- und Willenseigenschaften entgegentreten konnte. Zwischen der Rasse und der Individualität liegt das Volkstum mitten darinnen.",
      "Darum mußten wir heute die Grundbedingungen der Rasse im allge­meinen charakterisieren. Morgen wollen wir das Herauswachsen des Volkstumes aus den Rassen, das Eingreifen anderer Geister der Hierar­chien und insbesondere deren Eingreifen in das Wirken der Geister der Form betrachten."
    ],
    "sentences": [
      [
        "Will man zu dem Verhältnis der Menschenrassen zu einander vordrin­gen, welche ja die Grundlage sind, aus welcher sich die einzelnen Volksgemeinschaften herausheben, dann muß man berücksichtigen, daß der Mensch, den wir vor uns haben, der wir selber sind, eigentlich ein recht kompliziertes Wesen ist und nur durch das Zusammenwirken vieler, vieler Wesenheiten des Weltalls in seiner heutigen Form und Wesenheit hat entstehen können.",
        "Wir wissen ja aus der Betrachtung der «Akasha-Chronik» und aus anderen Betrachtungen, die über die Entwickelung des Menschen gepflogen worden sind, daß unsere Erde selbst früher - bevor sie den jetzigen Zustand erreicht hat - drei Zustände hat durch­machen müssen."
      ],
      [
        "Im Verlaufe dieser drei Zustände sind nach und nach veranlagt und bis zu ihrem heutigen Grade ausgebildet worden die drei sogenannten Glieder des Menschen: der physische Leib, der Äther- oder Lebensleib und der Astralleib.",
        "Während der jetzigen Erdenverkörpe­rung ist erst der Mensch fähig geworden, ein viertes Glied, ein Ich in sich aufzunehmen."
      ],
      [
        "Diese vier Glieder seiner Wesenheit zeigen uns alles das, was durch die drei oder vier Verkörperungen unserer Erde hin­durch geschehen ist, durch die Verkörperung als Saturn, Sonne, Mond und durch die Erdenzeit selbst, soweit sie bis jetzt verlaufen ist.",
        "Wenn Sie vorüberziehen lassen vor Ihrem Blick alle die Wesenheiten, die da zusammengewirkt haben, diese Geister des Willens oder Throne' die Geister der Weisheit, Geister der Bewegung, Geister der Form, Geister der Persönlichkeit, Erzengel, bis herunter zu den Engeln, und über den Geistern des Willens oder Thronen die Cherubime und Seraphime, so werden Sie sich sagen können, daß aus einem ganz komplizierten Zu­sammenwirken erst hervorgehen konnte, was des Menschen heutige Organisation möglich macht."
      ],
      [
        "Wir haben gesehen, daß nicht nur not­wendig war, daß so viele Wesenheiten und Naturkräfte zusammenwirkten im Kosmos, sondern daß zum Zustandekommen des Menschen auch noch nötig war, daß zu gewissen Epochen gewisse Wesenheiten auf den normalen Gang ihrer Entwickelung verzichteten, zurückgeblieben"
      ],
      [
        "sind, so daß sie in anderer Weise, als es bei ihrem normalen Entwickelungsgange möglich gewesen wäre, in die menschliche Orga­nisation eingreifen konnten."
      ],
      [
        "Also wir sehen in ein wunderbar vielgestaltiges und mannigfaltiges Gewebe hinein, wenn wir den Menschen, so wie er uns heute vor Augen tritt, eigentlich verstehen wollen.",
        "Wir müssen uns auch klar sein darüber, daß wir nur dann, wenn wir gewissermaßen dieses Gewebe aus­einanderhalten und die einzelnen Wesen in ihrer Tätigkeit belauschen, verstehen lernen, wie durch das Zusammenwirken dieser Wesenheiten der Mensch erst zustande gekommen ist."
      ],
      [
        "Da können wir nun sagen: Die hauptsächlichste Wesenheit, welche für den heutigen Menschen in Betracht kommt, ist diejenige, welche ihm die Möglichkeit gegeben hat, zu sich «Ich» zu sagen, nach und nach zu dem Bewußtsein des Ich zu kommen.",
        "Und wir wissen, daß diese Möglichkeit zuerst von den Gei­stern der Form, von denjenigen Wesenheiten gegeben worden ist, die wir Gewalten, Exusiai nennen."
      ],
      [
        "Wenn wir gerade diese Wesenheiten bei ihrer Tätigkeit, welche sie dem Menschen zuwenden, belauschen und uns gewissermaßen fragen: Wie würde es mit dem Menschen werden, wenn bloß diese Wesenheiten, und zwar nur diejenige Art dieser Wesen­heiten, die in normaler Entwickelung sich befindet, in der Hauptsache im Menschen tätig wäre? - so werden wir finden: Sie sind die Verleiher der Ich-Organisation.",
        "Damit ist aber schon gesagt, daß sie eigentlich, wenn wir sie ihrer eigenen Natur nach betrachten, ihr Hauptinteresse daran haben, den Menschen zu seinem Ich zu bringen."
      ],
      [
        "Nun aber ist das, was diese Wesenheiten eigentlich im Menschen zu verrichten haben, im heutigen Menschenleben erst in einem bestimmten Lebensalter aktuell, tritt erst in einem bestimmten Lebensalter zutage."
      ],
      [
        "Wenn Sie sich an das erinnern, was über die Erziehung des Kindes vom Standpunkte der Geisteswissenschaft gesagt worden ist, so werden Sie sich sagen: Der Mensch entwickelt hauptsächlich zwischen seiner physischen Geburt und dem Zahnwechsel, also bis zum siebenten Jahre hin, den physischen Leib.",
        "An der Entwickelung dieses physischen Leibes haben diese Geister der Form gar kein besonderes Interesse, denn diese ist im Grunde genommen eine Wiederholung dessen, was auf dem alten Saturn mit dem Menschen geschah, was sich schon oftmals wiederholt"
      ],
      [
        "hat, und was sich nach der letzten physischen Geburt bis zum siebenten Lebensjahre vorläufig zum letzten Male in einer besonderen Art wie­derholt hat.",
        "Dann kommt die Zeit vom siebenten bis zum vierzehnten Jahre, also bis zur Geschlechtsreife."
      ],
      [
        "Auch das ist eine Zeit, an der die Geister der Form kein besonderes Interesse haben; es ist eine Wieder­holung der alten Sonnenzeit, und die Geister der Form wollten eigent­lich mit ihrer Haupttätigkeit, mit der Verleihung des Ich, erst im Zustande des Erdenlebens eingreifen.",
        "Wir kommen dann zu dem dritten Lebensalter, das zwischen dem fünfzehnten und dem ein- oder zwei­undzwanzigsten Lebensjahre abläuft."
      ],
      [
        "In dieser Zeit wird der Astralleib, der in normaler Weise der Mondentwickelung zugehört, wiederholent­lich entwickelt im Menschen.",
        "Da haben die Geister der Form, die sich normal entwickeln, noch immer kein Interesse am Menschen, so daß wir sagen müssen: Die drei Lebensalter des Menschen, die der eigent­lichen Geburt des Ich vorangehen, die erst um das zwanzigste Jahr herum eintritt, bieten kein unmittelbares Interesse für die Geister der Form."
      ],
      [
        "Sie greifen - man möchte sagen, aus ihrer eigenen Natur heraus - erst um das zwanzigste Lebensjahr herum ein, so daß, wenn Sie das bedenken, Sie es nicht mehr so ganz sonderbar finden werden, wenn gesagt wird: Nach der eigentlichen Intention der Geister der Form würde der Mensch erst in dem Zustande, in welchem er sich um das zwanzigste Lebensjahr herum befindet, da zu sein brauchen.",
        "Das, was sich im Menschen bis dahin entwickelt, ist im Grunde genommen für diese Geister der Form eine Art Embryonal-, eine Art Keimzustand."
      ],
      [
        "Und wenn ich etwas bildlich sprechen darf, so möchte ich sagen: Den Geistern der Form, welche sich normal entwickelt haben, wäre es am liebsten, wenn alles mit einer gewissen Regelmäßigkeit herginge, wenn ihnen bis dahin niemand ins Handwerk pfuschte.",
        "Wenn niemand diesen Geistern der Form bis zum zwanzigsten Jahre dazwischen käme, so würde der Mensch während der ersten sieben Jahre der Entwickelung das Bewußtsein haben, das dem physischen Leibe zukommt; das ist nämlich ein sehr dumpfes Bewußtsein, wie es die Mineralwelt hat."
      ],
      [
        "Im zweiten Stadium - in der Zeit vom siebenten bis zum vierzehnten Jahre - würde er ein Schlafbewußtsein haben.",
        "Vom vierzehnten bis zwanzigsten Jahre würde er in intensiver Weise im Inneren wirksam"
      ],
      [
        "sein, aber eine Art von Traumdasein führen.",
        "Nach diesem Bewußtsein als Mondenwesenheit, etwa im einundzwanzigsten Jahre, würde der Mensch erst eigentlich erwachen.",
        "Da würde er erst zu dem Ichbewußt­sein kommen.",
        "Wenn es nach der normalen Entwickelung ginge, dann würde er da erst aus sich herausgehen und die Außenwelt in dem Weltbilde überblicken, das heute unser bekanntes Weltbild ist."
      ],
      [
        "So also sehen Sie, daß im Grunde genommen, wenn wir nur die Tätigkeit der Geister der Form in Betracht ziehen, der Mensch sehr verfrüht zu seinem Bewußtsein kommt, wie er es heute hat, denn Sie wissen, daß dieses Bewußtsein beim heutigen Menschen in gewissem Grade bald nach der physischen Geburt erwacht.",
        "Es würde nicht in der Form erwachen, daß es klar und deutlich die physische Außenwelt sieht, wenn nicht andere Geister, die eigentlich Geister der Bewegung sind, zurückgeblieben wären und verzichtet hätten auf die Entwicke­lung gewisser Fähigkeiten, die sie bis zur Erdenentwickelung hätten erlangen können, wenn sie nicht stehengeblieben wären in ihrer Ent­wickelung, so daß sie jetzt während der Erdenentwickelung in die Entwickelung des Menschen in besonderer Weise eingreifen können."
      ],
      [
        "Weil sie ihre Entwickelung in einer anderen Weise durchgemacht haben, sind sie in der Lage, dem Menschen schon früher das beizubringen, was er erst um das zwanzigste Jahr herum erringen sollte.",
        "So also sind das geistige Wesenheiten, welche verzichtet haben auf die Möglichkeit, ihre Entwickelung bis zur Erdenentwickelung in normaler Weise weiter­zutreiben, geistige Wesenheiten, die während der Erdenentwickelung Geister der Bewegung hätten sein können, die aber stehen geblieben sind auf der Stufe der Geister der Form und die nun in der Erdenentwickelung als Geister der Form wirken."
      ],
      [
        "So können sie während der Erdenentwickelung dem Menschen, der eigentlich noch gar nicht reif ist dazu und der manches aus der früheren Zeit noch nachzuholen hat, das verleihen, was die normale Entwickelungsform erst um das zwan­zigste Jahr herum verleihen würde.",
        "So tritt der Mensch in das Dasein und erhält von den abnormen Geistern der Form Fähigkeiten, die er sonst erst um das zwanzigste Jahr herum erhalten würde."
      ],
      [
        "Das alles hat ganz bedeutsame Folgen.",
        "Denken Sie sich einmal, es wäre nicht so.",
        "Wenn es nicht so wäre, wenn diese Geister mit abnormer"
      ],
      [
        "Entwickelung nicht eingreifen würden, dann würde der Mensch über­haupt erst für die physische Welt in Betracht kommen in dem Zustande, den er um das zwanzigste Jahr herum hat, das heißt, er müßte in diesem Zustande als physisches Wesen geboren werden, er müßte ganz andere Keimzustände durchmachen.",
        "In der Tat wird durch diese abnormen Gei­ster der Form die menschliche Entwickelung schon von der Geburt an bis zum zwanzigsten Jahre in die physische Welt hinausgestellt; das ist ungefähr das erste Drittel unseres Erdenlebens.",
        "Wir müssen also sagen:"
      ],
      [
        "Das erste Drittel unseres Erdenlebens wird nicht durch die den Erdenzustand beherrschenden geistigen Wesenheiten, sondern durch andere, abnorme geistige Wesenheiten regiert, und weil diese teilnehmen an der Entwickelung, so haben wir Menschen auch nicht die Gestalt, die wir hätten, wenn wir in dem Zustande geboren würden, den wir um das zwanzigste Jahr herum haben.",
        "Das muß der Mensch damit bezahlen, daß er ein Drittel seines Lebens - die Zeit bis zu seinem zwanzigsten Jahre hin - so zubringt, daß er dem großen Einfluß dieser abnormen Wesenheiten hingegeben ist.",
        "Sein ganzes Wachstum macht der Mensch eigentlich unter den Einflüssen der abnormen Wesenheiten durch.",
        "Er muß es dadurch bezahlen, daß, nachdem das mittlere Drittel abgelaufen ist - das im Grunde nur den normalen Geistern der Form gehört -, die absteigende Bahn, ein Zurückgehen beginnt, und seine Äther- und Astralorganisation zerfallen, so daß das Leben in drei Glieder oder Abteilungen zerfällt: in ein aufsteigendes, ein mittleres und ein abstei­gendes Drittel.",
        "In dem mittleren Teil wird der Mensch während seines Erdenlebens eigentlich erst Mensch, und im letzten Drittel muß er das zurückgeben, was er während des ersten, aufsteigenden Drittels em­pfangen hat, muß er die entsprechende Abschlagszahlung leisten."
      ],
      [
        "Wäre der Mensch in der Tat ausschließlich den Einflüssen der nor­malen Geister der Form hingegeben gewesen, dann würde alles das, was heute bis ins zwanzigste Jahr hinein geschieht, ein ganz anderes Antlitz, eine ganz andere Gestalt haben.",
        "Es wäre alles ganz anders verlaufen, so daß alles das, was mit des Menschen heutiger Entwickelung zusam­menhängt in der ersten der drei Lebensepochen, im Grunde genommen ein Dasein ist, das vieles von den späteren Lebensepochen vorausnimmt.",
        "Dadurch ist der Mensch bis zu der zweiten Epoche seines Lebens ein"
      ],
      [
        "materielleres Wesen geworden, als er sonst geworden wäre.",
        "Der Mensch hätte sonst bis zu diesem Momente seines Lebens nur geistige Zustände durchgemacht und würde bis zur jetzigen materiellen Verdichtung erst herabgestiegen sein in dem Zeitpunkte der Entwickelung, den er erst im zwanzigsten oder einundzwanzigsten Lebensjahre durchmacht, wo er sich selber an die Erde gebunden vorfände.",
        "Es sagt uns also die Geisteswissenschaft, daß, wenn diese Entwickelung so vorwärts gegan­gen wäre, der Mensch erst in dem Zustande so recht eigentlich auf die Erde herabgestiegen wäre, den er heute im zwanzigsten oder einund­zwanzigsten Lebensjahre erreicht; er würde die vorangehenden Zu­stände nicht auf der Erde haben durchmachen können.",
        "Er hätte sie erhöht über der Erde, im Umkreis der Erde durchmachen müssen.",
        "Und jetzt begreifen Sie den ganzen Gang der menschlichen Kindheit und Jugendentwickelung.",
        "Wir können sehen, wenn wir diese gerade Linie"
      ],
      [
        "B-C als Erdenweg bezeichnen, so wären es die Geister der Form, die den Menschen dazu bestimmt hätten, herunterzusteigen erst in diesem Punkte, (20/21 der Zeichnung).",
        "Hier würde der Mensch also erst die Erde erreicht haben, und er würde wieder hinaufsteigen nach dem vierzigsten Jahre und das letzte Drittel seines Lebens in einem vergeistigten Zustande durchmachen.",
        "Durch die abnormen Wesenheiten wurde der Mensch gedrängt, schon hier (bei A der Zeichnung) herabzusteigen und das Leben auf der Erde aufzunehmen.",
        "Das ist das Ge­heimnis unseres Daseins.",
        "So sehen wir, daß wir durch die uns eigentlich dirigierenden normalen Wesenheiten nur in dem mittleren Drittel unse­res Lebens ganz beherrscht sind, während unsere Wachstums- und unsere Niedergangsperiode unter dem Einfluß ganz anderer Wesen­heiten stehen, die in irgendeiner Weise auf ihre normale Entwickelung verzichtet haben."
      ],
      [
        "Wenn das alles so geworden wäre, wie es nicht geworden ist, wenn der Mensch erhöht im Umkreis der Erde das erste und dritte Drittel seines Lebens durchgemacht und nur im mittleren Teile die Erde be­rührt hätte, also im Grunde genommen ein ganz anderes Wesen gewor­den wäre, dann würde der Mensch nicht in dem Grade an die Erde gebunden sein, in dem er tatsächlich heute an dieselbe gebunden ist.",
        "Wenn das eingetreten wäre, dann würden alle Menschen, welche die Erde betreten, von gleicher Gestalt und Wesenheit sein; dann würden alle Menschen, die über die Erde hingegangen sind, gleichgestaltet gewesen sein."
      ],
      [
        "Eine Menschheit gäbe es nur.",
        "Dasjenige, was uns zu einem solchen Wesen macht, daß sich daraus die spezifischen Eigenschaften der Rassen ergeben, die im Menschentum zum Ausdruck kommen, das ist nicht im mittleren Drittel des Lebens enthalten."
      ],
      [
        "Durch alles das, was in der Zeit vorher liegt, was im ersten Drittel des Lebens sich vollzieht, sind wir mehr mit allen unseren Kräften an die Erde gebunden, als es die normalen Geister der Form für uns bestimmt haben.",
        "Dadurch aber ist der Mensch mehr von der Erde, auf der er lebt, abhängig geworden, als er es sonst geworden wäre."
      ],
      [
        "Er ist abhängig geworden von dem Orte der Erde, auf dem er lebt.",
        "Dadurch, daß der Mensch - sozusagen gegen die Intentionen der Geister der Form - früher auf die Erde herunter­steigt, wird er abhängig von dem Orte, weil er sich in einem Zustande mit der Erde verbindet, der ihm gar nicht vorgezeichnet ist."
      ],
      [
        "Unab­hängig wäre der Mensch geworden davon, ob er im Norden oder Süden, im Osten oder Westen die Erde betreten hätte, wenn er sie nur im mittleren Drittel seines Lebens betreten hätte.",
        "Dadurch aber, daß er abhängig wird von der Erde, dadurch, daß er eine Jugend durchmacht in der Weise, wie wir es charakterisiert haben, wird er erdgebunden, wird er ein mit dem Gebiete, auf dem er geboren ist, zusammenhängen­des, zu ihm gehörendes Wesen."
      ],
      [
        "Dadurch wird er abhängig von all den Verhältnissen der Erde, die diesem Orte zugehören, von dem Einfallen der Sonnenstrahlen, von dem Umstand, ob die Gegend nahe dem Äqua­tor in der heißen Zone oder in einem mehr gemäßigten Gebiete sich befindet, ob er auf einem niedrig gelegenen Gebiet oder auf einem Hochplateau geboren ist.",
        "Man atmet ja ganz verschiedenartig in der Ebene oder im Gebirge."
      ],
      [
        "Der Mensch wird also ganz abhängig von den"
      ],
      [
        "irdischen Verhältnissen, von dem Ort, an dem er geboren ist.",
        "So sehen wir, daß der Mensch förmlich mit seiner Erdenmutter zusammenge­wachsen ist dadurch, daß er so eng zusammenhängt mit dem Orte, mit dem Gebiete der Erde, auf dem er jeweils geboren wird, und daß er bestimmt wird durch diejenigen Eigenschaften, die er dadurch erhält, daß diese Kräfte der Erde, die durch den betreffenden Ort bestimmt sind, in ihm wirken.",
        "Das alles bestimmt seinen Rassencharakter, und auf diesem Umwege sind die abnormen Geister der Form - diejenigen Gei­ster der Form oder Gewalten, die zu einer anderen Zeit als zwischen dem einundzwanzigsten bis dreiundzwanzigsten Jahre dem Menschen das geben, was wir heutiges Erdenbewußtsein nennen - die Verursacher der Rassenverschiedenheit des Menschen über die ganze Erde hin, die also von dem Orte auf der Erde abhängt, auf dem der Mensch geboren wird."
      ],
      [
        "Nun erlangt der Mensch während dieser Zeit - die also im Grunde genommen unter der Herrschaft der abnormen Geister der Form steht - auch die Möglichkeit, die Fähigkeit, seinesgleichen hervorzubringen.",
        "Auch diese Fähigkeit wird während der Zeit erworben, in welcher der Mensch gar nicht rein von den normalen Geistern der Form dirigiert wird.",
        "Dadurch ist die Möglichkeit gegeben, daß der Mensch nicht nur in der geschilderten Weise abhängig wird von dem Orte, auf dem er geboren ist, sondern daß die Eigenschaften, die er dadurch erhält, auch auf seine Nachkommen vererbt werden können, daß also die Rassenzusammengehörigkeit nicht nur sich ausspricht in den Einflüssen des Wohnplatzes, sondern auch in dem, was durch die Rasse vererbt ist.",
        "Darin haben Sie die Erklärung dafür, warum die Rasse dasjenige ist, was vererbbar ist, und wir werden verstehen, was die Geisteswissen­schaft zeigt: daß nur in der Vergangenheit die Rassenmerkmale durch den Ort hervorgebracht sind, an dem die Menschen geboren wurden.",
        "Das war in der letzten lemurischen und in der ersten atlantischen Zeit der Fall, als der Mensch direkt von der irdischen Umgebung abhängig war.",
        "In späterer Zeit beginnt die Rasse den Charakter zu haben, daß sie an die Vererbung gebunden ist und nicht mehr an den Ort.",
        "So sehen wir in der Rasse etwas, was ursprünglich an einen bestimmten Ort der Erde gebunden war und das sich dann in der Menschheit durch die Verer­bung fortpflanzte, aber vom Orte immer unabhängiger wurde."
      ],
      [
        "Aus dem, was ich jetzt gesagt habe, werden Sie erkennen, in welchem Zeitraume der Evolution es erst einen Sinn hat, von dem Rassenbegriff zu sprechen.",
        "Es hat keinen Sinn - im eigentlichen Sinne des Wortes -, vor der lemurischen Zeit von einem Rassenbegriff zu sprechen, denn in dieser Zeit steigt der Mensch erst auf die Erde herab."
      ],
      [
        "Vorher war er im Umkreis der Erde; dann kam er auf die Erde, und es vererbten sich die Rassenmerkmale in der atlantischen Zeit und bis herein in unsere nachatlantische Epoche.",
        "Wir werden sehen, wie in unserer Zeit die Volksmerkmale das sind, was die Rassencharaktere wieder auseinander bringt, was sie wieder auszulöschen beginnt."
      ],
      [
        "Das alles werden wir noch später sehen.",
        "Wir müssen uns jetzt nur hüten, die Welt so zu betrachten, als ob die Evolution nur wie ein Rad wäre, das anfangs- und endlos um sich herumrollte; die Vorstellung von dem rollenden Rad, die in man­cher mystischen Weltanschauung so breit ausgeführt wird, bringt eine furchtbare Verwirrung in den Begriff der eigentlichen Menschheits­evolution."
      ],
      [
        "Wenn man sich den Vorgang so vorstellt, daß sich alles sozusagen wie um ein bleibendes Zentrum herum bewegt, wobei es in so- und soviele Rassen gegliedert ist, dann hat man eigentlich keinen Begriff davon, daß alles sich in Entwickelung befindet, und daß auch die Rassen sich entwickeln.",
        "Die Rassen sind entstanden und werden einmal vergehen, werden einmal nicht mehr da sein."
      ],
      [
        "Sie wiederholen sich nicht etwa immer in der gleichen Art, wie es bei Sinnett falsch im «Esoterischen Buddhismus» dargestellt wird.",
        "In der alten lemurischen Zeit müssen wir das Aufgehen der Rassenmerkmale, der Rasseneigen­tümlichkeiten suchen; wir müssen dann deren Sich-Fortpflanzen bis in unsere Zeit verfolgen, müssen uns dabei aber klar sein, daß, wenn unsere gegenwärtige fünfte Entwickelungsepoche von der sechsten und siebenten abgelöst wird, keine Rede mehr sein kann von einem Zu­stande, den wir als Rasse werden bezeichnen können."
      ],
      [
        "Wenn wir uns diese Entwickelung aber so vorstellen, als ob sie immer nur gleichmäßig so fortrollte, dann haben wir nur eine Art Mühlrad im Kopfe, sind aber weit entfernt von dem Verständnisse dessen, was in der Welt wirklich vor sich geht."
      ],
      [
        "Wir sehen also, wie die Rassenentwickelung erst beginnt in der lemu­rischen Zeit durch das Hineinwirken der abnormen Geister der Form."
      ],
      [
        "Da lassen diese Geister die Kräfte unseres Erdenplaneten eingreifen an dem Orte, wo der Mensch seine erste Lebenszeit zu verbringen hat, und das überträgt sich in gewisser Weise auch wieder auf das spätere Leben, weil der Mensch ein Gedächtnis hat, durch das er sich erinnert an die eigentlich abnormerweise vor dem einundzwanzigsten Jahre auf der Erde zugebrachte Zeit auch in dem späteren Leben.",
        "Der Mensch würde ein ganz anderes Wesen sein, wenn nur die normalen Geister der Form wirkten.",
        "Durch die abnormen Geister der Form ist der Mensch abhän­gig von dem Punkte der Erde, auf dem er lebt.",
        "Die Abweichung von den Gesetzen der normalen Geister der Form ist auf die eben geschil­derte Weise entstanden, so daß bedeutsam wurde für den Menschen der Punkt der Erde, auf dem er in einer bestimmten Verkörperung lebt."
      ],
      [
        "Wir werden diese Verhältnisse noch genauer begreifen durch die folgende Betrachtung.",
        "Da können wir in gewisser Weise angeben, wie der Untergrund, der Bodengrund, sein Wesen nach oben strahlt und die menschliche Organisation durchdringt, so daß der Mensch abhängig wird von diesem Erdenuntergrund.",
        "In dieser Beziehung können wir also bestimmte Punkte der Erde angeben, die mit der menschlichen Wesenheit entwickelungsgeschichtlich zusammenhängen.",
        "Wir werden auf diese Verhältnisse noch genauer eingehen.",
        "Ich will sie jetzt in ab­stracto charakterisieren."
      ],
      [
        "Da haben Sie zum Beispiel (siehe Figur Seite 74) einen Punkt, der im Innern von Afrika liegt.",
        "An diesem Punkte wirken gleichsam von der Erde ausstrahlend alle diejenigen Kräfte, welche den Menschen namentlich während seiner ersten Kindheitszeit ergreifen können.",
        "Spä­ter wird der Einfluß solcher Kräfte auf den Menschen geringer; er ist dann diesen Kräften weniger ausgesetzt, aber sie prägen sich ihm mit dem, was aus ihnen kommt, doch in der stärksten Weise auf.",
        "So also wirkt jener Punkt auf der Erde, auf dem der Mensch lebt, am allerstärksten in der ersten Kindheitszeit und bestimmt dadurch diejenigen Menschen, die ganz abhängig sind von diesen Kräften, ihr ganzes Leben hindurch so, daß jener Punkt ihnen die ersten Kindheitsmerkmale blei­bend aufprägt.",
        "Das ist ungefähr eine Charakteristik aller derjenigen Menschen - in bezug auf ihren Rassencharakter -, die sozusagen um diesen Erdenpunkt herum die bestimmenden Kräfte aus der Erde heraus"
      ],
      [
        "erhalten.",
        "Das, was wir schwarze Rasse nennen, ist im wesentlichen durch diese Eigenschaften bedingt."
      ],
      [
        "Wenn Sie nun weiter nach Asien hinübergehen, da haben Sie einen Punkt auf der Erdoberfläche, wo die späteren Jugendmerkmale dem Menschen aus den Erdenkräften heraus bleibend aufgedrückt werden, wo das, was die besonderen Eigenschaften des späteren Jugendzeitalters sind, aus der Erdenwesenheit heraus auf den Menschen übertragen wird und ihm den Rassencharakter gibt.",
        "Die hier in Betracht kommenden Rassen sind die gelben und bräunlichen Rassen unserer Zeit."
      ],
      [
        "Wenn wir dann weiter von Osten nach Westen gehen, so finden wir einen Punkt, der von Asien her gegen Europa zu liegt und der die spä­testen Merkmale, diejenigen Merkmale, die gerade in dem späteren, auf die erste Jugendzeit folgenden Lebensalter dem Menschen zukommen, dem Menschen bleibend aufdrückt' den Punkt, wo der Mensch nicht schon in der Kindheit von den Erdenkräften ergriffen wird, sondern dann, wenn die Jugend in das spätere Lebensalter übergeht."
      ],
      [
        "In dieser Art wird der Mensch von den Kräften ergriffen, die von der Erde aus bestimmend für ihn sind, so daß wir, wenn wir diese ein­zelnen Punkte ins Auge fassen, eine merkwürdig verlaufende Linie erhalten.",
        "Diese Linie besteht auch für unsere Zeit.",
        "Der afrikanische"
      ],
      [
        "Punkt entspricht denjenigen Kräften der Erde, welche dem Menschen die ersten Kindheitsmerkmale aufdrücken, der asiatische Punkt den­jenigen, welche dem Menschen die Jugendmerkmale geben, und die reifsten Merkmale drückt dem Menschen der entsprechende Punkt im europäischen Gebiete auf.",
        "Das ist einfach eine Gesetzmäßigkeit.",
        "Da alle Menschen in verschiedenen Reinkarnationen durch die verschiedenen Rassen durchgehen, so besteht, obgleich man uns entgegenhalten kann, daß der Europäer gegen die schwarze und die gelbe Rasse einen Vorsprung"
      ],
      [
        "hat, doch keine eigentliche Benachteiligung.",
        "Hier ist die Wahr­heit zwar manchmal verschleiert, aber Sie sehen, man kommt mit Hilfe der Geheimwissenschaft doch auf merkwürdige Erkenntnisse."
      ],
      [
        "Wenn wir dann diese Linie weiterziehen, so kommen wir weiter nach Westen nach den amerikanischen Gebieten hinüber, in jene Gebiete, wo diejenigen Kräfte wirksam sind, die jenseits des mittleren Lebensdrittels liegen.",
        "Und da kommen wir - ich bitte das nicht mißzuverstehen, was eben gesagt wird; es bezieht sich nur auf den Menschen, insofern er von den physisch-organisatorischen Kräften abhängig ist, von den Kräften, die nicht sein Wesen als Menschen ausmachen, sondern in denen er lebt -, da kommen wir zu den Kräften, die sehr viel zu tun haben mit dem Absterben des Menschen, mit demjenigen im Menschen, was dem letzten Lebensdrittel angehört.",
        "Diese gesetzmäßig verlaufende Linie gibt es durchaus; sie ist eine Wahrheit, eine reale Kurve, und drückt die Gesetzmäßigkeit im Wirken unserer Erde auf den Menschen aus.",
        "Diesen Gang nehmen die Kräfte, die auf den Menschen rassebestim­mend wirken.",
        "Nicht etwa deshalb, weil es den Europäern gefallen hat, ist die indianische Bevölkerung ausgestorben, sondern weil die india­nische Bevölkerung die Kräfte erwerben mußte, die sie zum Aussterben führten.",
        "Von der Eigentümlichkeit dieser Linie hängt das ab, was auf der Oberfläche unserer Erde mit den Rassen sich abspielt, was von den Kräften, die nicht unter dem Einfluß der normalen Geister der Form stehen, bewirkt wird.",
        "Wo Rassencharaktere in Betracht kommen, da wirken sie in dieser Weise.",
        "In unserer Zeit wird der Rassencharakter aber allmählich überwunden."
      ],
      [
        "So recht vorgebildet hat sich das schon in der allerfrühesten Erdenzeit.",
        "Wenn wir bis in die alte lemurische Zeit zurückgehen würden, so könnten wir die allerersten Ausgangspunkte der Rassenentwickelung in der Gegend des heutigen Afrika und Asien finden.",
        "Dann sehen wir später eine Herüberbewegung des Menschen nach der westlichen Rich­tung, und in der Verfolgung der rassebestimmenden Kräfte nach We­sten können wir dann das Absterben in den Indianern beobachten.",
        "Nach Westen mußte die Menschheit gehen, um als Rasse zu sterben.",
        "Um aufzufrischen die Menschheit mit neuer Jugendkraft, findet der Zug nach Osten statt, der Zug, der von Atlantis herüber über Europa nach"
      ],
      [
        "Asien sich bewegt.",
        "Dann geschieht eine Wiederholung des Zuges nach dem Westen.",
        "Es wiederholt sich aber jetzt nicht die Bewegung der Rassen, sondern gleichsam eine höhere Stufe der Rassenentwickelung, die Entwickelung der Kulturen."
      ],
      [
        "In gewisser Weise kann man sehen, daß die Entwickelung der Kulturen durchaus den Charakter annimmt, der im Sinne einer Fortsetzung der Rassenlinie liegt.",
        "So haben wir zum Beispiel diejenige Kultur, welche wir auch schon in dieser Betrachtung mit genügender Bewunderung charakterisiert haben, die uralt-indische Kultur, die als erste nachatlantische Kultur erschien, zu bezeichnen als die dem ersten Kindesalter entsprechende Epoche, wo der Mensch in Beziehung auf die Wertschätzung der physischen Natur noch schläft, und in seine Seele wirken hinein die Offenbarungen einer geistigen Welt."
      ],
      [
        "In der Tat ist die erste, indische Kultur eine Offenbarung von oben, eine Offenbarung aus spirituellen Höhen, und sie konnte nur aus dem Grunde in die Menschen hineinwirken, weil der Mensch unter den Einfluß der indischen Erde kam, unter dem er in weit zurückliegender Zeit schon gestanden hatte.",
        "Damals in urferner Vergangenheit wurde der physische Rassecharakter aus der Erde heraus bestimmt; jetzt bei wiederholter Anwesenheit an demselben Erden-Orte wurde mehr eine Seelenbeschaffenheit, die des altindischen Menschen bestimmt."
      ],
      [
        "Durch den Zug von Westen nach Osten ist eine solche Jugendfrische aufge­treten, daß durch diesen Vorgang die eigentümliche Geisteskonfigura­tion hervorgehen konnte, welche die ursprüngliche indische Kultur charakterisiert.",
        "Sie werden sehen, daß eine sehr alte indische Kultur, die noch nicht erforscht worden ist, und von der nur ein Abkömmling ist, was heute die Wissenschaft indische Kultur nennt, in dieser Weise ihre Erklärung findet, nämlich dadurch, daß die atlantische Kultur sich in gewisser Beziehung in der uralt-indischen wiederholt."
      ],
      [
        "Wenn wir nunmehr die Kulturen, die sich in der nachatlantischen Zeit gefolgt sind, betrachten, so können wir sehen, daß sie die aufein­anderfolgende Wiederholung früherer im physischen Leibe durchge­machter, aber wieder durch Verjüngung ganz anders gewordener Ver­hältnisse darstellen.",
        "So sehen wir in der persischen Kultur eine solche, welche in gewisser Weise mit dem zusammenhängt, was wir nennen können ein Sich-Durchringen desjenigen Menschen, der vorzugsweise"
      ],
      [
        "in der ersten menschlichen Lebenskraft lebt, wo er noch den Einflüssen der abnormen Geister der Form hingegeben ist, mit den Kräften, die von den normalen Geistern der Form stammen.",
        "Dieser Gegensatz ist in der persischen Kultur in dem Bewußtsein und in der Gestalt von Licht und Finsternis, von Ormuzd und Ahriman enthalten."
      ],
      [
        "Je weiter wir herüber kommen nach Westen, desto mehr sehen wir, wie die Eigenschaften eines reiferen Alters der Kultur aufgedrückt werden.",
        "Wenn wir auch zugeben müssen, daß bis zur heutigen Gegen­wart die Schöpfungen der Menschen in höherem Grade noch abhängig sind von den abnormen Kräften und Wesenheiten des Weltalls, so werden wir es doch begreiflich finden, wenn gesagt wird, daß nicht mehr ausschließlich mit Eigenschaften der Rasse die Menschen nach Westen gehen.",
        "Auch können wir verstehen, daß in gewisser Weise der Zug der Kultur ein solcher ist, daß die volle Jugendfrische der Kultur, das produktive Element derselben immer mehr erstirbt, je weiter sie nach Westen kommt."
      ],
      [
        "Wer objektiv betrachtet, kann aus vielen Verhältnissen ersehen, daß auch unsere Zeitkultur in dieser Weise gesetzmäßig bestimmt ist.",
        "Man ist aber nicht geneigt, objektiv zu sehen.",
        "Wenn Sie aber das, was sich ergibt, betrachten, das betrachten, daß in der Tat alle Kultur im Flusse ist, da sehen Sie, daß, je weiter wir nach Westen kommen, die Kultur immer unproduktiver wird.",
        "Sie nähert sich also als Kultur dem Abster­ben.",
        "Je weiter nach Westen, desto mehr werden nur die äußeren Teile der Kultur blühen, die, welche nicht Auffrischung durch Jugendkraft erleben, sondern sich in gewisser Weise in das Greisenhafte hinein ausleben.",
        "Daher wird der Mensch im Westen für die Menschheit noch Großes und Gewaltiges leisten können in bezug auf physikalische, chemische und astronomische Entdeckungen, für alles, was unabhängig ist von der erfrischenden Jugendkraft.",
        "Das aber, was produktive Kraft benötigt, das braucht in der Tat eine andere Konfiguration der auf den Menschen wirkenden Kräfte."
      ],
      [
        "Nehmen wir an, der Mensch wächst von der Kindheit bis zu einer gewissen Stufe; dann erblüht eigentlich erst sein Geistiges.",
        "Zuerst ist der Mensch ein physisch wachsendes Wesen.",
        "Es muß sich das, was bei einem kleinen Knirps in einem engen Raume zusammengedrängt ist,"
      ],
      [
        "erst physisch ausdehnen.",
        "Dann wird die Menschenbildung in das Innere zusammengedrängt. - So ist es aber auch mit der Menschheit im großen.",
        "Wir sehen ein eigentümliches Gesetz, wenn wir die charakterisierte Kurve verfolgen.",
        "Wir finden es sogar in den Kontinenten ausgedrückt.",
        "Wir sehen, daß zunächst eine Art ursprünglicher Anfangspunkt der physischen Menschenentwickelung in Afrika vorliegt, daß dann der Raum, auf dem sich die Menschheit ausbildet, sich ins Weite ausdehnt.",
        "Das finden wir dann in den weiten Flächen der asiatischen Bildung.",
        "Große, mächtige Flächen bewohnt der Mensch da."
      ],
      [
        "Schauen wir nun auf die Wiederholung der Rassenbildung in den nachatlantischen Kulturen.",
        "Wie der Mensch in der Jugend gleichsam neugierig mit den Augen hinschaut in die Umgebung, so blickt der Mensch der alten indischen Kultur in die Welt.",
        "Das hängt durchaus mit den jugendfrischen Kräften zusammen, die den Menschen ausdehnen und in seinem Wachstum in die Weite organisieren.",
        "Dann muß das Geistige beginnen und muß sich das Physische zusammendrängen; da sehen wir, daß, indem die Kultur in Europa fortschreitet, in merkwür­diger Weise der Raum, auf dem diese Menschheit ausgebreitet ist, zu­sammengedrängt wird in kleinere Dimensionen.",
        "Wir sehen, daß Europa der kleinste Erdteil ist, und je weiter der Mensch nach Westen fort­schreitet, desto mehr strebt er nach einem Zusammendrängen.",
        "Er strebt in Halbinseln hinaus ins Meer und schnürt sich immer mehr zusammen nach dem Westen hin."
      ],
      [
        "Dies hängt alles mit dem geistigen Gang der Entwickelung zusam­men.",
        "Sie sehen hier in eigenartiger Weise in die Mysterien der geistigen Entwickelung hinein.",
        "Aber mit dem Zusammendrängen nach Westen hin ist eine Krisis gegeben.",
        "Da ist eine Krisis, durch welche ein mehr unproduktives Element zu wirken beginnt.",
        "Die Produktivität stirbt in den Halbinselgebieten nach dem Westen hin in einer gewissen Weise ab.",
        "Diese Unproduktivität zeigt sich in dem, was vorhin charakterisiert worden ist, daß nämlich sozusagen selbst die Kultur, je weiter sie nach Westen geht, ein starres, greisenhaftes, nach dem Absterben hin gehen­des Element annimmt.",
        "Das ist etwas, was in den Geheimschulen immer bekannt war.",
        "Sie werden nun begreifen, daß ich sagte, das, was ich mitteilen werde, könnte etwas gefährlich werden, weil die Menschen"
      ],
      [
        "entrüstet werden könnten.",
        "Und es darf noch lange nicht alles gesagt werden, was dazu diente, den Menschen in bezug auf die höheren Ge­biete seines Wesens unabhängig zu machen, damit er wahrnimmt, was aus der Erde rassebestimmend aufsteigt, was später den Kulturcharak­ter bestimmt, und was in noch späterer Zeit wieder unbedeutend wer­den wird, wenn der Mensch zum Geistigen wieder zurückkehrt."
      ],
      [
        "Sie werden daher begreifen, daß mit diesem ganzen Gang der Menschheits­entwickelung der Gang der geistigen Entwickelung, den diejenigen immer gekannt haben, die tiefer in die Geheimnisse des Daseins einge­weiht waren, zusammenhängt.",
        "Die Richtigkeit des Gesagten hängt nicht davon ab, ob man für das eine mehr, für das andere weniger begeistert ist; die hängt von der Notwendigkeit in der Entwickelung ab."
      ],
      [
        "Wer gegen die Notwendigkeit sprechen würde, der könnte nichts erreichen.",
        "Gegen sie sprechen, heißt ihr Hindernisse in den Weg schie­ben.",
        "Daher ist es nur natürlich, daß in gewisser Weise die Menschen, die in das Gebiet ziehen, das mehr nach Westen liegt, sich eine Auffrischung wieder vom Osten holen müssen, einen Einschlag vom Osten erhalten müssen, daß aber das mitteleuropäische Gebiet sich auf die eigene Pro­duktivität, wie sie vor der Halbinselbildung bestanden hat, besinnen muß."
      ],
      [
        "Das ist der Grund, warum in Europa gerade - ich meine in dem Strich, der unser gemeinsames Gebiet umfaßt: Skandinavien und Deutschland - die Menschen sich auf ihr eigenes Seelisches besinnen müssen, und warum dagegen gerade im Westen aufgesucht werden muß der Teil der Menschheit, der etwas von Osten übertragen erhalten soll.",
        "Das ist tief durch den Gesamtcharakter der Erdenmenschheit bedingt."
      ],
      [
        "Sie sehen, daß selbst in der geisteswissenschaftlichen Entwickelung das sich noch wiederholt.",
        "Auch tritt uns das entgegen in der vierten nachatlantischen Kultur bei dem Römer- und Griechentum.",
        "Es ist Tatsache, daß die Römer in gewisser Beziehung weiter sind als die Griechen, daß sie aber von dem von ihnen eroberten Volke, welches weiter östlich wohnt, das Geistesleben nehmen."
      ],
      [
        "Das hier zutage tretende Gesetz wird immer mehr und mehr sich bewahrheiten, je weiter die Gebiete nach Westen gelegen sind.",
        "Diese großen Wahrheiten kann man im Grunde genommen nur andeutungs­weise sagen.",
        "Sie geben uns dasjenige, was dem inneren Charakter"
      ],
      [
        "unserer Mission für jedes Stück der Erdoberfläche entspricht.",
        "Sie sehen, daß wir begreifen müssen dasjenige, was wir zu tun haben, um uns zu dem Gemeinsamkeitscharakter der Menschheit zu erheben.",
        "Da liegt die große Verantwortlichkeit, die man hat, wenn man eingreifen will in die große Bewegung der Menschheit.",
        "Wo die große Bewegung der Mensch­heit in Betracht kommt, da darf keine persönliche Sympathie und kein persönlicher Enthusiasmus mitspielen.",
        "Denn nicht darauf kommt es an, sondern darauf, was in den großen Gesetzen des Menschentums bedingt ist.",
        "Das muß man aus den großen Gesetzen heraus erkennen und sich nicht beeinflussen lassen durch Voreingenommenheit für dieses oder jenes.",
        "So ist im Grunde genommen der Charakter des ganzen Rosen­kreuzertums.",
        "Rosenkreuzertum ist, zu wirken im Sinne der ganzen Menschheitsentwickelung.",
        "Wenn man den Boden, auf dem man steht, erkennt bis zur Insel- und Halbinselbildung, dann wird man fühlen, welche Empfindung einen überkommen muß, wenn man im Sinne der Menschheitsentwickelung wirken will."
      ],
      [
        "Einstmals wurde der Mensch durch die abnormen Geister der Form heruntergeführt auf die Erde, gebunden an die verschiedenen Punkte der Erdoberfläche; dadurch wurde die Grundlage der Rassenentwickelung geschaffen.",
        "Dann aber sehen wir immer mehr die Rassen sich vermischen.",
        "Wir sehen eingreifen in die Rassenentwickelung, das heißt sich aus ihr erheben die Volksentwickelung.",
        "Wir sehen sie hineingreifen bis in die Entwickelung des einzelnen Menschen.",
        "Es ist ein großes My­sterium damit ausgesprochen, wenn man etwa sagt: Wer war Plato in bezug auf seine äußere Wesenheit, in bezug auf das Hineingeborensein in die Menschheit?",
        "Das war ein Mensch, der hineingewachsen war in das Geschlecht der Soloniden, angehörte dem Stamme der Ionier, dem Volke der Griechen, der ganzen kaukasischen Rasse. - Das Verstehen, daß Plato ein Solonide, ein Ionier, ein Grieche, ein Kaukasier war, das spricht, wenn man es in seiner Gesetzmäßigkeit durchschaut, ein tiefes Mysterium aus.",
        "Es spricht das Mysterium aus, das uns zeigt, wie auf der weiten Basis des ganzen Erdenplaneten zusammenwirken die normalen und abnormen Geister der Form, die eigentlich das größte Interesse daran haben, den Menschen zum Erdenmenschen zu machen.",
        "Es spricht sich darin aus, wie sich durch dieses Zusammenwirken das Menschentum"
      ],
      [
        "spezifiziert, wie dann die anderen Wesenheiten eingreifen, von denen wir bei der Charakteristik der einzelnen Völkerschaften schon gesprochen haben.",
        "Jeder Mensch ist mit seiner Wesenheit an den Vor­gängen beteiligt, durch die alle die höheren Wesenheiten, diese höheren Geister zusammenwirkend die Weltentwickelung gestalten."
      ],
      [
        "Man versteht den einzelnen Menschen nicht, wenn man nicht sieht, wie er in seiner Gesamtentwickelung dadurch, daß diese Wesenheiten zusammenwirken, geworden ist.",
        "Dadurch, daß auf unserem Erdenpla­neten durch das geheimnisvolle Zusammenwirken der Geister der Form, die die normale Entwickelung durchgemacht haben, und der Geister der Form, die die abnorme Entwickelung durchgemacht haben, einmal eine kaukasische Rasse geschaffen wurde, dadurch wurde der Grund und Boden dafür geschaffen, daß ein Plato überhaupt werden konnte.",
        "Dadurch, daß wir die abnormen und normalen Erzengel bis zu den Engeln eingreifen sehen, sehen wir den Weg, der notwendig war, um einen Plato hervorzubringen, der uns als menschliche Wesenheit, mit menschlichem Antlitz, mit ganz bestimmten Verstandes-, Gefühls- und Willenseigenschaften entgegentreten konnte.",
        "Zwischen der Rasse und der Individualität liegt das Volkstum mitten darinnen."
      ],
      [
        "Darum mußten wir heute die Grundbedingungen der Rasse im allge­meinen charakterisieren.",
        "Morgen wollen wir das Herauswachsen des Volkstumes aus den Rassen, das Eingreifen anderer Geister der Hierar­chien und insbesondere deren Eingreifen in das Wirken der Geister der Form betrachten."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "FÜNFTER VORTRAG Kristiania, 11. Juni 1910",
    "paragraphs": [
      "Aus dem gestrigen Vortrage wird hervorgegangen sein, daß allerdings notwendig ist zum vorurteilsiosen Eindringen in die Tatsachen, welche dieser Betrachtung zugrunde liegen, ein gewisses Sichhinwegsetzen über alles dasjenige, was sonst leicht an Gefühlen, an Empfindungen den Menschen gerade von jener Seite her durchdringt, die wir jetzt objektiv charakterisieren müssen. Solange man noch irgendwie geneigt ist, eine objektive Charakteristik dieser oder jener Rasse, dieses oder jenes Volkstums oder dergleichen persönlich zu nehmen, so lange wird ein vorurteilsfreies Verständnis der Tatsachen gerade dieses Vortragszy­klus schwer zu erreichen sein.",
      "Damit hängt es auch zusammen, daß über diese Dinge auf keinem anderen Boden als auf dem Boden der Geistes­wissenschaft gesprochen werden kann. Denn was man auch hören soll über die Charaktere dieses oder jenes Volkstums, und wie sehr man auch deshalb, weil man doch innerhalb irgendeiner Rasse, innerhalb eines Volkstums steht mit seinen Empfindungen, Gefühlen und so weiter, dabei sein könnte, man hat ein genügendes Gegengewicht als Geisteswissenschafter, um es in die andere Waagschale zu legen.",
      "Das ist die wirklich verstandene Lehre von dem Karma und der Reinkar­nation. Sie bietet uns ja einen Ausblick darauf, daß wir mit dem inner­sten Kern unseres Wesens in den aufeianderfolgenden Zeiten in den verschiedensten Rassen, in den verschiedensten Völkern inkarniert werden.",
      "So können wir also gewiß sein, wenn wir auf diesen Kern unseres Wesens schauen, daß wir mit ihm teilnehmen werden nicht nur an den Sonnen- oder vielleicht auch Schattenseiten aller Rassen, aller Volkstümer, sondern wir können gewiß sein, daß wir in unserem inner­sten Wesen aufnehmen Beitrag auf Beitrag der Segnungen aller Rassen und Volkstümer, indem wir einmal da, einmal dort inkarniert werden.",
      "Es wird unser Bewußtsein, unser Horizont weiter, umfassender durch diese Ideen von Karma und Reinkarnation. Deshalb lernen wir erst durch sie dasjenige ertragen, was in unserer Gegenwart über die Ge­heimnisse der Rassen- und Volkszusammenhänge vor unser geistiges",
      "Auge treten muß. So wird denn gerade durch das in dieser Betrachtung Abgehandelte, wenn es richtig erkannt wird, ein Unbefriedigtsein über das Inkarniertwerden in diesem Volke oder jener Rasse nicht in uns hineingebracht werden können. Es wird aber trotzdem ebenso in die Menschheit durch ein solches objektives Anschauen der menschlichen Volks- und Rassencharaktere Unfrieden und Disharmonie hereinge­bracht werden können, wenn es nicht mit den angedeuteten Voraus­setzungen aufgenommen wird. Der geistig Strebende wird durch die Lehre von Karma und Reinkarnation lernen, wie jedes - und sei es auch das kleinste Volk - seinen Beitrag zu liefern hat zu der Gesamtentwik­kelung der Menschheit. Das wird gerade das Bedeutungsvolle sein, daß in dem zweiten Teile dieser Vorträge gezeigt werden wird, wie die einzelnen Einflüsse der Völkermissionen in die Gesamt-Menschheit einfließen, und wie sogar einzelne Volkssplitter, die da und dort in die großen Volksmassen zerstreut sind, ihre Bedeutung haben in der Ge­samtharmonie der Menschheitsevolution. Das aber wird nur allmählich vor unser geistiges Auge hintreten können.",
      "Wir werden uns - um ein volles Verständnis für die Charaktere der einzelnen Volksseelen zu gewinnen - an solche Beispiele halten müssen, die uns in gewisser Beziehung auf der einen Seite klarer sind als die Volkscharaktere der Gegenwart, innerhalb welcher wir mit unserer Zivilisation selber leben, und wir werden uns auf der anderen Seite vielleicht mit solchen Volkscharakteren beschäftigen müssen, die uns der Zeit nach etwas ferner liegen, damit wir uns ein Verständnis dafür erwerben, wie man überhaupt Volkscharaktere, Volksmissionen ver­stehen kann. Damit haben wir ja zunächst nur im allgemeinen das Rassenhafte, das Volksmäßige charakterisiert.",
      "Daß wir im Laufe der letzten Vorträge gefunden haben, daß in einer Rasse zusammenwirken müssen sozusagen ein normaler und ein abnor­mer Geist der Form, daß innerhalb eines Volkes ein in seiner normalen Entwickelung begriffener und ein in abnormer Entwickelung begrif­fener Erzengelgeist wirken müssen, das hat uns sozusagen verständlich gemacht, wie die Wesenheiten, die wir als die geistigen Hierarchien kennen gelernt haben, in die Evolution eingreifen.",
      "Jetzt fragen wir uns: Wie wirken denn die geistigen Wesenheiten",
      "höherer Art in das Konkrete hinein? Da wird es gut sein, wenn wir uns heute dadurch eine Grundlage schaffen, daß wir uns überhaupt ein Verständnis erwerben über die Hierarchien, zu denen, wie wir wissen, der Mensch als unterstes Glied gehört. Erinnern Sie sich an dasjenige, was wir bereits gehört haben, so wissen Sie, daß wir diese Hierarchien so auffassen, daß wir sagen: Auf der untersten Stufe steht der Mensch. -Unter ihm liegen die drei Naturreiche: Tierreich, Pflanzenreich, Mine­ralreich. - Dann kommen die Engel, dann die Erzengel, dann die Ur-kräfte oder Archai. Das ist dasjenige, was wir bezeichnen können als die erste der Hierarchien, vom Menschen aufsteigend. Die zweite der Hierarchien ist die folgende:",
      "1.    Geister der Form - Gewalten",
      "2.    Geister der Bewegung - Mächte",
      "3.    Geister der Weisheit - Herrschaften",
      "Sodann haben wir noch die höchste der drei Hierarchien:",
      "1.    Geister des Willens - Throne",
      "2.    Cherubim",
      "3.    Seraphim",
      "Nun fragen wir uns einmal: Da alle geistigen Wesenheiten sich irgendwie offenbaren, so daß sie im Bereiche der Maja oder Illusion, also im Bereiche der Sinnenwelt irgendwo erscheinen, wo können wir sie auf der untersten Stufe der Offenbarung, auf der Stufe der Täu­schung aufsuchen? Der Mensch in seiner gewöhnlichen Natur- und Geistesbetrachtung kennt ja nur das Gebiet der Maja oder Illusion, die alleräußerste Außerung dieser geistigen Wesenheiten. Ich will Ihnen an einem Beispiele zeigen, wie der Mensch eigentlich nur die alleräußerste Manifestation, die alleräußerste Offenbarung dieser Wesen kennt.",
      "Der Mensch geht zum Beispiel mit seinen Füßen über nordischen Felsengrund. Da wird er nun zunächst darüber sagen: Da ist Materie ausgebreitet, und er wird dieses dichte Felsengestein, über das er dahin-schreitet, so beschreiben, wie er es zunächst sieht und es in seiner gewöhnlichen Sprache «harte Gesteinsmaterie» nennen. Derjenige, der eindringt in das Wesen der Dinge, sieht in dieser Gesteinsmaterie etwas",
      "ganz anderes. Was ist das eigentlich, worauf wir auftreten und was uns Widerstand bietet? Das, wovon der Mensch glaubt, daß es da sei, das ist gar nicht da, das ist eine Täuschung. Die äußerste Oberfläche unserer Erde ist lediglich eine Täuschung.",
      "Die Wahrheit ist diese, daß Kräfte von unten heraufwirken, die wiederum nichts anderes sind als Kräfte, die von gewissen Wesenheiten ausströmen, so daß wir also sagen kön­nen: Wir sehen in einem solchen Stück Boden dasjenige vor uns, was sich zunächst als eine Kraft darstellt, die aus der Erde heraus nach allen Seiten hin wirkt. Diese Kräfte sind wirklich da und strahlen nach allen Seiten in den Raum hinaus.",
      "Der Mensch könnte allerdings nicht auf der Erde herumgehen, wenn nur diese Kräfte da wären. Diese Kräfte allein würden den Menschen mit rasender Schnelligkeit in den Raum hinaus­schleudern. Daß er auf festem Boden stehen kann, das verdankt er dem Umstande, daß aus dem Weltenraum von allen Seiten andere Kräfte hereinstrahlen.",
      "Immerfort begegnet sich die Sphäre der hereinstrahlen-den Kräfte mit derjenigen der herausstrahlenden Kräfte, und da, wo sie zusammenkommen, bilden sie sozusagen eine Grenze, und das ist die Oberfläche der Erde. So ist das, was man sieht als Oberfläche, nur eine Täuschung, die das Ergebnis von ein- und ausstrahlenden Kräften ist, welche so wirken, daß sie sich gerade an der betreffenden Oberfläche gegenseitig aufhalten.",
      "Was da herausströmt, ist im wesentlichen das­selbe, was wir die Wirkungen der Throne, die Wirkungen der Geister des Willens nennen müssen. Diese Geister strahlen von der Erde nach allen Seiten hin ihre Kräfte aus, und dasjenige, was von dem Welten-raum hereinkommt, das ist im wesentlichen das, was man nennen kann einstrahlende, hereinarbeitende Kräfte von gewissen Geistern der Be­wegung.",
      "Diese beiden Arten von Kräften begegnen sich also hier, und dieses Zusammenwirken der Throne mit den Geistern der Bewegung -dadurch, daß die Throne in ihrer Wirkung aufgehalten werden von den Geistern der Bewegung - gibt die verschiedenartig konfigurierte Ober­fläche, so daß das, was Sie draußen als Erdoberfläche sehen, das Un­wahrhaftigste, die äußerste Täuschung ist. Das, was wirklich da ist, ist ein Ausgleich von Kräften und gleichsam ein Vertrag zwischen den Geistern des Willens und den Geistern der Bewegung, der so geschlossen wird, daß er die Erde in der verschiedensten Weise konfiguriert.",
      "Allerdings würde das immer noch nicht hinreichen, daß unsere Erde, so wie sie jetzt gerade ist, sich als ein solcher Planet bilden könnte. Das Gegeneinanderwirken der Geister des Willens und der Geister der Be­wegung würde dazu noch nicht hinreichen. Das würde noch etwas ganz anderes geben. Wenn nämlich bloß die Geister des Willens vom Innern der Erde heraus wirken würden und nur einen Widerpart in den Gei­stern der Bewegung hätten, dann würde die Erde in fortwährendem Flusse, in einem fortwährenden inneren Strome sein. Der Planet würde noch nicht an irgendeiner Stelle zur Ruhe kommen können. Er wäre dann zwar nicht so flüssig wie das heutige Meer, er würde ein nicht so leicht wellenwerfendes und wellenbildendes Element sein wie das Was­ser, würde aber in einer dichteren Masse Wellen werfen und bilden.",
      "Wenn Sie sich eine Vorstellung davon machen wollen, wie die Geister des Willens und die Geister der Bewegung ursprünglich zusammen-wirkten, so möchte ich Ihnen ein Beispiel geben und Sie bitten, mich etwas auf der Landkarte zu begleiten. Da möchte ich zunächst auf die Alpen hinweisen, die heute ein festes Berggerippe sind, so daß wie ein fester Gesteinsboden das Alpenmassiv die italienische Halbinsel im Süden von den anderen europäischen Gebieten abtrennt. Wie ist diese Alpenkette nun eigentlich zustande gekommen? Es gab eine Zeit - sie liegt weit in urferner Vergangenheit zurück -, da war das Alpenmassiv überhaupt noch nicht da, aber nord- und westwärts hin, da waren bereits ältere Erhebungen, die damals schon fest geworden waren. Zäh-flüssige Wellen waren es, die dann von Süden herauf aufgeworfen wurden, so daß wir uns die Sache so vorstellen können:",
      "Hier bei A würden wir das Böhmische Plateau haben. Dann wollen Sie sich vorstellen, daß von Süden herauf eine mächtige Welle geworfen wurde, die sich nach rechts gegen das Böhmische Plateau und nach links gegen das französische Zentralplateau hinüber spaltete und verbreitet hat.",
      "Diese mächtige Welle bildete also in uralten Zeiten dieses Alpen-massiv. Selbst aus einer populären Vorstellung kann sich dies ergeben. Wer einmal auf einem Bergesgipfel der Alpen gestanden hat und die eigentümliche Konfiguration der Alpenkette überblickt, der sieht -wenn er es auch nicht wüßte - das, was die Geisteswissenschaft längst festgestellt hat und die heutigen Geologen sogar feststellen: die eigen­artige Wellenbildung, die in der Zeit, als die Urmasse der Erde noch in einem zähflüssigen Zustande war, stattgefunden hat.",
      "So würde sich durch das Zusammenwirken der Geister des Willens und der Geister der Bewegung die Erde heute noch gestalten, wenn nicht ein anderes Wirken eingetreten wäre, ein Wirken, das außerordentlich nachhaltig ist, und das sich auf unserer Erdoberfläche dadurch äußert, daß den Willenskräften, die mit den Geistern der Bewegung zusammenwirken, dasjenige eingegliedert wird, was wir eben die Geister der Form nennen. Sie können sich also vorstellen, daß diese Geister der Form, gleichsam auf den Wellen tanzend, die bewegten Massen zur Ruhe bringen, in Formen gießen, so daß wir also ein Zusammenwirken von dreierlei Kräften zu verzeichnen haben.",
      "Diese drei Kräfte führen auf dreierlei Wesenheiten zurück. Auf der einen Seite sehen Sie wirken die Geister der Form, die sowohl nach oben als nach unten, sowohl in die Sphäre der Geister des Willens als auch in die Sphäre der Geister der Bewegung hineinwirken.",
      "Über ihnen sind die Geister der Bewegung, unter ihnen die Geister des Willens. - Dasjenige, was auf unserer Erde äußerlich vorzugsweise als flüssiges Element erscheint - allerdings nicht unser heutiges Wasser, sondern das alte flüssige Element, das durch die Gei­ster der Form zur Ruhe gebracht worden ist -, das müssen wir als die äußerste Manifestation der Geister des Willens oder der Throne auf­fassen. Immer aber mischt sich in dieses Wirken ein anderes Element hinein; es wird sozusagen den Geistern des Willens oder Thronen Hilfe geleistet von den Cherubim und Seraphim.",
      "Von den Cherubim wird Hilfe geleistet im Elemente der Luft, in allem, was als Luftförmiges die",
      "scheinbare Materie der Erde durchdringt. Luft ist gleichsam eine Illu­sion, und dahinter stehen die mächtigen Wesenheiten, die wir Cherubim nennen. Die Seraphim wirken in dem, was wir als Wärme kennen, hin­ter allem, was irgend als Wärme vorhanden ist.",
      "Wir blicken damit auf das hin, was in unserem Planeten durch Aus­strahlen von innen heraus aus dem Mittelpunkte bewirkt wird. Wir können also sagen: Unser Planet ist so zusammengesetzt, daß aus seinem Mittelpunkt heraus wirken die Geister des Willens oder Throne, die Cherubim und Seraphim. Wir müssen unseren Planeten so auffassen:",
      "Wo die Luft- und Wärmegrenze desselben ist - das Luftmeer gehört ebenso zu unserem Planeten wie das Wasser oder die feste Erde -, da wird gleichsam eine Oberfläche gebildet. Auf dieser Oberfläche tanzen förmlich auf den Wellen und bringen sie zur Ruhe, zur Form, die Geister der Form. Aus diesem Grunde wurde ihnen der Name gegeben, weil sie das zähflüssige Element zur Ruhe bringen. Hinter ihnen stehen die Geister der Bewegung. In deren Element mischt sich wieder das­jenige, was wir die Geister der Weisheit nennen. So daß wir, wenn wir gegen den Mittelpunkt unseres Planeten hinblicken, sagen können: Da sind erhabene Wesenheiten, Throne, Cherubim, Seraphim. - Blicken wir hinaus, so schauen wir zunächst durch die Sphäre der Geister der Form, die Luft und Wärme durchdringen mit ihrem Element, auf die Geister der Bewegung und die Geister der Weisheit. Alles, was wir an Naturkräften und Erscheinungen haben, wenn wir den Blick hinaus­richten in den Umkreis unserer Erde, wenn wir hinaufschauen in Him­melshöhen, das ist im wesentlichen der zweiten Hierarchie zuzuschrei­ben. Alles, was wir erblicken, wenn wir in die Tiefen der Erde hinunter-schauen, das schreiben wir den Wesenheiten zu, die wir als die dritte Hierarchie bezeichnet haben. Das eigentümliche Zusammenwirken der zweiten und dritten Hierarchie, das gibt die Konfiguration unserer Umgebung.",
      "In welchem Naturelement - wir haben die drei Naturelemente Wasser, Luft, Feuer als mit den Geistern des Willens, den Cherubim und Seraphim in Verbindung stehend angeführt - geben sich nun die Geister der Form kund? Das sind die nächsten Wesen, die auf der Ober­fläche tanzen, auf der wir weben, leben und sind. Sie kommen aus dem",
      "Weltenraum herein, entfalten aber ihre Kraft nun in dem, was aus der Erde heraufströmt. Für unsere Beobachtung sind sie konzentriert in dem, was wir die ausstrahlenden Sonnenstrahlen nennen. Das Licht ist also das Element, in dem die Geister der Form zunächst weben und leben. Indem aber die Lichtwirkungen mit alle dem, was sie enthalten, sich an der Grenze, wo die Geister der Bewegung und die Geister des Willens zusammenwirken, entfalten, da werden die festen Formen erzeugt.",
      "Der Mensch hat zunächst keine Organe, um auch in das hinaufblik­ken zu können, was jenseits jener Kräfte des Lichtes - die wir auch die Geister der Form nennen - liegt, keine Organe, um in das hineinblicken zu können, was in das Licht hineinverwoben ist. Alles, was auf unserer Erde Zersetzungen und Zusammensetzungen bedingt, alles was als che­mische Kräfte auf derselben wirkt, ist hier noch in das Licht hineinver­woben, und das ist im wesentlichen das Terrain, auf dem die Geister der Bewegung tätig sind. Wenn der Mensch etwas wahrzunehmen lernt von dem, was er sonst nur als Maja in der Wirkung der chemischen Zusammensetzungen und Auflösungen sieht, dann hört er diese Geister der Bewegung, dann nimmt er die Sphärenmusik wahr, von der die pythagoräische und andere Geheimschulen sprechen. Das ist auch das, was Goethe beschreibt, wenn er von der Sonne nicht als der Lichtspen­derin spricht, sondern sagt: «Die Sonne tönt nach alter Weise in Bru­dersphären Wettgesang, und ihre vorgeschriebne Reise vollendet sie mit Donnergang.»",
      "Diese Sphärenmusik ist auch jetzt immer noch da, nur daß sie das gewöhnliche Bewußtsein nicht hört. Sie ist wirklich, diese Sphären-musik, die allen Menschen als astralische Wirkung von außen entgegen­kommt. Der Mensch hört sie nur nicht. Würde er in bezug aufdiese Sphärenmusik einen eben solchen Wechsel haben wie beim Licht, das er zu gewissen Zeiten, beim Eintreten der Dunkelheit, nicht sieht, dann würde er sie zu gewissen Zeiten auch hören. Sie tönt aber Tag und Nacht, und daher kann er sie nur dann hören, wenn er eine gewisse okkulte Schulung, eine gewisse okkulte Entwickelung durchmacht. Während das Licht uns während des Tages als Licht zuströmt und während der Nacht als aufgenommenes, absorbiertes Licht weiterwebt,",
      "tönt die Sphärenmusik Tag und Nacht. Es ist für den Menschen damit so wie bei dem Müller, der die Mühle nur dann hört, wenn sie stille steht.",
      "Es gibt außerdem noch die Geister der Weisheit, die von außen ihre Wirkungen hereinsenden und die hineinwirken in das webende Licht und die den Raum durchwebende Sphärenmusik. Das ist das auf die Erde einstrahlende Leben des Weltenäthers. Leben strömt vom Welten-raum auf die Erde ein und wird von den Wesen aufgefangen. Das kommt von den Geistern der Weisheit.",
      "So blicken wir in Weltenfernen und sehen zunächst zu der Sonne auf, in der diese Kräfte für uns konzentriert sind und sehen, wie aus dem Raume hereindringt strömendes Leben, webender Ton, Jormendes Licht, die Dreiheit der zweiten Hierarchie. Von unten herauf strömt uns die höchste der Hierarchien zu, die Seraphim, Cherubim und Throne. Hineinverwoben in all das Wirken über die Erde hin, mehr im Innern der Wesen wirkend, ist die erste Hierarchie. Dazu gehören zunächst die Archai, die als Zeitgeister wirken. Diese Zeitgeister weben in dem, was ihnen von den höheren Hierarchien zubereitet worden ist, und bewirken das, was wir unsere menschliche Geschichte, die Kultur-evolution auf der Erde nennen. Dann finden wir im Umkreise die Erz­engel, die Geister der Volksstämme und endlich die Vermittler zwischen dem einzelnen Menschen und den Erzengeln: die Engel.",
      "Wir können also sagen: In den Naturkräften, die wir auf dem Erd­planeten haben, in Erde, Wasser, Luft und Feuer strömen aus die Wesenheiten der dritten Hierarchie und strömen entgegen dem Wirken der Geister der Form, die von außen kommen. Von außen strömen die Wesenheiten der zweiten Hierarchie herein, und im Umkreis der Erde sind die Wesenheiten der ersten Hierarchie, welche sozusagen vorläufig diejenige ist, welche die schwächsten Kräfte hat. Denken Sie sich nur einmal, was für starke Kräfte die erhabenen Wesenheiten haben, welche wir die Geister des Willens nennen, die eigentlich den Boden meißeln, auf dem wir herumgehen. Dann haben wir diejenigen Kräfte, die von außen hereinströmen. Nehmen wir die uns am nächsten stehenden, die Geister der Form, welche die Massen plastisch modellieren. Sodann haben wir das, was intim in die menschliche Seele wirkt, das, was wir",
      "die Engel, Erzengel und Archai nennen. - In der dritten Hierarchie haben wir also diejenigen Naturkräfte, die wir als die stärksten, als die Untergrund-Naturkräfte, als die Kräfte unserer Erdfeste kennen. In der zweiten haben wir diejenigen Kräfte, die um uns im Atherelement leben und weben, und in der ersten Hierarchie haben wir dasjenige, was uns selber intim durchlebt und durchwebt.",
      "Wenn wir diese drei Hierarchien in ihrem Zusammenwirken nehmen und sehen, wie sie wirken in unserem Erdplaneten, wie sie ihn aus dem gesamten Mutterschoß des Weltenalls herausgestalten, dann bekommen wir einen Begriff von dem, was notwendig war, um diese Erde zustande zu bringen. Die Erde mußte durch verschiedene Verkörperungen hin-durchgehen, bevor sie Erde werden konnte: durch den Saturn-, den Sonnen- und den Mondzustand. Wenn Sie die Darstellungen in meiner Schrift zur «Akashachronik» und in meiner «Geheimwissenschaft» verfolgen, so werden Sie sehen, daß schon während früherer Verkör­perungen unserer Erde diese verschiedenen geistigen Wesenheiten zu­sammengewirkt haben, nur daß dieses Zusammenwirken in einer von der gegenwärtigen verschiedenartigen Weise stattgefunden hat. Jedes­mal, wenn eine neue Verkörperung auftrat, also Saturn-, Sonnen-, Mond- und Erdenzustand, gab es eine andere Art des Zusammenwir­kens dieser hierarchischen Wesenheiten, weil nämlich jeder dieser Zustände, durch die unsere Erde hindurchgegangen ist, eine besondere Aufgabe darstellt, die sich diese hierarchischen Wesenheiten setzten. Wir können durchaus davon sprechen, daß jeder der Zustände, die unsere Erde durchgemacht hat, und die Zustände, die sie noch durch­machen wird, eine besondere Mission in der kosmischen Entwickelung bedeuten und bedeutet haben.",
      "Es ist nun außerordentlich schwierig - denn alle Begriffe ändern sich von Planetenzustand zu Planetenzustand - zu definieren, was die Mission der alten Saturn-, der alten Sonnen-, der alten Mondepoche war. Es ist dies nicht leicht, weil man zunächst die Mission unserer Erde sehr abstrakt charakterisieren muß. Man bekommt am leichtesten eine Vorstellung davon, wenn man sich vergegenwärtigt, wie die verschie­denen Kräfte beschaffen sind, die im Weltenraum sich offenbaren. Nun haben Sie, wenn Sie auf das menschliche Innere, auf das Seelenleben",
      "schauen, Wollen, Fühlen und Denken, und wiederum haben Sie, wenn Sie auf die menschlichen Hüllen blicken, auf das Außere der Menschen-natur, physischen Leib, Atherleib und Astralleib, so daß Sie, wenn Sie den heutigen Menschen anschauen und von seinem Ich zunächst ab­sehen, ihn als ein Gewebe auffassen können des physischen, Ather- und Astralleibes, in das hineingewoben sind - wie in eine äußere Hülle -Wollen, Fühlen und Denken.",
      "Nun sind diese Kräfte im Menschen, sowohl im äußerlichen wie im inneren Menschen, immer verwandt mit irgendwelcher früheren Mis­sion, die gebunden war an frühere Verkörperungen der Erde. Da haben wir zum Beispiel die Saturnmission.",
      "Wenn Sie sich eine annähernde Vorstellung von derselben machen wollen, dann können Sie sich die­selbe verwandt denken mit dem, was menschlicher physischer Leib auf der einen Seite und menschlicher Wille auf der anderen Seite ist. Das ist so zu denken, daß, wenn es keine Saturnverkörperung unserer Erde gegeben hätte, der Wille des Menschen auf der einen Seite und sein physischer Leib auf der anderen Seite nicht hätten zu ihrer heutigen Gestaltung kommen können.",
      "Der Mensch verdankt das, was er an Wille und physischem Leib hat, dem alten Saturn. Daß er den physischen Leib dem Saturn verdankt, entnehmen wir aus der Akashachronik. Es wirkt aber auch jeder vorhergehende Zustand in den auf diesen Zustand folgenden Gestaltungen nach.",
      "Was sich daher heute kundgibt als Wille, ist zurückzuführen auf die Nachwirkung des Saturnelementes. Das wird zu dem Ergebnisse, daß vom Innern des Menschen sich dessen Wesenheit als Wille kundgibt. Von der Mission des Sonnenzustandes bekommen Sie einen Begriff, wenn Sie das, was man menschlichen Atherleib nennt, betrachten und daran anknüpfen das Fühlen.",
      "Daß der Atherleib bis auf die alte Sonne zurückgeht, wurde Ihnen schon gesagt. Die Nachwirkung wirkt aber so, daß der Mensch die inneren Kräfte des Fühlens später entwickeln konnte. Und wenn wir endlich auf den Mondzustand blicken, so sehen wir, daß der Astralleib des Menschen und das menschliche Denken an denselben gebunden ist.",
      "So daß wir sagen können: Damit diese Kräfte des inneren und äußeren Menschen -physischer Leib, Atherleib und Astralleib; Wollen, Fühlen und Den­ken - sich so haben entwickeln können, daß sie der Mensch heute als",
      "äußeres und inneres Leben besitzt, dazu waren drei aufeinanderfol­gende kosmische Missionen nötig. Und diejenigen Wesenheiten, die wir als die Wesenheiten der Hierarchien bezeichnet haben, mußten, damit die Aufgabe der drei aufeinanderfolgenden Verkörperungen unserer Erde erfüllt werden und dem Menschen verliehen werden konnte, was in seiner heutigen Konstitution zum Vorschein kommt, jedesmal in entsprechender Wechseltätigkeit zusammenwirken.",
      "Es mußte also die Mission des alten Saturnzustandes erfüllt werden, sonst hätte der Mensch nicht den Einschlag des physischen Leibes und des Wollens erhalten können. Es mußte die Mission der Sonne erfüllt werden, sonst hätte er nicht den Atherleib und das Fühlen erhalten können, und endlich mußte die Mission des Mondes erfüllt werden, sonst hätte er nicht den Astralleib und das, was wir die Kraft des Den­kens nennen, haben können. So sind die drei vorhergehenden Verkör­perungen unserer Erde insbesondere demjenigen gewidmet, was wir eines der vorherrschenden Elemente unserer eigenen, persönlichen We­senheit, unseres «Ich» nennen können. Es liegt nämlich die Tatsache vor, daß der äußere, physische Leib, der ausgeflossen ist aus dem Wesen des alten Saturn, aus den Geistern des Willens, nichts anderes darstellt, als den Willen von außen gesehen. Bei uns wirkt der Wille als Innen­leben aus dem Inneren. - Diese Worte sind ganz genau gewählt, sie sind nicht phantastisch, sondern ganz genau der Natur der Sache entspre­chend. Sie können aus ihnen viel lernen. - Die Sonnenperiode hat die Erde durchgemacht, um den Atherleib auf der einen Seite zu begründen durch den Einfluß der Geister der Weisheit, und um zu begründen auf der anderen Seite durch das Fortwirken des Elementes der Weisheit dasjenige, was die innere Weisheit reflektiert: das Gefühl. Dasjenige, was die Mondenmission war, hängt mit dem Astralleibe und mit dem Denken in ähnlicher Weise zusammen.",
      "Jetzt fragt es sich: Was haben die hauptsächlich auf der Erde wir­kenden und die Erde formenden Geister der Form für eine besondere Mission gewählt?",
      "Wir können zunächst sagen: Die Geister, die auf dem Saturn haupt­sächlich gewirkt haben, die Geister des Willens oder Throne, hatten die Mission, das Element einzuweben, das später während der Erdenentwickelung",
      "in dem Willen sich offenbart. Das ist die große Saturnmis­sion: den Willen einzuimpfen, die Willenskräfte einzupflanzen. Wenn wir so etwas betrachten, so bekommen wir Hochachtung und Respekt vor den waltenden kosmischen Mächten. Wir bekommen eine richtige Wertschätzung diesen Mächten gegenüber, wenn wir sehen, daß zu dem kunstvollen Gewebe von äußerem Willen, der in dem physischen Leibe lebt, und von innerem Willen eine besondere planetarische Mission notwendig war. Die gesamte Welt der Hierarchien mußte einen Pla­neten entstehen und wieder vergehen lassen, um das Verhältnis zu­stande zu bringen, was in uns als äußeres und inneres Willenselement eingewoben ist. Ebenso mußte die alte Sonne entstehen, um den Äther-leib und das Gefühlselement, das innere Weisheitselement entstehen zu lassen. Was sich dann in unserem Denkelement, in unserer Astralität, als inneres Gedankenelement im Menschen reflektiert, dazu war die Mondmission notwendig.",
      "Welche Mission haben nun die Geister der Form, was ist also die eigentliche Erdenmission? Wenn Sie an die Saturnmission die Einprä­gung des Willens anknüpfen, an die Sonnenmission vorzugsweise die Einprägung des Gefühiselementes, an die Mondmission vorzugsweise die Einprägung des Gedankenelementes - also dasjenige, was im menschlichen Astralleibe ist -, so hat man an den Erdenplaneten die Mission zu knüpfen, ein vollständiges Gleichgewicht dieser drei Ele­mente zu bewirken, das Gleichgewicht dieser drei Elemente herzustel­len, von denen jedes während eines der früheren Zustände unseres Planeten die Oberhand hatte, so daß im Gleichgewichtszustande zu­sammenwirken diese drei Elemente, von denen jedes die Hegemonie hatte in einer der früheren Verkörperungen der Erde. Das ist die Mission unserer Erde. Zum Stillstand zu bringen den Kampf dieser Elemente dadurch, daß sie in das richtige Gleichgewichtsverhältnis gebracht werden, das ist die Erdenmission. Der Mensch ist hineinver­woben in diese Erdenmission, um dieses Gleichgewicht zuerst in seinem eigenen Innern aus Denken, Fühlen und Wollen aufzubauen. Der Mensch war in dieser Beziehung in der Tat bei der Entstehung der Erde ein regelloses Gewebe von Denken, Fühlen und Wollen. Wie noch bei dem gegenwärtigen Menschen das innere Gleichgewicht nicht vollständig",
      "ist, sondern vielfach in Disharmonie, in Unordnung ist, das kann jeder an sich fühlen, der auch nur ein bißchen Selbsterkenntnis hat. Der Mensch ist zunächst berufen, in seinem Inneren das Gleichgewicht zwischen Denken, Fühlen und Wollen herzustellen, wodurch er von sich ausstrahlen und übertragen kann auf die Erde das, was dieses Gleichgewicht von Denken, Fühlen und Wollen bedeutet.",
      "In der okkulten Symbolik hat man immer diese Mission der Erde in ganz besonderer Weise durch eine Figur ausgedrückt. Wenn Sie alle geometrischen Figuren durchgehen, werden Sie keine finden, die dem Zusammenwirken im Sinne des Gleichgewichtes so genau entspricht, wie das gleichseitige Dreieck. Wenn Sie das gleichseitige Dreieck nur aufzeichnen, so finden Sie die drei Seiten einander gleich, die drei Win­kel einander gleich, jeder Scheitelpunkt ist gleich weit von dem anderen und alle gleich weit von dem Mittelpunkte entfernt. Der Mittelpunkt von dem gleichseitigen Dreieck ist ein absolutes Symbolum für das Gleichgewichtswirken, so daß, wenn der Okkultist das Dreieck an­schaut, er in demselben ein Symbolum sehen kann für das absolut equilibrierte Zusammenwirken dessen, was in den drei früheren Ver­körperungen unserer Erde jeweilig die Hegemonie hatte. Die Taten des Ich in dem Menschen bedeuten nichts anderes als das Schaffen eines tätigen, eines aktiven Mittelpunktes in der Menschennatur, wodurch dieser Gleichgewichtszustand von innen heraus vorbereitet werden kann. So ist in der Tat der Mensch zu Großem berufen auf unserer Erde, nämlich dazu, von innen heraus durch seine ganze Wesenheit zunächst das Gleichgewicht dessen zu bewirken, was früher in der ver­schiedensten Weise und zu verschiedenen Zeiten jeweilig vorherrschend war.",
      "Das ist zunächst eine recht abstrakte Definition unserer Erdenmis­sion, aber diese besteht einmal in dem Gesagten. Das Geheimnis dieser Mission spricht sich dadurch aus, daß durch dieses Zusammenwirken, durch dieses Gleichgewicht der drei Kräfte das Innere tatsächlich pro­duktiv Neues wirkt. Es wird dadurch wahrhaft ein viertes Element erzeugt zu den drei vorhergehenden, und dieses vierte Element ist das Element der Liebe. Die Liebe kann im Weltgetriebe sich nur entwickeln, wenn ein absolutes Gleichgewicht der drei in früheren Zeiten abwechselnd",
      "die Hegemonie führenden Kräfte eintritt. - Darüber werden wir in den nächsten Tagen noch mehr zu sprechen haben. Vorläufig nehmen Sie das als abstrakte Charakteristik hin.",
      "So ist unser Planet der Planet der Liebe, und deshalb ist sozusagen dieses Gleichgewicht, das sich herausstellt in dem Zusammenwirken dieser drei Kräfte, in seinem Ergebnis Liebeswirken, und Liebeswirken soll durch alle folgenden Verkörperungen der Erde, gerade durch die Mission des Erdenwirkens hineinverwoben werden in die gesamte Evo­lution. Dadurch wird die Dreiheit zu einer Vierheit, und diese Vierheit beginnt mit ihrem vierten Element auf der untersten Stufe, beginnt sozusagen mit der niedersten Form der Liebe, die geläutert und gereinigt wird bis zu dem Grade, daß am Ende der gesamten Erdenentwickelung die Liebe als ein völlig gleichberechtigtes Element erscheinen wird. Die Mission des Gleichgewichtes für unseren Erdenplaneten erfüllen, heißt also im Grunde genommen: die Dreiheit zu einer Vierheit machen. Des­halb wird auch das Geheimnis des Erdendaseins gewöhnlich okkult ausgesprochen mit den Worten «Die Dreiheit zur Vierheit machen». Das vierte Element ist natürlich heute noch sehr unvollkommen. Es wird aber, wenn die Erde ihre Mission erfüllt haben wird, ebenso hell-glänzend sein wie das heilige Dreieck, das uns mit seiner Gleichge­wichtslage als das höchste Symbolum, das wir für unser Erdenideal haben, vorleuchtet, insofern wir uns an die Vergangenheit der Erde erinnern.",
      "Es ist dieses Zusammenwirken der Elemente von Denken, Fühlen und Wollen im Innern des Menschen zunächst so, daß dieses eigentliche Innere zur Substanz der Liebe wird. Das ist dasjenige, was man das eigentlich Produktive, das innerlich Produzierende im Erdendasein nennen kann. Deshalb muß man die Geister der Form in ihrer Gesamt­heit, weil sie gerade diese Mission haben, die drei früheren Zustände ins Gleichgewicht zu bringen, zugleich als die Geister der Liebe be­zeichnen.",
      "Wenn wir so das Erdendasein betrachten, dann haben wir zunächst charakterisiert das Wollen, Fühlen und Denken und das Liebeswirken außerhalb unseres Erdenplaneten, und wir haben als besondere Auf­gabe der Geister der Form die Einimpfung, die Einprägung der Liebe,",
      "die das Resultat des Gleichgewichtes ist, bezeichnen können. Darin besteht also die Gesamtmission der Erde. Um diese die Erde durchdrin­gende Kraft der Liebe zustande zu bringen, dazu ist das Ineinander­wirken und Ineinanderarbeiten alles dessen notwendig, was wir als die Arbeit der niedersten Hierarchien bezeichnet haben. Wie wir schon in unserer vorhergehenden Betrachtung angefangen haben zu charakteri­sieren, muß dadurch sozusagen das Netz der Liebe gewoben werden, und es muß dieses Gewebe der Liebe so gewoben werden, daß die Hauptfäden hineingewoben werden - weil das ihrer Grundmission entspricht - durch die normalen Geister der Form. Dann weben hinein die abnormen Geister der Form, die eigentlich Geister der Bewegung sind, das, was die Rassen gibt. Dann weben die normalen und abnormen Zeitgeister die geschichtliche Entwickelung hinein, und dann weben die Erzengel mit normaler und abnormer Entwickelung die einzelnen Volks- und Sprachen-Entwickelungen hinein, und endlich wirken hin­ein die Wesen, welche den Menschen an den richtigen Platz auf der Erde stellen, die Engel. So wird dieses gewaltige Netz der Liebe gewo­ben. Das, was als Netz der Liebe, als die eigentliche Erdenmission, gewoben wird, das ist aber nur als Abglanz, als Maja in unserer Erde sichtbar.",
      "Das nächste Gebiet über der physischen Welt, wo dieses Netz gese­hen werden kann, ist die astralische Welt. Aber immer klarer und klarer sieht man das Arbeiten der Hierarchien an den Wahrheiten, die unserer äußeren Maja zugrunde liegen, wenn man sich erhebt aus der astrali­schen Welt in die Welt des niederen und höheren Devachan. Dann sieht man, wie dieses Gewebe gesponnen wird. Erhebt man sich zur Astral­welt, dann erblickt man allerdings zunächst dasjenige noch nicht, was hauptsächlich von innen spinnt, nämlich die Geister des Willens, die Cherubim und Seraphim. Wenn der Mensch diese Geister bei ihrer Arbeit finden will, dann muß er sich zum Schauen in noch höhere Welten erheben. Aber eines finden wir schon in der astralen Welt: das, was wir die abnormen Geister der Form nennen, welche, wenn sie eine normale Entwickelung erlangt hätten, von außen weben sollten. Wir haben gesehen, daß die Geister der zweiten Hierarchie von außen weben sollen; hier aber sehen wir, daß sie von innen weben. Wir können",
      "also sagen: In dieses Netz, in dem von außen weben die Geister der Bewegung, die Geister der Form und die Geister der Weisheit, von innen die Geister des Willens, die Seraphim und Cherubim, weben auch noch von innen Wesenheiten, die eigentlich von außen weben müßten. Sie weben aber unter der Oberfläche so, wie etwa der Seiden-wurm den Cocon webt.",
      "Innerlich ist das, was zunächst in der Astral-welt gesehen wird. Diese eigenartigen Geister der Bewegung, die depla­zierte, gestürzte Geister sind, sie sind das nächste, was sichtbar wird von diesen in der geistigen Erdenatmosphäre webenden und wogenden geistigen Wesenheiten.",
      "Diese geistigen Wesenheiten, die das erste sind, was auf dem Astralplan zunächst sichtbar wird, noch bevor dasjenige, was normalerweise auftritt, die Engelwesen oder Angeloi sichtbar werden, sind für das hellseherische Schauen eigentlich - trotzdem sie für die Erzeugung der Rassen im tiefsten Sinne notwendig sind - doch in gewisser Weise die verführerischen Geister. Diese Geister, von wel­chen jeder wieder viele unter sich hat - weil jeder viele geistig unter­geordnete Wesen erzeugt -, sind in der geistigen Welt eingehüllt in eine Summe von geistigen Wesenheiten, die immer unter den betreffen­den Hierarchien stehen.",
      "Auch die höheren Geister haben solche unter ihnen stehende Wesenheiten; die Geister des Willens: die Undinen; die Cherubim: die Sylphen; die Seraphim: die Salamander. Aber auch diese abnormen Geister der Form, die eigentlich Geister der Bewegung sind, die wie eine Art häßlicher geistiger Wesen auf dem astralischen Plane erscheinen, haben ihre untergeordneten Geister.",
      "Sie sind die Gei­ster, welche weben und leben in dem, was mit dem Entstehen der menschlichen Rassen zusammenhängt, was also beim Menschen mit dem zusammenhängt, sozusagen an dem Elemente hängt, das wir als das erdgebundene charakterisiert haben, als das mit der Fortpflanzung zusammenhängende und dergleichen. Das sind Wesenheiten, das ist überhaupt ein Terrain, welches zu den buntesten und gefährlichsten der astralischen Welt gehört, und es ist leider das Terrain - an dieser Stelle kann es am besten im Zusammenhange gesagt werden -, das von den­jenigen, die auf eine unrichtige Weise zum Schauen kommen, am aller-leichtesten gefunden werden kann.",
      "Am leichtesten kommt das Heer derjenigen Geister, die mit der Fortpflanzung der Rasse zu tun haben",
      "und dienende Glieder derselben sind, zum Vorschein. Mancher, der vorzeitig und auf unrichtige Weise sich in das okkulte Gebiet hinein-begeben hat, hat es teuer dadurch bezahlen müssen, daß ihm das Heer dieser geistigen Wesenheiten ohne die Harmonisierung durch andre geistige Wesen entgegentrat.",
      "So haben wir hineinleuchten können in das, was am Realen spinnt und webt, um das Gewebe zu weben, aus dem dann die eigentliche see­lische Welt des Menschen sich entfaltet. Wie diese Grundlage, in die wir jetzt ein wenig hineingeschaut haben, in der Rassen-, in der Volks-entstehung und so weiter zum Vorschein kommt, davon wollen wir morgen weiter sprechen."
    ],
    "sentences": [
      [
        "Aus dem gestrigen Vortrage wird hervorgegangen sein, daß allerdings notwendig ist zum vorurteilsiosen Eindringen in die Tatsachen, welche dieser Betrachtung zugrunde liegen, ein gewisses Sichhinwegsetzen über alles dasjenige, was sonst leicht an Gefühlen, an Empfindungen den Menschen gerade von jener Seite her durchdringt, die wir jetzt objektiv charakterisieren müssen.",
        "Solange man noch irgendwie geneigt ist, eine objektive Charakteristik dieser oder jener Rasse, dieses oder jenes Volkstums oder dergleichen persönlich zu nehmen, so lange wird ein vorurteilsfreies Verständnis der Tatsachen gerade dieses Vortragszy­klus schwer zu erreichen sein."
      ],
      [
        "Damit hängt es auch zusammen, daß über diese Dinge auf keinem anderen Boden als auf dem Boden der Geistes­wissenschaft gesprochen werden kann.",
        "Denn was man auch hören soll über die Charaktere dieses oder jenes Volkstums, und wie sehr man auch deshalb, weil man doch innerhalb irgendeiner Rasse, innerhalb eines Volkstums steht mit seinen Empfindungen, Gefühlen und so weiter, dabei sein könnte, man hat ein genügendes Gegengewicht als Geisteswissenschafter, um es in die andere Waagschale zu legen."
      ],
      [
        "Das ist die wirklich verstandene Lehre von dem Karma und der Reinkar­nation.",
        "Sie bietet uns ja einen Ausblick darauf, daß wir mit dem inner­sten Kern unseres Wesens in den aufeianderfolgenden Zeiten in den verschiedensten Rassen, in den verschiedensten Völkern inkarniert werden."
      ],
      [
        "So können wir also gewiß sein, wenn wir auf diesen Kern unseres Wesens schauen, daß wir mit ihm teilnehmen werden nicht nur an den Sonnen- oder vielleicht auch Schattenseiten aller Rassen, aller Volkstümer, sondern wir können gewiß sein, daß wir in unserem inner­sten Wesen aufnehmen Beitrag auf Beitrag der Segnungen aller Rassen und Volkstümer, indem wir einmal da, einmal dort inkarniert werden."
      ],
      [
        "Es wird unser Bewußtsein, unser Horizont weiter, umfassender durch diese Ideen von Karma und Reinkarnation.",
        "Deshalb lernen wir erst durch sie dasjenige ertragen, was in unserer Gegenwart über die Ge­heimnisse der Rassen- und Volkszusammenhänge vor unser geistiges"
      ],
      [
        "Auge treten muß.",
        "So wird denn gerade durch das in dieser Betrachtung Abgehandelte, wenn es richtig erkannt wird, ein Unbefriedigtsein über das Inkarniertwerden in diesem Volke oder jener Rasse nicht in uns hineingebracht werden können.",
        "Es wird aber trotzdem ebenso in die Menschheit durch ein solches objektives Anschauen der menschlichen Volks- und Rassencharaktere Unfrieden und Disharmonie hereinge­bracht werden können, wenn es nicht mit den angedeuteten Voraus­setzungen aufgenommen wird.",
        "Der geistig Strebende wird durch die Lehre von Karma und Reinkarnation lernen, wie jedes - und sei es auch das kleinste Volk - seinen Beitrag zu liefern hat zu der Gesamtentwik­kelung der Menschheit.",
        "Das wird gerade das Bedeutungsvolle sein, daß in dem zweiten Teile dieser Vorträge gezeigt werden wird, wie die einzelnen Einflüsse der Völkermissionen in die Gesamt-Menschheit einfließen, und wie sogar einzelne Volkssplitter, die da und dort in die großen Volksmassen zerstreut sind, ihre Bedeutung haben in der Ge­samtharmonie der Menschheitsevolution.",
        "Das aber wird nur allmählich vor unser geistiges Auge hintreten können."
      ],
      [
        "Wir werden uns - um ein volles Verständnis für die Charaktere der einzelnen Volksseelen zu gewinnen - an solche Beispiele halten müssen, die uns in gewisser Beziehung auf der einen Seite klarer sind als die Volkscharaktere der Gegenwart, innerhalb welcher wir mit unserer Zivilisation selber leben, und wir werden uns auf der anderen Seite vielleicht mit solchen Volkscharakteren beschäftigen müssen, die uns der Zeit nach etwas ferner liegen, damit wir uns ein Verständnis dafür erwerben, wie man überhaupt Volkscharaktere, Volksmissionen ver­stehen kann.",
        "Damit haben wir ja zunächst nur im allgemeinen das Rassenhafte, das Volksmäßige charakterisiert."
      ],
      [
        "Daß wir im Laufe der letzten Vorträge gefunden haben, daß in einer Rasse zusammenwirken müssen sozusagen ein normaler und ein abnor­mer Geist der Form, daß innerhalb eines Volkes ein in seiner normalen Entwickelung begriffener und ein in abnormer Entwickelung begrif­fener Erzengelgeist wirken müssen, das hat uns sozusagen verständlich gemacht, wie die Wesenheiten, die wir als die geistigen Hierarchien kennen gelernt haben, in die Evolution eingreifen."
      ],
      [
        "Jetzt fragen wir uns: Wie wirken denn die geistigen Wesenheiten"
      ],
      [
        "höherer Art in das Konkrete hinein?",
        "Da wird es gut sein, wenn wir uns heute dadurch eine Grundlage schaffen, daß wir uns überhaupt ein Verständnis erwerben über die Hierarchien, zu denen, wie wir wissen, der Mensch als unterstes Glied gehört.",
        "Erinnern Sie sich an dasjenige, was wir bereits gehört haben, so wissen Sie, daß wir diese Hierarchien so auffassen, daß wir sagen: Auf der untersten Stufe steht der Mensch. -Unter ihm liegen die drei Naturreiche: Tierreich, Pflanzenreich, Mine­ralreich. - Dann kommen die Engel, dann die Erzengel, dann die Ur-kräfte oder Archai.",
        "Das ist dasjenige, was wir bezeichnen können als die erste der Hierarchien, vom Menschen aufsteigend.",
        "Die zweite der Hierarchien ist die folgende:"
      ],
      [
        "Geister der Form - Gewalten"
      ],
      [
        "Geister der Bewegung - Mächte"
      ],
      [
        "Geister der Weisheit - Herrschaften"
      ],
      [
        "Sodann haben wir noch die höchste der drei Hierarchien:"
      ],
      [
        "Geister des Willens - Throne"
      ],
      [
        "Cherubim"
      ],
      [
        "Seraphim"
      ],
      [
        "Nun fragen wir uns einmal: Da alle geistigen Wesenheiten sich irgendwie offenbaren, so daß sie im Bereiche der Maja oder Illusion, also im Bereiche der Sinnenwelt irgendwo erscheinen, wo können wir sie auf der untersten Stufe der Offenbarung, auf der Stufe der Täu­schung aufsuchen?",
        "Der Mensch in seiner gewöhnlichen Natur- und Geistesbetrachtung kennt ja nur das Gebiet der Maja oder Illusion, die alleräußerste Außerung dieser geistigen Wesenheiten.",
        "Ich will Ihnen an einem Beispiele zeigen, wie der Mensch eigentlich nur die alleräußerste Manifestation, die alleräußerste Offenbarung dieser Wesen kennt."
      ],
      [
        "Der Mensch geht zum Beispiel mit seinen Füßen über nordischen Felsengrund.",
        "Da wird er nun zunächst darüber sagen: Da ist Materie ausgebreitet, und er wird dieses dichte Felsengestein, über das er dahin-schreitet, so beschreiben, wie er es zunächst sieht und es in seiner gewöhnlichen Sprache «harte Gesteinsmaterie» nennen.",
        "Derjenige, der eindringt in das Wesen der Dinge, sieht in dieser Gesteinsmaterie etwas"
      ],
      [
        "ganz anderes.",
        "Was ist das eigentlich, worauf wir auftreten und was uns Widerstand bietet?",
        "Das, wovon der Mensch glaubt, daß es da sei, das ist gar nicht da, das ist eine Täuschung.",
        "Die äußerste Oberfläche unserer Erde ist lediglich eine Täuschung."
      ],
      [
        "Die Wahrheit ist diese, daß Kräfte von unten heraufwirken, die wiederum nichts anderes sind als Kräfte, die von gewissen Wesenheiten ausströmen, so daß wir also sagen kön­nen: Wir sehen in einem solchen Stück Boden dasjenige vor uns, was sich zunächst als eine Kraft darstellt, die aus der Erde heraus nach allen Seiten hin wirkt.",
        "Diese Kräfte sind wirklich da und strahlen nach allen Seiten in den Raum hinaus."
      ],
      [
        "Der Mensch könnte allerdings nicht auf der Erde herumgehen, wenn nur diese Kräfte da wären.",
        "Diese Kräfte allein würden den Menschen mit rasender Schnelligkeit in den Raum hinaus­schleudern.",
        "Daß er auf festem Boden stehen kann, das verdankt er dem Umstande, daß aus dem Weltenraum von allen Seiten andere Kräfte hereinstrahlen."
      ],
      [
        "Immerfort begegnet sich die Sphäre der hereinstrahlen-den Kräfte mit derjenigen der herausstrahlenden Kräfte, und da, wo sie zusammenkommen, bilden sie sozusagen eine Grenze, und das ist die Oberfläche der Erde.",
        "So ist das, was man sieht als Oberfläche, nur eine Täuschung, die das Ergebnis von ein- und ausstrahlenden Kräften ist, welche so wirken, daß sie sich gerade an der betreffenden Oberfläche gegenseitig aufhalten."
      ],
      [
        "Was da herausströmt, ist im wesentlichen das­selbe, was wir die Wirkungen der Throne, die Wirkungen der Geister des Willens nennen müssen.",
        "Diese Geister strahlen von der Erde nach allen Seiten hin ihre Kräfte aus, und dasjenige, was von dem Welten-raum hereinkommt, das ist im wesentlichen das, was man nennen kann einstrahlende, hereinarbeitende Kräfte von gewissen Geistern der Be­wegung."
      ],
      [
        "Diese beiden Arten von Kräften begegnen sich also hier, und dieses Zusammenwirken der Throne mit den Geistern der Bewegung -dadurch, daß die Throne in ihrer Wirkung aufgehalten werden von den Geistern der Bewegung - gibt die verschiedenartig konfigurierte Ober­fläche, so daß das, was Sie draußen als Erdoberfläche sehen, das Un­wahrhaftigste, die äußerste Täuschung ist.",
        "Das, was wirklich da ist, ist ein Ausgleich von Kräften und gleichsam ein Vertrag zwischen den Geistern des Willens und den Geistern der Bewegung, der so geschlossen wird, daß er die Erde in der verschiedensten Weise konfiguriert."
      ],
      [
        "Allerdings würde das immer noch nicht hinreichen, daß unsere Erde, so wie sie jetzt gerade ist, sich als ein solcher Planet bilden könnte.",
        "Das Gegeneinanderwirken der Geister des Willens und der Geister der Be­wegung würde dazu noch nicht hinreichen.",
        "Das würde noch etwas ganz anderes geben.",
        "Wenn nämlich bloß die Geister des Willens vom Innern der Erde heraus wirken würden und nur einen Widerpart in den Gei­stern der Bewegung hätten, dann würde die Erde in fortwährendem Flusse, in einem fortwährenden inneren Strome sein.",
        "Der Planet würde noch nicht an irgendeiner Stelle zur Ruhe kommen können.",
        "Er wäre dann zwar nicht so flüssig wie das heutige Meer, er würde ein nicht so leicht wellenwerfendes und wellenbildendes Element sein wie das Was­ser, würde aber in einer dichteren Masse Wellen werfen und bilden."
      ],
      [
        "Wenn Sie sich eine Vorstellung davon machen wollen, wie die Geister des Willens und die Geister der Bewegung ursprünglich zusammen-wirkten, so möchte ich Ihnen ein Beispiel geben und Sie bitten, mich etwas auf der Landkarte zu begleiten.",
        "Da möchte ich zunächst auf die Alpen hinweisen, die heute ein festes Berggerippe sind, so daß wie ein fester Gesteinsboden das Alpenmassiv die italienische Halbinsel im Süden von den anderen europäischen Gebieten abtrennt.",
        "Wie ist diese Alpenkette nun eigentlich zustande gekommen?",
        "Es gab eine Zeit - sie liegt weit in urferner Vergangenheit zurück -, da war das Alpenmassiv überhaupt noch nicht da, aber nord- und westwärts hin, da waren bereits ältere Erhebungen, die damals schon fest geworden waren.",
        "Zäh-flüssige Wellen waren es, die dann von Süden herauf aufgeworfen wurden, so daß wir uns die Sache so vorstellen können:"
      ],
      [
        "Hier bei A würden wir das Böhmische Plateau haben.",
        "Dann wollen Sie sich vorstellen, daß von Süden herauf eine mächtige Welle geworfen wurde, die sich nach rechts gegen das Böhmische Plateau und nach links gegen das französische Zentralplateau hinüber spaltete und verbreitet hat."
      ],
      [
        "Diese mächtige Welle bildete also in uralten Zeiten dieses Alpen-massiv.",
        "Selbst aus einer populären Vorstellung kann sich dies ergeben.",
        "Wer einmal auf einem Bergesgipfel der Alpen gestanden hat und die eigentümliche Konfiguration der Alpenkette überblickt, der sieht -wenn er es auch nicht wüßte - das, was die Geisteswissenschaft längst festgestellt hat und die heutigen Geologen sogar feststellen: die eigen­artige Wellenbildung, die in der Zeit, als die Urmasse der Erde noch in einem zähflüssigen Zustande war, stattgefunden hat."
      ],
      [
        "So würde sich durch das Zusammenwirken der Geister des Willens und der Geister der Bewegung die Erde heute noch gestalten, wenn nicht ein anderes Wirken eingetreten wäre, ein Wirken, das außerordentlich nachhaltig ist, und das sich auf unserer Erdoberfläche dadurch äußert, daß den Willenskräften, die mit den Geistern der Bewegung zusammenwirken, dasjenige eingegliedert wird, was wir eben die Geister der Form nennen.",
        "Sie können sich also vorstellen, daß diese Geister der Form, gleichsam auf den Wellen tanzend, die bewegten Massen zur Ruhe bringen, in Formen gießen, so daß wir also ein Zusammenwirken von dreierlei Kräften zu verzeichnen haben."
      ],
      [
        "Diese drei Kräfte führen auf dreierlei Wesenheiten zurück.",
        "Auf der einen Seite sehen Sie wirken die Geister der Form, die sowohl nach oben als nach unten, sowohl in die Sphäre der Geister des Willens als auch in die Sphäre der Geister der Bewegung hineinwirken."
      ],
      [
        "Über ihnen sind die Geister der Bewegung, unter ihnen die Geister des Willens. - Dasjenige, was auf unserer Erde äußerlich vorzugsweise als flüssiges Element erscheint - allerdings nicht unser heutiges Wasser, sondern das alte flüssige Element, das durch die Gei­ster der Form zur Ruhe gebracht worden ist -, das müssen wir als die äußerste Manifestation der Geister des Willens oder der Throne auf­fassen.",
        "Immer aber mischt sich in dieses Wirken ein anderes Element hinein; es wird sozusagen den Geistern des Willens oder Thronen Hilfe geleistet von den Cherubim und Seraphim."
      ],
      [
        "Von den Cherubim wird Hilfe geleistet im Elemente der Luft, in allem, was als Luftförmiges die"
      ],
      [
        "scheinbare Materie der Erde durchdringt.",
        "Luft ist gleichsam eine Illu­sion, und dahinter stehen die mächtigen Wesenheiten, die wir Cherubim nennen.",
        "Die Seraphim wirken in dem, was wir als Wärme kennen, hin­ter allem, was irgend als Wärme vorhanden ist."
      ],
      [
        "Wir blicken damit auf das hin, was in unserem Planeten durch Aus­strahlen von innen heraus aus dem Mittelpunkte bewirkt wird.",
        "Wir können also sagen: Unser Planet ist so zusammengesetzt, daß aus seinem Mittelpunkt heraus wirken die Geister des Willens oder Throne, die Cherubim und Seraphim.",
        "Wir müssen unseren Planeten so auffassen:"
      ],
      [
        "Wo die Luft- und Wärmegrenze desselben ist - das Luftmeer gehört ebenso zu unserem Planeten wie das Wasser oder die feste Erde -, da wird gleichsam eine Oberfläche gebildet.",
        "Auf dieser Oberfläche tanzen förmlich auf den Wellen und bringen sie zur Ruhe, zur Form, die Geister der Form.",
        "Aus diesem Grunde wurde ihnen der Name gegeben, weil sie das zähflüssige Element zur Ruhe bringen.",
        "Hinter ihnen stehen die Geister der Bewegung.",
        "In deren Element mischt sich wieder das­jenige, was wir die Geister der Weisheit nennen.",
        "So daß wir, wenn wir gegen den Mittelpunkt unseres Planeten hinblicken, sagen können: Da sind erhabene Wesenheiten, Throne, Cherubim, Seraphim. - Blicken wir hinaus, so schauen wir zunächst durch die Sphäre der Geister der Form, die Luft und Wärme durchdringen mit ihrem Element, auf die Geister der Bewegung und die Geister der Weisheit.",
        "Alles, was wir an Naturkräften und Erscheinungen haben, wenn wir den Blick hinaus­richten in den Umkreis unserer Erde, wenn wir hinaufschauen in Him­melshöhen, das ist im wesentlichen der zweiten Hierarchie zuzuschrei­ben.",
        "Alles, was wir erblicken, wenn wir in die Tiefen der Erde hinunter-schauen, das schreiben wir den Wesenheiten zu, die wir als die dritte Hierarchie bezeichnet haben.",
        "Das eigentümliche Zusammenwirken der zweiten und dritten Hierarchie, das gibt die Konfiguration unserer Umgebung."
      ],
      [
        "In welchem Naturelement - wir haben die drei Naturelemente Wasser, Luft, Feuer als mit den Geistern des Willens, den Cherubim und Seraphim in Verbindung stehend angeführt - geben sich nun die Geister der Form kund?",
        "Das sind die nächsten Wesen, die auf der Ober­fläche tanzen, auf der wir weben, leben und sind.",
        "Sie kommen aus dem"
      ],
      [
        "Weltenraum herein, entfalten aber ihre Kraft nun in dem, was aus der Erde heraufströmt.",
        "Für unsere Beobachtung sind sie konzentriert in dem, was wir die ausstrahlenden Sonnenstrahlen nennen.",
        "Das Licht ist also das Element, in dem die Geister der Form zunächst weben und leben.",
        "Indem aber die Lichtwirkungen mit alle dem, was sie enthalten, sich an der Grenze, wo die Geister der Bewegung und die Geister des Willens zusammenwirken, entfalten, da werden die festen Formen erzeugt."
      ],
      [
        "Der Mensch hat zunächst keine Organe, um auch in das hinaufblik­ken zu können, was jenseits jener Kräfte des Lichtes - die wir auch die Geister der Form nennen - liegt, keine Organe, um in das hineinblicken zu können, was in das Licht hineinverwoben ist.",
        "Alles, was auf unserer Erde Zersetzungen und Zusammensetzungen bedingt, alles was als che­mische Kräfte auf derselben wirkt, ist hier noch in das Licht hineinver­woben, und das ist im wesentlichen das Terrain, auf dem die Geister der Bewegung tätig sind.",
        "Wenn der Mensch etwas wahrzunehmen lernt von dem, was er sonst nur als Maja in der Wirkung der chemischen Zusammensetzungen und Auflösungen sieht, dann hört er diese Geister der Bewegung, dann nimmt er die Sphärenmusik wahr, von der die pythagoräische und andere Geheimschulen sprechen.",
        "Das ist auch das, was Goethe beschreibt, wenn er von der Sonne nicht als der Lichtspen­derin spricht, sondern sagt: «Die Sonne tönt nach alter Weise in Bru­dersphären Wettgesang, und ihre vorgeschriebne Reise vollendet sie mit Donnergang.»"
      ],
      [
        "Diese Sphärenmusik ist auch jetzt immer noch da, nur daß sie das gewöhnliche Bewußtsein nicht hört.",
        "Sie ist wirklich, diese Sphären-musik, die allen Menschen als astralische Wirkung von außen entgegen­kommt.",
        "Der Mensch hört sie nur nicht.",
        "Würde er in bezug aufdiese Sphärenmusik einen eben solchen Wechsel haben wie beim Licht, das er zu gewissen Zeiten, beim Eintreten der Dunkelheit, nicht sieht, dann würde er sie zu gewissen Zeiten auch hören.",
        "Sie tönt aber Tag und Nacht, und daher kann er sie nur dann hören, wenn er eine gewisse okkulte Schulung, eine gewisse okkulte Entwickelung durchmacht.",
        "Während das Licht uns während des Tages als Licht zuströmt und während der Nacht als aufgenommenes, absorbiertes Licht weiterwebt,"
      ],
      [
        "tönt die Sphärenmusik Tag und Nacht.",
        "Es ist für den Menschen damit so wie bei dem Müller, der die Mühle nur dann hört, wenn sie stille steht."
      ],
      [
        "Es gibt außerdem noch die Geister der Weisheit, die von außen ihre Wirkungen hereinsenden und die hineinwirken in das webende Licht und die den Raum durchwebende Sphärenmusik.",
        "Das ist das auf die Erde einstrahlende Leben des Weltenäthers.",
        "Leben strömt vom Welten-raum auf die Erde ein und wird von den Wesen aufgefangen.",
        "Das kommt von den Geistern der Weisheit."
      ],
      [
        "So blicken wir in Weltenfernen und sehen zunächst zu der Sonne auf, in der diese Kräfte für uns konzentriert sind und sehen, wie aus dem Raume hereindringt strömendes Leben, webender Ton, Jormendes Licht, die Dreiheit der zweiten Hierarchie.",
        "Von unten herauf strömt uns die höchste der Hierarchien zu, die Seraphim, Cherubim und Throne.",
        "Hineinverwoben in all das Wirken über die Erde hin, mehr im Innern der Wesen wirkend, ist die erste Hierarchie.",
        "Dazu gehören zunächst die Archai, die als Zeitgeister wirken.",
        "Diese Zeitgeister weben in dem, was ihnen von den höheren Hierarchien zubereitet worden ist, und bewirken das, was wir unsere menschliche Geschichte, die Kultur-evolution auf der Erde nennen.",
        "Dann finden wir im Umkreise die Erz­engel, die Geister der Volksstämme und endlich die Vermittler zwischen dem einzelnen Menschen und den Erzengeln: die Engel."
      ],
      [
        "Wir können also sagen: In den Naturkräften, die wir auf dem Erd­planeten haben, in Erde, Wasser, Luft und Feuer strömen aus die Wesenheiten der dritten Hierarchie und strömen entgegen dem Wirken der Geister der Form, die von außen kommen.",
        "Von außen strömen die Wesenheiten der zweiten Hierarchie herein, und im Umkreis der Erde sind die Wesenheiten der ersten Hierarchie, welche sozusagen vorläufig diejenige ist, welche die schwächsten Kräfte hat.",
        "Denken Sie sich nur einmal, was für starke Kräfte die erhabenen Wesenheiten haben, welche wir die Geister des Willens nennen, die eigentlich den Boden meißeln, auf dem wir herumgehen.",
        "Dann haben wir diejenigen Kräfte, die von außen hereinströmen.",
        "Nehmen wir die uns am nächsten stehenden, die Geister der Form, welche die Massen plastisch modellieren.",
        "Sodann haben wir das, was intim in die menschliche Seele wirkt, das, was wir"
      ],
      [
        "die Engel, Erzengel und Archai nennen. - In der dritten Hierarchie haben wir also diejenigen Naturkräfte, die wir als die stärksten, als die Untergrund-Naturkräfte, als die Kräfte unserer Erdfeste kennen.",
        "In der zweiten haben wir diejenigen Kräfte, die um uns im Atherelement leben und weben, und in der ersten Hierarchie haben wir dasjenige, was uns selber intim durchlebt und durchwebt."
      ],
      [
        "Wenn wir diese drei Hierarchien in ihrem Zusammenwirken nehmen und sehen, wie sie wirken in unserem Erdplaneten, wie sie ihn aus dem gesamten Mutterschoß des Weltenalls herausgestalten, dann bekommen wir einen Begriff von dem, was notwendig war, um diese Erde zustande zu bringen.",
        "Die Erde mußte durch verschiedene Verkörperungen hin-durchgehen, bevor sie Erde werden konnte: durch den Saturn-, den Sonnen- und den Mondzustand.",
        "Wenn Sie die Darstellungen in meiner Schrift zur «Akashachronik» und in meiner «Geheimwissenschaft» verfolgen, so werden Sie sehen, daß schon während früherer Verkör­perungen unserer Erde diese verschiedenen geistigen Wesenheiten zu­sammengewirkt haben, nur daß dieses Zusammenwirken in einer von der gegenwärtigen verschiedenartigen Weise stattgefunden hat.",
        "Jedes­mal, wenn eine neue Verkörperung auftrat, also Saturn-, Sonnen-, Mond- und Erdenzustand, gab es eine andere Art des Zusammenwir­kens dieser hierarchischen Wesenheiten, weil nämlich jeder dieser Zustände, durch die unsere Erde hindurchgegangen ist, eine besondere Aufgabe darstellt, die sich diese hierarchischen Wesenheiten setzten.",
        "Wir können durchaus davon sprechen, daß jeder der Zustände, die unsere Erde durchgemacht hat, und die Zustände, die sie noch durch­machen wird, eine besondere Mission in der kosmischen Entwickelung bedeuten und bedeutet haben."
      ],
      [
        "Es ist nun außerordentlich schwierig - denn alle Begriffe ändern sich von Planetenzustand zu Planetenzustand - zu definieren, was die Mission der alten Saturn-, der alten Sonnen-, der alten Mondepoche war.",
        "Es ist dies nicht leicht, weil man zunächst die Mission unserer Erde sehr abstrakt charakterisieren muß.",
        "Man bekommt am leichtesten eine Vorstellung davon, wenn man sich vergegenwärtigt, wie die verschie­denen Kräfte beschaffen sind, die im Weltenraum sich offenbaren.",
        "Nun haben Sie, wenn Sie auf das menschliche Innere, auf das Seelenleben"
      ],
      [
        "schauen, Wollen, Fühlen und Denken, und wiederum haben Sie, wenn Sie auf die menschlichen Hüllen blicken, auf das Außere der Menschen-natur, physischen Leib, Atherleib und Astralleib, so daß Sie, wenn Sie den heutigen Menschen anschauen und von seinem Ich zunächst ab­sehen, ihn als ein Gewebe auffassen können des physischen, Ather- und Astralleibes, in das hineingewoben sind - wie in eine äußere Hülle -Wollen, Fühlen und Denken."
      ],
      [
        "Nun sind diese Kräfte im Menschen, sowohl im äußerlichen wie im inneren Menschen, immer verwandt mit irgendwelcher früheren Mis­sion, die gebunden war an frühere Verkörperungen der Erde.",
        "Da haben wir zum Beispiel die Saturnmission."
      ],
      [
        "Wenn Sie sich eine annähernde Vorstellung von derselben machen wollen, dann können Sie sich die­selbe verwandt denken mit dem, was menschlicher physischer Leib auf der einen Seite und menschlicher Wille auf der anderen Seite ist.",
        "Das ist so zu denken, daß, wenn es keine Saturnverkörperung unserer Erde gegeben hätte, der Wille des Menschen auf der einen Seite und sein physischer Leib auf der anderen Seite nicht hätten zu ihrer heutigen Gestaltung kommen können."
      ],
      [
        "Der Mensch verdankt das, was er an Wille und physischem Leib hat, dem alten Saturn.",
        "Daß er den physischen Leib dem Saturn verdankt, entnehmen wir aus der Akashachronik.",
        "Es wirkt aber auch jeder vorhergehende Zustand in den auf diesen Zustand folgenden Gestaltungen nach."
      ],
      [
        "Was sich daher heute kundgibt als Wille, ist zurückzuführen auf die Nachwirkung des Saturnelementes.",
        "Das wird zu dem Ergebnisse, daß vom Innern des Menschen sich dessen Wesenheit als Wille kundgibt.",
        "Von der Mission des Sonnenzustandes bekommen Sie einen Begriff, wenn Sie das, was man menschlichen Atherleib nennt, betrachten und daran anknüpfen das Fühlen."
      ],
      [
        "Daß der Atherleib bis auf die alte Sonne zurückgeht, wurde Ihnen schon gesagt.",
        "Die Nachwirkung wirkt aber so, daß der Mensch die inneren Kräfte des Fühlens später entwickeln konnte.",
        "Und wenn wir endlich auf den Mondzustand blicken, so sehen wir, daß der Astralleib des Menschen und das menschliche Denken an denselben gebunden ist."
      ],
      [
        "So daß wir sagen können: Damit diese Kräfte des inneren und äußeren Menschen -physischer Leib, Atherleib und Astralleib; Wollen, Fühlen und Den­ken - sich so haben entwickeln können, daß sie der Mensch heute als"
      ],
      [
        "äußeres und inneres Leben besitzt, dazu waren drei aufeinanderfol­gende kosmische Missionen nötig.",
        "Und diejenigen Wesenheiten, die wir als die Wesenheiten der Hierarchien bezeichnet haben, mußten, damit die Aufgabe der drei aufeinanderfolgenden Verkörperungen unserer Erde erfüllt werden und dem Menschen verliehen werden konnte, was in seiner heutigen Konstitution zum Vorschein kommt, jedesmal in entsprechender Wechseltätigkeit zusammenwirken."
      ],
      [
        "Es mußte also die Mission des alten Saturnzustandes erfüllt werden, sonst hätte der Mensch nicht den Einschlag des physischen Leibes und des Wollens erhalten können.",
        "Es mußte die Mission der Sonne erfüllt werden, sonst hätte er nicht den Atherleib und das Fühlen erhalten können, und endlich mußte die Mission des Mondes erfüllt werden, sonst hätte er nicht den Astralleib und das, was wir die Kraft des Den­kens nennen, haben können.",
        "So sind die drei vorhergehenden Verkör­perungen unserer Erde insbesondere demjenigen gewidmet, was wir eines der vorherrschenden Elemente unserer eigenen, persönlichen We­senheit, unseres «Ich» nennen können.",
        "Es liegt nämlich die Tatsache vor, daß der äußere, physische Leib, der ausgeflossen ist aus dem Wesen des alten Saturn, aus den Geistern des Willens, nichts anderes darstellt, als den Willen von außen gesehen.",
        "Bei uns wirkt der Wille als Innen­leben aus dem Inneren. - Diese Worte sind ganz genau gewählt, sie sind nicht phantastisch, sondern ganz genau der Natur der Sache entspre­chend.",
        "Sie können aus ihnen viel lernen. - Die Sonnenperiode hat die Erde durchgemacht, um den Atherleib auf der einen Seite zu begründen durch den Einfluß der Geister der Weisheit, und um zu begründen auf der anderen Seite durch das Fortwirken des Elementes der Weisheit dasjenige, was die innere Weisheit reflektiert: das Gefühl.",
        "Dasjenige, was die Mondenmission war, hängt mit dem Astralleibe und mit dem Denken in ähnlicher Weise zusammen."
      ],
      [
        "Jetzt fragt es sich: Was haben die hauptsächlich auf der Erde wir­kenden und die Erde formenden Geister der Form für eine besondere Mission gewählt?"
      ],
      [
        "Wir können zunächst sagen: Die Geister, die auf dem Saturn haupt­sächlich gewirkt haben, die Geister des Willens oder Throne, hatten die Mission, das Element einzuweben, das später während der Erdenentwickelung"
      ],
      [
        "in dem Willen sich offenbart.",
        "Das ist die große Saturnmis­sion: den Willen einzuimpfen, die Willenskräfte einzupflanzen.",
        "Wenn wir so etwas betrachten, so bekommen wir Hochachtung und Respekt vor den waltenden kosmischen Mächten.",
        "Wir bekommen eine richtige Wertschätzung diesen Mächten gegenüber, wenn wir sehen, daß zu dem kunstvollen Gewebe von äußerem Willen, der in dem physischen Leibe lebt, und von innerem Willen eine besondere planetarische Mission notwendig war.",
        "Die gesamte Welt der Hierarchien mußte einen Pla­neten entstehen und wieder vergehen lassen, um das Verhältnis zu­stande zu bringen, was in uns als äußeres und inneres Willenselement eingewoben ist.",
        "Ebenso mußte die alte Sonne entstehen, um den Äther-leib und das Gefühlselement, das innere Weisheitselement entstehen zu lassen.",
        "Was sich dann in unserem Denkelement, in unserer Astralität, als inneres Gedankenelement im Menschen reflektiert, dazu war die Mondmission notwendig."
      ],
      [
        "Welche Mission haben nun die Geister der Form, was ist also die eigentliche Erdenmission?",
        "Wenn Sie an die Saturnmission die Einprä­gung des Willens anknüpfen, an die Sonnenmission vorzugsweise die Einprägung des Gefühiselementes, an die Mondmission vorzugsweise die Einprägung des Gedankenelementes - also dasjenige, was im menschlichen Astralleibe ist -, so hat man an den Erdenplaneten die Mission zu knüpfen, ein vollständiges Gleichgewicht dieser drei Ele­mente zu bewirken, das Gleichgewicht dieser drei Elemente herzustel­len, von denen jedes während eines der früheren Zustände unseres Planeten die Oberhand hatte, so daß im Gleichgewichtszustande zu­sammenwirken diese drei Elemente, von denen jedes die Hegemonie hatte in einer der früheren Verkörperungen der Erde.",
        "Das ist die Mission unserer Erde.",
        "Zum Stillstand zu bringen den Kampf dieser Elemente dadurch, daß sie in das richtige Gleichgewichtsverhältnis gebracht werden, das ist die Erdenmission.",
        "Der Mensch ist hineinver­woben in diese Erdenmission, um dieses Gleichgewicht zuerst in seinem eigenen Innern aus Denken, Fühlen und Wollen aufzubauen.",
        "Der Mensch war in dieser Beziehung in der Tat bei der Entstehung der Erde ein regelloses Gewebe von Denken, Fühlen und Wollen.",
        "Wie noch bei dem gegenwärtigen Menschen das innere Gleichgewicht nicht vollständig"
      ],
      [
        "ist, sondern vielfach in Disharmonie, in Unordnung ist, das kann jeder an sich fühlen, der auch nur ein bißchen Selbsterkenntnis hat.",
        "Der Mensch ist zunächst berufen, in seinem Inneren das Gleichgewicht zwischen Denken, Fühlen und Wollen herzustellen, wodurch er von sich ausstrahlen und übertragen kann auf die Erde das, was dieses Gleichgewicht von Denken, Fühlen und Wollen bedeutet."
      ],
      [
        "In der okkulten Symbolik hat man immer diese Mission der Erde in ganz besonderer Weise durch eine Figur ausgedrückt.",
        "Wenn Sie alle geometrischen Figuren durchgehen, werden Sie keine finden, die dem Zusammenwirken im Sinne des Gleichgewichtes so genau entspricht, wie das gleichseitige Dreieck.",
        "Wenn Sie das gleichseitige Dreieck nur aufzeichnen, so finden Sie die drei Seiten einander gleich, die drei Win­kel einander gleich, jeder Scheitelpunkt ist gleich weit von dem anderen und alle gleich weit von dem Mittelpunkte entfernt.",
        "Der Mittelpunkt von dem gleichseitigen Dreieck ist ein absolutes Symbolum für das Gleichgewichtswirken, so daß, wenn der Okkultist das Dreieck an­schaut, er in demselben ein Symbolum sehen kann für das absolut equilibrierte Zusammenwirken dessen, was in den drei früheren Ver­körperungen unserer Erde jeweilig die Hegemonie hatte.",
        "Die Taten des Ich in dem Menschen bedeuten nichts anderes als das Schaffen eines tätigen, eines aktiven Mittelpunktes in der Menschennatur, wodurch dieser Gleichgewichtszustand von innen heraus vorbereitet werden kann.",
        "So ist in der Tat der Mensch zu Großem berufen auf unserer Erde, nämlich dazu, von innen heraus durch seine ganze Wesenheit zunächst das Gleichgewicht dessen zu bewirken, was früher in der ver­schiedensten Weise und zu verschiedenen Zeiten jeweilig vorherrschend war."
      ],
      [
        "Das ist zunächst eine recht abstrakte Definition unserer Erdenmis­sion, aber diese besteht einmal in dem Gesagten.",
        "Das Geheimnis dieser Mission spricht sich dadurch aus, daß durch dieses Zusammenwirken, durch dieses Gleichgewicht der drei Kräfte das Innere tatsächlich pro­duktiv Neues wirkt.",
        "Es wird dadurch wahrhaft ein viertes Element erzeugt zu den drei vorhergehenden, und dieses vierte Element ist das Element der Liebe.",
        "Die Liebe kann im Weltgetriebe sich nur entwickeln, wenn ein absolutes Gleichgewicht der drei in früheren Zeiten abwechselnd"
      ],
      [
        "die Hegemonie führenden Kräfte eintritt. - Darüber werden wir in den nächsten Tagen noch mehr zu sprechen haben.",
        "Vorläufig nehmen Sie das als abstrakte Charakteristik hin."
      ],
      [
        "So ist unser Planet der Planet der Liebe, und deshalb ist sozusagen dieses Gleichgewicht, das sich herausstellt in dem Zusammenwirken dieser drei Kräfte, in seinem Ergebnis Liebeswirken, und Liebeswirken soll durch alle folgenden Verkörperungen der Erde, gerade durch die Mission des Erdenwirkens hineinverwoben werden in die gesamte Evo­lution.",
        "Dadurch wird die Dreiheit zu einer Vierheit, und diese Vierheit beginnt mit ihrem vierten Element auf der untersten Stufe, beginnt sozusagen mit der niedersten Form der Liebe, die geläutert und gereinigt wird bis zu dem Grade, daß am Ende der gesamten Erdenentwickelung die Liebe als ein völlig gleichberechtigtes Element erscheinen wird.",
        "Die Mission des Gleichgewichtes für unseren Erdenplaneten erfüllen, heißt also im Grunde genommen: die Dreiheit zu einer Vierheit machen.",
        "Des­halb wird auch das Geheimnis des Erdendaseins gewöhnlich okkult ausgesprochen mit den Worten «Die Dreiheit zur Vierheit machen».",
        "Das vierte Element ist natürlich heute noch sehr unvollkommen.",
        "Es wird aber, wenn die Erde ihre Mission erfüllt haben wird, ebenso hell-glänzend sein wie das heilige Dreieck, das uns mit seiner Gleichge­wichtslage als das höchste Symbolum, das wir für unser Erdenideal haben, vorleuchtet, insofern wir uns an die Vergangenheit der Erde erinnern."
      ],
      [
        "Es ist dieses Zusammenwirken der Elemente von Denken, Fühlen und Wollen im Innern des Menschen zunächst so, daß dieses eigentliche Innere zur Substanz der Liebe wird.",
        "Das ist dasjenige, was man das eigentlich Produktive, das innerlich Produzierende im Erdendasein nennen kann.",
        "Deshalb muß man die Geister der Form in ihrer Gesamt­heit, weil sie gerade diese Mission haben, die drei früheren Zustände ins Gleichgewicht zu bringen, zugleich als die Geister der Liebe be­zeichnen."
      ],
      [
        "Wenn wir so das Erdendasein betrachten, dann haben wir zunächst charakterisiert das Wollen, Fühlen und Denken und das Liebeswirken außerhalb unseres Erdenplaneten, und wir haben als besondere Auf­gabe der Geister der Form die Einimpfung, die Einprägung der Liebe,"
      ],
      [
        "die das Resultat des Gleichgewichtes ist, bezeichnen können.",
        "Darin besteht also die Gesamtmission der Erde.",
        "Um diese die Erde durchdrin­gende Kraft der Liebe zustande zu bringen, dazu ist das Ineinander­wirken und Ineinanderarbeiten alles dessen notwendig, was wir als die Arbeit der niedersten Hierarchien bezeichnet haben.",
        "Wie wir schon in unserer vorhergehenden Betrachtung angefangen haben zu charakteri­sieren, muß dadurch sozusagen das Netz der Liebe gewoben werden, und es muß dieses Gewebe der Liebe so gewoben werden, daß die Hauptfäden hineingewoben werden - weil das ihrer Grundmission entspricht - durch die normalen Geister der Form.",
        "Dann weben hinein die abnormen Geister der Form, die eigentlich Geister der Bewegung sind, das, was die Rassen gibt.",
        "Dann weben die normalen und abnormen Zeitgeister die geschichtliche Entwickelung hinein, und dann weben die Erzengel mit normaler und abnormer Entwickelung die einzelnen Volks- und Sprachen-Entwickelungen hinein, und endlich wirken hin­ein die Wesen, welche den Menschen an den richtigen Platz auf der Erde stellen, die Engel.",
        "So wird dieses gewaltige Netz der Liebe gewo­ben.",
        "Das, was als Netz der Liebe, als die eigentliche Erdenmission, gewoben wird, das ist aber nur als Abglanz, als Maja in unserer Erde sichtbar."
      ],
      [
        "Das nächste Gebiet über der physischen Welt, wo dieses Netz gese­hen werden kann, ist die astralische Welt.",
        "Aber immer klarer und klarer sieht man das Arbeiten der Hierarchien an den Wahrheiten, die unserer äußeren Maja zugrunde liegen, wenn man sich erhebt aus der astrali­schen Welt in die Welt des niederen und höheren Devachan.",
        "Dann sieht man, wie dieses Gewebe gesponnen wird.",
        "Erhebt man sich zur Astral­welt, dann erblickt man allerdings zunächst dasjenige noch nicht, was hauptsächlich von innen spinnt, nämlich die Geister des Willens, die Cherubim und Seraphim.",
        "Wenn der Mensch diese Geister bei ihrer Arbeit finden will, dann muß er sich zum Schauen in noch höhere Welten erheben.",
        "Aber eines finden wir schon in der astralen Welt: das, was wir die abnormen Geister der Form nennen, welche, wenn sie eine normale Entwickelung erlangt hätten, von außen weben sollten.",
        "Wir haben gesehen, daß die Geister der zweiten Hierarchie von außen weben sollen; hier aber sehen wir, daß sie von innen weben.",
        "Wir können"
      ],
      [
        "also sagen: In dieses Netz, in dem von außen weben die Geister der Bewegung, die Geister der Form und die Geister der Weisheit, von innen die Geister des Willens, die Seraphim und Cherubim, weben auch noch von innen Wesenheiten, die eigentlich von außen weben müßten.",
        "Sie weben aber unter der Oberfläche so, wie etwa der Seiden-wurm den Cocon webt."
      ],
      [
        "Innerlich ist das, was zunächst in der Astral-welt gesehen wird.",
        "Diese eigenartigen Geister der Bewegung, die depla­zierte, gestürzte Geister sind, sie sind das nächste, was sichtbar wird von diesen in der geistigen Erdenatmosphäre webenden und wogenden geistigen Wesenheiten."
      ],
      [
        "Diese geistigen Wesenheiten, die das erste sind, was auf dem Astralplan zunächst sichtbar wird, noch bevor dasjenige, was normalerweise auftritt, die Engelwesen oder Angeloi sichtbar werden, sind für das hellseherische Schauen eigentlich - trotzdem sie für die Erzeugung der Rassen im tiefsten Sinne notwendig sind - doch in gewisser Weise die verführerischen Geister.",
        "Diese Geister, von wel­chen jeder wieder viele unter sich hat - weil jeder viele geistig unter­geordnete Wesen erzeugt -, sind in der geistigen Welt eingehüllt in eine Summe von geistigen Wesenheiten, die immer unter den betreffen­den Hierarchien stehen."
      ],
      [
        "Auch die höheren Geister haben solche unter ihnen stehende Wesenheiten; die Geister des Willens: die Undinen; die Cherubim: die Sylphen; die Seraphim: die Salamander.",
        "Aber auch diese abnormen Geister der Form, die eigentlich Geister der Bewegung sind, die wie eine Art häßlicher geistiger Wesen auf dem astralischen Plane erscheinen, haben ihre untergeordneten Geister."
      ],
      [
        "Sie sind die Gei­ster, welche weben und leben in dem, was mit dem Entstehen der menschlichen Rassen zusammenhängt, was also beim Menschen mit dem zusammenhängt, sozusagen an dem Elemente hängt, das wir als das erdgebundene charakterisiert haben, als das mit der Fortpflanzung zusammenhängende und dergleichen.",
        "Das sind Wesenheiten, das ist überhaupt ein Terrain, welches zu den buntesten und gefährlichsten der astralischen Welt gehört, und es ist leider das Terrain - an dieser Stelle kann es am besten im Zusammenhange gesagt werden -, das von den­jenigen, die auf eine unrichtige Weise zum Schauen kommen, am aller-leichtesten gefunden werden kann."
      ],
      [
        "Am leichtesten kommt das Heer derjenigen Geister, die mit der Fortpflanzung der Rasse zu tun haben"
      ],
      [
        "und dienende Glieder derselben sind, zum Vorschein.",
        "Mancher, der vorzeitig und auf unrichtige Weise sich in das okkulte Gebiet hinein-begeben hat, hat es teuer dadurch bezahlen müssen, daß ihm das Heer dieser geistigen Wesenheiten ohne die Harmonisierung durch andre geistige Wesen entgegentrat."
      ],
      [
        "So haben wir hineinleuchten können in das, was am Realen spinnt und webt, um das Gewebe zu weben, aus dem dann die eigentliche see­lische Welt des Menschen sich entfaltet.",
        "Wie diese Grundlage, in die wir jetzt ein wenig hineingeschaut haben, in der Rassen-, in der Volks-entstehung und so weiter zum Vorschein kommt, davon wollen wir morgen weiter sprechen."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "SECHSTER VORTRAG Kristiania, 12. Juni 1910 morgens",
    "paragraphs": [
      "Sie können sich denken, daß es eine sehr komplizierte Sache ist, wenn die Geister der verschiedenen Hierarchien mit ihren Kräften so zusam­menwirken müssen, daß die Erdenmission erfüllt werden kann, sozu­sagen so wirken müssen, daß zuletzt eine Gleichgewichtslage heraus­kommt. Daher werden Sie auch begreifen, daß Angaben wie diejenigen, die gestern gemacht worden sind, immer nur dann gemacht werden können, wenn man einen ganz bestimmten Punkt der Entwickelung ergreift, und daß sich die ganze Darstellung sofort verändert, wenn man die Evolution an einem anderen Punkte betrachtet. Daher werden Sie auch, wenn Sie zu einem geschlossenen Verständnis gerade dieser sehr komplizierten Sache kommen wollen, immer den einen Vortrags­zyklus mit dem andern zusammenhalten müssen.",
      "Ich will nur einen Punkt hervorheben, und das, was ich jetzt in diesem Augenblicke sage, soll eine Art von Anmerkung sein. In unserem Erdengleichgewicht stellt sich das ganze Zusammenwirken der Hierar­chien so dar, daß wir das, was wir gestern als dritte Hierarchie bezeich­neten - die Geister des Willens, die Cherubim und Seraphim -, suchen müssen als etwas, was in bezug auf diese Gleichgewichtslage aus der Erde heraus wirkt. Natürlich müssen Sie sich vorstellen, daß diese Hierarchie ursprünglich aus dem Weltall herein gegen den Erdmittel­punkt ihre Kräfte entfaltet, und daß, wie der Mensch diese Kräfte gewahr wird, nicht deren direkter Richtung entspricht, sondern der umgekehrten, welche sie erfahren, indem sie zurückgeworfen, reflek­tiert werden. Daher werden Sie zum Beispiel von dem ganz Intimen der Vorgänge, die da stattfinden, erst dann sich eine geschlossene Vor­stellung zu machen vermögen, wenn Sie das gestern Gesagte mit man­chem vergleichen, was über die Hierarchien in meinem Vortragszyklus in Düsseldorf gesagt worden ist, wo der himmlische Teil des Wirkens der drei Hierarchien in geschlossener Darstellung gegeben wurde. Diese Dinge sind eben nicht einfach, und um die Erdenmission begreiflich zu",
      "machen, ist es notwendig, den Gesichtspunkt so zu wählen, daß wir die zurückstrahlungen der Geister dieser Hierarchien in dem, was wir die Elemente des Erdendaseins nennen, erblicken.",
      "Wenn Sie dies berücksichtigen, dann werden Sie aber auch ein Ge­fühl bekommen von der unendlichen Weisheit, welche in dem ganzen Zusammenhang der Kräfte des Universums, der Kräfte des Kosmos ruht. Sie werden gewissermaßen auch dafür ein Gefühl erhalten, daß die Erkenntnisse immer weiter zu gehen haben, daß sie keine Grenze haben, da die Dinge so kompliziert sind, daß, wenn wir einen Gesichts­punkt erfaßt zu haben glauben, wir gleich genötigt sind, zu einem ande­ren überzugehen, der uns die Sache wieder von einer anderen Seite beleuchtet erscheinen läßt.",
      "Wir können nur nach und nach in unseren Erkenntnissen aufrücken, aber Sie werden dennoch aus den Andeu­tungen, die gestern gemacht worden sind, namentlich am Schlusse der Darstellung, sich etwas genauer bekannt gemacht haben mit dem, was man nennen kann: Zusammenwirken der abnormen und normalen Geister der Form, damit innerhalb unseres Erdenlebens nicht bloß ein einheitliches, sich über die ganze Erde ausbreitendes, gleichartiges Men­schentum entsteht, sondern damit ein solches Menschentum entsteht, das sich in der Mannigfaltigkeit der einzelnen Rassen ausleben kann. Zu jenem einheitlichen Menschentum, das der Mensch nur im Verlaufe der Erdenevolution wieder erreichen kann, wäre notwendig gewesen die reine Wirksamkeit der normalen Geister der Form.",
      "Es sind das die­selben geistigen Wesenheiten, welche in der Genesis mit dem Namen der Elohim benannt werden, und es sind eigentlich im gesamten Uni­versum, das die Erde umgibt und mit ihr zusammen ein Ganzes aus­macht, sieben solcher Geister der Form in normaler Entwickelung zu erkennen. Es gibt also sieben Geister der Form oder sieben Elohim.",
      "Wenn wir uns diese sieben Elohim mit ihren verschiedenen Missionen und dem Beruf, in der gesamten Erdenmission das Gleichgewicht oder die Liebe herzustellen, vorstellen wollen, dann müssen wir uns klar sein darüber, daß diese sieben Geister der Form in dem gesamten Weltall so zusammenwirken, daß wirklich das zustande kommen würde, was wir in einem der Vorträge als «den Menschen im zweiten Drittel seines Lebens» charakterisiert haben. Da würde der eigentliche Ich-Mensch",
      "sich ausprägen, wenn alle diese sieben Geister der Form in der entspre­chenden Weise, wie sie es für sich allein durch ihre eigene Gemeinschaft sich vorgenommen haben, wirken könnten. Weil aber andere geistige Wesenheiten mitwirken und dieses einheitliche Menschentum ver­mannigfaltigen, so war im Kosmos eine ganz besondere Einrichtung not­wendig.",
      "Wenn Sie heute die Lokalität im Kosmos suchen wollen, von der aus die normalen Geister der Form wirksam sind - also diejenigen Wesenheiten, die,wie ich das gestern charakterisierte, uns zuletzt im Lich­te entgegenstrahlen innerhalb unseres gegenwärtigen Kosmos-, so müs­sen Sie dieselben in der Sonne suchen. Sie müssen jedesmal in der Richtung der Sonne jene kosmische Loge, jene Gemeinschaft im Weltall suchen, wo diese Geister der Form ihre Beratungen pflegen zur Herstellung des irdischen Gleichgewichts, zur Erfüllung der irdischen Mission.",
      "Nur eines war notwendig, damit die abnormen Geister der Form durch ihre Wirksamkeit nicht gar zu große Unordnung in bezug auf den Menschen hervorriefen, es war notwendig, daß sich einer der Geister der Form ablöste aus der Gemeinschaft, so daß Sie eigentlich nur sechs dieser Geister der Form oder Elohim in der Sonnenrichtung zu suchen haben. Einer dieser Geister mußte sich, damit durch die gleichzeitige Wirksam­keit der abnormen Geister der Form - die eigentlich Geister der Bewe­gung sind - nicht völlige Unordnung in das Gleichgewicht hineinge­bracht wurde, absondern.",
      "Das war derjenige, welcher in der Bibel, in der Genesis, Jahve oder Jehova genannt wird. Wenn Sie dessen Wirk­samkeit im Weltall suchen wollen, so dürfen Sie nicht suchen in der Richtung, wo die Sonne steht, sondern in der Richtung, wo sich jeweilig der Mond befindet.",
      "Das ist auch in meiner «Geheimwissenschaft» an­gedeutet, nur von einer anderen Seite her betrachtet, indem gezeigt wird, daß die Geister der Form mit der Sonnentrennung weggehen, daß aber mit der besonderen Einrichtung, die mit der Mondtrennung zu­stande kommt, erst die Vorbedingung für die fernere Entwickelung des Menschen geschaffen wird. Denn, wenn der Mond mit der Erde verei­nigt geblieben wäre, so hätte die Evolution des Menschen nicht statt­finden können.",
      "Diese fernere Evolution des Menschen ist nur dadurch möglich gewesen, daß einer der Elohim, Jahve, mit dem Monde heraus­trat-während die anderen sechs Geister in der Sonne verblieben-, nur",
      "dadurch, daß Jahve im Entgegenwirken zusammenwirkte mit seinen sechs anderen Genossen.",
      "Sie können nun die Frage aufwerfen: Warum wurde überhaupt diese Sonne abgespalten? Das war aus folgenden Gründen notwendig. Nach­dem einmal ältere Geister der Bewegung, welche eine größere Kraft als die Geister der Form haben - denn sie stehen in der Reihe der Hierar­chien höher -, sich entschlossen hatten, zurückzubleiben, mußten die normalen Geister der Form ihre Wirksamkeit durch die Abspaltung des einen abschwächen. Sie hätten sonst nicht das Gleichgewicht hervor-bringen können, welches für die fernere Entwickelung erforderlich war.",
      "Wenn wir eine genügende Vorstellung haben wollen von dem Wirken dieser normalen Geister der Form, so ist es das Beste, wenn wir uns sagen: Sie strahlen uns im Sonnenlichte zu. Wenn wir aber von den abnormen Geistern der Form eine Vorstellung gewinnen wollen, wie sie zusammenwirken mit den normalen Geistern der Form, die gleich­sam zentriert sind in der Sonne - denn nur, damit das Gleichgewicht hergestellt werden kann, hat sich Jehova in der Mondrichtung abge­spalten -, dann müssen wir uns vorstellen, daß eine bestimmte Sonnen-kraft, die in den normalen Geistern der Form uns zuströmt, abgeändert wird durch die Kraft, die uns zuströmt von den abnormen Geistern der Form, die eigentlich Geister der Bewegung sind. Diese finden ihren Mittelpunkt in den anderen fünf Planeten, im alten Planetenstile ge­sprochen. Da haben Sie den Mittelpunkt zu suchen für diese anderen, für die abnormen Geister der Form, also im Saturn, Jupiter, Mars, Venus, Merkur.",
      "Jetzt haben Sie, wenn Sie in den Kosmos hinaussehen, eine Art Verteilung für die normalen und abnormen Geister der Form. Die nor­malen Geister der Form sind zu sechs zentriert in der Sonne, der Eine - Jahve oder Jehova - hält das Gleichgewicht jenen, vom Monde aus, indem er den letzteren regiert und leitet. Beeinflußt werden die Wirkungen dieser Geister der Form durch jene Wirkungen, die von Saturn, Jupiter, Mars, Venus und Merkur ausgehen. Diese Kräfte strah­len herunter auf die Erde, werden aufgehalten und strahlen wieder von der Erde auf in der Weise, wie das gestern am Ende des Vortrages beschrieben worden ist.",
      "Wenn Sie also ein Stück Erdoberfläche haben, und von der Sonne aus eine bestimmte Wirkung auf dieselbe durch die Elohim oder nor­malen Geister der Form ausgeübt wird, so würde auf dem betreffenden Punkte der Erdoberfläche nichts anderes entstehen als das ganz nor­male Ich. Es würde dasjenige entstehen, was dem Menschen sein nor­males Sein, durchschnittlich sein gesamtes Menschentum gibt. Nun mischen sich hinein in diese Kräfte der Geister der Form - die sonst durch die Gleichgewichtslage hier auf der Oberfläche tanzen würden -zum Beispiel die Kräfte des Merkur. Dadurch tanzt und vibriert in dem, was hier als Kraft der Geister der Form sich entfaltet, nicht nur das Nor­male, sondern auch dasjenige,was sich hineinmischt in die normalenKräf­te der Elohim, in die normalen Kräfte der Geister der Form, nämlich das, was von diesen in den Mittelpunkten der einzelnen Planeten zentrier­ten, abnormen Geistern der Form kommt. Hieraus ergibt sich, daß fünf Mittelpunkte der Beeinflussung möglich sind durch diese abnormen Geister der Form, und diese fünf Mittelpunkte der Beeinflussung ergeben in ihrer Rückstrahlung, in ihrer Reflektierung vom Erdmittel-punkte aus auf die Menschheit in der Tat dasjenige, was wir anerkennen als die fünf Grundrassen im Erdendasein.",
      "Wenn wir den Punkt, den wir vor einigen Tagen in unseren Dar­legungen in Afrika gefunden haben, uns jetzt näher dadurch charak­terisieren, daß, weil die normalen Geister der Form zusammenwirken mit denjenigen abnormen Geistern der Form, die im Merkur zentriert sind, die Rasse der Neger entsteht, so bezeichnen wir okkult ganz richtig das, was in der schwarzen Rasse herauskommt, als die Merkur-Rasse.",
      "Jetzt verfolgen wir diese Linie weiter, die wir dazumal durch die Mittelpunkte der einzelnen Rassenausstrahlungen gezogen haben. Da kommen wir nach Asien und finden die Venus-Rasse oder die malayi­sche Rasse. Wir kommen dann durch das breite Gebiet Asiens hindurch und finden in der mongolischen Rasse die Mars-Rasse. Wir gehen dann herüber auf europäisches Gebiet und finden in den europäischen Men­schen, in ihrem Ur-Charakter, in ihrem Rassen-Charakter die Jupiter­Menschen. Gehen wir über das Meer hinüber nach Amerika, wo der Punkt, der Ort ist, an dem die Rassen oder Kulturen sterben, so finden",
      "wir die Rasse des finsteren Saturn, die ursprüngliche indianische Rasse, die amerikanische Rasse. Die indianische Rasse ist also die Saturn­Rasse. Auf diese Weise bekommen Sie, wenn Sie sich okkult die Sache immer genauer vorstellen, die Kräfte, die in diesen Weltenpunkten, diesen fünf Planeten, ihre äußere materielle Offenbarung erfahren haben.",
      "Wenn Sie sich davon eine immer deutlichere und konkretere Vor­stellung machen, dann bekommen Sie eine innere Erkenntnis dieser eigentümlichen, über die Erde hin verbreiteten Rassen-Charaktere, eine Erkenntnis dieses eigenartigen Zusammenwirkens der normalen und der abnormen Geister der Form. Damit haben wir gleichsam das Bild gezeichnet, wie wir es in einem bestimmten Punkt festhalten können. Aber es gilt das, was ich gesagt habe für die verschiedenen Punkte der Erde, wieder nur für einen ganz bestimmten Zeitpunkt der Entwickelung. Es gilt für den Zeitpunkt, wo an einem bestimmten Momente der alten atlantischen Entwickelung die Völkerzüge von einem Punkt der Atlantis ausgehen und dorthin wandern, wo sie die entsprechende Rassenausbildung in dem betreffenden Punkte erhalten können. Daher finden Sie in meiner «Geheimwissenschaft» auch darauf hingewiesen, daß in der alten Atlantis, an ganz bestimmten Mysterien-stätten, die dort die atlantischen Orakel genannt sind, die Leitung dieser Verteilung der Menschen über die Erde in die Hand genommen wird, so daß in der Tat jenes Equilibrium, jene Gleichgewichtslage hervorgebracht werden konnte, die zur entsprechenden Rassenvertei­lung führte. In einem solchen Mysterien-Orakel wurden immer die Wahrheiten erforscht, die wir jetzt erzählen, und ursprünglich hat man sich ganz danach gerichtet. Es wurde auf diese Weise das, was auf der Erde geschah, von solchen Zentren aus in entsprechender Weise geleitet.",
      "Wir haben also gleichsam in der Völkerströmung, die durch Afrika hinüberzog und sich in der äthiopischen Rasse auskristallisierte, einen Impuls zu suchen, der von dem Merkur-Orakel gegeben werden konnte, in dem man ganz genau beobachtete, wie zusammenwirkten die nor­malen Geister der Form, die sechs Elohim mit Jahve oder Jehova, und wie hineinwirkten die abnormen Geister der Form, die vom Mittel­punkte des Merkur aus wirkten. Nach dem astrologischen Zusammenwirken",
      "dieser verschiedenen Punkte der Kräfte wurde der Gleichge­wichtspunkt ausgesucht auf unserer Erde und danach wurde der Gleichgewichtspunkt als Ausstrahlungspunkt für die betreffende Rasse angenommen.",
      "In ähnlicher Weise wurde auch die Bildung der anderen Rassen geleitet. Danach wird dann die große Landkarte gezeichnet, in welche die Einflüsse eingetragen werden mit Bezug auf Völker, Geschlechter und so weiter. Das ist die große Landkarte, die ein Abbild der Him­melswirksamkeit ist, die dadurch entsteht, daß die Kräfte der Him­melswirksamkeit in die Erde hineinstrahlen, von ihr zurückstrahlen und den Menschen bestimmen.",
      "Als was können wir nun einen Menschen der Merkur-Rasse, der äthiopischen Rasse ansehen? Wir können ihn so ansehen, daß wir sagen:",
      "Dieser Mensch ist ursprünglich durch die Elohim dazu bestimmt, dazu veranlagt gewesen, das gesamte Menschliche in seiner Totalität in sich auszudrücken. Aber nun wirkten von dem Merkurmittelpunkt aus die abnormen Geister der Form mit großer Gewalt und variierten den Menschen so, daß die Form der äthiopischen Rasse herauskam. Und so ähnlich verhält es sich bei jeder einzelnen Rasse. Dadurch aber, daß die Völkerströmungen in ganz bestimmter Weise von dem ursprüng­lichen Mittelpunkte aus geleitet worden sind, ist erst diese Linie, die ich Ihnen vor einigen Tagen zeichnete, entstanden. Sie müssen sich also denken, daß die Geister der Form von einem Mittelpunkte ausstrahlten. Diesen Mittelpunkt haben wir anzunehmen in einem bestimmten Zeit­punkte der alten Atlantis. Da haben wir das, was sich hinuntersenkt in den atlantischen Kontinent und ihn so ausgestaltet, daß die Menschen-geister unter die Herrschaft der entsprechenden abnormen Geister der Form gebracht wurden.",
      "Damit war die große Völkergrundlage geschaffen, und der Mensch hat, wenn er hinaufsieht in die unendlichen Weiten des Himmelsrau­mes, dort die Kräfte zu suchen, welche ihn konstituierten. Sie konsti­tuierten ihn aber in ihrer Rückstrahlung von der Erde. Indem er hinauf-blickt zu den normalen Geistern der Form, zu den Elohim, sieht er zu dem auf, was ihn eigentlich zum Menschen macht, und indem er hinauf-blickt zu dem, was in den einzelnen Planetengeistern - abgesehen von",
      "Sonne und Mond - zentriert ist, sieht er das, was ihn zu einer bestimm­ten Rasse macht.",
      "Wie arbeiten nun in und an den Menschen diese Rassengeister? Sie arbeiten in sehr eigentümlicher Art, so, daß sie, man möchte sagen, durchkochen seine Kräfte zunächst bis in den physischen Leib hinein. Nun wissen Sie ja, daß sich dasjenige, was wir die vier Grundteile des Menschen nennen, projiziert, abbildet in jeweiligen Teilen des physi­schen Leibes, so daß wir sagen können: Es bildet sich ab dasjenige, was das Ich ist, im Blut; dasjenige, was der astralische Leib ist, im Nerven­system; dasjenige, was der Äther- oder Lebensleib ist, im Drüsensystem, und erst der physische Leib ist ein Sichselbstsein, ein Abbild seines eigenen Wesens, das für den heutigen Menschen in sich selbst seine geschlossenen Gesetze hat. Das Ich bildet sich also ab im Blute, der Astralleib im Nervensystem, der Ätherleib im Drüsensystem.",
      "Zunächst können diejenigen geistigen Wesenheiten, die da in dem Menschen kochen, damit sein Rassencharakter entsteht, nicht gleich unmittelbar in die höheren Teile hineinwirken. Sie kochen zunächst in diesen Abbildungen der höheren Glieder im physischen Leibe. In den physischen Leib können sie nicht recht herein, aber sie kochen in den drei anderen Gliedern: in dem, was Abbild des Ich ist, im Blut, in dem, was Abbild des Astralleibes ist, im Nervensystem und in dem, was Abbild des Ätherleibes ist, im Drüsensystem. In diesen drei Systemen, die dem physischen Leibe angehören, aber Abbilder der höheren Glieder sind, kochen die Rassengeister, die abnormen Geister der Form.",
      "Sie sehen hier, daß des Menschen physischer Leib von innen bestimmt wird, so bestimmt wird, daß diese verschiedenen geistigen Wesenheiten eingreifen in die Glieder im physischen Leibe, welche die Projektionen, die Schattenbilder der höheren Glieder sind. Wo greift nun zum Bei­spiel der Merkur ein? - ich sage Merkur, um das zusammenzufassen, was sich als abnorme Geister der Form im Merkur befindet. Er greift so ein, daß er mit anderen zusammenwirkt, namentlich in das Drüsen­system. Er kocht in dem Drüsensystem drinnen, und da leben sich die Kräfte aus, die durch jenes Übergewicht der Merkurkräfte entstehen, die in der äthiopischen Rasse wirken. Alles, was der äthiopischen Rasse ihre besonderen Merkmale verleiht, das kommt davon her, daß die",
      "Merkurkräfte in dem Drüsensystem der betreffenden Menschen kochen und brodeln. Das kommt davon her, daß sie auskochen, was die allge­meine, gleiche Menschengestalt zu der besonderen der äthiopischen Rasse macht mit der schwarzen Hautfarbe, dem wolligen Haar und so weiter. Diese Modifikation der allgemeinen Menschengestalt kommt also von diesen Kräften her.",
      "Gehen Sie nun weiter nach Asien herüber, so haben Sie in ähnlicher Weise etwas, was man als Venuskräfte bezeichnen könnte, als eine ab­norme Ausgestaltung der Geister der Form. Diese Venuskräfte wirken wiederum, indem sie ihren Angriffspunkt vorzugsweise auf das ver­legen, was wir Abbild des astralischen Leibes nennen, im Nervensystem.",
      "Aber sie wirken auf eine besondere Art, und zwar nicht direkt als Venusgeister, auf das Nervensystem. Es kann nämlich auf zwei Um­wegen auf das Nervensystem gewirkt werden. Der eine Umweg ist durch die Atmung.",
      "Indem nämlich besonders auf die Atmung gewirkt wird, setzen sich im Menschen selber diese Wirkungen im Atmungs­und im Nervensystem fest und geben ihm eine bestimmte Form. Diesen Umweg wählen sich die abnormen Geister der Form, die wir Venus-wesen nennen können, eben in der malayischen Rasse, in den gelb­schattierten Rassen von Südasien und nach den Inseln des malayischen Gebietes hin.",
      "Da ist ausgebreitet, so wie über das äthiopische Gebiet die Drüsenmenschheit, über diese Fläche die Menschheit, bei der die abnor­men Geister der Form auf dem Umwege durch das Atmungssystem auf das Nervensystem wirken. Im Nervensystem wird auf dem Umwege über das Atmungssystem gewirkt.",
      "Im Nervensystem wird ausgekocht das, was mit besonderen Modifikationen die mehr oder weniger gelb-gefärbte Menschheit gibt. Die Umwandlung, welche da bewirkt wird, drückt sich allerdings mehr in jenem Nervensystem aus, das wir mit dem Ausdruck Sonnengeflecht zusammenfassen, also nicht eigentlich in dem höheren Nervensystem, sondern in jenem geheimnisvollen Teile des Nervensystems, der in zwei Strängen parallel dem Rückenmark läuft und sich in der verschiedensten Weise ausbreitet.",
      "Es wird also in diesem Teile des Nervensystems auf dem Umwege durch das Atmungs­system gewirkt, der in unserem Sinne noch nicht zu der höheren geisti­gen Tätigkeit gehört. Es wird tief im unterbewußten Organismus durch",
      "diese Venuskräfte gewühlt, die in diesem Rassenteile der Menschheit wirken.",
      "Jetzt gehen wir über die breiten, mongolischen Flächen herauf. Das sind diejenigen Flächen, in denen die Geister der Form vorzugsweise wirken, die den Umweg durch das Blut genommen haben. Da wird im Blute dasjenige ausgekocht, was die eigentliche Modifikation aus der Menschheit heraus, den Grundcharakter der Rasse bewirkt.",
      "Nun ist aber bei dieser mongolischen Rasse etwas höchst Eigentümliches vor­handen. Da gehen ins Blut hinein die Marsgeister. Sie arbeiten aber auf eine ganz bestimmte Weise im Blute, so daß sie den sechs Elohim, die in der Sonne zentriert sind, entgegenwirken können.",
      "Diesen sechs Elo­him wirken sie also entgegen in der mongolischen Rasse. Dabei machen sie eine ganz besondere Attacke nach der anderen Seite, nach Jahve oder Jehova, der abgetrennt hat sein Wirkungsgebiet von dem der sechs Elohim.",
      "Aber außer diesem Zusammenwirken der Marsgeister mit den sechs Elohim und Jahve, das die mongolische Rasse ergibt, gibt es noch ein Besonderes. Wenn wir die Art dieses besonderen Einflusses angeben wollen, so müssen wir sagen: Wie in das Mongolische hinein die sechs Elohim von der Sonne, Jahve vom Monde und ihnen entgegen die Marsgeister wirken, so müssen wir in einem anderen Falle anneh­men, daß von der Mondrichtung her die Jahvekräfte wieder zusam­mentreten und zusammenwirken mit den Marsgeistern, und daß da­durch eine besondere Modifikation entsteht.",
      "Hier haben Sie, aus dem okkultesten Hintergrunde heraus erklärt, eine besondere Modifikation der Menschheit, nämlich diejenige, die zum Semitentum gehört. Im Semitentum haben Sie eine Modifikation des gesamten Menschentums, so, daß sich ausschließt von den anderen Elohim Jahve oder Jehova und dieses Volk mit einem besonderen Charakter veranlagt, indem er zusammenwirkt mit den Geistern des Mars, um die besondere Modifi­kation dieses Volkes hervorzubringen.",
      "Jetzt werden Sie auch das Be­sondere einsehen, das in dem semitischen Volk und seiner Mission liegt. In einem gewissen, tiefen okkulten Sinn konnte der Schreiber der Bibel sagen, daß Jahve oder Jehova dieses Volk zu seinem Volke gemacht habe, und wenn Sie jetzt das dazu nehmen, daß hier ein Zusammen­wirken stattfindet mit den Marsgeistern, und daß die Marsgeister ihre",
      "Angriffe vorzugsweise auf das Blut richten, dann werden Sie auch begreifen, warum gerade die fortgehende Wirkung des Blutes von Ge­schlecht zu Geschlecht, von Generation zu Generatiön für das semi­tisch-hebräische Volk von ganz besonderer Wichtigkeit ist, und warum im semitischen Volk der Gott Jahve sich als der Gott bezeichnet, der mit dem Blute herunterrinnt von Abraham, Isaak, Jakob und so weiter. Das ist der Weg, wie das Blut rinnt durch alle diese Geschlechter. Indem sich Jahve bezeichnet: «Ich bin der Gott Abrahams, Isaaks und Ja­kobs», sagt er: Ich wirke in eurem Blute. - Was immer im Blute wirkt, was im Blute ausgefochten werden muß, das Zusammenwirken mit den Marsgeistern, das ist eines der Mysterien, die uns tief hineinführen in die weise Führung der gesamten Menschheit der Erde.",
      "So also sehen Sie, daß auf das Blut der Menschheit in zweifacher Weise gewirkt wird, daß zwei Rassenbildungen sozusagen entstehen, indem auf das Blut der Menschheit gewirkt wird. Auf der einen Seite haben wir alles dasjenige, was wir die mongolische Rasse nennen, auf der anderen Seite dasjenige, was wir als zum Semitentum gehörig bezeichnen können. Das ist eine große Polarität in der Menschheit, und wir werden auf diese Polarität unendlich Bedeutungsvolles zurückzu­führen haben, wenn wir die Tiefen der Volksseelen werden verstehen wollen.",
      "Wir haben noch weiter zu verfolgen, wie die Geister und Wesenhei­ten, die im Jupiter ihren Mittelpunkt haben, in dem Menschen kochen und brodeln. Diese wählen sich nun den zweiten Angriffspunkt, um unmittelbar auf das Nervensystem zu wirken, und zwar geht durch alles das, was die Sinne des Menschen sind, der eine Angriffspunkt; der ande­re Angriffspunkt, der in das Nervensystem hineinwirkt, geht auf dem Umwege durch das Atmungssystem in das Sonnengeflecht. Der Angriff, der von dem Jupiter ausgeht, geht auf dem Umweg durch die Sinnes­eindrücke und strömt von da aus auf die Teile des Nervensystems, die im Gehirn und Rückenmark zentriert sind. Da hinein fließen also bei denjenigen Rassen, die zur Jupiter-Menschheit gehören, jene Kräfte, die den Rassencharakter besonders ausprägen. Das ist bei den arischen, vorderasiatischen und europäischen Völkern, bei denen, die wir zu den Kaukasiern rechnen, mehr oder weniger der Fall. Da tritt die Modifikation",
      "der allgemeinen Menschheit, die von den abnormen Geistern der Form herrührt, dadurch ein, daß die abnormen Geister, die wir als Jupiter-Geister bezeichnen können, auf die Sinne einwirken. Also durch die Sinne werden die Kaukasier bestimmt.",
      "Nun werden Sie auch begreifen, daß ein ganz eminent und bewußt unter dem Jupiter- oder Zeus-Ein fluß stehendes Volk, wie die Griechen, die sich als Mittelpunkt für den Zeus-Einfluß fühlen, hervorragend bestimmt wird durch das, was durch die Sinne in das Nervensystem einfließt. Natürlich sind auch die Griechen beeinflußt durch die von der Sonne einströmenden Elohim. Aber die Sache ging so vor sich, daß bei den Griechen alles, was auf die Sinne wirkt, dem Jupiter- oder Zeus­Ein fluß hingegeben war, und dieses Volk dadurch seine Größe erlangte. In alledem, was die Griechen sehen als äußere Form, äußeres Leben, ist für sie ein wichtiger Sinn vorhanden. Sie sehen das Geistige in den sinn­lichen Anschauungen und werden dadurch das Grundvolk aller Plastik, das Grundvolk aller äußeren Formgebung. Damit haben wir schon hingewiesen auf eine ganz besondere Mission des griechischen Volkes, das gerade in ausgezeichneter Weise das Jupiter- oder Zeus-Volk ist, welches sich, auch in der Zeit, in der insbesondere durch die eintretende Sternkonstellation das Zusammenwirken der Zeus- oder Jupiter-Kräfte mit den allgemeinen Elohim-Kräften stattfand, als das Zeus-Volk fühlte.",
      "Modifikationen dieses Jupiter-Einflusses sind im Grunde genommen alle vorderasiatischen und namentlich europäischen Völker, und Sie können jetzt schon ahnen - da der Mensch viele Sinne hat -, daß viele Modifikationen eintreten können und daß für die Ausgestaltung der einzelnen Völker innerhalb dieser Grundrasse, die durch die Einwir­kung der Sinne auf das Nervensystem gebildet werden, der eine oder andere Sinn die Hegemonie erhalten kann. Dadurch können die ver­schiedenen Völker die verschiedenste Gestalt annehmen. Je nachdem das Auge oder das Ohr oder einer der anderen Sinne die Oberherrschaft hat, je nachdem werden die verschiedenen Völker in dieser oder jener Richtung disponiert zu der besonderen Volksrichtung innerhalb des Rassencharakters. Dadurch erwachsen ihnen ganz bestimmte Aufgaben. Eine Aufgabe, die besonders der kaukasischen Rasse obliegt, ist die: Sie",
      "soll den Weg machen durch die Sinne zum Geistigen, denn sie ist auf die Sinne hin organisiert.",
      "Hier liegt etwas von dem, was auch in die tieferen Ausgangspunkte des Okkultismus hineinführt und Ihnen zeigen wird, daß bei denjeni­gen Völkern, deren Zeichen sozusagen in dem Venus-Charakter liegt, der Hauptausgangspunkt - auch in der okkulten Ausbildung - da genommen werden muß, wo das Atmen das Wichtigste ist. Dagegen muß bei allem, was mehr im Westen liegt, der Ausgangspunkt von einer Vertiefung und Vergeistigung dessen genommen werden, was in der Sinneswelt liegt.",
      "Das haben in den höheren Erkenntnisstufen, in der Imagination, Inspiration und Intuition ganz in dem Sinne, wie der Jupitergeist ursprünglich den Charakter modifiziert, diejenigen Volks­tümer, die nach dem Westen gelegen sind. Deshalb gab es diese zwei Zentren immer in der Menschheitsevolution: jenes Zentrum, das sozu­sagen mehr von den Geistern der Venus regiert wurde, und jenes Zen­trum, das mehr regiert wurde von den Geistern des Jupiter.",
      "Die Geister des Jupiter wurden besonders beobachtet in jenen Mysterien, in denen sich zuletzt zusammengefunden haben - wie diejenigen wissen werden, die an meinem vorjährigen Münchener Vortragszyklus teilgenommen haben - die drei Individualitäten, die drei geistigen Wesenheiten des Buddha, des Zarathustra oder Zarathas in seiner späteren Inkarnation und desjenigen großen Führers der Menschheit, den wir mit dem Namen Skythianos bezeichnen. Das ist das Kollegium, das sich, unter der Führung eines noch Größeren, die Aufgabe gesetzt hat, die geheimnis­vollen Kräfte zu untersuchen, welche ausgebildet werden müssen für die Evolution der Menschheit, deren Ausgangspunkt genommen wor­den ist von jenem Punkte, der ursprünglich zusammenhängt mit den Jupiter-Kräften und in der erwähnten Landkarte der Erde vorher­bestimmt war.",
      "Auf das Drüsen-System endlich - nur auf dem Umwege durch alle anderen Systeme - wirkt dasjenige, was wir bezeichnen können als die abnormen Geister der Form, die im Saturn ihren Mittelpunkt haben. Da haben wir in allem, was wir als Saturn-Rasse zu bezeichnen haben, in allem, dem wir den Saturn-Charakter beizumessen haben, etwas zu suchen, was sozusagen zusammenführt, zusammenschließt das, was",
      "wieder der Abenddämmerung der Menschheit zuführt, deren Entwik­kelung in gewisser Weise zum Abschluß bringt, und zwar zu einem wirklichen Abschluß, zu einem Hinsterben. Wie sich das Wirken auf das Drüsensystem ausdrückt, sehen wir an der indianischen Rasse.",
      "Dar­auf beruht die Sterblichkeit derselben, ihr Verschwinden. Der Saturn­Einfluß wirkt durch alle anderen Systeme zuletzt auf das Drüsensystem ein. Das sondert aus die härtesten Teile des Menschen, und man kann daher sagen, daß dieses Hinsterben in einer Art Verknöcherung besteht, wie dies im Äußeren doch deutlich sich offenbart.",
      "Sehen Sie sich doch die Bilder der alten Indianer an, und Sie werden gleichsam mit Händen greifen können den geschilderten Vorgang, in dem Niedergang dieser Rasse. In einer solchen Rasse ist alles dasjenige gegenwärtig geworden, auf eine besondere Art gegenwärtig geworden, was in der Saturnent­wickelung vorhanden war; dann aber hat es sich in sich selber zurück­gezogen und hat den Menschen mit seinem harten Knochensystem allein gelassen, hat ihn zum Absterben gebracht.",
      "Man fühlt etwas von dieser wirklich okkulten Wirksamkeit, wenn man noch im neunzehnten Jahr­hundert sieht, wie ein Vertreter dieser alten Indianer davon spricht, daß in ihm lebt, was vorher für die Menschen groß und gewaltig war, das aber die Weiterentwickelung unmöglich mitmachen konnte. Es existiert die Schilderung einer schönen Szene, bei welcher ein Führer der untergehenden Indianer einem europäischen Eindringling gegen­übersteht.",
      "Denken Sie sich, was da Herz gegen Herz fühlt, indem sich zwei solche Menschen gegenüberstehen: Menschen, die von Europa herüberkamen, und Menschen, die in frühester Zeit, als die Rassen ver­teilt wurden, nach Westen hinübergegangen sind. Da haben die India­ner nach Westen hinübergenommen alles, was groß war in der atlanti­schen Kultur.",
      "Was war für den Indianer das Größte? Es war, daß er noch ahnen konnte etwas von der alten Größe und Herrlichkeit eines Zeitalters, das in der alten atlantischen Zeit vorhanden war, wo noch wenig um sich gegriffen hatte die Rassenspaltung, wo die Menschen hinaufschauen konnten nach der Sonne und wahrzunehmen vermoch­ten die durch das Nebelmeer eindringenden Geister der Form.",
      "Durch ein Nebelmeer blickte der Atlantier hinauf zu dem, was sich für ihn nicht spaltete in eine Sechs- oder Siebenheit, sondern zusammenwirkte.",
      "Das, was zusammenwirkte von den sieben Geistern der Form, das nannte der Atlantier den großen Geist, der in der alten Atlantis dem Menschen sich offenbarte. Dadurch hat er nicht mit aufgenommen das, was die Venus-, Merkur-, Mars- und Jupiter-Geister bewirkt haben im Osten.",
      "Durch dieses haben sich gebildet alle die Kulturen, die in Europa in der Mitte des neunzehnten Jahrhunderts zur Blüte gebracht wurden. Das alles hat er, der Sohn der braunen Rasse, nicht mitgemacht. Er hat festgehalten an dem großen Geist der urfernen Vergangenheit.",
      "Das, was die anderen gemacht haben, die in urferner Vergangenheit auch den großen Geist aufgenommen haben, das trat ihm vor Augen, als ihm ein Blatt Papier mit vielen kleinen Zeichen, den Buchstaben, von wel­chen er nichts verstand, vorgelegt wurde. Alles das war ihm fremd, aber er hatte noch in seiner Seele den großen Geist.",
      "Seine Rede ist uns aufbewahrt; sie ist bezeichnend, weil sie auf das Angedeutete hinweist, und sie lautet etwa so: «Da in dem Erdboden, wo die Eroberer unseres Landes schreiten, sind die Gebeine meiner Brüder begraben. Warum dürfen die Füße unserer Überwinder über die Gräber meiner Brüder schreiten?",
      "Weil sie im Besitze sind dessen, was groß macht den weißen Mann. Den braunen Mann macht etwas anderes groß. Ihn macht groß der große Geist, der zu ihm spricht in dem Wehen des Windes, in dem Rauschen des Waldes, dem Wogen des Wassers, in dem Rieseln der Quelle, in Blitz und Donner.",
      "Das ist der Geist, der für uns Wahr­heit spricht. Oh, der große Geist spricht Wahrheit! Eure Geister, die ihr auf dem Papiere hier habt, und die dasjenige ausdrücken, was für euch groß ist, die sprechen nicht die Wahrheit.» So sagte der Indianer­häuptling von seinem Standpunkte aus.",
      "Dem großen Geiste gehört der braune Mann, der blasse Mann gehört den Geistern, die in schwarzer Gestalt als kleine zwerghafte Wesen - er meinte die Buchstaben - auf dem Papier herumhüpfen; die sprechen nicht wahr. - Das ist ein welt-historischer Dialog, der gepflogen worden ist zwischen den Eroberern und dem letzten der großen Häuptlinge der braunen Männer. Da sehen wir, was dem Saturn mit seinem Wirken angehört und was aus dem Zusammenwirken mit anderen Geistern in einem solchen Momente, wo zwei Richtungen sich begegnen, auf der Erde entsteht.",
      "So haben wir gesehen, wie auf der Oberfläche unserer Erde herbeigeführt",
      "wird die allgemeine Menschheit durch die Elohim oder die normalen Geister der Form, wie sich dann heraushebt aus der gesamten Menschenmasse, aus der gesamten Menschenflut dasjenige, was die fünf Hauptrassen der Menschheitsentwickelung sind und wie diese zusam­menhängen mit den führenden Geistern in der Reihe der abnormen Gei­ster der Form, die wir mit den Namen benennen müssen, welche wir den fünf Planeten entnehmen, während die normalen Geister der Form in der Sonne und im Mond zu suchen sind. Von da werden wir weiter­gehen, übergehen zu etwas, das uns leichter werden wird, weil wir an Bekanntes, an Stämme und Völker werden anknüpfen können."
    ],
    "sentences": [
      [
        "Sie können sich denken, daß es eine sehr komplizierte Sache ist, wenn die Geister der verschiedenen Hierarchien mit ihren Kräften so zusam­menwirken müssen, daß die Erdenmission erfüllt werden kann, sozu­sagen so wirken müssen, daß zuletzt eine Gleichgewichtslage heraus­kommt.",
        "Daher werden Sie auch begreifen, daß Angaben wie diejenigen, die gestern gemacht worden sind, immer nur dann gemacht werden können, wenn man einen ganz bestimmten Punkt der Entwickelung ergreift, und daß sich die ganze Darstellung sofort verändert, wenn man die Evolution an einem anderen Punkte betrachtet.",
        "Daher werden Sie auch, wenn Sie zu einem geschlossenen Verständnis gerade dieser sehr komplizierten Sache kommen wollen, immer den einen Vortrags­zyklus mit dem andern zusammenhalten müssen."
      ],
      [
        "Ich will nur einen Punkt hervorheben, und das, was ich jetzt in diesem Augenblicke sage, soll eine Art von Anmerkung sein.",
        "In unserem Erdengleichgewicht stellt sich das ganze Zusammenwirken der Hierar­chien so dar, daß wir das, was wir gestern als dritte Hierarchie bezeich­neten - die Geister des Willens, die Cherubim und Seraphim -, suchen müssen als etwas, was in bezug auf diese Gleichgewichtslage aus der Erde heraus wirkt.",
        "Natürlich müssen Sie sich vorstellen, daß diese Hierarchie ursprünglich aus dem Weltall herein gegen den Erdmittel­punkt ihre Kräfte entfaltet, und daß, wie der Mensch diese Kräfte gewahr wird, nicht deren direkter Richtung entspricht, sondern der umgekehrten, welche sie erfahren, indem sie zurückgeworfen, reflek­tiert werden.",
        "Daher werden Sie zum Beispiel von dem ganz Intimen der Vorgänge, die da stattfinden, erst dann sich eine geschlossene Vor­stellung zu machen vermögen, wenn Sie das gestern Gesagte mit man­chem vergleichen, was über die Hierarchien in meinem Vortragszyklus in Düsseldorf gesagt worden ist, wo der himmlische Teil des Wirkens der drei Hierarchien in geschlossener Darstellung gegeben wurde.",
        "Diese Dinge sind eben nicht einfach, und um die Erdenmission begreiflich zu"
      ],
      [
        "machen, ist es notwendig, den Gesichtspunkt so zu wählen, daß wir die zurückstrahlungen der Geister dieser Hierarchien in dem, was wir die Elemente des Erdendaseins nennen, erblicken."
      ],
      [
        "Wenn Sie dies berücksichtigen, dann werden Sie aber auch ein Ge­fühl bekommen von der unendlichen Weisheit, welche in dem ganzen Zusammenhang der Kräfte des Universums, der Kräfte des Kosmos ruht.",
        "Sie werden gewissermaßen auch dafür ein Gefühl erhalten, daß die Erkenntnisse immer weiter zu gehen haben, daß sie keine Grenze haben, da die Dinge so kompliziert sind, daß, wenn wir einen Gesichts­punkt erfaßt zu haben glauben, wir gleich genötigt sind, zu einem ande­ren überzugehen, der uns die Sache wieder von einer anderen Seite beleuchtet erscheinen läßt."
      ],
      [
        "Wir können nur nach und nach in unseren Erkenntnissen aufrücken, aber Sie werden dennoch aus den Andeu­tungen, die gestern gemacht worden sind, namentlich am Schlusse der Darstellung, sich etwas genauer bekannt gemacht haben mit dem, was man nennen kann: Zusammenwirken der abnormen und normalen Geister der Form, damit innerhalb unseres Erdenlebens nicht bloß ein einheitliches, sich über die ganze Erde ausbreitendes, gleichartiges Men­schentum entsteht, sondern damit ein solches Menschentum entsteht, das sich in der Mannigfaltigkeit der einzelnen Rassen ausleben kann.",
        "Zu jenem einheitlichen Menschentum, das der Mensch nur im Verlaufe der Erdenevolution wieder erreichen kann, wäre notwendig gewesen die reine Wirksamkeit der normalen Geister der Form."
      ],
      [
        "Es sind das die­selben geistigen Wesenheiten, welche in der Genesis mit dem Namen der Elohim benannt werden, und es sind eigentlich im gesamten Uni­versum, das die Erde umgibt und mit ihr zusammen ein Ganzes aus­macht, sieben solcher Geister der Form in normaler Entwickelung zu erkennen.",
        "Es gibt also sieben Geister der Form oder sieben Elohim."
      ],
      [
        "Wenn wir uns diese sieben Elohim mit ihren verschiedenen Missionen und dem Beruf, in der gesamten Erdenmission das Gleichgewicht oder die Liebe herzustellen, vorstellen wollen, dann müssen wir uns klar sein darüber, daß diese sieben Geister der Form in dem gesamten Weltall so zusammenwirken, daß wirklich das zustande kommen würde, was wir in einem der Vorträge als «den Menschen im zweiten Drittel seines Lebens» charakterisiert haben.",
        "Da würde der eigentliche Ich-Mensch"
      ],
      [
        "sich ausprägen, wenn alle diese sieben Geister der Form in der entspre­chenden Weise, wie sie es für sich allein durch ihre eigene Gemeinschaft sich vorgenommen haben, wirken könnten.",
        "Weil aber andere geistige Wesenheiten mitwirken und dieses einheitliche Menschentum ver­mannigfaltigen, so war im Kosmos eine ganz besondere Einrichtung not­wendig."
      ],
      [
        "Wenn Sie heute die Lokalität im Kosmos suchen wollen, von der aus die normalen Geister der Form wirksam sind - also diejenigen Wesenheiten, die,wie ich das gestern charakterisierte, uns zuletzt im Lich­te entgegenstrahlen innerhalb unseres gegenwärtigen Kosmos-, so müs­sen Sie dieselben in der Sonne suchen.",
        "Sie müssen jedesmal in der Richtung der Sonne jene kosmische Loge, jene Gemeinschaft im Weltall suchen, wo diese Geister der Form ihre Beratungen pflegen zur Herstellung des irdischen Gleichgewichts, zur Erfüllung der irdischen Mission."
      ],
      [
        "Nur eines war notwendig, damit die abnormen Geister der Form durch ihre Wirksamkeit nicht gar zu große Unordnung in bezug auf den Menschen hervorriefen, es war notwendig, daß sich einer der Geister der Form ablöste aus der Gemeinschaft, so daß Sie eigentlich nur sechs dieser Geister der Form oder Elohim in der Sonnenrichtung zu suchen haben.",
        "Einer dieser Geister mußte sich, damit durch die gleichzeitige Wirksam­keit der abnormen Geister der Form - die eigentlich Geister der Bewe­gung sind - nicht völlige Unordnung in das Gleichgewicht hineinge­bracht wurde, absondern."
      ],
      [
        "Das war derjenige, welcher in der Bibel, in der Genesis, Jahve oder Jehova genannt wird.",
        "Wenn Sie dessen Wirk­samkeit im Weltall suchen wollen, so dürfen Sie nicht suchen in der Richtung, wo die Sonne steht, sondern in der Richtung, wo sich jeweilig der Mond befindet."
      ],
      [
        "Das ist auch in meiner «Geheimwissenschaft» an­gedeutet, nur von einer anderen Seite her betrachtet, indem gezeigt wird, daß die Geister der Form mit der Sonnentrennung weggehen, daß aber mit der besonderen Einrichtung, die mit der Mondtrennung zu­stande kommt, erst die Vorbedingung für die fernere Entwickelung des Menschen geschaffen wird.",
        "Denn, wenn der Mond mit der Erde verei­nigt geblieben wäre, so hätte die Evolution des Menschen nicht statt­finden können."
      ],
      [
        "Diese fernere Evolution des Menschen ist nur dadurch möglich gewesen, daß einer der Elohim, Jahve, mit dem Monde heraus­trat-während die anderen sechs Geister in der Sonne verblieben-, nur"
      ],
      [
        "dadurch, daß Jahve im Entgegenwirken zusammenwirkte mit seinen sechs anderen Genossen."
      ],
      [
        "Sie können nun die Frage aufwerfen: Warum wurde überhaupt diese Sonne abgespalten?",
        "Das war aus folgenden Gründen notwendig.",
        "Nach­dem einmal ältere Geister der Bewegung, welche eine größere Kraft als die Geister der Form haben - denn sie stehen in der Reihe der Hierar­chien höher -, sich entschlossen hatten, zurückzubleiben, mußten die normalen Geister der Form ihre Wirksamkeit durch die Abspaltung des einen abschwächen.",
        "Sie hätten sonst nicht das Gleichgewicht hervor-bringen können, welches für die fernere Entwickelung erforderlich war."
      ],
      [
        "Wenn wir eine genügende Vorstellung haben wollen von dem Wirken dieser normalen Geister der Form, so ist es das Beste, wenn wir uns sagen: Sie strahlen uns im Sonnenlichte zu.",
        "Wenn wir aber von den abnormen Geistern der Form eine Vorstellung gewinnen wollen, wie sie zusammenwirken mit den normalen Geistern der Form, die gleich­sam zentriert sind in der Sonne - denn nur, damit das Gleichgewicht hergestellt werden kann, hat sich Jehova in der Mondrichtung abge­spalten -, dann müssen wir uns vorstellen, daß eine bestimmte Sonnen-kraft, die in den normalen Geistern der Form uns zuströmt, abgeändert wird durch die Kraft, die uns zuströmt von den abnormen Geistern der Form, die eigentlich Geister der Bewegung sind.",
        "Diese finden ihren Mittelpunkt in den anderen fünf Planeten, im alten Planetenstile ge­sprochen.",
        "Da haben Sie den Mittelpunkt zu suchen für diese anderen, für die abnormen Geister der Form, also im Saturn, Jupiter, Mars, Venus, Merkur."
      ],
      [
        "Jetzt haben Sie, wenn Sie in den Kosmos hinaussehen, eine Art Verteilung für die normalen und abnormen Geister der Form.",
        "Die nor­malen Geister der Form sind zu sechs zentriert in der Sonne, der Eine - Jahve oder Jehova - hält das Gleichgewicht jenen, vom Monde aus, indem er den letzteren regiert und leitet.",
        "Beeinflußt werden die Wirkungen dieser Geister der Form durch jene Wirkungen, die von Saturn, Jupiter, Mars, Venus und Merkur ausgehen.",
        "Diese Kräfte strah­len herunter auf die Erde, werden aufgehalten und strahlen wieder von der Erde auf in der Weise, wie das gestern am Ende des Vortrages beschrieben worden ist."
      ],
      [
        "Wenn Sie also ein Stück Erdoberfläche haben, und von der Sonne aus eine bestimmte Wirkung auf dieselbe durch die Elohim oder nor­malen Geister der Form ausgeübt wird, so würde auf dem betreffenden Punkte der Erdoberfläche nichts anderes entstehen als das ganz nor­male Ich.",
        "Es würde dasjenige entstehen, was dem Menschen sein nor­males Sein, durchschnittlich sein gesamtes Menschentum gibt.",
        "Nun mischen sich hinein in diese Kräfte der Geister der Form - die sonst durch die Gleichgewichtslage hier auf der Oberfläche tanzen würden -zum Beispiel die Kräfte des Merkur.",
        "Dadurch tanzt und vibriert in dem, was hier als Kraft der Geister der Form sich entfaltet, nicht nur das Nor­male, sondern auch dasjenige,was sich hineinmischt in die normalenKräf­te der Elohim, in die normalen Kräfte der Geister der Form, nämlich das, was von diesen in den Mittelpunkten der einzelnen Planeten zentrier­ten, abnormen Geistern der Form kommt.",
        "Hieraus ergibt sich, daß fünf Mittelpunkte der Beeinflussung möglich sind durch diese abnormen Geister der Form, und diese fünf Mittelpunkte der Beeinflussung ergeben in ihrer Rückstrahlung, in ihrer Reflektierung vom Erdmittel-punkte aus auf die Menschheit in der Tat dasjenige, was wir anerkennen als die fünf Grundrassen im Erdendasein."
      ],
      [
        "Wenn wir den Punkt, den wir vor einigen Tagen in unseren Dar­legungen in Afrika gefunden haben, uns jetzt näher dadurch charak­terisieren, daß, weil die normalen Geister der Form zusammenwirken mit denjenigen abnormen Geistern der Form, die im Merkur zentriert sind, die Rasse der Neger entsteht, so bezeichnen wir okkult ganz richtig das, was in der schwarzen Rasse herauskommt, als die Merkur-Rasse."
      ],
      [
        "Jetzt verfolgen wir diese Linie weiter, die wir dazumal durch die Mittelpunkte der einzelnen Rassenausstrahlungen gezogen haben.",
        "Da kommen wir nach Asien und finden die Venus-Rasse oder die malayi­sche Rasse.",
        "Wir kommen dann durch das breite Gebiet Asiens hindurch und finden in der mongolischen Rasse die Mars-Rasse.",
        "Wir gehen dann herüber auf europäisches Gebiet und finden in den europäischen Men­schen, in ihrem Ur-Charakter, in ihrem Rassen-Charakter die Jupiter­Menschen.",
        "Gehen wir über das Meer hinüber nach Amerika, wo der Punkt, der Ort ist, an dem die Rassen oder Kulturen sterben, so finden"
      ],
      [
        "wir die Rasse des finsteren Saturn, die ursprüngliche indianische Rasse, die amerikanische Rasse.",
        "Die indianische Rasse ist also die Saturn­Rasse.",
        "Auf diese Weise bekommen Sie, wenn Sie sich okkult die Sache immer genauer vorstellen, die Kräfte, die in diesen Weltenpunkten, diesen fünf Planeten, ihre äußere materielle Offenbarung erfahren haben."
      ],
      [
        "Wenn Sie sich davon eine immer deutlichere und konkretere Vor­stellung machen, dann bekommen Sie eine innere Erkenntnis dieser eigentümlichen, über die Erde hin verbreiteten Rassen-Charaktere, eine Erkenntnis dieses eigenartigen Zusammenwirkens der normalen und der abnormen Geister der Form.",
        "Damit haben wir gleichsam das Bild gezeichnet, wie wir es in einem bestimmten Punkt festhalten können.",
        "Aber es gilt das, was ich gesagt habe für die verschiedenen Punkte der Erde, wieder nur für einen ganz bestimmten Zeitpunkt der Entwickelung.",
        "Es gilt für den Zeitpunkt, wo an einem bestimmten Momente der alten atlantischen Entwickelung die Völkerzüge von einem Punkt der Atlantis ausgehen und dorthin wandern, wo sie die entsprechende Rassenausbildung in dem betreffenden Punkte erhalten können.",
        "Daher finden Sie in meiner «Geheimwissenschaft» auch darauf hingewiesen, daß in der alten Atlantis, an ganz bestimmten Mysterien-stätten, die dort die atlantischen Orakel genannt sind, die Leitung dieser Verteilung der Menschen über die Erde in die Hand genommen wird, so daß in der Tat jenes Equilibrium, jene Gleichgewichtslage hervorgebracht werden konnte, die zur entsprechenden Rassenvertei­lung führte.",
        "In einem solchen Mysterien-Orakel wurden immer die Wahrheiten erforscht, die wir jetzt erzählen, und ursprünglich hat man sich ganz danach gerichtet.",
        "Es wurde auf diese Weise das, was auf der Erde geschah, von solchen Zentren aus in entsprechender Weise geleitet."
      ],
      [
        "Wir haben also gleichsam in der Völkerströmung, die durch Afrika hinüberzog und sich in der äthiopischen Rasse auskristallisierte, einen Impuls zu suchen, der von dem Merkur-Orakel gegeben werden konnte, in dem man ganz genau beobachtete, wie zusammenwirkten die nor­malen Geister der Form, die sechs Elohim mit Jahve oder Jehova, und wie hineinwirkten die abnormen Geister der Form, die vom Mittel­punkte des Merkur aus wirkten.",
        "Nach dem astrologischen Zusammenwirken"
      ],
      [
        "dieser verschiedenen Punkte der Kräfte wurde der Gleichge­wichtspunkt ausgesucht auf unserer Erde und danach wurde der Gleichgewichtspunkt als Ausstrahlungspunkt für die betreffende Rasse angenommen."
      ],
      [
        "In ähnlicher Weise wurde auch die Bildung der anderen Rassen geleitet.",
        "Danach wird dann die große Landkarte gezeichnet, in welche die Einflüsse eingetragen werden mit Bezug auf Völker, Geschlechter und so weiter.",
        "Das ist die große Landkarte, die ein Abbild der Him­melswirksamkeit ist, die dadurch entsteht, daß die Kräfte der Him­melswirksamkeit in die Erde hineinstrahlen, von ihr zurückstrahlen und den Menschen bestimmen."
      ],
      [
        "Als was können wir nun einen Menschen der Merkur-Rasse, der äthiopischen Rasse ansehen?",
        "Wir können ihn so ansehen, daß wir sagen:"
      ],
      [
        "Dieser Mensch ist ursprünglich durch die Elohim dazu bestimmt, dazu veranlagt gewesen, das gesamte Menschliche in seiner Totalität in sich auszudrücken.",
        "Aber nun wirkten von dem Merkurmittelpunkt aus die abnormen Geister der Form mit großer Gewalt und variierten den Menschen so, daß die Form der äthiopischen Rasse herauskam.",
        "Und so ähnlich verhält es sich bei jeder einzelnen Rasse.",
        "Dadurch aber, daß die Völkerströmungen in ganz bestimmter Weise von dem ursprüng­lichen Mittelpunkte aus geleitet worden sind, ist erst diese Linie, die ich Ihnen vor einigen Tagen zeichnete, entstanden.",
        "Sie müssen sich also denken, daß die Geister der Form von einem Mittelpunkte ausstrahlten.",
        "Diesen Mittelpunkt haben wir anzunehmen in einem bestimmten Zeit­punkte der alten Atlantis.",
        "Da haben wir das, was sich hinuntersenkt in den atlantischen Kontinent und ihn so ausgestaltet, daß die Menschen-geister unter die Herrschaft der entsprechenden abnormen Geister der Form gebracht wurden."
      ],
      [
        "Damit war die große Völkergrundlage geschaffen, und der Mensch hat, wenn er hinaufsieht in die unendlichen Weiten des Himmelsrau­mes, dort die Kräfte zu suchen, welche ihn konstituierten.",
        "Sie konsti­tuierten ihn aber in ihrer Rückstrahlung von der Erde.",
        "Indem er hinauf-blickt zu den normalen Geistern der Form, zu den Elohim, sieht er zu dem auf, was ihn eigentlich zum Menschen macht, und indem er hinauf-blickt zu dem, was in den einzelnen Planetengeistern - abgesehen von"
      ],
      [
        "Sonne und Mond - zentriert ist, sieht er das, was ihn zu einer bestimm­ten Rasse macht."
      ],
      [
        "Wie arbeiten nun in und an den Menschen diese Rassengeister?",
        "Sie arbeiten in sehr eigentümlicher Art, so, daß sie, man möchte sagen, durchkochen seine Kräfte zunächst bis in den physischen Leib hinein.",
        "Nun wissen Sie ja, daß sich dasjenige, was wir die vier Grundteile des Menschen nennen, projiziert, abbildet in jeweiligen Teilen des physi­schen Leibes, so daß wir sagen können: Es bildet sich ab dasjenige, was das Ich ist, im Blut; dasjenige, was der astralische Leib ist, im Nerven­system; dasjenige, was der Äther- oder Lebensleib ist, im Drüsensystem, und erst der physische Leib ist ein Sichselbstsein, ein Abbild seines eigenen Wesens, das für den heutigen Menschen in sich selbst seine geschlossenen Gesetze hat.",
        "Das Ich bildet sich also ab im Blute, der Astralleib im Nervensystem, der Ätherleib im Drüsensystem."
      ],
      [
        "Zunächst können diejenigen geistigen Wesenheiten, die da in dem Menschen kochen, damit sein Rassencharakter entsteht, nicht gleich unmittelbar in die höheren Teile hineinwirken.",
        "Sie kochen zunächst in diesen Abbildungen der höheren Glieder im physischen Leibe.",
        "In den physischen Leib können sie nicht recht herein, aber sie kochen in den drei anderen Gliedern: in dem, was Abbild des Ich ist, im Blut, in dem, was Abbild des Astralleibes ist, im Nervensystem und in dem, was Abbild des Ätherleibes ist, im Drüsensystem.",
        "In diesen drei Systemen, die dem physischen Leibe angehören, aber Abbilder der höheren Glieder sind, kochen die Rassengeister, die abnormen Geister der Form."
      ],
      [
        "Sie sehen hier, daß des Menschen physischer Leib von innen bestimmt wird, so bestimmt wird, daß diese verschiedenen geistigen Wesenheiten eingreifen in die Glieder im physischen Leibe, welche die Projektionen, die Schattenbilder der höheren Glieder sind.",
        "Wo greift nun zum Bei­spiel der Merkur ein? - ich sage Merkur, um das zusammenzufassen, was sich als abnorme Geister der Form im Merkur befindet.",
        "Er greift so ein, daß er mit anderen zusammenwirkt, namentlich in das Drüsen­system.",
        "Er kocht in dem Drüsensystem drinnen, und da leben sich die Kräfte aus, die durch jenes Übergewicht der Merkurkräfte entstehen, die in der äthiopischen Rasse wirken.",
        "Alles, was der äthiopischen Rasse ihre besonderen Merkmale verleiht, das kommt davon her, daß die"
      ],
      [
        "Merkurkräfte in dem Drüsensystem der betreffenden Menschen kochen und brodeln.",
        "Das kommt davon her, daß sie auskochen, was die allge­meine, gleiche Menschengestalt zu der besonderen der äthiopischen Rasse macht mit der schwarzen Hautfarbe, dem wolligen Haar und so weiter.",
        "Diese Modifikation der allgemeinen Menschengestalt kommt also von diesen Kräften her."
      ],
      [
        "Gehen Sie nun weiter nach Asien herüber, so haben Sie in ähnlicher Weise etwas, was man als Venuskräfte bezeichnen könnte, als eine ab­norme Ausgestaltung der Geister der Form.",
        "Diese Venuskräfte wirken wiederum, indem sie ihren Angriffspunkt vorzugsweise auf das ver­legen, was wir Abbild des astralischen Leibes nennen, im Nervensystem."
      ],
      [
        "Aber sie wirken auf eine besondere Art, und zwar nicht direkt als Venusgeister, auf das Nervensystem.",
        "Es kann nämlich auf zwei Um­wegen auf das Nervensystem gewirkt werden.",
        "Der eine Umweg ist durch die Atmung."
      ],
      [
        "Indem nämlich besonders auf die Atmung gewirkt wird, setzen sich im Menschen selber diese Wirkungen im Atmungs­und im Nervensystem fest und geben ihm eine bestimmte Form.",
        "Diesen Umweg wählen sich die abnormen Geister der Form, die wir Venus-wesen nennen können, eben in der malayischen Rasse, in den gelb­schattierten Rassen von Südasien und nach den Inseln des malayischen Gebietes hin."
      ],
      [
        "Da ist ausgebreitet, so wie über das äthiopische Gebiet die Drüsenmenschheit, über diese Fläche die Menschheit, bei der die abnor­men Geister der Form auf dem Umwege durch das Atmungssystem auf das Nervensystem wirken.",
        "Im Nervensystem wird auf dem Umwege über das Atmungssystem gewirkt."
      ],
      [
        "Im Nervensystem wird ausgekocht das, was mit besonderen Modifikationen die mehr oder weniger gelb-gefärbte Menschheit gibt.",
        "Die Umwandlung, welche da bewirkt wird, drückt sich allerdings mehr in jenem Nervensystem aus, das wir mit dem Ausdruck Sonnengeflecht zusammenfassen, also nicht eigentlich in dem höheren Nervensystem, sondern in jenem geheimnisvollen Teile des Nervensystems, der in zwei Strängen parallel dem Rückenmark läuft und sich in der verschiedensten Weise ausbreitet."
      ],
      [
        "Es wird also in diesem Teile des Nervensystems auf dem Umwege durch das Atmungs­system gewirkt, der in unserem Sinne noch nicht zu der höheren geisti­gen Tätigkeit gehört.",
        "Es wird tief im unterbewußten Organismus durch"
      ],
      [
        "diese Venuskräfte gewühlt, die in diesem Rassenteile der Menschheit wirken."
      ],
      [
        "Jetzt gehen wir über die breiten, mongolischen Flächen herauf.",
        "Das sind diejenigen Flächen, in denen die Geister der Form vorzugsweise wirken, die den Umweg durch das Blut genommen haben.",
        "Da wird im Blute dasjenige ausgekocht, was die eigentliche Modifikation aus der Menschheit heraus, den Grundcharakter der Rasse bewirkt."
      ],
      [
        "Nun ist aber bei dieser mongolischen Rasse etwas höchst Eigentümliches vor­handen.",
        "Da gehen ins Blut hinein die Marsgeister.",
        "Sie arbeiten aber auf eine ganz bestimmte Weise im Blute, so daß sie den sechs Elohim, die in der Sonne zentriert sind, entgegenwirken können."
      ],
      [
        "Diesen sechs Elo­him wirken sie also entgegen in der mongolischen Rasse.",
        "Dabei machen sie eine ganz besondere Attacke nach der anderen Seite, nach Jahve oder Jehova, der abgetrennt hat sein Wirkungsgebiet von dem der sechs Elohim."
      ],
      [
        "Aber außer diesem Zusammenwirken der Marsgeister mit den sechs Elohim und Jahve, das die mongolische Rasse ergibt, gibt es noch ein Besonderes.",
        "Wenn wir die Art dieses besonderen Einflusses angeben wollen, so müssen wir sagen: Wie in das Mongolische hinein die sechs Elohim von der Sonne, Jahve vom Monde und ihnen entgegen die Marsgeister wirken, so müssen wir in einem anderen Falle anneh­men, daß von der Mondrichtung her die Jahvekräfte wieder zusam­mentreten und zusammenwirken mit den Marsgeistern, und daß da­durch eine besondere Modifikation entsteht."
      ],
      [
        "Hier haben Sie, aus dem okkultesten Hintergrunde heraus erklärt, eine besondere Modifikation der Menschheit, nämlich diejenige, die zum Semitentum gehört.",
        "Im Semitentum haben Sie eine Modifikation des gesamten Menschentums, so, daß sich ausschließt von den anderen Elohim Jahve oder Jehova und dieses Volk mit einem besonderen Charakter veranlagt, indem er zusammenwirkt mit den Geistern des Mars, um die besondere Modifi­kation dieses Volkes hervorzubringen."
      ],
      [
        "Jetzt werden Sie auch das Be­sondere einsehen, das in dem semitischen Volk und seiner Mission liegt.",
        "In einem gewissen, tiefen okkulten Sinn konnte der Schreiber der Bibel sagen, daß Jahve oder Jehova dieses Volk zu seinem Volke gemacht habe, und wenn Sie jetzt das dazu nehmen, daß hier ein Zusammen­wirken stattfindet mit den Marsgeistern, und daß die Marsgeister ihre"
      ],
      [
        "Angriffe vorzugsweise auf das Blut richten, dann werden Sie auch begreifen, warum gerade die fortgehende Wirkung des Blutes von Ge­schlecht zu Geschlecht, von Generation zu Generatiön für das semi­tisch-hebräische Volk von ganz besonderer Wichtigkeit ist, und warum im semitischen Volk der Gott Jahve sich als der Gott bezeichnet, der mit dem Blute herunterrinnt von Abraham, Isaak, Jakob und so weiter.",
        "Das ist der Weg, wie das Blut rinnt durch alle diese Geschlechter.",
        "Indem sich Jahve bezeichnet: «Ich bin der Gott Abrahams, Isaaks und Ja­kobs», sagt er: Ich wirke in eurem Blute. - Was immer im Blute wirkt, was im Blute ausgefochten werden muß, das Zusammenwirken mit den Marsgeistern, das ist eines der Mysterien, die uns tief hineinführen in die weise Führung der gesamten Menschheit der Erde."
      ],
      [
        "So also sehen Sie, daß auf das Blut der Menschheit in zweifacher Weise gewirkt wird, daß zwei Rassenbildungen sozusagen entstehen, indem auf das Blut der Menschheit gewirkt wird.",
        "Auf der einen Seite haben wir alles dasjenige, was wir die mongolische Rasse nennen, auf der anderen Seite dasjenige, was wir als zum Semitentum gehörig bezeichnen können.",
        "Das ist eine große Polarität in der Menschheit, und wir werden auf diese Polarität unendlich Bedeutungsvolles zurückzu­führen haben, wenn wir die Tiefen der Volksseelen werden verstehen wollen."
      ],
      [
        "Wir haben noch weiter zu verfolgen, wie die Geister und Wesenhei­ten, die im Jupiter ihren Mittelpunkt haben, in dem Menschen kochen und brodeln.",
        "Diese wählen sich nun den zweiten Angriffspunkt, um unmittelbar auf das Nervensystem zu wirken, und zwar geht durch alles das, was die Sinne des Menschen sind, der eine Angriffspunkt; der ande­re Angriffspunkt, der in das Nervensystem hineinwirkt, geht auf dem Umwege durch das Atmungssystem in das Sonnengeflecht.",
        "Der Angriff, der von dem Jupiter ausgeht, geht auf dem Umweg durch die Sinnes­eindrücke und strömt von da aus auf die Teile des Nervensystems, die im Gehirn und Rückenmark zentriert sind.",
        "Da hinein fließen also bei denjenigen Rassen, die zur Jupiter-Menschheit gehören, jene Kräfte, die den Rassencharakter besonders ausprägen.",
        "Das ist bei den arischen, vorderasiatischen und europäischen Völkern, bei denen, die wir zu den Kaukasiern rechnen, mehr oder weniger der Fall.",
        "Da tritt die Modifikation"
      ],
      [
        "der allgemeinen Menschheit, die von den abnormen Geistern der Form herrührt, dadurch ein, daß die abnormen Geister, die wir als Jupiter-Geister bezeichnen können, auf die Sinne einwirken.",
        "Also durch die Sinne werden die Kaukasier bestimmt."
      ],
      [
        "Nun werden Sie auch begreifen, daß ein ganz eminent und bewußt unter dem Jupiter- oder Zeus-Ein fluß stehendes Volk, wie die Griechen, die sich als Mittelpunkt für den Zeus-Einfluß fühlen, hervorragend bestimmt wird durch das, was durch die Sinne in das Nervensystem einfließt.",
        "Natürlich sind auch die Griechen beeinflußt durch die von der Sonne einströmenden Elohim.",
        "Aber die Sache ging so vor sich, daß bei den Griechen alles, was auf die Sinne wirkt, dem Jupiter- oder Zeus­Ein fluß hingegeben war, und dieses Volk dadurch seine Größe erlangte.",
        "In alledem, was die Griechen sehen als äußere Form, äußeres Leben, ist für sie ein wichtiger Sinn vorhanden.",
        "Sie sehen das Geistige in den sinn­lichen Anschauungen und werden dadurch das Grundvolk aller Plastik, das Grundvolk aller äußeren Formgebung.",
        "Damit haben wir schon hingewiesen auf eine ganz besondere Mission des griechischen Volkes, das gerade in ausgezeichneter Weise das Jupiter- oder Zeus-Volk ist, welches sich, auch in der Zeit, in der insbesondere durch die eintretende Sternkonstellation das Zusammenwirken der Zeus- oder Jupiter-Kräfte mit den allgemeinen Elohim-Kräften stattfand, als das Zeus-Volk fühlte."
      ],
      [
        "Modifikationen dieses Jupiter-Einflusses sind im Grunde genommen alle vorderasiatischen und namentlich europäischen Völker, und Sie können jetzt schon ahnen - da der Mensch viele Sinne hat -, daß viele Modifikationen eintreten können und daß für die Ausgestaltung der einzelnen Völker innerhalb dieser Grundrasse, die durch die Einwir­kung der Sinne auf das Nervensystem gebildet werden, der eine oder andere Sinn die Hegemonie erhalten kann.",
        "Dadurch können die ver­schiedenen Völker die verschiedenste Gestalt annehmen.",
        "Je nachdem das Auge oder das Ohr oder einer der anderen Sinne die Oberherrschaft hat, je nachdem werden die verschiedenen Völker in dieser oder jener Richtung disponiert zu der besonderen Volksrichtung innerhalb des Rassencharakters.",
        "Dadurch erwachsen ihnen ganz bestimmte Aufgaben.",
        "Eine Aufgabe, die besonders der kaukasischen Rasse obliegt, ist die: Sie"
      ],
      [
        "soll den Weg machen durch die Sinne zum Geistigen, denn sie ist auf die Sinne hin organisiert."
      ],
      [
        "Hier liegt etwas von dem, was auch in die tieferen Ausgangspunkte des Okkultismus hineinführt und Ihnen zeigen wird, daß bei denjeni­gen Völkern, deren Zeichen sozusagen in dem Venus-Charakter liegt, der Hauptausgangspunkt - auch in der okkulten Ausbildung - da genommen werden muß, wo das Atmen das Wichtigste ist.",
        "Dagegen muß bei allem, was mehr im Westen liegt, der Ausgangspunkt von einer Vertiefung und Vergeistigung dessen genommen werden, was in der Sinneswelt liegt."
      ],
      [
        "Das haben in den höheren Erkenntnisstufen, in der Imagination, Inspiration und Intuition ganz in dem Sinne, wie der Jupitergeist ursprünglich den Charakter modifiziert, diejenigen Volks­tümer, die nach dem Westen gelegen sind.",
        "Deshalb gab es diese zwei Zentren immer in der Menschheitsevolution: jenes Zentrum, das sozu­sagen mehr von den Geistern der Venus regiert wurde, und jenes Zen­trum, das mehr regiert wurde von den Geistern des Jupiter."
      ],
      [
        "Die Geister des Jupiter wurden besonders beobachtet in jenen Mysterien, in denen sich zuletzt zusammengefunden haben - wie diejenigen wissen werden, die an meinem vorjährigen Münchener Vortragszyklus teilgenommen haben - die drei Individualitäten, die drei geistigen Wesenheiten des Buddha, des Zarathustra oder Zarathas in seiner späteren Inkarnation und desjenigen großen Führers der Menschheit, den wir mit dem Namen Skythianos bezeichnen.",
        "Das ist das Kollegium, das sich, unter der Führung eines noch Größeren, die Aufgabe gesetzt hat, die geheimnis­vollen Kräfte zu untersuchen, welche ausgebildet werden müssen für die Evolution der Menschheit, deren Ausgangspunkt genommen wor­den ist von jenem Punkte, der ursprünglich zusammenhängt mit den Jupiter-Kräften und in der erwähnten Landkarte der Erde vorher­bestimmt war."
      ],
      [
        "Auf das Drüsen-System endlich - nur auf dem Umwege durch alle anderen Systeme - wirkt dasjenige, was wir bezeichnen können als die abnormen Geister der Form, die im Saturn ihren Mittelpunkt haben.",
        "Da haben wir in allem, was wir als Saturn-Rasse zu bezeichnen haben, in allem, dem wir den Saturn-Charakter beizumessen haben, etwas zu suchen, was sozusagen zusammenführt, zusammenschließt das, was"
      ],
      [
        "wieder der Abenddämmerung der Menschheit zuführt, deren Entwik­kelung in gewisser Weise zum Abschluß bringt, und zwar zu einem wirklichen Abschluß, zu einem Hinsterben.",
        "Wie sich das Wirken auf das Drüsensystem ausdrückt, sehen wir an der indianischen Rasse."
      ],
      [
        "Dar­auf beruht die Sterblichkeit derselben, ihr Verschwinden.",
        "Der Saturn­Einfluß wirkt durch alle anderen Systeme zuletzt auf das Drüsensystem ein.",
        "Das sondert aus die härtesten Teile des Menschen, und man kann daher sagen, daß dieses Hinsterben in einer Art Verknöcherung besteht, wie dies im Äußeren doch deutlich sich offenbart."
      ],
      [
        "Sehen Sie sich doch die Bilder der alten Indianer an, und Sie werden gleichsam mit Händen greifen können den geschilderten Vorgang, in dem Niedergang dieser Rasse.",
        "In einer solchen Rasse ist alles dasjenige gegenwärtig geworden, auf eine besondere Art gegenwärtig geworden, was in der Saturnent­wickelung vorhanden war; dann aber hat es sich in sich selber zurück­gezogen und hat den Menschen mit seinem harten Knochensystem allein gelassen, hat ihn zum Absterben gebracht."
      ],
      [
        "Man fühlt etwas von dieser wirklich okkulten Wirksamkeit, wenn man noch im neunzehnten Jahr­hundert sieht, wie ein Vertreter dieser alten Indianer davon spricht, daß in ihm lebt, was vorher für die Menschen groß und gewaltig war, das aber die Weiterentwickelung unmöglich mitmachen konnte.",
        "Es existiert die Schilderung einer schönen Szene, bei welcher ein Führer der untergehenden Indianer einem europäischen Eindringling gegen­übersteht."
      ],
      [
        "Denken Sie sich, was da Herz gegen Herz fühlt, indem sich zwei solche Menschen gegenüberstehen: Menschen, die von Europa herüberkamen, und Menschen, die in frühester Zeit, als die Rassen ver­teilt wurden, nach Westen hinübergegangen sind.",
        "Da haben die India­ner nach Westen hinübergenommen alles, was groß war in der atlanti­schen Kultur."
      ],
      [
        "Was war für den Indianer das Größte?",
        "Es war, daß er noch ahnen konnte etwas von der alten Größe und Herrlichkeit eines Zeitalters, das in der alten atlantischen Zeit vorhanden war, wo noch wenig um sich gegriffen hatte die Rassenspaltung, wo die Menschen hinaufschauen konnten nach der Sonne und wahrzunehmen vermoch­ten die durch das Nebelmeer eindringenden Geister der Form."
      ],
      [
        "Durch ein Nebelmeer blickte der Atlantier hinauf zu dem, was sich für ihn nicht spaltete in eine Sechs- oder Siebenheit, sondern zusammenwirkte."
      ],
      [
        "Das, was zusammenwirkte von den sieben Geistern der Form, das nannte der Atlantier den großen Geist, der in der alten Atlantis dem Menschen sich offenbarte.",
        "Dadurch hat er nicht mit aufgenommen das, was die Venus-, Merkur-, Mars- und Jupiter-Geister bewirkt haben im Osten."
      ],
      [
        "Durch dieses haben sich gebildet alle die Kulturen, die in Europa in der Mitte des neunzehnten Jahrhunderts zur Blüte gebracht wurden.",
        "Das alles hat er, der Sohn der braunen Rasse, nicht mitgemacht.",
        "Er hat festgehalten an dem großen Geist der urfernen Vergangenheit."
      ],
      [
        "Das, was die anderen gemacht haben, die in urferner Vergangenheit auch den großen Geist aufgenommen haben, das trat ihm vor Augen, als ihm ein Blatt Papier mit vielen kleinen Zeichen, den Buchstaben, von wel­chen er nichts verstand, vorgelegt wurde.",
        "Alles das war ihm fremd, aber er hatte noch in seiner Seele den großen Geist."
      ],
      [
        "Seine Rede ist uns aufbewahrt; sie ist bezeichnend, weil sie auf das Angedeutete hinweist, und sie lautet etwa so: «Da in dem Erdboden, wo die Eroberer unseres Landes schreiten, sind die Gebeine meiner Brüder begraben.",
        "Warum dürfen die Füße unserer Überwinder über die Gräber meiner Brüder schreiten?"
      ],
      [
        "Weil sie im Besitze sind dessen, was groß macht den weißen Mann.",
        "Den braunen Mann macht etwas anderes groß.",
        "Ihn macht groß der große Geist, der zu ihm spricht in dem Wehen des Windes, in dem Rauschen des Waldes, dem Wogen des Wassers, in dem Rieseln der Quelle, in Blitz und Donner."
      ],
      [
        "Das ist der Geist, der für uns Wahr­heit spricht.",
        "Oh, der große Geist spricht Wahrheit!",
        "Eure Geister, die ihr auf dem Papiere hier habt, und die dasjenige ausdrücken, was für euch groß ist, die sprechen nicht die Wahrheit.» So sagte der Indianer­häuptling von seinem Standpunkte aus."
      ],
      [
        "Dem großen Geiste gehört der braune Mann, der blasse Mann gehört den Geistern, die in schwarzer Gestalt als kleine zwerghafte Wesen - er meinte die Buchstaben - auf dem Papier herumhüpfen; die sprechen nicht wahr. - Das ist ein welt-historischer Dialog, der gepflogen worden ist zwischen den Eroberern und dem letzten der großen Häuptlinge der braunen Männer.",
        "Da sehen wir, was dem Saturn mit seinem Wirken angehört und was aus dem Zusammenwirken mit anderen Geistern in einem solchen Momente, wo zwei Richtungen sich begegnen, auf der Erde entsteht."
      ],
      [
        "So haben wir gesehen, wie auf der Oberfläche unserer Erde herbeigeführt"
      ],
      [
        "wird die allgemeine Menschheit durch die Elohim oder die normalen Geister der Form, wie sich dann heraushebt aus der gesamten Menschenmasse, aus der gesamten Menschenflut dasjenige, was die fünf Hauptrassen der Menschheitsentwickelung sind und wie diese zusam­menhängen mit den führenden Geistern in der Reihe der abnormen Gei­ster der Form, die wir mit den Namen benennen müssen, welche wir den fünf Planeten entnehmen, während die normalen Geister der Form in der Sonne und im Mond zu suchen sind.",
        "Von da werden wir weiter­gehen, übergehen zu etwas, das uns leichter werden wird, weil wir an Bekanntes, an Stämme und Völker werden anknüpfen können."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "SIEBENTER VORTRAG Kristiania, 12. Juni1910 abends",
    "paragraphs": [
      "Wenn Sie den Geist der Betrachtungen verfolgen, die wir hier in den letzten Tagen gep flogen haben, so werden Sie es begreiflich finden, daß nicht nur eine Lenkung und Leitung der Vorgänge auf unserer Erde und vor allen Dingen in der menschlichen Entwickelung durch die Wesenheiten und Kräfte der verschiedenen Hierarchien geschieht, son­dern daß die Wesenheiten dieser Hierarchien selber eine Art Evolution, eine Art Entwickelung durchmachen. Wir sprachen davon in den letz­ten Vorträgen, wie die Wesenheiten dieser oder jener Hierarchie leitend eingreifen, wie sie zusammen organisieren, zum Beispiel die Rassen als Geister der Form in normaler und ahnormaler Entwickelung.",
      "Jetzt legen wir uns einmal diese Frage vor: Rücken diese geistigen Wesenheiten, mit denen wir es da zu tun haben, auch weiter in ihrer eigenen Entwickelung? Gerade in bezug auf gewisse geistige Wesen­heiten können wir, während unserer Epoche der Entwickelung, das Schauspiel erleben, daß sie in ihrer eigenen Evolution, in ihrer eigenen Entwickelung sozusagen um eine Stufe weiter schreiten. Wir leben seit der atlantischen Katastrophe, seitdem die nachatlantische Entwicke­lung begonnen hat, in einem Zeitalter, in dem gewisse Erzengelwesen, gewisse Wesenheiten aus der Hierarchie der Archangeloi, aufsteigen in die Hierarchie des Archai oder der Zeitgeister. Das ist außerordentlich interessant zu beobachten, denn wenn wir betrachten, wie die Volks-geister, die Volksseelen, die wir als Erzengel bezeichnen, zu einem höhe­ren Rang hinaufsteigen, dann bekommen wir erst eine richtige Vorstel­lung von dem, wie es in der großen Welt eigentlich hergeht. Dieses Aufsteigen ist verbunden damit, daß in jene Verteilung der Menschheit, die wir als die Rassenverteilung ansehen müssen, seit den atlantischen Zeiten her eine zweite Art von Völker-, von Menschheitsströmung hineingeschickt worden ist. Wir müssen nämlich weit zurückblicken, zurückblicken bis in die ersten atlantischen Zeiten, wenn wir die Zeit erfassen wollen, wo die Verteilung stattgefunden hat in die fünf",
      "Hauptrassen, von denen wir gesprochen haben, wenn wir fragen wol­len: Wann sind hingekommen an den bestimmten Punkt nach Afrika diejenigen Menschen, die dann die schwarze oder äthiopische Rasse bildeten, wann sind in das südliche Asien gekommen diejenigen Völker, welche die malayische Rasse ausmachen? Da müßten wir in frühe atlan­tische Zeiten zurücksehen. Aber später wurden diesen früheren Strö­mungen andere nachgeschickt.",
      "Während also die Erde mit den Grundlagen dieser Rassen schon besiedelt war, wurden andere hineingeschickt in die bereits besiedelten Erdengebiete. Da haben wir es mit einer späteren Strömung, mit einer Strömung der späteren atlantischen Zeit zu tun.",
      "Wenn wir begreifen wollen, was da, während die Atlantis allmählich abbröckelte, in Eu­ropa, Afrika und Amerika sich als Rassenverteilung vollzog und was dann später gegen Ende der atlantischen Zeit nachgesandt worden ist und zum Teil erst nachgesandt worden ist in der nachatlantischen Ent­wickelung, so müssen wir uns klar sein darüber, daß wir es zu tun haben mit jenem mächtigen Menschheits-Strom, der vorgeschoben wird bis hinein nach Asien, bis in das indische Gebiet, und daß - wie öfter angedeutet wurde - auf den verschiedenen Punkten Völkermassen zurückbleiben, aus denen sich dann die verschiedenen Volkstümer Asiens, Afrikas und Europas ergeben haben. Wir haben es also mit einer früheren Verteilung und einer späteren Vorschiebung, einer zwei­ten Strömung zu tun.",
      "Diese zweite Strömung hatte nun den Sinn, daß in der Richtung von Westen nach Osten solche Volksgemeinschaften ausgesandt wurden, welche unter der Leitung je eines Erzengels stan­den. Aber solche Erzengel waren die lenkenden geistigen Mächte dieser ausgesandten Stämme, die weniger oder mehr entwickelt waren, die, mit anderen Worten, weniger oder mehr nahe waren der Rangerhöhung zum Zeitgeiste.",
      "Diejenige Völkerströmung, deren Erzengel zu allererst emporgestiegen war zum Range eines Zeitgeistes, haben wir im fernen Osten zu suchen. Das war diejenige Völkerströmung, die sich zusam­menschloß mit der Urbevölkerung Indiens, die Völkerströmung, die das Herrenvolk in Indien bildete und die Grundlage abgab für die erste nachatlantische Kultur, nachdem der Erzengel dieser Volksgemein­schaft zum Zeitgeist, zum ersten Zeitgeist oder Arche der nachatlantischen",
      "Kulturperiode erhoben worden war. Nun leitete dieser Zeitgeist die uralt-heilige Kultur Indiens und machte sie zur tonangebenden Kultur in der ersten nachatlantischen Periode. Die anderen Völker Asiens, die sich allmählich heranbildeten, waren lange bloß unter der Leitung von Erzengeln.",
      "Auch die Völker Europas, die zurückgeblieben waren bei der Her­überwanderung vom Westen nach Osten, waren noch lange unter der Leitung von Erzengeln, als sich der Erzengel Indiens schon erhoben hatte zum Range eines Arche, der intuierend auf die großen Lehrer Indiens, die heiligen Rishis wirkte, die dadurch, daß sie die Vermitte­lung dieses erhabenen bedeutenden Geistes bekamen, ihre hohe Mission in der schon geschilderten Weise vollbringen konnten. Lange wirkte dieser Zeitgeist, als das nordwärts von dem alten Indien vorgelagerte Volk noch unter der Leitung des Erzengels stand. Nachdem der Zeit­geist Indiens seine Mission erfüllt hatte, wurde er erhoben zu der Lei­tung der gesamten Evolution der nachatlantischen Menschheit.",
      "In der Zeit, die wir als die urpersische Zeit bezeichnen, haben wir dann den Geist der Persönlichkeit, den Zeitgeist, der der Intuitor des großen Zarathustra oder Zoroaster, des Zarathustra der Urzeit ist. Das ist wieder ein solches Beispiel, wie ein Erzengel, also eine Volksseele, sich erhebt zu dem Range eines Zeitgeistes. Das ist gerade das Schau­spiel, das wir, wie wir es am Anfange unserer heutigen Darstellung gesagt haben, in unserer Epoche erleben, daß die Erzengel sich durch die Mission, die sie verrichten, zu lenkenden und waltenden Zeitgei­stern emporarbeiten.",
      "Eine spätere Emporarbeitung ist dann diejenige, welche erfolgt aus dem ägyptischen Volke mit seinem Erzengel einerseits und dem chal­däischen Volke und seinem Erzengel andererseits. Da vollzieht sich das Ereignis, daß der Erzengel des ägyptischen Volkes aufsteigt zum Range eines führenden Zeitgeistes und sozusagen die Lenkung und Leitung dessen übernimmt, was früher dem chaldäischen Erzengel oblag, so daß der Führer in der chaldäisch-ägyptischen Periode der dritte führende, gewaltige Zeitgeist wird, der sich aus dem Range des ägyptischen Erz­engels allmählich heraufentwickelt hat. Das ist aber auch die Zeit, in der eine andere bedeutungsvolle Entwickelung sich vollzieht: die",
      "Entwickelung, die parallel geht mit der ägyptisch-chaldäischen Kultur, und auf welche sich das bezieht, was wir im letzten Vortrag besonders hervorheben mußten.",
      "Wir haben gesehen, daß eine besondere Stelle, eine besondere Bedeu­tung alles dasjenige annimmt, was zu den semitischen Stämmen gehört, und daß innerhalb des Semitentums Jahve oder Jehova herausgehoben hatte gerade diese Rasse und sie zu seinem besonderen Volke erkoren hatte. Dadurch, daß er eine einzelne Rasse zu seinem besonderen Volke erkoren hatte, brauchte er, als diese Rasse nach und nach heranwuchs, zuerst zu seinem Stellvertreter gegenüber dem Volke eine Art von Erz­engel, so daß wir in dem heranwachsenden semitischen Volke, in den Urzeiten, einen unter der fortwährenden Inspiration des Jahve oder Jehova stehenden Erzengel haben, der dann später selber zu einem Zeitgeiste heranwächst.",
      "Wir haben daher, sozusagen außer den gewöhn­lichen, fortschreitenden Zeitgeistern im alten indischen, alten persi­schen, alten chaldäischen Volke noch einen Zeitgeist, der eine besondere Rolle für sich spielt, indem er innerhalb eines einzelnen Volkes wirkt. Wir haben da einen Zeitgeist, der also in gewisser Beziehung in der Mission eines Volksgeistes auftritt; wir haben einen Zeitgeist, den wir den semitischen Volksgeist nennen müssen.",
      "Er hatte eine ganz besondere Aufgabe. Dies wird Ihnen begreiflich erscheinen, wenn Sie ins Auge fassen, daß eigentlich gerade dieses Volkstum herausgehoben war aus der normalen Entwickelung und eine besondere Führung hatte, daß sozusagen besondere Einrichtungen getroffen worden sind, um dieses Volk zu führen.",
      "Durch diese besonderen Einrichtungen hatte dieses Volk eine Mission erhalten, die wirklich für die nachatlantische Zeit von ganz besonderer Wichtigkeit und Bedeutung war, die sich von der Mission aller anderen Völker und Volkstümer unterschied. Man kann diese Mission des Semitentums eigentlich dadurch am besten begreifen, daß man sie zusammenhält mit dem, was in der nachatlantischen Zeit die verschiedenen anderen Völker als diese oder jene Mission hatten.",
      "Es gibt zwei geistige Strömungen in der Menschheit. Die eine geistige Strömung muß man nennen, wenn man sie richtig bezeichnen will, die­jenige, die von dem Pluralismus, man könnte auch sagen, von der Mo­nadologie ausgeht, die also vorzugsweise in einer Vielheit von Wesenheiten",
      "und Kräften den Ursprung und die Ouelle des Daseins sieht. Sie können nun überall in der Welt umherschauen, in irgendeiner Weise werden Sie sehen, daß die Völker der nachatlantischen Zeit von Viel­heiten des Göttlichen ausgegangen sind. Beginnen Sie bei der Dreiheit des alten Indertums, die sich später ausgelebt hat in Brahma, Shiva und Vishnu. Sehen Sie auf die deutsche Mythologie, so finden Sie die Drei­heit von Odin, Hönir und Lödur und so weiter. So werden Sie überall eine Dreiheit und diese in eine Vielheit gegliedert finden. Sie sehen diese Eigentümlichkeit aber nicht nur da, wo sozusagen Göttermythen und Götterlehren auftreten, sondern auch in den Philosophien, wo uns dieselbe als Monadologie entgegentritt. Das ist die eine Strömung, wel­che, weil sie von der Vielheit ausgeht, die größtmögliche Mannigfaltig­keit annehmen kann. Man könnte sagen: In der nachatlantischen Zeit, vom weitesten Osten in Indien und im weiten Bogen durch Asien hin­durch bis nach Europa, hat dieser Dienst der Vielheit, der sich im Grunde genommen in unserer geisteswissenschaftlichen Weltanschau­ung dadurch ausdrückt, daß wir eine Summe der verschiedensten Wesenheiten, der verschiedensten Hierarchien anerkennen, seine man­nigfaltigsten Vertretungen und Ausgestaltungen gewonnen.",
      "Diesem Dienste der Vielheit mußte eine synthetische, eine zusammen­fassende Bewegung gegenüberstehen, eine Bewegung, die streng ausging von dem Monon, dem Monismus. Die eigentlichen Inspiratoren, die Jmpulsgeber alles Monotheismus und Monismus, aller Einheitsgöttlich­keit sind die semitischen Völker. Bei ihnen liegt es in der Natur, und -wenn Sie sich erinnern an das, was heute morgen gesagt wurde - es liegt bei ihnen im Blut, den Einheitsgott, das Monon zu vertreten.",
      "Wenn der Mensch hinaussieht in das große Weltendasein, dann würde er aber nicht weit kommen, wenn er immer nur betonte: Eine Einheit, ein Monon liegt der Welt zugrunde. Der Monismus oder Mono­theismus allein genommen ist dasjenige, was nur ein letztes Ideal darstellen kann. Dies würde aber niemals zu einer wirklichen Welt-erfassung, zu einer durchgreifenden konkreten Weltanschauung führen können. Doch es mußte in der nachatlantischen Zeit auch die Strömung des Monotheismus ihre Vertretung finden, so daß einem Volke über-tragen war, das Ferment, den Impuls zu geben zu diesem Monotheismus.",
      "Diese Aufgabe war dem semitischen Volke übertragen. Daher sehen Sie, wie sozusagen mit einer gewissen abstrakten Strenge, einer abstrakten Unerbittlichkeit das monistische Prinzip gerade in diesem Volke vertreten wird, und alle anderen Völker haben insofern, als sie ihre verschiedenen göttlichen Wesenheiten in eine Einheit zusammen­fassen, den Impuls dazu bekommen von dieser Seite her. Der monisti­sche Impuls ist immer von dieser Seite gekommen. Die anderen Völker haben pluralistische Impulse.",
      "Es ist außerordentlich wichtig, daß man das ins Auge faßt. Derjenige, der sich mit dem Fortwirken der althebräischen Impulse befaßt, der sieht heute noch bei dem gelehrten Rabbiner, dem gelehrten Rabbinis­mus in seinem extremsten Element den Monotheismus walten. Daß das Weltenprinzip nur ein einheitliches sein kann, das als Impuls zu geben, ist die Aufgabe gerade dieses Volkes. Man könnte daher sagen: Alle anderen Nationen, Völker und Zeitgeister hatten eine analytische Auf­gabe, eine Aufgabe, das Weltenprinzip in verschiedene Wesenheiten gegliedert vorzustellen, wie zum Beispiel die äußerste Abstraktion des Monon in Indien bald in eine Dreigliedrigkeit zerfallen ist, wie der Einheitgott des Christentums zerfällt in die drei Personen. Die anderen Völker haben alle die Aufgabe, den Weltengrund zu analysieren und dadurch viel Inhalt zu schaffen für die einzelnen Teile dieses Welten-grundes, sich zu erfüllen mit reichem Vorstellungsmaterial, das die Erscheinungen liebevoll umfassen kann. Das semitische Volk hat die Aufgabe, abzusehen von aller Vielheit und synthetisch sich der Einheit hinzugeben, daher die Kraft der Spekulation, die Kraft des syntheti­schen Denkens, zum Beispiel in der Kabbalistik, gerade aus diesem Impuls heraus die denkbar größte ist.",
      "Was aus der Einheit durch das synthetische, das zusammenfassende Wirken des Ich jemals herausgesponnen werden konnte, ist im Laufe der Jahrtausende durch den semitischen Geist herausgesponnen worden. Das ist die große Polarität zwischen Pluralismus und Monismus, und das ist die Bedeutung des semitischen Impulses in der Welt. Monismus ist nicht ohne Pluralismus, und dieser nicht ohne jenen möglich. Daher mussen wir die Notwendigkeit beider wohl anerkennen.",
      "Die objektive Sprache der Tatsachen führt oft zu ganz anderen Erkenntnissen",
      "als die Sympathien und Antipathien, die da oder dort wal­ten. Deshalb müssen wir die einzelnen Volksgeister wohl begreifen. Während die Führer der einzelnen Völker drüben in Asien und Afrika längst aufgestiegen waren zu dem Range von Zeitgeistern oder Geistern der Persönlichkeit und zum Teil sogar schon die Anwartschaft bekom­men hatten, sich umzuwandeln von Zeitgeistern in die nächsthöhere Stufe, zu Geistern der Form - wie zum Beispiel jener Zeitgeist, der im alten Jndien gewirkt hat, in gewisser Beziehung schon zum Range der Geister der Form emporgestiegen war -, waren die einzelnen Völker Europas noch lange geführt von ihren einzelnen Erzengeln.",
      "Erst in der vierten nachatlantischen Periode hob sich aus den verschiedenen Völ­kern Europas, die von ihren Erzengeln geleitet worden sind, der Erz­engel des Griechentums heraus zu einer führenden Stellung, indem er der tonangebende Zeitgeist der griechischen, der vierten leitenden Epo­che in der nachatlantischen Zeit wurde, so daß wir also den Erzengel des Griechentums emporsteigen sehen zu dem Range eines Arche, eines Geistes der Persönlichkeit. Dasjenige, wozu sich dieser Erzengel des Griechentums vorbereitet hatte, das tritt, als er Zeitgeist geworden war, für die Welt in Asien, Afrika und Europa hervor, deren Mittelpunkt eben das griechische Volk geworden war.",
      "Während sein Erzengel zum Arche sich entwickelt hatte, war der wirkende Zeitgeist des ägyptischen und auch der des persischen Volkes hinaufgestiegen zu einer Art von Geist der Form. Das, wozu wir jetzt kommen, ist etwas außeror­dentlich Interessantes im Verlaufe der nachatlantischen Entwickelung.",
      "Durch all die Entwickelung, welche der Erzengel des Griechentums früher durchgemacht hatte, konnte er in verhältnismäßig schneller Art dasjenige durchmachen, was ihn zu einer ganz besonderen führenden Stellung als Zeitgeist befähigte. Daher geschah aber etwas höchst Be­deutungsvolles in der vierten nachatlantischen Kulturperiode.",
      "Wir wissen, daß damals das Ereignis eintrat, welches wir als das Auf­nehmen des Christusimpulses von seiten der Menschheit bezeichnen. Der Christusimpuls wurde aufgenommen, das Mysterium von Golga­tha fand statt. Der Impuls, der da gegeben worden ist, sollte im Laufe der nächsten Jahrhunderte und Jahrtausende nach und nach seine Ver­breitung auf der Erde finden. Dazu bedurfte es nicht nur der Tatsache,",
      "daß dieses Ereignis stattfand, dazu bedurfte es gewisser lenkender und führender Wesenheiten aus der Reihe der Hierarchien heraus. Und da trat nun das höchst Merkwürdige und Interessante ein, daß der Zeit­geist des Griechentums in einem bestimmten Zeitmomente, der ungefähr zusammenfällt mit dem Auf-die-Erde-Kommen des Christusimpulses, für diese unsere jetzige Periode auf den ihm dazumal möglich gewor­denen Aufstieg in die Region der Geister der Form verzichtete und der führende Zeitgeist wurde, der dann über die Zeiten hinaus wirkt.",
      "Er wird der stellvertretende, führende Geist des exoterischen Christen­tums, so daß sich also hinstellt vor den Christusimpuls der Arche, der führende Geist des Griechentums. Daher zerfällt das Griechentum so rasch in der Zeit, in welcher sich das Christentum entwickelt, weil es sozusagen seinen führenden Zeitgeist abgegeben hat, damit er Führer des exoterischen Christentums werden konnte.",
      "Es wurde der Zeitgeist des alten Griechentums der Missionar, der Inspirator oder vielmehr Intuitor des sich ausbreitenden exoterischen Christentums. Da haben wir also das Schauspiel einer solchen Resignation, von der wir gespro­chen haben, in einem konkreten Falle vor uns.",
      "Der Zeitgeist des Grie­chentums konnte, weil er seine Mission in der vierten nachatlantischen Kulturperiode so außerordentlich gut erfüllt hatte, aufsteigen in ein höheres Gebiet, verzichtete aber und wurde dadurch der führende Geist des sich ausbreitenden exoterischen Christentums, als welcher er über die verschiedenen Völker hinweg wirkte.",
      "Solch eine Verzichtleistung findet noch einmal statt, und diese zweite Verzichtleistung ist wiederum von einem ganz besonderen Interesse, gerade für diejenigen, die sich Schüler der Geist-Erkenntnis nennen. Wir haben im wesentlichen, während sich drüben in Asien, bis herein in das Agypter- und Griechentum, die einzelnen Erzengel zu Zeitgei­stern entwickeln, in Europa einzelne Völker und Volksstämme, die von ihren verschiedenen Erzengeln geleitet werden. Da haben wir in Eu­ropa, während sonst die entsprechenden Erzengel, die einst von Westen nach Osten geschickt worden sind, aufgestiegen waren in die Reihe der Zeitgeister, noch immer einen Erzengel, der in den germanischen und vor allem in den keltischen Völkern wirkte, in den Völkern, welche noch zur Zeit. in der das Christentum seinen Anfang nahm, in einem",
      "großen Teile von Westeuropa, bis hinein in das heutige Ungarn, durch Süddeutschland und durch die Alpen hindurch, verbreitet waren. Diese Völker hatten als ihren Erzengel den keltischen Volksgeist. Auch weit herauf gegen den Nordosten Europas waren die Völker des keltischen Geistes verbreitet.",
      "Sie wurden von einem bedeutenden Erzengel gelenkt, der, bald nachdem der christliche Impuls der Menschheit gegeben wor­den war, darauf verzichtet hatte, ein Arche, ein Geist der Persönlichkeit zu werden, und der sich entschloß, auf der Stufe eines Erzengels stehen zu bleiben und sich in Zukunft den verschiedensten Zeitgeistern, die da zum Beispiel innerhalb Europas entstehen würden, unterzuordnen. Da­her auch schwanden die keltischen Völker als zusammengeschlossene Völkerschaft dahin, eben weil ihr Erzengel eine besondere Resigna­tion geübt und eine besondere Mission übernommen hatte.",
      "Das ist ein charakteristisches Beispiel dafür, wie, sagen wir, das Zurückbleiben in einem solchen Falle dazu beiträgt, besondere Missionen einzuleiten. Was wurde nun aus diesem Erzengel der keltischen Völker, als er dar­auf verzichtet hatte, ein Geist der Persönlichkeit zu werden?",
      "Da wurde er der inspirierende Geist des esoterischen Christentums, und von seinen Inspirationen gehen insbesondere diejenigen Lehren und Impulse aus, die dem esoterischen Christentum, dem wahrhaften esoterischen Chri­stentum zugrunde liegen. Im Westen Europas war die geheimnisvolle Stätte zu finden für diejenigen, die in diese Geheimnisse eingeweiht wurden, wo die Inspiration stattfand durch diesen leitenden Geist, der ursprünglich eine bedeutsame Schulung als Erzengel des Keltentums absolviert hatte, der auf den Aufstieg verzichtet und eine andere Mis­sion übernommen hatte, die Mission: Inspirator des esoterischen Chri­stentums zu sein, das fortwirken sollte durch die Geheimnisse des heili­gen Gral, fortwirken sollte durch das Rosenkreuzertum.",
      "Da haben Sie das Beispiel einer Verzichtleistung, eines Zurückbleibens einer solchen Wesenheit der Hierarchien, und da haben Sie zugleich ein Beispiel, an dem Sie unmittelbar, im Konkreten erkennen können, was solch ein Zurückbleiben für eine Bedeutung hat. Trotzdem dieser Erzengel zu dem Range eines Arche hätte aufsteigen können, blieb er bei dem Range eines Erzengels und leitete dafür die bedeutsame Strömung des esoteri­schen Christentums, welche durch die verschiedensten Zeitgeister hindurch",
      "fortwirken soll. Die Zeitgeister mögen so oder so wirken, dieses esoterische Christentum wird ein Ouell sein für alles, was sich unter dem Einflusse der verschiedenen Zeitgeister wieder wandeln, metamor­phosieren kann. Da haben wir also wieder ein Beispiel, wie eine solche Resignation stattfindet, während wir sonst das große Schauspiel erle­ben, daß die Volksgeister zu Zeitgeistern, gerade in unserer Epoche, aufsteigen.",
      "Nun haben wir - im europäischen Gebiet - die verschiedenen ger­manischen Völker. Diese verschiedenen germanischen Völker Europas, die ursprünglich von einem Erzengelwesen geleitet worden sind, waren dazu berufen, nach und nach unter die Leitung der verschiedensten Erzengel zu kommen, in der verschiedensten Weise Völker-Individua­litäten zu bilden.",
      "Es ist natürlich außerordentlich schwierig - schwierig nur aus dem Grunde, weil es in gewisser Beziehung leicht Leidenschaft und Eifersucht erwecken kann -, wenn über diese Dinge unbefangen gesprochen werden soll. Daher kann auf ganz bestimmte Mysterien dieser Entwickelung nur leise hingedeutet werden.",
      "Aus der Summe jener Erzengel ging hervor der Arche, der führende Zeitgeist unserer fünften Kulturepoche der nachatlantischen Zeit. Er ging hervor, nach­dem lange, lange Zeit einer der Erzengel der germanischen Völker eine gewisse Schulung durchgemacht hatte.",
      "Derjenige Zeitgeist, welcher der Volksgeist der griechisch-lateinischen Epoche war, wurde der Zeitgeist, der, wie Sie wissen, in der späteren Zeit damit beschäftigt war, das exo­terische Christentum auszubreiten. Die spätere römische Geschichte wurde auch geleitet von einer Art von Zeitgeist, der aus dem Erzengel des Römertums aufgestiegen war und sich in seiner Wirksamkeit mit dem christlichen Zeitgeist zu gemeinsamem Wirken verband.",
      "Diese beiden waren die Erzieher jenes Erzengels, welcher die germanischen Völker führte, der zu deren führenden Erzengeln gehörte, der sich dann zum Zeitgeiste der fünften nachatlantischen Kulturperiode emporhob. Es war vieles notwendig, vor allen Dingen aber, daß eine starke Indi­vidualisierung und Vermischung der verschiedenen Völkerelemente in Europa eintrat.",
      "Das war nur dadurch möglich, daß, während drüben in Asien und Afrika die Erzengel längst zu Zeitgeistern aufgerückt waren, in Europa die Führerschaft noch bei den Erzengeln selber lag,",
      "daß die einzelnen Völkerschaften von ihren Volksseelen geleitet wur­den, unbekümmert um die Zeitgeister, ganz hingegeben den Impulsen der Volksgeister selber. Als der christliche Impuls über die Menschheit dahinging, da war in Europa ein Durcheinanderwirken von einzelnen von freiem Sinn erfüllten Volksgeistern, von denen ein jeder seine eige­nen Wege ging, und die es im Grunde genommen dadurch schwer mach­ten, daß ein die einzelnen Volksgeister führender Zeitgeist der fünften Kulturepoche entstehen konnte.",
      "Es vermischten sich, sagen wir, um jenes Volk möglich zu machen, welches das französische Gebiet bewohnt, romanische, keltische und fränkische Volkselemente. Durch diese Vermischung nahm natürlich die ganze Führung eine bestimmte Gestalt an.",
      "Sie ging sozusagen von den einzelnen, leitenden Erzengeln, welche andere Aufgaben erhalten hatten, auf andere über. - Beim lei­tenden Erzengel der Kelten haben wir gesagt, was er für eine Mission erhalten hatte. Ebenso könnten wir von den anderen Volkstümern die Mission der Erzengel angeben. - Daher kamen unter die Völker, die durch Mischung entstanden, wieder andere Erzengel, die ihre Herr­schaft antraten, als sich die verschiedenen Elemente vermischten.",
      "So war in der Tat durch lange Zeit hindurch - noch im Mittelalter - im mittleren und nördlichen Europa im Grunde genommen das führende Element bei den Erzengeln, die nur nach und nach beeinflußt wurden von dem gemeinsamen Zeitgeiste, der einherging vor dem Christusim­pulse. Es wurden die einzelnen Volksgeister in Europa vielfach die Diener des Christus-Zeitgeistes.",
      "Die Erzengel Europas stellten sich in den Dienst dieses gemeinsamen Christus-Zeitgeistes, während die einzelnen Völker kaum in der Lage waren, irgendeinen der Erzengel zu dem Range eines Zeitgeistes emporsteigen zu lassen. Erst im sechzehnten bis siebzehnten Jahrhundert - vom zwölften Jahrhundert etwa angefan­gen - bereitete sich das vor, daß der führende Zeitgeist der fünften nachatlantischen Periode herausgebildet wurde, unter dessen Einfluß wir heute noch stehen.",
      "Er gehört ebenso zu den großen, führenden Zeitgeistern wie die, welche die großen, führenden Zeitgeister waren während der ägyptisch-chaldäisch-babylonischen, urpersischen und indischen Epoche. Aber er wirkte in einer ganz eigentümlichen Weise, dieser Zeitgeist unserer fünften nachatlantischen Kulturepoche.",
      "mußte nämlich eine Art Kompromiß eingehen mit einem der alten Zeit­geister, die gewirkt haben vor dem christlichen Impulse, und zwar mit dem agyptischen Zeitgeiste, der, wie wir gehört haben, in gewisser Be­ziehung aufgestiegen ist zu dem Range eines Geistes der Form. So kommt es, daß eigentlich unsere fünfte nachatlantische Kulturperiode, in der wir stehen, von einem Zeitgeiste beherrscht ist, der in gewisser Weise sehr, sehr dem Einflusse und den Impulsen des Zeitgeistes der alten ägyptischen Kultur unterliegt und der ein sozusagen in seinen allerersten Anfängen begriffener Geist der Form ist.",
      "Das gab die vielen Zersplitterungen und Zerklüftungen unseres Zeit­alters. Ünser Zeitgeist in der fünften nachatlantischen Kulturperiode strebt dahin, sich in gewisser Beziehung zu spirituellen Höhen zu erhe­ben und die vierte nachatlantische Kulturzeit hinaufzubringen auf eine höhere Stufe. Aber es liegt darin dasjenige, was materialistische Neigung, materialistischer Hang ist, und je nachdem die verschiedenen Erzengelwesen, die verschiedenen Volksseelen eine mehr oder weniger große Hinneigung zu diesem materialistischen Hang haben, kommt unter der Führung dieses Zeitgeistes der fünften nachatlantischen Kul­turperiode ein mehr oder weniger materialistisches Volk heraus, das sozusagen dem Zeitgeiste mehr eine Nuance nach dem Materialistischen hin gibt. Ein idealistisches Volk dagegen ist ein solches, welches dem Zeitgeiste mehr eine Nuance nach dem Idealismus hin gibt.",
      "Nun bildete sich vom zwölften bis sechzehnten Jahrhundert tatsäch­lich immer mehr etwas heraus, was in gewisser Beziehung neben dem christlichen Zeitgeiste wirkte - der der fortwirkende griechische Zeit­geist ist -, so daß in der Tat, in merkwürdiger Weise, in unsere Kultur einströmt dasjenige, was wir den christlichen Zeitgeist nennen, verbun­den mit einem eigentlichen Zeitgeist der fünften nachatlantischen Kul­turperiode, und da wirkt wieder hinein das alte Ägyptertum, dessen Zeitgeist sich bis zu einem gewissen Rang der Geister der Form erhoben hat. Nun aber ist es gerade dadurch, daß ein solches Trifolium in unse­rer ganzen Zeitkultur wirkt, möglich geworden, daß in der fünften Zeitepoche die verschiedensten Nuancen von Kultur- und Volksseelen­Strömungen herauskamen. Es wurde möglich, daß der Zeitgeist die verschiedensten Farben und Nuancen in seinem Wirken aufwies. Die",
      "Erzengel, die ihre Befehle von dem Zeitgeist erhielten, wirkten in der verschiedensten Weise.",
      "Diejenigen, die im Norden wohnen, wird etwas interessieren, worauf wir in den nächsten Betrachtungen genauer werden einzugehen haben, sie wird insbesondere interessieren müssen die Frage: Wie wirkte jener Erzengel, der einstmals mit den nordischen Völkern, den skandinavi­schen Völkern heraufgeschickt worden ist in dieses Gebiet, und von dem aus die verschiedenen Erzengelwesen Europas - namentlich West-, Mittel- und Nordeuropas - die Inspirationen bekamen? In der außen­stehenden Welt kann es nur als Narretei gelten, wenn geradezu hinge­wiesen wird auf jenen Punkt des europäischen Kontinentes, von dem einst die größten Impulse nach allen Seiten ausgestrahlt sind, auf jenen Punkt, der der Sitz erhabener Geister war, bevor der keltische Volks­geist als keltisches Erzengelwesen in der Hochburg des Grals ein neues Zentrum errichtet hatte.",
      "Von jenem Punkte, der in alten Zeiten Zen­trum war für die Ausstrahlung der Geistigkeit Europas, ist auch ausge­strahlt dasjenige, was zunächst der nordische Volks-Erzengel als seine Mission erhalten hat. Für die Außenwelt muß es, wie gesagt, als Narre­tei erscheinen, wenn wir als den Punkt, von dem ausstrahlt, was nach den verschiedensten germanischen Volksstämmen hinwirkt, dasjenige Gebiet bezeichnen, das heute über Mittel-Deutschland liegt, aber eigentlich über der Erde gelegen ist.",
      "Wenn Sie etwa eine Kreislinie zögen, so daß in diese Kreislinie hineinfallen würden die Städte Det­mold und Paderborn, so kommen Sie in die Gegend, von der ausströmte die Mission der erhabensten Geister, welche nach Nord- und West-Europa ihre Mission ausdehnten. Weil dort das große Jnspirationszen­trum war, deshalb ging später die Sage, daß Asgard eigentlich an diesem Punkte der Erdoberfläche gelegen habe.",
      "Es lag aber da das große Inspi­rationszentrum in uralter Vergangenheit, das Zentrum, welches dann später seine Hauptwirksamkeit abgegeben hat an das Zentrum des heiligen Gral.",
      "Die Völker Skandinaviens mit ihren ersten Erzengeln, haben damals ganz verschiedene Anlagen mitbekommen, Anlagen, die sich heute eigentlich nur noch in der eigenartigen Konfiguration der nordischen Mythologie aussprechen. Derjenige, der im okkulten Sinne die nordische",
      "Mythologie mit anderen Mythologien vergleicht, die über die Erde geherrscht haben, der mag wissen, daß diese nordische Mythologie die ursprüngliche Anlage des Erzengels darstellt, der hier herauf nach Norden geschickt worden ist, die ursprüngliche Anlage, die bei ihrer Gestaltung stehen geblieben ist, wie wir sie sozusagen bei einem Kinde sehen müßten, wenn bestimmte Talente, latentes Genie und so weiter auf der Kindheitstufe stehen blieben. Bei dem Erzengel, der nach Skan­dinavien geschickt wurde, haben wir diejenigen Anlagen, die dann in der eigentümlichen Konfiguration der nordischen Mythologie heraus­kommen.",
      "Daher rührt die große Bedeutung der nordischen Mythologie für das Verständnis des eigentlichen, inneren Wesens der skandinavi­schen Volksseele. Daher kommt auch die große Bedeutung, welche dieses Verständnis der Mythologie hat für die weitere Fortentwik­kelung dieses Erzengels, der allerdings die Anlage in sich hat, in einer gewissen Weise, aufzusteigen zu dem Range eines Arche Aber dazu ist mancherlei notwendig.",
      "Dazu ist notwendig, daß in ganz bestimmter Weise sich jene Anlagen entwickeln, die heute in gewisser Beziehung zurückgetreten sind hinter dem dämmernden, schattenhaf­ten Einfluß des Zeitgeistes, der sich vor die Impulse des Christentums hingestellt hat. So sonderbar ähnlich manche Dinge der germanisch-nordischen Mythologie den Darstellungen der griechischen Mythologie sind, so muß doch gesagt werden, daß es keine andere Mythologie der Erde gibt, welche in ihrem eigentümlichen Aufbau, in ihrer eigenartigen Durchführung ein bedeutsameres oder klareres Bild der Weltenevolu­tion gibt, als diese nordische Mythologie, so daß dieses Bild als eine Vorstufe des geisteswissenschaftlichen Bildes der Weltenentwickelung gelten kann.",
      "Die germanische Mythologie ist in der Art, wie sie ausgebildet wor­den ist aus der Anlage des Erzengels heraus, in ihren Bildern am bedeut­samsten ähnlich dem, was nach und nach als das geisteswissenschaft­liche Weltbild für die Menschheit erwachsen soll. Es wird sich darum handeln, wie jene Anlagen werden können, die einstmals ein Erzengel mitgebracht hat in die Welt, wie sie werden können, nachdem dieser Erzengel die Erziehung des Christus-Zeitgeistes genossen hat. Diese Anlagen werden zu einem wichtigen Gliede im führenden Zeitgeist",
      "werden können, wenn in der richtigen Weise im späteren Alter der Volksentwickelung verstanden wird, dasjenige auszubilden, was diese Volksentwickelung als Anlage in einem früheren Zeitalter enthält. Damit haben wir nur hingedeutet auf ein wichtiges Problem, auf eine wichtige Evolution eines europäischen Erzengels; wir haben sozusagen darauf hingedeutet, inwiefern er eine Anlage zu einem Zeitgeiste hat.",
      "An diesem Punkte wollen wir einen Augenblick stehen bleiben und dann unsere Betrachtung so fortsetzen, daß wir versuchen, aus der Konfiguration der Volksseele heraus in eine esoterische Betrachtung der Mythologie einzutreten. Damit wird, als ein besonderes Kapitel, die Schilderung der ganzen interessanten Eigenart gerade der germa­nischen und namentlich auch der nordischen Mythologie vor unsere Seele geführt werden."
    ],
    "sentences": [
      [
        "Wenn Sie den Geist der Betrachtungen verfolgen, die wir hier in den letzten Tagen gep flogen haben, so werden Sie es begreiflich finden, daß nicht nur eine Lenkung und Leitung der Vorgänge auf unserer Erde und vor allen Dingen in der menschlichen Entwickelung durch die Wesenheiten und Kräfte der verschiedenen Hierarchien geschieht, son­dern daß die Wesenheiten dieser Hierarchien selber eine Art Evolution, eine Art Entwickelung durchmachen.",
        "Wir sprachen davon in den letz­ten Vorträgen, wie die Wesenheiten dieser oder jener Hierarchie leitend eingreifen, wie sie zusammen organisieren, zum Beispiel die Rassen als Geister der Form in normaler und ahnormaler Entwickelung."
      ],
      [
        "Jetzt legen wir uns einmal diese Frage vor: Rücken diese geistigen Wesenheiten, mit denen wir es da zu tun haben, auch weiter in ihrer eigenen Entwickelung?",
        "Gerade in bezug auf gewisse geistige Wesen­heiten können wir, während unserer Epoche der Entwickelung, das Schauspiel erleben, daß sie in ihrer eigenen Evolution, in ihrer eigenen Entwickelung sozusagen um eine Stufe weiter schreiten.",
        "Wir leben seit der atlantischen Katastrophe, seitdem die nachatlantische Entwicke­lung begonnen hat, in einem Zeitalter, in dem gewisse Erzengelwesen, gewisse Wesenheiten aus der Hierarchie der Archangeloi, aufsteigen in die Hierarchie des Archai oder der Zeitgeister.",
        "Das ist außerordentlich interessant zu beobachten, denn wenn wir betrachten, wie die Volks-geister, die Volksseelen, die wir als Erzengel bezeichnen, zu einem höhe­ren Rang hinaufsteigen, dann bekommen wir erst eine richtige Vorstel­lung von dem, wie es in der großen Welt eigentlich hergeht.",
        "Dieses Aufsteigen ist verbunden damit, daß in jene Verteilung der Menschheit, die wir als die Rassenverteilung ansehen müssen, seit den atlantischen Zeiten her eine zweite Art von Völker-, von Menschheitsströmung hineingeschickt worden ist.",
        "Wir müssen nämlich weit zurückblicken, zurückblicken bis in die ersten atlantischen Zeiten, wenn wir die Zeit erfassen wollen, wo die Verteilung stattgefunden hat in die fünf"
      ],
      [
        "Hauptrassen, von denen wir gesprochen haben, wenn wir fragen wol­len: Wann sind hingekommen an den bestimmten Punkt nach Afrika diejenigen Menschen, die dann die schwarze oder äthiopische Rasse bildeten, wann sind in das südliche Asien gekommen diejenigen Völker, welche die malayische Rasse ausmachen?",
        "Da müßten wir in frühe atlan­tische Zeiten zurücksehen.",
        "Aber später wurden diesen früheren Strö­mungen andere nachgeschickt."
      ],
      [
        "Während also die Erde mit den Grundlagen dieser Rassen schon besiedelt war, wurden andere hineingeschickt in die bereits besiedelten Erdengebiete.",
        "Da haben wir es mit einer späteren Strömung, mit einer Strömung der späteren atlantischen Zeit zu tun."
      ],
      [
        "Wenn wir begreifen wollen, was da, während die Atlantis allmählich abbröckelte, in Eu­ropa, Afrika und Amerika sich als Rassenverteilung vollzog und was dann später gegen Ende der atlantischen Zeit nachgesandt worden ist und zum Teil erst nachgesandt worden ist in der nachatlantischen Ent­wickelung, so müssen wir uns klar sein darüber, daß wir es zu tun haben mit jenem mächtigen Menschheits-Strom, der vorgeschoben wird bis hinein nach Asien, bis in das indische Gebiet, und daß - wie öfter angedeutet wurde - auf den verschiedenen Punkten Völkermassen zurückbleiben, aus denen sich dann die verschiedenen Volkstümer Asiens, Afrikas und Europas ergeben haben.",
        "Wir haben es also mit einer früheren Verteilung und einer späteren Vorschiebung, einer zwei­ten Strömung zu tun."
      ],
      [
        "Diese zweite Strömung hatte nun den Sinn, daß in der Richtung von Westen nach Osten solche Volksgemeinschaften ausgesandt wurden, welche unter der Leitung je eines Erzengels stan­den.",
        "Aber solche Erzengel waren die lenkenden geistigen Mächte dieser ausgesandten Stämme, die weniger oder mehr entwickelt waren, die, mit anderen Worten, weniger oder mehr nahe waren der Rangerhöhung zum Zeitgeiste."
      ],
      [
        "Diejenige Völkerströmung, deren Erzengel zu allererst emporgestiegen war zum Range eines Zeitgeistes, haben wir im fernen Osten zu suchen.",
        "Das war diejenige Völkerströmung, die sich zusam­menschloß mit der Urbevölkerung Indiens, die Völkerströmung, die das Herrenvolk in Indien bildete und die Grundlage abgab für die erste nachatlantische Kultur, nachdem der Erzengel dieser Volksgemein­schaft zum Zeitgeist, zum ersten Zeitgeist oder Arche der nachatlantischen"
      ],
      [
        "Kulturperiode erhoben worden war.",
        "Nun leitete dieser Zeitgeist die uralt-heilige Kultur Indiens und machte sie zur tonangebenden Kultur in der ersten nachatlantischen Periode.",
        "Die anderen Völker Asiens, die sich allmählich heranbildeten, waren lange bloß unter der Leitung von Erzengeln."
      ],
      [
        "Auch die Völker Europas, die zurückgeblieben waren bei der Her­überwanderung vom Westen nach Osten, waren noch lange unter der Leitung von Erzengeln, als sich der Erzengel Indiens schon erhoben hatte zum Range eines Arche, der intuierend auf die großen Lehrer Indiens, die heiligen Rishis wirkte, die dadurch, daß sie die Vermitte­lung dieses erhabenen bedeutenden Geistes bekamen, ihre hohe Mission in der schon geschilderten Weise vollbringen konnten.",
        "Lange wirkte dieser Zeitgeist, als das nordwärts von dem alten Indien vorgelagerte Volk noch unter der Leitung des Erzengels stand.",
        "Nachdem der Zeit­geist Indiens seine Mission erfüllt hatte, wurde er erhoben zu der Lei­tung der gesamten Evolution der nachatlantischen Menschheit."
      ],
      [
        "In der Zeit, die wir als die urpersische Zeit bezeichnen, haben wir dann den Geist der Persönlichkeit, den Zeitgeist, der der Intuitor des großen Zarathustra oder Zoroaster, des Zarathustra der Urzeit ist.",
        "Das ist wieder ein solches Beispiel, wie ein Erzengel, also eine Volksseele, sich erhebt zu dem Range eines Zeitgeistes.",
        "Das ist gerade das Schau­spiel, das wir, wie wir es am Anfange unserer heutigen Darstellung gesagt haben, in unserer Epoche erleben, daß die Erzengel sich durch die Mission, die sie verrichten, zu lenkenden und waltenden Zeitgei­stern emporarbeiten."
      ],
      [
        "Eine spätere Emporarbeitung ist dann diejenige, welche erfolgt aus dem ägyptischen Volke mit seinem Erzengel einerseits und dem chal­däischen Volke und seinem Erzengel andererseits.",
        "Da vollzieht sich das Ereignis, daß der Erzengel des ägyptischen Volkes aufsteigt zum Range eines führenden Zeitgeistes und sozusagen die Lenkung und Leitung dessen übernimmt, was früher dem chaldäischen Erzengel oblag, so daß der Führer in der chaldäisch-ägyptischen Periode der dritte führende, gewaltige Zeitgeist wird, der sich aus dem Range des ägyptischen Erz­engels allmählich heraufentwickelt hat.",
        "Das ist aber auch die Zeit, in der eine andere bedeutungsvolle Entwickelung sich vollzieht: die"
      ],
      [
        "Entwickelung, die parallel geht mit der ägyptisch-chaldäischen Kultur, und auf welche sich das bezieht, was wir im letzten Vortrag besonders hervorheben mußten."
      ],
      [
        "Wir haben gesehen, daß eine besondere Stelle, eine besondere Bedeu­tung alles dasjenige annimmt, was zu den semitischen Stämmen gehört, und daß innerhalb des Semitentums Jahve oder Jehova herausgehoben hatte gerade diese Rasse und sie zu seinem besonderen Volke erkoren hatte.",
        "Dadurch, daß er eine einzelne Rasse zu seinem besonderen Volke erkoren hatte, brauchte er, als diese Rasse nach und nach heranwuchs, zuerst zu seinem Stellvertreter gegenüber dem Volke eine Art von Erz­engel, so daß wir in dem heranwachsenden semitischen Volke, in den Urzeiten, einen unter der fortwährenden Inspiration des Jahve oder Jehova stehenden Erzengel haben, der dann später selber zu einem Zeitgeiste heranwächst."
      ],
      [
        "Wir haben daher, sozusagen außer den gewöhn­lichen, fortschreitenden Zeitgeistern im alten indischen, alten persi­schen, alten chaldäischen Volke noch einen Zeitgeist, der eine besondere Rolle für sich spielt, indem er innerhalb eines einzelnen Volkes wirkt.",
        "Wir haben da einen Zeitgeist, der also in gewisser Beziehung in der Mission eines Volksgeistes auftritt; wir haben einen Zeitgeist, den wir den semitischen Volksgeist nennen müssen."
      ],
      [
        "Er hatte eine ganz besondere Aufgabe.",
        "Dies wird Ihnen begreiflich erscheinen, wenn Sie ins Auge fassen, daß eigentlich gerade dieses Volkstum herausgehoben war aus der normalen Entwickelung und eine besondere Führung hatte, daß sozusagen besondere Einrichtungen getroffen worden sind, um dieses Volk zu führen."
      ],
      [
        "Durch diese besonderen Einrichtungen hatte dieses Volk eine Mission erhalten, die wirklich für die nachatlantische Zeit von ganz besonderer Wichtigkeit und Bedeutung war, die sich von der Mission aller anderen Völker und Volkstümer unterschied.",
        "Man kann diese Mission des Semitentums eigentlich dadurch am besten begreifen, daß man sie zusammenhält mit dem, was in der nachatlantischen Zeit die verschiedenen anderen Völker als diese oder jene Mission hatten."
      ],
      [
        "Es gibt zwei geistige Strömungen in der Menschheit.",
        "Die eine geistige Strömung muß man nennen, wenn man sie richtig bezeichnen will, die­jenige, die von dem Pluralismus, man könnte auch sagen, von der Mo­nadologie ausgeht, die also vorzugsweise in einer Vielheit von Wesenheiten"
      ],
      [
        "und Kräften den Ursprung und die Ouelle des Daseins sieht.",
        "Sie können nun überall in der Welt umherschauen, in irgendeiner Weise werden Sie sehen, daß die Völker der nachatlantischen Zeit von Viel­heiten des Göttlichen ausgegangen sind.",
        "Beginnen Sie bei der Dreiheit des alten Indertums, die sich später ausgelebt hat in Brahma, Shiva und Vishnu.",
        "Sehen Sie auf die deutsche Mythologie, so finden Sie die Drei­heit von Odin, Hönir und Lödur und so weiter.",
        "So werden Sie überall eine Dreiheit und diese in eine Vielheit gegliedert finden.",
        "Sie sehen diese Eigentümlichkeit aber nicht nur da, wo sozusagen Göttermythen und Götterlehren auftreten, sondern auch in den Philosophien, wo uns dieselbe als Monadologie entgegentritt.",
        "Das ist die eine Strömung, wel­che, weil sie von der Vielheit ausgeht, die größtmögliche Mannigfaltig­keit annehmen kann.",
        "Man könnte sagen: In der nachatlantischen Zeit, vom weitesten Osten in Indien und im weiten Bogen durch Asien hin­durch bis nach Europa, hat dieser Dienst der Vielheit, der sich im Grunde genommen in unserer geisteswissenschaftlichen Weltanschau­ung dadurch ausdrückt, daß wir eine Summe der verschiedensten Wesenheiten, der verschiedensten Hierarchien anerkennen, seine man­nigfaltigsten Vertretungen und Ausgestaltungen gewonnen."
      ],
      [
        "Diesem Dienste der Vielheit mußte eine synthetische, eine zusammen­fassende Bewegung gegenüberstehen, eine Bewegung, die streng ausging von dem Monon, dem Monismus.",
        "Die eigentlichen Inspiratoren, die Jmpulsgeber alles Monotheismus und Monismus, aller Einheitsgöttlich­keit sind die semitischen Völker.",
        "Bei ihnen liegt es in der Natur, und -wenn Sie sich erinnern an das, was heute morgen gesagt wurde - es liegt bei ihnen im Blut, den Einheitsgott, das Monon zu vertreten."
      ],
      [
        "Wenn der Mensch hinaussieht in das große Weltendasein, dann würde er aber nicht weit kommen, wenn er immer nur betonte: Eine Einheit, ein Monon liegt der Welt zugrunde.",
        "Der Monismus oder Mono­theismus allein genommen ist dasjenige, was nur ein letztes Ideal darstellen kann.",
        "Dies würde aber niemals zu einer wirklichen Welt-erfassung, zu einer durchgreifenden konkreten Weltanschauung führen können.",
        "Doch es mußte in der nachatlantischen Zeit auch die Strömung des Monotheismus ihre Vertretung finden, so daß einem Volke über-tragen war, das Ferment, den Impuls zu geben zu diesem Monotheismus."
      ],
      [
        "Diese Aufgabe war dem semitischen Volke übertragen.",
        "Daher sehen Sie, wie sozusagen mit einer gewissen abstrakten Strenge, einer abstrakten Unerbittlichkeit das monistische Prinzip gerade in diesem Volke vertreten wird, und alle anderen Völker haben insofern, als sie ihre verschiedenen göttlichen Wesenheiten in eine Einheit zusammen­fassen, den Impuls dazu bekommen von dieser Seite her.",
        "Der monisti­sche Impuls ist immer von dieser Seite gekommen.",
        "Die anderen Völker haben pluralistische Impulse."
      ],
      [
        "Es ist außerordentlich wichtig, daß man das ins Auge faßt.",
        "Derjenige, der sich mit dem Fortwirken der althebräischen Impulse befaßt, der sieht heute noch bei dem gelehrten Rabbiner, dem gelehrten Rabbinis­mus in seinem extremsten Element den Monotheismus walten.",
        "Daß das Weltenprinzip nur ein einheitliches sein kann, das als Impuls zu geben, ist die Aufgabe gerade dieses Volkes.",
        "Man könnte daher sagen: Alle anderen Nationen, Völker und Zeitgeister hatten eine analytische Auf­gabe, eine Aufgabe, das Weltenprinzip in verschiedene Wesenheiten gegliedert vorzustellen, wie zum Beispiel die äußerste Abstraktion des Monon in Indien bald in eine Dreigliedrigkeit zerfallen ist, wie der Einheitgott des Christentums zerfällt in die drei Personen.",
        "Die anderen Völker haben alle die Aufgabe, den Weltengrund zu analysieren und dadurch viel Inhalt zu schaffen für die einzelnen Teile dieses Welten-grundes, sich zu erfüllen mit reichem Vorstellungsmaterial, das die Erscheinungen liebevoll umfassen kann.",
        "Das semitische Volk hat die Aufgabe, abzusehen von aller Vielheit und synthetisch sich der Einheit hinzugeben, daher die Kraft der Spekulation, die Kraft des syntheti­schen Denkens, zum Beispiel in der Kabbalistik, gerade aus diesem Impuls heraus die denkbar größte ist."
      ],
      [
        "Was aus der Einheit durch das synthetische, das zusammenfassende Wirken des Ich jemals herausgesponnen werden konnte, ist im Laufe der Jahrtausende durch den semitischen Geist herausgesponnen worden.",
        "Das ist die große Polarität zwischen Pluralismus und Monismus, und das ist die Bedeutung des semitischen Impulses in der Welt.",
        "Monismus ist nicht ohne Pluralismus, und dieser nicht ohne jenen möglich.",
        "Daher mussen wir die Notwendigkeit beider wohl anerkennen."
      ],
      [
        "Die objektive Sprache der Tatsachen führt oft zu ganz anderen Erkenntnissen"
      ],
      [
        "als die Sympathien und Antipathien, die da oder dort wal­ten.",
        "Deshalb müssen wir die einzelnen Volksgeister wohl begreifen.",
        "Während die Führer der einzelnen Völker drüben in Asien und Afrika längst aufgestiegen waren zu dem Range von Zeitgeistern oder Geistern der Persönlichkeit und zum Teil sogar schon die Anwartschaft bekom­men hatten, sich umzuwandeln von Zeitgeistern in die nächsthöhere Stufe, zu Geistern der Form - wie zum Beispiel jener Zeitgeist, der im alten Jndien gewirkt hat, in gewisser Beziehung schon zum Range der Geister der Form emporgestiegen war -, waren die einzelnen Völker Europas noch lange geführt von ihren einzelnen Erzengeln."
      ],
      [
        "Erst in der vierten nachatlantischen Periode hob sich aus den verschiedenen Völ­kern Europas, die von ihren Erzengeln geleitet worden sind, der Erz­engel des Griechentums heraus zu einer führenden Stellung, indem er der tonangebende Zeitgeist der griechischen, der vierten leitenden Epo­che in der nachatlantischen Zeit wurde, so daß wir also den Erzengel des Griechentums emporsteigen sehen zu dem Range eines Arche, eines Geistes der Persönlichkeit.",
        "Dasjenige, wozu sich dieser Erzengel des Griechentums vorbereitet hatte, das tritt, als er Zeitgeist geworden war, für die Welt in Asien, Afrika und Europa hervor, deren Mittelpunkt eben das griechische Volk geworden war."
      ],
      [
        "Während sein Erzengel zum Arche sich entwickelt hatte, war der wirkende Zeitgeist des ägyptischen und auch der des persischen Volkes hinaufgestiegen zu einer Art von Geist der Form.",
        "Das, wozu wir jetzt kommen, ist etwas außeror­dentlich Interessantes im Verlaufe der nachatlantischen Entwickelung."
      ],
      [
        "Durch all die Entwickelung, welche der Erzengel des Griechentums früher durchgemacht hatte, konnte er in verhältnismäßig schneller Art dasjenige durchmachen, was ihn zu einer ganz besonderen führenden Stellung als Zeitgeist befähigte.",
        "Daher geschah aber etwas höchst Be­deutungsvolles in der vierten nachatlantischen Kulturperiode."
      ],
      [
        "Wir wissen, daß damals das Ereignis eintrat, welches wir als das Auf­nehmen des Christusimpulses von seiten der Menschheit bezeichnen.",
        "Der Christusimpuls wurde aufgenommen, das Mysterium von Golga­tha fand statt.",
        "Der Impuls, der da gegeben worden ist, sollte im Laufe der nächsten Jahrhunderte und Jahrtausende nach und nach seine Ver­breitung auf der Erde finden.",
        "Dazu bedurfte es nicht nur der Tatsache,"
      ],
      [
        "daß dieses Ereignis stattfand, dazu bedurfte es gewisser lenkender und führender Wesenheiten aus der Reihe der Hierarchien heraus.",
        "Und da trat nun das höchst Merkwürdige und Interessante ein, daß der Zeit­geist des Griechentums in einem bestimmten Zeitmomente, der ungefähr zusammenfällt mit dem Auf-die-Erde-Kommen des Christusimpulses, für diese unsere jetzige Periode auf den ihm dazumal möglich gewor­denen Aufstieg in die Region der Geister der Form verzichtete und der führende Zeitgeist wurde, der dann über die Zeiten hinaus wirkt."
      ],
      [
        "Er wird der stellvertretende, führende Geist des exoterischen Christen­tums, so daß sich also hinstellt vor den Christusimpuls der Arche, der führende Geist des Griechentums.",
        "Daher zerfällt das Griechentum so rasch in der Zeit, in welcher sich das Christentum entwickelt, weil es sozusagen seinen führenden Zeitgeist abgegeben hat, damit er Führer des exoterischen Christentums werden konnte."
      ],
      [
        "Es wurde der Zeitgeist des alten Griechentums der Missionar, der Inspirator oder vielmehr Intuitor des sich ausbreitenden exoterischen Christentums.",
        "Da haben wir also das Schauspiel einer solchen Resignation, von der wir gespro­chen haben, in einem konkreten Falle vor uns."
      ],
      [
        "Der Zeitgeist des Grie­chentums konnte, weil er seine Mission in der vierten nachatlantischen Kulturperiode so außerordentlich gut erfüllt hatte, aufsteigen in ein höheres Gebiet, verzichtete aber und wurde dadurch der führende Geist des sich ausbreitenden exoterischen Christentums, als welcher er über die verschiedenen Völker hinweg wirkte."
      ],
      [
        "Solch eine Verzichtleistung findet noch einmal statt, und diese zweite Verzichtleistung ist wiederum von einem ganz besonderen Interesse, gerade für diejenigen, die sich Schüler der Geist-Erkenntnis nennen.",
        "Wir haben im wesentlichen, während sich drüben in Asien, bis herein in das Agypter- und Griechentum, die einzelnen Erzengel zu Zeitgei­stern entwickeln, in Europa einzelne Völker und Volksstämme, die von ihren verschiedenen Erzengeln geleitet werden.",
        "Da haben wir in Eu­ropa, während sonst die entsprechenden Erzengel, die einst von Westen nach Osten geschickt worden sind, aufgestiegen waren in die Reihe der Zeitgeister, noch immer einen Erzengel, der in den germanischen und vor allem in den keltischen Völkern wirkte, in den Völkern, welche noch zur Zeit. in der das Christentum seinen Anfang nahm, in einem"
      ],
      [
        "großen Teile von Westeuropa, bis hinein in das heutige Ungarn, durch Süddeutschland und durch die Alpen hindurch, verbreitet waren.",
        "Diese Völker hatten als ihren Erzengel den keltischen Volksgeist.",
        "Auch weit herauf gegen den Nordosten Europas waren die Völker des keltischen Geistes verbreitet."
      ],
      [
        "Sie wurden von einem bedeutenden Erzengel gelenkt, der, bald nachdem der christliche Impuls der Menschheit gegeben wor­den war, darauf verzichtet hatte, ein Arche, ein Geist der Persönlichkeit zu werden, und der sich entschloß, auf der Stufe eines Erzengels stehen zu bleiben und sich in Zukunft den verschiedensten Zeitgeistern, die da zum Beispiel innerhalb Europas entstehen würden, unterzuordnen.",
        "Da­her auch schwanden die keltischen Völker als zusammengeschlossene Völkerschaft dahin, eben weil ihr Erzengel eine besondere Resigna­tion geübt und eine besondere Mission übernommen hatte."
      ],
      [
        "Das ist ein charakteristisches Beispiel dafür, wie, sagen wir, das Zurückbleiben in einem solchen Falle dazu beiträgt, besondere Missionen einzuleiten.",
        "Was wurde nun aus diesem Erzengel der keltischen Völker, als er dar­auf verzichtet hatte, ein Geist der Persönlichkeit zu werden?"
      ],
      [
        "Da wurde er der inspirierende Geist des esoterischen Christentums, und von seinen Inspirationen gehen insbesondere diejenigen Lehren und Impulse aus, die dem esoterischen Christentum, dem wahrhaften esoterischen Chri­stentum zugrunde liegen.",
        "Im Westen Europas war die geheimnisvolle Stätte zu finden für diejenigen, die in diese Geheimnisse eingeweiht wurden, wo die Inspiration stattfand durch diesen leitenden Geist, der ursprünglich eine bedeutsame Schulung als Erzengel des Keltentums absolviert hatte, der auf den Aufstieg verzichtet und eine andere Mis­sion übernommen hatte, die Mission: Inspirator des esoterischen Chri­stentums zu sein, das fortwirken sollte durch die Geheimnisse des heili­gen Gral, fortwirken sollte durch das Rosenkreuzertum."
      ],
      [
        "Da haben Sie das Beispiel einer Verzichtleistung, eines Zurückbleibens einer solchen Wesenheit der Hierarchien, und da haben Sie zugleich ein Beispiel, an dem Sie unmittelbar, im Konkreten erkennen können, was solch ein Zurückbleiben für eine Bedeutung hat.",
        "Trotzdem dieser Erzengel zu dem Range eines Arche hätte aufsteigen können, blieb er bei dem Range eines Erzengels und leitete dafür die bedeutsame Strömung des esoteri­schen Christentums, welche durch die verschiedensten Zeitgeister hindurch"
      ],
      [
        "fortwirken soll.",
        "Die Zeitgeister mögen so oder so wirken, dieses esoterische Christentum wird ein Ouell sein für alles, was sich unter dem Einflusse der verschiedenen Zeitgeister wieder wandeln, metamor­phosieren kann.",
        "Da haben wir also wieder ein Beispiel, wie eine solche Resignation stattfindet, während wir sonst das große Schauspiel erle­ben, daß die Volksgeister zu Zeitgeistern, gerade in unserer Epoche, aufsteigen."
      ],
      [
        "Nun haben wir - im europäischen Gebiet - die verschiedenen ger­manischen Völker.",
        "Diese verschiedenen germanischen Völker Europas, die ursprünglich von einem Erzengelwesen geleitet worden sind, waren dazu berufen, nach und nach unter die Leitung der verschiedensten Erzengel zu kommen, in der verschiedensten Weise Völker-Individua­litäten zu bilden."
      ],
      [
        "Es ist natürlich außerordentlich schwierig - schwierig nur aus dem Grunde, weil es in gewisser Beziehung leicht Leidenschaft und Eifersucht erwecken kann -, wenn über diese Dinge unbefangen gesprochen werden soll.",
        "Daher kann auf ganz bestimmte Mysterien dieser Entwickelung nur leise hingedeutet werden."
      ],
      [
        "Aus der Summe jener Erzengel ging hervor der Arche, der führende Zeitgeist unserer fünften Kulturepoche der nachatlantischen Zeit.",
        "Er ging hervor, nach­dem lange, lange Zeit einer der Erzengel der germanischen Völker eine gewisse Schulung durchgemacht hatte."
      ],
      [
        "Derjenige Zeitgeist, welcher der Volksgeist der griechisch-lateinischen Epoche war, wurde der Zeitgeist, der, wie Sie wissen, in der späteren Zeit damit beschäftigt war, das exo­terische Christentum auszubreiten.",
        "Die spätere römische Geschichte wurde auch geleitet von einer Art von Zeitgeist, der aus dem Erzengel des Römertums aufgestiegen war und sich in seiner Wirksamkeit mit dem christlichen Zeitgeist zu gemeinsamem Wirken verband."
      ],
      [
        "Diese beiden waren die Erzieher jenes Erzengels, welcher die germanischen Völker führte, der zu deren führenden Erzengeln gehörte, der sich dann zum Zeitgeiste der fünften nachatlantischen Kulturperiode emporhob.",
        "Es war vieles notwendig, vor allen Dingen aber, daß eine starke Indi­vidualisierung und Vermischung der verschiedenen Völkerelemente in Europa eintrat."
      ],
      [
        "Das war nur dadurch möglich, daß, während drüben in Asien und Afrika die Erzengel längst zu Zeitgeistern aufgerückt waren, in Europa die Führerschaft noch bei den Erzengeln selber lag,"
      ],
      [
        "daß die einzelnen Völkerschaften von ihren Volksseelen geleitet wur­den, unbekümmert um die Zeitgeister, ganz hingegeben den Impulsen der Volksgeister selber.",
        "Als der christliche Impuls über die Menschheit dahinging, da war in Europa ein Durcheinanderwirken von einzelnen von freiem Sinn erfüllten Volksgeistern, von denen ein jeder seine eige­nen Wege ging, und die es im Grunde genommen dadurch schwer mach­ten, daß ein die einzelnen Volksgeister führender Zeitgeist der fünften Kulturepoche entstehen konnte."
      ],
      [
        "Es vermischten sich, sagen wir, um jenes Volk möglich zu machen, welches das französische Gebiet bewohnt, romanische, keltische und fränkische Volkselemente.",
        "Durch diese Vermischung nahm natürlich die ganze Führung eine bestimmte Gestalt an."
      ],
      [
        "Sie ging sozusagen von den einzelnen, leitenden Erzengeln, welche andere Aufgaben erhalten hatten, auf andere über. - Beim lei­tenden Erzengel der Kelten haben wir gesagt, was er für eine Mission erhalten hatte.",
        "Ebenso könnten wir von den anderen Volkstümern die Mission der Erzengel angeben. - Daher kamen unter die Völker, die durch Mischung entstanden, wieder andere Erzengel, die ihre Herr­schaft antraten, als sich die verschiedenen Elemente vermischten."
      ],
      [
        "So war in der Tat durch lange Zeit hindurch - noch im Mittelalter - im mittleren und nördlichen Europa im Grunde genommen das führende Element bei den Erzengeln, die nur nach und nach beeinflußt wurden von dem gemeinsamen Zeitgeiste, der einherging vor dem Christusim­pulse.",
        "Es wurden die einzelnen Volksgeister in Europa vielfach die Diener des Christus-Zeitgeistes."
      ],
      [
        "Die Erzengel Europas stellten sich in den Dienst dieses gemeinsamen Christus-Zeitgeistes, während die einzelnen Völker kaum in der Lage waren, irgendeinen der Erzengel zu dem Range eines Zeitgeistes emporsteigen zu lassen.",
        "Erst im sechzehnten bis siebzehnten Jahrhundert - vom zwölften Jahrhundert etwa angefan­gen - bereitete sich das vor, daß der führende Zeitgeist der fünften nachatlantischen Periode herausgebildet wurde, unter dessen Einfluß wir heute noch stehen."
      ],
      [
        "Er gehört ebenso zu den großen, führenden Zeitgeistern wie die, welche die großen, führenden Zeitgeister waren während der ägyptisch-chaldäisch-babylonischen, urpersischen und indischen Epoche.",
        "Aber er wirkte in einer ganz eigentümlichen Weise, dieser Zeitgeist unserer fünften nachatlantischen Kulturepoche."
      ],
      [
        "mußte nämlich eine Art Kompromiß eingehen mit einem der alten Zeit­geister, die gewirkt haben vor dem christlichen Impulse, und zwar mit dem agyptischen Zeitgeiste, der, wie wir gehört haben, in gewisser Be­ziehung aufgestiegen ist zu dem Range eines Geistes der Form.",
        "So kommt es, daß eigentlich unsere fünfte nachatlantische Kulturperiode, in der wir stehen, von einem Zeitgeiste beherrscht ist, der in gewisser Weise sehr, sehr dem Einflusse und den Impulsen des Zeitgeistes der alten ägyptischen Kultur unterliegt und der ein sozusagen in seinen allerersten Anfängen begriffener Geist der Form ist."
      ],
      [
        "Das gab die vielen Zersplitterungen und Zerklüftungen unseres Zeit­alters.",
        "Ünser Zeitgeist in der fünften nachatlantischen Kulturperiode strebt dahin, sich in gewisser Beziehung zu spirituellen Höhen zu erhe­ben und die vierte nachatlantische Kulturzeit hinaufzubringen auf eine höhere Stufe.",
        "Aber es liegt darin dasjenige, was materialistische Neigung, materialistischer Hang ist, und je nachdem die verschiedenen Erzengelwesen, die verschiedenen Volksseelen eine mehr oder weniger große Hinneigung zu diesem materialistischen Hang haben, kommt unter der Führung dieses Zeitgeistes der fünften nachatlantischen Kul­turperiode ein mehr oder weniger materialistisches Volk heraus, das sozusagen dem Zeitgeiste mehr eine Nuance nach dem Materialistischen hin gibt.",
        "Ein idealistisches Volk dagegen ist ein solches, welches dem Zeitgeiste mehr eine Nuance nach dem Idealismus hin gibt."
      ],
      [
        "Nun bildete sich vom zwölften bis sechzehnten Jahrhundert tatsäch­lich immer mehr etwas heraus, was in gewisser Beziehung neben dem christlichen Zeitgeiste wirkte - der der fortwirkende griechische Zeit­geist ist -, so daß in der Tat, in merkwürdiger Weise, in unsere Kultur einströmt dasjenige, was wir den christlichen Zeitgeist nennen, verbun­den mit einem eigentlichen Zeitgeist der fünften nachatlantischen Kul­turperiode, und da wirkt wieder hinein das alte Ägyptertum, dessen Zeitgeist sich bis zu einem gewissen Rang der Geister der Form erhoben hat.",
        "Nun aber ist es gerade dadurch, daß ein solches Trifolium in unse­rer ganzen Zeitkultur wirkt, möglich geworden, daß in der fünften Zeitepoche die verschiedensten Nuancen von Kultur- und Volksseelen­Strömungen herauskamen.",
        "Es wurde möglich, daß der Zeitgeist die verschiedensten Farben und Nuancen in seinem Wirken aufwies."
      ],
      [
        "Erzengel, die ihre Befehle von dem Zeitgeist erhielten, wirkten in der verschiedensten Weise."
      ],
      [
        "Diejenigen, die im Norden wohnen, wird etwas interessieren, worauf wir in den nächsten Betrachtungen genauer werden einzugehen haben, sie wird insbesondere interessieren müssen die Frage: Wie wirkte jener Erzengel, der einstmals mit den nordischen Völkern, den skandinavi­schen Völkern heraufgeschickt worden ist in dieses Gebiet, und von dem aus die verschiedenen Erzengelwesen Europas - namentlich West-, Mittel- und Nordeuropas - die Inspirationen bekamen?",
        "In der außen­stehenden Welt kann es nur als Narretei gelten, wenn geradezu hinge­wiesen wird auf jenen Punkt des europäischen Kontinentes, von dem einst die größten Impulse nach allen Seiten ausgestrahlt sind, auf jenen Punkt, der der Sitz erhabener Geister war, bevor der keltische Volks­geist als keltisches Erzengelwesen in der Hochburg des Grals ein neues Zentrum errichtet hatte."
      ],
      [
        "Von jenem Punkte, der in alten Zeiten Zen­trum war für die Ausstrahlung der Geistigkeit Europas, ist auch ausge­strahlt dasjenige, was zunächst der nordische Volks-Erzengel als seine Mission erhalten hat.",
        "Für die Außenwelt muß es, wie gesagt, als Narre­tei erscheinen, wenn wir als den Punkt, von dem ausstrahlt, was nach den verschiedensten germanischen Volksstämmen hinwirkt, dasjenige Gebiet bezeichnen, das heute über Mittel-Deutschland liegt, aber eigentlich über der Erde gelegen ist."
      ],
      [
        "Wenn Sie etwa eine Kreislinie zögen, so daß in diese Kreislinie hineinfallen würden die Städte Det­mold und Paderborn, so kommen Sie in die Gegend, von der ausströmte die Mission der erhabensten Geister, welche nach Nord- und West-Europa ihre Mission ausdehnten.",
        "Weil dort das große Jnspirationszen­trum war, deshalb ging später die Sage, daß Asgard eigentlich an diesem Punkte der Erdoberfläche gelegen habe."
      ],
      [
        "Es lag aber da das große Inspi­rationszentrum in uralter Vergangenheit, das Zentrum, welches dann später seine Hauptwirksamkeit abgegeben hat an das Zentrum des heiligen Gral."
      ],
      [
        "Die Völker Skandinaviens mit ihren ersten Erzengeln, haben damals ganz verschiedene Anlagen mitbekommen, Anlagen, die sich heute eigentlich nur noch in der eigenartigen Konfiguration der nordischen Mythologie aussprechen.",
        "Derjenige, der im okkulten Sinne die nordische"
      ],
      [
        "Mythologie mit anderen Mythologien vergleicht, die über die Erde geherrscht haben, der mag wissen, daß diese nordische Mythologie die ursprüngliche Anlage des Erzengels darstellt, der hier herauf nach Norden geschickt worden ist, die ursprüngliche Anlage, die bei ihrer Gestaltung stehen geblieben ist, wie wir sie sozusagen bei einem Kinde sehen müßten, wenn bestimmte Talente, latentes Genie und so weiter auf der Kindheitstufe stehen blieben.",
        "Bei dem Erzengel, der nach Skan­dinavien geschickt wurde, haben wir diejenigen Anlagen, die dann in der eigentümlichen Konfiguration der nordischen Mythologie heraus­kommen."
      ],
      [
        "Daher rührt die große Bedeutung der nordischen Mythologie für das Verständnis des eigentlichen, inneren Wesens der skandinavi­schen Volksseele.",
        "Daher kommt auch die große Bedeutung, welche dieses Verständnis der Mythologie hat für die weitere Fortentwik­kelung dieses Erzengels, der allerdings die Anlage in sich hat, in einer gewissen Weise, aufzusteigen zu dem Range eines Arche Aber dazu ist mancherlei notwendig."
      ],
      [
        "Dazu ist notwendig, daß in ganz bestimmter Weise sich jene Anlagen entwickeln, die heute in gewisser Beziehung zurückgetreten sind hinter dem dämmernden, schattenhaf­ten Einfluß des Zeitgeistes, der sich vor die Impulse des Christentums hingestellt hat.",
        "So sonderbar ähnlich manche Dinge der germanisch-nordischen Mythologie den Darstellungen der griechischen Mythologie sind, so muß doch gesagt werden, daß es keine andere Mythologie der Erde gibt, welche in ihrem eigentümlichen Aufbau, in ihrer eigenartigen Durchführung ein bedeutsameres oder klareres Bild der Weltenevolu­tion gibt, als diese nordische Mythologie, so daß dieses Bild als eine Vorstufe des geisteswissenschaftlichen Bildes der Weltenentwickelung gelten kann."
      ],
      [
        "Die germanische Mythologie ist in der Art, wie sie ausgebildet wor­den ist aus der Anlage des Erzengels heraus, in ihren Bildern am bedeut­samsten ähnlich dem, was nach und nach als das geisteswissenschaft­liche Weltbild für die Menschheit erwachsen soll.",
        "Es wird sich darum handeln, wie jene Anlagen werden können, die einstmals ein Erzengel mitgebracht hat in die Welt, wie sie werden können, nachdem dieser Erzengel die Erziehung des Christus-Zeitgeistes genossen hat.",
        "Diese Anlagen werden zu einem wichtigen Gliede im führenden Zeitgeist"
      ],
      [
        "werden können, wenn in der richtigen Weise im späteren Alter der Volksentwickelung verstanden wird, dasjenige auszubilden, was diese Volksentwickelung als Anlage in einem früheren Zeitalter enthält.",
        "Damit haben wir nur hingedeutet auf ein wichtiges Problem, auf eine wichtige Evolution eines europäischen Erzengels; wir haben sozusagen darauf hingedeutet, inwiefern er eine Anlage zu einem Zeitgeiste hat."
      ],
      [
        "An diesem Punkte wollen wir einen Augenblick stehen bleiben und dann unsere Betrachtung so fortsetzen, daß wir versuchen, aus der Konfiguration der Volksseele heraus in eine esoterische Betrachtung der Mythologie einzutreten.",
        "Damit wird, als ein besonderes Kapitel, die Schilderung der ganzen interessanten Eigenart gerade der germa­nischen und namentlich auch der nordischen Mythologie vor unsere Seele geführt werden."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "ACHTER VORTRAG Kristiania, 14. Juni 1910",
    "paragraphs": [
      "Wenn man die Entwickelung der germanisch-nordischen Geschichte und die darin geschilderten geistigen Impulse studieren will, dann hat man nötig, den Grundcharakter der germanisch-nordischen Mytho­logie zunächst ins Auge zu fassen, und es ist schon das letzte Mal darauf aufmerksam gemacht worden, daß diese germanisch-nordische Mytho­logie, trotz manchem, worin sie Ähnlichkeit hat mit anderen Mytho­logien und Götterauffassungen, doch etwas ganz Eigentümliches ist. Dabei bleibt doch richtig, daß ein sehr weitgehender Grundkern mythologischer Auffassung sich über alle germanischen Völker und Stämme Europas hin erstreckt, so daß bis weit nach Süden hin eine ein­heitliche mythologische Auffassung, im Grunde genommen ein gleich­artiges Verständnis jener verwandtschaftlichen Beziehungen möglich ist.",
      "Gerade für das Eigenartige der germanisch-nordischen Mythologie muß durch alle Volksgebiete, in denen in der einen oder anderen Form diese Mythologie ausgebreitet war, einstmals ein gleiches Verständnis vorhanden gewesen sein; denn es unterscheidet sich das, was gemeinsam ist in der Mythologie der germanisch-nordischen Völker, ganz gewaltig schon von dem Wesenskern der griechischen Mythologie, ganz zu schweigen von der ägyptischen, so daß alles, was verwandt ist in der germanischen Mythologie, einander ganz nahe steht und weit entfernt ist von dem, was das Wesentliche in der griechischen und römischen Mythologie ist. Man kann aber dieses Wesentliche heute nicht sehr leicht verstehen, aus dem Grunde nicht, weil aus Erkenntnisvoraus-setzungen - über welche zu sprechen hier zu weit führen würde -heute eine gewisse Sehnsucht, ein gewisser Trieb herrscht, die Religionen der verschiedenen Völker einfach miteinander zu vergleichen.",
      "Verglei­chende Religionswissenschaft, vergleichende Mythologie, das ist etwas, wofür heute viel Enthusiasmus herrscht. Es ist dies ein Gebiet, auf dem es möglich ist, den allergrößten Unfug zu treiben. Was geschieht denn gewöhnlich, wenn man Mythologien und Religionen einzelner Völker miteinander vergleicht?",
      "Man vergleicht die Äußerlichkeiten, die in den",
      "Göttergeschichten vorliegen, sucht nachzuweisen, daß die eine Götter­gestalt in der einen Mythologie vorkommt und in ähnlicher Weise auch in der anderen und dergleichen mehr. Diese Religionsvergleichung ist für denjenigen, der den Tatbestand, der darin vorliegt, wirklich kennt, so ziemlich das Unbehaglichste in unserer gegenwärtigen Wissenschafts­richtung, deshalb, weil man eigentlich überall nur die Äußerlichkeiten vergleicht. Eine solche Religionsvergleichung macht auf den, der den Tatbestand kennt, ungefähr den Eindruck, wie wenn jemand sagte:",
      "«Vor dreißig Jahren lernte ich einen Menschen kennen. Der trug eine Uniform, die war so und so beschaffen. Der Mann hatte blaue Hosen, einen roten Rock und diese oder jene Kopfbedeckung und so weiter» und schnell dann fortfährt: «Dann habe ich vor 20 Jahren einen Men­schen kennen gelernt, der trug dieselbe Uniform und vor zehn Jahren wieder einen, der trug wieder dieselbe Uniform.» Wenn der Betreffende nun glauben würde, die Menschen, die er da kennen gelernt hat vor dreißig Jahren, zwanzig Jahren und zehn Jahren, weil sie gleiche Uni­form trugen, auch ihrer Wesenheit nach miteinander vergleichen zu können, so kann er sich sehr irren; denn es kann ein ganz anderer Mensch, in den verschiedenen Zeiten, in der Uniform drinstecken, und es kommt doch im wesentlichen darauf an, was für ein Mensch in der Uniform steckt.",
      "Das Gleichnis ist scheinbar weit hergeholt, und denn-noch kommt es bei der Religionsvergleichung auf dasselbe hinaus, wenn man den Adonis nimmt und ihn mit dem Christus vergleicht. Da ver­gleicht man nur die äußere Uniform.",
      "Kleidung und Eigenschaften der Wesen in den Sagen können sehr ähnlich oder gleich sein, aber es han­delt sich darum, was für geistig-göttliche Individualitäten darinnen sind, und wenn das ganz andere Individualitäten sind, die im Adonis und im Christus darinnen stecken, so hat eben diese Vergleichung nur den Wert einer Vergleichung der Uniform. Dennoch ist diese Verglei­chung heute ungemein beliebt.",
      "Es kommt also auf das vielfach durchaus gar nicht an, was heute die vergleichende Religionswissenschaft mit ihren ganz äußerlichen Methoden auf diesem Gebiete zutage fördern kann. Es kommt vielmehr darauf an, daß man kennen lernt, gewisser­maßen aus der Differentiation der Volksgeister heraus, die Art und Weise wie dieses oder jenes Volk, sei es zu seiner Mythologie, sei es zu",
      "seiner sonstigen Götterlehre, sei es selbst zu seiner Philosophie, gekom­men ist.",
      "Wir können daher den Grundcharakter der germanisch-nordischen Mythologie kaum anders verstehen, als wenn wir noch einmal einen Streifzug machen durch die aufeinanderfolgenden fünf Kulturperioden der nachatlantischen Zeit. Diese fünf Kulturperioden wurden dadurch hervorgerufen, daß von Westen nach Osten Wanderzüge stattgefunden haben, daß sozusagen die allerreifsten, fortgeschrittensten Menschen nach Absolvierung dieser Wanderzüge in das indische Gebiet vorrück­ten und dann die heilige uralt-indische Kultur begründeten. Weiter herauf, gegen unsere Zeit, wird die persische Kultur begründet, dann die ägyptisch-chaldäisch-babylonische Kultur, dann die griechisch-lateinische Kultur, auf die endlich die unserige folgt. Diese fünf Kul­turen sind in ihren Wesenskernen nur dadurch zu verstehen, daß man weiß, daß die Menschen, die an diesen Kulturen beteiligt sind, und auch die Engelwesen, die Volksseelen oder Erzengel und die Zeitgeister in den verflossenen Zeiten selber alle durchaus voneinander verschieden waren. Heute wollen wir mehr Rücksicht darauf nehmen, wie die Men­schen verschieden waren, die an diesen Kulturen teilgenommen haben.",
      "Grundverschieden waren die Menschen, die im alten Indien die uralt-indische Kultur begründeten, die dann ihre literarische Einklei­dung in den Veden und in der späteren indischen Literatur gefunden hat, grundverschieden zum Beispiel von den griechisch-lateinischen Völkern, verschieden schon von den persischen, verschieden von den ägyptisch-chaldäischen und am meisten verschieden von den Völkern, welche in Europa vorbereitend heranwachsen zur fünften Kultur-periode der nachatlantischen Zeit. Inwiefern waren sie aber verschie­den? Es war die ganze Menschheitsanlage der uralt-indischen Völker absolut verschieden von den Menschen aller weiter nach Westen gele­genen Volksgebiete. Wenn wir uns eine Vorstellung davon bilden wollen, welche Verschiedenheit da bestand, so müssen wir uns sagen:",
      "Es waren die Völker des alten Indien sehr weit in der menschlichen Entwickelung fortgeschritten, bevor sie aufnahmen das Ich. Sie hatten in bezug auf alles übrige in der Menschheitsentwickelung große, unge­heuer große Fortschritte gemacht, sie hatten hinter sich eine lange,",
      "lange Menschheitsentwickelung. Das hatten sie aber durchgemacht gewissermaßen in einer Art von Dumpfheit. Dann trat das «Ich» ein, das Bewußtsein des Ich. Das trat in verhältnismäßig später Zeit beim indischen Volke ein; zu einer Zeit, als das indische Volk in gewissem Grade schon sehr reif war, als es schon durchgemacht hatte, was die germanisch-nordischen Völker noch durchmachen mußten, während sie schon ihr Ich besaßen. - Fassen Sie das wohl ins Auge! Die germa­nisch-nordischen Völker mußten mit ihrem vollentwickelten Ich bei dem dabei sein, was die Bewohner des uralten Indiens in einer gewissen Dumpfheit, also ohne mit ihrem Ich dabei zu sein, durchgemacht hatten.",
      "Was ist es denn nun, was man in der nachatlantischen Zeit als Menschheitsentwickelung durchmachen konnte? Wenn man in der alten atlantischen Zeit als Mensch lebte, so war man als solcher Mensch noch mit einem höheren Grade alten, dumpfen Hellsehens behaftet.",
      "Man sah durch altes, dumpfes Hellsehen in die göttlich-geistige Welt hinein, man sah die Vorgänge, die sich in dieser Welt abspielen. Ver­setzen Sie sich nun eine Weile hinüber in das alte atlantische Land, bevor die Züge nach Osten gehen.",
      "Die Luft war noch durchsetzt mit Wasser- und Nebeldämpfen. Aber auch die Seele der Menschen war anders. Der Mensch unterschied noch nicht einmal die verschiedenen äußeren Sinneswahrnehmungen von einander.",
      "Es war damals so, daß er wie ein geistiges Aroma, wie eine geistige Aura den geistigen Gehalt der Welt um sich ausgebreitet fand. Ein gewisses Hellsehen war also da vorhanden, und aus diesem Hellsehen mußte man herauskommen.",
      "Dies geschah durch die Wirkung der Kräfte, in deren Bereich die Menschen kamen bei den Wanderzügen von Westen nach Osten. Bei diesen Wan­derzügen wurden wieder die verschiedensten Seelenentwickelungen durchgemacht.",
      "Da gab es Völker, welche, indem sie hinüberwanderten nach dem Osten, zuerst wie verschliefen das Heraustreten aus dem alten Hellsehen und schon auf einer höheren Stufe der Entwickelung waren, als ihr Ich noch immer in Dumpfheit sich befand. Sie machten verschiedene Stufen der Entwickelung durch, und ihr Ich war noch immer ein dumpfes, ein träumerisches.",
      "Am weitesten waren die Inder entwickelt, als ihr Ich mit vollem Selbstbewußtsein erwachte. Da waren sie schon so, daß sie ein sehr reiches inneres Seelenleben hatten, das gar",
      "nicht mehr diejenigen Zustände besonders in sich zeigte, welche die Völker Europas noch lange erlebten. Diese hatten sie schon durchge­macht. Sie erwachten zum Selbstbewußtsein, als sie bereits mit geistigen Kräften und geistigen Fähigkeiten ausgestattet waren, durch die sie in hohem Grade hineindringen konnten in die geistigen Welten.",
      "Daher war den Fortgeschrittenen der indischen Bevölkerung bei ihrem Sich­herausarbeiten aus ihren alten dämmerhaften Hellseherzuständen all das Treiben und Tätigsein der verschiedenen Engel- und Erzengelwesen an den menschlichen Seelen im Grunde genommen höchst gleichgültig geworden. Die Arbeit der Erzengel und Engel und derjenigen geistigen Wesenheiten überhaupt, die besonders im Volksgeiste arbeiteten, hatten sie nicht mehr unmittelbar beobachtet.",
      "Das war an ihrer Seele, an ihrem Astral- und Ätherleib geleistet worden, als sie sozusagen noch gar nicht dabei waren. Sie erwachten, als ihre Seele mit einem ungeheueren Reife-grade bereits behaftet war; sie erwachten so, daß die Fortgeschritten­sten dasjenige, was früher mit der Menschheitsentwickelung geschehen war, durch eine leichte Entwickelung bereits in der Akasha-Chronik wieder lesen konnten, so daß sie hinausblickten in die Umgebung, in die Welt und daß sie dadurch in der Akasha-Chronik lesen konnten, was in der geistigen Welt vorging, was sie durchgemacht hatten in dump­fem, dämmerhaftem Bewußtseinszustande.",
      "Sie waren unbewußt in höhere Gebiete geleitet, sie hatten, bevor ihr Ichbewußtsein erwacht war, geistige Fähigkeiten erlangt, die viel reicher waren als die Seelen-fähigkeiten der westlichen Völker. So war die geistige Welt für diese Menschen eine unmittelbare Beobachtung.",
      "Die Fortgeschrittensten der indischen Volksführung waren so weit, daß sie, als ihr Ich erwachte, tatsächlich nicht einmal mehr darauf angewiesen waren, zu beobachten, wie sozusagen die menschliche Entwickelung heraussprudelte aus den Geistern der Form oder Gewalten, sondern es war ihnen dasjenige ver­trauter, was wir Geister der Bewegung, Mächte nennen und dasjenige, was über diesen ist, die Geister der Weisheit. Das interessierte sie ganz besonders.",
      "Diejenigen geistigen Wesenheiten, die darunter stehen, wa­ren dagegen solche Wesenheiten, in deren Bereich sie schon früher gewesen, die ihnen daher nicht mehr von so ganz besonderer Wichtig­keit waren. So sahen sie auf zu dem, was sie später nannten die Summe",
      "aller Geister der Bewegung und aller Geister der Weisheit; zu dem, was man später mit den griechischen Ausdrücken Dynameis und Kyrio­tetes bezeichnete. Zu diesen sahen sie auf und sagten zu ihnen: Mula­Prakriti, das ist die Summe der Geister der Bewegung, und Maha-Puru­sha, die gesamte Summe der Geister der Weisheit, was wie in einer geistigen Einheit lebt. Solche Anschauungen konnten sie gewinnen, weil die Angehörigen dieses Volkes in so späten Zuständen der Entwicke­lung zu ihrem Ich erwachten. Sie hatten schon abgemacht, was die späteren Völker mit ihrem Ich noch mit anschauen mußten.",
      "Weniger weit entwickelt waren die Völker der persischen Kultur. Sie waren so weit durch ihr eigenartiges Erkenntnisvermögen und durch das Erwachen ihres Ich auf einer niedrigeren Stufe, daß sie sich be­schäftigen konnten mit den Wesenheiten der Gewalten oder Geister der Form. Mit diesen wurden sie ganz besonders vertraut. Diese durch-schauten sie in gewisser Weise, und sie interessierten sich auch vorzugs­weise für sie. Eine Stufe tiefer als die Inder, aber doch auf einer Stufe, auf die dann wieder die Völker des Westens sich heraufarbeiten mußten, erwachten die Völker der persischen Gemeinschaften. Daher wurden sie mit den Gewalten oder Geistern der Form bekannt, die sie unter dem Begriffe der «Amshaspands» zusammenfaßten. Das sind die Ausstrahlungen, die wir als die Geister der Form oder Gewalten kennen und die, von ihrem Gesichtspunkte aus, gerade die Völker der persi­schen Kultur besonders gut beobachten konnten.",
      "Dann kommen wir zu den chaldäischen Völkern. Die hatten schon ein Bewußtsein von dem, was wir als Urkräfte, als führende Zeitgeister kennen. Sie hatten ein Bewußtsein von den Wesenheiten, die als Ur­kräfte, als Geister der Persönlichkeit erfaßt werden sollen. In einer anderen Weise hatten wiederum die Völker der griechisch-lateinischen Zeit gerade auch von diesen Urkräften oder Geistern der Persönlich­keit ein gewisses Bewußtsein. Aber bei ihnen war noch etwas ganz anderes vorhanden, und das war das, was uns ein Stück weiter in der Erkenntnis führen könnte. Die Griechen standen den germanischen Völkern noch näher. Aber doch erwachte dort das Ich auf einer höhe­ren Stufe als bei den germanisch-nordischen Völkern. Das, was bei den nordischen Völkern noch als Arbeit der Engel und Erzengel durchlebt",
      "wurde, das durchlebten die griechisch-lateinischen Völker nicht mehr unmittelbar. Sie hatten aber noch eine deutliche Erinnerung daran. Denken Sie sich also, daß der Unterschied zwischen den germanischen und den griechisch-lateinischen Völkern der ist, daß die griechisch-lateinischen Völker noch eine Erinnerung daran hatten, wie die Engel und Erzengel an ihrem Seelenleben, das sie in sich entwickelt hatten, teilgenommen haben.",
      "Sie hatten dies im Grunde genommen aber nicht allzu deutlich durchgemacht. Sie waren dabei noch in einem dumpfen Bewußtseinszustande. Doch in der Erinnerung trat es ihnen nun ganz besonders vor die Seele.",
      "Die Schöpfung dieser ganzen Welt, die Art und Weise, wie die Engel und Erzengel - die abnormen und die nor­malen - in die menschliche Seele hereinwirken, das kannten die Grie­chen. Was sie durchgemacht hatten, das hatten sie in einem gewaltigen Erinnerungsbilde in ihrer Seele.",
      "Erinnerung ist das, was abgeklärter ist, festere Konturen hat als das, was man erlebt. Es ist nicht mehr so frisch und nicht mehr so jung, aber es hat schärfere Umrisse, schärfere Kon­turen, was als Gedächtnis, als Erinnerung auftritt.",
      "Der Einfluß oder Impuls der Engel- und Erzengelwelt auf die Menschenseele wurde bei den Griechen aus der Erinnerung in festen, scharfen Konturen wach­gerufen. Das ist die griechische Mythologie. Wer sie nicht so ansieht, sondern nur die Namen vergleicht mit Namen, die anderswo auftreten, also nicht die besonderen Kräfte ins Auge faßt, nicht die Gestalten auffaßt, die auftreten als Apollo, Minerva und so weiter, der treibt äußere Religionsvergleichung, vergleicht bloß die Uniformen.",
      "Die Art und Weise, wie damals angeschaut wurde, ist es, worauf es ankommt.",
      "Nachdem wir dies gesehen haben, werden wir zugeben: Die Griechen formten sich ihre Mythologie heraus aus der Erinnerung. - Die ägyp­tisch-chaldäische Zeit hatte nur eine dunkle, dumpfe Erinnerung an das Wirken der Engel- und Erzengelwelt, aber einen Ausblick in die Welt der Urkräfte. Es ist bei ihr so, wie wenn sie anfinge, etwas zu vergessen. In der persischen Mythologie oder Götterlehre haben wir dafür ein vollständiges Vergessen der Engel- und Erzengelwelt, aber zugleich einen Ausblick in die Welt der Gewalten oder Geister der Form. Das, was in der griechischen Mythologie liegt, haben die persischen Völker und erst recht die indischen vergessen. Sie schauten die ganzen Vorgänge",
      "bereits wieder aus der Akasha-Chronik an und schufen sich die Bilder der früheren Vorgänge aus ihrer Erkenntnis heraus, die aber schon vergöttlichte Erkenntnis mit höher entwickelten Geisteskräften war. Daraus werden Sie aber auch erkennen, daß es gerade jenen Völ­kern des Ostens ungemein schwer wird, das abendländische Geistes­leben zu verstehen. Daher kommt dann jene Zugeknöpftheit der Völker des Ostens gegenüber dem abendländischen Geistesleben. Sie werden gewiß die materielle abendländische Kultur annehmen; aber die geistige Kultur des Abendlandes bleibt ihnen, wenn sie nicht auf dem Umwege der Geisteswissenschaft dazu kommen, mehr oder weniger verschlossen. Sie standen auf einer menschlich hohen Stufe zu der Zeit schon, als auf der Erde noch kein Christus Jesus war. Der kam erst in der vierten nachatlantischen Kulturepoche. Das ist ein Ereignis, das man nicht mehr auffassen konnte mit den Kräften, welche sich aus dem indischen Volkstum heraus entwickelt hatten. Dazu brauchte man noch Kräfte, die verwandt waren mit einem weniger hohen Stand des Ich, mit einem Darinstehen des Ich in untergeordneten Seelenkräften.",
      "In den germanisch-nordischen Gebieten war das Hereinarbeiten der Angeloi und Archangeloi in die Menschenseele nicht etwa bloß als Erinnerung vorhanden, sondern so, daß die Menschen, selbst noch zur Zeit als der Christus Jesus auf der Erde wandelte, das noch sehen konn­ten, daß sie noch darin standen, daß sie die Angelegenheiten der Engel-und Erzengelwesen, wie sie noch in ihrer Seele arbeiteten, mitmachten. Die griechisch-lateinischen Völker erinnerten sich bei diesen Seelen-Erlebnissen an etwas, was sie früher einmal durchgemacht hatten. Die germanischen Völker lebten darin als in ihren eigenen, unmittelbaren Angelegenheiten. Ihr Ich war erwacht auf der Stufe des Daseins, wo noch hereinarbeiteten in die Seele die Volksgeister und diejenigen gei­stigen Wesenheiten, die selbst noch unter den Volksgeistern stehen. Daher standen diese Völker am allernächsten dem, was wir die Vor­gänge in der alten Atlantis drüben kennen.",
      "In der alten Atlantis sah man auf zu den geistigen Mächten und sprach von einer Art von Einheitsgottheit, weil man eben hinaufsah in unmittelbarer Wahrnehmung in alte, urferne Entwickelungszustände der Menschheit. Man sah damals gleichsam noch das Walten der Geister",
      "der Weisheit und das Walten der Geister der Bewegung, das die spä­teren Inder wieder aus der Akasha-Chronik heraus beobachteten. Um eine Stufe hatten sich diese Völker des Westens über diesen Standpunkt hinauserhoben, so daß sie in unmittelbarer Gegenwart das Herausdrän­gen aus der alten Anschauung in die neue hinein erlebten.",
      "Sie sahen in ein Weben und Leben von wirklichen geistigen Mächten zu einer Zeit, als das Ich noch nicht erwacht war. Aber sie sahen zugleich, wie das Ich nach und nach erwachte, und wie Engeiwesen und Erzengel-wesen in die Seele eingriffen.",
      "Diesen unmittelbaren Übergang nahmen sie wahr. Sie hatten eine Erinnerung an ein früheres Weben und Leben, als die Anschauung noch so war, daß man gleichsam alles wie in einem Nebelmeer sah, und sie schauten, wie dann aus diesem Nebelmeer für sie das herauskam, was wir als die göttlich-geistigen Gestalten, die unmittelbar über dem Menschen stehen, kennen gelernt haben.",
      "Die alten Götter aber, die gewirkt haben, bevor in das menschliche Seelen-leben die Götter eingriffen, die man jetzt sah, mit denen man sich ver­bunden fühlte, diese göttlichen Wesenheiten, die in ferner, ferner Ver­gangenheit, in der Zeit der alten Atlantis, wirksam waren, nannte man die Wanen. Herausgetreten aus der alten atlantischen Zeit sind dann die Menschen und sahen auf das Weben der Engel und Erzengel; die nannte man die Asen.",
      "Das waren diejenigen Wesen, die sich als Engel und Erzengel kümmerten um das Ich der Menschen, das jetzt auf der untersten Stufe erwachte. Vorgesetzt waren sie jenen Völkern. Das, was die anderen Völker des Ostens verschlafen haben, nämlich zu sehen, wie die Seele sich hinaufarbeitet durch die verschiedenen Kräfte, die von den normalen und abnormen Engel- und Erzengelwesen verliehen werden, das mußten die Völker Europas von unten auf beginnend durchmachen; sie mußten ganz dabei sein, damit sich diese Seelenkräfte nach und nach entwickelten.",
      "So waren also die Göttergestalten, welche sich sozusagen vor die Seele des germanisch-nordischen Menschen stellten, die Göttergestal­ten, die unmittelbar an seiner Seele arbeiteten und dasjenige, was er selbst als das Sichherausringen des Menschlich-Seelischen aus dem Kos­mischen beobachtete, unmittelbare Anschauungen; das war etwas, was er unmittelbar erlebte. Er schaute nicht zurück in der Erinnerung auf",
      "die Art und Weise, wie die Seelen sich in die Leiber hineingebildet haben, er sieht vielmehr als gegenwärtig, was da gschieht. Es ist seine eigene Entwickelung, und er ist mit seinem Ich dabei. Er hat Verständ­nis dafür bis ins achte, neunte, zehnte Jahrhundert nach Christus.",
      "Er hat sich ein Verständnis dafür bewahrt, wie die Seelenkräfte nach und nach sich bilden, sich hineinkristallisieren in den Leib. Zuerst schaut er auf die Erzengelwesen, welche in seiner Seele arbeiteten, indem sie ihm das gaben, was seine Seelenkräfte werden sollten, und da findet er als den hervorragendsten dieser Erzengel Wotan oder Odin und sieht ihn an seiner Seele arbeiten, sieht, wie er in seine Seele hineinarbeitet.",
      "Was sieht er da? Wie nimmt er Wotan oder Odin wahr? Als was erkennt er ihn, und als was lernt er ihn lieben und, vor allen Dingen, als was ver­stehen? Er lernt ihn erkennen als einen derjenigen Erzengel, die dazu gekommen sind, einmal Verzicht zu leisten auf den Aufstieg zu höheren Stufen.",
      "Er lernt Odin als einen der abnormen Erzengel kennen, als einen der großen Verzichter der Vorzeit, die das Erzengeltum über­nommen hatten, als sie die wichtige Mission auf sich nahmen, in die Seele des Menschen hineinzuarbeiten. Den Odin in seiner Tätigkeit erlebt der germanisch-nordische Mensch noch in der Zeit, in der er an das Werk herangeht, der Seele die Sprache einzuimpfen.",
      "In wunder-barer Weise hat sich erhalten, wie Odin selbst an seinen Völkern arbei­tet, um ihnen die Sprache möglich zu machen. Das wird geschildert als eine Götter-Einweihung. Wie Odin dazu kam, sich die Macht zu ver­schaffen, den Seelen der germanisch-nordischen Völker die Sprache zu verleihen, das wird dadurch geschildert, daß Odin, bevor er diese Fä­higkeit erlangt hatte, dasjenige durchmacht, was uns als die Einweihung durch den Göttertrank dargestellt wird, den Göttertrank, der einstmals",
      "- in urferner Vergangenheit bei den Riesen war. Dieser Trank enthielt nicht bloß eine abstrakte Weisheit, sondern stellt uns die unmittelbar im Laut sich auslebende Weisheit dar. Über die im Laute sich ausle­bende Weisheit erringt Odin bei seiner Einweihung die Macht; er lernt sie handhaben, als er eine lange Einweihung, eine Einweihung von neun Tagen durchmacht, aus der er dann durch Mimir, den alten Träger der Weisheit, erlöst wird. So wird Odin der Herr der Sprachgewalt. Daher führt die spätere Sage die Sprache der Dichter, die Sprache der Skalden",
      "auf Odin zurück. Auf Odin wird auch zurückgeführt die Runenkunde, die in alten Zeiten mit der Sprache viel näher verwandt gedacht wurde als das spätere Schrifttum. Wie also die Seele auf dem Umwege durch den Ätherleib und hineinlebend in den physischen Leib durch den ent­sprechenden Erzengel die Sprache erwirbt, das drückt sich aus in den wunderbaren Geschichten, die über Odin erzählt werden.",
      "Ähnliche Erzengelwesen haben wir in den Genossen des Odin vor uns, in Hönir, welcher die Kraft des Vorstellens verleiht und in Lodur, welcher dasjenige verleiht, was der Rasse noch am nächsten liegt, also Hautfarbe und Blutcharakter. In diesen zwei Wesen haben wir also Erzengelwesen zu sehen, die sozusagen mehr nach der normalen Seite hin liegen. Die abnormen haben wir dann in den Wesen zu erkennen, die als Wili und We auftreten. Das sind Wesenheiten, die mehr noch im Innern, im Intimen der Seele wirken, wie ich es im vergangenen Vor-trage klargelegt habe. Aber innig verwandt fühlt sich gerade mit einem abnormen Erzengel ein solches Ich, das selbst auf einer abnormen Ent­wickelungsstufe steht, wo es schon bei der Heranbildung der unter­geordneten Seelenkräfte dabei ist. Ein solches Ich fühlt sich verwandt mit einem abnorm entwickelten Erzengelwesen Daher wird auch Odin nicht als abnormer Erzengel empfunden, vielmehr als solcher, der in seinem Zurückbleiben verwandt ist mit dem Zurückbleiben der west-ländischen Seelen, die in mehr bewußter Weise das in ihrem Ich erleben, was beim Durchgang durch jene Gebiete zurückgeblieben ist, wogegen die östlichen Seelen an gewissen Stadien des Seelenlebens vor-übergingen, bis sie sich entschlossen, zu erwachen. Daher lebt vor allen Dingen in der Seele der germanisch-nordischen Menschen alles das­jenige, was mit diesen in den elementaren Tiefen des Seelenlebens wüh­lenden und arbeitenden Erzengelkräften des Odin verbunden ist.",
      "Wenn wir gesagt haben, daß die Engel es sind, welche dasjenige, was die Erzengel bewirken, in die einzelnen Menschen heruntertragen, so hat ein Ich, das auf einer so frühen Elementarstufe des Seelenlebens erwacht, vor allen Dingen ein Interesse daran, daß in jenes Ich gleich­sam die Angelegenheiten der Erzengel hineingetragen werden. Daher hat der germanisch-nordische Mensch ein Interesse an einer solchen Engelgestalt, welche von besonderer Macht ist, aber zu gleicher Zeit",
      "innig verwandt ist mit dem einzelnen Menschen und seiner Individua­lität. Das ist Thor. Thor wird nur dadurch erkannt, daß man weiß, daß in ihm gesehen werden muß eine Wesenheit, die zwar sehr vorgerückt sein könnte, wenn sie normal sich weiter entwickelt hätte, die aber verhältnismäßig früh verzichtet hat und auf der Stufe der Engel zu­rückgeblieben ist, damit sie in der Zeit, da das Ich in der Seelenentwik­kelung erwachte, Führer in der Seelenwelt der germanisch-nordischen Gebiete sein konnte. Daß dasjenige, was aus der geistigen Welt in jedes einzelne Ich hineingetragen werden sollte, auch hineingetragen werden konnte, das ist es, was in Thor als verwandt mit dem einzelnen mensch­lichen Ich so unmittelbar empfunden wird. Wenn wir dies ins Auge fassen, dann werden wir das, was an Einzelheiten überliefert ist, auch besser verstehen. Bei uns handelt es sich ja darum, diese Götterindivi­dualitäten in entsprechender Weise verstehen zu können. Nun aber hat der germanisch-nordische Mensch empfunden, miterlebt dieses Ein­prägen der Seele in die Leiblichkeit. Er war dabei, als das Ich sich in die Leiblichkeit hineingliederte und von jedem einzelnen Menschen Besitz ergriff.",
      "Nun wissen wir, daß das Ich im Blute des physischen Leibes pulsiert, und es entspricht jedem Inneren ein Äußeres, jedem Mikrokosmischen ein Makrokosmisches. Der Arbeit des Sprachen- und Runenweisheit gebenden Odin, der auf einem weiten Umweg durch das Atmen wirkte, entspricht draußen im Makrokosmos die Windesbewegung. Dem regel­mäßigen Eindringen der Luft durch unsere Atmungsorgane, welche die Umformung der Luft zu dem Wort, der Sprache bewirken, dem ent­sprechen draußen im Makrokosmos die Bewegungen, die Strömungen im Winde. Ebenso wahr, wie wir das Walten des Odin in der Umgestal­tung der Luft zu den Worten in uns selber empfinden, ebenso wahr müssen wir ihn draußen im Winde walten und wirken sehen. Das aber hat derjenige, der noch die alten germanisch-nordischen Fähigkeiten besaß, zu denen besonders ein gewisser Grad von Hellsichtigkeit ge­hörte, wirklich gesehen. Der hat überall Odin im Weltenwind walten gesehen, hat ihn gesehen, wie er durch seinen Atem die Sprache formte. Das sah der nordische Mensch als eine Einheit. So wie das, was in uns lebt und die Sprache organisiert - das heißt so, wie bei der nordischen",
      "Organisation die Sprache war -, hindurchdringt in das Ich und die Pulsation des Blutes bewirkt, so entspricht dem, was sich da als Sprache hineinorganisiert, draußen im Makrokosmos der Blitz und der Donner. Die Sprache ist eher da, als das Ich geboren ist.",
      "Daher wird das Ich überall als der Sohn derjenigen Wesenheit empfunden, welche die Sprache gibt. An der Einprägung in das einzelne Ich ist insbesondere Thor beteiligt, und was dem Vorgange im Makrokosmos entspricht, ist im Mikrokosmos die Pulsation des Blutes.",
      "Was also draußen im Makro-kosmos der Pulsation des Blutes im Menschen entspricht, das ist das­jenige, was als Blitz und Donner durch die wehenden Winde und webenden Wolken geht. Das aber sieht wiederum der germanisch-nor­dische Mensch in seinem Hellsehen als eine Einheit, und er sieht das Wehen des Windes, das Zucken des Blitzes draußen in innigem Zusam­menhang mit dem Weben der von ihm eingeatmeten Luft.",
      "Er sieht, wie sie ins Blut übergeht und da das Ich pulsieren macht. Das wird heute als ein materieller Vorgang angesehen, war aber noch ein astralischer Vorgang bei den germanisch-nordischen Menschen. Der sah die innige Verwandtschaft des Feuers, des Blitzes mit dem, was durch das Blut geht.",
      "Er fühlte den Pulsschlag in seinem Blute und wußte: Das ist der Schlag des Ich; wußte: Das, was da schlägt, spüre ich und spüre ich nach einiger Zeit wieder. Aber den äußeren, materiellen Vorgang be­achtete er nicht.",
      "Das alles war in hellseherische Empfindung gekleidet. Er empfand das, was den Pulsschlag bewirkt und ihn immer wieder an dieselbe Stelle zurückgehen läßt, als Thors Tat. Als das Immer-wieder­Zurückkehren des Hammers des Thor in die Hand des Thor fühlte er in seinem Ich die Thor-Kraft, die Kraft eines der mächtigsten Engel, die überhaupt jemals verehrt worden sind, weil er eine mächtige Wesen­heit war, die angesehen wurde als stehengeblieben auf der Stufe des Engeltums.",
      "Wie die geistige Kraft den physischen Leib zusammenhält, das drückt sich in der germanisch-nordischen Mythologie dadurch aus, daß das Ich dasjenige ist, was bei dem Gesponnenwerden des seelisch-leiblichen Wesens dieses zusammenhält. Von innen heraus sieht der germanisch-nordische Mensch das Weben des leiblich-seelischen Menschen, und er hat in späterer Zeit noch Verständnis dafür, wie aus dem Astralischen",
      "sich sein Inneres hineingliedert, wie sozusagen das Innere dem Äußeren antwortet. Er hatte noch Verständnis dafür, wenn ihm von Eingeweih­ten gesagt wurde, wie die Welt zum Menschen sich formt. Da hatte er Verständnis dafür, zurückzugehen zu den früheren Stadien, zu dem, was ihm erzählt worden ist von den Geschehnissen, die das Verhältnis der Engel und Erzengel darstellen, zu den früheren Stadien, wo der Mensch aus dem Makrokosmos in physisch-geistiger Art herausgeboren worden ist.",
      "Er vermochte zu sehen, wie aus dem Makrokosmos der ein­zelne Mensch herausgebaut wird, wie er im Makrokosmos ruht. Er suchte sich im Makrokosmos diejenigen Vorgänge auf, die sich mikro­kosmisch so abspielen, daß von dem menschlichen Norden aus, aus dem kühlen Geistgebiet, die menschlichen Gedanken gewoben werden, und daß von dort aus die menschliche Leiblichkeit mit den zwölf Gehirn-nerven des Kopfes versorgt wird.",
      "Diesen Vorgang, der mikrokosmisch zu den zwölf Gehirnnerven geworden ist, sieht er. Er sieht den weben-den Geist in dem, was er «Nebelheim» oder «Niflheim» nennt; er sieht die zwölf Ströme, die sich zusammenziehen und materiell werden in den zwölf Gehirnnerven des Menschen; er sieht, wie entgegengewirkt dem, was von oben herunterkommt, dasjenige, was aus dem Herzen, aus dem menschlichen Süden kommt; er sucht es im Makrokosmos draußen und versteht es, wenn es ihm als «Muspelheim» genannt wird.",
      "So hat er noch in christlichen Jahrhunderten ein Verständnis für das Begreifen des Mikrokosmos aus dem ganzen Makrokosmos heraus, und man kann für ihn noch weiter zurückgehen, indem man den Menschen nach und nach aus dem Makrokosmos, als Extrakt der ganzen Welt, entstehen läßt. Er ist imstande, zurückzublicken in diese Zeit, und kann verstehen, daß diese Vorgänge eine Vergangenheit haben, welche er selber noch sieht als ein Hineinarbeiten der Engel und Erzengel in seine Seele.",
      "Er kann einsehen, daß diese Vorgänge eine Vergangenheit haben, und was er sich da als Vorstellungen erwirbt, das ist das, was uns ent­gegentritt, was erkannt wird als die altgermanisch-nordische Genesis, als die Entstehung der Menschheit aus dem gesamten Makrokosmos heraus.",
      "Da, wo angefangen wird bei dem germanisch-nordischen Chaos, bei dem Ginnungagap, mit dem stehen wir ungefähr da, wo die Erde sich",
      "wieder von neuem bildet, nachdem sie die drei früheren Zustände, Saturn-, Sonnen- und Mondzustand, durchgemacht hat, wo die Erde sich also aus dem Pralaya wieder heraushebt, wo die Reiche der Natur sich noch nicht differenziert haben, wo die Menschen noch ganz geistige Wesen sind. Da versteht der nordische Mensch dann, wie sich heraus­bilden die späteren Zustände.",
      "Und nun ist es interessant zu sehen, wie in der nordisch-germanischen Mythologie in Bildern imaginativer Form die Vorgänge geschildert werden, die sich in jenen Zeiten abgespielt haben, und für die wir in den geisteswissenschaftlichen Lehren nur reifere Ausdrücke, Begriffe statt der früheren Bilder gebrauchen. Es werden geschildert die Vorgänge, die stattfanden, als noch Sonne und Mond verbunden waren. Es wird uns das Hinausgehen des Mondes geschildert und wie dann die Ent­wickelung übergeht in dasjenige, was später zum «Riesenheim» wird. Es wird uns geschildert alles das, was während der atlantischen Zeit gewesen ist, als Fortsetzung von dem, was früher geschehen war und was eigene Angelegenheiten des germanisch-nordischen Volkes dar­stellte.",
      "Für heute wollte ich nur einen Begriff davon hervorrufen, wie das nordische Ich erwacht ist, als es noch auf einer niederen Stufe der Ent­wickelung stand, wie der nordische Mensch hineinsah in die Volksseele, in die Seele des Thor und so weiter. Ich wollte ein Gefühl dafür hervor­rufen, wie das Ich dabei war, wie es ein unmittelbares Interesse gewin­nen konnte für das Hineinweben auch höherer Wesenheiten, welche aber von einer ganz anderen Seite her kamen als die Wesenheiten, die wir bei den östlichen Völkerschaften finden.",
      "Morgen wollen wir versuchen, den Zugang zu finden zu den entlege­neren Teilen der germanischen Mythologie. Wir werden erkennen, wie diese entlegenen Teile Vorboten sind für das, was in den Volksseelen lebt, und wir werden sehen, welches die Natur gerade dieser unserer westlichen Volksseelen ist."
    ],
    "sentences": [
      [
        "Wenn man die Entwickelung der germanisch-nordischen Geschichte und die darin geschilderten geistigen Impulse studieren will, dann hat man nötig, den Grundcharakter der germanisch-nordischen Mytho­logie zunächst ins Auge zu fassen, und es ist schon das letzte Mal darauf aufmerksam gemacht worden, daß diese germanisch-nordische Mytho­logie, trotz manchem, worin sie Ähnlichkeit hat mit anderen Mytho­logien und Götterauffassungen, doch etwas ganz Eigentümliches ist.",
        "Dabei bleibt doch richtig, daß ein sehr weitgehender Grundkern mythologischer Auffassung sich über alle germanischen Völker und Stämme Europas hin erstreckt, so daß bis weit nach Süden hin eine ein­heitliche mythologische Auffassung, im Grunde genommen ein gleich­artiges Verständnis jener verwandtschaftlichen Beziehungen möglich ist."
      ],
      [
        "Gerade für das Eigenartige der germanisch-nordischen Mythologie muß durch alle Volksgebiete, in denen in der einen oder anderen Form diese Mythologie ausgebreitet war, einstmals ein gleiches Verständnis vorhanden gewesen sein; denn es unterscheidet sich das, was gemeinsam ist in der Mythologie der germanisch-nordischen Völker, ganz gewaltig schon von dem Wesenskern der griechischen Mythologie, ganz zu schweigen von der ägyptischen, so daß alles, was verwandt ist in der germanischen Mythologie, einander ganz nahe steht und weit entfernt ist von dem, was das Wesentliche in der griechischen und römischen Mythologie ist.",
        "Man kann aber dieses Wesentliche heute nicht sehr leicht verstehen, aus dem Grunde nicht, weil aus Erkenntnisvoraus-setzungen - über welche zu sprechen hier zu weit führen würde -heute eine gewisse Sehnsucht, ein gewisser Trieb herrscht, die Religionen der verschiedenen Völker einfach miteinander zu vergleichen."
      ],
      [
        "Verglei­chende Religionswissenschaft, vergleichende Mythologie, das ist etwas, wofür heute viel Enthusiasmus herrscht.",
        "Es ist dies ein Gebiet, auf dem es möglich ist, den allergrößten Unfug zu treiben.",
        "Was geschieht denn gewöhnlich, wenn man Mythologien und Religionen einzelner Völker miteinander vergleicht?"
      ],
      [
        "Man vergleicht die Äußerlichkeiten, die in den"
      ],
      [
        "Göttergeschichten vorliegen, sucht nachzuweisen, daß die eine Götter­gestalt in der einen Mythologie vorkommt und in ähnlicher Weise auch in der anderen und dergleichen mehr.",
        "Diese Religionsvergleichung ist für denjenigen, der den Tatbestand, der darin vorliegt, wirklich kennt, so ziemlich das Unbehaglichste in unserer gegenwärtigen Wissenschafts­richtung, deshalb, weil man eigentlich überall nur die Äußerlichkeiten vergleicht.",
        "Eine solche Religionsvergleichung macht auf den, der den Tatbestand kennt, ungefähr den Eindruck, wie wenn jemand sagte:"
      ],
      [
        "«Vor dreißig Jahren lernte ich einen Menschen kennen.",
        "Der trug eine Uniform, die war so und so beschaffen.",
        "Der Mann hatte blaue Hosen, einen roten Rock und diese oder jene Kopfbedeckung und so weiter» und schnell dann fortfährt: «Dann habe ich vor 20 Jahren einen Men­schen kennen gelernt, der trug dieselbe Uniform und vor zehn Jahren wieder einen, der trug wieder dieselbe Uniform.» Wenn der Betreffende nun glauben würde, die Menschen, die er da kennen gelernt hat vor dreißig Jahren, zwanzig Jahren und zehn Jahren, weil sie gleiche Uni­form trugen, auch ihrer Wesenheit nach miteinander vergleichen zu können, so kann er sich sehr irren; denn es kann ein ganz anderer Mensch, in den verschiedenen Zeiten, in der Uniform drinstecken, und es kommt doch im wesentlichen darauf an, was für ein Mensch in der Uniform steckt."
      ],
      [
        "Das Gleichnis ist scheinbar weit hergeholt, und denn-noch kommt es bei der Religionsvergleichung auf dasselbe hinaus, wenn man den Adonis nimmt und ihn mit dem Christus vergleicht.",
        "Da ver­gleicht man nur die äußere Uniform."
      ],
      [
        "Kleidung und Eigenschaften der Wesen in den Sagen können sehr ähnlich oder gleich sein, aber es han­delt sich darum, was für geistig-göttliche Individualitäten darinnen sind, und wenn das ganz andere Individualitäten sind, die im Adonis und im Christus darinnen stecken, so hat eben diese Vergleichung nur den Wert einer Vergleichung der Uniform.",
        "Dennoch ist diese Verglei­chung heute ungemein beliebt."
      ],
      [
        "Es kommt also auf das vielfach durchaus gar nicht an, was heute die vergleichende Religionswissenschaft mit ihren ganz äußerlichen Methoden auf diesem Gebiete zutage fördern kann.",
        "Es kommt vielmehr darauf an, daß man kennen lernt, gewisser­maßen aus der Differentiation der Volksgeister heraus, die Art und Weise wie dieses oder jenes Volk, sei es zu seiner Mythologie, sei es zu"
      ],
      [
        "seiner sonstigen Götterlehre, sei es selbst zu seiner Philosophie, gekom­men ist."
      ],
      [
        "Wir können daher den Grundcharakter der germanisch-nordischen Mythologie kaum anders verstehen, als wenn wir noch einmal einen Streifzug machen durch die aufeinanderfolgenden fünf Kulturperioden der nachatlantischen Zeit.",
        "Diese fünf Kulturperioden wurden dadurch hervorgerufen, daß von Westen nach Osten Wanderzüge stattgefunden haben, daß sozusagen die allerreifsten, fortgeschrittensten Menschen nach Absolvierung dieser Wanderzüge in das indische Gebiet vorrück­ten und dann die heilige uralt-indische Kultur begründeten.",
        "Weiter herauf, gegen unsere Zeit, wird die persische Kultur begründet, dann die ägyptisch-chaldäisch-babylonische Kultur, dann die griechisch-lateinische Kultur, auf die endlich die unserige folgt.",
        "Diese fünf Kul­turen sind in ihren Wesenskernen nur dadurch zu verstehen, daß man weiß, daß die Menschen, die an diesen Kulturen beteiligt sind, und auch die Engelwesen, die Volksseelen oder Erzengel und die Zeitgeister in den verflossenen Zeiten selber alle durchaus voneinander verschieden waren.",
        "Heute wollen wir mehr Rücksicht darauf nehmen, wie die Men­schen verschieden waren, die an diesen Kulturen teilgenommen haben."
      ],
      [
        "Grundverschieden waren die Menschen, die im alten Indien die uralt-indische Kultur begründeten, die dann ihre literarische Einklei­dung in den Veden und in der späteren indischen Literatur gefunden hat, grundverschieden zum Beispiel von den griechisch-lateinischen Völkern, verschieden schon von den persischen, verschieden von den ägyptisch-chaldäischen und am meisten verschieden von den Völkern, welche in Europa vorbereitend heranwachsen zur fünften Kultur-periode der nachatlantischen Zeit.",
        "Inwiefern waren sie aber verschie­den?",
        "Es war die ganze Menschheitsanlage der uralt-indischen Völker absolut verschieden von den Menschen aller weiter nach Westen gele­genen Volksgebiete.",
        "Wenn wir uns eine Vorstellung davon bilden wollen, welche Verschiedenheit da bestand, so müssen wir uns sagen:"
      ],
      [
        "Es waren die Völker des alten Indien sehr weit in der menschlichen Entwickelung fortgeschritten, bevor sie aufnahmen das Ich.",
        "Sie hatten in bezug auf alles übrige in der Menschheitsentwickelung große, unge­heuer große Fortschritte gemacht, sie hatten hinter sich eine lange,"
      ],
      [
        "lange Menschheitsentwickelung.",
        "Das hatten sie aber durchgemacht gewissermaßen in einer Art von Dumpfheit.",
        "Dann trat das «Ich» ein, das Bewußtsein des Ich.",
        "Das trat in verhältnismäßig später Zeit beim indischen Volke ein; zu einer Zeit, als das indische Volk in gewissem Grade schon sehr reif war, als es schon durchgemacht hatte, was die germanisch-nordischen Völker noch durchmachen mußten, während sie schon ihr Ich besaßen. - Fassen Sie das wohl ins Auge!",
        "Die germa­nisch-nordischen Völker mußten mit ihrem vollentwickelten Ich bei dem dabei sein, was die Bewohner des uralten Indiens in einer gewissen Dumpfheit, also ohne mit ihrem Ich dabei zu sein, durchgemacht hatten."
      ],
      [
        "Was ist es denn nun, was man in der nachatlantischen Zeit als Menschheitsentwickelung durchmachen konnte?",
        "Wenn man in der alten atlantischen Zeit als Mensch lebte, so war man als solcher Mensch noch mit einem höheren Grade alten, dumpfen Hellsehens behaftet."
      ],
      [
        "Man sah durch altes, dumpfes Hellsehen in die göttlich-geistige Welt hinein, man sah die Vorgänge, die sich in dieser Welt abspielen.",
        "Ver­setzen Sie sich nun eine Weile hinüber in das alte atlantische Land, bevor die Züge nach Osten gehen."
      ],
      [
        "Die Luft war noch durchsetzt mit Wasser- und Nebeldämpfen.",
        "Aber auch die Seele der Menschen war anders.",
        "Der Mensch unterschied noch nicht einmal die verschiedenen äußeren Sinneswahrnehmungen von einander."
      ],
      [
        "Es war damals so, daß er wie ein geistiges Aroma, wie eine geistige Aura den geistigen Gehalt der Welt um sich ausgebreitet fand.",
        "Ein gewisses Hellsehen war also da vorhanden, und aus diesem Hellsehen mußte man herauskommen."
      ],
      [
        "Dies geschah durch die Wirkung der Kräfte, in deren Bereich die Menschen kamen bei den Wanderzügen von Westen nach Osten.",
        "Bei diesen Wan­derzügen wurden wieder die verschiedensten Seelenentwickelungen durchgemacht."
      ],
      [
        "Da gab es Völker, welche, indem sie hinüberwanderten nach dem Osten, zuerst wie verschliefen das Heraustreten aus dem alten Hellsehen und schon auf einer höheren Stufe der Entwickelung waren, als ihr Ich noch immer in Dumpfheit sich befand.",
        "Sie machten verschiedene Stufen der Entwickelung durch, und ihr Ich war noch immer ein dumpfes, ein träumerisches."
      ],
      [
        "Am weitesten waren die Inder entwickelt, als ihr Ich mit vollem Selbstbewußtsein erwachte.",
        "Da waren sie schon so, daß sie ein sehr reiches inneres Seelenleben hatten, das gar"
      ],
      [
        "nicht mehr diejenigen Zustände besonders in sich zeigte, welche die Völker Europas noch lange erlebten.",
        "Diese hatten sie schon durchge­macht.",
        "Sie erwachten zum Selbstbewußtsein, als sie bereits mit geistigen Kräften und geistigen Fähigkeiten ausgestattet waren, durch die sie in hohem Grade hineindringen konnten in die geistigen Welten."
      ],
      [
        "Daher war den Fortgeschrittenen der indischen Bevölkerung bei ihrem Sich­herausarbeiten aus ihren alten dämmerhaften Hellseherzuständen all das Treiben und Tätigsein der verschiedenen Engel- und Erzengelwesen an den menschlichen Seelen im Grunde genommen höchst gleichgültig geworden.",
        "Die Arbeit der Erzengel und Engel und derjenigen geistigen Wesenheiten überhaupt, die besonders im Volksgeiste arbeiteten, hatten sie nicht mehr unmittelbar beobachtet."
      ],
      [
        "Das war an ihrer Seele, an ihrem Astral- und Ätherleib geleistet worden, als sie sozusagen noch gar nicht dabei waren.",
        "Sie erwachten, als ihre Seele mit einem ungeheueren Reife-grade bereits behaftet war; sie erwachten so, daß die Fortgeschritten­sten dasjenige, was früher mit der Menschheitsentwickelung geschehen war, durch eine leichte Entwickelung bereits in der Akasha-Chronik wieder lesen konnten, so daß sie hinausblickten in die Umgebung, in die Welt und daß sie dadurch in der Akasha-Chronik lesen konnten, was in der geistigen Welt vorging, was sie durchgemacht hatten in dump­fem, dämmerhaftem Bewußtseinszustande."
      ],
      [
        "Sie waren unbewußt in höhere Gebiete geleitet, sie hatten, bevor ihr Ichbewußtsein erwacht war, geistige Fähigkeiten erlangt, die viel reicher waren als die Seelen-fähigkeiten der westlichen Völker.",
        "So war die geistige Welt für diese Menschen eine unmittelbare Beobachtung."
      ],
      [
        "Die Fortgeschrittensten der indischen Volksführung waren so weit, daß sie, als ihr Ich erwachte, tatsächlich nicht einmal mehr darauf angewiesen waren, zu beobachten, wie sozusagen die menschliche Entwickelung heraussprudelte aus den Geistern der Form oder Gewalten, sondern es war ihnen dasjenige ver­trauter, was wir Geister der Bewegung, Mächte nennen und dasjenige, was über diesen ist, die Geister der Weisheit.",
        "Das interessierte sie ganz besonders."
      ],
      [
        "Diejenigen geistigen Wesenheiten, die darunter stehen, wa­ren dagegen solche Wesenheiten, in deren Bereich sie schon früher gewesen, die ihnen daher nicht mehr von so ganz besonderer Wichtig­keit waren.",
        "So sahen sie auf zu dem, was sie später nannten die Summe"
      ],
      [
        "aller Geister der Bewegung und aller Geister der Weisheit; zu dem, was man später mit den griechischen Ausdrücken Dynameis und Kyrio­tetes bezeichnete.",
        "Zu diesen sahen sie auf und sagten zu ihnen: Mula­Prakriti, das ist die Summe der Geister der Bewegung, und Maha-Puru­sha, die gesamte Summe der Geister der Weisheit, was wie in einer geistigen Einheit lebt.",
        "Solche Anschauungen konnten sie gewinnen, weil die Angehörigen dieses Volkes in so späten Zuständen der Entwicke­lung zu ihrem Ich erwachten.",
        "Sie hatten schon abgemacht, was die späteren Völker mit ihrem Ich noch mit anschauen mußten."
      ],
      [
        "Weniger weit entwickelt waren die Völker der persischen Kultur.",
        "Sie waren so weit durch ihr eigenartiges Erkenntnisvermögen und durch das Erwachen ihres Ich auf einer niedrigeren Stufe, daß sie sich be­schäftigen konnten mit den Wesenheiten der Gewalten oder Geister der Form.",
        "Mit diesen wurden sie ganz besonders vertraut.",
        "Diese durch-schauten sie in gewisser Weise, und sie interessierten sich auch vorzugs­weise für sie.",
        "Eine Stufe tiefer als die Inder, aber doch auf einer Stufe, auf die dann wieder die Völker des Westens sich heraufarbeiten mußten, erwachten die Völker der persischen Gemeinschaften.",
        "Daher wurden sie mit den Gewalten oder Geistern der Form bekannt, die sie unter dem Begriffe der «Amshaspands» zusammenfaßten.",
        "Das sind die Ausstrahlungen, die wir als die Geister der Form oder Gewalten kennen und die, von ihrem Gesichtspunkte aus, gerade die Völker der persi­schen Kultur besonders gut beobachten konnten."
      ],
      [
        "Dann kommen wir zu den chaldäischen Völkern.",
        "Die hatten schon ein Bewußtsein von dem, was wir als Urkräfte, als führende Zeitgeister kennen.",
        "Sie hatten ein Bewußtsein von den Wesenheiten, die als Ur­kräfte, als Geister der Persönlichkeit erfaßt werden sollen.",
        "In einer anderen Weise hatten wiederum die Völker der griechisch-lateinischen Zeit gerade auch von diesen Urkräften oder Geistern der Persönlich­keit ein gewisses Bewußtsein.",
        "Aber bei ihnen war noch etwas ganz anderes vorhanden, und das war das, was uns ein Stück weiter in der Erkenntnis führen könnte.",
        "Die Griechen standen den germanischen Völkern noch näher.",
        "Aber doch erwachte dort das Ich auf einer höhe­ren Stufe als bei den germanisch-nordischen Völkern.",
        "Das, was bei den nordischen Völkern noch als Arbeit der Engel und Erzengel durchlebt"
      ],
      [
        "wurde, das durchlebten die griechisch-lateinischen Völker nicht mehr unmittelbar.",
        "Sie hatten aber noch eine deutliche Erinnerung daran.",
        "Denken Sie sich also, daß der Unterschied zwischen den germanischen und den griechisch-lateinischen Völkern der ist, daß die griechisch-lateinischen Völker noch eine Erinnerung daran hatten, wie die Engel und Erzengel an ihrem Seelenleben, das sie in sich entwickelt hatten, teilgenommen haben."
      ],
      [
        "Sie hatten dies im Grunde genommen aber nicht allzu deutlich durchgemacht.",
        "Sie waren dabei noch in einem dumpfen Bewußtseinszustande.",
        "Doch in der Erinnerung trat es ihnen nun ganz besonders vor die Seele."
      ],
      [
        "Die Schöpfung dieser ganzen Welt, die Art und Weise, wie die Engel und Erzengel - die abnormen und die nor­malen - in die menschliche Seele hereinwirken, das kannten die Grie­chen.",
        "Was sie durchgemacht hatten, das hatten sie in einem gewaltigen Erinnerungsbilde in ihrer Seele."
      ],
      [
        "Erinnerung ist das, was abgeklärter ist, festere Konturen hat als das, was man erlebt.",
        "Es ist nicht mehr so frisch und nicht mehr so jung, aber es hat schärfere Umrisse, schärfere Kon­turen, was als Gedächtnis, als Erinnerung auftritt."
      ],
      [
        "Der Einfluß oder Impuls der Engel- und Erzengelwelt auf die Menschenseele wurde bei den Griechen aus der Erinnerung in festen, scharfen Konturen wach­gerufen.",
        "Das ist die griechische Mythologie.",
        "Wer sie nicht so ansieht, sondern nur die Namen vergleicht mit Namen, die anderswo auftreten, also nicht die besonderen Kräfte ins Auge faßt, nicht die Gestalten auffaßt, die auftreten als Apollo, Minerva und so weiter, der treibt äußere Religionsvergleichung, vergleicht bloß die Uniformen."
      ],
      [
        "Die Art und Weise, wie damals angeschaut wurde, ist es, worauf es ankommt."
      ],
      [
        "Nachdem wir dies gesehen haben, werden wir zugeben: Die Griechen formten sich ihre Mythologie heraus aus der Erinnerung. - Die ägyp­tisch-chaldäische Zeit hatte nur eine dunkle, dumpfe Erinnerung an das Wirken der Engel- und Erzengelwelt, aber einen Ausblick in die Welt der Urkräfte.",
        "Es ist bei ihr so, wie wenn sie anfinge, etwas zu vergessen.",
        "In der persischen Mythologie oder Götterlehre haben wir dafür ein vollständiges Vergessen der Engel- und Erzengelwelt, aber zugleich einen Ausblick in die Welt der Gewalten oder Geister der Form.",
        "Das, was in der griechischen Mythologie liegt, haben die persischen Völker und erst recht die indischen vergessen.",
        "Sie schauten die ganzen Vorgänge"
      ],
      [
        "bereits wieder aus der Akasha-Chronik an und schufen sich die Bilder der früheren Vorgänge aus ihrer Erkenntnis heraus, die aber schon vergöttlichte Erkenntnis mit höher entwickelten Geisteskräften war.",
        "Daraus werden Sie aber auch erkennen, daß es gerade jenen Völ­kern des Ostens ungemein schwer wird, das abendländische Geistes­leben zu verstehen.",
        "Daher kommt dann jene Zugeknöpftheit der Völker des Ostens gegenüber dem abendländischen Geistesleben.",
        "Sie werden gewiß die materielle abendländische Kultur annehmen; aber die geistige Kultur des Abendlandes bleibt ihnen, wenn sie nicht auf dem Umwege der Geisteswissenschaft dazu kommen, mehr oder weniger verschlossen.",
        "Sie standen auf einer menschlich hohen Stufe zu der Zeit schon, als auf der Erde noch kein Christus Jesus war.",
        "Der kam erst in der vierten nachatlantischen Kulturepoche.",
        "Das ist ein Ereignis, das man nicht mehr auffassen konnte mit den Kräften, welche sich aus dem indischen Volkstum heraus entwickelt hatten.",
        "Dazu brauchte man noch Kräfte, die verwandt waren mit einem weniger hohen Stand des Ich, mit einem Darinstehen des Ich in untergeordneten Seelenkräften."
      ],
      [
        "In den germanisch-nordischen Gebieten war das Hereinarbeiten der Angeloi und Archangeloi in die Menschenseele nicht etwa bloß als Erinnerung vorhanden, sondern so, daß die Menschen, selbst noch zur Zeit als der Christus Jesus auf der Erde wandelte, das noch sehen konn­ten, daß sie noch darin standen, daß sie die Angelegenheiten der Engel-und Erzengelwesen, wie sie noch in ihrer Seele arbeiteten, mitmachten.",
        "Die griechisch-lateinischen Völker erinnerten sich bei diesen Seelen-Erlebnissen an etwas, was sie früher einmal durchgemacht hatten.",
        "Die germanischen Völker lebten darin als in ihren eigenen, unmittelbaren Angelegenheiten.",
        "Ihr Ich war erwacht auf der Stufe des Daseins, wo noch hereinarbeiteten in die Seele die Volksgeister und diejenigen gei­stigen Wesenheiten, die selbst noch unter den Volksgeistern stehen.",
        "Daher standen diese Völker am allernächsten dem, was wir die Vor­gänge in der alten Atlantis drüben kennen."
      ],
      [
        "In der alten Atlantis sah man auf zu den geistigen Mächten und sprach von einer Art von Einheitsgottheit, weil man eben hinaufsah in unmittelbarer Wahrnehmung in alte, urferne Entwickelungszustände der Menschheit.",
        "Man sah damals gleichsam noch das Walten der Geister"
      ],
      [
        "der Weisheit und das Walten der Geister der Bewegung, das die spä­teren Inder wieder aus der Akasha-Chronik heraus beobachteten.",
        "Um eine Stufe hatten sich diese Völker des Westens über diesen Standpunkt hinauserhoben, so daß sie in unmittelbarer Gegenwart das Herausdrän­gen aus der alten Anschauung in die neue hinein erlebten."
      ],
      [
        "Sie sahen in ein Weben und Leben von wirklichen geistigen Mächten zu einer Zeit, als das Ich noch nicht erwacht war.",
        "Aber sie sahen zugleich, wie das Ich nach und nach erwachte, und wie Engeiwesen und Erzengel-wesen in die Seele eingriffen."
      ],
      [
        "Diesen unmittelbaren Übergang nahmen sie wahr.",
        "Sie hatten eine Erinnerung an ein früheres Weben und Leben, als die Anschauung noch so war, daß man gleichsam alles wie in einem Nebelmeer sah, und sie schauten, wie dann aus diesem Nebelmeer für sie das herauskam, was wir als die göttlich-geistigen Gestalten, die unmittelbar über dem Menschen stehen, kennen gelernt haben."
      ],
      [
        "Die alten Götter aber, die gewirkt haben, bevor in das menschliche Seelen-leben die Götter eingriffen, die man jetzt sah, mit denen man sich ver­bunden fühlte, diese göttlichen Wesenheiten, die in ferner, ferner Ver­gangenheit, in der Zeit der alten Atlantis, wirksam waren, nannte man die Wanen.",
        "Herausgetreten aus der alten atlantischen Zeit sind dann die Menschen und sahen auf das Weben der Engel und Erzengel; die nannte man die Asen."
      ],
      [
        "Das waren diejenigen Wesen, die sich als Engel und Erzengel kümmerten um das Ich der Menschen, das jetzt auf der untersten Stufe erwachte.",
        "Vorgesetzt waren sie jenen Völkern.",
        "Das, was die anderen Völker des Ostens verschlafen haben, nämlich zu sehen, wie die Seele sich hinaufarbeitet durch die verschiedenen Kräfte, die von den normalen und abnormen Engel- und Erzengelwesen verliehen werden, das mußten die Völker Europas von unten auf beginnend durchmachen; sie mußten ganz dabei sein, damit sich diese Seelenkräfte nach und nach entwickelten."
      ],
      [
        "So waren also die Göttergestalten, welche sich sozusagen vor die Seele des germanisch-nordischen Menschen stellten, die Göttergestal­ten, die unmittelbar an seiner Seele arbeiteten und dasjenige, was er selbst als das Sichherausringen des Menschlich-Seelischen aus dem Kos­mischen beobachtete, unmittelbare Anschauungen; das war etwas, was er unmittelbar erlebte.",
        "Er schaute nicht zurück in der Erinnerung auf"
      ],
      [
        "die Art und Weise, wie die Seelen sich in die Leiber hineingebildet haben, er sieht vielmehr als gegenwärtig, was da gschieht.",
        "Es ist seine eigene Entwickelung, und er ist mit seinem Ich dabei.",
        "Er hat Verständ­nis dafür bis ins achte, neunte, zehnte Jahrhundert nach Christus."
      ],
      [
        "Er hat sich ein Verständnis dafür bewahrt, wie die Seelenkräfte nach und nach sich bilden, sich hineinkristallisieren in den Leib.",
        "Zuerst schaut er auf die Erzengelwesen, welche in seiner Seele arbeiteten, indem sie ihm das gaben, was seine Seelenkräfte werden sollten, und da findet er als den hervorragendsten dieser Erzengel Wotan oder Odin und sieht ihn an seiner Seele arbeiten, sieht, wie er in seine Seele hineinarbeitet."
      ],
      [
        "Was sieht er da?",
        "Wie nimmt er Wotan oder Odin wahr?",
        "Als was erkennt er ihn, und als was lernt er ihn lieben und, vor allen Dingen, als was ver­stehen?",
        "Er lernt ihn erkennen als einen derjenigen Erzengel, die dazu gekommen sind, einmal Verzicht zu leisten auf den Aufstieg zu höheren Stufen."
      ],
      [
        "Er lernt Odin als einen der abnormen Erzengel kennen, als einen der großen Verzichter der Vorzeit, die das Erzengeltum über­nommen hatten, als sie die wichtige Mission auf sich nahmen, in die Seele des Menschen hineinzuarbeiten.",
        "Den Odin in seiner Tätigkeit erlebt der germanisch-nordische Mensch noch in der Zeit, in der er an das Werk herangeht, der Seele die Sprache einzuimpfen."
      ],
      [
        "In wunder-barer Weise hat sich erhalten, wie Odin selbst an seinen Völkern arbei­tet, um ihnen die Sprache möglich zu machen.",
        "Das wird geschildert als eine Götter-Einweihung.",
        "Wie Odin dazu kam, sich die Macht zu ver­schaffen, den Seelen der germanisch-nordischen Völker die Sprache zu verleihen, das wird dadurch geschildert, daß Odin, bevor er diese Fä­higkeit erlangt hatte, dasjenige durchmacht, was uns als die Einweihung durch den Göttertrank dargestellt wird, den Göttertrank, der einstmals"
      ],
      [
        "- in urferner Vergangenheit bei den Riesen war.",
        "Dieser Trank enthielt nicht bloß eine abstrakte Weisheit, sondern stellt uns die unmittelbar im Laut sich auslebende Weisheit dar.",
        "Über die im Laute sich ausle­bende Weisheit erringt Odin bei seiner Einweihung die Macht; er lernt sie handhaben, als er eine lange Einweihung, eine Einweihung von neun Tagen durchmacht, aus der er dann durch Mimir, den alten Träger der Weisheit, erlöst wird.",
        "So wird Odin der Herr der Sprachgewalt.",
        "Daher führt die spätere Sage die Sprache der Dichter, die Sprache der Skalden"
      ],
      [
        "auf Odin zurück.",
        "Auf Odin wird auch zurückgeführt die Runenkunde, die in alten Zeiten mit der Sprache viel näher verwandt gedacht wurde als das spätere Schrifttum.",
        "Wie also die Seele auf dem Umwege durch den Ätherleib und hineinlebend in den physischen Leib durch den ent­sprechenden Erzengel die Sprache erwirbt, das drückt sich aus in den wunderbaren Geschichten, die über Odin erzählt werden."
      ],
      [
        "Ähnliche Erzengelwesen haben wir in den Genossen des Odin vor uns, in Hönir, welcher die Kraft des Vorstellens verleiht und in Lodur, welcher dasjenige verleiht, was der Rasse noch am nächsten liegt, also Hautfarbe und Blutcharakter.",
        "In diesen zwei Wesen haben wir also Erzengelwesen zu sehen, die sozusagen mehr nach der normalen Seite hin liegen.",
        "Die abnormen haben wir dann in den Wesen zu erkennen, die als Wili und We auftreten.",
        "Das sind Wesenheiten, die mehr noch im Innern, im Intimen der Seele wirken, wie ich es im vergangenen Vor-trage klargelegt habe.",
        "Aber innig verwandt fühlt sich gerade mit einem abnormen Erzengel ein solches Ich, das selbst auf einer abnormen Ent­wickelungsstufe steht, wo es schon bei der Heranbildung der unter­geordneten Seelenkräfte dabei ist.",
        "Ein solches Ich fühlt sich verwandt mit einem abnorm entwickelten Erzengelwesen Daher wird auch Odin nicht als abnormer Erzengel empfunden, vielmehr als solcher, der in seinem Zurückbleiben verwandt ist mit dem Zurückbleiben der west-ländischen Seelen, die in mehr bewußter Weise das in ihrem Ich erleben, was beim Durchgang durch jene Gebiete zurückgeblieben ist, wogegen die östlichen Seelen an gewissen Stadien des Seelenlebens vor-übergingen, bis sie sich entschlossen, zu erwachen.",
        "Daher lebt vor allen Dingen in der Seele der germanisch-nordischen Menschen alles das­jenige, was mit diesen in den elementaren Tiefen des Seelenlebens wüh­lenden und arbeitenden Erzengelkräften des Odin verbunden ist."
      ],
      [
        "Wenn wir gesagt haben, daß die Engel es sind, welche dasjenige, was die Erzengel bewirken, in die einzelnen Menschen heruntertragen, so hat ein Ich, das auf einer so frühen Elementarstufe des Seelenlebens erwacht, vor allen Dingen ein Interesse daran, daß in jenes Ich gleich­sam die Angelegenheiten der Erzengel hineingetragen werden.",
        "Daher hat der germanisch-nordische Mensch ein Interesse an einer solchen Engelgestalt, welche von besonderer Macht ist, aber zu gleicher Zeit"
      ],
      [
        "innig verwandt ist mit dem einzelnen Menschen und seiner Individua­lität.",
        "Das ist Thor.",
        "Thor wird nur dadurch erkannt, daß man weiß, daß in ihm gesehen werden muß eine Wesenheit, die zwar sehr vorgerückt sein könnte, wenn sie normal sich weiter entwickelt hätte, die aber verhältnismäßig früh verzichtet hat und auf der Stufe der Engel zu­rückgeblieben ist, damit sie in der Zeit, da das Ich in der Seelenentwik­kelung erwachte, Führer in der Seelenwelt der germanisch-nordischen Gebiete sein konnte.",
        "Daß dasjenige, was aus der geistigen Welt in jedes einzelne Ich hineingetragen werden sollte, auch hineingetragen werden konnte, das ist es, was in Thor als verwandt mit dem einzelnen mensch­lichen Ich so unmittelbar empfunden wird.",
        "Wenn wir dies ins Auge fassen, dann werden wir das, was an Einzelheiten überliefert ist, auch besser verstehen.",
        "Bei uns handelt es sich ja darum, diese Götterindivi­dualitäten in entsprechender Weise verstehen zu können.",
        "Nun aber hat der germanisch-nordische Mensch empfunden, miterlebt dieses Ein­prägen der Seele in die Leiblichkeit.",
        "Er war dabei, als das Ich sich in die Leiblichkeit hineingliederte und von jedem einzelnen Menschen Besitz ergriff."
      ],
      [
        "Nun wissen wir, daß das Ich im Blute des physischen Leibes pulsiert, und es entspricht jedem Inneren ein Äußeres, jedem Mikrokosmischen ein Makrokosmisches.",
        "Der Arbeit des Sprachen- und Runenweisheit gebenden Odin, der auf einem weiten Umweg durch das Atmen wirkte, entspricht draußen im Makrokosmos die Windesbewegung.",
        "Dem regel­mäßigen Eindringen der Luft durch unsere Atmungsorgane, welche die Umformung der Luft zu dem Wort, der Sprache bewirken, dem ent­sprechen draußen im Makrokosmos die Bewegungen, die Strömungen im Winde.",
        "Ebenso wahr, wie wir das Walten des Odin in der Umgestal­tung der Luft zu den Worten in uns selber empfinden, ebenso wahr müssen wir ihn draußen im Winde walten und wirken sehen.",
        "Das aber hat derjenige, der noch die alten germanisch-nordischen Fähigkeiten besaß, zu denen besonders ein gewisser Grad von Hellsichtigkeit ge­hörte, wirklich gesehen.",
        "Der hat überall Odin im Weltenwind walten gesehen, hat ihn gesehen, wie er durch seinen Atem die Sprache formte.",
        "Das sah der nordische Mensch als eine Einheit.",
        "So wie das, was in uns lebt und die Sprache organisiert - das heißt so, wie bei der nordischen"
      ],
      [
        "Organisation die Sprache war -, hindurchdringt in das Ich und die Pulsation des Blutes bewirkt, so entspricht dem, was sich da als Sprache hineinorganisiert, draußen im Makrokosmos der Blitz und der Donner.",
        "Die Sprache ist eher da, als das Ich geboren ist."
      ],
      [
        "Daher wird das Ich überall als der Sohn derjenigen Wesenheit empfunden, welche die Sprache gibt.",
        "An der Einprägung in das einzelne Ich ist insbesondere Thor beteiligt, und was dem Vorgange im Makrokosmos entspricht, ist im Mikrokosmos die Pulsation des Blutes."
      ],
      [
        "Was also draußen im Makro-kosmos der Pulsation des Blutes im Menschen entspricht, das ist das­jenige, was als Blitz und Donner durch die wehenden Winde und webenden Wolken geht.",
        "Das aber sieht wiederum der germanisch-nor­dische Mensch in seinem Hellsehen als eine Einheit, und er sieht das Wehen des Windes, das Zucken des Blitzes draußen in innigem Zusam­menhang mit dem Weben der von ihm eingeatmeten Luft."
      ],
      [
        "Er sieht, wie sie ins Blut übergeht und da das Ich pulsieren macht.",
        "Das wird heute als ein materieller Vorgang angesehen, war aber noch ein astralischer Vorgang bei den germanisch-nordischen Menschen.",
        "Der sah die innige Verwandtschaft des Feuers, des Blitzes mit dem, was durch das Blut geht."
      ],
      [
        "Er fühlte den Pulsschlag in seinem Blute und wußte: Das ist der Schlag des Ich; wußte: Das, was da schlägt, spüre ich und spüre ich nach einiger Zeit wieder.",
        "Aber den äußeren, materiellen Vorgang be­achtete er nicht."
      ],
      [
        "Das alles war in hellseherische Empfindung gekleidet.",
        "Er empfand das, was den Pulsschlag bewirkt und ihn immer wieder an dieselbe Stelle zurückgehen läßt, als Thors Tat.",
        "Als das Immer-wieder­Zurückkehren des Hammers des Thor in die Hand des Thor fühlte er in seinem Ich die Thor-Kraft, die Kraft eines der mächtigsten Engel, die überhaupt jemals verehrt worden sind, weil er eine mächtige Wesen­heit war, die angesehen wurde als stehengeblieben auf der Stufe des Engeltums."
      ],
      [
        "Wie die geistige Kraft den physischen Leib zusammenhält, das drückt sich in der germanisch-nordischen Mythologie dadurch aus, daß das Ich dasjenige ist, was bei dem Gesponnenwerden des seelisch-leiblichen Wesens dieses zusammenhält.",
        "Von innen heraus sieht der germanisch-nordische Mensch das Weben des leiblich-seelischen Menschen, und er hat in späterer Zeit noch Verständnis dafür, wie aus dem Astralischen"
      ],
      [
        "sich sein Inneres hineingliedert, wie sozusagen das Innere dem Äußeren antwortet.",
        "Er hatte noch Verständnis dafür, wenn ihm von Eingeweih­ten gesagt wurde, wie die Welt zum Menschen sich formt.",
        "Da hatte er Verständnis dafür, zurückzugehen zu den früheren Stadien, zu dem, was ihm erzählt worden ist von den Geschehnissen, die das Verhältnis der Engel und Erzengel darstellen, zu den früheren Stadien, wo der Mensch aus dem Makrokosmos in physisch-geistiger Art herausgeboren worden ist."
      ],
      [
        "Er vermochte zu sehen, wie aus dem Makrokosmos der ein­zelne Mensch herausgebaut wird, wie er im Makrokosmos ruht.",
        "Er suchte sich im Makrokosmos diejenigen Vorgänge auf, die sich mikro­kosmisch so abspielen, daß von dem menschlichen Norden aus, aus dem kühlen Geistgebiet, die menschlichen Gedanken gewoben werden, und daß von dort aus die menschliche Leiblichkeit mit den zwölf Gehirn-nerven des Kopfes versorgt wird."
      ],
      [
        "Diesen Vorgang, der mikrokosmisch zu den zwölf Gehirnnerven geworden ist, sieht er.",
        "Er sieht den weben-den Geist in dem, was er «Nebelheim» oder «Niflheim» nennt; er sieht die zwölf Ströme, die sich zusammenziehen und materiell werden in den zwölf Gehirnnerven des Menschen; er sieht, wie entgegengewirkt dem, was von oben herunterkommt, dasjenige, was aus dem Herzen, aus dem menschlichen Süden kommt; er sucht es im Makrokosmos draußen und versteht es, wenn es ihm als «Muspelheim» genannt wird."
      ],
      [
        "So hat er noch in christlichen Jahrhunderten ein Verständnis für das Begreifen des Mikrokosmos aus dem ganzen Makrokosmos heraus, und man kann für ihn noch weiter zurückgehen, indem man den Menschen nach und nach aus dem Makrokosmos, als Extrakt der ganzen Welt, entstehen läßt.",
        "Er ist imstande, zurückzublicken in diese Zeit, und kann verstehen, daß diese Vorgänge eine Vergangenheit haben, welche er selber noch sieht als ein Hineinarbeiten der Engel und Erzengel in seine Seele."
      ],
      [
        "Er kann einsehen, daß diese Vorgänge eine Vergangenheit haben, und was er sich da als Vorstellungen erwirbt, das ist das, was uns ent­gegentritt, was erkannt wird als die altgermanisch-nordische Genesis, als die Entstehung der Menschheit aus dem gesamten Makrokosmos heraus."
      ],
      [
        "Da, wo angefangen wird bei dem germanisch-nordischen Chaos, bei dem Ginnungagap, mit dem stehen wir ungefähr da, wo die Erde sich"
      ],
      [
        "wieder von neuem bildet, nachdem sie die drei früheren Zustände, Saturn-, Sonnen- und Mondzustand, durchgemacht hat, wo die Erde sich also aus dem Pralaya wieder heraushebt, wo die Reiche der Natur sich noch nicht differenziert haben, wo die Menschen noch ganz geistige Wesen sind.",
        "Da versteht der nordische Mensch dann, wie sich heraus­bilden die späteren Zustände."
      ],
      [
        "Und nun ist es interessant zu sehen, wie in der nordisch-germanischen Mythologie in Bildern imaginativer Form die Vorgänge geschildert werden, die sich in jenen Zeiten abgespielt haben, und für die wir in den geisteswissenschaftlichen Lehren nur reifere Ausdrücke, Begriffe statt der früheren Bilder gebrauchen.",
        "Es werden geschildert die Vorgänge, die stattfanden, als noch Sonne und Mond verbunden waren.",
        "Es wird uns das Hinausgehen des Mondes geschildert und wie dann die Ent­wickelung übergeht in dasjenige, was später zum «Riesenheim» wird.",
        "Es wird uns geschildert alles das, was während der atlantischen Zeit gewesen ist, als Fortsetzung von dem, was früher geschehen war und was eigene Angelegenheiten des germanisch-nordischen Volkes dar­stellte."
      ],
      [
        "Für heute wollte ich nur einen Begriff davon hervorrufen, wie das nordische Ich erwacht ist, als es noch auf einer niederen Stufe der Ent­wickelung stand, wie der nordische Mensch hineinsah in die Volksseele, in die Seele des Thor und so weiter.",
        "Ich wollte ein Gefühl dafür hervor­rufen, wie das Ich dabei war, wie es ein unmittelbares Interesse gewin­nen konnte für das Hineinweben auch höherer Wesenheiten, welche aber von einer ganz anderen Seite her kamen als die Wesenheiten, die wir bei den östlichen Völkerschaften finden."
      ],
      [
        "Morgen wollen wir versuchen, den Zugang zu finden zu den entlege­neren Teilen der germanischen Mythologie.",
        "Wir werden erkennen, wie diese entlegenen Teile Vorboten sind für das, was in den Volksseelen lebt, und wir werden sehen, welches die Natur gerade dieser unserer westlichen Volksseelen ist."
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "NEUNTER VORTRAG Kristiania, 15. Juni 1910",
    "paragraphs": [
      "Wenn unter Ihnen Zuhörer sind, die den Vortrag von gestern philo­sophisch analysieren wollten, so könnten Sie vielleicht Schwierigkeiten, scheinbare Schwierigkeiten haben, und zwar aus dem Grunde, weil Sie ja aus früheren Darstellungen, die über ähnliche Themen gegeben wor­den sind, gehört haben, daß unser gesamter nachatlantischer Zeitraum und eigentlich schon die letzten Zeiten der atlantischen Entwickelung dazu da waren, das menschliche Ich als solches nach und nach zu ent­wickeln, immer mehr und mehr zur Bewußtheit zu bringen. Im Zusam­menhang damit wurde gesagt, daß gewissermaßen die Angehörigen der alten indischen Kultur die allerersten waren, welche, nachdem sie in der alten Atlantis noch durch das in der Menschheit sich findende alte Hellsehen den Einblick in eine geistige Welt hatten, unmittelbar aus diesem Hellsehen heraus in die physische Welt versetzt waren.",
      "Sie sahen diese physische Welt so, daß nun die Stimmung über die ganze erste nachatlantische Kulturperiode kam: Dasjenige ist die wahre Wirklich­keit, was hinter uns liegt in der geistigen Welt darinnen. Draußen aber in der Welt ist Maja oder Illusion.",
      "Nun wurde gestern auseinander­gesetzt - wie es auch den Tatsachen entspricht -, daß die Angehörigen dieser alten indischen Kultur gewissermaßen eine reiche Seelenentwik­kelung durchgemacht hatten, und es wurde gesagt, daß sie sie erlangt hatten mehr oder weniger bei schlafendem Ich, das heißt, daß das Ich erst erwacht ist, nachdem diese reife Seelenentwickelung schon erreicht war.",
      "Sie könnten sich jetzt vielleicht fragen: Was hat es denn eigentlich für diese indische Bevölkerung in der Zwischenzeit gegeben? Da muß ja sozusagen die indische Bevölkerung in einer ganz anderen Weise diese ganze Seelenentwickelung durchgemacht haben, als die europä­ische, namentlich die germanische Bevölkerung, die mit dem Ich dabei war, während sich die Fähigkeiten nach und nach entwickelten, die zugesehen hat, wie die göttlich-geistigen Mächte in ihre Seele herein-gewirkt haben. Das könnten Sie vielleicht schwer in Einklang bringen",
      "mit dem Gesagten, wenn Sie über den gestrigen Vortrag philosophisch denken wollten. Nur für diejenigen, die nicht aus völliger Unbefangen­heit, sondern aus einem solchen philosophischen Denken heraus den Vortrag analysieren wollen. muß ich noch etwas in Paranthese zur Aufklärung sagen.",
      "Sie werden den scheinbaren Widerspruch sofort auflösen, wenn Sie wie folgt zu Werke gehen, wenn Sie sich sagen: In bezug auf das Ich und seine Erkennbarkeit ist der Mensch in einer ganz anderen Lage als in bezug auf ein jegliches anderes Objekt. Wenn Sie irgendein anderes Objekt erkennen, einen anderen Gegenstand oder ein anderes Wesen als das Ich, dann haben Sie es eigentlich in der Erkenntnistätigkeit immer mit zweierlei zu tun: mit dem Erkenner, der Erkenntniskraft, und mit dem, was erkannt wird.",
      "Ob das, was erkannt wird, Mensch, Tier, Baum oder Stein ist, darauf kommt es nicht an für den rein formalen Erkennt­nisakt. Anders steht die Sache aber in bezug auf das Ich. Da ist das­jenige, was erkennt, und das, was erkannt wird, ein und dasselbe.",
      "Das Bedeutungsvolle ist, daß in der menschlichen Evolution, der mensch­lichen Entwickelung, diese zwei Dinge auseinanderfallen. Diejenigen, die die reife indische Kultur in der nachatlantischen Periode entwickelt hatten, die entwickelten das Ich subjektiv als ein erkennendes, und dieses subjektive Hinaufheben des Ich auf eine gewisse Höhe innerhalb der menschlichen Seelenkraft kann lange vorhanden sein, ehe der Mensch auch die Fähigkeit erlangt, das Ich objektiv, als Wesenheit, zu schauen.",
      "Dagegen entwickelten die Völker Europas verhältnismäßig außerordentlich früh, noch als sie im alten Hellsehen darinnen steckten, das Anschauen des objektiven Ich, das heißt, sie erschauten innerhalb dessen, was sie hellseherisch überschauten, als ein Wesen unter anderen Wesen auch das Ich. Wenn Sie dies genau auseinanderhalten, so werden Sie auch philosophisch, wie mit allen geisteswissenschaftlichen Dingen, zurechtkommen, wenn Sie es nur richtig machen.",
      "Man könnte es, wenn man gerade seine Freude an philosophischen Formeln hätte, so aus­drücken: Die indische Kultur stellt eine solche Seele dar, welche eine Hochblüte des subjektiven Ich erlangt, lange bevor die Anschauung des objektiven Ich da war. Die germanisch-europäischen Völker entwik­kelten, lange bevor sie sich des eigentlichen inneren Antriebes zum Ich",
      "bewußt wurden, die Anschauung des Ich. Sie sahen hellseherisch das Morgenrot des eigenen Ich, das imaginative Bild des Ich. In der Welt, die sie als eine astralische um sich hatten, sahen sie das Ich objektiv längst unter den anderen Wesen, die sie hellseherisch wahrnahmen. - So müssen wir uns den Gegensatz rein formal vorstellen; dann werden wir auch begreifen, daß gerade der europäische Boden dazu berufen war, das Ich des Menschen in einer solchen Weise, wie ich das in bezug auf die Mythologie gestern hervorhob, in Beziehung zu bringen zu den anderen Wesenheiten, den Engeln und Erzengeln.",
      "Wenn Sie dies ins Auge fassen, so begreifen Sie, daß der europäische Boden dazu bestimmt war, in der verschiedensten Weise dieses Ich auch zu der Welt, die als sinnenfällige Welt vor den Menschensinn trat, in Beziehung zu setzen, und daß das Ich, der eigentliche Wesenskern des Menschen, die verschiedensten Verhältnisse zur Außenwelt eingehen kann. Früher, bevor der Mensch sein Ich schaute, bevor er es wahr-nahm, waren dem Menschen diese Verhältnisse durch die höheren Wesen angewiesen, und er selbst konnte dazu nichts tun.",
      "Es war ein instinktives Verhältnis, in das er zur Außenwelt gesetzt war. Das ist das Wesentliche in der Entwickelung des Ich, daß es immer mehr und mehr selbst in die Hand nimmt, die Verhältnisse des Ich zur Außenwelt zu gestalten.",
      "Im wesentlichen war es die Aufgabe der europäischen Nationen, dieses Verhältnis des Ich zur ganzen Welt in irgendeiner Weise zu gestalten, und die führende Volksseele hatte und hat die Auf­gabe, den europäischen Menschen anzuweisen, sein Ich in Beziehung zur Außenwelt und zu den anderen Menschen und zu der Welt der göttlich-geistigen Wesenheiten zu setzen, so daß man im Grunde ge­nommen erst innerhalb der europäischen Kultur anfing, von dem Ver­hältnisse des Ich-Menschen zum gesamten Universum zu sprechen. Daher der ganz andere Grundton, wenn innerhalb der altindischen Kultur kosmologisch gesprochen wird und wenn innerhalb der euro­päisch-mythologischen Kultur kosmologisch gesprochen wird.",
      "Drüben im Orient ist alles unpersönlich, und vor allen Dingen wird verlangt, unpersönlich zu werden in seinem Erkennen, zu unterdrücken sozu­sagen das Ich, um aufzugehen in Brahma und um in sich selber Atma zu finden. Es ist also da als eine höchste Forderung diejenige der Unpersönlichkeit.",
      "Hier in Europa wird überall mitten hineingestellt in das Menschenleben gerade dieses menschliche Ich, wie es veranlagt ist von Anfang an, und wie es sich nach und nach in der Evolution ausgestaltet. Daher hat man gerade hier in Europa ein ganz besonderes Interesse daran, alles das wirklich im Verhältnis zum Ich zu betrachten, sich alles hellseherisch klarzumachen im Verhältnis zum Ich, was an dieser Ent­wickelung des Ich im Erdendasein einen Anteil hatte.",
      "Nun wissen Sie alle, daß an der Entwickelung des Erdenmenschen, der dazu berufen war, nach und nach zu seinem Ich zu kommen, zwei Kräfte von verschiedenen Seiten her Anteil genommen haben. Seit der lemurischen Zeit prägten sich ein dem Innern des Menschen, in seinen Astralleib, diejenigen Kräfte, die wir die luziferischen Kräfte nennen.",
      "Von diesen Kräften wissen Sie, daß sie vor allen Dingen ihren Angriffs­punkt innerhalb des Menschen dadurch gesucht haben, daß sie sich einschlichen in die menschlichen Begierden, Triebe und Leidenschaften. Dadurch hat sich der Mensch zweierlei errungen: Erstens hat er die Fähigkeit errungen, ein selbständiges, freies Wesen zu werden, in En­thusiasmus zu erglühen für das, was er denkt, fühlt und will, während er sonst für seine eigenen Angelegenheiten von göttlich-geistigen Mäch­ten geführt worden ist.",
      "Aber auf der anderen Seite mußte der Mensch gerade durch die luziferischen Mächte in Kauf nehmen, durch Triebe, Begierden und Leidenschaften in das Böse zu verfallen. Luzifer sitzt also in unserem Erdendasein so, daß er seinen Angriffspunkt im mensch­lichen Innern hat, da, wo das menschliche Astrale spielt.",
      "Da ist auch das Ich, wo sich das Astralische eingegliedert hat, von der luziferischen Macht durchsetzt worden. Sprechen wir also von Luzifer, so sprechen wir von dem, was den Menschen tiefer hinuntergesenkt hat in das mate­rielle, sinnliche Dasein, als er ohne diesen Einfluß gekommen wäre.",
      "So ist ein Bestes im Menschen: die Freiheit, und ein Verfängliches für die Menschennatur: die Möglichkeit des Bösen, den luziferischen Mächten zu verdanken.",
      "Nun wissen wir aber ferner, daß dadurch, daß diese luziferischen Mächte eingegriffen haben in das ganze Gefüge der Menschennatur, später andere Mächte in die Menschennatur hereinkommen konnten, die nicht gekommen wären, wenn Luzifer sich nicht in des Menschen",
      "Organisation hineingesetzt hätte. Der Mensch würde die Welt anders sehen, wenn er nicht unterworfen worden wäre dem Einfluß von Luzi­fer und anderen Wesen, die in dessen Gefolgschaft waren, wenn er nicht noch eine andere Macht an sich hätte herankommen lassen müssen, nachdem er der luziferischen Macht den Zugang möglich gemacht hatte. Ahriman kam von außen heran und schlich sich ein in den großen Umkreis der den Menschen umgebenden Sinnenwelt, so daß also der ahrimanische Einfluß eine Folge des luziferischen Einflusses ist. Der Mensch wird gleichsam von innen ergriffen von Luzifer, und infolge davon wird er ergriffen durch das, was von außen auf ihn wirkt, von Ahrim an.",
      "Die Geisteswissenschaft aller Zeiten, die wirklich die Tatsachen kennt, spricht auch wirklich von luziferischen und von ahrimanischen Mächten. Nun werden Sie es höchst merkwürdig finden, daß in den Anschauungen der verschiedenen Völker, da wo sich diese Anschau­ungen mythologisch ausleben, nicht immer in gleicher Weise ein deut­liches Bewußtsein vorhanden ist von Luzifer auf der einen Seite und Ahriman auf der anderen Seite.",
      "Ein deutliches Bewußtsein davon ist zum Beispiel überall da nicht vorhanden, wo über das Alte Testament herauf, aus der ganzen semitischen Tradition heraus, sich eine religiöse Anschauung bildete. Da hat man nur ein gewisses Bewußtsein von dem luziferischen Einfluß.",
      "Das können Sie schon aus der Erzählung des Alten Testamentes von der Schlange entnehmen, die nichts anderes ist als ein Bild für Luzifer. Daraus können Sie entnehmen, daß ein deut­liches Bewußtsein vorhanden ist davon, daß Luzifer teilgenommen hat an der Entwickelung.",
      "Dieses Bewußtsein ist in allen Traditionen, die verwandt sind mit der Bibel, deutlich vorhanden. Aber das Bewußtsein des ahrimanischen Einflusses ist da nicht in gleicher Weise vorhanden. Nur da ist es vorhanden, wo man geisteswissenschaftlich unterrichtete.",
      "Deshalb haben diejenigen, welche die Evangelien geschrieben haben, dies auch berücksichtigt. Sie finden daher, weil zur Zeit der Evangelien-schreiber das Wort «Dämon» aus dem Griechischen hergenommen ist, daß im Markus-Evangelium da, wo nicht von der Versuchung des Jesus die Rede ist, von einem «Dämon» gesprochen wird.",
      "Da aber, wo von Ahriman die Rede ist, ist das Wort «Satan» gebraucht. Aber wer beach­tet",
      "den wichtigen Unterschied dieser Bezeichnungen im Markus- und im Matthäus-Evangelium? Im Exoterischen beachtet man solche Fein­heiten gar nicht. Bei den äußeren Traditionen ist dieser Unterschied nicht vorhanden.",
      "Bemerkenswert tritt dieser Unterschied hervor in dem Gegensatz zwischen Indertum und Persertum. Da kommt er in einer gewissen Zeit in ganz auffälliger Weise zum Ausdruck. Das Persertum kennt weniger den luziferischen Einfluß; man sah da mehr den ahrimanischen.",
      "Da ist insbesondere der Kampf gegen die Mächte, die uns ein äußeres, falsches Weltbild geben und die uns in Dunkelheit und Finsternis hineinbringen, also dasjenige, was das Verhältnis des Menschen zur Außenwelt angeht. Vorzugsweise als ein Gegner des Guten und Lichtvollen wird Ahriman genannt.",
      "Woher kommt das? Weil in der zweiten nachatlantischen Kul­turperiode das menschliche Anschauungsvermögen sich entwickelte mit Bezug auf die Anschauung der Außenwelt. Bedenken Sie, daß Zoroaster darauf ausgeht, den Sonnengeist, den Geist des Lichtes erkenntlich zu machen.",
      "Er also muß zuerst darauf hinweisen, daß in diese Welt hinein-gemischt ist neben dem Geiste des Lichtes der Geist der Finsternis, der unsere Erkenntnis der äußeren Welt trübt. Der Perser richtet sein Hauptaugenmerk darauf, Ahriman zu besiegen und sich mit den Gei­stern zu verbinden, welche auf diesem Gebiete die großen Mächte, die Lichtvollen sind.",
      "Er ist darauf organisiert, sich auf dem Felde, das nach außen liegt, zu betätigen. Daher hat er seine Ahuras oder Asuras. Dage­gen ist es für den Angehörigen der persischen Religion eine gefährliche Sache, in die Welt hineinzusteigen, die der Mensch durch das Unter-tauchen in das eigene Innere erreichen kann; da, wo die luziferischen Mächte verborgen sind, da läßt er sich auch nicht auf die guten Mächte ein.",
      "Da hat er eine Gefahr gesehen. Er wendet den Blick nach außen und stellt sich den dunklen Asuras gegenüber die Licht-Asuras vor.",
      "Gerade umgekehrt machen es in dieser Zeit die Inder. Die sind in einer Periode, wo sie versuchen, durch Versenkung in das eigene Innere sich zu erheben, um in die höheren Gebiete zu kommen. Sie sehen darin das Heil, sich mit den Kräften zu verbinden, die gefunden werden auf dem Gebiete des inneren Schauens. Daher betrachten sie es als gefähr­lich, in die äußere Welt hineinzuschauen, wo sie mit Ahriman zu",
      "kämpfen hätten. Die äußere Welt fürchten sie, die betrachten sie als gefährlich. Während die Devas dasjenige waren, was der Perser meidet, werden sie für den Inder dasjenige, was er sucht, dasjenige, auf dessen Feld er sich zu betätigen sucht. Der Perser aber geht von diesem Felde hinweg und meidet das Gebiet, wo vor allen Dingen der Kampf gegen Luzifer ausgefochten wird.",
      "Sie können an die verschiedensten Mythologien und Weltanschau­ungen herangehen, und Sie werden nirgends eine so klare und tiefge­hende Anschauung davon finden, daß zweierlei Einflüsse an den Men­schen herantreten, wie in der germanisch-nordischen Mythologie. Da der germanisch-nordische Mensch hellseherisch noch schauen konnte, so sah er diese zwei Mächte wirklich und stellte sich zwischen beide hinein.",
      "Er sagte sich: Der Mensch, wie er sich entwickelt hat, hat heran­kommen sehen gewisse Mächte, die in sein Inneres, in seinen Astralleib hereinfahren. Die wirkten aus der Welt, aber auf den Astralleib ein, und er fühlte, weil er berufen war, das Ich, die Selbständigkeit des Menschen auszubilden, nicht bloß die Möglichkeit des Bösen, er fühlte vor allen Dingen in diesen Mächten, die an den Astralleib herankamen, um ihn zur Freiheit und Selbständigkeit zu bringen, das Freiheitliche; man möchte sagen, das empörerische Element fühlte er in diesen Kräf­ten sich offenbaren.",
      "Das luziferische Element wurde in derjenigen Macht gefühlt, die sogar noch in den germanisch-nordischen Gebieten an der Herstellung der Rassen beteiligt war, insofern sie dem Menschen äußere Gestalt und Farbe gab und ihn zum selbständigen, in der Welt wirkenden Wesen machte. Zunächst fühlte in seiner hellseherischen Anschauung der germanisch-nordische Mensch den Luzifer als das, was den Menschen zu einem freien Menschen macht, der sich nicht bloß an irgendwelche äußeren Mächte hingeben will, sondern der in sich selber den festen Wesenskern hat und aus sich heraus handeln will.",
      "Diesen luziferischen Einfluß empfand der germanisch-nordische Mensch als einen wohltätigen Einfluß.",
      "Nun aber wird er gewahr, daß auch noch anderes von diesem Einfluß herkommt. Luzifer verbirgt sich hinter der Loki-Figur, die eine merk­würdig schillernde Gestalt hat. Weil man die Wirklichkeit sah, so sah man, daß man auf Loki zurückführen kann die Gedanken der Freiheit",
      "und Selbständigkeit des Menschen. Man wußte aber auch durch das alte Hellsehen, daß dasjenige, was den Menschen immer wieder in sei­nen Begierden und Handlungen dazu bringt, in seiner ganzen Wesen­heit niedriger zu stehen, als wenn er nur an Odin und an die Asen hingegeben wäre, daß das auf den Einfluß des Loki zurückzuführen war. Und nun fühle man vor allen Dingen das Schauerlich-Großartige dieser germanisch-nordischen Mythologie. Man fühlte mit zwingender Richtigkeit das, was erst nach und nach durch die Geisteswissenschaft wieder zum Bewußtsein der Menschen kommen wird.",
      "Wie wirkt nun der luziferische Einfluß? Er schließt sich in den astra­lischen Leib ein, wirkt aber dadurch auf alle drei Glieder des Menschen, sowohl auf den Astralleib als auch auf den Äther- und den physischen Leib. Nur Andeutungen kann man heute außerhalb unserer Gesell­schaft über diesen Luzifer-Einfluß machen. Was Sie immer mehr ver­stehen werden, ist, daß der Luzifer-Einfluß sich dreifach geltend macht:",
      "im Astralleibe, im ätherischen und im physischen Leibe des Menschen.",
      "Im Ätherleibe wird hervorgerufen das, was im Menschen als Trieb zur Unwahrhaftigkeit, zur Lüge wird. Lüge und Unwahrhaftigkeit sind etwas, was über das Innere des Menschen hinausgeht. Im Astral­leibe, dem reinen Innern des Menschen, wird das Selbst durchdrungen von dem luziferischen Einfluß, und dieser erscheint dann als Selbst­sucht im Menschen. Der Ätherleib wird von innen heraus mit dem Triebe, unwahrhaftig zu sein, durchsetzt und dadurch zur Möglichkeit der Lüge bestimmt. Im physischen Leib wird hervorgerufen Krankheit und Tod. Für diejenigen, die an meinem letzten Kursus teilgenommen haben, wird das leicht verständlich sein. Aber hier will ich doch noch einmal darauf hinweisen, daß alles, was im menschlichen physischen Leibe als Krankheit und Tod auftritt, karmisch mit dem verknüpft ist, was wir luziferischen Einfluß nennen. Wenn wir alles das noch einmal kurz zusammenfassen, so bewirkt Luzifer im Astralleibe: Selbstsucht, im Ätherleibe: Lüge und Unwahrhaftigkeit, im physischen Leibe:",
      "Krankheit und Tod. Natürlich werden sich alle materialistisch denken­den Menschen der Gegenwart ungeheuer verwundern, daß in der Gei­steswissenschaft Krankheit und Tod auf einen luziferischen Einfluß zurückgeführt werden. Auch das hängt nämlich mit Karma zusammen.",
      "An den Menschen träte niemals Krankheit und Tod heran, wenn nicht der luziferische Einfluß stattgefunden hätte. Das ist eben die karmische Auswirkung des luziferischen Einflusses, daß der Mensch tiefer hin­untersteigt in das Physische, und das wird auf der anderen Seite ausge­glichen durch Krankheit und Tod.",
      "Wir können daher sagen: Indem der luziferische Einfluß hineinkam in den Menschen, wurden der physische, Äther- und Astralleib von Krankheit und Tod, Lüge und Unwahrhaftigkeit und Selbstsucht er­griffen. - Ich möchte noch darauf aufmerksam machen, daß die heutige materialistische Wissenschaft für den Tod im tierischen und im pflanz­lichen Leibe dieselbe Erklärung gibt, wie für den Tod der Menschen. Diese materialistisch denkenden Menschen können nicht begreifen, daß eine äußere Erscheinung ebenso aussehen kann wie eine andere und doch ganz andere Ursachen haben kann.",
      "Das, was äußerer Tatbestand ist, kann aus ganz verschiedenen Grün-den herrühren. So tritt der Tod beim Tiere nicht aus denselben Ursaten ein wie beim Menschen, trotzdem er dieselbe äußere Erscheinung hat. Das sind Dinge, die, wenn man sie erkenntnistheoretisch beweisen wollte, viel zu viel Zeit beanspruchen würden. Im Grunde wollte ich hier nur sagen, daß es mit dem, was die Wissenschaft Kausalität nennt, sehr schief steht. Fehler, die in solchen Unklarheiten wurzeln, werden nämlich fast immer gemacht auf Schritt und Tritt. Denken Sie sich zum Beispiel einmal: Ein Mensch ist aufs Dach hinaufgestiegen, fällt her­unter, hat sich eine todbringende Wunde geschlagen und wird tot auf­gefunden. Was liegt nun näher, als zu sagen: Der Mensch ist herunter­gefallen, hat sich eine todbringende Wunde geschlagen und ist an der Verletzung gestorben.- Es könnte der Fall aber auch ganz anders liegen. Der Mensch könnte ja oben vom Schlage getroffen und tot herunter­gefallen sein; die Verwundung könnte durch den Fall eingetreten sein, so daß der Fall äußerlich gerade so läge wie der vorher geschilderte, der Tod aber aus einer ganz anderen Ursache eingetreten wäre. Der Fall ist hier sehr kraß dargestellt, aber die Wissenschaft macht häufig diese Art Fehler. Die äußeren Tatbestände können oft ganz gleich sein, und doch sind die inneren Ursachen vollständig verschieden.",
      "Das wollen wir also einmal einfach als Ergebnis der geisteswissenschaftlichen",
      "Forschung hingestellt sein lassen, daß der luziferische Ein­fluß im Astralleibe: Selbstsucht, im Ätherleibe: Lüge und Unwahrhaf­tigkeit, im physischen Leibe: Krankheit und Tod bewirkt. Was müßte nun die germanisch-nordische Mythologie gesagt haben, wenn sie dem Loki, dem Luzifer, zugeschrieben hätte, daß dieses dreifache Wirken von ihm herkommen kann?",
      "Sie mußte sagen: Loki hat drei Sprößlinge. Der erste ist der, welcher Selbstsucht bewirkt. Das ist die Midgard­schlange, dasjenige, womit der Einfluß des luziferischen Geistes auf den Astralleib ausgedrückt ist.",
      "Das zweite ist das, was in das menschliche Erkennen sich hineinmischt als das Unrichtige. Beim Menschen auf dem physischen Plane sind es die Dinge, die in seinem Geiste leben und mit der Außenwelt nicht übereinstimmen.",
      "Da ist es das, was nicht wahr ist. Bei den nordischen Menschen, die noch mehr auf dem Astralplane leb­ten, lebte sich das, was bei uns abstrakte Lüge ist, gleich als astralische Wesenheit aus und lebte als solche auf dem astralischen Plan.",
      "Der Aus­druck für alles, was Verfinsterung, nicht richtiges Sehen ist, ist irgend­ein tierisches Wesen, hier im Norden hauptsächlich der Fenriswolf. Das ist das zweite, der Einfluß auf den Ätherleib von seiten des Loki, der bewirkt, daß der Mensch von innen heraus den Trieb hat, sich zu täu­schen, unwahrhaft über die Dinge zu denken, das heißt, es erscheinen ihm die Dinge in der Außenwelt nicht in der richtigen Weise.",
      "Das be­zeichnet also im Grunde genommen die alte germanisch-nordische My­thologie irgendwie mit einer Wolfsgestalt. Das ist die astrale Figur für die Lüge und alles das, was Unwahrhaftigkeit aus innerem Triebe ist.",
      "Aber hier, wo der Mensch in Beziehung zur äußeren Welt tritt, begeg­net sich schon Luzifer mit Ahriman, so daß aller Irrtum, der sich in die Erkenntnis einschleicht - auch in die hellseherische Erkenntnis - alle Illusion und alle Maja, die Folge des Hanges zur Unwahrhaftigkeit ist, der da hineinspielt. In dem Fenriswolf haben wir also die Gestaltung zu sehen, welche der Mensch um sich herum hat dadurch, daß er die Dinge nicht in der wahren Gestalt sieht. Da, wo sich den alten nordi­schen Menschen irgend etwas von äußerem Licht, von der Wahrheit, verdunkelt, da spricht er von einem Wolfe. Das geht durch das ganze nordische Bewußtsein, und Sie werden finden, daß das Bild bis auf die äußeren Tatsachen überall in diesem Sinne gebraucht wird.",
      "Wenn der alte nordische Mensch sich verständlich machen will über das, was er sieht bei einer Sonnenfinsternis - natürlich sah der Mensch zur Zeit des alten Hellsehens noch anders, als heute bei Benutzung des Fernrohres -, so wählte er das Bild des Wolfes, der die Sonne verfolgt und der in dem Momente, wo er sie erreicht, die Sonnenfinsternis be­wirkt. Das steht im innersten Einklang mit den Tatsachen. Diese Ter­minologie gehört mit zu dem Großartigen, ja sogar Schauerlich-Groß-artigen in der nordischen Mythologie. Ich kann hier nur Andeutungen geben. Wenn wir aber selbst wochenlang über die nordische Mythologie sprechen könnten, so würden Sie sehen, wie das allseitig durchgeführt ist im nordischen mythologischen Vorstellen. Das ist deshalb der Fall, weil die Mythologie ein Ergebnis des alten Hellsehertums ist, in das aber das Ich überall hineinspielt.",
      "Die materialistischen Menschen von heute werden sagen: Das ist aber doch Aberglaube. Es verfolgt doch kein Wolf die Sonne. Der alte nor­dische, imaginative Mensch sieht eben in Bildern diese Tatsachen, und ich könnte Ihnen vielleicht viele sogenannte wissenschaftliche Wahr­heiten aufzählen, die mehr Einfluß von Ahriman, die größeren Irrtum bergen, als vorhanden ist, wenn man die entsprechende astralische An­schauung beschreibt und sagt: Der Wolf verfolgt die Sonne. - Für den Okkultisten gibt es etwas, was noch in höherem Grad Aberglaube ist. Das ist, daß eine Sonnenfinsternis dadurch entsteht, daß sich der Mond vor die Sonne stellt. Das ist für die äußere Anschauung ganz richtig, ebenso richtig, wie für die astrale Anschauung die Sache vom Wolf richtig ist. Die astrale Anschauung ist sogar richtiger als die, welche Sie in den gegenwärtigen Büchern finden, denn die ist noch mehr dem Irrtum unterworfen. Wenn der Mensch einst an Stelle dieses Äußeren den wahren Tatbestand erkennen wird, dann wird er finden, daß der nordische Mythos recht hat. Ich weiß, daß ich für die heutige Anschau­ung etwas gräßlich Absurdes sage, aber ich weiß auch, daß man an theosophischen Stätten schon so weit ist, daß man darauf hindeuten darf, wo gerade unsere physische Weltanschauung am meisten beein­flußt ist von Maja, Täuschung oder Illusion.",
      "Nun kommen wir zum Einfluß von Loki auf den physischen Leib. In dem bewirkt er Krankheit und Tod. Der dritte Sprößling ist also das,",
      "was Krankheit und Tod bewirkt. Das ist die Hel. So haben Sie in der Tat in wunderbarer Weise in den Gestalten Hel, Fenriswolf und Mid­gardschlange den Einfluß des Loki oder Luzifer dargestellt, in der Form, wie ihn das alte Hellsehen, das wir in gewisser Beziehung als traumhaftes Hellsehen bezeichnen können, wahrgenommen hat. Wenn wir die ganze Geschichte von Loki durchgingen, überall würden wir finden, daß diese Dinge bis in die Einzelheiten hinein die Sache voll­ständig beleuchten.",
      "Dabei müssen wir uns immer klar sein, daß das, was der Hellseher sieht, nicht etwa eine allegorisch-symbolische Bezeichnung ist, sondern daß das Wesenheiten sind. Er sieht Wesenheiten. Nun hat aber der ger­manisch-nordische Mensch nicht bloß gewußt von seinem Loki, von dem luziferischen Einfluß, sondern auch von dem Einfluß des Ahriman, der von der anderen Seite her kam, und er hat mehr gewußt, nämlich daß das Befallensein von dem ahrimanischen Einfluß eine Folge des Loki-Einflusses ist. Sie müssen sich jetzt in die Zeit versetzen, wo der Mensch noch nicht in äußerer, physischer Anschauung die Welt ansah, sondern sie mit dem alten Hellsehen betrachtete, und da werden Sie finden, daß der betreffende Mythos für dieses Hellsehen ausgebildet ist. Was sagt der Mythos? Lokis Einfluß ist über die Menschen gekommen, was sich ausdrückt in dem Wirken der Midgardschlange, des Fenris­wolfes und der Hel. Der Mensch ist so geworden, daß seine Anschauung sein klares, lichtvolles Hineinschauen in die geistige Welt getrübt wurde dadurch, daß der luziferische Einfluß sich immer mehr geltend machte. Der Mensch wechselte in seinem Leben ab in der damaligen Zeit, als",
      "diese Anschauung sich ausbildete, zwischen dem Sehen in der geistigen Welt und dem Leben auf dem physischen Plan, wie man im Leben ab-wechselt zwischen Wachen und Schlafen. Wenn er in die geistige Welt hineinsah, sah er in die Welt, aus der er herausgeboren war. Das ist ja das Wesentliche, daß der Mythos aus dem hellseherischen Bewußtsein heraus entstanden ist. Das menschliche Bewußtsein aber bestand in diesem abwechselnden Hineinschauen und Nichthineinschauen in die geistige Welt. War der Zustand des Traumbewußtseins da, so sah man hinein in die geistige Welt; war der Zustand des Tagwachens da, so war man blind für sie. So wechselte der Zustand zwischen Blindheit und Hineinsehen in die geistige Welt. Es wechselte das Bewußtsein ab, wie ein gewisses Weltenwesen wechselte zwischen dem blinden Hödur und dem in die geistige Welt hinein schauenden, hellsichtigen Baldur.",
      "Es war der Mensch veranlagt für Baldurs Einfluß, und im Sinne die­ses Einflusses wäre der Mensch geworden, wenn er nicht den Loki-Ein-fluß aufgenommen hätte. Der aber hat bewirkt, daß Hödurs Natur den Sieg über die Baldurnatur davongetragen hat. Das wird ausgedrückt dadurch, daß Loki die Mistel herbeischafft, mit der der blinde Hödur den sehenden Baldur tötet.",
      "Loki ist also die tötende Macht, wie Luzifer, der den Menschen zu Ahriman getrieben hat. Indem der Mensch hingegeben ist an den blin­den Hödur, verlöscht das alte hellsichtige Anschauen. Das ist die Tö­tung des Baldur. Das empfindet der nordische Mensch, daß nach und nach wirklich verloren gegangen ist das Baldurhafte, das Hineinschauen in die geistige Welt. Es hat der nordische Mensch das Hinschwinden des Hellsehens so empfunden, daß ihm Loki in Baldur die Hellsichtig­keit getötet hat, und was ihm geblieben, ist die Ohnmacht gegenüber dieser Hellsichtigkeit. So ist ein größtes welthistorisches Ereignis, das allmähliche Hinschwinden der alten ungetrübten Erkenntnis, ausge­drückt in dem Baldur-, Hödur- und Loki-Mythos. Auf der einen Seite haben wir also den Loki mit seiner Sippe, den drei Wesenheiten, und auf der anderen Seite den tragischen Akt von der Tötung des Baldur.",
      "So haben wir in der nordischen Mythologie gespiegelt das, was wir aus der Geisteswissenschaft herausholen können: den zweifachen Ein­fluß, den luziferischen und den ahrimanischen. Das ist dasjenige, was",
      "Ihnen die Geisteswissenschaft immer als eine Darstellung des hellsehe­rischen Erkennens der alten Zeit darlegen wird und als ein Heraus-arbeiten des Mythos aus dem alten Hellsehen, das dann zugleich nach und nach dahinschwindet.",
      "Es würde zu weit führen, wollten wir uns auf dieses Gebiet noch weiter einlassen. Aber schon indem ich Ihnen das Prinzipielle gesagt habe, können Sie das Schaurig-Großartige empfinden in diesem My­thos, der nicht seinesgleichen hat, weil keine Mythologie sich so genau an den alten, hellseherischen Tatbestand angepaßt hat. Die griechische Mythologie ist nur die Erinnerung an etwas in der Vorzeit Erlebtes, das in plastischer Weise zum Ausdrucke kommt. Aber eine solche unmittel­bare Anknüpfung an die Tatsachen, wie sie in der germanisch-nordi­schen Mythologie vorliegt, das ist in der griechischen Mythologie nicht vorhanden. Dieselbe ist abgeklärter, die Gestalten erscheinen mit viel gerundeteren Konturen, daher in stark plastischer Weise, haben aber das Elementare des allerursprünglichsten Eindrucks verloren. Etwas vom alten Hellsehen ist dem nordischen Menschen lange geblieben. Dahingeschwunden war das alte Hellsehen der Menschen im übrigen Europa schon lange, als es sich noch im Norden lange bewahrt hat. Nur nach und nach, langsam und allmählich ist in das Blickfeld des Men­schen das physische Weltbild allein getreten. So war auch, als das Chri­stentum anfing sich auszubreiten, für die Mehrzahl der Menschen wahr geworden, was sich in der Baldur-Mythe, in dem Tod des Baldur aus­drückt. Es gab aber noch einzelne, die in unmittelbarer Anschauung haben konnten, was die nordischen Menschen hellseherisch erlebten.",
      "Es war also noch lange ein unmittelbares Anschauen von dieser gei­stigen Welt vorhanden, und weil das alles so elementar war, so unmit­telbar aus der hellseherischen Erfahrung heraus, deshalb blieb auch, als das Christentum schon anfing sich auszubreiten, das Bewußtsein vor­handen, das bei anderen Völkern nicht so stark sein konnte wie bei den alten germanisch-nordischen Menschen. Sie empfanden dann: Es schwindet alles dahin, was wir damals erlebt haben im Zusammenhang mit der göttlich-geistigen Urheimat. Es schwand dem Norden erst dahin, als der germanisch-nordische Mensch den Trost des Christen­tums empfing. Das enthielt für ihn aber nicht unmittelbare Anschauung.",
      "Er hatte das Schicksal des Baldur viel zu tief gefühlt, als daß er sich hätte trösten können damit, daß ihm ein Gott geboten wurde, der zum physischen Plan heruntergestiegen ist, damit die Menschen, die nur den physischen Plan wahrnehmen können, auch zum Gottesbe­wußtsein aufzusteigen vermögen. So wie die Menschen in Vorderasien ha­ben fühlen können die Worte: «Ändert eure Seelenverfassung, denn das Himmelreich ist nahe herbeigekommen», konnte man das in den nordi­schen Gebieten nicht.",
      "Drüben, wo Christus erschienen war, da konnte man nur alte Erinnerungen an die Tatsache finden, daß es ein altes Hellsehen einst gegeben hat. Dreitausend Jahre schon währte im Osten das Kali Yuga, das finstere Zeitalter, wo die Menschen nicht mehr hineinschauen konnten in die geistige Welt.",
      "Aber gesehnt haben sie sich immer nach der geistigen Welt, und immer haben sie erzählt von einer solchen Welt, in die der Mensch geistig hineinschauen konnte, die aber jetzt den Blicken entschwunden ist. Sie haben die geistige Welt in viel fernerer Vergangenheit erlebt, als die Menschen des nordischen Gebie­tes und haben es nur noch aus der Erinnerung gewußt, daß die geistige Welt einmal zugänglich gewesen ist.",
      "Daher konnte man in den vorder-asiatischen Gebieten das Wort: «Ändert eure Seelenverfassung, denn das Himmelreich ist nahe herbeigekommen» gut verstehen. Man ver­stand es, wenn gesagt wurde: Die Reiche der Himmel sind herbeige­kommen bis in den physischen Plan, seht also hin auf die einzigartige Gestalt, die da im Gebiete des palästinensischen Reiches erscheinen wird, seht auf den Messias, der den Gott in sich enthält, durch den ihr den Zusammenhang mit dem Göttlichen finden werdet, auch wenn ihr euch nicht von dem physischen Plan erheben könnt.",
      "Versteht die Ge­stalt von Palästina, versteht die Christus-Gestalt. - Das ist das tiefe Wort Johannes des Täufers.",
      "Das mußte der nordische Mensch anders empfinden, der noch länger viel mehr erlebt hatte als nur die erinnerungsgemäße Kunde von dem Hineinschauen in die göttlich-geistige Welt. Daher ging ihm ein Ge­danke auf von einer ungeheuern, ganz gewaltigen Tragweite, der Ge­danke: Dieses Heraustreten auf den physischen Plan, in die physische Welt, das Nichtsehen der göttlich-geistigen Welt, das kann nur eine Zwischenzeit sein. Der Mensch wird das als Schule durchzumachen",
      "haben und sehen müssen, was er sich aneignen kann in der physischen Welt. Er braucht diesen Durchgang, er muß also heraustreten aus der geistigen Welt; er muß die Erlebnisse der physischen Welt als Schule durchmachen. Aber gerade dadurch, daß er sie als Schule durchmacht, wird er wieder hineinkommen in die Welt, aus der er herausgetreten ist. Der Baldurblick wird ihn wieder beseelen können. - Mit anderen Worten: Die große Idee, die im Laufe der germanisch-nordischen Ent­wickelung entsteht, daß die Welt wieder sichtbar werden wird, die geschwunden ist und dem hellseherischen Blick entzogen wurde, be­wirkte, daß als Zwischenzeit empfunden wurde das Walten auf dem physischen Plan.",
      "Seine Eingeweihten machten es dem nordischen Menschen begreif­lich, daß in der göttlich-geistigen Welt in dieser Zwischenzeit, während er nicht in dieselbe hineinschauen kann, etwas vorgeht, durch das diese göttlich-geistige Welt einst anders ausschauen wird, als er früher ge­wohnt war, sie zu sehen. Sie machten ihm das begreiflich, in dem sie zu ihm ungefähr so sprachen: Du hast früher in die göttlich-geistige Welt hineingesehen, hast darin den Erzengel der Sprache, den Erzengel der Runen, den Erzengel des Atems, Odin, gesehen und den Engel der Ich­heit, den Thor. Du standest mit ihnen in Verbindung, und es wird der­jenige, der dazu vorbereitet ist, die Möglichkeit erwerben, wieder in diese geistige Welt hineinzukommen. Dann wird sie aber anders aus­sehen; andere Mächte werden hinzugetreten sein und die Machtbereiche und Machtverhältnisse dieser alten geistigen Führer des Menschenge­schlechts werden sich verändert haben. Du wirst dann zwar in diese Welt hineinsehen, aber du wirst anderes sehen, als was du bisher erlebt hast.",
      "Dasjenige, was der Mensch dann sehen wird, malten sie ihm als eine Zukunftsvision aus, als jene Zukunftsvision, die einmal vor die mensch­liche Seele treten wird, wenn der Mensch wieder hineinsehen kann in die geistige Welt und sehen wird, welches Schicksal die alten Göttergestalten gehabt haben, sehen wird, wie sie mit anderen Mächten in Beziehung traten. Diese Zukunftsvision, wie sie die Eingeweihten geschaut haben, malten sie ihm aus, wo in der Tat dasjenige, was von Luzifer kommt, in gewisser Weise in Kampf getreten sein wird mit dem, was von den",
      "Göttern kommt, und sich auch ausleben wird. Diese Zukunftsvision malten die Eingeweihten den Menschen in dem Bilde von der Götter­dämmerung aus. Die Götterdämmerung, Ragnarök, ist also das Bild, das die Eingeweihten dem germanisch-nordischen Menschen als Zu­kunftsbild vor Augen stellten. Und wieder werden wir finden, daß alle Vorgänge, die da als Zukunftsvorgänge dargestellt werden, bis in die Einzelheiten hinein nicht besser, nicht terminologisch richtiger und nicht treffender dargestellt werden könnten, als sie dargestellt worden sind in dem wunderbaren Bilde der Götterdämmerung. Das ist der ok­kulte Hintergrund des Bildes von der Götterdämmerung.",
      "Als was soll sich dann der Mensch sehen? Er soll sich sehen so, daß er alles dasjenige als Entwickelungsursache aufgenommen hat, was aus früheren Zeiten stammt; er soll denkend aufnehmen, was er als Gabe Odins bekommen hat, sich selber aber fühlen als durch die Entwicke­lung durchgegangen, die dann gefolgt ist. Er soll die Lehren, die Odin in ihn verpflanzt hat, in sich aufnehmen - Odin tritt ihm entgegen als Erzengel. Er soll sich zum Sohne des Odin machen; er soll in den Kampf eintreten, und zwar bald in diesen Kampf eintreten. Das macht der Eingeweihte, der Leiter der esoterischen Schule, besonders dem nordi­schen Menschen klar, indem er auf das göttlich-geistige Wesen hinweist, das uns so geheimnisvoll erscheint, das eigentlich erst bei der Götter­dämmerung eine bestimmte Rolle bekommt, weil es selbst diejenige Macht überwindet, durch die zuerst Odin überwunden wird. Der Rä­cher des Odin bekommt eine besondere Rolle und spielt sie in der Göt­terdämmerung. Wenn wir diese Rolle verstehen werden, so wird sich uns der wunderbare Zusammenhang ergeben zwischen den Anlagen des germanisch-nordischen Menschen und dem, was wir uns vorstellen können als die Vision der Zukunft. In wunderbarer Weise, bis in die Einzelheiten genau, ist das alles in der großen Vision von der Götter­dämmerung zum Ausdruck gekommen."
    ],
    "sentences": [
      [
        "Wenn unter Ihnen Zuhörer sind, die den Vortrag von gestern philo­sophisch analysieren wollten, so könnten Sie vielleicht Schwierigkeiten, scheinbare Schwierigkeiten haben, und zwar aus dem Grunde, weil Sie ja aus früheren Darstellungen, die über ähnliche Themen gegeben wor­den sind, gehört haben, daß unser gesamter nachatlantischer Zeitraum und eigentlich schon die letzten Zeiten der atlantischen Entwickelung dazu da waren, das menschliche Ich als solches nach und nach zu ent­wickeln, immer mehr und mehr zur Bewußtheit zu bringen.",
        "Im Zusam­menhang damit wurde gesagt, daß gewissermaßen die Angehörigen der alten indischen Kultur die allerersten waren, welche, nachdem sie in der alten Atlantis noch durch das in der Menschheit sich findende alte Hellsehen den Einblick in eine geistige Welt hatten, unmittelbar aus diesem Hellsehen heraus in die physische Welt versetzt waren."
      ],
      [
        "Sie sahen diese physische Welt so, daß nun die Stimmung über die ganze erste nachatlantische Kulturperiode kam: Dasjenige ist die wahre Wirklich­keit, was hinter uns liegt in der geistigen Welt darinnen.",
        "Draußen aber in der Welt ist Maja oder Illusion."
      ],
      [
        "Nun wurde gestern auseinander­gesetzt - wie es auch den Tatsachen entspricht -, daß die Angehörigen dieser alten indischen Kultur gewissermaßen eine reiche Seelenentwik­kelung durchgemacht hatten, und es wurde gesagt, daß sie sie erlangt hatten mehr oder weniger bei schlafendem Ich, das heißt, daß das Ich erst erwacht ist, nachdem diese reife Seelenentwickelung schon erreicht war."
      ],
      [
        "Sie könnten sich jetzt vielleicht fragen: Was hat es denn eigentlich für diese indische Bevölkerung in der Zwischenzeit gegeben?",
        "Da muß ja sozusagen die indische Bevölkerung in einer ganz anderen Weise diese ganze Seelenentwickelung durchgemacht haben, als die europä­ische, namentlich die germanische Bevölkerung, die mit dem Ich dabei war, während sich die Fähigkeiten nach und nach entwickelten, die zugesehen hat, wie die göttlich-geistigen Mächte in ihre Seele herein-gewirkt haben.",
        "Das könnten Sie vielleicht schwer in Einklang bringen"
      ],
      [
        "mit dem Gesagten, wenn Sie über den gestrigen Vortrag philosophisch denken wollten.",
        "Nur für diejenigen, die nicht aus völliger Unbefangen­heit, sondern aus einem solchen philosophischen Denken heraus den Vortrag analysieren wollen. muß ich noch etwas in Paranthese zur Aufklärung sagen."
      ],
      [
        "Sie werden den scheinbaren Widerspruch sofort auflösen, wenn Sie wie folgt zu Werke gehen, wenn Sie sich sagen: In bezug auf das Ich und seine Erkennbarkeit ist der Mensch in einer ganz anderen Lage als in bezug auf ein jegliches anderes Objekt.",
        "Wenn Sie irgendein anderes Objekt erkennen, einen anderen Gegenstand oder ein anderes Wesen als das Ich, dann haben Sie es eigentlich in der Erkenntnistätigkeit immer mit zweierlei zu tun: mit dem Erkenner, der Erkenntniskraft, und mit dem, was erkannt wird."
      ],
      [
        "Ob das, was erkannt wird, Mensch, Tier, Baum oder Stein ist, darauf kommt es nicht an für den rein formalen Erkennt­nisakt.",
        "Anders steht die Sache aber in bezug auf das Ich.",
        "Da ist das­jenige, was erkennt, und das, was erkannt wird, ein und dasselbe."
      ],
      [
        "Das Bedeutungsvolle ist, daß in der menschlichen Evolution, der mensch­lichen Entwickelung, diese zwei Dinge auseinanderfallen.",
        "Diejenigen, die die reife indische Kultur in der nachatlantischen Periode entwickelt hatten, die entwickelten das Ich subjektiv als ein erkennendes, und dieses subjektive Hinaufheben des Ich auf eine gewisse Höhe innerhalb der menschlichen Seelenkraft kann lange vorhanden sein, ehe der Mensch auch die Fähigkeit erlangt, das Ich objektiv, als Wesenheit, zu schauen."
      ],
      [
        "Dagegen entwickelten die Völker Europas verhältnismäßig außerordentlich früh, noch als sie im alten Hellsehen darinnen steckten, das Anschauen des objektiven Ich, das heißt, sie erschauten innerhalb dessen, was sie hellseherisch überschauten, als ein Wesen unter anderen Wesen auch das Ich.",
        "Wenn Sie dies genau auseinanderhalten, so werden Sie auch philosophisch, wie mit allen geisteswissenschaftlichen Dingen, zurechtkommen, wenn Sie es nur richtig machen."
      ],
      [
        "Man könnte es, wenn man gerade seine Freude an philosophischen Formeln hätte, so aus­drücken: Die indische Kultur stellt eine solche Seele dar, welche eine Hochblüte des subjektiven Ich erlangt, lange bevor die Anschauung des objektiven Ich da war.",
        "Die germanisch-europäischen Völker entwik­kelten, lange bevor sie sich des eigentlichen inneren Antriebes zum Ich"
      ],
      [
        "bewußt wurden, die Anschauung des Ich.",
        "Sie sahen hellseherisch das Morgenrot des eigenen Ich, das imaginative Bild des Ich.",
        "In der Welt, die sie als eine astralische um sich hatten, sahen sie das Ich objektiv längst unter den anderen Wesen, die sie hellseherisch wahrnahmen. - So müssen wir uns den Gegensatz rein formal vorstellen; dann werden wir auch begreifen, daß gerade der europäische Boden dazu berufen war, das Ich des Menschen in einer solchen Weise, wie ich das in bezug auf die Mythologie gestern hervorhob, in Beziehung zu bringen zu den anderen Wesenheiten, den Engeln und Erzengeln."
      ],
      [
        "Wenn Sie dies ins Auge fassen, so begreifen Sie, daß der europäische Boden dazu bestimmt war, in der verschiedensten Weise dieses Ich auch zu der Welt, die als sinnenfällige Welt vor den Menschensinn trat, in Beziehung zu setzen, und daß das Ich, der eigentliche Wesenskern des Menschen, die verschiedensten Verhältnisse zur Außenwelt eingehen kann.",
        "Früher, bevor der Mensch sein Ich schaute, bevor er es wahr-nahm, waren dem Menschen diese Verhältnisse durch die höheren Wesen angewiesen, und er selbst konnte dazu nichts tun."
      ],
      [
        "Es war ein instinktives Verhältnis, in das er zur Außenwelt gesetzt war.",
        "Das ist das Wesentliche in der Entwickelung des Ich, daß es immer mehr und mehr selbst in die Hand nimmt, die Verhältnisse des Ich zur Außenwelt zu gestalten."
      ],
      [
        "Im wesentlichen war es die Aufgabe der europäischen Nationen, dieses Verhältnis des Ich zur ganzen Welt in irgendeiner Weise zu gestalten, und die führende Volksseele hatte und hat die Auf­gabe, den europäischen Menschen anzuweisen, sein Ich in Beziehung zur Außenwelt und zu den anderen Menschen und zu der Welt der göttlich-geistigen Wesenheiten zu setzen, so daß man im Grunde ge­nommen erst innerhalb der europäischen Kultur anfing, von dem Ver­hältnisse des Ich-Menschen zum gesamten Universum zu sprechen.",
        "Daher der ganz andere Grundton, wenn innerhalb der altindischen Kultur kosmologisch gesprochen wird und wenn innerhalb der euro­päisch-mythologischen Kultur kosmologisch gesprochen wird."
      ],
      [
        "Drüben im Orient ist alles unpersönlich, und vor allen Dingen wird verlangt, unpersönlich zu werden in seinem Erkennen, zu unterdrücken sozu­sagen das Ich, um aufzugehen in Brahma und um in sich selber Atma zu finden.",
        "Es ist also da als eine höchste Forderung diejenige der Unpersönlichkeit."
      ],
      [
        "Hier in Europa wird überall mitten hineingestellt in das Menschenleben gerade dieses menschliche Ich, wie es veranlagt ist von Anfang an, und wie es sich nach und nach in der Evolution ausgestaltet.",
        "Daher hat man gerade hier in Europa ein ganz besonderes Interesse daran, alles das wirklich im Verhältnis zum Ich zu betrachten, sich alles hellseherisch klarzumachen im Verhältnis zum Ich, was an dieser Ent­wickelung des Ich im Erdendasein einen Anteil hatte."
      ],
      [
        "Nun wissen Sie alle, daß an der Entwickelung des Erdenmenschen, der dazu berufen war, nach und nach zu seinem Ich zu kommen, zwei Kräfte von verschiedenen Seiten her Anteil genommen haben.",
        "Seit der lemurischen Zeit prägten sich ein dem Innern des Menschen, in seinen Astralleib, diejenigen Kräfte, die wir die luziferischen Kräfte nennen."
      ],
      [
        "Von diesen Kräften wissen Sie, daß sie vor allen Dingen ihren Angriffs­punkt innerhalb des Menschen dadurch gesucht haben, daß sie sich einschlichen in die menschlichen Begierden, Triebe und Leidenschaften.",
        "Dadurch hat sich der Mensch zweierlei errungen: Erstens hat er die Fähigkeit errungen, ein selbständiges, freies Wesen zu werden, in En­thusiasmus zu erglühen für das, was er denkt, fühlt und will, während er sonst für seine eigenen Angelegenheiten von göttlich-geistigen Mäch­ten geführt worden ist."
      ],
      [
        "Aber auf der anderen Seite mußte der Mensch gerade durch die luziferischen Mächte in Kauf nehmen, durch Triebe, Begierden und Leidenschaften in das Böse zu verfallen.",
        "Luzifer sitzt also in unserem Erdendasein so, daß er seinen Angriffspunkt im mensch­lichen Innern hat, da, wo das menschliche Astrale spielt."
      ],
      [
        "Da ist auch das Ich, wo sich das Astralische eingegliedert hat, von der luziferischen Macht durchsetzt worden.",
        "Sprechen wir also von Luzifer, so sprechen wir von dem, was den Menschen tiefer hinuntergesenkt hat in das mate­rielle, sinnliche Dasein, als er ohne diesen Einfluß gekommen wäre."
      ],
      [
        "So ist ein Bestes im Menschen: die Freiheit, und ein Verfängliches für die Menschennatur: die Möglichkeit des Bösen, den luziferischen Mächten zu verdanken."
      ],
      [
        "Nun wissen wir aber ferner, daß dadurch, daß diese luziferischen Mächte eingegriffen haben in das ganze Gefüge der Menschennatur, später andere Mächte in die Menschennatur hereinkommen konnten, die nicht gekommen wären, wenn Luzifer sich nicht in des Menschen"
      ],
      [
        "Organisation hineingesetzt hätte.",
        "Der Mensch würde die Welt anders sehen, wenn er nicht unterworfen worden wäre dem Einfluß von Luzi­fer und anderen Wesen, die in dessen Gefolgschaft waren, wenn er nicht noch eine andere Macht an sich hätte herankommen lassen müssen, nachdem er der luziferischen Macht den Zugang möglich gemacht hatte.",
        "Ahriman kam von außen heran und schlich sich ein in den großen Umkreis der den Menschen umgebenden Sinnenwelt, so daß also der ahrimanische Einfluß eine Folge des luziferischen Einflusses ist.",
        "Der Mensch wird gleichsam von innen ergriffen von Luzifer, und infolge davon wird er ergriffen durch das, was von außen auf ihn wirkt, von Ahrim an."
      ],
      [
        "Die Geisteswissenschaft aller Zeiten, die wirklich die Tatsachen kennt, spricht auch wirklich von luziferischen und von ahrimanischen Mächten.",
        "Nun werden Sie es höchst merkwürdig finden, daß in den Anschauungen der verschiedenen Völker, da wo sich diese Anschau­ungen mythologisch ausleben, nicht immer in gleicher Weise ein deut­liches Bewußtsein vorhanden ist von Luzifer auf der einen Seite und Ahriman auf der anderen Seite."
      ],
      [
        "Ein deutliches Bewußtsein davon ist zum Beispiel überall da nicht vorhanden, wo über das Alte Testament herauf, aus der ganzen semitischen Tradition heraus, sich eine religiöse Anschauung bildete.",
        "Da hat man nur ein gewisses Bewußtsein von dem luziferischen Einfluß."
      ],
      [
        "Das können Sie schon aus der Erzählung des Alten Testamentes von der Schlange entnehmen, die nichts anderes ist als ein Bild für Luzifer.",
        "Daraus können Sie entnehmen, daß ein deut­liches Bewußtsein vorhanden ist davon, daß Luzifer teilgenommen hat an der Entwickelung."
      ],
      [
        "Dieses Bewußtsein ist in allen Traditionen, die verwandt sind mit der Bibel, deutlich vorhanden.",
        "Aber das Bewußtsein des ahrimanischen Einflusses ist da nicht in gleicher Weise vorhanden.",
        "Nur da ist es vorhanden, wo man geisteswissenschaftlich unterrichtete."
      ],
      [
        "Deshalb haben diejenigen, welche die Evangelien geschrieben haben, dies auch berücksichtigt.",
        "Sie finden daher, weil zur Zeit der Evangelien-schreiber das Wort «Dämon» aus dem Griechischen hergenommen ist, daß im Markus-Evangelium da, wo nicht von der Versuchung des Jesus die Rede ist, von einem «Dämon» gesprochen wird."
      ],
      [
        "Da aber, wo von Ahriman die Rede ist, ist das Wort «Satan» gebraucht.",
        "Aber wer beach­tet"
      ],
      [
        "den wichtigen Unterschied dieser Bezeichnungen im Markus- und im Matthäus-Evangelium?",
        "Im Exoterischen beachtet man solche Fein­heiten gar nicht.",
        "Bei den äußeren Traditionen ist dieser Unterschied nicht vorhanden."
      ],
      [
        "Bemerkenswert tritt dieser Unterschied hervor in dem Gegensatz zwischen Indertum und Persertum.",
        "Da kommt er in einer gewissen Zeit in ganz auffälliger Weise zum Ausdruck.",
        "Das Persertum kennt weniger den luziferischen Einfluß; man sah da mehr den ahrimanischen."
      ],
      [
        "Da ist insbesondere der Kampf gegen die Mächte, die uns ein äußeres, falsches Weltbild geben und die uns in Dunkelheit und Finsternis hineinbringen, also dasjenige, was das Verhältnis des Menschen zur Außenwelt angeht.",
        "Vorzugsweise als ein Gegner des Guten und Lichtvollen wird Ahriman genannt."
      ],
      [
        "Woher kommt das?",
        "Weil in der zweiten nachatlantischen Kul­turperiode das menschliche Anschauungsvermögen sich entwickelte mit Bezug auf die Anschauung der Außenwelt.",
        "Bedenken Sie, daß Zoroaster darauf ausgeht, den Sonnengeist, den Geist des Lichtes erkenntlich zu machen."
      ],
      [
        "Er also muß zuerst darauf hinweisen, daß in diese Welt hinein-gemischt ist neben dem Geiste des Lichtes der Geist der Finsternis, der unsere Erkenntnis der äußeren Welt trübt.",
        "Der Perser richtet sein Hauptaugenmerk darauf, Ahriman zu besiegen und sich mit den Gei­stern zu verbinden, welche auf diesem Gebiete die großen Mächte, die Lichtvollen sind."
      ],
      [
        "Er ist darauf organisiert, sich auf dem Felde, das nach außen liegt, zu betätigen.",
        "Daher hat er seine Ahuras oder Asuras.",
        "Dage­gen ist es für den Angehörigen der persischen Religion eine gefährliche Sache, in die Welt hineinzusteigen, die der Mensch durch das Unter-tauchen in das eigene Innere erreichen kann; da, wo die luziferischen Mächte verborgen sind, da läßt er sich auch nicht auf die guten Mächte ein."
      ],
      [
        "Da hat er eine Gefahr gesehen.",
        "Er wendet den Blick nach außen und stellt sich den dunklen Asuras gegenüber die Licht-Asuras vor."
      ],
      [
        "Gerade umgekehrt machen es in dieser Zeit die Inder.",
        "Die sind in einer Periode, wo sie versuchen, durch Versenkung in das eigene Innere sich zu erheben, um in die höheren Gebiete zu kommen.",
        "Sie sehen darin das Heil, sich mit den Kräften zu verbinden, die gefunden werden auf dem Gebiete des inneren Schauens.",
        "Daher betrachten sie es als gefähr­lich, in die äußere Welt hineinzuschauen, wo sie mit Ahriman zu"
      ],
      [
        "kämpfen hätten.",
        "Die äußere Welt fürchten sie, die betrachten sie als gefährlich.",
        "Während die Devas dasjenige waren, was der Perser meidet, werden sie für den Inder dasjenige, was er sucht, dasjenige, auf dessen Feld er sich zu betätigen sucht.",
        "Der Perser aber geht von diesem Felde hinweg und meidet das Gebiet, wo vor allen Dingen der Kampf gegen Luzifer ausgefochten wird."
      ],
      [
        "Sie können an die verschiedensten Mythologien und Weltanschau­ungen herangehen, und Sie werden nirgends eine so klare und tiefge­hende Anschauung davon finden, daß zweierlei Einflüsse an den Men­schen herantreten, wie in der germanisch-nordischen Mythologie.",
        "Da der germanisch-nordische Mensch hellseherisch noch schauen konnte, so sah er diese zwei Mächte wirklich und stellte sich zwischen beide hinein."
      ],
      [
        "Er sagte sich: Der Mensch, wie er sich entwickelt hat, hat heran­kommen sehen gewisse Mächte, die in sein Inneres, in seinen Astralleib hereinfahren.",
        "Die wirkten aus der Welt, aber auf den Astralleib ein, und er fühlte, weil er berufen war, das Ich, die Selbständigkeit des Menschen auszubilden, nicht bloß die Möglichkeit des Bösen, er fühlte vor allen Dingen in diesen Mächten, die an den Astralleib herankamen, um ihn zur Freiheit und Selbständigkeit zu bringen, das Freiheitliche; man möchte sagen, das empörerische Element fühlte er in diesen Kräf­ten sich offenbaren."
      ],
      [
        "Das luziferische Element wurde in derjenigen Macht gefühlt, die sogar noch in den germanisch-nordischen Gebieten an der Herstellung der Rassen beteiligt war, insofern sie dem Menschen äußere Gestalt und Farbe gab und ihn zum selbständigen, in der Welt wirkenden Wesen machte.",
        "Zunächst fühlte in seiner hellseherischen Anschauung der germanisch-nordische Mensch den Luzifer als das, was den Menschen zu einem freien Menschen macht, der sich nicht bloß an irgendwelche äußeren Mächte hingeben will, sondern der in sich selber den festen Wesenskern hat und aus sich heraus handeln will."
      ],
      [
        "Diesen luziferischen Einfluß empfand der germanisch-nordische Mensch als einen wohltätigen Einfluß."
      ],
      [
        "Nun aber wird er gewahr, daß auch noch anderes von diesem Einfluß herkommt.",
        "Luzifer verbirgt sich hinter der Loki-Figur, die eine merk­würdig schillernde Gestalt hat.",
        "Weil man die Wirklichkeit sah, so sah man, daß man auf Loki zurückführen kann die Gedanken der Freiheit"
      ],
      [
        "und Selbständigkeit des Menschen.",
        "Man wußte aber auch durch das alte Hellsehen, daß dasjenige, was den Menschen immer wieder in sei­nen Begierden und Handlungen dazu bringt, in seiner ganzen Wesen­heit niedriger zu stehen, als wenn er nur an Odin und an die Asen hingegeben wäre, daß das auf den Einfluß des Loki zurückzuführen war.",
        "Und nun fühle man vor allen Dingen das Schauerlich-Großartige dieser germanisch-nordischen Mythologie.",
        "Man fühlte mit zwingender Richtigkeit das, was erst nach und nach durch die Geisteswissenschaft wieder zum Bewußtsein der Menschen kommen wird."
      ],
      [
        "Wie wirkt nun der luziferische Einfluß?",
        "Er schließt sich in den astra­lischen Leib ein, wirkt aber dadurch auf alle drei Glieder des Menschen, sowohl auf den Astralleib als auch auf den Äther- und den physischen Leib.",
        "Nur Andeutungen kann man heute außerhalb unserer Gesell­schaft über diesen Luzifer-Einfluß machen.",
        "Was Sie immer mehr ver­stehen werden, ist, daß der Luzifer-Einfluß sich dreifach geltend macht:"
      ],
      [
        "im Astralleibe, im ätherischen und im physischen Leibe des Menschen."
      ],
      [
        "Im Ätherleibe wird hervorgerufen das, was im Menschen als Trieb zur Unwahrhaftigkeit, zur Lüge wird.",
        "Lüge und Unwahrhaftigkeit sind etwas, was über das Innere des Menschen hinausgeht.",
        "Im Astral­leibe, dem reinen Innern des Menschen, wird das Selbst durchdrungen von dem luziferischen Einfluß, und dieser erscheint dann als Selbst­sucht im Menschen.",
        "Der Ätherleib wird von innen heraus mit dem Triebe, unwahrhaftig zu sein, durchsetzt und dadurch zur Möglichkeit der Lüge bestimmt.",
        "Im physischen Leib wird hervorgerufen Krankheit und Tod.",
        "Für diejenigen, die an meinem letzten Kursus teilgenommen haben, wird das leicht verständlich sein.",
        "Aber hier will ich doch noch einmal darauf hinweisen, daß alles, was im menschlichen physischen Leibe als Krankheit und Tod auftritt, karmisch mit dem verknüpft ist, was wir luziferischen Einfluß nennen.",
        "Wenn wir alles das noch einmal kurz zusammenfassen, so bewirkt Luzifer im Astralleibe: Selbstsucht, im Ätherleibe: Lüge und Unwahrhaftigkeit, im physischen Leibe:"
      ],
      [
        "Krankheit und Tod.",
        "Natürlich werden sich alle materialistisch denken­den Menschen der Gegenwart ungeheuer verwundern, daß in der Gei­steswissenschaft Krankheit und Tod auf einen luziferischen Einfluß zurückgeführt werden.",
        "Auch das hängt nämlich mit Karma zusammen."
      ],
      [
        "An den Menschen träte niemals Krankheit und Tod heran, wenn nicht der luziferische Einfluß stattgefunden hätte.",
        "Das ist eben die karmische Auswirkung des luziferischen Einflusses, daß der Mensch tiefer hin­untersteigt in das Physische, und das wird auf der anderen Seite ausge­glichen durch Krankheit und Tod."
      ],
      [
        "Wir können daher sagen: Indem der luziferische Einfluß hineinkam in den Menschen, wurden der physische, Äther- und Astralleib von Krankheit und Tod, Lüge und Unwahrhaftigkeit und Selbstsucht er­griffen. - Ich möchte noch darauf aufmerksam machen, daß die heutige materialistische Wissenschaft für den Tod im tierischen und im pflanz­lichen Leibe dieselbe Erklärung gibt, wie für den Tod der Menschen.",
        "Diese materialistisch denkenden Menschen können nicht begreifen, daß eine äußere Erscheinung ebenso aussehen kann wie eine andere und doch ganz andere Ursachen haben kann."
      ],
      [
        "Das, was äußerer Tatbestand ist, kann aus ganz verschiedenen Grün-den herrühren.",
        "So tritt der Tod beim Tiere nicht aus denselben Ursaten ein wie beim Menschen, trotzdem er dieselbe äußere Erscheinung hat.",
        "Das sind Dinge, die, wenn man sie erkenntnistheoretisch beweisen wollte, viel zu viel Zeit beanspruchen würden.",
        "Im Grunde wollte ich hier nur sagen, daß es mit dem, was die Wissenschaft Kausalität nennt, sehr schief steht.",
        "Fehler, die in solchen Unklarheiten wurzeln, werden nämlich fast immer gemacht auf Schritt und Tritt.",
        "Denken Sie sich zum Beispiel einmal: Ein Mensch ist aufs Dach hinaufgestiegen, fällt her­unter, hat sich eine todbringende Wunde geschlagen und wird tot auf­gefunden.",
        "Was liegt nun näher, als zu sagen: Der Mensch ist herunter­gefallen, hat sich eine todbringende Wunde geschlagen und ist an der Verletzung gestorben.- Es könnte der Fall aber auch ganz anders liegen.",
        "Der Mensch könnte ja oben vom Schlage getroffen und tot herunter­gefallen sein; die Verwundung könnte durch den Fall eingetreten sein, so daß der Fall äußerlich gerade so läge wie der vorher geschilderte, der Tod aber aus einer ganz anderen Ursache eingetreten wäre.",
        "Der Fall ist hier sehr kraß dargestellt, aber die Wissenschaft macht häufig diese Art Fehler.",
        "Die äußeren Tatbestände können oft ganz gleich sein, und doch sind die inneren Ursachen vollständig verschieden."
      ],
      [
        "Das wollen wir also einmal einfach als Ergebnis der geisteswissenschaftlichen"
      ],
      [
        "Forschung hingestellt sein lassen, daß der luziferische Ein­fluß im Astralleibe: Selbstsucht, im Ätherleibe: Lüge und Unwahrhaf­tigkeit, im physischen Leibe: Krankheit und Tod bewirkt.",
        "Was müßte nun die germanisch-nordische Mythologie gesagt haben, wenn sie dem Loki, dem Luzifer, zugeschrieben hätte, daß dieses dreifache Wirken von ihm herkommen kann?"
      ],
      [
        "Sie mußte sagen: Loki hat drei Sprößlinge.",
        "Der erste ist der, welcher Selbstsucht bewirkt.",
        "Das ist die Midgard­schlange, dasjenige, womit der Einfluß des luziferischen Geistes auf den Astralleib ausgedrückt ist."
      ],
      [
        "Das zweite ist das, was in das menschliche Erkennen sich hineinmischt als das Unrichtige.",
        "Beim Menschen auf dem physischen Plane sind es die Dinge, die in seinem Geiste leben und mit der Außenwelt nicht übereinstimmen."
      ],
      [
        "Da ist es das, was nicht wahr ist.",
        "Bei den nordischen Menschen, die noch mehr auf dem Astralplane leb­ten, lebte sich das, was bei uns abstrakte Lüge ist, gleich als astralische Wesenheit aus und lebte als solche auf dem astralischen Plan."
      ],
      [
        "Der Aus­druck für alles, was Verfinsterung, nicht richtiges Sehen ist, ist irgend­ein tierisches Wesen, hier im Norden hauptsächlich der Fenriswolf.",
        "Das ist das zweite, der Einfluß auf den Ätherleib von seiten des Loki, der bewirkt, daß der Mensch von innen heraus den Trieb hat, sich zu täu­schen, unwahrhaft über die Dinge zu denken, das heißt, es erscheinen ihm die Dinge in der Außenwelt nicht in der richtigen Weise."
      ],
      [
        "Das be­zeichnet also im Grunde genommen die alte germanisch-nordische My­thologie irgendwie mit einer Wolfsgestalt.",
        "Das ist die astrale Figur für die Lüge und alles das, was Unwahrhaftigkeit aus innerem Triebe ist."
      ],
      [
        "Aber hier, wo der Mensch in Beziehung zur äußeren Welt tritt, begeg­net sich schon Luzifer mit Ahriman, so daß aller Irrtum, der sich in die Erkenntnis einschleicht - auch in die hellseherische Erkenntnis - alle Illusion und alle Maja, die Folge des Hanges zur Unwahrhaftigkeit ist, der da hineinspielt.",
        "In dem Fenriswolf haben wir also die Gestaltung zu sehen, welche der Mensch um sich herum hat dadurch, daß er die Dinge nicht in der wahren Gestalt sieht.",
        "Da, wo sich den alten nordi­schen Menschen irgend etwas von äußerem Licht, von der Wahrheit, verdunkelt, da spricht er von einem Wolfe.",
        "Das geht durch das ganze nordische Bewußtsein, und Sie werden finden, daß das Bild bis auf die äußeren Tatsachen überall in diesem Sinne gebraucht wird."
      ],
      [
        "Wenn der alte nordische Mensch sich verständlich machen will über das, was er sieht bei einer Sonnenfinsternis - natürlich sah der Mensch zur Zeit des alten Hellsehens noch anders, als heute bei Benutzung des Fernrohres -, so wählte er das Bild des Wolfes, der die Sonne verfolgt und der in dem Momente, wo er sie erreicht, die Sonnenfinsternis be­wirkt.",
        "Das steht im innersten Einklang mit den Tatsachen.",
        "Diese Ter­minologie gehört mit zu dem Großartigen, ja sogar Schauerlich-Groß-artigen in der nordischen Mythologie.",
        "Ich kann hier nur Andeutungen geben.",
        "Wenn wir aber selbst wochenlang über die nordische Mythologie sprechen könnten, so würden Sie sehen, wie das allseitig durchgeführt ist im nordischen mythologischen Vorstellen.",
        "Das ist deshalb der Fall, weil die Mythologie ein Ergebnis des alten Hellsehertums ist, in das aber das Ich überall hineinspielt."
      ],
      [
        "Die materialistischen Menschen von heute werden sagen: Das ist aber doch Aberglaube.",
        "Es verfolgt doch kein Wolf die Sonne.",
        "Der alte nor­dische, imaginative Mensch sieht eben in Bildern diese Tatsachen, und ich könnte Ihnen vielleicht viele sogenannte wissenschaftliche Wahr­heiten aufzählen, die mehr Einfluß von Ahriman, die größeren Irrtum bergen, als vorhanden ist, wenn man die entsprechende astralische An­schauung beschreibt und sagt: Der Wolf verfolgt die Sonne. - Für den Okkultisten gibt es etwas, was noch in höherem Grad Aberglaube ist.",
        "Das ist, daß eine Sonnenfinsternis dadurch entsteht, daß sich der Mond vor die Sonne stellt.",
        "Das ist für die äußere Anschauung ganz richtig, ebenso richtig, wie für die astrale Anschauung die Sache vom Wolf richtig ist.",
        "Die astrale Anschauung ist sogar richtiger als die, welche Sie in den gegenwärtigen Büchern finden, denn die ist noch mehr dem Irrtum unterworfen.",
        "Wenn der Mensch einst an Stelle dieses Äußeren den wahren Tatbestand erkennen wird, dann wird er finden, daß der nordische Mythos recht hat.",
        "Ich weiß, daß ich für die heutige Anschau­ung etwas gräßlich Absurdes sage, aber ich weiß auch, daß man an theosophischen Stätten schon so weit ist, daß man darauf hindeuten darf, wo gerade unsere physische Weltanschauung am meisten beein­flußt ist von Maja, Täuschung oder Illusion."
      ],
      [
        "Nun kommen wir zum Einfluß von Loki auf den physischen Leib.",
        "In dem bewirkt er Krankheit und Tod.",
        "Der dritte Sprößling ist also das,"
      ],
      [
        "was Krankheit und Tod bewirkt.",
        "Das ist die Hel.",
        "So haben Sie in der Tat in wunderbarer Weise in den Gestalten Hel, Fenriswolf und Mid­gardschlange den Einfluß des Loki oder Luzifer dargestellt, in der Form, wie ihn das alte Hellsehen, das wir in gewisser Beziehung als traumhaftes Hellsehen bezeichnen können, wahrgenommen hat.",
        "Wenn wir die ganze Geschichte von Loki durchgingen, überall würden wir finden, daß diese Dinge bis in die Einzelheiten hinein die Sache voll­ständig beleuchten."
      ],
      [
        "Dabei müssen wir uns immer klar sein, daß das, was der Hellseher sieht, nicht etwa eine allegorisch-symbolische Bezeichnung ist, sondern daß das Wesenheiten sind.",
        "Er sieht Wesenheiten.",
        "Nun hat aber der ger­manisch-nordische Mensch nicht bloß gewußt von seinem Loki, von dem luziferischen Einfluß, sondern auch von dem Einfluß des Ahriman, der von der anderen Seite her kam, und er hat mehr gewußt, nämlich daß das Befallensein von dem ahrimanischen Einfluß eine Folge des Loki-Einflusses ist.",
        "Sie müssen sich jetzt in die Zeit versetzen, wo der Mensch noch nicht in äußerer, physischer Anschauung die Welt ansah, sondern sie mit dem alten Hellsehen betrachtete, und da werden Sie finden, daß der betreffende Mythos für dieses Hellsehen ausgebildet ist.",
        "Was sagt der Mythos?",
        "Lokis Einfluß ist über die Menschen gekommen, was sich ausdrückt in dem Wirken der Midgardschlange, des Fenris­wolfes und der Hel.",
        "Der Mensch ist so geworden, daß seine Anschauung sein klares, lichtvolles Hineinschauen in die geistige Welt getrübt wurde dadurch, daß der luziferische Einfluß sich immer mehr geltend machte.",
        "Der Mensch wechselte in seinem Leben ab in der damaligen Zeit, als"
      ],
      [
        "diese Anschauung sich ausbildete, zwischen dem Sehen in der geistigen Welt und dem Leben auf dem physischen Plan, wie man im Leben ab-wechselt zwischen Wachen und Schlafen.",
        "Wenn er in die geistige Welt hineinsah, sah er in die Welt, aus der er herausgeboren war.",
        "Das ist ja das Wesentliche, daß der Mythos aus dem hellseherischen Bewußtsein heraus entstanden ist.",
        "Das menschliche Bewußtsein aber bestand in diesem abwechselnden Hineinschauen und Nichthineinschauen in die geistige Welt.",
        "War der Zustand des Traumbewußtseins da, so sah man hinein in die geistige Welt; war der Zustand des Tagwachens da, so war man blind für sie.",
        "So wechselte der Zustand zwischen Blindheit und Hineinsehen in die geistige Welt.",
        "Es wechselte das Bewußtsein ab, wie ein gewisses Weltenwesen wechselte zwischen dem blinden Hödur und dem in die geistige Welt hinein schauenden, hellsichtigen Baldur."
      ],
      [
        "Es war der Mensch veranlagt für Baldurs Einfluß, und im Sinne die­ses Einflusses wäre der Mensch geworden, wenn er nicht den Loki-Ein-fluß aufgenommen hätte.",
        "Der aber hat bewirkt, daß Hödurs Natur den Sieg über die Baldurnatur davongetragen hat.",
        "Das wird ausgedrückt dadurch, daß Loki die Mistel herbeischafft, mit der der blinde Hödur den sehenden Baldur tötet."
      ],
      [
        "Loki ist also die tötende Macht, wie Luzifer, der den Menschen zu Ahriman getrieben hat.",
        "Indem der Mensch hingegeben ist an den blin­den Hödur, verlöscht das alte hellsichtige Anschauen.",
        "Das ist die Tö­tung des Baldur.",
        "Das empfindet der nordische Mensch, daß nach und nach wirklich verloren gegangen ist das Baldurhafte, das Hineinschauen in die geistige Welt.",
        "Es hat der nordische Mensch das Hinschwinden des Hellsehens so empfunden, daß ihm Loki in Baldur die Hellsichtig­keit getötet hat, und was ihm geblieben, ist die Ohnmacht gegenüber dieser Hellsichtigkeit.",
        "So ist ein größtes welthistorisches Ereignis, das allmähliche Hinschwinden der alten ungetrübten Erkenntnis, ausge­drückt in dem Baldur-, Hödur- und Loki-Mythos.",
        "Auf der einen Seite haben wir also den Loki mit seiner Sippe, den drei Wesenheiten, und auf der anderen Seite den tragischen Akt von der Tötung des Baldur."
      ],
      [
        "So haben wir in der nordischen Mythologie gespiegelt das, was wir aus der Geisteswissenschaft herausholen können: den zweifachen Ein­fluß, den luziferischen und den ahrimanischen.",
        "Das ist dasjenige, was"
      ],
      [
        "Ihnen die Geisteswissenschaft immer als eine Darstellung des hellsehe­rischen Erkennens der alten Zeit darlegen wird und als ein Heraus-arbeiten des Mythos aus dem alten Hellsehen, das dann zugleich nach und nach dahinschwindet."
      ],
      [
        "Es würde zu weit führen, wollten wir uns auf dieses Gebiet noch weiter einlassen.",
        "Aber schon indem ich Ihnen das Prinzipielle gesagt habe, können Sie das Schaurig-Großartige empfinden in diesem My­thos, der nicht seinesgleichen hat, weil keine Mythologie sich so genau an den alten, hellseherischen Tatbestand angepaßt hat.",
        "Die griechische Mythologie ist nur die Erinnerung an etwas in der Vorzeit Erlebtes, das in plastischer Weise zum Ausdrucke kommt.",
        "Aber eine solche unmittel­bare Anknüpfung an die Tatsachen, wie sie in der germanisch-nordi­schen Mythologie vorliegt, das ist in der griechischen Mythologie nicht vorhanden.",
        "Dieselbe ist abgeklärter, die Gestalten erscheinen mit viel gerundeteren Konturen, daher in stark plastischer Weise, haben aber das Elementare des allerursprünglichsten Eindrucks verloren.",
        "Etwas vom alten Hellsehen ist dem nordischen Menschen lange geblieben.",
        "Dahingeschwunden war das alte Hellsehen der Menschen im übrigen Europa schon lange, als es sich noch im Norden lange bewahrt hat.",
        "Nur nach und nach, langsam und allmählich ist in das Blickfeld des Men­schen das physische Weltbild allein getreten.",
        "So war auch, als das Chri­stentum anfing sich auszubreiten, für die Mehrzahl der Menschen wahr geworden, was sich in der Baldur-Mythe, in dem Tod des Baldur aus­drückt.",
        "Es gab aber noch einzelne, die in unmittelbarer Anschauung haben konnten, was die nordischen Menschen hellseherisch erlebten."
      ],
      [
        "Es war also noch lange ein unmittelbares Anschauen von dieser gei­stigen Welt vorhanden, und weil das alles so elementar war, so unmit­telbar aus der hellseherischen Erfahrung heraus, deshalb blieb auch, als das Christentum schon anfing sich auszubreiten, das Bewußtsein vor­handen, das bei anderen Völkern nicht so stark sein konnte wie bei den alten germanisch-nordischen Menschen.",
        "Sie empfanden dann: Es schwindet alles dahin, was wir damals erlebt haben im Zusammenhang mit der göttlich-geistigen Urheimat.",
        "Es schwand dem Norden erst dahin, als der germanisch-nordische Mensch den Trost des Christen­tums empfing.",
        "Das enthielt für ihn aber nicht unmittelbare Anschauung."
      ],
      [
        "Er hatte das Schicksal des Baldur viel zu tief gefühlt, als daß er sich hätte trösten können damit, daß ihm ein Gott geboten wurde, der zum physischen Plan heruntergestiegen ist, damit die Menschen, die nur den physischen Plan wahrnehmen können, auch zum Gottesbe­wußtsein aufzusteigen vermögen.",
        "So wie die Menschen in Vorderasien ha­ben fühlen können die Worte: «Ändert eure Seelenverfassung, denn das Himmelreich ist nahe herbeigekommen», konnte man das in den nordi­schen Gebieten nicht."
      ],
      [
        "Drüben, wo Christus erschienen war, da konnte man nur alte Erinnerungen an die Tatsache finden, daß es ein altes Hellsehen einst gegeben hat.",
        "Dreitausend Jahre schon währte im Osten das Kali Yuga, das finstere Zeitalter, wo die Menschen nicht mehr hineinschauen konnten in die geistige Welt."
      ],
      [
        "Aber gesehnt haben sie sich immer nach der geistigen Welt, und immer haben sie erzählt von einer solchen Welt, in die der Mensch geistig hineinschauen konnte, die aber jetzt den Blicken entschwunden ist.",
        "Sie haben die geistige Welt in viel fernerer Vergangenheit erlebt, als die Menschen des nordischen Gebie­tes und haben es nur noch aus der Erinnerung gewußt, daß die geistige Welt einmal zugänglich gewesen ist."
      ],
      [
        "Daher konnte man in den vorder-asiatischen Gebieten das Wort: «Ändert eure Seelenverfassung, denn das Himmelreich ist nahe herbeigekommen» gut verstehen.",
        "Man ver­stand es, wenn gesagt wurde: Die Reiche der Himmel sind herbeige­kommen bis in den physischen Plan, seht also hin auf die einzigartige Gestalt, die da im Gebiete des palästinensischen Reiches erscheinen wird, seht auf den Messias, der den Gott in sich enthält, durch den ihr den Zusammenhang mit dem Göttlichen finden werdet, auch wenn ihr euch nicht von dem physischen Plan erheben könnt."
      ],
      [
        "Versteht die Ge­stalt von Palästina, versteht die Christus-Gestalt. - Das ist das tiefe Wort Johannes des Täufers."
      ],
      [
        "Das mußte der nordische Mensch anders empfinden, der noch länger viel mehr erlebt hatte als nur die erinnerungsgemäße Kunde von dem Hineinschauen in die göttlich-geistige Welt.",
        "Daher ging ihm ein Ge­danke auf von einer ungeheuern, ganz gewaltigen Tragweite, der Ge­danke: Dieses Heraustreten auf den physischen Plan, in die physische Welt, das Nichtsehen der göttlich-geistigen Welt, das kann nur eine Zwischenzeit sein.",
        "Der Mensch wird das als Schule durchzumachen"
      ],
      [
        "haben und sehen müssen, was er sich aneignen kann in der physischen Welt.",
        "Er braucht diesen Durchgang, er muß also heraustreten aus der geistigen Welt; er muß die Erlebnisse der physischen Welt als Schule durchmachen.",
        "Aber gerade dadurch, daß er sie als Schule durchmacht, wird er wieder hineinkommen in die Welt, aus der er herausgetreten ist.",
        "Der Baldurblick wird ihn wieder beseelen können. - Mit anderen Worten: Die große Idee, die im Laufe der germanisch-nordischen Ent­wickelung entsteht, daß die Welt wieder sichtbar werden wird, die geschwunden ist und dem hellseherischen Blick entzogen wurde, be­wirkte, daß als Zwischenzeit empfunden wurde das Walten auf dem physischen Plan."
      ],
      [
        "Seine Eingeweihten machten es dem nordischen Menschen begreif­lich, daß in der göttlich-geistigen Welt in dieser Zwischenzeit, während er nicht in dieselbe hineinschauen kann, etwas vorgeht, durch das diese göttlich-geistige Welt einst anders ausschauen wird, als er früher ge­wohnt war, sie zu sehen.",
        "Sie machten ihm das begreiflich, in dem sie zu ihm ungefähr so sprachen: Du hast früher in die göttlich-geistige Welt hineingesehen, hast darin den Erzengel der Sprache, den Erzengel der Runen, den Erzengel des Atems, Odin, gesehen und den Engel der Ich­heit, den Thor.",
        "Du standest mit ihnen in Verbindung, und es wird der­jenige, der dazu vorbereitet ist, die Möglichkeit erwerben, wieder in diese geistige Welt hineinzukommen.",
        "Dann wird sie aber anders aus­sehen; andere Mächte werden hinzugetreten sein und die Machtbereiche und Machtverhältnisse dieser alten geistigen Führer des Menschenge­schlechts werden sich verändert haben.",
        "Du wirst dann zwar in diese Welt hineinsehen, aber du wirst anderes sehen, als was du bisher erlebt hast."
      ],
      [
        "Dasjenige, was der Mensch dann sehen wird, malten sie ihm als eine Zukunftsvision aus, als jene Zukunftsvision, die einmal vor die mensch­liche Seele treten wird, wenn der Mensch wieder hineinsehen kann in die geistige Welt und sehen wird, welches Schicksal die alten Göttergestalten gehabt haben, sehen wird, wie sie mit anderen Mächten in Beziehung traten.",
        "Diese Zukunftsvision, wie sie die Eingeweihten geschaut haben, malten sie ihm aus, wo in der Tat dasjenige, was von Luzifer kommt, in gewisser Weise in Kampf getreten sein wird mit dem, was von den"
      ],
      [
        "Göttern kommt, und sich auch ausleben wird.",
        "Diese Zukunftsvision malten die Eingeweihten den Menschen in dem Bilde von der Götter­dämmerung aus.",
        "Die Götterdämmerung, Ragnarök, ist also das Bild, das die Eingeweihten dem germanisch-nordischen Menschen als Zu­kunftsbild vor Augen stellten.",
        "Und wieder werden wir finden, daß alle Vorgänge, die da als Zukunftsvorgänge dargestellt werden, bis in die Einzelheiten hinein nicht besser, nicht terminologisch richtiger und nicht treffender dargestellt werden könnten, als sie dargestellt worden sind in dem wunderbaren Bilde der Götterdämmerung.",
        "Das ist der ok­kulte Hintergrund des Bildes von der Götterdämmerung."
      ],
      [
        "Als was soll sich dann der Mensch sehen?",
        "Er soll sich sehen so, daß er alles dasjenige als Entwickelungsursache aufgenommen hat, was aus früheren Zeiten stammt; er soll denkend aufnehmen, was er als Gabe Odins bekommen hat, sich selber aber fühlen als durch die Entwicke­lung durchgegangen, die dann gefolgt ist.",
        "Er soll die Lehren, die Odin in ihn verpflanzt hat, in sich aufnehmen - Odin tritt ihm entgegen als Erzengel.",
        "Er soll sich zum Sohne des Odin machen; er soll in den Kampf eintreten, und zwar bald in diesen Kampf eintreten.",
        "Das macht der Eingeweihte, der Leiter der esoterischen Schule, besonders dem nordi­schen Menschen klar, indem er auf das göttlich-geistige Wesen hinweist, das uns so geheimnisvoll erscheint, das eigentlich erst bei der Götter­dämmerung eine bestimmte Rolle bekommt, weil es selbst diejenige Macht überwindet, durch die zuerst Odin überwunden wird.",
        "Der Rä­cher des Odin bekommt eine besondere Rolle und spielt sie in der Göt­terdämmerung.",
        "Wenn wir diese Rolle verstehen werden, so wird sich uns der wunderbare Zusammenhang ergeben zwischen den Anlagen des germanisch-nordischen Menschen und dem, was wir uns vorstellen können als die Vision der Zukunft.",
        "In wunderbarer Weise, bis in die Einzelheiten genau, ist das alles in der großen Vision von der Götter­dämmerung zum Ausdruck gekommen."
      ]
    ]
  },
  {
    "order": 11,
    "title_de": "ZEHNTER VORTRAG Kristiania, 16. Juni 1910",
    "paragraphs": [
      "Bevor wir dasjenige entwickeln, was sich in Anknüpfung an das be­deutsame Bild der Götterdämmerung ergeben wird, wird es gut sein, wenn wir uns dafür eine Grundlage schaffen. Denn es wird sich dar­um handeln, das Wesen der germanisch-nordischen Volksseele aus den gewonnenen Resultaten heraus genauer zu schildern.",
      "Wir müssen se­hen, wie in Europa das gesamte europäische Geistesleben zusammen­wirkt, wie durch die Tätigkeit der verschiedenen Volksgeister ein Fortschritt der Menschheit bewirkt wird - aus uralten Zeiten heraus, durch unsere Gegenwart hindurch, in die Zukunft hinein. Jedes ein­zelne Volk, ja sogar alle einzelnen, kleineren Volkssplitter haben in diesem großen Gesamtgemälde ihre besondere Aufgabe, und aus dem, was gesagt worden ist, können Sie erkennen, daß, in gewisser Bezie­hung, gerade der vor- und nachchristlichen Kultur Europas die Auf­gabe, die Mission zugefallen ist, das Ich durch die verschiedenen Stu­fen der menschlichen Wesenheit hindurch zu erziehen, es herauszu­bilden und nach und nach zu entwickeln.",
      "Es wurde ja in gewisser Beziehung dieses Ich in uralter Zeit noch aus der geistigen Welt her­aus, wie wir dies am germanisch-nordischen Volke gezeigt haben, hell­seherisch dem Menschen gezeigt. Es wurde gesagt, wie dieses Ich den Menschen verliehen wird von einem der Engelwesen, das sogar zwi­schen dem Menschen und der Volksseele mitten darinnen steht: von dem Donar oder Thor.",
      "Wir haben gesehen, daß sich der einzelne noch vorkam wie Ich-los, wie unpersönlich. Er sah das Ich wie eine Gabe an, die ihm aus der geistigen Welt geschenkt wurde.",
      "In solcher Weise hat man natürlich im Orient, als das Ich über­haupt erwachte, das Ich nicht gefunden. Da war der Mensch schon subjektiv so weit entwickelt zu einer hohen Stufe menschlicher Voll­kommenheit, daß er das Ich nicht als fremdes, sondern als eigenes empfand. Als der Mensch im Orient zum Ich erwachte, war die orien­talische Kultur schon so weit, daß sie fähig war, eine so fein ausge­sponnene Spekulation, Logik und Weisheit nach und nach zu entwickeln,",
      "wie wir sie in der orientalischen Weisheit vor uns sehen. Also den ganzen Prozeß des Empfangens des Ich wie aus einer höhe­ren, geistigen Welt unter der Beihilfe einer solchen göttlich-geistigen Individualität wie der Thor es war, hat der Orientalismus nicht mehr mitgemacht.",
      "Ihn hat mitgemacht der Europäismus, und daher empfin­det dieser Europäismus auch dieses allmähliche Hinaufsteigen zu dem individuellen Ich wie das Herauskommen aus einer Art von Gruppen-seele. Der germanisch-nordische Mensch fühlte sich selbst noch wie mit einer Gruppenseele behaftet, wie zu einer ganzen Gemeinschaft gehörig, wie ein Glied in der großen Zusammengehörigkeit des Stam­mes.",
      "Nur so konnte es kommen, daß noch fast hundert Jahre, nach­dem der christliche Impuls der Erde gegeben worden ist, Tacitus die Germanen Mitteleuropas so schildern konnte, daß sie immer als zu einzelnen Stämmen gehörig erscheinen, daß sie wie die Glieder eines Organismus sind und zu der Einheit des Organismus gehören. So fühlte sich der einzelne in jener Zeit noch wie ein Glied des Stammes-Ich.",
      "Er fühlte das nach und nach Heraus-geboren-Werden des indivi­duellen Ich aus dem Stammes-Ich, und er fühlte in dem Gotte Thor den Geber, den Verleiher des Ich, den Gott, der ihn eigentlich mit dem individuellen Ich begabte. Aber er fühlte diesen Gott noch ver­bunden mit dem gesamten Geiste des Stammes, mit dem, was in der Gruppenseele lebt.",
      "Für diese Gruppenseele findet sich nun der Aus­druck «Sif». Das ist der Name für die Gemahlin des Thor. Sif muß sprachlich verwandt sein mit dem Worte Sippe, Stammeszusammen­gehörigkeit und ist es auch in der Tat, wenn das auch maskiert und verborgen ist.",
      "Okkult bedeutet aber Sif die Gruppenseele der einzel­nen Gemeinschaft, aus der herauswächst das einzelne Individuum. Sif ist diejenige Wesenheit, die sich verbindet mit dem Gotte des indivi­duellen Ich, mit dem Geber des individuellen Ich, mit Thor.",
      "Sif und Thor empfindet der individuelle Mensch als die Wesenheiten, die ihm das Ich gaben. Die empfand der nordische Mensch noch so, als den Völkern in anderen Gegenden Europas bereits andere Aufgaben in der Erziehung des Menschen zum Ich hin zugeteilt waren.",
      "Jedes einzelne Volk hat seine besondere Aufgabe. Da finden wir vor allen Dingen dasjenige Volk, diejenige Völkerzusammengehörigkeit,",
      "diejenige Volksgemeinsamkeit ausgebreitet, die wir unter dem Na­men der Kelten kennen. Der Volksgeist der Kelten, von dem wir aus den vorangegangenen Darstellungen wissen, daß er später ganz an­dere Aufgaben bekommen hat, hatte die Aufgabe, das noch junge Ich der europäischen Bevölkerung heranzuziehen. Dazu aber mußte noch eine Erziehung, ein Unterricht der Kelten selbst vorhanden sein, der unmittelbar aus der höheren Welt vermittelt war. Daher ist es durchaus richtig, daß die Kelten durch ihre Eingeweihten, die Druiden-Priester, einen Unterricht aus höheren Welten erhielten, den sie aus eigener Kraft nicht hätten empfangen können, und den sie an die übrigen Völker dann weiterzugeben hatten.",
      "Die gesamte europäische Kultur ist eine Gabe der europäischen My­sterien. Die fortschreitenden Volksseelen sind immer die Lenker der Gesamtkultur der Menschheit in ihrem Fortschritt. Aber in der Zeit, in welcher diese Volksgeister Europas die Menschen dazu anleiten sollten, aus sich selber heraus zu arbeiten, aus sich selber heraus wirk­sam zu sein, war es notwendig, daß sich die Mysterien mehr zurück-zogen.",
      "Daher trat mit dem Zurückziehen des keltischen Elementes auch eine Art Zurückziehung der Mysterien in viel geheimere Unter­gründe ein. Ein viel direkterer, unmittelbarer Verkehr der Geistes-wesen mit dem Volke durch die Mysterien war zur Zeit der alten Kelten vorhanden, weil das Ich noch gebunden war an die Gruppen­haftigkeit, und doch sollte das keltische Element der Verleiher des Ich für die übrige Bevölkerung sein.",
      "Wir können also sagen: In der Zeit, die vor der eigentlichen germanisch-nordischen Entwickelung liegt, konnte nur durch die alten keltischen Mysterien der europäischen Kultur die Mysterien-Erziehung gegeben werden. Diese Mysterien-Erziehung hat gerade so viel an die Oberfläche kommen lassen, als notwendig war, um eine Grundlage für die gesamte Kultur Europas zu geben.",
      "Aus dieser alten Kultur haben sich nun durch Vermischung mit den verschiedensten Rassensplittern, Volksbestandteilen und Ras­sengemeinschaften die verschiedensten Volksseelen und Volksgeister befruchten können und haben immer das Ich in andere Lagen ge­bracht, um es zu erziehen, das Ich, das sich herauswühlte aus dem Un­tergrunde dessen, was unter dem Ich des Menschen liegt.",
      "Man kann sagen, daß, nachdem die alte griechische Kultur bis zu einem gewissen Grade ihren Höhepunkt erreicht hatte in der Ausbil­dung desjenigen, was sie eben als ihre besondere Mission hatte, eine ganz andere Seite dieser selben Mission im alten Römertum und seinen verschiedenen Kulturperioden zutage trat. Wir haben bereits er­wähnt, wie in einer strengen Stufenfolge aufeinanderfolgen die ein­zelnen nachatlantischen Kulturen. Wenn wir uns einen Überblick ver­schaffen wollen über diese Stufenfolge der nachatlantischen Kulturen, so können wir sagen: Die alte indische Kultur arbeitete am mensch­lichen Ätherleibe. Daher der hellsichtige, wunderbar weisheitsvolle Charakter der alten indischen Kultur, weil sie - nach Ausbildung der besonderen menschlichen Fähigkeiten - eine im menschlichen Äther-leibe reflektierte Kultur ist, so daß wir die alte indische Kultur etwa in der folgenden Weise fassen können.",
      "Von der atlantischen bis zur späteren nachatlantischen Zeit hat der indische Volksgeist die ganze Entwickelung der inneren Seelen-kräfte durchgemacht, ohne daß sein Ich erwacht war. Er hat dann wieder den Weg zurück genommen bis zu seiner Arbeit im menschlichen",
      "Ätherleibe. Das ist das Wesentliche der alten indischen Kultur, daß mit fertig ausgebildeten Seelenkräften, mit Seelenkräften, die im höchsten Grade verfeinert waren, der Inder wiederum hineingeht in den Ätherleib, zurückgeht bis zum Ätherleib und in demselben jene wunderbar feinen Kräfte ausbildet, deren späterer Reflex wir in den Veden und in noch verfeinerterem Zustande in der Vedanta-Philoso­phie sehen.",
      "Das war alles nur möglich dadurch, daß sich die indische Volksseele bis zu einem hohen Grade entwickelt hatte, bevor das Ich angeschaut, wahrgenommen worden ist, und schon wieder zu einer Zeit, als der Mensch mit den Kräften des Ätherleibes selber sehen konnte. Die persische Volksseele war nicht so weit gekommen.",
      "Die war nur so weit gekommen, in dem Empfindungsleibe oder Astral­leibe wahrzunehmen. Noch anders war es in der babylonisch-chal­däisch-ägyptischen Kultur. Da war es so, daß der Teil, den wir als die Empfindungsseele bezeichnen, wahrnehmen konnte.",
      "Wir müssen also diese ägyptisch-chaldäische Kultur als eine solche bezeichnen, welche in der Empfindungsseele arbeitet. Beim griechisch-lateinischen Volks-geiste war das so, daß er geleitet worden ist bis zur Verstandes- oder Gemütsseele; in dieser Verstandes- oder Gemütsseele arbeitete er.",
      "An der Verstandes- oder Gemütsseele konnte er selbst nur dadurch arbei­ten, daß diese Verstandes- oder Gemütsseele wiederum im Ätherleibe eine Art Ausprägung ihres Wesens hatte. Aber es ist dies gleichsam eine weniger reale, weniger anschauliche und der Wirklichkeit einge­prägte Form des Weltbildes, wie es jetzt im Griechentum herauskam.",
      "Während ein unmittelbares Arbeiten im Ätherleibe bei der alten indi­schen Kultur da war, ist jetzt ein verwischtes, ein abgeschattetes, ein matteres Abbild der Wirklichkeit vorhanden, wie ich es charakteri­siert habe dadurch, daß ich sagte: Es ist wie eine Erinnerung an das, was diese Völker einst erlebt hatten, wie eine Erinnerung, die zurück-strahlt auf ihren Ätherleib (vgl. die schematische Abbildung).",
      "Bei den anderen Völkern, die jetzt auf das griechische Volk folgten, haben wir es zu tun mit dem vorzugsweisen Gebrauche des physischen Leibes zur stufenweisen Ausbildung der Bewußtseinsseele. Daher war die griechische Kultur eine solche, die wir nur begreifen können, wenn wir sie aus dem Innern heraus zu begreifen vermögen; wenn wir uns",
      "klar sind, daß bei ihr als äußere Erfahrung wichtig ist, was aus dem Innern des Griechen heraussprudelt. Dagegen haben die Völker, die mehr nach Westen und Norden gelegen sind, die Aufgabe, unter Lei­tung ihrer Volksseelen den Blick in die Welt hinauszurichten und das in der Welt zu sehen, was auf dem physischen Plane zu sehen ist, auszubilden das, was auf dem physischen Plane eine Rolle spielen soll. Die germanisch-nordischen Völker hatten noch die besondere Auf­gabe, daß sie das alles so ausbilden sollten, wie sie es ausbilden konn­ten, da sie noch die Gnade, die welthistorische Gnade genossen, im alten Hellsehen hineinzusehen in die geistige Welt und hineinzutragen die uralten Erfahrungen, die sie wie lebendig empfanden, in das, was auf dem physischen Plane eingerichtet werden sollte.",
      "Ein Volk gab es, das in seiner späteren Zeit diese Gnade nicht mehr hatte, ein Volk, das keine solche Vorentwicklung zunächst durch­gemacht hatte, das daher gleichsam wie mit einem Sprung vor die Geburt des menschlichen Ich auf dem physischen Plane gestellt wur­de und daher nur unter Anleitung seiner Volksseele, seines Erzengels für alles das sorgen konnte, was dieses menschliche Ich auf dem phy­sischen Plane förderte, was zur Wohlfahrt dieses menschlichen Ich auf dem physischen Plane notwendig war. Dies war das römische Volk.",
      "Alles, was das römische Volk unter Anleitung seines Volksgei­stes für die gesamte Mission Europas zu leisten hatte, war dazu be­stimmt, dem Ich des Menschen als solchem Geltung zu verschaffen. Daher konnte das römische Volk dasjenige ausbilden, was das Ich zwischen die anderen Iche hineinstellt.",
      "Es konnte die ganze Summe der Privatrechte begründen. Daher wurde es der Schöpfer der Juris­prudenz, die rein auf das Ich gebaut ist. Wie das Ich dem Ich gegen­übersteht, das war die große Frage in der Mission des römischen Vol­kes.",
      "Die anderen Völker, die aus der Kultur des römischen Volkes herausgewachsen sind, hatten schon mehr von dem, was sozusagen aus der Empfindungsseele, aus der Verstandes- oder Gemütsseele und aus der Bewußtseinsseele selbst heraus dieses Ich in irgendeiner Weise be­fruchtet, dieses Ich in die Welt hineintreibt. Dazu waren notwendig alle von der äußeren Geschichte aufgezählten Rassenvermischungen, die auf der italischen und pyrenäischen Halbinsel, im heutigen",
      "Frankreich und im heutigen Großbritannien zustande gekommen sind, um das Ich nach den verschiedenen Nuancen, nach der Empfin­dungsseele, nach der Verstandes- oder Gemütsseele und nach der Bewußtseinsseele auszubilden auf dem physischen Plan. Das war die große Mission der Völker, die sich nach und nach im Westen Europas in der verschiedensten Weise ausgebildet haben.",
      "Alle einzelnen Kulturnuancen und Missionen im Westen Europas finden zuletzt ihre Erklärung darin, daß in der Richtung nach der italischen und pyrenäischen Halbinsel hin dasjenige auszubilden war, was durch die Impulse der Empfindungsseele in das Ich hinein ausgebildet werden konnte. Studieren Sie die einzelnen Volkscharak­tere nach ihren Licht- und Schattenseiten, da werden Sie finden, daß Sie bei den Völkern der italischen und pyrenäischen Halbinsel die eigentümliche Mischung des Ich mit der Empfindungsseele haben.",
      "Bei den Völkern aber, die auf Frankreichs Boden bis in die neueste Zeit herauf gelebt haben, werden Sie ihre Eigenart begreiflich finden, wenn Sie das Werden und die Vermischungen der Verstandes- oder Gemütsseele mit dem Ich betrachten. Die großen, welthistorischen Er­folge aber, als deren Repräsentant wir Großbritannien betrachten können, sind darauf zurückzuführen, daß der Impuls der Bewußt­seinsseele in das menschliche Ich hineingedrängt worden ist.",
      "Mit dem, was als welthistorische Mission aus den britischen Ländern hervor­ging, ist auch zusammenhängend das, was aus der Begründung der äußeren, staatsrechtlichen Form hervorging. Die Verbindung der Be­wußtseinsseele mit dem Ich war noch nicht innerlich vorhanden.",
      "Wenn Sie aber durchschauen, wie diese Verbindung der Bewußtseins­seele mit dem nach außen getriebenen Ich zustande kam, so werden Sie finden, daß die großen welthistorischen Eroberungen der Bevöl­kerung jener Insel von diesem Impulse herrühren. Sie finden aber auch, daß das, was da geschieht an Begründungen der parlanientari­schen Regierungsformen, sofort verständlich wird, wenn man weiß, daß damit ein Impuls der Bewußtseinsseele auf den Plan der Welt­geschichte hingestellt werden sollte.",
      "Es waren also viele Nuancen notwendig, denn durch viele Stufen des Ich waren die einzelnen Völker zu führen. Wir würden wahre Geschichtsbilder",
      "finden, wenn wir Zeit genug hätten, diese Dinge weiter zu verfolgen, die uns zeigen, wie die Grundkräfte sich verzweigen und sich in der verschiedensten Weise auswirken. So wirkte die See­lenkonstitution bei den westlichen Völkern, die für sich selbst nicht die unmittelbare, elementare Erinnerung hatten an die hellseherisch erlebten Dinge der geistigen Welt von früher.",
      "Ganz anders mußte in der späteren Zeit im germanisch-nordischen Gebiet sich ausbilden das­jenige, was unmittelbar aus einer nach und nach erfolgten Entwicke­lung des schon in die Empfindungsseele hineingegossenen, ursprüng­lichen Hellsehens hervorging. Daher jener Zug der Innerlichkeit, der ja nur die Nachwirkung innerlicher, in der Vorzeit erfolgter hellsehe­rischer Erfahrung ist.",
      "Die südlich-germanischen Völker hatten zu­nächst ihre Aufgabe auf dem Gebiet der Bewußtseinsseele. Die grie­chisch-lateinische Zeit hatte auszubilden die Verstandes- oder Ge­mütsseele. Sie hatte aber nicht bloß den Impuls zu geben mit der Ver­standes- oder Gemütsseele, sie hatte hineinzuwirken mit einer wun­derbaren, mit hellseherischer Erfahrung ausgestatteten vorzeitlichen Entwickelung.",
      "Das alles ergoß sich in die Bewußtseinsseelen der mittel­europäisch-nordisch-germanischen Völker. Das wirkte bei diesen als Seelenanlage nach, und die südlicheren Teile der germanischen Mensch­heit hatten zunächst auszubilden das, was dazu gehört, um die Be­wußtseinsseele innerlich vorzubereiten, innerlich mit dem auf den physischen Plan umgesetzten Bewußtseinsinhalt des alten Hellsehens zu erfüllen.",
      "Scheinbar liegen weit ab von dem mythologischen Gebiet die Phi­losophien Mitteleuropas, diese Philosophien, welche Fichte, Schelling und Hegel noch im neunzehnten Jahrhundert vertraten. Dennoch sind sie nichts anderes, als das Resultat des sublimiertesten alten Hell­sehens, des im Innern des Menschen eroberten Zusammenarbeitens mit göttlich-geistigen Mächten. Unmöglich hätte sonst ein Hegel in seinen Jdeen Realitäten sehen können, unmöglich hätte ein Hegel den son­derbaren Ausspruch tun können, der ihn so sehr charakterisiert, in­dem er auf die Frage: «Was ist das Abstrakte?» antwortet: «Das Abstrakte ist zum Beispiel ein einzelner Mensch, der seine täglichen Verrichtungen tut, nehmen wir an: ein Zimmermann.» Dasjenige also,",
      "was für den Abstraktling etwas Konkretes ist, das war für Hegel etwas Abstraktes. Das, was für den Abstraktling nur Gedanken sind, das waren für ihn große, gewaltige Werkmeister der Welt. Die Ideen­welt Hegels ist der letzte sublimierteste Ausdruck der Bewusstseins-seele und enthält in reinen Begriffen das, was der nordische Mensch noch als sinnlich-übersinnliche, göttlich-geistige Mächte gesehen hat in Verbindung mit dem Ich. Und als bei Fichte das Ich zum Ausdruck kam, da war es nichts anderes als der Niederschlag dessen, was der Gott Thor der menschlichen Seele gegeben hat, von Fichte nur gesehen aus der Bewußtseinsseele, in dem scheinbar ärmsten Gedanken, dem Gedanken «Ich bin», von dem die Fichtesche Philosophie ausgeht. Eine gerade Entwickelungslinie geht von der Begabung des alten nor­dischen Volkes mit dem Ich ausströmend durch den Gott Thor oder Donar aus der Geistwelt bis in die Philosophie. Dieser Gott hatte das alles vorzubereiten für die Bewußtseinsseele, damit sie einen ihr angemessenen Inhalt habe, denn sie ist darauf angewiesen, in die äußere Welt hineinzuschauen und innerhalb dieser Welt zu wirken. Aber diese Philosophie findet nicht bloß die äußere, grobsinnliche, materialistische Erfahrung, sondern sie findet den Inhalt der Be­wußtsseinsseele selber in der äußeren Welt und sieht die Natur nur an als die Idee in ihrem Anderssein. Nehmen Sie diesen fortwirkenden Impuls, so haben Sie darin die Mission der germanisch-nordischen Völker in Mitteleuropa.",
      "Nun müssen wir uns fragen, da alle Entwickelung einen Fortgang zu nehmen hat: Wie schreitet diese Evolution vorwärts? Wir können da Merkwürdiges sehen, wenn wir in ältere Zeiten zurückschauen. Wir haben gesagt: Im alten Indertum fand die erste Kultur im Äther-leibe statt, nachdem die entsprechende Ausbildung der geistigen Kräf­te da war. Es gibt aber auch noch Kulturen, die sich die alte, atlan­tische Kultur bewahrt und sie hineingetragen haben in die Menschen der nachatlantischen Zeit. Während der Inder von dieser Seite aus an seinen Ätherleib herankommt und aus diesem heraus, mit den Kräf­ten desselben, seine gewaltig große Kultur und sein großartiges Gei­stesleben schafft, haben wir von der anderen Seite eine Kultur, wel­che im Atlantiertum wurzelt und hineinarbeitet in die nachatlantische",
      "Zeit eine Kultur, welche gleichsam zu ihrer Begründung und Ausbil­dung die andere Seite des Ätherleib-Bewußtseins herausarbeitet. Das ist die chinesische Kultur. Die Einzelheiten der chinesischen Kultur werden Sie begreifen, wenn Sie diesen Zusammenhang ins Auge fas­sen und sich erinnern, daß die atlantische Kultur ein unmittelbares Verhältnis hatte zu dem, was wir in unseren früheren Darstellungen den «Großen Geist» nannten, so daß also diese Kultur ein unmittel­bares Verhältnis hatte zu den höchsten Stufen der Weltentwickelung. Aber diese Kultur wirkt noch hinein in moderne Menschenkörper, und zwar von einer ganz anderen Seite. Daher wird auch begreiflich erscheinen, daß gerade in diesen beiden Kulturen einmal zusammen­stoßen werden die zwei großen Gegensätze der nachatlantischen Zeit:",
      "das Indertum, das in gewissen Grenzen entwickelungsfähig ist, und das Chinesentum, das sich abschließt und starr bleibt, das wiederholt, was in der alten atlantischen Zeit da war. Man bekommt förmlich den Eindruck von einer okkult-wissenschaftlich-poetischen Art, wenn man das Chinesenreich in seiner Entwickelung beobachtet, wenn man an die chinesische Mauer denkt, die nach allen Seiten hin dasjenige abschließen sollte, was aus den uralten Zeiten stammte und in der nachatlantischen Zeit sich entwickelt hatte.",
      "Ich sage jetzt, es be­schleicht einen etwas wie eine poetisch-okkulte Empfindung, wenn man die chinesische Mauer vergleicht mit dem, was es einmal in frü­heren Zeiten gegeben hat. Ich kann diese Dinge nur andeuten.",
      "Sie werden finden, wenn Sie dies mit den heute schon vorhandenen wis­senschaftlichen Ergebnissen vergleichen, wie außerordentlich auf­schlußgebend diese Dinge sind. Betrachten wir hellseherisch den alten Kontinent der atlantischen Welt, den wir zu suchen haben da, wo jetzt der Atlantische Ozean ist, zwischen Afrika und Europa einer­seits und Amerika anderseits.",
      "Dieser Kontinent war umschlossen von einer Art von warmem Strom, von einem Strom, bezüglich dessen das hellseherische Bewußtsein ergibt, daß er, so sonderbar es klingen mag, von Süden heraufging, durch die Baffins-Bai gegen das nörd­liche Grönland verlaufend und es umfassend, dann herüberfloß nach Osten, sich allmählich abkühlte, dann in der Zeit, in welcher Sibirien und Rußland noch lange nicht zur Erdoberfläche gehoben waren, in",
      "der Gegend des Ural hinunterfloß, sich umkehrte, die östlichen Kar­pathen berührte, in die Gegend hineinfloß, wo die heutige Sahara ist, und endlich beim Meerbusen von Biskaya dem Atlantischen Ozean zuging, so daß er ein ganz geschlossenes Stromgebiet hatte. Sie wer­den begreifen, daß dieser Strom nur noch in den allerletzten Resten vorhanden sein kann. Dieser Strom ist der Golfstrom, der einst den atlantischen Kontinent umflossen hat. - Und jetzt werden Sie auch begreifen, daß bei den Griechen das Seelenleben Erinnerung ist. Es tauchte in ihnen auf das Bild des Okeanos, der eine Erinnerung ist an jene atlantische Zeit. Ihr Weltbild ist nicht so unrichtig, weil es aus der alten atlantischen Zeit geschöpft ist. - Den Strom, der über Spitz­bergen als warmer Strom herunterkam und nach und nach sich ab­kühlte usw., dieses geschlossene Stromgebiet haben sich die Chinesen förmlich wiedererschaffen in ihrer von der Mauer umschlossenen, aus der atlantischen Zeit herübergeretteten Kultur. Das Geschichtliche war in der atlantischen Kultur noch nicht vorhanden. Daher hat auch die chinesische Kultur etwas Ungeschichtliches behalten. Daher haben wir da etwas Vorindisches, etwas aus der Atlantis Stammendes.",
      "Wenden wir uns jetzt zu der Schilderung im Weitergange des ger­manisch-nordischen Volksgeistes zu dem, was auf ihn folgt. Was wird das nächste sein, wenn ein Volksgeist sein Volk so leitet, daß das Geistselbst sich besonders entwickeln kann? Erinnern wir uns daran, daß der Ätherleib in der indischen Kultur, der Empfindungsleib in der persischen Kultur, die Empfindungsseele in der ägyptisch-chal­däischen Kultur, die Verstandes- oder Gemütsseele in der griechisch-lateinischen Kultur, die Bewußtseinsseele in unserer, noch nicht abge­schlossenen Kultur zur Entwickelung kommt. Nun folgt aber das Er­greifen des Geistselbst durch die Bewußtseinsseele, so daß hinein­leuchtet das Geistselbst in die Bewußtseinsseele, was als Aufgabe der sechsten Kulturstufe nach und nach vorbereitet werden muß. Diese Kultur, die im eminentesten Sinne eine empfängliche Kultur sein muß, denn sie muß hingebungsvoll das Hereindringen des Geistselbst in die Bewußtseinsseele abwarten, wird vorbereitet durch die Völker West­asiens und die vorgeschobenen slawischen Völker Osteuropas. Die letzteren sind aus gutem Grunde mit ihren Volksseelen vorgeschoben,",
      "aus dem Grunde, weil alles, was in Zukunft kommen wird, in einer gewissen Weise seine Vorbereitung vorher erfahren muß, sich schon hineinschieben muß, um die Elemente für das Spätere abzugeben. Im höchsten Grade interessant ist es, diese vorgeschobenen Posten einer für die späteren Epochen sich vorbereitenden Volksseele zu studieren.",
      "Daher das Eigenartige der für uns zunächst östlich wohnenden slawi­schen Völker. Ihre ganze Kultur mutet den Westeuropäer an als sich im Vorbereitungsstadium befindend, und in sonderbarer Weise schie­ben sie vor, durch die Medien ihrer vorgeschobenen Posten, dasjenige, was dem Geiste nach etwas ganz anderes ist, als irgendeine Mytho­logie.",
      "Es würde verkennen heißen dasjenige, was von Osten herüber vorgeschoben wird als zu erwartende Kultur, es würde diese Kultur verkennen heißen, wenn man sie vergleichen wollte mit dem, was die westeuropäischen Völker in sich haben, die einen geradlinig fortlau­fenden Impuls, der noch im alten Hellsehen seine Wurzel und Quelle hat, besitzen. Das Eigenartige, wodurch sich die Seele dieser osteuro­päischen Völker darlebt, das drückt sich in dem ganzen Verhältnis aus, das diese Völker immer offenbarten, wenn ihre Beziehungen zu den höheren Welten in Betracht kamen.",
      "Diese Beziehung ist, wenn wir sie mit dem vergleichen, was sich in unseren Mythologien, in Westeuropa, zeigt, mit den sonderbaren, bis ins Individuelle ausge­arbeiteten Götterfiguren, etwas ganz anderes. Sie tritt uns so entgegen, daß wir das, was sie uns gibt als unmittelbaren Ausfluß des Volks-wesens vergleichen können mit unsern verschiedenen Planen oder Wel­ten, durch die wir uns vorbereiten zum Begreifen einer geistigen, höheren Kultur.",
      "Da finden wir zum Beispiel im Osten folgende Vor­stellung: Empfangen hat der Westen aufeinanderfolgende, nebenein­anderliegende Welten. Wir haben da zunächst ein deutliches Bewußt­sein von einer Welt des kosmischen Vaters.",
      "Alles dasjenige, was in Luft und Feuer, was überhaupt in den Elementen, die in und über der Erde sich finden, schöpferisch tätig ist, das tritt uns wie in einem großen, umfassenden Gesamtbegriffe, der zugleich Gesamtempfindung ist, entgegen als der Begriff des Himmelsvaters. So wie wir uns etwa die Welt des Devachan unsere Erde befruchtend denken, so tritt uns diese Himmelswelt, diese väterliche Welt, von Osten her entgegen,",
      "und sie befruchtet dasjenige, was als Mütterliches empfunden wird, den Geist der Erde. Wir haben keinen anderen Ausdruck und kein anderes Mittel, als den gesamten Geist der Erde unter dem Bilde des Befruchtetwerdens des mütterlichen Erdenwesens uns zu denken.",
      "Da stehen sich dann zwei Welten gegenüber, nicht einzelne, individuelle Götterfiguren. Und als eine dritte Welt steht jenen zwei Welten das­jenige gegenüber, was man als das Segenskind der beiden empfindet.",
      "Das ist nicht ein individuelles Wesen, nicht eine Empfindung der Seele, sondern etwas, was das Erzeugnis des Himmelsvaters und der Erdenmutter ist. So wird, aus der geistigen Welt heraus, das Verhält­nis von Devachan zur Erde empfunden.",
      "Was da entsteht als der Seg­ner, als der Frühling und als das, was da sprießt und sproßt im ma­teriellen Leibe, das wird durchaus als Geistiges empfunden, und was da sproßt und sprießt in der Seele, das wird empfunden als die Welt, die zugleich empfunden wird als Segenskind vom Himmelsvater und der irdischen Mutter. So universell diese Vorstellungen auch sind, wir finden sie bei den vorgeschobenen slawischen Völkern, die nach Westen vorgedrungen sind.",
      "Als so universelle Empfindung finden wir das bei keiner westeuropäischen Mythologie. Da finden wir klar aus­gearbeitete Göttergestalten, aber nicht dasjenige, was wir in unsern geistigen Planen darstellen; diese finden wir mehr in dem Himmels-vater, in der irdischen Mutter und dem Segenskinde des Ostens.",
      "In dem Segenskinde ist wieder eine Welt darinnen, die eine andere durchdringt. Das ist die Welt, welche allerdings schon individuell vorgestellt wird, weil sie an die physische Sonne mit ihrem Licht ge­knüpft ist.",
      "Dieses Wesen, das uns vielfach in der persischen Mytho­logie entgegengetreten ist, hat auch - allerdings in einer anders aus­gebildeten Empfindungs- und Vorstellungsform - das slawische Ele­ment; es hat das Sonnenwesen, das seine Segnungen hineingießt in die anderen drei Welten, so daß das Schicksal des Menschen eingesponnen ist in die Schöpfung, in die gegebene Erde, durch die Befruchtung der Erdenmutter mit dem Himmelsvater und durch das, was hineinspinnt der Sonnengeist in diese beiden Welten. Eine fünfte Welt ist das, was alles Geistige umfaßt.",
      "Es empfindet das osteuropäische Element in allen Naturkräften und Geschöpfen die zugrunde liegende geistige",
      "Welt. Aber die müssen wir uns in einer ganz anderen Empfindungs­nuance denken, vielleicht mehr mit den Naturwesen, Naturtatsachen und Naturschöpfungen verknüpft.",
      "Wir müssen uns vorstellen, daß diese östliche Seele in der Lage ist, in einem Naturvorgange Wesen zu sehen, nicht bloß das Äußerlich-Physisch-Sinnliche, sondern das Astral-Geistige. Daher die Vorstel­lungen einer ungeheuren Anzahl von Wesenheiten in dieser eigen­artigen geistigen Welt, die sich höchstens vergleichen läßt mit der Welt der Lichtelfen. Die geistige Welt, welche von den geisteswissen­schaftlichen Vorstellungen als die fünfte Welt angesehen wird, ist un­gefähr die Welt, die da aufdämmert dem Volksgemüte des Ostens. Ob Sie sie mit diesem oder jenem Namen benennen, darauf kommt es nicht an, aber darauf kommt es an, daß die Empfindungen nuan­ciert und schattiert sind, daß die Vorstellungen, durch welche dieser fünfte Plan oder diese fünfte geistige Welt charakterisiert worden ist, sich in der Welt des Ostens findet. Mit dieser Empfindung arbeitete diese Welt des Ostens demjenigen Geiste vor, der das Geistselbst in die Menschen hineinbringen soll, für jene Epoche, wo aufsteigen soll die Bewußtseinsseele zum Geistselbst im sechsten nachatlantischen Kulturzeitraum, der unseren fünften ablösen wird. In einer höchst eigenartigen Weise tritt uns das nicht nur in den Schöpfungen der Volksseelen entgegen, die so sind, wie ich sie eben charakterisiert habe, sondern auch in einer wunderbar vorbereitenden Weise in den mancherlei anderen Äußerungen Osteuropas und seiner Kultur.",
      "Es ist sehr merkwürdig und im höchsten Grade interessant, wie die­ser Osteuropäer seine Anlage für Empfänglichkeit dem reinen Geiste gegenüber dadurch ausdrückt, daß er die westeuropäische Kultur mit großer Hingebung aufnahm, dadurch prophetisch andeutend, daß er noch Größeres mit seinem Wesen wird vereinigen können. Daher auch das geringe Interesse, das er den Einzelheiten dieser westeuropäischen Kultur entgegenbringt. Er nimmt das sich Darbietende mehr in gro­ßen Zügen und weniger in den Einzelheiten auf, weil er sich vor­bereitet, dasjenige sich anzueignen, was als Geistselbst in die Mensch­heit hineintreten wird. Insbesondere interessant ist es zu sehen, wie unter diesem Einfluß im Osten ein viel fortgeschrittenerer Christus-Begriff",
      "hat zustande kommen können als in Westeuropa, soweit er dort nicht durch die Geisteswissenschaft zustande gekommen ist. Von allen ihr Fernstehenden hat den fortgeschrittensten Christus-Begriff der russische Philosoph Solowjew.",
      "Er hat einen solchen Christus-Begriff, daß er nur von Schülern der Geist-Erkenntnis verstanden werden kann, weil er ihn immer weiter hinaufentwickelt und in un­endlicher Perspektive zeigt, so daß von ihm gezeigt wird, daß das, was heute die Menschen davon erkennen, nur der Anfang ist, weil der Christus-Impuls erst wenig der Menschheit offenbaren konnte von dem, was er in sich enthält. Aber wenn wir in bezug auf den Christus-Begriff hinschauen, wie er zum Beispiel bei Hegel gefaßt ist, so werden wir finden, daß man sagen kann: Hegel faßt ihn so, wie die feinste, die sublimierteste Bewußtseinsseele ihn fassen kann.",
      "Ganz anders aber tritt uns der Christus-Begriff bei Solowjew ent­gegen. Da wird die Zweigliedrigkeit im Christus-Begriffe klar, und es wird alles dasjenige abgelehnt, was in den verschiedensten theolo­gischen Streitigkeiten zum Ausdruck gekommen ist und was im Grunde genommen auf tiefen Mißverständnissen beruht, weil ge­wöhnliche Begriffe nicht ausreichen, um den Christus-Begriff in sei­ner zweifachen Wesenheit verständlich zu machen, nicht ausreichen, um zu verstehen, daß das Menschliche und das Geistige darin genau unterschieden werden müssen.",
      "Gerade darauf beruht der Christus-Begriff, daß genau gefaßt wird, was geschah, als in den Menschen Jesus von Nazareth, der ausgebildet hatte alle erforderlichen Eigen­schaften, der Christus hineinkam. Da hat man dann zwei Naturen darinnen, die zunächst erfaßt werden müssen, obwohl sie sich auf einer höheren Stufe wieder in eine Einheit zusammenfassen.",
      "So lange hat man den Christus nicht in seiner vollen Gestalt erfaßt, als man diese Zweigliedrigkeit nicht erfaßt hat. Dies kann aber nur dasjenige philosophische Erfassen, das vorausahnt, daß der Mensch selber in eine Kultur hineinkommen wird, wo seine Bewußtseinsseele in dem Zustand sein wird, daß das Geistselbst ihm zukommen kann, so daß der Mensch sich in dieser sechsten Kulturperiode als eine Zweiheit fühlen wird, bei der die höhere Natur die niedere in Zaum und Zügel halten wird.",
      "Diese Zweigliedrigkeit trägt Solowjew in seinen Christus-Begriff hinein und macht ausdrücklich geltend, daß der Christus-Begriff nur dann einen Sinn haben kann, wenn man eine göttliche und eine menschliche Natur annimmt, die nur dadurch, daß sie real zusammen­wirken, daß sie nicht eine abstrakte, sondern eine organische Einheit sind, begriffen werden können. Solowjew erkennt bereits, daß in die­sem Wesen zwei Willenszentren vorgestellt werden müssen.",
      "Wenn Sie die theosophischen Theorien von der wahren Bedeutung der Christus­Wesenheit nehmen, wie sie durch das Vorhandensein des nicht bloß gedachten, sondern spirituell wirklichen indischen Einflusses entstan­den, dann haben Sie da den Christus so, daß in ihm ausgebildet ist in den drei Leibern das Moment des Fühlens, das Moment des Den­kens und das Moment des Wollens. Sie haben da ein menschliches Fühlen, Denken und Wollen, in das sich hineinsenkt das göttliche Fühlen, Denken und Wollen.",
      "Das wird die europäische Menschheit erst ganz verarbeiten, wenn sie zur sechsten Kulturstufe hinaufgestie­gen sein wird. Prophetisch ist das in wunderbarer Weise zum Aus­druck gekommen in dem, was bei Solowjew als Christus-Begriff wie die Morgenröte einer späteren Kultur voranleuchtet.",
      "Daher geht diese Philosophie des östlichen Europa mit solchen Riesenschritten über das Hegeltum und den Kantianismus hinaus, und man fühlt, wenn man in die Atmosphäre dieser Philosophie kommt, plötzlich etwas wie einen Keim einer späteren Entfaltung. Das geht deshalb so weit, weil dieser Christus-Begriff als ein prophetisches Voranleuchten, als die Morgenröte der sechsten nachatlantischen Kultur empfunden wird.",
      "Dadurch wird das ganze Christus-Wesen und die ganze Bedeu­tung des Christus-Wesens für die Philosophie in den Mittelpunkt ge­rückt, und es wird dadurch zu etwas ganz anderem als dem, was die westeuropäischen Begriffe davon zu geben vermögen. Der Christus-Begriff, soweit er auf nicht geisteswissenschaftlichem Gebiete ausge­arbeitet ist und begriffen wird als lebendige Substanz, die hinein-arbeiten soll wie eine geistige Persönlichkeit in alles staatliche und soziale Wesen, - der empfunden wird wie eine Persönlichkeit, in deren Dienerschaft sich der Mensch als «Mensch mit dem Geistselbst» befindet, diese Christus-Persönlichkeit wird in einer wunderbar plastischen",
      "Weise ausgearbeitet in den verschiedenen Auseinandersetzun­gen, die Solowjew gibt über das Johannes-Evangelium und seine Ein­gangsworte. Wiederum nur auf geisteswissenschaftlichem Felde kann sich ein Verständnis für das finden, wie bei Solowjew tief erfaßt wird der Satz: «Im Urbeginne war das Wort oder der Logos», wie anders das Johannes-Evangelium gerade erfaßt wird durch eine Phi­losophie, bei der gefühlt werden kann, daß sie eine keimende Philoso­phie ist, daß sie in einer merkwürdigen Weise in die Zukunft hinein-weist.",
      "Wenn man auf der einen Seite sagen muß, daß Hegel auf philoso­phischein Gebiete eine reifste Frucht darstellt, etwas, was als reifste philosophische Frucht aus der Bewußtseinsseele herausgeboren ist, so ist auf der anderen Seite diese Philosophie Solowjews der Keim in der Bewußtseinsseele für die Philosophie des Geistselbst, das in der sechsten Kulturperiode eingegliedert wird. Es gibt vielleicht keinen größeren Gegensatz, als den im eminentesten Sinne christlichen Staatsbegriff, der als hohes Ideal dem Solowjew wie ein Traum der Zukunft vorschwebt, diesen christlichen Staats- und Volksbegriff, der alles, was da ist, nimmt, um es darzubringen dem herabströmen-den Geistselbst, um es der Zukunft entgegenzuhalten, um es von den Gewalten der Zukunft durchchristen zu lassen - es gibt also keinen größeren Gegensaz, als diesen Begriff der im Solowjewschen Sinne gehaltenen christlichen Gemeinschaft, wobei der Christus-Begriff ein ganz zukünftiger ist, und den Begriff des Gottesstaates des heiligen Augustinus, der den Christus-Begriff zwar aufnimmt, aber den Staat so konstruiert, daß er der römische Staat ist, der den Christus auf­nimmt in die Vorstellung vom Staate, die ihm der römische Staat gegeben hat.",
      "Das, worauf es ankommt, ist dasjenige, was das Wissen abgibt für das in die Zukunft hineinwachsende Christentum. Im So­lowjewschen Staate ist der Christus das Blut, das alles soziale Zusam­menleben durchrinnt.",
      "Und das Wesentliche ist, daß der Staat gedacht wird mit aller Konkretheit der Persönlichkeit, so daß er zwar als geistiges Wesen wirken, aber auch mit allen Charaktereigentümlich­keiten der Persönlichkeit seine Mission erfüllen wird. So sehr durch­drungen von dem Christus-Begriff, der uns vorleuchtet in der Geisteswissenschaft",
      "auf höheren Höhen, und dabei so sehr im Keime geblie­ben ist keine andere Philosophie. Alles, was wir im Osten finden, vom Volksgemüt angefangen bis hinauf zur Philosophie, das erscheint uns als etwas, das erst den Keim einer zukünftigen Entwickelung in sich trägt, und das deshalb auch die besondere Erziehung jenes Zeitgeistes sich hat angedeihen lassen müssen, den wir schon kennen, nachdem wir gesagt haben, daß der Zeitgeist des alten griechischen Volkes, als Impuls dem Christentum gegeben, mit der Mission versehen worden ist, der wirkende Zeitgeist für das spätere Europa zu werden. Dem­jenigen Volksgemüt, das die Keime für den sechsten Kulturzeitraum auszubilden haben wird, hat dieser Zeitgeist nicht allein Erzieher, sondern Pfleger sein müssen von der ersten Stufe des Daseins an. So können wir förmlich sagen - wobei Vater- und Mutterbegriff ihren getrennten Sinn verlieren -, daß das, was russisches Volks-gemüt ist und sich allmählich zur Volksseele entwickeln soll, nicht nur erzogen, sondern ernährt, gesäugt worden ist von demjenigen, wovon wir gesehen haben, daß es aus dem alten griechischen Zeitgeist heraus gebildet worden ist und dann einen anderen Rang nach außen angenommen hat.",
      "So verteilen sich die Missionen zwischen West-, Mittel- und Nord-Europa und dem Osten Europas. Eine Andeutung von diesen Dingen wollte ich Ihnen geben. Wir werden auf der Grundlage dieser An­deutungen noch einige Betrachtungen anstellen und zeigen, wie sich die europäische Zukunft ausnehmen wird, die gelten lassen wird, daß wir unsere Ideale aus solchen Erkenntnissen heraus bilden müssen; wir werden zeigen, wie sich der germanisch-nordische Volksgeist durch diesen Einfluß nach und nach zu einem Zeitgeiste umwandelt."
    ],
    "sentences": [
      [
        "Bevor wir dasjenige entwickeln, was sich in Anknüpfung an das be­deutsame Bild der Götterdämmerung ergeben wird, wird es gut sein, wenn wir uns dafür eine Grundlage schaffen.",
        "Denn es wird sich dar­um handeln, das Wesen der germanisch-nordischen Volksseele aus den gewonnenen Resultaten heraus genauer zu schildern."
      ],
      [
        "Wir müssen se­hen, wie in Europa das gesamte europäische Geistesleben zusammen­wirkt, wie durch die Tätigkeit der verschiedenen Volksgeister ein Fortschritt der Menschheit bewirkt wird - aus uralten Zeiten heraus, durch unsere Gegenwart hindurch, in die Zukunft hinein.",
        "Jedes ein­zelne Volk, ja sogar alle einzelnen, kleineren Volkssplitter haben in diesem großen Gesamtgemälde ihre besondere Aufgabe, und aus dem, was gesagt worden ist, können Sie erkennen, daß, in gewisser Bezie­hung, gerade der vor- und nachchristlichen Kultur Europas die Auf­gabe, die Mission zugefallen ist, das Ich durch die verschiedenen Stu­fen der menschlichen Wesenheit hindurch zu erziehen, es herauszu­bilden und nach und nach zu entwickeln."
      ],
      [
        "Es wurde ja in gewisser Beziehung dieses Ich in uralter Zeit noch aus der geistigen Welt her­aus, wie wir dies am germanisch-nordischen Volke gezeigt haben, hell­seherisch dem Menschen gezeigt.",
        "Es wurde gesagt, wie dieses Ich den Menschen verliehen wird von einem der Engelwesen, das sogar zwi­schen dem Menschen und der Volksseele mitten darinnen steht: von dem Donar oder Thor."
      ],
      [
        "Wir haben gesehen, daß sich der einzelne noch vorkam wie Ich-los, wie unpersönlich.",
        "Er sah das Ich wie eine Gabe an, die ihm aus der geistigen Welt geschenkt wurde."
      ],
      [
        "In solcher Weise hat man natürlich im Orient, als das Ich über­haupt erwachte, das Ich nicht gefunden.",
        "Da war der Mensch schon subjektiv so weit entwickelt zu einer hohen Stufe menschlicher Voll­kommenheit, daß er das Ich nicht als fremdes, sondern als eigenes empfand.",
        "Als der Mensch im Orient zum Ich erwachte, war die orien­talische Kultur schon so weit, daß sie fähig war, eine so fein ausge­sponnene Spekulation, Logik und Weisheit nach und nach zu entwickeln,"
      ],
      [
        "wie wir sie in der orientalischen Weisheit vor uns sehen.",
        "Also den ganzen Prozeß des Empfangens des Ich wie aus einer höhe­ren, geistigen Welt unter der Beihilfe einer solchen göttlich-geistigen Individualität wie der Thor es war, hat der Orientalismus nicht mehr mitgemacht."
      ],
      [
        "Ihn hat mitgemacht der Europäismus, und daher empfin­det dieser Europäismus auch dieses allmähliche Hinaufsteigen zu dem individuellen Ich wie das Herauskommen aus einer Art von Gruppen-seele.",
        "Der germanisch-nordische Mensch fühlte sich selbst noch wie mit einer Gruppenseele behaftet, wie zu einer ganzen Gemeinschaft gehörig, wie ein Glied in der großen Zusammengehörigkeit des Stam­mes."
      ],
      [
        "Nur so konnte es kommen, daß noch fast hundert Jahre, nach­dem der christliche Impuls der Erde gegeben worden ist, Tacitus die Germanen Mitteleuropas so schildern konnte, daß sie immer als zu einzelnen Stämmen gehörig erscheinen, daß sie wie die Glieder eines Organismus sind und zu der Einheit des Organismus gehören.",
        "So fühlte sich der einzelne in jener Zeit noch wie ein Glied des Stammes-Ich."
      ],
      [
        "Er fühlte das nach und nach Heraus-geboren-Werden des indivi­duellen Ich aus dem Stammes-Ich, und er fühlte in dem Gotte Thor den Geber, den Verleiher des Ich, den Gott, der ihn eigentlich mit dem individuellen Ich begabte.",
        "Aber er fühlte diesen Gott noch ver­bunden mit dem gesamten Geiste des Stammes, mit dem, was in der Gruppenseele lebt."
      ],
      [
        "Für diese Gruppenseele findet sich nun der Aus­druck «Sif».",
        "Das ist der Name für die Gemahlin des Thor.",
        "Sif muß sprachlich verwandt sein mit dem Worte Sippe, Stammeszusammen­gehörigkeit und ist es auch in der Tat, wenn das auch maskiert und verborgen ist."
      ],
      [
        "Okkult bedeutet aber Sif die Gruppenseele der einzel­nen Gemeinschaft, aus der herauswächst das einzelne Individuum.",
        "Sif ist diejenige Wesenheit, die sich verbindet mit dem Gotte des indivi­duellen Ich, mit dem Geber des individuellen Ich, mit Thor."
      ],
      [
        "Sif und Thor empfindet der individuelle Mensch als die Wesenheiten, die ihm das Ich gaben.",
        "Die empfand der nordische Mensch noch so, als den Völkern in anderen Gegenden Europas bereits andere Aufgaben in der Erziehung des Menschen zum Ich hin zugeteilt waren."
      ],
      [
        "Jedes einzelne Volk hat seine besondere Aufgabe.",
        "Da finden wir vor allen Dingen dasjenige Volk, diejenige Völkerzusammengehörigkeit,"
      ],
      [
        "diejenige Volksgemeinsamkeit ausgebreitet, die wir unter dem Na­men der Kelten kennen.",
        "Der Volksgeist der Kelten, von dem wir aus den vorangegangenen Darstellungen wissen, daß er später ganz an­dere Aufgaben bekommen hat, hatte die Aufgabe, das noch junge Ich der europäischen Bevölkerung heranzuziehen.",
        "Dazu aber mußte noch eine Erziehung, ein Unterricht der Kelten selbst vorhanden sein, der unmittelbar aus der höheren Welt vermittelt war.",
        "Daher ist es durchaus richtig, daß die Kelten durch ihre Eingeweihten, die Druiden-Priester, einen Unterricht aus höheren Welten erhielten, den sie aus eigener Kraft nicht hätten empfangen können, und den sie an die übrigen Völker dann weiterzugeben hatten."
      ],
      [
        "Die gesamte europäische Kultur ist eine Gabe der europäischen My­sterien.",
        "Die fortschreitenden Volksseelen sind immer die Lenker der Gesamtkultur der Menschheit in ihrem Fortschritt.",
        "Aber in der Zeit, in welcher diese Volksgeister Europas die Menschen dazu anleiten sollten, aus sich selber heraus zu arbeiten, aus sich selber heraus wirk­sam zu sein, war es notwendig, daß sich die Mysterien mehr zurück-zogen."
      ],
      [
        "Daher trat mit dem Zurückziehen des keltischen Elementes auch eine Art Zurückziehung der Mysterien in viel geheimere Unter­gründe ein.",
        "Ein viel direkterer, unmittelbarer Verkehr der Geistes-wesen mit dem Volke durch die Mysterien war zur Zeit der alten Kelten vorhanden, weil das Ich noch gebunden war an die Gruppen­haftigkeit, und doch sollte das keltische Element der Verleiher des Ich für die übrige Bevölkerung sein."
      ],
      [
        "Wir können also sagen: In der Zeit, die vor der eigentlichen germanisch-nordischen Entwickelung liegt, konnte nur durch die alten keltischen Mysterien der europäischen Kultur die Mysterien-Erziehung gegeben werden.",
        "Diese Mysterien-Erziehung hat gerade so viel an die Oberfläche kommen lassen, als notwendig war, um eine Grundlage für die gesamte Kultur Europas zu geben."
      ],
      [
        "Aus dieser alten Kultur haben sich nun durch Vermischung mit den verschiedensten Rassensplittern, Volksbestandteilen und Ras­sengemeinschaften die verschiedensten Volksseelen und Volksgeister befruchten können und haben immer das Ich in andere Lagen ge­bracht, um es zu erziehen, das Ich, das sich herauswühlte aus dem Un­tergrunde dessen, was unter dem Ich des Menschen liegt."
      ],
      [
        "Man kann sagen, daß, nachdem die alte griechische Kultur bis zu einem gewissen Grade ihren Höhepunkt erreicht hatte in der Ausbil­dung desjenigen, was sie eben als ihre besondere Mission hatte, eine ganz andere Seite dieser selben Mission im alten Römertum und seinen verschiedenen Kulturperioden zutage trat.",
        "Wir haben bereits er­wähnt, wie in einer strengen Stufenfolge aufeinanderfolgen die ein­zelnen nachatlantischen Kulturen.",
        "Wenn wir uns einen Überblick ver­schaffen wollen über diese Stufenfolge der nachatlantischen Kulturen, so können wir sagen: Die alte indische Kultur arbeitete am mensch­lichen Ätherleibe.",
        "Daher der hellsichtige, wunderbar weisheitsvolle Charakter der alten indischen Kultur, weil sie - nach Ausbildung der besonderen menschlichen Fähigkeiten - eine im menschlichen Äther-leibe reflektierte Kultur ist, so daß wir die alte indische Kultur etwa in der folgenden Weise fassen können."
      ],
      [
        "Von der atlantischen bis zur späteren nachatlantischen Zeit hat der indische Volksgeist die ganze Entwickelung der inneren Seelen-kräfte durchgemacht, ohne daß sein Ich erwacht war.",
        "Er hat dann wieder den Weg zurück genommen bis zu seiner Arbeit im menschlichen"
      ],
      [
        "Ätherleibe.",
        "Das ist das Wesentliche der alten indischen Kultur, daß mit fertig ausgebildeten Seelenkräften, mit Seelenkräften, die im höchsten Grade verfeinert waren, der Inder wiederum hineingeht in den Ätherleib, zurückgeht bis zum Ätherleib und in demselben jene wunderbar feinen Kräfte ausbildet, deren späterer Reflex wir in den Veden und in noch verfeinerterem Zustande in der Vedanta-Philoso­phie sehen."
      ],
      [
        "Das war alles nur möglich dadurch, daß sich die indische Volksseele bis zu einem hohen Grade entwickelt hatte, bevor das Ich angeschaut, wahrgenommen worden ist, und schon wieder zu einer Zeit, als der Mensch mit den Kräften des Ätherleibes selber sehen konnte.",
        "Die persische Volksseele war nicht so weit gekommen."
      ],
      [
        "Die war nur so weit gekommen, in dem Empfindungsleibe oder Astral­leibe wahrzunehmen.",
        "Noch anders war es in der babylonisch-chal­däisch-ägyptischen Kultur.",
        "Da war es so, daß der Teil, den wir als die Empfindungsseele bezeichnen, wahrnehmen konnte."
      ],
      [
        "Wir müssen also diese ägyptisch-chaldäische Kultur als eine solche bezeichnen, welche in der Empfindungsseele arbeitet.",
        "Beim griechisch-lateinischen Volks-geiste war das so, daß er geleitet worden ist bis zur Verstandes- oder Gemütsseele; in dieser Verstandes- oder Gemütsseele arbeitete er."
      ],
      [
        "An der Verstandes- oder Gemütsseele konnte er selbst nur dadurch arbei­ten, daß diese Verstandes- oder Gemütsseele wiederum im Ätherleibe eine Art Ausprägung ihres Wesens hatte.",
        "Aber es ist dies gleichsam eine weniger reale, weniger anschauliche und der Wirklichkeit einge­prägte Form des Weltbildes, wie es jetzt im Griechentum herauskam."
      ],
      [
        "Während ein unmittelbares Arbeiten im Ätherleibe bei der alten indi­schen Kultur da war, ist jetzt ein verwischtes, ein abgeschattetes, ein matteres Abbild der Wirklichkeit vorhanden, wie ich es charakteri­siert habe dadurch, daß ich sagte: Es ist wie eine Erinnerung an das, was diese Völker einst erlebt hatten, wie eine Erinnerung, die zurück-strahlt auf ihren Ätherleib (vgl. die schematische Abbildung)."
      ],
      [
        "Bei den anderen Völkern, die jetzt auf das griechische Volk folgten, haben wir es zu tun mit dem vorzugsweisen Gebrauche des physischen Leibes zur stufenweisen Ausbildung der Bewußtseinsseele.",
        "Daher war die griechische Kultur eine solche, die wir nur begreifen können, wenn wir sie aus dem Innern heraus zu begreifen vermögen; wenn wir uns"
      ],
      [
        "klar sind, daß bei ihr als äußere Erfahrung wichtig ist, was aus dem Innern des Griechen heraussprudelt.",
        "Dagegen haben die Völker, die mehr nach Westen und Norden gelegen sind, die Aufgabe, unter Lei­tung ihrer Volksseelen den Blick in die Welt hinauszurichten und das in der Welt zu sehen, was auf dem physischen Plane zu sehen ist, auszubilden das, was auf dem physischen Plane eine Rolle spielen soll.",
        "Die germanisch-nordischen Völker hatten noch die besondere Auf­gabe, daß sie das alles so ausbilden sollten, wie sie es ausbilden konn­ten, da sie noch die Gnade, die welthistorische Gnade genossen, im alten Hellsehen hineinzusehen in die geistige Welt und hineinzutragen die uralten Erfahrungen, die sie wie lebendig empfanden, in das, was auf dem physischen Plane eingerichtet werden sollte."
      ],
      [
        "Ein Volk gab es, das in seiner späteren Zeit diese Gnade nicht mehr hatte, ein Volk, das keine solche Vorentwicklung zunächst durch­gemacht hatte, das daher gleichsam wie mit einem Sprung vor die Geburt des menschlichen Ich auf dem physischen Plane gestellt wur­de und daher nur unter Anleitung seiner Volksseele, seines Erzengels für alles das sorgen konnte, was dieses menschliche Ich auf dem phy­sischen Plane förderte, was zur Wohlfahrt dieses menschlichen Ich auf dem physischen Plane notwendig war.",
        "Dies war das römische Volk."
      ],
      [
        "Alles, was das römische Volk unter Anleitung seines Volksgei­stes für die gesamte Mission Europas zu leisten hatte, war dazu be­stimmt, dem Ich des Menschen als solchem Geltung zu verschaffen.",
        "Daher konnte das römische Volk dasjenige ausbilden, was das Ich zwischen die anderen Iche hineinstellt."
      ],
      [
        "Es konnte die ganze Summe der Privatrechte begründen.",
        "Daher wurde es der Schöpfer der Juris­prudenz, die rein auf das Ich gebaut ist.",
        "Wie das Ich dem Ich gegen­übersteht, das war die große Frage in der Mission des römischen Vol­kes."
      ],
      [
        "Die anderen Völker, die aus der Kultur des römischen Volkes herausgewachsen sind, hatten schon mehr von dem, was sozusagen aus der Empfindungsseele, aus der Verstandes- oder Gemütsseele und aus der Bewußtseinsseele selbst heraus dieses Ich in irgendeiner Weise be­fruchtet, dieses Ich in die Welt hineintreibt.",
        "Dazu waren notwendig alle von der äußeren Geschichte aufgezählten Rassenvermischungen, die auf der italischen und pyrenäischen Halbinsel, im heutigen"
      ],
      [
        "Frankreich und im heutigen Großbritannien zustande gekommen sind, um das Ich nach den verschiedenen Nuancen, nach der Empfin­dungsseele, nach der Verstandes- oder Gemütsseele und nach der Bewußtseinsseele auszubilden auf dem physischen Plan.",
        "Das war die große Mission der Völker, die sich nach und nach im Westen Europas in der verschiedensten Weise ausgebildet haben."
      ],
      [
        "Alle einzelnen Kulturnuancen und Missionen im Westen Europas finden zuletzt ihre Erklärung darin, daß in der Richtung nach der italischen und pyrenäischen Halbinsel hin dasjenige auszubilden war, was durch die Impulse der Empfindungsseele in das Ich hinein ausgebildet werden konnte.",
        "Studieren Sie die einzelnen Volkscharak­tere nach ihren Licht- und Schattenseiten, da werden Sie finden, daß Sie bei den Völkern der italischen und pyrenäischen Halbinsel die eigentümliche Mischung des Ich mit der Empfindungsseele haben."
      ],
      [
        "Bei den Völkern aber, die auf Frankreichs Boden bis in die neueste Zeit herauf gelebt haben, werden Sie ihre Eigenart begreiflich finden, wenn Sie das Werden und die Vermischungen der Verstandes- oder Gemütsseele mit dem Ich betrachten.",
        "Die großen, welthistorischen Er­folge aber, als deren Repräsentant wir Großbritannien betrachten können, sind darauf zurückzuführen, daß der Impuls der Bewußt­seinsseele in das menschliche Ich hineingedrängt worden ist."
      ],
      [
        "Mit dem, was als welthistorische Mission aus den britischen Ländern hervor­ging, ist auch zusammenhängend das, was aus der Begründung der äußeren, staatsrechtlichen Form hervorging.",
        "Die Verbindung der Be­wußtseinsseele mit dem Ich war noch nicht innerlich vorhanden."
      ],
      [
        "Wenn Sie aber durchschauen, wie diese Verbindung der Bewußtseins­seele mit dem nach außen getriebenen Ich zustande kam, so werden Sie finden, daß die großen welthistorischen Eroberungen der Bevöl­kerung jener Insel von diesem Impulse herrühren.",
        "Sie finden aber auch, daß das, was da geschieht an Begründungen der parlanientari­schen Regierungsformen, sofort verständlich wird, wenn man weiß, daß damit ein Impuls der Bewußtseinsseele auf den Plan der Welt­geschichte hingestellt werden sollte."
      ],
      [
        "Es waren also viele Nuancen notwendig, denn durch viele Stufen des Ich waren die einzelnen Völker zu führen.",
        "Wir würden wahre Geschichtsbilder"
      ],
      [
        "finden, wenn wir Zeit genug hätten, diese Dinge weiter zu verfolgen, die uns zeigen, wie die Grundkräfte sich verzweigen und sich in der verschiedensten Weise auswirken.",
        "So wirkte die See­lenkonstitution bei den westlichen Völkern, die für sich selbst nicht die unmittelbare, elementare Erinnerung hatten an die hellseherisch erlebten Dinge der geistigen Welt von früher."
      ],
      [
        "Ganz anders mußte in der späteren Zeit im germanisch-nordischen Gebiet sich ausbilden das­jenige, was unmittelbar aus einer nach und nach erfolgten Entwicke­lung des schon in die Empfindungsseele hineingegossenen, ursprüng­lichen Hellsehens hervorging.",
        "Daher jener Zug der Innerlichkeit, der ja nur die Nachwirkung innerlicher, in der Vorzeit erfolgter hellsehe­rischer Erfahrung ist."
      ],
      [
        "Die südlich-germanischen Völker hatten zu­nächst ihre Aufgabe auf dem Gebiet der Bewußtseinsseele.",
        "Die grie­chisch-lateinische Zeit hatte auszubilden die Verstandes- oder Ge­mütsseele.",
        "Sie hatte aber nicht bloß den Impuls zu geben mit der Ver­standes- oder Gemütsseele, sie hatte hineinzuwirken mit einer wun­derbaren, mit hellseherischer Erfahrung ausgestatteten vorzeitlichen Entwickelung."
      ],
      [
        "Das alles ergoß sich in die Bewußtseinsseelen der mittel­europäisch-nordisch-germanischen Völker.",
        "Das wirkte bei diesen als Seelenanlage nach, und die südlicheren Teile der germanischen Mensch­heit hatten zunächst auszubilden das, was dazu gehört, um die Be­wußtseinsseele innerlich vorzubereiten, innerlich mit dem auf den physischen Plan umgesetzten Bewußtseinsinhalt des alten Hellsehens zu erfüllen."
      ],
      [
        "Scheinbar liegen weit ab von dem mythologischen Gebiet die Phi­losophien Mitteleuropas, diese Philosophien, welche Fichte, Schelling und Hegel noch im neunzehnten Jahrhundert vertraten.",
        "Dennoch sind sie nichts anderes, als das Resultat des sublimiertesten alten Hell­sehens, des im Innern des Menschen eroberten Zusammenarbeitens mit göttlich-geistigen Mächten.",
        "Unmöglich hätte sonst ein Hegel in seinen Jdeen Realitäten sehen können, unmöglich hätte ein Hegel den son­derbaren Ausspruch tun können, der ihn so sehr charakterisiert, in­dem er auf die Frage: «Was ist das Abstrakte?» antwortet: «Das Abstrakte ist zum Beispiel ein einzelner Mensch, der seine täglichen Verrichtungen tut, nehmen wir an: ein Zimmermann.» Dasjenige also,"
      ],
      [
        "was für den Abstraktling etwas Konkretes ist, das war für Hegel etwas Abstraktes.",
        "Das, was für den Abstraktling nur Gedanken sind, das waren für ihn große, gewaltige Werkmeister der Welt.",
        "Die Ideen­welt Hegels ist der letzte sublimierteste Ausdruck der Bewusstseins-seele und enthält in reinen Begriffen das, was der nordische Mensch noch als sinnlich-übersinnliche, göttlich-geistige Mächte gesehen hat in Verbindung mit dem Ich.",
        "Und als bei Fichte das Ich zum Ausdruck kam, da war es nichts anderes als der Niederschlag dessen, was der Gott Thor der menschlichen Seele gegeben hat, von Fichte nur gesehen aus der Bewußtseinsseele, in dem scheinbar ärmsten Gedanken, dem Gedanken «Ich bin», von dem die Fichtesche Philosophie ausgeht.",
        "Eine gerade Entwickelungslinie geht von der Begabung des alten nor­dischen Volkes mit dem Ich ausströmend durch den Gott Thor oder Donar aus der Geistwelt bis in die Philosophie.",
        "Dieser Gott hatte das alles vorzubereiten für die Bewußtseinsseele, damit sie einen ihr angemessenen Inhalt habe, denn sie ist darauf angewiesen, in die äußere Welt hineinzuschauen und innerhalb dieser Welt zu wirken.",
        "Aber diese Philosophie findet nicht bloß die äußere, grobsinnliche, materialistische Erfahrung, sondern sie findet den Inhalt der Be­wußtsseinsseele selber in der äußeren Welt und sieht die Natur nur an als die Idee in ihrem Anderssein.",
        "Nehmen Sie diesen fortwirkenden Impuls, so haben Sie darin die Mission der germanisch-nordischen Völker in Mitteleuropa."
      ],
      [
        "Nun müssen wir uns fragen, da alle Entwickelung einen Fortgang zu nehmen hat: Wie schreitet diese Evolution vorwärts?",
        "Wir können da Merkwürdiges sehen, wenn wir in ältere Zeiten zurückschauen.",
        "Wir haben gesagt: Im alten Indertum fand die erste Kultur im Äther-leibe statt, nachdem die entsprechende Ausbildung der geistigen Kräf­te da war.",
        "Es gibt aber auch noch Kulturen, die sich die alte, atlan­tische Kultur bewahrt und sie hineingetragen haben in die Menschen der nachatlantischen Zeit.",
        "Während der Inder von dieser Seite aus an seinen Ätherleib herankommt und aus diesem heraus, mit den Kräf­ten desselben, seine gewaltig große Kultur und sein großartiges Gei­stesleben schafft, haben wir von der anderen Seite eine Kultur, wel­che im Atlantiertum wurzelt und hineinarbeitet in die nachatlantische"
      ],
      [
        "Zeit eine Kultur, welche gleichsam zu ihrer Begründung und Ausbil­dung die andere Seite des Ätherleib-Bewußtseins herausarbeitet.",
        "Das ist die chinesische Kultur.",
        "Die Einzelheiten der chinesischen Kultur werden Sie begreifen, wenn Sie diesen Zusammenhang ins Auge fas­sen und sich erinnern, daß die atlantische Kultur ein unmittelbares Verhältnis hatte zu dem, was wir in unseren früheren Darstellungen den «Großen Geist» nannten, so daß also diese Kultur ein unmittel­bares Verhältnis hatte zu den höchsten Stufen der Weltentwickelung.",
        "Aber diese Kultur wirkt noch hinein in moderne Menschenkörper, und zwar von einer ganz anderen Seite.",
        "Daher wird auch begreiflich erscheinen, daß gerade in diesen beiden Kulturen einmal zusammen­stoßen werden die zwei großen Gegensätze der nachatlantischen Zeit:"
      ],
      [
        "das Indertum, das in gewissen Grenzen entwickelungsfähig ist, und das Chinesentum, das sich abschließt und starr bleibt, das wiederholt, was in der alten atlantischen Zeit da war.",
        "Man bekommt förmlich den Eindruck von einer okkult-wissenschaftlich-poetischen Art, wenn man das Chinesenreich in seiner Entwickelung beobachtet, wenn man an die chinesische Mauer denkt, die nach allen Seiten hin dasjenige abschließen sollte, was aus den uralten Zeiten stammte und in der nachatlantischen Zeit sich entwickelt hatte."
      ],
      [
        "Ich sage jetzt, es be­schleicht einen etwas wie eine poetisch-okkulte Empfindung, wenn man die chinesische Mauer vergleicht mit dem, was es einmal in frü­heren Zeiten gegeben hat.",
        "Ich kann diese Dinge nur andeuten."
      ],
      [
        "Sie werden finden, wenn Sie dies mit den heute schon vorhandenen wis­senschaftlichen Ergebnissen vergleichen, wie außerordentlich auf­schlußgebend diese Dinge sind.",
        "Betrachten wir hellseherisch den alten Kontinent der atlantischen Welt, den wir zu suchen haben da, wo jetzt der Atlantische Ozean ist, zwischen Afrika und Europa einer­seits und Amerika anderseits."
      ],
      [
        "Dieser Kontinent war umschlossen von einer Art von warmem Strom, von einem Strom, bezüglich dessen das hellseherische Bewußtsein ergibt, daß er, so sonderbar es klingen mag, von Süden heraufging, durch die Baffins-Bai gegen das nörd­liche Grönland verlaufend und es umfassend, dann herüberfloß nach Osten, sich allmählich abkühlte, dann in der Zeit, in welcher Sibirien und Rußland noch lange nicht zur Erdoberfläche gehoben waren, in"
      ],
      [
        "der Gegend des Ural hinunterfloß, sich umkehrte, die östlichen Kar­pathen berührte, in die Gegend hineinfloß, wo die heutige Sahara ist, und endlich beim Meerbusen von Biskaya dem Atlantischen Ozean zuging, so daß er ein ganz geschlossenes Stromgebiet hatte.",
        "Sie wer­den begreifen, daß dieser Strom nur noch in den allerletzten Resten vorhanden sein kann.",
        "Dieser Strom ist der Golfstrom, der einst den atlantischen Kontinent umflossen hat. - Und jetzt werden Sie auch begreifen, daß bei den Griechen das Seelenleben Erinnerung ist.",
        "Es tauchte in ihnen auf das Bild des Okeanos, der eine Erinnerung ist an jene atlantische Zeit.",
        "Ihr Weltbild ist nicht so unrichtig, weil es aus der alten atlantischen Zeit geschöpft ist. - Den Strom, der über Spitz­bergen als warmer Strom herunterkam und nach und nach sich ab­kühlte usw., dieses geschlossene Stromgebiet haben sich die Chinesen förmlich wiedererschaffen in ihrer von der Mauer umschlossenen, aus der atlantischen Zeit herübergeretteten Kultur.",
        "Das Geschichtliche war in der atlantischen Kultur noch nicht vorhanden.",
        "Daher hat auch die chinesische Kultur etwas Ungeschichtliches behalten.",
        "Daher haben wir da etwas Vorindisches, etwas aus der Atlantis Stammendes."
      ],
      [
        "Wenden wir uns jetzt zu der Schilderung im Weitergange des ger­manisch-nordischen Volksgeistes zu dem, was auf ihn folgt.",
        "Was wird das nächste sein, wenn ein Volksgeist sein Volk so leitet, daß das Geistselbst sich besonders entwickeln kann?",
        "Erinnern wir uns daran, daß der Ätherleib in der indischen Kultur, der Empfindungsleib in der persischen Kultur, die Empfindungsseele in der ägyptisch-chal­däischen Kultur, die Verstandes- oder Gemütsseele in der griechisch-lateinischen Kultur, die Bewußtseinsseele in unserer, noch nicht abge­schlossenen Kultur zur Entwickelung kommt.",
        "Nun folgt aber das Er­greifen des Geistselbst durch die Bewußtseinsseele, so daß hinein­leuchtet das Geistselbst in die Bewußtseinsseele, was als Aufgabe der sechsten Kulturstufe nach und nach vorbereitet werden muß.",
        "Diese Kultur, die im eminentesten Sinne eine empfängliche Kultur sein muß, denn sie muß hingebungsvoll das Hereindringen des Geistselbst in die Bewußtseinsseele abwarten, wird vorbereitet durch die Völker West­asiens und die vorgeschobenen slawischen Völker Osteuropas.",
        "Die letzteren sind aus gutem Grunde mit ihren Volksseelen vorgeschoben,"
      ],
      [
        "aus dem Grunde, weil alles, was in Zukunft kommen wird, in einer gewissen Weise seine Vorbereitung vorher erfahren muß, sich schon hineinschieben muß, um die Elemente für das Spätere abzugeben.",
        "Im höchsten Grade interessant ist es, diese vorgeschobenen Posten einer für die späteren Epochen sich vorbereitenden Volksseele zu studieren."
      ],
      [
        "Daher das Eigenartige der für uns zunächst östlich wohnenden slawi­schen Völker.",
        "Ihre ganze Kultur mutet den Westeuropäer an als sich im Vorbereitungsstadium befindend, und in sonderbarer Weise schie­ben sie vor, durch die Medien ihrer vorgeschobenen Posten, dasjenige, was dem Geiste nach etwas ganz anderes ist, als irgendeine Mytho­logie."
      ],
      [
        "Es würde verkennen heißen dasjenige, was von Osten herüber vorgeschoben wird als zu erwartende Kultur, es würde diese Kultur verkennen heißen, wenn man sie vergleichen wollte mit dem, was die westeuropäischen Völker in sich haben, die einen geradlinig fortlau­fenden Impuls, der noch im alten Hellsehen seine Wurzel und Quelle hat, besitzen.",
        "Das Eigenartige, wodurch sich die Seele dieser osteuro­päischen Völker darlebt, das drückt sich in dem ganzen Verhältnis aus, das diese Völker immer offenbarten, wenn ihre Beziehungen zu den höheren Welten in Betracht kamen."
      ],
      [
        "Diese Beziehung ist, wenn wir sie mit dem vergleichen, was sich in unseren Mythologien, in Westeuropa, zeigt, mit den sonderbaren, bis ins Individuelle ausge­arbeiteten Götterfiguren, etwas ganz anderes.",
        "Sie tritt uns so entgegen, daß wir das, was sie uns gibt als unmittelbaren Ausfluß des Volks-wesens vergleichen können mit unsern verschiedenen Planen oder Wel­ten, durch die wir uns vorbereiten zum Begreifen einer geistigen, höheren Kultur."
      ],
      [
        "Da finden wir zum Beispiel im Osten folgende Vor­stellung: Empfangen hat der Westen aufeinanderfolgende, nebenein­anderliegende Welten.",
        "Wir haben da zunächst ein deutliches Bewußt­sein von einer Welt des kosmischen Vaters."
      ],
      [
        "Alles dasjenige, was in Luft und Feuer, was überhaupt in den Elementen, die in und über der Erde sich finden, schöpferisch tätig ist, das tritt uns wie in einem großen, umfassenden Gesamtbegriffe, der zugleich Gesamtempfindung ist, entgegen als der Begriff des Himmelsvaters.",
        "So wie wir uns etwa die Welt des Devachan unsere Erde befruchtend denken, so tritt uns diese Himmelswelt, diese väterliche Welt, von Osten her entgegen,"
      ],
      [
        "und sie befruchtet dasjenige, was als Mütterliches empfunden wird, den Geist der Erde.",
        "Wir haben keinen anderen Ausdruck und kein anderes Mittel, als den gesamten Geist der Erde unter dem Bilde des Befruchtetwerdens des mütterlichen Erdenwesens uns zu denken."
      ],
      [
        "Da stehen sich dann zwei Welten gegenüber, nicht einzelne, individuelle Götterfiguren.",
        "Und als eine dritte Welt steht jenen zwei Welten das­jenige gegenüber, was man als das Segenskind der beiden empfindet."
      ],
      [
        "Das ist nicht ein individuelles Wesen, nicht eine Empfindung der Seele, sondern etwas, was das Erzeugnis des Himmelsvaters und der Erdenmutter ist.",
        "So wird, aus der geistigen Welt heraus, das Verhält­nis von Devachan zur Erde empfunden."
      ],
      [
        "Was da entsteht als der Seg­ner, als der Frühling und als das, was da sprießt und sproßt im ma­teriellen Leibe, das wird durchaus als Geistiges empfunden, und was da sproßt und sprießt in der Seele, das wird empfunden als die Welt, die zugleich empfunden wird als Segenskind vom Himmelsvater und der irdischen Mutter.",
        "So universell diese Vorstellungen auch sind, wir finden sie bei den vorgeschobenen slawischen Völkern, die nach Westen vorgedrungen sind."
      ],
      [
        "Als so universelle Empfindung finden wir das bei keiner westeuropäischen Mythologie.",
        "Da finden wir klar aus­gearbeitete Göttergestalten, aber nicht dasjenige, was wir in unsern geistigen Planen darstellen; diese finden wir mehr in dem Himmels-vater, in der irdischen Mutter und dem Segenskinde des Ostens."
      ],
      [
        "In dem Segenskinde ist wieder eine Welt darinnen, die eine andere durchdringt.",
        "Das ist die Welt, welche allerdings schon individuell vorgestellt wird, weil sie an die physische Sonne mit ihrem Licht ge­knüpft ist."
      ],
      [
        "Dieses Wesen, das uns vielfach in der persischen Mytho­logie entgegengetreten ist, hat auch - allerdings in einer anders aus­gebildeten Empfindungs- und Vorstellungsform - das slawische Ele­ment; es hat das Sonnenwesen, das seine Segnungen hineingießt in die anderen drei Welten, so daß das Schicksal des Menschen eingesponnen ist in die Schöpfung, in die gegebene Erde, durch die Befruchtung der Erdenmutter mit dem Himmelsvater und durch das, was hineinspinnt der Sonnengeist in diese beiden Welten.",
        "Eine fünfte Welt ist das, was alles Geistige umfaßt."
      ],
      [
        "Es empfindet das osteuropäische Element in allen Naturkräften und Geschöpfen die zugrunde liegende geistige"
      ],
      [
        "Welt.",
        "Aber die müssen wir uns in einer ganz anderen Empfindungs­nuance denken, vielleicht mehr mit den Naturwesen, Naturtatsachen und Naturschöpfungen verknüpft."
      ],
      [
        "Wir müssen uns vorstellen, daß diese östliche Seele in der Lage ist, in einem Naturvorgange Wesen zu sehen, nicht bloß das Äußerlich-Physisch-Sinnliche, sondern das Astral-Geistige.",
        "Daher die Vorstel­lungen einer ungeheuren Anzahl von Wesenheiten in dieser eigen­artigen geistigen Welt, die sich höchstens vergleichen läßt mit der Welt der Lichtelfen.",
        "Die geistige Welt, welche von den geisteswissen­schaftlichen Vorstellungen als die fünfte Welt angesehen wird, ist un­gefähr die Welt, die da aufdämmert dem Volksgemüte des Ostens.",
        "Ob Sie sie mit diesem oder jenem Namen benennen, darauf kommt es nicht an, aber darauf kommt es an, daß die Empfindungen nuan­ciert und schattiert sind, daß die Vorstellungen, durch welche dieser fünfte Plan oder diese fünfte geistige Welt charakterisiert worden ist, sich in der Welt des Ostens findet.",
        "Mit dieser Empfindung arbeitete diese Welt des Ostens demjenigen Geiste vor, der das Geistselbst in die Menschen hineinbringen soll, für jene Epoche, wo aufsteigen soll die Bewußtseinsseele zum Geistselbst im sechsten nachatlantischen Kulturzeitraum, der unseren fünften ablösen wird.",
        "In einer höchst eigenartigen Weise tritt uns das nicht nur in den Schöpfungen der Volksseelen entgegen, die so sind, wie ich sie eben charakterisiert habe, sondern auch in einer wunderbar vorbereitenden Weise in den mancherlei anderen Äußerungen Osteuropas und seiner Kultur."
      ],
      [
        "Es ist sehr merkwürdig und im höchsten Grade interessant, wie die­ser Osteuropäer seine Anlage für Empfänglichkeit dem reinen Geiste gegenüber dadurch ausdrückt, daß er die westeuropäische Kultur mit großer Hingebung aufnahm, dadurch prophetisch andeutend, daß er noch Größeres mit seinem Wesen wird vereinigen können.",
        "Daher auch das geringe Interesse, das er den Einzelheiten dieser westeuropäischen Kultur entgegenbringt.",
        "Er nimmt das sich Darbietende mehr in gro­ßen Zügen und weniger in den Einzelheiten auf, weil er sich vor­bereitet, dasjenige sich anzueignen, was als Geistselbst in die Mensch­heit hineintreten wird.",
        "Insbesondere interessant ist es zu sehen, wie unter diesem Einfluß im Osten ein viel fortgeschrittenerer Christus-Begriff"
      ],
      [
        "hat zustande kommen können als in Westeuropa, soweit er dort nicht durch die Geisteswissenschaft zustande gekommen ist.",
        "Von allen ihr Fernstehenden hat den fortgeschrittensten Christus-Begriff der russische Philosoph Solowjew."
      ],
      [
        "Er hat einen solchen Christus-Begriff, daß er nur von Schülern der Geist-Erkenntnis verstanden werden kann, weil er ihn immer weiter hinaufentwickelt und in un­endlicher Perspektive zeigt, so daß von ihm gezeigt wird, daß das, was heute die Menschen davon erkennen, nur der Anfang ist, weil der Christus-Impuls erst wenig der Menschheit offenbaren konnte von dem, was er in sich enthält.",
        "Aber wenn wir in bezug auf den Christus-Begriff hinschauen, wie er zum Beispiel bei Hegel gefaßt ist, so werden wir finden, daß man sagen kann: Hegel faßt ihn so, wie die feinste, die sublimierteste Bewußtseinsseele ihn fassen kann."
      ],
      [
        "Ganz anders aber tritt uns der Christus-Begriff bei Solowjew ent­gegen.",
        "Da wird die Zweigliedrigkeit im Christus-Begriffe klar, und es wird alles dasjenige abgelehnt, was in den verschiedensten theolo­gischen Streitigkeiten zum Ausdruck gekommen ist und was im Grunde genommen auf tiefen Mißverständnissen beruht, weil ge­wöhnliche Begriffe nicht ausreichen, um den Christus-Begriff in sei­ner zweifachen Wesenheit verständlich zu machen, nicht ausreichen, um zu verstehen, daß das Menschliche und das Geistige darin genau unterschieden werden müssen."
      ],
      [
        "Gerade darauf beruht der Christus-Begriff, daß genau gefaßt wird, was geschah, als in den Menschen Jesus von Nazareth, der ausgebildet hatte alle erforderlichen Eigen­schaften, der Christus hineinkam.",
        "Da hat man dann zwei Naturen darinnen, die zunächst erfaßt werden müssen, obwohl sie sich auf einer höheren Stufe wieder in eine Einheit zusammenfassen."
      ],
      [
        "So lange hat man den Christus nicht in seiner vollen Gestalt erfaßt, als man diese Zweigliedrigkeit nicht erfaßt hat.",
        "Dies kann aber nur dasjenige philosophische Erfassen, das vorausahnt, daß der Mensch selber in eine Kultur hineinkommen wird, wo seine Bewußtseinsseele in dem Zustand sein wird, daß das Geistselbst ihm zukommen kann, so daß der Mensch sich in dieser sechsten Kulturperiode als eine Zweiheit fühlen wird, bei der die höhere Natur die niedere in Zaum und Zügel halten wird."
      ],
      [
        "Diese Zweigliedrigkeit trägt Solowjew in seinen Christus-Begriff hinein und macht ausdrücklich geltend, daß der Christus-Begriff nur dann einen Sinn haben kann, wenn man eine göttliche und eine menschliche Natur annimmt, die nur dadurch, daß sie real zusammen­wirken, daß sie nicht eine abstrakte, sondern eine organische Einheit sind, begriffen werden können.",
        "Solowjew erkennt bereits, daß in die­sem Wesen zwei Willenszentren vorgestellt werden müssen."
      ],
      [
        "Wenn Sie die theosophischen Theorien von der wahren Bedeutung der Christus­Wesenheit nehmen, wie sie durch das Vorhandensein des nicht bloß gedachten, sondern spirituell wirklichen indischen Einflusses entstan­den, dann haben Sie da den Christus so, daß in ihm ausgebildet ist in den drei Leibern das Moment des Fühlens, das Moment des Den­kens und das Moment des Wollens.",
        "Sie haben da ein menschliches Fühlen, Denken und Wollen, in das sich hineinsenkt das göttliche Fühlen, Denken und Wollen."
      ],
      [
        "Das wird die europäische Menschheit erst ganz verarbeiten, wenn sie zur sechsten Kulturstufe hinaufgestie­gen sein wird.",
        "Prophetisch ist das in wunderbarer Weise zum Aus­druck gekommen in dem, was bei Solowjew als Christus-Begriff wie die Morgenröte einer späteren Kultur voranleuchtet."
      ],
      [
        "Daher geht diese Philosophie des östlichen Europa mit solchen Riesenschritten über das Hegeltum und den Kantianismus hinaus, und man fühlt, wenn man in die Atmosphäre dieser Philosophie kommt, plötzlich etwas wie einen Keim einer späteren Entfaltung.",
        "Das geht deshalb so weit, weil dieser Christus-Begriff als ein prophetisches Voranleuchten, als die Morgenröte der sechsten nachatlantischen Kultur empfunden wird."
      ],
      [
        "Dadurch wird das ganze Christus-Wesen und die ganze Bedeu­tung des Christus-Wesens für die Philosophie in den Mittelpunkt ge­rückt, und es wird dadurch zu etwas ganz anderem als dem, was die westeuropäischen Begriffe davon zu geben vermögen.",
        "Der Christus-Begriff, soweit er auf nicht geisteswissenschaftlichem Gebiete ausge­arbeitet ist und begriffen wird als lebendige Substanz, die hinein-arbeiten soll wie eine geistige Persönlichkeit in alles staatliche und soziale Wesen, - der empfunden wird wie eine Persönlichkeit, in deren Dienerschaft sich der Mensch als «Mensch mit dem Geistselbst» befindet, diese Christus-Persönlichkeit wird in einer wunderbar plastischen"
      ],
      [
        "Weise ausgearbeitet in den verschiedenen Auseinandersetzun­gen, die Solowjew gibt über das Johannes-Evangelium und seine Ein­gangsworte.",
        "Wiederum nur auf geisteswissenschaftlichem Felde kann sich ein Verständnis für das finden, wie bei Solowjew tief erfaßt wird der Satz: «Im Urbeginne war das Wort oder der Logos», wie anders das Johannes-Evangelium gerade erfaßt wird durch eine Phi­losophie, bei der gefühlt werden kann, daß sie eine keimende Philoso­phie ist, daß sie in einer merkwürdigen Weise in die Zukunft hinein-weist."
      ],
      [
        "Wenn man auf der einen Seite sagen muß, daß Hegel auf philoso­phischein Gebiete eine reifste Frucht darstellt, etwas, was als reifste philosophische Frucht aus der Bewußtseinsseele herausgeboren ist, so ist auf der anderen Seite diese Philosophie Solowjews der Keim in der Bewußtseinsseele für die Philosophie des Geistselbst, das in der sechsten Kulturperiode eingegliedert wird.",
        "Es gibt vielleicht keinen größeren Gegensatz, als den im eminentesten Sinne christlichen Staatsbegriff, der als hohes Ideal dem Solowjew wie ein Traum der Zukunft vorschwebt, diesen christlichen Staats- und Volksbegriff, der alles, was da ist, nimmt, um es darzubringen dem herabströmen-den Geistselbst, um es der Zukunft entgegenzuhalten, um es von den Gewalten der Zukunft durchchristen zu lassen - es gibt also keinen größeren Gegensaz, als diesen Begriff der im Solowjewschen Sinne gehaltenen christlichen Gemeinschaft, wobei der Christus-Begriff ein ganz zukünftiger ist, und den Begriff des Gottesstaates des heiligen Augustinus, der den Christus-Begriff zwar aufnimmt, aber den Staat so konstruiert, daß er der römische Staat ist, der den Christus auf­nimmt in die Vorstellung vom Staate, die ihm der römische Staat gegeben hat."
      ],
      [
        "Das, worauf es ankommt, ist dasjenige, was das Wissen abgibt für das in die Zukunft hineinwachsende Christentum.",
        "Im So­lowjewschen Staate ist der Christus das Blut, das alles soziale Zusam­menleben durchrinnt."
      ],
      [
        "Und das Wesentliche ist, daß der Staat gedacht wird mit aller Konkretheit der Persönlichkeit, so daß er zwar als geistiges Wesen wirken, aber auch mit allen Charaktereigentümlich­keiten der Persönlichkeit seine Mission erfüllen wird.",
        "So sehr durch­drungen von dem Christus-Begriff, der uns vorleuchtet in der Geisteswissenschaft"
      ],
      [
        "auf höheren Höhen, und dabei so sehr im Keime geblie­ben ist keine andere Philosophie.",
        "Alles, was wir im Osten finden, vom Volksgemüt angefangen bis hinauf zur Philosophie, das erscheint uns als etwas, das erst den Keim einer zukünftigen Entwickelung in sich trägt, und das deshalb auch die besondere Erziehung jenes Zeitgeistes sich hat angedeihen lassen müssen, den wir schon kennen, nachdem wir gesagt haben, daß der Zeitgeist des alten griechischen Volkes, als Impuls dem Christentum gegeben, mit der Mission versehen worden ist, der wirkende Zeitgeist für das spätere Europa zu werden.",
        "Dem­jenigen Volksgemüt, das die Keime für den sechsten Kulturzeitraum auszubilden haben wird, hat dieser Zeitgeist nicht allein Erzieher, sondern Pfleger sein müssen von der ersten Stufe des Daseins an.",
        "So können wir förmlich sagen - wobei Vater- und Mutterbegriff ihren getrennten Sinn verlieren -, daß das, was russisches Volks-gemüt ist und sich allmählich zur Volksseele entwickeln soll, nicht nur erzogen, sondern ernährt, gesäugt worden ist von demjenigen, wovon wir gesehen haben, daß es aus dem alten griechischen Zeitgeist heraus gebildet worden ist und dann einen anderen Rang nach außen angenommen hat."
      ],
      [
        "So verteilen sich die Missionen zwischen West-, Mittel- und Nord-Europa und dem Osten Europas.",
        "Eine Andeutung von diesen Dingen wollte ich Ihnen geben.",
        "Wir werden auf der Grundlage dieser An­deutungen noch einige Betrachtungen anstellen und zeigen, wie sich die europäische Zukunft ausnehmen wird, die gelten lassen wird, daß wir unsere Ideale aus solchen Erkenntnissen heraus bilden müssen; wir werden zeigen, wie sich der germanisch-nordische Volksgeist durch diesen Einfluß nach und nach zu einem Zeitgeiste umwandelt."
      ]
    ]
  },
  {
    "order": 12,
    "title_de": "ELFTER VORTRAG Kristiania, 17. Juni 1910",
    "paragraphs": [
      "Bei Beginn dieser unserer letzten Betrachtungen darf ich wahrlich sagen, daß eigentlich noch recht, recht viel zu besprechen wäre, und daß im Grunde genommen das Allerwenigste von dem, was in dieses reiche Thema hereinfallen würde, im Verlaufe dieses Vortragszyklus wirklich hat besprochen werden können. Allein ich darf ja wohl hof­fen, daß es nicht zum letzten Male ist, daß wir über ähnliche Themen hier zusammen sprechen, und es muß genügen, wenn gerade über die­ses Thema, das in gewisser Beziehung einer weiteren Besprechung in der Gegenwart ohnedies noch einige Schwierigkeiten bietet, nur An­deutungen gegeben worden sind für den Anfang. Dabei ging das wie ein roter Faden durch die letzten Darstellungen hindurch, daß inner­halb der germanisch-nordischen Mythologie oder Götterlehre etwas enthalten ist, was in einer imaginativen Form wunderbar anknüpft an alles, was wir in erkenntnismäßiger Gestalt herausholen können aus der geistigen Forschung unserer Gegenwart. Das ist nun auch einer der Gründe, warum wir hoffen dürfen, daß jener Volksgeist, jener Erzengel, welcher seine erzieherische und führende Tätigkeit über dieses Land hier erstreckt, mit dem, was er als seine Anlagen im Laufe der Jahrhunderte entwickelt hat, durchdringen wird dasjenige, was moderne Philosophie, moderne Geistesforschung genannt werden kann, und daß von da aus diese moderne Geistesforschung eine im volkstümlichen Sinne gehaltene Befruchtung erlangen wird.",
      "Je weiter wir in die Einzelheiten der germanisch-nordischen My­thologie eindringen würden, desto mehr würden wir sehen, daß wun­derbar in den Bildern dieser Mythologie die größten okkulten Wahr­heiten zum Ausdrucke kommen, wie es wirklich in keiner anderen Mythologie der Fall ist. So erinnern sich vielleicht einige von Ihnen, die meine «Geheimwissenschaft» gelesen oder andere Darstellungen, die ich hier geben durfte, mit angehört haben, daß einmal im Verlaufe der Erdenevolution ein Vorgang stattfand, den wir bezeichnen kön­nen als das Herabsteigen jener Seelen der Menschen, die in uralten",
      "Zeiten, vor der alten lemurischen Periode, hinaufgestiegen sind zu den einzelnen Planeten unseres Planetensystems, die aus ganz besonderen Gründen hinaufgestiegen sind zu Saturn, Jupiter, Mars, Venus, Mer­kur, und daß diese während der letzten lemurischen und der ganzen atlantischen Zeit sich zu vereinigen strebten mit dem, was der Men­schenleib nach und nach entwickelt und an Anlagen ausgebildet hatte, die möglich geworden waren durch das Hinausgehen des Mondes aus unserer Erde. Da sind sie heruntergestiegen, diese Saturn-, Jupiter-, Mars-, Venus- und Merkurseelen. Das ist ein Vorgang, den man heute noch finden kann in der Akasha-Chronik. Daß im Laufe der atlanti­schen Zeit die Wasser nebelförmig die Luft der Atlantis durchdran­gen, das war ein Zustand, der damals damit zusammenhing, daß eben diese Seelen herunterstiegen, die man mit dem alten Hellsehen der atlantischen Zeit wahrnahm. Immer wieder, wenn neue Wesen ge­boren wurden in dem dazumal noch plastisch-weichen, biegsamen, bildsamen Leibe, wenn solche sozusagen aus geistigen Höhen her­unterstiegen, so betrachtete man das als den äußeren Ausdruck dafür, daß aus der geistigen Umgebung, aus der Atmosphäre, aus dem pla­netarischen Dasein, Seelen herunterstiegen, um sich mit den auf der Erde entstehenden Leibern zu vereinigen.",
      "Der Vorgang, wie sich gleichsam die Erdenleiber der Befruchtung dessen erschließen, was aus Himmelshöhen herunterstrahlt, dieser Vorgang hat sich erhalten in der Anschauung, die sich hineinver­pflanzt hat in die nordisch-germanische Mythologie. Das Bewußtsein davon hat sich so lange erhalten, daß es selbst Tacitus noch bei den südlicheren Germanen fand in der Zeit, da er die Beobachtungen machte, die er in seiner «Germania» beschrieb. Niemand wird die Er-zählung verstehen, die Tacitus von der Göttin Nerthus gibt, der nicht weiß, daß es diesen Vorgang einmal gegeben hat. Der Wagen der Göttin Nerthus wird über die Gewässer gefahren. Später hat sich das als Ritual, als Ritus erhalten. In früherer Zeit war es Beobachtung. Dargeboten hat diese Göttin das, was an Menschenleibern dargeboten werden konnte den aus den planetarischen Sphären herunterdringen­den Menschenseelen. Das ist der geheimnisvolle Vorgang, der dem Nerthus-Mythus zugrunde liegt, und der in alledem sich erhalten hat,",
      "was in den älteren Sagen und Legenden, bei denen auf das Werden des physischen Menschen hingedeutet wird, uns überliefert ist. Njordr, der innerlich verwandt ist mit der Göttin Nerthus, ist das männliche Gegenbild. Der soll uns darstellen die uralte Erinnerung an das Hin­untersteigen der geistig-seelischen Menschen, die einst hinaufgestiegen waren in planetarische Höhen, und die während der atlantischen Zeit wieder heruntergestiegen sind, um sich mit physischen Menschenlei­bern wiederum zu vereinigen.",
      "Aus meiner kleinen Schrift «Blut ist ein ganz besonderer Saft» kön­nen Sie entnehmen, welche bedeutungsvolle Rolle Völkermischungen und Völkerzusammenhänge in gewissen Zeiten gespielt haben. Nun haben nicht nur Völkermischungen und Völkerzusammenhänge, die ihren Ausdruck in der Blutmischung gefunden haben, sondern auch die geistigen und seelischen Förderungen der Volksgeister eine große Rolle gespielt.",
      "Die Anschauung jenes Hinuntersteigens ist am reinsten erhalten auf dem Grunde jener Sagenwelt, welche sich in früherer Zeit in diesen nordischen Gebieten gebildet hat. In den Wanensagen können Sie daher eine älteste Erinnerung an solche Dinge noch finden.",
      "Insbesondere war hier im Norden lebendig, in der finnischen Tradi­tion, die Erinnerung an diese Verbindung des Geistig-Seelischen, das aus planetarischen Höhen herunterstieg, mit dem, was aus dem Erden-leib selber hervorgegangen ist und was die nordische Tradition als «Riesenheim» kennt. Was sich aus dem Erdenleib entwickelt hat, das gehört zu Riesenheim.",
      "So begreifen wir es, daß der nordisch-germa­nische Mensch immer den Impuls von dieser Seite her gefühlt hat, daß er fühlte, wie in seiner Seele, die sich nach und nach ausgebildet hat, dieser alte Götterblick arbeitete, der hier noch heimisch war, als die Nebelwasser der Atlantis noch hinüberreichten in diese Gegend in der alten Zeit. Es fühlte der nordisch-germanische Mensch in seiner Seele etwas von der Herkunft eines Gottes, der abstammte direkt von jenen göttlich-geistigen Wesenheiten, jenen Erzengelwesenheiten, die das Zusammenfügen des Seelisch-Geistigen mit dem Irdisch-Physi­schen leiteten.",
      "Freyr, der Gott, und Freya, seine Schwester, die ja hier im Norden einstmals ganz besonders beliebte Gottheiten waren, wa­ren in ihrem Ursprung gedacht und empfunden als diejenigen Engelwesen,",
      "welche in die menschliche Seele gegossen haben alles dasjenige, was diese menschliche Seele brauchte, um unmittelbar auf dem physi­schen Plane fortzuentwickeln die alten, durch das hellseherische Ver­mögen aufgenommenen Kräfte. Freyr war innerhalb der physisch-sinnlichen Welt, innerhalb der auf die äußeren Sinne beschränkten Welt der Fortsetzer alles dessen, was früher im Hellsehen aufgenom­men worden ist.",
      "Er war die lebendige Fortsetzung der hellseherisch aufgenommenen Kräfte. Daher mußte er sich verbinden mit dem, was im menschlichen Leibe selber als physisch-leibliche Werkzeuge vor­handen ist für diese Seelenkräfte, die dann in den physischen Plan hineintragen das, was im uralten Hellsehen wahrgenommen wurde.",
      "Das spiegelt sich in der Ehe des Freyr mit Gerd, der Riesentochter. Sie ist den physischen Kräften des Erdenwerdens selber entnommen. In diesen Vorstellungen spiegelt sich noch nach das Herabsteigen des Göttlich-Geistigen in das Physische.",
      "Ganz wunderbar ist ausgedrückt in dieser Freyrgestalt, wie Freyr sich dessen bedient, was dem Men­schen auf dem physischen Plane möglich macht, auszuleben das, wozu er erzogen ist durch seine vorhergehenden hellseherischen Wahrneh­mungen. Bluthuf heißt das Pferd, das dem Freyr zur Verfügung steht, um anzudeuten, daß das Blut das Wesentliche ist, um sein Ich zu ent­wickeln.",
      "Ein merkwürdiges, wunderbares Schiff steht auch dem Freyr zur Verfügung. Ausgebreitet kann es werden ins Unermeßliche, und zusammengefaltet kann es werden, so, daß es in den kleinsten Kasten hineingeht.",
      "Was ist nun dieses Wunderschiff? Wenn Freyr die Macht ist, die hineinträgt die hellseherischen Kräfte in die Gebiete, die sich auf dem physischen Plane ausleben, dann muß es das sein, was ihm ganz besonders eigen ist: die Abwechslung zwischen Tagwachen und Nachtschlafen.",
      "Und wie die Menschenseele sich während des Schla­fens bis zum Wiederaufwachen ausbreitet im Makrokosmos, so breitet sich das Wunderschiff aus und wird dann wieder zusammengefaltet in die Gehirnfalten, um dann während der Tageszeit in dem kleinsten Kasten - dem Menschenschädel - untergebracht zu werden. Das alles finden Sie in einer wunderbaren Weise in dieser nordisch-germani­schen Mythologie, in diesen Bildercharakteren.",
      "Diejenigen von Ihnen, die näher eingehen werden auf diese Dinge,",
      "werden sich nach und nach überzeugen, daß es keine Phantastik ist, sondern daß es wirklich aus den Schulen der Eingeweihten stammt, was mit diesen Bildern hineinverpflanzt, hineingeimpft worden ist in die Volksseele, in das Volksgemüt. So ist ungeheuer viel geblieben in dem leitenden Erzengel, in dem Volksgeist im Norden, von dem, was alte Erziehung war durch hellseherische Wahrnehmung, von dem, was in einer Seele werden kann, die sozusagen in ihrer Entwickelung auf dem physischen Plane sich anschließt an eine hellseherische Entwicke­lung.",
      "Wenn das Äußerliche heute auch anders aussieht, der Erzengel des germanischen Nordens hat in sich diese Anlage, und mit dieser An­lage ist er ganz besonders geeignet, dasjenige zu verstehen, was mo­derne Geisteswissenschaft ist, und es umzuwandeln in dem Sinne, wie es im Sinne volkstümlicher Kraft umgewandelt werden muß. Daher werden Sie auch verstehen, wenn gesagt wird, daß die besten Bedin­gungen gegeben sind gerade innerhalb des germanisch-nordischen Wesens, um das zu verstehen, was ich nur andeutend sagen konnte in dem hier gehaltenen öffentlichen Vortrage von der Wiederoffenba­rung des Christus.",
      "Da zeigt uns die Geistesforschung in unserer jetzi­gen Zeit, daß nachdem das Kali Yuga abgelaufen ist, das fünftausend Jahre gedauert hat - ungefähr von 3100 v. Chr. bis 1899-, im Men­schen sich neue Fähigkeiten heranentwickeln.",
      "Sie werden zunächst bei einzelnen, wenigen zum Vorschein kommen, die für diese Fähigkeiten besonders geeignet sind. Da wird zum Beispiel eintreten, daß Men­schen aus der naturgemäßen Evolution ihrer Fähigkeiten heraus von dem etwas sehen werden, was heute nur durch die Geisteswissen­schaft, nur von der geistigen Forschung aus verkündet wird.",
      "Da wird uns erzählt, daß in Zukunft die Menschen, bei denen die Organe des Ätherleibes entwickelt sind, in immer größerer Zahl auftreten und zum Hellsehen kommen werden, zu dem man heute nur durch Schu­lung kommen kann. Und warum wird es so sein?",
      "Was wird der Äther-leib für die Anschauung einiger Menschen haben? Menschen wird es geben, die Eindrücke haben werden, von denen ich einen etwa so schildern möchte. Es wird der Mensch etwas tun in der äußeren Welt, und er wird sich dabei gedrängt fühlen, etwas zu bemerken.",
      "ihm wie eine Art von Traumbild vor die Augen treten, das er zunächst nicht verstehen wird. Hat er aber etwas gehört von Karma, von der Gesetzmäßigkeit im Weltgeschehen, so wird er es nach und nach ver­stehen lernen, denn es ist das karmische Gegenbild seiner Taten in der Ätherwelt, das er gesehen hat. So bilden sich nach und nach die er­sten Elemente künftiger Fähigkeiten.",
      "Diejenigen Menschen, die sich durch die Geisteswissenschaft anre­gen lassen, werden nach und nach erleben können - von der Mitte des zwanzigsten Jahrhunderts an - eine Wiedererneuerung desjeni­gen, was Paulus im ätherischen Hellsehen gesehen hat als ein kom­mendes Mysterium, als das Mysterium des lebenden Christus. Es wird eine neue Offenbarung des Christus sein, eine Offenbarung wie sie kommen muß, wenn die menschlichen Fähigkeiten in naturgemäßer Weise sich dahin entwickeln, daß der Christus von den Menschen gesehen werden kann in der Welt, in der er seit dem Mysterium von Golgatha immer war und in der er für den Eingeweihten auch zu fin­den ist.",
      "In diese Welt wächst die Menschheit hinein, um vom phy­sischen Plane aus wahrnehmen zu können, was sonst nur in den My­sterienschulen, von höheren Planen aus, gesehen wurde. Trotzdem wird die Mysterienschulung nicht überflüssig.",
      "Sie gibt die Dinge noch immer in anderer Art, als sie der nichtgeschulten Seele vorliegen. Aber das, was von der Mysterienschulung gegeben wird, wird durch Umwandelung des physischen Menschenleibes das Mysterium des le­benden Christus in einer neuen Weise zeigen, wie es perspektivisch von dem physischen Plan aus gesehen werden kann, wie es im Äther wird gesehen werden können, zuerst von einzelnen Menschen, dann aber von immer mehr und mehr Menschen im Laufe der nächsten dreitausend Jahre.",
      "Dasjenige, was Paulus gesehen hat als den lebenden Christus, der in der Ätherwelt zu finden ist seit dem Ereignis von Golgatha, wird von immer mehr Menschen geschaut werden können.",
      "Immer höher werden die Offenbarungen des Christus liegen. Das ist das Mysterium der Entwickelung des Christus. Da die Menschen zur Zeit, als das Mysterium von Golgatha sich vollzog, alles von dem physischen Plane aus auffassen sollten, so war es notwendig, daß sie auch auf dem physischen Plan den Christus sehen konnten, daß sie",
      "Nachricht von ihm bekommen und sein Walten auf dem physischen Plan bezeugen konnten. Aber die Menschheit ist auf Fortschritt an­gelegt, auf die Entwickelung höherer Kräfte, und derjenige müßte nichts wissen von dem Fortschritte der Menschheit, der glauben woll­te, daß die Offenbarungen des Christus in derselben Weise, wie sie vor 1900 Jahren nötig war, sich wiederholen wird. Dazumal geschah sie auf dem physischen Plan, weil die Kräfte des Menschen auf den physischen Plan eingestellt waren. Aber die Kräfte des Menschen werden sich entwickeln, und dadurch wird Christus zu den erhöhten menschlichen Kräften im Laufe der nächsten 3000 Jahre immer mehr und mehr sprechen können.",
      "Das, was ich jetzt eben gesagt habe, ist eine Wahrheit, die seit langem einzelnen wenigen Menschen mitgeteilt worden ist aus den esoterischen Schulen heraus, und es ist eine Wahrheit, die insbesondere auf dem Boden der Geisteswissenschaft heute gefunden werden muß aus dem Grunde, weil die Geisteswissenschaft eine Vorschule sein soll für dasjenige, was da kommen wird. Die Menschheit ist jetzt ein­gestellt auf Freiheit, auf Selbstanerkennung dessen, was sich in ihr bildet, und es könnte geschehen, daß diejenigen Menschen, die als erste Pioniere der Christus-Anschauung sich einstellen werden, als Narren verschrieen werden mit dem, was sie der Menschheit darzu­bieten haben, und es könnte die Menschheit weiter noch versinken in den Materialismus, als sie dies bis jetzt schon ist, und tottreten das, was eine wunderbarste Offenbarung für die Menschheit werden könnte. Alles, was in Zukunft geschehen kann, ist in gewissem Grade in den Willen der Menschheit gestellt, so daß die Menschen auch ver­fehlen können, was zu ihrem Heile ist. Das ist außerordentlich wich­tig, daß die Geisteswissenschaft eine Vorbereitung ist für dasjenige, was die neue Christus-Offenbarung sein wird.",
      "Der Materialismus kann in zweifacher Weise da einen Fehler ma­chen. Der eine, der wahrscheinlich gemacht werden wird aus den Traditionen des Okzidents heraus, besteht darin, daß es als eine wilde Phantastik, als eine wüste Narretei angesehen werden wird, was die ersten Pioniere der neuen Christus-Offenbarung aus ihrer eigenen An­schauung heraus im zwanzigsten Jahrhundert verkündigen werden.",
      "Der Materialismus hat alle Kreise heute ergriffen. Er ist nicht nur im Okzident heimisch, er hat auch den Orient erfaßt; nur in einer anderen Form kommt er da zum Vorschein. Es könnte sein, daß der orientalische Materialismus dahin führen werde, daß die Menschen verkennen das Höhere einer Christus-Offenbarung auf einer höheren Stufe, und daß eintreten wird dasjenige, was hier so oft gesagt wurde und immer wieder gesagt werden wird: daß materialistisches Denken das Erscheinen des Christus in eine materialistische Anschauung um­setzen wird. Es könnte sein, daß man in jener Zeit unter dem Einfluß der geisteswissenschaftlichen Wahrheiten zwar sprechen dürfte da­von, daß der Christus sich offenbaren wird, aber gleichzeitig glaubt, daß Christus in einem materiellen Leibe erscheinen wird. Das Ergebnis wäre dann ein anders gefärbter Materialismus. Da würde sich nur fortsetzen, was seit Jahrhunderten gewesen ist.",
      "Diesen falschen Materialismus haben sich immer wieder die Men­schen zunutze gemacht, und zwar so, daß sich einzelne Menschen für den wiedererschienenen Christus ausgaben. Der letzte bedeutendere Fall eines derartigen falschen Christus war im siebzehnten Jahrhun­dert, wo ein Mann namens Sabbatai Z'vi aus Smyrna als der wieder-erschienene Christus auftrat. Er hat großes Aufsehen gemacht. Zu ihm sind hingepilgert nicht nur die Menschen, die in der unmittel­baren Umgebung waren, sondern Leute aus Ungarn, Polen, Deutsch­land, Frankreich, Italien und Nordafrika. Überall wurde in Sabbatai Z'vi die physische Inkarnation eines Messias gesehen. Ich möchte nicht die Menschheitstragik erzählen, die sich an die Persönlichkeit des Sabbatai Z'vi knüpft. Im siebzehnten Jahrhundert war diese Tra­gik allerdings nicht besonders groß. Der Mensch war damals noch nicht so sehr unter den freien Willen gestellt; aber er konnte durch seine Erkenntnis, die ein spirituelles Empfinden war, erkennen, was die Wahrheit ist. Das Unglück wäre aber groß im zwanzigsten Jahr­hundert, wenn unter dem Drucke des Materialismus die Lehre, daß Christus sich offenbaren wird, eine materialistische Ausdeutung er­fahren würde in der Weise, als ob Christus im physischen Leibe wie­derkommen könnte. Damit würde die Menschheit nur beweisen, daß sie keine Anschauung und keine Einsicht gewonnen hat bezüglich des",
      "wirklichen Fortschrittes der menschlichen Entwickelung zu höheren geistigen Kräften. Falsche Messiasse werden ganz gewiß auftreten, und sie werden aus dem Materialismus unserer Zeit ebenso Zuspruch erhalten, wie Sabbatai Z'vi im siebzehnten Jahrhundert. Es wird eine Probe, eine harte Prüfung sein für die geistig Vorbereiteten, zu er­kennen, wo die Wahrheit liegt, ob sich in die spirituellen Theorien wirklich auch spirituelles lebensvolles Empfinden hineinlebt, oder ob in diesen spirituellen Theorien nur ein versteckter Materialismus lebt. Da wird die Probe sein auf die Fortentwickelung der Geisteswissen­schaft, ob Menschen genug durch diese Geisteswissenschaft entwickelt sein werden, welche einsehen können, daß sie den Geist im Geiste zu schauen haben, daß sie hinaufzuschauen haben in die ätherische Welt, hinaufzuschauen auf eine Neuoffenbarung des Christus, oder ob sie auf dem physischen Plane stehen bleiben und eine Offenbarung im physischen Leibe, die sich auf den Christus bezieht, sehen wollen. Diese Prüfung wird unsere Bewegung noch bestehen müssen. Wir kön­nen aber sagen, daß nirgends besser der Boden vorbereitet ist, gerade auf diesem Gebiete die Wahrheit zu erkennen, als da, wo die germa­nisch-nordische Mythologie ersprossen ist.",
      "In dem, was uns als Götterdämmerung überliefert ist, ist eine be­deutsame Zukunftsvision enthalten, und damit komme ich auf ein Kapitel, von dem ich sozusagen schon den Ausgangspunkt angedeutet habe. Ich habe Ihnen gesagt, daß innerhalb einer Volksgemeinschaft, die das, was hellseherische Vergangenheit ist, erst so kurze Zeit hinter sich hat, auch ein heilseherischer Sinn in dem leitenden Volksgeiste entwickelt ist, um das, was uns heilseherisch erblüht, wieder zu ver­stehen. Wenn nun eine Menschheit gerade auf dem Boden die neue Zeit mit neuen menschlichen Fähigkeiten erlebt, wo die germanisch-nordi­sche Mythologie erblühte, da soll sie verstehen, daß dasjenige, was altes Hellsehen war, eine andere Gestalt erfahren muß, nachdem der Mensch durchgegangen ist durch die Entwickelung des physischen Planes. Da hat eine Weile geschwiegen das, was aus dem alten Hell-sehen heraus gesprochen hat; da hat eine Weile hinter dem Menschen gestanden, sich dem menschlichen Blicke entzogen die Welt des Odin und Thor, des Baldur und Hödur, des Freyr und der Freya. Aber hervorkommen",
      "wird sie wieder in einer Zeit, wo andere Kräfte mittler­weile an der menschlichen Seele gearbeitet haben. Wenn diese mensch­liche Seele mit dem neuen Hellsehen, das mit ätherischem Hellsehen beginnt, hineinschauen wird in die neue Welt, dann wird sie sehen, daß sie sich nicht halten kann an die alten Formen der die Seele er­ziehenden Kräfte.",
      "Würde sie sich daran halten können, dann würden auch all die Gegenkräfte hervortreten gegen die Kraft, die in alten Zeiten hat erziehen sollen die menschlichen Kräfte zu einer gewissen Höhe. Odin und Thor werden wieder dastehen vor dem Blicke der Menschheit, jetzt aber so, daß die menschliche Seele eine neue Ent­wickelung durchgemacht haben wird.",
      "Der menschlichen Seele wird alles erscheinen, was die Gegenkräfte des Odin und Thor sind. Alles, was sich als Gegenkraft entwickelt hat, wird in einem gewaltigen Tableau wieder sichtbar werden. Aber nicht vorwärtskommen würde die menschliche Seele, nicht wehren gegen Schädliches würde sie sich können, wenn sie sich nur den Kräften unterwerfen würde, welche im alten Hellsehen gesehen worden sind.",
      "Thor hat einst den Menschen das Ich gegeben. Das Ich hat sich erzogen auf dem physischen Plane, hat sich herausentwickelt aus dem, was Loki, die luziferische Gewalt, im Astralleibe zurückgelassen hatte, aus der Midgardschlange.",
      "Das, was einst Thor geben konnte, und worüber die menschliche Seele hin­auswächst, das steht im Kampfe mit dem, was aus der Midgard­schlange kommt. Das tritt uns in der nordischen Mythologie als der mit der Midgardschlange kämpfende Thor entgegen.",
      "Gegenseitig hal­ten sie sich das Gleichgewicht, das heißt sie töten einander. Ebenso waltet Odin gegen den Fenriswolf, wobei sie sich gegenseitig vernich­ten. Dasjenige, was eine Weile die menschliche Seelenkraft gebildet hat, Freyr, das muß unterliegen demjenigen, was dem auf dem physi­schen Plan mittlerweile herangezogenen Ich aus den Erdenkräften selber heraus gegeben worden ist.",
      "Freyr unterliegt dem Flammen­schwert des aus der Erde entsprossenen Surtur.",
      "Alle diese Einzelheiten, die in der Götterdämmerung hingestellt sind, werden dem entsprechen, was in einer neuen, in die Zukunft wirklich hineinweisenden Äthervision vor der Menschheit stehen wird. Zurückbleiben wird der Fenriswolf. Oh, darin, daß dieser Fenriswolf",
      "zurückbleibt im Kampfe gegen Odin, verbirgt sich eine tiefe, tiefe Wahrheit. Es wird in der nächsten Zukunft der Menschheit nichts so sehr gefährlich werden, als wenn der Hang, beim alten, nicht durch neue Kräfte entwickelten Hellsehen zu bleiben, die Men­schen dazu verführen könnte, stehen zu bleiben bei dem, was das alte, astrale Hellsehen in Urzeiten geben konnte, nämlich solche Seelen-bilder wie der Fenriswolf. Es wäre wieder eine harte Prüfung für das­jenige, was auf dem Boden der Geisteswissenschaft erwachsen muß, wenn etwa auch auf diesem Boden der Hang entstehen würde zu aller­lei ungeklärtem, chaotischem Hellsehen, die Neigung, nicht das von Vernunft und Wissenschaft durchleuchtete Hellsehen höher zu schät­zen, sondern das alte, chaotische, dem dieser Vorzug abgeht.",
      "Mit furchtbarer Gewalt würden sich rächen solche Überbleibsel alten Hellsehens, die mit allerlei chaotischen Bildern die Anschauun­gen der Menschen verwirren könnten. Einem solchen Hellsehen könn­te nicht mit demjenigen begegnet werden, was selber aus alter Hell­seherkraft entstand, sondern nur mit dem, was während des Kali Yuga als gesunde Kraft zu einem neuen Hellsehen herangebildet wor­den ist. Nicht dasjenige, was an Kraft der alte Erzengel Odin gegeben hat, nicht die alten hellseherischen Kräfte können retten; da muß et­was weit anderes kommen. Dieses andere aber kennt die germanisch­nordische Mythologie. Von dem weiß sie, daß es vorhanden ist. Sie weiß, daß die Äthergestalt lebt, in der sich inkarnieren soll dasjenige, was wir wiedersehen sollen als ätherische Christusgestalt. Und dieser erst wird es gelingen, auszutreiben, was an ungeklärter hellseherischer Kraft die Menschheit verwirren wird, wenn Odin nicht vernichtet den Fenriswolf, der nichts anderes repräsentiert als die zurückgeblie­bene Hellseherkraft. Widar, der sich schweigend verhalten hat wäh­rend der ganzen Zeit, der wird den Fenriswolf überwinden. Das sagt uns auch die Götterdämmerung.",
      "Wer Widar in seiner Bedeutung erkennt und ihn in seiner Seele fühlt, der wird finden, daß im zwanzigsten Jahrhundert den Men­schen wieder die Fähigkeit gegeben werden kann, den Christus zu schauen. Der Widar wird wieder vor ihm stehen, der uns allen ge­meinschaftlich ist in Nord- und Mittel-Europa. Er wurde geheim gehalten",
      "in den Mysterien und Geheimschulen als ein Gott, der erst in Zukunft seine Mission erhalten wird. Selbst von seinem Bilde wird nur unbestimmt gesprochen. Das mag hervorgehen daraus, daß ein Bild in der Nähe von Köln gefunden worden ist, von dem man nicht weiß, wen es darstellt, das aber nichts anderes bedeutet als ein Bild­nis von Widar.",
      "Durch das Kali Yuga hindurch wurden die Kräfte erworben, die die neuen Menschen befähigen sollen, die neue Christus-Offenbarung zu schauen. Diejenigen, welche berufen sind, aus den Zeichen der Zeit heraus zu deuten das, was da kommen muß, wissen, daß die neue Geistesforschung wieder aufrichten wird die Kraft Widars, der alles dasjenige aus den Gemütern der Menschen vertreiben wird, was als Überbleibsel chaotischer alter Hellseherkräfte verwirrend wirken könnte, und der das neu sich heranentwickelnde Hellsehen in der menschlichen Brust, in der menschlichen Seele wachrufen wird.",
      "So sehen wir, indem uns aus der Götterdämmerung herausglänzt die wundersame Gestalt des Widar, daß uns sozusagen eine Hoffnung für die Zukunft aus der germanisch-nordischen Mythologie entgegen-leuchtet. Indem wir uns verwandt fühlen gerade mit der Gestalt des Widar, den wir nun in seiner tieferen Wesenheit erfassen wollen, hof­fen wir, daß dasjenige, was der Grundnerv und die lebendige Essenz alles geisteswissenschaftlichen Wesens sein muß, sich aus jenen Kräf­ten, welche der Erzengel der germanisch-nordischen Welt zu der mo­dernen Zeitentwickelung hinzubringen kann, wird ergeben können. Ein Teil erst von einem größeren Ganzen ist für den fünften nach-atlantischen Kulturzeitraum an Menschheits- und Geistesentwickelung geleistet worden, ein anderer Teil muß noch geleistet werden. Am meisten werden zu dieser Leistung beizutragen haben diejenigen aus der Summe der nordisch-germanischen Völker heraus, die in sich füh­len, daß sie elementare, frische Völkerkraft in sich haben. Aber es wird das gewissermaßen in die Seelen der Menschen gelegt werden. Sie werden sich selbst entschließen müssen, zu arbeiten. Im zwanzig­sten Jahrhundert kann man irren, weil es in gewisser Weise in die Freiheit der Menschen gestellt sein muß, was erreicht werden soll, weil es nicht unter Zwang gesetzt sein darf. Daher handelt es sich darum,",
      "ein richtiges Verständnis dessen zu haben, was kommen soll. So sehen Sie, daß, wenn aus unserer heutigen Geisteswissenschaft heraus-spricht die Erkenntnis des Christus-Wesens, und wenn wir anknüpfen an die wahre Erkenntnis dieses Christus-Wesens, das wir aus europäi­schen Volkssubstanzen selber heraussuchen, wenn wir daran knüpfen unsere Zukunftshoffnungen, so beruht das wirklich nicht auf irgend­einer Vorliebe oder irgendeiner Temperamentsanlage.",
      "Es ist manchmal gesagt worden, daß man nennen könne wie man wolle dasjenige, was man als erstes Wesen in der Menschheitsevolu­tion bezeichnen kann. Niemals wird derjenige, der das Christus-Wesen erkennt, sich darauf versteifen, daß der Name des Christus bleibt. Aber, wenn wir den Christus-Impuls im richtigen Sinne ver­stehen, so werden wir auch nicht so sprechen, daß wir sagen: Ein We­sen lebt in der Menschheitsevolution, in der Menschheit des Westens und Ostens, und das muß so sein, daß es den Sympathien der Mensch­heit für diese oder jene Wahrheit entspricht. - Das ist nicht okkul­tistisch. Okkultistisch ist es, daß in dem Augenblicke, wo man erken­nen würde, daß dieses Wesen getauft werden müßte auf den Namen des Buddha, dies rückhaltlos getan wird, ganz gleich, ob es einem sympathisch oder antipathisch ist. Nicht auf Sympathie oder Anti­pathie kommt es also an, sondern auf die Wahrheit der Tatsachen.",
      "In dem Augenblicke, wo uns die Tatsachen anders belehren wür­den, wären wir bereit, anders zu handeln. Einzig und allein die Tat­sachen müssen maßgebend sein. Wir wollen keinen Orientalismus und keinen Okzidentalismus hineintragen in das, was wir als eigentliches Lebensblut unserer Geisteswissenschaft ansehen, und wenn wir her­ausfinden sollten in der nordisch-germanischen Erzengelwelt das­jenige, was einen befruchtenden Keim abgeben kann für die wahr-hafte Geisteswissenschaft, so wird es etwas sein, was nicht gegeben wird auf diesem Boden für ein einzelnes Volk oder einen einzelnen Stamm, sondern was der gesamten Menschheit gegeben wird. Das, was der gesamten Menschheit gegeben wird, gegeben werden muß, kann zwar an diesem oder jenem Orte entspringen, gegeben werden muß es aber der gesamten Menschheit. Wir kennen nicht einen Unter­schied zwischen Orient und Okzident; wir nehmen mit inniger Liebe",
      "dasjenige auf, was wir als das überwältigend Große der uralten Kul­tur der heiligen Rishis in ihrer wahren Gestalt kennen; wir nehmen mit Liebe auf die persische Kultur, nehmen mit Liebe auf dasjenige, was wir als ägyptisch-chaldäische und griechisch-lateinische Kulturen kennen; wir nehmen auch mit ebensolcher Objektivität auf, was uns aus dem europäischen Boden erwachsen ist. Nur die Notwendigkeit der Tatsachen zwingt uns, die Angaben so zu machen, wie sie ge­macht werden.",
      "Indem wir alles empfangen von der gesamten Menschheit, alles, was jede Religion beizutragen hat zum Kulturprozeß der Menschheit, aufnehmen in das, was wir heute erkennen, was wir heute Gemeingut der Menschheit nennen, indem wir das mehr und mehr tun, sind wir gerade im Sinne des Christus-Prinzips tätig. Da es fortentwickelungs­fähig ist, so müssen wir das überwinden, was es in den ersten Jahr­hunderten und Jahrtausenden durchmachen mußte, wo das Christus-Prinzip in den unvollkommensten Anfängen begriffen war.",
      "Wir sehen nicht in diese Vergangenheit, lassen uns auch nicht von ihr belehren, Uns liegt nichts an dieser Überlieferung, uns liegt in der Hauptsache an dem, was aus der geistigen Welt heraus erforscht werden kann, Deshalb sehen wir das Wichtigste des Christus-Prinzips nicht in dem, was war - und wenn es noch so oft betont wird, aus der Tradition heraus -, sondern in dem, was da kommen wird. Wir berufen uns nicht so sehr auf das, was historisch überliefert wird, sondern suchen zu wissen das, was da kommen wird.",
      "Das ist der Schwerpunkt des Christus-Impulses, der in den Anfang des christlichen Zeitalters fällt, und wir geben nicht viel auf das Äußerlich-Historische. Nachdem das Christentum die Kinderkrankheiten durchgemacht hat, wird es sich weiter entwickeln.",
      "Es ist auch in fremde Länder gegangen und wollte die Menschen zu dem bekehren, was man in den einzelnen christlichen Dogmen eines Zeitalters gehabt hat. Vor unserer Seele steht aber ein Christentum, von dem wir wissen, daß Christus in allen Zeiten wirk­sam war, und daß wir Christus finden werden an allen Orten, wohin wir kommen, daß das Christus-Prinzip das allergeisteswissenschaft­lichste Prinzip ist.",
      "Und wenn der Buddhismus nur als Buddhisten gel­ten läßt diejenigen, welche auf Buddha schwören, dann wird das",
      "Christentum dasjenige sein, das auf keinen Propheten schwört, weil es nicht unter dem Eindruck eines völkischen Religionsstifters steht, sondern den Menschheitsgott anerkennt.",
      "Derjenige, der das Christentum kennt, weiß, daß es sich dabei um ein Mysterium handelt, das auf Golgatha auf dem physischen Plane zur Anschauung gekommen ist. Die Anschauung dieses Mysteriums ist es, die uns in der Richtung führt, die ich geschildert habe. Man kann auch wissen, daß das geistige Leben zur Zeit des Mysteriums von Golgatha ein solches war, daß dieses Mysterium gerade so in je­ner Zeit erlebt werden mußte, wie es erlebt worden ist von der Menschheit. Wir lassen uns keine Dogmen aufdrängen, auch nicht die Dogmen der christlichen Vergangenheit, und wenn uns aufge­drängt werden sollte ein Dogma von der einen oder anderen Seite, dann würden wir es im Sinne des wahrhaft verstandenen Christus­Prinzipes zurückweisen. Mögen noch so viele Menschen kommen und den geschichtlichen Christus in ein konfessionelles Bekenntnis zwän­gen, oder mögen sie falsch nennen das, was wir als Zukunfts-Christus schauen, wir lassen uns nicht beirren dadurch, wenn uns von ihnen gesagt wird: So oder so muß der Christus sein, - auch wenn es von denen gesagt wird, die verstehen sollten, wer der Christus ist. Ebenso­wenig darf die Christus-Wesenheit gedrückt und beengt werden aus den orientalischen Traditionen heraus, ebensowenig eine Färbung er­halten durch die Dogmen des orientalischen Dogmatismus. Frei und unabhängig von jeder Tradition und jeder Autorität will das vor die Menschheit hintreten, was aus den Quellen des Okkultismus heraus gerade über diese Zukunftsevolution zu sagen ist.",
      "Wunderbar erscheint es mir, wie die Menschen sich auf diesem Boden verstehen können. Immer und immer wieder ist mir in diesen Tagen von den hierher gereisten Nicht-Norden gesagt worden, wie sie sich gegenüber den Persönlichkeiten des skandinavischen Nordens so frei gefühlt haben. Viele haben das ausgesprochen. Ein Beweis da­für, wie wir uns, vielleicht noch für manche unbewußt, in dem tief­sten Wesen der Geistes-Erkenntnis verstehen können, wie wir uns namentlich in dem verstehen werden, was ich schon bei dem letzten «Theosophischen Kongreß» in Budapest hervorhob, und was ich wiederholte",
      "während unserer eigenen Generalversammlung in Berlin, wo wir die große Freude hatten, auch Freunde aus dem Norden bei uns zu sehen. Schlecht wäre es für die Geisteswissenschaft, wenn derje­nige, der noch nicht in das geistige Gebiet hineinschauen kann, auf blinden Glauben hin annehmen müßte dasjenige, was gesagt wird. Ich bitte Sie und habe Sie gebeten in Berlin, nichts auf Autorität und Glauben hinzunehmen, was ich jemals gesagt habe oder sagen werde. Es gibt, auch bevor der Mensch die hellseherische Stufe erreicht, die Möglichkeit, dasjenige zu prüfen, was aus hellseherischer Beobach­tung heraus gewonnen wird. Was ich je gesagt habe über Zarathustra und Jesus von Nazareth, über Hermes und Moses, über Odin und Thor, über den Christus Jesus selber, ich bitte Sie nicht, es zu glauben und meine Worte auf Autorität hin anzunehmen. Ich bitte Sie, sich abzugewöhnen das Autoritätsprinzip; denn von Übel würde das Autoritätsprinzip für uns werden.",
      "Ich weiß aber ganz gewiß, wenn Sie anfangen, nachzudenken mit unbefangenem Wahrheitssinn, wenn Sie sagen: Das wird uns gesagt; prüfen wir die uns zugänglichen Urkunden, die Religions- und my­thologischen Dokumente, prüfen wir, was uns sagt jegliche Natur­wissenschaft, - so werden Sie die Richtigkeit des Gesagten einsehen. Nehmen Sie alles zu Hilfe, und je mehr Sie zu Hilfe nehmen können, desto besser. Ich bin unbesorgt. Was aus den Quellen des Rosenkreu­zertums heraus gesagt wird, Sie können es prüfen mit allen Mitteln. Prüfen Sie mit der materialistischen Kritik an den Evangelien, was ich über den Christus Jesus gesagt habe, prüfen Sie, was ich über Ge­schichte gesagt habe, an allen Quellen, die Ihnen zugänglich sind, prüfen Sie so genau als möglich mit den Mitteln, die Ihnen für den äußerlich-physischen Plan zu Gebote stehen! Ich bin überzeugt, je genauer Sie prüfen, um so mehr werden Sie das, was aus den Quellen des Rosenkreuzermysteriums heraus gesagt wird, der Wahrheit ent­sprechend finden. Darauf rechne ich, daß die Mitteilungen, welche aus dem Rosenkreuzertum heraus gemacht werden, nicht geglaubt, sondern geprüft werden, nicht oberflächlich, mit den oberflächlichen Methoden der gegenwärtigen Wissenschaft, sondern immer gewissen­hafter und gewissenhafter. Nehmen Sie alles, was die neueste Naturwissenschaft",
      "mit ihren neuesten Methoden Ihnen bieten kann, nehmen Sie alles, was die historischen oder religiösen Forschungen ergeben haben - ich bin unbesorgt. Je mehr Sie prüfen, desto mehr werden Sie bewahrheitet finden, was aus dieser Quelle heraus gesagt worden ist. Sie sollen nichts auf die Autorität hin annehmen. Das sind die besten Schüler der Geist-Erkenntnis, die das, was gesagt wird, zu­nächst als Anregung empfangen und es dann in den Dienst des Le­bens stellen, um es am Leben zu prüfen. Denn auch im Leben, auf jeder Stufe des Lebens, werden Sie prüfen können das, was aus den Quellen des Rosenkreuzertums heraus gesagt wird. Fern liegt es der Gesinnung, die dieser Darstellung zugrunde liegt, ein Dogma hinzu­stellen und zu sagen: Dies oder jenes ist so und so und muß geglaubt werden. Prüfen Sie das an dem, was Ihnen jetzt schon an seelisch markigen und gesunden Menschen entgegentreten kann, und Sie wer­den das selbst bewahrheitet finden, was wie ein prophetischer Hin­weis auf die zukünftige Christus-Offenbarung gesagt worden ist. Sie brauchen nur die Augen aufzumachen und unbefangen zu prüfen. Keine Anforderung an den Autoritätsglauben wird gestellt. Das ist eine Art Grundstimmung, die wie ein roter Faden alles geistige Emp­fangen durchdringen sollte.",
      "Also, ans Herz legen möchte ich Ihnen: Es ist nicht wahrhaft theo­sophisch, etwas als Dogma anzunehmen, weil es dieser oder jener ge­sagt hat; wahrhaft theosophisch ist es, sich anregen zu lassen aus der Geisteswissenschaft und das Empfangene im Leben zu prüfen. Da wird hinwegschwinden das, was eine wahrhaft theosophische An­schauung von irgendeiner Seite her färben könnte. Nicht orienta­lische, nicht okzidentalische Nuancen dürfen unsere Anschauungen färben. Der, welcher im rosenkreuzerischen Sinne spricht, kennt nicht Orientalismus und nicht Okzidentalismus; für ihn sind beide gleich sympathisch. Er stellt allein aus der inneren Natur der Tatsachen die Wahrheit dar. Das ist dasjenige, was wir ins Auge fassen müssen, ins­besondere ins Auge fassen müssen in einem so wichtigen Moment, wo wir hingewiesen haben auf den Volksgeist, der waltet in all den nörd­lichen Gebieten. In ihnen lebt der germanisch-nordisch-mythologi­sche Geist, wenn er auch heute noch unter der Oberfläche lebt, und",
      "er lebt viel weiter verbreitet in Europa, als man denkt. Wenn ein nördlicher Völkerstreit entstehen könnte, so könnte er nicht darin bestehen, daß ein Volksteil dem anderen streitig macht dasjenige, was zu geben ist, sondern daß ein jedes Volk Selbsterkenntnis übt und sich frägt: Was ist das Beste, was ich geben kann?",
      "Dann wird schon auf den gemeinsamen Altar fließen das, was zum Gesamtfortschritt, zur Gesamtwohlfahrt der Menschheit führt. Die Quellen dessen, was wir bringen können, liegen im Individuellen. Der germanisch-nordische Erzengel wird der gesamten Menschheitskultur der Zukunft gerade das bringen, wozu er veranlagt ist durch die mitbekommenen Anla­gen, welche wir annahernd charakterisiert haben.",
      "Er ist aber insbe­sondere befähigt, zu bewirken, daß das, was in der ersten Hälfte der fünften nachatlantischen Kulturzeit noch nicht gegeben werden konn­te, sich in der zweiten Hälfte noch abspielen kann, nämlich das, was als geistiges Element, prophetisch keimhaft, in der slawischen Phi­losopie und Volksempfindung gezeigt werden konnte. Solange sich das im Vorbereitungsstadium befindet, muß die erste Hälfte der fünf­ten nachatlantischen Kulturperiode zurückgelegt werden.",
      "Zunächst konnte da nur erreicht werden eine fein sublimierte geistige Anschau­ung als Philosophie. Von den Volkskräften muß diese dann erfaßt und durchdrungen werden, damit sie allgemeines Menschheitsgut werden kann, damit sie verständlich werden kann auf den weiten Terrains unseres Erdenlebens.",
      "Versuchen Sie es einmal, ob wir uns auf diesem Gebiete verstehen können; dann wird dieses sonst etwas gefährliche Thema doch nicht böse Früchte getragen haben, wenn wir alles, was hier zusammengekommen ist aus Nord-, Süd- und Ost-, West- und Mitteleuropa, so empfinden, daß es wichtig ist innerhalb der gesamten Menschheit; wenn wir fühlen, daß die großen Völker sowohl als die kleinen Volkssplitter ihre Mission haben und beizu­tragen haben ihren Teil für das Ganze. Zuweilen haben kleine Volks-splitter, weil sie alte oder neue Seelenmotive bewahren sollen, Aller-wichtigstes beizutragen.",
      "So kann, selbst wenn wir auch diese gefähr­liche Frage zum Gegenstand der Darstellung machen, nichts anderes dabei herauskommen als die Grundempfindung einer Seelengemein­schaft aller derjenigen, die vereinigt sind im Zeichen geisteswissenschaftlichen",
      "Denkens und Fühlens und der geisteswissenschaftlichen Ideale.",
      "Nur dann, wenn wir noch aus unseren Sympathien und Antipa­thien heraus empfinden würden, wenn wir undeutlich den Kern unserer Weltbewegung erfaßt hätten, könnten Mißverständnisse entstehen aus dem, was gesagt worden ist. Haben wir aber das er­faßt, was als Geist in diesen Vorträgen waltet, dann können auch die Dinge, die uns da entgegengetreten sind, dazu verhelfen, daß wir den festen Entschluß und das hohe Ideal fassen, dasjenige beizutragen zu dem gemeinsamen Ziele - jeder auf seinem Standpunkte und auf seinem Boden -, was in unserer Mission liegt.",
      "Wir können das am besten mit dem, was aus unserem Selbst, aus dem entspringt, wozu wir veranlagt sind. Wir dienen der gesamten Menschheit am besten, wenn wir das in uns besonders Veranlagte entwickeln, um es der ge­samten Menschheit einzuverleiben als ein Opfer, das wir dem fort­schreitenden Kulturstrom bringen.",
      "Das müssen wir verstehen lernen. Verstehen müssen wir lernen, daß es schlimm wäre, wenn die Geistes­wissenschaft nicht beitragen würde zur Entwickelung von Mensch, Engel und Erzengel, sondern beitragen würde zur Überwindung einer Volksgesinnung durch die andere.",
      "Nicht dazu ist die Geisteswissen­schaft da, dazu zu verhelfen, daß sich das, was als religiöses Bekenntnis irgendwo auf der Erde herrscht, ein anderes Gebiet erobern kann. Würde jemals der Okzident durch den Orient erobert werden oder umgekehrt, so entspräche das durchaus nicht der geisteswissenschaft­lichen Gesinnung.",
      "Allein das entspricht ihr, wenn wir unser Bestes, rein Menschliches für die gesamte Menschheit hingeben. Und wenn wir ganz in uns selber leben, aber nicht für uns, sondern für alle Menschen, so ist das wahrhafte geisteswissenschaftliche Toleranz.",
      "Das sind Worte, die ich anschließen mußte an unser bedenkliches Thema.",
      "Durch die Geisteswissenschaft - das werden wir immer mehr ein­sehen - wird alle Menschen-Zersplitterung aufhören. Deshalb ist ge­rade jetzt die richtige Zeit, die Volksseelen kennen zu lernen, weil die Geisteswissenschaft da ist, die uns dazu bringt, die Volksseelen nicht einander gegenüber zu stellen in Opposition, sondern sie auf­zurufen zu harmonischem Zusammenwirken. Je besser wir das verstehen,",
      "desto bessere Schüler der Geist-Erkenntnis werden wir sein. Dahin sollen die Darstellungen, die wir gegeben haben, zunächst aus­klingen. Ausklingen muß ja doch zuletzt das, was wir an Erkenntnis­sen sammeln, in unserem Empfinden, Fühlen und Denken und in un­serem geisteswissenschaftlichen Ideal. Je mehr wir dieses leben, desto bessere Schüler der Geisterkenntnis sind wir. Ich habe erlebt, daß man­che von denen, die mit heraufgezogen sind nach dem Norden, den be­sten Eindruck erhalten haben, was bei ihnen dadurch zum Ausdruck kam, daß sich ihnen das Wort auf die Lippen drängte: «Wie gern ich hier im Norden bin!»",
      "Und wenn wir mit den Worten des schweigsamen Asen Widar sprechen wollen: Wenn hohe Kräfte in der Menschheit in Zukunft erwacht sein werden, die wir ganz gewiß vor unseren Augen sehen werden, dann wird er der tätige, der aktive Freund des Zusammen-arbeitens, des Zusammen-Fleißigseins sein, in dessen Sinne wir alle zusammengewesen sind. Lassen Sie uns in diesem Sinne nach einigen Tagen des Beisammenseins wieder räumlich scheiden, uns aber im Geiste in diesem Sinne immer beisammen sein. Woher wir auch als Schüler der Geist-Erkenntnis kommen, von weit oder nah, mögen wir uns stets in Harmonie zusammenfinden, auch wenn wir uns einmal bei einem Thema fragen, was die Individualitäten dieser oder jener Erdengebiete sind. Wir wissen, daß das nur einzelne Opferflammen sind, die nicht auseinander züngeln, sondern zusammenschlagen wer­den zu dem gewaltigen Opferfeuer, das zum Wohle der Menschheit zusammenschlagen muß durch die geisteswissenschaftliche Weltan­schauung, die uns so sehr am Herzen liegt und tief in unserer Seele wurzelt."
    ],
    "sentences": [
      [
        "Bei Beginn dieser unserer letzten Betrachtungen darf ich wahrlich sagen, daß eigentlich noch recht, recht viel zu besprechen wäre, und daß im Grunde genommen das Allerwenigste von dem, was in dieses reiche Thema hereinfallen würde, im Verlaufe dieses Vortragszyklus wirklich hat besprochen werden können.",
        "Allein ich darf ja wohl hof­fen, daß es nicht zum letzten Male ist, daß wir über ähnliche Themen hier zusammen sprechen, und es muß genügen, wenn gerade über die­ses Thema, das in gewisser Beziehung einer weiteren Besprechung in der Gegenwart ohnedies noch einige Schwierigkeiten bietet, nur An­deutungen gegeben worden sind für den Anfang.",
        "Dabei ging das wie ein roter Faden durch die letzten Darstellungen hindurch, daß inner­halb der germanisch-nordischen Mythologie oder Götterlehre etwas enthalten ist, was in einer imaginativen Form wunderbar anknüpft an alles, was wir in erkenntnismäßiger Gestalt herausholen können aus der geistigen Forschung unserer Gegenwart.",
        "Das ist nun auch einer der Gründe, warum wir hoffen dürfen, daß jener Volksgeist, jener Erzengel, welcher seine erzieherische und führende Tätigkeit über dieses Land hier erstreckt, mit dem, was er als seine Anlagen im Laufe der Jahrhunderte entwickelt hat, durchdringen wird dasjenige, was moderne Philosophie, moderne Geistesforschung genannt werden kann, und daß von da aus diese moderne Geistesforschung eine im volkstümlichen Sinne gehaltene Befruchtung erlangen wird."
      ],
      [
        "Je weiter wir in die Einzelheiten der germanisch-nordischen My­thologie eindringen würden, desto mehr würden wir sehen, daß wun­derbar in den Bildern dieser Mythologie die größten okkulten Wahr­heiten zum Ausdrucke kommen, wie es wirklich in keiner anderen Mythologie der Fall ist.",
        "So erinnern sich vielleicht einige von Ihnen, die meine «Geheimwissenschaft» gelesen oder andere Darstellungen, die ich hier geben durfte, mit angehört haben, daß einmal im Verlaufe der Erdenevolution ein Vorgang stattfand, den wir bezeichnen kön­nen als das Herabsteigen jener Seelen der Menschen, die in uralten"
      ],
      [
        "Zeiten, vor der alten lemurischen Periode, hinaufgestiegen sind zu den einzelnen Planeten unseres Planetensystems, die aus ganz besonderen Gründen hinaufgestiegen sind zu Saturn, Jupiter, Mars, Venus, Mer­kur, und daß diese während der letzten lemurischen und der ganzen atlantischen Zeit sich zu vereinigen strebten mit dem, was der Men­schenleib nach und nach entwickelt und an Anlagen ausgebildet hatte, die möglich geworden waren durch das Hinausgehen des Mondes aus unserer Erde.",
        "Da sind sie heruntergestiegen, diese Saturn-, Jupiter-, Mars-, Venus- und Merkurseelen.",
        "Das ist ein Vorgang, den man heute noch finden kann in der Akasha-Chronik.",
        "Daß im Laufe der atlanti­schen Zeit die Wasser nebelförmig die Luft der Atlantis durchdran­gen, das war ein Zustand, der damals damit zusammenhing, daß eben diese Seelen herunterstiegen, die man mit dem alten Hellsehen der atlantischen Zeit wahrnahm.",
        "Immer wieder, wenn neue Wesen ge­boren wurden in dem dazumal noch plastisch-weichen, biegsamen, bildsamen Leibe, wenn solche sozusagen aus geistigen Höhen her­unterstiegen, so betrachtete man das als den äußeren Ausdruck dafür, daß aus der geistigen Umgebung, aus der Atmosphäre, aus dem pla­netarischen Dasein, Seelen herunterstiegen, um sich mit den auf der Erde entstehenden Leibern zu vereinigen."
      ],
      [
        "Der Vorgang, wie sich gleichsam die Erdenleiber der Befruchtung dessen erschließen, was aus Himmelshöhen herunterstrahlt, dieser Vorgang hat sich erhalten in der Anschauung, die sich hineinver­pflanzt hat in die nordisch-germanische Mythologie.",
        "Das Bewußtsein davon hat sich so lange erhalten, daß es selbst Tacitus noch bei den südlicheren Germanen fand in der Zeit, da er die Beobachtungen machte, die er in seiner «Germania» beschrieb.",
        "Niemand wird die Er-zählung verstehen, die Tacitus von der Göttin Nerthus gibt, der nicht weiß, daß es diesen Vorgang einmal gegeben hat.",
        "Der Wagen der Göttin Nerthus wird über die Gewässer gefahren.",
        "Später hat sich das als Ritual, als Ritus erhalten.",
        "In früherer Zeit war es Beobachtung.",
        "Dargeboten hat diese Göttin das, was an Menschenleibern dargeboten werden konnte den aus den planetarischen Sphären herunterdringen­den Menschenseelen.",
        "Das ist der geheimnisvolle Vorgang, der dem Nerthus-Mythus zugrunde liegt, und der in alledem sich erhalten hat,"
      ],
      [
        "was in den älteren Sagen und Legenden, bei denen auf das Werden des physischen Menschen hingedeutet wird, uns überliefert ist.",
        "Njordr, der innerlich verwandt ist mit der Göttin Nerthus, ist das männliche Gegenbild.",
        "Der soll uns darstellen die uralte Erinnerung an das Hin­untersteigen der geistig-seelischen Menschen, die einst hinaufgestiegen waren in planetarische Höhen, und die während der atlantischen Zeit wieder heruntergestiegen sind, um sich mit physischen Menschenlei­bern wiederum zu vereinigen."
      ],
      [
        "Aus meiner kleinen Schrift «Blut ist ein ganz besonderer Saft» kön­nen Sie entnehmen, welche bedeutungsvolle Rolle Völkermischungen und Völkerzusammenhänge in gewissen Zeiten gespielt haben.",
        "Nun haben nicht nur Völkermischungen und Völkerzusammenhänge, die ihren Ausdruck in der Blutmischung gefunden haben, sondern auch die geistigen und seelischen Förderungen der Volksgeister eine große Rolle gespielt."
      ],
      [
        "Die Anschauung jenes Hinuntersteigens ist am reinsten erhalten auf dem Grunde jener Sagenwelt, welche sich in früherer Zeit in diesen nordischen Gebieten gebildet hat.",
        "In den Wanensagen können Sie daher eine älteste Erinnerung an solche Dinge noch finden."
      ],
      [
        "Insbesondere war hier im Norden lebendig, in der finnischen Tradi­tion, die Erinnerung an diese Verbindung des Geistig-Seelischen, das aus planetarischen Höhen herunterstieg, mit dem, was aus dem Erden-leib selber hervorgegangen ist und was die nordische Tradition als «Riesenheim» kennt.",
        "Was sich aus dem Erdenleib entwickelt hat, das gehört zu Riesenheim."
      ],
      [
        "So begreifen wir es, daß der nordisch-germa­nische Mensch immer den Impuls von dieser Seite her gefühlt hat, daß er fühlte, wie in seiner Seele, die sich nach und nach ausgebildet hat, dieser alte Götterblick arbeitete, der hier noch heimisch war, als die Nebelwasser der Atlantis noch hinüberreichten in diese Gegend in der alten Zeit.",
        "Es fühlte der nordisch-germanische Mensch in seiner Seele etwas von der Herkunft eines Gottes, der abstammte direkt von jenen göttlich-geistigen Wesenheiten, jenen Erzengelwesenheiten, die das Zusammenfügen des Seelisch-Geistigen mit dem Irdisch-Physi­schen leiteten."
      ],
      [
        "Freyr, der Gott, und Freya, seine Schwester, die ja hier im Norden einstmals ganz besonders beliebte Gottheiten waren, wa­ren in ihrem Ursprung gedacht und empfunden als diejenigen Engelwesen,"
      ],
      [
        "welche in die menschliche Seele gegossen haben alles dasjenige, was diese menschliche Seele brauchte, um unmittelbar auf dem physi­schen Plane fortzuentwickeln die alten, durch das hellseherische Ver­mögen aufgenommenen Kräfte.",
        "Freyr war innerhalb der physisch-sinnlichen Welt, innerhalb der auf die äußeren Sinne beschränkten Welt der Fortsetzer alles dessen, was früher im Hellsehen aufgenom­men worden ist."
      ],
      [
        "Er war die lebendige Fortsetzung der hellseherisch aufgenommenen Kräfte.",
        "Daher mußte er sich verbinden mit dem, was im menschlichen Leibe selber als physisch-leibliche Werkzeuge vor­handen ist für diese Seelenkräfte, die dann in den physischen Plan hineintragen das, was im uralten Hellsehen wahrgenommen wurde."
      ],
      [
        "Das spiegelt sich in der Ehe des Freyr mit Gerd, der Riesentochter.",
        "Sie ist den physischen Kräften des Erdenwerdens selber entnommen.",
        "In diesen Vorstellungen spiegelt sich noch nach das Herabsteigen des Göttlich-Geistigen in das Physische."
      ],
      [
        "Ganz wunderbar ist ausgedrückt in dieser Freyrgestalt, wie Freyr sich dessen bedient, was dem Men­schen auf dem physischen Plane möglich macht, auszuleben das, wozu er erzogen ist durch seine vorhergehenden hellseherischen Wahrneh­mungen.",
        "Bluthuf heißt das Pferd, das dem Freyr zur Verfügung steht, um anzudeuten, daß das Blut das Wesentliche ist, um sein Ich zu ent­wickeln."
      ],
      [
        "Ein merkwürdiges, wunderbares Schiff steht auch dem Freyr zur Verfügung.",
        "Ausgebreitet kann es werden ins Unermeßliche, und zusammengefaltet kann es werden, so, daß es in den kleinsten Kasten hineingeht."
      ],
      [
        "Was ist nun dieses Wunderschiff?",
        "Wenn Freyr die Macht ist, die hineinträgt die hellseherischen Kräfte in die Gebiete, die sich auf dem physischen Plane ausleben, dann muß es das sein, was ihm ganz besonders eigen ist: die Abwechslung zwischen Tagwachen und Nachtschlafen."
      ],
      [
        "Und wie die Menschenseele sich während des Schla­fens bis zum Wiederaufwachen ausbreitet im Makrokosmos, so breitet sich das Wunderschiff aus und wird dann wieder zusammengefaltet in die Gehirnfalten, um dann während der Tageszeit in dem kleinsten Kasten - dem Menschenschädel - untergebracht zu werden.",
        "Das alles finden Sie in einer wunderbaren Weise in dieser nordisch-germani­schen Mythologie, in diesen Bildercharakteren."
      ],
      [
        "Diejenigen von Ihnen, die näher eingehen werden auf diese Dinge,"
      ],
      [
        "werden sich nach und nach überzeugen, daß es keine Phantastik ist, sondern daß es wirklich aus den Schulen der Eingeweihten stammt, was mit diesen Bildern hineinverpflanzt, hineingeimpft worden ist in die Volksseele, in das Volksgemüt.",
        "So ist ungeheuer viel geblieben in dem leitenden Erzengel, in dem Volksgeist im Norden, von dem, was alte Erziehung war durch hellseherische Wahrnehmung, von dem, was in einer Seele werden kann, die sozusagen in ihrer Entwickelung auf dem physischen Plane sich anschließt an eine hellseherische Entwicke­lung."
      ],
      [
        "Wenn das Äußerliche heute auch anders aussieht, der Erzengel des germanischen Nordens hat in sich diese Anlage, und mit dieser An­lage ist er ganz besonders geeignet, dasjenige zu verstehen, was mo­derne Geisteswissenschaft ist, und es umzuwandeln in dem Sinne, wie es im Sinne volkstümlicher Kraft umgewandelt werden muß.",
        "Daher werden Sie auch verstehen, wenn gesagt wird, daß die besten Bedin­gungen gegeben sind gerade innerhalb des germanisch-nordischen Wesens, um das zu verstehen, was ich nur andeutend sagen konnte in dem hier gehaltenen öffentlichen Vortrage von der Wiederoffenba­rung des Christus."
      ],
      [
        "Da zeigt uns die Geistesforschung in unserer jetzi­gen Zeit, daß nachdem das Kali Yuga abgelaufen ist, das fünftausend Jahre gedauert hat - ungefähr von 3100 v.",
        "Chr. bis 1899-, im Men­schen sich neue Fähigkeiten heranentwickeln."
      ],
      [
        "Sie werden zunächst bei einzelnen, wenigen zum Vorschein kommen, die für diese Fähigkeiten besonders geeignet sind.",
        "Da wird zum Beispiel eintreten, daß Men­schen aus der naturgemäßen Evolution ihrer Fähigkeiten heraus von dem etwas sehen werden, was heute nur durch die Geisteswissen­schaft, nur von der geistigen Forschung aus verkündet wird."
      ],
      [
        "Da wird uns erzählt, daß in Zukunft die Menschen, bei denen die Organe des Ätherleibes entwickelt sind, in immer größerer Zahl auftreten und zum Hellsehen kommen werden, zu dem man heute nur durch Schu­lung kommen kann.",
        "Und warum wird es so sein?"
      ],
      [
        "Was wird der Äther-leib für die Anschauung einiger Menschen haben?",
        "Menschen wird es geben, die Eindrücke haben werden, von denen ich einen etwa so schildern möchte.",
        "Es wird der Mensch etwas tun in der äußeren Welt, und er wird sich dabei gedrängt fühlen, etwas zu bemerken."
      ],
      [
        "ihm wie eine Art von Traumbild vor die Augen treten, das er zunächst nicht verstehen wird.",
        "Hat er aber etwas gehört von Karma, von der Gesetzmäßigkeit im Weltgeschehen, so wird er es nach und nach ver­stehen lernen, denn es ist das karmische Gegenbild seiner Taten in der Ätherwelt, das er gesehen hat.",
        "So bilden sich nach und nach die er­sten Elemente künftiger Fähigkeiten."
      ],
      [
        "Diejenigen Menschen, die sich durch die Geisteswissenschaft anre­gen lassen, werden nach und nach erleben können - von der Mitte des zwanzigsten Jahrhunderts an - eine Wiedererneuerung desjeni­gen, was Paulus im ätherischen Hellsehen gesehen hat als ein kom­mendes Mysterium, als das Mysterium des lebenden Christus.",
        "Es wird eine neue Offenbarung des Christus sein, eine Offenbarung wie sie kommen muß, wenn die menschlichen Fähigkeiten in naturgemäßer Weise sich dahin entwickeln, daß der Christus von den Menschen gesehen werden kann in der Welt, in der er seit dem Mysterium von Golgatha immer war und in der er für den Eingeweihten auch zu fin­den ist."
      ],
      [
        "In diese Welt wächst die Menschheit hinein, um vom phy­sischen Plane aus wahrnehmen zu können, was sonst nur in den My­sterienschulen, von höheren Planen aus, gesehen wurde.",
        "Trotzdem wird die Mysterienschulung nicht überflüssig."
      ],
      [
        "Sie gibt die Dinge noch immer in anderer Art, als sie der nichtgeschulten Seele vorliegen.",
        "Aber das, was von der Mysterienschulung gegeben wird, wird durch Umwandelung des physischen Menschenleibes das Mysterium des le­benden Christus in einer neuen Weise zeigen, wie es perspektivisch von dem physischen Plan aus gesehen werden kann, wie es im Äther wird gesehen werden können, zuerst von einzelnen Menschen, dann aber von immer mehr und mehr Menschen im Laufe der nächsten dreitausend Jahre."
      ],
      [
        "Dasjenige, was Paulus gesehen hat als den lebenden Christus, der in der Ätherwelt zu finden ist seit dem Ereignis von Golgatha, wird von immer mehr Menschen geschaut werden können."
      ],
      [
        "Immer höher werden die Offenbarungen des Christus liegen.",
        "Das ist das Mysterium der Entwickelung des Christus.",
        "Da die Menschen zur Zeit, als das Mysterium von Golgatha sich vollzog, alles von dem physischen Plane aus auffassen sollten, so war es notwendig, daß sie auch auf dem physischen Plan den Christus sehen konnten, daß sie"
      ],
      [
        "Nachricht von ihm bekommen und sein Walten auf dem physischen Plan bezeugen konnten.",
        "Aber die Menschheit ist auf Fortschritt an­gelegt, auf die Entwickelung höherer Kräfte, und derjenige müßte nichts wissen von dem Fortschritte der Menschheit, der glauben woll­te, daß die Offenbarungen des Christus in derselben Weise, wie sie vor 1900 Jahren nötig war, sich wiederholen wird.",
        "Dazumal geschah sie auf dem physischen Plan, weil die Kräfte des Menschen auf den physischen Plan eingestellt waren.",
        "Aber die Kräfte des Menschen werden sich entwickeln, und dadurch wird Christus zu den erhöhten menschlichen Kräften im Laufe der nächsten 3000 Jahre immer mehr und mehr sprechen können."
      ],
      [
        "Das, was ich jetzt eben gesagt habe, ist eine Wahrheit, die seit langem einzelnen wenigen Menschen mitgeteilt worden ist aus den esoterischen Schulen heraus, und es ist eine Wahrheit, die insbesondere auf dem Boden der Geisteswissenschaft heute gefunden werden muß aus dem Grunde, weil die Geisteswissenschaft eine Vorschule sein soll für dasjenige, was da kommen wird.",
        "Die Menschheit ist jetzt ein­gestellt auf Freiheit, auf Selbstanerkennung dessen, was sich in ihr bildet, und es könnte geschehen, daß diejenigen Menschen, die als erste Pioniere der Christus-Anschauung sich einstellen werden, als Narren verschrieen werden mit dem, was sie der Menschheit darzu­bieten haben, und es könnte die Menschheit weiter noch versinken in den Materialismus, als sie dies bis jetzt schon ist, und tottreten das, was eine wunderbarste Offenbarung für die Menschheit werden könnte.",
        "Alles, was in Zukunft geschehen kann, ist in gewissem Grade in den Willen der Menschheit gestellt, so daß die Menschen auch ver­fehlen können, was zu ihrem Heile ist.",
        "Das ist außerordentlich wich­tig, daß die Geisteswissenschaft eine Vorbereitung ist für dasjenige, was die neue Christus-Offenbarung sein wird."
      ],
      [
        "Der Materialismus kann in zweifacher Weise da einen Fehler ma­chen.",
        "Der eine, der wahrscheinlich gemacht werden wird aus den Traditionen des Okzidents heraus, besteht darin, daß es als eine wilde Phantastik, als eine wüste Narretei angesehen werden wird, was die ersten Pioniere der neuen Christus-Offenbarung aus ihrer eigenen An­schauung heraus im zwanzigsten Jahrhundert verkündigen werden."
      ],
      [
        "Der Materialismus hat alle Kreise heute ergriffen.",
        "Er ist nicht nur im Okzident heimisch, er hat auch den Orient erfaßt; nur in einer anderen Form kommt er da zum Vorschein.",
        "Es könnte sein, daß der orientalische Materialismus dahin führen werde, daß die Menschen verkennen das Höhere einer Christus-Offenbarung auf einer höheren Stufe, und daß eintreten wird dasjenige, was hier so oft gesagt wurde und immer wieder gesagt werden wird: daß materialistisches Denken das Erscheinen des Christus in eine materialistische Anschauung um­setzen wird.",
        "Es könnte sein, daß man in jener Zeit unter dem Einfluß der geisteswissenschaftlichen Wahrheiten zwar sprechen dürfte da­von, daß der Christus sich offenbaren wird, aber gleichzeitig glaubt, daß Christus in einem materiellen Leibe erscheinen wird.",
        "Das Ergebnis wäre dann ein anders gefärbter Materialismus.",
        "Da würde sich nur fortsetzen, was seit Jahrhunderten gewesen ist."
      ],
      [
        "Diesen falschen Materialismus haben sich immer wieder die Men­schen zunutze gemacht, und zwar so, daß sich einzelne Menschen für den wiedererschienenen Christus ausgaben.",
        "Der letzte bedeutendere Fall eines derartigen falschen Christus war im siebzehnten Jahrhun­dert, wo ein Mann namens Sabbatai Z'vi aus Smyrna als der wieder-erschienene Christus auftrat.",
        "Er hat großes Aufsehen gemacht.",
        "Zu ihm sind hingepilgert nicht nur die Menschen, die in der unmittel­baren Umgebung waren, sondern Leute aus Ungarn, Polen, Deutsch­land, Frankreich, Italien und Nordafrika.",
        "Überall wurde in Sabbatai Z'vi die physische Inkarnation eines Messias gesehen.",
        "Ich möchte nicht die Menschheitstragik erzählen, die sich an die Persönlichkeit des Sabbatai Z'vi knüpft.",
        "Im siebzehnten Jahrhundert war diese Tra­gik allerdings nicht besonders groß.",
        "Der Mensch war damals noch nicht so sehr unter den freien Willen gestellt; aber er konnte durch seine Erkenntnis, die ein spirituelles Empfinden war, erkennen, was die Wahrheit ist.",
        "Das Unglück wäre aber groß im zwanzigsten Jahr­hundert, wenn unter dem Drucke des Materialismus die Lehre, daß Christus sich offenbaren wird, eine materialistische Ausdeutung er­fahren würde in der Weise, als ob Christus im physischen Leibe wie­derkommen könnte.",
        "Damit würde die Menschheit nur beweisen, daß sie keine Anschauung und keine Einsicht gewonnen hat bezüglich des"
      ],
      [
        "wirklichen Fortschrittes der menschlichen Entwickelung zu höheren geistigen Kräften.",
        "Falsche Messiasse werden ganz gewiß auftreten, und sie werden aus dem Materialismus unserer Zeit ebenso Zuspruch erhalten, wie Sabbatai Z'vi im siebzehnten Jahrhundert.",
        "Es wird eine Probe, eine harte Prüfung sein für die geistig Vorbereiteten, zu er­kennen, wo die Wahrheit liegt, ob sich in die spirituellen Theorien wirklich auch spirituelles lebensvolles Empfinden hineinlebt, oder ob in diesen spirituellen Theorien nur ein versteckter Materialismus lebt.",
        "Da wird die Probe sein auf die Fortentwickelung der Geisteswissen­schaft, ob Menschen genug durch diese Geisteswissenschaft entwickelt sein werden, welche einsehen können, daß sie den Geist im Geiste zu schauen haben, daß sie hinaufzuschauen haben in die ätherische Welt, hinaufzuschauen auf eine Neuoffenbarung des Christus, oder ob sie auf dem physischen Plane stehen bleiben und eine Offenbarung im physischen Leibe, die sich auf den Christus bezieht, sehen wollen.",
        "Diese Prüfung wird unsere Bewegung noch bestehen müssen.",
        "Wir kön­nen aber sagen, daß nirgends besser der Boden vorbereitet ist, gerade auf diesem Gebiete die Wahrheit zu erkennen, als da, wo die germa­nisch-nordische Mythologie ersprossen ist."
      ],
      [
        "In dem, was uns als Götterdämmerung überliefert ist, ist eine be­deutsame Zukunftsvision enthalten, und damit komme ich auf ein Kapitel, von dem ich sozusagen schon den Ausgangspunkt angedeutet habe.",
        "Ich habe Ihnen gesagt, daß innerhalb einer Volksgemeinschaft, die das, was hellseherische Vergangenheit ist, erst so kurze Zeit hinter sich hat, auch ein heilseherischer Sinn in dem leitenden Volksgeiste entwickelt ist, um das, was uns heilseherisch erblüht, wieder zu ver­stehen.",
        "Wenn nun eine Menschheit gerade auf dem Boden die neue Zeit mit neuen menschlichen Fähigkeiten erlebt, wo die germanisch-nordi­sche Mythologie erblühte, da soll sie verstehen, daß dasjenige, was altes Hellsehen war, eine andere Gestalt erfahren muß, nachdem der Mensch durchgegangen ist durch die Entwickelung des physischen Planes.",
        "Da hat eine Weile geschwiegen das, was aus dem alten Hell-sehen heraus gesprochen hat; da hat eine Weile hinter dem Menschen gestanden, sich dem menschlichen Blicke entzogen die Welt des Odin und Thor, des Baldur und Hödur, des Freyr und der Freya.",
        "Aber hervorkommen"
      ],
      [
        "wird sie wieder in einer Zeit, wo andere Kräfte mittler­weile an der menschlichen Seele gearbeitet haben.",
        "Wenn diese mensch­liche Seele mit dem neuen Hellsehen, das mit ätherischem Hellsehen beginnt, hineinschauen wird in die neue Welt, dann wird sie sehen, daß sie sich nicht halten kann an die alten Formen der die Seele er­ziehenden Kräfte."
      ],
      [
        "Würde sie sich daran halten können, dann würden auch all die Gegenkräfte hervortreten gegen die Kraft, die in alten Zeiten hat erziehen sollen die menschlichen Kräfte zu einer gewissen Höhe.",
        "Odin und Thor werden wieder dastehen vor dem Blicke der Menschheit, jetzt aber so, daß die menschliche Seele eine neue Ent­wickelung durchgemacht haben wird."
      ],
      [
        "Der menschlichen Seele wird alles erscheinen, was die Gegenkräfte des Odin und Thor sind.",
        "Alles, was sich als Gegenkraft entwickelt hat, wird in einem gewaltigen Tableau wieder sichtbar werden.",
        "Aber nicht vorwärtskommen würde die menschliche Seele, nicht wehren gegen Schädliches würde sie sich können, wenn sie sich nur den Kräften unterwerfen würde, welche im alten Hellsehen gesehen worden sind."
      ],
      [
        "Thor hat einst den Menschen das Ich gegeben.",
        "Das Ich hat sich erzogen auf dem physischen Plane, hat sich herausentwickelt aus dem, was Loki, die luziferische Gewalt, im Astralleibe zurückgelassen hatte, aus der Midgardschlange."
      ],
      [
        "Das, was einst Thor geben konnte, und worüber die menschliche Seele hin­auswächst, das steht im Kampfe mit dem, was aus der Midgard­schlange kommt.",
        "Das tritt uns in der nordischen Mythologie als der mit der Midgardschlange kämpfende Thor entgegen."
      ],
      [
        "Gegenseitig hal­ten sie sich das Gleichgewicht, das heißt sie töten einander.",
        "Ebenso waltet Odin gegen den Fenriswolf, wobei sie sich gegenseitig vernich­ten.",
        "Dasjenige, was eine Weile die menschliche Seelenkraft gebildet hat, Freyr, das muß unterliegen demjenigen, was dem auf dem physi­schen Plan mittlerweile herangezogenen Ich aus den Erdenkräften selber heraus gegeben worden ist."
      ],
      [
        "Freyr unterliegt dem Flammen­schwert des aus der Erde entsprossenen Surtur."
      ],
      [
        "Alle diese Einzelheiten, die in der Götterdämmerung hingestellt sind, werden dem entsprechen, was in einer neuen, in die Zukunft wirklich hineinweisenden Äthervision vor der Menschheit stehen wird.",
        "Zurückbleiben wird der Fenriswolf.",
        "Oh, darin, daß dieser Fenriswolf"
      ],
      [
        "zurückbleibt im Kampfe gegen Odin, verbirgt sich eine tiefe, tiefe Wahrheit.",
        "Es wird in der nächsten Zukunft der Menschheit nichts so sehr gefährlich werden, als wenn der Hang, beim alten, nicht durch neue Kräfte entwickelten Hellsehen zu bleiben, die Men­schen dazu verführen könnte, stehen zu bleiben bei dem, was das alte, astrale Hellsehen in Urzeiten geben konnte, nämlich solche Seelen-bilder wie der Fenriswolf.",
        "Es wäre wieder eine harte Prüfung für das­jenige, was auf dem Boden der Geisteswissenschaft erwachsen muß, wenn etwa auch auf diesem Boden der Hang entstehen würde zu aller­lei ungeklärtem, chaotischem Hellsehen, die Neigung, nicht das von Vernunft und Wissenschaft durchleuchtete Hellsehen höher zu schät­zen, sondern das alte, chaotische, dem dieser Vorzug abgeht."
      ],
      [
        "Mit furchtbarer Gewalt würden sich rächen solche Überbleibsel alten Hellsehens, die mit allerlei chaotischen Bildern die Anschauun­gen der Menschen verwirren könnten.",
        "Einem solchen Hellsehen könn­te nicht mit demjenigen begegnet werden, was selber aus alter Hell­seherkraft entstand, sondern nur mit dem, was während des Kali Yuga als gesunde Kraft zu einem neuen Hellsehen herangebildet wor­den ist.",
        "Nicht dasjenige, was an Kraft der alte Erzengel Odin gegeben hat, nicht die alten hellseherischen Kräfte können retten; da muß et­was weit anderes kommen.",
        "Dieses andere aber kennt die germanisch­nordische Mythologie.",
        "Von dem weiß sie, daß es vorhanden ist.",
        "Sie weiß, daß die Äthergestalt lebt, in der sich inkarnieren soll dasjenige, was wir wiedersehen sollen als ätherische Christusgestalt.",
        "Und dieser erst wird es gelingen, auszutreiben, was an ungeklärter hellseherischer Kraft die Menschheit verwirren wird, wenn Odin nicht vernichtet den Fenriswolf, der nichts anderes repräsentiert als die zurückgeblie­bene Hellseherkraft.",
        "Widar, der sich schweigend verhalten hat wäh­rend der ganzen Zeit, der wird den Fenriswolf überwinden.",
        "Das sagt uns auch die Götterdämmerung."
      ],
      [
        "Wer Widar in seiner Bedeutung erkennt und ihn in seiner Seele fühlt, der wird finden, daß im zwanzigsten Jahrhundert den Men­schen wieder die Fähigkeit gegeben werden kann, den Christus zu schauen.",
        "Der Widar wird wieder vor ihm stehen, der uns allen ge­meinschaftlich ist in Nord- und Mittel-Europa.",
        "Er wurde geheim gehalten"
      ],
      [
        "in den Mysterien und Geheimschulen als ein Gott, der erst in Zukunft seine Mission erhalten wird.",
        "Selbst von seinem Bilde wird nur unbestimmt gesprochen.",
        "Das mag hervorgehen daraus, daß ein Bild in der Nähe von Köln gefunden worden ist, von dem man nicht weiß, wen es darstellt, das aber nichts anderes bedeutet als ein Bild­nis von Widar."
      ],
      [
        "Durch das Kali Yuga hindurch wurden die Kräfte erworben, die die neuen Menschen befähigen sollen, die neue Christus-Offenbarung zu schauen.",
        "Diejenigen, welche berufen sind, aus den Zeichen der Zeit heraus zu deuten das, was da kommen muß, wissen, daß die neue Geistesforschung wieder aufrichten wird die Kraft Widars, der alles dasjenige aus den Gemütern der Menschen vertreiben wird, was als Überbleibsel chaotischer alter Hellseherkräfte verwirrend wirken könnte, und der das neu sich heranentwickelnde Hellsehen in der menschlichen Brust, in der menschlichen Seele wachrufen wird."
      ],
      [
        "So sehen wir, indem uns aus der Götterdämmerung herausglänzt die wundersame Gestalt des Widar, daß uns sozusagen eine Hoffnung für die Zukunft aus der germanisch-nordischen Mythologie entgegen-leuchtet.",
        "Indem wir uns verwandt fühlen gerade mit der Gestalt des Widar, den wir nun in seiner tieferen Wesenheit erfassen wollen, hof­fen wir, daß dasjenige, was der Grundnerv und die lebendige Essenz alles geisteswissenschaftlichen Wesens sein muß, sich aus jenen Kräf­ten, welche der Erzengel der germanisch-nordischen Welt zu der mo­dernen Zeitentwickelung hinzubringen kann, wird ergeben können.",
        "Ein Teil erst von einem größeren Ganzen ist für den fünften nach-atlantischen Kulturzeitraum an Menschheits- und Geistesentwickelung geleistet worden, ein anderer Teil muß noch geleistet werden.",
        "Am meisten werden zu dieser Leistung beizutragen haben diejenigen aus der Summe der nordisch-germanischen Völker heraus, die in sich füh­len, daß sie elementare, frische Völkerkraft in sich haben.",
        "Aber es wird das gewissermaßen in die Seelen der Menschen gelegt werden.",
        "Sie werden sich selbst entschließen müssen, zu arbeiten.",
        "Im zwanzig­sten Jahrhundert kann man irren, weil es in gewisser Weise in die Freiheit der Menschen gestellt sein muß, was erreicht werden soll, weil es nicht unter Zwang gesetzt sein darf.",
        "Daher handelt es sich darum,"
      ],
      [
        "ein richtiges Verständnis dessen zu haben, was kommen soll.",
        "So sehen Sie, daß, wenn aus unserer heutigen Geisteswissenschaft heraus-spricht die Erkenntnis des Christus-Wesens, und wenn wir anknüpfen an die wahre Erkenntnis dieses Christus-Wesens, das wir aus europäi­schen Volkssubstanzen selber heraussuchen, wenn wir daran knüpfen unsere Zukunftshoffnungen, so beruht das wirklich nicht auf irgend­einer Vorliebe oder irgendeiner Temperamentsanlage."
      ],
      [
        "Es ist manchmal gesagt worden, daß man nennen könne wie man wolle dasjenige, was man als erstes Wesen in der Menschheitsevolu­tion bezeichnen kann.",
        "Niemals wird derjenige, der das Christus-Wesen erkennt, sich darauf versteifen, daß der Name des Christus bleibt.",
        "Aber, wenn wir den Christus-Impuls im richtigen Sinne ver­stehen, so werden wir auch nicht so sprechen, daß wir sagen: Ein We­sen lebt in der Menschheitsevolution, in der Menschheit des Westens und Ostens, und das muß so sein, daß es den Sympathien der Mensch­heit für diese oder jene Wahrheit entspricht. - Das ist nicht okkul­tistisch.",
        "Okkultistisch ist es, daß in dem Augenblicke, wo man erken­nen würde, daß dieses Wesen getauft werden müßte auf den Namen des Buddha, dies rückhaltlos getan wird, ganz gleich, ob es einem sympathisch oder antipathisch ist.",
        "Nicht auf Sympathie oder Anti­pathie kommt es also an, sondern auf die Wahrheit der Tatsachen."
      ],
      [
        "In dem Augenblicke, wo uns die Tatsachen anders belehren wür­den, wären wir bereit, anders zu handeln.",
        "Einzig und allein die Tat­sachen müssen maßgebend sein.",
        "Wir wollen keinen Orientalismus und keinen Okzidentalismus hineintragen in das, was wir als eigentliches Lebensblut unserer Geisteswissenschaft ansehen, und wenn wir her­ausfinden sollten in der nordisch-germanischen Erzengelwelt das­jenige, was einen befruchtenden Keim abgeben kann für die wahr-hafte Geisteswissenschaft, so wird es etwas sein, was nicht gegeben wird auf diesem Boden für ein einzelnes Volk oder einen einzelnen Stamm, sondern was der gesamten Menschheit gegeben wird.",
        "Das, was der gesamten Menschheit gegeben wird, gegeben werden muß, kann zwar an diesem oder jenem Orte entspringen, gegeben werden muß es aber der gesamten Menschheit.",
        "Wir kennen nicht einen Unter­schied zwischen Orient und Okzident; wir nehmen mit inniger Liebe"
      ],
      [
        "dasjenige auf, was wir als das überwältigend Große der uralten Kul­tur der heiligen Rishis in ihrer wahren Gestalt kennen; wir nehmen mit Liebe auf die persische Kultur, nehmen mit Liebe auf dasjenige, was wir als ägyptisch-chaldäische und griechisch-lateinische Kulturen kennen; wir nehmen auch mit ebensolcher Objektivität auf, was uns aus dem europäischen Boden erwachsen ist.",
        "Nur die Notwendigkeit der Tatsachen zwingt uns, die Angaben so zu machen, wie sie ge­macht werden."
      ],
      [
        "Indem wir alles empfangen von der gesamten Menschheit, alles, was jede Religion beizutragen hat zum Kulturprozeß der Menschheit, aufnehmen in das, was wir heute erkennen, was wir heute Gemeingut der Menschheit nennen, indem wir das mehr und mehr tun, sind wir gerade im Sinne des Christus-Prinzips tätig.",
        "Da es fortentwickelungs­fähig ist, so müssen wir das überwinden, was es in den ersten Jahr­hunderten und Jahrtausenden durchmachen mußte, wo das Christus-Prinzip in den unvollkommensten Anfängen begriffen war."
      ],
      [
        "Wir sehen nicht in diese Vergangenheit, lassen uns auch nicht von ihr belehren, Uns liegt nichts an dieser Überlieferung, uns liegt in der Hauptsache an dem, was aus der geistigen Welt heraus erforscht werden kann, Deshalb sehen wir das Wichtigste des Christus-Prinzips nicht in dem, was war - und wenn es noch so oft betont wird, aus der Tradition heraus -, sondern in dem, was da kommen wird.",
        "Wir berufen uns nicht so sehr auf das, was historisch überliefert wird, sondern suchen zu wissen das, was da kommen wird."
      ],
      [
        "Das ist der Schwerpunkt des Christus-Impulses, der in den Anfang des christlichen Zeitalters fällt, und wir geben nicht viel auf das Äußerlich-Historische.",
        "Nachdem das Christentum die Kinderkrankheiten durchgemacht hat, wird es sich weiter entwickeln."
      ],
      [
        "Es ist auch in fremde Länder gegangen und wollte die Menschen zu dem bekehren, was man in den einzelnen christlichen Dogmen eines Zeitalters gehabt hat.",
        "Vor unserer Seele steht aber ein Christentum, von dem wir wissen, daß Christus in allen Zeiten wirk­sam war, und daß wir Christus finden werden an allen Orten, wohin wir kommen, daß das Christus-Prinzip das allergeisteswissenschaft­lichste Prinzip ist."
      ],
      [
        "Und wenn der Buddhismus nur als Buddhisten gel­ten läßt diejenigen, welche auf Buddha schwören, dann wird das"
      ],
      [
        "Christentum dasjenige sein, das auf keinen Propheten schwört, weil es nicht unter dem Eindruck eines völkischen Religionsstifters steht, sondern den Menschheitsgott anerkennt."
      ],
      [
        "Derjenige, der das Christentum kennt, weiß, daß es sich dabei um ein Mysterium handelt, das auf Golgatha auf dem physischen Plane zur Anschauung gekommen ist.",
        "Die Anschauung dieses Mysteriums ist es, die uns in der Richtung führt, die ich geschildert habe.",
        "Man kann auch wissen, daß das geistige Leben zur Zeit des Mysteriums von Golgatha ein solches war, daß dieses Mysterium gerade so in je­ner Zeit erlebt werden mußte, wie es erlebt worden ist von der Menschheit.",
        "Wir lassen uns keine Dogmen aufdrängen, auch nicht die Dogmen der christlichen Vergangenheit, und wenn uns aufge­drängt werden sollte ein Dogma von der einen oder anderen Seite, dann würden wir es im Sinne des wahrhaft verstandenen Christus­Prinzipes zurückweisen.",
        "Mögen noch so viele Menschen kommen und den geschichtlichen Christus in ein konfessionelles Bekenntnis zwän­gen, oder mögen sie falsch nennen das, was wir als Zukunfts-Christus schauen, wir lassen uns nicht beirren dadurch, wenn uns von ihnen gesagt wird: So oder so muß der Christus sein, - auch wenn es von denen gesagt wird, die verstehen sollten, wer der Christus ist.",
        "Ebenso­wenig darf die Christus-Wesenheit gedrückt und beengt werden aus den orientalischen Traditionen heraus, ebensowenig eine Färbung er­halten durch die Dogmen des orientalischen Dogmatismus.",
        "Frei und unabhängig von jeder Tradition und jeder Autorität will das vor die Menschheit hintreten, was aus den Quellen des Okkultismus heraus gerade über diese Zukunftsevolution zu sagen ist."
      ],
      [
        "Wunderbar erscheint es mir, wie die Menschen sich auf diesem Boden verstehen können.",
        "Immer und immer wieder ist mir in diesen Tagen von den hierher gereisten Nicht-Norden gesagt worden, wie sie sich gegenüber den Persönlichkeiten des skandinavischen Nordens so frei gefühlt haben.",
        "Viele haben das ausgesprochen.",
        "Ein Beweis da­für, wie wir uns, vielleicht noch für manche unbewußt, in dem tief­sten Wesen der Geistes-Erkenntnis verstehen können, wie wir uns namentlich in dem verstehen werden, was ich schon bei dem letzten «Theosophischen Kongreß» in Budapest hervorhob, und was ich wiederholte"
      ],
      [
        "während unserer eigenen Generalversammlung in Berlin, wo wir die große Freude hatten, auch Freunde aus dem Norden bei uns zu sehen.",
        "Schlecht wäre es für die Geisteswissenschaft, wenn derje­nige, der noch nicht in das geistige Gebiet hineinschauen kann, auf blinden Glauben hin annehmen müßte dasjenige, was gesagt wird.",
        "Ich bitte Sie und habe Sie gebeten in Berlin, nichts auf Autorität und Glauben hinzunehmen, was ich jemals gesagt habe oder sagen werde.",
        "Es gibt, auch bevor der Mensch die hellseherische Stufe erreicht, die Möglichkeit, dasjenige zu prüfen, was aus hellseherischer Beobach­tung heraus gewonnen wird.",
        "Was ich je gesagt habe über Zarathustra und Jesus von Nazareth, über Hermes und Moses, über Odin und Thor, über den Christus Jesus selber, ich bitte Sie nicht, es zu glauben und meine Worte auf Autorität hin anzunehmen.",
        "Ich bitte Sie, sich abzugewöhnen das Autoritätsprinzip; denn von Übel würde das Autoritätsprinzip für uns werden."
      ],
      [
        "Ich weiß aber ganz gewiß, wenn Sie anfangen, nachzudenken mit unbefangenem Wahrheitssinn, wenn Sie sagen: Das wird uns gesagt; prüfen wir die uns zugänglichen Urkunden, die Religions- und my­thologischen Dokumente, prüfen wir, was uns sagt jegliche Natur­wissenschaft, - so werden Sie die Richtigkeit des Gesagten einsehen.",
        "Nehmen Sie alles zu Hilfe, und je mehr Sie zu Hilfe nehmen können, desto besser.",
        "Ich bin unbesorgt.",
        "Was aus den Quellen des Rosenkreu­zertums heraus gesagt wird, Sie können es prüfen mit allen Mitteln.",
        "Prüfen Sie mit der materialistischen Kritik an den Evangelien, was ich über den Christus Jesus gesagt habe, prüfen Sie, was ich über Ge­schichte gesagt habe, an allen Quellen, die Ihnen zugänglich sind, prüfen Sie so genau als möglich mit den Mitteln, die Ihnen für den äußerlich-physischen Plan zu Gebote stehen!",
        "Ich bin überzeugt, je genauer Sie prüfen, um so mehr werden Sie das, was aus den Quellen des Rosenkreuzermysteriums heraus gesagt wird, der Wahrheit ent­sprechend finden.",
        "Darauf rechne ich, daß die Mitteilungen, welche aus dem Rosenkreuzertum heraus gemacht werden, nicht geglaubt, sondern geprüft werden, nicht oberflächlich, mit den oberflächlichen Methoden der gegenwärtigen Wissenschaft, sondern immer gewissen­hafter und gewissenhafter.",
        "Nehmen Sie alles, was die neueste Naturwissenschaft"
      ],
      [
        "mit ihren neuesten Methoden Ihnen bieten kann, nehmen Sie alles, was die historischen oder religiösen Forschungen ergeben haben - ich bin unbesorgt.",
        "Je mehr Sie prüfen, desto mehr werden Sie bewahrheitet finden, was aus dieser Quelle heraus gesagt worden ist.",
        "Sie sollen nichts auf die Autorität hin annehmen.",
        "Das sind die besten Schüler der Geist-Erkenntnis, die das, was gesagt wird, zu­nächst als Anregung empfangen und es dann in den Dienst des Le­bens stellen, um es am Leben zu prüfen.",
        "Denn auch im Leben, auf jeder Stufe des Lebens, werden Sie prüfen können das, was aus den Quellen des Rosenkreuzertums heraus gesagt wird.",
        "Fern liegt es der Gesinnung, die dieser Darstellung zugrunde liegt, ein Dogma hinzu­stellen und zu sagen: Dies oder jenes ist so und so und muß geglaubt werden.",
        "Prüfen Sie das an dem, was Ihnen jetzt schon an seelisch markigen und gesunden Menschen entgegentreten kann, und Sie wer­den das selbst bewahrheitet finden, was wie ein prophetischer Hin­weis auf die zukünftige Christus-Offenbarung gesagt worden ist.",
        "Sie brauchen nur die Augen aufzumachen und unbefangen zu prüfen.",
        "Keine Anforderung an den Autoritätsglauben wird gestellt.",
        "Das ist eine Art Grundstimmung, die wie ein roter Faden alles geistige Emp­fangen durchdringen sollte."
      ],
      [
        "Also, ans Herz legen möchte ich Ihnen: Es ist nicht wahrhaft theo­sophisch, etwas als Dogma anzunehmen, weil es dieser oder jener ge­sagt hat; wahrhaft theosophisch ist es, sich anregen zu lassen aus der Geisteswissenschaft und das Empfangene im Leben zu prüfen.",
        "Da wird hinwegschwinden das, was eine wahrhaft theosophische An­schauung von irgendeiner Seite her färben könnte.",
        "Nicht orienta­lische, nicht okzidentalische Nuancen dürfen unsere Anschauungen färben.",
        "Der, welcher im rosenkreuzerischen Sinne spricht, kennt nicht Orientalismus und nicht Okzidentalismus; für ihn sind beide gleich sympathisch.",
        "Er stellt allein aus der inneren Natur der Tatsachen die Wahrheit dar.",
        "Das ist dasjenige, was wir ins Auge fassen müssen, ins­besondere ins Auge fassen müssen in einem so wichtigen Moment, wo wir hingewiesen haben auf den Volksgeist, der waltet in all den nörd­lichen Gebieten.",
        "In ihnen lebt der germanisch-nordisch-mythologi­sche Geist, wenn er auch heute noch unter der Oberfläche lebt, und"
      ],
      [
        "er lebt viel weiter verbreitet in Europa, als man denkt.",
        "Wenn ein nördlicher Völkerstreit entstehen könnte, so könnte er nicht darin bestehen, daß ein Volksteil dem anderen streitig macht dasjenige, was zu geben ist, sondern daß ein jedes Volk Selbsterkenntnis übt und sich frägt: Was ist das Beste, was ich geben kann?"
      ],
      [
        "Dann wird schon auf den gemeinsamen Altar fließen das, was zum Gesamtfortschritt, zur Gesamtwohlfahrt der Menschheit führt.",
        "Die Quellen dessen, was wir bringen können, liegen im Individuellen.",
        "Der germanisch-nordische Erzengel wird der gesamten Menschheitskultur der Zukunft gerade das bringen, wozu er veranlagt ist durch die mitbekommenen Anla­gen, welche wir annahernd charakterisiert haben."
      ],
      [
        "Er ist aber insbe­sondere befähigt, zu bewirken, daß das, was in der ersten Hälfte der fünften nachatlantischen Kulturzeit noch nicht gegeben werden konn­te, sich in der zweiten Hälfte noch abspielen kann, nämlich das, was als geistiges Element, prophetisch keimhaft, in der slawischen Phi­losopie und Volksempfindung gezeigt werden konnte.",
        "Solange sich das im Vorbereitungsstadium befindet, muß die erste Hälfte der fünf­ten nachatlantischen Kulturperiode zurückgelegt werden."
      ],
      [
        "Zunächst konnte da nur erreicht werden eine fein sublimierte geistige Anschau­ung als Philosophie.",
        "Von den Volkskräften muß diese dann erfaßt und durchdrungen werden, damit sie allgemeines Menschheitsgut werden kann, damit sie verständlich werden kann auf den weiten Terrains unseres Erdenlebens."
      ],
      [
        "Versuchen Sie es einmal, ob wir uns auf diesem Gebiete verstehen können; dann wird dieses sonst etwas gefährliche Thema doch nicht böse Früchte getragen haben, wenn wir alles, was hier zusammengekommen ist aus Nord-, Süd- und Ost-, West- und Mitteleuropa, so empfinden, daß es wichtig ist innerhalb der gesamten Menschheit; wenn wir fühlen, daß die großen Völker sowohl als die kleinen Volkssplitter ihre Mission haben und beizu­tragen haben ihren Teil für das Ganze.",
        "Zuweilen haben kleine Volks-splitter, weil sie alte oder neue Seelenmotive bewahren sollen, Aller-wichtigstes beizutragen."
      ],
      [
        "So kann, selbst wenn wir auch diese gefähr­liche Frage zum Gegenstand der Darstellung machen, nichts anderes dabei herauskommen als die Grundempfindung einer Seelengemein­schaft aller derjenigen, die vereinigt sind im Zeichen geisteswissenschaftlichen"
      ],
      [
        "Denkens und Fühlens und der geisteswissenschaftlichen Ideale."
      ],
      [
        "Nur dann, wenn wir noch aus unseren Sympathien und Antipa­thien heraus empfinden würden, wenn wir undeutlich den Kern unserer Weltbewegung erfaßt hätten, könnten Mißverständnisse entstehen aus dem, was gesagt worden ist.",
        "Haben wir aber das er­faßt, was als Geist in diesen Vorträgen waltet, dann können auch die Dinge, die uns da entgegengetreten sind, dazu verhelfen, daß wir den festen Entschluß und das hohe Ideal fassen, dasjenige beizutragen zu dem gemeinsamen Ziele - jeder auf seinem Standpunkte und auf seinem Boden -, was in unserer Mission liegt."
      ],
      [
        "Wir können das am besten mit dem, was aus unserem Selbst, aus dem entspringt, wozu wir veranlagt sind.",
        "Wir dienen der gesamten Menschheit am besten, wenn wir das in uns besonders Veranlagte entwickeln, um es der ge­samten Menschheit einzuverleiben als ein Opfer, das wir dem fort­schreitenden Kulturstrom bringen."
      ],
      [
        "Das müssen wir verstehen lernen.",
        "Verstehen müssen wir lernen, daß es schlimm wäre, wenn die Geistes­wissenschaft nicht beitragen würde zur Entwickelung von Mensch, Engel und Erzengel, sondern beitragen würde zur Überwindung einer Volksgesinnung durch die andere."
      ],
      [
        "Nicht dazu ist die Geisteswissen­schaft da, dazu zu verhelfen, daß sich das, was als religiöses Bekenntnis irgendwo auf der Erde herrscht, ein anderes Gebiet erobern kann.",
        "Würde jemals der Okzident durch den Orient erobert werden oder umgekehrt, so entspräche das durchaus nicht der geisteswissenschaft­lichen Gesinnung."
      ],
      [
        "Allein das entspricht ihr, wenn wir unser Bestes, rein Menschliches für die gesamte Menschheit hingeben.",
        "Und wenn wir ganz in uns selber leben, aber nicht für uns, sondern für alle Menschen, so ist das wahrhafte geisteswissenschaftliche Toleranz."
      ],
      [
        "Das sind Worte, die ich anschließen mußte an unser bedenkliches Thema."
      ],
      [
        "Durch die Geisteswissenschaft - das werden wir immer mehr ein­sehen - wird alle Menschen-Zersplitterung aufhören.",
        "Deshalb ist ge­rade jetzt die richtige Zeit, die Volksseelen kennen zu lernen, weil die Geisteswissenschaft da ist, die uns dazu bringt, die Volksseelen nicht einander gegenüber zu stellen in Opposition, sondern sie auf­zurufen zu harmonischem Zusammenwirken.",
        "Je besser wir das verstehen,"
      ],
      [
        "desto bessere Schüler der Geist-Erkenntnis werden wir sein.",
        "Dahin sollen die Darstellungen, die wir gegeben haben, zunächst aus­klingen.",
        "Ausklingen muß ja doch zuletzt das, was wir an Erkenntnis­sen sammeln, in unserem Empfinden, Fühlen und Denken und in un­serem geisteswissenschaftlichen Ideal.",
        "Je mehr wir dieses leben, desto bessere Schüler der Geisterkenntnis sind wir.",
        "Ich habe erlebt, daß man­che von denen, die mit heraufgezogen sind nach dem Norden, den be­sten Eindruck erhalten haben, was bei ihnen dadurch zum Ausdruck kam, daß sich ihnen das Wort auf die Lippen drängte: «Wie gern ich hier im Norden bin!»"
      ],
      [
        "Und wenn wir mit den Worten des schweigsamen Asen Widar sprechen wollen: Wenn hohe Kräfte in der Menschheit in Zukunft erwacht sein werden, die wir ganz gewiß vor unseren Augen sehen werden, dann wird er der tätige, der aktive Freund des Zusammen-arbeitens, des Zusammen-Fleißigseins sein, in dessen Sinne wir alle zusammengewesen sind.",
        "Lassen Sie uns in diesem Sinne nach einigen Tagen des Beisammenseins wieder räumlich scheiden, uns aber im Geiste in diesem Sinne immer beisammen sein.",
        "Woher wir auch als Schüler der Geist-Erkenntnis kommen, von weit oder nah, mögen wir uns stets in Harmonie zusammenfinden, auch wenn wir uns einmal bei einem Thema fragen, was die Individualitäten dieser oder jener Erdengebiete sind.",
        "Wir wissen, daß das nur einzelne Opferflammen sind, die nicht auseinander züngeln, sondern zusammenschlagen wer­den zu dem gewaltigen Opferfeuer, das zum Wohle der Menschheit zusammenschlagen muß durch die geisteswissenschaftliche Weltan­schauung, die uns so sehr am Herzen liegt und tief in unserer Seele wurzelt."
      ]
    ]
  },
  {
    "order": 13,
    "title_de": "HINWEISE",
    "paragraphs": [
      "Allgemeiner Hinweis: Geisteswissenschaft; geisteswissenschaftlich:",
      "in der Nachichrift steht dafür gewöhnlich «Theosophie», «theosophisch». - Im Vorwort zu Rudolf Steiner «Wendepunkte des Geisteslebens» schreibt Frau Marie Steiner: «Rudolf Steiner versuchte zunächst, das altehrwürdige Wort , das durch den Dilettantismus Unberufener stark kompromittiert war, wieder zu Ehren zu bringen. Anknüpfend an Jakob Böhme und spätere deutsche Denker konnte er dies versuchen. Aber die notwendige Distanzierung von dem, was um die Wende des zwanzigsten Jahrhunderts diesen Namen usurpiert hatte, ließ ihn später für seine okzidentalisch-christliche Strömung den Namen Anthroposophie wählen -, ein zutiefst begründeter Name, da durch Menschenerkenntnis hindurch hier zur Geist- und Welterkenntnis geschritten wird. Meistens brauchte er jedoch das schlichte deutsche Wort",
      "9    So steht z. B. auf S. 3 des ersten Vortrages: In der vorliegenden Ausgabe steht dieser Passus auf Seite 13.",
      "100    . . . meinem Vortragszyklus in Düsseldorf: »Geistige Hierarchien und ihre Wi­derspiegelung in der physischen Welt» (Tierkreis, Planeten, Kosmos). Zehn Vor­träge, gehalten in Düsseldorf vom 12. bis 18. April 1909. Gesamtausgabe Dorn-ach 1960.",
      "112    . . . meinem vorjähri gen Münchener Vürtragszyklus: «Der Orient im Lichte des Okzidents. Die Kinder des Luzifer und die Brüder Christi.» Neun Vorträge, gehalten in München vom 23. bis 29. August 1909. Gesamtausgabe Dornach 1960.",
      "153    . . . meinem letzten Kursus: »Die Offenbarungen des Karma.» Elf Vorträge, ge­halten in Hamburg vom 15. bis 29. Mai 1910. Gesamtausgabe Dornach 1956.",
      "179    . . . daß der Staat . . . auch mit allen Gharaktereigentümlichkeiten der Persön­lichkeit seine Mission erfüllen wird: s. Rudolf Steiner: «Einige Worte über So­lowjew als Zusatz zum vorangehenden Vorwort» zu den «Zwölf Vorlesungen über das Gottmenschentum», in Bd. II der ausgewählten Werke von Wladimir Solowjew, Stuttgart 1921.",
      "185    . . . in dem hier gehaltenen öffentlichen Vortrage von der Wiederoffenharung des Christus: »Das Wiedererscheinen des Christus im Ätherischen». Öffentlicher Vortrag, gehalten in Kristiania (Oslo), am 13. Juni 1910."
    ],
    "sentences": [
      [
        "Allgemeiner Hinweis: Geisteswissenschaft; geisteswissenschaftlich:"
      ],
      [
        "in der Nachichrift steht dafür gewöhnlich «Theosophie», «theosophisch». - Im Vorwort zu Rudolf Steiner «Wendepunkte des Geisteslebens» schreibt Frau Marie Steiner: «Rudolf Steiner versuchte zunächst, das altehrwürdige Wort , das durch den Dilettantismus Unberufener stark kompromittiert war, wieder zu Ehren zu bringen.",
        "Anknüpfend an Jakob Böhme und spätere deutsche Denker konnte er dies versuchen.",
        "Aber die notwendige Distanzierung von dem, was um die Wende des zwanzigsten Jahrhunderts diesen Namen usurpiert hatte, ließ ihn später für seine okzidentalisch-christliche Strömung den Namen Anthroposophie wählen -, ein zutiefst begründeter Name, da durch Menschenerkenntnis hindurch hier zur Geist- und Welterkenntnis geschritten wird.",
        "Meistens brauchte er jedoch das schlichte deutsche Wort"
      ],
      [
        "9 So steht z.",
        "B. auf S. 3 des ersten Vortrages: In der vorliegenden Ausgabe steht dieser Passus auf Seite 13."
      ],
      [
        "100 . . . meinem Vortragszyklus in Düsseldorf: »Geistige Hierarchien und ihre Wi­derspiegelung in der physischen Welt» (Tierkreis, Planeten, Kosmos).",
        "Zehn Vor­träge, gehalten in Düsseldorf vom 12. bis 18.",
        "April 1909.",
        "Gesamtausgabe Dorn-ach 1960."
      ],
      [
        "112 . . . meinem vorjähri gen Münchener Vürtragszyklus: «Der Orient im Lichte des Okzidents.",
        "Die Kinder des Luzifer und die Brüder Christi.» Neun Vorträge, gehalten in München vom 23. bis 29.",
        "August 1909.",
        "Gesamtausgabe Dornach 1960."
      ],
      [
        "153 . . . meinem letzten Kursus: »Die Offenbarungen des Karma.» Elf Vorträge, ge­halten in Hamburg vom 15. bis 29.",
        "Mai 1910.",
        "Gesamtausgabe Dornach 1956."
      ],
      [
        "179 . . . daß der Staat . . . auch mit allen Gharaktereigentümlichkeiten der Persön­lichkeit seine Mission erfüllen wird: s.",
        "Rudolf Steiner: «Einige Worte über So­lowjew als Zusatz zum vorangehenden Vorwort» zu den «Zwölf Vorlesungen über das Gottmenschentum», in Bd.",
        "II der ausgewählten Werke von Wladimir Solowjew, Stuttgart 1921."
      ],
      [
        "185 . . . in dem hier gehaltenen öffentlichen Vortrage von der Wiederoffenharung des Christus: »Das Wiedererscheinen des Christus im Ätherischen».",
        "Öffentlicher Vortrag, gehalten in Kristiania (Oslo), am 13.",
        "Juni 1910."
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
