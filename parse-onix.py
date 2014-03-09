__author__ = 'mich'


from bs4 import BeautifulStoneSoup
import requests


file = '/Users/mich/datascience-projects/onix-titelbank/titelbank/TB30_totaal_2014-03_073van073.onx/TB30_totaal_2014-03_073van073.onx'
soup = BeautifulStoneSoup(open(file, 'r'))


RecordReference = soup.find_all('RecordReference')
for eachRecordReference in RecordReference:
    print eachRecordReference


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
