class Photoalbum < ActiveRecord::Base
	belongs_to :cabin
	belongs_to :user
	mount_uploader :picture, PictureUploader
	validates :cabin, presence: true
end
