package org.launchcode.hellospring.controllers;


import org.apache.catalina.servlet4preview.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
//@RequestMapping("Hello") Illustrated how the request mapping segments the url
public class HelloController {

    @RequestMapping(value = "")
    @ResponseBody
    public String index(HttpServletRequest request){

        String name = request.getParameter("name");

        if (name == null) {
            name = "World";
        }

        return "Hello " + name + "!";
    }

    @RequestMapping(value = "hello", method = RequestMethod.GET)
    @ResponseBody
    public String helloForm(){

        String html = "<form method='post'>" +
                "<input type='text' name='name' />" +
                "<input type='submit' value='Greet Me' />" +
                "</form>";

        return html;
    }

    @RequestMapping(value = "hello", method = RequestMethod.POST)
    @ResponseBody
    public String helloPost(HttpServletRequest request){

        String name = request.getParameter("name");

        if (name == null) {
            name = "World";
        }

        return "Hello " + name + "!";

    }

    @RequestMapping(value = "helloml", method = RequestMethod.GET)
    @ResponseBody
    public String createMessage(){

        String html = "<form method='post'>" +
                "<input type='text' name='name' />" +
                "<select name='lang'>" +
                "<option value='eng'>English</option>" +
                "<option value='fr'>French</option>" +
                "<option value='sp'>Spanish</option>" +
                "<option value='man'>Mandarin</option>" +
                "<option value='jp'>Japanese</option>" +
                "</select>" +
                "<input type='submit' value='Greet Me' />" +
                "</form>";

        return html;

    }

    @RequestMapping(value = "helloml", method = RequestMethod.POST)
    @ResponseBody
    public String createMessage(HttpServletRequest request){

        String name = request.getParameter("name");
        String lang = request.getParameter("lang");

        if (name == null) {
            name = "World";
        }

        if (lang.equals("eng")) {
            return "Hello " + name + "!";
        }
        else if (lang.equals("fr")) {
            return "Bonjour " + name + "!";
        }
        else if (lang.equals("sp")) {
            return "Hola " + name + "!";
        }
        else if (lang.equals("man")) {
            return "Ni hao " + name + "!";
        }
        else if (lang.equals("jp")) {
            return "oh hi yo " + name + "!";
        }
        else {
            return "You did not select a language.";
        }
    }

    @RequestMapping(value = "hello/{name}")
    @ResponseBody
    public String helloUrlSegment(@PathVariable String name){

        if (name == null) {
            name = "World";
        }

        return "Hello " + name + "!";
    }

    @RequestMapping(value = "goodbye")
    public String goodbye(){
        return "redirect:/";
    }
}
