from tag import TagLibrary
from category import CategoryLibrary
from task import Task

def verify_features():
    print("Starting Verification...")
    
    # 1. Setup Libraries
    tag_lib = TagLibrary()
    cat_lib = CategoryLibrary()
    
    # 2. Verify Tag Creation and Uniqueness
    print("\n--- Verifying Tag Creation & Uniqueness ---")
    t1 = tag_lib.add_tag("Urgent", "Red")
    t2 = tag_lib.add_tag("Urgent", "Blue") # Should return t1
    
    assert t1.get_id() == t2.get_id(), "Tags with same name should return same object"
    assert t1.get_color() == "Red", "Tag color should not change on duplicate add (unless updated)"
    print("Tag Uniqueness: PASS")
    
    # 3. Verify Category Creation
    print("\n--- Verifying Category Creation ---")
    c1 = cat_lib.add_category("Work", "Blue")
    c2 = cat_lib.add_category("Work", "Green")
    
    assert c1.get_id() == c2.get_id(), "Categories with same name should return same object"
    print("Category Uniqueness: PASS")
    
    # 4. Integrate with Task
    print("\n--- Verifying Task Integration ---")
    task = Task("Complete Project")
    
    # Add Tags
    task.add_tag("Urgent", "Red", tag_lib)
    task.add_tag("Home", "Green", tag_lib)
    task.add_tag("Urgent", "Yellow", tag_lib) # Should not add duplicate to task list
    
    assert len(task.tag_list) == 2, f"Task should have 2 tags, got {len(task.tag_list)}"
    print("Task Add Tag: PASS")
    
    # Set Category
    task.set_category(c1)
    assert task.category.get_name() == "Work", "Task category should be set"
    print("Task Set Category: PASS")
    
    # 5. Verify Updates Reflect
    print("\n--- Verifying Updates Reflect on Task ---")
    
    # Update Tag
    tag_lib.update_tag(t1.get_id(), name="Super Urgent", color="Dark Red")
    
    # Check if task sees changes
    task_urget_tag = next(t for t in task.tag_list if t.get_id() == t1.get_id())
    assert task_urget_tag.get_name() == "Super Urgent", "Task tag name update failed"
    assert task_urget_tag.get_color() == "Dark Red", "Task tag color update failed"
    print("Tag Update Reflection: PASS")
    
    # Update Category
    cat_lib.update_category(c1.get_id(), name="Office", color="Navy")
    
    assert task.category.get_name() == "Office", "Task category name update failed"
    assert task.category.get_color() == "Navy", "Task category color update failed"
    print("Category Update Reflection: PASS")
    
    print("\nAll Verifications PASSED!")

if __name__ == "__main__":
    verify_features()
