/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package visiontest;

public class App {

    public static void main(String[] args) {
        try {
            DetectText.detectText();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
