from selenium import webdriver
from config import selenium_driver_path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class SplinterlandsPage:
    def __init__(self, driver):
        self.driver = driver
    def first_page_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "play_now_btn"))
        )
    def login_page_email_box(self):
        return  WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )


    def login_page_password_box(self):
        return  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))

    def login_page_submin_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"login_dialog_v2\"]/div/div/div[2]/div/div[2]/form[2]/div[3]")))
    def main_page_decs_info(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,  "//*[@id=\"bs-example-navbar-collapse-1\"]/ul[2]/li[2]/div[1]/div[2]")))

    def main_page_rating_info(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"about_player__status\"]/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/span[2]")))
    def main_page_power_info(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"power_progress\"]/div[1]/span[2]")))
    def main_page_quest_info(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "quest_title1")))
    def main_page_balance_diag(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"bs-example-navbar-collapse-1\"]/ul[2]/li[2]/div[1]")))

    def main_page_rate_info(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"dec_dialog\"]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]")))
    def main_page_new_quest_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "quest_new_btn")))
    def refresh_main_page(self, dec):
        time.sleep(dec)
        self.driver.refresh()
        time.sleep(dec)
        self.driver.refresh()
        time.sleep(dec)
        self.driver.refresh()
        time.sleep(dec)
    def balance_diag_select_wallet(self, isToPlayer=False):
        if not isToPlayer:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"dec_wallet_type\"]/option[6]")))
        else:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"dec_wallet_type\"]/option[7]")))
    def balance_diag_game_dec(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "game_balance")))

    def balance_diag_dec_box(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "dec_amount")))

    def balance_diag_transfer_out(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "transfer_out_btn")))

    def transfer_diag_active_key_box(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "active_key")))

    def transfer_diag_approve_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "approve_tx")))

    def transfer_diag_playername_box(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "playerName")))

    def menu_item_collection_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "menu_item_collection")))

    def menu_item_collection_cards_filter_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"filter-owned\"]/option[2]")))

    def menu_item_collection_combine_cards(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "btn_combine")))

    def menu_item_collection_get_cards(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-img")))
        except:
            return []

    def menu_item_collection_card_name(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page_container > div > div.details-header > div > div > div.header-bottom > div.name-container > div.name")))


    def menu_item_collection_card_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-checkbox")))

    def menu_item_collection_send_card(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "btn_send")))

    def menu_item_collection_resipient(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "recipient")))

    def menu_item_collection_send_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "btn_send_popup_send")))

    def menu_item_collection_key_box(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "active_key")))

    def menu_item_collection_approve_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "approve_tx")))
