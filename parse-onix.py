__author__ = 'mich'
from bs4 import BeautifulSoup

onxFile = 'data/TB30_totaal_2014-03_073van073.onx'
soup = BeautifulSoup(open(onxFile, 'r'), features='lxml')

# collect unique ID's
productBlock = soup.find_all('product')
for eachProductBlock in productBlock:
    idValue = eachProductBlock.idvalue.string
    idType = eachProductBlock.productidtype.string

    # collect publishing details
    publishingSoup = BeautifulSoup(str(eachProductBlock), features='lxml')
    publishingBlock = publishingSoup.find_all('publishingdate')
    for eachPublishBlock in publishingBlock:
        publishingRole = eachPublishBlock.publishingdaterole.string
        publishingDateFormat = eachPublishBlock.dateformat.string
        publishingDate = eachPublishBlock.date.string

    # collect descriptive details










    eachProductBlock.recordreference.string
    eachProductBlock.notificationtype.string
    eachProductBlock.productidtype.string
    eachProductBlock.idvalue.string



    """




    eachProductBlock.productform.string
    eachProductBlock.editionnumber.string
    eachProductBlock.languagerole.string
    eachProductBlock.languagecode.string
    eachProductBlock.illustrated.string
    eachProductBlock.subjectschemeidentifier.string
    eachProductBlock.subjectcode.string
    eachProductBlock.texttype.string
    eachProductBlock.contentaudience.string


	eachProductBlock.productidentifier
		eachProductBlock.productidtype.string
		eachProductBlock.idvalue.string

    # Interate
    eachProductBlock.titledetail
        eachProductBlock.titleelementlevel.next
        eachProductBlock.titletext.string


    # <descriptivedetail>
    eachProductBlock.descriptivedetail
        eachProductBlock.productcomposition.string
        eachProductBlock.productform.string
        eachProductBlock.productformdetail.string

        eachProductBlock.productformfeature
            eachProductBlock.productformfeature.productformfeaturetype.string
            eachProductBlock.productformfeature.productformfeaturevalue.string

        # Conditinal based on epub
        eachProductBlock.epubtechnicalprotection.string



    eachProductBlock.supplierrole.string
    eachProductBlock.suppliername.string
    eachProductBlock.productavailability.string
    eachProductBlock.pricetype.string
    eachProductBlock.priceamount.string
    eachProductBlock.publishingrole.string
    eachProductBlock.publisheridtype.string
    eachProductBlock.idvalue.string
    eachProductBlock.publishingstatus.string
    eachProductBlock.publishingdaterole.string
    eachProductBlock.dateformat.string
    eachProductBlock.date.string

    eachProductBlock.relatedmaterial.string
    eachProductBlock.date.string

    """



    # cook new soup from a productBlock before parsing further
    productSoup = BeautifulSoup(str(eachProductBlock))
    productSoup.find('RecordReference')


soup.find_all('ProductIDType')
soup.find_all('IDValue')
soup.find_all('ProductComposition')
soup.find_all('ProductForm')
soup.find_all('TitleType')
soup.find_all('TitleElementLevel')
soup.find_all('TitleText')
soup.find_all('SequenceNumber')
soup.find_all('ContributorRole')
soup.find_all('EditionNumber')
soup.find_all('LanguageRole')
soup.find_all('TextType')
soup.find_all('ContentAudience')
soup.find_all('LanguageCode')
soup.find_all('LanguageCode')

soup.TitleText()



