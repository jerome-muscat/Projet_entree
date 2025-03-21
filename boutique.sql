-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: Boutique
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categorie`
--

DROP TABLE IF EXISTS `categorie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorie` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorie`
--

LOCK TABLES `categorie` WRITE;
/*!40000 ALTER TABLE `categorie` DISABLE KEYS */;
INSERT INTO `categorie` VALUES (2,'roman'),(3,'cuisine'),(4,'bande dessinee'),(5,'scolaire');
/*!40000 ALTER TABLE `categorie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produit`
--

DROP TABLE IF EXISTS `produit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `description` text,
  `prix` int NOT NULL,
  `quantite` int NOT NULL,
  `id_categorie` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_categorie` (`id_categorie`),
  CONSTRAINT `produit_ibfk_1` FOREIGN KEY (`id_categorie`) REFERENCES `categorie` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produit`
--

LOCK TABLES `produit` WRITE;
/*!40000 ALTER TABLE `produit` DISABLE KEYS */;
INSERT INTO `produit` VALUES (6,'Le sang et la cendre t.1','Un royaume... Abandonné par les dieux et craint par les mortels, un autre royaume déchu se soulève, déterminé à reprendre ce qui lui est dû par la violence et la vengeance. Et alors que la menace se rapproche, Poppy est non seulement sur le point de perdre son coeur et d\'être jugée indigne par les dieux, mais aussi sa propre vie à mesure que tout ce qui constituait son univers s\'écroule inexorablement.?',10,50,2),(7,'La femme de ménage','Chaque jour, Millie fait le ménage dans la belle maison des Winchester, une riche famille new-yorkaise. Elle récupère aussi leur fille à l\'école et prépare les repas avant d\'aller se coucher dans sa chambre, au grenier. Pour la jeune femme, ce nouveau travail est une chance inespérée. L\'occasion de repartir de zéro. Mais, sous des dehors respectables, sa patronne se montre de plus en plus instable et toxique. Et puis il y a aussi cette rumeur dérangeante qui court dans le quartier : madame Winchester aurait tenté de noyer sa fille il y a quelques années. Heureusement, le gentil et séduisant monsieur Winchester est là pour rendre la situation supportable. Mais le danger se tapit parfois sous des apparences trompeuses. Et lorsque Millie découvre que la porte de sa chambre mansardée ne ferme que de l\'extérieur, il est peut-être déjà trop tard...',20,70,2),(8,'Le soleil de minuit t.1','Que deviendront Milann et Aaron au douzième coup de minuit ?20 janvier, 16h20. Quelque part en région parisienne, deux étoiles filantes entrent en collision Aaron a toujours vécu dans cette petite ville de banlieue. Il y a ses petites habitudes, ses amis, ses secrets Son monde bascule quand il y voit Milann pour la première fois, triste et seule sous la pluie, et qu\'il décide d\'aller lui parler. Milann a le coeur en miettes, elle est trempée de la tête aux pieds et pétrifiée par le froid. Pourtant, elle ne parvient pas à quitter Aaron du regard, assis à l\'arrêt de bus de l\'autre côté de la rue depuis une éternité. Ils ne se connaissent pas mais sont inéluctablement attirés l\'un par l\'autre, comme deux aimants. Leur rencontre était écrite. Le temps d\'une soirée, Milann et Aaron sont emportés par un tourbillon d\'émotions. Mais qu\'adviendra-t-il de leur histoire naissante quand sonnera le dernier coup de minuit ?',8,40,2),(9,'Là où les arbres rencontrent les étoiles','Au coeur des forêts de l\'Illinois, rien que le chant des oiseaux... Chaque matin, Joanna note, recense, balise, cartographie - s\'enfonçant chaque jour davantage dans la forêt. Loin des tourments du monde, la jeune biologiste apprécie la solitude de cette routine. Jusqu\'à ce qu\'un jour, une enfant surgisse des sous-bois et vienne bousculer cet équilibre... Perdue, pieds nus, loin de chez elle ? Ou « tombée des étoiles » ? C\'est ce que prétend Ursa, la petite fille en pyjama, laquelle a bien l\'intention de nicher chez Jo et, peut-être, réenchanter sa vie...',9,73,2),(10,'Compass : tempêtes du sud','Même un mouton noir peut avoir besoin d\'un ami...Je voulais m\'enfuir, tout simplement. Jamais je ne me serais attendue à lui tomber dans les bras Laissant derrière moi ma vie urbaine pour échapper à un mariage sans amour, j\'allai m\'installer à Havenbarrow, avec l\'intention de prendre un nouveau départ. C\'était sans compter sur l\'attraction inattendue qu\'allait exercer sur moi le mouton noir de la ville. Parfois vous vous retrouvez seul au milieu des dégâts provoqués par la tempête. « Un nouveau coup de maitre. Brittainy Cherry nous fait rire et pleurer à chaque page. Un roman à savourer. » The Bookery Review',8,86,2),(11,'Les petits Marabout : ramens & nouilles d\'Asie','Connaissez-vous ces délicieuses soupes japonaises adorées par tous les amoureux de cuisine ? Apprenez à cuisiner des ramens à la maison et tous les petits plats qui les entourent au travers de 100 recettes simples et savoureuses.',5,120,3),(12,'Pains et brioches du monde','De l\'Europe à l\'Afrique, de l\'Asie à l\'Amérique, les pains sont au coeur des traditions culinaires partout dans le monde. Focaccia, buns, naan, pita, batbout, tortillas, msemen, pain burger, brioche suisse, babka... partez à la découverte des pains et brioches du monde à travers plus de 60 recettes sélectionnées par Karima El Makhloufi, à réaliser à la maison nature ou garnie en toute simplicité.',20,110,3),(13,'Je batch cook toute l\'année - 52 menus au fil des saisons','Vous avez toujours rêvé d\'avoir votre menu prêt chaque soir de la semaine et durant toute l\'année, sans vous creuser les méninges ni passer toutes vos soirées à cuisiner ? Ce livre est LA bible du batch cooking ! Découvrez 52 semaines de menus imaginés par Sandra au fil des saisons, faciles et rapides à préparer et toujours gourmands. Choisissez celui qui vous fait envie, faites vos courses grâce à la liste fournie et réservez-vous 2 ou 3 heures le dimanche pour préparer les dîners du lundi au vendredi en suivant les recettes pas à pas. Il ne vous restera plus qu\'à les assembler et les réchauffer les soirs venus et vous régaler en famille !',26,130,3),(14,'Fait maison par cyril lignac t.1','Cyril Lignac cuisine chez lui pour toi ! Envie d\'une cuisine maison savoureuse et rapide ? En direct de sa cuisine, Cyril Lignac te propose 45 recettes salées et/ou sucrées pour mettre un peu de peps dans ton quotidien. Un risotto aux coquillettes, un poisson au four à l\'huile vierge et aux petits légumes ou encore une fabuleuse tarte aux fraises ou des petits pots de crème à la vanille... Tu vas te régaler en toute simplicité ! Un livre indispensable, ultra-pratique et sans prétention, pour égayer tes déjeuners et dîners ; des recettes gourmandes, croquantes, craquantes, à déguster en solo, à deux, en famille ou entre amis. Avec Cyril, le fait-maison c\'est ultra-facile ! Mets ton tablier et laisse-toi guider par ses précieux conseils et ses recettes ultra-réconfortantes.',13,140,3),(15,'Cuisinez bien accompagné avec ma methode mentor : mes 100 recettes pas chères pour tous les jours','Vous rêvez de cuisiner tous les jours de bons plats, pas chers, sans passer votre journée en cuisine ou au supermarché ?Découvrez Mentor, la méthode que j\'ai créée pour vous aider au quotidien à cuisiner simplement, efficacement et de façon responsable. À travers 13 principes fondamentaux et ultrasimples, je vous apprends à optimiser vos courses, à ranger efficacement votre réfrigérateur et vos placards, à vous constituer un garde-manger indispensable. Vous apprendrez également à sélectionner votre matériel de cuisine et de pâtisserie, mais aussi vos aliments - frais et de saison bien sûr !Pour bien manger tous les jours, pas besoin de recettes compliquées. Rien ne vaut les classiques de notre enfance. C\'est pourquoi j\'ai sélectionné pour vous mes 100 recettes préférées, grâce auxquelles vous pourrez vous faire plaisir, même si vous n\'êtes pas (encore) un as des fourneaux : gratin dauphinois, tomates farcies, navarin d\'agneau, risotto, moules marinières, soufflé au fromage, boeuf bourguignon, riz au lait, pain perdu... Alors, qu\'attendez-vous pour devenir le chef de votre cuisine ?',23,100,3),(16,'Le château des animaux t.1 : Miss Bengalore','Quelque part dans la France de l\'entre-deux guerres, niché au coeur d\'une ferme oubliée des hommes, le Château des animaux est dirigé d\'un sabot de fer par le président Silvio... Secondé par une milice de chiens, le taureau dictateur exploite les autres animaux, tous contraints à des travaux de peine épuisants pour le bien de la communauté... Miss Bengalore, chatte craintive qui ne cherche qu\'à protéger ses deux petits, et César, un lapin gigolo, vont s\'allier au sage et mystérieux Azélar, un rat à lunettes pour prôner la résistance à l\'injustice, la lutte contre les crocs et les griffes par la désobéissance et le rire... Premier tome d\'une série prévue en quatre volumes, Le Château des animaux revisite La Ferme des animaux de George Orwell (1945) et nous invite à une multitude de réflexions parfois très actuelles...',16,36,4),(17,'Les enfants de la résistance t.1 : premières actions','Dans un petit village de France occupé par l\'armée allemande, trois enfants refusent de se soumettre à l\'ennemi. Mais comment s\'opposer à un si puissant adversaire quand on n\'a que treize ans ?',11,76,4),(18,'Astérix t.1 - astérix le gaulois','La toute première histoire d\'Astérix, pour faire connaissance avec la troupe des irréductibles Gaulois.',10,84,4),(19,'Seuls t.1 : la disparition - édition spéciale','Il y a d\'abord Yvan, 9 ans, l\'artiste rigolo et carrément lâche. Il y a ensuite Leïla, 12 ans, la garçonne énergique et optimiste. Viennent ensuite Camille, 8 ans, la naïve généreuse et moralisatrice et Terry, 5 ans et demi, le gamin turbulent et attachant. Et puis, il y a aussi Dodji, 10 ans, l\'ours au grand coeur. Ces cinq enfants se réveillent un matin et constatent que tous les habitants de la ville ont mystérieusement disparu. Que s\'est-il passé ? Où sont leurs parents et amis ? Ils se retrouvent livrés à eux-mêmes dans une grande ville vide et vont devoir apprendre à se débrouiller... SEULS !',5,210,4),(20,'Kid Paddle t.1 : jeux de vilains','PADDLE : 1. TECHN. Manette de jeu (synonyme de joystick). 2. NOM PROPRE. Prénom : Kid. Nom du meilleur joueur de jeu vidéo du journal de Spirou. Particularités : porte toujours sa casquette verte (à l\'endroit ou à l\'envers, selon son humeur), capable d\'exploser tous les records sur tous les jeux, ennemi juré de \'Mirador\', surveillant de Citygame, salle d\'arcade où il traîne avec ses copains. 3. NOM PROPRE. Nom de la nouvelle future série vedette des Editions Dupuis.',13,220,4),(21,'Hggsp spécialité, nouveau tle.','- Le cours complet pour comprendre les enjeux et retenir l\'essentiel. - Des cartes et des schémas pour retenir efficacement. - Des rappels des acquis 1re et des quiz pour se tester. - Des méthodes pas à pas pour progresser. - Des sujets guidés et des sujets complets corrigés pour s\'entraîner. - Des conseils pratiques pour bien se préparer à l\'épreuve. + Inclus : Ton kit de survie pour le Bac avec SchoolMouv > Des fiches de révision avec des focus sur des points de cours. > Des vidéos pour mieux comprendre et s\'en souvenir à coup sûr. > Un tchat avec un prof particulier pour poser toutes les questions gratuitement pendant 7 jours.',13,34,5),(22,'Objectif bac - mes 4 épreuves du bac : stss, chimie, biologie et physiopathologie humaines, philosophie, grand oral - 1re, terminale st2s - fiches tout-en-un','Pour une révision efficace de mes 4 épreuves du Bac ! Tous les résumés de cours, pour mémoriser l\'essentiel ; Des exercices pour maîtriser les fondamentaux en Chimie et Biologie, avec leurs corrigés commentés ; Des schémas et des exemples pour bien comprendre ; Toutes les notions du programme de philosophie ; Tout ce qu\'il faut savoir pour bien préparer mon Grand Oral ; Le descriptif de chaque épreuve et des conseils pour réussir ; Un aide-mémoire des citations clés en philosophie.',13,44,5),(23,'Objectif bac - spécialité svt - terminale','Tout pour maîtriser le programme et réussir votre Bac ! Chaque chapitre, centré sur un thème du programme, vous propose : Un rappel de cours détaillé et une carte mentale , pour comprendre et mémoriser l\'essentiel. Des conseils de méthode pour réussir les deux exercices de l\'épreuve écrite. De nombreux QCM et des exercices ciblés pour un entraînement efficace. 16 sujets types de Bac, pour bien se préparer à l\'examen. Tous les corrigés détaillés et commentés. Un dépliant sur le Grand Oral : l\'épreuve expliquée, des conseils pour réussir l\'épreuve et des exemples de questions traitées dans la spécialité SVT.',13,45,5),(24,'Annales abc du bac - sujets & corrigés - physique-chimie : terminale (édition 2023)','- 30 sujets corrigés pour préparer l\'épreuve et le Grand oral. - Des fiches de révisions pour retenir l\'essentiel. - Des exercices pour contrôler ses connaissances. - Des aides pas à pas et la méthode en contexte ; + Rédigé par des enseignants ! + Annales ABC du BAC 2023 Physique-Chimie Terminale - Enseignement de spécialité ; Conforme aux programmes du Bac ; Une nouvelle formule pour préparer avec succès l\'épreuve finale du nouveau Bac ! Les épreuves du nouveau Bac expliquées. Les bonnes méthodes à acquérir pour réussir. Des rappels de cours, des QCM et des exercices pour faire le point. Des sujets pas à pas avec des corrigés expliqués. Des sujets de Bac comme à l\'examen pour s\'exercer. Un cahier spécial Grand oral.',9,37,5);
/*!40000 ALTER TABLE `produit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `utilisateur` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `mot_de_passe` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilisateur`
--

LOCK TABLES `utilisateur` WRITE;
/*!40000 ALTER TABLE `utilisateur` DISABLE KEYS */;
INSERT INTO `utilisateur` VALUES (1,'Muscat','Jerome','jerome@domain.com','e79f4992364a2e5f7d383b03ffd9aa411505964c6d259b2822b4575a41b226a6');
/*!40000 ALTER TABLE `utilisateur` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-19 23:14:23
