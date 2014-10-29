class Post < ActiveRecord::Base
  belongs_to :cabin
  belongs_to :parent
end
