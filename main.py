import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_details(restaurant, id):

    food = {"McDonald's":
                {"Бигмак": {"Есть": False, "Доп. Соус": False, "Доп. Халапеньо": False},
                 "Биг&Тейсти": {"Есть": False, "Без помидора": False, "Острый": False, "Доп. Халапеньо": False,
                                "Доп. Соус": False},
                 "Картоха-Картошечка": {"Есть": False, "Маленькая": False, "Стандартная": False, "Большая": False,
                                        "Кетчуп": False},
                 "Шейк бейба": {"Есть": False, "Маленький": False, "Стандартный": False, "Большой": False}},
            "Baskin-Robbins":
                {"Милкшейк": {"Есть": False, "Ванильный": False, "Волшебные леденцы": False, "Стандартный": False,
                              "Большой": False},
                 "Фриз": {"Есть": False, "Ванильный": False, "Волшебные леденцы": False, "Спрайт": False,
                          "Кока-Кола": False, "Фанта": False, "Стандартный": False, "Большой": False}},
            "SubWay":
                {"Саб Острый Итальянский с луком, сладким перцем и капустой": {"Есть": False, "Острый перчик": False,
                                                                               "Кетчуп": False, "Чипоттл": False,
                                                                               "Сладкий лук": False,
                                                                               "Медово-Горчичный": False,
                                                                               "Кисло-Сладкий": False,
                                                                               "Майонез": False},
                 "Пепси": {"Есть": False, "0.3": False, "0.4": False, "0.5": False},
                 "Спрайт или 7-вверх": {"Есть": False, "0.3": False, "0.4": False, "0.5": False},
                 "Фанта или миринда": {"Есть": False, "0.3": False, "0.4": False, "0.5": False},
                 "Сок яблочный": False},
            "KFC":
                {"Острые стрипсы": {"Есть": False, "3 штуки": False, "6 штук": False, "9 штук": False},
                 "Твистер острый": {"Есть": False, "Без помидора": False},
                 "Картоха-картошечка": {"Есть": False, "Малая": False, "Стандартная": False, "Большая": False},
                 "Соус Кисло-Сладкий Чили": False,
                 "Пепси 0.4": False,
                 "Пепси бутылка": False,
                 "Милк-Шейк": {"Есть": False, "0.3": False, "0.4": False, "0.5": False}
                 }
            }

    possible_food = food[restaurant]
    order = ""

    yesno = VkKeyboard(one_time=True)
    yesno.add_button("ДА", color=VkKeyboardColor.POSITIVE)
    yesno.add_line()
    yesno.add_button("НЕТ", color=VkKeyboardColor.NEGATIVE)

    for dish in possible_food:

        vk.method("messages.send", {"user_id": id, "random_id": 0, "message": dish, "keyboard": yesno.get_keyboard()})
        take = False

        for event in longpoll.listen():

            if event.type == VkEventType.MESSAGE_NEW and event.to_me:

                txt = event.text

                if txt == "ДА":

                    take = True
                    break

                else:

                    break

        if take:

            food[restaurant][dish]["Есть"] = True

            for addition in possible_food[dish]:

                if addition != "Есть":

                    vk.method("messages.send", {"user_id": id, "random_id": 0, "message": addition, "keyboard": yesno.get_keyboard()})

                    for event in longpoll.listen():

                        if event.type == VkEventType.MESSAGE_NEW and event.to_me:

                            txt = event.text

                            if txt == "ДА":

                                food[restaurant][dish][addition] = True

                            break

    for dish in food[restaurant]:

        if food[restaurant][dish]["Есть"]:

            order += dish + ": "

            for addition in food[restaurant][dish]:

                if addition != "Есть" and food[restaurant][dish][addition]:

                    order += addition + ", "

            order += "\n"

        else:

            continue

    return order


token = "token"

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)