<Product>
    <RecordReference>9789059372009</RecordReference>
    <NotificationType>03</NotificationType>
    <RecordSourceType>01</RecordSourceType>
    <ProductIdentifier>
        <ProductIDType>03</ProductIDType>
        <IDValue>9789059372009</IDValue>
    </ProductIdentifier>
    <DescriptiveDetail>
        <ProductComposition>00</ProductComposition>
        <ProductForm>BB</ProductForm>
        <NoCollection/>
        <TitleDetail>
            <TitleType>01</TitleType>
            <TitleElement>
                <TitleElementLevel>01</TitleElementLevel>
                <TitleText>Nederland voor gevorderden</TitleText>
            </TitleElement>
        </TitleDetail>
        <Contributor>
            <SequenceNumber>1</SequenceNumber>
            <ContributorRole>A01</ContributorRole>
            <PersonName>Koning</PersonName>
            <NamesBeforeKey>D.</NamesBeforeKey>
            <KeyNames>Koning</KeyNames>
        </Contributor>
        <Contributor>
            <SequenceNumber>2</SequenceNumber>
            <ContributorRole>A01</ContributorRole>
            <PersonName>Kloos</PersonName>
            <NamesBeforeKey>M.</NamesBeforeKey>
            <KeyNames>Kloos</KeyNames>
        </Contributor>
        <EditionNumber>1</EditionNumber>
			<Language>
				<LanguageRole>01</LanguageRole>
				<LanguageCode>dut</LanguageCode>
			</Language>
			<Extent>
				<ExtentType>00</ExtentType>
				<ExtentValue>166</ExtentValue>
				<ExtentUnit>03</ExtentUnit>
			</Extent>
			<Illustrated>02</Illustrated>
			<Subject>
				<MainSubject/>
				<SubjectSchemeIdentifier>32</SubjectSchemeIdentifier>
				<SubjectCode>652</SubjectCode>
			</Subject>
		</DescriptiveDetail>
		<CollateralDetail>
			<TextContent>
				<TextType>05</TextType>
				<ContentAudience>03</ContentAudience>
				<Text>Hoe ziet Nederland er uit aan het begin van de eenentwintigste eeuw? &lt;br/&gt;Fotograaf Daniel Koning doorkruiste tussen 2005 en 2008 het land en legde zowel de bebouwde als landelijke omgeving vast in ruim 140 verrassende foto&#x92;s. &lt;br/&gt;Koning toont onze eigen woonomgeving en hij confronteert ons met de opmerkelijke tendenzen die we daarin kunnen waarnemen. &lt;br/&gt;Met het verdwijnen van de koe uit de wei, zien we hetzelfde dier steeds vaker in polyester op boerenerven. De strijd tegen graffiti leidt in een enkele gemeente tot een nieuw fenomeen: de graffiti-gedoogzone. Bedrijventerreinen schieten als paddenstoelen uit de grond, terwijl oude met leegstand kampen. Geluidswallen rukken op langs de wegen en benemen automobilisten het zicht op het landschap. De termen &#x91;verrommeling&#x92; en &#x91;horizonvervuiling&#x92; verrijken de Nederlandse taal. &lt;br/&gt;&lt;br/&gt;Daniel Koning (1940) was fotograaf van De Tijd en de Volkskrant. Hij publiceerde twaalf fotoboeken, waaronder Met ons gaat alles goed, Wij eisen geluk, Tijd van leven en Vrouwen van Nederland. &lt;br/&gt;&lt;br/&gt;</Text>
			</TextContent>
			<SupportingResource>
				<ResourceContentType>01</ResourceContentType>
				<ContentAudience>03</ContentAudience>
				<ResourceMode>03</ResourceMode>
				<ResourceVersion>
					<ResourceForm>01</ResourceForm>
					<ResourceLink>9789059372009_VRK.jpg</ResourceLink>
				</ResourceVersion>
			</SupportingResource>
			<SupportingResource>
				<ResourceContentType>02</ResourceContentType>
				<ContentAudience>03</ContentAudience>
				<ResourceMode>03</ResourceMode>
				<ResourceVersion>
					<ResourceForm>01</ResourceForm>
					<ResourceLink>9789059372009_ATK.jpg</ResourceLink>
				</ResourceVersion>
			</SupportingResource>
		</CollateralDetail>
		<PublishingDetail>
			<Publisher>
				<PublishingRole>01</PublishingRole>
				<PublisherIdentifier>
					<PublisherIDType>10</PublisherIDType>
					<IDValue>7000522</IDValue>
				</PublisherIdentifier>
			</Publisher>
			<PublishingStatus>04</PublishingStatus>
			<PublishingDate>
				<PublishingDateRole>01</PublishingDateRole>
				<DateFormat>00</DateFormat>
				<Date>20081106</Date>
			</PublishingDate>
		</PublishingDetail>
		<RelatedMaterial/>
		<ProductSupply>
			<SupplyDetail>
				<Supplier>
					<SupplierRole>00</SupplierRole>
					<SupplierName>TitelBank</SupplierName>
				</Supplier>
				<ProductAvailability>20</ProductAvailability>
				<Price>
					<PriceType>02</PriceType>
					<PriceAmount>32.5</PriceAmount>
				</Price>
			</SupplyDetail>
		</ProductSupply>
	</Product>
<product>
	<recordreference>9789492001023</recordreference>
	<notificationtype>03</notificationtype>
	<recordsourcetype>01</recordsourcetype>
	<productidentifier>
		<productidtype>03</productidtype>
		<idvalue>9789492001023</idvalue>
	</productidentifier>
	<descriptivedetail>
		<productcomposition>00</productcomposition>
		<productform>00</productform>
		<productformdetail>E101</productformdetail>
		<productformfeature>
			<productformfeaturetype>10</productformfeaturetype>
			<productformfeaturevalue>3</productformfeaturevalue>
		</productformfeature>
		<epubtechnicalprotection>02</epubtechnicalprotection>
		<nocollection/>
		<titledetail>
			<titletype>01</titletype>
			<titleelement>
				<titleelementlevel>01</titleelementlevel>
				<titletext>leerjaar: 3 - lesboek + handboek - niveau: HV - schoolcode: 330 - D</titletext>
			</titleelement>
			<titleelement>
				<titleelementlevel>02</titleelementlevel>
				<titletext>Leswijs Nederlands</titletext>
			</titleelement>
		</titledetail>
		<nocontributor/>
		<editionnumber>1</editionnumber>
		<language>
			<languagerole>01</languagerole>
			<languagecode>dut</languagecode>
		</language>
		<illustrated>01</illustrated>
		<subject>
			<mainsubject/>
			<subjectschemeidentifier>32</subjectschemeidentifier>
			<subjectcode>112</subjectcode>
		</subject>
	</descriptivedetail>
	<publishingdetail>
		<publisher>
			<publishingrole>01</publishingrole>
			<publisheridentifier>
				<publisheridtype>10</publisheridtype>
				<idvalue>7366006</idvalue>
			</publisheridentifier>
		</publisher>
	</publishingdetail>
	<relatedmaterial/>
</product>