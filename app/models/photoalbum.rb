class Photoalbum < ActiveRecord::Base
	belongs_to :cabin
	mount_uploader :picture, PictureUploader
end