class BotExtension:
    def __init__(self, bot, driver):

        self.driver = driver
        self.bot = bot
        self.site = SplinterlandsPage(driver)

    def open_login_page(self):
        self.driver.get("https://splinterlands.com/")
        elem = self.site.first_page_button()
        time.sleep(1)
        elem.click()

    def login(self):
        time.sleep(3)
        email_box = self.site.login_page_email_box()
        password_box = self.site.login_page_password_box()
        submit_button = self.site.login_page_submin_button()

        email_box.send_keys(self.bot.game_login)
        password_box.send_keys(self.bot.p_key)

        time.sleep(2)
        submit_button.click()

    def check_data(self):
       self.site.refresh_main_page(7)
       self.bot.decs = self.site.main_page_decs_info().text
       self.bot.rating = self.site.main_page_rating_info().text
       self.bot.power = self.site.main_page_power_info().text
       self.bot.quest_name = self.site.main_page_quest_info().text
       balance_diag = self.site.main_page_balance_diag()
       balance_diag.click()
       time.sleep(2)
       self.bot.rate = self.site.main_page_rate_info().text
       time.sleep(2)
    def new_quest(self):
        self.open_login_page()
        self.login()
        self.site.refresh_main_page(7)
        try:
            button = self.site.main_page_new_quest_button()
            button.click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            time.sleep(5)
            self.close_page()
        except:
            self.close_page()
    def withdraw_decs(self, playername="arius14", isToPlayer=False):
        self.site.refresh_main_page(7)
        balance_diag = self.site.main_page_balance_diag()
        balance_diag.click()
        time.sleep(5)
        if not isToPlayer:
            select_wallet_button = self.site.balance_diag_select_wallet()
            select_wallet_button.click()
        else:
            select_wallet_button = self.site.balance_diag_select_wallet(True)
            select_wallet_button.click()
            playername_box = self.site.transfer_diag_playername_box()
            time.sleep(2)
            playername_box.send_keys(playername)

        dec_amount = self.site.balance_diag_game_dec().text.split(".")[0]
        dec_box = self.site.balance_diag_dec_box()
        if dec_amount == "0":
            return 0
        time.sleep(2)
        dec_box.send_keys(dec_amount)
        time.sleep(5)
        transfer_out_button = self.site.balance_diag_transfer_out()
        transfer_out_button.click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        active_key_box = self.site.transfer_diag_active_key_box()
        active_key_box.send_keys(self.bot.a_key)
        submit_transaction = self.site.transfer_diag_approve_btn()
        time.sleep(5)
        submit_transaction.click()
        return dec_amount

    def close_page(self):
        self.driver.close()

    def withdraw_on_wallet(self):
        try:
            self.open_login_page()
            self.login()
            decs = self.withdraw_decs()
            time.sleep(30)
            self.close_page()
            return int(decs)
        except:
            self.close_page()
            return 0

    def withdraw_to_player(self, playername, isToPlayer):
        try:
            self.open_login_page()
            self.login()
            decs = self.withdraw_decs(playername, isToPlayer)
            time.sleep(30)
            self.close_page()
            return int(decs)
        except:
            self.close_page()
            return 0

    def check(self):
        try:
            self.open_login_page()
            self.login()
            self.check_data()
            self.close_page()
        except:
            self.close_page()

    def select_cards(self, playername):
        menu_item_collection = self.site.menu_item_collection_btn()
        menu_item_collection.click()
        time.sleep(5)
        menu_item_collection_cards_filter = self.site.menu_item_collection_cards_filter_btn()
        menu_item_collection_cards_filter.click()
        time.sleep(5)
        try:
            menu_item_collection_combine_cards = self.site.menu_item_collection_combine_cards()
            menu_item_collection_combine_cards.click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            time.sleep(15)
        except:
            pass
        time.sleep(5)
        card_names = []
        cards = self.site.menu_item_collection_get_cards()
        while len(cards)!=0:
            try:
                time.sleep(5)
                cards[0].click()
                time.sleep(5)
                checkbox = self.site.menu_item_collection_card_checkbox()
                checkbox.click()
                time.sleep(5)
                card_name = self.site.menu_item_collection_card_name()
                card_names.append(str(card_name.text))
                time.sleep(4)
                send_card = self.site.menu_item_collection_send_card()
                send_card.click()
                time.sleep(5)
                recipient = self.site.menu_item_collection_resipient()
                recipient.send_keys(playername)
                time.sleep(5)
                send_button = self.site.menu_item_collection_send_button()
                send_button.click()
                time.sleep(5)
                active_key_box = self.site.menu_item_collection_key_box()
                active_key_box.send_keys(self.bot.a_key)
                submit_transaction = self.site.menu_item_collection_approve_btn()
                time.sleep(5)
                submit_transaction.click()
                time.sleep(15)
                self.driver.back()
                time.sleep(5)
                cards = self.site.menu_item_collection_get_cards()
            except:
                self.driver.get("https://splinterlands.com/?p=collection&a="+self.bot.game_login)
                time.sleep(5)
                menu_item_collection_cards_filter = self.site.menu_item_collection_cards_filter_btn()
                menu_item_collection_cards_filter.click()
                time.sleep(5)
                cards = self.site.menu_item_collection_get_cards()
        return card_names


    def send_cards_to_player(self, playername):
        self.open_login_page()
        self.login()
        self.site.refresh_main_page(7)
        cards = self.select_cards(playername)
        self.close_page()
        string = self.bot.game_login + ": "
        if len(cards) != 0:
            for card in cards:
               string+=str(card)+", "
        else:
            string+="No cards or error"
        return string