keyboard = VkKeyboard(one_time=True)
keyboard.add_button("Макдак", color=VkKeyboardColor.PRIMARY)
keyboard.add_button("Баскин", color=VkKeyboardColor.PRIMARY)
keyboard.add_button("subway", color=VkKeyboardColor.PRIMARY)
keyboard.add_button("KFC", color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button("Смешанная ЕДАААААА", color=VkKeyboardColor.POSITIVE)

start = VkKeyboard(one_time=True)
start.add_button("Заказать еду", color=VkKeyboardColor.POSITIVE)

food = VkKeyboard(one_time=True)
food.add_button("Что-то новенькое", color=VkKeyboardColor.POSITIVE)
food.add_button("Не сегодня", color=VkKeyboardColor.NEGATIVE)

make_order = False
mcdonald = False
br = False
subway = False
kfc = False
get_food = False
get_text_of_order = False
get_order_for_rest = False
get_restaurant = False
ready = False
ready_for_rest = False
order = ""
restaurant = ""
go_to_function = True
go_to_cycle = False
id = None
times = 0

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        vk.method("messages.send",
                  {"user_id": event.user_id, "random_id": 0, "message": """Ваши обычные заказы: 
                  \nМакдак: милкшейк ванильный, бигмак, биг тейсти, картоха
                  \nBR: фриз-спрайт-ваниль, шейк ванильный
                  \nSubWay: Spicy Italian
                  \nKFC: ОСТРЕЕЕЕЙШИЕ СТРИПСЫ ПОСТО АГОНЬ, твистер АСТРЕЙШИЙ"""})

        vk.method("messages.send",
                  {"user_id": event.user_id, "random_id": 0, "message": "Приветствую Вас, сударь",
                   "keyboard": start.get_keyboard()})
        break


for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW or go_to_cycle:

        if event.to_me or go_to_cycle:

            if go_to_cycle:

                go_to_cycle = False

                mcdonald = False
                br = False
                subway = False
                kfc = False

                vk.method("messages.send",
                          {"user_id": id, "random_id": 0, "message": "Шо кушать соизволим??",
                           "keyboard": food.get_keyboard()})

                get_food = True

                continue

            txt = event.text
            id = event.user_id

            if txt == "Заказать еду":

                vk.method("messages.send",
                          {"user_id": event.user_id, "random_id": 0,
                           "message": "В каком ресторане соизволите отобедать??", "keyboard": keyboard.get_keyboard()})
                make_order = True

            if get_food:

                if txt == "Что-то новенькое":

                    get_text_of_order = True

                else:

                    break

            if mcdonald or br or subway or kfc:

                mcdonald = False
                br = False
                subway = False
                kfc = False

                vk.method("messages.send",
                          {"user_id": event.user_id, "random_id": 0, "message": "Шо кушать соизволим??",
                           "keyboard": food.get_keyboard()})

                get_food = True

            if make_order:

                times += 1

                if times == 2:

                    go_to_cycle = True

                make_order = False

                if txt == "Макдак":

                    mcdonald = True
                    restaurant = "McDonald's"

                elif txt == "Баскин":

                    br = True
                    restaurant = "Baskin-Robbins"

                elif txt == "subway":

                    subway = True
                    restaurant = "SubWay"

                elif txt == "KFC":

                    kfc = True
                    restaurant = "KFC"

                elif txt == "Смешанная ЕДАААААА":

                    get_text_of_order = True

                elif txt != "":

                    make_order = True
                    vk.method("messages.send",
                              {"user_id": event.user_id, "random_id": 0,
                               "message": "Боюсь, не совсем Вас понимаю, сударь", "keyboard": keyboard.get_keyboard()})

            if ready:

                go_to_function = False
                order = txt
                break

            if get_text_of_order:

                vk.method("messages.send",
                          {"user_id": event.user_id, "random_id": 0,
                           "message": "Напишите, пожалуйста заказ, мы передадим его курьеру"})

                get_food = False
                ready = True

if go_to_function:

    order = get_details(restaurant, id)

else:

    char = " : "

    if restaurant == "":

        char = ""

    order = restaurant + char + order

vk.method("messages.send",
          {"user_id": id_of_the_courier, "random_id": 0, "message": "Заказ:\n" + order})
