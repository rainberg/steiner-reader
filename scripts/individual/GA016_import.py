#!/usr/bin/env python3
"""Standalone import script for GA016 — GA016 - Ein Weg zur Selbsterkenntnis des Menschen (1912)"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA016 - Ein Weg zur Selbsterkenntnis des Menschen (1912)"""
GA_NUMBER = "GA016"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "EINLEITENDE BEMERKUNGEN",
    "paragraphs": [
      "Rudolf Steiner",
      "Ein Weg zur Selbsterkenntnis",
      "des Menschen",
      "IN ACHT MEDITATIONEN",
      "der Rudolf Steiner-Nachlassverwaltung",
      "Dornach / Schweiz 1956",
      "In dieser Schrift ist angestrebt, geisteswissenschaftliche Erkenntnisse über die Wesenheit des Menschen zu geben. Die Darstellung ist so gehalten, daß der Leser in das Darge­stellte hineinwachsen mag, so daß es ihm im Verlaufe des Lesens wie zu einer Art Selbstgespräch wird. Gestaltet sich dieses Selbstgespräch so, daß dabei vorher verborgene Kräfte sich offenbaren, welche in jeder Seele erweckt wer­den können, so führt dann das Lesen zu einer wirklichen inneren Seelenarbeit. Und diese kann sich allmählich zur Seelenwanderschaft gedrängt sehen, welche wahrhaftig in das Schauen der geistigen Welt hineinversetzt. Deshalb wurde das Mitgeteilte in der Form von acht Meditationen gegeben, welche wirklich durchgeführt werden können. Geschieht dies, so können sie geeignet sein, der Seele das durch die eigene innere Vertiefung zu übermitteln, wovon in ihnen gesprochen wird.",
      "Angestrebt ist worden, einerseits demjenigen Leser et­was zu geben, der sich bereits mit der Literatur und den Arbeiten auf dem Gebiete des Übersinnlichen, wie es hier gemeint ist, eingehender bekanntgemacht hat. So wird vielleicht hier der Kenner des übersinnlichen Lebens durch die Art des Dargestellten, durch die unmittelbar mit dem Seelen-Erleben zusammenhängende Mitteilung, etwas fin­den, was ihm wichtig erscheinen kann. Und andrerseits kann mancher finden, daß gerade durch diese Darstellung auch dem genützt werden kann, welcher den Ergebnissen der Geisteswissenschaft noch ferne steht.",
      "Zu meinen übrigen Schriften auf geisteswissenschaftli­chem Gebiete soll diese eine Ergänzung und auch Erweiterung",
      "liefern. Doch soll sie auch für sich gelesen werden können.",
      "In meiner «Theosophie» und in meinem «Umriß einer Geheimwissenschaft» ist angestrebt worden, die Dinge so darzustellen, wie sie sich der Beobachtung ergeben, die auf das Geistige geht. Die Darstellung ist in diesen Schriften eine beschreibende, deren Fortgang durch die aus den Din­gen sich offenbarende Gesetzmäßigkeit vorgeschrieben war. - In diesem «Weg zur Selbsterkenntnis des Menschen» ist die Darstellung anders. Es ist in ihr gesagt worden, was eine Seele erleben kann, welche sich auf den Weg zum Gei­ste hin in einer gewissen Weise begibt. Die Schrift kann deshalb angesehen werden als die Wiedergabe von Seelen-erlebnissen. Es muß nur beachtet werden, daß die Erleb­nisse, die in solcher Art, wie sie hier beschrieben sind, ge­macht werden können, bei einer einzelnen Seele, nach ihrer besonderen Eigenart, eine individuelle Form annehmen müssen. Es ist angestrebt worden, dieser Tatsache gerecht zu werden, so daß man sich auch vorstellen kann, das Ge­schilderte sei so, wie es dargestellt ist, von einer bestimm­ten Seele genau durchlebt worden. (Der Titel heißt des­halb: «Ein Weg zur Selbsterkenntnis.») Eben deshalb kann die Schrift dazu dienen, daß sich auch andre Seelen in dies Geschilderte hineinieben und zu entsprechenden Zielen gelangen. So ist diese Schrift auch eine Ergänzung und Erweiterung dessen, was sich in meinem Buche «Wie erlangt man Erkenntnisse der höheren Welten?» findet.",
      "Dargestellt sind nur einzelne geisteswissenschaftliche Grunderlebnisse. Auf die Mitteilung weiterer Gebiete der «Geisteswissenschaft» in dieser Art ist vorläufig verzichtet.",
      "München, im August 1912                        Rudolf Steiner"
    ],
    "sentences": [
      [
        "Rudolf Steiner"
      ],
      [
        "Ein Weg zur Selbsterkenntnis"
      ],
      [
        "des Menschen"
      ],
      [
        "IN ACHT MEDITATIONEN"
      ],
      [
        "der Rudolf Steiner-Nachlassverwaltung"
      ],
      [
        "Dornach / Schweiz 1956"
      ],
      [
        "In dieser Schrift ist angestrebt, geisteswissenschaftliche Erkenntnisse über die Wesenheit des Menschen zu geben.",
        "Die Darstellung ist so gehalten, daß der Leser in das Darge­stellte hineinwachsen mag, so daß es ihm im Verlaufe des Lesens wie zu einer Art Selbstgespräch wird.",
        "Gestaltet sich dieses Selbstgespräch so, daß dabei vorher verborgene Kräfte sich offenbaren, welche in jeder Seele erweckt wer­den können, so führt dann das Lesen zu einer wirklichen inneren Seelenarbeit.",
        "Und diese kann sich allmählich zur Seelenwanderschaft gedrängt sehen, welche wahrhaftig in das Schauen der geistigen Welt hineinversetzt.",
        "Deshalb wurde das Mitgeteilte in der Form von acht Meditationen gegeben, welche wirklich durchgeführt werden können.",
        "Geschieht dies, so können sie geeignet sein, der Seele das durch die eigene innere Vertiefung zu übermitteln, wovon in ihnen gesprochen wird."
      ],
      [
        "Angestrebt ist worden, einerseits demjenigen Leser et­was zu geben, der sich bereits mit der Literatur und den Arbeiten auf dem Gebiete des Übersinnlichen, wie es hier gemeint ist, eingehender bekanntgemacht hat.",
        "So wird vielleicht hier der Kenner des übersinnlichen Lebens durch die Art des Dargestellten, durch die unmittelbar mit dem Seelen-Erleben zusammenhängende Mitteilung, etwas fin­den, was ihm wichtig erscheinen kann.",
        "Und andrerseits kann mancher finden, daß gerade durch diese Darstellung auch dem genützt werden kann, welcher den Ergebnissen der Geisteswissenschaft noch ferne steht."
      ],
      [
        "Zu meinen übrigen Schriften auf geisteswissenschaftli­chem Gebiete soll diese eine Ergänzung und auch Erweiterung"
      ],
      [
        "liefern.",
        "Doch soll sie auch für sich gelesen werden können."
      ],
      [
        "In meiner «Theosophie» und in meinem «Umriß einer Geheimwissenschaft» ist angestrebt worden, die Dinge so darzustellen, wie sie sich der Beobachtung ergeben, die auf das Geistige geht.",
        "Die Darstellung ist in diesen Schriften eine beschreibende, deren Fortgang durch die aus den Din­gen sich offenbarende Gesetzmäßigkeit vorgeschrieben war. - In diesem «Weg zur Selbsterkenntnis des Menschen» ist die Darstellung anders.",
        "Es ist in ihr gesagt worden, was eine Seele erleben kann, welche sich auf den Weg zum Gei­ste hin in einer gewissen Weise begibt.",
        "Die Schrift kann deshalb angesehen werden als die Wiedergabe von Seelen-erlebnissen.",
        "Es muß nur beachtet werden, daß die Erleb­nisse, die in solcher Art, wie sie hier beschrieben sind, ge­macht werden können, bei einer einzelnen Seele, nach ihrer besonderen Eigenart, eine individuelle Form annehmen müssen.",
        "Es ist angestrebt worden, dieser Tatsache gerecht zu werden, so daß man sich auch vorstellen kann, das Ge­schilderte sei so, wie es dargestellt ist, von einer bestimm­ten Seele genau durchlebt worden. (Der Titel heißt des­halb: «Ein Weg zur Selbsterkenntnis.») Eben deshalb kann die Schrift dazu dienen, daß sich auch andre Seelen in dies Geschilderte hineinieben und zu entsprechenden Zielen gelangen.",
        "So ist diese Schrift auch eine Ergänzung und Erweiterung dessen, was sich in meinem Buche «Wie erlangt man Erkenntnisse der höheren Welten?» findet."
      ],
      [
        "Dargestellt sind nur einzelne geisteswissenschaftliche Grunderlebnisse.",
        "Auf die Mitteilung weiterer Gebiete der «Geisteswissenschaft» in dieser Art ist vorläufig verzichtet."
      ],
      [
        "München, im August 1912 Rudolf Steiner"
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "ERSTE MEDITATION",
    "paragraphs": [
      "ERSTE MEDITATION",
      "Der Meditierende versucht eine wahre Vorstellung",
      "von dein physischen Leibe zu gewinnen",
      "Wenn die Seele durch die Sinne und durch ihr Vorstellen an die Erscheinungen der Außenwelt hingegeben ist, dann kann sie bei wirklicher Selbstbesinnung nicht sagen, sie nehme diese Erscheinungen wahr, oder sie erlebe die Din­ge der Außenwelt. Denn sie weiß in Wahrheit in der Zeit ihrer Hingabe an die Außenwelt nichts von sich.",
      "Das Son­nenlicht, das von den Dingen in vielartiger Farbenerschei­nung sich im Raume ausbreitet, das erlebt sich eigentlich in der Seele. Freut sich die Seele über irgendeinen Vorgang, so ist sie in dem Zeitpunkte des Freuens selbst Freude, so­weit sie von der Sache weiß.",
      "Die Freude erlebt sich in ihr. Die Seele ist eins mit ihrem Erleben von der Welt; sie er­lebt sich nicht als etwas, das sich freut, das bewundert, das sich ergötzt oder fürchtet. Sie ist Freude, Bewunderung, Ergötzen, Furcht.",
      "Wenn sich die Seele dies immer gestehen wollte, dann erschienen ihr die Zeiten, in welchen sie von dem Erleben an der Außenwelt zurücktritt und sich selbst betrachtet, erst in dem rechten Lichte. Sie erschienen als ein Leben von ganz besondrer Art, die zunächst ganz un­vergleichlich ist mit dem gewöhnlichen Seelenleben.",
      "Mit dieser besondren Art des Lebens beginnen die Rätsel des seelischen Daseins im Bewußtsein aufzutauchen. Und diese Rätsel sind im Grunde die Quelle aller andern Weltenrätsel. - Außenwelt und Innenwelt stellen sich vor den Men­schengeist, wenn die Seele für kürzere oder längere Zeit aufhört mit der Außenwelt eins zu sein und sich in die Ein­samkeit des Eigenseins zurückzieht.",
      "Dieses Zurückziehen ist kein einfacher Vorgang, der einmal sich vollzieht und dann etwa in derselben Art wie­derholt werden könnte. Es ist vielmehr der Beginn einer Wanderung in vorher unbekannte Welten. Hat man die Wanderung begonnen, dann wird jeder Schritt, den man gemacht hat, die Veranlassung zu weiteren. Und er ist auch die Vorbereitung zu diesen weiteren. Er macht die Seele für die folgenden erst fähig. Und mit jedem Schritte er­fährt man mehr über die Antwort auf die Frage: Was ist der Mensch im wahren Sinne des Wortes? Welten eröffnen sich, die vor der gewöhnlichen Lebensbetrachtung verbor­gen sind. Und doch liegt in ihnen allein dasjenige, was auch über diese Lebensbetrachtung die Wahrheit offenba­ren kann. - Wenn auch keine Antwort eine umfassende, endgültige ist, so sind die Antworten, welche durch innere Seelenwanderschaft errungen werden, doch solche, die über alles hinausgehen, was die äußeren Sinne und der an sie gebundene Verstand geben können. Und dieses andre hat der Mensch nötig. Er bemerkt, daß dies so ist, wenn er sich wahrhaftig auf sich selbst besinnt.",
      "Zunächst sind zu dieser Wanderschaft nüchterne, trok­kene Überlegungen notwendig. Sie geben den sicheren Ausgangspunkt für das weitere Vordringen in die über­sinnlichen Gebiete, um die es zuletzt der Seele zu tun ist. Manche Seele möchte sich diesen Ausgangspunkt ersparen und sogleich in das Übersinnliche eindringen. Eine ge­sunde Seele wird, selbst wenn sie durch Abneigung gegen eine solche Überlegung diese erst vermieden hat, später doch sich derselben hingeben. Denn wieviel man auch über das Übersinnliche von einem andern Ausgangspunkte her erfahren hat, sichern Boden unter sich gewinnt man",
      "nur durch Überlegungen von der Art, wie die hier zunächst folgende ist.",
      "Es können im Leben der Seele die Augenblicke kom­men, in denen sie zu sich selber so spricht: Du mußt dich allem entziehen können, was dir eine Außenwelt geben kann, wenn du dir nicht ein Geständnis abpressen lassen willst, mit dem sich nicht leben läßt, nämlich du seiest nur der sich selbst erlebende Widersinn. - Was du da draußen wahrnimmst, es ist da ohne dich; es war ohne dich und wird ohne dich sein. Warum empfinden sich die Farben in dir, da dein Empfinden für sie doch bedeutungslos sein könnte?",
      "Warum bilden die Stoffe und Kräfte der Außen­welt deinen Leib? Er belebt sich zu deiner äußeren Er­scheinung. Die Außenwelt gestaltet sich zu dir. Du wirst gewahr, daß du diesen Leib brauchst. Weil du ohne deine Sinne, welche nur Er dir einbilden kann, zunächst gar nicht etwas in dir erleben könntest.",
      "Du wärest, so wie du vorerst bist, leer ohne deinen Leib. Er gibt dir innere Fülle und Inhalt. - Und dann können alle die Überlegungen auf­treten, ohne welche ein menschliches Dasein nicht bleiben kann, wenn es nicht in gewissen Zeiten, die für jeden Men­schen kommen, mit sich in einen unerträglichen Wider­spruch geraten will.",
      "Dieser Leib - er lebt so, daß er jetzt Ausdruck ist des seelischen Erlebens. Seine Vorgänge sind von der Art, daß die Seele durch ihn lebt und sich in ihm erlebt. Das wird einmal nicht so sein. Was in dem Leibe lebt, wird einmal ganz anderen Gesetzen unterworfen sein als jetzt, da es für mich verläuft, für mein seelisches Erle­ben.",
      "Es wird den Gesetzen unterworfen sein, nach denen Stoffe und Kräfte draußen in der Natur sich verhalten, Ge­setzen, die nichts mehr mit mir und meinem Leben zu tun",
      "haben. Der Leib, dem ich mein seelisches Erleben verdan­ke, wird in den allgemeinen Weltverlauf aufgenommen sein und sich in demselben so verhalten, daß er mit allem, was ich in mir erlebe, nichts mehr gemeinsam haben wird.",
      "Eine solche Überlegung kann alle Schauer des Todesge­dankens vor das innere Erleben bringen, ohne daß sich in diesen Eindruck die bloß persönlichen Empfindungen mi­schen, welche in der Seele gewöhnlich mit diesem Gedan­ken verbunden sind. Solche Empfindungen bewirken, daß ihm gegenüber die ruhige, gelassene Stimmung nicht leicht sich einstellt, die zur erkennenden Betrachtung notwendig ist. - Es ist nur zu begreiflich, daß der Mensch ein Wissen gewinnen will über den Tod und über ein Leben der Seele unabhängig von der Auflösung des Leibes.",
      "Die Art, wie er zu den Fragen steht, die hier in Betracht kommen, ist, wie kaum irgend etwas andres in der Welt, geeignet, den sach­lichen Blick zu trüben und Antworten als gültig hinzuneh­men, welche vom Wunsche eingegeben sind. Man kann aber über nichts eine wahre Erkenntnis auf geistigem Ge­biete erhalten, bei dem man nicht wie ein völlig Unbetei­ligter das «Nein» ebenso willig hinnimmt wie das «Ja».",
      "Und man wird nur gewissenhaft in sich selbst zu blicken brauchen, um sich völlig klar darüber zu sein, daß man nicht mit demselben Gleichmut die Erkenntnis hinnehmen würde, mit dem Tode des Leibes erlischt auch das seelische Leben, wie die andre, die von dem Fortbestand der Seele nach dem Tode spricht. Gewiß, es gibt Menschen, die völ­lig ehrlich an die Vernichtung der Seele mit der Auflösung des Leibeslebens glauben, und die mit einem solchen Ge­danken sich ihr Leben einrichten.",
      "Doch auch für diese gilt, daß sie mit ihren Gefühlen keineswegs unbefangen diesem",
      "Gedanken gegenüberstehen. Sie lassen sich durch die Schrecken der Vernichtung allerdings nicht dazu hinreißen, die Gründe der Erkenntnis, welche für sie deutlich sprechen, von dem Wunsche übertönt zu fühlen, der nach einem Fortleben zielt.",
      "Insoferne sind die Vorstellungen solcher Menschen oft sachlicher als diejenigen der andern, welche, ohne dies zu wissen, sich Gründe für das Fortleben vorspiegeln oder vorspiegeln lassen, weil in ihren gehei­men Seelengründen eben die Begierde nach solchem Fort­leben brennt. Doch ist bei den Unsterblichkeitsleugnern die Befangenheit eine nicht weniger große.",
      "Sie ist nur anders geartet. Es gibt unter ihnen solche, welche sich eine ge­wisse Vorstellung von dem machen, was Leben und Da­sein heißt. Diese Vorstellung führt sie dazu, bestimmte Bedingungen denken zu müssen, unter denen dieses Leben nur allein möglich ist.",
      "So wie sie nun das Dasein ansehen, ergibt sich ihnen, daß die Bedingungen des seelischen Le­bens nicht mehr vorhanden sein können, wenn der Leib wegfällt. Solche Menschen bemerken nicht, daß sie sich erst eine bestimmte Vorstellung gebildet haben, wie Leben nur sein könne, und daß sie allein deshalb nicht glauben können, es dauere nach dem Tode fort, weil sich aus ihrer Vorstellung heraus keine Möglichkeit ergibt, sich ein leibfreies Dasein zu denken.",
      "Sie sind zwar nicht durch ihre Wünsche, wohl aber durch die Vorstellungen befangen, von denen sie nun eben nicht loskommen können. Es gibt noch viele Befangenheiten auf diesem Gebiete. Man kann immer nur einzelne Beispiele dessen anführen, was in die­ser Art alles vorhanden ist.",
      "Der Gedanke, daß der Leib, in dessen Vorgängen sich die Seele auslebt, einmal der Außenwelt verfallen werde",
      "und Gesetzen folgen, die in keinem Verhältnisse stehen zum inneren Erleben, er läßt das Todeserlebnis so vor die Seele treten, daß kein Wunsch, kein persönliches Interesse sich in die Betrachtung einzumischen brauchen; daß dieses Erlebnis zu einer reinen, unpersönlichen Erkenntnisfrage führen kann. Es wird sich aber dann auch bald die Empfin­dung ergeben, daß der Todesgedanke nicht um seiner selbst willen bedeutsam ist, sondern deshalb, weil er Licht verbreiten kann über das Leben. Man wird zu der Ansicht kommen müssen, daß das Rätsel des Lebens zu erkennen ist durch das Wesen des Todes.",
      "Daß die Seele nach ihrer Fortdauer verlangt, sollte unter allen Umständen dazu führen, sie mißtrauisch zu machen gegen alle Meinungen, welche sie sich über diese Fortdauer bildet. Denn warum sollten sich die Tatsachen der Welt kümmern um das, was die Seele empfindet. Sie mag nach ihren Bedürfnissen sich selber sinnlos fühlen, wenn sie denken müßte, sie könnte, einer Flamme gleich, die aus dem Brennmaterial sich ergibt, aus dem Stoffe ihres Leibes aufflackern und dann wieder verlöschen. Es könnte sich dies doch so verhalten, auch wenn es als sinnlos empfun­den würde. - Wenn die Seele den Blick zum Leibe wendet, so soll sie auch nur mit dem rechnen, was er ihr zeigen kann. Es scheint da, als ob in der Natur die Gesetze wirk­ten, welche die Stoffe und Kräfte in ein Wechselspiel brin­gen, und als ob diese Gesetze den Leib beherrschten, und ihn nach einiger Zeit wieder in das allgemeine Wechsel­spiel einbezögen.",
      "Man mag diesen Gedanken nun wenden, wie man will:",
      "er ist naturwissenschaftlich wohl brauchbar, doch er er­weist sich der wahren Wirklichkeit gegenüber als ganz unmöglich.",
      "Man kann finden, daß er allein wissenschaftlich klar, nüchtern, und alles andre nur subjektiver Glaube sei; man kann sich dies wohi einbilden. Man kann es aber bei wirklicher Unbefangenheit nicht festhalten.",
      "Und darauf kommt es an. Nicht was die Seele durch ihr Wesen als not­wendig empfindet, kommt in Betracht, sondern dasjenige, was die Außenwelt offenbart, welcher der Leib entnom­men ist. Diese Außenwelt nimmt seine Stoffe und Kräfte nach dem Tode in sich au£ In ihr folgen sie dann Gesetzen, welchen ganz gleichgültig ist, was im menschlichen Leibe während des Lebens vorgeht.",
      "Diese Gesetze (die physi­scher und chemischer Art sind) stellen sich zu dem Leibe nicht anders als zu jedem andern leblosen Dinge der Au­ßenwelt. Es ist unmöglich, etwas anderes zu denken, als daß dieses gleichgültige Verhältnis der Außenwelt zum Menschenleibe nicht erst mit dem Tode eintritt, sondern daß es auch schon während des Lebens besteht.",
      "Nicht aus dem Leben kann man eine Vorstellung gewinnen über den Anteil der sinnlichen Außenwelt an dem Menschenleibe, sondern allein dadurch, daß man denkt: alles, was da an dir ist als Träger deiner Sinne, als Vermittler von Vorgän­gen, durch welche deine Seele lebt, das wird von der Welt, welche du wahrnimmst, so behandelt, wie dir die Vorstel­lung ergibt, die über dein Leben hinaus schweift. Die damit rechnet, daß eine Zeit kommen werde, in der du alles die­ses nicht mehr an dir hast, worinnen du dich jetzt erlebst.",
      "Jede andere Vorstellung über das Verhältnis der sinnlichen Außenwelt zum Leibe läßt durch sich selber erfühlen, daß sie gegenüber der Wirklichkeit nicht haltbar ist. Die Vor­stellung aber, daß erst nach dem Tode der wirkliche Anteil der Außenwelt an dem Leibe zutage tritt, kommt mit",
      "nichts in Konflikt, was wahrhaft in Außenwelt und Innen­welt erlebt wird. Die Seele fühlt nichts Unerträgliches bei dem Gedanken, daß ihre Stoffe und Kräfte Vorgängen der Außenwelt verfallen, die mit ihrem eigenen Leben nichts zu tun haben. Sie kann in ihren Tiefen bei vollkommen unbefangener Hingabe an das Leben keinen aus dem Leibe aufsteigenden Wunsch entdecken, der ihr den Gedanken unbehaglich machte an die Auflösung nach dem Tode. Das Unerträgliche tritt erst dann ein, wenn die Vorstellung gebildet werden sollte, die in die Außenwelt zurückkeh­renden Stoffe und Kräfte nehmen die sich erlebende Seele mit. Eine solche Vorstellung wäre aus demselben Grunde unerträglich wie jede andre, die sich nicht naturgemäß aus der Hingabe an die Offenbarung der Außenwelt ergibt.",
      "Der Außenwelt während des Lebens einen ganz andren Anteil an dem Leibesdasein zuzuerkennen als nach dem Tode, ist ein Gedanke, der aus dem Nichts hergeholt wer­den müßte. Als sinnloser Gedanke muß er stets vor der Wirklichkeit zurückprallen, während doch die Vorstellung ganz gesund ist, daß die Außenwelt während des Lebens ganz den gleichen Anteil an dem Leibe hat wie nach dem Tode. Die Seele fühlt sich, wenn sie den letztern Gedan­ken hegt, ganz im Einklange mit der Offenbarung der Tat­sachen. Sie kann empfinden, daß sie durch diese Vorstel­lung nicht in Mißklang kommt mit den Tatsachen, die durch sich selbst sprechen, und denen kein künstlicher Ge­danke hinzugefügt werden darf.",
      "Man achtet nicht immer darauf, in wie schönem Ein­klange das natürliche, gesunde Empfinden der Seele mit der Naturoffenbarung ist. Es könnte dies so selbstver­ständlich erscheinen, daß es gar keiner Beachtung wert",
      "wäre; und doch ist dies scheinbar Bedeutungslose licht­bringend. Nichts Unerträgliches hat der Gedanke, daß der Leib in die Elemente aufgelöst werde; etwas Sinnloses da­gegen der andre, daß dies auch mit der Seele geschehe. Es gibt viele menschlich persönliche Gründe, welche dies als sinnlos erscheinen lassen; diese müssen von der objektiven Betrachtung unberücksichtigt gelassen werden. Die ganz unpersönliche Hingabe jedoch an das, was die Außenwelt lehrt, zeigt, daß auch während des Lebens dieser Außen­welt an der Seele kein andrer Anteil zugeschrieben werden kann als nach dem Tode. Maßgebend ist, daß dieser Ge­danke sich als ein notwendiger ergibt, und daß er stand­hält gegenüber allen Einwänden, die man gegen ihn erhe­ben kann. Wer ihn ganz bewußt denkt, der fühlt dieses als unmittelbare Gewißheit. In Wahrheit denken so aber sowohl Unsterblichkeitsgläubige wie Unsterblichkeitsleug­ner. Die letztern werden wohl sagen, in den Gesetzen, wel­che wirksam sind am Leibe nach dem Tode, seien auch die Bedingungen seiner Vorgänge während des Lebens ent­halten; aber sie irren sich, wenn sie glauben, sich wirklich vorstellen zu können, diese Gesetze stünden während des Lebens in einem andern Verhältnisse zum Leibe als Seelen-träger als nach dem Tode.",
      "In sich möglich ist nur die Vorstellung, auch jener be­sondre Zusammenhang von Kräften, der mit dem Leibe in die Erscheinung tritt, stehe dem Leibe als Seelenträger ge­nau so anteilslos gegenüber wie derjenige, welcher die Vor­gänge am toten Leibe bewirkt. Nicht für die Seele ist diese Anteilslosigkeit vorhanden, wohl aber für die Stoffe und Kräfte des Leibes. Die Seele erlebt sich am Leibe; der Leib jedoch lebt mit der Außenwelt, in ihr, durch sie und läßt das",
      "Seelische für sich nicht anders maßgebend sein als die Vor­gänge der Außenwelt. Man muß zu der Ansicht kommen, daß für die Blutbewegung im Leibe die Wärme und Kälte der Außenwelt so maßgebend sind, wie die Furcht oder das Schamgefühl, die sich in der Seele abspielen.",
      "So fühlt man zunächst in sich die Gesetze der Außen­welt in jenem ganz besondren Zusammenhange wirksam, der sich als die Gestaltung des Menschenleibes kundgibt. Man empfindet diesen Leib als ein Glied der Außenwelt. Aber man steht seinem innern Zusammenhang fremd ge­genüber. Die äußere Wissenschaft klärt gegenwärtig zum Teil auf, wie sich die Gesetze der Außenwelt in dem ganz besondren Wesen zusammenfügen, das sich als Menschenleib darstellt. Von der Zukunft darf gehofft werden, daß diese Erkenntnis immer weiter fortschreiten werde. Wie die Seele über ihr Verhältnis zum Leibe denken muß, daran kann diese fortschreitende Erkenntnis nicht das geringste ändern. Im Gegenteil, sie wird immer klarer zeigen müs­sen, daß die Gesetze der Außenwelt vor und nach dem Tode in dem gleichen Verhältnisse zur Seele stehen. Es ist eine Illusion, zu erwarten, mit fortschreitender Naturer­kenntnis werde aus den Gesetzen der Außenwelt sich er­geben, inwieferne die Leibesvorgänge die Vermittler des Seelenlebens sind. Man wird immer deutlicher erkennen, was im Leibe während des Lebens vorgeht; aber die ent­sprechenden Vorgänge werden sich stets als solche zeigen, welche die Seele als ihr äußerlich so empfindet, wie die Vorgänge am Leibe nach dem Tode.",
      "Innerhalb der Außenwelt muß daher der Leib als ein Zu­sammenhang von Kräften und Stoffen erscheinen, der für sich besteht und in sich erklärbar ist als Glied dieser Außenwelt. -",
      "Die Natur läßt die Pflanze entstehen; sie löst sie wieder auf. Sie beherrscht den Menschenleib und läßt ihn innerhalb ihrer Wesenheit vergehen. Stellt sich der Mensch mit einer solchen Betrachtung der Natur gegenüber, so kann er sich und alles, was in ihm ist, vergessen, und sei­nen Leib als Glied der Außenwelt an sich empfinden. Denkt er so über sein Verhältnis zu sich und zur Natur, so erlebt er an sich, was man seinen physischen Leib nennen kann."
    ],
    "sentences": [
      [
        "ERSTE MEDITATION"
      ],
      [
        "Der Meditierende versucht eine wahre Vorstellung"
      ],
      [
        "von dein physischen Leibe zu gewinnen"
      ],
      [
        "Wenn die Seele durch die Sinne und durch ihr Vorstellen an die Erscheinungen der Außenwelt hingegeben ist, dann kann sie bei wirklicher Selbstbesinnung nicht sagen, sie nehme diese Erscheinungen wahr, oder sie erlebe die Din­ge der Außenwelt.",
        "Denn sie weiß in Wahrheit in der Zeit ihrer Hingabe an die Außenwelt nichts von sich."
      ],
      [
        "Das Son­nenlicht, das von den Dingen in vielartiger Farbenerschei­nung sich im Raume ausbreitet, das erlebt sich eigentlich in der Seele.",
        "Freut sich die Seele über irgendeinen Vorgang, so ist sie in dem Zeitpunkte des Freuens selbst Freude, so­weit sie von der Sache weiß."
      ],
      [
        "Die Freude erlebt sich in ihr.",
        "Die Seele ist eins mit ihrem Erleben von der Welt; sie er­lebt sich nicht als etwas, das sich freut, das bewundert, das sich ergötzt oder fürchtet.",
        "Sie ist Freude, Bewunderung, Ergötzen, Furcht."
      ],
      [
        "Wenn sich die Seele dies immer gestehen wollte, dann erschienen ihr die Zeiten, in welchen sie von dem Erleben an der Außenwelt zurücktritt und sich selbst betrachtet, erst in dem rechten Lichte.",
        "Sie erschienen als ein Leben von ganz besondrer Art, die zunächst ganz un­vergleichlich ist mit dem gewöhnlichen Seelenleben."
      ],
      [
        "Mit dieser besondren Art des Lebens beginnen die Rätsel des seelischen Daseins im Bewußtsein aufzutauchen.",
        "Und diese Rätsel sind im Grunde die Quelle aller andern Weltenrätsel. - Außenwelt und Innenwelt stellen sich vor den Men­schengeist, wenn die Seele für kürzere oder längere Zeit aufhört mit der Außenwelt eins zu sein und sich in die Ein­samkeit des Eigenseins zurückzieht."
      ],
      [
        "Dieses Zurückziehen ist kein einfacher Vorgang, der einmal sich vollzieht und dann etwa in derselben Art wie­derholt werden könnte.",
        "Es ist vielmehr der Beginn einer Wanderung in vorher unbekannte Welten.",
        "Hat man die Wanderung begonnen, dann wird jeder Schritt, den man gemacht hat, die Veranlassung zu weiteren.",
        "Und er ist auch die Vorbereitung zu diesen weiteren.",
        "Er macht die Seele für die folgenden erst fähig.",
        "Und mit jedem Schritte er­fährt man mehr über die Antwort auf die Frage: Was ist der Mensch im wahren Sinne des Wortes?",
        "Welten eröffnen sich, die vor der gewöhnlichen Lebensbetrachtung verbor­gen sind.",
        "Und doch liegt in ihnen allein dasjenige, was auch über diese Lebensbetrachtung die Wahrheit offenba­ren kann. - Wenn auch keine Antwort eine umfassende, endgültige ist, so sind die Antworten, welche durch innere Seelenwanderschaft errungen werden, doch solche, die über alles hinausgehen, was die äußeren Sinne und der an sie gebundene Verstand geben können.",
        "Und dieses andre hat der Mensch nötig.",
        "Er bemerkt, daß dies so ist, wenn er sich wahrhaftig auf sich selbst besinnt."
      ],
      [
        "Zunächst sind zu dieser Wanderschaft nüchterne, trok­kene Überlegungen notwendig.",
        "Sie geben den sicheren Ausgangspunkt für das weitere Vordringen in die über­sinnlichen Gebiete, um die es zuletzt der Seele zu tun ist.",
        "Manche Seele möchte sich diesen Ausgangspunkt ersparen und sogleich in das Übersinnliche eindringen.",
        "Eine ge­sunde Seele wird, selbst wenn sie durch Abneigung gegen eine solche Überlegung diese erst vermieden hat, später doch sich derselben hingeben.",
        "Denn wieviel man auch über das Übersinnliche von einem andern Ausgangspunkte her erfahren hat, sichern Boden unter sich gewinnt man"
      ],
      [
        "nur durch Überlegungen von der Art, wie die hier zunächst folgende ist."
      ],
      [
        "Es können im Leben der Seele die Augenblicke kom­men, in denen sie zu sich selber so spricht: Du mußt dich allem entziehen können, was dir eine Außenwelt geben kann, wenn du dir nicht ein Geständnis abpressen lassen willst, mit dem sich nicht leben läßt, nämlich du seiest nur der sich selbst erlebende Widersinn. - Was du da draußen wahrnimmst, es ist da ohne dich; es war ohne dich und wird ohne dich sein.",
        "Warum empfinden sich die Farben in dir, da dein Empfinden für sie doch bedeutungslos sein könnte?"
      ],
      [
        "Warum bilden die Stoffe und Kräfte der Außen­welt deinen Leib?",
        "Er belebt sich zu deiner äußeren Er­scheinung.",
        "Die Außenwelt gestaltet sich zu dir.",
        "Du wirst gewahr, daß du diesen Leib brauchst.",
        "Weil du ohne deine Sinne, welche nur Er dir einbilden kann, zunächst gar nicht etwas in dir erleben könntest."
      ],
      [
        "Du wärest, so wie du vorerst bist, leer ohne deinen Leib.",
        "Er gibt dir innere Fülle und Inhalt. - Und dann können alle die Überlegungen auf­treten, ohne welche ein menschliches Dasein nicht bleiben kann, wenn es nicht in gewissen Zeiten, die für jeden Men­schen kommen, mit sich in einen unerträglichen Wider­spruch geraten will."
      ],
      [
        "Dieser Leib - er lebt so, daß er jetzt Ausdruck ist des seelischen Erlebens.",
        "Seine Vorgänge sind von der Art, daß die Seele durch ihn lebt und sich in ihm erlebt.",
        "Das wird einmal nicht so sein.",
        "Was in dem Leibe lebt, wird einmal ganz anderen Gesetzen unterworfen sein als jetzt, da es für mich verläuft, für mein seelisches Erle­ben."
      ],
      [
        "Es wird den Gesetzen unterworfen sein, nach denen Stoffe und Kräfte draußen in der Natur sich verhalten, Ge­setzen, die nichts mehr mit mir und meinem Leben zu tun"
      ],
      [
        "haben.",
        "Der Leib, dem ich mein seelisches Erleben verdan­ke, wird in den allgemeinen Weltverlauf aufgenommen sein und sich in demselben so verhalten, daß er mit allem, was ich in mir erlebe, nichts mehr gemeinsam haben wird."
      ],
      [
        "Eine solche Überlegung kann alle Schauer des Todesge­dankens vor das innere Erleben bringen, ohne daß sich in diesen Eindruck die bloß persönlichen Empfindungen mi­schen, welche in der Seele gewöhnlich mit diesem Gedan­ken verbunden sind.",
        "Solche Empfindungen bewirken, daß ihm gegenüber die ruhige, gelassene Stimmung nicht leicht sich einstellt, die zur erkennenden Betrachtung notwendig ist. - Es ist nur zu begreiflich, daß der Mensch ein Wissen gewinnen will über den Tod und über ein Leben der Seele unabhängig von der Auflösung des Leibes."
      ],
      [
        "Die Art, wie er zu den Fragen steht, die hier in Betracht kommen, ist, wie kaum irgend etwas andres in der Welt, geeignet, den sach­lichen Blick zu trüben und Antworten als gültig hinzuneh­men, welche vom Wunsche eingegeben sind.",
        "Man kann aber über nichts eine wahre Erkenntnis auf geistigem Ge­biete erhalten, bei dem man nicht wie ein völlig Unbetei­ligter das «Nein» ebenso willig hinnimmt wie das «Ja»."
      ],
      [
        "Und man wird nur gewissenhaft in sich selbst zu blicken brauchen, um sich völlig klar darüber zu sein, daß man nicht mit demselben Gleichmut die Erkenntnis hinnehmen würde, mit dem Tode des Leibes erlischt auch das seelische Leben, wie die andre, die von dem Fortbestand der Seele nach dem Tode spricht.",
        "Gewiß, es gibt Menschen, die völ­lig ehrlich an die Vernichtung der Seele mit der Auflösung des Leibeslebens glauben, und die mit einem solchen Ge­danken sich ihr Leben einrichten."
      ],
      [
        "Doch auch für diese gilt, daß sie mit ihren Gefühlen keineswegs unbefangen diesem"
      ],
      [
        "Gedanken gegenüberstehen.",
        "Sie lassen sich durch die Schrecken der Vernichtung allerdings nicht dazu hinreißen, die Gründe der Erkenntnis, welche für sie deutlich sprechen, von dem Wunsche übertönt zu fühlen, der nach einem Fortleben zielt."
      ],
      [
        "Insoferne sind die Vorstellungen solcher Menschen oft sachlicher als diejenigen der andern, welche, ohne dies zu wissen, sich Gründe für das Fortleben vorspiegeln oder vorspiegeln lassen, weil in ihren gehei­men Seelengründen eben die Begierde nach solchem Fort­leben brennt.",
        "Doch ist bei den Unsterblichkeitsleugnern die Befangenheit eine nicht weniger große."
      ],
      [
        "Sie ist nur anders geartet.",
        "Es gibt unter ihnen solche, welche sich eine ge­wisse Vorstellung von dem machen, was Leben und Da­sein heißt.",
        "Diese Vorstellung führt sie dazu, bestimmte Bedingungen denken zu müssen, unter denen dieses Leben nur allein möglich ist."
      ],
      [
        "So wie sie nun das Dasein ansehen, ergibt sich ihnen, daß die Bedingungen des seelischen Le­bens nicht mehr vorhanden sein können, wenn der Leib wegfällt.",
        "Solche Menschen bemerken nicht, daß sie sich erst eine bestimmte Vorstellung gebildet haben, wie Leben nur sein könne, und daß sie allein deshalb nicht glauben können, es dauere nach dem Tode fort, weil sich aus ihrer Vorstellung heraus keine Möglichkeit ergibt, sich ein leibfreies Dasein zu denken."
      ],
      [
        "Sie sind zwar nicht durch ihre Wünsche, wohl aber durch die Vorstellungen befangen, von denen sie nun eben nicht loskommen können.",
        "Es gibt noch viele Befangenheiten auf diesem Gebiete.",
        "Man kann immer nur einzelne Beispiele dessen anführen, was in die­ser Art alles vorhanden ist."
      ],
      [
        "Der Gedanke, daß der Leib, in dessen Vorgängen sich die Seele auslebt, einmal der Außenwelt verfallen werde"
      ],
      [
        "und Gesetzen folgen, die in keinem Verhältnisse stehen zum inneren Erleben, er läßt das Todeserlebnis so vor die Seele treten, daß kein Wunsch, kein persönliches Interesse sich in die Betrachtung einzumischen brauchen; daß dieses Erlebnis zu einer reinen, unpersönlichen Erkenntnisfrage führen kann.",
        "Es wird sich aber dann auch bald die Empfin­dung ergeben, daß der Todesgedanke nicht um seiner selbst willen bedeutsam ist, sondern deshalb, weil er Licht verbreiten kann über das Leben.",
        "Man wird zu der Ansicht kommen müssen, daß das Rätsel des Lebens zu erkennen ist durch das Wesen des Todes."
      ],
      [
        "Daß die Seele nach ihrer Fortdauer verlangt, sollte unter allen Umständen dazu führen, sie mißtrauisch zu machen gegen alle Meinungen, welche sie sich über diese Fortdauer bildet.",
        "Denn warum sollten sich die Tatsachen der Welt kümmern um das, was die Seele empfindet.",
        "Sie mag nach ihren Bedürfnissen sich selber sinnlos fühlen, wenn sie denken müßte, sie könnte, einer Flamme gleich, die aus dem Brennmaterial sich ergibt, aus dem Stoffe ihres Leibes aufflackern und dann wieder verlöschen.",
        "Es könnte sich dies doch so verhalten, auch wenn es als sinnlos empfun­den würde. - Wenn die Seele den Blick zum Leibe wendet, so soll sie auch nur mit dem rechnen, was er ihr zeigen kann.",
        "Es scheint da, als ob in der Natur die Gesetze wirk­ten, welche die Stoffe und Kräfte in ein Wechselspiel brin­gen, und als ob diese Gesetze den Leib beherrschten, und ihn nach einiger Zeit wieder in das allgemeine Wechsel­spiel einbezögen."
      ],
      [
        "Man mag diesen Gedanken nun wenden, wie man will:"
      ],
      [
        "er ist naturwissenschaftlich wohl brauchbar, doch er er­weist sich der wahren Wirklichkeit gegenüber als ganz unmöglich."
      ],
      [
        "Man kann finden, daß er allein wissenschaftlich klar, nüchtern, und alles andre nur subjektiver Glaube sei; man kann sich dies wohi einbilden.",
        "Man kann es aber bei wirklicher Unbefangenheit nicht festhalten."
      ],
      [
        "Und darauf kommt es an.",
        "Nicht was die Seele durch ihr Wesen als not­wendig empfindet, kommt in Betracht, sondern dasjenige, was die Außenwelt offenbart, welcher der Leib entnom­men ist.",
        "Diese Außenwelt nimmt seine Stoffe und Kräfte nach dem Tode in sich au£ In ihr folgen sie dann Gesetzen, welchen ganz gleichgültig ist, was im menschlichen Leibe während des Lebens vorgeht."
      ],
      [
        "Diese Gesetze (die physi­scher und chemischer Art sind) stellen sich zu dem Leibe nicht anders als zu jedem andern leblosen Dinge der Au­ßenwelt.",
        "Es ist unmöglich, etwas anderes zu denken, als daß dieses gleichgültige Verhältnis der Außenwelt zum Menschenleibe nicht erst mit dem Tode eintritt, sondern daß es auch schon während des Lebens besteht."
      ],
      [
        "Nicht aus dem Leben kann man eine Vorstellung gewinnen über den Anteil der sinnlichen Außenwelt an dem Menschenleibe, sondern allein dadurch, daß man denkt: alles, was da an dir ist als Träger deiner Sinne, als Vermittler von Vorgän­gen, durch welche deine Seele lebt, das wird von der Welt, welche du wahrnimmst, so behandelt, wie dir die Vorstel­lung ergibt, die über dein Leben hinaus schweift.",
        "Die damit rechnet, daß eine Zeit kommen werde, in der du alles die­ses nicht mehr an dir hast, worinnen du dich jetzt erlebst."
      ],
      [
        "Jede andere Vorstellung über das Verhältnis der sinnlichen Außenwelt zum Leibe läßt durch sich selber erfühlen, daß sie gegenüber der Wirklichkeit nicht haltbar ist.",
        "Die Vor­stellung aber, daß erst nach dem Tode der wirkliche Anteil der Außenwelt an dem Leibe zutage tritt, kommt mit"
      ],
      [
        "nichts in Konflikt, was wahrhaft in Außenwelt und Innen­welt erlebt wird.",
        "Die Seele fühlt nichts Unerträgliches bei dem Gedanken, daß ihre Stoffe und Kräfte Vorgängen der Außenwelt verfallen, die mit ihrem eigenen Leben nichts zu tun haben.",
        "Sie kann in ihren Tiefen bei vollkommen unbefangener Hingabe an das Leben keinen aus dem Leibe aufsteigenden Wunsch entdecken, der ihr den Gedanken unbehaglich machte an die Auflösung nach dem Tode.",
        "Das Unerträgliche tritt erst dann ein, wenn die Vorstellung gebildet werden sollte, die in die Außenwelt zurückkeh­renden Stoffe und Kräfte nehmen die sich erlebende Seele mit.",
        "Eine solche Vorstellung wäre aus demselben Grunde unerträglich wie jede andre, die sich nicht naturgemäß aus der Hingabe an die Offenbarung der Außenwelt ergibt."
      ],
      [
        "Der Außenwelt während des Lebens einen ganz andren Anteil an dem Leibesdasein zuzuerkennen als nach dem Tode, ist ein Gedanke, der aus dem Nichts hergeholt wer­den müßte.",
        "Als sinnloser Gedanke muß er stets vor der Wirklichkeit zurückprallen, während doch die Vorstellung ganz gesund ist, daß die Außenwelt während des Lebens ganz den gleichen Anteil an dem Leibe hat wie nach dem Tode.",
        "Die Seele fühlt sich, wenn sie den letztern Gedan­ken hegt, ganz im Einklange mit der Offenbarung der Tat­sachen.",
        "Sie kann empfinden, daß sie durch diese Vorstel­lung nicht in Mißklang kommt mit den Tatsachen, die durch sich selbst sprechen, und denen kein künstlicher Ge­danke hinzugefügt werden darf."
      ],
      [
        "Man achtet nicht immer darauf, in wie schönem Ein­klange das natürliche, gesunde Empfinden der Seele mit der Naturoffenbarung ist.",
        "Es könnte dies so selbstver­ständlich erscheinen, daß es gar keiner Beachtung wert"
      ],
      [
        "wäre; und doch ist dies scheinbar Bedeutungslose licht­bringend.",
        "Nichts Unerträgliches hat der Gedanke, daß der Leib in die Elemente aufgelöst werde; etwas Sinnloses da­gegen der andre, daß dies auch mit der Seele geschehe.",
        "Es gibt viele menschlich persönliche Gründe, welche dies als sinnlos erscheinen lassen; diese müssen von der objektiven Betrachtung unberücksichtigt gelassen werden.",
        "Die ganz unpersönliche Hingabe jedoch an das, was die Außenwelt lehrt, zeigt, daß auch während des Lebens dieser Außen­welt an der Seele kein andrer Anteil zugeschrieben werden kann als nach dem Tode.",
        "Maßgebend ist, daß dieser Ge­danke sich als ein notwendiger ergibt, und daß er stand­hält gegenüber allen Einwänden, die man gegen ihn erhe­ben kann.",
        "Wer ihn ganz bewußt denkt, der fühlt dieses als unmittelbare Gewißheit.",
        "In Wahrheit denken so aber sowohl Unsterblichkeitsgläubige wie Unsterblichkeitsleug­ner.",
        "Die letztern werden wohl sagen, in den Gesetzen, wel­che wirksam sind am Leibe nach dem Tode, seien auch die Bedingungen seiner Vorgänge während des Lebens ent­halten; aber sie irren sich, wenn sie glauben, sich wirklich vorstellen zu können, diese Gesetze stünden während des Lebens in einem andern Verhältnisse zum Leibe als Seelen-träger als nach dem Tode."
      ],
      [
        "In sich möglich ist nur die Vorstellung, auch jener be­sondre Zusammenhang von Kräften, der mit dem Leibe in die Erscheinung tritt, stehe dem Leibe als Seelenträger ge­nau so anteilslos gegenüber wie derjenige, welcher die Vor­gänge am toten Leibe bewirkt.",
        "Nicht für die Seele ist diese Anteilslosigkeit vorhanden, wohl aber für die Stoffe und Kräfte des Leibes.",
        "Die Seele erlebt sich am Leibe; der Leib jedoch lebt mit der Außenwelt, in ihr, durch sie und läßt das"
      ],
      [
        "Seelische für sich nicht anders maßgebend sein als die Vor­gänge der Außenwelt.",
        "Man muß zu der Ansicht kommen, daß für die Blutbewegung im Leibe die Wärme und Kälte der Außenwelt so maßgebend sind, wie die Furcht oder das Schamgefühl, die sich in der Seele abspielen."
      ],
      [
        "So fühlt man zunächst in sich die Gesetze der Außen­welt in jenem ganz besondren Zusammenhange wirksam, der sich als die Gestaltung des Menschenleibes kundgibt.",
        "Man empfindet diesen Leib als ein Glied der Außenwelt.",
        "Aber man steht seinem innern Zusammenhang fremd ge­genüber.",
        "Die äußere Wissenschaft klärt gegenwärtig zum Teil auf, wie sich die Gesetze der Außenwelt in dem ganz besondren Wesen zusammenfügen, das sich als Menschenleib darstellt.",
        "Von der Zukunft darf gehofft werden, daß diese Erkenntnis immer weiter fortschreiten werde.",
        "Wie die Seele über ihr Verhältnis zum Leibe denken muß, daran kann diese fortschreitende Erkenntnis nicht das geringste ändern.",
        "Im Gegenteil, sie wird immer klarer zeigen müs­sen, daß die Gesetze der Außenwelt vor und nach dem Tode in dem gleichen Verhältnisse zur Seele stehen.",
        "Es ist eine Illusion, zu erwarten, mit fortschreitender Naturer­kenntnis werde aus den Gesetzen der Außenwelt sich er­geben, inwieferne die Leibesvorgänge die Vermittler des Seelenlebens sind.",
        "Man wird immer deutlicher erkennen, was im Leibe während des Lebens vorgeht; aber die ent­sprechenden Vorgänge werden sich stets als solche zeigen, welche die Seele als ihr äußerlich so empfindet, wie die Vorgänge am Leibe nach dem Tode."
      ],
      [
        "Innerhalb der Außenwelt muß daher der Leib als ein Zu­sammenhang von Kräften und Stoffen erscheinen, der für sich besteht und in sich erklärbar ist als Glied dieser Außenwelt. -"
      ],
      [
        "Die Natur läßt die Pflanze entstehen; sie löst sie wieder auf.",
        "Sie beherrscht den Menschenleib und läßt ihn innerhalb ihrer Wesenheit vergehen.",
        "Stellt sich der Mensch mit einer solchen Betrachtung der Natur gegenüber, so kann er sich und alles, was in ihm ist, vergessen, und sei­nen Leib als Glied der Außenwelt an sich empfinden.",
        "Denkt er so über sein Verhältnis zu sich und zur Natur, so erlebt er an sich, was man seinen physischen Leib nennen kann."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "ZWEITE MEDITATION",
    "paragraphs": [
      "ZWEITE MEDITATION",
      "Der    Meditierende versucht eine wahre Vorstellung von dem",
      "elementarischen oder ätherischen Leibe zu gewinnen",
      "Durch die Vorstellung, welche die Seele sich in Anknüp­fung an die Tatsache des Todes machen muß, kann sie in eine völlige Unsicherheit über ihr eigenes Wesen hineinge­trieben werden. Es wird dies dann der Fall sein, wenn sie glaubt, von keiner andern Welt etwas wissen zu können, als nur allein von der Sinnenwelt und von dem, was der Verstand über diese Welt zu erkennen vermag. Das ge­wöhnliche Seelenleben richtet den Blick auf den physischen Leib. Es sieht diesen nach dem Tode übergehen in den Na­turzusammenhang, der ohne Anteil ist an dem, was die Seele vor dem Tode als ihr eigenes Dasein erlebt. Sie kann zwar wissen (durch die vorangehende Meditation), daß der physische Leib auch während des Lebens zu ihr in dem­selben Verhältnisse steht wie nach dem Tode: aber dies führt sie nicht weiter als zur Anerkennung der inneren Selbständigkeit des eigenen Erlebens bis zum Tode. Was mit dem physischen Leibe nach dem Tode geschieht, das ergibt ihr die Beobachtung der Außenwelt. Für das innere Erleben gibt es eine solche Beobachtung nicht. So wie die­ses Seelenleben ist, kann es den Blick nicht über die Grenze des Todes hinaus richten. Ist die Seele außerstande sich Vorstellungen zu machen, welche über die Welt hinaus­gehen, von welcher der Leib nach dem Tode aufgenommen wird, dann hat sie auch keine Möglichkeit, in etwas anderes als in das leere Nichts jenseits des Todes in bezug auf alles Seelische zu blicken.",
      "Sollte dies anders sein, so müßte die Seele die Außenwelt",
      "mit anderen Mitteln wahrnehmen als mit den Sinnen und mit dem an die Sinne gebundenen Verstand. Diese sind selbst zum Leibe gehörig und verfallen mit ihm. Was sie sagen, kann nie zu etwas anderem führen als zu dem Er­gebnis der ersten Meditation. Und das besteht nur darin, daß die Seele sich gestehen kann: - du bist an deinen Leib gebunden. Dieser ist Naturgesetzen unterworfen, welche zu dir stehen, wie alle andern Naturgesetze. Du bist durch sie ein Glied der Außenwelt, und diese hat an dir einen Anteil, der sich dir am deutlichsten offenbart, wenn du be­trachtest, was sie mit deinem Leibe nach dem Tode macht. Für das Leben gibt sie dir Sinne und einen Verstand, wel­che es dir unmöglich machen, zu sehen, wie es mit deinem seelischen Erleben jenseits der Todesgrenze steht. Dies Ge­ständnis kann nur zu zwei Ergebnissen führen. Entweder es wird alles weitere Nachforschen über das Seelenrätsel unterdrückt und Verzicht geleistet, auf diesem Gebiete et­was zu wissen. Oder es werden Anstrengungen gemacht, durch das seelische Erleben im Innern das zu erreichen, was die Außenwelt versagt. - Diese Anstrengungen kön­nen dazu führen, das innere Erleben kraftvoller, energischer zu machen, als es im gewöhnlichen Dasein ist.",
      "Im gewöhnlichen Leben hat der Mensch eine gewisse Stärke seiner inneren Erlebnisse, seines Empfindungs- und Gedankenlebens. Er hegt zum Beispiel einen Gedanken so oft, als sich ein äußerer oder innerer Anlaß dazu ergibt. Es kann aber irgendein Gedanke aus der Zahl der andern her­ausgenommen werden und ohne weiteren Anlaß immer wieder durchdacht, in intensiver Art innerlich erlebt wer­den. Man kann einen solchen Gedanken wiederholt zum einzigen Gegenstande des inneren Erlebens machen. Und",
      "während man dieses tut, kann man alle äußeren Eindrücke und alle Erinnerungen, die in der Seele auftauchen möch­ten, von sich ferne halten. Man kann eine solche volle, alles andre ausschließende Hingabe an Gedanken, oder auch an Empfindungen, zu einer regelmäßigen inneren Betätigung machen. - Soll ein solches inneres Erleben zu wirklich be­deutsamen Ergebnissen führen, so muß es allerdings nach gewissen, erprobten Gesetzen unternommen werden. Sol­che Gesetze werden von der Wissenschaft des Geistesle­bens verzeichnet. Man findet eine größere Anzahl in mei­ner Schrift angegeben: «Wie erlangt man Erkenntnisse der höheren Welten?» - Durch solches Vorgehen erreicht man eine Verstärkung der Kräfte des inneren Erlebens. Dieses verdichtet sich gewissermaßen. Was dadurch geschieht, das kann man erkennen an den Beobachtungen an sich selbst, die eintreten, wenn die geschilderte innere Betäti­gung eine genügend lange Zeit fortgesetzt wird. Man braucht allerdings in den meisten Fällen viel Geduld, bis überzeugende Ergebnisse eintreten. Und wer nicht geneigt ist, diese Geduld jahrelang zu üben, der wird nichts Be­sonderes erzielen.",
      "Es ist nur möglich, hier ein Beispiel anzuführen von sol­chen Ergebnissen. Diese sind mannigfaltiger Art. Und was hier angeführt wird, das ist geeignet, den Meditationsweg, mit dessen Schilderung hier begonnen worden ist, fortzu­setzen.",
      "Ein Mensch kann lange die angegebene innere Verstär­kung seines Seelenlebens üben. Er wird vielleicht nichts in sich erleben, was geeignet ist, ihn anders über die Welt denken zu lassen, als er bisher gewohnt war. Dann aber kann einmal das Folgende eintreten. Naturgemäß wird,",
      "was hier zu schildern ist, nicht in genau der gleichen Art sich bei zwei Menschen einstellen. Wer aber von einem sol­chen Erlebnis eine Vorstellung zu gewinnen sucht, der hat sich über das ganze hier in Betracht kommende Gebiet aufgeklärt.",
      "Es kann ein Augenblick eintreten, in dem die Seele sich innerlich ganz anders erlebt als gewöhnlich. Zumeist wird das anfangs so geschehen, daß die Seele aus dem Schlafe wie zu einem Traume sich belebt. Nur zeigt sich sogleich, daß sich das Erlebnis mit dem nicht vergleichen läßt, was man sonst als Träume kennt. Man ist dann der Sinnes- und Verstandeswelt ganz entrückt, und man erlebt doch so, wie man im gewöhnlichen Dasein nur erlebt, wenn man im wachen Zustande der Außenwelt gegenübersteht. Man fühlt sich gedrängt, das Erlebnis in sich vorzustellen. Man nimmt zu dem Vorstellen solche Begriffe, die man im ge­wöhnlichen Leben hat; aber man weiß sehr genau, daß man anderes erlebt, als das ist, worauf sich in normaler Art diese Begriffe beziehen. Diese betrachtet man nur als ein Ausdrucksmittel für ein Erlebnis, das man vorher nicht gehabt hat, und von dem man auch wissen kann, daß es im gewöhnlichen Dasein unmöglich ist. Man fühlt sich etwa allseitig von Gewitterstürmen umgeben. Man hört Don­ner und vernimmt Blitze. Man weiß sich in einem Zimmer eines Hauses. Man fühlt sich durchsetzt von einer Kraft, von welcher man vorher nichts gewußt hat. Dann ver­meint man Risse um sich her in den Mauern zu sehen. Man ist veranlaßt, sich oder einer Person, die man neben sich zu haben glaubt, zu sagen: jetzt handelt es sich um Schweres; der Blitz geht durch das Haus, er erfaßt mich; ich fühle mich von ihm ergriffen. Er löst mich auf. - Wenn dann",
      "eine solche Reihe von Vorstellungen abgelaufen ist, dann geht das innere Erleben in die gewöhnliche Seelenverfassung über. Man findet sich in sich mit der Erinnerung an das eben Erlebte. Ist diese Erinnerung so lebhaft und so treu wie eine andre, dann befähigt sie auch, ein Urteil sich zu bilden über das Erlebte. Man weiß dann unmittelbar, daß man etwas durchgemacht hat, was man durch keinen leiblichen Sinn und auch nicht durch den gewöhnlichen Verstand durchmachen kann. Denn man fühlt, daß die eben gemachte Beschreibung, die man sich oder andern geben kann, nur ein Mittel ist, das Erlebnis auszudrücken. Der Ausdruck ist zwar ein Verständigungsmittel über die Sache; aber er hat mit dieser nichts gemein. Man weiß, daß man für ein solches Erlebnis keinen seiner Sinne braucht.",
      "- Wer etwa von einer verborgenen Wirksamkeit der Sinne oder des Gehirnes sprechen will, der kennt die wahre Ge­stalt des Erlebnisses nicht. Er hält sich an die Beschrei­bung, die vom Blitz, Donner, Mauerrissen redet, und des­wegen glaubt er, daß die Seele nichts erlebt hat als Nach­klänge des gewöhnlichen Daseins. Er muß das Erlebte für eine Vision im gewöhnlichen Sinne des Wortes halten. Er vermag nicht anders, als so zu denken. Er berücksichtigt nur nicht, daß derjenige, welcher ein solches Erlebnis schildert, mit den Worten Blitz, Donner, Mauerrisse nur Bilder meint für das Erlebte, und daß er dieses nicht mit den Bildern verwechselt. Es ist richtig, daß ihm die Sache so erscheint, als ob er diese Bilder wirklich wahrnehmen würde. Er verhält sich aber in einem solchen Falle zur Blitzerscheinung nicht so, wie er dies tut, wenn er mit sei­nem Auge einen Blitz sieht. Für ihn bildet die Vision des Blitzes nur etwas, was sich gewissermaßen über das wahre",
      "Erlebnis hinüberbreitet; er sieht durch den Blitz auf etwas ganz anderes, auf etwas, das in der sinnlichen Außenwelt nicht erlebt werden kann.",
      "Notwendig ist, damit ein richtiges Urteil zustande kom­me, daß die Seele, die solches erlebt, dann, wenn das Er­lebnis vorbei ist, in völlig gesunder Art sich zur Außen­welt verhält. Sie muß richtig vergleichen können, was sie als besonderes Erlebnis gehabt hat, mit dem Erleben der gewöhnlichen Außenwelt. Wer schon im gewöhnlichen Leben dazu neigt, sich zu allerlei Schwärmereien über die Dinge hinreißen zu lassen, der taugt schlecht zu einem sol­chen Urteil. Je mehr der Mensch gesunden, man möchte sagen, nüchternen Wirklichkeitssinn hat, desto besser ist es, wenn es sich um eine wahrhafte und wertvolle Beurtei­lung solcher Dinge handelt. Vertrauen in übersinnliche Erlebnisse kann man sich selbst nur entgegenbringen, wenn man in bezug auf die gewöhnliche Welt sich sagen darf, daß man die Vorgänge und Dinge in klarer Weise so nimmt, wie sie sind.",
      "Sind so alle notwendigen Bedingungen erfüllt, und hat man Grund anzunehmen, daß man nicht einer gewöhnli­chen Vision zum Opfer gefallen ist, dann weiß man, daß man etwas erlebt hat, wozu man den Leib nicht als Ver­mittler der Beobachtung gehabt hat. Man hat ohne den Leib unmittelbar durch die in sich stärker gewordene Seele beobachtet. Man hat die Vorstellung eines Erlebnisses außerhalb seines Leibes gewonnen.",
      "Es kann einleuchtend sein, daß auf diesem Gebiete ge­setzmäßige Unterschiede zwischen Träumerei oder Illu­sion und wahrer außerhalb des Leibes vollzogener Beob­achtung nicht in anderem Sinne angegeben werden können",
      "als auf dem Gebiet der äußeren Sinneswahrnehmung. Es kann vorkommen, daß jemand lebendige Geschmacksphantasie hat und schon bei der bloßen Vorstellung einer Limonade ähnlich empfindet, wie wenn er eine solche wirk­lich trinkt. Den Unterschied des einen von dem andern er­gibt aber denn doch der ganze Zusammenhang des Lebens. Und so ist es auch mit den Erlebnissen, die außerhalb des Leibes gemacht werden. Um zu völlig überzeugenden Vor­stellungen auf diesem Gebiete zu kommen, ist notwendig, sich in gesunder Art in dasselbe einzuleben, sich die Fähig­keit anzueignen, die Zusammenhänge des Erlebens zu be­obachten, und so das eine durch das andere zu korrigieren.",
      "Man hat durch ein Erlebnis, wie das geschilderte es ist, die Möglichkeit gewonnen, dasjenige, was zu dem eigenen Selbst gehört, nicht nur durch die Sinne und den Verstand, also durch die leiblichen Werkzeuge, zu beobachten. Man weiß nunmehr über die Welt nicht nur etwas andres, als was diese Werkzeuge erkennen lassen; man weiß auch auf andere Art. Darauf kommt es ganz besonders an. Eine Seele, die eine innerliche Umwandlung durchmacht, kommt immer mehr dazu, einzusehen, daß in der Sinneswelt des­wegen die bedrückenden Daseinsfragen sich nicht zur Lö­sung bringen lassen, weil die Sinne und der Verstand nicht tief genug in die Welt eindringen können. Tiefer dringen die Seelen ein, welche sich so umwandeln, daß sie außer­halb des Leibes erleben können. In den Mitteilungen, wel­che sie über ihre Erlebnisse machen können, liegt vor, was die seelischen Rätsel lösen kann.",
      "Nun ist ein Erleben, das außerhalb des Leibes sich vollzieht, von ganz andrer Art als ein solches im Leibe. Dar­über klärt eben das Urteil auf, das in bezug auf das geschil­derte",
      "Erlebnis gebildet werden kann, wenn nach ihm der gewöhnliche wache Seelenzustand wieder eingetreten und die Erinnerung lebhaft und klar genug zustande gekom­men ist. Den sinnlichen Leib fühlt die Seele getrennt von der übrigen Welt, sie nimmt ihn als nur zu sich gehörig wahr. So ist es nicht mit dem, was man in sich und an sich erlebt außerhalb des Leibes. Da fühlt man sich verbunden mit allem, was man Außenwelt nennen kann. Was in der Umgebung ist, das fühlt man mit sich verbunden wie im Sinnesleben seine Hand. Es ist keine Gleichgültigkeit der Außenwelt gegenüber einer seelischen Innenwelt vorhan­den. Man empfindet sich im vollen Maße als zusammen­gewachsen, verwoben mit dem, was man die Welt nennen kann. Deren Wirkungen gehen durch die eigene Wesen­heit wahrnehmbar hindurch. Es ist keine scharfe Grenze zwischen Innenwelt und Außenwelt. Es gehört von dieser zu der betrachtenden Seele die ganze Umgebung, wie zum physischen Kopf die beiden Hände des Leibes gehören. Trotzdem kann man von einem Stück dieser Außenwelt sprechen, das mehr zum eigenen Selbst gehört als die übri­ge Umgebung, wie man vom Kopfe als selbständigem Gliede gegenüber den Händen oder Füßen spricht.",
      "Die Seele nennt ein Stück sinnlicher Außenwelt ihren Leib. Die außerhalb dieses Leibes erlebende Seele kann ebensogut einen Teil der nicht sinnlichen Außenwelt zu sich gehörig betrachten. Dringt der Mensch zu einer Beob­achtung dieses jenseits der Sinnenwelt ihm zugänglichen Gebietes vor, so kann er davon sprechen, daß ein sinnlich nicht wahrnehmbarer Leib zu ihm gehört. Man kann die­sen Leib den elementarischen oder ätherischen Leib nen­nen; wobei man bei dem Worte «ätherisch» nicht den von",
      "der Physik «Äther» genannten feinen Stoff in seine Vor­stellung einbeziehen soll.",
      "Wie die bloße Überlegung über das Verhältnis des Men­schen zur natürlichen Außenwelt die den Tatsachen ent­sprechende Vorstellung des physischen Leibes ergibt, so führt die Wanderschaft der Seele in Gebiete, die außerhalb des Sinnenleibes erschaut werden können, zur Anerken­nung eines elementarischen oder ätherischen oder Bildekräfte­leibes."
    ],
    "sentences": [
      [
        "ZWEITE MEDITATION"
      ],
      [
        "Der Meditierende versucht eine wahre Vorstellung von dem"
      ],
      [
        "elementarischen oder ätherischen Leibe zu gewinnen"
      ],
      [
        "Durch die Vorstellung, welche die Seele sich in Anknüp­fung an die Tatsache des Todes machen muß, kann sie in eine völlige Unsicherheit über ihr eigenes Wesen hineinge­trieben werden.",
        "Es wird dies dann der Fall sein, wenn sie glaubt, von keiner andern Welt etwas wissen zu können, als nur allein von der Sinnenwelt und von dem, was der Verstand über diese Welt zu erkennen vermag.",
        "Das ge­wöhnliche Seelenleben richtet den Blick auf den physischen Leib.",
        "Es sieht diesen nach dem Tode übergehen in den Na­turzusammenhang, der ohne Anteil ist an dem, was die Seele vor dem Tode als ihr eigenes Dasein erlebt.",
        "Sie kann zwar wissen (durch die vorangehende Meditation), daß der physische Leib auch während des Lebens zu ihr in dem­selben Verhältnisse steht wie nach dem Tode: aber dies führt sie nicht weiter als zur Anerkennung der inneren Selbständigkeit des eigenen Erlebens bis zum Tode.",
        "Was mit dem physischen Leibe nach dem Tode geschieht, das ergibt ihr die Beobachtung der Außenwelt.",
        "Für das innere Erleben gibt es eine solche Beobachtung nicht.",
        "So wie die­ses Seelenleben ist, kann es den Blick nicht über die Grenze des Todes hinaus richten.",
        "Ist die Seele außerstande sich Vorstellungen zu machen, welche über die Welt hinaus­gehen, von welcher der Leib nach dem Tode aufgenommen wird, dann hat sie auch keine Möglichkeit, in etwas anderes als in das leere Nichts jenseits des Todes in bezug auf alles Seelische zu blicken."
      ],
      [
        "Sollte dies anders sein, so müßte die Seele die Außenwelt"
      ],
      [
        "mit anderen Mitteln wahrnehmen als mit den Sinnen und mit dem an die Sinne gebundenen Verstand.",
        "Diese sind selbst zum Leibe gehörig und verfallen mit ihm.",
        "Was sie sagen, kann nie zu etwas anderem führen als zu dem Er­gebnis der ersten Meditation.",
        "Und das besteht nur darin, daß die Seele sich gestehen kann: - du bist an deinen Leib gebunden.",
        "Dieser ist Naturgesetzen unterworfen, welche zu dir stehen, wie alle andern Naturgesetze.",
        "Du bist durch sie ein Glied der Außenwelt, und diese hat an dir einen Anteil, der sich dir am deutlichsten offenbart, wenn du be­trachtest, was sie mit deinem Leibe nach dem Tode macht.",
        "Für das Leben gibt sie dir Sinne und einen Verstand, wel­che es dir unmöglich machen, zu sehen, wie es mit deinem seelischen Erleben jenseits der Todesgrenze steht.",
        "Dies Ge­ständnis kann nur zu zwei Ergebnissen führen.",
        "Entweder es wird alles weitere Nachforschen über das Seelenrätsel unterdrückt und Verzicht geleistet, auf diesem Gebiete et­was zu wissen.",
        "Oder es werden Anstrengungen gemacht, durch das seelische Erleben im Innern das zu erreichen, was die Außenwelt versagt. - Diese Anstrengungen kön­nen dazu führen, das innere Erleben kraftvoller, energischer zu machen, als es im gewöhnlichen Dasein ist."
      ],
      [
        "Im gewöhnlichen Leben hat der Mensch eine gewisse Stärke seiner inneren Erlebnisse, seines Empfindungs- und Gedankenlebens.",
        "Er hegt zum Beispiel einen Gedanken so oft, als sich ein äußerer oder innerer Anlaß dazu ergibt.",
        "Es kann aber irgendein Gedanke aus der Zahl der andern her­ausgenommen werden und ohne weiteren Anlaß immer wieder durchdacht, in intensiver Art innerlich erlebt wer­den.",
        "Man kann einen solchen Gedanken wiederholt zum einzigen Gegenstande des inneren Erlebens machen."
      ],
      [
        "während man dieses tut, kann man alle äußeren Eindrücke und alle Erinnerungen, die in der Seele auftauchen möch­ten, von sich ferne halten.",
        "Man kann eine solche volle, alles andre ausschließende Hingabe an Gedanken, oder auch an Empfindungen, zu einer regelmäßigen inneren Betätigung machen. - Soll ein solches inneres Erleben zu wirklich be­deutsamen Ergebnissen führen, so muß es allerdings nach gewissen, erprobten Gesetzen unternommen werden.",
        "Sol­che Gesetze werden von der Wissenschaft des Geistesle­bens verzeichnet.",
        "Man findet eine größere Anzahl in mei­ner Schrift angegeben: «Wie erlangt man Erkenntnisse der höheren Welten?» - Durch solches Vorgehen erreicht man eine Verstärkung der Kräfte des inneren Erlebens.",
        "Dieses verdichtet sich gewissermaßen.",
        "Was dadurch geschieht, das kann man erkennen an den Beobachtungen an sich selbst, die eintreten, wenn die geschilderte innere Betäti­gung eine genügend lange Zeit fortgesetzt wird.",
        "Man braucht allerdings in den meisten Fällen viel Geduld, bis überzeugende Ergebnisse eintreten.",
        "Und wer nicht geneigt ist, diese Geduld jahrelang zu üben, der wird nichts Be­sonderes erzielen."
      ],
      [
        "Es ist nur möglich, hier ein Beispiel anzuführen von sol­chen Ergebnissen.",
        "Diese sind mannigfaltiger Art.",
        "Und was hier angeführt wird, das ist geeignet, den Meditationsweg, mit dessen Schilderung hier begonnen worden ist, fortzu­setzen."
      ],
      [
        "Ein Mensch kann lange die angegebene innere Verstär­kung seines Seelenlebens üben.",
        "Er wird vielleicht nichts in sich erleben, was geeignet ist, ihn anders über die Welt denken zu lassen, als er bisher gewohnt war.",
        "Dann aber kann einmal das Folgende eintreten.",
        "Naturgemäß wird,"
      ],
      [
        "was hier zu schildern ist, nicht in genau der gleichen Art sich bei zwei Menschen einstellen.",
        "Wer aber von einem sol­chen Erlebnis eine Vorstellung zu gewinnen sucht, der hat sich über das ganze hier in Betracht kommende Gebiet aufgeklärt."
      ],
      [
        "Es kann ein Augenblick eintreten, in dem die Seele sich innerlich ganz anders erlebt als gewöhnlich.",
        "Zumeist wird das anfangs so geschehen, daß die Seele aus dem Schlafe wie zu einem Traume sich belebt.",
        "Nur zeigt sich sogleich, daß sich das Erlebnis mit dem nicht vergleichen läßt, was man sonst als Träume kennt.",
        "Man ist dann der Sinnes- und Verstandeswelt ganz entrückt, und man erlebt doch so, wie man im gewöhnlichen Dasein nur erlebt, wenn man im wachen Zustande der Außenwelt gegenübersteht.",
        "Man fühlt sich gedrängt, das Erlebnis in sich vorzustellen.",
        "Man nimmt zu dem Vorstellen solche Begriffe, die man im ge­wöhnlichen Leben hat; aber man weiß sehr genau, daß man anderes erlebt, als das ist, worauf sich in normaler Art diese Begriffe beziehen.",
        "Diese betrachtet man nur als ein Ausdrucksmittel für ein Erlebnis, das man vorher nicht gehabt hat, und von dem man auch wissen kann, daß es im gewöhnlichen Dasein unmöglich ist.",
        "Man fühlt sich etwa allseitig von Gewitterstürmen umgeben.",
        "Man hört Don­ner und vernimmt Blitze.",
        "Man weiß sich in einem Zimmer eines Hauses.",
        "Man fühlt sich durchsetzt von einer Kraft, von welcher man vorher nichts gewußt hat.",
        "Dann ver­meint man Risse um sich her in den Mauern zu sehen.",
        "Man ist veranlaßt, sich oder einer Person, die man neben sich zu haben glaubt, zu sagen: jetzt handelt es sich um Schweres; der Blitz geht durch das Haus, er erfaßt mich; ich fühle mich von ihm ergriffen.",
        "Er löst mich auf. - Wenn dann"
      ],
      [
        "eine solche Reihe von Vorstellungen abgelaufen ist, dann geht das innere Erleben in die gewöhnliche Seelenverfassung über.",
        "Man findet sich in sich mit der Erinnerung an das eben Erlebte.",
        "Ist diese Erinnerung so lebhaft und so treu wie eine andre, dann befähigt sie auch, ein Urteil sich zu bilden über das Erlebte.",
        "Man weiß dann unmittelbar, daß man etwas durchgemacht hat, was man durch keinen leiblichen Sinn und auch nicht durch den gewöhnlichen Verstand durchmachen kann.",
        "Denn man fühlt, daß die eben gemachte Beschreibung, die man sich oder andern geben kann, nur ein Mittel ist, das Erlebnis auszudrücken.",
        "Der Ausdruck ist zwar ein Verständigungsmittel über die Sache; aber er hat mit dieser nichts gemein.",
        "Man weiß, daß man für ein solches Erlebnis keinen seiner Sinne braucht."
      ],
      [
        "- Wer etwa von einer verborgenen Wirksamkeit der Sinne oder des Gehirnes sprechen will, der kennt die wahre Ge­stalt des Erlebnisses nicht.",
        "Er hält sich an die Beschrei­bung, die vom Blitz, Donner, Mauerrissen redet, und des­wegen glaubt er, daß die Seele nichts erlebt hat als Nach­klänge des gewöhnlichen Daseins.",
        "Er muß das Erlebte für eine Vision im gewöhnlichen Sinne des Wortes halten.",
        "Er vermag nicht anders, als so zu denken.",
        "Er berücksichtigt nur nicht, daß derjenige, welcher ein solches Erlebnis schildert, mit den Worten Blitz, Donner, Mauerrisse nur Bilder meint für das Erlebte, und daß er dieses nicht mit den Bildern verwechselt.",
        "Es ist richtig, daß ihm die Sache so erscheint, als ob er diese Bilder wirklich wahrnehmen würde.",
        "Er verhält sich aber in einem solchen Falle zur Blitzerscheinung nicht so, wie er dies tut, wenn er mit sei­nem Auge einen Blitz sieht.",
        "Für ihn bildet die Vision des Blitzes nur etwas, was sich gewissermaßen über das wahre"
      ],
      [
        "Erlebnis hinüberbreitet; er sieht durch den Blitz auf etwas ganz anderes, auf etwas, das in der sinnlichen Außenwelt nicht erlebt werden kann."
      ],
      [
        "Notwendig ist, damit ein richtiges Urteil zustande kom­me, daß die Seele, die solches erlebt, dann, wenn das Er­lebnis vorbei ist, in völlig gesunder Art sich zur Außen­welt verhält.",
        "Sie muß richtig vergleichen können, was sie als besonderes Erlebnis gehabt hat, mit dem Erleben der gewöhnlichen Außenwelt.",
        "Wer schon im gewöhnlichen Leben dazu neigt, sich zu allerlei Schwärmereien über die Dinge hinreißen zu lassen, der taugt schlecht zu einem sol­chen Urteil.",
        "Je mehr der Mensch gesunden, man möchte sagen, nüchternen Wirklichkeitssinn hat, desto besser ist es, wenn es sich um eine wahrhafte und wertvolle Beurtei­lung solcher Dinge handelt.",
        "Vertrauen in übersinnliche Erlebnisse kann man sich selbst nur entgegenbringen, wenn man in bezug auf die gewöhnliche Welt sich sagen darf, daß man die Vorgänge und Dinge in klarer Weise so nimmt, wie sie sind."
      ],
      [
        "Sind so alle notwendigen Bedingungen erfüllt, und hat man Grund anzunehmen, daß man nicht einer gewöhnli­chen Vision zum Opfer gefallen ist, dann weiß man, daß man etwas erlebt hat, wozu man den Leib nicht als Ver­mittler der Beobachtung gehabt hat.",
        "Man hat ohne den Leib unmittelbar durch die in sich stärker gewordene Seele beobachtet.",
        "Man hat die Vorstellung eines Erlebnisses außerhalb seines Leibes gewonnen."
      ],
      [
        "Es kann einleuchtend sein, daß auf diesem Gebiete ge­setzmäßige Unterschiede zwischen Träumerei oder Illu­sion und wahrer außerhalb des Leibes vollzogener Beob­achtung nicht in anderem Sinne angegeben werden können"
      ],
      [
        "als auf dem Gebiet der äußeren Sinneswahrnehmung.",
        "Es kann vorkommen, daß jemand lebendige Geschmacksphantasie hat und schon bei der bloßen Vorstellung einer Limonade ähnlich empfindet, wie wenn er eine solche wirk­lich trinkt.",
        "Den Unterschied des einen von dem andern er­gibt aber denn doch der ganze Zusammenhang des Lebens.",
        "Und so ist es auch mit den Erlebnissen, die außerhalb des Leibes gemacht werden.",
        "Um zu völlig überzeugenden Vor­stellungen auf diesem Gebiete zu kommen, ist notwendig, sich in gesunder Art in dasselbe einzuleben, sich die Fähig­keit anzueignen, die Zusammenhänge des Erlebens zu be­obachten, und so das eine durch das andere zu korrigieren."
      ],
      [
        "Man hat durch ein Erlebnis, wie das geschilderte es ist, die Möglichkeit gewonnen, dasjenige, was zu dem eigenen Selbst gehört, nicht nur durch die Sinne und den Verstand, also durch die leiblichen Werkzeuge, zu beobachten.",
        "Man weiß nunmehr über die Welt nicht nur etwas andres, als was diese Werkzeuge erkennen lassen; man weiß auch auf andere Art.",
        "Darauf kommt es ganz besonders an.",
        "Eine Seele, die eine innerliche Umwandlung durchmacht, kommt immer mehr dazu, einzusehen, daß in der Sinneswelt des­wegen die bedrückenden Daseinsfragen sich nicht zur Lö­sung bringen lassen, weil die Sinne und der Verstand nicht tief genug in die Welt eindringen können.",
        "Tiefer dringen die Seelen ein, welche sich so umwandeln, daß sie außer­halb des Leibes erleben können.",
        "In den Mitteilungen, wel­che sie über ihre Erlebnisse machen können, liegt vor, was die seelischen Rätsel lösen kann."
      ],
      [
        "Nun ist ein Erleben, das außerhalb des Leibes sich vollzieht, von ganz andrer Art als ein solches im Leibe.",
        "Dar­über klärt eben das Urteil auf, das in bezug auf das geschil­derte"
      ],
      [
        "Erlebnis gebildet werden kann, wenn nach ihm der gewöhnliche wache Seelenzustand wieder eingetreten und die Erinnerung lebhaft und klar genug zustande gekom­men ist.",
        "Den sinnlichen Leib fühlt die Seele getrennt von der übrigen Welt, sie nimmt ihn als nur zu sich gehörig wahr.",
        "So ist es nicht mit dem, was man in sich und an sich erlebt außerhalb des Leibes.",
        "Da fühlt man sich verbunden mit allem, was man Außenwelt nennen kann.",
        "Was in der Umgebung ist, das fühlt man mit sich verbunden wie im Sinnesleben seine Hand.",
        "Es ist keine Gleichgültigkeit der Außenwelt gegenüber einer seelischen Innenwelt vorhan­den.",
        "Man empfindet sich im vollen Maße als zusammen­gewachsen, verwoben mit dem, was man die Welt nennen kann.",
        "Deren Wirkungen gehen durch die eigene Wesen­heit wahrnehmbar hindurch.",
        "Es ist keine scharfe Grenze zwischen Innenwelt und Außenwelt.",
        "Es gehört von dieser zu der betrachtenden Seele die ganze Umgebung, wie zum physischen Kopf die beiden Hände des Leibes gehören.",
        "Trotzdem kann man von einem Stück dieser Außenwelt sprechen, das mehr zum eigenen Selbst gehört als die übri­ge Umgebung, wie man vom Kopfe als selbständigem Gliede gegenüber den Händen oder Füßen spricht."
      ],
      [
        "Die Seele nennt ein Stück sinnlicher Außenwelt ihren Leib.",
        "Die außerhalb dieses Leibes erlebende Seele kann ebensogut einen Teil der nicht sinnlichen Außenwelt zu sich gehörig betrachten.",
        "Dringt der Mensch zu einer Beob­achtung dieses jenseits der Sinnenwelt ihm zugänglichen Gebietes vor, so kann er davon sprechen, daß ein sinnlich nicht wahrnehmbarer Leib zu ihm gehört.",
        "Man kann die­sen Leib den elementarischen oder ätherischen Leib nen­nen; wobei man bei dem Worte «ätherisch» nicht den von"
      ],
      [
        "der Physik «Äther» genannten feinen Stoff in seine Vor­stellung einbeziehen soll."
      ],
      [
        "Wie die bloße Überlegung über das Verhältnis des Men­schen zur natürlichen Außenwelt die den Tatsachen ent­sprechende Vorstellung des physischen Leibes ergibt, so führt die Wanderschaft der Seele in Gebiete, die außerhalb des Sinnenleibes erschaut werden können, zur Anerken­nung eines elementarischen oder ätherischen oder Bildekräfte­leibes."
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "DRITTE MEDITATION",
    "paragraphs": [
      "DRITTE MEDITATION",
      "Der Meditierende versucht sich Vorstellungen zu bilden",
      "über die hellsichtige Erkenntnis der elementarischen Welt",
      "Man erlebt eine Welt, welche der Sinneswahrnehmung und dem gewöhnlichen Verstandesdenken unbekannt bleibt, wenn man nicht durch den sinnlichen Leib, sondern au­ßerhalb desselben durch den elementarischen Leib wahr­nimmt. Will man diese Welt mit etwas vergleichen, das dem gewöhnlichen Erleben angehört, so bietet sich die Welt der Erinnerungen, der Gedächtnisvorstellungen dar. Wie diese aus dem Innern der Seele aufsteigen, so ge­schieht es auch mit den übersinnlichen Erlebnissen des ele­mentarischen Leibes. Nur weiß die Seele bei einer Erinne­rungsvorstellung, daß sich diese auf ein früheres Erlebnis innerhalb der Sinnenwelt bezieht. Die übersinnliche Vor­stellung trägt ebenso eine Beziehung in sich. Wie sich die Erinnerungsvorstellung durch sich selbst als etwas ankün­digt, was man nicht als bloßes Phantasiegebilde bezeich­nen kann, so auch die übersinnliche Vorstellung. Sie ringt sich aus dem seelischen Erleben heraus, aber sie offenbart sich sogleich als ein inneres Erlebnis, welches sich auf et­was Äußeres bezieht. Durch die Erinnerungsvorstellung wird etwas in der Seele gegenwärtig, was man erlebt hat. Durch die übersinnliche Vorstellung wird inneres Seelenerlebnis, was irgendwann oder irgendwo in der übersinn­lichen Welt vorhanden ist. Es offenbart sich also durch die Wesenheit der übersinnlichen Vorstellungen selbst, daß man sie so ansehen kann wie sich innerlich erschließende Mitteilungen aus einer übersinnlichen Welt.",
      "Wie weit man kommt mit den Erlebnissen in der übersinnlichen",
      "Welt auf diese Art, das hängt davon ab, wie energisch man die Verstärkung des Seelenlebens betreibt. Ob man bloß einen Begriff davon erhält, daß eine Pflanze nicht bloß dasjenige ist, was man innerhalb der Sinnen­welt wahrnimmt, oder ob man einen ähnlichen Begriff von der ganzen Erde erhält, das gehört beides dem gleichen Gebiete des übersinnlichen Erlebens an.",
      "Betrachtet derje­nige, welcher sich die Fähigkeit erworben hat, außerhalb seines sinnlichen Leibes wahrzunehmen, eine Pflanze, so kann er außer dem, was die Sinne an ihr zeigen, eine feine Gestalt wahrnehmen, welche die ganze Pflanze durch­dringt. Diese Gestalt bietet sich ihm als eine Kraftwesen­heit dar; und er kommt dazu, diese Kraftwesenheit als das­jenige anzusehen, was aus den Stoffen und Kräften der Sinnenwelt die Pflanze gestaltet, was den Umlauf ihrer Säfte bewirkt.",
      "Er kann sagen, wenn er einen brauchbaren, wenn auch nicht ganz zutreffenden Ausdruck anwenden will: in der Pflanze ist etwas, was die Säfte so in Umlauf bringt, wie meine eigene Seele meinen Arm hebt. Er blickt auf ein Inneres in der Pflanze.",
      "Und er muß diesem Inneren des Pflanzenwesens eine Selbständigkeit zugestehen gegen­über dem, was die Sinne an der Pflanze sehen. Er muß ihm auch zugestehen, daß es vor der sinnlichen Pflanze vorhan­den ist.",
      "Er gelangt dazu, zu beobachten, wie eine Pflanze wächst, verwelkt, Keime treibt, und wie aus den letztern eine neue Pflanze entsteht. Die übersinnliche Kraftgestalt ist besonders dann am mächtigsten, wenn die Beobachtung dem Pflanzenkeim gegenüber geschieht.",
      "Da ist die sinnli­che Wesenheit unscheinbar in einer gewissen Beziehung; die übersinnliche dagegen ist vielgliedrig. Sie enthält alles, was an dem Aufbau und Wachstum der Pflanze aus der",
      "übersinnlichen Welt heraus mitarbeitet. - Bei der übersinn­lichen Beobachtung der ganzen Erde ergibt sich eine Kraftwesenheit, von welcher man ganz sicher wissen kann, sie war vorhanden, bevor alles dasjenige entstanden ist, was auf der Erde und innerhalb derselben sinnlich wahr­nehmbar ist. Man kommt auf diesem Wege dazu, die über­sinnlichen Kräfte vor sich zu erleben, welche in der Vor­zeit der Erde an derselben mitgearbeitet haben. Was man so erlebt, kann man ebenso die ätherischen oder elementa­rischen Grundwesenheiten oder Leiber der Pflanze und der Erde nennen, wie man den Leib, durch welchen man au­ßerhalb des physischen Leibes wahrnimmt, den eigenen elementarischen oder ätherischen Leib nennt.",
      "Schon im Beginne der übersinnlichen Beobachtungsfä­higkeit wird man gewissen Dingen und Vorgängen der Sinnenwelt außer ihren sinnlichen Eigenschaften noch sol­che elementarische Grundwesenheiten zuschreiben kön­nen. Man wird von einem ätherischen Leib der Pflanze oder der Erde sprechen. Doch sind die auf solche Art be­obachteten elementarischen Wesenheiten durchaus nicht die einzigen, welche sich dem übersinnlichen Erleben darbieten. Von dem elementarischen Leibe einer Pflanze wird man sagen, er gestaltet die Stoffe und Kräfte der Sinnenwelt und lebt sich dadurch in einem sinnlichen Leib aus. Doch kann man auch Wesenheiten beobachten, welche ein elementarisches Dasein führen, ohne sich in einem Sinnenleib auszuleben. Es gibt also für die übersinnliche Beob­achtung auch rein elementarische Wesenheiten. Man erlebt nicht etwa bloß zu der Sinnenwelt etwas hinzu; man er­lebt eine Welt, innerhalb welcher die Sinnenwelt sich dar­stellt, wie etwa Eisstücke im Wasser schwimmend. Wer",
      "nur das Eis sehen könnte und nicht das Wasser, dem wäre es möglich, nur dem Eise Wirklichkeit zuzugestehen, und nicht dem Wasser. Wer sich nur an das halten will, was sich durch die Sinne offenbart, der leugnet die übersinnli­che Welt, innerhalb welcher die Sinnenwelt ein Teil ist wie die im Wasser befindlichen Eisstücke ein Teil der ganzen Wassermasse.",
      "Man wird nun finden, daß diejenigen Menschen, welche übersinnliche Beobachtungen machen können, dasjenige, was sie schauen, so beschreiben, daß sie sich der Ausdrücke bedienen, welche den sinnlichen Empfindungen entlehnt sind. So kann man den elementarischen Leib eines Wesens der Sinnenwelt, oder ein rein elementarisches Wesen so beschrieben finden, daß gesagt wird, es offenbare sich als in sich geschlossener, mannigfaltig gefärbter Lichtleib. Es blitze in Farben auf, glimmere oder leuchte und lasse be­merken, daß diese Farben- oder Lichterscheinung seine Lebensäußerung sei. Wovon der Beobachter da eigentlich spricht, ist durchaus unsichtbar, und er ist sich dessen be­wußt, daß mit dem, was er wahrnimmt, das Licht- oder Farbenbild nichts anderes zu tun hat, als etwa die Schrift, in welcher eine Tatsache mitgeteilt wird, mit dieser Tat­sache selbst. Dennoch hat man nicht etwa bloß ein Übersinnliches in willkürlicher Art durch sinnliche Empfin­dungsvorstellungen ausgedrückt; sondern man hat wäh­rend der Beobachtung das Erlebnis wirklich gemacht, das einem Sinneseindruck ähnlich ist. Es kommt dies davon her, daß im übersinnlichen Erleben die Befreiung von dem sinnlichen Leibe keine vollkommene ist. Dieser lebt mit dem elementarischen Leibe doch noch mit und bringt das übersinnliche Erlebnis in eine sinnliche Form. Die Beschreibung,",
      "die man so gibt von einer elementarischen We­senheit, ist dann tatsächlich so gehalten, daß sie sich wie eine visionäre, oder phantastische Zusammenstellung von Sinneseindrücken zeigt. Wenn die Beschreibung so gege­ben wird, dann ist sie trotzdem die wahre Wiedergabe des Erlebten. Denn man hat geschaut, was man schildert. Der Fehler, der gemacht werden kann, liegt nicht darin, daß man das Bild als solches schildert. Es liegt ein Fehler erst dann vor, wenn man das Bild für die Wirklichkeit hält, und nicht dasjenige, auf was das Bild, als auf die ihm entspre­chende Wirklichkeit, hindeutet.",
      "Ein Mensch, welcher niemals Farben wahrgenommen hat - ein Blindgeborener - wird, wenn er sich die entspre­chende Fähigkeit erwirbt, elementarische Wesenheiten nicht so beschreiben, daß er sagt, sie blitzen als Farbener­scheinungen auf. Er wird sich derjenigen Empfindungs­vorstellungen zum Ausdrucke bedienen, welche ihm ge­wohnt sind. Für die Menschen aber, welche sinnlich sehen können, ist eine Schilderung durchaus geeignet, welche sich etwa des Ausdruckes bedient, es blitzte eine Farbengestalt au£ Sie können dadurch sich die Empfindung von dem bilden, was der Beobachter der elementarischen Welt geschaut hat. Und das gilt nicht etwa nur für Mitteilungen, welche ein Hellsichtiger - es sei ein Mensch so genannt, der durch seinen elementarischen Leib beobachten kann - einem Nicht-Hellsichtigen macht, sondern auch für die Verständigung der Hellsichtigen untereinander. In der Sin­nenwelt lebt der Mensch eben in seinem sinnlichen Leib, und dieser kleidet ihm die übersinnlichen Beobachtungen in Sinnesformen ein; daher ist innerhalb des menschlichen Erdenlebens der Ausdruck der übersinnlichen Beobachtungen",
      "durch die von ihnen erzeugten Sinnesbilder denn doch zunächst eine brauchbare Art der Mitteilung.",
      "Es kommt darauf an, daß derjenige, welcher eine solche Mitteilung empfängt, in seiner Seele ein Erlebnis hat, wel­ches zu der in Betracht kommenden Tatsache in dem rich­tigen Verhältnisse steht. Die sinnlichen Bilder werden nur mitgeteilt, damit durch sie etwas erlebt wird. So wie sie sich darbieten, können sie nicht in der Sinnenwelt vor­kommen. Das ist eben ihre Eigentümlichkeit. Und deswe­gen rufen sie auch Erlebnisse hervor, die sich auf nichts Sinnliches beziehen.",
      "Im Beginne seiner Hellsichtigkeit wird sich der Mensch nur schwer von dem Ausdruck des Sinnenbildes frei ma­chen. Bei weiter dringender Fähigkeit wird aber allerdings das Bedürfnis entstehen, mehr willkürliche Darstellungsmittel zur Mitteilung für das Geschaute zu ersinnen. Bei diesen ergibt sich dann immer die Notwendigkeit, erst die gewissen Zeichen, deren man sich bedient, zu erklären. Je mehr die Zeitkultur erfordert, daß die übersinnlichen Erkenntnisse allgemein bekanntgemacht werden, desto mehr wird sich das Bedürfnis herausstellen, diese Erkennt­nisse durch die Ausdrucksmittel des alltäglichen Lebens in der Sinnenwelt zu geben.",
      "Die übersinnlichen Erlebnisse können so auftreten, daß sie sich zu gewissen Zeiten einstellen. Sie überkommen dann den Menschen. Und dieser hat dann Gelegenheit, durch eigenes Erleben über die übersinnliche Welt etwas zu erfahren, in dem Maße, als er gewissermaßen von dieser mehr oder weniger oft dadurch begnadet wird, daß sie in sein gewöhnliches Seelenleben hineinleuchtet. Eine höhere Fähigkeit besteht aber darinnen, willkürlich hellseherische",
      "Beobachtung aus dem gewöhnlichen Seelenleben heraus herbeizuführen. Der Weg zur Erlangung dieser Fähigkeit ergibt sich im allgemeinen durch eine energische Fortset­zung der inneren Verstärkung des Seelenlebens. Doch hängt auch viel von der Erlangung einer gewissen Seelen­stimmung ab. Ein ruhiges, gelassenes Verhalten gegenüber der übersinnlichen Welt ist notwendig. Ein Verhalten, welches ebenso weit entfernt ist von dem brennenden Wunsch, möglichst viel und möglichst Deutliches zu er­fahren, wie andrerseits auch von der persönlichen Un­interessiertheit gegenüber dieser Welt. Der brennende Wunsch wirkt so, daß er vor das leibfreie Schauen etwas wie einen unsichtbaren Nebel breitet. Die Uninteressiert­heit verhält sich so, daß die übersinnlichen Dinge wirklich sich offenbaren, aber einfach nicht bemerkt werden. Diese Uninteressiertheit kommt zuweilen in einer ganz besonde­ren Form zum Ausdrucke. Es gibt Menschen, welche in der ehrlichsten Art Erlebnisse des Heilsehens haben möch­ten. Aber sie machen sich von vornherein eine ganz be­stimmte Vorstellung, wie diese sein müssen, wenn sie sie als echte anerkennen sollen. Und dann kommen wirkliche Erlebnisse; diese huschen jedoch vorbei, ohne daß ihnen Interesse entgegengebracht wird, weil sie eben nicht so sind, wie man sich vorgestellt hat, daß sie sein sollten.",
      "Bei der willkürlich herbeigeführten Helisichtigkeit kommt im Verlaufe der inneren Seelenbetätigung einmal der Augenblick, in dem man weiß: jetzt erlebt die Seele etwas, was sie vorher nicht erlebt hat. Das Erlebnis ist kein bestimmtes, sondern das allgemeine Gefühl, man stehe nicht der sinnlichen Außenwelt gegenüber, man sei nicht in ihr, jedoch man sei auch nicht in sich, wie man es",
      "im gewöhnlichen Seelenleben ist. Das äußere und das in­nere Erleben fließen in eins, in ein Lebensgefühl zusam­men, das bisher der Seele unbekannt war, und von dem sie weiß, sie könnte es nicht haben, wenn sie nur durch die Sinne mit der Außenwelt lebte, oder wenn sie in ihren ge­wöhnlichen Empfindungen und Erinnerungsvorstellungen lebte.",
      "Man empfindet dann weiter, daß sich in diesen Seelenzustand etwas aus einer bisher unbekannten Welt hereinschiebt. Aber man kann nicht zu einer Vorstellung von die­sem Unbekannten kommen. Man erlebt, aber man kann nicht vorstellen.",
      "Dagegen überkommt denjenigen, der sol­ches erlebt, das Gefühl, als ob er an seinem physisch-sinn­lichen Leibe ein Hindernis hätte, das vorzustellen, was sich in die Seele hereindrängt. Setzt man nun die innere Seelenanstrengung immer wieder fort, so wird man sich nach eini­ger Zeit wie den Überwinder seines Leibeswiderstandes fühlen.",
      "Der physische Verstandesapparat war bisher nur geeignet Vorstellungen zu bilden, welche sich an Erlebnisse in der Sinnenwelt anschließen. Er ist zunächst unfähig, das zur Vorstellung zu erheben, was aus der übersinnlichen Welt sich offenbaren will.",
      "Er muß erst so bearbeitet wer­den, daß er dies vermag. So wie das Kind die Außenwelt um sich hat, sein Verstandesapparat aber erst im Erleben an der Außenwelt zubereitet werden muß, um sich auch Vorstellungen über die Umgebung zu machen, so ist der Mensch im allgemeinen unfähig, die übersinnliche Welt vor­zustellen.",
      "Der angehende Hellseher vollzieht an seinem Vor­stellungsapparat dasselbe auf höherer Stufe, was sich im Kinde vollzieht. Er läßt seine verstärkten Gedanken auf die­sen Apparat wirken. Dadurch wird dieser allmählich umgebildet.",
      "Er wird imstande, die übersinnliche Welt in das Vorstellungsleben",
      "aufzunehmen. Man fühlt, wie man durch die Seelentätigkeit formend wirkt auf den eigenen Leib. Erst macht sich dieser als schwerer Gegendruck gegen das See­lenleben geltend; man fühlt ihn wie einen Fremdkörper in sich.",
      "Dann bemerkt man, wie er immer mehr sich anpaßt an das Seelen-Erleben; zuletzt fühlt man den Leib nicht mehr, aber man hat dafür vor sich die übersinnliche Welt, wie man das Auge nicht wahrnimmt, durch das man die Far­benwelt sieht. Der Leib muß unwahrnehmbar werden, be­vor die Seele die übersinnliche Welt erschauen kann.",
      "Hat man auf diese Art es dahin gebracht, die Seele willkürlich hell­seherisch zu machen, dann wird man in der Regel diesen Zustand immer wieder herbeiführen können, wenn man sich auf einen Gedanken konzentriert, den man besonders kraft­voll in sich erleben kann. Als Folge der Hingabe an diesen Gedanken wird man dann die Hellsichtigkeit herbeigeführt finden.",
      "Zunächst wird man noch nicht in der Lage sein, etwas ganz bestimmtes zu sehen, was man sehen will. Es werden in das Seelenleben übersinnliche Dinge oder Vorgänge her-einspielen, auf die man in keiner Art vorbereitet ist, und die man als solche nicht herbeiführen wollte.",
      "Doch gelangt man im weiteren Verfolg der inneren Anstrengung dazu, auch den geistigen Blick auf solche Dinge zu lenken, die man zu erkennen beabsichtigt. Wie man ein vergessenes Erlebnis ins Gedächtnis zu bringen sucht dadurch, daß man ein verwandtes sich in die Seele ruft, so kann man als Hell­seher von einem Erlebnis ausgehen, von dem man mit Recht glauben darf, daß es mit dem gesuchten in einem Ver­hältnis stehe.",
      "Wenn man sich an das Bekannte intensiv hin­gibt, so kommt oft nach längerer oder kürzerer Zeit dasje­nige hinzu, das man zu erleben beabsichtigt. Im allgemeinen",
      "ist aber zu beachten, daß für den Hellseher ein ruhiges Abwarten der günstigen Augenblicke von dem allergrößten Wert ist. Man soll nichts herbeiziehen wollen. Ergibt sich ein angestrebtes Erleben nicht, so ist es gut, vorläufig darauf zu verzichten und die Gelegenheit ein andres Mal wieder herbeizuführen. Der menschliche Erkenntnisappa­rat bedarf des ruhigen Heranreifens zu bestimmten Erleb­nissen. Wer nicht die Geduld hat, ein solches Reifen abzu­warten, der wird unrichtige oder ungenaue Beobachtungen machen."
    ],
    "sentences": [
      [
        "DRITTE MEDITATION"
      ],
      [
        "Der Meditierende versucht sich Vorstellungen zu bilden"
      ],
      [
        "über die hellsichtige Erkenntnis der elementarischen Welt"
      ],
      [
        "Man erlebt eine Welt, welche der Sinneswahrnehmung und dem gewöhnlichen Verstandesdenken unbekannt bleibt, wenn man nicht durch den sinnlichen Leib, sondern au­ßerhalb desselben durch den elementarischen Leib wahr­nimmt.",
        "Will man diese Welt mit etwas vergleichen, das dem gewöhnlichen Erleben angehört, so bietet sich die Welt der Erinnerungen, der Gedächtnisvorstellungen dar.",
        "Wie diese aus dem Innern der Seele aufsteigen, so ge­schieht es auch mit den übersinnlichen Erlebnissen des ele­mentarischen Leibes.",
        "Nur weiß die Seele bei einer Erinne­rungsvorstellung, daß sich diese auf ein früheres Erlebnis innerhalb der Sinnenwelt bezieht.",
        "Die übersinnliche Vor­stellung trägt ebenso eine Beziehung in sich.",
        "Wie sich die Erinnerungsvorstellung durch sich selbst als etwas ankün­digt, was man nicht als bloßes Phantasiegebilde bezeich­nen kann, so auch die übersinnliche Vorstellung.",
        "Sie ringt sich aus dem seelischen Erleben heraus, aber sie offenbart sich sogleich als ein inneres Erlebnis, welches sich auf et­was Äußeres bezieht.",
        "Durch die Erinnerungsvorstellung wird etwas in der Seele gegenwärtig, was man erlebt hat.",
        "Durch die übersinnliche Vorstellung wird inneres Seelenerlebnis, was irgendwann oder irgendwo in der übersinn­lichen Welt vorhanden ist.",
        "Es offenbart sich also durch die Wesenheit der übersinnlichen Vorstellungen selbst, daß man sie so ansehen kann wie sich innerlich erschließende Mitteilungen aus einer übersinnlichen Welt."
      ],
      [
        "Wie weit man kommt mit den Erlebnissen in der übersinnlichen"
      ],
      [
        "Welt auf diese Art, das hängt davon ab, wie energisch man die Verstärkung des Seelenlebens betreibt.",
        "Ob man bloß einen Begriff davon erhält, daß eine Pflanze nicht bloß dasjenige ist, was man innerhalb der Sinnen­welt wahrnimmt, oder ob man einen ähnlichen Begriff von der ganzen Erde erhält, das gehört beides dem gleichen Gebiete des übersinnlichen Erlebens an."
      ],
      [
        "Betrachtet derje­nige, welcher sich die Fähigkeit erworben hat, außerhalb seines sinnlichen Leibes wahrzunehmen, eine Pflanze, so kann er außer dem, was die Sinne an ihr zeigen, eine feine Gestalt wahrnehmen, welche die ganze Pflanze durch­dringt.",
        "Diese Gestalt bietet sich ihm als eine Kraftwesen­heit dar; und er kommt dazu, diese Kraftwesenheit als das­jenige anzusehen, was aus den Stoffen und Kräften der Sinnenwelt die Pflanze gestaltet, was den Umlauf ihrer Säfte bewirkt."
      ],
      [
        "Er kann sagen, wenn er einen brauchbaren, wenn auch nicht ganz zutreffenden Ausdruck anwenden will: in der Pflanze ist etwas, was die Säfte so in Umlauf bringt, wie meine eigene Seele meinen Arm hebt.",
        "Er blickt auf ein Inneres in der Pflanze."
      ],
      [
        "Und er muß diesem Inneren des Pflanzenwesens eine Selbständigkeit zugestehen gegen­über dem, was die Sinne an der Pflanze sehen.",
        "Er muß ihm auch zugestehen, daß es vor der sinnlichen Pflanze vorhan­den ist."
      ],
      [
        "Er gelangt dazu, zu beobachten, wie eine Pflanze wächst, verwelkt, Keime treibt, und wie aus den letztern eine neue Pflanze entsteht.",
        "Die übersinnliche Kraftgestalt ist besonders dann am mächtigsten, wenn die Beobachtung dem Pflanzenkeim gegenüber geschieht."
      ],
      [
        "Da ist die sinnli­che Wesenheit unscheinbar in einer gewissen Beziehung; die übersinnliche dagegen ist vielgliedrig.",
        "Sie enthält alles, was an dem Aufbau und Wachstum der Pflanze aus der"
      ],
      [
        "übersinnlichen Welt heraus mitarbeitet. - Bei der übersinn­lichen Beobachtung der ganzen Erde ergibt sich eine Kraftwesenheit, von welcher man ganz sicher wissen kann, sie war vorhanden, bevor alles dasjenige entstanden ist, was auf der Erde und innerhalb derselben sinnlich wahr­nehmbar ist.",
        "Man kommt auf diesem Wege dazu, die über­sinnlichen Kräfte vor sich zu erleben, welche in der Vor­zeit der Erde an derselben mitgearbeitet haben.",
        "Was man so erlebt, kann man ebenso die ätherischen oder elementa­rischen Grundwesenheiten oder Leiber der Pflanze und der Erde nennen, wie man den Leib, durch welchen man au­ßerhalb des physischen Leibes wahrnimmt, den eigenen elementarischen oder ätherischen Leib nennt."
      ],
      [
        "Schon im Beginne der übersinnlichen Beobachtungsfä­higkeit wird man gewissen Dingen und Vorgängen der Sinnenwelt außer ihren sinnlichen Eigenschaften noch sol­che elementarische Grundwesenheiten zuschreiben kön­nen.",
        "Man wird von einem ätherischen Leib der Pflanze oder der Erde sprechen.",
        "Doch sind die auf solche Art be­obachteten elementarischen Wesenheiten durchaus nicht die einzigen, welche sich dem übersinnlichen Erleben darbieten.",
        "Von dem elementarischen Leibe einer Pflanze wird man sagen, er gestaltet die Stoffe und Kräfte der Sinnenwelt und lebt sich dadurch in einem sinnlichen Leib aus.",
        "Doch kann man auch Wesenheiten beobachten, welche ein elementarisches Dasein führen, ohne sich in einem Sinnenleib auszuleben.",
        "Es gibt also für die übersinnliche Beob­achtung auch rein elementarische Wesenheiten.",
        "Man erlebt nicht etwa bloß zu der Sinnenwelt etwas hinzu; man er­lebt eine Welt, innerhalb welcher die Sinnenwelt sich dar­stellt, wie etwa Eisstücke im Wasser schwimmend."
      ],
      [
        "nur das Eis sehen könnte und nicht das Wasser, dem wäre es möglich, nur dem Eise Wirklichkeit zuzugestehen, und nicht dem Wasser.",
        "Wer sich nur an das halten will, was sich durch die Sinne offenbart, der leugnet die übersinnli­che Welt, innerhalb welcher die Sinnenwelt ein Teil ist wie die im Wasser befindlichen Eisstücke ein Teil der ganzen Wassermasse."
      ],
      [
        "Man wird nun finden, daß diejenigen Menschen, welche übersinnliche Beobachtungen machen können, dasjenige, was sie schauen, so beschreiben, daß sie sich der Ausdrücke bedienen, welche den sinnlichen Empfindungen entlehnt sind.",
        "So kann man den elementarischen Leib eines Wesens der Sinnenwelt, oder ein rein elementarisches Wesen so beschrieben finden, daß gesagt wird, es offenbare sich als in sich geschlossener, mannigfaltig gefärbter Lichtleib.",
        "Es blitze in Farben auf, glimmere oder leuchte und lasse be­merken, daß diese Farben- oder Lichterscheinung seine Lebensäußerung sei.",
        "Wovon der Beobachter da eigentlich spricht, ist durchaus unsichtbar, und er ist sich dessen be­wußt, daß mit dem, was er wahrnimmt, das Licht- oder Farbenbild nichts anderes zu tun hat, als etwa die Schrift, in welcher eine Tatsache mitgeteilt wird, mit dieser Tat­sache selbst.",
        "Dennoch hat man nicht etwa bloß ein Übersinnliches in willkürlicher Art durch sinnliche Empfin­dungsvorstellungen ausgedrückt; sondern man hat wäh­rend der Beobachtung das Erlebnis wirklich gemacht, das einem Sinneseindruck ähnlich ist.",
        "Es kommt dies davon her, daß im übersinnlichen Erleben die Befreiung von dem sinnlichen Leibe keine vollkommene ist.",
        "Dieser lebt mit dem elementarischen Leibe doch noch mit und bringt das übersinnliche Erlebnis in eine sinnliche Form.",
        "Die Beschreibung,"
      ],
      [
        "die man so gibt von einer elementarischen We­senheit, ist dann tatsächlich so gehalten, daß sie sich wie eine visionäre, oder phantastische Zusammenstellung von Sinneseindrücken zeigt.",
        "Wenn die Beschreibung so gege­ben wird, dann ist sie trotzdem die wahre Wiedergabe des Erlebten.",
        "Denn man hat geschaut, was man schildert.",
        "Der Fehler, der gemacht werden kann, liegt nicht darin, daß man das Bild als solches schildert.",
        "Es liegt ein Fehler erst dann vor, wenn man das Bild für die Wirklichkeit hält, und nicht dasjenige, auf was das Bild, als auf die ihm entspre­chende Wirklichkeit, hindeutet."
      ],
      [
        "Ein Mensch, welcher niemals Farben wahrgenommen hat - ein Blindgeborener - wird, wenn er sich die entspre­chende Fähigkeit erwirbt, elementarische Wesenheiten nicht so beschreiben, daß er sagt, sie blitzen als Farbener­scheinungen auf.",
        "Er wird sich derjenigen Empfindungs­vorstellungen zum Ausdrucke bedienen, welche ihm ge­wohnt sind.",
        "Für die Menschen aber, welche sinnlich sehen können, ist eine Schilderung durchaus geeignet, welche sich etwa des Ausdruckes bedient, es blitzte eine Farbengestalt au£ Sie können dadurch sich die Empfindung von dem bilden, was der Beobachter der elementarischen Welt geschaut hat.",
        "Und das gilt nicht etwa nur für Mitteilungen, welche ein Hellsichtiger - es sei ein Mensch so genannt, der durch seinen elementarischen Leib beobachten kann - einem Nicht-Hellsichtigen macht, sondern auch für die Verständigung der Hellsichtigen untereinander.",
        "In der Sin­nenwelt lebt der Mensch eben in seinem sinnlichen Leib, und dieser kleidet ihm die übersinnlichen Beobachtungen in Sinnesformen ein; daher ist innerhalb des menschlichen Erdenlebens der Ausdruck der übersinnlichen Beobachtungen"
      ],
      [
        "durch die von ihnen erzeugten Sinnesbilder denn doch zunächst eine brauchbare Art der Mitteilung."
      ],
      [
        "Es kommt darauf an, daß derjenige, welcher eine solche Mitteilung empfängt, in seiner Seele ein Erlebnis hat, wel­ches zu der in Betracht kommenden Tatsache in dem rich­tigen Verhältnisse steht.",
        "Die sinnlichen Bilder werden nur mitgeteilt, damit durch sie etwas erlebt wird.",
        "So wie sie sich darbieten, können sie nicht in der Sinnenwelt vor­kommen.",
        "Das ist eben ihre Eigentümlichkeit.",
        "Und deswe­gen rufen sie auch Erlebnisse hervor, die sich auf nichts Sinnliches beziehen."
      ],
      [
        "Im Beginne seiner Hellsichtigkeit wird sich der Mensch nur schwer von dem Ausdruck des Sinnenbildes frei ma­chen.",
        "Bei weiter dringender Fähigkeit wird aber allerdings das Bedürfnis entstehen, mehr willkürliche Darstellungsmittel zur Mitteilung für das Geschaute zu ersinnen.",
        "Bei diesen ergibt sich dann immer die Notwendigkeit, erst die gewissen Zeichen, deren man sich bedient, zu erklären.",
        "Je mehr die Zeitkultur erfordert, daß die übersinnlichen Erkenntnisse allgemein bekanntgemacht werden, desto mehr wird sich das Bedürfnis herausstellen, diese Erkennt­nisse durch die Ausdrucksmittel des alltäglichen Lebens in der Sinnenwelt zu geben."
      ],
      [
        "Die übersinnlichen Erlebnisse können so auftreten, daß sie sich zu gewissen Zeiten einstellen.",
        "Sie überkommen dann den Menschen.",
        "Und dieser hat dann Gelegenheit, durch eigenes Erleben über die übersinnliche Welt etwas zu erfahren, in dem Maße, als er gewissermaßen von dieser mehr oder weniger oft dadurch begnadet wird, daß sie in sein gewöhnliches Seelenleben hineinleuchtet.",
        "Eine höhere Fähigkeit besteht aber darinnen, willkürlich hellseherische"
      ],
      [
        "Beobachtung aus dem gewöhnlichen Seelenleben heraus herbeizuführen.",
        "Der Weg zur Erlangung dieser Fähigkeit ergibt sich im allgemeinen durch eine energische Fortset­zung der inneren Verstärkung des Seelenlebens.",
        "Doch hängt auch viel von der Erlangung einer gewissen Seelen­stimmung ab.",
        "Ein ruhiges, gelassenes Verhalten gegenüber der übersinnlichen Welt ist notwendig.",
        "Ein Verhalten, welches ebenso weit entfernt ist von dem brennenden Wunsch, möglichst viel und möglichst Deutliches zu er­fahren, wie andrerseits auch von der persönlichen Un­interessiertheit gegenüber dieser Welt.",
        "Der brennende Wunsch wirkt so, daß er vor das leibfreie Schauen etwas wie einen unsichtbaren Nebel breitet.",
        "Die Uninteressiert­heit verhält sich so, daß die übersinnlichen Dinge wirklich sich offenbaren, aber einfach nicht bemerkt werden.",
        "Diese Uninteressiertheit kommt zuweilen in einer ganz besonde­ren Form zum Ausdrucke.",
        "Es gibt Menschen, welche in der ehrlichsten Art Erlebnisse des Heilsehens haben möch­ten.",
        "Aber sie machen sich von vornherein eine ganz be­stimmte Vorstellung, wie diese sein müssen, wenn sie sie als echte anerkennen sollen.",
        "Und dann kommen wirkliche Erlebnisse; diese huschen jedoch vorbei, ohne daß ihnen Interesse entgegengebracht wird, weil sie eben nicht so sind, wie man sich vorgestellt hat, daß sie sein sollten."
      ],
      [
        "Bei der willkürlich herbeigeführten Helisichtigkeit kommt im Verlaufe der inneren Seelenbetätigung einmal der Augenblick, in dem man weiß: jetzt erlebt die Seele etwas, was sie vorher nicht erlebt hat.",
        "Das Erlebnis ist kein bestimmtes, sondern das allgemeine Gefühl, man stehe nicht der sinnlichen Außenwelt gegenüber, man sei nicht in ihr, jedoch man sei auch nicht in sich, wie man es"
      ],
      [
        "im gewöhnlichen Seelenleben ist.",
        "Das äußere und das in­nere Erleben fließen in eins, in ein Lebensgefühl zusam­men, das bisher der Seele unbekannt war, und von dem sie weiß, sie könnte es nicht haben, wenn sie nur durch die Sinne mit der Außenwelt lebte, oder wenn sie in ihren ge­wöhnlichen Empfindungen und Erinnerungsvorstellungen lebte."
      ],
      [
        "Man empfindet dann weiter, daß sich in diesen Seelenzustand etwas aus einer bisher unbekannten Welt hereinschiebt.",
        "Aber man kann nicht zu einer Vorstellung von die­sem Unbekannten kommen.",
        "Man erlebt, aber man kann nicht vorstellen."
      ],
      [
        "Dagegen überkommt denjenigen, der sol­ches erlebt, das Gefühl, als ob er an seinem physisch-sinn­lichen Leibe ein Hindernis hätte, das vorzustellen, was sich in die Seele hereindrängt.",
        "Setzt man nun die innere Seelenanstrengung immer wieder fort, so wird man sich nach eini­ger Zeit wie den Überwinder seines Leibeswiderstandes fühlen."
      ],
      [
        "Der physische Verstandesapparat war bisher nur geeignet Vorstellungen zu bilden, welche sich an Erlebnisse in der Sinnenwelt anschließen.",
        "Er ist zunächst unfähig, das zur Vorstellung zu erheben, was aus der übersinnlichen Welt sich offenbaren will."
      ],
      [
        "Er muß erst so bearbeitet wer­den, daß er dies vermag.",
        "So wie das Kind die Außenwelt um sich hat, sein Verstandesapparat aber erst im Erleben an der Außenwelt zubereitet werden muß, um sich auch Vorstellungen über die Umgebung zu machen, so ist der Mensch im allgemeinen unfähig, die übersinnliche Welt vor­zustellen."
      ],
      [
        "Der angehende Hellseher vollzieht an seinem Vor­stellungsapparat dasselbe auf höherer Stufe, was sich im Kinde vollzieht.",
        "Er läßt seine verstärkten Gedanken auf die­sen Apparat wirken.",
        "Dadurch wird dieser allmählich umgebildet."
      ],
      [
        "Er wird imstande, die übersinnliche Welt in das Vorstellungsleben"
      ],
      [
        "aufzunehmen.",
        "Man fühlt, wie man durch die Seelentätigkeit formend wirkt auf den eigenen Leib.",
        "Erst macht sich dieser als schwerer Gegendruck gegen das See­lenleben geltend; man fühlt ihn wie einen Fremdkörper in sich."
      ],
      [
        "Dann bemerkt man, wie er immer mehr sich anpaßt an das Seelen-Erleben; zuletzt fühlt man den Leib nicht mehr, aber man hat dafür vor sich die übersinnliche Welt, wie man das Auge nicht wahrnimmt, durch das man die Far­benwelt sieht.",
        "Der Leib muß unwahrnehmbar werden, be­vor die Seele die übersinnliche Welt erschauen kann."
      ],
      [
        "Hat man auf diese Art es dahin gebracht, die Seele willkürlich hell­seherisch zu machen, dann wird man in der Regel diesen Zustand immer wieder herbeiführen können, wenn man sich auf einen Gedanken konzentriert, den man besonders kraft­voll in sich erleben kann.",
        "Als Folge der Hingabe an diesen Gedanken wird man dann die Hellsichtigkeit herbeigeführt finden."
      ],
      [
        "Zunächst wird man noch nicht in der Lage sein, etwas ganz bestimmtes zu sehen, was man sehen will.",
        "Es werden in das Seelenleben übersinnliche Dinge oder Vorgänge her-einspielen, auf die man in keiner Art vorbereitet ist, und die man als solche nicht herbeiführen wollte."
      ],
      [
        "Doch gelangt man im weiteren Verfolg der inneren Anstrengung dazu, auch den geistigen Blick auf solche Dinge zu lenken, die man zu erkennen beabsichtigt.",
        "Wie man ein vergessenes Erlebnis ins Gedächtnis zu bringen sucht dadurch, daß man ein verwandtes sich in die Seele ruft, so kann man als Hell­seher von einem Erlebnis ausgehen, von dem man mit Recht glauben darf, daß es mit dem gesuchten in einem Ver­hältnis stehe."
      ],
      [
        "Wenn man sich an das Bekannte intensiv hin­gibt, so kommt oft nach längerer oder kürzerer Zeit dasje­nige hinzu, das man zu erleben beabsichtigt.",
        "Im allgemeinen"
      ],
      [
        "ist aber zu beachten, daß für den Hellseher ein ruhiges Abwarten der günstigen Augenblicke von dem allergrößten Wert ist.",
        "Man soll nichts herbeiziehen wollen.",
        "Ergibt sich ein angestrebtes Erleben nicht, so ist es gut, vorläufig darauf zu verzichten und die Gelegenheit ein andres Mal wieder herbeizuführen.",
        "Der menschliche Erkenntnisappa­rat bedarf des ruhigen Heranreifens zu bestimmten Erleb­nissen.",
        "Wer nicht die Geduld hat, ein solches Reifen abzu­warten, der wird unrichtige oder ungenaue Beobachtungen machen."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "VIERTE MEDITATION",
    "paragraphs": [
      "VIERTE MEDITATION",
      "Der    Meditierende versucht eine Vorstellung von",
      "dem «Hüter der Schwelle » zu bilden",
      "Wenn die Seele zu der Fähigkeit gekommen ist, außerhalb des Sinnenleibes etwas zu beobachten, können für sie ge­wisse Schwierigkeiten des Gefühlslebens eintreten. Sie kann sich gezwungen sehen, eine ganz andre Stellung zu sich selbst einzunehmen, als sie vorher gewohnt war. Der Sin­nenwelt stand sie so gegenüber, daß sie dieselbe als Außen­welt ansah und die Erlebnisse des Innern als ihr Eigentum. Zur übersinnlichen Außenwelt kann sie sich nicht in dieser Art verhalten. Sobald sie diese Außenwelt wahrnimmt, fließt sie gewissermaßen mit ihr zusammen; sie kann sich nicht so von ihr abgetrennt vorstellen wie von der sinnli­chen Außenwelt. Dadurch nimmt alles, was sie dieser über­sinnlichen Außenwelt gegenüber als die eigene Innenwelt bezeichnen kann, eine gewisse Eigentümlichkeit an, wel­che zunächst schwer mit den Vorstellungen von Innerlich­keit zu vereinigen ist. Man kann nicht mehr sagen: ich den­ke, ich fühle, oder ich habe meine Gedanken und gestalte sie. Man muß sagen: etwas denkt in mir, etwas läßt in mir Gefühle aufleuchten, etwas gestaltet die Gedanken, so daß sie in einer ganz bestimmten Art auftreten und im Bewußt­sein sich als anwesend zeigen.",
      "Dieses Gefühl kann nun etwas außerordentlich Bedrük­kendes dann haben, wenn die Art des übersinnlichen Erle­bens sich als eine solche erweist, die Gewißheit darüber gibt, daß man richtig eine Wirklichkeit erlebt, und sich nicht einer Phantasterei oder Illusion hingibt. So wie es auf­tritt, kann es zeigen, daß sich die übersinnliche Außenwelt",
      "wohl erfühlen, sich denken will; daß sie aber an dem, was sie zustande bringen will, gehindert wird. Zugleich erhält man die Empfindung, daß dasjenige, was da in die Seele herein will, die wahre Wirklichkeit ist, und daß sie allein über das aufklären kann, was man bisher als Wirklichkeit erlebt hat. Auch die Form nimmt diese Empfindung an, daß die übersinnliche Wirklichkeit sich als etwas zeigt, was die bisher der Seele bekannte Wirklichkeit an Wert unend­lich überstrahlt. Es hat diese Empfindung deshalb etwas Bedrückendes, weil man zu dem Gedanken kommt, den nächsten Schritt, welchen man nun zu machen hat, muß man wollen. Es liegt in der Wesenheit dessen, was man durch sein inneres Erleben geworden ist, diesen Schritt zu machen. Wie eine Verleugnung dessen, was man ist, ja wie eine Selbstvernichtung müßte man es empfinden, wenn man den Schritt nicht täte. Und doch kann auch das Gefühl auf­treten, man kann ihn nicht tun, oder wenn man ihn unter­nimmt, so wie es möglich ist, so bleibt er unvollkommen.",
      "Das alles verwandelt sich in die Vorstellung: so wie die Seele nunmehr ist, so liegt vor ihr eine Aufgabe, die sie nicht bewältigen kann, weil sie so, wie sie ist, von der über­sinnlichen Außenwelt nicht aufgenommen wird, weil diese sie nicht in sich haben will. So kommt die Seele dazu, sich im Gegensatze zur übersinnlichen Welt zu fühlen, sie muß sich sagen, du bist nicht so, wie du mit dieser Welt zusam­menfließen kannst. Sie aber kann dir nur die wahre Wirk­lichkeit zeigen, und auch, wie du selbst zu dieser wahren Wirklichkeit dich verhältst; du hast dich also von dem ech­ten Beobachten des Wahren abgetrennt. Dieses Gefühl be-deutet eine Erfahrung, welche immer mehr über den gan­zen Wert der eigenen Seele entscheidend wird. Man fühlt",
      "sich mit seinem vollen Leben in einem Irrtum drinnen ste­hend. Doch unterscheidet sich dieser Irrtum von anderen Irrtümern. Diese werden gedacht, er aber wird erlebt. Ein Irrtum, der gedacht ist, wird weggeschafft, wenn man an die Stelle des unrichtigen Gedankens den richtigen setzt. Der erlebte Irrtum ist ein Teil des Seelenlebens selbst ge­worden; man ist der Irrtum; man kann ihn nicht einfach verbessern, denn man mag denken, wie man will, er ist da, er ist ein Teil der Wirklichkeit, und zwar der eigenen Wirk­lichkeit. Ein solches Erlebnis hat etwas Vernichtendes für das eigene Selbst. Man empfindet seine Innerlichkeit schmerzvoll zurückgestoßen von allem, was man ersehnt. Dieser Schmerz, der auf einer Stufe der Seelenwanderschaft empfunden wird, überragt weit alles, was man an Schmer­zen in der Sinnenwelt empfinden kann. Und deshalb kann er auch alles das überragen, dem man durch das bisherige Seelenleben gewachsen ist. Er kann etwas Betäubendes ha­ben. Die Seele steht vor der bangen Frage, woher soll ich die Kräfte nehmen, um zu ertragen, was mir da auferlegt ist? Und sie muß innerhalb ihres eigenen Lebens diese Kräfte finden. Sie bestehen in etwas, das man als inneren Mut, als innere Furchtlosigkeit bezeichnen kann.",
      "Um nun weiter in der Seelenwanderschaft zu kommen, muß man dazu geführt werden, daß aus dem Innern solche Kräfte des Ertragens seiner Erlebnisse sich erschließen, die inneren Mut und innere Furchtlosigkeit ergeben, wie man sie zum Leben innerhalb des Sinnenleibes nicht nötig hatte. Solche Kräfte ergeben sich nur durch wahre Selbsterkennt­nis. Man sieht im Grunde auf dieser Stufe der Entwickelung erst ein, wie wenig man bisher von sich wirklich gewußt hat. Man überließ sich dem inneren Erleben, ohne dieses",
      "etwa so zu betrachten, wie man einen Teil der Außenwelt betrachtet. Man erhält aber durch die Schritte, welche zur Fähigkeit geführt haben, außerhalb des Leibes zu erleben, besondere Mittel zur Selbsterkenntnis. Man lernt sich ge­wissermaßen von einem Gesichtspunkt aus betrachten, der sich nur ergibt, wenn man außerhalb des sinnlichen Leibes ist. Und es ist das geschilderte bedrückende Gefühl selbst schon der Anfang wahrer Selbsterkenntnis. Sich in einem Irrtum erleben in seinem Verhältnis zur Außenwelt, das zeigt ja das eigene Seelenwesen, wie es wirklich ist.",
      "Nun liegt es in der Natur der Menschenseele, solche Aufklärung über sich selbst als peinvoll zu empfinden. Man er­fährt erst, wenn man diese Pein empfindet, wie stark die ganz selbstverständliche Sehnsucht ist, sich als Menschen, so wie man ist, als wertvoll, als bedeutungsvoll zu halten. Es mag häßlich aussehen, daß dies so ist; man muß sich dieser Häßlichkeit des eigenen Selbstes frei gegenüberstellen. Man empfand diese Häßlichkeit vorher eben aus dem Grunde nicht, weil man nie mit seinem Bewußtsein in die eigene Wesenheit wirklich eingedrungen ist. Man bemerkt erst in einem solchen Augenblicke, wie man an sich liebt, was man nun als häßlich empfinden soll. Die Gewalt der Eigenliebe zeigt sich in ihrer vollen Größe. Und zugleich zeigt sich, wie wenig Neigung man hat, diese Eigenliebe abzulegen. Wenn es sich um die Eigenschaften der Seele handelt, die für das gewöhnliche Leben, für das Verhältnis zu andern Menschen in Betracht kommen, so stellt sich die Schwierigkeit schon als groß genug heraus. Man erfährt durch wahre Selbsterkenntnis zum Beispiel, daß man bis­her geglaubt hat, man stünde einem Menschen wohlwol­lend gegenüber, und daß man doch in den Seelengründen",
      "verborgenen Neid, oder Haß, oder ähnliches hegt. Man er­kennt, daß diese bisher nicht zutage getretenen Gefühle sich ganz gewiß einmal werden äußern wollen. Und man wird gewahr, daß es ganz oberflächlich wäre, sich zu sagen:",
      "nun hast du doch erkannt, daß es so mit dir stehe, vertilge also in dir den Neid, den Haß. Man entdeckt aber, daß man mit einem solchen Gedanken ganz gewiß einmal sich recht schwach erweisen werde, wenn der Drang, den Haß zu be­friedigen, den Neid auszuleben, wie mit Naturgewalt aus der Seele hervorbrechen werden. Solche besonderen Selbsterkenntnisse treten bei diesem oder jenem Menschen je nach der Beschaffenheit seines Seelenwesens au£ Sie stellen sich ein, wenn Erleben außerhalb des Sinnenleibes eintritt, weil dann die Selbsterkenntnis eben eine wahre wird, und nicht mehr getrübt sein kann von dem Wunsche, sich in der einen oder anderen Art zu finden, wie man es doch nur liebt, zu sein.",
      "Diese besonderen Selbsterkenntnisse sind schmerzvoll, sind bedrückend für die Seele. Derjenige, der sich die Fä­higkeit erwerben will, außerhalb des Leibes zu erleben, kann sie nicht vermeiden. Denn sie treten notwendig auf durch das ganz besondere Verhältnis, in das er sich zu der eigenen Seele stellen muß. Doch der stärksten Seelenkräfte bedarf es, wenn es sich um eine ganz allgemeine menschli­che Selbsterkenntnis handelt. Man beobachtet sich von ei­nem Gesichtspunkte, der außerhalb des bisherigen Seelen­lebens liegt. Man sagt zu sich selber: du hast nach deiner menschlichen Wesenheit die Dinge und Vorgänge der Welt betrachtet und über sie geurteilt. Versuche dir einmal vor­zustellen, du könntest sie nicht so betrachten, nicht so über sie urteilen. Dann wärest du überhaupt nicht das, was du",
      "bist. Du hättest keine inneren Erlebnisse. Du selbst wärest ein Nichts. So zu sich sagen, muß nicht etwa nur der Mensch, der im Alltagsleben drinnen steht, und sich nur selten einmal Vorstellungen über die Welt und das Leben macht.",
      "So muß jeder Wissenschafter, jeder Philosoph sa­gen. Denn auch Philosophie ist nur eine Beobachtung und Beurteilung der Welt nach Maßgabe der Eigenschaften des menschlichen Seelenlebens. Eine solche Beurteilung kann aber mit der übersinnlichen Außenwelt nicht zusammenfließen.",
      "Sie wird von derselben zurückgewiesen. Damit wird aber alles zurückgewiesen, was man bisher gewesen ist. Man sieht auf seine ganze Seele, auf sein «Ich» als auf etwas zurück, was man ablegen muß, wenn man die über­sinnliche Welt betreten will. - Nun kann aber die Seele gar nicht anders, als dieses «Ich» für ihre eigentliche Wesen­heit halten, bevor sie die übersinnliche Welt betritt.",
      "Sie muß in ihr die wahre menschliche Wesenheit sehen. Sie muß sich sagen: durch dieses mein Ich muß ich mir Vorstellungen über die Welt machen; dieses mein Ich darf ich nicht verlieren, wenn ich mich nicht als Wesenheit selbst ver­loren geben will.",
      "Der stärkste Trieb ist in ihr, das Ich sich überall zu wahren, um nicht allen Boden unter den Füßen zu verlieren. Was so die Seele im gewöhnlichen Leben berech­tigt empfinden muß, das darf sie nicht mehr empfinden, so­bald sie in die übersinnliche Außenwelt eintritt.",
      "Sie muß da eine Schwelle überschreiten, an der sie nicht den einen oder anderen wertvollen Besitz nur, an welcher sie das zurücklas­sen muß, was sie sich bisher selbst war. Sie muß sich sagen können, was dir bisher als deine stärkste Wahrheit zu gel­ten hatte, das muß nun jenseits der Schwelle zur übersinn­lichen Welt dir als der stärkste Irrtum erscheinen können.",
      "Gegenüber einer solchen Forderung kann die Seele zu­rückschaudern. Sie kann, was sie zu tun hätte, so stark als ein Hingeben, eine Nichtigkeitserklärung der eigenen We­senheit empfinden, daß sie an der bezeichneten Schwelle sich mehr oder weniger die eigne Ohnmacht eingesteht, der Forderung zu genügen. Dieses Eingeständnis kann alle möglichen Formen annehmen. Es kann ganz instinktiv auf­treten, und dem Menschen, der in seinem Sinne denkt und handelt, als etwas ganz anderes erscheinen, als es wirklich ist. Er kann zum Beispiel eine tiefe Abneigung gegen alle übersinnlichen Wahrheiten empfinden. Er kann sie für Träumereien, Phantastereien halten. Er tut dies nur aus dem Grunde, weil er in seinen ihm selbst unbekannten See­lengründen eine geheime Furcht vor diesen Wahrheiten hat. Er empfindet, daß er nur mit dem leben kann, was die Sinne und das Verstandesurteil offenbaren. Er vermeidet es deshalb, an die Schwelle zur übersinnlichen Welt heranzu­kommen. Er kleidet sich dieses Vermeiden so ein, daß er sagt, was jenseits dieser Schwelle liegen soll, ist vor Ver­nunft und Wissenschaft nicht haltbar. Es handelt sich aber doch nur darum, daß er Vernunft und Wissenschaft, wie er sie kennt, liebt, weil sie an sein Ich gebunden sind. Es han­delt sich um eine ganz allgemein menschliche Form von Ei­genliebe. Diese aber kann in die übersinnliche Welt nicht mit hineingenommen werden.",
      "Es kann aber auch der Fall eintreten, daß es bei diesem instinktiven Haltmachen vor der Schwelle nicht bleibt. Daß der Mensch bewußt bis zu ihr herantritt, und dann umkehrt, weil er Furcht empfindet vor dem, was ihm bevor­steht. Er wird dann nicht leicht die Wirkungen verwischen können, welche durch sein Herantreten an die Schwelle sich",
      "für sein gewöhnliches Seelenleben einstellen. Diese werden in den Folgen liegen, welche die Ohnmacht, die er empfun­den hat, über sein ganzes Seelensein ausbreitet.",
      "Was eintreten soll, besteht darin, daß der Mensch sich fähig mache, das, was er im gewöhnlichen Leben als stärk­ste Wahrheit empfindet, beim Betreten der übersinnlichen Welt abzulegen und sich auf eine andere Art einzurichten, die Dinge zu empfinden und zu beurteilen. Er muß nur sich auch klar darüber sein, daß er, wenn er wieder der Sinnenwelt gegenübersteht, auch wieder die für diese gültige Empfindungs- und Beurteilungsart gebrauchen muß. Er muß nicht nur lernen, in zwei Welten zu leben, sondern auch in beiden auf ganz verschiedene Art zu leben. Er darf sich für das gewöhnliche Stehen in der Sinnes- und Verstandeswelt das gesunde Urteil nicht beeinträchtigen, weil er für eine andre Welt zur Anwendung einer andren Urteilsart ge­zwungen ist.",
      "Für die menschliche Wesenheit ist eine solche Stellung­nahme schwierig. Die Fähigkeit für sie erlangt man nur durch fortgesetzte energische und geduldige Verstärkung des Seelenlebens. Wer die Erfahrungen an der Schwelle macht, der empfindet, daß es für das gewöhnliche mensch­liche Seelenleben eine Wohltat ist, nicht bis zu dieser Schwelle hingeführt zu werden. Die Empfindungen, wel­che in ihm auftreten, sind so, daß man gar nicht anders kann, als diese Wohltat von einer wesenhaften Macht herrührend zu denken, welche den Menschen schützt vor der Gefahr, die Schrecken der Selbstvernichtung an der Schwel­le zu erleben. - Es liegt hinter der Außenwelt, welche dem gewöhnlichen Leben gegeben ist, eine andre. Vor deren Schwelle steht ein strenger Hüter, welcher bewirkt, daß der",
      "Mensch nichts erfährt von dem, was Gesetze der übersinnlichen Welt sind. Denn alle Zweifel, alle Ungewißheit über diese Welt sind doch noch leichter zu ertragen, als das Schauen dessen, was man zurücklassen muß, wenn man sie betreten will.",
      "Der Mensch bleibt geschützt vor den geschilderten Erleb­nissen, solange er nicht an diese Schwelle selbst herantritt. Daß er Erzählungen von ihren Erlebnissen von denen ent­gegennimmt, welche diese Schwelle betreten oder über­schritten haben, das ändert nichts daran, daß er geschützt ist. Dagegen kann ihm solche Entgegennahme dienen im guten Sinne, wenn er sich der Schwelle nähert. Es ist auch in diesem Falle so wie in vielen andern, daß eine Verrich­tung besser vollzogen wird, wenn man vorher schon eine Vorstellung von ihr sich machen kann, als im entgegenge­setzten Falle. An dem aber, was der Wanderer in die über­sinnliche Welt an Selbsterkenntnis gewinnen soll, wird durch solches Vorherwis sen nichts geändert. Es ist deshalb nicht den Tatsachen entsprechend, wenn manche hellsich­tige oder mit dem Wesen der Hellsichtigkeit vertraute Per­sonen behaupten, von solchen Dingen solle überhaupt im Kreise von Menschen nicht gesprochen werden, die nicht vor dem Entschlusse unmittelbar stehen, sich in die über­sinnliche Welt selbst hineinzubegeben. Wir leben gegen­wärtig in einer Zeit, in welcher die Menschen immer mehr mit dem Wesen der übersinnlichen Welt bekannt werden müssen, wenn sie den Forderungen des Lebens seelisch ge­wachsen sein wollen. Die Verbreitung der übersinnlichen Erkenntnisse und somit auch derjenigen vom Hüter der Schwelle gehört zu den Aufgaben der Gegenwart und der nächsten Zukunft."
    ],
    "sentences": [
      [
        "VIERTE MEDITATION"
      ],
      [
        "Der Meditierende versucht eine Vorstellung von"
      ],
      [
        "dem «Hüter der Schwelle » zu bilden"
      ],
      [
        "Wenn die Seele zu der Fähigkeit gekommen ist, außerhalb des Sinnenleibes etwas zu beobachten, können für sie ge­wisse Schwierigkeiten des Gefühlslebens eintreten.",
        "Sie kann sich gezwungen sehen, eine ganz andre Stellung zu sich selbst einzunehmen, als sie vorher gewohnt war.",
        "Der Sin­nenwelt stand sie so gegenüber, daß sie dieselbe als Außen­welt ansah und die Erlebnisse des Innern als ihr Eigentum.",
        "Zur übersinnlichen Außenwelt kann sie sich nicht in dieser Art verhalten.",
        "Sobald sie diese Außenwelt wahrnimmt, fließt sie gewissermaßen mit ihr zusammen; sie kann sich nicht so von ihr abgetrennt vorstellen wie von der sinnli­chen Außenwelt.",
        "Dadurch nimmt alles, was sie dieser über­sinnlichen Außenwelt gegenüber als die eigene Innenwelt bezeichnen kann, eine gewisse Eigentümlichkeit an, wel­che zunächst schwer mit den Vorstellungen von Innerlich­keit zu vereinigen ist.",
        "Man kann nicht mehr sagen: ich den­ke, ich fühle, oder ich habe meine Gedanken und gestalte sie.",
        "Man muß sagen: etwas denkt in mir, etwas läßt in mir Gefühle aufleuchten, etwas gestaltet die Gedanken, so daß sie in einer ganz bestimmten Art auftreten und im Bewußt­sein sich als anwesend zeigen."
      ],
      [
        "Dieses Gefühl kann nun etwas außerordentlich Bedrük­kendes dann haben, wenn die Art des übersinnlichen Erle­bens sich als eine solche erweist, die Gewißheit darüber gibt, daß man richtig eine Wirklichkeit erlebt, und sich nicht einer Phantasterei oder Illusion hingibt.",
        "So wie es auf­tritt, kann es zeigen, daß sich die übersinnliche Außenwelt"
      ],
      [
        "wohl erfühlen, sich denken will; daß sie aber an dem, was sie zustande bringen will, gehindert wird.",
        "Zugleich erhält man die Empfindung, daß dasjenige, was da in die Seele herein will, die wahre Wirklichkeit ist, und daß sie allein über das aufklären kann, was man bisher als Wirklichkeit erlebt hat.",
        "Auch die Form nimmt diese Empfindung an, daß die übersinnliche Wirklichkeit sich als etwas zeigt, was die bisher der Seele bekannte Wirklichkeit an Wert unend­lich überstrahlt.",
        "Es hat diese Empfindung deshalb etwas Bedrückendes, weil man zu dem Gedanken kommt, den nächsten Schritt, welchen man nun zu machen hat, muß man wollen.",
        "Es liegt in der Wesenheit dessen, was man durch sein inneres Erleben geworden ist, diesen Schritt zu machen.",
        "Wie eine Verleugnung dessen, was man ist, ja wie eine Selbstvernichtung müßte man es empfinden, wenn man den Schritt nicht täte.",
        "Und doch kann auch das Gefühl auf­treten, man kann ihn nicht tun, oder wenn man ihn unter­nimmt, so wie es möglich ist, so bleibt er unvollkommen."
      ],
      [
        "Das alles verwandelt sich in die Vorstellung: so wie die Seele nunmehr ist, so liegt vor ihr eine Aufgabe, die sie nicht bewältigen kann, weil sie so, wie sie ist, von der über­sinnlichen Außenwelt nicht aufgenommen wird, weil diese sie nicht in sich haben will.",
        "So kommt die Seele dazu, sich im Gegensatze zur übersinnlichen Welt zu fühlen, sie muß sich sagen, du bist nicht so, wie du mit dieser Welt zusam­menfließen kannst.",
        "Sie aber kann dir nur die wahre Wirk­lichkeit zeigen, und auch, wie du selbst zu dieser wahren Wirklichkeit dich verhältst; du hast dich also von dem ech­ten Beobachten des Wahren abgetrennt.",
        "Dieses Gefühl be-deutet eine Erfahrung, welche immer mehr über den gan­zen Wert der eigenen Seele entscheidend wird.",
        "Man fühlt"
      ],
      [
        "sich mit seinem vollen Leben in einem Irrtum drinnen ste­hend.",
        "Doch unterscheidet sich dieser Irrtum von anderen Irrtümern.",
        "Diese werden gedacht, er aber wird erlebt.",
        "Ein Irrtum, der gedacht ist, wird weggeschafft, wenn man an die Stelle des unrichtigen Gedankens den richtigen setzt.",
        "Der erlebte Irrtum ist ein Teil des Seelenlebens selbst ge­worden; man ist der Irrtum; man kann ihn nicht einfach verbessern, denn man mag denken, wie man will, er ist da, er ist ein Teil der Wirklichkeit, und zwar der eigenen Wirk­lichkeit.",
        "Ein solches Erlebnis hat etwas Vernichtendes für das eigene Selbst.",
        "Man empfindet seine Innerlichkeit schmerzvoll zurückgestoßen von allem, was man ersehnt.",
        "Dieser Schmerz, der auf einer Stufe der Seelenwanderschaft empfunden wird, überragt weit alles, was man an Schmer­zen in der Sinnenwelt empfinden kann.",
        "Und deshalb kann er auch alles das überragen, dem man durch das bisherige Seelenleben gewachsen ist.",
        "Er kann etwas Betäubendes ha­ben.",
        "Die Seele steht vor der bangen Frage, woher soll ich die Kräfte nehmen, um zu ertragen, was mir da auferlegt ist?",
        "Und sie muß innerhalb ihres eigenen Lebens diese Kräfte finden.",
        "Sie bestehen in etwas, das man als inneren Mut, als innere Furchtlosigkeit bezeichnen kann."
      ],
      [
        "Um nun weiter in der Seelenwanderschaft zu kommen, muß man dazu geführt werden, daß aus dem Innern solche Kräfte des Ertragens seiner Erlebnisse sich erschließen, die inneren Mut und innere Furchtlosigkeit ergeben, wie man sie zum Leben innerhalb des Sinnenleibes nicht nötig hatte.",
        "Solche Kräfte ergeben sich nur durch wahre Selbsterkennt­nis.",
        "Man sieht im Grunde auf dieser Stufe der Entwickelung erst ein, wie wenig man bisher von sich wirklich gewußt hat.",
        "Man überließ sich dem inneren Erleben, ohne dieses"
      ],
      [
        "etwa so zu betrachten, wie man einen Teil der Außenwelt betrachtet.",
        "Man erhält aber durch die Schritte, welche zur Fähigkeit geführt haben, außerhalb des Leibes zu erleben, besondere Mittel zur Selbsterkenntnis.",
        "Man lernt sich ge­wissermaßen von einem Gesichtspunkt aus betrachten, der sich nur ergibt, wenn man außerhalb des sinnlichen Leibes ist.",
        "Und es ist das geschilderte bedrückende Gefühl selbst schon der Anfang wahrer Selbsterkenntnis.",
        "Sich in einem Irrtum erleben in seinem Verhältnis zur Außenwelt, das zeigt ja das eigene Seelenwesen, wie es wirklich ist."
      ],
      [
        "Nun liegt es in der Natur der Menschenseele, solche Aufklärung über sich selbst als peinvoll zu empfinden.",
        "Man er­fährt erst, wenn man diese Pein empfindet, wie stark die ganz selbstverständliche Sehnsucht ist, sich als Menschen, so wie man ist, als wertvoll, als bedeutungsvoll zu halten.",
        "Es mag häßlich aussehen, daß dies so ist; man muß sich dieser Häßlichkeit des eigenen Selbstes frei gegenüberstellen.",
        "Man empfand diese Häßlichkeit vorher eben aus dem Grunde nicht, weil man nie mit seinem Bewußtsein in die eigene Wesenheit wirklich eingedrungen ist.",
        "Man bemerkt erst in einem solchen Augenblicke, wie man an sich liebt, was man nun als häßlich empfinden soll.",
        "Die Gewalt der Eigenliebe zeigt sich in ihrer vollen Größe.",
        "Und zugleich zeigt sich, wie wenig Neigung man hat, diese Eigenliebe abzulegen.",
        "Wenn es sich um die Eigenschaften der Seele handelt, die für das gewöhnliche Leben, für das Verhältnis zu andern Menschen in Betracht kommen, so stellt sich die Schwierigkeit schon als groß genug heraus.",
        "Man erfährt durch wahre Selbsterkenntnis zum Beispiel, daß man bis­her geglaubt hat, man stünde einem Menschen wohlwol­lend gegenüber, und daß man doch in den Seelengründen"
      ],
      [
        "verborgenen Neid, oder Haß, oder ähnliches hegt.",
        "Man er­kennt, daß diese bisher nicht zutage getretenen Gefühle sich ganz gewiß einmal werden äußern wollen.",
        "Und man wird gewahr, daß es ganz oberflächlich wäre, sich zu sagen:"
      ],
      [
        "nun hast du doch erkannt, daß es so mit dir stehe, vertilge also in dir den Neid, den Haß.",
        "Man entdeckt aber, daß man mit einem solchen Gedanken ganz gewiß einmal sich recht schwach erweisen werde, wenn der Drang, den Haß zu be­friedigen, den Neid auszuleben, wie mit Naturgewalt aus der Seele hervorbrechen werden.",
        "Solche besonderen Selbsterkenntnisse treten bei diesem oder jenem Menschen je nach der Beschaffenheit seines Seelenwesens au£ Sie stellen sich ein, wenn Erleben außerhalb des Sinnenleibes eintritt, weil dann die Selbsterkenntnis eben eine wahre wird, und nicht mehr getrübt sein kann von dem Wunsche, sich in der einen oder anderen Art zu finden, wie man es doch nur liebt, zu sein."
      ],
      [
        "Diese besonderen Selbsterkenntnisse sind schmerzvoll, sind bedrückend für die Seele.",
        "Derjenige, der sich die Fä­higkeit erwerben will, außerhalb des Leibes zu erleben, kann sie nicht vermeiden.",
        "Denn sie treten notwendig auf durch das ganz besondere Verhältnis, in das er sich zu der eigenen Seele stellen muß.",
        "Doch der stärksten Seelenkräfte bedarf es, wenn es sich um eine ganz allgemeine menschli­che Selbsterkenntnis handelt.",
        "Man beobachtet sich von ei­nem Gesichtspunkte, der außerhalb des bisherigen Seelen­lebens liegt.",
        "Man sagt zu sich selber: du hast nach deiner menschlichen Wesenheit die Dinge und Vorgänge der Welt betrachtet und über sie geurteilt.",
        "Versuche dir einmal vor­zustellen, du könntest sie nicht so betrachten, nicht so über sie urteilen.",
        "Dann wärest du überhaupt nicht das, was du"
      ],
      [
        "bist.",
        "Du hättest keine inneren Erlebnisse.",
        "Du selbst wärest ein Nichts.",
        "So zu sich sagen, muß nicht etwa nur der Mensch, der im Alltagsleben drinnen steht, und sich nur selten einmal Vorstellungen über die Welt und das Leben macht."
      ],
      [
        "So muß jeder Wissenschafter, jeder Philosoph sa­gen.",
        "Denn auch Philosophie ist nur eine Beobachtung und Beurteilung der Welt nach Maßgabe der Eigenschaften des menschlichen Seelenlebens.",
        "Eine solche Beurteilung kann aber mit der übersinnlichen Außenwelt nicht zusammenfließen."
      ],
      [
        "Sie wird von derselben zurückgewiesen.",
        "Damit wird aber alles zurückgewiesen, was man bisher gewesen ist.",
        "Man sieht auf seine ganze Seele, auf sein «Ich» als auf etwas zurück, was man ablegen muß, wenn man die über­sinnliche Welt betreten will. - Nun kann aber die Seele gar nicht anders, als dieses «Ich» für ihre eigentliche Wesen­heit halten, bevor sie die übersinnliche Welt betritt."
      ],
      [
        "Sie muß in ihr die wahre menschliche Wesenheit sehen.",
        "Sie muß sich sagen: durch dieses mein Ich muß ich mir Vorstellungen über die Welt machen; dieses mein Ich darf ich nicht verlieren, wenn ich mich nicht als Wesenheit selbst ver­loren geben will."
      ],
      [
        "Der stärkste Trieb ist in ihr, das Ich sich überall zu wahren, um nicht allen Boden unter den Füßen zu verlieren.",
        "Was so die Seele im gewöhnlichen Leben berech­tigt empfinden muß, das darf sie nicht mehr empfinden, so­bald sie in die übersinnliche Außenwelt eintritt."
      ],
      [
        "Sie muß da eine Schwelle überschreiten, an der sie nicht den einen oder anderen wertvollen Besitz nur, an welcher sie das zurücklas­sen muß, was sie sich bisher selbst war.",
        "Sie muß sich sagen können, was dir bisher als deine stärkste Wahrheit zu gel­ten hatte, das muß nun jenseits der Schwelle zur übersinn­lichen Welt dir als der stärkste Irrtum erscheinen können."
      ],
      [
        "Gegenüber einer solchen Forderung kann die Seele zu­rückschaudern.",
        "Sie kann, was sie zu tun hätte, so stark als ein Hingeben, eine Nichtigkeitserklärung der eigenen We­senheit empfinden, daß sie an der bezeichneten Schwelle sich mehr oder weniger die eigne Ohnmacht eingesteht, der Forderung zu genügen.",
        "Dieses Eingeständnis kann alle möglichen Formen annehmen.",
        "Es kann ganz instinktiv auf­treten, und dem Menschen, der in seinem Sinne denkt und handelt, als etwas ganz anderes erscheinen, als es wirklich ist.",
        "Er kann zum Beispiel eine tiefe Abneigung gegen alle übersinnlichen Wahrheiten empfinden.",
        "Er kann sie für Träumereien, Phantastereien halten.",
        "Er tut dies nur aus dem Grunde, weil er in seinen ihm selbst unbekannten See­lengründen eine geheime Furcht vor diesen Wahrheiten hat.",
        "Er empfindet, daß er nur mit dem leben kann, was die Sinne und das Verstandesurteil offenbaren.",
        "Er vermeidet es deshalb, an die Schwelle zur übersinnlichen Welt heranzu­kommen.",
        "Er kleidet sich dieses Vermeiden so ein, daß er sagt, was jenseits dieser Schwelle liegen soll, ist vor Ver­nunft und Wissenschaft nicht haltbar.",
        "Es handelt sich aber doch nur darum, daß er Vernunft und Wissenschaft, wie er sie kennt, liebt, weil sie an sein Ich gebunden sind.",
        "Es han­delt sich um eine ganz allgemein menschliche Form von Ei­genliebe.",
        "Diese aber kann in die übersinnliche Welt nicht mit hineingenommen werden."
      ],
      [
        "Es kann aber auch der Fall eintreten, daß es bei diesem instinktiven Haltmachen vor der Schwelle nicht bleibt.",
        "Daß der Mensch bewußt bis zu ihr herantritt, und dann umkehrt, weil er Furcht empfindet vor dem, was ihm bevor­steht.",
        "Er wird dann nicht leicht die Wirkungen verwischen können, welche durch sein Herantreten an die Schwelle sich"
      ],
      [
        "für sein gewöhnliches Seelenleben einstellen.",
        "Diese werden in den Folgen liegen, welche die Ohnmacht, die er empfun­den hat, über sein ganzes Seelensein ausbreitet."
      ],
      [
        "Was eintreten soll, besteht darin, daß der Mensch sich fähig mache, das, was er im gewöhnlichen Leben als stärk­ste Wahrheit empfindet, beim Betreten der übersinnlichen Welt abzulegen und sich auf eine andere Art einzurichten, die Dinge zu empfinden und zu beurteilen.",
        "Er muß nur sich auch klar darüber sein, daß er, wenn er wieder der Sinnenwelt gegenübersteht, auch wieder die für diese gültige Empfindungs- und Beurteilungsart gebrauchen muß.",
        "Er muß nicht nur lernen, in zwei Welten zu leben, sondern auch in beiden auf ganz verschiedene Art zu leben.",
        "Er darf sich für das gewöhnliche Stehen in der Sinnes- und Verstandeswelt das gesunde Urteil nicht beeinträchtigen, weil er für eine andre Welt zur Anwendung einer andren Urteilsart ge­zwungen ist."
      ],
      [
        "Für die menschliche Wesenheit ist eine solche Stellung­nahme schwierig.",
        "Die Fähigkeit für sie erlangt man nur durch fortgesetzte energische und geduldige Verstärkung des Seelenlebens.",
        "Wer die Erfahrungen an der Schwelle macht, der empfindet, daß es für das gewöhnliche mensch­liche Seelenleben eine Wohltat ist, nicht bis zu dieser Schwelle hingeführt zu werden.",
        "Die Empfindungen, wel­che in ihm auftreten, sind so, daß man gar nicht anders kann, als diese Wohltat von einer wesenhaften Macht herrührend zu denken, welche den Menschen schützt vor der Gefahr, die Schrecken der Selbstvernichtung an der Schwel­le zu erleben. - Es liegt hinter der Außenwelt, welche dem gewöhnlichen Leben gegeben ist, eine andre.",
        "Vor deren Schwelle steht ein strenger Hüter, welcher bewirkt, daß der"
      ],
      [
        "Mensch nichts erfährt von dem, was Gesetze der übersinnlichen Welt sind.",
        "Denn alle Zweifel, alle Ungewißheit über diese Welt sind doch noch leichter zu ertragen, als das Schauen dessen, was man zurücklassen muß, wenn man sie betreten will."
      ],
      [
        "Der Mensch bleibt geschützt vor den geschilderten Erleb­nissen, solange er nicht an diese Schwelle selbst herantritt.",
        "Daß er Erzählungen von ihren Erlebnissen von denen ent­gegennimmt, welche diese Schwelle betreten oder über­schritten haben, das ändert nichts daran, daß er geschützt ist.",
        "Dagegen kann ihm solche Entgegennahme dienen im guten Sinne, wenn er sich der Schwelle nähert.",
        "Es ist auch in diesem Falle so wie in vielen andern, daß eine Verrich­tung besser vollzogen wird, wenn man vorher schon eine Vorstellung von ihr sich machen kann, als im entgegenge­setzten Falle.",
        "An dem aber, was der Wanderer in die über­sinnliche Welt an Selbsterkenntnis gewinnen soll, wird durch solches Vorherwis sen nichts geändert.",
        "Es ist deshalb nicht den Tatsachen entsprechend, wenn manche hellsich­tige oder mit dem Wesen der Hellsichtigkeit vertraute Per­sonen behaupten, von solchen Dingen solle überhaupt im Kreise von Menschen nicht gesprochen werden, die nicht vor dem Entschlusse unmittelbar stehen, sich in die über­sinnliche Welt selbst hineinzubegeben.",
        "Wir leben gegen­wärtig in einer Zeit, in welcher die Menschen immer mehr mit dem Wesen der übersinnlichen Welt bekannt werden müssen, wenn sie den Forderungen des Lebens seelisch ge­wachsen sein wollen.",
        "Die Verbreitung der übersinnlichen Erkenntnisse und somit auch derjenigen vom Hüter der Schwelle gehört zu den Aufgaben der Gegenwart und der nächsten Zukunft."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "FÜNFTE MEDITATION",
    "paragraphs": [
      "FÜNFTE MEDITATION",
      "Der Meditierende versucht eine Vorstellung des",
      "«astralischen Leibes» zu bilden",
      "Wenn man durch den elementarischen Leib eine übersinn­liche Außenwelt erlebt, ist man von dieser weniger abge­schlossen, als man beim Erleben im Sinnenleib von seiner physischen Umgebung ist. Dennoch hat man ein Verhält­nis zu dieser übersinnlichen Außenwelt, das sich in der Art ausdrücken läßt, daß man sagt, man habe mit sich verbun­den gewisse Substanzen der elementarischen Welt als einen besonderen elementarischen Leib, wie man die Stoffe und Kräfte der physischen Außenwelt in dem physischen Leibe an sich trägt. Daß dieses sich so verhält, das bemerkt man, wenn man außerhalb seines Sinnenleibes sich in der über­sinnlichen Welt orientieren will. Es kann vorkommen, daß man irgendeine Tatsache oder Wesenheit der übersinnli­chen Welt vor sich hat; sie kann da sein; man kann sie schauen; aber man weiß nicht, was sie ist. Ist man stark ge­nug dazu, dann kann man sie vertreiben; aber nur dadurch, daß man durch energische Besinnung auf seine Erfahrung in der Sinnenwelt sich in diese zurückversetzt. Aber man kann nicht innerhalb der übersinnlichen Welt bleiben, und die geschaute Tatsache oder Wesenheit mit anderen ver­gleichen. Nur dadurch könnte man sich darüber orientie­ren, was das Geschaute bedeutet. Das Schauen der über­sinnlichen Welt kann sich also darauf beschränken, daß man Einzelheiten wahrnimmt, sich aber nicht von dem ei­nen zu dem andern frei bewegen kann. Man fühlt sich dann an der Einzelheit festgehalten.",
      "Man kann nun den Grund dieser Beschränkung suchen.",
      "Man wird ihn nur finden, wenn man durch weitere innere Entwickelung, welche das Seelenleben noch mehr verstärkt, dazu kommt, daß in einem besonderen Falle diese Be­schränkung nicht mehr da ist. Dann aber wird man gewahr, daß der Grund, warum man von dem einen Geschauten nicht zu einem andern sich hinbewegen konnte, in der eige­nen Seele gelegen ist.",
      "Man lernt erkennen, daß das Schauen der übersinnlichen Welt sich auch noch dadurch von dem Wahrnehmen in der sinnlichen Welt unterscheidet, daß man in der letzteren zum Beispiele alles Sichtbare sehen kann, wenn man richtig arbeitende Augen hat. Sieht man das eine, so kann man durch dasselbe Auge auch das andre sehen.",
      "So ist es in der übersinnlichen Welt nicht. Man kann das übersinnliche Beobachtungsorgan des elementarischen Leibes so ausgebildet haben, daß man diese oder jene Tat­sache erleben kann; soll eine andere geschaut werden, so muß das Organ für diese erst wieder besonders ausgebildet werden. - Nun hat man gegenüber einer solchen Ausbil­dung eine Empfindung, die wie ein Erwachen des Organs für einen bestimmten Teil der übersinnlichen Welt ist.",
      "Man fühlt, wie wenn der elementarische Leib gegenüber der übersinnlichen Welt in einer Art von Schlafzustand sei, und als ob er für jede Einzelheit erst erweckt werden müsse. Man kann wirklich von einem Schlafen und Wachen in der elementarischen Welt sprechen.",
      "Nur sind für diese Welt Schlafen und Wachen nicht Wechselzustände, wie sie es in­nerhalb des Lebens in der Sinnenwelt sind. Sie sind als Zu­stände gleichzeitig am Menschen vorhanden. Solange sich der Mensch keine Fähigkeit erworben hat, durch seinen elementarischen Leib etwas zu erleben, schläft dieser Leib.",
      "Der Mensch trägt diesen Leib immer an sich, aber als einen",
      "schlafenden. Mit der Verstärkung des Seelenlebens beginnt das Erwachen, aber zunächst nur für einen Teil dieses Lei­bes. Man lebt sich immer mehr in die elementarische Welt hinein, indem man immer mehr und mehr von dem eige­nen elementarischen Wesen erweckt.",
      "Zu diesem Erwecken kann nun der Seele nichts in der elementarischen Welt selbst verhelfen. So viel auch schon geschaut werden kann: das eine Geschaute trägt nichts da­zu bei, daß auch ein andres geschaut werden kann. Freie Beweglichkeit in der übersinnlichen Welt kann die Seele durch nichts erlangen, was in der elementarischen Umge­bung zu finden ist. Wenn man die Übungen in der Seelenverstärkung fortsetzt, so erlangt man immer mehr und mehr für gewisse Gebiete diese Beweglichkeit. Durch alles dieses wird man auf etwas in sich aufmerksam, welches der elementarischen Welt nicht angehört, das man aber im Er­leben dieser Welt in sich selber entdeckt. Man findet sich als ein besonderes Wesen in der übersinnlichen Welt, das wie ein Lenker seines elementarischen Leibes sich er­scheint, wie ein Beherrscher desselben, der allmählich die­sen Leib zu einem übersinnlichen Bewußtsein erweckt.",
      "Ist man dazu gelangt, so überkommt die Seele ein unge­heures Einsamkeitsgefühl. Man schaut sich in einer Welt, die nach allen Seiten hin elementarisch ist; nur sich selbst schaut man innerhalb der unendlichen elementarischen Wei­ten als ein Wesen, das nicht seinesgleichen irgendwo erschauen kann. - Es soll nicht behauptet werden, daß jede Entwickelung zum Hellsehertum zu dieser schauervollen Einsamkeit führt; doch derjenige, welcher durch eigene Kraft bewußt sich die Seelenverstärkung aneignet, wird da­zu gelangen. Und wer einem Lehrer folgt, der ihm von",
      "Schritt zu Schritt Anleitung gibr, um in der Entwickelung vorwärts zu dringen, der wird - vielleicht spät - aber doch eines ,Tages erfahren müssen, daß sein Lehrer ihn sich selbst überlassen hat. Er wird sich zunächst von ihm verlassen und der Einsamkeit in der elementarischen Welt überge­ben finden. Nachträglich erst wird er erkennen, daß er wei­se von dem Lehrer behandelt worden ist, und daß dieser ihn auf sich selbst verweisen mußte, nachdem die Notwen­digkeit zu solcher Selbständigkeit sich ergeben hatte.",
      "Wie ein in die elementarische Welt Verbannter erscheint sich der Mensch auf dieser Stufe der Seelenwanderschaft. Nun aber kann er weiter gelangen, wenn durch seine inne­ren Übungen genügende Seelenkraft in ihm ist. Er kann beginnen - nicht in der elementarischen Welt, wohl aber in sich selbst eine neue Welt auftauchen zu sehen, welche we­der mit der Sinnenwelt, noch mit der elementarischen Welt eine und dieselbe ist. Es kommt für einen solchen Men­schen eine zweite übersinnliche Welt zu der ersten hinzu. Diese zweite übersinnliche Welt ist nun zunächst eine voll­ständige Innenwelt. Man fühlt, daß man sie in sich selbst trägt und mit ihr allein ist. Will man diesen Zustand mit et­was aus der Sinnenwelt vergleichen, so bietet sich das fol­gende dar. Jemand habe alle seine lieben Angehörigen hin-sterben sehen und trage in sich nur noch die Erinnerung an sie in seiner Seele. Sie leben für ihn nur noch als seine Ge­danken weiter. - So ist man in der zweiten übersinnlichen Welt. Man trägt sie in sich; aber man weiß, daß man von ihrer Wirklichkeit abgeschlossen ist. Nur hat dasjenige, was von dieser Wirklichkeit in der Seele lebt, selbst eine ganz andre Wirklichkeit als bloße Erinnerungsvorstellungen in der Sinnenwelt. Es lebt in der eigenen Seele diese übersinnliche",
      "Welt ein selbständiges Dasein. Alles, was da ist, will aus der Seele hinaus, will zu etwas anderem hin. So fühlt man eine Welt in sich, aber so, daß diese Welt nicht in der Seele bleiben will. Das ruft ein Gefühl hervor, als ob man durch jede Einzelheit dieser Welt zersprengt werden sollte. Man kann dazu kommen, daß sich diese Einzelheiten selbst befreien, daß sie etwas wie eine Seelenhülle gleichsam durchreißen und der Seele entfliehen. Dann kann man sich verarmt fühlen um alles, was sich der Seele so entrissen hat. -",
      "Man lernt nun erkennen, daß sich dasjenige in einer ge­wissen Weise verhält, was man von dem übersinnlichen Seeleninhalt so lieben kann, daß man es um seiner selbst willen liebt und nicht deswegen, weil es in der eigenen See­le ist. Was man in solcher Art hingebend lieben kann, das entreißt sich der Seele nicht; es dringt zwar aus der Seele heraus, aber es nimmt diese Seele gewissermaßen mit. Es führt sie dorthin, wo es in seiner Wirklichkeit lebt. Es fin­det eine Art Vereinigung mit dem wirklichen Wesen statt, während man vorher nur etwas wie ein Nachbild dieses Wesens in sich getragen hat. Die hier gemeinte Liebe muß aber eine solche sein, welche in der übersinnlichen Welt er­lebt wird. In der Sinnenwelt kann man sich für eine solche Liebe nur vorbereiten. Doch bereitet man sich vor, wenn man die Liebefähigkeit in der Sinnenwelt zu einer starken macht. Einer um so stärkeren Liebe man in der Sinnenwelt fähig ist, um so mehr verbleibt der Seele von dieser Liebefähigkeit für die übersinnliche Welt. Dieses bezieht sich auf die Einzelheiten der übersinnlichen Welt so, daß man zum Beispiel zu jenen wirklichen übersinnlichen Wesen, welche mit den Pflanzen der Sinnenwelt in Verbindung ste­hen,",
      "nicht gelangen kann, wenn man Pflanzen in der sinn­lichen Welt nicht liebt. Doch kann in bezug auf solche Din­ge leicht eine Täuschung eintreten. Es kann vorkommen, daß ein Mensch in der Sinnenwelt ganz lieblos an der Pflan­zenwelt vorbeigeht; es kann aber trotzdem in seiner Seele verborgen eine ihm unbewußte Neigung für diese Weh vorhanden sein. Dann kann diese Liebe erwachen, wenn er die übersinnliche Welt betritt.",
      "Wie von der Liebe, so kann das Vereinigen mit Wesen der übersinnlichen Welt auch von andern Eigenschaften der Seele abhängen, wie von der Achtung oder Ehrfurcht, welche innerhalb der übersinnlichen Welt die Seele für ein Wesen empfinden kann, wenn sie erst das Nachbild dieses Wesens in sich auftauchen fühlt. Es werden aber diese Ei­genschaften stets solche sein, die man zu den inneren See­leneigenschaften zu zählen hat. - Man wird so diejenigen Wesen der übersinnlichen Welt kennenlernen, zu denen sich die Seele durch solche Eigenschaften selbst den Zu­gang eröffnet Es erschließt sich ein sicherer Weg zur Orien­tierung in der übersinnlichen Welt dadurch, daß man durch seine Verhältnisse zu den Nachbildern der Wesen sich den Zugang zu ihnen frei macht. In der Sinnenwelt liebt man ein Wesen, nachdem man es kennengelernt hat; in der zwei­ten übersinnlichen Welt kann man vor der Begegnung mlt der Wirklichkeit das Abbild lieben, weil dieses Abbild vor jener Begegnung sich einstellt.",
      "Was die Seele auf diese Art in sich kennenlernt, ist nicht der elementarische Leib. Denn es steht diesem als sein Er-wecker gegenüber. Es ist ein in der Seele vorhandenes We­sen, das man so erlebt, wie man sich erleben wurde, wenn man im Schlafe nicht bewußtlos würde, sondern bewußt",
      "außer seinem physischen Leibe sich erfühlte und beim Erwachen sich als den Erwecker empfände. So lernt die Seele eine in ihr vorhandene Wesenheit kennen, welche ein Drit­tes ist außer dem physischen und dem elementarischen Leib. Es sei diese Wesenheit der astralische Leib genannt, und mit diesem Worte hier zunächst nichts anderes angedeutet, als was sich innerhalb des Seelenseins in der geschilderten Weise erlebt."
    ],
    "sentences": [
      [
        "FÜNFTE MEDITATION"
      ],
      [
        "Der Meditierende versucht eine Vorstellung des"
      ],
      [
        "«astralischen Leibes» zu bilden"
      ],
      [
        "Wenn man durch den elementarischen Leib eine übersinn­liche Außenwelt erlebt, ist man von dieser weniger abge­schlossen, als man beim Erleben im Sinnenleib von seiner physischen Umgebung ist.",
        "Dennoch hat man ein Verhält­nis zu dieser übersinnlichen Außenwelt, das sich in der Art ausdrücken läßt, daß man sagt, man habe mit sich verbun­den gewisse Substanzen der elementarischen Welt als einen besonderen elementarischen Leib, wie man die Stoffe und Kräfte der physischen Außenwelt in dem physischen Leibe an sich trägt.",
        "Daß dieses sich so verhält, das bemerkt man, wenn man außerhalb seines Sinnenleibes sich in der über­sinnlichen Welt orientieren will.",
        "Es kann vorkommen, daß man irgendeine Tatsache oder Wesenheit der übersinnli­chen Welt vor sich hat; sie kann da sein; man kann sie schauen; aber man weiß nicht, was sie ist.",
        "Ist man stark ge­nug dazu, dann kann man sie vertreiben; aber nur dadurch, daß man durch energische Besinnung auf seine Erfahrung in der Sinnenwelt sich in diese zurückversetzt.",
        "Aber man kann nicht innerhalb der übersinnlichen Welt bleiben, und die geschaute Tatsache oder Wesenheit mit anderen ver­gleichen.",
        "Nur dadurch könnte man sich darüber orientie­ren, was das Geschaute bedeutet.",
        "Das Schauen der über­sinnlichen Welt kann sich also darauf beschränken, daß man Einzelheiten wahrnimmt, sich aber nicht von dem ei­nen zu dem andern frei bewegen kann.",
        "Man fühlt sich dann an der Einzelheit festgehalten."
      ],
      [
        "Man kann nun den Grund dieser Beschränkung suchen."
      ],
      [
        "Man wird ihn nur finden, wenn man durch weitere innere Entwickelung, welche das Seelenleben noch mehr verstärkt, dazu kommt, daß in einem besonderen Falle diese Be­schränkung nicht mehr da ist.",
        "Dann aber wird man gewahr, daß der Grund, warum man von dem einen Geschauten nicht zu einem andern sich hinbewegen konnte, in der eige­nen Seele gelegen ist."
      ],
      [
        "Man lernt erkennen, daß das Schauen der übersinnlichen Welt sich auch noch dadurch von dem Wahrnehmen in der sinnlichen Welt unterscheidet, daß man in der letzteren zum Beispiele alles Sichtbare sehen kann, wenn man richtig arbeitende Augen hat.",
        "Sieht man das eine, so kann man durch dasselbe Auge auch das andre sehen."
      ],
      [
        "So ist es in der übersinnlichen Welt nicht.",
        "Man kann das übersinnliche Beobachtungsorgan des elementarischen Leibes so ausgebildet haben, daß man diese oder jene Tat­sache erleben kann; soll eine andere geschaut werden, so muß das Organ für diese erst wieder besonders ausgebildet werden. - Nun hat man gegenüber einer solchen Ausbil­dung eine Empfindung, die wie ein Erwachen des Organs für einen bestimmten Teil der übersinnlichen Welt ist."
      ],
      [
        "Man fühlt, wie wenn der elementarische Leib gegenüber der übersinnlichen Welt in einer Art von Schlafzustand sei, und als ob er für jede Einzelheit erst erweckt werden müsse.",
        "Man kann wirklich von einem Schlafen und Wachen in der elementarischen Welt sprechen."
      ],
      [
        "Nur sind für diese Welt Schlafen und Wachen nicht Wechselzustände, wie sie es in­nerhalb des Lebens in der Sinnenwelt sind.",
        "Sie sind als Zu­stände gleichzeitig am Menschen vorhanden.",
        "Solange sich der Mensch keine Fähigkeit erworben hat, durch seinen elementarischen Leib etwas zu erleben, schläft dieser Leib."
      ],
      [
        "Der Mensch trägt diesen Leib immer an sich, aber als einen"
      ],
      [
        "schlafenden.",
        "Mit der Verstärkung des Seelenlebens beginnt das Erwachen, aber zunächst nur für einen Teil dieses Lei­bes.",
        "Man lebt sich immer mehr in die elementarische Welt hinein, indem man immer mehr und mehr von dem eige­nen elementarischen Wesen erweckt."
      ],
      [
        "Zu diesem Erwecken kann nun der Seele nichts in der elementarischen Welt selbst verhelfen.",
        "So viel auch schon geschaut werden kann: das eine Geschaute trägt nichts da­zu bei, daß auch ein andres geschaut werden kann.",
        "Freie Beweglichkeit in der übersinnlichen Welt kann die Seele durch nichts erlangen, was in der elementarischen Umge­bung zu finden ist.",
        "Wenn man die Übungen in der Seelenverstärkung fortsetzt, so erlangt man immer mehr und mehr für gewisse Gebiete diese Beweglichkeit.",
        "Durch alles dieses wird man auf etwas in sich aufmerksam, welches der elementarischen Welt nicht angehört, das man aber im Er­leben dieser Welt in sich selber entdeckt.",
        "Man findet sich als ein besonderes Wesen in der übersinnlichen Welt, das wie ein Lenker seines elementarischen Leibes sich er­scheint, wie ein Beherrscher desselben, der allmählich die­sen Leib zu einem übersinnlichen Bewußtsein erweckt."
      ],
      [
        "Ist man dazu gelangt, so überkommt die Seele ein unge­heures Einsamkeitsgefühl.",
        "Man schaut sich in einer Welt, die nach allen Seiten hin elementarisch ist; nur sich selbst schaut man innerhalb der unendlichen elementarischen Wei­ten als ein Wesen, das nicht seinesgleichen irgendwo erschauen kann. - Es soll nicht behauptet werden, daß jede Entwickelung zum Hellsehertum zu dieser schauervollen Einsamkeit führt; doch derjenige, welcher durch eigene Kraft bewußt sich die Seelenverstärkung aneignet, wird da­zu gelangen.",
        "Und wer einem Lehrer folgt, der ihm von"
      ],
      [
        "Schritt zu Schritt Anleitung gibr, um in der Entwickelung vorwärts zu dringen, der wird - vielleicht spät - aber doch eines ,Tages erfahren müssen, daß sein Lehrer ihn sich selbst überlassen hat.",
        "Er wird sich zunächst von ihm verlassen und der Einsamkeit in der elementarischen Welt überge­ben finden.",
        "Nachträglich erst wird er erkennen, daß er wei­se von dem Lehrer behandelt worden ist, und daß dieser ihn auf sich selbst verweisen mußte, nachdem die Notwen­digkeit zu solcher Selbständigkeit sich ergeben hatte."
      ],
      [
        "Wie ein in die elementarische Welt Verbannter erscheint sich der Mensch auf dieser Stufe der Seelenwanderschaft.",
        "Nun aber kann er weiter gelangen, wenn durch seine inne­ren Übungen genügende Seelenkraft in ihm ist.",
        "Er kann beginnen - nicht in der elementarischen Welt, wohl aber in sich selbst eine neue Welt auftauchen zu sehen, welche we­der mit der Sinnenwelt, noch mit der elementarischen Welt eine und dieselbe ist.",
        "Es kommt für einen solchen Men­schen eine zweite übersinnliche Welt zu der ersten hinzu.",
        "Diese zweite übersinnliche Welt ist nun zunächst eine voll­ständige Innenwelt.",
        "Man fühlt, daß man sie in sich selbst trägt und mit ihr allein ist.",
        "Will man diesen Zustand mit et­was aus der Sinnenwelt vergleichen, so bietet sich das fol­gende dar.",
        "Jemand habe alle seine lieben Angehörigen hin-sterben sehen und trage in sich nur noch die Erinnerung an sie in seiner Seele.",
        "Sie leben für ihn nur noch als seine Ge­danken weiter. - So ist man in der zweiten übersinnlichen Welt.",
        "Man trägt sie in sich; aber man weiß, daß man von ihrer Wirklichkeit abgeschlossen ist.",
        "Nur hat dasjenige, was von dieser Wirklichkeit in der Seele lebt, selbst eine ganz andre Wirklichkeit als bloße Erinnerungsvorstellungen in der Sinnenwelt.",
        "Es lebt in der eigenen Seele diese übersinnliche"
      ],
      [
        "Welt ein selbständiges Dasein.",
        "Alles, was da ist, will aus der Seele hinaus, will zu etwas anderem hin.",
        "So fühlt man eine Welt in sich, aber so, daß diese Welt nicht in der Seele bleiben will.",
        "Das ruft ein Gefühl hervor, als ob man durch jede Einzelheit dieser Welt zersprengt werden sollte.",
        "Man kann dazu kommen, daß sich diese Einzelheiten selbst befreien, daß sie etwas wie eine Seelenhülle gleichsam durchreißen und der Seele entfliehen.",
        "Dann kann man sich verarmt fühlen um alles, was sich der Seele so entrissen hat. -"
      ],
      [
        "Man lernt nun erkennen, daß sich dasjenige in einer ge­wissen Weise verhält, was man von dem übersinnlichen Seeleninhalt so lieben kann, daß man es um seiner selbst willen liebt und nicht deswegen, weil es in der eigenen See­le ist.",
        "Was man in solcher Art hingebend lieben kann, das entreißt sich der Seele nicht; es dringt zwar aus der Seele heraus, aber es nimmt diese Seele gewissermaßen mit.",
        "Es führt sie dorthin, wo es in seiner Wirklichkeit lebt.",
        "Es fin­det eine Art Vereinigung mit dem wirklichen Wesen statt, während man vorher nur etwas wie ein Nachbild dieses Wesens in sich getragen hat.",
        "Die hier gemeinte Liebe muß aber eine solche sein, welche in der übersinnlichen Welt er­lebt wird.",
        "In der Sinnenwelt kann man sich für eine solche Liebe nur vorbereiten.",
        "Doch bereitet man sich vor, wenn man die Liebefähigkeit in der Sinnenwelt zu einer starken macht.",
        "Einer um so stärkeren Liebe man in der Sinnenwelt fähig ist, um so mehr verbleibt der Seele von dieser Liebefähigkeit für die übersinnliche Welt.",
        "Dieses bezieht sich auf die Einzelheiten der übersinnlichen Welt so, daß man zum Beispiel zu jenen wirklichen übersinnlichen Wesen, welche mit den Pflanzen der Sinnenwelt in Verbindung ste­hen,"
      ],
      [
        "nicht gelangen kann, wenn man Pflanzen in der sinn­lichen Welt nicht liebt.",
        "Doch kann in bezug auf solche Din­ge leicht eine Täuschung eintreten.",
        "Es kann vorkommen, daß ein Mensch in der Sinnenwelt ganz lieblos an der Pflan­zenwelt vorbeigeht; es kann aber trotzdem in seiner Seele verborgen eine ihm unbewußte Neigung für diese Weh vorhanden sein.",
        "Dann kann diese Liebe erwachen, wenn er die übersinnliche Welt betritt."
      ],
      [
        "Wie von der Liebe, so kann das Vereinigen mit Wesen der übersinnlichen Welt auch von andern Eigenschaften der Seele abhängen, wie von der Achtung oder Ehrfurcht, welche innerhalb der übersinnlichen Welt die Seele für ein Wesen empfinden kann, wenn sie erst das Nachbild dieses Wesens in sich auftauchen fühlt.",
        "Es werden aber diese Ei­genschaften stets solche sein, die man zu den inneren See­leneigenschaften zu zählen hat. - Man wird so diejenigen Wesen der übersinnlichen Welt kennenlernen, zu denen sich die Seele durch solche Eigenschaften selbst den Zu­gang eröffnet Es erschließt sich ein sicherer Weg zur Orien­tierung in der übersinnlichen Welt dadurch, daß man durch seine Verhältnisse zu den Nachbildern der Wesen sich den Zugang zu ihnen frei macht.",
        "In der Sinnenwelt liebt man ein Wesen, nachdem man es kennengelernt hat; in der zwei­ten übersinnlichen Welt kann man vor der Begegnung mlt der Wirklichkeit das Abbild lieben, weil dieses Abbild vor jener Begegnung sich einstellt."
      ],
      [
        "Was die Seele auf diese Art in sich kennenlernt, ist nicht der elementarische Leib.",
        "Denn es steht diesem als sein Er-wecker gegenüber.",
        "Es ist ein in der Seele vorhandenes We­sen, das man so erlebt, wie man sich erleben wurde, wenn man im Schlafe nicht bewußtlos würde, sondern bewußt"
      ],
      [
        "außer seinem physischen Leibe sich erfühlte und beim Erwachen sich als den Erwecker empfände.",
        "So lernt die Seele eine in ihr vorhandene Wesenheit kennen, welche ein Drit­tes ist außer dem physischen und dem elementarischen Leib.",
        "Es sei diese Wesenheit der astralische Leib genannt, und mit diesem Worte hier zunächst nichts anderes angedeutet, als was sich innerhalb des Seelenseins in der geschilderten Weise erlebt."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "SECHSTE MEDITATION",
    "paragraphs": [
      "SECHSTE MEDITATION",
      "Der Meditierende versucht eine Vorstellung des",
      "«Ich-Leibes», oder «Gedanken-Leibes» zu bilden",
      "Das Gefühl, außerhalb seines Sinnenleibes zu sein, hat man beim Erleben innerhalb des astralischen Leibes stärker als beim Erleben im elementarischen Leibe. Bei diesem fühlt man sich außer dem Gebiete, in welchem der Sinnenleib ist; aber man fühlt diesen mit.",
      "Im astralischen Leibe aber fühlt man den Sinnenleib selbst als etwas Äußeres. Beim Übergang in den elementarischen Leib empfindet man et­was wie eine Erweiterung der eigenen Wesenheit, beim Einleben in den astralischen Leib dagegen eine Art Übersprin­gen in eine andre Wesenheit.",
      "Und in diese Wesenheit fühlt man eine geistige Welt von Wesenheiten hereinwirkend. Man empfindet sich in der einen oder andern Art verbun­den, oder auch verwandt mit diesen Wesenheiten. Und man lernt allmählich erkennen, wie diese Wesenheiten selbst zu­einander stehen.",
      "Es erweitert sich für das menschliche Be­wußtsein die Welt nach dem Geiste hin. Der Mensch schaut geistige Wesenheiten, welche zum Beispiele bewirken, daß die aufeinanderfolgenden Epochen der Menschheitsent­wickelung in ihrem Charakter wirklich von Wesenheiten bestimmt werden.",
      "Es sind dies die Zeitgeister, oder Urkräfte. Andre Wesen lernt man kennen, deren Dasein see­lisch so verläuft, daß ihre Gedanken zugleich wirksame Na­turkräfte sind. Man kommt dazu, anzuerkennen, daß es nur für das sinnliche Wahrnehmen mit den Naturkräften so be­stellt erscheint, wie eben dieses sinnliche Wahrnehmen glaubt.",
      "Daß vielmehr in Wirklichkeit überall da, wo eine Naturkraft wirkt, sich ein Gedanke einer Wesenheit auslebt,",
      "wie in der Bewegung der Hand eine menschliche Seele sich auslebt. - Dies alles ist nicht etwa so, daß der Mensch durch irgendeine Theorie sich zu den Naturvorgängen hin­ter diesen stehende Wesenheiten hinzudenkt; der im astra­lischen Leibe sich Erlebende tritt zu diesen Wesenheiten in ein so begriffreies, konkretes Verhältnis, wie der Mensch in der Sinnenwelt zu andern individuellen Menschen tritt. - Man kann innerhalb der Wesenheiten, in deren Gebiet man auf diese Art eintritt, eine Stufenreihe unterscheiden und von einer Welt von höheren Hierarchien sprechen. Die We­senheiten, deren Gedanken dem sinnlichen Wahrnehmen als Naturkräfte sich offenbaren, kann man Geister der Form nennen.",
      "Das Erleben in dieser Welt bedingt, daß man sein Wesen innerhalb der Sinnenwelt so als Äußeres empfindet, wie man im Sinnensein eine Pflanze als äußeres Wesen an­schaut. - Man wird diese Art, außerhalb dessen zu sein, was man im gewöhnlichen Leben als den ganzen Umfang der eigenen Wesenheit empfinden muß, so lange als höchst schmerzvoll empfinden, als nicht ein anderes Erleben hin­zutritt. Bei einem energischen inneren seelischen Arbeiten, das zur rechten Verdichtung und Verstärkung des Seelen­lebens führt, ist nicht notwendig, daß gerade dieser Schmerz in besonders starkem Maße auftritt. Denn es kann ein lang­sames Hineintreten in das andre Erleben zugleich mit dem Einleben in den astralischen Leib sich einstellen.",
      "Dieses andre Erleben wird darinnen bestehen, daß man alles, was in und an der eignen Seele vorher war, als eine Art Erinnerung empfinden kann, und daß man also zu sei­nem Ich, wie es vorher war, sich so verhält, wie man sich in der Sinnenwelt zu Erinnerungen verhält. Erst durch ein",
      "solches Erleben erringt man das volle Bewußtsein, daß man wahrhaftig selbst, in einer ganz andren Welt, als die Sin­nenwelt ist, mit seiner eigenen Wesenheit darinnen lebt. Man hat nunmehr ein Wissen davon, daß man das bisherige «Ich» als etwas anderes, als man eigentlich ist, an sich trägt.",
      "Man kann sich nun selbst sich gegenüberstellen. Und man erhält eine Vorstellung von dem, was der eignen Seele jetzt gegenübersteht, und wovon sie vorher gesagt hat: das bin ich selbst. Jetzt sagt sie nicht mehr, das bin ich selbst, son­dern, das trage ich als etwas an mir.",
      "Wie sich das Ich im ge­wöhnlichen Leben als selbständig gegenüber seinen Erin­nerungen fühlt, so fühlt sich das nunmehr errungne Ich ge­genüber dem frühern Ich selbständig. Es fühlt sich der Welt rein geistiger Wesenheiten angehörig.",
      "Und so, wie sich die­se Erfahrung - und zwar diese und wieder nicht eine Theo­rie - gibt, erkennt man, was das eigentlich ist, was man bis­her als seine Ichwesenheit angesehen hat. Es stellt sich dar wie ein Gewebe aus Erinnerungsvorstellungen, die so von dem Sinnenleib, von dem elementatischen und astralischen Leibe bewirkt werden wie ein Spiegelbild durch einen Spie­gel.",
      "So wenig sich ein Mensch für eins hält mit seinem Spie­gelbild, so wenig hält sich die Seele, welche sich in der gei­stigen Welt erlebt, für eines mit dem, was sie von sich in der Sinnenwelt erlebt. Der Vergleich mit dem Spiegelbild kann naturgemäß nur als ein Vergleich genommen werden.",
      "Denn das Spiegelbild hört auf, wenn der Mensch seine Lage zum Spiegel entsprechend ändert. Das Gewebe, das wie aus Er­innerungsvorstellungen gewoben ist und darstellt, was man in der Sinnenwelt für sein eigenes Wesen ansieht, hat eine größere Selbständigkeit als ein Spiegelbild.",
      "Es hat auf seine Art eine Wesenheit für sich. Und doch ist es dem wahrhaf­ten",
      "Seelensein gegenüber wie ein Bild der eigenen Wesen­heit. Das wahrhafte Seelensein empfindet, daß es dieses Bild zu seiner Selbstoffenbarung nötig hat. Es weiß, daß es et­was andres ist, daß es aber nie dazu gelangt wäre, von sich wirklich etwas zu wissen, wenn es sich nicht zuerst als sein eigenes Abbild in jener Welt erfaßt hätte, die ihm nach sei­nem Aufstieg in die geistige Welt eine Außenwelt gewor­den ist.",
      "Das Gewebe von Erinnerungsvotstellungen, das man nunmehr als sein früheres «Ich» anschaut, kann man den «Ich-Leib» oder auch « Gedankenleib» nennen. Das Wort «Leib» muß in einem solchen Zusammenhange in einem erweiterten Sinne dem gegenüber genommen werden, was man sonst gewohnt ist, einen «Leib» zu nennen. «Leib» bedeutet hier eben alles, was man an sich erlebt, und von dem man nicht sagt, man ist es, sondern man hat es an sich.",
      "Erst wenn das hellsichtige Bewußtsein dahin gelangt ist, dasjenige, was es bisher als sich selbst bezeichnet hat, wie eine Summe von Erinnerungsvorstellungen zu erleben, kann es eine Erfahrung von dem im wahrhaften Sinne ge­winnen, was sich hinter der Erscheinung des Todes ver­birgt. Denn es ist jetzt an die Wesenheit einer wahrhaft wirklichen Welt herangelangt, in welcher es sich selber als ein Wesen erfühlt, das wie in einem Gedächtnisse festhal­ten kann, was im Sinnesdasein erlebt wird. Dieses im Sin­nensein Erlebte bedarf, um sein Dasein weiter zu leben, ei­ner Wesenheit, von welcher es so festgehalten werden kann, wie die Erinnerungsvorsteilungen im Sinnensein von dem gewöhnlichen Ich festgehalten werden. Die übersinn­liche Erkenntnis offenbart, daß der Mensch innerhalb der Welt geistiger Wesenheit ein Dasein hat, und daß er es",
      "selbst ist, der sein Sinnendasein innerhalb Seiner wie eine Erinnerung aufbewahrt. Die Frage, was kann nach dem,  Tode alles das sein, was ich jetzt bin, beantwortet sich für die hellseherische Forschung so: du wirst sein, was du von dir selbst bewahrst kraft deines Daseins als ein Geistwesen unter andern Geistwesen.",
      "Man erkennt die Natur dieser Geistwesen und innerhalb derselben seine eigene. Und diese Erkenntnis ist unmittel­bares Erleben. Man weiß durch dasselbe, daß die Geistwe­sen und mit ihnen auch die eigne Seele ein Dasein haben, für welches das Sinnensein eine vorübergehende Offenba­rung ist. - Zeigt sich für das gewöhnliche Bewußtsein - im Sinne der ersten Meditation -, daß der Leib einer Welt an­gehört, deren wahrer Anteil an ihm sich in seiner Auflösung nach dem Tode offenbart, so zeigt die hellseherische Beobachtung daß das menschliche Ichwesen einer Welt angehört, an ,welche sie durch ganz andere Bande gebunden ist, als der Leib an die Naturgesetze. Die Bande, mit denen das Ichwesen an die Geistwesen der übersinnlichen Welt gebunden ist werden von Geburt und, Tod in ihrer innersten Wesenheit nicht berührt. Im sinnlichen Leibesleben offenbaren sich diese Bande nur in einer besonderen Art. Was in diesem Leben erscheint, ist der Ausdruck für Zusammenhänge, welche übersinnlicher Art sind. Da nun der Mensch als solcher ein übersinnliches Wesen ist - und für die übersinnliche Beobachtung auch als solches er­scheint, so ist auch im Übersinnlichen der Zusammenhang von Menschenseele zu Menschenseele nicht durch den Tod beeinträchtigt. Und was der Seele als bange Frage vor das gewöhnliche Bewußtsein in der primitiven Form tritt: wer­de ich diejenigen, welche ich im Sinnesleben mit mir verbunden­",
      "gewußt habe, nach dem Tode wiederschauen, muß von der wirklichen Forschung, die auf diesem Gebiete zu einem Erfahrungsurteil berechtigt ist, mit einem entschie­denen «Ja» beantwortet werden.",
      "Alles, was hier für das Erleben des Seelenwesens als gei­stige Wirklichkeit innerhalb der Welt anderer Geistwesen gesagt worden ist, kann durch die schon oft erwähnte Ver­stärkung des Seelenlebens geschaut werden. Man kann aber noch durch besondere Empfindungen, welche man ausbil­det, diesem Erleben eine Hilfe zuführen. - Im gewöhnli­chen Erleben innerhalb der Sinnenwelt stellt man sich zu dem, was man als sein Schicksal empfindet, so, daß man das eine als sympathisch, das andre als antipathisch empfindet.",
      "Eine Selbstbesinnung, welche sich selbst gegenüber ganz unbefangen sein kann, wird sich gestehen müssen, daß die hier in Betracht kommenden Sympathien und Antipathien zu den stärksten gehören, welche der Mensch empfinden kann. Eine gewöhnliche Überlegung etwa von der Art, daß doch alles notwendig sei im Leben, daß man sein Schicksal ertragen müsse, kann zwar sehr weit führen für eine gelas­sene Lebensstimmung.",
      "Um aber für ein Erfassen des wah­ren Menschenwesens etwas zu erzielen, ist noch mehr not­wendig. Die gekennzeichnete Überlegung wird dem See­lenleben die besten Dienste leisten; doch wird man oft be­merken können, daß dasjenige, was man an Sympathien und Antipathien in der angegebenen Richtung abgestreift hat, nur verschwunden ist für das unmittelbare Bewußt­sein.",
      "Es hat sich in die tieferen Gründe des Menschenwe­sens zurückgezogen und lebt sich aus als Seelenstimmung, oder auch als Abspannungs- oder sonstige Gefühle des Lei­bes. Wahre Gleichmütigkeit gegenüber dem Schicksale erlangt",
      "man nur, wenn man auf diesem Felde sich genau so verhält wie mit dem wiederholten, verstärkten Hingeben an Gedanken oder Empfindungen zur Seelenverstärkung im allgemeinen. Es genügt nicht die Überlegung, welche es bis zur Verstandeseinsicht bringt, sondern es bedarf eines intensiven Zusammenlebens mit solcher Überlegung, eines durch Zeiten dauernden Festhaltens derselben in der Seele mit gleichzeitigem Entfernthalten der Sinneserlebnisse und der übrigen Lebenserinnerungen.",
      "Durch solche Übung kommt man zu einer gewissen Grund-Seelenstimmung ge­genüber seinem Lebensschicksal. Man kann gründlich aus sich heraustreiben die Antipathien und Sympathien auf die­sem Gebiete und kann zuletzt alles, was dem Menschen ge­schieht, an ihn herankommen sehen, wie man als völlig äu­ßerer Beobachter einen Wasserstrahl über einen Felsen fal­len und unten aufschlagen sieht.",
      "Es ist damit nicht gesagt, daß man auf solche Art dazu gelangen solle, gefühllos sei­nem Schicksale gegenüberzustehen. Wer dazu kommt, mit Gleichgültigkeit auf alles zu sehen, was mit ihm geschieht, der ist ganz gewiß auf keinem gedeihlichen Wege.",
      "Man steht aber doch nicht anteilslos der Außenwelt gegen­über in bezug auf dasjenige, was die eigene Seele nicht schicksalsmäßig berührt. Man sieht, was vor den Augen sich abspielt, mit Freude oder mit Abneigung.",
      "Nicht An­teilslosigkeit am Leben soll der nach übersinnlicher Er­kenntnis Strebende suchen, sondern Umwandlung des An­teils, welchen das «Ich» in bezug auf alles zunächst hat, was es schicksalsmäßig berührt. Es kann durchaus vorkommen, daß durch diese Umwandlung die Lebhaftigkeit des Ge­fühlswesens sogar verstärkt, nicht abgeschwächt wird.",
      "Im gewöhnlichen Leben pressen sich über manches die ,Tränen",
      "in die Augen, was die eigne Seele betrifft in schicksalsmäßi­ger Art. Man kann sich aber auch zu dem Gesichtspunkt durchringen, daß man das gleiche lebhafte Gefühl seinem eigenen Mißgeschick gegenüber hat, das man empfindet, wenn dasselbe einen andern Menschen trifft. Es gelangt der Mensch leichter zu einer solchen Art des Erlebens in bezug auf die Vorfälle, die ihn schicksalsmäßig treffen, als zum Beispiele in bezug auf die eigenen Fähigkeiten. Der Ge­danke ist denn doch nicht so leicht erreichbar, der sich ebenso in Freude auslebt, wenn ein anderer eine Fähigkeit hat, als wenn man diese selbst besitzt. Wenn Selbstbesin­nung vorzudringen sucht bis in die tiefsten Seelengründe, so kann da manches entdeckt werden an selbstischer Freu­de über so manches, was man selbst kann. Ein intensives, wiederholtes (meditatives) Zusammenleben mit dem Ge­danken, daß es in vieler Beziehung für den Gang des Men­schenlebens doch gleich ist, ob man selbst, oder ob ein and­rer etwas kann, vermag weit zu führen in bezug auf wahre Gelassenheit gegenüber dem, was man als innerstes Lebens-schicksal empfindet. - Es kann solche innere gedankenkräf­tige Verstärkung des Seelenlebens, wenn sie richtig ange­stellt wird, nur nie dazu führen, daß man das Gefühl für sei­ne Fähigkeiten bloß abstumpft: man verwandelt es viel­mehr. Man empfindet die Notwendigkeit, sich diesen Fä­higkeiten entsprechend zu verhalten.",
      "Und damit ist schon hingedeutet auf die Richtung, wel­che eine solche gedankenkräftige Verstärkung des Seelen­lebens nimmt. Man lernt in sich etwas erkennen, was der Seele im eigenen Innern als ein zweites Wesen erscheint. Besonders offenbart sich dies, wenn man damit die Gedan­ken verbindet, welche zeigen, wie man im gewöhnlichen",
      "Leben dies oder jenes im Schicksal herbeiführt. Man kann doch wahrnehmen, dieses oder jenes wäre mit dir nicht ge­schehen, wenn du selbst in einer früheren Zeit nicht dich in einer gewissen Art verhalten hättest.",
      "Was dem Menschen heute geschieht, ergibt sich ja vielfach aus dem, was er ge­stern getan hat. Man kann nun mit dem Ziele, sein Seelen­erleben weiter zu führen, als es in einem gewissen Zeit­punkt ist, einen Rückblick anstellen in das bisherige Erle­ben.",
      "Man kann dabei alles aufsuchen, welches zeigt, wie man spätere Schicksalsvorfälle vorher selbst vorbereitet hat. Man kann versuchen, mit einem solchen Rückblick auf das Leben bis zu jenem Zeitpunkte zu kommen, in welchem beim Kinde das Bewußtsein so erwacht, daß es sich im spä­teren Leben an das erinnert, was es erlebt hat.",
      "Stellt man einen solchen Rückblick so an, daß man mit ihm die Seelenstimmung verbindet, welche die gewöhnlichen selbstischen Sympathien und Antipathien mit schicksalsmäßigen Vorfäl­len ausschaltet, so steht man, wenn man erinnerungsmäßig den bezeichneten Zeitpunkt des Kindeslebens erreicht, sich so gegenüber, daß man sich sagt: da hat wohl die Möglich­keit erst begonnen, daß du dich in dir fühlst und an deinem Seelenleben bewußt arbeitest; dieses dein «Ich» war aber auch vorher da, es hat zwar nicht wissend in dir gearbeitet, aber dich sogar zu deiner Wissensfähigkeit wie zu allem an­dern, wovon du weißt, erst gebracht. Was keine verstan­desmäßige Überlegung erkennen kann, das führt die ge­schilderte Stellung zu dem eignen Lebensschicksale herbei.",
      "Man lernt auf die Schicksalsvorfälle blicken; mit Gelassen­heit; man sieht sie unbefangen an sich herantreten; aber man erschaut sich selbst in der Wesenheit, welche diese Vorfälle heranbringt. Und wenn man sich in solcher Art",
      "schaut, so stellen sich der Seele die Bedingungen des eignen Schicksals, die schon mit der Geburt gegeben sind, verbun­den mit dem eigenen Selbst dar. Man ringt sich durch, zu sagen, wie du an dir gearbeitet hast in der Zeit, nachdem dein Bewußtsein erwacht ist, so hast du auch schon an dir gearbeitet, bevor dein gegenwärtiges Bewußtsein erwacht ist.",
      "Ein solches Sich-Hindurcharbeiten zu einem überge­ordneten Ichwesen in dem gewöhnlichen Ich führt nicht nur dazu, sich sagen zu können, mein Gedanke bringt mich dazu, ein solches übergeordnetes Ich theoretisch zu ersin­nen, sondern es führt dazu, das lebendige Wesen dieses «Ich» in seiner Wirklichkeit als Macht in sich zu erfühlen, und das gewöhnliche Ich als ein Geschöpf dieses Anderen in sich zu empfinden. Dieses Fühlen ist ein wahrhafter An­fang des Schauens der Geistwesenheit der Seele.",
      "Und wenn es zu nichts führt, so liegt das nur daran, daß man es beim Anfang bewenden läßt. Dieser Anfang kann ein kaum be­merkbares, dumpfes Empfinden sein. Er wird dies vielleicht lange bleiben. Doch wenn man stark und kräftig das weiter verfolgt, was zu diesem Anfang geführt hat, bringt man es zuletzt zum Schauen der Seele als Geistwesenheit.",
      "Und wer es zu diesem Schauen gebracht hat, der findet es ganz be­greiflich, wenn jemand, der keine Erfahrung auf diesem Gebiete sich verschafft hat, sagt, derjenige, der solches zu schauen glaubt, habe sich nur durch seelisches Gebahren zur Einbildung - Autosuggestion - des übergeordneten Ich gebracht. Doch weiß der mit solchem Schauen Ausgerü­stete auch, daß ein so gearteter Einwand nur von diesem Fehlen der Erfahrung herrühren kann.",
      "Denn wer im Ern­ste das Geschilderte durchmacht, der eignet sich zugleich auch die Fähigkeit an, seine Einbildungen von Wirklichkeiten",
      "unterscheiden zu können. Die inneren Erlebnisse und Betätigungen, die auf solcher Seelenwanderschaft notwen­dig sind, wenn sie eine richtige sein soll, führt dazu, gegen sich selbst in bezug auf Einbildung und Wirklichkeit die strengste Vorsicht anzuwenden. Man wird, wenn zielvoll angestrebt wird, in dem übergeordneten «Ich» sich als Geistwesen zu erleben, das Haupterlebnis in demjenigen sehen, was zu Anfang dieser Meditation charakterisiert ist, und das an zweiter Stelle Angeführte als eine Hilfe der See­lenwanderschaft anerkennen."
    ],
    "sentences": [
      [
        "SECHSTE MEDITATION"
      ],
      [
        "Der Meditierende versucht eine Vorstellung des"
      ],
      [
        "«Ich-Leibes», oder «Gedanken-Leibes» zu bilden"
      ],
      [
        "Das Gefühl, außerhalb seines Sinnenleibes zu sein, hat man beim Erleben innerhalb des astralischen Leibes stärker als beim Erleben im elementarischen Leibe.",
        "Bei diesem fühlt man sich außer dem Gebiete, in welchem der Sinnenleib ist; aber man fühlt diesen mit."
      ],
      [
        "Im astralischen Leibe aber fühlt man den Sinnenleib selbst als etwas Äußeres.",
        "Beim Übergang in den elementarischen Leib empfindet man et­was wie eine Erweiterung der eigenen Wesenheit, beim Einleben in den astralischen Leib dagegen eine Art Übersprin­gen in eine andre Wesenheit."
      ],
      [
        "Und in diese Wesenheit fühlt man eine geistige Welt von Wesenheiten hereinwirkend.",
        "Man empfindet sich in der einen oder andern Art verbun­den, oder auch verwandt mit diesen Wesenheiten.",
        "Und man lernt allmählich erkennen, wie diese Wesenheiten selbst zu­einander stehen."
      ],
      [
        "Es erweitert sich für das menschliche Be­wußtsein die Welt nach dem Geiste hin.",
        "Der Mensch schaut geistige Wesenheiten, welche zum Beispiele bewirken, daß die aufeinanderfolgenden Epochen der Menschheitsent­wickelung in ihrem Charakter wirklich von Wesenheiten bestimmt werden."
      ],
      [
        "Es sind dies die Zeitgeister, oder Urkräfte.",
        "Andre Wesen lernt man kennen, deren Dasein see­lisch so verläuft, daß ihre Gedanken zugleich wirksame Na­turkräfte sind.",
        "Man kommt dazu, anzuerkennen, daß es nur für das sinnliche Wahrnehmen mit den Naturkräften so be­stellt erscheint, wie eben dieses sinnliche Wahrnehmen glaubt."
      ],
      [
        "Daß vielmehr in Wirklichkeit überall da, wo eine Naturkraft wirkt, sich ein Gedanke einer Wesenheit auslebt,"
      ],
      [
        "wie in der Bewegung der Hand eine menschliche Seele sich auslebt. - Dies alles ist nicht etwa so, daß der Mensch durch irgendeine Theorie sich zu den Naturvorgängen hin­ter diesen stehende Wesenheiten hinzudenkt; der im astra­lischen Leibe sich Erlebende tritt zu diesen Wesenheiten in ein so begriffreies, konkretes Verhältnis, wie der Mensch in der Sinnenwelt zu andern individuellen Menschen tritt. - Man kann innerhalb der Wesenheiten, in deren Gebiet man auf diese Art eintritt, eine Stufenreihe unterscheiden und von einer Welt von höheren Hierarchien sprechen.",
        "Die We­senheiten, deren Gedanken dem sinnlichen Wahrnehmen als Naturkräfte sich offenbaren, kann man Geister der Form nennen."
      ],
      [
        "Das Erleben in dieser Welt bedingt, daß man sein Wesen innerhalb der Sinnenwelt so als Äußeres empfindet, wie man im Sinnensein eine Pflanze als äußeres Wesen an­schaut. - Man wird diese Art, außerhalb dessen zu sein, was man im gewöhnlichen Leben als den ganzen Umfang der eigenen Wesenheit empfinden muß, so lange als höchst schmerzvoll empfinden, als nicht ein anderes Erleben hin­zutritt.",
        "Bei einem energischen inneren seelischen Arbeiten, das zur rechten Verdichtung und Verstärkung des Seelen­lebens führt, ist nicht notwendig, daß gerade dieser Schmerz in besonders starkem Maße auftritt.",
        "Denn es kann ein lang­sames Hineintreten in das andre Erleben zugleich mit dem Einleben in den astralischen Leib sich einstellen."
      ],
      [
        "Dieses andre Erleben wird darinnen bestehen, daß man alles, was in und an der eignen Seele vorher war, als eine Art Erinnerung empfinden kann, und daß man also zu sei­nem Ich, wie es vorher war, sich so verhält, wie man sich in der Sinnenwelt zu Erinnerungen verhält.",
        "Erst durch ein"
      ],
      [
        "solches Erleben erringt man das volle Bewußtsein, daß man wahrhaftig selbst, in einer ganz andren Welt, als die Sin­nenwelt ist, mit seiner eigenen Wesenheit darinnen lebt.",
        "Man hat nunmehr ein Wissen davon, daß man das bisherige «Ich» als etwas anderes, als man eigentlich ist, an sich trägt."
      ],
      [
        "Man kann sich nun selbst sich gegenüberstellen.",
        "Und man erhält eine Vorstellung von dem, was der eignen Seele jetzt gegenübersteht, und wovon sie vorher gesagt hat: das bin ich selbst.",
        "Jetzt sagt sie nicht mehr, das bin ich selbst, son­dern, das trage ich als etwas an mir."
      ],
      [
        "Wie sich das Ich im ge­wöhnlichen Leben als selbständig gegenüber seinen Erin­nerungen fühlt, so fühlt sich das nunmehr errungne Ich ge­genüber dem frühern Ich selbständig.",
        "Es fühlt sich der Welt rein geistiger Wesenheiten angehörig."
      ],
      [
        "Und so, wie sich die­se Erfahrung - und zwar diese und wieder nicht eine Theo­rie - gibt, erkennt man, was das eigentlich ist, was man bis­her als seine Ichwesenheit angesehen hat.",
        "Es stellt sich dar wie ein Gewebe aus Erinnerungsvorstellungen, die so von dem Sinnenleib, von dem elementatischen und astralischen Leibe bewirkt werden wie ein Spiegelbild durch einen Spie­gel."
      ],
      [
        "So wenig sich ein Mensch für eins hält mit seinem Spie­gelbild, so wenig hält sich die Seele, welche sich in der gei­stigen Welt erlebt, für eines mit dem, was sie von sich in der Sinnenwelt erlebt.",
        "Der Vergleich mit dem Spiegelbild kann naturgemäß nur als ein Vergleich genommen werden."
      ],
      [
        "Denn das Spiegelbild hört auf, wenn der Mensch seine Lage zum Spiegel entsprechend ändert.",
        "Das Gewebe, das wie aus Er­innerungsvorstellungen gewoben ist und darstellt, was man in der Sinnenwelt für sein eigenes Wesen ansieht, hat eine größere Selbständigkeit als ein Spiegelbild."
      ],
      [
        "Es hat auf seine Art eine Wesenheit für sich.",
        "Und doch ist es dem wahrhaf­ten"
      ],
      [
        "Seelensein gegenüber wie ein Bild der eigenen Wesen­heit.",
        "Das wahrhafte Seelensein empfindet, daß es dieses Bild zu seiner Selbstoffenbarung nötig hat.",
        "Es weiß, daß es et­was andres ist, daß es aber nie dazu gelangt wäre, von sich wirklich etwas zu wissen, wenn es sich nicht zuerst als sein eigenes Abbild in jener Welt erfaßt hätte, die ihm nach sei­nem Aufstieg in die geistige Welt eine Außenwelt gewor­den ist."
      ],
      [
        "Das Gewebe von Erinnerungsvotstellungen, das man nunmehr als sein früheres «Ich» anschaut, kann man den «Ich-Leib» oder auch « Gedankenleib» nennen.",
        "Das Wort «Leib» muß in einem solchen Zusammenhange in einem erweiterten Sinne dem gegenüber genommen werden, was man sonst gewohnt ist, einen «Leib» zu nennen.",
        "«Leib» bedeutet hier eben alles, was man an sich erlebt, und von dem man nicht sagt, man ist es, sondern man hat es an sich."
      ],
      [
        "Erst wenn das hellsichtige Bewußtsein dahin gelangt ist, dasjenige, was es bisher als sich selbst bezeichnet hat, wie eine Summe von Erinnerungsvorstellungen zu erleben, kann es eine Erfahrung von dem im wahrhaften Sinne ge­winnen, was sich hinter der Erscheinung des Todes ver­birgt.",
        "Denn es ist jetzt an die Wesenheit einer wahrhaft wirklichen Welt herangelangt, in welcher es sich selber als ein Wesen erfühlt, das wie in einem Gedächtnisse festhal­ten kann, was im Sinnesdasein erlebt wird.",
        "Dieses im Sin­nensein Erlebte bedarf, um sein Dasein weiter zu leben, ei­ner Wesenheit, von welcher es so festgehalten werden kann, wie die Erinnerungsvorsteilungen im Sinnensein von dem gewöhnlichen Ich festgehalten werden.",
        "Die übersinn­liche Erkenntnis offenbart, daß der Mensch innerhalb der Welt geistiger Wesenheit ein Dasein hat, und daß er es"
      ],
      [
        "selbst ist, der sein Sinnendasein innerhalb Seiner wie eine Erinnerung aufbewahrt.",
        "Die Frage, was kann nach dem, Tode alles das sein, was ich jetzt bin, beantwortet sich für die hellseherische Forschung so: du wirst sein, was du von dir selbst bewahrst kraft deines Daseins als ein Geistwesen unter andern Geistwesen."
      ],
      [
        "Man erkennt die Natur dieser Geistwesen und innerhalb derselben seine eigene.",
        "Und diese Erkenntnis ist unmittel­bares Erleben.",
        "Man weiß durch dasselbe, daß die Geistwe­sen und mit ihnen auch die eigne Seele ein Dasein haben, für welches das Sinnensein eine vorübergehende Offenba­rung ist. - Zeigt sich für das gewöhnliche Bewußtsein - im Sinne der ersten Meditation -, daß der Leib einer Welt an­gehört, deren wahrer Anteil an ihm sich in seiner Auflösung nach dem Tode offenbart, so zeigt die hellseherische Beobachtung daß das menschliche Ichwesen einer Welt angehört, an ,welche sie durch ganz andere Bande gebunden ist, als der Leib an die Naturgesetze.",
        "Die Bande, mit denen das Ichwesen an die Geistwesen der übersinnlichen Welt gebunden ist werden von Geburt und, Tod in ihrer innersten Wesenheit nicht berührt.",
        "Im sinnlichen Leibesleben offenbaren sich diese Bande nur in einer besonderen Art.",
        "Was in diesem Leben erscheint, ist der Ausdruck für Zusammenhänge, welche übersinnlicher Art sind.",
        "Da nun der Mensch als solcher ein übersinnliches Wesen ist - und für die übersinnliche Beobachtung auch als solches er­scheint, so ist auch im Übersinnlichen der Zusammenhang von Menschenseele zu Menschenseele nicht durch den Tod beeinträchtigt.",
        "Und was der Seele als bange Frage vor das gewöhnliche Bewußtsein in der primitiven Form tritt: wer­de ich diejenigen, welche ich im Sinnesleben mit mir verbunden­"
      ],
      [
        "gewußt habe, nach dem Tode wiederschauen, muß von der wirklichen Forschung, die auf diesem Gebiete zu einem Erfahrungsurteil berechtigt ist, mit einem entschie­denen «Ja» beantwortet werden."
      ],
      [
        "Alles, was hier für das Erleben des Seelenwesens als gei­stige Wirklichkeit innerhalb der Welt anderer Geistwesen gesagt worden ist, kann durch die schon oft erwähnte Ver­stärkung des Seelenlebens geschaut werden.",
        "Man kann aber noch durch besondere Empfindungen, welche man ausbil­det, diesem Erleben eine Hilfe zuführen. - Im gewöhnli­chen Erleben innerhalb der Sinnenwelt stellt man sich zu dem, was man als sein Schicksal empfindet, so, daß man das eine als sympathisch, das andre als antipathisch empfindet."
      ],
      [
        "Eine Selbstbesinnung, welche sich selbst gegenüber ganz unbefangen sein kann, wird sich gestehen müssen, daß die hier in Betracht kommenden Sympathien und Antipathien zu den stärksten gehören, welche der Mensch empfinden kann.",
        "Eine gewöhnliche Überlegung etwa von der Art, daß doch alles notwendig sei im Leben, daß man sein Schicksal ertragen müsse, kann zwar sehr weit führen für eine gelas­sene Lebensstimmung."
      ],
      [
        "Um aber für ein Erfassen des wah­ren Menschenwesens etwas zu erzielen, ist noch mehr not­wendig.",
        "Die gekennzeichnete Überlegung wird dem See­lenleben die besten Dienste leisten; doch wird man oft be­merken können, daß dasjenige, was man an Sympathien und Antipathien in der angegebenen Richtung abgestreift hat, nur verschwunden ist für das unmittelbare Bewußt­sein."
      ],
      [
        "Es hat sich in die tieferen Gründe des Menschenwe­sens zurückgezogen und lebt sich aus als Seelenstimmung, oder auch als Abspannungs- oder sonstige Gefühle des Lei­bes.",
        "Wahre Gleichmütigkeit gegenüber dem Schicksale erlangt"
      ],
      [
        "man nur, wenn man auf diesem Felde sich genau so verhält wie mit dem wiederholten, verstärkten Hingeben an Gedanken oder Empfindungen zur Seelenverstärkung im allgemeinen.",
        "Es genügt nicht die Überlegung, welche es bis zur Verstandeseinsicht bringt, sondern es bedarf eines intensiven Zusammenlebens mit solcher Überlegung, eines durch Zeiten dauernden Festhaltens derselben in der Seele mit gleichzeitigem Entfernthalten der Sinneserlebnisse und der übrigen Lebenserinnerungen."
      ],
      [
        "Durch solche Übung kommt man zu einer gewissen Grund-Seelenstimmung ge­genüber seinem Lebensschicksal.",
        "Man kann gründlich aus sich heraustreiben die Antipathien und Sympathien auf die­sem Gebiete und kann zuletzt alles, was dem Menschen ge­schieht, an ihn herankommen sehen, wie man als völlig äu­ßerer Beobachter einen Wasserstrahl über einen Felsen fal­len und unten aufschlagen sieht."
      ],
      [
        "Es ist damit nicht gesagt, daß man auf solche Art dazu gelangen solle, gefühllos sei­nem Schicksale gegenüberzustehen.",
        "Wer dazu kommt, mit Gleichgültigkeit auf alles zu sehen, was mit ihm geschieht, der ist ganz gewiß auf keinem gedeihlichen Wege."
      ],
      [
        "Man steht aber doch nicht anteilslos der Außenwelt gegen­über in bezug auf dasjenige, was die eigene Seele nicht schicksalsmäßig berührt.",
        "Man sieht, was vor den Augen sich abspielt, mit Freude oder mit Abneigung."
      ],
      [
        "Nicht An­teilslosigkeit am Leben soll der nach übersinnlicher Er­kenntnis Strebende suchen, sondern Umwandlung des An­teils, welchen das «Ich» in bezug auf alles zunächst hat, was es schicksalsmäßig berührt.",
        "Es kann durchaus vorkommen, daß durch diese Umwandlung die Lebhaftigkeit des Ge­fühlswesens sogar verstärkt, nicht abgeschwächt wird."
      ],
      [
        "Im gewöhnlichen Leben pressen sich über manches die ,Tränen"
      ],
      [
        "in die Augen, was die eigne Seele betrifft in schicksalsmäßi­ger Art.",
        "Man kann sich aber auch zu dem Gesichtspunkt durchringen, daß man das gleiche lebhafte Gefühl seinem eigenen Mißgeschick gegenüber hat, das man empfindet, wenn dasselbe einen andern Menschen trifft.",
        "Es gelangt der Mensch leichter zu einer solchen Art des Erlebens in bezug auf die Vorfälle, die ihn schicksalsmäßig treffen, als zum Beispiele in bezug auf die eigenen Fähigkeiten.",
        "Der Ge­danke ist denn doch nicht so leicht erreichbar, der sich ebenso in Freude auslebt, wenn ein anderer eine Fähigkeit hat, als wenn man diese selbst besitzt.",
        "Wenn Selbstbesin­nung vorzudringen sucht bis in die tiefsten Seelengründe, so kann da manches entdeckt werden an selbstischer Freu­de über so manches, was man selbst kann.",
        "Ein intensives, wiederholtes (meditatives) Zusammenleben mit dem Ge­danken, daß es in vieler Beziehung für den Gang des Men­schenlebens doch gleich ist, ob man selbst, oder ob ein and­rer etwas kann, vermag weit zu führen in bezug auf wahre Gelassenheit gegenüber dem, was man als innerstes Lebens-schicksal empfindet. - Es kann solche innere gedankenkräf­tige Verstärkung des Seelenlebens, wenn sie richtig ange­stellt wird, nur nie dazu führen, daß man das Gefühl für sei­ne Fähigkeiten bloß abstumpft: man verwandelt es viel­mehr.",
        "Man empfindet die Notwendigkeit, sich diesen Fä­higkeiten entsprechend zu verhalten."
      ],
      [
        "Und damit ist schon hingedeutet auf die Richtung, wel­che eine solche gedankenkräftige Verstärkung des Seelen­lebens nimmt.",
        "Man lernt in sich etwas erkennen, was der Seele im eigenen Innern als ein zweites Wesen erscheint.",
        "Besonders offenbart sich dies, wenn man damit die Gedan­ken verbindet, welche zeigen, wie man im gewöhnlichen"
      ],
      [
        "Leben dies oder jenes im Schicksal herbeiführt.",
        "Man kann doch wahrnehmen, dieses oder jenes wäre mit dir nicht ge­schehen, wenn du selbst in einer früheren Zeit nicht dich in einer gewissen Art verhalten hättest."
      ],
      [
        "Was dem Menschen heute geschieht, ergibt sich ja vielfach aus dem, was er ge­stern getan hat.",
        "Man kann nun mit dem Ziele, sein Seelen­erleben weiter zu führen, als es in einem gewissen Zeit­punkt ist, einen Rückblick anstellen in das bisherige Erle­ben."
      ],
      [
        "Man kann dabei alles aufsuchen, welches zeigt, wie man spätere Schicksalsvorfälle vorher selbst vorbereitet hat.",
        "Man kann versuchen, mit einem solchen Rückblick auf das Leben bis zu jenem Zeitpunkte zu kommen, in welchem beim Kinde das Bewußtsein so erwacht, daß es sich im spä­teren Leben an das erinnert, was es erlebt hat."
      ],
      [
        "Stellt man einen solchen Rückblick so an, daß man mit ihm die Seelenstimmung verbindet, welche die gewöhnlichen selbstischen Sympathien und Antipathien mit schicksalsmäßigen Vorfäl­len ausschaltet, so steht man, wenn man erinnerungsmäßig den bezeichneten Zeitpunkt des Kindeslebens erreicht, sich so gegenüber, daß man sich sagt: da hat wohl die Möglich­keit erst begonnen, daß du dich in dir fühlst und an deinem Seelenleben bewußt arbeitest; dieses dein «Ich» war aber auch vorher da, es hat zwar nicht wissend in dir gearbeitet, aber dich sogar zu deiner Wissensfähigkeit wie zu allem an­dern, wovon du weißt, erst gebracht.",
        "Was keine verstan­desmäßige Überlegung erkennen kann, das führt die ge­schilderte Stellung zu dem eignen Lebensschicksale herbei."
      ],
      [
        "Man lernt auf die Schicksalsvorfälle blicken; mit Gelassen­heit; man sieht sie unbefangen an sich herantreten; aber man erschaut sich selbst in der Wesenheit, welche diese Vorfälle heranbringt.",
        "Und wenn man sich in solcher Art"
      ],
      [
        "schaut, so stellen sich der Seele die Bedingungen des eignen Schicksals, die schon mit der Geburt gegeben sind, verbun­den mit dem eigenen Selbst dar.",
        "Man ringt sich durch, zu sagen, wie du an dir gearbeitet hast in der Zeit, nachdem dein Bewußtsein erwacht ist, so hast du auch schon an dir gearbeitet, bevor dein gegenwärtiges Bewußtsein erwacht ist."
      ],
      [
        "Ein solches Sich-Hindurcharbeiten zu einem überge­ordneten Ichwesen in dem gewöhnlichen Ich führt nicht nur dazu, sich sagen zu können, mein Gedanke bringt mich dazu, ein solches übergeordnetes Ich theoretisch zu ersin­nen, sondern es führt dazu, das lebendige Wesen dieses «Ich» in seiner Wirklichkeit als Macht in sich zu erfühlen, und das gewöhnliche Ich als ein Geschöpf dieses Anderen in sich zu empfinden.",
        "Dieses Fühlen ist ein wahrhafter An­fang des Schauens der Geistwesenheit der Seele."
      ],
      [
        "Und wenn es zu nichts führt, so liegt das nur daran, daß man es beim Anfang bewenden läßt.",
        "Dieser Anfang kann ein kaum be­merkbares, dumpfes Empfinden sein.",
        "Er wird dies vielleicht lange bleiben.",
        "Doch wenn man stark und kräftig das weiter verfolgt, was zu diesem Anfang geführt hat, bringt man es zuletzt zum Schauen der Seele als Geistwesenheit."
      ],
      [
        "Und wer es zu diesem Schauen gebracht hat, der findet es ganz be­greiflich, wenn jemand, der keine Erfahrung auf diesem Gebiete sich verschafft hat, sagt, derjenige, der solches zu schauen glaubt, habe sich nur durch seelisches Gebahren zur Einbildung - Autosuggestion - des übergeordneten Ich gebracht.",
        "Doch weiß der mit solchem Schauen Ausgerü­stete auch, daß ein so gearteter Einwand nur von diesem Fehlen der Erfahrung herrühren kann."
      ],
      [
        "Denn wer im Ern­ste das Geschilderte durchmacht, der eignet sich zugleich auch die Fähigkeit an, seine Einbildungen von Wirklichkeiten"
      ],
      [
        "unterscheiden zu können.",
        "Die inneren Erlebnisse und Betätigungen, die auf solcher Seelenwanderschaft notwen­dig sind, wenn sie eine richtige sein soll, führt dazu, gegen sich selbst in bezug auf Einbildung und Wirklichkeit die strengste Vorsicht anzuwenden.",
        "Man wird, wenn zielvoll angestrebt wird, in dem übergeordneten «Ich» sich als Geistwesen zu erleben, das Haupterlebnis in demjenigen sehen, was zu Anfang dieser Meditation charakterisiert ist, und das an zweiter Stelle Angeführte als eine Hilfe der See­lenwanderschaft anerkennen."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "SIEBENTE MEDITATION",
    "paragraphs": [
      "SIEBENTE MEDITATION",
      "Der Meditierende versucht Vorstellungen zu bilden über die Art",
      "des Erlebens in übersinnlichen Welten",
      "Die Erlebnisse, welche sich für die Seele als notwendig zeig­ten, wenn sie in die übersinnlichen Welten vordringen will, können abschreckend für manchen Menschen erscheinen. Ein solcher kann sich sagen, er wisse nicht, was sich für ihn ergebe, wenn er sich in diese Vorgänge wagt, und wie er sie ertragen werde. Unter dem Einflusse einer solchen Empfin­dung entsteht auch leicht der Gedanke, es sei besser, nicht künstlich einzugreifen in den Entwicklungsgang der Seele, sondern sich ruhig der unbewußt bleibenden Führung zu überlassen und abzuwarten, wohin diese im Laufe der Zu­kunft das Menschen-Innere bringen werde. Einen solchen Gedanken wird jedoch derjenige immer zurückdrängen müssen, der in sich den andren recht beleben kann, daß es im Menschenwesen naturgemäß liegt, sich selbst vorwärts zu bringen, und daß es bedeuten würde, Kräfte, die in der Seele ihrer Entfaltung harren, pflichtwidrig verdorren las­sen, wenn man sich um sie nicht bekümmerte. Die Kräfte der Selbstentwickelung liegen in jeder Menschenseele; und es kann keine einzige geben, welche die Stimme nach Ent­faltung dieser Kräfte nicht hören wollte, wenn sie von ihr und ihrer Bedeutung in irgendeiner Art etwas zu erfahren vermag.",
      "Es wird sich auch niemand von dem Aufstieg in die hö­hern Welten abhalten lassen, wenn er sich zu den Vorgän­gen, welche er durchzumachen hat, nicht von vorneherein in ein unrichtiges Verhältnis bringt. Diese Vorgänge sind so, wie sie sich - in den vorangegangenen Meditationen -",
      "darstellten. Und wenn man sie durch Worte ausdrückt, die ja nur dem gewöhnlichen Menschenleben entnommen sein können, dann können sie nur in dieser Art richtig ausge­drückt werden. Denn Erlebnisse des übersinnlichen Er­kenntnisweges stellen sich eben zur menschlichen Seele so, daß sie ganz gleich dem sind, was zum Beispiele ein hoch­gesteigertes Einsamkeitsgefühl, ein Sich-Fühlen wie über einem Bodenlosen schwebend, und dergleichen für die Menschenseele bedeuten kann. In dem Erleben solcher Empfindungen erzeugen sich die Kräfte zum Erkenntnis-weg. Sie sind die Keime für die Früchte der übersinnlichen Erkenntnis. Es tragen gewissermaßen alle diese Erlebnisse etwas in sich, das in ihnen tief verborgen liegt. Wenn sie dann durchlebt werden, so wird dieses Verborgene zur voll­sten Spannung gebracht; es sprengt etwas das Einsamkeits­gefühl, das wie eine Hülle um dieses «Etwas» ist, und dringt hervor im Seelenleben als ein Mittel der Erkenntnis.",
      "Man muß aber in Betracht ziehen, daß, wenn der rechte Weg eingeschlagen wird, hinter jedem solchen Erlebnis sich sogleich ein anderes einstellt. Es geschieht das so, daß, wenn das eine da ist, das andre nicht ausbleiben kann. Zu dem, was man zu ertragen hat, kommt sogleich die Kraft hinzu, das Vorkommnis wirklich zu ertragen, wenn man nur auf diese Kraft in Ruhe sich besinnen will, und sich die Zeit läßt, um dasjenige auch zu bemerken, was sich in der Seele offenbaren will. Wenn sich ein Peinigendes einstellt, und zugleich das sichere Gefühl in der Seele lebt, daß es Kräfte gibt, welche die Pein ertragen lassen, und mit denen man sich verbinden kann, dann kommt es dahin, daß man sich zu den Erlebnissen, die unerträglich wären, wenn sie im Folgelauf des gewöhnlichen Lebens sich einstellten, in solcher",
      "Art verhält, wie wenn man bei allem so Erlebten sein eigener Zuschauer wäre. Dies macht, daß Menschen, wel­che auf dem Wege zur übersinnlichen Erkenntnis sind, in ihrem Innern das Auf- und Abwogen mancher Gefühiswo­gen durchleben, und doch in völligem Gleichmut innerhalb des Sinnenlebens sich zeigen. - Es ist ja durchaus die Mög­lichkeit vorhanden, daß Erlebnisse, welche im Innern sich vollziehen, auch der Stimmung des äußeren Lebens in der Sinnenwelt sich mitteilen, so daß man dann mit dem Leben und mit sich selbst zeitweilig nicht so zustande kommt, wie man es in dem Leben konnte, das vor dem Erkenntniswege liegt. Man ist dann darauf angewiesen, aus dem, was man sich im Innern bereits errungen hat, die Kräfte zu holen, die bewirken, daß man wieder zurechtkommt. Und es kann keine Lage auf dem rechtmäßig beschrittenen Erkenntnis-wege geben, in welcher dies nicht möglich wäre.",
      "Der beste Erkenntnisweg wird immer der sein, welcher zur übersinnlichen Welt durch die Verstärkung oder Ver­dichtung des Seeleniebens mittels innerer Versenkung ge­dankenkräftig oder empfindungskräftig führt. Es kommt dabei nicht darauf an, den Gedanken oder die Empfindung so zu erleben, wie man dies tut, um sich innerhalb der Sin­neswelt zurechtzufinden, sondern darauf, daß man intensiv mit und in dem Gedanken oder der Empfindung lebt und alle seine Seelenkräfte in sie zusammenzieht. Sie sollen für die Zeit der inneren Versenkung das Bewußtsein ganz allein ausfüllen. Man denke zum Beispiel an einen Gedanken, wel­cher der Seele irgendeine Überzeugung gebracht hat; man lasse zunächst aus dem Spiele, was er an Überzeugungs­wert hat und lebe immer wieder mit ihm, so daß man mit ihm ganz eins werde. Es bedarf durchaus nicht eines Gedankens,",
      "welcher sich auf die Dinge der höhern Weltord­nung bezieht, obwohl ein solcher im erhöhten Maße brauch­bar ist. Es kann zur inneren Versenkung auch ein Gedanke genommen werden, welcher ein gewöhnliches Erlebnis ab-bildet. Fruchtbar sind Empfindungen, welche Vorsätze zum Beispiel in bezug auf Liebestaten darstellen, und die man in sich zum menschlich wärmsten und aufrichtigsten Erleben entzündet. Wirksam, wenn es sich vor allem um Erkennt­nis handelt, sind aber sinnbildliche Vorstellungen, welche am Leben gewonnen werden, oder welchen man sich hin­gibt auf den Rat solcher Menschen, die gewissermaßen auf diesem Gebiet sachverständig sind, weil sie die Fruchtbar­keit der angewendeten Mittel kennen aus dem, was sich für sie selbst durch dieselben ergeben hat.",
      "Durch solche Versenkung, die zu einer Lebensgewohn­heit, ja Lebensbedingung werden muß, wie das Atmen eine Bedingung des Leibeslebens ist, wird man die Kräfte der Seele zusammenziehen und im Zusammenziehen verstär­ken. Es muß nur gelingen, sich für die Zeiten der inneren Versenkung ganz so zu halten, daß keine äußeren Sinneseindrücke und auch keine Erinnerungen an solche in das Seelenleben hereinspielen. Auch die Erinnerungen an alles, was man im gewöhnlichen Leben erfahren hat, was der Seele Freude oder Schmerz macht, muß schweigen, so daß diese ganz allein demjenigen hingegeben ist, wovon man selbst will, daß es in ihr sei. Die Kräfte zur übersinnlichen Er­kenntnis erwachsen nur aus dem in rechter Art, was man sich so errungen hat durch innere Versenkungen, deren In­halt und Form man durch Aufwendung eigener Seelenmacht herbeigeführt hat. Nicht darauf kommt es an, woher man den Inhalt der Versenkung hat; man kann ihn von",
      "einem auf dem Gebiete Sachverständigen haben, oder auch aus der geisteswissenschaftlichen Literatur; man muß ihn nur selbst zum inneren Erleben machen und sich nicht zur Versenkung von dem nur bestimmen lassen wollen, was der eigenen Seele entstammt, was man selbst für den besten Versenkungsinhalt hält. Ein solcher hat deshalb geringe Kraft, weil sich die Seele von vorneherein ihm verwandt fühlt und so nicht die nötigen Anstrengungen machen kann, um mit ihm erst eins zu werden. In dieser Anstrengung liegt aber das Wirksame für die übersinnlichen Erkenntniskräfte, nicht in dem Einssein mit dem Inhalt der Versen­kung als solcher.",
      "Man kann zu übersinnlichem Schauen auch auf andre Art gelangen. Es können Menschen durch ihre ganze Veranla­gung zu innerer Vertiefung, zu inbrünstigem Erleben kom­men. Dadurch können sich übersinnliche Erkenntnis kräfte in ihrer Seele loslösen. Es können sich solche Kräfte oft wie plötzlich in Seelen ergeben, von denen es scheinen könnte, als ob sie zu derartigem Erleben durchaus nicht vorherbestimmt seien. Auf die mannigfaltigste Art kann übersinnliches Seelenleben eintreten; doch zu einem Erle­ben, das sich beherrscht, wie der Mensch sich beherrscht in seinem gewöhnlichen Sinnessein, kann es nur kommen, wenn der geschilderte Erkenntnisweg beschritten wird. Je­des andre Hereinbrechen der übersinnlichen Welt in die Seelenerlehnisse wird dazu führen, daß sie sich wie durch Zwang einstellen und der Mensch an sie sich verliert, oder daß er sich über ihren Wert, über ihre wahre Bedeutung innerhalb der wirklichen übersinnlichen Welt allen mögli­chen Täuschungen hingibt.",
      "Man muß sich durchaus vor Augen halten, daß sich die",
      "Seele auf dem übersinnlichen Erkenntniswege wandelt. Es kann vorkommen, daß man für das Leben im Sinnensein durchaus nicht so veranlagt ist, sich allen möglichen Täu­schungen und Illusionen hinzugeben; daß man aber, so­bald man die übersinnliche Welt betritt, in der leichtgläu­bigsten Weise sich solchen Täuschungen oder Illusionen hingibt. Auch das kann sich ereignen, daß man im Sinnen­sein ganz guten gesunden Wahrheits sinn hat, der sich sagt:",
      "du darfst nicht dasjenige über eine Sache oder einen Vor­gang glauben, was nur deinen Selbstsinn befriedigt; und trotzdem dies der Fall ist, kann eine solche Seele dazu kom­men, in der übersinnlichen Welt dasjenige zu schauen, was diesem Selbstsinn angemessen ist. Man muß bedenken, wie dieser Selbstsinn an dem beteiligt ist, was man erschaut. Man schaut dasjenige, worauf sich dieser Selbstsinn nach seiner Neigung richtet. Man weiß nicht, daß er es ist, wel­cher den geistigen Blick lenkt. Und es ist dann ganz selbst­verständlich, daß man das Geschaute für Wahrheit hin­nimmt. Schutz kann da nur gewähren, daß man sich durch gute Selbstbesinnung, durch den energischen Willen zur Selbsterkenntnis auf dem übersinnlichen Erkenntniswege stets mehr und mehr bereit macht, wirklich an der eigenen Seele zu bemerken, wieviel von Selbstsinn vorhanden ist, und wo er spricht. Dann wird man, wenn man sich die Mög­lichkeit der eignen Seele, da oder dort dem Selbstsinn zu verfallen, in innerer Versenkung schonungslos und ener­gisch vorführt, allmählich loskommen von der Führung des Selbstsinnes.",
      "Zu wahrer ungehinderter Beweglichkeit der Seele in den höheren Welten gehört es, daß sich diese eine Anschauung aneigne, wie anders gewisse seelische Eigenschaften der",
      "geistigen Welt gegenüberstehen als der sinnlichen. Es tritt dies besonders deutlich zutage, wenn der Blick auf die mo­ralischen Seeleneigenschaften gelenkt wird. Innerhalb des Sinnenseins sind zu unterscheiden die Naturgesetze und die moralischen Gesetze. Man kann, wenn man sich den Ver­lauf von Naturvorgängen erklären will, sich nicht an mora­lische Vorstellungen halten. Eine Giftpflanze erklärt man nach Naturgesetzen und verurteilt nicht moralisch, daß sie giftig ist. Man wird sich selbst darüber klar sein, daß man für die Tierwelt höchstens von Anklängen an das Morali­sche sprechen kann, daß aber eine im echten Sinne morali­sche Beurteilung nur eine Störung dessen bewirkte, was wahrhaft in Betracht kommt. In den Zusammenhängen des menschlichen Lebens beginnt die moralische Beurteilung über den Wert des Daseins die Bedeutung zu haben. Sie ist etwas, wovon der Mensch selbst stets seinen Wert abhän­gig macht, wenn er dazu gelangt, über sich unbefangen zu urteilen. Niemand kann es aber bei richtiger Betrachtung des Sinnenseins einfallen, die Naturgesetze als etwas den Moralgesetzen Gleiches, ja auch nur Ähnliches anzusehen.",
      "Sobald man die höheren Welten betritt, wird das anders. Je geistiger die Welten sind, welche man betritt, desto mehr fallen Moralgesetze und das, was man für diese Welten Na­turgesetze nennen kann, zusammen. Im Sinnensein ist man sich dessen bewußt, daß man für dieses Sein im uneigent­lichen Sinne spricht, wenn man von einer bösen Tat sagt, sie brenne in der Seele. Man weiß, daß das natürliche Bren­nen etwas ganz anderes ist. Eine ähnliche Scheidung be­steht für die übersinnlichen Welten nicht. Haß oder Neid sind da zugleich Kräfte, welche so wirken, daß man die ent­sprechenden Wirkungen als die Naturvorgänge dieser Welten",
      "bezeichnen kann. Haß oder Neid bewirken da, daß das gehaßte oder beneidete Wesen auf den Hasser oder Neider wie verzehrend, auslöschend wirkt, so daß sich Zerstö­rungsprozesse bilden, die dem geistigen Wesen nachteilig sind.",
      "Liebe wirkt in den geistigen Welten so, daß man die Wirkung wie Wärmeausstrahlung, die hervorbringend, för­dernd ist, ansprechen muß. - Schon am menschlichen ele­mentarischen Leibe kann dies bemerkt werden. Innerhalb der Sinnenwelt muß die Hand, welche eine unmoralische Tat verrichtet, in ihrer Verrichtung nach Naturgesetzen genau so erklärt werden wie diejenige, welche dem mora­lischen Handeln dient.",
      "Gewisse elementarische Teile des Menschen bleiben aber unentwickelt, wenn ihnen entspre­chende moralische Empfindungen nicht vorhanden sind. Und man hat unvollkommene Ausbildungen von elemen­tarischen Organen auf moralische Eigenschaften zurückzu­führen ganz in solcher Art, wie man nach Naturgesetzen im Sinnensein Naturvorgänge durch Naturgesetze erklärt.",
      "Man darf nur niemals etwa von der unvollkommenen Entwicke­lung eines sinnlichen Organs auf die unvollkommene Ent­faltung des entsprechenden Teiles im elementarischen Lei­be schließen. Dessen muß man sich immer bewußt sein, daß für die verschiedenen Welten auch ganz verschiedene Ar­ten von Gesetzmäßigkeit gelten.",
      "Ein Mensch kann ein phy­sisches Organ unvollkommen ausgebildet haben; das ent­sprechende elementarische Organ kann dabei nicht etwa bloß normal vollkommen sein, sondern es kann sogar in dem Maße vollkommen sein, als das physische unvollkom­men ist.",
      "Bedeutsam tritt der Unterschied der übersinnlichen Wel­ten von der sinnlichen auch bei allem auf, was mit den Vorstellungen",
      "des «Schönen» und «Häßlichen» zusammen­hängt. Die Art, wie man diese Begriffe im Sinnensein an­wendet, verliert alle Bedeutung, sobald man die übersinn­lichen Welten betritt. Ein «Schönes» kann da nur, wenn man sich auf die Bedeutung des Wortes im Sinnensein be­sinnt, ein solches Wesen genannt werden, dem es gelingt, alles, was es in sich erlebt, auch den andern Wesen seiner Welt zu offenbaren, so daß diese andern Wesen an seinem ganzen Erleben teilnehmen können. Die Fähigkeit, sich ganz mit allem, was im Innern ist, zu offenbaren, und nichts in sich verborgen halten zu müssen, könnte als «schön»in den höheren Welten bezeichnet werden. Und es fällt da die­ser Begriff völlig zusammen mit dem von rückhaltloser Auf­richtigkeit, von ehrlichem Darleben dessen, was ein Wesen in sich trägt. «Häßlich» könnte das genannt werden, was den innern Inhalt, den es hat, nicht in der äußern Erschei­nung offenbaren will, was das eigne Erleben in sich zurückhält und für andre Wesen sich in bezug auf gewisse Eigen­schaften verbirgt. Es entzieht sich ein solches Wesen seiner geistigen Umgebung. Es fällt dieser Begriff zusammen mit dem von unaufrichtigem Sich-Offenbaren. Lügen und Häßlichsein ist in der geistigen Welt als Wirklichkeit dasselbe, so daß ein häßlich auftretendes Wesen ein lügnerisches ist.",
      "Auch das, was man im Sinnensein als Begierden, Wün­sche erkennt, tritt mit ganz andrer Bedeutung in der geisti­gen Welt auf Solche Begierden, welche aus der inneren Na­tur der Menschenseele in der Sinnenwelt entspringen, gibt es in der geistigen Welt nicht. Was man da Begierden nen­nen kann, entzündet sich an dem, was außer dem Wesen geschaut wird. Ein Wesen, das empfinden muß, es habe ir­gendeine Eigenschaft nicht, die es seiner Natur nach haben",
      "sollte, schaut ein andres Wesen, das diese Eigenschaft hat. Und es kann gar nicht anders, als beständig dieses andre Wesen vor sich zu haben. Wie in der Sinnenwelt naturge­mäß das Auge Sichtbares sieht, so führt der Mangel einer Eigenschaft ein Wesen der übersinnlichen Welt stets in die Nähe eines entsprechenden andern Wesens, das die in Be­tracht kommende Vollkommenheit hat. Und der Anblick dieses Wesens wird ein immerwährender Vorwurf, der als wirkliche Kraft wirkt, so daß das Wesen, welches mit dem Fehler behaftet ist, durch den Anblick die Begierde hat, den Fehler an sich auszubessern. Es ist dies ein ganz andersarti­ges Erlebnis, als es eine Begierde im Sinnensein ist.. - Das freie Wollen wird durch solche Verhältnisse in der geisti­gen Welt nicht beeinträchtigt. Ein Wesen kann sich wehren gegen das, was ein Anblick in ihm hervorrufen will. Dann wird es allmählich erreichen, daß es aus der Nähe des vor­bildlichen Wesens hinwegkommt. Es wird jedoch die Fol­ge davon sein, daß ein solches sein Vorbild abwehrendes Wesen sich selbst in Welten versetzt, in welchen es schlech­tere Daseinsbedingungen hat, als die gewesen wären, die ihm gegeben waren in der Welt, für die es gewissermaßen vorbestimmt ist.",
      "Dies alles zeigt der menschlichen Seele, daß nät dem Be­treten der übersinnlichen Welten die Vorstellungswelt umgebildet werden muß. Es müssen Begriffe umgewandelt, erweitert, mit anderen verschmolzen werden, wenn man die übersinnliche Welt richtig beschreiben will. - Daher kommt es, daß Beschreibungen der übersinnlichen Welten, welche die für das Sinnensein geprägten Begriffe ohne wei­tere Veränderung gebrauchen wollen, immer etwas Unzu­treffendes haben. - Man kann sich darauf besinnen, daß es",
      "aus einem richtigen menschlichen Gefühle hervorgeht, Be­griffe, die für die übersinnlichen Welten erst ihre volle Be­deutung haben, innerhalb des Sinnenseins mehr oder weni­ger sinnbildlich, oder auch als wirklich die Sache bezeich­nend, zu gebrauchen. So kann jemand das Lügnerische wirklich als häßlich empfinden.",
      "Gegenüber dem, wie es mit diesem Begriffe in der übersinnlichen Welt steht, ist aber ein solcher Wortgebrauch im Sinnensein doch nur ein An­klang, der sich ergibt, weil alle Welten Beziehungen zuein­ander haben, und diese Beziehungen dunkel gefühlt, unbe­wußt gedacht im Sinnensein werden. Doch muß berück­sichtigt werden, daß im Sinnensein das Lügnerische, das man als häßlich empfindet, nicht häßlich zu sein braucht in seiner äußeren Erscheinung.",
      "Daß man sogar die Vorstel­lungen durcheinander werfen würde, wenn man ein Häßli­ches in der sinnlichen Natur aus einem Lügnerischen erklä­ren wollte. Für die übersinnliche Welt ist es aber so, daß das Lügnerische, wenn es wahr gesehen wird, in seiner Of­fenbarung sich als häßlich aufdrängt. - Auch hier kommen wieder Täuschungen in Betracht, vor denen man sich zu hüten hat.",
      "Es kann der Seele in der übersinnlichen Welt ein Wesen entgegentreten, das mit Recht als böse bezeichnet werden muß, und welches doch in einem solchen Bilde sich offenbart, welches man «schön» nennt, wenn man die Vor­stellung vom «Schönen» anwendet, welche man aus dem Sinnensein mitbringt. In einem solchen Falle wird man erst richtig schauen, wenn man bis zum Innengrunde des We­sens durchdringt.",
      "Dann wird man erleben, wie die «schö­ne» Offenbarung eine Maske ist, die nicht dem Wesen ent­spricht; und man wird dann das, was man nach Vorstellun­gen aus dem Sinnensein als «schön» empfinden wollte, mit",
      "besonderer Stärke als Häßlichkeit ansprechen. Und in dem Augenblicke, wo dies gelingt, ist das «böse» Wesen auch nicht mehr imstande, die «Schönheit» vorzutäuschen. Es muß sich für einen solchen Beschauer in seiner wahren Ge­stalt enthüllen, die ein unvollkommener Ausdruck dessen nur sein kann, was es im Innern ist. An solchen Erscheinun­gen der übersinnlichen Welt wird es besonders anschaulich, wie sich die menschlichen Vorstellungen beim Betreten die­ser Welt wandeln müssen."
    ],
    "sentences": [
      [
        "SIEBENTE MEDITATION"
      ],
      [
        "Der Meditierende versucht Vorstellungen zu bilden über die Art"
      ],
      [
        "des Erlebens in übersinnlichen Welten"
      ],
      [
        "Die Erlebnisse, welche sich für die Seele als notwendig zeig­ten, wenn sie in die übersinnlichen Welten vordringen will, können abschreckend für manchen Menschen erscheinen.",
        "Ein solcher kann sich sagen, er wisse nicht, was sich für ihn ergebe, wenn er sich in diese Vorgänge wagt, und wie er sie ertragen werde.",
        "Unter dem Einflusse einer solchen Empfin­dung entsteht auch leicht der Gedanke, es sei besser, nicht künstlich einzugreifen in den Entwicklungsgang der Seele, sondern sich ruhig der unbewußt bleibenden Führung zu überlassen und abzuwarten, wohin diese im Laufe der Zu­kunft das Menschen-Innere bringen werde.",
        "Einen solchen Gedanken wird jedoch derjenige immer zurückdrängen müssen, der in sich den andren recht beleben kann, daß es im Menschenwesen naturgemäß liegt, sich selbst vorwärts zu bringen, und daß es bedeuten würde, Kräfte, die in der Seele ihrer Entfaltung harren, pflichtwidrig verdorren las­sen, wenn man sich um sie nicht bekümmerte.",
        "Die Kräfte der Selbstentwickelung liegen in jeder Menschenseele; und es kann keine einzige geben, welche die Stimme nach Ent­faltung dieser Kräfte nicht hören wollte, wenn sie von ihr und ihrer Bedeutung in irgendeiner Art etwas zu erfahren vermag."
      ],
      [
        "Es wird sich auch niemand von dem Aufstieg in die hö­hern Welten abhalten lassen, wenn er sich zu den Vorgän­gen, welche er durchzumachen hat, nicht von vorneherein in ein unrichtiges Verhältnis bringt.",
        "Diese Vorgänge sind so, wie sie sich - in den vorangegangenen Meditationen -"
      ],
      [
        "darstellten.",
        "Und wenn man sie durch Worte ausdrückt, die ja nur dem gewöhnlichen Menschenleben entnommen sein können, dann können sie nur in dieser Art richtig ausge­drückt werden.",
        "Denn Erlebnisse des übersinnlichen Er­kenntnisweges stellen sich eben zur menschlichen Seele so, daß sie ganz gleich dem sind, was zum Beispiele ein hoch­gesteigertes Einsamkeitsgefühl, ein Sich-Fühlen wie über einem Bodenlosen schwebend, und dergleichen für die Menschenseele bedeuten kann.",
        "In dem Erleben solcher Empfindungen erzeugen sich die Kräfte zum Erkenntnis-weg.",
        "Sie sind die Keime für die Früchte der übersinnlichen Erkenntnis.",
        "Es tragen gewissermaßen alle diese Erlebnisse etwas in sich, das in ihnen tief verborgen liegt.",
        "Wenn sie dann durchlebt werden, so wird dieses Verborgene zur voll­sten Spannung gebracht; es sprengt etwas das Einsamkeits­gefühl, das wie eine Hülle um dieses «Etwas» ist, und dringt hervor im Seelenleben als ein Mittel der Erkenntnis."
      ],
      [
        "Man muß aber in Betracht ziehen, daß, wenn der rechte Weg eingeschlagen wird, hinter jedem solchen Erlebnis sich sogleich ein anderes einstellt.",
        "Es geschieht das so, daß, wenn das eine da ist, das andre nicht ausbleiben kann.",
        "Zu dem, was man zu ertragen hat, kommt sogleich die Kraft hinzu, das Vorkommnis wirklich zu ertragen, wenn man nur auf diese Kraft in Ruhe sich besinnen will, und sich die Zeit läßt, um dasjenige auch zu bemerken, was sich in der Seele offenbaren will.",
        "Wenn sich ein Peinigendes einstellt, und zugleich das sichere Gefühl in der Seele lebt, daß es Kräfte gibt, welche die Pein ertragen lassen, und mit denen man sich verbinden kann, dann kommt es dahin, daß man sich zu den Erlebnissen, die unerträglich wären, wenn sie im Folgelauf des gewöhnlichen Lebens sich einstellten, in solcher"
      ],
      [
        "Art verhält, wie wenn man bei allem so Erlebten sein eigener Zuschauer wäre.",
        "Dies macht, daß Menschen, wel­che auf dem Wege zur übersinnlichen Erkenntnis sind, in ihrem Innern das Auf- und Abwogen mancher Gefühiswo­gen durchleben, und doch in völligem Gleichmut innerhalb des Sinnenlebens sich zeigen. - Es ist ja durchaus die Mög­lichkeit vorhanden, daß Erlebnisse, welche im Innern sich vollziehen, auch der Stimmung des äußeren Lebens in der Sinnenwelt sich mitteilen, so daß man dann mit dem Leben und mit sich selbst zeitweilig nicht so zustande kommt, wie man es in dem Leben konnte, das vor dem Erkenntniswege liegt.",
        "Man ist dann darauf angewiesen, aus dem, was man sich im Innern bereits errungen hat, die Kräfte zu holen, die bewirken, daß man wieder zurechtkommt.",
        "Und es kann keine Lage auf dem rechtmäßig beschrittenen Erkenntnis-wege geben, in welcher dies nicht möglich wäre."
      ],
      [
        "Der beste Erkenntnisweg wird immer der sein, welcher zur übersinnlichen Welt durch die Verstärkung oder Ver­dichtung des Seeleniebens mittels innerer Versenkung ge­dankenkräftig oder empfindungskräftig führt.",
        "Es kommt dabei nicht darauf an, den Gedanken oder die Empfindung so zu erleben, wie man dies tut, um sich innerhalb der Sin­neswelt zurechtzufinden, sondern darauf, daß man intensiv mit und in dem Gedanken oder der Empfindung lebt und alle seine Seelenkräfte in sie zusammenzieht.",
        "Sie sollen für die Zeit der inneren Versenkung das Bewußtsein ganz allein ausfüllen.",
        "Man denke zum Beispiel an einen Gedanken, wel­cher der Seele irgendeine Überzeugung gebracht hat; man lasse zunächst aus dem Spiele, was er an Überzeugungs­wert hat und lebe immer wieder mit ihm, so daß man mit ihm ganz eins werde.",
        "Es bedarf durchaus nicht eines Gedankens,"
      ],
      [
        "welcher sich auf die Dinge der höhern Weltord­nung bezieht, obwohl ein solcher im erhöhten Maße brauch­bar ist.",
        "Es kann zur inneren Versenkung auch ein Gedanke genommen werden, welcher ein gewöhnliches Erlebnis ab-bildet.",
        "Fruchtbar sind Empfindungen, welche Vorsätze zum Beispiel in bezug auf Liebestaten darstellen, und die man in sich zum menschlich wärmsten und aufrichtigsten Erleben entzündet.",
        "Wirksam, wenn es sich vor allem um Erkennt­nis handelt, sind aber sinnbildliche Vorstellungen, welche am Leben gewonnen werden, oder welchen man sich hin­gibt auf den Rat solcher Menschen, die gewissermaßen auf diesem Gebiet sachverständig sind, weil sie die Fruchtbar­keit der angewendeten Mittel kennen aus dem, was sich für sie selbst durch dieselben ergeben hat."
      ],
      [
        "Durch solche Versenkung, die zu einer Lebensgewohn­heit, ja Lebensbedingung werden muß, wie das Atmen eine Bedingung des Leibeslebens ist, wird man die Kräfte der Seele zusammenziehen und im Zusammenziehen verstär­ken.",
        "Es muß nur gelingen, sich für die Zeiten der inneren Versenkung ganz so zu halten, daß keine äußeren Sinneseindrücke und auch keine Erinnerungen an solche in das Seelenleben hereinspielen.",
        "Auch die Erinnerungen an alles, was man im gewöhnlichen Leben erfahren hat, was der Seele Freude oder Schmerz macht, muß schweigen, so daß diese ganz allein demjenigen hingegeben ist, wovon man selbst will, daß es in ihr sei.",
        "Die Kräfte zur übersinnlichen Er­kenntnis erwachsen nur aus dem in rechter Art, was man sich so errungen hat durch innere Versenkungen, deren In­halt und Form man durch Aufwendung eigener Seelenmacht herbeigeführt hat.",
        "Nicht darauf kommt es an, woher man den Inhalt der Versenkung hat; man kann ihn von"
      ],
      [
        "einem auf dem Gebiete Sachverständigen haben, oder auch aus der geisteswissenschaftlichen Literatur; man muß ihn nur selbst zum inneren Erleben machen und sich nicht zur Versenkung von dem nur bestimmen lassen wollen, was der eigenen Seele entstammt, was man selbst für den besten Versenkungsinhalt hält.",
        "Ein solcher hat deshalb geringe Kraft, weil sich die Seele von vorneherein ihm verwandt fühlt und so nicht die nötigen Anstrengungen machen kann, um mit ihm erst eins zu werden.",
        "In dieser Anstrengung liegt aber das Wirksame für die übersinnlichen Erkenntniskräfte, nicht in dem Einssein mit dem Inhalt der Versen­kung als solcher."
      ],
      [
        "Man kann zu übersinnlichem Schauen auch auf andre Art gelangen.",
        "Es können Menschen durch ihre ganze Veranla­gung zu innerer Vertiefung, zu inbrünstigem Erleben kom­men.",
        "Dadurch können sich übersinnliche Erkenntnis kräfte in ihrer Seele loslösen.",
        "Es können sich solche Kräfte oft wie plötzlich in Seelen ergeben, von denen es scheinen könnte, als ob sie zu derartigem Erleben durchaus nicht vorherbestimmt seien.",
        "Auf die mannigfaltigste Art kann übersinnliches Seelenleben eintreten; doch zu einem Erle­ben, das sich beherrscht, wie der Mensch sich beherrscht in seinem gewöhnlichen Sinnessein, kann es nur kommen, wenn der geschilderte Erkenntnisweg beschritten wird.",
        "Je­des andre Hereinbrechen der übersinnlichen Welt in die Seelenerlehnisse wird dazu führen, daß sie sich wie durch Zwang einstellen und der Mensch an sie sich verliert, oder daß er sich über ihren Wert, über ihre wahre Bedeutung innerhalb der wirklichen übersinnlichen Welt allen mögli­chen Täuschungen hingibt."
      ],
      [
        "Man muß sich durchaus vor Augen halten, daß sich die"
      ],
      [
        "Seele auf dem übersinnlichen Erkenntniswege wandelt.",
        "Es kann vorkommen, daß man für das Leben im Sinnensein durchaus nicht so veranlagt ist, sich allen möglichen Täu­schungen und Illusionen hinzugeben; daß man aber, so­bald man die übersinnliche Welt betritt, in der leichtgläu­bigsten Weise sich solchen Täuschungen oder Illusionen hingibt.",
        "Auch das kann sich ereignen, daß man im Sinnen­sein ganz guten gesunden Wahrheits sinn hat, der sich sagt:"
      ],
      [
        "du darfst nicht dasjenige über eine Sache oder einen Vor­gang glauben, was nur deinen Selbstsinn befriedigt; und trotzdem dies der Fall ist, kann eine solche Seele dazu kom­men, in der übersinnlichen Welt dasjenige zu schauen, was diesem Selbstsinn angemessen ist.",
        "Man muß bedenken, wie dieser Selbstsinn an dem beteiligt ist, was man erschaut.",
        "Man schaut dasjenige, worauf sich dieser Selbstsinn nach seiner Neigung richtet.",
        "Man weiß nicht, daß er es ist, wel­cher den geistigen Blick lenkt.",
        "Und es ist dann ganz selbst­verständlich, daß man das Geschaute für Wahrheit hin­nimmt.",
        "Schutz kann da nur gewähren, daß man sich durch gute Selbstbesinnung, durch den energischen Willen zur Selbsterkenntnis auf dem übersinnlichen Erkenntniswege stets mehr und mehr bereit macht, wirklich an der eigenen Seele zu bemerken, wieviel von Selbstsinn vorhanden ist, und wo er spricht.",
        "Dann wird man, wenn man sich die Mög­lichkeit der eignen Seele, da oder dort dem Selbstsinn zu verfallen, in innerer Versenkung schonungslos und ener­gisch vorführt, allmählich loskommen von der Führung des Selbstsinnes."
      ],
      [
        "Zu wahrer ungehinderter Beweglichkeit der Seele in den höheren Welten gehört es, daß sich diese eine Anschauung aneigne, wie anders gewisse seelische Eigenschaften der"
      ],
      [
        "geistigen Welt gegenüberstehen als der sinnlichen.",
        "Es tritt dies besonders deutlich zutage, wenn der Blick auf die mo­ralischen Seeleneigenschaften gelenkt wird.",
        "Innerhalb des Sinnenseins sind zu unterscheiden die Naturgesetze und die moralischen Gesetze.",
        "Man kann, wenn man sich den Ver­lauf von Naturvorgängen erklären will, sich nicht an mora­lische Vorstellungen halten.",
        "Eine Giftpflanze erklärt man nach Naturgesetzen und verurteilt nicht moralisch, daß sie giftig ist.",
        "Man wird sich selbst darüber klar sein, daß man für die Tierwelt höchstens von Anklängen an das Morali­sche sprechen kann, daß aber eine im echten Sinne morali­sche Beurteilung nur eine Störung dessen bewirkte, was wahrhaft in Betracht kommt.",
        "In den Zusammenhängen des menschlichen Lebens beginnt die moralische Beurteilung über den Wert des Daseins die Bedeutung zu haben.",
        "Sie ist etwas, wovon der Mensch selbst stets seinen Wert abhän­gig macht, wenn er dazu gelangt, über sich unbefangen zu urteilen.",
        "Niemand kann es aber bei richtiger Betrachtung des Sinnenseins einfallen, die Naturgesetze als etwas den Moralgesetzen Gleiches, ja auch nur Ähnliches anzusehen."
      ],
      [
        "Sobald man die höheren Welten betritt, wird das anders.",
        "Je geistiger die Welten sind, welche man betritt, desto mehr fallen Moralgesetze und das, was man für diese Welten Na­turgesetze nennen kann, zusammen.",
        "Im Sinnensein ist man sich dessen bewußt, daß man für dieses Sein im uneigent­lichen Sinne spricht, wenn man von einer bösen Tat sagt, sie brenne in der Seele.",
        "Man weiß, daß das natürliche Bren­nen etwas ganz anderes ist.",
        "Eine ähnliche Scheidung be­steht für die übersinnlichen Welten nicht.",
        "Haß oder Neid sind da zugleich Kräfte, welche so wirken, daß man die ent­sprechenden Wirkungen als die Naturvorgänge dieser Welten"
      ],
      [
        "bezeichnen kann.",
        "Haß oder Neid bewirken da, daß das gehaßte oder beneidete Wesen auf den Hasser oder Neider wie verzehrend, auslöschend wirkt, so daß sich Zerstö­rungsprozesse bilden, die dem geistigen Wesen nachteilig sind."
      ],
      [
        "Liebe wirkt in den geistigen Welten so, daß man die Wirkung wie Wärmeausstrahlung, die hervorbringend, för­dernd ist, ansprechen muß. - Schon am menschlichen ele­mentarischen Leibe kann dies bemerkt werden.",
        "Innerhalb der Sinnenwelt muß die Hand, welche eine unmoralische Tat verrichtet, in ihrer Verrichtung nach Naturgesetzen genau so erklärt werden wie diejenige, welche dem mora­lischen Handeln dient."
      ],
      [
        "Gewisse elementarische Teile des Menschen bleiben aber unentwickelt, wenn ihnen entspre­chende moralische Empfindungen nicht vorhanden sind.",
        "Und man hat unvollkommene Ausbildungen von elemen­tarischen Organen auf moralische Eigenschaften zurückzu­führen ganz in solcher Art, wie man nach Naturgesetzen im Sinnensein Naturvorgänge durch Naturgesetze erklärt."
      ],
      [
        "Man darf nur niemals etwa von der unvollkommenen Entwicke­lung eines sinnlichen Organs auf die unvollkommene Ent­faltung des entsprechenden Teiles im elementarischen Lei­be schließen.",
        "Dessen muß man sich immer bewußt sein, daß für die verschiedenen Welten auch ganz verschiedene Ar­ten von Gesetzmäßigkeit gelten."
      ],
      [
        "Ein Mensch kann ein phy­sisches Organ unvollkommen ausgebildet haben; das ent­sprechende elementarische Organ kann dabei nicht etwa bloß normal vollkommen sein, sondern es kann sogar in dem Maße vollkommen sein, als das physische unvollkom­men ist."
      ],
      [
        "Bedeutsam tritt der Unterschied der übersinnlichen Wel­ten von der sinnlichen auch bei allem auf, was mit den Vorstellungen"
      ],
      [
        "des «Schönen» und «Häßlichen» zusammen­hängt.",
        "Die Art, wie man diese Begriffe im Sinnensein an­wendet, verliert alle Bedeutung, sobald man die übersinn­lichen Welten betritt.",
        "Ein «Schönes» kann da nur, wenn man sich auf die Bedeutung des Wortes im Sinnensein be­sinnt, ein solches Wesen genannt werden, dem es gelingt, alles, was es in sich erlebt, auch den andern Wesen seiner Welt zu offenbaren, so daß diese andern Wesen an seinem ganzen Erleben teilnehmen können.",
        "Die Fähigkeit, sich ganz mit allem, was im Innern ist, zu offenbaren, und nichts in sich verborgen halten zu müssen, könnte als «schön»in den höheren Welten bezeichnet werden.",
        "Und es fällt da die­ser Begriff völlig zusammen mit dem von rückhaltloser Auf­richtigkeit, von ehrlichem Darleben dessen, was ein Wesen in sich trägt.",
        "«Häßlich» könnte das genannt werden, was den innern Inhalt, den es hat, nicht in der äußern Erschei­nung offenbaren will, was das eigne Erleben in sich zurückhält und für andre Wesen sich in bezug auf gewisse Eigen­schaften verbirgt.",
        "Es entzieht sich ein solches Wesen seiner geistigen Umgebung.",
        "Es fällt dieser Begriff zusammen mit dem von unaufrichtigem Sich-Offenbaren.",
        "Lügen und Häßlichsein ist in der geistigen Welt als Wirklichkeit dasselbe, so daß ein häßlich auftretendes Wesen ein lügnerisches ist."
      ],
      [
        "Auch das, was man im Sinnensein als Begierden, Wün­sche erkennt, tritt mit ganz andrer Bedeutung in der geisti­gen Welt auf Solche Begierden, welche aus der inneren Na­tur der Menschenseele in der Sinnenwelt entspringen, gibt es in der geistigen Welt nicht.",
        "Was man da Begierden nen­nen kann, entzündet sich an dem, was außer dem Wesen geschaut wird.",
        "Ein Wesen, das empfinden muß, es habe ir­gendeine Eigenschaft nicht, die es seiner Natur nach haben"
      ],
      [
        "sollte, schaut ein andres Wesen, das diese Eigenschaft hat.",
        "Und es kann gar nicht anders, als beständig dieses andre Wesen vor sich zu haben.",
        "Wie in der Sinnenwelt naturge­mäß das Auge Sichtbares sieht, so führt der Mangel einer Eigenschaft ein Wesen der übersinnlichen Welt stets in die Nähe eines entsprechenden andern Wesens, das die in Be­tracht kommende Vollkommenheit hat.",
        "Und der Anblick dieses Wesens wird ein immerwährender Vorwurf, der als wirkliche Kraft wirkt, so daß das Wesen, welches mit dem Fehler behaftet ist, durch den Anblick die Begierde hat, den Fehler an sich auszubessern.",
        "Es ist dies ein ganz andersarti­ges Erlebnis, als es eine Begierde im Sinnensein ist.. - Das freie Wollen wird durch solche Verhältnisse in der geisti­gen Welt nicht beeinträchtigt.",
        "Ein Wesen kann sich wehren gegen das, was ein Anblick in ihm hervorrufen will.",
        "Dann wird es allmählich erreichen, daß es aus der Nähe des vor­bildlichen Wesens hinwegkommt.",
        "Es wird jedoch die Fol­ge davon sein, daß ein solches sein Vorbild abwehrendes Wesen sich selbst in Welten versetzt, in welchen es schlech­tere Daseinsbedingungen hat, als die gewesen wären, die ihm gegeben waren in der Welt, für die es gewissermaßen vorbestimmt ist."
      ],
      [
        "Dies alles zeigt der menschlichen Seele, daß nät dem Be­treten der übersinnlichen Welten die Vorstellungswelt umgebildet werden muß.",
        "Es müssen Begriffe umgewandelt, erweitert, mit anderen verschmolzen werden, wenn man die übersinnliche Welt richtig beschreiben will. - Daher kommt es, daß Beschreibungen der übersinnlichen Welten, welche die für das Sinnensein geprägten Begriffe ohne wei­tere Veränderung gebrauchen wollen, immer etwas Unzu­treffendes haben. - Man kann sich darauf besinnen, daß es"
      ],
      [
        "aus einem richtigen menschlichen Gefühle hervorgeht, Be­griffe, die für die übersinnlichen Welten erst ihre volle Be­deutung haben, innerhalb des Sinnenseins mehr oder weni­ger sinnbildlich, oder auch als wirklich die Sache bezeich­nend, zu gebrauchen.",
        "So kann jemand das Lügnerische wirklich als häßlich empfinden."
      ],
      [
        "Gegenüber dem, wie es mit diesem Begriffe in der übersinnlichen Welt steht, ist aber ein solcher Wortgebrauch im Sinnensein doch nur ein An­klang, der sich ergibt, weil alle Welten Beziehungen zuein­ander haben, und diese Beziehungen dunkel gefühlt, unbe­wußt gedacht im Sinnensein werden.",
        "Doch muß berück­sichtigt werden, daß im Sinnensein das Lügnerische, das man als häßlich empfindet, nicht häßlich zu sein braucht in seiner äußeren Erscheinung."
      ],
      [
        "Daß man sogar die Vorstel­lungen durcheinander werfen würde, wenn man ein Häßli­ches in der sinnlichen Natur aus einem Lügnerischen erklä­ren wollte.",
        "Für die übersinnliche Welt ist es aber so, daß das Lügnerische, wenn es wahr gesehen wird, in seiner Of­fenbarung sich als häßlich aufdrängt. - Auch hier kommen wieder Täuschungen in Betracht, vor denen man sich zu hüten hat."
      ],
      [
        "Es kann der Seele in der übersinnlichen Welt ein Wesen entgegentreten, das mit Recht als böse bezeichnet werden muß, und welches doch in einem solchen Bilde sich offenbart, welches man «schön» nennt, wenn man die Vor­stellung vom «Schönen» anwendet, welche man aus dem Sinnensein mitbringt.",
        "In einem solchen Falle wird man erst richtig schauen, wenn man bis zum Innengrunde des We­sens durchdringt."
      ],
      [
        "Dann wird man erleben, wie die «schö­ne» Offenbarung eine Maske ist, die nicht dem Wesen ent­spricht; und man wird dann das, was man nach Vorstellun­gen aus dem Sinnensein als «schön» empfinden wollte, mit"
      ],
      [
        "besonderer Stärke als Häßlichkeit ansprechen.",
        "Und in dem Augenblicke, wo dies gelingt, ist das «böse» Wesen auch nicht mehr imstande, die «Schönheit» vorzutäuschen.",
        "Es muß sich für einen solchen Beschauer in seiner wahren Ge­stalt enthüllen, die ein unvollkommener Ausdruck dessen nur sein kann, was es im Innern ist.",
        "An solchen Erscheinun­gen der übersinnlichen Welt wird es besonders anschaulich, wie sich die menschlichen Vorstellungen beim Betreten die­ser Welt wandeln müssen."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "ACHTE MEDITATION",
    "paragraphs": [
      "ACHTE MEDITATION",
      "Der Meditierende versucht eine Vorstellung zu bilden von",
      "dem Schauen der wiederholten Erdenleben des Menschen",
      "Von Gefahren der Seelenwanderschaft in die übersinnlichen Welten zu sprechen, ist nicht eigentlich berechtigt, wenn diese Wanderschaft eine sachgemäße ist. Eine solche würde ihr Ziel nicht erreichen, wenn unter ihren seelischen Ver­haltungsmaßregeln etwas wäre, welches darauf hinausliefe, für den Menschen Gefahren herbeizuführen. Das Ziel ist vielmehr immer, die Seele stark zu machen, ihre Kräfte zu­sammenzuziehen, so daß der Mensch fäbig werde, die see­lischen Erlebnisse zu ertragen, die er durchmachen muß, wenn er andre Welten als das Sinnensein schauen und be­greifen will.",
      "Ein wesentlicher Unterschied der Sinnenwelt von den übersinnlichen Welten ergibt sich auch noch daraus, daß Schauen, Wahrnehmen und Begreifen bei den übersinnli­chen Welten in einem andern Verhältnisse stehen als im Sinnensein. Wer von einem Teile der Sinnenwelt hört, wird mit einem gewissen Rechte das Gefühl haben, daß er zu ei­nem völligen Begreifen doch nur durch die Anschauung, die Wahrnehmung gelangt. Eine Landschaft, ein Gemälde wird man erst verstanden glauben, wenn man sie gesehen hat. Die übersinnlichen Welten kann man vollkommen be­greifen, wenn man durch die unbefangene Urteilskraft eine sachgemäße Beschreibung entgegennimmt. Zum Begreifen und zum Erleben aller lebenfördernden, lebenbefriedigen­den Kräfte der geistigen Welten bedarf man bloß der Be­schreibungen, welche von denjenigen gegeben werden, die schauen können. Wirkliche Erkenntnisse solcher Welten",
      "gewinnen können nur diejenigen, welche außerhalb des Sinnenleibes zu beobachten in der Lage sind. Beschreibun­gen der Geisteswelt müssen zuletzt immer ausgehen von Beobachtern derselben. Was aber zum Seelenleben an Er­kenntnissen dieser Welten notwendig ist, das wird erreicht durch das Begreifen. Und es ist durchaus möglich, daß je­mand gar keinen eigenen Einblick in die übersinnlichen Welten hat, und dennoch sie und ihre Eigentümlichkeiten vollkommen versteht; sie so versteht, wie die Seele dies un­ter gewissen Verhältnissen stets mit vollem Rechte verlan­gen wird und muß.",
      "Deshalb ist auch möglich, daß jemand die Mittel seiner inneren Versenkung aus dem Schatze der Vorstellungen nimmt, welche er sich über die Geisteswelten angeeignet hat. Ein solcher Versenkungsstoff ist der allerbeste. Ist der­jenige, welcher am sichersten zum Ziele führt. Der Glaube entspricht nicht den Tatsachen, welcher nahe legt, daß es für das Aneignen des übersinnlichen Schauens hinderlich sei, vor dieser Aneignung durch Begreifen sich die Erkennt­nisse dieser Welten erworben zu haben. Es ist vielmehr das Gegenteil richtig, nämlich, daß man sicherer und leichter zum Schauen mit dem vorangegangenen Begreifen kommt als ohne dasselbe. Ob es jemand beim Begreifen läßt, oder das Schauen anstrebt, das hängt davon ab, ob der Drang nach der eigenen Beobachtung bei ihm schon aufgetreten ist, oder nicht. Ist er eingetreten, dann kann er gar nicht anders, als die Gelegenheit suchen, die Wanderschaft in die übersinnlichen Welten wirklich anzutreten. - Nach dem Verstehen dieser Welten werden aber von unseren Zeiten an immer mehr und mehr Menschen verlangen, denn eine wahre Lebensbeobachtung zeigt, daß von der Gegenwart",
      "an die Menschenseelen in einen solchen Zustand eintreten, daß sie ohne das Begreifen der übersinnlichen Welten mit dem Leben in das notwendige Verhältnis nicht kommen können.",
      "Wenn der Mensch auf der Seelenwanderschaft soweit ge­langt ist, daß er alles, was er « sich», was er seine Wesen­heit in dem Sinnensein nennt, als Erinnerung in sich trägt, und sich in einem nunmehr errungenen übergeordneten «Ich» erlebt, dann wird er fähig, auch zum Schauen des Le­bensverlaufes über das sinnliche Erdensein hinaus zu ge­langen. Vor seinen geistigen Blick tritt die Tatsache, daß diesem Sinnensein ein andres Dasein seiner selbst in der Geisteswelt vorangegangen ist.",
      "Und daß in diesem geisti­gen Sein die wahren Ursachen liegen für die Gestaltung des Sinnenseins. Man lernt die Tatsache kennen, daß man vor diesem Sinnenleben, in das man eingetreten ist, als man ei­nen sinnlichen Leib erhalten hat, schon rein geistig gelebt hat. - Wie man als Mensch jetzt ist, mit diesen oder jenen Fähigkeiten, diesen oder jenen Trieben, das sieht man vorbereitet in einem Dasein, welches man vorher in einer rein geistigen Welt verlebt hat.",
      "Man schaut sich an, als ein, sei­nem Eintritt in die Sinnenwelt vorangegangenes geistig le­bendes Wesen, das angestrebt hat, mit den Fähigkeiten und Seeleneigentümlichkeiten als Sinnenwesenzu leben, die man an sich trägt und entwickelt hat seit der Geburt. Derjenige wäre im Irrtum befangen, der etwa sagen wollte, wie sollte ich Fähigkeiten und Triebe im Geistessein angestrebt ha­ben, welche mir nun, da ich sie an mir trage, doch gar nicht gefallen.",
      "Es kommt nicht darauf an, ob der Seele im Sinnen-sein etwas gefällt oder nicht; sie hat für das Anstreben im",
      "Geistes sein ganz andre Gesichtspunkte als nachher im Sin­nensein. Die Art des Wissens und Wollens ist in beiden Welten eine durchaus verschiedene. Man weiß im Geistes-sein, daß man zu seiner Gesamtentwickelung ein Sinnesle­ben nötig hat, das der Seele dann vielleicht im Sinnensein unsympathisch oder bedrückend verläuft; und man strebt es doch an, weil man im Geistessein nicht auf das Sympa­thische und Angenehme, sondern auf dasjenige sieht, was zur rechten Entfaltung des Eigenseins notwendig ist.",
      "In ähnlicher Art verhält es sich mit den Geschicken des Lebens. Man sieht dieselben und schaut, wie man sich das Sympathische und auch das Unsympathische im Geistes-sein zubereitet hat, wie man selbst die Mittel herbeigeführt hat, die verursachen, daß man dieses oder jenes Glückliche oder auch Schmerzvolie im Sinnensein durchmacht. Auch da kann der Mensch, solange er sich bloß im Sinnensein er­lebt, es unbegreiflich finden, diese oder jene Lebenslage selbst herbeigeführt zu haben; im Geistessein hat er aber das gehabt, was man eine übersinnliche Einsicht nennen kann, dahingehend, daß er sich sagte, du mußt das Schmerz-volle oder Unsympathische durchmachen, denn nur solches Erleben bringt dich in deiner Gesamtentwickelung um eine Stufe weiter. Aus der bloßen Beurteilung aus dem Sinnen-sein heraus kann man nie erkennen, inwiefern ein Erden-leben den Menschen in seiner Gesamtentwickelung vor­wärts bringt.",
      "Nach Erkenntnis des dem sinnlichen Erdensein voran­gegangenen Geistessein ergibt sich dann das Anschauen der Gründe, warum man im Geistessein eine gewisse Art und ein gewisses Schicksal für das Sinnensein angestrebt hat. Diese Gründe führen hin zu einem früheren Erdenle­ben,",
      "das man in der Vergangenheit durchlebt hat. Je nach­dem dieses verlaufen ist, je nachdem man da gewisse Erfahrungen gemacht oder sich Fähigkeiten angeeignet hat, strebte man im darauffolgenden Geistessein darnach, man­gelhaft gemachte Erfahrungen in einem neuen Erdenleben besser zu machen, unausgebildet gebliebene Fähigkeiten auszubilden. Man empfindet im Geistessein ein Unrechtes, das man zum Beispiel einem Menschen zugefügt hat so, daß man dadurch die Weltenordnung gestört hat, und daß es notwendig ist, in einem weiteren Lebenslauf mit dem ent­sprechenden Menschen zugleich auf Erden zu sein, um in den entsprechenden Beziehungen zu ihm das Unrecht gut-zumachen. - Bei weiter fortschreitender Seelenentwicke­lung erweitert sich der Blick auf eine Reihe vorangegange­ner Erdenleben. Man gelangt auf solche Art zur beobach­tenden Erkenntnis des wahren Lebenslaufes des übergeord­neten «Ich». Man erschaut, daß der Mensch in wiederhol­ten Erdenieben sein Gesamtdasein auf der Erde durchläuft, und daß zwischen den wiederholten Erdenieben rein gei­stige Lebensläufe liegen, welche mit den Erdenleben in ge­setzmäßigem Zusammenhange stehen.",
      "Auf diese Art wird die Erkenntnis von den wiederholten Erdenleben zur wirklichen Beobachtung gebracht. (Nur um immer wieder vorkommenden Mißverständnissen vor­zubeugen, sei erwähnt, was in andern meiner Schriften ge­nauer dargestellt ist. Das Gesamtdasein des Menschen ver­läuft nicht etwa so, daß sich das Leben ewig wiederholt. Es findet eine gewisse Zahl von Wiederholungen statt, daran schließen sich vorher und nachher ganz andre Daseinsarten; und alles dieses zeigt sich in seinem Gesamtverlaufe als weisheitsvolle Entwickelung.)",
      "Die Erkenntnis, daß der Mensch in wiederholten Leben seine Entwickelung durchmacht, kann auch durch ver­nunftgemäße Beobachtung des Sinnenseins gewonnen wer­den. In meinem Buche «Theosophie», in meinem «Umriß der Geheimwissenschaft» sowie in kleineren Schriften von mir sind Beweise für die wiederholten Erdenleben und ih­ren Zusammenhang versucht worden, die in solcher Form gehalten sind, welche den wissenschaftlichen Erwägungen der gegenwärtigen naturwissenschaftlichen Entwickelungs­lehre eigen ist.",
      "Es sollte da gezeigt werden, wie ein folge-rechtes Denken und Forschen, das wirklich die naturwis­senschaftlichen Forschungen zu Ende führt, gar nicht an­ders kann, als den Entwickelungsgedanken, wie ihn die letzten Zeiten gebracht haben, für den Menschen so zu ge­stalten, daß die wahre Wesenheit, die Seelenindividualität des Menschen als etwas angesehen wird, das sich durch wiederholte Sinnenleben mit dazwischenliegenden rein geistigen Lebensläufen hindurch entwickelt. Was da als Be­weise versucht wurde, kann naturgemäß viel weiter ausge­baut, vervollkommnet werden.",
      "Aber es kann die Meinung nicht unberechtigt erscheinen, daß Beweise auf diesem Ge­biete genau denselben wissenschaftlichen Erkennmiswert haben, wie das, was man sonst naturwissenschaftliche Be­weise nennt. Es gibt nichts in der Wissenschaft des Geisti­gen, was sich nicht durch so gehaltene Beweise stützen lie­ße.",
      "Man muß ja allerdings sagen, daßdiegeisteswissenschaft­lichen Beweise ganz selbstverständlich sich viel schwerer Anerkennung verschaffen können als die naturwissenschaft­lichen. Das rührt aber nicht davon her, weil sie weniger strenge sind, sondern weil der Mensch, wenn er sie vor sich hat, den sinnlichen Tatsachenboden nicht empfindet, der",
      "ihm in der Naturwissenschaft die Zustimmung zu den Be­weisen leicht macht. Mit der Beweiskraft als solcher hat das aber gar nichts zu tun. Und wer imstande ist, unbefangen die naturwissenschaftlichen Beweise mit den in derselben Art gegebenen geisteswissenschaftlichen Beweisen zu ver­gleichen, der wird sich von dem gleichen Wert in bezug auf die Beweiskraft wohl überzeugen können. So kann zu dem, was der Beobachter der geistigen Welten aus seinem Schauen als Beschreibung über die wiederholten Erdenleben geben kann, noch hinzukommen, was durch solche Beweise dar­über zu bekräftigen ist. Das eine kann dem andern helfen, eine Überzeugung von der Wiederholung des gesamten menschlichen Lebenslaufes zu gewinnen durch bloßes Begreifen. - Hier wurde versucht, den Weg zu zeigen, wel­cher über das Begreifen hinaus zum übersinnlichen Schauen dieser Wiederholung führt."
    ],
    "sentences": [
      [
        "ACHTE MEDITATION"
      ],
      [
        "Der Meditierende versucht eine Vorstellung zu bilden von"
      ],
      [
        "dem Schauen der wiederholten Erdenleben des Menschen"
      ],
      [
        "Von Gefahren der Seelenwanderschaft in die übersinnlichen Welten zu sprechen, ist nicht eigentlich berechtigt, wenn diese Wanderschaft eine sachgemäße ist.",
        "Eine solche würde ihr Ziel nicht erreichen, wenn unter ihren seelischen Ver­haltungsmaßregeln etwas wäre, welches darauf hinausliefe, für den Menschen Gefahren herbeizuführen.",
        "Das Ziel ist vielmehr immer, die Seele stark zu machen, ihre Kräfte zu­sammenzuziehen, so daß der Mensch fäbig werde, die see­lischen Erlebnisse zu ertragen, die er durchmachen muß, wenn er andre Welten als das Sinnensein schauen und be­greifen will."
      ],
      [
        "Ein wesentlicher Unterschied der Sinnenwelt von den übersinnlichen Welten ergibt sich auch noch daraus, daß Schauen, Wahrnehmen und Begreifen bei den übersinnli­chen Welten in einem andern Verhältnisse stehen als im Sinnensein.",
        "Wer von einem Teile der Sinnenwelt hört, wird mit einem gewissen Rechte das Gefühl haben, daß er zu ei­nem völligen Begreifen doch nur durch die Anschauung, die Wahrnehmung gelangt.",
        "Eine Landschaft, ein Gemälde wird man erst verstanden glauben, wenn man sie gesehen hat.",
        "Die übersinnlichen Welten kann man vollkommen be­greifen, wenn man durch die unbefangene Urteilskraft eine sachgemäße Beschreibung entgegennimmt.",
        "Zum Begreifen und zum Erleben aller lebenfördernden, lebenbefriedigen­den Kräfte der geistigen Welten bedarf man bloß der Be­schreibungen, welche von denjenigen gegeben werden, die schauen können.",
        "Wirkliche Erkenntnisse solcher Welten"
      ],
      [
        "gewinnen können nur diejenigen, welche außerhalb des Sinnenleibes zu beobachten in der Lage sind.",
        "Beschreibun­gen der Geisteswelt müssen zuletzt immer ausgehen von Beobachtern derselben.",
        "Was aber zum Seelenleben an Er­kenntnissen dieser Welten notwendig ist, das wird erreicht durch das Begreifen.",
        "Und es ist durchaus möglich, daß je­mand gar keinen eigenen Einblick in die übersinnlichen Welten hat, und dennoch sie und ihre Eigentümlichkeiten vollkommen versteht; sie so versteht, wie die Seele dies un­ter gewissen Verhältnissen stets mit vollem Rechte verlan­gen wird und muß."
      ],
      [
        "Deshalb ist auch möglich, daß jemand die Mittel seiner inneren Versenkung aus dem Schatze der Vorstellungen nimmt, welche er sich über die Geisteswelten angeeignet hat.",
        "Ein solcher Versenkungsstoff ist der allerbeste.",
        "Ist der­jenige, welcher am sichersten zum Ziele führt.",
        "Der Glaube entspricht nicht den Tatsachen, welcher nahe legt, daß es für das Aneignen des übersinnlichen Schauens hinderlich sei, vor dieser Aneignung durch Begreifen sich die Erkennt­nisse dieser Welten erworben zu haben.",
        "Es ist vielmehr das Gegenteil richtig, nämlich, daß man sicherer und leichter zum Schauen mit dem vorangegangenen Begreifen kommt als ohne dasselbe.",
        "Ob es jemand beim Begreifen läßt, oder das Schauen anstrebt, das hängt davon ab, ob der Drang nach der eigenen Beobachtung bei ihm schon aufgetreten ist, oder nicht.",
        "Ist er eingetreten, dann kann er gar nicht anders, als die Gelegenheit suchen, die Wanderschaft in die übersinnlichen Welten wirklich anzutreten. - Nach dem Verstehen dieser Welten werden aber von unseren Zeiten an immer mehr und mehr Menschen verlangen, denn eine wahre Lebensbeobachtung zeigt, daß von der Gegenwart"
      ],
      [
        "an die Menschenseelen in einen solchen Zustand eintreten, daß sie ohne das Begreifen der übersinnlichen Welten mit dem Leben in das notwendige Verhältnis nicht kommen können."
      ],
      [
        "Wenn der Mensch auf der Seelenwanderschaft soweit ge­langt ist, daß er alles, was er « sich», was er seine Wesen­heit in dem Sinnensein nennt, als Erinnerung in sich trägt, und sich in einem nunmehr errungenen übergeordneten «Ich» erlebt, dann wird er fähig, auch zum Schauen des Le­bensverlaufes über das sinnliche Erdensein hinaus zu ge­langen.",
        "Vor seinen geistigen Blick tritt die Tatsache, daß diesem Sinnensein ein andres Dasein seiner selbst in der Geisteswelt vorangegangen ist."
      ],
      [
        "Und daß in diesem geisti­gen Sein die wahren Ursachen liegen für die Gestaltung des Sinnenseins.",
        "Man lernt die Tatsache kennen, daß man vor diesem Sinnenleben, in das man eingetreten ist, als man ei­nen sinnlichen Leib erhalten hat, schon rein geistig gelebt hat. - Wie man als Mensch jetzt ist, mit diesen oder jenen Fähigkeiten, diesen oder jenen Trieben, das sieht man vorbereitet in einem Dasein, welches man vorher in einer rein geistigen Welt verlebt hat."
      ],
      [
        "Man schaut sich an, als ein, sei­nem Eintritt in die Sinnenwelt vorangegangenes geistig le­bendes Wesen, das angestrebt hat, mit den Fähigkeiten und Seeleneigentümlichkeiten als Sinnenwesenzu leben, die man an sich trägt und entwickelt hat seit der Geburt.",
        "Derjenige wäre im Irrtum befangen, der etwa sagen wollte, wie sollte ich Fähigkeiten und Triebe im Geistessein angestrebt ha­ben, welche mir nun, da ich sie an mir trage, doch gar nicht gefallen."
      ],
      [
        "Es kommt nicht darauf an, ob der Seele im Sinnen-sein etwas gefällt oder nicht; sie hat für das Anstreben im"
      ],
      [
        "Geistes sein ganz andre Gesichtspunkte als nachher im Sin­nensein.",
        "Die Art des Wissens und Wollens ist in beiden Welten eine durchaus verschiedene.",
        "Man weiß im Geistes-sein, daß man zu seiner Gesamtentwickelung ein Sinnesle­ben nötig hat, das der Seele dann vielleicht im Sinnensein unsympathisch oder bedrückend verläuft; und man strebt es doch an, weil man im Geistessein nicht auf das Sympa­thische und Angenehme, sondern auf dasjenige sieht, was zur rechten Entfaltung des Eigenseins notwendig ist."
      ],
      [
        "In ähnlicher Art verhält es sich mit den Geschicken des Lebens.",
        "Man sieht dieselben und schaut, wie man sich das Sympathische und auch das Unsympathische im Geistes-sein zubereitet hat, wie man selbst die Mittel herbeigeführt hat, die verursachen, daß man dieses oder jenes Glückliche oder auch Schmerzvolie im Sinnensein durchmacht.",
        "Auch da kann der Mensch, solange er sich bloß im Sinnensein er­lebt, es unbegreiflich finden, diese oder jene Lebenslage selbst herbeigeführt zu haben; im Geistessein hat er aber das gehabt, was man eine übersinnliche Einsicht nennen kann, dahingehend, daß er sich sagte, du mußt das Schmerz-volle oder Unsympathische durchmachen, denn nur solches Erleben bringt dich in deiner Gesamtentwickelung um eine Stufe weiter.",
        "Aus der bloßen Beurteilung aus dem Sinnen-sein heraus kann man nie erkennen, inwiefern ein Erden-leben den Menschen in seiner Gesamtentwickelung vor­wärts bringt."
      ],
      [
        "Nach Erkenntnis des dem sinnlichen Erdensein voran­gegangenen Geistessein ergibt sich dann das Anschauen der Gründe, warum man im Geistessein eine gewisse Art und ein gewisses Schicksal für das Sinnensein angestrebt hat.",
        "Diese Gründe führen hin zu einem früheren Erdenle­ben,"
      ],
      [
        "das man in der Vergangenheit durchlebt hat.",
        "Je nach­dem dieses verlaufen ist, je nachdem man da gewisse Erfahrungen gemacht oder sich Fähigkeiten angeeignet hat, strebte man im darauffolgenden Geistessein darnach, man­gelhaft gemachte Erfahrungen in einem neuen Erdenleben besser zu machen, unausgebildet gebliebene Fähigkeiten auszubilden.",
        "Man empfindet im Geistessein ein Unrechtes, das man zum Beispiel einem Menschen zugefügt hat so, daß man dadurch die Weltenordnung gestört hat, und daß es notwendig ist, in einem weiteren Lebenslauf mit dem ent­sprechenden Menschen zugleich auf Erden zu sein, um in den entsprechenden Beziehungen zu ihm das Unrecht gut-zumachen. - Bei weiter fortschreitender Seelenentwicke­lung erweitert sich der Blick auf eine Reihe vorangegange­ner Erdenleben.",
        "Man gelangt auf solche Art zur beobach­tenden Erkenntnis des wahren Lebenslaufes des übergeord­neten «Ich».",
        "Man erschaut, daß der Mensch in wiederhol­ten Erdenieben sein Gesamtdasein auf der Erde durchläuft, und daß zwischen den wiederholten Erdenieben rein gei­stige Lebensläufe liegen, welche mit den Erdenleben in ge­setzmäßigem Zusammenhange stehen."
      ],
      [
        "Auf diese Art wird die Erkenntnis von den wiederholten Erdenleben zur wirklichen Beobachtung gebracht. (Nur um immer wieder vorkommenden Mißverständnissen vor­zubeugen, sei erwähnt, was in andern meiner Schriften ge­nauer dargestellt ist.",
        "Das Gesamtdasein des Menschen ver­läuft nicht etwa so, daß sich das Leben ewig wiederholt.",
        "Es findet eine gewisse Zahl von Wiederholungen statt, daran schließen sich vorher und nachher ganz andre Daseinsarten; und alles dieses zeigt sich in seinem Gesamtverlaufe als weisheitsvolle Entwickelung.)"
      ],
      [
        "Die Erkenntnis, daß der Mensch in wiederholten Leben seine Entwickelung durchmacht, kann auch durch ver­nunftgemäße Beobachtung des Sinnenseins gewonnen wer­den.",
        "In meinem Buche «Theosophie», in meinem «Umriß der Geheimwissenschaft» sowie in kleineren Schriften von mir sind Beweise für die wiederholten Erdenleben und ih­ren Zusammenhang versucht worden, die in solcher Form gehalten sind, welche den wissenschaftlichen Erwägungen der gegenwärtigen naturwissenschaftlichen Entwickelungs­lehre eigen ist."
      ],
      [
        "Es sollte da gezeigt werden, wie ein folge-rechtes Denken und Forschen, das wirklich die naturwis­senschaftlichen Forschungen zu Ende führt, gar nicht an­ders kann, als den Entwickelungsgedanken, wie ihn die letzten Zeiten gebracht haben, für den Menschen so zu ge­stalten, daß die wahre Wesenheit, die Seelenindividualität des Menschen als etwas angesehen wird, das sich durch wiederholte Sinnenleben mit dazwischenliegenden rein geistigen Lebensläufen hindurch entwickelt.",
        "Was da als Be­weise versucht wurde, kann naturgemäß viel weiter ausge­baut, vervollkommnet werden."
      ],
      [
        "Aber es kann die Meinung nicht unberechtigt erscheinen, daß Beweise auf diesem Ge­biete genau denselben wissenschaftlichen Erkennmiswert haben, wie das, was man sonst naturwissenschaftliche Be­weise nennt.",
        "Es gibt nichts in der Wissenschaft des Geisti­gen, was sich nicht durch so gehaltene Beweise stützen lie­ße."
      ],
      [
        "Man muß ja allerdings sagen, daßdiegeisteswissenschaft­lichen Beweise ganz selbstverständlich sich viel schwerer Anerkennung verschaffen können als die naturwissenschaft­lichen.",
        "Das rührt aber nicht davon her, weil sie weniger strenge sind, sondern weil der Mensch, wenn er sie vor sich hat, den sinnlichen Tatsachenboden nicht empfindet, der"
      ],
      [
        "ihm in der Naturwissenschaft die Zustimmung zu den Be­weisen leicht macht.",
        "Mit der Beweiskraft als solcher hat das aber gar nichts zu tun.",
        "Und wer imstande ist, unbefangen die naturwissenschaftlichen Beweise mit den in derselben Art gegebenen geisteswissenschaftlichen Beweisen zu ver­gleichen, der wird sich von dem gleichen Wert in bezug auf die Beweiskraft wohl überzeugen können.",
        "So kann zu dem, was der Beobachter der geistigen Welten aus seinem Schauen als Beschreibung über die wiederholten Erdenleben geben kann, noch hinzukommen, was durch solche Beweise dar­über zu bekräftigen ist.",
        "Das eine kann dem andern helfen, eine Überzeugung von der Wiederholung des gesamten menschlichen Lebenslaufes zu gewinnen durch bloßes Begreifen. - Hier wurde versucht, den Weg zu zeigen, wel­cher über das Begreifen hinaus zum übersinnlichen Schauen dieser Wiederholung führt."
      ]
    ]
  },
  {
    "order": 10,
    "title_de": "NACHWORT ZUR NEUAUFLAGE",
    "paragraphs": [
      "Es kann wohl schon aus den Ausführungen der zweiten dieser «Meditationen» klar sein und wird aus den folgenden mit noch größerer Deutlichkeit zu erkennen sein, daß der Seelenweg, von dem in dieser Schrift gesprochen wird, in entschiedenster Weise alles auf krankhaften oder abnor­men Leibesverhältnissen beruhende sogenannte «Hellse­hen» ablehnt. Alles Visionäre, Mediumistische, das aus solchen Verhältnissen heraus entsteht, bleibt auf diesem Seelenweg ausgeschlossen. Solche Seeleninhalte gehen aus einer Verfassung des menschlichen Innern hervor, gegen­über welcher das sinnliche Wahrnehmen und das darauf ge­stützte Denken ein höheres Gebiet darstellen. Man lebt mit diesem Wahrnehmen und diesem Denken mehr in dem über­sinnlichen Gebiet und man ist mit ihm mehr vom Leibe un­abhängig, als dies der Fall ist, wenn eine unregelmäßige Leibesorganisation der Seele einen Inhalt vorgaukelt, der aus Vorgängen entspringt, die eigentlich dem Leibe dienen sollten, und die in krankhafter Art von ihrer naturgemäßen Aufgabe abirren und zu Vorstellungen führen, die weder in einer Wahrnehmung von außen, noch in einer eigenen Betätigung des Willens ihre Grundlage haben.",
      "Unter den im gewöhnlichen Bewußtsein anwesenden Seelenverrichtungen ist es nur das Denken, das sich von der Wahrnehmung loslösen und zur selbständigen, nicht an ab­norme Leibesäußerungen bedingten Betätigung führen kann. Nicht unter diejenige Seelenverfassung herunter, tie­fer in die organischen Verrichtungen hinein geht, was hier als hellsehendes Schauen gemeint ist, sondern in Gebiete",
      "geht es hinauf, die mit dem von der Seele innerlich durch­hellten, vom Eigenwollen beherrschten Denken beginnen. Aus diesem selbstbeherrschten Denken heraus entwickelt die Seele das hier gemeinte hellseherische Schauen. Das Denken ist für das Schauen Vorbild. Was in den «Medita­tionen» als solches Schauen beschrieben wird, unterschei­det sich allerdings ganz wesentlich vom bloßen Denken. Und es führt hinein in übersinnliche Weltenerfahrungen, in welche dieses Denken nicht dringen kann. Aber das Leben, das die Seele entfaltet in diesem Schauen, darf kein anderes sein als das im Denken entwickelte. Mit derselben Bewußt­heit, mit der die Seele in einem Gedanken lebt, mit der sie von einem zum andern Gedanken übergeht, muß sie in den Schauungen, in den Erleuchtungen leben.",
      "Das Verhältnis der Seele zu diesen Schauungen ist aller­dings ein wesentlich anderes als dasjenige zu den gewöhn­lichen Gedanken. Wenn auch die seelische Beziehung einer Schauung auf die ihr entsprechende Wirklichkeit Ähnlich­keit hat mit der Beziehung einer Erinnerungsvorstellung zu der erlebten Wirklichkeit, an die sie erinnert, so ist doch ein Bedeutsames im Schauen gerade dies, daß während dessen Tätigkeit die Kraft der Erinnerung in der Seele gar nicht wirksam ist. Was man einmal vorgestellt hat, daran kann man sich erinnern, auch wenn die Vorstellung ein bloßes Phan­tasiegebilde ist. Was man in hellseherischem Schauen er­fahren hat: das ist in dem Augenblicke dem Bewußtsein entschwunden, in dem die Schauung aufhört, wenn man nicht zu der seelischen Kraft des Schauens auch noch die andere hinzuentwickelt hat, in der Seele wieder dieselben Bedingungen des Schauens herzustellen, welche zu dieser Schauung geführt haben. Man kann sich an diese Bedin­gungen",
      "erinnern und kann dadurch die Schauung wieder­holen; aber man kann sich nicht unmittelbar an die Schau­ung erinnern. Wer sich die notwendige Einsicht in diese Dinge verschafft hat, der hat gerade an dieser Einsicht ein Mittel, die Wirklichkeit, welche seiner Schauung entspricht, als solche zu erkennen.",
      "Wie man sich an eine Wahrneh­mung, an ein Erlebnis erinnern kann, mit dieser Erinne­rung aber das Erlebnis, die Wahrnehmung nicht selbst durchgemacht werden, so ist mit dem, was bei der Schau­ung für die Erinnerung verbleibt, nicht der wirkliche Inhalt dieser Schauung enthalten. Man kann daran erkennen, daß ebensowenig, wie die wirkliche Wahrnehmung eine bloße Illusion im Sinnesgebiet ist, so auch die der Schauung ent­sprechende übersinnliche Wirklichkeit dies nicht ist.",
      "Men­schen, die sich mit dem Wesen des hier gemeinten Schauens nicht genügend bekanntgemacht haben und die das dar­über Vorgebrachte nur von außen, nach ihren vorgefaßten Meinungen beurteilen, verfallen in dieser Beziehung in ei­nen Irrtum. Sie glauben, daß was im hellsichtigen Bewußt­sein auftritt, auf einem Spiel der Phantasie oder einem We­ben von Vorstellungen beruhen könne, das aus unterbe­wußten Tiefen der Seele wie unklare Erinnerungen heraufflutet.",
      "Solche Beurteiler wissen nicht, daß das wahrhaft hell­seherische Bewußtsein nur in solchen Seeleninhalten lebt, die niemals als solche in die organischen Tiefen untertau­chen können, die schon bei ihrer Entstehung dem Schick­sal widerstreben, von irgendeiner Erinnerungskraft erfaßt zu werden.",
      "Eine weitere Eigentümlichkeit des hellseherischen Le­bens ist die, daß sein Verlauf in wichtigen Kennzeichen ab­weicht von demjenigen des gewöhnlichen Seelenlebens. In",
      "diesem spielen die Übung, die Gewöhnung eine für das Men­schenleben fruchtbare Rolle. Wer wiederholt eine gewisse Betätigung ausführt, der steigert seine Fähigkeit, diese Be­tätigung in geschickter Weise auszuführen.",
      "Wie wäre Fort­schritt im Leben, in der Kunst, wie wäre irgendein Lernen überhaupt möglich, wenn nicht solcher Gewinn der mensch­lichen Geschicklichkeit durch Übung erreicht werden könnte. Ein Gleiches gilt aber nicht für die Aneignung des hellseherischen Schauens.",
      "Wer eine übersinnliche Erfah­rung gemacht hat, der ist dadurch nicht geschickter gewor­den, sie ein zweitesmal zu machen. Hat er sie einmal ge­habt, so ist dies ein Grund, daß sie von ihm fortstrebt. Sie sucht ihn gewissermaßen zu fliehen.",
      "Und er muß zu beson­deren Seelenverrichtungen seine Zuflucht nehmen, die für ein wiederholtes Erfahren seine Seele mit einer stärkeren Kraft ausstatten als diejenige war, die ihn das erstemal in den Stand gesetzt hat, die Erfahrung zu machen. Für An­fänger auf dem übersinnlichen Seelenweg liegt in dieser Tatsache oft eine Quelle schwerer Enttäuschungen.",
      "Man kann bei entsprechenden Übungen, welche in dem in die­ser Schrift angedeuteten Sinne zur Seelenverstärkung füh­ren, verhältnismäßig leicht erste übersinnliche Erfahrun­gen machen. Man ist dann erst erfreut über den gemachten Fortschritt.",
      "Allein man wird bald bemerken, daß sich die gleichen Erfahrungen nicht wiederholen. Man fühlt sich dann in der Seele dem Übersinnlichen gegenüber wie leer. Was in Betracht kommt, ist, daß man sich klar darüber sein muß: dieselben Anstrengungen, die zum erstenmal zu dem Ergebnis geführt haben, wirken nicht ein zweitesmal, son­dern stärkere, oft ganz andere. - Man muß sich eben zu der Einsicht durchringen, daß die Gesetze des übersinnlichen",
      "Erlebens in vielen Fällen andere, oft entgegengesetzte sind gegenüber den physischen. Aber man muß sich auch wie­der hüten, daraus die Schlußfolgerung zu ziehen, daß man über das übersinnliche Erleben etwas wissen könne da­durch, daß man seine Vorgänge etwa immer als eine Um­kehrung entsprechender sinnlicher denkt. Wie die Dinge im einzelnen stehen, muß eben in jedem individuellen Falle durch übersinnliche Erfahrung durchschaut werden.",
      "Ein drittes Kennzeichen des übersinnlichen Erfahrens ist dieses, daß die Schauungen kaum einen bemeßbaren Zeit­inhalt hindurch vor dem hellseherischen Bewußtsein auf­leuchten. Man kann sagen: in dem Augenblicke, in dem sie auftreten, sind sie auch schon wieder entflohen. Das be­wirkt, daß nur rasche Besinnung, rasche Einstellung der Aufmerksamkeit zum Bemerken wahrer Schauungen führ­te. Wer solche rasche Besinnung und Aufmerksamkeitsein­stellung nicht unter seinen Seelenfähigkeiten entwickelt, der mag Schauungen haben; er erlangt kein Wissen davon. Darin liegt der Grund, warum von den Menschen die über­sinnliche Welt in einem so großen Umfange verleugnet wird, als es der Fall ist. Das übersinnliche Erleben ist wirk­lich viel verbreiteter, als man gewöhnlich denkt. Der Ver­kehr des Menschen mit der geistigen Welt ist im Grunde etwas ganz Allgemein-Menschliches. Aber die Fähigkeit, mit rasch wirkender Bewußtseinskraft diesen Verkehr er­kennend zu verfolgen, muß mühsam erworben werden. Man kann sich für diese Fähigkeit im gewöhnlichen Leben geeignet machen, wenn man sich darin übt, in gewissen Lebenslagen aus raschem Überblicken dessen, was vorliegt, einen Entschluß zum Handeln zu fassen. Wer in solchen Lebenslagen sich stets an ein immer wiederkehrendes Umdrehen",
      "des Entschlusses, an ein zu nichts als Zeitverlust führendes Zaudern: « Soll ich, soll ich nicht» gewöhnt, der wird aus diesem gewöhnlichen Leben heraus sich nur in schlechter Art für die Beobachtung der geistigen Welt vorbereiten können. Wer dazu kommt, schon in diesem Leben, wenn es angebracht ist, Geistesgegenwart zu entwickeln, der wird diese in das übersinnliche Erleben hineintragen können, in dem sie ein unbedingtes Erfordernis ist. - Lägen in dem Menschen, so wie er im gewöhnlichen Leben ist, die Fähigkeiten des übersinnlichen Erlebens, er wäre für seine Aufgabe in der Sinneswelt untüchtig.",
      "Er kann in heilsamer Art zu übersinnlichen Fähigkeiten nur kommen, wenn er diese aus einem gesunden Leben in der sinnlichen Wirklich­keit heraus entwickelt. Wer durch Abkehr von diesem Le­ben, durch Sonderlings-Eigenschaften glaubt, der übersinnlichen Welt nahe zu kommen, der ist auf einem Irrwege.",
      "Wahres hellseherisches Schauen verhält sich zu den gesun­den Verrichtungen des gewöhnlichen Bewußtseins wie die­ses sich zu dem Schlafbewußtsein, dessen Inhalt in Träu­men vor die Seele tritt, verhält. Wie aber durch ein unge­sundes Schlafleben das gewöhnliche Bewußtsein gestört und untergraben wird, so kann auf der Grundlage einer le­bensfeindlichen, lebensunpraktischen Haltung in der ge­wöhnlichen Wirklichkeit kein gesundes hellseherisches Schauen sich aufbauen.",
      "Je fester der Mensch im Leben steht, je verständnisvoller er den Aufgaben des gewöhnli­chen intellektuellen, gefühlsmäßigen, moralischen und so­zialen Daseins gegenüber sich verhält, desto gesünder wird er aus einer solchen Lebensführung die Seelenfähigkeiten hervorgehen lassen können, welche ihn zum Erleben der übersinnlichen Welten bringen. - Von einem solchen gesunden",
      "hellseherischen Schauen wollen die vorangehenden « Meditationen» sprechen. Alles Krankhafte, im üblen Sin­ne Visionäre und Phantastische ist auf dem Wege nicht zu finden, den sie beschreiben und der in das Erkennen der übersinnlichen Welt mündet."
    ],
    "sentences": [
      [
        "Es kann wohl schon aus den Ausführungen der zweiten dieser «Meditationen» klar sein und wird aus den folgenden mit noch größerer Deutlichkeit zu erkennen sein, daß der Seelenweg, von dem in dieser Schrift gesprochen wird, in entschiedenster Weise alles auf krankhaften oder abnor­men Leibesverhältnissen beruhende sogenannte «Hellse­hen» ablehnt.",
        "Alles Visionäre, Mediumistische, das aus solchen Verhältnissen heraus entsteht, bleibt auf diesem Seelenweg ausgeschlossen.",
        "Solche Seeleninhalte gehen aus einer Verfassung des menschlichen Innern hervor, gegen­über welcher das sinnliche Wahrnehmen und das darauf ge­stützte Denken ein höheres Gebiet darstellen.",
        "Man lebt mit diesem Wahrnehmen und diesem Denken mehr in dem über­sinnlichen Gebiet und man ist mit ihm mehr vom Leibe un­abhängig, als dies der Fall ist, wenn eine unregelmäßige Leibesorganisation der Seele einen Inhalt vorgaukelt, der aus Vorgängen entspringt, die eigentlich dem Leibe dienen sollten, und die in krankhafter Art von ihrer naturgemäßen Aufgabe abirren und zu Vorstellungen führen, die weder in einer Wahrnehmung von außen, noch in einer eigenen Betätigung des Willens ihre Grundlage haben."
      ],
      [
        "Unter den im gewöhnlichen Bewußtsein anwesenden Seelenverrichtungen ist es nur das Denken, das sich von der Wahrnehmung loslösen und zur selbständigen, nicht an ab­norme Leibesäußerungen bedingten Betätigung führen kann.",
        "Nicht unter diejenige Seelenverfassung herunter, tie­fer in die organischen Verrichtungen hinein geht, was hier als hellsehendes Schauen gemeint ist, sondern in Gebiete"
      ],
      [
        "geht es hinauf, die mit dem von der Seele innerlich durch­hellten, vom Eigenwollen beherrschten Denken beginnen.",
        "Aus diesem selbstbeherrschten Denken heraus entwickelt die Seele das hier gemeinte hellseherische Schauen.",
        "Das Denken ist für das Schauen Vorbild.",
        "Was in den «Medita­tionen» als solches Schauen beschrieben wird, unterschei­det sich allerdings ganz wesentlich vom bloßen Denken.",
        "Und es führt hinein in übersinnliche Weltenerfahrungen, in welche dieses Denken nicht dringen kann.",
        "Aber das Leben, das die Seele entfaltet in diesem Schauen, darf kein anderes sein als das im Denken entwickelte.",
        "Mit derselben Bewußt­heit, mit der die Seele in einem Gedanken lebt, mit der sie von einem zum andern Gedanken übergeht, muß sie in den Schauungen, in den Erleuchtungen leben."
      ],
      [
        "Das Verhältnis der Seele zu diesen Schauungen ist aller­dings ein wesentlich anderes als dasjenige zu den gewöhn­lichen Gedanken.",
        "Wenn auch die seelische Beziehung einer Schauung auf die ihr entsprechende Wirklichkeit Ähnlich­keit hat mit der Beziehung einer Erinnerungsvorstellung zu der erlebten Wirklichkeit, an die sie erinnert, so ist doch ein Bedeutsames im Schauen gerade dies, daß während dessen Tätigkeit die Kraft der Erinnerung in der Seele gar nicht wirksam ist.",
        "Was man einmal vorgestellt hat, daran kann man sich erinnern, auch wenn die Vorstellung ein bloßes Phan­tasiegebilde ist.",
        "Was man in hellseherischem Schauen er­fahren hat: das ist in dem Augenblicke dem Bewußtsein entschwunden, in dem die Schauung aufhört, wenn man nicht zu der seelischen Kraft des Schauens auch noch die andere hinzuentwickelt hat, in der Seele wieder dieselben Bedingungen des Schauens herzustellen, welche zu dieser Schauung geführt haben.",
        "Man kann sich an diese Bedin­gungen"
      ],
      [
        "erinnern und kann dadurch die Schauung wieder­holen; aber man kann sich nicht unmittelbar an die Schau­ung erinnern.",
        "Wer sich die notwendige Einsicht in diese Dinge verschafft hat, der hat gerade an dieser Einsicht ein Mittel, die Wirklichkeit, welche seiner Schauung entspricht, als solche zu erkennen."
      ],
      [
        "Wie man sich an eine Wahrneh­mung, an ein Erlebnis erinnern kann, mit dieser Erinne­rung aber das Erlebnis, die Wahrnehmung nicht selbst durchgemacht werden, so ist mit dem, was bei der Schau­ung für die Erinnerung verbleibt, nicht der wirkliche Inhalt dieser Schauung enthalten.",
        "Man kann daran erkennen, daß ebensowenig, wie die wirkliche Wahrnehmung eine bloße Illusion im Sinnesgebiet ist, so auch die der Schauung ent­sprechende übersinnliche Wirklichkeit dies nicht ist."
      ],
      [
        "Men­schen, die sich mit dem Wesen des hier gemeinten Schauens nicht genügend bekanntgemacht haben und die das dar­über Vorgebrachte nur von außen, nach ihren vorgefaßten Meinungen beurteilen, verfallen in dieser Beziehung in ei­nen Irrtum.",
        "Sie glauben, daß was im hellsichtigen Bewußt­sein auftritt, auf einem Spiel der Phantasie oder einem We­ben von Vorstellungen beruhen könne, das aus unterbe­wußten Tiefen der Seele wie unklare Erinnerungen heraufflutet."
      ],
      [
        "Solche Beurteiler wissen nicht, daß das wahrhaft hell­seherische Bewußtsein nur in solchen Seeleninhalten lebt, die niemals als solche in die organischen Tiefen untertau­chen können, die schon bei ihrer Entstehung dem Schick­sal widerstreben, von irgendeiner Erinnerungskraft erfaßt zu werden."
      ],
      [
        "Eine weitere Eigentümlichkeit des hellseherischen Le­bens ist die, daß sein Verlauf in wichtigen Kennzeichen ab­weicht von demjenigen des gewöhnlichen Seelenlebens."
      ],
      [
        "diesem spielen die Übung, die Gewöhnung eine für das Men­schenleben fruchtbare Rolle.",
        "Wer wiederholt eine gewisse Betätigung ausführt, der steigert seine Fähigkeit, diese Be­tätigung in geschickter Weise auszuführen."
      ],
      [
        "Wie wäre Fort­schritt im Leben, in der Kunst, wie wäre irgendein Lernen überhaupt möglich, wenn nicht solcher Gewinn der mensch­lichen Geschicklichkeit durch Übung erreicht werden könnte.",
        "Ein Gleiches gilt aber nicht für die Aneignung des hellseherischen Schauens."
      ],
      [
        "Wer eine übersinnliche Erfah­rung gemacht hat, der ist dadurch nicht geschickter gewor­den, sie ein zweitesmal zu machen.",
        "Hat er sie einmal ge­habt, so ist dies ein Grund, daß sie von ihm fortstrebt.",
        "Sie sucht ihn gewissermaßen zu fliehen."
      ],
      [
        "Und er muß zu beson­deren Seelenverrichtungen seine Zuflucht nehmen, die für ein wiederholtes Erfahren seine Seele mit einer stärkeren Kraft ausstatten als diejenige war, die ihn das erstemal in den Stand gesetzt hat, die Erfahrung zu machen.",
        "Für An­fänger auf dem übersinnlichen Seelenweg liegt in dieser Tatsache oft eine Quelle schwerer Enttäuschungen."
      ],
      [
        "Man kann bei entsprechenden Übungen, welche in dem in die­ser Schrift angedeuteten Sinne zur Seelenverstärkung füh­ren, verhältnismäßig leicht erste übersinnliche Erfahrun­gen machen.",
        "Man ist dann erst erfreut über den gemachten Fortschritt."
      ],
      [
        "Allein man wird bald bemerken, daß sich die gleichen Erfahrungen nicht wiederholen.",
        "Man fühlt sich dann in der Seele dem Übersinnlichen gegenüber wie leer.",
        "Was in Betracht kommt, ist, daß man sich klar darüber sein muß: dieselben Anstrengungen, die zum erstenmal zu dem Ergebnis geführt haben, wirken nicht ein zweitesmal, son­dern stärkere, oft ganz andere. - Man muß sich eben zu der Einsicht durchringen, daß die Gesetze des übersinnlichen"
      ],
      [
        "Erlebens in vielen Fällen andere, oft entgegengesetzte sind gegenüber den physischen.",
        "Aber man muß sich auch wie­der hüten, daraus die Schlußfolgerung zu ziehen, daß man über das übersinnliche Erleben etwas wissen könne da­durch, daß man seine Vorgänge etwa immer als eine Um­kehrung entsprechender sinnlicher denkt.",
        "Wie die Dinge im einzelnen stehen, muß eben in jedem individuellen Falle durch übersinnliche Erfahrung durchschaut werden."
      ],
      [
        "Ein drittes Kennzeichen des übersinnlichen Erfahrens ist dieses, daß die Schauungen kaum einen bemeßbaren Zeit­inhalt hindurch vor dem hellseherischen Bewußtsein auf­leuchten.",
        "Man kann sagen: in dem Augenblicke, in dem sie auftreten, sind sie auch schon wieder entflohen.",
        "Das be­wirkt, daß nur rasche Besinnung, rasche Einstellung der Aufmerksamkeit zum Bemerken wahrer Schauungen führ­te.",
        "Wer solche rasche Besinnung und Aufmerksamkeitsein­stellung nicht unter seinen Seelenfähigkeiten entwickelt, der mag Schauungen haben; er erlangt kein Wissen davon.",
        "Darin liegt der Grund, warum von den Menschen die über­sinnliche Welt in einem so großen Umfange verleugnet wird, als es der Fall ist.",
        "Das übersinnliche Erleben ist wirk­lich viel verbreiteter, als man gewöhnlich denkt.",
        "Der Ver­kehr des Menschen mit der geistigen Welt ist im Grunde etwas ganz Allgemein-Menschliches.",
        "Aber die Fähigkeit, mit rasch wirkender Bewußtseinskraft diesen Verkehr er­kennend zu verfolgen, muß mühsam erworben werden.",
        "Man kann sich für diese Fähigkeit im gewöhnlichen Leben geeignet machen, wenn man sich darin übt, in gewissen Lebenslagen aus raschem Überblicken dessen, was vorliegt, einen Entschluß zum Handeln zu fassen.",
        "Wer in solchen Lebenslagen sich stets an ein immer wiederkehrendes Umdrehen"
      ],
      [
        "des Entschlusses, an ein zu nichts als Zeitverlust führendes Zaudern: « Soll ich, soll ich nicht» gewöhnt, der wird aus diesem gewöhnlichen Leben heraus sich nur in schlechter Art für die Beobachtung der geistigen Welt vorbereiten können.",
        "Wer dazu kommt, schon in diesem Leben, wenn es angebracht ist, Geistesgegenwart zu entwickeln, der wird diese in das übersinnliche Erleben hineintragen können, in dem sie ein unbedingtes Erfordernis ist. - Lägen in dem Menschen, so wie er im gewöhnlichen Leben ist, die Fähigkeiten des übersinnlichen Erlebens, er wäre für seine Aufgabe in der Sinneswelt untüchtig."
      ],
      [
        "Er kann in heilsamer Art zu übersinnlichen Fähigkeiten nur kommen, wenn er diese aus einem gesunden Leben in der sinnlichen Wirklich­keit heraus entwickelt.",
        "Wer durch Abkehr von diesem Le­ben, durch Sonderlings-Eigenschaften glaubt, der übersinnlichen Welt nahe zu kommen, der ist auf einem Irrwege."
      ],
      [
        "Wahres hellseherisches Schauen verhält sich zu den gesun­den Verrichtungen des gewöhnlichen Bewußtseins wie die­ses sich zu dem Schlafbewußtsein, dessen Inhalt in Träu­men vor die Seele tritt, verhält.",
        "Wie aber durch ein unge­sundes Schlafleben das gewöhnliche Bewußtsein gestört und untergraben wird, so kann auf der Grundlage einer le­bensfeindlichen, lebensunpraktischen Haltung in der ge­wöhnlichen Wirklichkeit kein gesundes hellseherisches Schauen sich aufbauen."
      ],
      [
        "Je fester der Mensch im Leben steht, je verständnisvoller er den Aufgaben des gewöhnli­chen intellektuellen, gefühlsmäßigen, moralischen und so­zialen Daseins gegenüber sich verhält, desto gesünder wird er aus einer solchen Lebensführung die Seelenfähigkeiten hervorgehen lassen können, welche ihn zum Erleben der übersinnlichen Welten bringen. - Von einem solchen gesunden"
      ],
      [
        "hellseherischen Schauen wollen die vorangehenden « Meditationen» sprechen.",
        "Alles Krankhafte, im üblen Sin­ne Visionäre und Phantastische ist auf dem Wege nicht zu finden, den sie beschreiben und der in das Erkennen der übersinnlichen Welt mündet."
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
