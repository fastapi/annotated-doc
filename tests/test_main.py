from annotated_doc import Doc


def test_doc_basic() -> None:
    doc = Doc("This is a test documentation.")
    assert doc.documentation == "This is a test documentation."
    assert repr(doc) == "Doc('This is a test documentation.')"
    assert hash(doc) == hash("This is a test documentation.")
    assert doc == Doc("This is a test documentation.")
    assert doc != Doc("Different documentation.")
    assert doc != "Not a Doc instance"
