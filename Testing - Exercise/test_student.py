from project.student import Student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Student("Pako")

    def test_init(self):
        s = Student("Pako")
        self.assertEqual("Pako", s.name)
        self.assertEqual({}, s.courses)

    def test_init_with_course(self):
        s = Student("Pako", {"Python": ["Codene"]})
        self.assertEqual("Pako", s.name)
        self.assertEqual({"Python": ["Codene"]}, s.courses)

    def test_init_with_none(self):
        s = Student("Pako", None)
        self.assertEqual("Pako", s.name)
        self.assertEqual({}, s.courses)

    def test_enroll_duplicate_course(self):
        self.s.courses = {"Python": ["note1"]}
        res = self.s.enroll("Python", ["note2"])
        self.assertEqual(res, "Course already added. Notes have been updated.")
        self.assertEqual(["note1", "note2"], self.s.courses["Python"])

    def test_enroll_course_with_notes(self):
        res = self.s.enroll("Python", ["note1"])

        self.assertEqual(res, "Course and course notes have been added.")
        self.assertEqual(self.s.courses["Python"], ["note1"])

    def test_enroll_course_without_adding_notes(self):
        res = self.s.enroll("Python", ["note1"], "runtavgaz")

        self.assertEqual(res, "Course has been added.")
        self.assertEqual(self.s.courses["Python"], [])

    def test_enroll_course_with_adding_notes(self):
        res = self.s.enroll("Python", ["note1", "note2"], "Y")

        self.assertEqual(res, "Course and course notes have been added.")
        self.assertEqual(self.s.courses["Python"], ["note1", "note2"])

    def test_enroll_in_existing_course_with_adding_notes(self):
        self.s.enroll("Python", ["note1", "note2"], "Y")
        res = self.s.enroll("Python", ["note3"], "Y")

        self.assertEqual(res, "Course already added. Notes have been updated.")
        self.assertEqual(self.s.courses["Python"], ["note1", "note2", "note3"])

    def test_add_notes(self):
        self.s.courses = {"Python": []}
        res = self.s.add_notes("Python", "note1")

        self.assertEqual(res, "Notes have been updated")
        self.assertEqual(["note1"], self.s.courses["Python"])

    def test_add_notes_course_not_found_raise(self):
        with self.assertRaises(Exception) as ex:
            self.s.add_notes("C++", "blabla")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual(self.s.courses, {})

    def test_leave_course(self):
        self.s.courses = {"Python": []}
        res = self.s.leave_course("Python")
        self.assertEqual(res, "Course has been removed")
        self.assertEqual(self.s.courses, {})

    def test_leave_course_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.s.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
