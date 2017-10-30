import csv

from django.core.management.base import BaseCommand
from skills.models import Skill

class Command(BaseCommand):
    help = 'Import skills data from csv file'

#def add_arguments(self, parser):
#    parser.add_argument('skillsfile', type=argparse.FileType('r'))

    def insert_or_ignore(self, field):
        if field!='' and field!=' ':
            return field
        else:
            return None

    def handle(self, *args, **options):
        filename = 'tt2_skills.csv'
        self.stdout.write('it works so far!')
        c = csv.reader(open(filename, 'r'), delimiter=',', quotechar='"')

        headers = None

        for i in c:
            # i = [j.decode('latin-1') for j in i]
            if headers is None:
                headers = i
                continue
            #self.stdout.write(headers)
            l = dict(zip(headers, i))

            #self.stdout.write(l)

            s = Skill()#.objects.get_or_create(id=l['TalentID'])
            #self.stdout.write(s)
            self.stdout.write(l['TalentID'])
            s.id = l['TalentID']
            s.branch = l['Branch']
            s.slot = l['Slot']
            s.sp_req = l['SPReq']
            if l['TalentReq']!='None':
                s.skill_req = l['TalentReq']
            s.tier = l['Tier']
            s.name = l['Name']
            s.note = l['Note']
            s.max_level = l['MaxLevel']
            s.stage = l['Stage']
            s.cost_lvl0 = self.insert_or_ignore(l['C0'])
            s.cost_lvl1 = self.insert_or_ignore(l['C1'])
            s.cost_lvl2 = self.insert_or_ignore(l['C2'])
            s.cost_lvl3 = self.insert_or_ignore(l['C3'])
            s.cost_lvl4 = self.insert_or_ignore(l['C4'])
            s.cost_lvl5 = self.insert_or_ignore(l['C5'])
            s.cost_lvl6 = self.insert_or_ignore(l['C6'])
            s.cost_lvl7 = self.insert_or_ignore(l['C7'])
            s.cost_lvl8 = self.insert_or_ignore(l['C8'])
            s.cost_lvl9 = self.insert_or_ignore(l['C9'])
            s.cost_lvl10 = self.insert_or_ignore(l['C10'])
            s.cost_lvl11 = self.insert_or_ignore(l['C11'])
            s.cost_lvl12 = self.insert_or_ignore(l['C12'])
            s.cost_lvl13 = self.insert_or_ignore(l['C13'])
            s.cost_lvl14 = self.insert_or_ignore(l['C14'])
            s.cost_lvl15 = self.insert_or_ignore(l['C15'])
            s.cost_lvl16 = self.insert_or_ignore(l['C16'])
            s.cost_lvl17 = self.insert_or_ignore(l['C17'])
            s.cost_lvl18 = self.insert_or_ignore(l['C18'])
            s.cost_lvl19 = self.insert_or_ignore(l['C19'])
            s.cost_lvl20 = self.insert_or_ignore(l['C20'])
            s.bonus_effect1_text = l['BonusTypeA']
            s.bonus_effect1_lvl1 = self.insert_or_ignore(l['A1'])
            s.bonus_effect1_lvl2 = self.insert_or_ignore(l['A2'])
            s.bonus_effect1_lvl3 = self.insert_or_ignore(l['A3'])
            s.bonus_effect1_lvl4 = self.insert_or_ignore(l['A4'])
            s.bonus_effect1_lvl5 = self.insert_or_ignore(l['A5'])
            s.bonus_effect1_lvl6 = self.insert_or_ignore(l['A6'])
            s.bonus_effect1_lvl7 = self.insert_or_ignore(l['A7'])
            s.bonus_effect1_lvl8 = self.insert_or_ignore(l['A8'])
            s.bonus_effect1_lvl9 = self.insert_or_ignore(l['A9'])
            s.bonus_effect1_lvl10 = self.insert_or_ignore(l['A10'])
            s.bonus_effect1_lvl11 = self.insert_or_ignore(l['A11'])
            s.bonus_effect1_lvl12 = self.insert_or_ignore(l['A12'])
            s.bonus_effect1_lvl13 = self.insert_or_ignore(l['A13'])
            s.bonus_effect1_lvl14 = self.insert_or_ignore(l['A14'])
            s.bonus_effect1_lvl15 = self.insert_or_ignore(l['A15'])
            s.bonus_effect1_lvl16 = self.insert_or_ignore(l['A16'])
            s.bonus_effect1_lvl17 = self.insert_or_ignore(l['A17'])
            s.bonus_effect1_lvl18 = self.insert_or_ignore(l['A18'])
            s.bonus_effect1_lvl19 = self.insert_or_ignore(l['A19'])
            s.bonus_effect1_lvl20 = self.insert_or_ignore(l['A20'])
            s.bonus_effect2_text = l['BonusTypeB']
            s.bonus_effect2_lvl1 = self.insert_or_ignore(l['B1'])
            s.bonus_effect2_lvl2 = self.insert_or_ignore(l['B2'])
            s.bonus_effect2_lvl3 = self.insert_or_ignore(l['B3'])
            s.bonus_effect2_lvl4 = self.insert_or_ignore(l['B4'])
            s.bonus_effect2_lvl5 = self.insert_or_ignore(l['B5'])
            s.bonus_effect2_lvl6 = self.insert_or_ignore(l['B6'])
            s.bonus_effect2_lvl7 = self.insert_or_ignore(l['B7'])
            s.bonus_effect2_lvl8 = self.insert_or_ignore(l['B8'])
            s.bonus_effect2_lvl9 = self.insert_or_ignore(l['B9'])
            s.bonus_effect2_lvl10 = self.insert_or_ignore(l['B10'])
            s.bonus_effect2_lvl11 = self.insert_or_ignore(l['B11'])
            s.bonus_effect2_lvl12 = self.insert_or_ignore(l['B12'])
            s.bonus_effect2_lvl13 = self.insert_or_ignore(l['B13'])
            s.bonus_effect2_lvl14 = self.insert_or_ignore(l['B14'])
            s.bonus_effect2_lvl15 = self.insert_or_ignore(l['B15'])
            s.bonus_effect2_lvl16 = self.insert_or_ignore(l['B16'])
            s.bonus_effect2_lvl17 = self.insert_or_ignore(l['B17'])
            s.bonus_effect2_lvl18 = self.insert_or_ignore(l['B18'])
            s.bonus_effect2_lvl19 = self.insert_or_ignore(l['B19'])
            s.bonus_effect2_lvl20 = self.insert_or_ignore(l['B20'])
            s.save()
