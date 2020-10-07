from rest_framework import permissions 

class UpdateOwnProfile(permissions.BasePermission):
  """Allow users to update their profile"""

  def has_object_permission(self, request, view, obj):
    """Check if user is trying to update own profile"""
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.id == request.user.id 


class UpdateOwnStatus(permissions.BasePermission):
  """Allows user to update only their own profile"""
  def has_object_permission(self, request, views, obj):
    """CCheck if user is trying to update own status"""
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.user_profile.id == request.user.id 