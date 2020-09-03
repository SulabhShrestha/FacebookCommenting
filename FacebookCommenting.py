from selenium import webdriver 
import time

with open('secret.txt') as file:
    secret_txt = file.read()
    secret_txt.replace('\n', '')

website = webdriver.Firefox()

website.get('https://m.facebook.com')

#Logging into facebook
email_box = website.find_element_by_id('m_login_email')
password_box = website.find_element_by_xpath("//input[@name='pass']")

email_box.send_keys("sulabh.shrestha.50")
password_box.send_keys(secret_txt)
website.find_element_by_name('login').click()

time.sleep(2)

website.find_element_by_xpath("//span[contains(text(), 'Not Now')]//parent::a//parent::div").click()

#post on i wan to comment
website.get('https://m.facebook.com/story.php?story_fbid=368605597638691&id=100034677609807&refid=17&ref=104&_ft_=mf_story_key.368605597638691%3Atop_level_post_id.368605597638691%3Atl_objid.368605597638691%3Acontent_owner_id_new.100034677609807%3Aoriginal_content_id.1214375595592465%3Aoriginal_content_owner_id.702924290070934%3Athrowback_story_fbid.368605597638691%3Apage_id.702924290070934%3Aphoto_id.351379572916941%3Astory_location.4%3Aattached_story_attachment_style.video_inline%3Atds_flgs.3%3Apage_insights.%7B%22702924290070934%22%3A%7B%22page_id%22%3A702924290070934%2C%22page_id_type%22%3A%22page%22%2C%22actor_id%22%3A100034677609807%2C%22attached_story%22%3A%7B%22page_id%22%3A702924290070934%2C%22page_id_type%22%3A%22page%22%2C%22actor_id%22%3A702924290070934%2C%22dm%22%3A%7B%22isShare%22%3A0%2C%22originalPostOwnerID%22%3A0%7D%2C%22psn%22%3A%22EntStatusCreationStory%22%2C%22post_context%22%3A%7B%22object_fbtype%22%3A266%2C%22publish_time%22%3A1598001276%2C%22story_name%22%3A%22EntStatusCreationStory%22%2C%22story_fbid%22%3A%5B1214375595592465%5D%7D%2C%22role%22%3A1%2C%22sl%22%3A4%7D%2C%22dm%22%3A%7B%22isShare%22%3A0%2C%22originalPostOwnerID%22%3A0%7D%2C%22psn%22%3A%22EntStatusCreationStory%22%2C%22role%22%3A1%2C%22sl%22%3A4%2C%22targets%22%3A%5B%7B%22actor_id%22%3A100034677609807%2C%22page_id%22%3A702924290070934%2C%22post_id%22%3A1214375595592465%2C%22role%22%3A1%2C%22share_id%22%3A0%7D%5D%7D%7D%3Athid.100034677609807%3A306061129499414%3A2%3A0%3A1601535599%3A-665690229197354770&__tn__=%2AW-R')

#actually we cannot comment same text more than 5 or some times.
for i in range(1, 21):
    website.implicitly_wait(7)
    #had to search for id and xpath or any, after refreshing page.
    #otherwise, stale error is produce
    comment_box = website.find_element_by_id('composerInput')
    comment_btn =  website.find_element_by_xpath("//textarea[@id='composerInput']//following::input")
    
    comment_box.send_keys("My facebook BOT is tried of seeing this. Please remove. Comment will be flood every 10 sec.. GOOD LUCK...")
    comment_btn.click()
    

