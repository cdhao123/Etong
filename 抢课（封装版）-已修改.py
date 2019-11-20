import requests,time
from bs4 import BeautifulSoup
#获取token
url_gettoken = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/student/register.do?number=2193612793'
headers_1 = {
    'Cookie':'_WEU=sU6HVMXpyHUw5Bfe75mbHS3FqsgsD9pajotM3x6YUpX8VOnG_Pd_Ej..; AUTHTGC="h4JamO9fpZGIhd9U9um08/AtJmZEjMYjTvieCHSN++FQqUVHLyUmyQ=="; MOD_AMP_AUTH=MOD_AMP_5969429b-fa9a-4142-aa65-5fc435e938d5; JSESSIONID=ufx-3hcnHGXk1syzmQ3aFJzg4W2e-MY7Bxky9cD3Ocid2D74q9dB!-1064408887'
}
res = requests.get(url_gettoken,headers = headers_1).json()
token = res['data']['token']
headers = {
    'Cookie':'_WEU=sU6HVMXpyHUw5Bfe75mbHS3FqsgsD9pajotM3x6YUpX8VOnG_Pd_Ej..; AUTHTGC="h4JamO9fpZGIhd9U9um08/AtJmZEjMYjTvieCHSN++FQqUVHLyUmyQ=="; MOD_AMP_AUTH=MOD_AMP_5969429b-fa9a-4142-aa65-5fc435e938d5; JSESSIONID=ufx-3hcnHGXk1syzmQ3aFJzg4W2e-MY7Bxky9cD3Ocid2D74q9dB!-1064408887',
    'token':token
}

#获取课程信息列表
def get_course_list(headers):
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/programCourse.do'
    data = {
        'querySetting': '{"data":{"studentCode":"2193612793","campus":"1","electiveBatchCode":"1a10492bc4054f61a95d4e0be1aa0a15","isMajor":"1","teachingClassType":"FAWKC","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"0","order":""}'
    }
    res = requests.post(url,headers = headers,data=data).json()
    courses_list = res['dataList']
    course_list =['']
    count = 1
    for course in courses_list:
        courses = course['tcList']
        for course in courses:
            print(str(count)+'.  ',end = '  ')
            count += 1
            course_list.append(course['teachingClassID'])
            print(course['teacherName'],end = '  ')
            print(course['teachingClassID'],end = '  ')
            print(course['teachingPlace'])
            conflict = course['conflictDesc']
            if conflict:
                print(course['conflictDesc'])
            else:
                print('不冲突')
            print('课程容量'+course['classCapacity'],end = '  ')
            print('已选人数'+course['numberOfSelected'],end = '  ')
            print('剩余名额'+str(int(course['classCapacity'])-int(course['numberOfSelected'])))
            print('-------------------------------------')
    return course_list

#获得可选课程列表
def get_available_course_list(headers):
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/programCourse.do'
    data = {
        'querySetting': '{"data":{"studentCode":"2193612793","campus":"1","electiveBatchCode":"1a10492bc4054f61a95d4e0be1aa0a15","isMajor":"1","teachingClassType":"FAWKC","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"0","order":""}'
    }
    res = requests.post(url,headers = headers,data=data).json()
    courses_list = res['dataList']
    course_list =['']
    count = 1
    for course in courses_list:
        courses = course['tcList']
        for course in courses:
            conflict = course['conflictDesc']
            if conflict or int(course['classCapacity'])-int(course['numberOfSelected']) < 0:
                continue
            else:
                pass
            print(str(count)+'.  ',end = '  ')
            count += 1
            course_list.append(course['teachingClassID'])
            print(course['teacherName'],end = '  ')
            print(course['teachingClassID'],end = '  ')
            print(course['teachingPlace'])
            if conflict:
                print(course['conflictDesc'])
            else:
                print('不冲突')
            print('课程容量'+course['classCapacity'],end = '  ')
            print('已选人数'+course['numberOfSelected'],end = '  ')
            print('剩余名额'+str(int(course['classCapacity'])-int(course['numberOfSelected'])))
            print('-------------------------------------')
    return course_list

#选课
def select_course(ID,course_list,headers):
    teachingClassId = course_list[ID]
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/volunteer.do'
    param = {
        'addParam': '{"data":{"operationType":"1","studentCode":"2193612793","electiveBatchCode":"1a10492bc4054f61a95d4e0be1aa0a15","teachingClassId":'+teachingClassId+',"isMajor":"1","campus":"1","teachingClassType":"FAWKC"}}'
    }
    res = requests.post(url,headers = headers,params=param)
    print('')
    print(res.json()['msg'])
    print('')
    time.sleep(1)

#退课
def delete_course(ID,my_courses_list,headers):
    teachingClassId = my_courses_list[ID]
    timestamp = str(int(time.time()))
    param = {
        'deleteParam': '{"data":{"operationType":"2","studentCode":"2193612793","electiveBatchCode":"1a10492bc4054f61a95d4e0be1aa0a15","teachingClassId":'+teachingClassId+',"isMajor":"1","campus":"1","teachingClassType":"FAWKC"}}',
        'timestamp':timestamp
    }
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/deleteVolunteer.do'
    res = requests.get(url,headers = headers,params = param)
    print('')
    print(res.json()['msg'])
    print('')


#查看课表
def show_my_courses(headers):
    timestamp = str(int(time.time()))
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/courseResult.do?timestamp='+timestamp+'&studentCode=2193612793&electiveBatchCode=1a10492bc4054f61a95d4e0be1aa0a15'
    my_courses = requests.get(url,headers = headers).json()
    my_courses = my_courses['dataList']
    print('课程列表')
    my_courses_list = ['']
    count = 1
    for course in my_courses:
        print(str(count)+'.',end = '  ')
        count += 1
        print(course['courseName'],end = '  ')
        print(course['teacherName'],end = '  ')
        print(course['teachingClassID'])
        my_courses_list.append(course['teachingClassID'])
        print('')
    return my_courses_list

key = input('输入1查看所有课程，输入2查看可选课程：')
if key == '1':
    course_list = get_course_list(headers)
else:
    course_list = get_available_course_list(headers)
ID = int(input('请输入你要选择的课程编号：'))
select_course(ID,course_list,headers)
my_courses_list = show_my_courses(headers)
ID = int(input('请输入要退选的课程序号'))
delete_course(ID,my_courses_list,headers)


